# gwiki - Rust port of llm-wiki on Gobby's data stack

**Plan ID:** gwiki

## O1: Overview
`kind: framing`

Port the useful shape of [nvk/llm-wiki](https://github.com/nvk/llm-wiki) into a Rust crate named `gobby-wiki` with binary `gwiki`. The user experience stays file-first and Obsidian-compatible: topic vaults, `[[wikilinks]]`, immutable `raw/` sources, synthesized `wiki/` articles, `_index.md`, `log.md`, and agent-assisted research/compile/audit workflows.

The implementation should not copy the gcode indexing pipeline. Shared context/config resolution, setup contracts, datastore adapters, generic indexing/search primitives, and degradation vocabulary come from `.gobby/plans/gcore-rust-foundation.md`. `gobby-wiki` owns wiki-specific behavior: vault layout, scope resolution, markdown/frontmatter/link parsing, source manifests, ingestion, research dispatch, synthesis, audit, and command UX.

Filesystem markdown is the source of truth. PostgreSQL, FalkorDB, and Qdrant hold derived `gwiki` indexes that can be wiped and rebuilt from the vault.

## C1: Constraints
`kind: framing`

- **Foundation dependency**: `gobby-wiki` consumes `gobby-core` primitives for context/config, setup, PostgreSQL, FalkorDB, Qdrant, generic indexing/search, and degradation handling.
- **Workspace integration**: the crate lives at `crates/gwiki/`, has `package.name = "gobby-wiki"`, and exposes binary `gwiki`.
- **Dual scopes**: global topics and project-local wiki scopes both work. Global topics default under `~/wiki/topics/<topic>/`; project scope defaults under `<project-root>/.gobby/wiki/`.
- **Vault UX**: each scope preserves llm-wiki-style `raw/`, `wiki/`, `inbox/`, `_index.md`, `log.md`, frontmatter, and `[[wikilinks]]`.
- **Filesystem source of truth**: `gwiki` writes user-facing markdown through explicit vault operations. Index rows, graph nodes, and vectors are derived state.
- **Namespaced data**: PostgreSQL tables use `gwiki_*`; FalkorDB labels use wiki-owned labels such as `WikiDoc`, `WikiSource`, and `WikiTopic`; Qdrant collections use `gwiki:project:<id>` and `gwiki:topic:<name>`.
- **No daemon schema ownership assumption**: the Gobby daemon does not own `gwiki` schema. `gwiki setup` may create only `gwiki`-owned resources after explicit opt-in; runtime commands validate prerequisites and never create schema implicitly.
- **No gcode ownership leakage**: `gwiki` must not create or mutate gcode tables, gcode graph labels, code symbols, `.gobby/project.json`, or `config_store`.
- **Daemon services are integrations**: LLM completions, embeddings, vision, transcription, and agent dispatch use configured Gobby daemon endpoints when available. Missing optional services degrade honestly.

## D1: Storage Model
`kind: framing`

Global topic scope:

- Default root: `~/wiki/topics/<topic>/`.
- Registry: `~/wiki/wikis.json`.
- Shared global log: `~/wiki/log.md`.
- Use case: durable personal or team knowledge not tied to one code project.

Project scope:

- Default root: `<project-root>/.gobby/wiki/`.
- Registry: `<project-root>/.gobby/wiki/wikis.json`.
- Scope log: `<project-root>/.gobby/wiki/log.md`.
- Use case: project-local research, decisions, source notes, and compiled wiki pages.

Both scopes use the same vault shape and data model. Scope identity is explicit in every index row, graph node, vector payload, and command result so cross-scope leakage can be tested.

## R1: Roadmap
`kind: framing`

| Version | Focus | Owner Boundary |
|---|---|---|
| v0.1 | crate, scope/vault model, setup, markdown indexing, BM25, core CLI | `gobby-wiki` domain on `gobby-core` primitives |
| v0.2 | Qdrant semantic search, FalkorDB backlinks, RRF fusion | shared adapters, wiki-owned payloads |
| v0.3 | research dispatch, sessions, source manifest, credibility, compile handoff | daemon endpoints, wiki workflow state |
| v0.4 | URL, PDF, local file, stdin, and inbox collect ingestion | wiki source capture |
| v0.5 | compile, audit, lint, output formats, bundled skills | wiki synthesis and QA |
| v0.6 | MediaWiki, Wayback, and Git repository ingestion | external corpus connectors |
| v0.7 | image and audio ingestion via vision/transcription services | multimodal source capture |
| v0.8 | video frame/audio extraction and transcript alignment | multimodal synthesis |

## P1: Foundation And Vault Model
`kind: framing`

**Goal**: create the `gobby-wiki` crate and define the wiki domain model on top of the shared Rust foundation.

### 1.1 Add workspace crate and CLI shell [category: code]
`kind: deliverable`

Targets: `Cargo.toml`, `crates/gwiki/Cargo.toml`, `crates/gwiki/src/main.rs`, `crates/gwiki/src/lib.rs`

Add `crates/gwiki/` to the workspace with package name `gobby-wiki` and binary `gwiki`. The CLI should start with thin command parsing and call library modules for behavior. Initial commands can return structured "not yet implemented" errors for subcommands whose domain modules are not ready, but the binary must build under the workspace no-default-features profile.

`gobby-wiki` depends on `gobby-core` for shared project/context/config/setup primitives. It should not depend on `gobby-code`.

**Acceptance:**

- 1.1.1 - Workspace includes `crates/gwiki` without changing existing package names. file: `Cargo.toml`.
- 1.1.2 - `gobby-wiki` crate and `gwiki` binary build under no-default-features. file: `crates/gwiki/Cargo.toml`.
- 1.1.3 - CLI parsing is thin and delegates to library entry points. file: `crates/gwiki/src/main.rs`.
- 1.1.4 - `gobby-wiki` depends on `gobby-core`, not `gobby-code`. test: `crates/gwiki/src/lib.rs::tests::crate_has_no_gcode_dependency`.

### 1.2 Implement scope and vault resolution [category: code] (depends: 1.1)
`kind: deliverable`

Targets: `crates/gwiki/src/scope.rs`, `crates/gwiki/src/vault.rs`, `crates/gwiki/src/registry.rs`, `_index.md`, `log.md`

Implement explicit scope resolution for global topics and project-local wikis:

- `--topic <name>` resolves to a global topic under the configured wiki hub path, defaulting to `~/wiki/topics/<name>/`.
- `--project` or project-root context resolves to `<project-root>/.gobby/wiki/`.
- Both scopes create or validate `raw/`, `wiki/`, `inbox/`, `_index.md`, `log.md`, and `.gwiki/` metadata on explicit init.
- `wikis.json` stores registered topics/scopes without clobbering existing entries.
- Scope identity is carried in command context, datastore rows, graph nodes, and vector payloads.

**Acceptance:**

- 1.2.1 - Global topic resolution honors configured hub path and `--topic`. test: `crates/gwiki/src/scope.rs::tests::resolves_global_topic`.
- 1.2.2 - Project scope resolves under `<project-root>/.gobby/wiki/` without writing `.gobby/project.json`. test: `crates/gwiki/src/scope.rs::tests::resolves_project_scope_read_only`.
- 1.2.3 - `gwiki init` creates the llm-wiki vault shape for both scopes. test: `crates/gwiki/tests/cli_init.rs::init_creates_vault_shape`.
- 1.2.4 - `wikis.json` registration preserves existing topics and project entries. test: `crates/gwiki/src/registry.rs::tests::register_preserves_existing_entries`.

### 1.3 Define gwiki-owned setup and datastore schema [category: code] (depends: 1.2)
`kind: deliverable`

Targets: `crates/gwiki/src/setup.rs`, `crates/gwiki/src/schema.rs`, `crates/gwiki/src/models.rs`

Define `gwiki`-owned derived storage through `gobby-core` setup contracts:

- Runtime commands validate required `gwiki_*` tables and indexes without implicit creation.
- `gwiki setup` is an explicit opt-in operation that may create only `gwiki`-owned PostgreSQL tables and indexes.
- PostgreSQL rows include scope, project/topic identity, path, source kind, content hash, frontmatter, and provenance.
- FalkorDB nodes use wiki-owned labels such as `WikiDoc`, `WikiSource`, and `WikiTopic`.
- Qdrant collection names are namespaced as `gwiki:project:<id>` and `gwiki:topic:<name>`.

The daemon is not the schema owner. No task in this plan edits a daemon schema file to add `gwiki` tables.

**Acceptance:**

- 1.3.1 - Runtime schema validation is read-only and reports setup guidance when `gwiki_*` objects are missing. test: `crates/gwiki/src/schema.rs::tests::missing_schema_requires_explicit_setup`.
- 1.3.2 - `gwiki setup` creates only `gwiki_*` PostgreSQL objects. test: `crates/gwiki/src/setup.rs::tests::setup_creates_only_gwiki_owned_objects`.
- 1.3.3 - Graph labels and vector collection names are wiki-namespaced. test: `crates/gwiki/src/models.rs::tests::derived_storage_names_are_namespaced`.
- 1.3.4 - No daemon schema source file is part of the gwiki setup contract. behavior: "gwiki setup is owned by `crates/gwiki/src/setup.rs`" in `crates/gwiki/src/setup.rs`.

### 1.4 Implement markdown domain parsing [category: code] (depends: 1.3)
`kind: deliverable`

Targets: `crates/gwiki/src/markdown.rs`, `crates/gwiki/src/frontmatter.rs`, `crates/gwiki/src/links.rs`

Implement wiki-specific parsing:

- Parse YAML/TOML frontmatter into typed metadata while preserving unknown keys.
- Extract headings and byte ranges for chunk context.
- Extract `[[wikilinks]]`, aliases, markdown links, and unresolved targets.
- Normalize wiki paths without rewriting user-facing markdown.
- Produce domain records consumed by the index writer.

Generic walking, hashing, chunk records, and index event vocabulary should come from `gobby-core`; markdown semantics stay here.

**Acceptance:**

- 1.4.1 - Frontmatter parser preserves unknown keys and exposes known metadata. test: `crates/gwiki/src/frontmatter.rs::tests::preserves_unknown_frontmatter`.
- 1.4.2 - Markdown parser emits heading-aware byte ranges. test: `crates/gwiki/src/markdown.rs::tests::extracts_heading_ranges`.
- 1.4.3 - Link parser extracts wikilinks, aliases, markdown links, and unresolved targets. test: `crates/gwiki/src/links.rs::tests::extracts_all_link_shapes`.
- 1.4.4 - Parser does not rewrite vault markdown during indexing. test: `crates/gwiki/src/markdown.rs::tests::index_parse_is_read_only`.

## P2: Indexing And Search
`kind: framing`

**Goal**: build derived indexes and query surfaces while keeping search mechanics shared and wiki semantics local.

### 2.1 Implement wiki index writer [category: code] (depends: P1)
`kind: deliverable`

Targets: `crates/gwiki/src/indexer.rs`, `crates/gwiki/src/store.rs`

Use `gobby-core` indexing primitives to discover markdown/source files, hash content, produce index events, and write derived `gwiki` records:

- Upsert documents, chunks, links, sources, and ingestion records.
- Delete stale derived rows when vault files are removed.
- Preserve immutable `raw/` sources and user-authored `wiki/` pages.
- Track source file hashes for incremental indexing.

**Acceptance:**

- 2.1.1 - Index writer upserts documents, chunks, links, sources, and ingestions. file: `crates/gwiki/src/indexer.rs`.
- 2.1.2 - Deleted vault files remove only derived index rows. test: `crates/gwiki/src/indexer.rs::tests::deleted_file_removes_derived_rows_only`.
- 2.1.3 - Raw sources are never rewritten by indexing. test: `crates/gwiki/src/indexer.rs::tests::raw_sources_are_immutable`.
- 2.1.4 - Incremental indexing uses content hashes from `gobby-core`. test: `crates/gwiki/src/indexer.rs::tests::unchanged_files_are_skipped`.

### 2.2 Add BM25 and semantic search [category: code] (depends: 2.1)
`kind: deliverable`

Targets: `crates/gwiki/src/search/bm25.rs`, `crates/gwiki/src/search/semantic.rs`, `crates/gwiki/src/search/mod.rs`

Implement search over wiki documents and chunks:

- BM25 queries target `gwiki` document/chunk tables using PostgreSQL `pg_search`.
- Semantic search uses `gobby-core` Qdrant and embedding config adapters with wiki-owned payload filters.
- Queries are scoped to the selected topic or project.
- Missing embeddings/Qdrant degrade to BM25-only results with structured degradation metadata.

**Acceptance:**

- 2.2.1 - BM25 search returns scoped wiki chunk/document hits. test: `crates/gwiki/src/search/bm25.rs::tests::bm25_is_scope_filtered`.
- 2.2.2 - Semantic search uses wiki collection names and payload filters. test: `crates/gwiki/src/search/semantic.rs::tests::semantic_search_is_scope_filtered`.
- 2.2.3 - Missing vector services degrade to BM25-only search without fake semantic hits. test: `crates/gwiki/src/search/mod.rs::tests::semantic_unavailable_degrades`.
- 2.2.4 - Search result structs include provenance and source path. file: `crates/gwiki/src/search/mod.rs`.

### 2.3 Add wiki graph, backlinks, and fusion [category: code] (depends: 2.2)
`kind: deliverable`

Targets: `crates/gwiki/src/graph.rs`, `crates/gwiki/src/search/rrf.rs`, `crates/gwiki/src/search/graph_boost.rs`

Write and query wiki graph facts:

- `(:WikiDoc)-[:WIKI_LINKS_TO]->(:WikiDoc)` for resolved links.
- `(:WikiDoc)-[:MENTIONS_TARGET]->(:WikiTarget)` for unresolved targets.
- `(:WikiSource)-[:SUPPORTS]->(:WikiDoc)` for source provenance.
- Backlinks and link suggestions are scope-filtered.
- RRF fusion combines BM25, semantic, and graph relevance through `gobby-core` search primitives.

**Acceptance:**

- 2.3.1 - Link graph writes use only wiki-owned labels and relations. test: `crates/gwiki/src/graph.rs::tests::graph_labels_are_wiki_owned`.
- 2.3.2 - Backlinks return only same-scope wiki documents. test: `crates/gwiki/src/graph.rs::tests::backlinks_are_scope_filtered`.
- 2.3.3 - Link suggestions rank unresolved targets without mutating markdown. test: `crates/gwiki/src/graph.rs::tests::link_suggest_is_read_only`.
- 2.3.4 - RRF fusion records source explanations and degradation metadata. test: `crates/gwiki/src/search/rrf.rs::tests::fusion_preserves_sources`.

### 2.4 Add core CLI surfaces [category: code] (depends: 2.3)
`kind: deliverable`

Targets: `crates/gwiki/src/main.rs`, `crates/gwiki/src/commands/init.rs`, `crates/gwiki/src/commands/index.rs`, `crates/gwiki/src/commands/search.rs`, `crates/gwiki/src/commands/backlinks.rs`, `crates/gwiki/src/commands/status.rs`

Expose the v0.1/v0.2 command surface:

- `gwiki init`
- `gwiki setup`
- `gwiki index`
- `gwiki ingest-file`
- `gwiki search`
- `gwiki backlinks`
- `gwiki link-suggest`
- `gwiki status`

Commands use global output formatting conventions, return structured JSON for machine use, and text output for humans. Status messages go to stderr.

**Acceptance:**

- 2.4.1 - Core commands parse with shared scope flags. test: `crates/gwiki/tests/cli_parse.rs::core_commands_parse_scope_flags`.
- 2.4.2 - JSON output is structured and includes scope identity. test: `crates/gwiki/tests/cli_search.rs::search_json_includes_scope`.
- 2.4.3 - Text output is rendered through command output helpers, not raw debug prints. test: `crates/gwiki/tests/cli_output.rs::text_output_uses_renderer`.
- 2.4.4 - Status messages use stderr and command results use stdout. test: `crates/gwiki/tests/cli_output.rs::status_goes_to_stderr`.

## P3: Research Dispatch And Source State
`kind: framing`

**Goal**: preserve llm-wiki's agent-driven research workflow while routing orchestration through Gobby daemon endpoints and durable wiki state.

### 3.1 Verify daemon service endpoints [category: docs] (depends: P2)
`kind: deliverable`

Targets: `docs/guides/gwiki-development-guide.md`, `crates/gwiki/src/daemon.rs`

Document and probe the daemon endpoints `gwiki` needs:

- embeddings
- completions or synthesis
- vision
- transcription
- agent dispatch
- session/event stream monitoring

The command layer should surface unavailable optional capabilities as structured degradation. Endpoint shapes must be verified before implementation code assumes request or response schemas.

**Acceptance:**

- 3.1.1 - Development guide records verified endpoint paths, request shapes, response shapes, and fallback behavior. file: `docs/guides/gwiki-development-guide.md`.
- 3.1.2 - Daemon capability probe returns structured availability flags. file: `crates/gwiki/src/daemon.rs`.
- 3.1.3 - Missing optional endpoints produce degradation metadata. test: `crates/gwiki/src/daemon.rs::tests::missing_optional_endpoint_degrades`.
- 3.1.4 - Agent dispatch is treated as daemon integration, not internal subprocess management. file: `docs/guides/gwiki-development-guide.md`.

### 3.2 Implement research sessions and agent dispatch [category: code] (depends: 3.1)
`kind: deliverable`

Targets: `crates/gwiki/src/research.rs`, `crates/gwiki/src/session.rs`, `crates/gwiki/src/events.rs`

Implement `gwiki research` around durable wiki session state:

- Record research question, scope, source constraints, agent count, and dispatch metadata.
- Dispatch research workers through the Gobby daemon.
- Monitor session events and write progress to `.gwiki/session-events.jsonl`.
- Support checkpoint and `--resume`.
- Keep accepted research notes under `raw/research/` until compile.

**Acceptance:**

- 3.2.1 - Research session state records scope, prompt, agent count, and daemon dispatch id. file: `crates/gwiki/src/session.rs`.
- 3.2.2 - Event monitor appends durable JSONL events. test: `crates/gwiki/src/events.rs::tests::events_append_jsonl`.
- 3.2.3 - `--resume` reloads checkpointed research state. test: `crates/gwiki/src/research.rs::tests::resume_reloads_checkpoint`.
- 3.2.4 - Accepted research notes land under `raw/research/` and are indexable. test: `crates/gwiki/src/research.rs::tests::accepted_notes_land_in_raw_research`.

### 3.3 Add source manifest, dedupe, and credibility [category: code] (depends: 3.2)
`kind: deliverable`

Targets: `crates/gwiki/src/sources.rs`, `crates/gwiki/src/credibility.rs`, `crates/gwiki/src/provenance.rs`

Track source provenance independent of compiled articles:

- Source manifest entries include URL/path, source kind, fetched timestamp, hash, license/citation fields, and ingestion method.
- Dedupe sources by canonical URL/path plus content hash.
- Credibility scoring records source type, freshness, author/publisher metadata, and corroboration signals.
- Provenance links connect source chunks to synthesized wiki sections.

**Acceptance:**

- 3.3.1 - Source manifest records citation, hash, kind, and ingestion metadata. file: `crates/gwiki/src/sources.rs`.
- 3.3.2 - Duplicate source ingestion reuses the existing source record. test: `crates/gwiki/src/sources.rs::tests::dedupes_by_canonical_identity_and_hash`.
- 3.3.3 - Credibility scoring stores explainable signals. test: `crates/gwiki/src/credibility.rs::tests::credibility_score_has_explanation`.
- 3.3.4 - Provenance links connect source chunks to compiled wiki sections. test: `crates/gwiki/src/provenance.rs::tests::links_sources_to_sections`.

### 3.4 Add compile handoff state [category: code] (depends: 3.3)
`kind: deliverable`

Targets: `crates/gwiki/src/compile.rs`, `crates/gwiki/src/session.rs`

Prepare research output for synthesis:

- Select accepted raw notes and source chunks.
- Build a compile bundle with topic outline, citations, conflicting claims, and missing evidence.
- Record compile state so synthesis can resume or be audited.
- Do not overwrite existing wiki pages without explicit write intent.

**Acceptance:**

- 3.4.1 - Compile bundle includes outline, accepted sources, citations, conflicts, and gaps. test: `crates/gwiki/src/compile.rs::tests::compile_bundle_contains_required_sections`.
- 3.4.2 - Compile state is durable and resumable. test: `crates/gwiki/src/session.rs::tests::compile_state_is_resumable`.
- 3.4.3 - Existing wiki pages are not overwritten without explicit write intent. test: `crates/gwiki/src/compile.rs::tests::compile_handoff_is_non_destructive_by_default`.
- 3.4.4 - Compile bundles remain scope-filtered. test: `crates/gwiki/src/compile.rs::tests::compile_bundle_is_scope_filtered`.

## P4: Ingestion Roadmap
`kind: framing`

**Goal**: capture external material into immutable `raw/` sources and index it with provenance.

### 4.1 Add URL, PDF, local file, and stdin ingestion [category: code] (depends: P3)
`kind: deliverable`

Targets: `crates/gwiki/src/ingest/url.rs`, `crates/gwiki/src/ingest/pdf.rs`, `crates/gwiki/src/ingest/file.rs`, `crates/gwiki/src/ingest/mod.rs`

Implement v0.4 ingestion:

- URL to markdown with canonical URL, fetch timestamp, title, and source hash.
- PDF to markdown/text with page provenance.
- Local file and stdin ingestion with source kind detection.
- Every ingest writes immutable raw material plus manifest metadata, then triggers indexing.

**Acceptance:**

- 4.1.1 - URL ingest writes raw markdown and source manifest metadata. test: `crates/gwiki/src/ingest/url.rs::tests::url_ingest_writes_raw_and_manifest`.
- 4.1.2 - PDF ingest preserves page provenance. test: `crates/gwiki/src/ingest/pdf.rs::tests::pdf_ingest_preserves_page_refs`.
- 4.1.3 - Local file and stdin ingest detect source kind and hash content. test: `crates/gwiki/src/ingest/file.rs::tests::file_and_stdin_ingest_hash_sources`.
- 4.1.4 - Ingestion triggers indexing without rewriting existing wiki pages. test: `crates/gwiki/src/ingest/mod.rs::tests::ingest_indexes_raw_without_wiki_rewrite`.

### 4.2 Add inbox collect workflow [category: code] (depends: 4.1)
`kind: deliverable`

Targets: `crates/gwiki/src/collect.rs`, `crates/gwiki/src/commands/collect.rs`

Implement `gwiki collect` for bulk inbox processing:

- Scan `inbox/` for dropped URLs, PDFs, markdown, text, and local files.
- Move accepted raw material into structured `raw/` paths.
- Leave rejected or ambiguous items in `inbox/` with clear status.
- Append scope `log.md` entries for every action.

**Acceptance:**

- 4.2.1 - Collect scans inbox and routes known source kinds to raw storage. test: `crates/gwiki/src/collect.rs::tests::collect_routes_known_items`.
- 4.2.2 - Ambiguous items remain in inbox with status metadata. test: `crates/gwiki/src/collect.rs::tests::ambiguous_items_remain_in_inbox`.
- 4.2.3 - Collect appends log entries for accepted and skipped items. test: `crates/gwiki/src/collect.rs::tests::collect_logs_actions`.
- 4.2.4 - CLI exposes `gwiki collect` with scope flags. test: `crates/gwiki/tests/cli_collect.rs::collect_parses_scope_flags`.

### 4.3 Add external corpus connectors [category: code] (depends: 4.2)
`kind: deliverable`

Targets: `crates/gwiki/src/ingest/mediawiki.rs`, `crates/gwiki/src/ingest/wayback.rs`, `crates/gwiki/src/ingest/git.rs`

Implement v0.6 connectors:

- MediaWiki page/category export with revision metadata.
- Wayback capture fetch with original URL and capture timestamp.
- Git repository ingestion that captures selected files, commit SHA, remote URL, and path provenance.
- All connectors write raw sources first, then derived indexes.

**Acceptance:**

- 4.3.1 - MediaWiki ingest records page title, revision, and source URL. test: `crates/gwiki/src/ingest/mediawiki.rs::tests::mediawiki_records_revision_metadata`.
- 4.3.2 - Wayback ingest records original URL and capture timestamp. test: `crates/gwiki/src/ingest/wayback.rs::tests::wayback_records_capture_metadata`.
- 4.3.3 - Git ingest records remote, commit SHA, and file path provenance. test: `crates/gwiki/src/ingest/git.rs::tests::git_ingest_records_commit_provenance`.
- 4.3.4 - External connectors preserve raw-before-index ordering. test: `crates/gwiki/src/ingest/mod.rs::tests::external_connectors_write_raw_first`.

## P5: Compile, Audit, Lint, And Output
`kind: framing`

**Goal**: turn raw research into maintained wiki pages with provenance and quality checks.

### 5.1 Implement compile to wiki articles [category: code] (depends: P4)
`kind: deliverable`

Targets: `crates/gwiki/src/compile.rs`, `crates/gwiki/src/synthesis.rs`, `crates/gwiki/src/citations.rs`, `_index.md`

Implement `gwiki compile`:

- Build prompts from compile bundles and daemon completion endpoint availability.
- Generate or update `wiki/` markdown with frontmatter, citations, backlinks, and `_index.md` updates.
- Preserve existing user edits by requiring merge/diff handling before overwrite.
- Write source-to-section provenance for audit.

**Acceptance:**

- 5.1.1 - Compile writes Obsidian-compatible wiki markdown with frontmatter and wikilinks. test: `crates/gwiki/src/compile.rs::tests::compile_writes_obsidian_markdown`.
- 5.1.2 - Citations are rendered from source manifest metadata. test: `crates/gwiki/src/citations.rs::tests::renders_source_citations`.
- 5.1.3 - Existing pages require merge/diff handling before overwrite. test: `crates/gwiki/src/synthesis.rs::tests::existing_page_requires_merge_intent`.
- 5.1.4 - Compile updates `_index.md` without removing unrelated entries. test: `crates/gwiki/src/compile.rs::tests::index_update_preserves_unrelated_entries`.

### 5.2 Implement audit and lint [category: code] (depends: 5.1)
`kind: deliverable`

Targets: `crates/gwiki/src/audit.rs`, `crates/gwiki/src/lint.rs`

Implement `gwiki audit` and `gwiki lint`:

- Verify claims have source support.
- Detect stale citations, orphan pages, broken wikilinks, duplicate aliases, and missing frontmatter.
- Check dual-linking expectations between related pages.
- Produce JSON and text reports with actionable paths.

**Acceptance:**

- 5.2.1 - Audit reports unsupported claims with source context. test: `crates/gwiki/src/audit.rs::tests::reports_unsupported_claims`.
- 5.2.2 - Lint detects broken wikilinks and orphan pages. test: `crates/gwiki/src/lint.rs::tests::detects_broken_links_and_orphans`.
- 5.2.3 - Reports include actionable file paths and scope identity. test: `crates/gwiki/src/audit.rs::tests::reports_include_paths_and_scope`.
- 5.2.4 - Audit and lint are read-only unless an explicit fix command is added later. test: `crates/gwiki/src/lint.rs::tests::lint_is_read_only`.

### 5.3 Package skills, logs, and output formats [category: code] (depends: 5.2)
`kind: deliverable`

Targets: `crates/gwiki/src/output.rs`, `crates/gwiki/src/log.rs`, `crates/gwiki/assets/skills/`

Package the user-facing workflow:

- Bundled prompt/skill assets for research, compile, query, and audit.
- `log.md` append helpers for scope logs and global hub logs.
- JSON/text output structs for commands.
- Query output that cites source paths and wiki pages.

**Acceptance:**

- 5.3.1 - Bundled workflow assets are packaged under `crates/gwiki/assets/skills/`. file: `crates/gwiki/assets/skills/`.
- 5.3.2 - Log helper can write scope log and optional global log. test: `crates/gwiki/src/log.rs::tests::writes_scope_and_global_logs`.
- 5.3.3 - Output structs serialize stable JSON for search/query/audit. test: `crates/gwiki/src/output.rs::tests::json_output_is_stable`.
- 5.3.4 - Query output cites source paths and wiki pages. test: `crates/gwiki/src/output.rs::tests::query_output_includes_citations`.

## P6: Multimodal Ingestion
`kind: framing`

**Goal**: extend ingestion to images, audio, and video while keeping raw assets immutable and derived text rebuildable.

### 6.1 Add image ingestion and vision extraction [category: code] (depends: P5)
`kind: deliverable`

Targets: `crates/gwiki/src/ingest/image.rs`, `crates/gwiki/src/vision.rs`

Implement v0.7 image ingestion:

- Store original images under `raw/media/`.
- Call configured vision endpoint when available.
- Store extracted descriptions, OCR text, metadata, and source references as derived markdown.
- Degrade clearly when vision is unavailable.

**Acceptance:**

- 6.1.1 - Image ingest stores original files immutably under raw media. test: `crates/gwiki/src/ingest/image.rs::tests::stores_original_image`.
- 6.1.2 - Vision extraction writes derived markdown with source references. test: `crates/gwiki/src/vision.rs::tests::vision_writes_derived_markdown`.
- 6.1.3 - Missing vision endpoint degrades without dropping the raw asset. test: `crates/gwiki/src/vision.rs::tests::missing_vision_degrades`.
- 6.1.4 - Image metadata is indexed with scope identity. test: `crates/gwiki/src/ingest/image.rs::tests::image_metadata_is_scope_indexed`.

### 6.2 Add audio ingestion and transcription [category: code] (depends: 6.1)
`kind: deliverable`

Targets: `crates/gwiki/src/ingest/audio.rs`, `crates/gwiki/src/transcribe.rs`

Implement v0.7 audio ingestion:

- Store original audio under `raw/media/`.
- Call configured transcription endpoint when available.
- Store transcripts with timestamps and source references.
- Index transcripts as derived raw material for search and compile.

**Acceptance:**

- 6.2.1 - Audio ingest stores original files immutably under raw media. test: `crates/gwiki/src/ingest/audio.rs::tests::stores_original_audio`.
- 6.2.2 - Transcription writes timestamped transcript markdown. test: `crates/gwiki/src/transcribe.rs::tests::writes_timestamped_transcript`.
- 6.2.3 - Missing transcription endpoint degrades without dropping the raw asset. test: `crates/gwiki/src/transcribe.rs::tests::missing_transcription_degrades`.
- 6.2.4 - Transcript chunks are searchable in the same scope. test: `crates/gwiki/src/ingest/audio.rs::tests::transcript_chunks_are_scope_searchable`.

### 6.3 Add video ingestion and alignment [category: code] (depends: 6.2)
`kind: deliverable`

Targets: `crates/gwiki/src/ingest/video.rs`, `crates/gwiki/src/video.rs`

Implement v0.8 video ingestion:

- Store original video under `raw/media/`.
- Sample frames for image/vision extraction.
- Split or reference audio for transcription.
- Align frame descriptions and transcript segments by timestamp.
- Index aligned derived markdown with provenance back to the original video.

**Acceptance:**

- 6.3.1 - Video ingest stores original files immutably under raw media. test: `crates/gwiki/src/ingest/video.rs::tests::stores_original_video`.
- 6.3.2 - Frame sampling records timestamps and source references. test: `crates/gwiki/src/video.rs::tests::frame_sampling_records_timestamps`.
- 6.3.3 - Transcript and frame descriptions align by timestamp. test: `crates/gwiki/src/video.rs::tests::aligns_transcript_and_frames`.
- 6.3.4 - Derived video markdown indexes with provenance to the original asset. test: `crates/gwiki/src/ingest/video.rs::tests::video_derivatives_keep_provenance`.

## VS1: Verification
`kind: verification`

Plan validation for this pass:

- `uv run gobby plans validate .gobby/plans/gwiki.md`

Implementation validation after expansion:

- `cargo build -p gobby-wiki --no-default-features`
- `cargo test -p gobby-wiki --no-default-features`
- `cargo clippy -p gobby-wiki --no-default-features -- -D warnings`
- Smoke flow: `gwiki init`, `gwiki setup`, `gwiki ingest-file`, `gwiki index`, `gwiki search`, `gwiki backlinks`, `gwiki research`, `gwiki compile`, and `gwiki audit` against a temporary topic vault.

## AC1: Acceptance Criteria
`kind: verification`

- `gobby-wiki` is a Rust workspace crate and binary that consumes `gobby-core` foundation primitives.
- Global topic and project-local scopes both preserve llm-wiki vault UX.
- Filesystem markdown remains the source of truth; databases and vectors are rebuildable derived indexes.
- `gwiki` data is namespaced in PostgreSQL, FalkorDB, and Qdrant without touching gcode-owned objects.
- Schema creation belongs to explicit `gwiki setup`, not daemon schema ownership or runtime side effects.
- Research, ingestion, compile, audit, and multimodal roadmap are represented with concrete deliverables.

## V1 Plan Changelog
`kind: verification`

- **R1 (2026-05-26)**: Reframed the gwiki plan around `gobby-core` shared primitives plus `gobby-wiki` domain behavior. Preserved llm-wiki vault UX, dual scopes, namespaced data, filesystem source of truth, ingestion/research/compile/audit roadmap, and multimodal extensions. Removed copied-gcode-pipeline and daemon-schema-owner assumptions.
