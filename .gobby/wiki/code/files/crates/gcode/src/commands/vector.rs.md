---
title: crates/gcode/src/commands/vector.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/vector.rs
  ranges:
  - 13-19
  - 21-25
  - 27-42
  - 44-63
  - 65-72
  - 74-84
  - 86-98
  - 100-110
  - 112-131
  - 134-150
  - 152-172
  - 181-195
  - 197-202
  - 204-220
  - 223-243
  - 246-304
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/vector.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Implements the `gcode` command layer for code-symbol vector lifecycle management: it builds a vector lifecycle from project context/config, checks status, syncs or rebuilds indexed files, clears project vectors, and removes orphaned vectors from Qdrant. The helper functions centralize lifecycle construction and output formatting, while the payload struct and tests verify the JSON/text contract and required configuration behavior.
[crates/gcode/src/commands/vector.rs:13-19]
[crates/gcode/src/commands/vector.rs:21-25]
[crates/gcode/src/commands/vector.rs:27-42]
[crates/gcode/src/commands/vector.rs:44-63]
[crates/gcode/src/commands/vector.rs:65-72]

## API Symbols

- `lifecycle_status` (function) component `lifecycle_status [function]` (`28fec698-1b64-5ca2-badf-b1c1f8eae721`) lines 13-19 [crates/gcode/src/commands/vector.rs:13-19]
  - Signature: `pub fn lifecycle_status(`
  - Purpose: Returns the lifecycle status for the current project’s code symbol collection by delegating to 'code_symbols::lifecycle_status' with 'ctx.project_id.clone()', 'CODE_SYMBOL_COLLECTION_PREFIX', and the provided 'CodeSymbolVectorLifecycleAction'. [crates/gcode/src/commands/vector.rs:13-19]
- `lifecycle_from_context` (function) component `lifecycle_from_context [function]` (`056d3555-6fcc-598a-b863-88f38c81af45`) lines 21-25 [crates/gcode/src/commands/vector.rs:21-25]
  - Signature: `pub(crate) fn lifecycle_from_context(`
  - Purpose: Constructs a 'CodeSymbolVectorLifecycle' from a 'Context' by deriving the embedding source from that context and delegating to 'lifecycle_from_resolved_embedding_source', returning a 'VectorLifecycleError' on failure. [crates/gcode/src/commands/vector.rs:21-25]
- `lifecycle_from_resolved_embedding_source` (function) component `lifecycle_from_resolved_embedding_source [function]` (`ebbccf33-77b9-522f-8762-f93b08c0a423`) lines 27-42 [crates/gcode/src/commands/vector.rs:27-42]
  - Signature: `fn lifecycle_from_resolved_embedding_source(`
  - Purpose: Constructs a 'CodeSymbolVectorLifecycle' from the current 'Context' by requiring a configured Qdrant client and embedding source, then passing those along with the project ID and code vectors, or returning 'MissingQdrantConfig'/'MissingEmbeddingConfig' if either is absent. [crates/gcode/src/commands/vector.rs:27-42]
- `sync_file` (function) component `sync_file [function]` (`faff068c-165b-5b51-a584-f98081d6fdeb`) lines 44-63 [crates/gcode/src/commands/vector.rs:44-63]
  - Signature: `pub fn sync_file(ctx: &Context, file_path: &str, format: Format) -> anyhow::Result<()> {`
  - Purpose: Synchronizes a single indexed file by loading project lifecycle and a read-write DB connection, verifying the file exists, fetching its symbols, syncing those symbols through the lifecycle, marking the file’s vectors as synced, and printing the lifecycle output as a 'ProjectionSyncReport' while returning any error encountered. [crates/gcode/src/commands/vector.rs:44-63]
