---
title: crates/gwiki/src/search/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/mod.rs
  ranges:
  - 14-18
  - 20-60
  - 63-67
  - 69-86
  - 89-92
  - 95-100
  - 103-108
  - 111-115
  - 118-131
  - 133-142
  - 144-149
  - 152-157
  - 160-163
  - 166-169
  - 171-180
  - '182'
  - 186-266
  - 268-285
  - 287-300
  - 302-304
  - 311-352
  - 355-386
  - 389-427
  - 429-454
  - 456-475
  - 477-483
  - '485'
  - 487-502
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/mod.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Purpose

This module defines the search domain model and shared utilities for wiki search, while re-exporting the BM25, graph-boost, RRF, and semantic submodules that implement the actual retrieval pipeline. It centers on `SearchScope` and `SearchSource` for describing where results come from and how they are filtered, `SearchHitKind` plus provenance structs for attaching chunk/document metadata to hits, and `WikiSearchResult`/`WikiSearchResponse` for packaging ranked results, explanations, and degradation details. It also provides `normalized_path` and `SearchError` so results can be keyed and reported consistently, and includes search helpers/tests that show the search flow combining BM25 with optional semantic and graph boosting, including graceful fallback when backends are unavailable.
[crates/gwiki/src/search/mod.rs:14-18]
[crates/gwiki/src/search/mod.rs:20-60]
[crates/gwiki/src/search/mod.rs:21-23]
[crates/gwiki/src/search/mod.rs:25-29]
[crates/gwiki/src/search/mod.rs:31-35]

## API Symbols

- `SearchScope` (type) component `SearchScope [type]` (`a63cb94e-d63c-58fd-af84-544dcd0bd720`) lines 14-18 [crates/gwiki/src/search/mod.rs:14-18]
  - Signature: `pub enum SearchScope {`
  - Purpose: Indexed type `SearchScope` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:14-18]
- `SearchScope` (class) component `SearchScope [class]` (`9c0a1c25-8b03-5683-b905-c46d1f99bc1a`) lines 20-60 [crates/gwiki/src/search/mod.rs:20-60]
  - Signature: `impl SearchScope {`
  - Purpose: 'SearchScope' is an enum-like scope discriminator that represents either 'Global', 'Project { project_id }', or 'Topic { topic }' and provides helpers to construct each variant plus expose its kind, raw string value, and optional '(field, value)' filter for searches. [crates/gwiki/src/search/mod.rs:20-60]
- `SearchScope.global` (method) component `SearchScope.global [method]` (`b27ef063-c0ad-59d0-9e50-be86046d0b3c`) lines 21-23 [crates/gwiki/src/search/mod.rs:21-23]
  - Signature: `pub fn global() -> Self {`
  - Purpose: Constructs and returns the 'Self::Global' variant of the type. [crates/gwiki/src/search/mod.rs:21-23]
- `SearchScope.project` (method) component `SearchScope.project [method]` (`70ae924d-f3f7-5971-bc71-3511345d8122`) lines 25-29 [crates/gwiki/src/search/mod.rs:25-29]
  - Signature: `pub fn project(project_id: impl Into<String>) -> Self {`
  - Purpose: Constructs and returns a 'Self::Project' variant, converting the provided 'project_id' into a 'String' and storing it in the 'project_id' field. [crates/gwiki/src/search/mod.rs:25-29]
- `SearchScope.topic` (method) component `SearchScope.topic [method]` (`aff26efa-2cb6-58e9-8db8-5fc6cac04600`) lines 31-35 [crates/gwiki/src/search/mod.rs:31-35]
  - Signature: `pub fn topic(topic: impl Into<String>) -> Self {`
  - Purpose: Constructs and returns 'Self::Topic' by converting the provided 'topic' argument into a 'String' and storing it in the variant. [crates/gwiki/src/search/mod.rs:31-35]
- `SearchScope.scope_kind` (method) component `SearchScope.scope_kind [method]` (`3dd66973-b246-5962-a7c6-4d9fc30dfc93`) lines 37-43 [crates/gwiki/src/search/mod.rs:37-43]
  - Signature: `pub fn scope_kind(&self) -> &'static str {`
  - Purpose: Returns the static string discriminator for the enum variant, mapping 'Global' to '"global"', 'Project' to '"project"', and 'Topic' to '"topic"'. [crates/gwiki/src/search/mod.rs:37-43]
