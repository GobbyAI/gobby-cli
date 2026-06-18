---
title: crates/gcode/src/graph/code_graph/payload.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/payload.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/graph/code_graph/payload.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Overview

To prevent duplicate entities, `GraphPayload` uses internal caches to track node uniqueness. When a node is added via `push_node` [crates/gcode/src/graph/code_graph/payload.rs:32-43], the struct uses `refresh_node_cache` [crates/gcode/src/graph/code_graph/payload.rs:77-85] to populate its internal lookup set, ensuring that duplicate node IDs are rejected and integrity is preserved.

## How it fits

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphPayload` | class | 'GraphPayload' is a serializable graph container that stores a vector of 'GraphNode's and 'GraphLink's plus an optional 'center' node identifier, while maintaining skipped internal caches ('node_ids' and 'node_cache_ready') for node lookup/validation. [crates/gcode/src/graph/code_graph/payload.rs:10-19] |
| `GraphPayload::with_center` | method | Constructs and returns a new 'Self' with no nodes or links, 'center' set to 'Some(center.into())', an empty 'node_ids' set, and 'node_cache_ready' initialized to 'false'. [crates/gcode/src/graph/code_graph/payload.rs:22-30] |
| `GraphPayload::push_node` | method | Adds a non-empty 'GraphNode' to 'self.nodes' only after ensuring the node cache is initialized and the node ID is unique, otherwise it returns early without modifying state. [crates/gcode/src/graph/code_graph/payload.rs:32-43] |
| `GraphPayload::nodes` | method | Returns an immutable slice reference to the graph’s internal 'nodes' collection. [crates/gcode/src/graph/code_graph/payload.rs:45-47] |
| `GraphPayload::node_count` | method | Returns the number of nodes by delegating to 'self.nodes.len()', yielding the length of the underlying node collection as a 'usize'. [crates/gcode/src/graph/code_graph/payload.rs:49-51] |
| `GraphPayload::analytics_graph_from_parts` | method | Constructs an 'AnalyticsGraph' by collecting '(id, kind, weight)' tuples into 'AnalyticsNode' values and '(source, target, kind)' tuples into 'AnalyticsEdge' values, computing each edge’s weight via 'weight_for_kind(&kind)'. [crates/gcode/src/graph/code_graph/payload.rs:53-75] |
| `GraphPayload::refresh_node_cache` | method | Rebuilds 'self.node_ids' as the 'HashSet' of all non-empty 'id' values cloned from 'self.nodes', then marks the node cache as ready by setting 'self.node_cache_ready = true'. [crates/gcode/src/graph/code_graph/payload.rs:77-85] |
| `GraphPayload::eq` | method | Returns 'true' only when 'self.nodes', 'self.links', and 'self.center' are all equal to the corresponding fields in 'other'; otherwise returns 'false'. [crates/gcode/src/graph/code_graph/payload.rs:89-91] |
| `AnalyticsGraph::from` | method | Builds an analytics graph from a 'GraphPayload' by iterating its nodes and links, cloning each node’s 'id' and 'node_type' while converting 'symbol_count' to an analytics weight, cloning each link’s 'source', 'target', and 'link_type', and passing those iterators to 'GraphPayload::analytics_graph_from_parts'. [crates/gcode/src/graph/code_graph/payload.rs:95-112] |
| `analytics_node_weight` | function | Returns the provided symbol count as an 'f64' with a minimum of '1.0', or '1.0' when 'symbol_count' is 'None'. [crates/gcode/src/graph/code_graph/payload.rs:115-117] |
| `GraphNode` | class | 'GraphNode' is a Serde-serializable Rust struct representing a graph entity with required 'id', 'name', and JSON-renamed 'type' fields plus optional metadata such as kind, source location, signature, symbol count, language, and blast distance. [crates/gcode/src/graph/code_graph/payload.rs:120-139] |
| `GraphNode::new` | method | Constructs a new instance by converting 'id', 'name', and 'node_type' into owned 'String's and initializing all optional metadata fields ('kind', 'file_path', 'line_start', 'signature', 'symbol_count', 'language', 'blast_distance') to 'None'. [crates/gcode/src/graph/code_graph/payload.rs:142-159] |
| `GraphNode::from_row` | method | 'from_row' constructs a 'Self' from a database 'Row' by requiring an 'id'/'node_id', populating 'name' and 'type' from alternate column names with fallbacks ('id' and 'default_type'), then filling optional fields ('kind', 'file_path', 'line_start', 'signature', 'symbol_count', 'language', 'blast_distance') before returning 'Some(node)'. [crates/gcode/src/graph/code_graph/payload.rs:165-181] |
| `GraphNode::from_prefixed_row` | method | Constructs an instance from a 'Row' by reading '{prefix}_id' as required, defaulting '{prefix}_name' to the id and '{prefix}_type' to 'default_type', populating optional 'kind', 'file_path', 'line_start', and 'signature' fields, and returning 'None' if the id is absent. [crates/gcode/src/graph/code_graph/payload.rs:183-203] |
| `GraphLink` | class | 'GraphLink' is a serializable edge record connecting a 'source' node to a 'target' node, labeled by a string 'link_type' and optionally annotated with 'line', 'distance', and 'metadata' ('ProjectionMetadata'). [crates/gcode/src/graph/code_graph/payload.rs:207-218] |
| `GraphLink::new` | method | Constructs a new instance by converting the 'source', 'target', and 'link_type' arguments into owned 'String's and initializing 'line', 'distance', and 'metadata' to 'None'. [crates/gcode/src/graph/code_graph/payload.rs:221-234] |
| `GraphLink::from_row` | method | Constructs a 'Self' link from a database 'Row' by reading required 'source' and 'target' strings, defaulting 'type'/'rel_type' to '"CALLS"', populating optional 'line', 'distance', and 'metadata' fields, and returning 'Some(link)' when the required fields are present. [crates/gcode/src/graph/code_graph/payload.rs:236-246] |
| `GraphBlastRadiusTarget` | type | Indexed type `GraphBlastRadiusTarget` in `crates/gcode/src/graph/code_graph/payload.rs`. [crates/gcode/src/graph/code_graph/payload.rs:250-253] |
| `extracted_code_edge_metadata` | function | Constructs a 'ProjectionMetadata' for extracted edge code by initializing 'gcode_extracted' metadata with the given source file path and line number, and conditionally attaching a source symbol ID when provided. [crates/gcode/src/graph/code_graph/payload.rs:254-266] |
| `row_to_projection_metadata` | function | Builds a 'ProjectionMetadata' from a database 'Row' by requiring valid 'provenance' and 'source_system', then populating optional fields such as confidence, source file path, source line, source symbol ID, and matching method from several fallback column names, returning 'None' if the required values are missing or invalid. [crates/gcode/src/graph/code_graph/payload.rs:268-294] |
| `row_string_owned` | function | Returns the first non-empty string value found in 'row' for any key in 'keys', cloning it into an owned 'String', or 'None' if no such string exists. [crates/gcode/src/graph/code_graph/payload.rs:296-301] |
| `row_usize` | function | Returns the first integer-valued field found under any of the provided keys in 'row', converting nonnegative 'u64'/'i64' values to 'usize' with checked conversion, logging and returning 'None' for negative 'i64' values that cannot fit. [crates/gcode/src/graph/code_graph/payload.rs:303-320] |
| `add_link_from_row` | function | Attempts to parse a 'GraphLink' from 'row' and, if successful, appends it to 'payload.links'. [crates/gcode/src/graph/code_graph/payload.rs:322-326] |
| `add_node_from_row` | function | Creates a 'GraphNode' from 'row' using 'default_type' and appends it to 'payload' only if node construction succeeds. [crates/gcode/src/graph/code_graph/payload.rs:328-332] |
| `add_prefixed_node_from_row` | function | Parses a 'GraphNode' from 'row' using the given 'prefix' and 'default_type', and if successful pushes it into 'payload'. [crates/gcode/src/graph/code_graph/payload.rs:334-343] |

