---
title: crates/gcode/src/graph/code_graph/payload.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/payload.rs
  ranges:
  - 10-19
  - 21-86
  - 88-92
  - 94-113
  - 115-117
  - 120-139
  - 141-204
  - 207-218
  - 220-247
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

# crates/gcode/src/graph/code_graph/payload.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

This file defines the graph payload model used by `gcode` to move code graphs between storage, serialization, and analytics. `GraphPayload` holds deduplicated `GraphNode` entries, `GraphLink` edges, and an optional center node, lazily maintains a node-ID cache to reject duplicate inserts, and exposes helpers to build analytics graphs from node/edge tuples.

The rest of the file provides the supporting record types and parsing utilities: `GraphNode` and `GraphLink` constructors plus row deserializers for Falkor query results, metadata parsing helpers, and small adapters that add nodes or links from rows into a payload.
[crates/gcode/src/graph/code_graph/payload.rs:10-19]
[crates/gcode/src/graph/code_graph/payload.rs:21-86]
[crates/gcode/src/graph/code_graph/payload.rs:22-30]
[crates/gcode/src/graph/code_graph/payload.rs:32-43]
[crates/gcode/src/graph/code_graph/payload.rs:45-47]

## API Symbols

- `GraphPayload` (class) component `GraphPayload [class]` (`59acbb71-b370-54d6-ba65-1c3d9c88e1cb`) lines 10-19 [crates/gcode/src/graph/code_graph/payload.rs:10-19]
  - Signature: `pub struct GraphPayload {`
  - Purpose: 'GraphPayload' is a serialized graph container holding a private 'Vec<GraphNode>' plus public 'Vec<GraphLink>' and optional 'center' identifier, with internal skipped fields for deduplicating node IDs and tracking whether the node cache has been initialized. [crates/gcode/src/graph/code_graph/payload.rs:10-19]
- `GraphPayload` (class) component `GraphPayload [class]` (`2fadce14-8b9b-5d57-883b-dd6701bff7b8`) lines 21-86 [crates/gcode/src/graph/code_graph/payload.rs:21-86]
  - Signature: `impl GraphPayload {`
  - Purpose: 'GraphPayload' is a deduplicating graph container that stores 'GraphNode's plus links and an optional center, lazily rebuilds an internal 'HashSet' cache of non-empty node IDs to reject duplicate node inserts, and provides accessors plus a helper to construct an 'AnalyticsGraph' from node and edge tuples. [crates/gcode/src/graph/code_graph/payload.rs:21-86]
- `GraphPayload.with_center` (method) component `GraphPayload.with_center [method]` (`66f22962-9d4e-5c1a-a2d8-0a280e19cf4c`) lines 22-30 [crates/gcode/src/graph/code_graph/payload.rs:22-30]
  - Signature: `pub fn with_center(center: impl Into<String>) -> Self {`
  - Purpose: Constructs and returns a new instance initialized with empty 'nodes' and 'links', 'center' set to 'Some(center.into())', an empty 'HashSet' for 'node_ids', and 'node_cache_ready' set to 'false'. [crates/gcode/src/graph/code_graph/payload.rs:22-30]
- `GraphPayload.push_node` (method) component `GraphPayload.push_node [method]` (`81ab65e5-5c6e-5d40-860b-9184c8ef5b60`) lines 32-43 [crates/gcode/src/graph/code_graph/payload.rs:32-43]
  - Signature: `pub fn push_node(&mut self, node: GraphNode) {`
  - Purpose: Adds a non-empty 'GraphNode' to 'self.nodes' only if the node cache is initialized, refreshing it if needed, and only when its 'id' is newly inserted into 'self.node_ids' to prevent duplicates. [crates/gcode/src/graph/code_graph/payload.rs:32-43]
- `GraphPayload.nodes` (method) component `GraphPayload.nodes [method]` (`1645c6d6-98e2-5b25-9fd6-a744b131f2fe`) lines 45-47 [crates/gcode/src/graph/code_graph/payload.rs:45-47]
  - Signature: `pub fn nodes(&self) -> &[GraphNode] {`
  - Purpose: Returns an immutable slice view of the graph’s internal 'nodes' collection. [crates/gcode/src/graph/code_graph/payload.rs:45-47]
- `GraphPayload.node_count` (method) component `GraphPayload.node_count [method]` (`40bb6569-53e5-5f36-bd7f-7371b7ed6168`) lines 49-51 [crates/gcode/src/graph/code_graph/payload.rs:49-51]
  - Signature: `pub fn node_count(&self) -> usize {`
  - Purpose: Returns the number of nodes currently stored in 'self.nodes' by delegating to its 'len()' method. [crates/gcode/src/graph/code_graph/payload.rs:49-51]
