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
| 1 | gobby-code review (#592) | ⬜ |
| 1 | gobby-wiki review (#593) | ⬜ |
| 1 | gsqz review (#594) | ⬜ |
| 1 | gloc review (#595) | ⬜ |
| 1 | ghook review (#596) | ⬜ |
| 2 | Competitor verification & feature inventory | ✅ |
| 2 | Parity matrix + per-dimension verdict | ⬜ |
| 3 | Fresh wiki + codewiki by the book | ⬜ |

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

_Pending (blocked on #591 — now unblocked)._

### gobby-wiki (gwiki) — task #593

_Pending._

### gsqz — task #594 · gloc — task #595 · ghook — task #596

_Pending._

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

### Parity matrix & verdict

_Pending — produced after Phase 3 (fresh wiki + codewiki build) so our side of each dimension is
evidence-backed, not spec-backed._

---

## Phase 3 — Fresh wiki + codewiki, by the book

_Pending._