- `SearchScope.scope_value` (method) component `SearchScope.scope_value [method]` (`0418928a-81f8-5b89-99ee-bddb52956242`) lines 45-51 [crates/gwiki/src/search/mod.rs:45-51]
  - Signature: `pub fn scope_value(&self) -> &str {`
  - Purpose: Returns the scope string for the enum variant, yielding '""' for 'Global' and borrowing 'project_id' or 'topic' for 'Project' and 'Topic', respectively. [crates/gwiki/src/search/mod.rs:45-51]
- `SearchScope.scope_filter` (method) component `SearchScope.scope_filter [method]` (`86ab9027-1d50-54b8-96ac-549535fbb473`) lines 53-59 [crates/gwiki/src/search/mod.rs:53-59]
  - Signature: `pub fn scope_filter(&self) -> Option<(&'static str, &str)> {`
  - Purpose: Returns 'None' for 'Global', and otherwise returns a scope filter tuple of '("project", project_id)' or '("topic", topic)' for the 'Project' and 'Topic' variants, respectively. [crates/gwiki/src/search/mod.rs:53-59]
- `SearchSource` (type) component `SearchSource [type]` (`f9ed8292-0111-5c80-b179-fffd4ded63c1`) lines 63-67 [crates/gwiki/src/search/mod.rs:63-67]
  - Signature: `pub enum SearchSource {`
  - Purpose: Indexed type `SearchSource` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:63-67]
- `SearchSource` (class) component `SearchSource [class]` (`042ad156-1bed-56d8-a90a-125f88967f2f`) lines 69-86 [crates/gwiki/src/search/mod.rs:69-86]
  - Signature: `impl SearchSource {`
  - Purpose: 'SearchSource' is an enum-backed source identifier that converts 'Bm25', 'Graph', and 'Semantic' variants to canonical string literals ('"bm25"', '"graph"', '"semantic"') and can fallibly parse those names back into a variant. [crates/gwiki/src/search/mod.rs:69-86]
- `SearchSource.as_str` (method) component `SearchSource.as_str [method]` (`d747f79b-5dbe-5969-911a-6c3e5540a68c`) lines 70-76 [crates/gwiki/src/search/mod.rs:70-76]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Returns the static string identifier for the enum variant, mapping 'Bm25' to '"bm25"', 'Graph' to '"graph"', and 'Semantic' to '"semantic"'. [crates/gwiki/src/search/mod.rs:70-76]
- `SearchSource.from_source_name` (method) component `SearchSource.from_source_name [method]` (`2739f536-c326-5de1-baf4-7ba55775033f`) lines 78-85 [crates/gwiki/src/search/mod.rs:78-85]
  - Signature: `pub(crate) fn from_source_name(source: &str) -> Option<Self> {`
  - Purpose: It converts the source name string '"bm25"', '"graph"', or '"semantic"' into the corresponding 'Self' enum variant, and returns 'None' for any unrecognized input. [crates/gwiki/src/search/mod.rs:78-85]
- `SearchHitKind` (type) component `SearchHitKind [type]` (`7e10eaf5-b0bf-551e-b2ac-1659a4ba4909`) lines 89-92 [crates/gwiki/src/search/mod.rs:89-92]
  - Signature: `pub enum SearchHitKind {`
  - Purpose: Indexed type `SearchHitKind` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:89-92]
- `ChunkProvenance` (class) component `ChunkProvenance [class]` (`5118d0c5-3226-5954-aa30-fc988ef44685`) lines 95-100 [crates/gwiki/src/search/mod.rs:95-100]
  - Signature: `pub struct ChunkProvenance {`
  - Purpose: 'ChunkProvenance' is a Rust data structure that records a chunk’s index, byte range ('byte_start' to 'byte_end'), and optional heading metadata for provenance tracking. [crates/gwiki/src/search/mod.rs:95-100]
- `SearchProvenance` (class) component `SearchProvenance [class]` (`06d0a076-3d6f-59bb-a654-075e9d4d514f`) lines 103-108 [crates/gwiki/src/search/mod.rs:103-108]
  - Signature: `pub struct SearchProvenance {`
  - Purpose: 'SearchProvenance' is a provenance metadata struct that ties a searched document to its originating source via 'document_path', 'source_path', 'source_kind', and an optional 'content_hash'. [crates/gwiki/src/search/mod.rs:103-108]