- `GraphPayload.analytics_graph_from_parts` (method) component `GraphPayload.analytics_graph_from_parts [method]` (`eb23c4e5-aa26-56fd-aee5-06dc7acd9964`) lines 53-75 [crates/gcode/src/graph/code_graph/payload.rs:53-75]
  - Signature: `pub(crate) fn analytics_graph_from_parts(`
  - Purpose: Builds an 'AnalyticsGraph' by converting an iterable of '(id, kind, weight)' tuples into 'AnalyticsNode' structs and an iterable of '(source, target, kind)' tuples into 'AnalyticsEdge' structs with weights derived from 'weight_for_kind', then collects both into the graph. [crates/gcode/src/graph/code_graph/payload.rs:53-75]
- `GraphPayload.refresh_node_cache` (method) component `GraphPayload.refresh_node_cache [method]` (`543fee1e-5dcf-583b-bd05-92afc9859200`) lines 77-85 [crates/gcode/src/graph/code_graph/payload.rs:77-85]
  - Signature: `fn refresh_node_cache(&mut self) {`
  - Purpose: Rebuilds 'self.node_ids' as the set of non-empty 'id' values cloned from 'self.nodes' and marks 'self.node_cache_ready' as 'true'. [crates/gcode/src/graph/code_graph/payload.rs:77-85]
- `GraphPayload` (class) component `GraphPayload [class]` (`7e78e2f1-f454-5ff6-b333-a4c327d74c56`) lines 88-92 [crates/gcode/src/graph/code_graph/payload.rs:88-92]
  - Signature: `impl PartialEq for GraphPayload {`
  - Purpose: GraphPayload implements 'PartialEq' by returning true only when its 'nodes', 'links', and 'center' fields are all equal to those of the other value. [crates/gcode/src/graph/code_graph/payload.rs:88-92]
- `GraphPayload.eq` (method) component `GraphPayload.eq [method]` (`5dfa87e0-7f0c-58a3-95ff-63471039010e`) lines 89-91 [crates/gcode/src/graph/code_graph/payload.rs:89-91]
  - Signature: `fn eq(&self, other: &Self) -> bool {`
  - Purpose: Returns 'true' only when 'self.nodes', 'self.links', and 'self.center' are all equal to the corresponding fields in 'other'. [crates/gcode/src/graph/code_graph/payload.rs:89-91]
- `AnalyticsGraph` (class) component `AnalyticsGraph [class]` (`37c2a4dc-1124-5023-b110-05fb248398f6`) lines 94-113 [crates/gcode/src/graph/code_graph/payload.rs:94-113]
  - Signature: `impl From<&GraphPayload> for AnalyticsGraph {`
  - Purpose: 'AnalyticsGraph' is constructed from a 'GraphPayload' by transforming each node into an analytics tuple of '(id, node_type, weighted_symbol_count)' and each link into '(source, target, link_type)' before delegating to 'GraphPayload::analytics_graph_from_parts'. [crates/gcode/src/graph/code_graph/payload.rs:94-113]
- `AnalyticsGraph.from` (method) component `AnalyticsGraph.from [method]` (`89749514-64eb-5602-9484-518182453bc0`) lines 95-112 [crates/gcode/src/graph/code_graph/payload.rs:95-112]
  - Signature: `fn from(payload: &GraphPayload) -> Self {`
  - Purpose: Constructs an analytics graph from the payload by mapping each node to '(id, node_type, analytics_node_weight(symbol_count))' and each link to '(source, target, link_type)', then delegating to 'GraphPayload::analytics_graph_from_parts'. [crates/gcode/src/graph/code_graph/payload.rs:95-112]
- `analytics_node_weight` (function) component `analytics_node_weight [function]` (`3a2ef6ba-832d-5404-9e7d-ea65551068a9`) lines 115-117 [crates/gcode/src/graph/code_graph/payload.rs:115-117]
  - Signature: `fn analytics_node_weight(symbol_count: Option<usize>) -> f64 {`
  - Purpose: Returns the provided symbol count as a 'f64' after clamping it to a minimum of '1', or '1.0' when 'symbol_count' is 'None'. [crates/gcode/src/graph/code_graph/payload.rs:115-117]
- `GraphNode` (class) component `GraphNode [class]` (`f084c167-85f8-5ab9-8b1a-168a2c6af1a5`) lines 120-139 [crates/gcode/src/graph/code_graph/payload.rs:120-139]
  - Signature: `pub struct GraphNode {`
  - Purpose: 'GraphNode' is a serializable Rust struct representing a graph entity with required identity, display name, and node type fields, plus optional metadata such as kind, source file location, signature, symbol count, language, and blast distance. [crates/gcode/src/graph/code_graph/payload.rs:120-139]
