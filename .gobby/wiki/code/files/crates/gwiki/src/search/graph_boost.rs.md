---
title: crates/gwiki/src/search/graph_boost.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/graph_boost.rs
  ranges:
  - 21-24
  - 26-33
  - 27-32
  - 35-39
  - 41-44
  - 46-51
  - '53'
  - 55-65
  - 56-64
  - 67-69
  - 71-77
  - 72-76
  - 79-89
  - 80-88
  - 92-97
  - 100-102
  - 104-108
  - 105-107
  - 110-123
  - 111-122
  - 125-128
  - 130-145
  - 131-133
  - 135-144
  - 147-184
  - 148-183
  - 187-190
  - 193-196
  - 198-263
  - 265-276
  - 278-300
  - 302-307
  - 309-346
  - 348-361
  - 363-383
  - 385-391
  - 398-426
  - 429-451
  - 454-472
  - 475-488
  - 491-511
  - 513-518
  - 520-525
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/graph_boost.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Purpose

`crates/gwiki/src/search/graph_boost.rs` exposes 43 indexed API symbols.
[crates/gwiki/src/search/graph_boost.rs:21-24]
[crates/gwiki/src/search/graph_boost.rs:26-33]
[crates/gwiki/src/search/graph_boost.rs:27-32]
[crates/gwiki/src/search/graph_boost.rs:35-39]
[crates/gwiki/src/search/graph_boost.rs:41-44]

## API Symbols

- `GraphBoostConfig` (class) component `GraphBoostConfig [class]` (`c6a6d24a-b8ee-52d3-9c20-562e234ab20e`) lines 21-24 [crates/gwiki/src/search/graph_boost.rs:21-24]
  - Signature: `pub struct GraphBoostConfig {`
  - Purpose: Indexed class `GraphBoostConfig` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:21-24]
- `GraphBoostConfig` (class) component `GraphBoostConfig [class]` (`111dfcc3-3f75-57aa-87b0-b9dc128ebbcb`) lines 26-33 [crates/gwiki/src/search/graph_boost.rs:26-33]
  - Signature: `impl Default for GraphBoostConfig {`
  - Purpose: Indexed class `GraphBoostConfig` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:26-33]
- `GraphBoostConfig.default` (method) component `GraphBoostConfig.default [method]` (`78eceb97-9cc6-5e56-b572-150250b3dbd6`) lines 27-32 [crates/gwiki/src/search/graph_boost.rs:27-32]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `GraphBoostConfig.default` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:27-32]
- `GraphBoostRequest` (class) component `GraphBoostRequest [class]` (`8f5be825-7c2b-53eb-b02a-82f0654d2051`) lines 35-39 [crates/gwiki/src/search/graph_boost.rs:35-39]
  - Signature: `pub struct GraphBoostRequest {`
  - Purpose: Indexed class `GraphBoostRequest` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:35-39]
- `GraphBoostOutcome` (class) component `GraphBoostOutcome [class]` (`3a59b0b5-bc0e-5cd9-9b25-309e57f45d4b`) lines 41-44 [crates/gwiki/src/search/graph_boost.rs:41-44]
  - Signature: `pub struct GraphBoostOutcome {`
  - Purpose: Indexed class `GraphBoostOutcome` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:41-44]
- `GraphBoostBackend` (type) component `GraphBoostBackend [type]` (`79b9f5cf-8ade-5662-b3ca-60dc0207e563`) lines 46-51 [crates/gwiki/src/search/graph_boost.rs:46-51]
  - Signature: `pub trait GraphBoostBackend {`
  - Purpose: Indexed type `GraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:46-51]
- `NoopGraphBoostBackend` (class) component `NoopGraphBoostBackend [class]` (`e66a2440-b384-554a-a3e9-5d0384f9e039`) lines 53-53 [crates/gwiki/src/search/graph_boost.rs:53]
  - Signature: `pub struct NoopGraphBoostBackend;`
  - Purpose: Indexed class `NoopGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:53]
- `NoopGraphBoostBackend` (class) component `NoopGraphBoostBackend [class]` (`44067d65-c431-55f4-834f-bd49bb29ed4b`) lines 55-65 [crates/gwiki/src/search/graph_boost.rs:55-65]
  - Signature: `impl GraphBoostBackend for NoopGraphBoostBackend {`
  - Purpose: Indexed class `NoopGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:55-65]
- `NoopGraphBoostBackend.search_graph_boost` (method) component `NoopGraphBoostBackend.search_graph_boost [method]` (`32b6a519-80ca-5300-8ffa-7b57b7ee0d81`) lines 56-64 [crates/gwiki/src/search/graph_boost.rs:56-64]
  - Signature: `fn search_graph_boost(`
  - Purpose: Indexed method `NoopGraphBoostBackend.search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:56-64]
