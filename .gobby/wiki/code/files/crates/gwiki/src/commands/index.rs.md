---
title: crates/gwiki/src/commands/index.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/index.rs
  ranges:
  - 31-37
  - 39-59
  - 61-126
  - 128-164
  - 166-178
  - 180-202
  - 204-227
  - 229-231
  - 233-239
  - 241-245
  - 247-251
  - 253-258
  - 260-283
  - 285-336
  - 338-373
  - 375-399
  - 401-411
  - 413-438
  - 440-495
  - 497-567
  - 569-579
  - 585-587
  - 589-599
  - 590-594
  - 596-598
  - 602-609
  - 613-618
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/index.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

`crates/gwiki/src/commands/index.rs` exposes 27 indexed API symbols.
[crates/gwiki/src/commands/index.rs:31-37]
[crates/gwiki/src/commands/index.rs:39-59]
[crates/gwiki/src/commands/index.rs:61-126]
[crates/gwiki/src/commands/index.rs:128-164]
[crates/gwiki/src/commands/index.rs:166-178]
[crates/gwiki/src/commands/index.rs:180-202]
[crates/gwiki/src/commands/index.rs:204-227]
[crates/gwiki/src/commands/index.rs:229-231]
[crates/gwiki/src/commands/index.rs:233-239]
[crates/gwiki/src/commands/index.rs:241-245]
[crates/gwiki/src/commands/index.rs:247-251]
[crates/gwiki/src/commands/index.rs:253-258]
[crates/gwiki/src/commands/index.rs:260-283]
[crates/gwiki/src/commands/index.rs:285-336]
[crates/gwiki/src/commands/index.rs:338-373]
[crates/gwiki/src/commands/index.rs:375-399]
[crates/gwiki/src/commands/index.rs:401-411]
[crates/gwiki/src/commands/index.rs:413-438]
[crates/gwiki/src/commands/index.rs:440-495]
[crates/gwiki/src/commands/index.rs:497-567]
[crates/gwiki/src/commands/index.rs:569-579]
[crates/gwiki/src/commands/index.rs:585-587]
[crates/gwiki/src/commands/index.rs:589-599]
[crates/gwiki/src/commands/index.rs:590-594]
[crates/gwiki/src/commands/index.rs:596-598]
[crates/gwiki/src/commands/index.rs:602-609]
[crates/gwiki/src/commands/index.rs:613-618]

## API Symbols

- `execute` (function) component `execute [function]` (`6ddfec1b-c9ec-565f-bdbd-02f449d99b3e`) lines 31-37 [crates/gwiki/src/commands/index.rs:31-37]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves and validates a scope selection, indexes its contents, and returns a rendered index with scope identity and entry counts. [crates/gwiki/src/commands/index.rs:31-37]
- `index_resolved_scope` (function) component `index_resolved_scope [function]` (`9db1115f-a7c2-5a0e-bc2c-1f90403a015d`) lines 39-59 [crates/gwiki/src/commands/index.rs:39-59]
  - Signature: `pub(crate) fn index_resolved_scope(`
  - Purpose: Indexes a vault's resolved scope to a PostgreSQL-backed store with Qdrant vector and Falkor graph synchronization if a database is available, otherwise to a local in-memory store. [crates/gwiki/src/commands/index.rs:39-59]
- `execute_ingest_file` (function) component `execute_ingest_file [function]` (`a7e925a1-8625-5f65-8d93-cf582938ea04`) lines 61-126 [crates/gwiki/src/commands/index.rs:61-126]
  - Signature: `pub(crate) fn execute_ingest_file(`
  - Purpose: Ingests a file into a PostgreSQL search store using AI context and vector embeddings, then synchronizes the vectors to Qdrant for the specified wiki scope. [crates/gwiki/src/commands/index.rs:61-126]
