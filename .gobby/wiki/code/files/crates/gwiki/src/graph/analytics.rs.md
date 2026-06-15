---
title: crates/gwiki/src/graph/analytics.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/analytics.rs
  ranges:
  - 14-22
  - 24-39
  - '41'
  - 44-51
  - 54-58
  - 61-65
  - 68-71
  - 74-78
  - 81-85
  - 87-91
  - 94-98
  - 100-161
  - 163-184
  - 186-221
  - 223-235
  - 237-245
  - 247-255
  - 257-264
  - 266-274
  - 288-319
  - 322-347
  - 350-365
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/analytics.rs

Module: [[code/modules/crates/gwiki/src/graph|crates/gwiki/src/graph]]

## Purpose

Builds graph analytics from wiki facts and converts the core analytics results into export-friendly records. It defines a `GraphAnalyticsError` for duplicate node metadata, constructs an `AnalyticsGraph` by inserting document/source/citation/link-related nodes and edges, and provides `from_core`/`From` conversions that map core communities, centrality, hotspots, node refs, and edge refs into serialized export structs.
[crates/gwiki/src/graph/analytics.rs:14-22]
[crates/gwiki/src/graph/analytics.rs:24-39]
[crates/gwiki/src/graph/analytics.rs:25-38]
[crates/gwiki/src/graph/analytics.rs:41]
[crates/gwiki/src/graph/analytics.rs:44-51]

## API Symbols

- `GraphAnalyticsError` (type) component `GraphAnalyticsError [type]` (`a728344c-24af-5a8a-bcb1-e70ff6b39cea`) lines 14-22 [crates/gwiki/src/graph/analytics.rs:14-22]
  - Signature: `pub enum GraphAnalyticsError {`
  - Purpose: Indexed type `GraphAnalyticsError` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:14-22]
- `GraphAnalyticsError` (class) component `GraphAnalyticsError [class]` (`80311bef-5cbf-577a-a865-dfc51df63524`) lines 24-39 [crates/gwiki/src/graph/analytics.rs:24-39]
  - Signature: `impl std::fmt::Display for GraphAnalyticsError {`
  - Purpose: 'GraphAnalyticsError' is a 'Display' implementation that formats the 'DuplicateNode' variant as a diagnostic message reporting a duplicate graph node ID and the conflicting existing versus duplicate kind and weight metadata. [crates/gwiki/src/graph/analytics.rs:24-39]
- `GraphAnalyticsError.fmt` (method) component `GraphAnalyticsError.fmt [method]` (`0410a958-c158-5f73-a010-4d238fbde733`) lines 25-38 [crates/gwiki/src/graph/analytics.rs:25-38]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Formats the 'DuplicateNode' variant as a human-readable error message describing the node ID and the conflicting existing versus duplicate kind and weight metadata. [crates/gwiki/src/graph/analytics.rs:25-38]
- `GraphAnalyticsError` (class) component `GraphAnalyticsError [class]` (`c7cedb8e-ca45-5e55-a0fd-054d0d56200f`) lines 41-41 [crates/gwiki/src/graph/analytics.rs:41]
  - Signature: `impl std::error::Error for GraphAnalyticsError {}`
  - Purpose: 'GraphAnalyticsError' is a Rust error type that implements the standard 'std::error::Error' trait, making it usable anywhere a trait-object-compatible error is required. [crates/gwiki/src/graph/analytics.rs:41]
- `GraphExportAnalytics` (class) component `GraphExportAnalytics [class]` (`bd8038f9-aef7-589f-b93a-6f9620d5c9a6`) lines 44-51 [crates/gwiki/src/graph/analytics.rs:44-51]
  - Signature: `pub struct GraphExportAnalytics {`
  - Purpose: 'GraphExportAnalytics' is a graph-export analysis container that aggregates community detections, node centrality results, bridge and hub node references, unexpected edge references, and hotspot findings. [crates/gwiki/src/graph/analytics.rs:44-51]
- `GraphExportCommunity` (class) component `GraphExportCommunity [class]` (`991274d0-969a-592f-b866-36c2e3136f33`) lines 54-58 [crates/gwiki/src/graph/analytics.rs:54-58]
  - Signature: `pub struct GraphExportCommunity {`
  - Purpose: 'GraphExportCommunity' is a public data container for a community in a graph export, holding its string identifier, the referenced nodes belonging to it, and a floating-point weight. [crates/gwiki/src/graph/analytics.rs:54-58]