- `clear` (function) component `clear [function]` (`9ad3d844-f4e7-5a55-9e58-0de1a383655e`) lines 65-72 [crates/gcode/src/commands/vector.rs:65-72]
  - Signature: `pub fn clear(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Initializes lifecycle and a read-write database connection, resets the project’s synchronized vector state in the database, clears the project vectors via the lifecycle, then emits lifecycle output with an empty successful 'ProjectionSyncReport' formatted per 'format'. [crates/gcode/src/commands/vector.rs:65-72]
- `rebuild` (function) component `rebuild [function]` (`f89801cd-0fba-59ea-a695-54ff60349b32`) lines 74-84 [crates/gcode/src/commands/vector.rs:74-84]
  - Signature: `pub fn rebuild(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Rebuilds a project’s symbol/vector projection by loading lifecycle and a read-write DB connection, enumerating indexed file paths, resetting project vectors, fetching symbols, regenerating symbol output, marking vectors synced, and printing the lifecycle output with a sync report. [crates/gcode/src/commands/vector.rs:74-84]
- `cleanup_orphans` (function) component `cleanup_orphans [function]` (`f02502f7-48e7-5f50-bfda-fc5ac0432e29`) lines 86-98 [crates/gcode/src/commands/vector.rs:86-98]
  - Signature: `pub fn cleanup_orphans(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Validates Qdrant config, opens a read-only database connection, collects all indexed file paths for the project into a 'HashSet', computes orphaned file vectors to remove via 'code_symbols::cleanup_orphan_file_vectors', and prints the cleanup result in the requested format. [crates/gcode/src/commands/vector.rs:86-98]
- `print_lifecycle_output` (function) component `print_lifecycle_output [function]` (`b6a83260-1b23-575c-ad7a-75a10b45d151`) lines 100-110 [crates/gcode/src/commands/vector.rs:100-110]
  - Signature: `fn print_lifecycle_output(`
  - Purpose: Serializes a lifecycle payload from 'output' and 'report', then prints it as JSON when 'format' is 'Format::Json' or as text using a JSON string representation when 'format' is 'Format::Text', returning any printing or serialization error as 'anyhow::Result<()>'. [crates/gcode/src/commands/vector.rs:100-110]
- `print_orphan_cleanup` (function) component `print_orphan_cleanup [function]` (`58b3a93a-7213-512d-96ad-bc2e68539ccc`) lines 112-131 [crates/gcode/src/commands/vector.rs:112-131]
  - Signature: `fn print_orphan_cleanup(cleanup: &VectorOrphanCleanup, format: Format) -> anyhow::Result<()> {`
  - Purpose: 'print_orphan_cleanup' builds a JSON payload describing a successful vector orphan cleanup (project, collection, scan/delete counts, and human-readable summary) and prints it as JSON or text depending on 'Format', returning any serialization/printing error. [crates/gcode/src/commands/vector.rs:112-131]
- `VectorLifecycleJsonPayload` (class) component `VectorLifecycleJsonPayload [class]` (`10ab8c31-c0c7-55dc-a750-d05c9e0ceb28`) lines 134-150 [crates/gcode/src/commands/vector.rs:134-150]
  - Signature: `pub(crate) struct VectorLifecycleJsonPayload {`
  - Purpose: 'VectorLifecycleJsonPayload' is a serde-serializable internal payload struct that captures a projection’s vector lifecycle state and metrics, including project/projection identifiers, lifecycle action, optional file path, sync/status/error information, symbol and file counts, vector upsert/delete operation counts, and a summary string. [crates/gcode/src/commands/vector.rs:134-150]
- `lifecycle_json_payload` (function) component `lifecycle_json_payload [function]` (`d58fe363-48f3-5bcc-9ee8-aa397fd8df4b`) lines 152-172 [crates/gcode/src/commands/vector.rs:152-172]
  - Signature: `pub(crate) fn lifecycle_json_payload(`
  - Purpose: Constructs and returns a 'VectorLifecycleJsonPayload' by copying selected fields from 'CodeSymbolVectorLifecycleOutput' and 'ProjectionSyncReport', fixing 'projection' to '"vector"' and transferring status, sync counts, degradation/error state, symbol/vector operation data, and summary. [crates/gcode/src/commands/vector.rs:152-172]
- `make_ctx` (function) component `make_ctx [function]` (`3fd7061d-0134-5744-b205-0aa6cf6e9364`) lines 181-195 [crates/gcode/src/commands/vector.rs:181-195]
  - Signature: `fn make_ctx() -> Context {`
  - Purpose: Constructs and returns a 'Context' populated with fixed test/default values, including a localhost PostgreSQL URL, a nonexistent project root, project ID 'project-1', 'quiet' enabled, all optional service endpoints unset, default indexing settings, and a 'Single' project index scope. [crates/gcode/src/commands/vector.rs:181-195]
- `qdrant_config` (function) component `qdrant_config [function]` (`535a0b67-cd6d-594d-b4f7-6492c9cc6233`) lines 197-202 [crates/gcode/src/commands/vector.rs:197-202]
  - Signature: `fn qdrant_config() -> crate::config::QdrantConfig {`
  - Purpose: Returns a 'QdrantConfig' with 'url' set to 'Some("http://localhost:6333")' and 'api_key' set to 'None'. [crates/gcode/src/commands/vector.rs:197-202]
- `daemon_embedding_source` (function) component `daemon_embedding_source [function]` (`e128fda4-599b-58a3-a44a-8e0f4e76006e`) lines 204-220 [crates/gcode/src/commands/vector.rs:204-220]
  - Signature: `fn daemon_embedding_source() -> EmbeddingSource {`
  - Purpose: Creates an AI context for project '"project-1"' with 'forced_routing' set to 'AiRouting::Daemon' and returns it wrapped as 'EmbeddingSource::Daemon(Box<...>)'. [crates/gcode/src/commands/vector.rs:204-220]
- `vector_lifecycle_requires_config` (function) component `vector_lifecycle_requires_config [function]` (`2f4013d3-56a8-5759-bbff-f1ffa6a70a50`) lines 223-243 [crates/gcode/src/commands/vector.rs:223-243]
  - Signature: `fn vector_lifecycle_requires_config() {`
  - Purpose: Verifies that vector lifecycle construction fails with 'MissingQdrantConfig' when Qdrant config is absent, fails with 'MissingEmbeddingConfig' when embedding config is absent, and succeeds when both a Qdrant config and daemon embedding source are provided. [crates/gcode/src/commands/vector.rs:223-243]
- `lifecycle_json_contract` (function) component `lifecycle_json_contract [function]` (`5080141d-e66d-5efe-bee6-27ddd26b2da5`) lines 246-304 [crates/gcode/src/commands/vector.rs:246-304]
  - Signature: `fn lifecycle_json_contract() {`
  - Purpose: Verifies that 'lifecycle_json_payload' serializes a 'CodeSymbolVectorLifecycleOutput' plus 'ProjectionSyncReport' into the expected JSON shape and field values, including both OK and degraded projection states. [crates/gcode/src/commands/vector.rs:246-304]