- `execute_ingest_url` (function) component `execute_ingest_url [function]` (`4457a3e0-3993-5f49-aa02-8009820d0ef9`) lines 128-164 [crates/gwiki/src/commands/index.rs:128-164]
  - Signature: `pub(crate) fn execute_ingest_url(`
  - Purpose: Ingests URLs into a scoped vault, persisting them to PostgreSQL with synchronized Qdrant vector and Falkor graph indices if available, otherwise using an in-memory fallback store. [crates/gwiki/src/commands/index.rs:128-164]
- `resolve_ingest_ai_context` (function) component `resolve_ingest_ai_context [function]` (`4e549873-6a52-52b5-8545-955542916d88`) lines 166-178 [crates/gwiki/src/commands/index.rs:166-178]
  - Signature: `fn resolve_ingest_ai_context(`
  - Purpose: Resolves an `AiContext` from a project ID and configuration source, applies the supplied `IngestFileOptions` with a resolved or defaulted video frame interval, and returns both. [crates/gwiki/src/commands/index.rs:166-178]
- `resolve_ingest_file_ai_context` (function) component `resolve_ingest_file_ai_context [function]` (`db278293-f2eb-540b-90e4-4d8e189f0c4f`) lines 180-202 [crates/gwiki/src/commands/index.rs:180-202]
  - Signature: `pub(crate) fn resolve_ingest_file_ai_context(`
  - Purpose: Resolves AI context for file ingestion by loading configuration from a command-specific PostgreSQL database if available, otherwise falling back to local configuration in gobby_home. [crates/gwiki/src/commands/index.rs:180-202]
- `resolve_video_frame_interval_seconds` (function) component `resolve_video_frame_interval_seconds [function]` (`ec2c79f5-d7d0-53a7-b258-13c73dd8815b`) lines 204-227 [crates/gwiki/src/commands/index.rs:204-227]
  - Signature: `fn resolve_video_frame_interval_seconds(source: &mut impl ConfigSource) -> Result<u32, WikiError> {`
  - Purpose: Resolves and validates the video frame interval configuration value as a strictly positive u32, with a default fallback when unset. [crates/gwiki/src/commands/index.rs:204-227]
- `ai_project_id` (function) component `ai_project_id [function]` (`8d9ea157-db6a-5f7a-914e-9eb3e64e106c`) lines 229-231 [crates/gwiki/src/commands/index.rs:229-231]
  - Signature: `fn ai_project_id(scope: &ScopeIdentity) -> Option<String> {`
  - Purpose: Returns the cloned scope ID wrapped in `Some` if the scope kind is `Project`, otherwise `None`. [crates/gwiki/src/commands/index.rs:229-231]
- `ai_project_id_for_search` (function) component `ai_project_id_for_search [function]` (`6c87f5fa-fd95-50fe-93eb-2d5df8c679b0`) lines 233-239 [crates/gwiki/src/commands/index.rs:233-239]
  - Signature: `fn ai_project_id_for_search(scope: &SearchScope) -> Option<String> {`
  - Purpose: Returns the contained project ID as `Some` if the search scope is a Project variant, otherwise returns `None` for Global and Topic scopes. [crates/gwiki/src/commands/index.rs:233-239]
- `gobby_home` (function) component `gobby_home [function]` (`81a124ba-cc67-536b-bd6d-b3ff5b47ff57`) lines 241-245 [crates/gwiki/src/commands/index.rs:241-245]
  - Signature: `fn gobby_home() -> Result<PathBuf, WikiError> {`
  - Purpose: Resolves the Gobby home directory path by delegating to `gobby_core::gobby_home()` and converting any errors to a `WikiError::Config` variant with contextual detail. [crates/gwiki/src/commands/index.rs:241-245]
- `connect_postgres_index` (function) component `connect_postgres_index [function]` (`2804243b-20ae-5238-a154-ae0427db510e`) lines 247-251 [crates/gwiki/src/commands/index.rs:247-251]
  - Signature: `fn connect_postgres_index(database_url: &str, command: &str) -> Result<Client, WikiError> {`
  - Purpose: # Summary