- `GraphExportCentrality` (class) component `GraphExportCentrality [class]` (`65447477-7b2a-5a7d-88b9-8907c05a5a31`) lines 61-65 [crates/gwiki/src/graph/analytics.rs:61-65]
  - Signature: `pub struct GraphExportCentrality {`
  - Purpose: 'GraphExportCentrality' is a Rust data structure that associates a 'GraphExportNodeRef' with its integer degree and a floating-point centrality score for graph export. [crates/gwiki/src/graph/analytics.rs:61-65]
- `GraphExportNodeRef` (class) component `GraphExportNodeRef [class]` (`6095a595-4dc2-51c8-bc6d-1b1428493295`) lines 68-71 [crates/gwiki/src/graph/analytics.rs:68-71]
  - Signature: `pub struct GraphExportNodeRef {`
  - Purpose: 'GraphExportNodeRef' is a plain data struct that identifies an exported graph node by its 'id' and semantic 'kind', both stored as 'String' values. [crates/gwiki/src/graph/analytics.rs:68-71]
- `GraphExportEdgeRef` (class) component `GraphExportEdgeRef [class]` (`13ad723c-d4a5-59f8-9688-9c6fef0e3ff1`) lines 74-78 [crates/gwiki/src/graph/analytics.rs:74-78]
  - Signature: `pub struct GraphExportEdgeRef {`
  - Purpose: 'GraphExportEdgeRef' is a simple exported edge record containing the 'source' node ID, 'target' node ID, and edge 'kind', all stored as 'String' values. [crates/gwiki/src/graph/analytics.rs:74-78]
- `GraphExportHotspot` (class) component `GraphExportHotspot [class]` (`57cf85b0-e509-5b48-af83-f19998bc1709`) lines 81-85 [crates/gwiki/src/graph/analytics.rs:81-85]
  - Signature: `pub struct GraphExportHotspot {`
  - Purpose: 'GraphExportHotspot' is a data structure that identifies a graph export node reference as a hotspot and associates it with an occurrence frequency and a floating-point weight score. [crates/gwiki/src/graph/analytics.rs:81-85]
- `analyze_facts` (function) component `analyze_facts [function]` (`79cd25b2-34a4-56fa-ad19-122096231d80`) lines 87-91 [crates/gwiki/src/graph/analytics.rs:87-91]
  - Signature: `pub fn analyze_facts(facts: &WikiGraphFacts) -> Result<GraphExportAnalytics, GraphAnalyticsError> {`
  - Purpose: Builds an analytics graph from 'WikiGraphFacts', runs core analysis on it, and wraps the result in 'GraphExportAnalytics', propagating any graph-construction or analysis errors. [crates/gwiki/src/graph/analytics.rs:87-91]
- `analytics_graph_from_memory` (function) component `analytics_graph_from_memory [function]` (`6d03da4d-80fa-51c9-8fd5-174c617260c4`) lines 94-98 [crates/gwiki/src/graph/analytics.rs:94-98]
  - Signature: `pub fn analytics_graph_from_memory(`
  - Purpose: Builds an 'AnalyticsGraph' from a 'MemoryWikiGraph' by delegating to 'analytics_graph_from_facts' on the graph’s 'facts' collection, returning a 'GraphAnalyticsError' on failure. [crates/gwiki/src/graph/analytics.rs:94-98]
- `analytics_graph_from_facts` (function) component `analytics_graph_from_facts [function]` (`88ba2ef7-d638-54aa-9256-b846ade995ca`) lines 100-161 [crates/gwiki/src/graph/analytics.rs:100-161]
  - Signature: `pub fn analytics_graph_from_facts(`
  - Purpose: Builds an 'AnalyticsGraph' from 'WikiGraphFacts' by inserting document, source, citation, resolved-link, and unresolved-target nodes with fixed weights and emitting 'supports', 'cites', and 'links' edges between the corresponding node IDs. [crates/gwiki/src/graph/analytics.rs:100-161]
- `insert_node` (function) component `insert_node [function]` (`11666de7-90ca-5e58-84ce-cde8b3d982d0`) lines 163-184 [crates/gwiki/src/graph/analytics.rs:163-184]
  - Signature: `fn insert_node(`
  - Purpose: Inserts a new 'AnalyticsNode' into the 'BTreeMap' by 'id', or returns a 'DuplicateNode' error if an existing node with the same 'id' has different 'kind' or 'weight', while treating an identical duplicate as a no-op. [crates/gwiki/src/graph/analytics.rs:163-184]