- `UnavailableGraphBoostBackend` (class) component `UnavailableGraphBoostBackend [class]` (`226b1b7c-2fe3-5863-bd9b-8ab9aee735e8`) lines 67-69 [crates/gwiki/src/search/graph_boost.rs:67-69]
  - Signature: `pub struct UnavailableGraphBoostBackend {`
  - Purpose: Indexed class `UnavailableGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:67-69]
- `UnavailableGraphBoostBackend` (class) component `UnavailableGraphBoostBackend [class]` (`330f31f8-165b-5eb1-817d-3ab643bca26d`) lines 71-77 [crates/gwiki/src/search/graph_boost.rs:71-77]
  - Signature: `impl UnavailableGraphBoostBackend {`
  - Purpose: Indexed class `UnavailableGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:71-77]
- `UnavailableGraphBoostBackend.unreachable` (method) component `UnavailableGraphBoostBackend.unreachable [method]` (`dec7de72-0db3-5547-89bf-ef0046732d37`) lines 72-76 [crates/gwiki/src/search/graph_boost.rs:72-76]
  - Signature: `pub fn unreachable(message: String) -> Self {`
  - Purpose: Indexed method `UnavailableGraphBoostBackend.unreachable` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:72-76]
- `UnavailableGraphBoostBackend` (class) component `UnavailableGraphBoostBackend [class]` (`6cb7473e-7c6c-594e-8cb8-0d4c9be0351a`) lines 79-89 [crates/gwiki/src/search/graph_boost.rs:79-89]
  - Signature: `impl GraphBoostBackend for UnavailableGraphBoostBackend {`
  - Purpose: Indexed class `UnavailableGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:79-89]
- `UnavailableGraphBoostBackend.search_graph_boost` (method) component `UnavailableGraphBoostBackend.search_graph_boost [method]` (`006e9539-6463-5936-81a4-052222237a3a`) lines 80-88 [crates/gwiki/src/search/graph_boost.rs:80-88]
  - Signature: `fn search_graph_boost(`
  - Purpose: Indexed method `UnavailableGraphBoostBackend.search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:80-88]
- `search_graph_boost` (function) component `search_graph_boost [function]` (`6685cc89-2c3c-5645-9ea9-21b64dde8a72`) lines 92-97 [crates/gwiki/src/search/graph_boost.rs:92-97]
  - Signature: `fn search_graph_boost(`
  - Purpose: Indexed function `search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:92-97]
- `MemoryGraphBoostBackend` (class) component `MemoryGraphBoostBackend [class]` (`c30cbebe-2767-59da-bc02-51f5f21f27b1`) lines 100-102 [crates/gwiki/src/search/graph_boost.rs:100-102]
  - Signature: `pub struct MemoryGraphBoostBackend {`
  - Purpose: Indexed class `MemoryGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:100-102]
