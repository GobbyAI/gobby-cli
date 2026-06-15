---
title: crates/gcode/src/graph/code_graph/read/relationships.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
  ranges:
  - 16-26
  - 28-38
  - 40-51
  - 53-64
  - 66-79
  - 81-90
  - 92-105
  - 107-123
  - 125-138
  - 140-156
  - 158-164
  - 166-177
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/relationships.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

This file provides read-side graph relationship helpers over the optional core graph for a project. It wraps typed queries to count callers and usages, fetch paginated callers/usages as `GraphResult`s, return caller and usage ID lists, run batch caller/callee lookups, retrieve imports for a file, and compute blast-radius nodes. Each function uses the current `Context` and `project_id`, falls back to empty results or `0` when the core graph is unavailable, and shares common conversion helpers to turn raw rows into counts, IDs, or `GraphResult` values.
[crates/gcode/src/graph/code_graph/read/relationships.rs:16-26]
[crates/gcode/src/graph/code_graph/read/relationships.rs:28-38]
[crates/gcode/src/graph/code_graph/read/relationships.rs:40-51]
[crates/gcode/src/graph/code_graph/read/relationships.rs:53-64]
[crates/gcode/src/graph/code_graph/read/relationships.rs:66-79]

## API Symbols

- `count_callers` (function) component `count_callers [function]` (`c1771689-2d42-5a50-92fe-4039cd036f99`) lines 16-26 [crates/gcode/src/graph/code_graph/read/relationships.rs:16-26]
  - Signature: `pub fn count_callers(ctx: &Context, symbol_id: &str) -> anyhow::Result<usize> {`
  - Purpose: Returns the number of callers for 'symbol_id' in 'ctx.project_id' by querying the core graph when available and otherwise falling back to '0'. [crates/gcode/src/graph/code_graph/read/relationships.rs:16-26]
- `count_usages` (function) component `count_usages [function]` (`a19f28c1-bb36-5045-993f-18eb462a5f5d`) lines 28-38 [crates/gcode/src/graph/code_graph/read/relationships.rs:28-38]
  - Signature: `pub fn count_usages(ctx: &Context, symbol_id: &str) -> anyhow::Result<usize> {`
  - Purpose: Returns the number of usage rows for 'symbol_id' in the current project by executing a usage-count query against the core graph client when available, or '0' if the core graph is absent. [crates/gcode/src/graph/code_graph/read/relationships.rs:28-38]
- `find_callers` (function) component `find_callers [function]` (`cf411694-2a2b-5299-893e-98f9a7a0bf1a`) lines 40-51 [crates/gcode/src/graph/code_graph/read/relationships.rs:40-51]
  - Signature: `pub fn find_callers(`
  - Purpose: Queries the optional core graph for callers of the given 'symbol_id' in 'ctx.project_id' using 'offset' and 'limit', then converts the returned rows into a 'Vec<GraphResult>' or returns an empty vector if the graph is unavailable. [crates/gcode/src/graph/code_graph/read/relationships.rs:40-51]
- `find_usages` (function) component `find_usages [function]` (`b25b5be2-7399-5a8c-bc2a-2f26c5d0d8cb`) lines 53-64 [crates/gcode/src/graph/code_graph/read/relationships.rs:53-64]
  - Signature: `pub fn find_usages(`
  - Purpose: Executes a graph query for the given project and symbol ID to retrieve a paginated list of usage 'GraphResult's, returning an empty vector if no core graph is available. [crates/gcode/src/graph/code_graph/read/relationships.rs:53-64]
- `find_caller_ids` (function) component `find_caller_ids [function]` (`e2c6e5ab-a33f-5992-8808-1e6d4e8f55b3`) lines 66-79 [crates/gcode/src/graph/code_graph/read/relationships.rs:66-79]
  - Signature: `pub fn find_caller_ids(`
  - Purpose: Queries the optional core graph for caller rows of the given 'symbol_id' within 'ctx.project_id', up to 'limit', and returns the collected 'id' values as a 'Vec<String>' or an empty vector if no core graph is available. [crates/gcode/src/graph/code_graph/read/relationships.rs:66-79]
