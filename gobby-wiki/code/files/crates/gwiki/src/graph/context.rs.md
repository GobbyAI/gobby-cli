---
title: crates/gwiki/src/graph/context.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/context.rs
  ranges:
  - 8-11
  - 14-16
  - 18-23
  - 25-28
  - 32-39
  - 42-45
  - 48-53
  - 56-61
  - 64-73
  - 76-80
  - 83-88
  - 91-99
  - 102-105
  - 107-153
  - 155-172
  - 174-183
  - 185-201
  - 203-212
  - 214-227
  - 229-242
  - 244-272
  - 274-311
  - 313-320
  - 322-329
  - 331-340
  - 342-390
  - 392-394
  - 407-502
  - 505-557
  - 560-654
  - 656-662
  - 664-670
  - 672-684
  - 686-693
  - 695-714
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/graph/context.rs:8-11](crates/gwiki/src/graph/context.rs#L8-L11), [crates/gwiki/src/graph/context.rs:14-16](crates/gwiki/src/graph/context.rs#L14-L16), [crates/gwiki/src/graph/context.rs:18-23](crates/gwiki/src/graph/context.rs#L18-L23), [crates/gwiki/src/graph/context.rs:25-28](crates/gwiki/src/graph/context.rs#L25-L28), [crates/gwiki/src/graph/context.rs:32-39](crates/gwiki/src/graph/context.rs#L32-L39), [crates/gwiki/src/graph/context.rs:42-45](crates/gwiki/src/graph/context.rs#L42-L45), [crates/gwiki/src/graph/context.rs:48-53](crates/gwiki/src/graph/context.rs#L48-L53), [crates/gwiki/src/graph/context.rs:56-61](crates/gwiki/src/graph/context.rs#L56-L61), [crates/gwiki/src/graph/context.rs:64-73](crates/gwiki/src/graph/context.rs#L64-L73), [crates/gwiki/src/graph/context.rs:76-80](crates/gwiki/src/graph/context.rs#L76-L80), [crates/gwiki/src/graph/context.rs:83-88](crates/gwiki/src/graph/context.rs#L83-L88), [crates/gwiki/src/graph/context.rs:91-99](crates/gwiki/src/graph/context.rs#L91-L99), [crates/gwiki/src/graph/context.rs:102-105](crates/gwiki/src/graph/context.rs#L102-L105), [crates/gwiki/src/graph/context.rs:107-153](crates/gwiki/src/graph/context.rs#L107-L153), [crates/gwiki/src/graph/context.rs:155-172](crates/gwiki/src/graph/context.rs#L155-L172), [crates/gwiki/src/graph/context.rs:174-183](crates/gwiki/src/graph/context.rs#L174-L183), [crates/gwiki/src/graph/context.rs:185-201](crates/gwiki/src/graph/context.rs#L185-L201), [crates/gwiki/src/graph/context.rs:203-212](crates/gwiki/src/graph/context.rs#L203-L212), [crates/gwiki/src/graph/context.rs:214-227](crates/gwiki/src/graph/context.rs#L214-L227), [crates/gwiki/src/graph/context.rs:229-242](crates/gwiki/src/graph/context.rs#L229-L242), [crates/gwiki/src/graph/context.rs:244-272](crates/gwiki/src/graph/context.rs#L244-L272), [crates/gwiki/src/graph/context.rs:274-311](crates/gwiki/src/graph/context.rs#L274-L311), [crates/gwiki/src/graph/context.rs:313-320](crates/gwiki/src/graph/context.rs#L313-L320), [crates/gwiki/src/graph/context.rs:322-329](crates/gwiki/src/graph/context.rs#L322-L329), [crates/gwiki/src/graph/context.rs:331-340](crates/gwiki/src/graph/context.rs#L331-L340), [crates/gwiki/src/graph/context.rs:342-390](crates/gwiki/src/graph/context.rs#L342-L390), [crates/gwiki/src/graph/context.rs:392-394](crates/gwiki/src/graph/context.rs#L392-L394), [crates/gwiki/src/graph/context.rs:407-502](crates/gwiki/src/graph/context.rs#L407-L502), [crates/gwiki/src/graph/context.rs:505-557](crates/gwiki/src/graph/context.rs#L505-L557), [crates/gwiki/src/graph/context.rs:560-654](crates/gwiki/src/graph/context.rs#L560-L654), [crates/gwiki/src/graph/context.rs:656-662](crates/gwiki/src/graph/context.rs#L656-L662), [crates/gwiki/src/graph/context.rs:664-670](crates/gwiki/src/graph/context.rs#L664-L670), [crates/gwiki/src/graph/context.rs:672-684](crates/gwiki/src/graph/context.rs#L672-L684), [crates/gwiki/src/graph/context.rs:686-693](crates/gwiki/src/graph/context.rs#L686-L693), [crates/gwiki/src/graph/context.rs:695-714](crates/gwiki/src/graph/context.rs#L695-L714)

</details>

# crates/gwiki/src/graph/context.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the data model and assembly helpers for a serialized graph-context response used by `gwiki`. `GraphContextOptions` captures whether the context is fully available or degraded/truncated, and `GraphContextPack` bundles the final output: scope, degradation state, warnings, neighborhood details, and recommendations. The helper functions build each part from graph facts and filesystem paths by collecting neighbors, document links, citations, code calls/imports, and per-path warnings, then combine wiki and code edges into unified recommendations and JSON-ready neighborhood records.
[crates/gwiki/src/graph/context.rs:8-11]
[crates/gwiki/src/graph/context.rs:14-16]
[crates/gwiki/src/graph/context.rs:18-23]
[crates/gwiki/src/graph/context.rs:25-28]
[crates/gwiki/src/graph/context.rs:32-39]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GraphContextOptions` | class | `pub struct GraphContextOptions {` | `GraphContextOptions [class]` | `ae429cf1-c77b-58be-bee2-630e1150849f` | 8-11 [crates/gwiki/src/graph/context.rs:8-11] | Indexed class `GraphContextOptions` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:8-11] |
| `GraphContextOptions::available` | method | `pub fn available() -> Self {` | `GraphContextOptions::available [method]` | `ab54c7a8-455e-527e-82db-17c7e366cbd2` | 14-16 [crates/gwiki/src/graph/context.rs:14-16] | Indexed method `GraphContextOptions::available` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:14-16] |
| `GraphContextOptions::degraded` | method | `pub fn degraded(degraded_sources: Vec<String>) -> Self {` | `GraphContextOptions::degraded [method]` | `efaf4f24-0dbc-5da1-9760-f4ec1ae31fc2` | 18-23 [crates/gwiki/src/graph/context.rs:18-23] | Indexed method `GraphContextOptions::degraded` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:18-23] |
| `GraphContextOptions::with_truncated_components` | method | `pub fn with_truncated_components(mut self, truncated_components: Vec<String>) -> Self {` | `GraphContextOptions::with_truncated_components [method]` | `00aa606b-8887-508d-bd4a-76d562bfdfef` | 25-28 [crates/gwiki/src/graph/context.rs:25-28] | Indexed method `GraphContextOptions::with_truncated_components` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:25-28] |
| `GraphContextPack` | class | `pub struct GraphContextPack {` | `GraphContextPack [class]` | `085f1593-8267-50e2-9788-b8672653e4cf` | 32-39 [crates/gwiki/src/graph/context.rs:32-39] | Indexed class `GraphContextPack` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:32-39] |
| `GraphContextScope` | class | `pub struct GraphContextScope {` | `GraphContextScope [class]` | `81940199-14f2-52f7-b553-a043a46cb99e` | 42-45 [crates/gwiki/src/graph/context.rs:42-45] | Indexed class `GraphContextScope` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:42-45] |
| `GraphContextDegradation` | class | `pub struct GraphContextDegradation {` | `GraphContextDegradation [class]` | `8d3dc1e2-3854-5ea4-9faf-d87cc94769c6` | 48-53 [crates/gwiki/src/graph/context.rs:48-53] | Indexed class `GraphContextDegradation` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:48-53] |
| `GraphContextWarning` | class | `pub struct GraphContextWarning {` | `GraphContextWarning [class]` | `dae1bbc5-3b4c-5c33-8cd1-671ee6f706c3` | 56-61 [crates/gwiki/src/graph/context.rs:56-61] | Indexed class `GraphContextWarning` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:56-61] |
| `GraphContextNeighborhood` | class | `pub struct GraphContextNeighborhood {` | `GraphContextNeighborhood [class]` | `94a7851c-1c7a-5287-bae1-9b4239062561` | 64-73 [crates/gwiki/src/graph/context.rs:64-73] | Indexed class `GraphContextNeighborhood` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:64-73] |
| `GraphContextNeighbor` | class | `pub struct GraphContextNeighbor {` | `GraphContextNeighbor [class]` | `839ccabb-30c6-5660-8b60-12001f3fcaed` | 76-80 [crates/gwiki/src/graph/context.rs:76-80] | Indexed class `GraphContextNeighbor` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:76-80] |
| `GraphContextDocLink` | class | `pub struct GraphContextDocLink {` | `GraphContextDocLink [class]` | `bb150b11-0bd9-5a7b-90d1-d37a443367cb` | 83-88 [crates/gwiki/src/graph/context.rs:83-88] | Indexed class `GraphContextDocLink` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:83-88] |
| `GraphContextCodeEdge` | class | `pub struct GraphContextCodeEdge {` | `GraphContextCodeEdge [class]` | `23901316-3853-5209-9121-4dcf36bc096a` | 91-99 [crates/gwiki/src/graph/context.rs:91-99] | Indexed class `GraphContextCodeEdge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:91-99] |
| `GraphContextRecommendation` | class | `pub struct GraphContextRecommendation {` | `GraphContextRecommendation [class]` | `3c9d1ab6-770b-5794-9f13-4e51a0170bd2` | 102-105 [crates/gwiki/src/graph/context.rs:102-105] | Indexed class `GraphContextRecommendation` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:102-105] |
| `build_context_pack` | function | `pub fn build_context_pack(` | `build_context_pack [function]` | `390af12e-a48d-51ee-a2c3-b48f854f1065` | 107-153 [crates/gwiki/src/graph/context.rs:107-153] | Indexed function `build_context_pack` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:107-153] |
| `context_scope` | function | `fn context_scope(facts: &WikiGraphFacts) -> GraphContextScope {` | `context_scope [function]` | `031478d6-2bba-5920-ac6a-ee17c2d497eb` | 155-172 [crates/gwiki/src/graph/context.rs:155-172] | Indexed function `context_scope` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:155-172] |
| `citations_by_document` | function | `fn citations_by_document(facts: &WikiGraphFacts) -> BTreeMap<PathBuf, BTreeSet<String>> {` | `citations_by_document [function]` | `2289f8d2-db5f-589b-9812-e444b861ebb4` | 174-183 [crates/gwiki/src/graph/context.rs:174-183] | Indexed function `citations_by_document` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:174-183] |
| `degradation_warnings` | function | `fn degradation_warnings(` | `degradation_warnings [function]` | `3188ca19-45e3-5d82-a48b-a862e1b9c7ec` | 185-201 [crates/gwiki/src/graph/context.rs:185-201] | Indexed function `degradation_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:185-201] |
| `capped_graph_warning` | function | `fn capped_graph_warning(truncated_components: &[String]) -> String {` | `capped_graph_warning [function]` | `daab9c99-4bfe-5408-a14d-a19d4058753a` | 203-212 [crates/gwiki/src/graph/context.rs:203-212] | Indexed function `capped_graph_warning` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:203-212] |
| `stale_link_warnings` | function | `fn stale_link_warnings(facts: &WikiGraphFacts) -> Vec<GraphContextWarning> {` | `stale_link_warnings [function]` | `927e84de-831c-546f-b888-34afec7daa35` | 214-227 [crates/gwiki/src/graph/context.rs:214-227] | Indexed function `stale_link_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:214-227] |
| `audit_warnings` | function | `fn audit_warnings(` | `audit_warnings [function]` | `3c908a9e-7ec0-5316-ab44-9748bf8d4cf2` | 229-242 [crates/gwiki/src/graph/context.rs:229-242] | Indexed function `audit_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:229-242] |
| `neighbors_for_path` | function | `fn neighbors_for_path(facts: &WikiGraphFacts, path: &Path) -> Vec<GraphContextNeighbor> {` | `neighbors_for_path [function]` | `116bd1b0-a85d-5eb3-b701-758669e4d90a` | 244-272 [crates/gwiki/src/graph/context.rs:244-272] | Indexed function `neighbors_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:244-272] |
| `doc_links_for_path` | function | `fn doc_links_for_path(facts: &WikiGraphFacts, path: &Path) -> Vec<GraphContextDocLink> {` | `doc_links_for_path [function]` | `f9eca0d4-d6cd-593e-a78a-0def53a2921c` | 274-311 [crates/gwiki/src/graph/context.rs:274-311] | Indexed function `doc_links_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:274-311] |
| `code_calls_for_path` | function | `fn code_calls_for_path(facts: &WikiGraphFacts, path: &Path) -> Vec<GraphContextCodeEdge> {` | `code_calls_for_path [function]` | `c5de296b-0fa5-5040-9908-f12f668eeb58` | 313-320 [crates/gwiki/src/graph/context.rs:313-320] | Indexed function `code_calls_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:313-320] |
| `code_imports_for_path` | function | `fn code_imports_for_path(facts: &WikiGraphFacts, path: &Path) -> Vec<GraphContextCodeEdge> {` | `code_imports_for_path [function]` | `7cc6251b-6f6e-5110-8e0f-76e13187f226` | 322-329 [crates/gwiki/src/graph/context.rs:322-329] | Indexed function `code_imports_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:322-329] |
| `graph_context_code_edge` | function | `fn graph_context_code_edge(edge: &WikiGraphCodeEdge) -> GraphContextCodeEdge {` | `graph_context_code_edge [function]` | `c56def57-c58a-5054-9681-a828f60fb30b` | 331-340 [crates/gwiki/src/graph/context.rs:331-340] | Indexed function `graph_context_code_edge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:331-340] |
| `recommendations` | function | `fn recommendations(` | `recommendations [function]` | `c6d13b57-41a9-5bc9-80b8-7c9136cba20d` | 342-390 [crates/gwiki/src/graph/context.rs:342-390] | Indexed function `recommendations` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:342-390] |
| `display_path` | function | `fn display_path(path: &Path) -> String {` | `display_path [function]` | `44fb0018-7548-564f-8e8b-15854ccf489e` | 392-394 [crates/gwiki/src/graph/context.rs:392-394] | Indexed function `display_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:392-394] |
| `graph_context_json_includes_neighborhoods_and_empty_code_edges` | function | `fn graph_context_json_includes_neighborhoods_and_empty_code_edges() {` | `graph_context_json_includes_neighborhoods_and_empty_code_edges [function]` | `2a674ccf-433f-591a-b751-8bba0c39eddc` | 407-502 [crates/gwiki/src/graph/context.rs:407-502] | Indexed function `graph_context_json_includes_neighborhoods_and_empty_code_edges` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:407-502] |
| `graph_context_json_reports_truncated_shared_code_as_capped_data` | function | `fn graph_context_json_reports_truncated_shared_code_as_capped_data() {` | `graph_context_json_reports_truncated_shared_code_as_capped_data [function]` | `4c042788-2347-572d-84c9-86c85fbc31fb` | 505-557 [crates/gwiki/src/graph/context.rs:505-557] | Indexed function `graph_context_json_reports_truncated_shared_code_as_capped_data` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:505-557] |
| `ask_unified_graph_context_merges_wiki_and_code_edges` | function | `fn ask_unified_graph_context_merges_wiki_and_code_edges() {` | `ask_unified_graph_context_merges_wiki_and_code_edges [function]` | `e9bbaf7b-c48c-5cc3-8300-7804712fd68a` | 560-654 [crates/gwiki/src/graph/context.rs:560-654] | Indexed function `ask_unified_graph_context_merges_wiki_and_code_edges` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:560-654] |
| `doc` | function | `fn doc(scope: SearchScope, path: &str, title: Option<&str>) -> WikiGraphDocument {` | `doc [function]` | `1fe41e41-9221-5863-8ebe-e33434d242ab` | 656-662 [crates/gwiki/src/graph/context.rs:656-662] | Indexed function `doc` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:656-662] |
| `source` | function | `fn source(scope: SearchScope, source_path: &str, document_path: &str) -> WikiGraphSource {` | `source [function]` | `a344636d-27a7-584c-a4f8-657e8830da01` | 664-670 [crates/gwiki/src/graph/context.rs:664-670] | Indexed function `source` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:664-670] |
| `resolved_link` | function | `fn resolved_link(` | `resolved_link [function]` | `86eae7bb-ed54-5a36-9f34-dfe81a217197` | 672-684 [crates/gwiki/src/graph/context.rs:672-684] | Indexed function `resolved_link` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:672-684] |
| `unresolved_link` | function | `fn unresolved_link(scope: SearchScope, source_path: &str, raw_target: &str) -> WikiGraphLink {` | `unresolved_link [function]` | `c40a8ac3-c381-53ee-9768-4a1a61f3b35a` | 686-693 [crates/gwiki/src/graph/context.rs:686-693] | Indexed function `unresolved_link` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:686-693] |
| `code_edge` | function | `fn code_edge(` | `code_edge [function]` | `cc789d4c-c904-5cba-8d63-b5b3aae6fe21` | 695-714 [crates/gwiki/src/graph/context.rs:695-714] | Indexed function `code_edge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:695-714] |
