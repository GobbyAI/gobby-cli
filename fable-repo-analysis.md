# Gobby CLI — Repo Analysis & Parity-Plus Benchmark

Working document for epic **#590** (source plan: `.gobby/plans/goal.md`).
Scope: per-crate review findings (Phase 1), competitor feature comparison (Phase 2), and the
per-dimension parity-plus verdict for gcode codewiki + gwiki against the leading open-source
repo-wiki generators.

Status legend: ✅ done · 🔄 in progress · ⬜ pending

| Phase | Item | Status |
|---|---|---|
| 0 | Build & deploy (gcode 1.0.0, gwiki 0.3.0, gsqz 0.4.6, gloc 0.1.4, ghook 0.4.6 → `~/.gobby/bin`) | ✅ |
| 1 | gobby-core review (#591) | ✅ |
| 1 | gobby-code review (#592) | ✅ |
| 1 | gobby-wiki review (#593) | ✅ |
| 1 | gsqz review (#594) | ✅ |
| 1 | gloc review (#595) | ✅ |
| 1 | ghook review (#596) | ✅ |
| 2 | Competitor verification & feature inventory | ✅ |
| 2 | Parity matrix + per-dimension verdict | ⬜ |
| 3 | Fresh wiki + codewiki by the book (#611) | 🔄 |

---

## Phase 1 — Per-crate reviews

### gobby-core (gcore) — task #591

**Verdict: SOLID-WITH-ISSUES.**

gcore is a genuinely well-built foundation crate: every feature gate compiles standalone
(no-default-features plus each of postgres/falkor/qdrant/indexing/search/graph-analytics/
local-backend/ai/full individually — all PASS), clippy is clean under `--all-features`, and the
documented AI ownership split holds mechanically — no `reqwest`/`ureq` reachable from
`ai_context`/`ai_types` or any always-compiled module; HTTP transport is confined to `ai/`
(feature `ai`) and `qdrant.rs` (feature `qdrant`). Test density is high (99 tests no-default,
189 all-features, all passing) with dependency-injected fakes in the right places. Consumers
delegate properly for search/RRF, postgres, falkor, qdrant, indexing, secrets, and graph
analytics.

The real problems: an inconsistent `GOBBY_HOME` contract that can make the AI daemon probe and
the AI daemon POST resolve **different daemon URLs**; a cluster of dead/test-only public API;
`ureq` wired to the wrong Cargo feature; and three divergent reimplementations of daemon-URL
resolution in gcode/gsqz that bypass gcore entirely (gsqz never reads bootstrap.yaml at all, so
a custom `daemon_port` silently breaks its daemon integration).

`tests/public_boundary.rs` is meaningful for locking feature wiring and gloc's
`default-features = false` posture, but is string-snippet based (pins exact dep lines including
versions) and does not check the actual exported API surface.

#### Findings → tasks

| Finding | Sev | Category | Task | Title |
|---|---|---|---|---|
| GCORE-01 | high | correctness | #597 | Unify GOBBY_HOME handling for bootstrap.yaml and daemon URL resolution |
| GCORE-02 | medium | correctness | #598 | Expand env patterns in AiConfigSource when standalone layer absent |
| GCORE-03 | medium | error-handling | #599 | Log swallowed resolve_value errors in config resolution |
| GCORE-04 | medium | architecture | #600 | Move ureq to the ai feature; unify HTTP probe implementations |
| GCORE-05 | medium | straggler | #601 | Remove test-only local-backend discovery shim from ai_context |
| GCORE-06 | medium | straggler | #602 | Delete unused public API (CoreContext, probe_local_backend, default_backends) |
| GCORE-07 | medium | consolidation | #603 | Consolidate all daemon URL resolution onto gobby_core::daemon_url |
| GCORE-08 | low | consolidation | #604 | Deduplicate keyword-DSN tokenizer (degradation vs postgres) |
| GCORE-09 | low | straggler | #605 | Remove stale migration-era comments (project.rs, types.rs, dev guide) |
| GCORE-10 | low | straggler | #606 | Fix stale allow(dead_code) justifications in test_http |
| GCORE-11 | low | test-gap | #607 | Add serialization tests for cli_contract |
| GCORE-12 | low | error-handling | #608 | Align invalid-value handling (resolve_port vs resolve_config_bool) |
| GCORE-13 | low | consolidation | #609 | Lift gsqz/gloc layered YAML config loader into gcore |
| GCORE-14 | low | test-gap | #610 | Add connector-construction tests for postgres TLS modes |

### gobby-code (gcode) — task #592

**Verdict: SOLID-WITH-ISSUES.**

Cleanly layered (thin `main.rs` → `dispatch.rs` → `commands/` over `index/`, `search/`, `graph/`,
`vector/`, `visibility`, `freshness`, `projection`). Consolidation discipline against gcore is
strong and test-guarded: `hasher`/`secrets` are pure re-exports, RRF delegates to
`gobby_core::search::rrf_merge`, FTS uses gcore's `TrustedRowId`/`bm25_score_expr`, and the
chunker documents and asserts why it stays gcode-owned. UUID5 parity is correct with Python
golden vectors; runtime schema is validate-only with creation confined to `gcode setup`
(touches only `code_*` relations). 602 tests pass; clippy clean.

The two big holes are both in the codewiki path: scoped runs (`--scope`) delete every
out-of-scope generated doc (io.rs prunes anything absent from the current run), and daemon-written
symbol summaries are wiped on every reindex because delete-then-insert makes the ON CONFLICT
summary-preservation clause dead code — silently degrading wiki prose to bland structural lines
over time. "Incremental regeneration" only skips disk writes, not AI generation cost. Also: no
logger is initialized so every `log::*` diagnostic is dropped, and PG-gated tests vacuously pass
when the test DSN is absent.

**Codewiki readiness:** nothing blocks a fresh by-the-book run. Citation handling is real
(`ground_text` strips citations not matching indexed source spans and appends a valid fallback
span); provenance frontmatter and `[[wikilinks]]` follow the gwiki contract; graph-degraded mode
produces valid docs exactly as documented. Fix-before-production-use: #614 (scope deletion) and
#616 (unbounded AI regeneration cost).

#### Findings → tasks

| Finding | Sev | Category | Task | Title |
|---|---|---|---|---|
| GCODE-01 | high | correctness | #613 | Preserve unchanged-symbol summaries across file reindex |
| GCODE-02 | high | correctness | #614 | Make scoped codewiki runs preserve out-of-scope docs |
| GCODE-03 | medium | error-handling | #615 | Initialize a logger or route log calls to stderr |
| GCODE-04 | medium | correctness | #616 | Skip AI prose regeneration for unchanged files |
| GCODE-05 | medium | correctness | #617 | Reconcile stale facts for discovered files that fail AST indexing |
| GCODE-06 | medium | test-gap | #618 | Postgres-backed tests for code-fact upsert SQL semantics |
| GCODE-07 | medium | error-handling | #619 | Propagate DB errors in embedding/AI config resolution |
| GCODE-08 | medium | architecture | #620 | Batch codewiki symbol loading (N+1) |
| GCODE-09 | low | straggler | #621 | Replace leaked blame worker threads |
| GCODE-10 | low | straggler | #622 | Update CLAUDE.md re: standalone projection sync ownership |
| GCODE-11 | low | error-handling | #623 | Actual affected-row counts; dedupe MAX_FILE_SIZE |
| GCODE-12 | low | consolidation | #624 | Pin codewiki→gwiki frontmatter contract with shared fixture |

### gobby-wiki (gwiki) — task #593

**Verdict: SOLID-WITH-ISSUES.**

Cleanly layered: `Command` enum → `commands::run` dispatch, trait-based search backends fused via
gcore's shared `rrf_merge`, modality orchestrators returning explicit degradation envelopes, and a
vault model with durable atomic writes and a locked provenance graph. The hybrid search stack is
already largely consolidated into gcore (RRF, BM25 sanitization, Qdrant client, Falkor
`GraphClient`) — the remaining gcode/gwiki duplication is the direct OpenAI-compatible embeddings
HTTP client (#625). 522/522 tests pass with default features; clippy clean.

Seam-level issues: one legacy compat shim in session checkpoints (policy violation → removal task
#626), `gwiki index` swallows Qdrant/Falkor sync failures and reports success (#628),
`citation-quality`'s contradiction detection is a permanent placeholder (#627), and `ask --llm`
prose is grounded by prompt only — no post-generation citation check (#629), the one real gap
against the "AI prose must be citation-checked" constraint. Persisted content (research → compile
→ audit) is sound: uncited claims are rejected at note validation, compiled pages carry
provenance links with byte offsets, and audit checks pages against the provenance graph.

**Live regression found during Phase 3 (fixed directly, #612):** commit 6a9bc97's CodeRabbit
batch reverted the deliberate `::text::jsonb` casts in `store.rs`, breaking every PostgreSQL
wiki index write (`error serializing parameter 9`). Fixed type-correctly with
`serde_json::Value` params (postgres `with-serde_json-1`); also surfaced DbError detail in
`StoreError` and made `gwiki_ingestions.content_hash` nullable to match the indexer's
Deleted/Skipped event model. No unit test could have caught it — store.rs Postgres writes have
no live-DB coverage (same shape as GCODE-06/GCORE-14).

#### Findings → tasks

| Finding | Sev | Category | Task | Title |
|---|---|---|---|---|
| GWIKI-01 | medium | consolidation | #625 | Move direct embeddings client into gobby_core::ai |
| GWIKI-02 | medium | straggler | #626 | Remove legacy checkpoint scope-root migration |
| GWIKI-03 | medium | placeholder | #627 | Implement contradiction detection in citation-quality |
| GWIKI-04 | medium | error-handling | #628 | Surface Qdrant/Falkor sync degradations in index output |
| GWIKI-05 | medium | correctness | #629 | Citation-check or mark unverified ask --llm output |
| GWIKI-06 | low | error-handling | #630 | Unify modality/daemon-probe degradation reasons |
| GWIKI-07 | low | correctness | #631 | Accurate degradation kind for global semantic fan-out |
| GWIKI-08 | low | test-gap | #632 | Run feature-gated tests in canonical invocation |
| GWIKI-09 | low | straggler | #633 | Fix stale 'sync flags for daemon' in CLAUDE.md |
| GWIKI-10 | low | straggler | #634 | Narrow lib.rs blanket dead_code allowances (#357) |
| GWIKI-11 | low | docs | #635 | Document or gate undocumented subcommands |
| GWIKI-12 | low | consolidation | #636 | Consolidate vision/transcription degradation constructors |
| GWIKI-13 | low | correctness | #637 | Per-section provenance links during compile |

### gsqz — task #594

**Verdict: SOLID-WITH-ISSUES** (one blocker).

Clean seams (`main.rs` → `compressor` → pure `primitives/*`), daemon HTTP correctly
feature-gated, primitives panic-free on dynamic input (156 tests, clippy clean) — the exit-0
contract cannot be broken by a panic in the wrapped-command path. But the blocker is bad:
`group_test_failures`' uppercase-anchored markers miss lowercase rustc/cargo errors and the
fallback **fabricates "All tests passed."** on compile failures (empirically reproduced) — with
exit-0, the LLM is told the opposite of the truth (#638). "First match wins" is actually
alphabetical (BTreeMap discards YAML order, #639), and README/SKILL.md teach the removed bare
`gsqz --` form which exits 2 (#640 — SKILL.md is served to agents).

| Finding | Sev | Category | Task | Title |
|---|---|---|---|---|
| GSQZ-01 | **blocker** | correctness | #638 | test_failures fabricates "All tests passed." on compile errors |
| GSQZ-02 | high | correctness | #639 | Pipeline matching order is alphabetical, not config order |
| GSQZ-03 | high | straggler/docs | #640 | README/SKILL.md document removed bare `gsqz --` form |
| GSQZ-04 | medium | error-handling | #641 | Malformed config makes every wrapped command exit 1 |
| GSQZ-05 | medium | correctness | #642 | Surface nonzero exit code in content |
| GSQZ-06 | medium | straggler | #643 | git_status/git_diff group modes are unreachable dead code |
| GSQZ-07 | medium | test-gap | #644 | Binary-level integration tests for exit-0 contract |
| GSQZ-08 | low | error-handling | #645 | Warn when config regexes fail to compile |
| GSQZ-09 | low | correctness | #646 | ANSI stripping misses OSC/non-CSI sequences |
| GSQZ-10 | low | consolidation | #647 | Consolidate group-by-key and head/tail scaffolding |
| GSQZ-11 | low | consolidation | #648 | Route input-mode stats through CompressionResult |
| GSQZ-12 | low | architecture | #649 | Resolve layered-docs vs first-found-wins; frozen auto-export |

### gloc — task #595

**Verdict: SOLID-WITH-ISSUES.**

Clean four-module binary; re-exports gcore's `Backend` and delegates all probe logic to
`gobby_core::local_backend` (no duplication — its own `backend.rs` is exclusively Ollama model
lifecycle). 35 tests pass, clippy clean. Issues: the documented `--backend X --url Y` escape
hatch is broken because `--url` is applied after validation (#650); the shipped codex client
defaults target the retired TS codex CLI's `--provider` flag so `gloc --client codex` fails at
launch (#653); the Ollama lifecycle HTTP paths have zero test coverage (#655); and the first-run
auto-export freezes built-in defaults forever (#656, same pattern as gsqz #649).

| Finding | Sev | Category | Task | Title |
|---|---|---|---|---|
| GLOC-01 | high | correctness | #650 | Apply --url override before backend validation |
| GLOC-02 | medium | correctness | #651 | Stream Ollama pull progress; remove 600s cap |
| GLOC-03 | low | correctness | #652 | Stop flooring probe_timeout_ms to 5s |
| GLOC-04 | medium | straggler | #653 | Update codex client defaults for Rust codex CLI |
| GLOC-05 | low | correctness | #654 | Explicit default_client instead of alphabetical-first |
| GLOC-06 | medium | test-gap | #655 | Mock-server tests for Ollama lifecycle |
| GLOC-07 | low | architecture | #656 | Rethink first-run auto-export of built-in config |
| GLOC-08 | low | error-handling | #657 | Distinguish unreadable config from missing |
| GLOC-09 | low | nitpick | #658 | Redundant match arm, hand-rolled dump, dup gcore tests |
| GLOC-10 | low | correctness | #659 | Env injection hygiene + token redaction in --status |

### ghook — task #596

**Verdict: SOLID-WITH-ISSUES.**

Well-factored small binary with deliberate enqueue-first sequencing and thoroughly golden-tested
per-CLI action mapping (82 tests, clippy clean). `.ghook-compatibility` is fully retired from
source. The seam problems: an inbox-write failure aborts dispatch without ever attempting the
daemon POST — enqueue-first leaking into the observable contract on exactly the sandboxed-FS
paths ghook exists to tolerate (#660); home-dir/daemon-URL resolution is split-brained across
three implementations (`gobby_core::gobby_home` vs `dirs::home_dir` vs local `marker_home`,
#665 + GHOOK-07 folded into #603); at-least-once delivery has no idempotency key for drain
dedupe (#661, cross-repo); and the statusline write→wait→read sequencing deadlocks on
>pipe-buffer traffic (#662). The hard per-CLI stdout/stderr/exit contract has no binary-level
test (#666).

| Finding | Sev | Category | Task | Title |
|---|---|---|---|---|
| GHOOK-01 | high | correctness | #660 | Fall back to direct daemon POST when enqueue fails |
| GHOOK-02 | medium | correctness | #661 | Envelope/idempotency ID on live POST (cross-repo) |
| GHOOK-03 | medium | correctness | #662 | Statusline concurrent stdout read (pipe deadlock) |
| GHOOK-04 | low | error-handling | #663 | EPIPE-tolerant emit_action for detached survivors |
| GHOOK-05 | low | straggler | #664 | Remove dead sdk-py branch in detect_source |
| GHOOK-06 | medium | consolidation | #665 | Consolidate Gobby-home resolution on gobby_core |
| GHOOK-07 | low | consolidation | → #603 | Statusline daemon-URL override (folded into #603) |
| GHOOK-08 | medium | test-gap | #666 | Binary-level integration tests for per-CLI contract |
| GHOOK-09 | low | consolidation | #667 | Dedupe HTTP test helper + truthiness predicate |
| GHOOK-10 | low | correctness | #668 | fsync inbox directory after envelope rename |

---

## Phase 2 — Competitor analysis

### Repo verification (2026-06-09)

| Tool | Repo | Canonical? | Stars | Last activity | Note |
|---|---|---|---|---|---|
| DeepWiki | AsyncFuncAI/deepwiki-open | yes, with caveat | 16,820 | 2026-06-03 | README gutted May 2026 to promote closed-source "Grok-Wiki 2.0" pivot; OSS FastAPI/Next.js code still in-tree and merging (LiteLLM router, Jun 3). Zero tagged releases ever; 260 open issues. Benchmark against the pre-pivot feature set (README at commit `43ed8a22`, 2026-01-12). |
| OpenDeepWiki | AIDotNet/OpenDeepWiki | yes | 3,307 | 2026-06-04 | .NET 10 + Next.js open-core platform; v2.0.3 on 2026-05-30; 20 open issues. |
| llm-wiki | Pratiyush/llm-wiki | **no** — most-popular by name is nashsu/llm_wiki (10,978★) | 295 | 2026-05-22 | Contested namespace from the Apr-2026 Karpathy "LLM Wiki" wave. **Neither is a repo-wiki generator**: Pratiyush's documents *coding-session transcripts*; nashsu's is a document-KB desktop app. Treated as a marginal comparator — see note below. |
| CodeWiki | FSoft-AI4Code/CodeWiki | yes | 1,212 | 2026-06-09 | ACL 2026 paper (arXiv 2510.24428), FPT Software AI4Code; own benchmark (CodeWikiBench). No versioned releases (pip from git). |
| Graphify | safishamsi/graphify | yes — verified legit despite explosive growth | 64,278 | 2026-06-08 (v0.8.36) | Created 2026-04-03, viral post-Karpathy; 1.2M+ PyPI downloads (`graphifyy` — double-y; other `graphify*` PyPI names are typosquats), 77 contributors, YC S26. 326 open issues. |

**llm-wiki scoping note:** the plan's given repo (Pratiyush/llm-wiki) is a session-transcript
wiki, and the canonical-by-name nashsu/llm_wiki is documents-in, not repos-in. Neither competes
on the repo-wiki dimensions directly. Both are kept in the feature inventory for the ideas worth
stealing (machine-readable exports, lint rules, confidence scoring), but the parity matrix
weighs DeepWiki, OpenDeepWiki, CodeWiki, and Graphify as the real comparators.

### Feature inventory

#### DeepWiki-Open (AsyncFuncAI, 16.8k★)
- **Pipeline:** clone → text chunking → embeddings (adalflow) → LLM writes wiki sections → Mermaid generation with auto-repair. No AST — pure RAG + LLM summarization.
- **Providers:** Gemini (default), OpenAI, OpenRouter, Azure, Bedrock, Ollama; embedders incl. any OpenAI-compatible; new LiteLLM routing. Local LLM: yes.
- **Coverage:** whole repo → LLM-decided topic pages (no per-file/module guarantee).
- **Structure/nav:** interactive Next.js wiki; section nav; 10 UI languages.
- **Diagrams:** Mermaid architecture/data-flow.
- **Citations:** not documented (RAG grounds chat answers; page→source links not advertised).
- **Incremental:** cache-only (`~/.adalflow/*`); no changed-file regeneration.
- **Search/ask:** "Ask" RAG chat (streaming, history) + DeepResearch multi-turn auto-continuing investigation (≤5 iterations).
- **Output:** web app; no static export documented.
- **Maturity risk:** single-maintainer, no releases, 260 open issues, active closed-source pivot.
- **Worth stealing:** DeepResearch loop; per-deployment provider/model picker in UI.

#### OpenDeepWiki (AIDotNet, 3.3k★)
- **Pipeline:** workspace prep (LibGit2Sharp/ZIP/local dir) → tree + repo-context analysis → LLM generates README summary, overview, wiki **catalog**, then per-document content → background workers (translation, mind maps, Graphify artifacts). No own AST; bundles `graphifyy`.
- **Providers:** any OpenAI-compatible; **separate model bindings per stage** (`WIKI_CATALOG_*`, `WIKI_CONTENT_*`, `WIKI_TRANSLATION_*`, `CHAT_*`). Local LLM: yes.
- **Coverage:** whole repo → catalog + per-document pages; multi-language wiki output.
- **Structure/nav:** public SEO routes `/{owner}/{repo}` (+ `/mindmap`, `/graphify`); admin console; share links; embeddable chat.
- **Diagrams:** Mermaid mind maps + optional Graphify knowledge-graph pages.
- **Citations:** not documented.
- **Incremental:** yes — scheduled incremental-update background workers.
- **Search/ask:** built-in chat over indexed content; **repo-scoped MCP endpoints** (`/api/mcp/{owner}/{repo}`); IM webhooks (Feishu/QQ/WeChat/Slack).
- **Output:** hosted web platform (Next.js + SQLite/PostgreSQL); not static files.
- **Worth stealing:** per-stage model binding; repo-scoped MCP endpoint per wiki; IM-channel Q&A delivery.

#### CodeWiki (FSoft-AI4Code, 1.2k★)
- **Pipeline:** static per-language analysis → dependency graph → **hierarchical decomposition** (DP-inspired clustering into a module tree, token-budgeted: `--max-token-per-module`, `--max-depth`) → recursive multi-agent LLM generation with dynamic delegation → synthesis with a **Mermaid-validating editor**. AST/dep-graph driven; no embeddings.
- **Providers:** OpenAI-compatible, Anthropic, Azure, Bedrock, plus **subscription mode** through local `claude`/`codex` CLI binaries. Keys in OS keychain.
- **Coverage:** whole repo → `overview.md` + per-module hierarchical pages; `--focus`, `--include/--exclude`, doc types (api/architecture/user-guide/developer), custom agent instructions.
- **Structure/nav:** `docs/` Markdown + `module_tree.json` + optional `index.html` interactive viewer (`--github-pages`, `--create-branch`); module pages cross-link.
- **Diagrams:** Mermaid system architecture, data-flow, sequence, dependency — validated before write.
- **Citations:** inter-page cross-links only; **no source file:line citations** observed.
- **Incremental:** `codewiki generate --update` regenerates only changed modules.
- **Search/ask:** none in output; MCP server for IDE integration.
- **Output:** Markdown + static HTML viewer.
- **Languages:** Python, Java, JS, TS, C, C++, C#, Kotlin (+PHP per its own docs).
- **Maturity:** ACL 2026 paper; CodeWikiBench (21 repos, 86K–1.4M LOC) where it beats Devin's DeepWiki +4.73% overall.
- **Worth stealing:** token-budgeted hierarchical decomposition; Mermaid validation gate; subscription-mode LLM via coding-CLI binaries; published eval methodology.

#### Graphify (safishamsi, 64.3k★)
- **Pipeline:** hybrid AST + LLM — tree-sitter (28 grammars, zero API calls for code-only corpora) + LLM semantic extraction for docs/PDFs/media; typed knowledge graph with **confidence tags** (EXTRACTED/INFERRED/AMBIGUOUS); Leiden/Louvain communities with LLM naming; ghost-duplicate merging.
- **Providers:** defaults to your IDE agent's model; headless: Anthropic, OpenAI, Gemini, DeepSeek, Moonshot, Azure, Bedrock, Ollama (fully local), claude-cli subscription mode.
- **Coverage:** whole project incl. non-code — SQL schemas, live Postgres introspection, Terraform/HCL, Apex, MCP configs, Office/Google docs, arXiv, YouTube (local faster-whisper); cross-project global graph.
- **Structure/nav:** `graph.html` (interactive force graph), `GRAPH_REPORT.md` (god nodes, surprising connections, suggested questions), `graph.json`; **`--wiki` builds a Markdown wiki from the graph**; `--obsidian` vault export.
- **Diagrams:** Mermaid architecture/call-flow page auto-regenerated on every commit via hook; SVG/GraphML/Neo4j exports.
- **Citations:** AST nodes carry source locations; confidence tags on inferred edges; inline `# WHY:`/`# HACK:` comments become graph nodes linked to code.
- **Incremental:** `--update` (changed files), `--watch`, post-commit/post-checkout hooks, git **merge driver** union-merging `graph.json`, portable team-committed graphs.
- **Search/ask:** `graphify query/path/explain` CLI; MCP stdio + team HTTP server; **PreToolUse hooks intercept grep/Read** and redirect agents to graph queries (claims 71.5x token reduction).
- **Output:** HTML + JSON + Markdown report/wiki/Obsidian.
- **Worth stealing:** query-first hook enforcement; confidence/provenance tags on inferred edges; graph as committed team artifact with union merge driver; PR triage by graph-community overlap.

#### llm-wiki (both namesakes — marginal comparators)
- **Pratiyush/llm-wiki (295★):** parses AI-coding-session transcripts (Claude Code/Codex/Cursor/Gemini CLI/Copilot) → redacted Markdown → Karpathy 3-layer wiki with `[[wikilinks]]` → stdlib-Python static site. Static HTML plus **AI-consumable siblings**: `llms.txt`, `llms-full.txt`, JSON-LD graph, per-page `.txt`/`.json`, sitemap, RSS. Cmd+K fuzzy search; 12-tool MCP server; 4-factor confidence scoring; 16 lint rules (3 LLM-powered: contradictions, claim verification, summary accuracy); SessionStart hook auto-sync; content-hash caching. Quiet since 2026-05-22.
- **nashsu/llm_wiki (11k★):** Tauri v2 desktop app; documents (PDF/DOCX/PPTX/XLSX/web clips) → self-maintaining Obsidian-compatible wiki; SHA-256 incremental cache; `sources:[]` frontmatter traceability; 4-signal knowledge graph + Louvain communities; optional LanceDB vector search; chat cites pages by number; MCP server + HTTP API. Documents-in, not repos-in.

### Cross-tool observations

- **Table stakes (3+ tools):** Mermaid diagrams; multi-provider LLM config with OpenAI-compatible escape hatch + Ollama; MCP exposure of the generated artifact; some incremental-update story (deepwiki-open is the laggard: cache-only).
- **"Ask the repo" chat/RAG is near-table-stakes** — notably absent from CodeWiki's output, the most wiki-like generator of the five.
- **Structure-aware generation is the differentiator:** only CodeWiki (dep-graph decomposition) and Graphify (tree-sitter AST) use code structure; DeepWiki/OpenDeepWiki are pure LLM-over-text. This is exactly gcode's home turf (tree-sitter + FalkorDB graph + UUID5 symbol identity).
- **Source citations to file:line are weak across the board.** Nobody reliably anchors generated wiki prose to source files/lines (Graphify's AST node locations come closest; CodeWiki only cross-links its own pages). gcode already has byte-offset symbol identity — citation-anchored prose is a genuine parity-plus differentiator.
- **Unique-to-one:** CodeWiki's published benchmark + Mermaid validation gate; Graphify's query-first agent hooks, confidence tags, graph merge driver; OpenDeepWiki's per-stage model binding + IM chatbots; Pratiyush's llms.txt/JSON-LD machine-readable exports. Subscription-mode LLM via `claude`/`codex` binaries appears in two (CodeWiki, Graphify) and is spreading.
- **Maintenance flags:** deepwiki-open mid-pivot to closed source; Pratiyush/llm-wiki quiet since May 22.

### Output inspection (cloned, 2026-06-09)

deepwiki-open (pre-pivot 43ed8a2) and FSoft CodeWiki (HEAD 972dba9) were cloned and inspected
(features/output only, no code review). Key evidence for the parity matrix:

- **Citations are theater across the field.** deepwiki-open's page prompt demands
  `Sources: [file.ext:start-end]()` but feeds the model line-number-free 350-word RAG chunks
  (chunk metadata carries only `file_path`) and never validates a citation — line references
  are structurally hallucinated. CodeWiki has no file:line citation convention at all (its
  sample `docs/*.md` contain zero `Sources:` citations); provenance exists only at pipeline
  level (component IDs, commit_id in metadata.json). Neither has post-generation grounding.
  gcode's `ground_text` (strip-invalid + repair-with-valid-span against indexed byte offsets)
  has no counterpart in any of the four tools.
- **Diagrams are drawn from memory, not data.** Both prompt the model to invent Mermaid;
  CodeWiki validates *syntax* with the real JS Mermaid parser fed back into an agent edit loop
  (the one mechanical quality gate worth copying), but neither derives edges from the
  dependency graph they computed. gcode emits Mermaid from actual FalkorDB call/import edges.
- **Incrementality:** deepwiki-open is full-regen-or-cache (stale embeddings reused without
  change detection). CodeWiki has real git-diff invalidation (changed files → modules →
  parents → overview) but fuzzy substring matching of component IDs and no per-symbol diffing.
- **Wiki-level search exists nowhere.** deepwiki's ask/Deep-Research RAG searches code
  embeddings, not the generated wiki; CodeWiki has no search at all. gwiki's hybrid
  BM25+semantic+graph over the generated vault has no counterpart.
- **What they do better:** deepwiki's editorial prose scaffolding (mandated page anatomy,
  40-line Mermaid style guide, forced source-file header) and LLM-decided topic taxonomy
  (pages read as concepts, not directory listings); CodeWiki's bottom-up hierarchical
  synthesis (leaf docs from full source, parent docs from child docs) and closed-loop Mermaid
  validation; deepwiki's multi-turn Deep-Research UX.

### Parity matrix & verdict

Our-side evidence is from the Phase 3 fresh build of this repo (1,029 core files, 75 modules,
8,913 symbols; vault wiped and rebuilt by the book). Competitor evidence is from the feature
inventory + cloned-output inspection above.

| Dimension | Best competitor showing | gcode/gwiki (Phase 3 evidence) | Verdict |
| --- | --- | --- | --- |
| Coverage | CodeWiki: module-level docs from dep-graph decomposition; deepwiki: ~dozens of LLM-chosen topic pages, no per-file coverage guarantee | Deterministic full coverage: repo.md + 75 module docs + 1,029 file docs + per-symbol tables, plus `_architecture`/`_onboarding`/`_hotspots`/`_changes`/`_ownership` section pages | **Parity-plus** — coverage is structural, not model-discretionary |
| Structure & navigation | deepwiki: LLM topic taxonomy (concept pages); CodeWiki: bottom-up hierarchy, cross-linked | Hierarchical repo→module→file with `[[wikilinks]]` (102 links, `gwiki lint`: broken links none), INDEX pages, `gwiki backlinks` over the vault | **Parity** — our navigation is denser and verifiable; their concept-level taxonomy reads better editorially (noted as future direction, no task) |
| Diagram/graph quality | CodeWiki: LLM-invented Mermaid, syntax-validated via real JS parser in an agent loop; nobody derives edges from their own graph | Mermaid dependency/call-sequence diagrams emitted from actual FalkorDB call/import edges (4,786 CALLS / 2,369 IMPORTS project-scoped), bounded per module | **Parity-plus** — data-derived vs. hallucinated; their syntax-validation loop is the one idea worth copying (#616 family) |
| AI prose quality | deepwiki: strong editorial scaffolding (mandated page anatomy, style guide) over ungrounded RAG | Sections run completed (qwen3.6-35b local, ~2h): 75/75 module overviews + 65/72 architecture subsystems with grounded prose; per-symbol purposes reuse daemon-enriched index summaries at zero codewiki-time LLM cost; 7 largest prompts degraded honestly (`degraded_sources: model-unavailable`) — root-caused to the shared 60s timeout, fixed (#680, TextGenerate now 300s) | **Parity** — grounded prose at every tier with explicit degradation beats their ungrounded editorial polish, but their page anatomy still reads better; rerun post-#680 should clear the degraded cells |
| Citations/provenance | None real: deepwiki prompts for `file:line` but feeds line-number-free chunks (structurally hallucinated); CodeWiki has no citation convention | `ground_text` strips invalid citations and repairs with valid indexed spans; provenance frontmatter with file paths + line ranges on every page; audit/credibility tracking in gwiki | **Parity-plus** — only tool with post-generation grounding against indexed byte offsets |
| Incremental updates | CodeWiki: git-diff invalidation (file→module→parent chain), fuzzy component matching; deepwiki: cache-or-full-regen | Source-hash invalidation per doc + index snapshot diffing (`_changes.md`) + AI-mode invalidation (#677); daemon watcher auto-reindexes vault output | **Parity-plus** — finer-grained than git-diff (per-source-hash), discloses truncation/degradation in frontmatter |
| Search over generated wiki | Nonexistent: deepwiki RAG searches code embeddings (not the wiki); CodeWiki ships no search | gwiki hybrid BM25 + semantic + graph-boost over the vault, verified live (zero degradations); `ask`, `research` loop, `compile` consume it | **Parity-plus** — uncontested; no competitor searches its own output |

---

## Phase 3 — Fresh wiki + codewiki, by the book

_In progress (task #611). Vault wiped and re-initialized from scratch._

Progress log (2026-06-09):

- `gwiki --project init` ✅ — scaffolds the documented tree, **plus** `knowledge/INDEX.md`,
  `code/INDEX.md`, `_meta/`, and `.gwiki/scope.json`, which the user guide's init table omits
  (doc fix queued for this task).
- `gwiki --project setup --standalone` ✅ — created gwiki tables + BM25 indexes,
  `status: created`.
- `gwiki --project status` ✅ — `datastore-ready` (PostgreSQL, FalkorDB :16379, Qdrant :6333,
  embeddings LM Studio `nomic-embed-text`).
- `gwiki --project trust` ⚠️ — on a freshly wiped vault it reported the **old** hub rows
  (17 documents) with `fresh: true`; hub state is per-scope and survives a file wipe. Honest
  once `index` prunes, but trust-on-stale-hub is misleading.
- `gwiki --project index` ❌→✅ — failed with the #612 jsonb regression (fixed directly;
  see gwiki section). After the fix, indexing succeeds and **stale-row pruning works**: old
  codewiki rows were pruned via `deleted` ingestion events (which exposed a second bug — the
  gwiki-owned `gwiki_ingestions.content_hash` NOT NULL constraint contradicted the indexer's
  `Option<String>` model; fixed in #612 too).
- Doc-gap candidate for `docs/guides/codewiki.md`: the previous real output contained
  `_architecture.md`, `_changes.md`, `_hotspots.md`, `_onboarding.md`, `_ownership.md`, and
  `_meta/ownership.json` — none documented in the guide's Output Tree. To confirm against a
  fresh run.

Progress log (2026-06-09, continued):

- `ingest-url` / `ingest-file` / `collect` ✅ — Wikipedia URL, README.md, and an inbox drop all
  captured with manifest entries; ingest auto-indexes the vault.
- `gwiki index` + hybrid `search` ✅ — but graph boost reported `gwiki_graph_unreachable`.
  Root-caused to **three stacked breaks** (fixed directly, #670): a CodeRabbit batch (2afd51f)
  added a guard rejecting leading `$secret:` references before the shared resolver (the
  FalkorDB password is stored as exactly that); another CodeRabbit batch (6757743) removed
  `escape_string` quoting from Cypher params (falkordb 0.2 interpolates `CYPHER k=v` raw text);
  and the WikiSource SUPPORTS statement ran MATCH after MERGE without WITH. After the fixes the
  wiki graph syncs fully (552 docs / 552 sources / 1185 targets) and search runs with
  **zero degradations**.
- **Wiki inception found and fixed (#671):** the walker deliberately allowlists
  `.gobby/wiki/**/*.md` into the content index, and the daemon watcher indexes codewiki output —
  so the next codewiki run documented its own previous output (observed live: AI prompts for
  `.gobby/wiki/code/files/**.rs.md`), compounding AI cost every cycle. `is_core_file` now
  excludes hidden path components.
- **Stale specials fixed (#672):** docs without provenance frontmatter (`_ownership.md`,
  `_hotspots.md`) hash to an empty source set, which always compared equal — they were never
  rewritten after generator changes. Empty hash sets no longer count as "unchanged".
- **Wikilink resolution fixed (#673):** gwiki stripped `.md` from wikilink targets, breaking
  all 102 codewiki links to markdown-source docs (`[[code/files/AGENTS.md]]` →
  `code/files/AGENTS.md.md`). Wikilinks now keep `.md` as part of the page name.
  `gwiki lint`: **Broken links: none**.
- `ask` (retrieval), `read`, `backlinks`, `link-suggest`, `lint`, `audit`, `health`,
  `refresh --dry-run` ✅ all exercised (refresh correctly reports the no-replay inbox note in
  `failed`, per the documented contract).
- New findings filed: #674 (repo.md is a 637KB landing page with per-line provenance entries
  instead of coalesced ranges), #675 (audit attributes generated code-doc claims to unrelated
  raw sources), #669 (daemon config_store rejects the ai.text_generate keys the CLIs read —
  configured via gcore.yaml + `$secret:` as the documented workaround).
- **Process note:** three of the four live-breaking bugs this phase were regressions introduced
  by CodeRabbit batch-fix commits (6a9bc97 jsonb params → #612, 2afd51f secret rejection and
  6757743 param de-quoting → #670) that "simplified" deliberate workarounds without live
  verification. CodeRabbit suggestions touching DB params, query encoding, or secret handling
  deserve a live-pipeline check before merging.

- **Research path fixed (#676, two stacked bugs):** `gwiki --project research` failed instantly
  with `invalid_scope` — `ResearchScope` stores the vault root for checkpoints, but the
  selection round-trip passed it back as a `--project` root (looking for project identity
  *inside* the vault). After that fix, every direct text call returned HTTP 401 —
  `research_ai_config_source` was local-only (gcore.yaml, no hub primary) so the canonical
  `$secret:` api_key could never resolve. Research now layers a hub-backed primary like
  search/index. Live: model loop executes (steps_used=2, degradation=null, structured
  stop_reason).

- **AI cost model fixed (#677, two coupled defects):** the first AI codewiki run issued one
  LLM call per symbol (7,891 on this repo) plus one per file — at the observed local pace
  (2.5 generations/min through qwen3.6-35b, a reasoning model) a full run projected to >2 days;
  killed after 7h17m/~1,092 calls. Worse, it would have written **nothing**: incremental writes
  compared only source hashes, so enabling AI after a structural run marked every provenance doc
  "unchanged". Fix: `--ai-depth <sections|files|symbols>` (default `files`) gates the per-symbol
  and per-file prompts behind opt-in tiers with the existing structural fallbacks, and
  `_meta/codewiki.json` now records the run's AI mode — a mode change invalidates all docs.
  Competitor context: every comparator generates page-level prose only; per-symbol prose is a
  parity-plus tier that must stay opt-in.
- **Operational note:** parking large analysis artifacts (4.5MB `graph.json`) inside the watched
  vault made the daemon sync worker time out on `gcode graph sync-file` for that file repeatedly;
  moved out of the vault. Filed as a finding on large content-only file sync behavior.

Progress log (2026-06-10) — sections AI run completed, e2e battery run, four bugs fixed:

- **Sections AI run completed** (~2h, 514 pages): 75/75 module overviews and 65/72 architecture
  subsystems carry grounded AI prose with repaired citations; per-symbol purposes come free from
  daemon-enriched index summaries (`structural_symbol_purpose` prefers `symbol.summary`), so the
  "structural fallback" at sections depth is already AI-quality. Zero FalkorDB warnings (#679
  validated live). The 7 largest prompts (repo overview, top-level crate subsystems) degraded
  honestly with `degraded: true` / `model-unavailable` frontmatter.
- **Timeout split (#680):** the degraded cells root-caused to the shared 60s
  `TEXT_VISION_TIMEOUT` — ~11k-token prompts at ~58 t/s decode cannot finish in 60s on a local
  reasoning model. `TextGenerate` now gets 300s; vision keeps 60s.
- **`gwiki index`:** 517 documents / 2,190 chunks / 2,939 links; `gwiki health` clean (no broken
  links, no stale citations).
- **e2e search ✅:** hybrid BM25+semantic hits over codewiki pages, zero degradations.
- **e2e ask ✅ after two fixes:** `ask --llm` 401'd because ask/citation-quality built AI config
  from the local-only source that refuses `$secret:` api_keys — promoted research's hub-backed
  primary to shared `support::config::hub_ai_config_source` (#683). Graph context always reported
  `shared_code_graph_unavailable` because FalkorDB rejects `LIMIT toInteger($limit)` — invisible
  for months since gwiki never initializes a logger (#685 filed); fixed to `LIMIT $limit` (#684).
  Now: `ask --llm --ai direct --require-ai` answers with grounded citations and 969 real call
  edges in context, sole remaining flag the honest `shared_code_graph_truncated`.
- **e2e research ◐:** loop machinery verified (search/read/cite steps, budget enforcement,
  structured stop reasons, degradation warnings) but the local reasoning model appends prose
  after its action JSON, so note acceptance stalls (`model_response_invalid: trailing
  characters`) — lenient-parse task filed (#686).
- **e2e compile ✅ (mechanically):** wrote `knowledge/topics/...md` with frontmatter, manifest
  citations, conflict/missing-evidence sections; content empty pending accepted notes (#686).

### Verdict — parity-plus, confirmed

Across the seven dimensions: five **parity-plus** (coverage, diagrams-from-real-edges,
citations/provenance, incremental invalidation, search-over-own-wiki — the last two uncontested,
no competitor has them at all), two **parity** (structure/navigation, AI prose). Nothing scores
below parity. The two parity rows share one cause: deepwiki's editorial scaffolding (mandated
page anatomy, concept-level taxonomy) produces nicer-reading pages than our schema-shaped ones.
That is prompt/template work, not architecture — our grounding, coverage, and freshness
guarantees are the hard part and are already ahead. Highest-leverage follow-ups, in order:
regeneration reuse for unchanged docs (#681 — re-runs currently re-pay the full LLM cost),
lenient action-JSON parsing so local models can complete research→compile (#686), degraded-doc
healing (#687 — source-hash skip means a degraded page survives re-runs unless deleted first;
the post-#680 healing rerun uses the delete-first workaround), and editorial page-anatomy
polish (documented as direction, no stack change).
