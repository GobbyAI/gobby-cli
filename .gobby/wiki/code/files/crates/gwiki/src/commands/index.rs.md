---
title: crates/gwiki/src/commands/index.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/index.rs
  ranges:
  - 35-38
  - 40-46
  - 48-52
  - 54-86
  - 88-153
  - 155-191
  - 193-205
  - 207-229
  - 231-254
  - 256-258
  - 260-266
  - 268-272
  - 274-278
  - 280-285
  - 287-311
  - 313-364
  - 366-368
  - 370-372
  - 374-384
  - 386-391
  - 393-428
  - 430-454
  - 456-466
  - 468-509
  - 511-566
  - 568-638
  - 640-650
  - 656-658
  - 660-670
  - 673-680
  - 683-700
  - 703-727
  - 731-736
  - 738-746
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/index.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `gwiki index` and ingest command flow for a resolved scope: it validates the target root, computes index reports, and renders command outcomes for indexing, file ingest, and URL ingest. The core path branches between a PostgreSQL-backed index when a database URL is configured and an in-memory fallback otherwise, then layers in optional Qdrant and FalkorDB synchronization, capturing any service degradations alongside `IndexCounts` in `IndexReport`. Helper functions resolve AI context and embedding configuration, derive project IDs and config sources, check video frame interval settings, open Postgres connections, build scoped stores, and format consistent success output. The file also includes degradation constructors, scope-root validation, a test config source, and tests covering invalid video intervals, empty degradations, Qdrant failure reporting, and embedding-route fallback behavior.
[crates/gwiki/src/commands/index.rs:35-38]
[crates/gwiki/src/commands/index.rs:40-46]
[crates/gwiki/src/commands/index.rs:48-52]
[crates/gwiki/src/commands/index.rs:54-86]
[crates/gwiki/src/commands/index.rs:88-153]

## API Symbols

- `IndexReport` (class) component `IndexReport [class]` (`841f90e8-756b-5f27-999e-57a7ec5d9b09`) lines 35-38 [crates/gwiki/src/commands/index.rs:35-38]
  - Signature: `struct IndexReport {`
  - Purpose: `IndexReport` is a Rust struct that packages `IndexCounts` together with a `Vec<DegradationKind>` to report index metrics alongside any detected degradations. [crates/gwiki/src/commands/index.rs:35-38]
- `execute` (function) component `execute [function]` (`678c88e9-6753-57dc-a8e3-e1e21e3ecfbc`) lines 40-46 [crates/gwiki/src/commands/index.rs:40-46]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves the command scope from `selection`, verifies it has a valid scope root, computes the scope identity and index report, and returns the rendered indexing `CommandOutcome` or propagates any `WikiError`. [crates/gwiki/src/commands/index.rs:40-46]
- `index_resolved_scope` (function) component `index_resolved_scope [function]` (`37703920-7301-538b-8d5e-31f0b51a00ea`) lines 48-52 [crates/gwiki/src/commands/index.rs:48-52]
  - Signature: `pub(crate) fn index_resolved_scope(`
  - Purpose: Returns the `counts` from `index_resolved_scope_report(scope)` for a `ResolvedScope`, propagating any `WikiError` from the underlying report generation. [crates/gwiki/src/commands/index.rs:48-52]
- `index_resolved_scope_report` (function) component `index_resolved_scope_report [function]` (`e7aa8d66-45f1-53aa-83e0-dc2c1689cc42`) lines 54-86 [crates/gwiki/src/commands/index.rs:54-86]
  - Signature: `fn index_resolved_scope_report(`
  - Purpose: Indexes the resolved scope’s vault into the Postgres-backed search store when a database URL is available, synchronizes Qdrant and Falkor degradations, and returns indexed counts plus any degradations; otherwise it performs a local in-memory index and returns only counts. [crates/gwiki/src/commands/index.rs:54-86]
- `execute_ingest_file` (function) component `execute_ingest_file [function]` (`77dbe63b-0177-50c3-8465-0a851f1d031b`) lines 88-153 [crates/gwiki/src/commands/index.rs:88-153]
  - Signature: `pub(crate) fn execute_ingest_file(`
  - Purpose: I’m locating the full function body so I can summarize its behavior precisely rather than rely on the truncated snippet.`gcode` isn’t reachable in this environment, so I’m falling back to a direct source search to recover the full function context.I’ve confirmed the codebase is mostly Python, so I’m checking whether the Rust implementation exists in another path or whether the snippet is all I have to summarize.It resolves the requested scope, idempotently initializes the vault paths, and, when a Postgres index is configured, loads AI config, ingests the given file path into the scoped search store, syncs Qdrant vectors, and returns a `CommandOutcome` or `WikiError`. [crates/gwiki/src/commands/index.rs:88-153]