Establishes a read-write PostgreSQL client connection using the provided database URL, mapping connection errors to WikiError with contextual information about the command that failed. [crates/gwiki/src/commands/index.rs:247-251]
- `postgres_store_for_search` (function) component `postgres_store_for_search [function]` (`089ba086-dd1c-5fd3-b3a1-e5b9eef9123f`) lines 253-258 [crates/gwiki/src/commands/index.rs:253-258]
  - Signature: `fn postgres_store_for_search<'a>(`
  - Purpose: Constructs a PostgresWikiStore from a mutable database client connection and search scope, with the store's lifetime bound to the connection's lifetime. [crates/gwiki/src/commands/index.rs:253-258]
- `sync_falkor_graph` (function) component `sync_falkor_graph [function]` (`170e3ad5-15e7-5d99-966f-ac2a3a5de0de`) lines 260-283 [crates/gwiki/src/commands/index.rs:260-283]
  - Signature: `fn sync_falkor_graph(`
  - Purpose: Resolves FalkorDB configuration from a composite config source and synchronizes a specified search scope from PostgreSQL to the FalkorDB graph database, gracefully handling configuration and sync failures. [crates/gwiki/src/commands/index.rs:260-283]
- `sync_qdrant_vectors` (function) component `sync_qdrant_vectors [function]` (`ca945602-1958-5069-a200-89ba88051809`) lines 285-336 [crates/gwiki/src/commands/index.rs:285-336]
  - Signature: `fn sync_qdrant_vectors(`
  - Purpose: Synchronizes wiki vector chunks from PostgreSQL to Qdrant using resolved embedding and Qdrant configurations, with graceful fallback on missing or failed configuration. [crates/gwiki/src/commands/index.rs:285-336]
- `resolve_vector_embedding` (function) component `resolve_vector_embedding [function]` (`f95db7be-612e-5a16-97bc-5951a7bdcb7b`) lines 338-373 [crates/gwiki/src/commands/index.rs:338-373]
  - Signature: `fn resolve_vector_embedding(`
  - Purpose: Conditionally constructs and returns a `SemanticEmbedding` variant by routing to either a daemon-backed or config-resolved implementation based on the effective embedding strategy derived from context and compile-time feature flags. [crates/gwiki/src/commands/index.rs:338-373]
- `effective_embedding_route` (function) component `effective_embedding_route [function]` (`b8ffe67a-d4f3-5c22-8526-2bfcb3ce05e3`) lines 375-399 [crates/gwiki/src/commands/index.rs:375-399]
  - Signature: `fn effective_embedding_route(context: &AiContext) -> AiRouting {`
  - Purpose: Resolves the effective AI embedding routing strategy by delegating to `effective_route` when the 'ai' feature is enabled, or downgrading unsupported routing modes (Daemon→Off, Auto→Direct) when the feature is disabled. [crates/gwiki/src/commands/index.rs:375-399]
- `indexed_counts_for_postgres` (function) component `indexed_counts_for_postgres [function]` (`20159b63-3311-5d07-b5a1-817f4783d490`) lines 401-411 [crates/gwiki/src/commands/index.rs:401-411]
  - Signature: `fn indexed_counts_for_postgres(`
  - Purpose: Conditionally retrieves PostgreSQL index counts for a given search scope based on a boolean flag, returning either computed counts or default empty counts. [crates/gwiki/src/commands/index.rs:401-411]
- `render_index` (function) component `render_index [function]` (`906e9925-f4ee-5461-b042-c16b492508a6`) lines 413-438 [crates/gwiki/src/commands/index.rs:413-438]
  - Signature: `fn render_index(scope: ScopeIdentity, root: &Path, counts: IndexCounts) -> CommandOutcome {`
  - Purpose: Returns a scoped CommandOutcome containing JSON-serialized index completion metadata and human-readable text summary with document, chunk, link, source, and ingestion counts for the specified scope and root path. [crates/gwiki/src/commands/index.rs:413-438]
- `render_ingest_file` (function) component `render_ingest_file [function]` (`cc108563-f0a5-5db1-9f5a-bbb82b7665d9`) lines 440-495 [crates/gwiki/src/commands/index.rs:440-495]
  - Signature: `fn render_ingest_file(`
  - Purpose: Returns a scoped command outcome containing JSON and formatted text that report successful file ingestion along with source metadata and indexing statistics. [crates/gwiki/src/commands/index.rs:440-495]
