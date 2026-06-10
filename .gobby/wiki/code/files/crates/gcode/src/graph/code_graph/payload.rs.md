---
title: crates/gcode/src/graph/code_graph/payload.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/payload.rs
  ranges:
  - 10-19
  - 21-82
  - 22-30
  - 32-43
  - 45-47
  - 49-51
  - 53-71
  - 73-81
  - 84-88
  - 85-87
  - 90-109
  - 91-108
  - 111-113
  - 116-135
  - 137-200
  - 138-155
  - 161-177
  - 179-199
  - 203-214
  - 216-243
  - 217-230
  - 232-242
  - 246-249
  - 250-262
  - 264-290
  - 292-297
  - 299-316
  - 318-322
  - 324-328
  - 330-339
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/payload.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

`crates/gcode/src/graph/code_graph/payload.rs` exposes 30 indexed API symbols.
[crates/gcode/src/graph/code_graph/payload.rs:10-19]
[crates/gcode/src/graph/code_graph/payload.rs:21-82]
[crates/gcode/src/graph/code_graph/payload.rs:22-30]
[crates/gcode/src/graph/code_graph/payload.rs:32-43]
[crates/gcode/src/graph/code_graph/payload.rs:45-47]
[crates/gcode/src/graph/code_graph/payload.rs:49-51]
[crates/gcode/src/graph/code_graph/payload.rs:53-71]
[crates/gcode/src/graph/code_graph/payload.rs:73-81]
[crates/gcode/src/graph/code_graph/payload.rs:84-88]
[crates/gcode/src/graph/code_graph/payload.rs:85-87]
[crates/gcode/src/graph/code_graph/payload.rs:90-109]
[crates/gcode/src/graph/code_graph/payload.rs:91-108]
[crates/gcode/src/graph/code_graph/payload.rs:111-113]
[crates/gcode/src/graph/code_graph/payload.rs:116-135]
[crates/gcode/src/graph/code_graph/payload.rs:137-200]
[crates/gcode/src/graph/code_graph/payload.rs:138-155]
[crates/gcode/src/graph/code_graph/payload.rs:161-177]
[crates/gcode/src/graph/code_graph/payload.rs:179-199]
[crates/gcode/src/graph/code_graph/payload.rs:203-214]
[crates/gcode/src/graph/code_graph/payload.rs:216-243]
[crates/gcode/src/graph/code_graph/payload.rs:217-230]
[crates/gcode/src/graph/code_graph/payload.rs:232-242]
[crates/gcode/src/graph/code_graph/payload.rs:246-249]
[crates/gcode/src/graph/code_graph/payload.rs:250-262]
[crates/gcode/src/graph/code_graph/payload.rs:264-290]
[crates/gcode/src/graph/code_graph/payload.rs:292-297]
[crates/gcode/src/graph/code_graph/payload.rs:299-316]
[crates/gcode/src/graph/code_graph/payload.rs:318-322]
[crates/gcode/src/graph/code_graph/payload.rs:324-328]
[crates/gcode/src/graph/code_graph/payload.rs:330-339]

## API Symbols

- `GraphPayload` (class) component `GraphPayload [class]` (`b6ce4f8f-620e-5843-bf9b-0bdd6218d53e`) lines 10-19 [crates/gcode/src/graph/code_graph/payload.rs:10-19]
  - Signature: `pub struct GraphPayload {`
  - Purpose: Indexed class `GraphPayload` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:10-19]
- `GraphPayload` (class) component `GraphPayload [class]` (`df198b8a-8f88-5019-8fc0-e7a246b8e828`) lines 21-82 [crates/gcode/src/graph/code_graph/payload.rs:21-82]
  - Signature: `impl GraphPayload {`
  - Purpose: Indexed class `GraphPayload` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:21-82]
- `GraphPayload.with_center` (method) component `GraphPayload.with_center [method]` (`7d3749b7-41d2-5478-910b-2689e57f92c4`) lines 22-30 [crates/gcode/src/graph/code_graph/payload.rs:22-30]
  - Signature: `pub fn with_center(center: impl Into<String>) -> Self {`
  - Purpose: Indexed method `GraphPayload.with_center` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:22-30]
- `GraphPayload.push_node` (method) component `GraphPayload.push_node [method]` (`9a6c7bf6-a2bc-506f-8207-d0ea83981d02`) lines 32-43 [crates/gcode/src/graph/code_graph/payload.rs:32-43]
  - Signature: `pub fn push_node(&mut self, node: GraphNode) {`
  - Purpose: Indexed method `GraphPayload.push_node` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:32-43]
- `GraphPayload.nodes` (method) component `GraphPayload.nodes [method]` (`72a7b60d-95c7-5304-a5a0-066a668a52a7`) lines 45-47 [crates/gcode/src/graph/code_graph/payload.rs:45-47]
  - Signature: `pub fn nodes(&self) -> &[GraphNode] {`
  - Purpose: Indexed method `GraphPayload.nodes` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:45-47]