- `find_usage_ids` (function) component `find_usage_ids [function]` (`adbe4d4c-401a-5b9a-90b6-6154d18c9a48`) lines 81-90 [crates/gcode/src/graph/code_graph/read/relationships.rs:81-90]
  - Signature: `pub fn find_usage_ids(ctx: &Context, symbol_id: &str, limit: usize) -> anyhow::Result<Vec<String>> {`
  - Purpose: Executes a graph query for usages of 'symbol_id' within 'ctx.project_id' up to 'limit', returning the '"id"' field from each result row as a 'Vec<String>' and propagating any query errors via 'anyhow::Result'. [crates/gcode/src/graph/code_graph/read/relationships.rs:81-90]
- `find_callers_batch` (function) component `find_callers_batch [function]` (`1ece53ce-6f54-5fe9-86ea-b3bec4999fd4`) lines 92-105 [crates/gcode/src/graph/code_graph/read/relationships.rs:92-105]
  - Signature: `pub fn find_callers_batch(`
  - Purpose: Returns an empty vector when 'symbol_ids' is empty, otherwise queries the core graph for callers of the given symbols in the specified project with the provided 'limit' and converts the resulting rows into 'GraphResult' values. [crates/gcode/src/graph/code_graph/read/relationships.rs:92-105]
- `find_caller_ids_batch` (function) component `find_caller_ids_batch [function]` (`be3b899b-6e46-5ab9-be0e-ca3b11420353`) lines 107-123 [crates/gcode/src/graph/code_graph/read/relationships.rs:107-123]
  - Signature: `pub fn find_caller_ids_batch(`
  - Purpose: Returns up to 'limit' caller symbol IDs for the given 'symbol_ids' in the current project by querying the optional core graph and extracting each result row’s 'id' field, returning an empty vector immediately when 'symbol_ids' is empty. [crates/gcode/src/graph/code_graph/read/relationships.rs:107-123]
- `find_callees_batch` (function) component `find_callees_batch [function]` (`a838d1d5-fa4e-57b3-8692-13ed60f53120`) lines 125-138 [crates/gcode/src/graph/code_graph/read/relationships.rs:125-138]
  - Signature: `pub fn find_callees_batch(`
  - Purpose: Returns an empty vector for no input, otherwise queries the core graph for callees of the provided symbol IDs with the given limit and converts each returned row into a 'GraphResult'. [crates/gcode/src/graph/code_graph/read/relationships.rs:125-138]
- `find_callee_ids_batch` (function) component `find_callee_ids_batch [function]` (`fbad7d43-7ee4-5300-94a5-e2d586663235`) lines 140-156 [crates/gcode/src/graph/code_graph/read/relationships.rs:140-156]
  - Signature: `pub fn find_callee_ids_batch(`
  - Purpose: Returns the callee symbol IDs for a batch of input 'symbol_ids' by querying the optional core graph with the project ID and 'limit', returning an empty vector immediately when the input slice is empty. [crates/gcode/src/graph/code_graph/read/relationships.rs:140-156]
- `get_imports` (function) component `get_imports [function]` (`01d6c63f-2f0f-53f2-9bfe-f4a1d4acea53`) lines 158-164 [crates/gcode/src/graph/code_graph/read/relationships.rs:158-164]
  - Signature: `pub fn get_imports(ctx: &Context, file_path: &str) -> anyhow::Result<Vec<GraphResult>> {`
  - Purpose: Builds and executes an imports query for the given 'file_path' in the current project via the optional core graph client, then converts each returned row into a 'GraphResult' and returns them as a 'Vec' wrapped in 'anyhow::Result'. [crates/gcode/src/graph/code_graph/read/relationships.rs:158-164]
- `blast_radius` (function) component `blast_radius [function]` (`13678dac-8882-5166-83e8-0c83d40d3bfb`) lines 166-177 [crates/gcode/src/graph/code_graph/read/relationships.rs:166-177]
  - Signature: `pub fn blast_radius(`
  - Purpose: Queries the core graph for nodes within the configured blast-radius depth around 'symbol_id' in the current project, then converts the returned rows into 'GraphResult' values and returns them as a 'Vec<GraphResult>'. [crates/gcode/src/graph/code_graph/read/relationships.rs:166-177]