- `GraphExportAnalytics` (class) component `GraphExportAnalytics [class]` (`8fc5924b-464e-5324-a14e-7b24583f9ade`) lines 186-221 [crates/gwiki/src/graph/analytics.rs:186-221]
  - Signature: `impl GraphExportAnalytics {`
  - Purpose: 'GraphExportAnalytics' is a conversion wrapper that transforms a 'GraphAnalytics' instance into export-ready collections of communities, centrality records, bridge and god-node references, unexpected link references, and hotspot entries via 'from_core' mappings. [crates/gwiki/src/graph/analytics.rs:186-221]
- `GraphExportAnalytics.from_core` (method) component `GraphExportAnalytics.from_core [method]` (`54e18678-d866-5f33-85a9-d819dc9fdb81`) lines 187-220 [crates/gwiki/src/graph/analytics.rs:187-220]
  - Signature: `fn from_core(analytics: GraphAnalytics) -> Self {`
  - Purpose: Converts a 'GraphAnalytics' into 'Self' by mapping each analytics collection into its corresponding export type, including communities, centrality, bridge and god node references, unexpected link references, and hotspots. [crates/gwiki/src/graph/analytics.rs:187-220]
- `GraphExportCommunity` (class) component `GraphExportCommunity [class]` (`e70dce11-cea7-5efa-b359-5a57213eda4a`) lines 223-235 [crates/gwiki/src/graph/analytics.rs:223-235]
  - Signature: `impl GraphExportCommunity {`
  - Purpose: 'GraphExportCommunity' is a conversion wrapper that constructs a graph-export community record from a core 'Community', preserving its 'id' and 'weight' while transforming each contained node into a 'GraphExportNodeRef'. [crates/gwiki/src/graph/analytics.rs:223-235]
- `GraphExportCommunity.from_core` (method) component `GraphExportCommunity.from_core [method]` (`78267316-5e7f-5fb7-b0c2-8a8e4eec2910`) lines 224-234 [crates/gwiki/src/graph/analytics.rs:224-234]
  - Signature: `fn from_core(community: Community) -> Self {`
  - Purpose: Constructs a 'Self' by moving 'community.id', converting each 'community.nodes' element into a 'GraphExportNodeRef', and copying 'community.weight'. [crates/gwiki/src/graph/analytics.rs:224-234]
- `GraphExportCentrality` (class) component `GraphExportCentrality [class]` (`1154dac3-4b86-55a5-a4e0-da536452fe97`) lines 237-245 [crates/gwiki/src/graph/analytics.rs:237-245]
  - Signature: `impl GraphExportCentrality {`
  - Purpose: 'GraphExportCentrality' is a conversion wrapper that constructs an export-facing centrality record from a 'CentralityScore' by mapping the node reference through 'GraphExportNodeRef::from' and copying the 'degree' and 'score' fields unchanged. [crates/gwiki/src/graph/analytics.rs:237-245]
- `GraphExportCentrality.from_core` (method) component `GraphExportCentrality.from_core [method]` (`5e0b58ed-d457-58a5-bdd8-92349055d719`) lines 238-244 [crates/gwiki/src/graph/analytics.rs:238-244]
  - Signature: `fn from_core(score: CentralityScore) -> Self {`
  - Purpose: Constructs a 'Self' by converting 'score.node' into a 'GraphExportNodeRef' and copying over the 'degree' and 'score' fields from the provided 'CentralityScore'. [crates/gwiki/src/graph/analytics.rs:238-244]
- `GraphExportHotspot` (class) component `GraphExportHotspot [class]` (`d9b76b9a-9db0-5737-beca-4c32b628ec63`) lines 247-255 [crates/gwiki/src/graph/analytics.rs:247-255]
  - Signature: `impl GraphExportHotspot {`
  - Purpose: 'GraphExportHotspot' is a conversion wrapper that constructs an exportable hotspot record from a core 'Hotspot', mapping its node into a 'GraphExportNodeRef' while copying the 'frequency' and 'weight' fields unchanged. [crates/gwiki/src/graph/analytics.rs:247-255]
- `GraphExportHotspot.from_core` (method) component `GraphExportHotspot.from_core [method]` (`106df146-0da5-52fa-b6e3-851848e4b6ac`) lines 248-254 [crates/gwiki/src/graph/analytics.rs:248-254]
  - Signature: `fn from_core(hotspot: Hotspot) -> Self {`
  - Purpose: Constructs 'Self' by converting 'hotspot.node' into a 'GraphExportNodeRef' and copying 'hotspot.frequency' and 'hotspot.weight' into the corresponding fields. [crates/gwiki/src/graph/analytics.rs:248-254]
