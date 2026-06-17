---
title: crates/gcode/src/graph/code_graph/payload.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/payload.rs
  ranges:
  - 10-19
  - 22-30
  - 32-43
  - 45-47
  - 49-51
  - 53-75
  - 77-85
  - 89-91
  - 95-112
  - 115-117
  - 120-139
  - 142-159
  - 165-181
  - 183-203
  - 207-218
  - 221-234
  - 236-246
  - 250-266
  - 268-294
  - 296-301
  - 303-320
  - 322-326
  - 328-332
  - 334-343
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/payload.rs:10-19](crates/gcode/src/graph/code_graph/payload.rs#L10-L19), [crates/gcode/src/graph/code_graph/payload.rs:22-30](crates/gcode/src/graph/code_graph/payload.rs#L22-L30), [crates/gcode/src/graph/code_graph/payload.rs:32-43](crates/gcode/src/graph/code_graph/payload.rs#L32-L43), [crates/gcode/src/graph/code_graph/payload.rs:45-47](crates/gcode/src/graph/code_graph/payload.rs#L45-L47), [crates/gcode/src/graph/code_graph/payload.rs:49-51](crates/gcode/src/graph/code_graph/payload.rs#L49-L51), [crates/gcode/src/graph/code_graph/payload.rs:53-75](crates/gcode/src/graph/code_graph/payload.rs#L53-L75), [crates/gcode/src/graph/code_graph/payload.rs:77-85](crates/gcode/src/graph/code_graph/payload.rs#L77-L85), [crates/gcode/src/graph/code_graph/payload.rs:89-91](crates/gcode/src/graph/code_graph/payload.rs#L89-L91), [crates/gcode/src/graph/code_graph/payload.rs:95-112](crates/gcode/src/graph/code_graph/payload.rs#L95-L112), [crates/gcode/src/graph/code_graph/payload.rs:115-117](crates/gcode/src/graph/code_graph/payload.rs#L115-L117), [crates/gcode/src/graph/code_graph/payload.rs:120-139](crates/gcode/src/graph/code_graph/payload.rs#L120-L139), [crates/gcode/src/graph/code_graph/payload.rs:142-159](crates/gcode/src/graph/code_graph/payload.rs#L142-L159), [crates/gcode/src/graph/code_graph/payload.rs:165-181](crates/gcode/src/graph/code_graph/payload.rs#L165-L181), [crates/gcode/src/graph/code_graph/payload.rs:183-203](crates/gcode/src/graph/code_graph/payload.rs#L183-L203), [crates/gcode/src/graph/code_graph/payload.rs:207-218](crates/gcode/src/graph/code_graph/payload.rs#L207-L218), [crates/gcode/src/graph/code_graph/payload.rs:221-234](crates/gcode/src/graph/code_graph/payload.rs#L221-L234), [crates/gcode/src/graph/code_graph/payload.rs:236-246](crates/gcode/src/graph/code_graph/payload.rs#L236-L246), [crates/gcode/src/graph/code_graph/payload.rs:250-266](crates/gcode/src/graph/code_graph/payload.rs#L250-L266), [crates/gcode/src/graph/code_graph/payload.rs:268-294](crates/gcode/src/graph/code_graph/payload.rs#L268-L294), [crates/gcode/src/graph/code_graph/payload.rs:296-301](crates/gcode/src/graph/code_graph/payload.rs#L296-L301), [crates/gcode/src/graph/code_graph/payload.rs:303-320](crates/gcode/src/graph/code_graph/payload.rs#L303-L320), [crates/gcode/src/graph/code_graph/payload.rs:322-326](crates/gcode/src/graph/code_graph/payload.rs#L322-L326), [crates/gcode/src/graph/code_graph/payload.rs:328-332](crates/gcode/src/graph/code_graph/payload.rs#L328-L332), [crates/gcode/src/graph/code_graph/payload.rs:334-343](crates/gcode/src/graph/code_graph/payload.rs#L334-L343)

</details>

# crates/gcode/src/graph/code_graph/payload.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

Defines the graph payload model and its conversion helpers for code-graph data. `GraphPayload` owns the serialized node/link collection plus an optional center, and it keeps an internal ID cache so `push_node` skips empty or duplicate nodes while exposing read access and counts. The rest of the file builds supporting `GraphNode` and `GraphLink` values from Falkor rows, translates rows into projection metadata, derives edge metadata for extracted code, and assembles an `AnalyticsGraph` from node and edge parts with weights computed from edge kind.
[crates/gcode/src/graph/code_graph/payload.rs:10-19]
[crates/gcode/src/graph/code_graph/payload.rs:22-30]
[crates/gcode/src/graph/code_graph/payload.rs:32-43]
[crates/gcode/src/graph/code_graph/payload.rs:45-47]
[crates/gcode/src/graph/code_graph/payload.rs:49-51]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GraphPayload` | class | `pub struct GraphPayload {` | `GraphPayload [class]` | `59acbb71-b370-54d6-ba65-1c3d9c88e1cb` | 10-19 [crates/gcode/src/graph/code_graph/payload.rs:10-19] | Indexed class `GraphPayload` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:10-19] |
| `GraphPayload::with_center` | method | `pub fn with_center(center: impl Into<String>) -> Self {` | `GraphPayload::with_center [method]` | `66f22962-9d4e-5c1a-a2d8-0a280e19cf4c` | 22-30 [crates/gcode/src/graph/code_graph/payload.rs:22-30] | Indexed method `GraphPayload::with_center` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:22-30] |
| `GraphPayload::push_node` | method | `pub fn push_node(&mut self, node: GraphNode) {` | `GraphPayload::push_node [method]` | `81ab65e5-5c6e-5d40-860b-9184c8ef5b60` | 32-43 [crates/gcode/src/graph/code_graph/payload.rs:32-43] | Indexed method `GraphPayload::push_node` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:32-43] |
| `GraphPayload::nodes` | method | `pub fn nodes(&self) -> &[GraphNode] {` | `GraphPayload::nodes [method]` | `1645c6d6-98e2-5b25-9fd6-a744b131f2fe` | 45-47 [crates/gcode/src/graph/code_graph/payload.rs:45-47] | Indexed method `GraphPayload::nodes` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:45-47] |
| `GraphPayload::node_count` | method | `pub fn node_count(&self) -> usize {` | `GraphPayload::node_count [method]` | `40bb6569-53e5-5f36-bd7f-7371b7ed6168` | 49-51 [crates/gcode/src/graph/code_graph/payload.rs:49-51] | Indexed method `GraphPayload::node_count` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:49-51] |
| `GraphPayload::analytics_graph_from_parts` | method | `pub(crate) fn analytics_graph_from_parts(` | `GraphPayload::analytics_graph_from_parts [method]` | `eb23c4e5-aa26-56fd-aee5-06dc7acd9964` | 53-75 [crates/gcode/src/graph/code_graph/payload.rs:53-75] | Indexed method `GraphPayload::analytics_graph_from_parts` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:53-75] |
| `GraphPayload::refresh_node_cache` | method | `fn refresh_node_cache(&mut self) {` | `GraphPayload::refresh_node_cache [method]` | `543fee1e-5dcf-583b-bd05-92afc9859200` | 77-85 [crates/gcode/src/graph/code_graph/payload.rs:77-85] | Indexed method `GraphPayload::refresh_node_cache` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:77-85] |
| `GraphPayload::eq` | method | `fn eq(&self, other: &Self) -> bool {` | `GraphPayload::eq [method]` | `5dfa87e0-7f0c-58a3-95ff-63471039010e` | 89-91 [crates/gcode/src/graph/code_graph/payload.rs:89-91] | Indexed method `GraphPayload::eq` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:89-91] |
| `AnalyticsGraph::from` | method | `fn from(payload: &GraphPayload) -> Self {` | `AnalyticsGraph::from [method]` | `89749514-64eb-5602-9484-518182453bc0` | 95-112 [crates/gcode/src/graph/code_graph/payload.rs:95-112] | Indexed method `AnalyticsGraph::from` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:95-112] |
| `analytics_node_weight` | function | `fn analytics_node_weight(symbol_count: Option<usize>) -> f64 {` | `analytics_node_weight [function]` | `3a2ef6ba-832d-5404-9e7d-ea65551068a9` | 115-117 [crates/gcode/src/graph/code_graph/payload.rs:115-117] | Indexed function `analytics_node_weight` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:115-117] |
| `GraphNode` | class | `pub struct GraphNode {` | `GraphNode [class]` | `f084c167-85f8-5ab9-8b1a-168a2c6af1a5` | 120-139 [crates/gcode/src/graph/code_graph/payload.rs:120-139] | Indexed class `GraphNode` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:120-139] |
| `GraphNode::new` | method | `pub fn new(` | `GraphNode::new [method]` | `7c8f5bff-550a-5077-b256-c43b1eedf9b7` | 142-159 [crates/gcode/src/graph/code_graph/payload.rs:142-159] | Indexed method `GraphNode::new` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:142-159] |
| `GraphNode::from_row` | method | `pub(super) fn from_row(row: &Row, default_type: &str) -> Option<Self> {` | `GraphNode::from_row [method]` | `d9d38321-f19f-5c23-af74-48fac3d49eef` | 165-181 [crates/gcode/src/graph/code_graph/payload.rs:165-181] | Indexed method `GraphNode::from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:165-181] |
| `GraphNode::from_prefixed_row` | method | `pub(super) fn from_prefixed_row(row: &Row, prefix: &str, default_type: &str) -> Option<Self> {` | `GraphNode::from_prefixed_row [method]` | `765d28f7-393f-59be-aca8-959d4b707d10` | 183-203 [crates/gcode/src/graph/code_graph/payload.rs:183-203] | Indexed method `GraphNode::from_prefixed_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:183-203] |
| `GraphLink` | class | `pub struct GraphLink {` | `GraphLink [class]` | `582adffe-7460-55ed-9016-f77bcade5426` | 207-218 [crates/gcode/src/graph/code_graph/payload.rs:207-218] | Indexed class `GraphLink` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:207-218] |
| `GraphLink::new` | method | `pub fn new(` | `GraphLink::new [method]` | `f2fe7253-6bad-5c3e-b67d-a44f9a09d0a7` | 221-234 [crates/gcode/src/graph/code_graph/payload.rs:221-234] | Indexed method `GraphLink::new` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:221-234] |
| `GraphLink::from_row` | method | `pub fn from_row(row: &Row) -> Option<Self> {` | `GraphLink::from_row [method]` | `18e47e6e-97a7-57d8-a61d-916d57d82b9b` | 236-246 [crates/gcode/src/graph/code_graph/payload.rs:236-246] | Indexed method `GraphLink::from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:236-246] |
| `GraphBlastRadiusTarget` | type | `pub enum GraphBlastRadiusTarget {` | `GraphBlastRadiusTarget [type]` | `30b07a2a-7b46-5d59-ad55-62de25a0947c` | 250-253 [crates/gcode/src/graph/code_graph/payload.rs:250-253] | Indexed type `GraphBlastRadiusTarget` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:250-253] |
| `extracted_code_edge_metadata` | function | `pub fn extracted_code_edge_metadata(` | `extracted_code_edge_metadata [function]` | `207ca297-f0bd-54c4-bc52-d0fe71f91047` | 254-266 [crates/gcode/src/graph/code_graph/payload.rs:254-266] | Indexed function `extracted_code_edge_metadata` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:254-266] |
| `row_to_projection_metadata` | function | `pub(super) fn row_to_projection_metadata(row: &Row) -> Option<ProjectionMetadata> {` | `row_to_projection_metadata [function]` | `2e82aca5-7fdb-588e-a360-b3a64ee080aa` | 268-294 [crates/gcode/src/graph/code_graph/payload.rs:268-294] | Indexed function `row_to_projection_metadata` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:268-294] |
| `row_string_owned` | function | `pub(super) fn row_string_owned(row: &Row, keys: &[&str]) -> Option<String> {` | `row_string_owned [function]` | `e62c0138-29fb-5919-86bf-453bb4f023d4` | 296-301 [crates/gcode/src/graph/code_graph/payload.rs:296-301] | Indexed function `row_string_owned` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:296-301] |
| `row_usize` | function | `pub(super) fn row_usize(row: &Row, keys: &[&str]) -> Option<usize> {` | `row_usize [function]` | `d89d3ab9-ad0a-58d2-9645-87a1b3e2929a` | 303-320 [crates/gcode/src/graph/code_graph/payload.rs:303-320] | Indexed function `row_usize` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:303-320] |
| `add_link_from_row` | function | `pub(super) fn add_link_from_row(payload: &mut GraphPayload, row: &Row) {` | `add_link_from_row [function]` | `316b191e-843c-5997-af74-bb6649eb2d9c` | 322-326 [crates/gcode/src/graph/code_graph/payload.rs:322-326] | Indexed function `add_link_from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:322-326] |
| `add_node_from_row` | function | `pub(super) fn add_node_from_row(payload: &mut GraphPayload, row: &Row, default_type: &str) {` | `add_node_from_row [function]` | `4f8faa12-96dd-5138-a79d-f172aeb84990` | 328-332 [crates/gcode/src/graph/code_graph/payload.rs:328-332] | Indexed function `add_node_from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:328-332] |
| `add_prefixed_node_from_row` | function | `pub(super) fn add_prefixed_node_from_row(` | `add_prefixed_node_from_row [function]` | `9d11ce7c-21ed-5948-b738-b3d53511ecd3` | 334-343 [crates/gcode/src/graph/code_graph/payload.rs:334-343] | Indexed function `add_prefixed_node_from_row` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:334-343] |
