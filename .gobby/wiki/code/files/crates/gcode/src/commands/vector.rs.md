---
title: crates/gcode/src/commands/vector.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/vector.rs
  ranges:
  - 12-18
  - 20-24
  - 26-41
  - 43-62
  - 64-71
  - 73-83
  - 85-95
  - 98-114
  - 116-136
  - 145-159
  - 161-166
  - 168-184
  - 187-207
  - 210-268
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/vector.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

The file manages the vector lifecycle for code symbols, coordinating between indexed code metadata and a Qdrant vector database. It provides core operations including constructing lifecycle instances from context and embedding sources (lifecycle_from_context, lifecycle_from_resolved_embedding_source), performing lifecycle actions like syncing files to vectors (sync_file), clearing and rebuilding collections (clear, rebuild), and querying lifecycle status (lifecycle_status). The module wraps the underlying CodeSymbolVectorLifecycle to handle project-specific configuration, database connectivity, and formatted output reporting (print_lifecycle_output). Support functions build configuration objects (qdrant_config, daemon_embedding_source), construct contexts (make_ctx), validate required configuration (vector_lifecycle_requires_config), and serialize status as JSON payloads (lifecycle_json_payload, VectorLifecycleJsonPayload).
[crates/gcode/src/commands/vector.rs:12-18]
[crates/gcode/src/commands/vector.rs:20-24]
[crates/gcode/src/commands/vector.rs:26-41]
[crates/gcode/src/commands/vector.rs:43-62]
[crates/gcode/src/commands/vector.rs:64-71]

## API Symbols

- `lifecycle_status` (function) component `lifecycle_status [function]` (`356461b5-4bb7-58d2-990d-5cb9f865d3ee`) lines 12-18 [crates/gcode/src/commands/vector.rs:12-18]
  - Signature: `pub fn lifecycle_status(`
  - Purpose: Indexed function `lifecycle_status` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:12-18]
- `lifecycle_from_context` (function) component `lifecycle_from_context [function]` (`1a57d4f7-9ff3-5405-a3eb-039d0f3d8eda`) lines 20-24 [crates/gcode/src/commands/vector.rs:20-24]
  - Signature: `pub(crate) fn lifecycle_from_context(`
  - Purpose: Indexed function `lifecycle_from_context` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:20-24]
- `lifecycle_from_resolved_embedding_source` (function) component `lifecycle_from_resolved_embedding_source [function]` (`4aaf04a5-d95f-5020-be3f-09f5880e610b`) lines 26-41 [crates/gcode/src/commands/vector.rs:26-41]
  - Signature: `fn lifecycle_from_resolved_embedding_source(`
  - Purpose: Indexed function `lifecycle_from_resolved_embedding_source` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:26-41]
- `sync_file` (function) component `sync_file [function]` (`03804e55-1653-5e20-9e60-d9becc5a799b`) lines 43-62 [crates/gcode/src/commands/vector.rs:43-62]
  - Signature: `pub fn sync_file(ctx: &Context, file_path: &str, format: Format) -> anyhow::Result<()> {`
  - Purpose: Indexed function `sync_file` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:43-62]
- `clear` (function) component `clear [function]` (`81f53124-5cbb-5248-9eef-15b86ceb810d`) lines 64-71 [crates/gcode/src/commands/vector.rs:64-71]
  - Signature: `pub fn clear(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Indexed function `clear` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:64-71]
- `rebuild` (function) component `rebuild [function]` (`778f3eee-94df-573c-b119-850ca89ea9a5`) lines 73-83 [crates/gcode/src/commands/vector.rs:73-83]
  - Signature: `pub fn rebuild(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Indexed function `rebuild` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:73-83]
- `print_lifecycle_output` (function) component `print_lifecycle_output [function]` (`55648085-91c5-5864-83a1-ef83e42c6fa9`) lines 85-95 [crates/gcode/src/commands/vector.rs:85-95]
  - Signature: `fn print_lifecycle_output(`
  - Purpose: Indexed function `print_lifecycle_output` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:85-95]
- `VectorLifecycleJsonPayload` (class) component `VectorLifecycleJsonPayload [class]` (`a452f2bd-f89c-5a56-baac-f59774b2d8b5`) lines 98-114 [crates/gcode/src/commands/vector.rs:98-114]
  - Signature: `pub(crate) struct VectorLifecycleJsonPayload {`
  - Purpose: Indexed class `VectorLifecycleJsonPayload` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:98-114]
- `lifecycle_json_payload` (function) component `lifecycle_json_payload [function]` (`542cfbc8-254d-51a1-b76f-90eb4ee4c9b9`) lines 116-136 [crates/gcode/src/commands/vector.rs:116-136]
  - Signature: `pub(crate) fn lifecycle_json_payload(`
  - Purpose: Indexed function `lifecycle_json_payload` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:116-136]
- `make_ctx` (function) component `make_ctx [function]` (`24b12c0f-2f94-5fd4-988f-3c9dd44f2763`) lines 145-159 [crates/gcode/src/commands/vector.rs:145-159]
  - Signature: `fn make_ctx() -> Context {`
  - Purpose: Indexed function `make_ctx` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:145-159]
- `qdrant_config` (function) component `qdrant_config [function]` (`5a6d85c2-ea41-5aa6-bf0b-0987652f611e`) lines 161-166 [crates/gcode/src/commands/vector.rs:161-166]
  - Signature: `fn qdrant_config() -> crate::config::QdrantConfig {`
  - Purpose: Indexed function `qdrant_config` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:161-166]
- `daemon_embedding_source` (function) component `daemon_embedding_source [function]` (`641c24a6-b147-5ade-ac3f-1161c65226c8`) lines 168-184 [crates/gcode/src/commands/vector.rs:168-184]
  - Signature: `fn daemon_embedding_source() -> EmbeddingSource {`
  - Purpose: Indexed function `daemon_embedding_source` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:168-184]
- `vector_lifecycle_requires_config` (function) component `vector_lifecycle_requires_config [function]` (`2cc0d68a-d05e-5467-baf1-f044d9713266`) lines 187-207 [crates/gcode/src/commands/vector.rs:187-207]
  - Signature: `fn vector_lifecycle_requires_config() {`
  - Purpose: Indexed function `vector_lifecycle_requires_config` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:187-207]
- `lifecycle_json_contract` (function) component `lifecycle_json_contract [function]` (`b6018ece-6193-5ead-9935-149b4aae2c62`) lines 210-268 [crates/gcode/src/commands/vector.rs:210-268]
  - Signature: `fn lifecycle_json_contract() {`
  - Purpose: Indexed function `lifecycle_json_contract` in `crates/gcode/src/commands/vector.rs`. [crates/gcode/src/commands/vector.rs:210-268]