- `execute_ingest_url` (function) component `execute_ingest_url [function]` (`ecf220bb-76ab-5eb1-bfd5-660fa389652d`) lines 155-191 [crates/gwiki/src/commands/index.rs:155-191]
  - Signature: `pub(crate) fn execute_ingest_url(`
  - Purpose: Resolves the target scope, idempotently initializes the vault paths, timestamps the run, and ingests the provided URLs into either the PostgreSQL-backed wiki index (with Qdrant/Falkor sync when any URLs are accepted) or an in-memory fallback store before rendering a `CommandOutcome`. [crates/gwiki/src/commands/index.rs:155-191]
- `resolve_ingest_ai_context` (function) component `resolve_ingest_ai_context [function]` (`9729101d-7abb-55a0-a226-979234dd085a`) lines 193-205 [crates/gwiki/src/commands/index.rs:193-205]
  - Signature: `fn resolve_ingest_ai_context(`
  - Purpose: Resolves an `AiContext` from the optional `project_id` and `ConfigSource`, clones and normalizes `IngestFileOptions` by defaulting `video_frame_interval_seconds` when absent, applies the options to the context, and returns the resulting `(AiContext, IngestFileOptions)` or a `WikiError`. [crates/gwiki/src/commands/index.rs:193-205]
- `resolve_ingest_file_ai_context` (function) component `resolve_ingest_file_ai_context [function]` (`cfbe3467-16d0-567b-94b9-2c6e77dba77b`) lines 207-229 [crates/gwiki/src/commands/index.rs:207-229]
  - Signature: `pub(crate) fn resolve_ingest_file_ai_context(`
  - Purpose: Resolves the ingest AI context and possibly adjusted `IngestFileOptions` for the given scope by deriving a project ID, selecting a PostgreSQL-backed config source when `database_url_for(command)` returns one or otherwise falling back to `LocalAiConfigSource` from `gobby_home`, and then delegating to `resolve_ingest_ai_context` while mapping config resolution failures to `WikiError::Config`. [crates/gwiki/src/commands/index.rs:207-229]
- `resolve_video_frame_interval_seconds` (function) component `resolve_video_frame_interval_seconds [function]` (`59c4b099-4d0e-521f-958b-c4bdd8c0d5f2`) lines 231-254 [crates/gwiki/src/commands/index.rs:231-254]
  - Signature: `fn resolve_video_frame_interval_seconds(source: &mut impl ConfigSource) -> Result<u32, WikiError> {`
  - Purpose: Resolves `VIDEO_FRAME_INTERVAL_KEY` from `source` to a trimmed `u32`, returns `ingest::video::DEFAULT_FRAME_INTERVAL_SECONDS` if unset, and otherwise errors with `WikiError::Config` on resolution, parse, or zero-value failures. [crates/gwiki/src/commands/index.rs:231-254]
- `ai_project_id` (function) component `ai_project_id [function]` (`c64a5c44-b124-5b2c-9f89-31495292256a`) lines 256-258 [crates/gwiki/src/commands/index.rs:256-258]
  - Signature: `fn ai_project_id(scope: &ScopeIdentity) -> Option<String> {`
  - Purpose: Returns `Some(scope.id.clone())` only when `scope.kind` is `ScopeKind::Project`; otherwise it returns `None`. [crates/gwiki/src/commands/index.rs:256-258]
- `ai_project_id_for_search` (function) component `ai_project_id_for_search [function]` (`c009b1dd-36e8-58ec-9f9b-f4695741fd3c`) lines 260-266 [crates/gwiki/src/commands/index.rs:260-266]
  - Signature: `fn ai_project_id_for_search(scope: &SearchScope) -> Option<String> {`
  - Purpose: Returns `Some(project_id.clone())` only when `scope` is `SearchScope::Project { project_id }`, and `None` for `SearchScope::Global` or `SearchScope::Topic { .. }`. [crates/gwiki/src/commands/index.rs:260-266]
- `gobby_home` (function) component `gobby_home [function]` (`2be8454c-2cb6-5653-a99f-2738e4b40648`) lines 268-272 [crates/gwiki/src/commands/index.rs:268-272]
  - Signature: `fn gobby_home() -> Result<PathBuf, WikiError> {`
  - Purpose: Returns the Gobby home directory path from `gobby_core::gobby_home()`, converting any resolution failure into `WikiError::Config` with a gwiki-specific error message. [crates/gwiki/src/commands/index.rs:268-272]
