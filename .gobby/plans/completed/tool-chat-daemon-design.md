# Daemon `tool_chat` feature — implementation design (file-anchored)

> ## SHIPPED (2026-06-29) — gcode-direct. Supersedes the gobby-index / before_tool-rule / session-marker design in the rest of this file.
>
> **Final architecture (task #997 / daemon #17393 + #17448, branch `0.5.0`):** Lane B spawn
> providers (codex / droid / grok / qwen) each run the **`gcode` CLI directly inside their own OS
> sandbox** — `gcode <read subcommand> --project <path>` via the agent's shell. No `gobby-index`
> internal MCP server, no codex on-PATH shim, no `before_tool` read-only rule, no session/marker.
> All of that compensating machinery was removed; it existed only to serve a **false premise
> (now deleted from memory `ee774216`): that droid/grok/qwen have no OS sandbox.** They all do.
>
> **Read-only is enforced by:** the provider sandbox + the shared `compose_gcode_direct_prompt`
> ("run gcode … read-only, do NOT modify anything") + the bounded, recoverable blast radius of
> gcode's worst-case mutating subcommands (`index`/`invalidate`/`graph rebuild`/`prune` — index
> churn only; never source / `project.json` / `config_store` / hub schema). `tool_policy.allow_mutation=false`.
>
> **Dispatch** stays purely on `AIAdapterStyle`: codex→DAEMON, droid→CLI, grok/qwen→ACP (the
> `ACPSpawnToolChatAdapter` composite dispatches grok vs qwen). All three styles plus LLM_PROVIDER
> are in `_TOOL_CHAT_EXECUTABLE_STYLES`. `/api/llm/status` shows every binding `supports_tools=true`.
>
> **Provider-specific exec requirements (learned from the live round-trip):**
> - `~/.gobby/bin/gcode` must be on each adapter's sandbox PATH — routed through
>   `spawn_cache_policy.merge_spawn_path` for all four (daemon commit `0e9b1899`).
> - **droid** needs `exec --auto high` (default autonomy blocks the `Execute` tool; high permits
>   non-destructive exec, destructive still blocked without `--skip-permissions-unsafe`).
> - **grok** enforces `--max-turns` and exits 1 on "max turns reached" (codex ignores it).
> - **qwen** (LM Studio backend) emits Claude-Code-style stream-json: tool_use blocks nest under
>   `message.content`, so `parse_qwen_stream` reads there (daemon commit `734ddeda`, with droid `--auto high`).
>
> **Live proof matrix** (`POST /api/llm/chat/completions`, provider-pinned, against the gobby-cli
> index): codex(daemon)=23, droid(cli)=31, grok(acp)=20, qwen(acp)=4 tool calls; all
> `stop_reason=completed` with grounded `file:line` narratives; gobby-cli HEAD byte-identical after
> the runs (mutation denied). Daemon commits: `f9afd6658`, `ec9770603`, `0e9b1899`, `734ddeda`.
>
> Everything below is the **historical** Phase-2 design (gobby-index MCP + rule + session marker)
> and is retained for trace only — it does NOT reflect the shipped code.

Synthesized from a full read of the daemon repo `/Users/josh/Projects/gobby` at HEAD
`01a868aaf`. Companion to `goal-973-lane-b-provider-agnostic-agentic.md` (the approved
architecture). This file adds concrete file:line anchors + the build sequence. Daemon
commits use `[gobby-#17393]`; tests run under `GOBBY_TEST_PROTECT=1` pytest.

## Pattern source — one-shot `text_generate` (the thing to MIRROR)

- contracts `src/gobby/ai/_text_generation_contracts.py`:
  - `TextGenerationRequest` (16–30): prompt/provider/profile/candidates/system_prompt/model/
    max_tokens/reasoning_effort/caller/cwd/timeouts.
  - `TextGenerateAdapter` Protocol (33–37): `async def generate(request) -> str | LLMTextResult`.
- service `src/gobby/ai/_text_generation_service.py`:
  - `TextGenerationService.generate_result(request)` → `_try_generate_result_candidates` (393–484)
    iterates candidates; per candidate `_select_binding` (630–638) → `registry.select(
    AICapability.TEXT_GENERATE, provider, model)`; `_adapter_for_provider(binding.provider)`
    (641–652) → factory map; `_candidate_requests` (540–568) reads `DEFAULT_PROFILE_CANDIDATES`.
  - **DIVERGENCE (goal mandate):** text_generate dispatches on `binding.provider`.
    `tool_chat` MUST dispatch on `binding.adapter_style`. Factory map keyed by `AIAdapterStyle`,
    NOT provider. Zero provider names in service/route/call-site.
- builder `src/gobby/ai/_text_generation_builder.py`:
  - `build_daemon_text_generation_service(config, *, registry=None)` (12–25).
  - `_daemon_text_generation_adapter_factories(config)` (28–51): provider-keyed
    (claude/codex/agy/grok/qwen/droid/`local:{endpoint}`).
- adapters `src/gobby/ai/_text_generation_adapters.py`: ClaudeTextGenerateAdapter (89–114, wraps
  `ClaudeLLMProvider`), LocalTextGenerateAdapter (117–142, wraps `LocalLLMProvider`), Codex/Agy/
  Droid/Grok/Qwen CLI adapters.
- route template `generate_text` (`src/gobby/servers/routes/llm.py` 204–247): pulls
  `server.services.text_generation_service`, builds `TextGenerationRequest`, returns text + capability.
- `LLMTextResult` (`src/gobby/llm/base.py` 11–19): text/usage/provider/model/profile/applied_reasoning_effort.

## Capability registry

