---
title: crates/gwiki/src/search/graph_boost.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/graph_boost.rs
  ranges:
  - 21-24
  - 26-33
  - 35-39
  - 41-44
  - 46-51
  - '54'
  - 56-66
  - 68-70
  - 72-78
  - 80-90
  - 93-98
  - 101-103
  - 105-109
  - 111-124
  - 126-129
  - 131-146
  - 148-185
  - 188-191
  - 194-197
  - 199-264
  - 266-277
  - 279-301
  - 303-308
  - 310-347
  - 349-362
  - 364-384
  - 386-392
  - 399-427
  - 430-452
  - 455-473
  - 476-489
  - 492-512
  - 514-519
  - 521-526
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/graph_boost.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Purpose

This file defines the graph-boost search layer for `gwiki`: configuration and request/response types, a `GraphBoostBackend` trait, and three backend implementations for no-op, unavailable, in-memory, and Falkor-backed search. The supporting helpers normalize and resolve link targets, rank neighbor documents from outbound links and backlinks, turn ranked paths into `WikiSearchResult` hits, and attach degradation metadata when the graph service is unavailable.
[crates/gwiki/src/search/graph_boost.rs:21-24]
[crates/gwiki/src/search/graph_boost.rs:26-33]
[crates/gwiki/src/search/graph_boost.rs:27-32]
[crates/gwiki/src/search/graph_boost.rs:35-39]
[crates/gwiki/src/search/graph_boost.rs:41-44]

## API Symbols

- `GraphBoostConfig` (class) component `GraphBoostConfig [class]` (`c6a6d24a-b8ee-52d3-9c20-562e234ab20e`) lines 21-24 [crates/gwiki/src/search/graph_boost.rs:21-24]
  - Signature: `pub struct GraphBoostConfig {`
  - Purpose: 'GraphBoostConfig' is a Rust configuration struct that sets separate integer query limits for document searches and link searches via 'document_query_limit' and 'link_query_limit'. [crates/gwiki/src/search/graph_boost.rs:21-24]
- `GraphBoostConfig` (class) component `GraphBoostConfig [class]` (`111dfcc3-3f75-57aa-87b0-b9dc128ebbcb`) lines 26-33 [crates/gwiki/src/search/graph_boost.rs:26-33]
  - Signature: `impl Default for GraphBoostConfig {`
  - Purpose: 'GraphBoostConfig' is a Rust configuration type whose 'Default' implementation initializes 'document_query_limit' and 'link_query_limit' from the corresponding 'DEFAULT_GRAPH_BOOST_*' constants. [crates/gwiki/src/search/graph_boost.rs:26-33]
- `GraphBoostConfig.default` (method) component `GraphBoostConfig.default [method]` (`78eceb97-9cc6-5e56-b572-150250b3dbd6`) lines 27-32 [crates/gwiki/src/search/graph_boost.rs:27-32]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a 'Self' instance initialized with 'document_query_limit' set to 'DEFAULT_GRAPH_BOOST_DOCUMENT_QUERY_LIMIT' and 'link_query_limit' set to 'DEFAULT_GRAPH_BOOST_LINK_QUERY_LIMIT'. [crates/gwiki/src/search/graph_boost.rs:27-32]
- `GraphBoostRequest` (class) component `GraphBoostRequest [class]` (`8f5be825-7c2b-53eb-b02a-82f0654d2051`) lines 35-39 [crates/gwiki/src/search/graph_boost.rs:35-39]
  - Signature: `pub struct GraphBoostRequest {`
  - Purpose: 'GraphBoostRequest' is a request struct that specifies a 'SearchScope', a set of seed file paths ('Vec<PathBuf>'), and a result 'limit' ('usize') for a graph-boosted search operation. [crates/gwiki/src/search/graph_boost.rs:35-39]