- `GraphPayload.node_count` (method) component `GraphPayload.node_count [method]` (`8c438192-3140-57af-a36c-cf156753fb70`) lines 49-51 [crates/gcode/src/graph/code_graph/payload.rs:49-51]
  - Signature: `pub fn node_count(&self) -> usize {`
  - Purpose: Indexed method `GraphPayload.node_count` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:49-51]
- `GraphPayload.analytics_graph_from_parts` (method) component `GraphPayload.analytics_graph_from_parts [method]` (`bd10be28-d77f-5822-bc76-b287fc7ed611`) lines 53-71 [crates/gcode/src/graph/code_graph/payload.rs:53-71]
  - Signature: `pub(crate) fn analytics_graph_from_parts(`
  - Purpose: Indexed method `GraphPayload.analytics_graph_from_parts` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:53-71]
- `GraphPayload.refresh_node_cache` (method) component `GraphPayload.refresh_node_cache [method]` (`48bdb900-86fb-5ed0-ba01-dbc8d611af7a`) lines 73-81 [crates/gcode/src/graph/code_graph/payload.rs:73-81]
  - Signature: `fn refresh_node_cache(&mut self) {`
  - Purpose: Indexed method `GraphPayload.refresh_node_cache` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:73-81]
- `GraphPayload` (class) component `GraphPayload [class]` (`f6a6730e-342b-5566-b52b-f9ece2db04b3`) lines 84-88 [crates/gcode/src/graph/code_graph/payload.rs:84-88]
  - Signature: `impl PartialEq for GraphPayload {`
  - Purpose: Indexed class `GraphPayload` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:84-88]
- `GraphPayload.eq` (method) component `GraphPayload.eq [method]` (`8e653bba-18cc-5cd5-bd28-2c8489928b76`) lines 85-87 [crates/gcode/src/graph/code_graph/payload.rs:85-87]
  - Signature: `fn eq(&self, other: &Self) -> bool {`
  - Purpose: Indexed method `GraphPayload.eq` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:85-87]
- `AnalyticsGraph` (class) component `AnalyticsGraph [class]` (`450dbc97-6f90-52ba-8995-bbb35d4c7a65`) lines 90-109 [crates/gcode/src/graph/code_graph/payload.rs:90-109]
  - Signature: `impl From<&GraphPayload> for AnalyticsGraph {`
  - Purpose: Indexed class `AnalyticsGraph` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:90-109]
- `AnalyticsGraph.from` (method) component `AnalyticsGraph.from [method]` (`6af8553a-586c-57c1-b509-962b15b6cba4`) lines 91-108 [crates/gcode/src/graph/code_graph/payload.rs:91-108]
  - Signature: `fn from(payload: &GraphPayload) -> Self {`
  - Purpose: Indexed method `AnalyticsGraph.from` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:91-108]
- `analytics_node_weight` (function) component `analytics_node_weight [function]` (`de9e32b9-3ca6-5ccb-b15b-c99f15deb36c`) lines 111-113 [crates/gcode/src/graph/code_graph/payload.rs:111-113]
  - Signature: `fn analytics_node_weight(symbol_count: Option<usize>) -> f64 {`
  - Purpose: Indexed function `analytics_node_weight` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:111-113]
- `GraphNode` (class) component `GraphNode [class]` (`285bf827-eeac-54e3-9599-5ac737692107`) lines 116-135 [crates/gcode/src/graph/code_graph/payload.rs:116-135]
  - Signature: `pub struct GraphNode {`
  - Purpose: Indexed class `GraphNode` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:116-135]
- `GraphNode` (class) component `GraphNode [class]` (`ea771c32-df61-5d69-9c62-234d101d926e`) lines 137-200 [crates/gcode/src/graph/code_graph/payload.rs:137-200]
  - Signature: `impl GraphNode {`
  - Purpose: Indexed class `GraphNode` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:137-200]
- `GraphNode.new` (method) component `GraphNode.new [method]` (`b2733cef-3d40-5a43-95f8-fecbe032c555`) lines 138-155 [crates/gcode/src/graph/code_graph/payload.rs:138-155]
  - Signature: `pub fn new(`
  - Purpose: Indexed method `GraphNode.new` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:138-155]
- `GraphNode.from_row` (method) component `GraphNode.from_row [method]` (`c4b69336-b2ff-5244-a040-4a0d88caf971`) lines 161-177 [crates/gcode/src/graph/code_graph/payload.rs:161-177]
  - Signature: `pub(super) fn from_row(row: &Row, default_type: &str) -> Option<Self> {`
  - Purpose: Indexed method `GraphNode.from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:161-177]
- `GraphNode.from_prefixed_row` (method) component `GraphNode.from_prefixed_row [method]` (`88357457-6f31-5970-b20b-4075a316ce46`) lines 179-199 [crates/gcode/src/graph/code_graph/payload.rs:179-199]
  - Signature: `pub(super) fn from_prefixed_row(row: &Row, prefix: &str, default_type: &str) -> Option<Self> {`
  - Purpose: Indexed method `GraphNode.from_prefixed_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:179-199]