- `GraphNode` (class) component `GraphNode [class]` (`df2ddf8e-744c-5571-906b-6ab34a4631e4`) lines 141-204 [crates/gcode/src/graph/code_graph/payload.rs:141-204]
  - Signature: `impl GraphNode {`
  - Purpose: GraphNode is a Rust graph-record value object with constructors and row-parsing helpers that deserialize Falkor query rows into node instances, applying fallback key lookup for unprefixed or prefixed fields and populating optional metadata such as kind, file path, line number, signature, symbol count, language, and blast distance. [crates/gcode/src/graph/code_graph/payload.rs:141-204]
- `GraphNode.new` (method) component `GraphNode.new [method]` (`7c8f5bff-550a-5077-b256-c43b1eedf9b7`) lines 142-159 [crates/gcode/src/graph/code_graph/payload.rs:142-159]
  - Signature: `pub fn new(`
  - Purpose: Constructs a new node instance from 'id', 'name', and 'node_type', converting each into owned 'String's and initializing all optional metadata fields to 'None'. [crates/gcode/src/graph/code_graph/payload.rs:142-159]
- `GraphNode.from_row` (method) component `GraphNode.from_row [method]` (`d9d38321-f19f-5c23-af74-48fac3d49eef`) lines 165-181 [crates/gcode/src/graph/code_graph/payload.rs:165-181]
  - Signature: `pub(super) fn from_row(row: &Row, default_type: &str) -> Option<Self> {`
  - Purpose: Constructs a 'Self' from a database 'Row' by reading the required 'id'/'node_id', defaulting 'name' to the id and 'type' to 'default_type' when absent, then populating optional fields ('kind', 'file_path', 'line_start', 'signature', 'symbol_count', 'language', 'blast_distance') and returning 'Some(node)' if the id is present. [crates/gcode/src/graph/code_graph/payload.rs:165-181]
- `GraphNode.from_prefixed_row` (method) component `GraphNode.from_prefixed_row [method]` (`765d28f7-393f-59be-aca8-959d4b707d10`) lines 183-203 [crates/gcode/src/graph/code_graph/payload.rs:183-203]
  - Signature: `pub(super) fn from_prefixed_row(row: &Row, prefix: &str, default_type: &str) -> Option<Self> {`
  - Purpose: Constructs a 'Self' from 'Row' columns sharing a common prefix by requiring '{prefix}_id', defaulting name to the id and type to 'default_type', and optionally populating kind, file path, line start, and signature before returning 'Some(node)' or 'None' if the id is missing. [crates/gcode/src/graph/code_graph/payload.rs:183-203]
- `GraphLink` (class) component `GraphLink [class]` (`582adffe-7460-55ed-9016-f77bcade5426`) lines 207-218 [crates/gcode/src/graph/code_graph/payload.rs:207-218]
  - Signature: `pub struct GraphLink {`
  - Purpose: 'GraphLink' is a serializable link record representing a directed relationship between two graph nodes, with required 'source', 'target', and 'link_type' fields plus optional 'line', 'distance', and 'metadata' attributes. [crates/gcode/src/graph/code_graph/payload.rs:207-218]
- `GraphLink` (class) component `GraphLink [class]` (`c9696acc-0c13-5d87-97ca-f25570c82fb2`) lines 220-247 [crates/gcode/src/graph/code_graph/payload.rs:220-247]
  - Signature: `impl GraphLink {`
  - Purpose: GraphLink is a lightweight Rust record for a directed edge between 'source' and 'target' with a 'link_type' plus optional 'line', 'distance', and 'metadata', constructible either directly or from a database row. [crates/gcode/src/graph/code_graph/payload.rs:220-247]
- `GraphLink.new` (method) component `GraphLink.new [method]` (`f2fe7253-6bad-5c3e-b67d-a44f9a09d0a7`) lines 221-234 [crates/gcode/src/graph/code_graph/payload.rs:221-234]
  - Signature: `pub fn new(`
  - Purpose: Constructs a new instance by converting 'source', 'target', and 'link_type' into owned 'String' values and initializing 'line', 'distance', and 'metadata' to 'None'. [crates/gcode/src/graph/code_graph/payload.rs:221-234]
- `GraphLink.from_row` (method) component `GraphLink.from_row [method]` (`18e47e6e-97a7-57d8-a61d-916d57d82b9b`) lines 236-246 [crates/gcode/src/graph/code_graph/payload.rs:236-246]
  - Signature: `pub fn from_row(row: &Row) -> Option<Self> {`
  - Purpose: 'from_row' constructs a 'Self' instance from a database 'Row' by reading 'source' and 'target' string fields, using 'type' or 'rel_type' with a default of '"CALLS"', then populating 'line', 'distance', and 'metadata' from the row before returning 'Some(link)'. [crates/gcode/src/graph/code_graph/payload.rs:236-246]
