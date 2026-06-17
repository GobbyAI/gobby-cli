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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/vector.rs:13-19](crates/gcode/src/commands/vector.rs#L13-L19), [crates/gcode/src/commands/vector.rs:21-25](crates/gcode/src/commands/vector.rs#L21-L25), [crates/gcode/src/commands/vector.rs:27-42](crates/gcode/src/commands/vector.rs#L27-L42), [crates/gcode/src/commands/vector.rs:44-63](crates/gcode/src/commands/vector.rs#L44-L63), [crates/gcode/src/commands/vector.rs:65-72](crates/gcode/src/commands/vector.rs#L65-L72), [crates/gcode/src/commands/vector.rs:74-84](crates/gcode/src/commands/vector.rs#L74-L84), [crates/gcode/src/commands/vector.rs:86-98](crates/gcode/src/commands/vector.rs#L86-L98), [crates/gcode/src/commands/vector.rs:100-110](crates/gcode/src/commands/vector.rs#L100-L110), [crates/gcode/src/commands/vector.rs:112-131](crates/gcode/src/commands/vector.rs#L112-L131), [crates/gcode/src/commands/vector.rs:134-150](crates/gcode/src/commands/vector.rs#L134-L150), [crates/gcode/src/commands/vector.rs:152-172](crates/gcode/src/commands/vector.rs#L152-L172), [crates/gcode/src/commands/vector.rs:181-195](crates/gcode/src/commands/vector.rs#L181-L195), [crates/gcode/src/commands/vector.rs:197-202](crates/gcode/src/commands/vector.rs#L197-L202), [crates/gcode/src/commands/vector.rs:204-220](crates/gcode/src/commands/vector.rs#L204-L220), [crates/gcode/src/commands/vector.rs:223-243](crates/gcode/src/commands/vector.rs#L223-L243), [crates/gcode/src/commands/vector.rs:246-304](crates/gcode/src/commands/vector.rs#L246-L304)

</details>

# crates/gcode/src/commands/vector.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

This file implements the `gcode` vector-management commands for code symbols. It wraps the lower-level `code_symbols` lifecycle API with helpers that build a `CodeSymbolVectorLifecycle` from the current `Context`, require Qdrant and embedding configuration, and expose operations like status lookup, syncing a single file, clearing collections, rebuilding vectors, and cleaning up orphaned vectors. The sync path validates that the file is indexed, fetches its symbols from the database, applies them through the lifecycle, marks the file as synced, and prints a lifecycle report. It also defines JSON payload types and tests to keep the lifecycle output contract stable.
[crates/gcode/src/commands/vector.rs:13-19]
[crates/gcode/src/commands/vector.rs:21-25]
[crates/gcode/src/commands/vector.rs:27-42]
[crates/gcode/src/commands/vector.rs:44-63]
[crates/gcode/src/commands/vector.rs:65-72]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `lifecycle_status` | function | `pub fn lifecycle_status(` | `lifecycle_status [function]` | `28fec698-1b64-5ca2-badf-b1c1f8eae721` | 13-19 [crates/gcode/src/commands/vector.rs:13-19] | Indexed function `lifecycle_status` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:13-19] |
| `lifecycle_from_context` | function | `pub(crate) fn lifecycle_from_context(` | `lifecycle_from_context [function]` | `056d3555-6fcc-598a-b863-88f38c81af45` | 21-25 [crates/gcode/src/commands/vector.rs:21-25] | Indexed function `lifecycle_from_context` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:21-25] |
| `lifecycle_from_resolved_embedding_source` | function | `fn lifecycle_from_resolved_embedding_source(` | `lifecycle_from_resolved_embedding_source [function]` | `ebbccf33-77b9-522f-8762-f93b08c0a423` | 27-42 [crates/gcode/src/commands/vector.rs:27-42] | Indexed function `lifecycle_from_resolved_embedding_source` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:27-42] |
| `sync_file` | function | `pub fn sync_file(ctx: &Context, file_path: &str, format: Format) -> anyhow::Result<()> {` | `sync_file [function]` | `faff068c-165b-5b51-a584-f98081d6fdeb` | 44-63 [crates/gcode/src/commands/vector.rs:44-63] | Indexed function `sync_file` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:44-63] |
| `clear` | function | `pub fn clear(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `clear [function]` | `9ad3d844-f4e7-5a55-9e58-0de1a383655e` | 65-72 [crates/gcode/src/commands/vector.rs:65-72] | Indexed function `clear` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:65-72] |
| `rebuild` | function | `pub fn rebuild(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `rebuild [function]` | `f89801cd-0fba-59ea-a695-54ff60349b32` | 74-84 [crates/gcode/src/commands/vector.rs:74-84] | Indexed function `rebuild` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:74-84] |
| `cleanup_orphans` | function | `pub fn cleanup_orphans(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `cleanup_orphans [function]` | `f02502f7-48e7-5f50-bfda-fc5ac0432e29` | 86-98 [crates/gcode/src/commands/vector.rs:86-98] | Indexed function `cleanup_orphans` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:86-98] |
| `print_lifecycle_output` | function | `fn print_lifecycle_output(` | `print_lifecycle_output [function]` | `b6a83260-1b23-575c-ad7a-75a10b45d151` | 100-110 [crates/gcode/src/commands/vector.rs:100-110] | Indexed function `print_lifecycle_output` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:100-110] |
| `print_orphan_cleanup` | function | `fn print_orphan_cleanup(cleanup: &VectorOrphanCleanup, format: Format) -> anyhow::Result<()> {` | `print_orphan_cleanup [function]` | `58b3a93a-7213-512d-96ad-bc2e68539ccc` | 112-131 [crates/gcode/src/commands/vector.rs:112-131] | Indexed function `print_orphan_cleanup` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:112-131] |
| `VectorLifecycleJsonPayload` | class | `pub(crate) struct VectorLifecycleJsonPayload {` | `VectorLifecycleJsonPayload [class]` | `10ab8c31-c0c7-55dc-a750-d05c9e0ceb28` | 134-150 [crates/gcode/src/commands/vector.rs:134-150] | Indexed class `VectorLifecycleJsonPayload` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:134-150] |
| `lifecycle_json_payload` | function | `pub(crate) fn lifecycle_json_payload(` | `lifecycle_json_payload [function]` | `d58fe363-48f3-5bcc-9ee8-aa397fd8df4b` | 152-172 [crates/gcode/src/commands/vector.rs:152-172] | Indexed function `lifecycle_json_payload` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:152-172] |
| `make_ctx` | function | `fn make_ctx() -> Context {` | `make_ctx [function]` | `3fd7061d-0134-5744-b205-0aa6cf6e9364` | 181-195 [crates/gcode/src/commands/vector.rs:181-195] | Indexed function `make_ctx` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:181-195] |
| `qdrant_config` | function | `fn qdrant_config() -> crate::config::QdrantConfig {` | `qdrant_config [function]` | `535a0b67-cd6d-594d-b4f7-6492c9cc6233` | 197-202 [crates/gcode/src/commands/vector.rs:197-202] | Indexed function `qdrant_config` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:197-202] |
| `daemon_embedding_source` | function | `fn daemon_embedding_source() -> EmbeddingSource {` | `daemon_embedding_source [function]` | `e128fda4-599b-58a3-a44a-8e0f4e76006e` | 204-220 [crates/gcode/src/commands/vector.rs:204-220] | Indexed function `daemon_embedding_source` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:204-220] |
| `vector_lifecycle_requires_config` | function | `fn vector_lifecycle_requires_config() {` | `vector_lifecycle_requires_config [function]` | `2f4013d3-56a8-5759-bbff-f1ffa6a70a50` | 223-243 [crates/gcode/src/commands/vector.rs:223-243] | Indexed function `vector_lifecycle_requires_config` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:223-243] |
| `lifecycle_json_contract` | function | `fn lifecycle_json_contract() {` | `lifecycle_json_contract [function]` | `5080141d-e66d-5efe-bee6-27ddd26b2da5` | 246-304 [crates/gcode/src/commands/vector.rs:246-304] | Indexed function `lifecycle_json_contract` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:246-304] |
