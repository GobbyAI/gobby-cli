---
title: crates/gwiki/src/search/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/mod.rs
  ranges:
  - 14-18
  - 20-60
  - 21-23
  - 25-29
  - 31-35
  - 37-43
  - 45-51
  - 53-59
  - 63-67
  - 69-86
  - 70-76
  - 78-85
  - 89-92
  - 95-100
  - 103-108
  - 111-115
  - 118-131
  - 133-142
  - 134-141
  - 144-149
  - 152-157
  - 160-163
  - 166-169
  - 171-180
  - 172-179
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
  - 488-501
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/mod.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Purpose

`crates/gwiki/src/search/mod.rs` exposes 39 indexed API symbols.
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
  - Purpose: Indexed class `SearchScope` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:20-60]
- `SearchScope.global` (method) component `SearchScope.global [method]` (`b27ef063-c0ad-59d0-9e50-be86046d0b3c`) lines 21-23 [crates/gwiki/src/search/mod.rs:21-23]
  - Signature: `pub fn global() -> Self {`
  - Purpose: Indexed method `SearchScope.global` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:21-23]
- `SearchScope.project` (method) component `SearchScope.project [method]` (`70ae924d-f3f7-5971-bc71-3511345d8122`) lines 25-29 [crates/gwiki/src/search/mod.rs:25-29]
  - Signature: `pub fn project(project_id: impl Into<String>) -> Self {`
  - Purpose: Indexed method `SearchScope.project` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:25-29]
- `SearchScope.topic` (method) component `SearchScope.topic [method]` (`aff26efa-2cb6-58e9-8db8-5fc6cac04600`) lines 31-35 [crates/gwiki/src/search/mod.rs:31-35]
  - Signature: `pub fn topic(topic: impl Into<String>) -> Self {`
  - Purpose: Indexed method `SearchScope.topic` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:31-35]
- `SearchScope.scope_kind` (method) component `SearchScope.scope_kind [method]` (`3dd66973-b246-5962-a7c6-4d9fc30dfc93`) lines 37-43 [crates/gwiki/src/search/mod.rs:37-43]
  - Signature: `pub fn scope_kind(&self) -> &'static str {`
  - Purpose: Indexed method `SearchScope.scope_kind` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:37-43]
- `SearchScope.scope_value` (method) component `SearchScope.scope_value [method]` (`0418928a-81f8-5b89-99ee-bddb52956242`) lines 45-51 [crates/gwiki/src/search/mod.rs:45-51]
  - Signature: `pub fn scope_value(&self) -> &str {`
  - Purpose: Indexed method `SearchScope.scope_value` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:45-51]
- `SearchScope.scope_filter` (method) component `SearchScope.scope_filter [method]` (`86ab9027-1d50-54b8-96ac-549535fbb473`) lines 53-59 [crates/gwiki/src/search/mod.rs:53-59]
  - Signature: `pub fn scope_filter(&self) -> Option<(&'static str, &str)> {`
  - Purpose: Indexed method `SearchScope.scope_filter` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:53-59]
- `SearchSource` (type) component `SearchSource [type]` (`f9ed8292-0111-5c80-b179-fffd4ded63c1`) lines 63-67 [crates/gwiki/src/search/mod.rs:63-67]
  - Signature: `pub enum SearchSource {`
  - Purpose: Indexed type `SearchSource` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:63-67]
- `SearchSource` (class) component `SearchSource [class]` (`042ad156-1bed-56d8-a90a-125f88967f2f`) lines 69-86 [crates/gwiki/src/search/mod.rs:69-86]
  - Signature: `impl SearchSource {`
  - Purpose: Indexed class `SearchSource` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:69-86]
- `SearchSource.as_str` (method) component `SearchSource.as_str [method]` (`d747f79b-5dbe-5969-911a-6c3e5540a68c`) lines 70-76 [crates/gwiki/src/search/mod.rs:70-76]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Indexed method `SearchSource.as_str` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:70-76]
- `SearchSource.from_source_name` (method) component `SearchSource.from_source_name [method]` (`2739f536-c326-5de1-baf4-7ba55775033f`) lines 78-85 [crates/gwiki/src/search/mod.rs:78-85]
  - Signature: `pub(crate) fn from_source_name(source: &str) -> Option<Self> {`
  - Purpose: Indexed method `SearchSource.from_source_name` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:78-85]
- `SearchHitKind` (type) component `SearchHitKind [type]` (`7e10eaf5-b0bf-551e-b2ac-1659a4ba4909`) lines 89-92 [crates/gwiki/src/search/mod.rs:89-92]
  - Signature: `pub enum SearchHitKind {`
  - Purpose: Indexed type `SearchHitKind` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:89-92]