- `src/gobby/ai/registry.py`:
  - `AICapability` StrEnum (33–42): EMBED, AUDIO_TRANSCRIBE, AUDIO_TRANSLATE, VISION_EXTRACT,
    TEXT_GENERATE, AGENT_SPAWN, WEB_CHAT → **ADD `TOOL_CHAT = "tool_chat"`**.
  - `AIAdapterStyle` (48–57): ACP, CLI, DAEMON, LLM_PROVIDER, LOCAL, OPENAI_COMPATIBLE, UNAVAILABLE.
  - `CapabilityBinding` (131–281): capability/provider/`adapter_style`/models/strict_models/metadata/
    availability; `to_dict()` includes `adapter_style.value`; `supports_model`, `available`.
  - `AICapabilityRegistry` (321–463): `select(capability,*,provider,model)`, `bindings_for`,
    `binding`, `register`, `status`, `statuses`, `status_snapshot`.
  - `CapabilityUnavailableError` (60–80).
- `src/gobby/ai/registry_builder.py`:
  - `_text_generate_adapter_style(provider)` (451–458): claude→LLM_PROVIDER, codex→DAEMON,
    {agy,droid,grok,qwen}→CLI. **ADD `_tool_chat_adapter_style`** (same families; local endpoints
    lm-studio/ollama → OPENAI_COMPATIBLE).
  - `_text_generate_binding` (294–325): builds binding + attaches adapter_style. **ADD
    `_tool_chat_binding`** with tool-capability filter.
  - `_local_text_generate_endpoint_bindings` (328–354): local endpoints → OPENAI_COMPATIBLE
    bindings. **ADD parallel** for TOOL_CHAT.
  - `build_daemon_ai_capability_registry` (35–91): add TOOL_CHAT bindings beside TEXT_GENERATE.
- profiles `src/gobby/config/feature_base.py`: `FeatureProfile` LOW/MID/HIGH = feature_low/mid/high.
  `DEFAULT_PROFILE_CANDIDATES`: LOW=claude/haiku,codex/gpt-5.4-mini; MID=claude/sonnet,codex/gpt-5.5;
  HIGH=codex/gpt-5.5(xhigh),claude/opus(high). **No `supports_tools` metadata today** → add per-binding
  tool-capability flag the filter reads; surface exclusion in `/api/llm/status`.

## Adapter targets

### Family B — claude (`llm_provider`)  [Phase 1]
- `src/gobby/llm/claude.py`: `ClaudeLLMProvider.generate_agentic` (583–689) — Agent SDK `query` loop;
  `ClaudeAgentOptions(system_prompt, max_turns, model, allowed_tools, permission_mode=
  "bypassPermissions", setting_sources=[], cli_path, cwd, **reasoning_options)`; returns
  `AgenticGenerationResult(text, model, tool_use_count, turns, tools, usage, applied_reasoning_effort)`
  (121–135). Helpers `_strip_leading_preamble` (138–152), `_is_max_turns_error` (223–231),
  `_normalize_claude_usage` (54–117).
- GENERALIZE: take the caller's tool policy → (a) build an in-process MCP server via
  `create_sdk_mcp_server`/`tool` exposing the whitelisted gcode/gwiki read commands; (b)
  `disallowed_tools=[Bash,Write,Edit,MultiEdit,NotebookEdit,Task,Agent]` so the agent uses ONLY the
  constrained tools (read-only enforced). DELETE the Bash + code-index-skill-injection approach.

### Family A — `openai_compatible`/`local` (lm-studio, ollama)  [Phase 1]
- `src/gobby/llm/local.py` `LocalLLMProvider` (43–192, NO `generate_agentic`); `local_provider_adapters.py`
  `OpenAICompatibleLocalProviderAdapter` (209–358). `.client` = `AsyncOpenAI(base_url, api_key)`;
  `generate_text_result` (237–266) sends NO `tools`/`tool_choice` (single turn).
- BUILD a daemon-side OpenAI tool loop: pass `tools` (from registry schema) + `tool_choice="auto"`;
  read `response.choices[0].message.tool_calls`; execute each via the registry dispatcher (whitelisted
  command in cwd=project_path, byte-cap, timeout); append `role:"tool"` results; repeat until no
  tool_calls or limits hit. Mirror gcore `ToolLoopLimits` (8 turns/24 calls/16KB/180s).

### Family B — codex(`daemon`/app-server), `cli`(droid/qwen/grok/agy), `acp`  [Phase 2]
- AGENT_SPAWN seam: `spawn_agent` (`dispatch/spawn.py` 69–255) → `spawn_agent_impl`
  (`mcp_proxy/tools/spawn_agent/_implementation.py` 153–908) → `TmuxSpawner.spawn_agent`
  (`agents/tmux/spawner.py` 221–308) → `build_cli_command` (`agents/spawners/command_builder.py`
  12–180; codex `--ask-for-approval never exec -C <dir>` + sandbox_args, droid `exec --input-format
  stream-json --cwd`, claude `--disallowedTools`).
- **GAP:** spawn returns run_id + tmux metadata, NOT final text; output captured async via transcript
  parsers (`CodexTranscriptParser.extract_last_messages`). Phase 2 needs a synchronous spawn→wait→
  extract-final path (goal cites codex `exec --output-last-message <path>` — verify flag). DEFER.

## Tool registry / policy (Shared, foundational — build FIRST)

- `ToolPolicy`: `cli` ("gcode"|"gwiki"), `tools: tuple[str,...]` (whitelisted subcommands),
  `allow_mutation: bool`, optional per-tool arg schema. Core hardcodes NO tool set / NO prompt /
  NO global read-only — the CALLER declares them.
- Read whitelist — gcode: search, search-symbol, search-text, search-content, grep, outline, symbol,
  symbols, symbol-at, repo-outline, tree, kinds, callers, usages, imports, path, blast-radius. gwiki:
  search, read, backlinks, sources, status, trust, audit, lint.
- Mutators rejected unless `allow_mutation` — gcode: index, invalidate, prune, graph *, vector *,
  setup, init, codewiki. gwiki: index, collect, ingest-*, compile, export, graph, remove-source.
- Registry produces: (a) OpenAI `tools[]` schema (Family A); (b) claude SDK in-process MCP server
  (Family B claude); (c) `dispatch(name, args) -> str`: run `<cli> <subcommand> <args>` in
  cwd=project_path; reject mutators + shell metachars; timeout; byte-cap.