- `render_ingest_url` (function) component `render_ingest_url [function]` (`f50db82e-a5cb-55fc-9258-e6951e62e35f`) lines 497-567 [crates/gwiki/src/commands/index.rs:497-567]
  - Signature: `fn render_ingest_url(`
  - Purpose: Renders a CommandOutcome by transforming URL batch ingestion results (accepted/failed URLs and index statistics) into structured JSON and human-readable text representations. [crates/gwiki/src/commands/index.rs:497-567]
- `ensure_scope_root` (function) component `ensure_scope_root [function]` (`0a87b97b-f933-5f65-a570-77ed9afb1e66`) lines 569-579 [crates/gwiki/src/commands/index.rs:569-579]
  - Signature: `fn ensure_scope_root(scope: &crate::scope::ResolvedScope) -> Result<(), WikiError> {`
  - Purpose: Validates that the scope root is an existing directory, returning `WikiError::InvalidScope` if it is missing or not a directory. [crates/gwiki/src/commands/index.rs:569-579]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`af93486d-d885-57a4-8a6a-8f5aed789013`) lines 585-587 [crates/gwiki/src/commands/index.rs:585-587]
  - Signature: `struct TestConfigSource {`
  - Purpose: `TestConfigSource` is a struct that wraps an optional static string reference (`Option<&'static str>`) for configuration testing purposes. [crates/gwiki/src/commands/index.rs:585-587]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`b40c07b8-d815-595b-9bcc-82d4904cb5b8`) lines 589-599 [crates/gwiki/src/commands/index.rs:589-599]
  - Signature: `impl ConfigSource for TestConfigSource {`
  - Purpose: `TestConfigSource` is a test implementation of `ConfigSource` that returns a stored value only when the key matches `VIDEO_FRAME_INTERVAL_KEY` and performs identity resolution on string values. [crates/gwiki/src/commands/index.rs:589-599]
- `TestConfigSource.config_value` (method) component `TestConfigSource.config_value [method]` (`c1b7ab97-5087-5f6e-8e39-8e1a52f11abc`) lines 590-594 [crates/gwiki/src/commands/index.rs:590-594]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Returns `Some(String)` containing the string representation of `self.value` if the key matches `VIDEO_FRAME_INTERVAL_KEY`, otherwise returns `None`. [crates/gwiki/src/commands/index.rs:590-594]
- `TestConfigSource.resolve_value` (method) component `TestConfigSource.resolve_value [method]` (`5e77ac48-9e46-5891-9b89-a54c8c032446`) lines 596-598 [crates/gwiki/src/commands/index.rs:596-598]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Converts a string slice to an owned `String` and returns it as a successful `anyhow::Result`. [crates/gwiki/src/commands/index.rs:596-598]
- `video_frame_interval_zero_is_invalid` (function) component `video_frame_interval_zero_is_invalid [function]` (`1753ca14-3845-5829-88ce-c4a2da02f7d9`) lines 602-609 [crates/gwiki/src/commands/index.rs:602-609]
  - Signature: `fn video_frame_interval_zero_is_invalid() {`
  - Purpose: This test verifies that `resolve_video_frame_interval_seconds` rejects a zero-valued interval by returning a `WikiError::Config` variant with an error message asserting the value must be greater than zero. [crates/gwiki/src/commands/index.rs:602-609]
- `auto_embedding_route_falls_back_to_direct_without_ai` (function) component `auto_embedding_route_falls_back_to_direct_without_ai [function]` (`8ca187d2-c36e-5354-a0ee-15c1996fca82`) lines 613-618 [crates/gwiki/src/commands/index.rs:613-618]
  - Signature: `fn auto_embedding_route_falls_back_to_direct_without_ai() {`
  - Purpose: This test function asserts that when `AiContext` is resolved without configuration values, the effective embedding route defaults to `AiRouting::Direct`. [crates/gwiki/src/commands/index.rs:613-618]