- `SearchSourceExplanation` (class) component `SearchSourceExplanation [class]` (`bf098cd0-f7b6-509b-ac2e-2334317dc22c`) lines 111-115 [crates/gwiki/src/search/mod.rs:111-115]
  - Signature: `pub struct SearchSourceExplanation {`
  - Purpose: 'SearchSourceExplanation' is a Rust struct that encapsulates a 'SearchSource' together with its 'rank' ('usize') and relevance 'score' ('f64'). [crates/gwiki/src/search/mod.rs:111-115]
- `WikiSearchResult` (class) component `WikiSearchResult [class]` (`93643579-4075-5161-991e-eac8c12cafaa`) lines 118-131 [crates/gwiki/src/search/mod.rs:118-131]
  - Signature: `pub struct WikiSearchResult {`
  - Purpose: 'WikiSearchResult' is a search-result struct that identifies a wiki hit and packages its title, search scope, paths, hit classification, snippet, relevance score, source/explanation lists, optional chunk provenance, and overall provenance metadata. [crates/gwiki/src/search/mod.rs:118-131]
- `WikiSearchResult` (class) component `WikiSearchResult [class]` (`b0f1d507-d6e7-5b43-ab3e-f609d749caeb`) lines 133-142 [crates/gwiki/src/search/mod.rs:133-142]
  - Signature: `impl WikiSearchResult {`
  - Purpose: 'WikiSearchResult' provides a 'fusion_key()' method that deterministically composes 'scope_kind:scope_value:normalized_path(path)' into a stable string key, returning 'SearchError' if path normalization fails. [crates/gwiki/src/search/mod.rs:133-142]
- `WikiSearchResult.fusion_key` (method) component `WikiSearchResult.fusion_key [method]` (`47d3ba11-a1f0-5527-a3dd-c6d03288d75a`) lines 134-141 [crates/gwiki/src/search/mod.rs:134-141]
  - Signature: `pub fn fusion_key(&self) -> Result<String, SearchError> {`
  - Purpose: 'fusion_key' constructs and returns a 'Result<String, SearchError>' containing a colon-delimited key of the form 'scope_kind:scope_value:normalized_path', propagating any error from 'normalized_path(&self.path)'. [crates/gwiki/src/search/mod.rs:134-141]
- `normalized_path` (function) component `normalized_path [function]` (`259af494-7635-5c39-9db3-429610dc6821`) lines 144-149 [crates/gwiki/src/search/mod.rs:144-149]
  - Signature: `fn normalized_path(path: &Path) -> Result<String, SearchError> {`
  - Purpose: Converts a 'Path' to a UTF-8 'String', returns 'SearchError::InvalidPath' if it is not valid UTF-8, and normalizes directory separators by replacing '\' with '/'. [crates/gwiki/src/search/mod.rs:144-149]
- `SearchRequest` (class) component `SearchRequest [class]` (`c45344b7-6b8c-5b2c-b52d-e7672c54efb7`) lines 152-157 [crates/gwiki/src/search/mod.rs:152-157]
  - Signature: `pub struct SearchRequest {`
  - Purpose: 'SearchRequest' is a search-API request struct containing the query string, the 'SearchScope' to search within, a result 'limit', and an 'include_semantic' flag to enable semantic matching. [crates/gwiki/src/search/mod.rs:152-157]
- `WikiSearchResponse` (class) component `WikiSearchResponse [class]` (`5a16aadf-dccd-5200-846f-e086df69e820`) lines 160-163 [crates/gwiki/src/search/mod.rs:160-163]
  - Signature: `pub struct WikiSearchResponse {`
  - Purpose: 'WikiSearchResponse' is a response struct that carries a vector of 'WikiSearchResult' items and a vector of 'DegradationKind' values describing any quality or capability degradations encountered during the search. [crates/gwiki/src/search/mod.rs:160-163]
- `SearchError` (type) component `SearchError [type]` (`9d7f2f31-2c39-50bb-993e-64c2e52b8308`) lines 166-169 [crates/gwiki/src/search/mod.rs:166-169]
  - Signature: `pub enum SearchError {`
  - Purpose: Indexed type `SearchError` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:166-169]
- `SearchError` (class) component `SearchError [class]` (`b9f7c22b-f760-59d4-a43e-9e3b691c278c`) lines 171-180 [crates/gwiki/src/search/mod.rs:171-180]
  - Signature: `impl fmt::Display for SearchError {`
  - Purpose: 'SearchError'’s 'Display' implementation renders 'Backend(message)' as 'wiki search backend failed: {message}' and 'InvalidPath { path }' as 'search result path is not valid UTF-8: {path:?}'. [crates/gwiki/src/search/mod.rs:171-180]