## New `tool_chat` files (mirror `_text_generation_*`)

- `_tool_chat_contracts.py`: `ToolChatRequest` (messages|system_prompt+prompt, profile, candidates,
  provider?, model?, max_turns, max_tokens, reasoning_effort, `tool_policy`, project_path, caller,
  timeouts), `ToolChatResult` (text, model, provider, usage, tool_use_count, turns, tools,
  applied_reasoning_effort, `adapter_style`/route), `ToolChatAdapter` Protocol
  (`async chat(request, binding, tool_runtime) -> ToolChatResult`).
- `_tool_chat_service.py`: `ToolChatService.chat_result(request)` — resolve candidates
  (profile→DEFAULT_PROFILE_CANDIDATES, tool-capable filter), `registry.select(AICapability.TOOL_CHAT)`,
  dispatch on `binding.adapter_style` via `_adapter_for_style`, run adapter with the request's tool
  policy + prompt. NO provider names; NO fallback to another provider / text_generate / skeleton →
  raise `CapabilityUnavailableError`.
- `_tool_chat_builder.py`: `build_daemon_tool_chat_service(config, *, registry=None)`,
  `_daemon_tool_chat_adapter_factories(config)` keyed by `AIAdapterStyle`: OPENAI_COMPATIBLE/LOCAL→
  Family A loop adapter, LLM_PROVIDER→claude Family B adapter. (Phase 2: DAEMON/CLI/ACP→spawn adapter.)
- `_tool_chat_adapters.py`: the two Phase-1 adapters (Family A loop; Family B claude).
- route `chat_completions` (llm.py 250–308): build `ToolChatRequest` (incl. `tool_policy` from
  payload) → `server.services.tool_chat_service.chat_result(...)`. DELETE
  `_resolve_claude_model_for_profile` (91–109), `_build_agentic_provider` (182–190),
  `_code_index_skill_text` (138–153), `_augment_system_prompt_with_code_index` (156–179). Keep the
  OpenAI-shaped response + `investigation` block. Register the service onto `server.services`.
- registry: register TOOL_CHAT bindings (tool-capable filtered); surface in `/api/llm/status`
  (additive, backward-compatible; `/api/llm/generate` + `text_generate` status unchanged).

## gcore (Rust) payload — verify/extend

- gcore `DaemonChatTransport` POSTs `/api/llm/chat/completions`. The caller's `tool_policy` (codewiki =
  read-only gcode tools) must reach the daemon. Verify the current payload shape; extend to carry
  `tool_policy` + directive WITHOUT breaking the provider-agnostic `daemon_agentic_chat` structure (KEEP).

## Build sequence (Phase 1)

1. ToolPolicy + tool registry (schema + dispatcher) — standalone, unit-testable.
2. `_tool_chat_contracts.py` (request/result/protocol).
3. registry.py `TOOL_CHAT` + registry_builder.py `_tool_chat_adapter_style`/`_tool_chat_binding` +
   tool-capable filter + bindings in `build_daemon_ai_capability_registry`.
4. `_tool_chat_service.py` (dispatch on adapter_style).
5. Family A adapter (OpenAI loop) + Family B claude adapter (generalize generate_agentic).
6. `_tool_chat_builder.py` (style-keyed factories) + wire onto `server.services`.
7. route generalization + DELETE the 4 claude-hardcoded helpers; `/api/llm/status` add tool_chat.
8. gcore payload: send tool_policy from codewiki caller.
9. tests: provider-name grep clean (route/service/call site); same path across llm_provider +
   openai_compatible; codewiki read-only denies write/shell + repo byte-identical; write-capable
   policy fixture passes unchanged; `/api/llm/status` backward-compatible.

## Acceptance recap (provable without bakeoff)
Route/service/call-site request `tool_chat`, resolve via registry, dispatch only on adapter_style,
provider-name grep = NONE. Same path runs through an `llm_provider` and an `openai_compatible` binding.
codewiki read-only policy denies write/shell + repo byte-identical; a write-capable policy fixture passes
unchanged. One clean daemon regen: EXIT 0, zero degraded, lane=tool_loop with real tool calls. Then #981.

## STATUS — daemon Phase 1 COMPLETE (commits on daemon branch `0.5.0`, all `[gobby-#17393]`)

Daemon (`~/Projects/gobby`) tool_chat feature is built, wired, and tested (239 ai+route tests pass;
ruff + mypy --strict clean). Provider-name grep over route/service/tools/contracts = NONE.

- `9681e3f98` contracts + read-only tool registry (`_tool_chat_contracts.py`, `_tool_chat_tools.py`)
- `b86d88901` TOOL_CHAT capability + adapter_style bindings (registry/registry_builder)
- `4d7218463` `ToolChatService` (dispatch on adapter_style; no fallback)
- `b8abcd026` Family A `openai_compatible` adapter (daemon OpenAI tool loop)
- `0946e2bd8` Family B `claude` adapter (in-process MCP tools + mutation hard-denied) +
  `generate_agentic` generalized with `mcp_servers`/`disallowed_tools`
- `786579824` builder (style-keyed factories) + ServiceContainer/runner wiring + route generalized
  (`/api/llm/chat/completions` → ToolChatService; deleted `_resolve_claude_model_for_profile`,
  `_build_agentic_provider`, `_code_index_skill_text`, `_augment_system_prompt_with_code_index`;
  `tool_policy` REQUIRED in the payload) + `/api/llm/status` surfaces tool_chat

### REMAINING