- `GraphBoostOutcome` (class) component `GraphBoostOutcome [class]` (`3a59b0b5-bc0e-5cd9-9b25-309e57f45d4b`) lines 41-44 [crates/gwiki/src/search/graph_boost.rs:41-44]
  - Signature: `pub struct GraphBoostOutcome {`
  - Purpose: 'GraphBoostOutcome' is a struct that packages the boosted graph-search results as a 'Vec<WikiSearchResult>' and an optional 'DegradationKind' indicating whether and how the boost operation degraded. [crates/gwiki/src/search/graph_boost.rs:41-44]
- `GraphBoostBackend` (type) component `GraphBoostBackend [type]` (`79b9f5cf-8ade-5662-b3ca-60dc0207e563`) lines 46-51 [crates/gwiki/src/search/graph_boost.rs:46-51]
  - Signature: `pub trait GraphBoostBackend {`
  - Purpose: Indexed type `GraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:46-51]
- `NoopGraphBoostBackend` (class) component `NoopGraphBoostBackend [class]` (`fdcf7e67-3ae8-5cd0-bbf5-cbf0b414835b`) lines 54-54 [crates/gwiki/src/search/graph_boost.rs:54]
  - Signature: `pub struct NoopGraphBoostBackend;`
  - Purpose: 'NoopGraphBoostBackend' is a zero-sized Rust unit struct that represents a no-op implementation of the graph-boost backend interface. [crates/gwiki/src/search/graph_boost.rs:54]
- `NoopGraphBoostBackend` (class) component `NoopGraphBoostBackend [class]` (`10a25239-1459-5946-89f1-9e0a51be5313`) lines 56-66 [crates/gwiki/src/search/graph_boost.rs:56-66]
  - Signature: `impl GraphBoostBackend for NoopGraphBoostBackend {`
  - Purpose: 'NoopGraphBoostBackend' is a 'GraphBoostBackend' implementation whose 'search_graph_boost' method ignores the request and always returns an empty 'GraphBoostOutcome' with no degradation. [crates/gwiki/src/search/graph_boost.rs:56-66]
- `NoopGraphBoostBackend.search_graph_boost` (method) component `NoopGraphBoostBackend.search_graph_boost [method]` (`f32690f3-5a50-56d2-ba9a-9cbcfdecf2fe`) lines 57-65 [crates/gwiki/src/search/graph_boost.rs:57-65]
  - Signature: `fn search_graph_boost(`
  - Purpose: 'search_graph_boost' ignores the provided 'GraphBoostRequest' and immediately returns 'Ok(GraphBoostOutcome { hits: Vec::new(), degradation: None })', i.e. an empty successful outcome with no degradation. [crates/gwiki/src/search/graph_boost.rs:57-65]
- `UnavailableGraphBoostBackend` (class) component `UnavailableGraphBoostBackend [class]` (`40dcc694-d455-5d95-878f-28874a4b72f6`) lines 68-70 [crates/gwiki/src/search/graph_boost.rs:68-70]
  - Signature: `pub struct UnavailableGraphBoostBackend {`
  - Purpose: 'UnavailableGraphBoostBackend' is a Rust struct that stores a 'DegradationKind' value describing how the GraphBoost backend is degraded or unavailable. [crates/gwiki/src/search/graph_boost.rs:68-70]
- `UnavailableGraphBoostBackend` (class) component `UnavailableGraphBoostBackend [class]` (`85b9c1ad-d53f-5860-b15d-eaa2f692e7b0`) lines 72-78 [crates/gwiki/src/search/graph_boost.rs:72-78]
  - Signature: `impl UnavailableGraphBoostBackend {`
  - Purpose: 'UnavailableGraphBoostBackend' is a constructor-only Rust impl that creates an instance whose 'degradation' field is initialized from a 'graph_degradation(message)' value to represent an unreachable backend state. [crates/gwiki/src/search/graph_boost.rs:72-78]
- `UnavailableGraphBoostBackend.unreachable` (method) component `UnavailableGraphBoostBackend.unreachable [method]` (`add1c616-c757-52e5-a5c1-55ee56ebaa9f`) lines 73-77 [crates/gwiki/src/search/graph_boost.rs:73-77]
  - Signature: `pub fn unreachable(message: String) -> Self {`
  - Purpose: Constructs a 'Self' instance whose 'degradation' field is initialized from 'graph_degradation(message)'. [crates/gwiki/src/search/graph_boost.rs:73-77]
- `UnavailableGraphBoostBackend` (class) component `UnavailableGraphBoostBackend [class]` (`bc4ba5f4-1b2f-5625-9238-9c17078bff8f`) lines 80-90 [crates/gwiki/src/search/graph_boost.rs:80-90]
  - Signature: `impl GraphBoostBackend for UnavailableGraphBoostBackend {`
  - Purpose: 'UnavailableGraphBoostBackend' is a 'GraphBoostBackend' implementation that ignores every search request and returns an empty 'GraphBoostOutcome' while propagating its stored 'degradation' state. [crates/gwiki/src/search/graph_boost.rs:80-90]
- `UnavailableGraphBoostBackend.search_graph_boost` (method) component `UnavailableGraphBoostBackend.search_graph_boost [method]` (`0a53f15f-1efa-59fd-86e8-dbf219fb2520`) lines 81-89 [crates/gwiki/src/search/graph_boost.rs:81-89]
  - Signature: `fn search_graph_boost(`
  - Purpose: 'search_graph_boost' ignores the request, returns an empty 'hits' vector, and propagates the current 'degradation' state by cloning 'self.degradation' into a successful 'GraphBoostOutcome'. [crates/gwiki/src/search/graph_boost.rs:81-89]
- `search_graph_boost` (function) component `search_graph_boost [function]` (`70163a3f-43fe-5629-80aa-8c5df7226a57`) lines 93-98 [crates/gwiki/src/search/graph_boost.rs:93-98]
  - Signature: `fn search_graph_boost(`
  - Purpose: Forwards the 'GraphBoostRequest' to the inner 'search_graph_boost' implementation via double dereference and returns its 'Result<GraphBoostOutcome, SearchError>'. [crates/gwiki/src/search/graph_boost.rs:93-98]
- `MemoryGraphBoostBackend` (class) component `MemoryGraphBoostBackend [class]` (`1d246388-9a09-55e8-ac0a-d925bebd6cab`) lines 101-103 [crates/gwiki/src/search/graph_boost.rs:101-103]
  - Signature: `pub struct MemoryGraphBoostBackend {`
  - Purpose: 'MemoryGraphBoostBackend' is a Rust struct that encapsulates a single 'MemoryWikiGraph' instance as its internal 'graph' backend state. [crates/gwiki/src/search/graph_boost.rs:101-103]
- `MemoryGraphBoostBackend` (class) component `MemoryGraphBoostBackend [class]` (`3f9bc16a-2c00-5675-9203-3f7e80cfb5d2`) lines 105-109 [crates/gwiki/src/search/graph_boost.rs:105-109]
  - Signature: `impl MemoryGraphBoostBackend {`
  - Purpose: 'MemoryGraphBoostBackend' is a thin wrapper type that owns a 'MemoryWikiGraph' and provides a 'new' constructor that initializes the backend by storing the supplied graph. [crates/gwiki/src/search/graph_boost.rs:105-109]
- `MemoryGraphBoostBackend.new` (method) component `MemoryGraphBoostBackend.new [method]` (`8c18633a-8ea1-5131-8d52-c333b9b42f3b`) lines 106-108 [crates/gwiki/src/search/graph_boost.rs:106-108]
  - Signature: `pub fn new(graph: MemoryWikiGraph) -> Self {`
  - Purpose: Constructs a new instance by initializing 'Self' with the provided 'MemoryWikiGraph' stored in its 'graph' field. [crates/gwiki/src/search/graph_boost.rs:106-108]
- `MemoryGraphBoostBackend` (class) component `MemoryGraphBoostBackend [class]` (`0bbd103a-f087-5b8b-b5fd-74d1be8652bc`) lines 111-124 [crates/gwiki/src/search/graph_boost.rs:111-124]
  - Signature: `impl GraphBoostBackend for MemoryGraphBoostBackend {`
  - Purpose: 'MemoryGraphBoostBackend' implements 'GraphBoostBackend' by computing related graph paths from the request scope, seed paths, and limit, then returning them as 'GraphBoostOutcome.hits' with no degradation. [crates/gwiki/src/search/graph_boost.rs:111-124]
- `MemoryGraphBoostBackend.search_graph_boost` (method) component `MemoryGraphBoostBackend.search_graph_boost [method]` (`6790f5e3-3bd0-52ab-a222-0c1734c084a1`) lines 112-123 [crates/gwiki/src/search/graph_boost.rs:112-123]
  - Signature: `fn search_graph_boost(`
  - Purpose: 'search_graph_boost' computes related paths from the graph for the request scope and seed paths up to the requested limit, then returns a 'GraphBoostOutcome' containing graph-boost hits derived from those ranked paths with 'degradation' set to 'None'. [crates/gwiki/src/search/graph_boost.rs:112-123]
- `FalkorGraphBoostBackend` (class) component `FalkorGraphBoostBackend [class]` (`712ab77e-617b-5fd8-9c07-592dc9d51642`) lines 126-129 [crates/gwiki/src/search/graph_boost.rs:126-129]
  - Signature: `pub struct FalkorGraphBoostBackend {`
  - Purpose: 'FalkorGraphBoostBackend' is a backend wrapper that holds a 'GraphClient' and a 'GraphBoostConfig', encapsulating the client and configuration needed to operate the graph-boost integration. [crates/gwiki/src/search/graph_boost.rs:126-129]
- `FalkorGraphBoostBackend` (class) component `FalkorGraphBoostBackend [class]` (`d4cfaa9b-2244-5fa3-a8d4-556ad1602614`) lines 131-146 [crates/gwiki/src/search/graph_boost.rs:131-146]
  - Signature: `impl FalkorGraphBoostBackend {`
  - Purpose: 'FalkorGraphBoostBackend' is a thin constructor wrapper that initializes a FalkorDB 'GraphClient' from 'FalkorConfig' using the fixed wiki graph name, maps connection failures into 'SearchError::Backend', and stores the resulting client alongside a 'GraphBoostConfig'. [crates/gwiki/src/search/graph_boost.rs:131-146]
- `FalkorGraphBoostBackend.new` (method) component `FalkorGraphBoostBackend.new [method]` (`7cc7999d-089c-5f8c-937b-9857da600394`) lines 132-134 [crates/gwiki/src/search/graph_boost.rs:132-134]
  - Signature: `pub fn new(config: &FalkorConfig) -> Result<Self, SearchError> {`
  - Purpose: Constructs a new instance by delegating to 'new_with_config' with the provided 'FalkorConfig' and 'GraphBoostConfig::default()', returning a 'Result<Self, SearchError>'. [crates/gwiki/src/search/graph_boost.rs:132-134]
- `FalkorGraphBoostBackend.new_with_config` (method) component `FalkorGraphBoostBackend.new_with_config [method]` (`0bd13d2e-41a2-591a-a482-6b576bc6976b`) lines 136-145 [crates/gwiki/src/search/graph_boost.rs:136-145]
  - Signature: `pub fn new_with_config(`
  - Purpose: Constructs a 'GraphBoost' instance by creating a 'GraphClient' from the provided 'FalkorConfig' for the 'FALKORDB_GRAPH_NAME' graph, mapping any connection failure into 'SearchError::Backend', and returning 'Self { client, config }'. [crates/gwiki/src/search/graph_boost.rs:136-145]
- `FalkorGraphBoostBackend` (class) component `FalkorGraphBoostBackend [class]` (`1b495188-16e0-5626-9fe5-790990586a6c`) lines 148-185 [crates/gwiki/src/search/graph_boost.rs:148-185]
  - Signature: `impl GraphBoostBackend for FalkorGraphBoostBackend {`
  - Purpose: 'FalkorGraphBoostBackend' implements 'GraphBoostBackend' by short-circuiting empty requests, loading graph-boost data from Falkor with configured query limits, returning an empty degraded outcome on load failure, and otherwise ranking link neighborhoods around the seed paths to produce scoped graph-boost hits with any upstream degradation metadata. [crates/gwiki/src/search/graph_boost.rs:148-185]
- `FalkorGraphBoostBackend.search_graph_boost` (method) component `FalkorGraphBoostBackend.search_graph_boost [method]` (`2e663a3b-96f6-5002-abfb-da5c0995391b`) lines 149-184 [crates/gwiki/src/search/graph_boost.rs:149-184]
  - Signature: `fn search_graph_boost(`
  - Purpose: 'search_graph_boost' returns an empty 'GraphBoostOutcome' when the requested limit is zero or there are no seed paths, otherwise it loads graph-boost data for the requested scope, ranks link neighborhoods around the seed paths up to the limit, and returns the resulting hits with any degradation information from the load step. [crates/gwiki/src/search/graph_boost.rs:149-184]
- `GraphBoostDocument` (class) component `GraphBoostDocument [class]` (`fde38213-4994-52f6-af90-c7927cdbbb4d`) lines 188-191 [crates/gwiki/src/search/graph_boost.rs:188-191]
  - Signature: `pub struct GraphBoostDocument {`
  - Purpose: 'GraphBoostDocument' is a Rust struct that represents a document identified by a filesystem 'path' and an optional 'title' string. [crates/gwiki/src/search/graph_boost.rs:188-191]
- `GraphBoostLink` (class) component `GraphBoostLink [class]` (`2d5784f3-b5af-54db-9564-f1dfb698531a`) lines 194-197 [crates/gwiki/src/search/graph_boost.rs:194-197]
  - Signature: `pub struct GraphBoostLink {`
  - Purpose: 'GraphBoostLink' is a Rust data structure that represents a link from a source filesystem path ('PathBuf') to a target path string ('String'). [crates/gwiki/src/search/graph_boost.rs:194-197]
- `rank_link_neighborhood` (function) component `rank_link_neighborhood [function]` (`399bea63-f61b-5125-b349-6fbb15c7749e`) lines 199-264 [crates/gwiki/src/search/graph_boost.rs:199-264]
  - Signature: `pub fn rank_link_neighborhood(`
  - Purpose: Ranks non-seed graph neighbors of the provided seed paths by accumulating weighted scores from direct outbound links and backlinks to valid document paths, then returns the top results sorted by descending score. [crates/gwiki/src/search/graph_boost.rs:199-264]
- `graph_boost_hits` (function) component `graph_boost_hits [function]` (`c5b8b0c9-5895-5b22-b50d-9380acf8430d`) lines 266-277 [crates/gwiki/src/search/graph_boost.rs:266-277]
  - Signature: `pub fn graph_boost_hits(`
  - Purpose: 'graph_boost_hits' filters the input '(PathBuf, score)' candidates to keyword-searchable paths, truncates the list to 'limit', converts each remaining path and score into a 'WikiSearchResult' via 'graph_result', and returns the collected results. [crates/gwiki/src/search/graph_boost.rs:266-277]
- `graph_result` (function) component `graph_result [function]` (`252c20c0-2879-5e9a-ace9-2c20b779f1bb`) lines 279-301 [crates/gwiki/src/search/graph_boost.rs:279-301]
  - Signature: `fn graph_result(scope: &SearchScope, path: PathBuf, score: f64) -> WikiSearchResult {`
  - Purpose: Constructs a 'WikiSearchResult' for a graph-backed document path by normalizing the path into a 'document:' ID, cloning the search scope and path into provenance fields, marking the hit as a document from 'SearchSource::Graph', and attaching the provided score. [crates/gwiki/src/search/graph_boost.rs:279-301]
- `graph_degradation` (function) component `graph_degradation [function]` (`c3c15f84-b5cf-5302-a3df-fbab1d14abad`) lines 303-308 [crates/gwiki/src/search/graph_boost.rs:303-308]
  - Signature: `fn graph_degradation(message: String) -> DegradationKind {`
  - Purpose: Creates and returns a 'DegradationKind::ServiceUnavailable' for 'GRAPH_SERVICE', wrapping the provided 'message' in 'ServiceState::Unreachable'. [crates/gwiki/src/search/graph_boost.rs:303-308]
- `resolve_graph_target` (function) component `resolve_graph_target [function]` (`dc80325d-a260-5da1-b7e6-fb3ea37368a9`) lines 310-347 [crates/gwiki/src/search/graph_boost.rs:310-347]
  - Signature: `fn resolve_graph_target(`
  - Purpose: 'resolve_graph_target' normalizes a raw link target, rejects external or empty targets, then resolves it by exact path match, normalized path relative to 'source_path'’s parent, or finally by slug lookup, returning the matching 'PathBuf' if found. [crates/gwiki/src/search/graph_boost.rs:310-347]
- `normalize_path` (function) component `normalize_path [function]` (`78122284-8a95-5c83-a110-878250ca0676`) lines 349-362 [crates/gwiki/src/search/graph_boost.rs:349-362]
  - Signature: `fn normalize_path(path: PathBuf) -> PathBuf {`
  - Purpose: Returns a new 'PathBuf' by iterating the input path’s components and removing '.' and '..' segments while discarding root/prefix components, effectively collapsing the path into a relative, normalized form. [crates/gwiki/src/search/graph_boost.rs:349-362]
- `slug_target_map` (function) component `slug_target_map [function]` (`5497cb79-b2bb-5b5d-943a-0f9d4af8d67e`) lines 364-384 [crates/gwiki/src/search/graph_boost.rs:364-384]
  - Signature: `fn slug_target_map(documents: &[GraphBoostDocument]) -> BTreeMap<String, PathBuf> {`
  - Purpose: Builds a 'BTreeMap' from slugified document file stems and titles to the first corresponding 'PathBuf', preserving the earliest path encountered for each slug. [crates/gwiki/src/search/graph_boost.rs:364-384]
- `is_external_target` (function) component `is_external_target [function]` (`2a76763b-11aa-53db-a2c2-91355e88c41b`) lines 386-392 [crates/gwiki/src/search/graph_boost.rs:386-392]
  - Signature: `fn is_external_target(target: &str) -> bool {`
  - Purpose: Returns 'true' when the target is empty or uses an external URI/network form, specifically containing '://', starting with '//' or '\\\\', or using the 'mailto:' scheme. [crates/gwiki/src/search/graph_boost.rs:386-392]
- `rank_link_neighborhood_boosts_outbound_and_backlinks` (function) component `rank_link_neighborhood_boosts_outbound_and_backlinks [function]` (`919d4929-726e-54d4-bfff-6d45ae422378`) lines 399-427 [crates/gwiki/src/search/graph_boost.rs:399-427]
  - Signature: `fn rank_link_neighborhood_boosts_outbound_and_backlinks() {`
  - Purpose: Verifies that 'rank_link_neighborhood' ranks a seed document’s outbound link target above a backlink target, yielding two results with scores '1.0' for 'knowledge/topics/outbound.md' and '0.8' for 'knowledge/topics/backlink.md'. [crates/gwiki/src/search/graph_boost.rs:399-427]
- `rank_link_neighborhood_filters_non_searchable_before_truncating` (function) component `rank_link_neighborhood_filters_non_searchable_before_truncating [function]` (`b5d596ff-a374-5d33-bbfd-6cc4cc9efee2`) lines 430-452 [crates/gwiki/src/search/graph_boost.rs:430-452]
  - Signature: `fn rank_link_neighborhood_filters_non_searchable_before_truncating() {`
  - Purpose: Verifies that 'rank_link_neighborhood' filters out non-searchable neighborhood entries before applying the truncation limit, so only 'knowledge/topics/low.md' remains ranked at '0.8' when the seed neighborhood is capped at one result. [crates/gwiki/src/search/graph_boost.rs:430-452]
- `rank_link_neighborhood_resolves_targets_relative_to_source` (function) component `rank_link_neighborhood_resolves_targets_relative_to_source [function]` (`d6ed0fc2-a13e-5a0d-9cc3-57070804098c`) lines 455-473 [crates/gwiki/src/search/graph_boost.rs:455-473]
  - Signature: `fn rank_link_neighborhood_resolves_targets_relative_to_source() {`
  - Purpose: Tests that 'rank_link_neighborhood' resolves a relative link target against the source document path, ranking 'knowledge/topics/outbound.md' as the neighborhood result for a link from 'knowledge/topics/seed.md' to 'outbound.md'. [crates/gwiki/src/search/graph_boost.rs:455-473]
- `graph_boost_hits_marks_graph_source` (function) component `graph_boost_hits_marks_graph_source [function]` (`07a0094a-ab99-575b-b481-334a769e52a4`) lines 476-489 [crates/gwiki/src/search/graph_boost.rs:476-489]
  - Signature: `fn graph_boost_hits_marks_graph_source() {`
  - Purpose: Verifies that 'graph_boost_hits' returns a single hit for the 'docs' topic whose source is marked 'SearchSource::Graph' and whose provenance document path is 'knowledge/topics/linked.md'. [crates/gwiki/src/search/graph_boost.rs:476-489]
- `unavailable_graph_backend_reports_service_degradation` (function) component `unavailable_graph_backend_reports_service_degradation [function]` (`5819796a-5e77-539e-9acd-1fbefbc7e2ec`) lines 492-512 [crates/gwiki/src/search/graph_boost.rs:492-512]
  - Signature: `fn unavailable_graph_backend_reports_service_degradation() {`
  - Purpose: Verifies that when an 'UnavailableGraphBoostBackend' is unreachable, 'search_graph_boost' returns an empty hit set and a 'ServiceUnavailable' degradation report for 'GRAPH_SERVICE' whose unreachable message includes 'connection refused'. [crates/gwiki/src/search/graph_boost.rs:492-512]
- `document` (function) component `document [function]` (`17385d68-e8e9-5c02-94c9-eed3651bf547`) lines 514-519 [crates/gwiki/src/search/graph_boost.rs:514-519]
  - Signature: `fn document(path: &str, title: Option<&str>) -> GraphBoostDocument {`
  - Purpose: Constructs a 'GraphBoostDocument' by converting 'path' into a 'PathBuf' and mapping the optional 'title' to an owned 'String' when present. [crates/gwiki/src/search/graph_boost.rs:514-519]
- `link` (function) component `link [function]` (`276cff58-94f4-5748-bee9-4deb1a269a57`) lines 521-526 [crates/gwiki/src/search/graph_boost.rs:521-526]
  - Signature: `fn link(source_path: &str, target_path: &str) -> GraphBoostLink {`
  - Purpose: Constructs and returns a 'GraphBoostLink' by converting 'source_path' into a 'PathBuf' and cloning 'target_path' into an owned 'String'. [crates/gwiki/src/search/graph_boost.rs:521-526]