- `SearchError.fmt` (method) component `SearchError.fmt [method]` (`7db4ab35-8c10-5a6b-859c-bc41fbc56fad`) lines 172-179 [crates/gwiki/src/search/mod.rs:172-179]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Implements 'fmt::Display' for the error type by rendering 'Backend' as 'wiki search backend failed: {message}' and 'InvalidPath' as 'search result path is not valid UTF-8: {path:?}'. [crates/gwiki/src/search/mod.rs:172-179]
- `SearchError` (class) component `SearchError [class]` (`0332c212-278e-58d3-90cd-f796264124bc`) lines 182-182 [crates/gwiki/src/search/mod.rs:182]
  - Signature: `impl std::error::Error for SearchError {}`
  - Purpose: 'SearchError' is a Rust error type that implements 'std::error::Error', making it compatible with the standard error trait ecosystem without adding any custom behavior in this impl. [crates/gwiki/src/search/mod.rs:182]
- `search` (function) component `search [function]` (`b4816375-18b6-5a61-99a2-8fed1ec25de2`) lines 186-266 [crates/gwiki/src/search/mod.rs:186-266]
  - Signature: `pub fn search<B, S, G>(`
  - Purpose: I’m locating the function body in the repo so I can summarize the exact behavior rather than infer from the snippet alone.'gcode' can’t connect in this environment, so I’m falling back to a direct source search to recover the full function and keep the summary precise.I found the surrounding search pipeline, but the repo search is noisy and the snippet is truncated, so I’m anchoring the summary to the visible control flow: BM25, optional semantic search, graph boosting, and degradation aggregati [crates/gwiki/src/search/mod.rs:186-266]
- `graph_seed_paths` (function) component `graph_seed_paths [function]` (`d1715451-a38b-5f95-83f2-4281d2859ce6`) lines 268-285 [crates/gwiki/src/search/mod.rs:268-285]
  - Signature: `fn graph_seed_paths(`
  - Purpose: 'graph_seed_paths' iterates over BM25 hits followed by semantic hits, collects each hit’s 'provenance.document_path' into a deduplicated 'Vec<PathBuf>' in first-seen order, and stops once 'limit' paths have been accumulated. [crates/gwiki/src/search/mod.rs:268-285]
- `available_sources` (function) component `available_sources [function]` (`16966054-19cc-57fb-befe-703147f828d7`) lines 287-300 [crates/gwiki/src/search/mod.rs:287-300]
  - Signature: `fn available_sources(`
  - Purpose: Returns a 'Vec<String>' containing 'Bm25' unconditionally, 'Graph' when 'graph_unavailable' is false, and 'Semantic' when 'include_semantic' is true and 'semantic_unavailable' is false. [crates/gwiki/src/search/mod.rs:287-300]
- `search_source_unavailable` (function) component `search_source_unavailable [function]` (`078b8f70-5599-55ea-b4a0-e9e925df08dd`) lines 302-304 [crates/gwiki/src/search/mod.rs:302-304]
  - Signature: `fn search_source_unavailable(degradation: &DegradationKind) -> bool {`
  - Purpose: Returns 'true' if and only if 'degradation' is the 'DegradationKind::ServiceUnavailable' variant, and 'false' for all other variants. [crates/gwiki/src/search/mod.rs:302-304]
- `semantic_unavailable_degrades` (function) component `semantic_unavailable_degrades [function]` (`6c04c67b-f714-5f35-b2d6-0c14b30fa25d`) lines 311-352 [crates/gwiki/src/search/mod.rs:311-352]
  - Signature: `fn semantic_unavailable_degrades() {`
  - Purpose: Verifies that 'search' gracefully degrades to BM25-only results when the semantic backend is unavailable, while recording both a 'ServiceUnavailable' degradation for 'qdrant' and a 'PartialSearch' degradation indicating 'semantic' was unavailable. [crates/gwiki/src/search/mod.rs:311-352]
- `graph_linked_pages_enter_search_results` (function) component `graph_linked_pages_enter_search_results [function]` (`282251c4-626e-523d-81ef-94eb2b0819b7`) lines 355-386 [crates/gwiki/src/search/mod.rs:355-386]
  - Signature: `fn graph_linked_pages_enter_search_results() {`
  - Purpose: This test verifies that a project-scoped 'search' query for '"seed"' includes graph-neighborhood pages, specifically returning 'knowledge/topics/linked.md' with 'SearchSource::Graph' in its result sources. [crates/gwiki/src/search/mod.rs:355-386]