- `connect_postgres_index` (function) component `connect_postgres_index [function]` (`017829fc-abe9-5a85-93fb-fcc437d7ce86`) lines 274-278 [crates/gwiki/src/commands/index.rs:274-278]
  - Signature: `fn connect_postgres_index(database_url: &str, command: &str) -> Result<Client, WikiError> {`
  - Purpose: Attempts to open a read-write PostgreSQL `Client` via `gobby_core::postgres::connect_readwrite(database_url)` and maps any failure into `WikiError::Config` with a command-specific message. [crates/gwiki/src/commands/index.rs:274-278]
- `postgres_store_for_search` (function) component `postgres_store_for_search [function]` (`d97f234b-180f-5583-95e4-8e7d72b04fb8`) lines 280-285 [crates/gwiki/src/commands/index.rs:280-285]
  - Signature: `fn postgres_store_for_search<'a>(`
  - Purpose: It constructs and returns a `store::PostgresWikiStore<'a>` bound to the provided mutable PostgreSQL `Client` and the store scope computed from `search_scope`. [crates/gwiki/src/commands/index.rs:280-285]
- `sync_falkor_graph` (function) component `sync_falkor_graph [function]` (`d64fa9f2-6d5a-5b44-8b49-1c73c39c287a`) lines 287-311 [crates/gwiki/src/commands/index.rs:287-311]
  - Signature: `fn sync_falkor_graph(`
  - Purpose: `sync_falkor_graph` resolves FalkorDB config from Gobby home plus the provided Postgres client, skips graph sync and returns a `not_configured` degradation when no FalkorDB config is present, otherwise runs `sync_scope_from_postgres` for the given `SearchScope` and returns `None` on success or an `unreachable` degradation if sync fails. [crates/gwiki/src/commands/index.rs:287-311]
- `sync_qdrant_vectors` (function) component `sync_qdrant_vectors [function]` (`7e033ae3-37d0-5c08-9eb4-0c30804f7957`) lines 313-364 [crates/gwiki/src/commands/index.rs:313-364]
  - Signature: `fn sync_qdrant_vectors(`
  - Purpose: `sync_qdrant_vectors` resolves embedding and Qdrant configuration from Gobby/AI config, returns a not-configured degradation if either is missing, and otherwise syncs vectors for the given `SearchScope` from PostgreSQL wiki chunks into Qdrant, converting sync errors into a Qdrant degradation result. [crates/gwiki/src/commands/index.rs:313-364]
- `qdrant_sync_degradation` (function) component `qdrant_sync_degradation [function]` (`d20d5bda-cde0-5045-ac35-9191d3d5152e`) lines 366-368 [crates/gwiki/src/commands/index.rs:366-368]
  - Signature: `fn qdrant_sync_degradation(error: vector::WikiVectorError) -> DegradationKind {`
  - Purpose: It maps a `vector::WikiVectorError` to a `DegradationKind` by delegating to `unreachable_degradation(QDRANT_SERVICE, error)`, indicating Qdrant sync failures are treated as unreachable degradation paths. [crates/gwiki/src/commands/index.rs:366-368]
- `not_configured_degradation` (function) component `not_configured_degradation [function]` (`9c6bb4d8-caf2-50d0-90fb-a2b49f2ba605`) lines 370-372 [crates/gwiki/src/commands/index.rs:370-372]
  - Signature: `fn not_configured_degradation(service: &'static str) -> DegradationKind {`
  - Purpose: `not_configured_degradation` constructs a `DegradationKind` for the given service by delegating to `service_unavailable_degradation(service, ServiceState::NotConfigured)`. [crates/gwiki/src/commands/index.rs:370-372]
- `unreachable_degradation` (function) component `unreachable_degradation [function]` (`835a6f2c-f0a3-5478-96d7-d2ceed81c223`) lines 374-384 [crates/gwiki/src/commands/index.rs:374-384]
  - Signature: `fn unreachable_degradation(`
  - Purpose: It converts a displayable error into a `ServiceState::Unreachable` for the given service and delegates to `service_unavailable_degradation` to return the corresponding `DegradationKind`. [crates/gwiki/src/commands/index.rs:374-384]
- `service_unavailable_degradation` (function) component `service_unavailable_degradation [function]` (`88f3017e-d04a-5b86-8545-972ed85d3622`) lines 386-391 [crates/gwiki/src/commands/index.rs:386-391]
  - Signature: `fn service_unavailable_degradation(service: &'static str, state: ServiceState) -> DegradationKind {`
  - Purpose: Constructs and returns a `DegradationKind::ServiceUnavailable` variant by cloning the `service` name into an owned `String` and pairing it with the provided `ServiceState`. [crates/gwiki/src/commands/index.rs:386-391]