- `GraphLink` (class) component `GraphLink [class]` (`4b3fb968-81d6-5c00-9fa3-b93223eb6a45`) lines 203-214 [crates/gcode/src/graph/code_graph/payload.rs:203-214]
  - Signature: `pub struct GraphLink {`
  - Purpose: Indexed class `GraphLink` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:203-214]
- `GraphLink` (class) component `GraphLink [class]` (`9d5463ba-e6f5-5bb9-bb4e-1c557a9cc64e`) lines 216-243 [crates/gcode/src/graph/code_graph/payload.rs:216-243]
  - Signature: `impl GraphLink {`
  - Purpose: Indexed class `GraphLink` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:216-243]
- `GraphLink.new` (method) component `GraphLink.new [method]` (`0ae7f4d0-4dcf-528a-bc41-dad45f95dfd5`) lines 217-230 [crates/gcode/src/graph/code_graph/payload.rs:217-230]
  - Signature: `pub fn new(`
  - Purpose: Indexed method `GraphLink.new` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:217-230]
- `GraphLink.from_row` (method) component `GraphLink.from_row [method]` (`83a203fa-d966-5cb8-ae62-627e46dd9323`) lines 232-242 [crates/gcode/src/graph/code_graph/payload.rs:232-242]
  - Signature: `pub fn from_row(row: &Row) -> Option<Self> {`
  - Purpose: Indexed method `GraphLink.from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:232-242]
- `GraphBlastRadiusTarget` (type) component `GraphBlastRadiusTarget [type]` (`c3e83663-569b-534e-939a-ad1b05617fe0`) lines 246-249 [crates/gcode/src/graph/code_graph/payload.rs:246-249]
  - Signature: `pub enum GraphBlastRadiusTarget {`
  - Purpose: Indexed type `GraphBlastRadiusTarget` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:246-249]
- `extracted_code_edge_metadata` (function) component `extracted_code_edge_metadata [function]` (`85ac5fd4-9bd7-554b-b380-1d6c58a4cc10`) lines 250-262 [crates/gcode/src/graph/code_graph/payload.rs:250-262]
  - Signature: `pub fn extracted_code_edge_metadata(`
  - Purpose: Indexed function `extracted_code_edge_metadata` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:250-262]
- `row_to_projection_metadata` (function) component `row_to_projection_metadata [function]` (`9c8a8bb8-3659-53cd-b76f-38d9901d25b1`) lines 264-290 [crates/gcode/src/graph/code_graph/payload.rs:264-290]
  - Signature: `pub(super) fn row_to_projection_metadata(row: &Row) -> Option<ProjectionMetadata> {`
  - Purpose: Indexed function `row_to_projection_metadata` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:264-290]
- `row_string_owned` (function) component `row_string_owned [function]` (`8fc344e4-c8e3-53db-8d35-6e2813a6d439`) lines 292-297 [crates/gcode/src/graph/code_graph/payload.rs:292-297]
  - Signature: `pub(super) fn row_string_owned(row: &Row, keys: &[&str]) -> Option<String> {`
  - Purpose: Indexed function `row_string_owned` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:292-297]
- `row_usize` (function) component `row_usize [function]` (`5b2e343b-f802-504d-88c8-6ca297fba2bf`) lines 299-316 [crates/gcode/src/graph/code_graph/payload.rs:299-316]
  - Signature: `pub(super) fn row_usize(row: &Row, keys: &[&str]) -> Option<usize> {`
  - Purpose: Indexed function `row_usize` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:299-316]
- `add_link_from_row` (function) component `add_link_from_row [function]` (`6c18fcf6-4109-5765-a289-5c8c146b2f49`) lines 318-322 [crates/gcode/src/graph/code_graph/payload.rs:318-322]
  - Signature: `pub(super) fn add_link_from_row(payload: &mut GraphPayload, row: &Row) {`
  - Purpose: Indexed function `add_link_from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:318-322]
- `add_node_from_row` (function) component `add_node_from_row [function]` (`c5e6b7f2-467e-563f-a84d-a475e7c01d25`) lines 324-328 [crates/gcode/src/graph/code_graph/payload.rs:324-328]
  - Signature: `pub(super) fn add_node_from_row(payload: &mut GraphPayload, row: &Row, default_type: &str) {`
  - Purpose: Indexed function `add_node_from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:324-328]
- `add_prefixed_node_from_row` (function) component `add_prefixed_node_from_row [function]` (`84131c3f-68d4-5c25-a711-53aabf8ad89b`) lines 330-339 [crates/gcode/src/graph/code_graph/payload.rs:330-339]
  - Signature: `pub(super) fn add_prefixed_node_from_row(`
  - Purpose: Indexed function `add_prefixed_node_from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:330-339]