- `MemoryGraphBoostBackend` (class) component `MemoryGraphBoostBackend [class]` (`7e4f282c-89f1-5843-827a-318ce46923d2`) lines 104-108 [crates/gwiki/src/search/graph_boost.rs:104-108]
  - Signature: `impl MemoryGraphBoostBackend {`
  - Purpose: Indexed class `MemoryGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:104-108]
- `MemoryGraphBoostBackend.new` (method) component `MemoryGraphBoostBackend.new [method]` (`5bb7cd22-8580-50ef-9f8d-d229fdb65034`) lines 105-107 [crates/gwiki/src/search/graph_boost.rs:105-107]
  - Signature: `pub fn new(graph: MemoryWikiGraph) -> Self {`
  - Purpose: Indexed method `MemoryGraphBoostBackend.new` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:105-107]
- `MemoryGraphBoostBackend` (class) component `MemoryGraphBoostBackend [class]` (`aa90d159-1da5-5b91-be74-96a480a785cc`) lines 110-123 [crates/gwiki/src/search/graph_boost.rs:110-123]
  - Signature: `impl GraphBoostBackend for MemoryGraphBoostBackend {`
  - Purpose: Indexed class `MemoryGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:110-123]
- `MemoryGraphBoostBackend.search_graph_boost` (method) component `MemoryGraphBoostBackend.search_graph_boost [method]` (`bbca9a54-385f-5ed5-b262-a1728d6e1f5a`) lines 111-122 [crates/gwiki/src/search/graph_boost.rs:111-122]
  - Signature: `fn search_graph_boost(`
  - Purpose: Indexed method `MemoryGraphBoostBackend.search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:111-122]
- `FalkorGraphBoostBackend` (class) component `FalkorGraphBoostBackend [class]` (`26713af0-5f85-5d8e-bf4b-168cad1d36f0`) lines 125-128 [crates/gwiki/src/search/graph_boost.rs:125-128]
  - Signature: `pub struct FalkorGraphBoostBackend {`
  - Purpose: Indexed class `FalkorGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:125-128]
- `FalkorGraphBoostBackend` (class) component `FalkorGraphBoostBackend [class]` (`4bd06c19-1dba-548c-bd16-d39a628681d7`) lines 130-145 [crates/gwiki/src/search/graph_boost.rs:130-145]
  - Signature: `impl FalkorGraphBoostBackend {`
  - Purpose: Indexed class `FalkorGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:130-145]
- `FalkorGraphBoostBackend.new` (method) component `FalkorGraphBoostBackend.new [method]` (`3074e6a4-a582-5333-bf1d-5ddb443df364`) lines 131-133 [crates/gwiki/src/search/graph_boost.rs:131-133]
  - Signature: `pub fn new(config: &FalkorConfig) -> Result<Self, SearchError> {`
  - Purpose: Indexed method `FalkorGraphBoostBackend.new` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:131-133]
- `FalkorGraphBoostBackend.new_with_config` (method) component `FalkorGraphBoostBackend.new_with_config [method]` (`c94f4149-23c3-5480-b613-ab216a5881c0`) lines 135-144 [crates/gwiki/src/search/graph_boost.rs:135-144]
  - Signature: `pub fn new_with_config(`
  - Purpose: Indexed method `FalkorGraphBoostBackend.new_with_config` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:135-144]
- `FalkorGraphBoostBackend` (class) component `FalkorGraphBoostBackend [class]` (`f6dda4c4-ba57-5cf4-aa15-27ef500996b9`) lines 147-184 [crates/gwiki/src/search/graph_boost.rs:147-184]
  - Signature: `impl GraphBoostBackend for FalkorGraphBoostBackend {`
  - Purpose: Indexed class `FalkorGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:147-184]
- `FalkorGraphBoostBackend.search_graph_boost` (method) component `FalkorGraphBoostBackend.search_graph_boost [method]` (`cfe875d6-69be-5cc0-bbe5-f93566f20c85`) lines 148-183 [crates/gwiki/src/search/graph_boost.rs:148-183]
  - Signature: `fn search_graph_boost(`
  - Purpose: Indexed method `FalkorGraphBoostBackend.search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:148-183]
- `GraphBoostDocument` (class) component `GraphBoostDocument [class]` (`2e3e4a4c-9ece-5a0a-ad49-8a300112da87`) lines 187-190 [crates/gwiki/src/search/graph_boost.rs:187-190]
  - Signature: `pub struct GraphBoostDocument {`
  - Purpose: Indexed class `GraphBoostDocument` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:187-190]
- `GraphBoostLink` (class) component `GraphBoostLink [class]` (`54b6cb11-c78c-5de5-9c2e-3ae920c1bd42`) lines 193-196 [crates/gwiki/src/search/graph_boost.rs:193-196]
  - Signature: `pub struct GraphBoostLink {`
  - Purpose: Indexed class `GraphBoostLink` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:193-196]
- `rank_link_neighborhood` (function) component `rank_link_neighborhood [function]` (`b74b6fbe-cf70-5109-a481-8fbd0fd6348a`) lines 198-263 [crates/gwiki/src/search/graph_boost.rs:198-263]
  - Signature: `pub fn rank_link_neighborhood(`
  - Purpose: Indexed function `rank_link_neighborhood` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:198-263]
- `graph_boost_hits` (function) component `graph_boost_hits [function]` (`07327f8f-1ee3-5f82-b528-c0825ff9eda9`) lines 265-276 [crates/gwiki/src/search/graph_boost.rs:265-276]
  - Signature: `pub fn graph_boost_hits(`
  - Purpose: Indexed function `graph_boost_hits` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:265-276]
- `graph_result` (function) component `graph_result [function]` (`8bb5fcfc-9bfd-5192-95f3-5408b87e8e9f`) lines 278-300 [crates/gwiki/src/search/graph_boost.rs:278-300]
  - Signature: `fn graph_result(scope: &SearchScope, path: PathBuf, score: f64) -> WikiSearchResult {`
  - Purpose: Indexed function `graph_result` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:278-300]
- `graph_degradation` (function) component `graph_degradation [function]` (`b57e7bb4-5b8a-570a-8708-6b1c71e52d1e`) lines 302-307 [crates/gwiki/src/search/graph_boost.rs:302-307]
  - Signature: `fn graph_degradation(message: String) -> DegradationKind {`
  - Purpose: Indexed function `graph_degradation` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:302-307]
- `resolve_graph_target` (function) component `resolve_graph_target [function]` (`38f6d167-e3ad-5dc7-bc6c-aed414e42259`) lines 309-346 [crates/gwiki/src/search/graph_boost.rs:309-346]
  - Signature: `fn resolve_graph_target(`
  - Purpose: Indexed function `resolve_graph_target` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:309-346]
- `normalize_path` (function) component `normalize_path [function]` (`30c42656-3e15-598c-870b-eaab68f28588`) lines 348-361 [crates/gwiki/src/search/graph_boost.rs:348-361]
  - Signature: `fn normalize_path(path: PathBuf) -> PathBuf {`
  - Purpose: Indexed function `normalize_path` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:348-361]
- `slug_target_map` (function) component `slug_target_map [function]` (`03f40a7f-98c6-53fe-b0ee-5f89ab47e68d`) lines 363-383 [crates/gwiki/src/search/graph_boost.rs:363-383]
  - Signature: `fn slug_target_map(documents: &[GraphBoostDocument]) -> BTreeMap<String, PathBuf> {`
  - Purpose: Indexed function `slug_target_map` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:363-383]
- `is_external_target` (function) component `is_external_target [function]` (`d7947f91-c709-58f8-8413-3f7b0d707c00`) lines 385-391 [crates/gwiki/src/search/graph_boost.rs:385-391]
  - Signature: `fn is_external_target(target: &str) -> bool {`
  - Purpose: Indexed function `is_external_target` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:385-391]
- `rank_link_neighborhood_boosts_outbound_and_backlinks` (function) component `rank_link_neighborhood_boosts_outbound_and_backlinks [function]` (`1c7467e0-e1dc-5305-88b8-95350229127b`) lines 398-426 [crates/gwiki/src/search/graph_boost.rs:398-426]
  - Signature: `fn rank_link_neighborhood_boosts_outbound_and_backlinks() {`
  - Purpose: Indexed function `rank_link_neighborhood_boosts_outbound_and_backlinks` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:398-426]
- `rank_link_neighborhood_filters_non_searchable_before_truncating` (function) component `rank_link_neighborhood_filters_non_searchable_before_truncating [function]` (`bc77a448-779e-577b-97e5-7933920336ea`) lines 429-451 [crates/gwiki/src/search/graph_boost.rs:429-451]
  - Signature: `fn rank_link_neighborhood_filters_non_searchable_before_truncating() {`
  - Purpose: Indexed function `rank_link_neighborhood_filters_non_searchable_before_truncating` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:429-451]
- `rank_link_neighborhood_resolves_targets_relative_to_source` (function) component `rank_link_neighborhood_resolves_targets_relative_to_source [function]` (`d5e975cf-f240-54ab-bf58-a5c27a8bffa9`) lines 454-472 [crates/gwiki/src/search/graph_boost.rs:454-472]
  - Signature: `fn rank_link_neighborhood_resolves_targets_relative_to_source() {`
  - Purpose: Indexed function `rank_link_neighborhood_resolves_targets_relative_to_source` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:454-472]
- `graph_boost_hits_marks_graph_source` (function) component `graph_boost_hits_marks_graph_source [function]` (`e673cda7-f20f-5753-81da-d305bc0fc023`) lines 475-488 [crates/gwiki/src/search/graph_boost.rs:475-488]
  - Signature: `fn graph_boost_hits_marks_graph_source() {`
  - Purpose: Indexed function `graph_boost_hits_marks_graph_source` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:475-488]
- `unavailable_graph_backend_reports_service_degradation` (function) component `unavailable_graph_backend_reports_service_degradation [function]` (`e32fd87d-d63e-5855-9b99-57930c56b006`) lines 491-511 [crates/gwiki/src/search/graph_boost.rs:491-511]
  - Signature: `fn unavailable_graph_backend_reports_service_degradation() {`
  - Purpose: Indexed function `unavailable_graph_backend_reports_service_degradation` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:491-511]
- `document` (function) component `document [function]` (`10606c7d-551a-5ce5-b5b5-ebaad55c4ac6`) lines 513-518 [crates/gwiki/src/search/graph_boost.rs:513-518]
  - Signature: `fn document(path: &str, title: Option<&str>) -> GraphBoostDocument {`
  - Purpose: Indexed function `document` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:513-518]
- `link` (function) component `link [function]` (`34862526-6253-5dfc-804b-2d97ed43d494`) lines 520-525 [crates/gwiki/src/search/graph_boost.rs:520-525]
  - Signature: `fn link(source_path: &str, target_path: &str) -> GraphBoostLink {`
  - Purpose: Indexed function `link` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:520-525]