- `ChunkProvenance` (class) component `ChunkProvenance [class]` (`5118d0c5-3226-5954-aa30-fc988ef44685`) lines 95-100 [crates/gwiki/src/search/mod.rs:95-100]
  - Signature: `pub struct ChunkProvenance {`
  - Purpose: Indexed class `ChunkProvenance` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:95-100]
- `SearchProvenance` (class) component `SearchProvenance [class]` (`06d0a076-3d6f-59bb-a654-075e9d4d514f`) lines 103-108 [crates/gwiki/src/search/mod.rs:103-108]
  - Signature: `pub struct SearchProvenance {`
  - Purpose: Indexed class `SearchProvenance` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:103-108]
- `SearchSourceExplanation` (class) component `SearchSourceExplanation [class]` (`bf098cd0-f7b6-509b-ac2e-2334317dc22c`) lines 111-115 [crates/gwiki/src/search/mod.rs:111-115]
  - Signature: `pub struct SearchSourceExplanation {`
  - Purpose: Indexed class `SearchSourceExplanation` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:111-115]
- `WikiSearchResult` (class) component `WikiSearchResult [class]` (`93643579-4075-5161-991e-eac8c12cafaa`) lines 118-131 [crates/gwiki/src/search/mod.rs:118-131]
  - Signature: `pub struct WikiSearchResult {`
  - Purpose: Indexed class `WikiSearchResult` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:118-131]
- `WikiSearchResult` (class) component `WikiSearchResult [class]` (`b0f1d507-d6e7-5b43-ab3e-f609d749caeb`) lines 133-142 [crates/gwiki/src/search/mod.rs:133-142]
  - Signature: `impl WikiSearchResult {`
  - Purpose: Indexed class `WikiSearchResult` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:133-142]
- `WikiSearchResult.fusion_key` (method) component `WikiSearchResult.fusion_key [method]` (`47d3ba11-a1f0-5527-a3dd-c6d03288d75a`) lines 134-141 [crates/gwiki/src/search/mod.rs:134-141]
  - Signature: `pub fn fusion_key(&self) -> Result<String, SearchError> {`
  - Purpose: Indexed method `WikiSearchResult.fusion_key` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:134-141]
- `normalized_path` (function) component `normalized_path [function]` (`259af494-7635-5c39-9db3-429610dc6821`) lines 144-149 [crates/gwiki/src/search/mod.rs:144-149]
  - Signature: `fn normalized_path(path: &Path) -> Result<String, SearchError> {`
  - Purpose: Indexed function `normalized_path` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:144-149]
- `SearchRequest` (class) component `SearchRequest [class]` (`c45344b7-6b8c-5b2c-b52d-e7672c54efb7`) lines 152-157 [crates/gwiki/src/search/mod.rs:152-157]
  - Signature: `pub struct SearchRequest {`
  - Purpose: Indexed class `SearchRequest` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:152-157]
- `WikiSearchResponse` (class) component `WikiSearchResponse [class]` (`5a16aadf-dccd-5200-846f-e086df69e820`) lines 160-163 [crates/gwiki/src/search/mod.rs:160-163]
  - Signature: `pub struct WikiSearchResponse {`
  - Purpose: Indexed class `WikiSearchResponse` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:160-163]
- `SearchError` (type) component `SearchError [type]` (`9d7f2f31-2c39-50bb-993e-64c2e52b8308`) lines 166-169 [crates/gwiki/src/search/mod.rs:166-169]
  - Signature: `pub enum SearchError {`
  - Purpose: Indexed type `SearchError` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:166-169]
- `SearchError` (class) component `SearchError [class]` (`b9f7c22b-f760-59d4-a43e-9e3b691c278c`) lines 171-180 [crates/gwiki/src/search/mod.rs:171-180]
  - Signature: `impl fmt::Display for SearchError {`
  - Purpose: Indexed class `SearchError` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:171-180]
- `SearchError.fmt` (method) component `SearchError.fmt [method]` (`7db4ab35-8c10-5a6b-859c-bc41fbc56fad`) lines 172-179 [crates/gwiki/src/search/mod.rs:172-179]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Indexed method `SearchError.fmt` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:172-179]
- `SearchError` (class) component `SearchError [class]` (`0332c212-278e-58d3-90cd-f796264124bc`) lines 182-182 [crates/gwiki/src/search/mod.rs:182]
  - Signature: `impl std::error::Error for SearchError {}`
  - Purpose: Indexed class `SearchError` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:182]
- `search` (function) component `search [function]` (`b4816375-18b6-5a61-99a2-8fed1ec25de2`) lines 186-266 [crates/gwiki/src/search/mod.rs:186-266]
  - Signature: `pub fn search<B, S, G>(`
  - Purpose: Indexed function `search` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:186-266]
