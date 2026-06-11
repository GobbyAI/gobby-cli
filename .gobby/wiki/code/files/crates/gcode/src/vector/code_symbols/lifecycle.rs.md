---
title: crates/gcode/src/vector/code_symbols/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
  ranges:
  - 29-37
  - 39-43
  - 45-56
  - 58-376
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

# crates/gcode/src/vector/code_symbols/lifecycle.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

`crates/gcode/src/vector/code_symbols/lifecycle.rs` exposes 24 indexed API symbols.
[crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:58-376]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82]

## API Symbols

- `CodeSymbolVectorLifecycle` (class) component `CodeSymbolVectorLifecycle [class]` (`0248dc7f-c15d-57e0-b0e5-d01474551f24`) lines 29-37 [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]
  - Signature: `pub struct CodeSymbolVectorLifecycle {`
  - Purpose: Indexed class `CodeSymbolVectorLifecycle` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]
- `resolve_lifecycle_qdrant_config` (function) component `resolve_lifecycle_qdrant_config [function]` (`d09cbdf3-4bb8-57cf-bde2-ec364e34db0d`) lines 39-43 [crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43]
  - Signature: `pub fn resolve_lifecycle_qdrant_config(`
  - Purpose: Indexed function `resolve_lifecycle_qdrant_config` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43]
- `lifecycle_status` (function) component `lifecycle_status [function]` (`453c36c5-c71e-5ea5-ad42-ba8eb1b45dc7`) lines 45-56 [crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56]
  - Signature: `pub fn lifecycle_status(`
  - Purpose: Indexed function `lifecycle_status` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56]
- `CodeSymbolVectorLifecycle` (class) component `CodeSymbolVectorLifecycle [class]` (`4252d8b2-a42a-528d-86e7-72c0177ae17e`) lines 58-376 [crates/gcode/src/vector/code_symbols/lifecycle.rs:58-376]
  - Signature: `impl CodeSymbolVectorLifecycle {`
  - Purpose: Indexed class `CodeSymbolVectorLifecycle` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:58-376]
- `CodeSymbolVectorLifecycle.new` (method) component `CodeSymbolVectorLifecycle.new [method]` (`5d17f77c-20fa-579e-9499-a6c89612ae3b`) lines 59-82 [crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82]
  - Signature: `pub fn new(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.new` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82]
- `CodeSymbolVectorLifecycle.collection` (method) component `CodeSymbolVectorLifecycle.collection [method]` (`25527c57-d44a-5f35-9c4f-c70d856105f2`) lines 84-86 [crates/gcode/src/vector/code_symbols/lifecycle.rs:84-86]
  - Signature: `pub fn collection(&self) -> &str {`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.collection` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:84-86]
- `CodeSymbolVectorLifecycle.ensure_collection` (method) component `CodeSymbolVectorLifecycle.ensure_collection [method]` (`743bc508-89a2-559c-8b66-e29afa7f77c7`) lines 88-98 [crates/gcode/src/vector/code_symbols/lifecycle.rs:88-98]
  - Signature: `pub fn ensure_collection(&mut self) -> Result<VectorCollectionSchema, VectorLifecycleError> {`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.ensure_collection` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:88-98]
- `CodeSymbolVectorLifecycle.sync_file_symbols` (method) component `CodeSymbolVectorLifecycle.sync_file_symbols [method]` (`52aeda26-6804-5faf-89e0-ded9618d7d95`) lines 100-118 [crates/gcode/src/vector/code_symbols/lifecycle.rs:100-118]
  - Signature: `pub fn sync_file_symbols(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.sync_file_symbols` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:100-118]
- `CodeSymbolVectorLifecycle.clear_project_vectors` (method) component `CodeSymbolVectorLifecycle.clear_project_vectors [method]` (`de1b1007-cf93-5a44-b636-9fdc6e8da25a`) lines 120-141 [crates/gcode/src/vector/code_symbols/lifecycle.rs:120-141]
  - Signature: `pub fn clear_project_vectors(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.clear_project_vectors` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:120-141]
- `CodeSymbolVectorLifecycle.rebuild_symbols` (method) component `CodeSymbolVectorLifecycle.rebuild_symbols [method]` (`bdbeae70-257b-5ac4-a4e0-905da7f8af57`) lines 143-160 [crates/gcode/src/vector/code_symbols/lifecycle.rs:143-160]
  - Signature: `pub fn rebuild_symbols(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.rebuild_symbols` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:143-160]
- `CodeSymbolVectorLifecycle.output` (method) component `CodeSymbolVectorLifecycle.output [method]` (`6cea2e87-eec6-5287-af1e-b9428af70da1`) lines 162-182 [crates/gcode/src/vector/code_symbols/lifecycle.rs:162-182]
  - Signature: `fn output(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.output` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:162-182]
- `CodeSymbolVectorLifecycle.expected_schema` (method) component `CodeSymbolVectorLifecycle.expected_schema [method]` (`23282e34-a1e7-5437-9cf9-e52d2d3e6221`) lines 184-201 [crates/gcode/src/vector/code_symbols/lifecycle.rs:184-201]
  - Signature: `fn expected_schema(&mut self) -> Result<VectorCollectionSchema, VectorLifecycleError> {`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.expected_schema` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:184-201]
- `CodeSymbolVectorLifecycle.require_qdrant_boundary` (method) component `CodeSymbolVectorLifecycle.require_qdrant_boundary [method]` (`2236ba22-7da0-5e9b-852a-657cdbf625de`) lines 203-205 [crates/gcode/src/vector/code_symbols/lifecycle.rs:203-205]
  - Signature: `fn require_qdrant_boundary(&self) -> Result<(), VectorLifecycleError> {`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.require_qdrant_boundary` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:203-205]