- `GraphExportNodeRef` (class) component `GraphExportNodeRef [class]` (`39e5f959-a144-5278-a123-96f7c9e4eb99`) lines 257-264 [crates/gwiki/src/graph/analytics.rs:257-264]
  - Signature: `impl From<NodeRef> for GraphExportNodeRef {`
  - Purpose: 'GraphExportNodeRef' is a conversion target that implements 'From<NodeRef>' by constructing a new export reference containing only the source node’s 'id' and 'kind' fields. [crates/gwiki/src/graph/analytics.rs:257-264]
- `GraphExportNodeRef.from` (method) component `GraphExportNodeRef.from [method]` (`c0440e5b-0a07-5671-abcd-1db61053bda8`) lines 258-263 [crates/gwiki/src/graph/analytics.rs:258-263]
  - Signature: `fn from(node: NodeRef) -> Self {`
  - Purpose: Constructs 'Self' by copying the 'id' and 'kind' fields from the provided 'NodeRef' into a new instance. [crates/gwiki/src/graph/analytics.rs:258-263]
- `GraphExportEdgeRef` (class) component `GraphExportEdgeRef [class]` (`0095c9da-702f-5cb4-8b6c-8c2c2e9dff50`) lines 266-274 [crates/gwiki/src/graph/analytics.rs:266-274]
  - Signature: `impl From<EdgeRef> for GraphExportEdgeRef {`
  - Purpose: 'GraphExportEdgeRef' is a conversion target that implements 'From<EdgeRef>' by copying the 'source', 'target', and 'kind' fields from an 'EdgeRef' into a new export edge reference. [crates/gwiki/src/graph/analytics.rs:266-274]
- `GraphExportEdgeRef.from` (method) component `GraphExportEdgeRef.from [method]` (`3a73bcf9-9765-58e0-9090-09c68a9fdfb1`) lines 267-273 [crates/gwiki/src/graph/analytics.rs:267-273]
  - Signature: `fn from(edge: EdgeRef) -> Self {`
  - Purpose: Constructs a new 'Self' by moving 'source', 'target', and 'kind' directly from the given 'EdgeRef'. [crates/gwiki/src/graph/analytics.rs:267-273]
- `graph_analytics_converts_memory_graph_to_core_graph` (function) component `graph_analytics_converts_memory_graph_to_core_graph [function]` (`3ad916c3-f82b-5773-9170-04d1263017f6`) lines 288-319 [crates/gwiki/src/graph/analytics.rs:288-319]
  - Signature: `fn graph_analytics_converts_memory_graph_to_core_graph() {`
  - Purpose: Verifies that 'analytics_graph_from_memory' converts a memory wiki graph with two documents and one resolved link into a core analytics graph containing two nodes, one edge, and an edge kind of '"links"'. [crates/gwiki/src/graph/analytics.rs:288-319]
- `graph_analytics_adds_placeholder_for_missing_resolved_target` (function) component `graph_analytics_adds_placeholder_for_missing_resolved_target [function]` (`f3e40b0f-2820-518f-a6cc-6650349c24a4`) lines 322-347 [crates/gwiki/src/graph/analytics.rs:322-347]
  - Signature: `fn graph_analytics_adds_placeholder_for_missing_resolved_target() {`
  - Purpose: Verifies that 'analytics_graph_from_memory' creates a 'wiki_page' placeholder node with weight '1.0' for a link target that is resolved in the graph facts but missing from the document set. [crates/gwiki/src/graph/analytics.rs:322-347]
- `graph_analytics_rejects_duplicate_node_metadata` (function) component `graph_analytics_rejects_duplicate_node_metadata [function]` (`810cf12d-73c7-590a-9d9f-c0a878e7a6e4`) lines 350-365 [crates/gwiki/src/graph/analytics.rs:350-365]
  - Signature: `fn graph_analytics_rejects_duplicate_node_metadata() {`
  - Purpose: Verifies that inserting a second node with the same ID into the graph analytics node map fails with 'GraphAnalyticsError::DuplicateNode' and preserves the original kind ('"topic"') alongside the conflicting duplicate kind ('"source"'). [crates/gwiki/src/graph/analytics.rs:350-365]