1. **gcore (Rust, THIS repo) payload — DONE** (`4d590772`, `[gobby-cli-#996]`; gobby-core
   0.6.7→0.6.8, gobby-code 1.3.11→1.3.12). **CORRECTION to the earlier reconciliation note:** the
   codewiki daemon caller is `daemon_agentic_chat`/`build_daemon_agentic_body` (daemon-owns-loop), NOT
   `DaemonChatTransport`/`build_daemon_chat_body` (that raw-`tools` path is gcore-runs-loop, used by
   gwiki `compile` + Direct route, and is correctly LEFT UNCHANGED). Fix: added provider-agnostic
   `gobby_core::ai::generation::ToolPolicy {cli, tools, allow_mutation}` (transport.rs), threaded it
   through `daemon_agentic_chat` + `build_daemon_agentic_body` (serialized as
   `tool_policy:{cli,tools,allow_mutation}` in the POST body alongside the existing `project_path`),
   re-exported via `generation/mod.rs`. gcode codewiki `resolve_tool_loop_generator`
   (`commands/codewiki/text/generation.rs`) now builds a read-only policy
   `codewiki_readonly_tool_policy()` (`cli:"gcode"`, the 17 read-only subcommands matching the daemon
   `GCODE_READONLY_TOOLS` whitelist, `allow_mutation:false`) and passes it. Tests:
   `generation/tests.rs` daemon_agentic body assertions extended for `tool_policy`; new gcode unit
   test `codewiki_tool_policy_is_read_only_gcode`. Verified: `cargo nextest -p gobby-core --features
   ai generation` (33), `-p gobby-code codewiki::text::generation` (24), clippy `-D warnings`,
   `fmt --all --check`, doctests — all green. **No provider names** in the gcore/gcode call sites
   (only the `"gcode"` CLI family).
   **Phase-2 caveat:** gwiki `compile`'s daemon route still POSTs raw `tools` via `DaemonChatTransport`
   → it will 422 against the new daemon route until Phase 2 wires its own `tool_policy`. The codewiki
   regen (#981) only exercises the gcode `daemon_agentic_chat` path, so it is unblocked.
2. **Phase 2** — Family B spawn adapters (codex `daemon`/app-server, `cli` droid/…, `acp`) via the
   AGENT_SPAWN seam (`spawn_agent`→`spawn_agent_impl`→`TmuxSpawner.spawn_agent`→`build_cli_command`);
   add a synchronous spawn→wait→final-text path (codex `exec --output-last-message <path>`); flip the
   corresponding styles in `_TOOL_CHAT_EXECUTABLE_STYLES`. Wire the gwiki caller (its own
   richer/optionally-write-capable policy + prompts).

   **VERIFIED RUNTIME FACTS (2026-06-29, autonomous):** all four spawn runtimes installed + credentialed
   (codex `~/.codex/auth.json`; droid `~/.factory/auth.v2.*`; grok `~/.grok/active_sessions.json`;
   qwen `~/.qwen/oauth_creds.json`). Headless invocations confirmed via `--help`:
   - **codex** `exec`: `-s/--sandbox read-only` (FS-only — does NOT block gcode hub/projection writes,
     which mutate Postgres/Falkor/Qdrant not files), `-o/--output-last-message <FILE>` (final text),
     `--json` (JSONL events), `-C/--cd <DIR>`, `-m/--model`, `--ignore-rules`, execpolicy `.rules`.
   - **droid** `exec`: read-only by DEFAULT (`--auto low|medium|high` to widen), `-o/--output-format`,
     `--enabled-tools`/`--disabled-tools`, `--append-system-prompt[-file]`, `--cwd`, `-m`, `-r`,
     `--input-format stream-json|stream-jsonrpc` (multi-turn / JSON-RPC control).
   - **grok/qwen**: ACP style — need an ACP client in the daemon (confirm whether one exists).
   - **gcode has NO `mcp` subcommand** → read-only gcode tools reach claude (Phase 1) via an *in-process*
     SDK MCP server (`create_sdk_mcp_server`). Spawned agents are separate processes → each needs a REAL
     read-only gcode tool surface: either (a) a standalone stdio MCP server wrapping the daemon
     `_tool_chat_tools.py` dispatcher, configured into each agent's MCP config (clean, uniform, the
     LINCHPIN build piece), or (b) sandboxed shell + a command allowlist that blocks gcode mutators
     (codex execpolicy `.rules`; droid `--disabled-tools`/read-only default) — weaker, per-agent. The FS
     sandbox alone is insufficient because gcode mutators write external datastores, not workspace files.
3. **Phase 3** — build/install gcode/gwiki (atomic cp→.new→mv + sidecars), deploy daemon (no regen in
   flight), full daemon regen (EXIT 0, zero degraded, lane=tool_loop), then #981 bakeoff.

## SESSION LOG — 2026-06-29 (deploy + validation, autonomous)

- **Daemon deployed**: user restarted the daemon; it loaded the 7 Phase-1 commits (HEAD `786579824`).
  `/api/llm/status` confirms `tool_chat` live + `available:true` with the two Phase-1 tool-capable
  bindings — `claude` (`llm_provider`) and `local:lm-studio` (`openai_compatible`), both
  `supports_tools:true`; codex/droid/grok/qwen/agy report unavailable with
  `"tool_chat is not yet available for adapter style '…'"`. `text_generate` + `/api/llm/generate`
  unchanged. → #996 criterion 2 PROVEN LIVE.
- **gcode installed**: `cargo build --workspace --release` (exit 0); gcode 1.3.12 atomically installed
  to `~/.gobby/bin/gcode` + `.gcode-version` → `1.3.12`. (`.gcode-install.json` is a stale build-time
  artifact at 1.3.2, not maintained by installs — left as-is.)
- **adapter_style bug (caught by Josh) FIXED** — daemon `4fea44f56` `[gobby-#17393]`:
  `_tool_chat_adapter_style` had copied `text_generate`'s mapping (all CLI-launched providers → `cli`).
  tool_chat is agentic, so it now mirrors `_vision_extract_adapter_style`: grok/qwen → **ACP**,
  droid → **CLI**, codex → daemon, claude → llm_provider, **agy → None** (no agentic transport →
  no tool_chat binding). Corrects `/api/llm/status` labels + Phase-2 spawn-family routing. No Phase-1
  behavior change (ACP/CLI/DAEMON still non-executable). ruff/mypy/`tests/ai` (195) green. **Needs the
  next daemon restart to surface in status** — fold into the post-regen redeploy (do NOT restart
  mid-regen).