- `resolve_vector_embedding` (function) component `resolve_vector_embedding [function]` (`ecf85ac6-782e-5275-8059-41b0513f8cf8`) lines 393-428 [crates/gwiki/src/commands/index.rs:393-428]
  - Signature: `fn resolve_vector_embedding(`
  - Purpose: Selects a `SemanticEmbedding` backend from the effective AI routing, returning `None` when routing is off or unsupported, using a daemon-backed embedding via `context.clone()` when routing is `Daemon` or `Auto` with the `ai` feature enabled, and otherwise resolving a direct embedding from `source`. [crates/gwiki/src/commands/index.rs:393-428]
- `effective_embedding_route` (function) component `effective_embedding_route [function]` (`1cfd6c70-d7c8-5e2f-a1f9-9222705b28fe`) lines 430-454 [crates/gwiki/src/commands/index.rs:430-454]
  - Signature: `fn effective_embedding_route(context: &AiContext) -> AiRouting {`
  - Purpose: `effective_embedding_route` returns the embedding `AiRouting` for the given `AiContext`, delegating to `effective_route(..., AiCapability::Embed)` when the `ai` feature is enabled and otherwise mapping `Off`/`Direct` through unchanged while downgrading `Daemon` to `Off` and `Auto` to `Direct` with warnings. [crates/gwiki/src/commands/index.rs:430-454]
- `indexed_counts_for_postgres` (function) component `indexed_counts_for_postgres [function]` (`72f82a07-ad9a-5dc6-a531-6cfb8422e95a`) lines 456-466 [crates/gwiki/src/commands/index.rs:456-466]
  - Signature: `fn indexed_counts_for_postgres(`
  - Purpose: Returns PostgreSQL-backed index counts for the given `SearchScope` when `should_count` is `true`, otherwise returns `IndexCounts::default()` without querying the database. [crates/gwiki/src/commands/index.rs:456-466]
- `render_index` (function) component `render_index [function]` (`78921df2-77e0-5db8-b2ae-1647d846dd74`) lines 468-509 [crates/gwiki/src/commands/index.rs:468-509]
  - Signature: `fn render_index(scope: ScopeIdentity, root: &Path, report: IndexReport) -> CommandOutcome {`
  - Purpose: `render_index` converts an `IndexReport` into a scoped `CommandOutcome` by emitting a JSON payload with the `index` command, scope, root path, indexed counts, and degradations, while also formatting a human-readable “Index complete” summary with degradation labels or `none`. [crates/gwiki/src/commands/index.rs:468-509]
- `render_ingest_file` (function) component `render_ingest_file [function]` (`8207455e-bf1f-54ab-bcb5-82cf810d4d1a`) lines 511-566 [crates/gwiki/src/commands/index.rs:511-566]
  - Signature: `fn render_ingest_file(`
  - Purpose: Constructs a scoped `CommandOutcome` for a successful `ingest-file` command by packaging the path, raw/asset locations, source metadata, and index counts into both a JSON payload and a formatted status string. [crates/gwiki/src/commands/index.rs:511-566]
- `render_ingest_url` (function) component `render_ingest_url [function]` (`d2700626-88b1-521c-887e-ba14b4c544a7`) lines 568-638 [crates/gwiki/src/commands/index.rs:568-638]
  - Signature: `fn render_ingest_url(`
  - Purpose: `render_ingest_url` builds a scoped `CommandOutcome` for a batch URL ingest by serializing accepted and failed items plus index counts into a JSON payload and human-readable summary text, then sets the outcome’s exit code from `result.exit_code()`. [crates/gwiki/src/commands/index.rs:568-638]
- `ensure_scope_root` (function) component `ensure_scope_root [function]` (`5d23e034-fc13-56a8-b98f-9573a6d74a39`) lines 640-650 [crates/gwiki/src/commands/index.rs:640-650]
  - Signature: `fn ensure_scope_root(scope: &crate::scope::ResolvedScope) -> Result<(), WikiError> {`
  - Purpose: `ensure_scope_root` validates that `scope.root()` exists as a directory and returns `Ok(())` if so, otherwise it returns `WikiError::InvalidScope` with a message identifying the missing or non-directory root path. [crates/gwiki/src/commands/index.rs:640-650]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`db7d0eb3-249f-5a41-973d-e1ba40ffb8cd`) lines 656-658 [crates/gwiki/src/commands/index.rs:656-658]
  - Signature: `struct TestConfigSource {`
  - Purpose: `TestConfigSource` is a test-only configuration source struct that stores an optional `'static` string slice as its backing value. [crates/gwiki/src/commands/index.rs:656-658]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`ec331ffd-525f-5b3d-af07-b956c0120ba1`) lines 660-670 [crates/gwiki/src/commands/index.rs:660-670]
  - Signature: `impl ConfigSource for TestConfigSource {`
  - Purpose: `TestConfigSource` is a test-only `ConfigSource` implementation that returns its stored optional value only for `VIDEO_FRAME_INTERVAL_KEY` and otherwise yields `None`, while `resolve_value` is a no-op identity conversion returning the input string unchanged. [crates/gwiki/src/commands/index.rs:660-670]