- `graph_seed_paths` (function) component `graph_seed_paths [function]` (`d1715451-a38b-5f95-83f2-4281d2859ce6`) lines 268-285 [crates/gwiki/src/search/mod.rs:268-285]
  - Signature: `fn graph_seed_paths(`
  - Purpose: Indexed function `graph_seed_paths` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:268-285]
- `available_sources` (function) component `available_sources [function]` (`16966054-19cc-57fb-befe-703147f828d7`) lines 287-300 [crates/gwiki/src/search/mod.rs:287-300]
  - Signature: `fn available_sources(`
  - Purpose: Indexed function `available_sources` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:287-300]
- `search_source_unavailable` (function) component `search_source_unavailable [function]` (`078b8f70-5599-55ea-b4a0-e9e925df08dd`) lines 302-304 [crates/gwiki/src/search/mod.rs:302-304]
  - Signature: `fn search_source_unavailable(degradation: &DegradationKind) -> bool {`
  - Purpose: Indexed function `search_source_unavailable` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:302-304]
- `semantic_unavailable_degrades` (function) component `semantic_unavailable_degrades [function]` (`6c04c67b-f714-5f35-b2d6-0c14b30fa25d`) lines 311-352 [crates/gwiki/src/search/mod.rs:311-352]
  - Signature: `fn semantic_unavailable_degrades() {`
  - Purpose: Indexed function `semantic_unavailable_degrades` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:311-352]
- `graph_linked_pages_enter_search_results` (function) component `graph_linked_pages_enter_search_results [function]` (`282251c4-626e-523d-81ef-94eb2b0819b7`) lines 355-386 [crates/gwiki/src/search/mod.rs:355-386]
  - Signature: `fn graph_linked_pages_enter_search_results() {`
  - Purpose: Indexed function `graph_linked_pages_enter_search_results` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:355-386]
- `combined_partial_search_reports_all_unavailable_sources_once` (function) component `combined_partial_search_reports_all_unavailable_sources_once [function]` (`419738fe-3b7e-5097-8f51-40685e008784`) lines 389-427 [crates/gwiki/src/search/mod.rs:389-427]
  - Signature: `fn combined_partial_search_reports_all_unavailable_sources_once() {`
  - Purpose: Indexed function `combined_partial_search_reports_all_unavailable_sources_once` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:389-427]
- `search_result` (function) component `search_result [function]` (`cf7401b8-eafb-5d98-b247-ebd9137391e8`) lines 429-454 [crates/gwiki/src/search/mod.rs:429-454]
  - Signature: `fn search_result(id: &str, scope: SearchScope, path: &str) -> WikiSearchResult {`
  - Purpose: Indexed function `search_result` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:429-454]
- `memory_graph` (function) component `memory_graph [function]` (`ad0392d9-ba55-585f-b864-5a7b751f2a7f`) lines 456-475 [crates/gwiki/src/search/mod.rs:456-475]
  - Signature: `fn memory_graph(scope: SearchScope) -> crate::graph::MemoryWikiGraph {`
  - Purpose: Indexed function `memory_graph` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:456-475]
- `graph_doc` (function) component `graph_doc [function]` (`c958ce76-8fa9-53fc-ac87-5ef843ccd51f`) lines 477-483 [crates/gwiki/src/search/mod.rs:477-483]
  - Signature: `fn graph_doc(scope: SearchScope, path: &str) -> crate::graph::WikiGraphDocument {`
  - Purpose: Indexed function `graph_doc` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:477-483]
- `DegradedGraphBackend` (class) component `DegradedGraphBackend [class]` (`3267fed8-3392-5a02-8ea2-e6101cdfd1d6`) lines 485-485 [crates/gwiki/src/search/mod.rs:485]
  - Signature: `struct DegradedGraphBackend;`
  - Purpose: Indexed class `DegradedGraphBackend` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:485]
- `DegradedGraphBackend` (class) component `DegradedGraphBackend [class]` (`45a99ef8-ce87-5531-89bb-597cd6cd5683`) lines 487-502 [crates/gwiki/src/search/mod.rs:487-502]
  - Signature: `impl graph_boost::GraphBoostBackend for DegradedGraphBackend {`
  - Purpose: Indexed class `DegradedGraphBackend` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:487-502]
- `DegradedGraphBackend.search_graph_boost` (method) component `DegradedGraphBackend.search_graph_boost [method]` (`33a97877-4fbb-5668-9f67-0e149bf1d9c5`) lines 488-501 [crates/gwiki/src/search/mod.rs:488-501]
  - Signature: `fn search_graph_boost(`
  - Purpose: Indexed method `DegradedGraphBackend.search_graph_boost` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:488-501]

