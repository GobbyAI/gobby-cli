---
title: crates/gwiki/src/search/graph_boost.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/graph_boost.rs
  ranges:
  - 21-24
  - 27-32
  - 35-39
  - 41-44
  - 46-51
  - '54'
  - 57-65
  - 68-70
  - 73-77
  - 81-89
  - 93-98
  - 101-103
  - 106-108
  - 112-123
  - 126-129
  - 132-134
  - 136-145
  - 149-184
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/search/graph_boost.rs:21-24](crates/gwiki/src/search/graph_boost.rs#L21-L24), [crates/gwiki/src/search/graph_boost.rs:27-32](crates/gwiki/src/search/graph_boost.rs#L27-L32), [crates/gwiki/src/search/graph_boost.rs:35-39](crates/gwiki/src/search/graph_boost.rs#L35-L39), [crates/gwiki/src/search/graph_boost.rs:41-44](crates/gwiki/src/search/graph_boost.rs#L41-L44), [crates/gwiki/src/search/graph_boost.rs:46-51](crates/gwiki/src/search/graph_boost.rs#L46-L51), [crates/gwiki/src/search/graph_boost.rs:54](crates/gwiki/src/search/graph_boost.rs#L54), [crates/gwiki/src/search/graph_boost.rs:57-65](crates/gwiki/src/search/graph_boost.rs#L57-L65), [crates/gwiki/src/search/graph_boost.rs:68-70](crates/gwiki/src/search/graph_boost.rs#L68-L70), [crates/gwiki/src/search/graph_boost.rs:73-77](crates/gwiki/src/search/graph_boost.rs#L73-L77), [crates/gwiki/src/search/graph_boost.rs:81-89](crates/gwiki/src/search/graph_boost.rs#L81-L89), [crates/gwiki/src/search/graph_boost.rs:93-98](crates/gwiki/src/search/graph_boost.rs#L93-L98), [crates/gwiki/src/search/graph_boost.rs:101-103](crates/gwiki/src/search/graph_boost.rs#L101-L103), [crates/gwiki/src/search/graph_boost.rs:106-108](crates/gwiki/src/search/graph_boost.rs#L106-L108), [crates/gwiki/src/search/graph_boost.rs:112-123](crates/gwiki/src/search/graph_boost.rs#L112-L123), [crates/gwiki/src/search/graph_boost.rs:126-129](crates/gwiki/src/search/graph_boost.rs#L126-L129), [crates/gwiki/src/search/graph_boost.rs:132-134](crates/gwiki/src/search/graph_boost.rs#L132-L134), [crates/gwiki/src/search/graph_boost.rs:136-145](crates/gwiki/src/search/graph_boost.rs#L136-L145), [crates/gwiki/src/search/graph_boost.rs:149-184](crates/gwiki/src/search/graph_boost.rs#L149-L184), [crates/gwiki/src/search/graph_boost.rs:188-191](crates/gwiki/src/search/graph_boost.rs#L188-L191), [crates/gwiki/src/search/graph_boost.rs:194-197](crates/gwiki/src/search/graph_boost.rs#L194-L197), [crates/gwiki/src/search/graph_boost.rs:199-264](crates/gwiki/src/search/graph_boost.rs#L199-L264), [crates/gwiki/src/search/graph_boost.rs:266-277](crates/gwiki/src/search/graph_boost.rs#L266-L277), [crates/gwiki/src/search/graph_boost.rs:279-301](crates/gwiki/src/search/graph_boost.rs#L279-L301), [crates/gwiki/src/search/graph_boost.rs:303-308](crates/gwiki/src/search/graph_boost.rs#L303-L308), [crates/gwiki/src/search/graph_boost.rs:310-347](crates/gwiki/src/search/graph_boost.rs#L310-L347), [crates/gwiki/src/search/graph_boost.rs:349-362](crates/gwiki/src/search/graph_boost.rs#L349-L362), [crates/gwiki/src/search/graph_boost.rs:364-384](crates/gwiki/src/search/graph_boost.rs#L364-L384), [crates/gwiki/src/search/graph_boost.rs:386-392](crates/gwiki/src/search/graph_boost.rs#L386-L392), [crates/gwiki/src/search/graph_boost.rs:399-427](crates/gwiki/src/search/graph_boost.rs#L399-L427), [crates/gwiki/src/search/graph_boost.rs:430-452](crates/gwiki/src/search/graph_boost.rs#L430-L452), [crates/gwiki/src/search/graph_boost.rs:455-473](crates/gwiki/src/search/graph_boost.rs#L455-L473), [crates/gwiki/src/search/graph_boost.rs:476-489](crates/gwiki/src/search/graph_boost.rs#L476-L489), [crates/gwiki/src/search/graph_boost.rs:492-512](crates/gwiki/src/search/graph_boost.rs#L492-L512), [crates/gwiki/src/search/graph_boost.rs:514-519](crates/gwiki/src/search/graph_boost.rs#L514-L519), [crates/gwiki/src/search/graph_boost.rs:521-526](crates/gwiki/src/search/graph_boost.rs#L521-L526)

</details>

# crates/gwiki/src/search/graph_boost.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements graph-based search boosting for wiki search, with a configurable backend interface that takes seed paths and returns boosted `WikiSearchResult` hits plus an optional degradation signal. It defines a default config, request/outcome types, a `GraphBoostBackend` trait, no-op and unavailable fallbacks, and a Falkor/memory-backed implementation that resolves graph targets, ranks linked neighborhoods, filters and normalizes paths, and turns graph relationships into search hits and provenance.
[crates/gwiki/src/search/graph_boost.rs:21-24]
[crates/gwiki/src/search/graph_boost.rs:27-32]
[crates/gwiki/src/search/graph_boost.rs:35-39]
[crates/gwiki/src/search/graph_boost.rs:41-44]
[crates/gwiki/src/search/graph_boost.rs:46-51]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GraphBoostConfig` | class | `pub struct GraphBoostConfig {` | `GraphBoostConfig [class]` | `c6a6d24a-b8ee-52d3-9c20-562e234ab20e` | 21-24 [crates/gwiki/src/search/graph_boost.rs:21-24] | Indexed class `GraphBoostConfig` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:21-24] |
| `GraphBoostConfig::default` | method | `fn default() -> Self {` | `GraphBoostConfig::default [method]` | `78eceb97-9cc6-5e56-b572-150250b3dbd6` | 27-32 [crates/gwiki/src/search/graph_boost.rs:27-32] | Indexed method `GraphBoostConfig::default` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:27-32] |
| `GraphBoostRequest` | class | `pub struct GraphBoostRequest {` | `GraphBoostRequest [class]` | `8f5be825-7c2b-53eb-b02a-82f0654d2051` | 35-39 [crates/gwiki/src/search/graph_boost.rs:35-39] | Indexed class `GraphBoostRequest` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:35-39] |
| `GraphBoostOutcome` | class | `pub struct GraphBoostOutcome {` | `GraphBoostOutcome [class]` | `3a59b0b5-bc0e-5cd9-9b25-309e57f45d4b` | 41-44 [crates/gwiki/src/search/graph_boost.rs:41-44] | Indexed class `GraphBoostOutcome` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:41-44] |
| `GraphBoostBackend` | type | `pub trait GraphBoostBackend {` | `GraphBoostBackend [type]` | `79b9f5cf-8ade-5662-b3ca-60dc0207e563` | 46-51 [crates/gwiki/src/search/graph_boost.rs:46-51] | Indexed type `GraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:46-51] |
| `NoopGraphBoostBackend` | class | `pub struct NoopGraphBoostBackend;` | `NoopGraphBoostBackend [class]` | `fdcf7e67-3ae8-5cd0-bbf5-cbf0b414835b` | 54-54 [crates/gwiki/src/search/graph_boost.rs:54] | Indexed class `NoopGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:54] |
| `NoopGraphBoostBackend::search_graph_boost` | method | `fn search_graph_boost(` | `NoopGraphBoostBackend::search_graph_boost [method]` | `f32690f3-5a50-56d2-ba9a-9cbcfdecf2fe` | 57-65 [crates/gwiki/src/search/graph_boost.rs:57-65] | Indexed method `NoopGraphBoostBackend::search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:57-65] |
| `UnavailableGraphBoostBackend` | class | `pub struct UnavailableGraphBoostBackend {` | `UnavailableGraphBoostBackend [class]` | `40dcc694-d455-5d95-878f-28874a4b72f6` | 68-70 [crates/gwiki/src/search/graph_boost.rs:68-70] | Indexed class `UnavailableGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:68-70] |
| `UnavailableGraphBoostBackend::unreachable` | method | `pub fn unreachable(message: String) -> Self {` | `UnavailableGraphBoostBackend::unreachable [method]` | `add1c616-c757-52e5-a5c1-55ee56ebaa9f` | 73-77 [crates/gwiki/src/search/graph_boost.rs:73-77] | Indexed method `UnavailableGraphBoostBackend::unreachable` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:73-77] |
| `UnavailableGraphBoostBackend::search_graph_boost` | method | `fn search_graph_boost(` | `UnavailableGraphBoostBackend::search_graph_boost [method]` | `0a53f15f-1efa-59fd-86e8-dbf219fb2520` | 81-89 [crates/gwiki/src/search/graph_boost.rs:81-89] | Indexed method `UnavailableGraphBoostBackend::search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:81-89] |
| `search_graph_boost` | function | `fn search_graph_boost(` | `search_graph_boost [function]` | `70163a3f-43fe-5629-80aa-8c5df7226a57` | 93-98 [crates/gwiki/src/search/graph_boost.rs:93-98] | Indexed function `search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:93-98] |
| `MemoryGraphBoostBackend` | class | `pub struct MemoryGraphBoostBackend {` | `MemoryGraphBoostBackend [class]` | `1d246388-9a09-55e8-ac0a-d925bebd6cab` | 101-103 [crates/gwiki/src/search/graph_boost.rs:101-103] | Indexed class `MemoryGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:101-103] |
| `MemoryGraphBoostBackend::new` | method | `pub fn new(graph: MemoryWikiGraph) -> Self {` | `MemoryGraphBoostBackend::new [method]` | `8c18633a-8ea1-5131-8d52-c333b9b42f3b` | 106-108 [crates/gwiki/src/search/graph_boost.rs:106-108] | Indexed method `MemoryGraphBoostBackend::new` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:106-108] |
| `MemoryGraphBoostBackend::search_graph_boost` | method | `fn search_graph_boost(` | `MemoryGraphBoostBackend::search_graph_boost [method]` | `6790f5e3-3bd0-52ab-a222-0c1734c084a1` | 112-123 [crates/gwiki/src/search/graph_boost.rs:112-123] | Indexed method `MemoryGraphBoostBackend::search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:112-123] |
| `FalkorGraphBoostBackend` | class | `pub struct FalkorGraphBoostBackend {` | `FalkorGraphBoostBackend [class]` | `712ab77e-617b-5fd8-9c07-592dc9d51642` | 126-129 [crates/gwiki/src/search/graph_boost.rs:126-129] | Indexed class `FalkorGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:126-129] |
| `FalkorGraphBoostBackend::new` | method | `pub fn new(config: &FalkorConfig) -> Result<Self, SearchError> {` | `FalkorGraphBoostBackend::new [method]` | `7cc7999d-089c-5f8c-937b-9857da600394` | 132-134 [crates/gwiki/src/search/graph_boost.rs:132-134] | Indexed method `FalkorGraphBoostBackend::new` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:132-134] |
| `FalkorGraphBoostBackend::new_with_config` | method | `pub fn new_with_config(` | `FalkorGraphBoostBackend::new_with_config [method]` | `0bd13d2e-41a2-591a-a482-6b576bc6976b` | 136-145 [crates/gwiki/src/search/graph_boost.rs:136-145] | Indexed method `FalkorGraphBoostBackend::new_with_config` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:136-145] |
| `FalkorGraphBoostBackend::search_graph_boost` | method | `fn search_graph_boost(` | `FalkorGraphBoostBackend::search_graph_boost [method]` | `2e663a3b-96f6-5002-abfb-da5c0995391b` | 149-184 [crates/gwiki/src/search/graph_boost.rs:149-184] | Indexed method `FalkorGraphBoostBackend::search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:149-184] |
| `GraphBoostDocument` | class | `pub struct GraphBoostDocument {` | `GraphBoostDocument [class]` | `fde38213-4994-52f6-af90-c7927cdbbb4d` | 188-191 [crates/gwiki/src/search/graph_boost.rs:188-191] | Indexed class `GraphBoostDocument` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:188-191] |
| `GraphBoostLink` | class | `pub struct GraphBoostLink {` | `GraphBoostLink [class]` | `2d5784f3-b5af-54db-9564-f1dfb698531a` | 194-197 [crates/gwiki/src/search/graph_boost.rs:194-197] | Indexed class `GraphBoostLink` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:194-197] |
| `rank_link_neighborhood` | function | `pub fn rank_link_neighborhood(` | `rank_link_neighborhood [function]` | `399bea63-f61b-5125-b349-6fbb15c7749e` | 199-264 [crates/gwiki/src/search/graph_boost.rs:199-264] | Indexed function `rank_link_neighborhood` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:199-264] |
| `graph_boost_hits` | function | `pub fn graph_boost_hits(` | `graph_boost_hits [function]` | `c5b8b0c9-5895-5b22-b50d-9380acf8430d` | 266-277 [crates/gwiki/src/search/graph_boost.rs:266-277] | Indexed function `graph_boost_hits` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:266-277] |
| `graph_result` | function | `fn graph_result(scope: &SearchScope, path: PathBuf, score: f64) -> WikiSearchResult {` | `graph_result [function]` | `252c20c0-2879-5e9a-ace9-2c20b779f1bb` | 279-301 [crates/gwiki/src/search/graph_boost.rs:279-301] | Indexed function `graph_result` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:279-301] |
| `graph_degradation` | function | `fn graph_degradation(message: String) -> DegradationKind {` | `graph_degradation [function]` | `c3c15f84-b5cf-5302-a3df-fbab1d14abad` | 303-308 [crates/gwiki/src/search/graph_boost.rs:303-308] | Indexed function `graph_degradation` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:303-308] |
| `resolve_graph_target` | function | `fn resolve_graph_target(` | `resolve_graph_target [function]` | `dc80325d-a260-5da1-b7e6-fb3ea37368a9` | 310-347 [crates/gwiki/src/search/graph_boost.rs:310-347] | Indexed function `resolve_graph_target` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:310-347] |
| `normalize_path` | function | `fn normalize_path(path: PathBuf) -> PathBuf {` | `normalize_path [function]` | `78122284-8a95-5c83-a110-878250ca0676` | 349-362 [crates/gwiki/src/search/graph_boost.rs:349-362] | Indexed function `normalize_path` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:349-362] |
| `slug_target_map` | function | `fn slug_target_map(documents: &[GraphBoostDocument]) -> BTreeMap<String, PathBuf> {` | `slug_target_map [function]` | `5497cb79-b2bb-5b5d-943a-0f9d4af8d67e` | 364-384 [crates/gwiki/src/search/graph_boost.rs:364-384] | Indexed function `slug_target_map` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:364-384] |
| `is_external_target` | function | `fn is_external_target(target: &str) -> bool {` | `is_external_target [function]` | `2a76763b-11aa-53db-a2c2-91355e88c41b` | 386-392 [crates/gwiki/src/search/graph_boost.rs:386-392] | Indexed function `is_external_target` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:386-392] |
| `rank_link_neighborhood_boosts_outbound_and_backlinks` | function | `fn rank_link_neighborhood_boosts_outbound_and_backlinks() {` | `rank_link_neighborhood_boosts_outbound_and_backlinks [function]` | `919d4929-726e-54d4-bfff-6d45ae422378` | 399-427 [crates/gwiki/src/search/graph_boost.rs:399-427] | Indexed function `rank_link_neighborhood_boosts_outbound_and_backlinks` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:399-427] |
| `rank_link_neighborhood_filters_non_searchable_before_truncating` | function | `fn rank_link_neighborhood_filters_non_searchable_before_truncating() {` | `rank_link_neighborhood_filters_non_searchable_before_truncating [function]` | `b5d596ff-a374-5d33-bbfd-6cc4cc9efee2` | 430-452 [crates/gwiki/src/search/graph_boost.rs:430-452] | Indexed function `rank_link_neighborhood_filters_non_searchable_before_truncating` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:430-452] |
| `rank_link_neighborhood_resolves_targets_relative_to_source` | function | `fn rank_link_neighborhood_resolves_targets_relative_to_source() {` | `rank_link_neighborhood_resolves_targets_relative_to_source [function]` | `d6ed0fc2-a13e-5a0d-9cc3-57070804098c` | 455-473 [crates/gwiki/src/search/graph_boost.rs:455-473] | Indexed function `rank_link_neighborhood_resolves_targets_relative_to_source` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:455-473] |
| `graph_boost_hits_marks_graph_source` | function | `fn graph_boost_hits_marks_graph_source() {` | `graph_boost_hits_marks_graph_source [function]` | `07a0094a-ab99-575b-b481-334a769e52a4` | 476-489 [crates/gwiki/src/search/graph_boost.rs:476-489] | Indexed function `graph_boost_hits_marks_graph_source` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:476-489] |
| `unavailable_graph_backend_reports_service_degradation` | function | `fn unavailable_graph_backend_reports_service_degradation() {` | `unavailable_graph_backend_reports_service_degradation [function]` | `5819796a-5e77-539e-9acd-1fbefbc7e2ec` | 492-512 [crates/gwiki/src/search/graph_boost.rs:492-512] | Indexed function `unavailable_graph_backend_reports_service_degradation` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:492-512] |
| `document` | function | `fn document(path: &str, title: Option<&str>) -> GraphBoostDocument {` | `document [function]` | `17385d68-e8e9-5c02-94c9-eed3651bf547` | 514-519 [crates/gwiki/src/search/graph_boost.rs:514-519] | Indexed function `document` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:514-519] |
| `link` | function | `fn link(source_path: &str, target_path: &str) -> GraphBoostLink {` | `link [function]` | `276cff58-94f4-5748-bee9-4deb1a269a57` | 521-526 [crates/gwiki/src/search/graph_boost.rs:521-526] | Indexed function `link` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:521-526] |