- `TestConfigSource.config_value` (method) component `TestConfigSource.config_value [method]` (`12dcd5a1-c8e0-543a-9c78-cc03866fe453`) lines 661-665 [crates/gwiki/src/commands/index.rs:661-665]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Returns `Some(self.value.to_string())` only when `key == VIDEO_FRAME_INTERVAL_KEY` and `self.value` is `Some`, otherwise returns `None` without mutating state. [crates/gwiki/src/commands/index.rs:661-665]
- `TestConfigSource.resolve_value` (method) component `TestConfigSource.resolve_value [method]` (`cf13850f-c20d-52d0-9565-eb661ddda8ce`) lines 667-669 [crates/gwiki/src/commands/index.rs:667-669]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Returns the input `&str` as an owned `String` wrapped in `Ok`, without using `self` or performing any resolution logic. [crates/gwiki/src/commands/index.rs:667-669]
- `video_frame_interval_zero_is_invalid` (function) component `video_frame_interval_zero_is_invalid [function]` (`a47a8d54-63cf-5742-ab78-41718f559a8b`) lines 673-680 [crates/gwiki/src/commands/index.rs:673-680]
  - Signature: `fn video_frame_interval_zero_is_invalid() {`
  - Purpose: This test verifies that a configured video frame interval of `0` is rejected by `resolve_video_frame_interval_seconds`, producing a `WikiError::Config` whose message states the interval must be greater than `0`. [crates/gwiki/src/commands/index.rs:673-680]
- `index_render_includes_empty_degradations` (function) component `index_render_includes_empty_degradations [function]` (`f0e72029-e1a1-52ef-9a1a-3b7add578b39`) lines 683-700 [crates/gwiki/src/commands/index.rs:683-700]
  - Signature: `fn index_render_includes_empty_degradations() {`
  - Purpose: Verifies that `render_index` serializes an empty `degradations` list as an empty JSON array and includes the text `Degradations: none` in the rendered output. [crates/gwiki/src/commands/index.rs:683-700]
- `index_render_reports_qdrant_sync_failure_degradation` (function) component `index_render_reports_qdrant_sync_failure_degradation [function]` (`2ca0a3ce-ecd2-59e1-b72d-917336cbf3ff`) lines 703-727 [crates/gwiki/src/commands/index.rs:703-727]
  - Signature: `fn index_render_reports_qdrant_sync_failure_degradation() {`
  - Purpose: Verifies that `render_index` serializes a Qdrant sync failure into a `ServiceUnavailable` degradation with `service == "qdrant"`, an `Unreachable` message of `"wiki vector qdrant error: connection refused"`, and a rendered text summary containing `Degradations: qdrant_unreachable`. [crates/gwiki/src/commands/index.rs:703-727]
- `auto_embedding_route_falls_back_to_direct_without_ai` (function) component `auto_embedding_route_falls_back_to_direct_without_ai [function]` (`c1db0ae3-66a7-5978-9166-b68df05b7a42`) lines 731-736 [crates/gwiki/src/commands/index.rs:731-736]
  - Signature: `fn auto_embedding_route_falls_back_to_direct_without_ai() {`
  - Purpose: Verifies that when `AiContext::resolve(None, &mut source)` is constructed from an empty config source, `effective_embedding_route` falls back to `AiRouting::Direct` rather than using an AI-backed route. [crates/gwiki/src/commands/index.rs:731-736]
- `sample_counts` (function) component `sample_counts [function]` (`74d4d4d3-8618-5361-b946-a19d96de3be7`) lines 738-746 [crates/gwiki/src/commands/index.rs:738-746]
  - Signature: `fn sample_counts() -> IndexCounts {`
  - Purpose: Returns a fixed `IndexCounts` instance populated with the sample values `documents: 3`, `chunks: 5`, `links: 7`, `sources: 11`, and `ingestions: 13`. [crates/gwiki/src/commands/index.rs:738-746]

