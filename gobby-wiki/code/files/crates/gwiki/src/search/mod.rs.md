---
title: crates/gwiki/src/search/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/mod.rs
  ranges:
  - 14-18
  - 21-23
  - 25-29
  - 31-35
  - 37-43
  - 45-51
  - 53-59
  - 63-67
  - 70-76
  - 78-85
  - 89-92
  - 95-100
  - 103-108
  - 111-115
  - 118-131
  - 134-141
  - 144-149
  - 152-157
  - 160-163
  - 166-169
  - 172-179
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
  - 488-501
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/search/mod.rs:14-18](crates/gwiki/src/search/mod.rs#L14-L18), [crates/gwiki/src/search/mod.rs:21-23](crates/gwiki/src/search/mod.rs#L21-L23), [crates/gwiki/src/search/mod.rs:25-29](crates/gwiki/src/search/mod.rs#L25-L29), [crates/gwiki/src/search/mod.rs:31-35](crates/gwiki/src/search/mod.rs#L31-L35), [crates/gwiki/src/search/mod.rs:37-43](crates/gwiki/src/search/mod.rs#L37-L43), [crates/gwiki/src/search/mod.rs:45-51](crates/gwiki/src/search/mod.rs#L45-L51), [crates/gwiki/src/search/mod.rs:53-59](crates/gwiki/src/search/mod.rs#L53-L59), [crates/gwiki/src/search/mod.rs:63-67](crates/gwiki/src/search/mod.rs#L63-L67), [crates/gwiki/src/search/mod.rs:70-76](crates/gwiki/src/search/mod.rs#L70-L76), [crates/gwiki/src/search/mod.rs:78-85](crates/gwiki/src/search/mod.rs#L78-L85), [crates/gwiki/src/search/mod.rs:89-92](crates/gwiki/src/search/mod.rs#L89-L92), [crates/gwiki/src/search/mod.rs:95-100](crates/gwiki/src/search/mod.rs#L95-L100), [crates/gwiki/src/search/mod.rs:103-108](crates/gwiki/src/search/mod.rs#L103-L108), [crates/gwiki/src/search/mod.rs:111-115](crates/gwiki/src/search/mod.rs#L111-L115), [crates/gwiki/src/search/mod.rs:118-131](crates/gwiki/src/search/mod.rs#L118-L131), [crates/gwiki/src/search/mod.rs:134-141](crates/gwiki/src/search/mod.rs#L134-L141), [crates/gwiki/src/search/mod.rs:144-149](crates/gwiki/src/search/mod.rs#L144-L149), [crates/gwiki/src/search/mod.rs:152-157](crates/gwiki/src/search/mod.rs#L152-L157), [crates/gwiki/src/search/mod.rs:160-163](crates/gwiki/src/search/mod.rs#L160-L163), [crates/gwiki/src/search/mod.rs:166-169](crates/gwiki/src/search/mod.rs#L166-L169), [crates/gwiki/src/search/mod.rs:172-179](crates/gwiki/src/search/mod.rs#L172-L179), [crates/gwiki/src/search/mod.rs:186-266](crates/gwiki/src/search/mod.rs#L186-L266), [crates/gwiki/src/search/mod.rs:268-285](crates/gwiki/src/search/mod.rs#L268-L285), [crates/gwiki/src/search/mod.rs:287-300](crates/gwiki/src/search/mod.rs#L287-L300), [crates/gwiki/src/search/mod.rs:302-304](crates/gwiki/src/search/mod.rs#L302-L304), [crates/gwiki/src/search/mod.rs:311-352](crates/gwiki/src/search/mod.rs#L311-L352), [crates/gwiki/src/search/mod.rs:355-386](crates/gwiki/src/search/mod.rs#L355-L386), [crates/gwiki/src/search/mod.rs:389-427](crates/gwiki/src/search/mod.rs#L389-L427), [crates/gwiki/src/search/mod.rs:429-454](crates/gwiki/src/search/mod.rs#L429-L454), [crates/gwiki/src/search/mod.rs:456-475](crates/gwiki/src/search/mod.rs#L456-L475), [crates/gwiki/src/search/mod.rs:477-483](crates/gwiki/src/search/mod.rs#L477-L483), [crates/gwiki/src/search/mod.rs:485](crates/gwiki/src/search/mod.rs#L485), [crates/gwiki/src/search/mod.rs:488-501](crates/gwiki/src/search/mod.rs#L488-L501)

</details>

# crates/gwiki/src/search/mod.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Purpose

Defines the search subsystem for `gwiki`, wiring together BM25, graph, RRF, and semantic search modules and the shared types they use to coordinate results. It models search scope and source selection, records hit/provenance metadata, and provides request/response and error types for the main `search` flow. The helper functions assemble search outputs, normalize paths, derive graph seed paths and available sources, and handle degraded or unavailable backends so combined searches can report partial results consistently.
[crates/gwiki/src/search/mod.rs:14-18]
[crates/gwiki/src/search/mod.rs:21-23]
[crates/gwiki/src/search/mod.rs:25-29]
[crates/gwiki/src/search/mod.rs:31-35]
[crates/gwiki/src/search/mod.rs:37-43]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SearchScope` | type | `pub enum SearchScope {` | `SearchScope [type]` | `a63cb94e-d63c-58fd-af84-544dcd0bd720` | 14-18 [crates/gwiki/src/search/mod.rs:14-18] | Indexed type `SearchScope` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:14-18] |
| `SearchScope::global` | method | `pub fn global() -> Self {` | `SearchScope::global [method]` | `b27ef063-c0ad-59d0-9e50-be86046d0b3c` | 21-23 [crates/gwiki/src/search/mod.rs:21-23] | Indexed method `SearchScope::global` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:21-23] |
| `SearchScope::project` | method | `pub fn project(project_id: impl Into<String>) -> Self {` | `SearchScope::project [method]` | `70ae924d-f3f7-5971-bc71-3511345d8122` | 25-29 [crates/gwiki/src/search/mod.rs:25-29] | Indexed method `SearchScope::project` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:25-29] |
| `SearchScope::topic` | method | `pub fn topic(topic: impl Into<String>) -> Self {` | `SearchScope::topic [method]` | `aff26efa-2cb6-58e9-8db8-5fc6cac04600` | 31-35 [crates/gwiki/src/search/mod.rs:31-35] | Indexed method `SearchScope::topic` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:31-35] |
| `SearchScope::scope_kind` | method | `pub fn scope_kind(&self) -> &'static str {` | `SearchScope::scope_kind [method]` | `3dd66973-b246-5962-a7c6-4d9fc30dfc93` | 37-43 [crates/gwiki/src/search/mod.rs:37-43] | Indexed method `SearchScope::scope_kind` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:37-43] |
| `SearchScope::scope_value` | method | `pub fn scope_value(&self) -> &str {` | `SearchScope::scope_value [method]` | `0418928a-81f8-5b89-99ee-bddb52956242` | 45-51 [crates/gwiki/src/search/mod.rs:45-51] | Indexed method `SearchScope::scope_value` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:45-51] |
| `SearchScope::scope_filter` | method | `pub fn scope_filter(&self) -> Option<(&'static str, &str)> {` | `SearchScope::scope_filter [method]` | `86ab9027-1d50-54b8-96ac-549535fbb473` | 53-59 [crates/gwiki/src/search/mod.rs:53-59] | Indexed method `SearchScope::scope_filter` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:53-59] |
| `SearchSource` | type | `pub enum SearchSource {` | `SearchSource [type]` | `f9ed8292-0111-5c80-b179-fffd4ded63c1` | 63-67 [crates/gwiki/src/search/mod.rs:63-67] | Indexed type `SearchSource` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:63-67] |
| `SearchSource::as_str` | method | `pub fn as_str(self) -> &'static str {` | `SearchSource::as_str [method]` | `d747f79b-5dbe-5969-911a-6c3e5540a68c` | 70-76 [crates/gwiki/src/search/mod.rs:70-76] | Indexed method `SearchSource::as_str` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:70-76] |
| `SearchSource::from_source_name` | method | `pub(crate) fn from_source_name(source: &str) -> Option<Self> {` | `SearchSource::from_source_name [method]` | `2739f536-c326-5de1-baf4-7ba55775033f` | 78-85 [crates/gwiki/src/search/mod.rs:78-85] | Indexed method `SearchSource::from_source_name` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:78-85] |
| `SearchHitKind` | type | `pub enum SearchHitKind {` | `SearchHitKind [type]` | `7e10eaf5-b0bf-551e-b2ac-1659a4ba4909` | 89-92 [crates/gwiki/src/search/mod.rs:89-92] | Indexed type `SearchHitKind` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:89-92] |
| `ChunkProvenance` | class | `pub struct ChunkProvenance {` | `ChunkProvenance [class]` | `5118d0c5-3226-5954-aa30-fc988ef44685` | 95-100 [crates/gwiki/src/search/mod.rs:95-100] | Indexed class `ChunkProvenance` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:95-100] |
| `SearchProvenance` | class | `pub struct SearchProvenance {` | `SearchProvenance [class]` | `06d0a076-3d6f-59bb-a654-075e9d4d514f` | 103-108 [crates/gwiki/src/search/mod.rs:103-108] | Indexed class `SearchProvenance` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:103-108] |
| `SearchSourceExplanation` | class | `pub struct SearchSourceExplanation {` | `SearchSourceExplanation [class]` | `bf098cd0-f7b6-509b-ac2e-2334317dc22c` | 111-115 [crates/gwiki/src/search/mod.rs:111-115] | Indexed class `SearchSourceExplanation` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:111-115] |
| `WikiSearchResult` | class | `pub struct WikiSearchResult {` | `WikiSearchResult [class]` | `93643579-4075-5161-991e-eac8c12cafaa` | 118-131 [crates/gwiki/src/search/mod.rs:118-131] | Indexed class `WikiSearchResult` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:118-131] |
| `WikiSearchResult::fusion_key` | method | `pub fn fusion_key(&self) -> Result<String, SearchError> {` | `WikiSearchResult::fusion_key [method]` | `47d3ba11-a1f0-5527-a3dd-c6d03288d75a` | 134-141 [crates/gwiki/src/search/mod.rs:134-141] | Indexed method `WikiSearchResult::fusion_key` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:134-141] |
| `normalized_path` | function | `fn normalized_path(path: &Path) -> Result<String, SearchError> {` | `normalized_path [function]` | `259af494-7635-5c39-9db3-429610dc6821` | 144-149 [crates/gwiki/src/search/mod.rs:144-149] | Indexed function `normalized_path` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:144-149] |
| `SearchRequest` | class | `pub struct SearchRequest {` | `SearchRequest [class]` | `c45344b7-6b8c-5b2c-b52d-e7672c54efb7` | 152-157 [crates/gwiki/src/search/mod.rs:152-157] | Indexed class `SearchRequest` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:152-157] |
| `WikiSearchResponse` | class | `pub struct WikiSearchResponse {` | `WikiSearchResponse [class]` | `5a16aadf-dccd-5200-846f-e086df69e820` | 160-163 [crates/gwiki/src/search/mod.rs:160-163] | Indexed class `WikiSearchResponse` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:160-163] |
| `SearchError` | type | `pub enum SearchError {` | `SearchError [type]` | `9d7f2f31-2c39-50bb-993e-64c2e52b8308` | 166-169 [crates/gwiki/src/search/mod.rs:166-169] | Indexed type `SearchError` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:166-169] |
| `SearchError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `SearchError::fmt [method]` | `7db4ab35-8c10-5a6b-859c-bc41fbc56fad` | 172-179 [crates/gwiki/src/search/mod.rs:172-179] | Indexed method `SearchError::fmt` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:172-179] |
| `search` | function | `pub fn search<B, S, G>(` | `search [function]` | `b4816375-18b6-5a61-99a2-8fed1ec25de2` | 186-266 [crates/gwiki/src/search/mod.rs:186-266] | Indexed function `search` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:186-266] |
| `graph_seed_paths` | function | `fn graph_seed_paths(` | `graph_seed_paths [function]` | `d1715451-a38b-5f95-83f2-4281d2859ce6` | 268-285 [crates/gwiki/src/search/mod.rs:268-285] | Indexed function `graph_seed_paths` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:268-285] |
| `available_sources` | function | `fn available_sources(` | `available_sources [function]` | `16966054-19cc-57fb-befe-703147f828d7` | 287-300 [crates/gwiki/src/search/mod.rs:287-300] | Indexed function `available_sources` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:287-300] |
| `search_source_unavailable` | function | `fn search_source_unavailable(degradation: &DegradationKind) -> bool {` | `search_source_unavailable [function]` | `078b8f70-5599-55ea-b4a0-e9e925df08dd` | 302-304 [crates/gwiki/src/search/mod.rs:302-304] | Indexed function `search_source_unavailable` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:302-304] |
| `semantic_unavailable_degrades` | function | `fn semantic_unavailable_degrades() {` | `semantic_unavailable_degrades [function]` | `6c04c67b-f714-5f35-b2d6-0c14b30fa25d` | 311-352 [crates/gwiki/src/search/mod.rs:311-352] | Indexed function `semantic_unavailable_degrades` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:311-352] |
| `graph_linked_pages_enter_search_results` | function | `fn graph_linked_pages_enter_search_results() {` | `graph_linked_pages_enter_search_results [function]` | `282251c4-626e-523d-81ef-94eb2b0819b7` | 355-386 [crates/gwiki/src/search/mod.rs:355-386] | Indexed function `graph_linked_pages_enter_search_results` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:355-386] |
| `combined_partial_search_reports_all_unavailable_sources_once` | function | `fn combined_partial_search_reports_all_unavailable_sources_once() {` | `combined_partial_search_reports_all_unavailable_sources_once [function]` | `419738fe-3b7e-5097-8f51-40685e008784` | 389-427 [crates/gwiki/src/search/mod.rs:389-427] | Indexed function `combined_partial_search_reports_all_unavailable_sources_once` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:389-427] |
| `search_result` | function | `fn search_result(id: &str, scope: SearchScope, path: &str) -> WikiSearchResult {` | `search_result [function]` | `cf7401b8-eafb-5d98-b247-ebd9137391e8` | 429-454 [crates/gwiki/src/search/mod.rs:429-454] | Indexed function `search_result` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:429-454] |
| `memory_graph` | function | `fn memory_graph(scope: SearchScope) -> crate::graph::MemoryWikiGraph {` | `memory_graph [function]` | `ad0392d9-ba55-585f-b864-5a7b751f2a7f` | 456-475 [crates/gwiki/src/search/mod.rs:456-475] | Indexed function `memory_graph` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:456-475] |
| `graph_doc` | function | `fn graph_doc(scope: SearchScope, path: &str) -> crate::graph::WikiGraphDocument {` | `graph_doc [function]` | `c958ce76-8fa9-53fc-ac87-5ef843ccd51f` | 477-483 [crates/gwiki/src/search/mod.rs:477-483] | Indexed function `graph_doc` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:477-483] |
| `DegradedGraphBackend` | class | `struct DegradedGraphBackend;` | `DegradedGraphBackend [class]` | `3267fed8-3392-5a02-8ea2-e6101cdfd1d6` | 485-485 [crates/gwiki/src/search/mod.rs:485] | Indexed class `DegradedGraphBackend` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:485] |
| `DegradedGraphBackend::search_graph_boost` | method | `fn search_graph_boost(` | `DegradedGraphBackend::search_graph_boost [method]` | `33a97877-4fbb-5668-9f67-0e149bf1d9c5` | 488-501 [crates/gwiki/src/search/mod.rs:488-501] | Indexed method `DegradedGraphBackend::search_graph_boost` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:488-501] |
