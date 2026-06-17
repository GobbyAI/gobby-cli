---
title: crates/gcode/src/vector/code_symbols/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
  ranges:
  - 29-37
  - 39-43
  - 45-56
  - 59-82
  - 84-86
  - 88-98
  - 100-118
  - 120-141
  - 143-160
  - 162-182
  - 184-201
  - 203-205
  - 207-217
  - 219-240
  - 242-261
  - 263-282
  - 284-292
  - 294-307
  - 309-326
  - 328-367
  - 369-375
  - 378-389
  - 391-393
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37](crates/gcode/src/vector/code_symbols/lifecycle.rs#L29-L37), [crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43](crates/gcode/src/vector/code_symbols/lifecycle.rs#L39-L43), [crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56](crates/gcode/src/vector/code_symbols/lifecycle.rs#L45-L56), [crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82](crates/gcode/src/vector/code_symbols/lifecycle.rs#L59-L82), [crates/gcode/src/vector/code_symbols/lifecycle.rs:84-86](crates/gcode/src/vector/code_symbols/lifecycle.rs#L84-L86), [crates/gcode/src/vector/code_symbols/lifecycle.rs:88-98](crates/gcode/src/vector/code_symbols/lifecycle.rs#L88-L98), [crates/gcode/src/vector/code_symbols/lifecycle.rs:100-118](crates/gcode/src/vector/code_symbols/lifecycle.rs#L100-L118), [crates/gcode/src/vector/code_symbols/lifecycle.rs:120-141](crates/gcode/src/vector/code_symbols/lifecycle.rs#L120-L141), [crates/gcode/src/vector/code_symbols/lifecycle.rs:143-160](crates/gcode/src/vector/code_symbols/lifecycle.rs#L143-L160), [crates/gcode/src/vector/code_symbols/lifecycle.rs:162-182](crates/gcode/src/vector/code_symbols/lifecycle.rs#L162-L182), [crates/gcode/src/vector/code_symbols/lifecycle.rs:184-201](crates/gcode/src/vector/code_symbols/lifecycle.rs#L184-L201), [crates/gcode/src/vector/code_symbols/lifecycle.rs:203-205](crates/gcode/src/vector/code_symbols/lifecycle.rs#L203-L205), [crates/gcode/src/vector/code_symbols/lifecycle.rs:207-217](crates/gcode/src/vector/code_symbols/lifecycle.rs#L207-L217), [crates/gcode/src/vector/code_symbols/lifecycle.rs:219-240](crates/gcode/src/vector/code_symbols/lifecycle.rs#L219-L240), [crates/gcode/src/vector/code_symbols/lifecycle.rs:242-261](crates/gcode/src/vector/code_symbols/lifecycle.rs#L242-L261), [crates/gcode/src/vector/code_symbols/lifecycle.rs:263-282](crates/gcode/src/vector/code_symbols/lifecycle.rs#L263-L282), [crates/gcode/src/vector/code_symbols/lifecycle.rs:284-292](crates/gcode/src/vector/code_symbols/lifecycle.rs#L284-L292), [crates/gcode/src/vector/code_symbols/lifecycle.rs:294-307](crates/gcode/src/vector/code_symbols/lifecycle.rs#L294-L307), [crates/gcode/src/vector/code_symbols/lifecycle.rs:309-326](crates/gcode/src/vector/code_symbols/lifecycle.rs#L309-L326), [crates/gcode/src/vector/code_symbols/lifecycle.rs:328-367](crates/gcode/src/vector/code_symbols/lifecycle.rs#L328-L367), [crates/gcode/src/vector/code_symbols/lifecycle.rs:369-375](crates/gcode/src/vector/code_symbols/lifecycle.rs#L369-L375), [crates/gcode/src/vector/code_symbols/lifecycle.rs:378-389](crates/gcode/src/vector/code_symbols/lifecycle.rs#L378-L389), [crates/gcode/src/vector/code_symbols/lifecycle.rs:391-393](crates/gcode/src/vector/code_symbols/lifecycle.rs#L391-L393)

</details>

# crates/gcode/src/vector/code_symbols/lifecycle.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

Implements the lifecycle manager for project code-symbol vectors stored in Qdrant. `CodeSymbolVectorLifecycle` ties together project/config state, embedding generation, and Qdrant HTTP requests to resolve collection setup, validate or create compatible schemas, sync symbols in batches, delete stale or targeted vectors, and build lifecycle/status/output records; the small free functions provide Qdrant config resolution, lifecycle status construction, and point payload/id helpers used by those operations.
[crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:84-86]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CodeSymbolVectorLifecycle` | class | `pub struct CodeSymbolVectorLifecycle {` | `CodeSymbolVectorLifecycle [class]` | `0248dc7f-c15d-57e0-b0e5-d01474551f24` | 29-37 [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37] | Indexed class `CodeSymbolVectorLifecycle` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37] |
| `resolve_lifecycle_qdrant_config` | function | `pub fn resolve_lifecycle_qdrant_config(` | `resolve_lifecycle_qdrant_config [function]` | `d09cbdf3-4bb8-57cf-bde2-ec364e34db0d` | 39-43 [crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43] | Indexed function `resolve_lifecycle_qdrant_config` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43] |
| `lifecycle_status` | function | `pub fn lifecycle_status(` | `lifecycle_status [function]` | `453c36c5-c71e-5ea5-ad42-ba8eb1b45dc7` | 45-56 [crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56] | Indexed function `lifecycle_status` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56] |
| `CodeSymbolVectorLifecycle::new` | method | `pub fn new(` | `CodeSymbolVectorLifecycle::new [method]` | `5d17f77c-20fa-579e-9499-a6c89612ae3b` | 59-82 [crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82] | Indexed method `CodeSymbolVectorLifecycle::new` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82] |
| `CodeSymbolVectorLifecycle::collection` | method | `pub fn collection(&self) -> &str {` | `CodeSymbolVectorLifecycle::collection [method]` | `25527c57-d44a-5f35-9c4f-c70d856105f2` | 84-86 [crates/gcode/src/vector/code_symbols/lifecycle.rs:84-86] | Indexed method `CodeSymbolVectorLifecycle::collection` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:84-86] |
| `CodeSymbolVectorLifecycle::ensure_collection` | method | `pub fn ensure_collection(&mut self) -> Result<VectorCollectionSchema, VectorLifecycleError> {` | `CodeSymbolVectorLifecycle::ensure_collection [method]` | `743bc508-89a2-559c-8b66-e29afa7f77c7` | 88-98 [crates/gcode/src/vector/code_symbols/lifecycle.rs:88-98] | Indexed method `CodeSymbolVectorLifecycle::ensure_collection` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:88-98] |
| `CodeSymbolVectorLifecycle::sync_file_symbols` | method | `pub fn sync_file_symbols(` | `CodeSymbolVectorLifecycle::sync_file_symbols [method]` | `52aeda26-6804-5faf-89e0-ded9618d7d95` | 100-118 [crates/gcode/src/vector/code_symbols/lifecycle.rs:100-118] | Indexed method `CodeSymbolVectorLifecycle::sync_file_symbols` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:100-118] |
| `CodeSymbolVectorLifecycle::clear_project_vectors` | method | `pub fn clear_project_vectors(` | `CodeSymbolVectorLifecycle::clear_project_vectors [method]` | `de1b1007-cf93-5a44-b636-9fdc6e8da25a` | 120-141 [crates/gcode/src/vector/code_symbols/lifecycle.rs:120-141] | Indexed method `CodeSymbolVectorLifecycle::clear_project_vectors` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:120-141] |
| `CodeSymbolVectorLifecycle::rebuild_symbols` | method | `pub fn rebuild_symbols(` | `CodeSymbolVectorLifecycle::rebuild_symbols [method]` | `bdbeae70-257b-5ac4-a4e0-905da7f8af57` | 143-160 [crates/gcode/src/vector/code_symbols/lifecycle.rs:143-160] | Indexed method `CodeSymbolVectorLifecycle::rebuild_symbols` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:143-160] |
| `CodeSymbolVectorLifecycle::output` | method | `fn output(` | `CodeSymbolVectorLifecycle::output [method]` | `6cea2e87-eec6-5287-af1e-b9428af70da1` | 162-182 [crates/gcode/src/vector/code_symbols/lifecycle.rs:162-182] | Indexed method `CodeSymbolVectorLifecycle::output` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:162-182] |
| `CodeSymbolVectorLifecycle::expected_schema` | method | `fn expected_schema(&mut self) -> Result<VectorCollectionSchema, VectorLifecycleError> {` | `CodeSymbolVectorLifecycle::expected_schema [method]` | `23282e34-a1e7-5437-9cf9-e52d2d3e6221` | 184-201 [crates/gcode/src/vector/code_symbols/lifecycle.rs:184-201] | Indexed method `CodeSymbolVectorLifecycle::expected_schema` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:184-201] |
| `CodeSymbolVectorLifecycle::require_qdrant_boundary` | method | `fn require_qdrant_boundary(&self) -> Result<(), VectorLifecycleError> {` | `CodeSymbolVectorLifecycle::require_qdrant_boundary [method]` | `2236ba22-7da0-5e9b-852a-657cdbf625de` | 203-205 [crates/gcode/src/vector/code_symbols/lifecycle.rs:203-205] | Indexed method `CodeSymbolVectorLifecycle::require_qdrant_boundary` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:203-205] |
| `CodeSymbolVectorLifecycle::require_qdrant_boundary_config` | method | `fn require_qdrant_boundary_config(qdrant: &QdrantConfig) -> Result<(), VectorLifecycleError> {` | `CodeSymbolVectorLifecycle::require_qdrant_boundary_config [method]` | `45b020d7-47a9-5d75-bb8d-b191dd51942d` | 207-217 [crates/gcode/src/vector/code_symbols/lifecycle.rs:207-217] | Indexed method `CodeSymbolVectorLifecycle::require_qdrant_boundary_config` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:207-217] |
| `CodeSymbolVectorLifecycle::ensure_compatible_schema` | method | `fn ensure_compatible_schema(` | `CodeSymbolVectorLifecycle::ensure_compatible_schema [method]` | `5d5a0e28-8001-5666-b446-cae92242d292` | 219-240 [crates/gcode/src/vector/code_symbols/lifecycle.rs:219-240] | Indexed method `CodeSymbolVectorLifecycle::ensure_compatible_schema` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:219-240] |
| `CodeSymbolVectorLifecycle::get_collection_schema` | method | `fn get_collection_schema(` | `CodeSymbolVectorLifecycle::get_collection_schema [method]` | `8cc7a803-e403-5c0c-9921-4b3b53ec1ff3` | 242-261 [crates/gcode/src/vector/code_symbols/lifecycle.rs:242-261] | Indexed method `CodeSymbolVectorLifecycle::get_collection_schema` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:242-261] |
| `CodeSymbolVectorLifecycle::create_collection` | method | `fn create_collection(` | `CodeSymbolVectorLifecycle::create_collection [method]` | `c65ed172-fac5-5e0e-9ba7-488ec324fca8` | 263-282 [crates/gcode/src/vector/code_symbols/lifecycle.rs:263-282] | Indexed method `CodeSymbolVectorLifecycle::create_collection` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:263-282] |
| `CodeSymbolVectorLifecycle::delete_vectors` | method | `fn delete_vectors(&self, file_path: Option<&str>) -> Result<usize, VectorLifecycleError> {` | `CodeSymbolVectorLifecycle::delete_vectors [method]` | `e481c014-41cb-5c53-a7e9-4128b0362c7d` | 284-292 [crates/gcode/src/vector/code_symbols/lifecycle.rs:284-292] | Indexed method `CodeSymbolVectorLifecycle::delete_vectors` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:284-292] |
| `CodeSymbolVectorLifecycle::delete_stale_vectors` | method | `fn delete_stale_vectors(` | `CodeSymbolVectorLifecycle::delete_stale_vectors [method]` | `de594626-fe18-54e5-81ed-e34d6198b406` | 294-307 [crates/gcode/src/vector/code_symbols/lifecycle.rs:294-307] | Indexed method `CodeSymbolVectorLifecycle::delete_stale_vectors` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:294-307] |
| `CodeSymbolVectorLifecycle::upsert_points` | method | `fn upsert_points(&self, points: Vec<UpsertRequest>) -> Result<usize, VectorLifecycleError> {` | `CodeSymbolVectorLifecycle::upsert_points [method]` | `a0640a4e-2d32-582c-90fe-3cf870fa0026` | 309-326 [crates/gcode/src/vector/code_symbols/lifecycle.rs:309-326] | Indexed method `CodeSymbolVectorLifecycle::upsert_points` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:309-326] |
| `CodeSymbolVectorLifecycle::points_for_symbols` | method | `fn points_for_symbols(` | `CodeSymbolVectorLifecycle::points_for_symbols [method]` | `8320fb2a-1627-5f5d-854a-7dc3d656afcd` | 328-367 [crates/gcode/src/vector/code_symbols/lifecycle.rs:328-367] | Indexed method `CodeSymbolVectorLifecycle::points_for_symbols` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:328-367] |
| `CodeSymbolVectorLifecycle::qdrant_request` | method | `fn qdrant_request(` | `CodeSymbolVectorLifecycle::qdrant_request [method]` | `fa63f5e2-5fc6-5644-8e7c-1986aa30319a` | 369-375 [crates/gcode/src/vector/code_symbols/lifecycle.rs:369-375] | Indexed method `CodeSymbolVectorLifecycle::qdrant_request` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:369-375] |
| `payload_map` | function | `fn payload_map(` | `payload_map [function]` | `9644ea59-e921-5ce7-af06-12ab75c1073e` | 378-389 [crates/gcode/src/vector/code_symbols/lifecycle.rs:378-389] | Indexed function `payload_map` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:378-389] |
| `point_ids` | function | `fn point_ids(points: &[UpsertRequest]) -> Vec<String> {` | `point_ids [function]` | `fbcf6b62-c2a7-52bd-afd3-3fe6073c5f61` | 391-393 [crates/gcode/src/vector/code_symbols/lifecycle.rs:391-393] | Indexed function `point_ids` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:391-393] |