- `combined_partial_search_reports_all_unavailable_sources_once` (function) component `combined_partial_search_reports_all_unavailable_sources_once [function]` (`419738fe-3b7e-5097-8f51-40685e008784`) lines 389-427 [crates/gwiki/src/search/mod.rs:389-427]
  - Signature: `fn combined_partial_search_reports_all_unavailable_sources_once() {`
  - Purpose: Verifies that a combined search with BM25 available and semantic/graph backends unavailable returns a bm25-degraded result and records exactly one 'PartialSearch' degradation listing 'bm25' as available and 'semantic' plus 'graph' as unavailable. [crates/gwiki/src/search/mod.rs:389-427]
- `search_result` (function) component `search_result [function]` (`cf7401b8-eafb-5d98-b247-ebd9137391e8`) lines 429-454 [crates/gwiki/src/search/mod.rs:429-454]
  - Signature: `fn search_result(id: &str, scope: SearchScope, path: &str) -> WikiSearchResult {`
  - Purpose: Constructs a 'WikiSearchResult' for the given 'id', 'scope', and 'path', copying those inputs into the result and populating all other fields with fixed chunk-search metadata, snippet, score, source attribution, chunk provenance, and document provenance. [crates/gwiki/src/search/mod.rs:429-454]
- `memory_graph` (function) component `memory_graph [function]` (`ad0392d9-ba55-585f-b864-5a7b751f2a7f`) lines 456-475 [crates/gwiki/src/search/mod.rs:456-475]
  - Signature: `fn memory_graph(scope: SearchScope) -> crate::graph::MemoryWikiGraph {`
  - Purpose: Constructs and returns a default 'MemoryWikiGraph' whose facts contain two documents ('knowledge/topics/seed.md' and 'knowledge/topics/linked.md'), one resolved link from the seed document to the linked document, and empty 'sources' and 'code_edges' collections. [crates/gwiki/src/search/mod.rs:456-475]
- `graph_doc` (function) component `graph_doc [function]` (`c958ce76-8fa9-53fc-ac87-5ef843ccd51f`) lines 477-483 [crates/gwiki/src/search/mod.rs:477-483]
  - Signature: `fn graph_doc(scope: SearchScope, path: &str) -> crate::graph::WikiGraphDocument {`
  - Purpose: Constructs and returns a 'crate::graph::WikiGraphDocument' with the given 'scope', 'path' converted into a 'PathBuf', and 'title' set to 'None'. [crates/gwiki/src/search/mod.rs:477-483]
- `DegradedGraphBackend` (class) component `DegradedGraphBackend [class]` (`3267fed8-3392-5a02-8ea2-e6101cdfd1d6`) lines 485-485 [crates/gwiki/src/search/mod.rs:485]
  - Signature: `struct DegradedGraphBackend;`
  - Purpose: 'DegradedGraphBackend' is a graph-backend implementation that provides limited, fallback behavior when the normal backend is unavailable or operating in a degraded state. [crates/gwiki/src/search/mod.rs:485]
- `DegradedGraphBackend` (class) component `DegradedGraphBackend [class]` (`45a99ef8-ce87-5531-89bb-597cd6cd5683`) lines 487-502 [crates/gwiki/src/search/mod.rs:487-502]
  - Signature: `impl graph_boost::GraphBoostBackend for DegradedGraphBackend {`
  - Purpose: 'DegradedGraphBackend' is a fallback 'graph_boost::GraphBoostBackend' implementation that ignores the request and always returns an empty 'GraphBoostOutcome' with a 'ServiceUnavailable' degradation marking 'gwiki_graph' as unreachable ('offline'). [crates/gwiki/src/search/mod.rs:487-502]
- `DegradedGraphBackend.search_graph_boost` (method) component `DegradedGraphBackend.search_graph_boost [method]` (`33a97877-4fbb-5668-9f67-0e149bf1d9c5`) lines 488-501 [crates/gwiki/src/search/mod.rs:488-501]
  - Signature: `fn search_graph_boost(`
  - Purpose: It ignores the request and returns 'Ok(GraphBoostOutcome)' with no hits and a 'ServiceUnavailable' degradation indicating 'gwiki_graph' is unreachable ('offline'). [crates/gwiki/src/search/mod.rs:488-501]