- `CodeSymbolVectorLifecycle.require_qdrant_boundary_config` (method) component `CodeSymbolVectorLifecycle.require_qdrant_boundary_config [method]` (`45b020d7-47a9-5d75-bb8d-b191dd51942d`) lines 207-217 [crates/gcode/src/vector/code_symbols/lifecycle.rs:207-217]
  - Signature: `fn require_qdrant_boundary_config(qdrant: &QdrantConfig) -> Result<(), VectorLifecycleError> {`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.require_qdrant_boundary_config` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:207-217]
- `CodeSymbolVectorLifecycle.ensure_compatible_schema` (method) component `CodeSymbolVectorLifecycle.ensure_compatible_schema [method]` (`5d5a0e28-8001-5666-b446-cae92242d292`) lines 219-240 [crates/gcode/src/vector/code_symbols/lifecycle.rs:219-240]
  - Signature: `fn ensure_compatible_schema(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.ensure_compatible_schema` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:219-240]
- `CodeSymbolVectorLifecycle.get_collection_schema` (method) component `CodeSymbolVectorLifecycle.get_collection_schema [method]` (`8cc7a803-e403-5c0c-9921-4b3b53ec1ff3`) lines 242-261 [crates/gcode/src/vector/code_symbols/lifecycle.rs:242-261]
  - Signature: `fn get_collection_schema(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.get_collection_schema` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:242-261]
- `CodeSymbolVectorLifecycle.create_collection` (method) component `CodeSymbolVectorLifecycle.create_collection [method]` (`c65ed172-fac5-5e0e-9ba7-488ec324fca8`) lines 263-282 [crates/gcode/src/vector/code_symbols/lifecycle.rs:263-282]
  - Signature: `fn create_collection(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.create_collection` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:263-282]
- `CodeSymbolVectorLifecycle.delete_vectors` (method) component `CodeSymbolVectorLifecycle.delete_vectors [method]` (`e481c014-41cb-5c53-a7e9-4128b0362c7d`) lines 284-292 [crates/gcode/src/vector/code_symbols/lifecycle.rs:284-292]
  - Signature: `fn delete_vectors(&self, file_path: Option<&str>) -> Result<usize, VectorLifecycleError> {`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.delete_vectors` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:284-292]
- `CodeSymbolVectorLifecycle.delete_stale_vectors` (method) component `CodeSymbolVectorLifecycle.delete_stale_vectors [method]` (`de594626-fe18-54e5-81ed-e34d6198b406`) lines 294-307 [crates/gcode/src/vector/code_symbols/lifecycle.rs:294-307]
  - Signature: `fn delete_stale_vectors(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.delete_stale_vectors` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:294-307]
- `CodeSymbolVectorLifecycle.upsert_points` (method) component `CodeSymbolVectorLifecycle.upsert_points [method]` (`a0640a4e-2d32-582c-90fe-3cf870fa0026`) lines 309-326 [crates/gcode/src/vector/code_symbols/lifecycle.rs:309-326]
  - Signature: `fn upsert_points(&self, points: Vec<UpsertRequest>) -> Result<usize, VectorLifecycleError> {`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.upsert_points` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:309-326]
- `CodeSymbolVectorLifecycle.points_for_symbols` (method) component `CodeSymbolVectorLifecycle.points_for_symbols [method]` (`8320fb2a-1627-5f5d-854a-7dc3d656afcd`) lines 328-367 [crates/gcode/src/vector/code_symbols/lifecycle.rs:328-367]
  - Signature: `fn points_for_symbols(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.points_for_symbols` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:328-367]
- `CodeSymbolVectorLifecycle.qdrant_request` (method) component `CodeSymbolVectorLifecycle.qdrant_request [method]` (`fa63f5e2-5fc6-5644-8e7c-1986aa30319a`) lines 369-375 [crates/gcode/src/vector/code_symbols/lifecycle.rs:369-375]
  - Signature: `fn qdrant_request(`
  - Purpose: Indexed method `CodeSymbolVectorLifecycle.qdrant_request` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:369-375]
- `payload_map` (function) component `payload_map [function]` (`9644ea59-e921-5ce7-af06-12ab75c1073e`) lines 378-389 [crates/gcode/src/vector/code_symbols/lifecycle.rs:378-389]
  - Signature: `fn payload_map(`
  - Purpose: Indexed function `payload_map` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:378-389]
- `point_ids` (function) component `point_ids [function]` (`fbcf6b62-c2a7-52bd-afd3-3fe6073c5f61`) lines 391-393 [crates/gcode/src/vector/code_symbols/lifecycle.rs:391-393]
  - Signature: `fn point_ids(points: &[UpsertRequest]) -> Vec<String> {`
  - Purpose: Indexed function `point_ids` in `crates/gcode/src/vector/code_symbols/lifecycle.rs`. [crates/gcode/src/vector/code_symbols/lifecycle.rs:391-393]