- `GraphBlastRadiusTarget` (type) component `GraphBlastRadiusTarget [type]` (`30b07a2a-7b46-5d59-ad55-62de25a0947c`) lines 250-253 [crates/gcode/src/graph/code_graph/payload.rs:250-253]
  - Signature: `pub enum GraphBlastRadiusTarget {`
  - Purpose: Indexed type `GraphBlastRadiusTarget` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:250-253]
- `extracted_code_edge_metadata` (function) component `extracted_code_edge_metadata [function]` (`207ca297-f0bd-54c4-bc52-d0fe71f91047`) lines 254-266 [crates/gcode/src/graph/code_graph/payload.rs:254-266]
  - Signature: `pub fn extracted_code_edge_metadata(`
  - Purpose: Builds a 'ProjectionMetadata' value for extracted code edges by marking it as gcode-extracted, setting the source file path and line, and optionally attaching a source symbol ID. [crates/gcode/src/graph/code_graph/payload.rs:254-266]
- `row_to_projection_metadata` (function) component `row_to_projection_metadata [function]` (`2e82aca5-7fdb-588e-a360-b3a64ee080aa`) lines 268-294 [crates/gcode/src/graph/code_graph/payload.rs:268-294]
  - Signature: `pub(super) fn row_to_projection_metadata(row: &Row) -> Option<ProjectionMetadata> {`
  - Purpose: Parses a 'Row' into 'ProjectionMetadata' by requiring valid 'provenance' and 'source_system', then populating optional confidence, source file path, source line, source symbol ID, and matching method fields from the row with fallback column names. [crates/gcode/src/graph/code_graph/payload.rs:268-294]
- `row_string_owned` (function) component `row_string_owned [function]` (`e62c0138-29fb-5919-86bf-453bb4f023d4`) lines 296-301 [crates/gcode/src/graph/code_graph/payload.rs:296-301]
  - Signature: `pub(super) fn row_string_owned(row: &Row, keys: &[&str]) -> Option<String> {`
  - Purpose: Returns the first non-empty string value found in 'row' for any of the provided 'keys', cloning it into an owned 'String', or 'None' if no such value exists. [crates/gcode/src/graph/code_graph/payload.rs:296-301]
- `row_usize` (function) component `row_usize [function]` (`d89d3ab9-ad0a-58d2-9645-87a1b3e2929a`) lines 303-320 [crates/gcode/src/graph/code_graph/payload.rs:303-320]
  - Signature: `pub(super) fn row_usize(row: &Row, keys: &[&str]) -> Option<usize> {`
  - Purpose: Searches the provided 'Row' for the first matching key and returns that value as a 'usize' if it can be losslessly converted from either a 'u64' or nonnegative 'i64', otherwise logs a warning for negative integers and returns 'None'. [crates/gcode/src/graph/code_graph/payload.rs:303-320]
- `add_link_from_row` (function) component `add_link_from_row [function]` (`316b191e-843c-5997-af74-bb6649eb2d9c`) lines 322-326 [crates/gcode/src/graph/code_graph/payload.rs:322-326]
  - Signature: `pub(super) fn add_link_from_row(payload: &mut GraphPayload, row: &Row) {`
  - Purpose: Parses a 'GraphLink' from 'row' and appends it to 'payload.links' only when deserialization succeeds. [crates/gcode/src/graph/code_graph/payload.rs:322-326]
- `add_node_from_row` (function) component `add_node_from_row [function]` (`4f8faa12-96dd-5138-a79d-f172aeb84990`) lines 328-332 [crates/gcode/src/graph/code_graph/payload.rs:328-332]
  - Signature: `pub(super) fn add_node_from_row(payload: &mut GraphPayload, row: &Row, default_type: &str) {`
  - Purpose: Attempts to construct a 'GraphNode' from the given 'Row' using 'default_type' and, if successful, appends it to the 'GraphPayload'. [crates/gcode/src/graph/code_graph/payload.rs:328-332]
- `add_prefixed_node_from_row` (function) component `add_prefixed_node_from_row [function]` (`9d11ce7c-21ed-5948-b738-b3d53511ecd3`) lines 334-343 [crates/gcode/src/graph/code_graph/payload.rs:334-343]
  - Signature: `pub(super) fn add_prefixed_node_from_row(`
  - Purpose: Creates a 'GraphNode' from 'row' using the given 'prefix' and 'default_type', and appends it to 'payload' only when parsing succeeds. [crates/gcode/src/graph/code_graph/payload.rs:334-343]