- **Lane B validation IN PROGRESS**: scoped regen `gcode codewiki --project <gobby-cli>
  --scope crates/ghook --ai daemon` → exercises the gcode `daemon_agentic_chat` path resolving
  `tool_chat`→claude(`llm_provider`). Verifying: EXIT 0, aggregate frontmatter `lane=tool_loop` +
  `tool_call_count>0`, real (non-echo/non-empty) narrative, zero degraded. openai_compatible
  round-trip probe (lm-studio) deferred until the claude regen completes to avoid confounding.

## SESSION LOG — 2026-06-29 (Phase 1 close + Phase 2 codex, autonomous overnight)

**Phase 1 (#996) CLOSED.** Daemon redeployed at `4fea44f56` (grok/qwen→ACP labels live). Proven live:
claude `llm_provider` (provider=claude/sonnet → adapter_style=llm_provider, tool_use_count=4, read-only
enforced, cited `crates/ghook/src/main.rs:41-64`) + openai_compatible lm-studio (tool_use_count=3).
Grep audit recorded: zero `claude`/`codex` literals in tool_chat service + route (`llm.py`) + contracts;
`_resolve_claude_model_for_profile` + `_build_agentic_provider` absent repo-wide.

**Phase 2 (#997) — codex DONE+PROVEN, then GATED.** Daemon commits (gobby branch `0.5.0`, `[gobby-#17393]`):
- `CodexSpawnToolChatAdapter` (`src/gobby/ai/_tool_chat_spawn.py`): `codex exec` agentic in a neutral cwd,
  `--sandbox workspace-write -c sandbox_workspace_write.network_access=true` (FS read-only on the repo +
  network for gcode→Postgres), on-PATH read-only `gcode` shim (`build_readonly_cli_shim`: whitelist =
  `policy.tools`, injects `--project` unless already present, rejects non-whitelisted/mutators, logs each
  call for `tool_use_count`), final message via `--output-last-message`. Reuses
  `_run_cli_text_generation_command`. 9 unit tests; mypy/ruff green.
- **PROVEN LIVE** (while DAEMON was momentarily executable): provider=codex/gpt-5.5 →
  adapter_style=daemon, **19 read-only gcode tool calls** (repo-outline/grep/outline/symbol/search-symbol),
  grounded multi-citation narrative, repo byte-identical.
- **GATED OFF** in `_TOOL_CHAT_EXECUTABLE_STYLES` (commit: `chore: gate codex…`). WHY: codewiki aggregate
  Lane B sends bare `profile=feature_high` (no candidates) via `build_daemon_agentic_body`; with codex
  tool-capable, `feature_high` = [codex/gpt-5.5, claude/opus] resolves **codex-first**, silently repointing
  codewiki aggregates claude→codex (violates never-codex). Before the flip codewiki got claude only because
  codex was unavailable. Adapter+factory stay wired; re-enabling = 1 line + the caller fix below.

**EMPIRICAL FINDINGS (de-risking before building):**
- `codex exec --sandbox read-only` BLOCKS gcode's Postgres socket (`Operation not permitted (os error 1)`).
  Fix = `workspace-write` + `network_access=true` in a neutral cwd (proven: gcode ran in 199ms).
- `droid exec --auto low` refuses to run gcode (insufficient permission); needs medium/high. droid has NO
  OS write-sandbox → a shell+shim approach can't enforce read-only (shell can always write files). **droid
  (and any spawn agent w/o an OS sandbox) needs a gcode-MCP-tools-only surface (shell disabled).**
- **feature_high tool_chat is broken on the daemon route**: codex/gpt-5.5 (gated) + claude/opus — but
  claude's tool_chat binding only supports `haiku`+`sonnet`, NOT `opus` → 400. WORKING never-codex aggregate
  path = **`feature_mid`** (claude/sonnet), proven. Bakeoff launched with `--ai-aggregate-profile feature_mid`.

### CORRECTION (Josh, 2026-06-29): there is NO never-codex rule
The requirement is **every provider works through feature config** (adapter_style dispatch); the rejected
past work was provider-EXCLUSIVE builds (old codex-pinned writer; a claude-only variant). codex is a
first-class peer. **codex tool_chat is now ENABLED** (`AIAdapterStyle.DAEMON` back in
`_TOOL_CHAT_EXECUTABLE_STYLES`, commit `[gobby-#17393] feat: enable codex…`). So codewiki feature_high
resolving to codex is CORRECT provider-agnostic behavior — not a repoint. NEEDS DAEMON REDEPLOY to go live
(was deferred: bakeoff regen `b0tumhxfk` holds the daemon; redeploy when it finishes). With codex enabled,
the latent feature_high "claude/opus unsupported → 400" is moot (codex is first + available).

### REMAINING Phase 2 work
1. **Redeploy daemon** after the bakeoff regen completes so the codex re-enable goes live; confirm
   `/api/llm/status` tool_chat codex available + a default feature_high probe resolves codex.
2. **droid (CLI)**: build a read-only gcode tool surface the spawned agent uses WITHOUT shell — likely a
   stdio MCP server wrapping `ToolRuntime`, with droid `--disabled-tools` removing shell/write, OR route
   droid's tool calls through the daemon. (Shell+shim is unsafe for droid: no OS sandbox.)
3. **grok/qwen (ACP)**: `adapters/acp_client.py` `ACPClient.send(message, *, model, reasoning_effort,
   pre_tool_callback)` drives one `session/prompt` turn and yields `StreamEvent`s (text + tool events).
   CORRECTION to the earlier note: the agent runs its OWN tools (shell/file in its cwd) — `ACPClient`
   does NOT execute tools for it. The enforcement seam is **`pre_tool_callback`** (async, called before
   each tool request, returns a decision dict|None): approve only read-only ops (read file; run
   `gcode <readonly>` via the on-PATH shim) and DENY writes / mutating-gcode / arbitrary shell. Build a
   grok/qwen ACP tool_chat adapter that: `start()` + `create_session()` in a neutral cwd with the gcode
   shim on PATH, `send()` the composed investigation prompt, gate tools via `pre_tool_callback`
   (read-only classifier), accumulate text StreamEvents into the narrative, count gcode calls from the
   shim log. NOTE the same no-OS-sandbox caveat as droid: `pre_tool_callback` is the ONLY read-only
   guarantee (there is no Seatbelt-style sandbox like codex), so the classifier must be airtight —
   default-deny. Not live-testable until the daemon is free (was holding the bakeoff regen); do NOT ship
   blind. Per-agent ACP subclasses + launch commands already exist in the spawn layer to model from.
   **EMPIRICAL PROBE (2026-06-29, daemon-free, scratchpad/acp_probe.py):** `QwenACPClient` starts +
   creates a session fine, but `send()` (`session/prompt`) immediately returns
   `StreamEvent(event_type='error', data={'message':'Internal error','code':-32603})` and qwen never runs
   the tool (shim log empty). So qwen ACP prompting is NOT working out-of-the-box — diagnose the -32603
   first (likely a required `model` param — qwen text_generate models list is empty in status — or a
   prompt/content-block format issue, or a qwen ACP version mismatch). Do this with the daemon free, then
   build the adapter against confirmed behavior. grok (`GrokACPClient`) unprobed; likely similar.
   ADDITIONAL FINDING: there is NO production caller of `ACPClient.send()` anywhere in `src/gobby` (only the
   class docstring example). So ACP *prompting* has never been exercised — grok/qwen ACP tool_chat is
   greenfield (make ACP `session/prompt` work at all, then wrap it), not a wire-up. Budget accordingly.
   **PROBE RESULTS (2026-06-29, daemon-free):**
   - **qwen ACP**: `-32603` = `'401 Malformed LM Studio API token provided: lm-studio'`. qwen's OWN model
     backend is configured to LM Studio with a bad token (Josh-env config in ~/.qwen, touches the
     LM-Studio token — do NOT modify/reproduce). ACP machinery is fine; qwen just can't reach its model.
   - **grok ACP WORKS**: model `grok-composer-2.5-fast`, auto-connected the `gobby` MCP server (12 tools),
     reasoned, and requested the gcode `Shell`/`run_terminal_command`. TWO seams confirmed: (a) grok
     advertises `_meta.'x.ai/hooks'.blockingEvents=['pre_tool_use'], decisions=['deny']` → a read-only
     ENFORCEMENT seam (deny non-read-only tools); (b) grok delegates terminal commands to the client's
     `ACPTerminalManager`. BUG: the terminal exec failed — it tried to run the literal string
     `/bin/bash -lc 'gcode …'` as argv[0] → `No such file or directory` (argv-vs-shell-string mishandling
     in the ACP terminal path; gcode never ran). FIX that exec path (or route gcode via an MCP server grok
     connects to — grok has `mcpCapabilities: http+sse`), then wire read-only enforcement via the
     pre_tool_use deny seam + capture the assistant text deltas as the narrative. grok is the viable ACP
     target; qwen is blocked until its model-backend config is fixed.
4. **gwiki compile** daemon route still POSTs raw `tools` via `DaemonChatTransport` → 422s against the new
   route; wire its own `tool_policy`.

## SESSION LOG — 2026-06-29 (Josh-steered ARCHITECTURE PIVOT: gobby-index MCP)

**Josh corrected the spawn-provider architecture (do NOT build per-provider shell/MCP plumbing):**
- "gobby is the only mcp our providers use" — droid/grok/qwen/codex connect to exactly ONE MCP: the
  gobby MCP proxy (droid `~/.factory/mcp.json` = `gobby mcp-server`; grok auto-connects `gobby`).
- "you'd build an internal mcp, like gobby-index, a thin shim over gcode, and agents access tools via
  progressive discovery and call_tool." → the read-only gcode surface is a NEW internal MCP server
  proxied by the daemon (sibling of gobby-tasks/gobby-wiki), reached via
  `call_tool("gobby-index", "gcode_search", {...})`.

**This OBSOLETES earlier Phase-2 plans:** the grok `acp_terminal.py` bash-exec "fix", the codex-style
on-PATH shell shim for droid/grok, and any per-provider MCP config injection. My grok probe only hit the
`/bin/bash -lc '…'` bug because the PROMPT said "run the shell command gcode…"; with gcode as gobby-index
MCP tools and shell DISABLED, the bash path is never taken. Read-only is guaranteed by: (a) shell off on
the agent, (b) only gobby MCP reachable, (c) gobby-index exposes ONLY read-only subcommands.

**DONE this session — the linchpin (commit `[gobby-#17393] d5191bd9`):**
`src/gobby/mcp_proxy/tools/code_index.py` `create_index_registry()` → internal `gobby-index` registry.
Exposes the 17 `GCODE_READONLY_TOOLS` as MCP tools named `gcode_<sub>`; each delegates to the existing
`ToolRuntime` (read whitelist validation + argv-exec, no shell + byte-cap). Tool names/descriptions come
from `ToolRuntime.openai_schemas` (identical to the Family A in-process loop). Project resolved per call
from `project` arg (UUID or abs path) → `resolve_project_root`, falling back to the daemon's bound project.
Mutators are NOT registered (unreachable). Wired into `registries.py setup_internal_registries` after
gobby-wiki. 6 unit tests green; ruff/format/mypy clean. **NEEDS DAEMON REDEPLOY to go live** (then
`list_mcp_servers` shows `gobby-index`; `call_tool("gobby-index", "gcode_*", …)` works).

**REVISED remaining Phase 2 (all via gobby-index, after daemon redeploy):**
1. **Redeploy daemon** (`gobby restart`) when no regen is in flight → makes codex re-enable + gobby-index
   live. Confirm `/api/llm/status` codex available + `list_mcp_servers` shows `gobby-index` + a
   `call_tool("gobby-index","gcode_repo_outline",{project:<id>})` round-trips read-only.
2. **droid (CLI)** — ✅ BUILT (commit `[gobby-#17393] 8e37675e`). `DroidSpawnToolChatAdapter` in
   `_tool_chat_spawn.py`: `droid exec --output-format stream-json --disabled-tools Execute,Edit,Create,…`
   in an isolated neutral cwd (Factory home seeded so auth + `~/.factory/mcp.json` travel → gobby MCP
   available). Investigates via `gobby-index` (prompt = `compose_index_investigation_prompt`, passes
   `project=<path>`). Narrative = stream-json `completion.finalText`; tool count from `tool_call` events.
   Read-only proven to rest on droid's DEFAULT read-only exec autonomy (live probe: a Create/Execute
   write attempt was REFUSED, no file written) + gobby-index being read-only. Wired `CLI →
   DroidSpawnToolChatAdapter` in the factory; CLI kept OUT of `_TOOL_CHAT_EXECUTABLE_STYLES` until a live
   gobby-index round-trip proves it. 7 unit tests (real droid 0.159.1 stream-json schema). REMAINING:
   after daemon redeploy + gobby-index live, flip CLI into executable styles + record the live read-only
   proof (droid spawns, calls `gobby___call_tool`→`gobby-index`, returns grounded narrative, repo
   byte-identical). droid model ids are EXACT (`claude-haiku-4-5-20251001`, `gpt-5.5`, …); the droid
   tool_chat binding's models must use droid's ids.
3. **grok (ACP)** `GrokACPToolChatAdapter`: grok already auto-connects `gobby` MCP. Prompt it to use
   `gobby-index` tools (NOT shell); gate any non-gobby-index tool via the `pre_tool_use` deny seam
   (default-deny). Capture assistant text deltas. No bash-exec fix needed.
4. **qwen (ACP)**: STILL externally blocked — qwen's own model backend is LM Studio with a malformed token
   in Josh's `~/.qwen` (do not touch). qwen can't reach its model regardless of tool surface. Document;
   needs Josh to fix his qwen model config. (#997 full-matrix closure depends on this.)
5. **gwiki compile** tool_policy wiring (unchanged).

## SESSION LOG — 2026-06-29 (qwen unblocked + read-only GAP found via probes)

**qwen ACP UNBLOCKED.** Josh provided a working LM Studio API key; set `env.LMSTUDIO_API_KEY`
in `~/.qwen/settings.json` (backup `settings.json.pre-qwen-token.backup`; token NOT printed/committed).
Re-probe (`scratchpad/qwen_probe2.py`, daemon-free): qwen ACP `session/prompt` now WORKS — replied
"READY", `result stopReason=end_turn`, NO -32603/401. qwen model = `gemma-4-31b-q8-local` via LM Studio,
`auth.selectedType=openai`. qwen streams assistant text via **`content_delta`** events
(`data['content']`), completion via **`result`**.

**ACP read-only contract mapped** (`acp_client_requests.py`): `pre_tool_callback({"tool_name","tool_input"})`
→ `{"decision": "deny"|"allow", "reason"}`; deny set = `{deny,block,decline,reject}`; fired for
`fs/write_text_file`, `terminal/*`, `session/request_permission`. qwen tool_call event shape:
`{call_id, tool_name, tool_input, tool_status:"calling"}`; tool_result: `{call_id, tool_status:"completed",
content_blocks:[{type:"text",content}]}`.

**⚠️ CRITICAL READ-ONLY GAP (must resolve before droid/qwen ship read-only):**
qwen tool probe (`scratchpad/qwen_tool_probe.py`) found:
1. qwen ACP **auto-connects its configured gobby MCP** (called `list_mcp_servers` → real server list). Good
   for reach, but it's the FULL proxy, not a read-only subset.
2. **`pre_tool_callback` fired 0 times** — qwen `tools.approvalMode=yolo` auto-executes tools with no
   `session/request_permission`. So the ACP deny seam does NOT fire for qwen-in-yolo.
3. Spawn agents reach gobby-index THROUGH `gobby___call_tool` (the full proxy). The SAME `call_tool` proxies
   to MUTATING tools (`gobby-tasks/create_task`, `set_variable`, config writes). The gobby `call_tool`
   (`mcp_proxy/server.py` GobbyDaemonTools.call_tool) has NO general read-only gating — only a per-workflow
   `blocked_tools` lever + session scope. droid's read-only autonomy gates shell/file tools but marks
   `gobby___call_tool` ALLOWED (can't introspect the proxy's downstream effect). So neither droid nor qwen is
   airtight read-only via agent-side controls. codex is unaffected (Seatbelt + shell shim, never touches the
   proxy).

****context7 research (2026-06-29) confirms agent-side controls are fragile/per-provider:**
- ACP spec: `session/new.mcpServers` is the client-supplied server set; `session/request_permission`
  (options allow_once/reject_once, outcome selected/cancelled) is the deny seam — BUT only fires if the
  agent's approval mode requests permission. (qwen empirically still merges its own settings.json
  mcpServers, so passing a scoped list in session/new is not guaranteed to REPLACE the full proxy.)
- qwen-code: approval mode is configurable (`permissions.defaultMode`: plan/auto-edit/yolo; Josh's is
  yolo → no permission prompts). Per-server `includeTools`/`excludeTools` exists but is tool-NAME level —
  it cannot restrict what `call_tool` TARGETS, so it can't stop the proxy from reaching mutators.
- => No per-provider knob is uniformly airtight. Server-side gating is the answer.

RESOLUTION NEEDED (Josh design call) — recommend (A):** server-side read-only gating of `call_tool` for
tool_chat spawn sessions — restrict targets to a read-only allowlist (gobby-index + read-only servers/tools),
deny mutating targets. Reuse/extend the existing `blocked_tools`/session-scope mechanism (set a read-only
scope when the daemon spawns a tool_chat agent). Uniform + airtight across qwen(yolo)/droid/grok; preserves
"gobby is the only MCP." Alternatives: (B) a read-only-only gobby MCP variant for spawn agents; (C) per-agent
approval-mode + classifier (fragile: qwen yolo, droid can't gate proxy by effect). The droid commit
(8e37675e) read-only claim is INCOMPLETE until (A) lands — `_DROID_DISABLED_TOOLS` blocks native shell/write
but not the proxy path; note added here so it isn't trusted as airtight.

### GAP FIX = TARGETED RULES (Josh, 2026-06-29) — SUPERSEDES the "bespoke call_tool gating" framing above
Josh: "why wouldn't we just use targeted rules?" → DO NOT hand-roll read-only logic inside
`GobbyDaemonTools.call_tool`. Use Gobby's existing RULES ENGINE (the layer that gates my own tool use).
Confirmed it CAN block MCP tool calls (`services/tool_execution.py` `_tool_filter`; `result_handling.py`
"Tool call blocked by workflow rules"; `hooks/rule_evaluator.py`). Aligns with the recalled "use existing
side channels, don't half-land infra" principle.

**Rule shape** (per `build-rule` skill, loaded): `before_tool` + `block`. `effect.block` matches
`mcp_tools: ["server:tool"]` (supports `"server:*"`) and native `tools` (`mcp__gobby__call_tool`, Bash,
Edit, Write). Conditions read `event.data.get('tool_name')`, `tool_input` (call_tool args →
`tool_input.get('server_name')`/`get('tool_name')`), `variables`. Scoping levers: `agent_scope:[..]`,
top-level `audience:` (precedent `rules/build/build-agent-safety.yaml` = `audience: autonomous` +
before_tool/block, no session marker), or a session variable. Rules live in
`src/gobby/install/shared/rules/...`; install via `gobby rules import <file>` or `gobby-workflows
create_rule`. Gotchas: first block wins; block FAILS CLOSED on condition error; YAML regex double-escaped.

**Draft rule** (default-deny the proxy for read-only tool_chat spawn sessions):
```yaml
group: tool-chat-readonly
rules:
  tool-chat-readonly-proxy-allowlist:
    description: "Read-only tool_chat spawn agents may only proxy to gobby-index + discovery."
    event: before_tool
    priority: 15
    when: >-
      variables.get('tool_chat_readonly', False)
      and event.data.get('tool_name') == 'mcp__gobby__call_tool'
      and tool_input.get('server_name') not in ['gobby-index']
      and tool_input.get('tool_name') not in ['list_mcp_servers','list_tools','get_tool_schema','search_tools','recommend_tools']
    effect:
      type: block
      reason: "Read-only investigation: only gobby-index tools and discovery are permitted."
```

### SCOPING MARKER — RESOLVED 2026-06-29 (reuse the existing GOBBY_SESSION_ID child-session pattern)
Josh: "we have a pattern for this — we inject an env var for spawned agents in gobby-agents already."
Confirmed by direct code reading:
- `src/gobby/mcp_proxy/stdio_proxy.py:87` — the spawned agent's `gobby mcp-server` (DaemonProxy) does
  `self._session_id = os.environ.get("GOBBY_SESSION_ID")` and binds EVERY proxied call to that session.
- `src/gobby/agents/constants.py` (~L100 builder; env dict at L126: `GOBBY_SESSION_ID: session_id`,
  `GOBBY_AGENT_RUN_ID`, `GOBBY_PROJECT_ID`, …) — canonical spawned-agent env builder, keyed on a
  pre-created child `session_id`. `prepare_terminal_spawn` (`src/gobby/agents/spawn.py:76` → returns
  `PreparedSpawn` at L48) pre-creates that child session.
- Session variable set from daemon code: `SessionVariableManager.set_variable(session_id, name, value)`
  (`src/gobby/workflows/state_manager.py:~214`).

**Mechanism:** the tool_chat spawn adapter (1) pre-creates a child daemon session, (2) sets
`tool_chat_readonly=true` on it via `set_variable`, (3) injects `GOBBY_SESSION_ID=<that session>`
(+ `GOBBY_PROJECT_ID`) into the codex/droid subprocess env (`env_overrides` to
`_run_cli_text_generation_command`). The agent's `gobby mcp-server` reads `GOBBY_SESSION_ID` → every
`call_tool` binds to the tagged session → the `before_tool` rule fires for exactly those calls. No new
plumbing; reuses the gobby-agents child-session env pattern. Native tool vectors (droid/qwen own
shell/edit) run in a NEUTRAL temp cwd (harmless) + the agent's own read-only mode; the rule closes the
gobby-proxy vector.

**Decision (Josh, 2026-06-29):** REMOVE the read-only CLI shim (`build_readonly_cli_shim` /
`compose_spawn_prompt`) — it was never requested. Codex investigates via `gobby-index` over the gobby MCP
proxy like droid; read-only is enforced by the rule above, not a shell shim. Remaining: rewire codex off
the shim onto gobby-index (needs codex's gobby-MCP config: codex `config.toml` `mcp_servers.gobby` →
`gobby mcp-server` carrying `GOBBY_SESSION_ID`; ref memory aaf145b0 "Codex MCP config overrides for the
internal gobby server carry GOBBY_SESSION_ID/GOBBY_PROJECT_ID; stdio DaemonProxy reads X-Gobby-Session-Id"),
delete shim helpers, author rule (`scratchpad/tool-chat-readonly.yaml` draft), wire pre-create+tag session,
test, `gobby sync` to activate, (post-redeploy) live proof.

PENDING FROM JOSH: (a) redeploy timing — stop 7h+ regen `b0tumhxfk` + `gobby restart` (unblocks ALL live
proofs: codex, gobby-index, droid, qwen); (b) qwen yolo flip (NOT needed with the rule).
