# Wiki parity+ program — Claude executes all WPs via /goal, self-audits at the end

**Execution model (Josh, 2026-06-12):** Claude executes all work packages directly — this is too critical for a worker handoff. Fresh-context session driven by a /goal prompt; **run `compact_self` between work packages** (after each WP's task is closed) to keep context tight. WP order: WP2a → WP2 → WP2b → WP3 → WP4 → WP5, one gobby task per WP (claim before edits, close with commit SHA per task-transitions gates). The "Final audit" section below becomes a final self-audit pass run with post-compact fresh eyes; Josh reviews and pushes.

## Already done (summary)

- **Root causes diagnosed (2026-06-12):** daemon ran one-shot text generation as full agent-harness turns (no sandbox/approval/tool restrictions, no per-candidate timeout); codewiki output is thin **by design** (one-sentence prompts, 600-char excerpts, alphabetical citation fallback `text.rs:277-298`, unbounded frontmatter, architecture diagram can't render off the `crates/docs/scripts` root split); old gwiki ask shipped ~66K-token synthesis prompts (codex transcript `~/.codex/sessions/2026/06/12/rollout-2026-06-12T13-14-32-019ebd0a-f491-7702-a02e-bcda9ad8360d.jsonl`).
- **WP1 daemon fix: DONE** (daemon task #17061 closed): codex one-shot contract (approval never, readOnly sandbox, no-tools/no-narration directive, effort auto), ACP deny-all `pre_tool_callback` for gemini/grok/qwen, `ai.generation.candidate_timeout_seconds` (60s) in text+JSON candidate loops. Verified live: codex probe 20.2s→~12s; gemini clean at 30s; `tasks.validation` passing; 1009 focused tests/ruff/mypy/audit green. Follow-up **#17062** filed (pre-warmed codex client reuse, ~6–8s savings).
- **Pivot (Josh, refined 2026-06-12):** gwiki works like gcode lookups — `gwiki search` becomes the agent retrieval primitive; `research` (unshipped) is removed (the calling agent IS the research loop; background automation returns later as a daemon goal-loop if wanted); `ask` is **rebuilt thin** (search top-k → bounded ≤~12K-token prompt → one completion → grounded citations) with transport daemon **or** standalone OpenAI-compatible endpoint including LM Studio — DeepWiki-parity Q&A without the old 66K context machine. Note-deposit primitives (collect/ingest, citations, provenance) stay. The general wiki additionally gains synthesized explainers (WP2b) — today it has zero LLM synthesis (ingest converts, compile assembles, both deterministic).
- **Degraded-regen finding:** the current vault was regenerated 2026-06-12 00:02 (91d4021) during the broken-lane window — **134 pages carry structural-fallback stubs** ("exposes N symbols" etc.), 12 explicit degraded markers; per-symbol purposes (442 file pages) survived via hash reuse and are genuinely good. Top-down browsing hits the degraded/thin tiers first, which is why the wiki reads as empty. Auto-heal (#687) regenerates these on the WP3 re-run.

## Execution conventions (binding)

- `/Users/josh/Projects/gobby` = daemon repo — one coordinated change in scope: the WP2a research-removal/ask-sync (own gobby task). Anything else WP3 surfaces: file tasks, don't fix drive-by. `/Users/josh/Projects/gobby-cli` = all other WP work.
- Create/claim a gobby-cli MCP task per WP before edits; close each with commit SHA before `compact_self`. Task refs are project-qualified (gobby-cli #720 is the narration task — already closed, do not reopen).
- Explicit paths, explicit git staging, no `git add -A`, **no push** (Josh pushes). Commit format `[gobby-cli-#NNN] type: summary`.
- Focused validations only; `GOBBY_TEST_PROTECT=1` prefix for any pytest. `.env` files mode 600; never print secrets.
- No speculative file decomposition (no repo rule requires it; in-scope files are 41–955 lines). Minimal mechanical extraction only if a gate forces it.

## WP2a — gwiki search as the agent retrieval primitive + thin RAG ask (remove research)

Execute the Codex spec "Make gwiki search the Agent Retrieval Primitive" (2026-06-12), amended per Josh: **ask is rebuilt thin, not removed; research is removed.**

- Extend `gwiki search` like `gcode search-content`: compact ranked query-token snippets (never full document bodies), provenance, `result_type`, `source_path`, `sources`, `code_citations` tied to returned hits only, degradation flags, `--limit`, `--format text|json`, semantic toggle, scope selection. Drop whole-scope related-page/code-citation expansion from the default path.
- **Thin ask (DeepWiki-parity Q&A):** rebuild `gwiki ask` as a thin layer over search — top-k bounded evidence (≤ ~12K tokens) → one completion → answer with grounded citations. Transport: daemon route (default) **or** standalone OpenAI-compatible endpoint via the existing gcore direct path (`ai.text_generate.api_base`/`api_key`, including LM Studio local). Delete the old whole-scope context machine (the 66K-token assembly behind the previous ask path); keep the shipped narration stripper as defense-in-depth on the answer.
- Remove `research` from CLI, API enum, dispatch, `gwiki.contract.json`, docs, daemon command list. Delete `crates/gwiki/src/commands/research.rs`, `crates/gwiki/src/research/`, `crates/gwiki/src/research_loop/` after moving reusable helpers. Keep collect/ingest, citations, provenance — agents deposit research artifacts through those.
- **Keep ask's CLI flag surface unchanged** (`--llm`, `--ai auto|daemon|direct|off`, `--require-ai`) — only the context assembly and output JSON change. This keeps `GwikiGateway.ask` (`gwiki_gateway.py:89-111`) untouched.
- **Coordinated daemon change (separate gobby task, `[gobby-#NNNNN]` commit):** remove `GwikiGateway.research()` (`src/gobby/gwiki_gateway.py:137`), the scheduled research jobs (`src/gobby/wiki/scheduled_jobs.py:73,133` — these fail at runtime once the command is gone), the MCP research tool (`src/gobby/mcp_proxy/tools/wiki.py:224`), and the HTTP route (`src/gobby/servers/routes/wiki.py:184`). Sync the MCP ask tool description/schema (`mcp_proxy/tools/wiki.py:118`) and any daemon tests pinning the old `AskOutput` whole-scope fields to the new bounded-evidence output. Retire `docs/contracts/gwiki-research.md` in gobby-cli alongside. Focused daemon tests with `GOBBY_TEST_PROTECT=1`; restart daemon after.
- Tests: CLI parser (research gone; ask + search flags intact), contract drift (pinned `gwiki.contract.json` matches new command set), search output bounds (no full bodies / no whole-scope dumps), ask prompt-budget bound (never exceeds the token cap), citation/provenance helpers covered at their new home.
- Gates: `cargo fmt --check`, `clippy -p gobby-wiki -- -D warnings`, `cargo nextest run -p gobby-wiki`.

## WP2 — Codewiki content parity upgrade (DeepWiki-grade pages)

`crates/gcode/src/commands/codewiki/`. Gates: fmt, `clippy -D warnings`, `cargo nextest run -p gobby-code`.

1. **Prompts → documentation briefs with real retrieved input** (`prompts.rs`, `build_parts/`): Aggregate-tier pages get structured multi-paragraph briefs (module: responsibilities, key flows, submodule collaboration; repo: what the system is, how pieces fit, where to start; architecture: layered subsystem-interaction narrative). **Feed the model actual source content, not just summaries-of-summaries**: per page, retrieve top-k chunks/symbols for that module from our own index alongside child summaries (the DeepWiki lesson: rich input + demanding template → rich output). Symbol purpose stays one sentence. `CHILD_SUMMARY_EXCERPT_MAX_CHARS` 600 → ~2000. Keep no-fences + grounding contract.
2. **Real architecture page** (`build_parts/architecture.rs`, `render.rs`): decomposition starts at meaningful units (the six crates, not `crates/docs/scripts`) so the cross-subsystem mermaid renders; enumerate top 1–2 module levels only; add layered narrative.
3. **Front page** (`render.rs`): system narrative + crate-level dependency mermaid; drop "has no indexed API symbols" filler.
4. **Non-code file stubs** (`build_parts/file.rs`, `render.rs:716`): generate Purpose from leading content chunks for markdown/config files; structural fallback unchanged.
5. **Citation relevance** (`text.rs:277-298`): lexical-overlap scoring (sentence text vs span file path + symbol names); deprioritize asset/data files unless sole provenance; keep `MAX_FALLBACK_CITATIONS=5`.
6. **Frontmatter provenance cap** (`text.rs:486-533`): cap per page (~top 30 files by span count + `provenance_truncated: N`).
7. **Diagram coverage:** with (2), dependency/call mermaid emits wherever bounded edges exist; keep hops/edges bounds; never fabricate edge-free diagrams.

Unit tests for new prompt builders, citation scoring, provenance cap, architecture clustering.

## WP2b — General-wiki synthesis (knowledge explainers)

Per Josh's expectation ("summaries… explainers… same for the wiki"): the general wiki currently has **zero** LLM synthesis — ingest converts faithfully, compile assembles deterministically. Add cited synthesized pages over ingested content:

- Extend `compile` (or add a sibling surface) to generate overview/topic pages from vault notes through the daemon text lanes: per ingested source (or topic cluster), a structured explainer with citations into the source documents, using the same grounding approach as codewiki (`ground_text`-style validation against vault provenance).
- Deterministic skeleton + LLM prose sections, degradation markers + structural fallback on AI failure (mirror codewiki's honesty contract). Bounded prompts (same ~12K budget discipline).
- Tests: explainer generation with mocked AI client (prompt shape, citation grounding, fallback), compile integration, contract/docs updates.
- Gates: fmt, `clippy -p gobby-wiki -- -D warnings`, `cargo nextest run -p gobby-wiki`.

## WP3 — Regenerate + general-wiki re-verification

1. `cargo build --workspace --release`; deploy gcode/gwiki to `~/.gobby/bin` (atomic cp→mv + `.{name}-version` sidecars).
2. Regenerate codewiki (`gcode codewiki`, daemon routing); `gwiki collect/index`. Verify **zero degraded pages AND zero structural-fallback markers** (greps: "exposes N symbols" pattern, "has no indexed API symbols", `degraded_sources`) — the 134 currently-degraded pages must heal.
3. General wiki "by the book" (mirror `fable-repo-analysis.md:371-559`): `init`/`setup`/`status` sanity, fresh `ingest-url` (Wikipedia page), `ingest-file` (README or docs/guides page), `collect` inbox drop, one multimodal source if convenient; `index` zero degradations; hybrid `search` shows bm25+semantic+graph sources; `compile` + WP2b explainers produce valid cited output through the fixed lanes.
4. Retrieval Q&A evidence: 4–5 questions (incl. "What happens when the ghook inbox enqueue fails?") answered two ways, transcripts saved: (a) agent-composed `gwiki search` + `gwiki read` (sub-second search, compact snippets, correct citations), and (b) **thin `gwiki ask`** — once via daemon route, once via the direct OpenAI-compatible endpoint (LM Studio) — clean cited answers, prompt within budget, target <10s.
5. Agent research-deposit demo (replaces the old research run): research a small topic via `gwiki search`/`read`, write a cited note, register it via `collect`/`ingest-file`, and show it lands in the vault with provenance and survives `index`/`lint`.

## WP4 — Competitor bake-off (DeepWiki-Open, Graphify, CodeWiki, OpenDeepWiki, llm-wiki)

**Status: DONE (2026-06-14), task #734.** All 7 comparators run + scored across 3 tracks (A1 gcode↔Graphify, A2 codewiki↔DeepWiki-Open/CodeWiki-Rust/CodeWiki-Py/OpenDeepWiki, B gwiki↔llm-wiki). Per-tool `SCORECARD.md`+`SETUP.md` and the `ADOPTION-CANDIDATES.md` running log (C1–C10 + W1) on disk at `~/Projects/wiki-bakeoff/`; lightweight copies committed to `docs/evidence/wiki-bakeoff-2026-06/`. Raw outputs preserved as the before-baseline for a post-adoption re-run.

Workspace `~/Projects/wiki-bakeoff/`. **Credentials source of truth: `/Users/josh/Projects/gobby/.env`** (chmod 600; defines `OPENAI_API_KEY` + `OPENAI_BASE_URL`). Copy these values into `~/Projects/wiki-bakeoff/.env` (also chmod 600) and per-tool configs as needed — never print or commit values; rewrite the base-URL host per transport below. **Prefer each repo's Docker/docker-compose setup over local installs** (Josh's preference); fall back to local only if no container path, noted in per-tool `SETUP.md`. Containers reach LM Studio via `http://host.docker.internal:1234/v1`; local runs via `http://localhost:1234/v1`. Model `google/gemma-4-26b-a4b-qat`. Mount gobby-cli read-only; bind outputs to `~/Projects/wiki-bakeoff/outputs/<tool>/`; list containers/images in `SETUP.md` for later cleanup.

1. Run all five tools against gobby-cli, **one Docker stack at a time** (the daemon stack — postgres/falkordb/qdrant/postgres-test — is already up; do NOT stack 5 more concurrently: bring one up, capture, tear down, next). Capture complete outputs to `~/Projects/wiki-bakeoff/outputs/<tool>/`.
2. **Primary axis is OUTPUT QUALITY for humans AND agents — not speed** (Josh, 2026-06-14). Wall-clock is model-bound on one shared local gemma and is recorded only as a caveated note, never a ranking axis. Score each tool with a per-tool `SCORECARD.md` on two axes: **human-reader** (coverage of files/modules vs total, narrative depth vs one-line stubs, navigation/cross-links/hierarchy, diagrams that render + are accurate, broken-link count, does browsing actually teach the system) and **agent-consumer** (grounding precision — claims cite `file:line` vs ungrounded prose, retrievability/searchability, Q&A with cited answers, provenance/frontmatter, and **honesty** — does it hallucinate APIs that don't exist or honestly degrade).
3. Fairness note: all tools use the same local gemma-4-26b + nomic embeddings, configured with ONLY endpoint+API-key+model-ids — the tool's OWN defaults for all inference/chunking/retrieval (no hand-tuning token budgets etc.; how a product configures itself for the model we give it is part of what we measure). State the model-quality caveat; the comparison is structure/coverage/grounding/honesty.
4. **Document what each competitor does BETTER and what gobby should adopt** (Josh, 2026-06-14). Maintain the durable running log `~/Projects/wiki-bakeoff/ADOPTION-CANDIDATES.md` (on disk → persists across compaction) — per candidate: source tool + evidence path, what it does, **why it's better**, how it maps into gobby's codewiki (`crates/gcode/src/commands/codewiki/`) / gwiki (`crates/gwiki/`) internals, rough effort/risk, dedupe notes. Also log competitor weaknesses (gobby wins) for the proof matrix. This file feeds WP5.

## WP5 — Parity+ proof artifact

**Status: DONE (2026-06-14), task #734.** `fable-repo-analysis.md` → "Phase 4 — Live parity-plus proof" appended (3 per-track re-scored matrices, honest verdicts incl. competitor wins, "What competitors do better → what to adopt" C1–C10 deep analysis). Adoption epic **#761** created with one leaf task per candidate: #762 (C1), #763 (C2), #764 (C3), #765 (C4), #766 (C5), #767 (C6), #768 (C7), #769 (C8), #770 (C9), #771 (C10).

Append dated **"Live parity+ proof (2026-06)"** to `/Users/josh/Projects/gobby-cli/fable-repo-analysis.md`: the 7-dimension matrix re-scored with WP3 outputs side-by-side against WP4 outputs, file-path pointers into `~/Projects/wiki-bakeoff/outputs/` and command transcripts, honest per-dimension verdicts including any competitor wins. **Q&A dimension now has both claims:** thin `gwiki ask` compared apples-to-apples against DeepWiki chat (bounded RAG, grounded citations — theirs hallucinate), PLUS the agent-native retrieval primitive (search+read composition) that no competitor offers.

**Adoption deliverable (Josh, 2026-06-14):** beyond noting competitor wins, the report includes a **"What competitors do better → what to adopt"** section carrying the *deep per-candidate analysis* (what the competitor does, evidence artifact, why incorporate, gobby codewiki/gwiki mapping, effort/risk), sourced from `~/Projects/wiki-bakeoff/ADOPTION-CANDIDATES.md`. Then create **one gobby-cli epic with one leaf task per adoption candidate** — created ONCE here at WP5, evidence-backed and deduped across all five tools; each leaf body quotes its report analysis and links the evidence artifact. The bake-off's highest-value output is this adoption backlog, not the win/loss scorecard.

## Final audit (Claude, after WP5)

1. **Code review:** post-compact diff review of all program commits in both repos (contract/schema safety, no hub mutations, test honesty); re-run gates: fmt, `clippy -D warnings`, `cargo nextest run -p gobby-wiki -p gobby-code`.
2. **Pivot verification:** research fully gone (CLI/contract/docs/daemon list); Claude personally answers 2–3 questions via `gwiki search`+`read` (compact evidence, correct citations, sub-second), runs thin `gwiki ask` on both transports (daemon + LM Studio direct) verifying budget + citations + <10s, and runs the deposit path once (note → collect → indexed with provenance).
3. **Wiki quality:** spot-check regenerated repo.md/_architecture.md/gwiki-module page against the DeepWiki bar (multi-section narrative, diagrams, relevant citations, no filler, bounded frontmatter); `gwiki lint` zero broken links; `status`/`health`/`audit` clean; zero structural-fallback markers.
4. **Bake-off integrity:** each competitor run completed without sandbagging misconfiguration (check tool logs); metrics table matches outputs on disk.
5. **Proof artifact:** every claim in the new fable-repo-analysis.md section traceable to a disk artifact.
6. **Close-out:** verify every WP task closed with commit SHAs; flag anything unfinished; report the full program summary to Josh. Josh pushes both repos (daemon commits + gobby-cli commits); no tags from Claude.
