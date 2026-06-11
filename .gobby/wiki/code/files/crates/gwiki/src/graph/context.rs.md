---
title: crates/gwiki/src/graph/context.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/context.rs
  ranges:
  - 8-11
  - 13-29
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

# crates/gwiki/src/graph/context.rs

Module: [[code/modules/crates/gwiki/src/graph|crates/gwiki/src/graph]]

## Purpose

`crates/gwiki/src/graph/context.rs` exposes 36 indexed API symbols.
[crates/gwiki/src/graph/context.rs:8-11]
[crates/gwiki/src/graph/context.rs:13-29]
[crates/gwiki/src/graph/context.rs:14-16]
[crates/gwiki/src/graph/context.rs:18-23]
[crates/gwiki/src/graph/context.rs:25-28]

## API Symbols

- `GraphContextOptions` (class) component `GraphContextOptions [class]` (`ae429cf1-c77b-58be-bee2-630e1150849f`) lines 8-11 [crates/gwiki/src/graph/context.rs:8-11]
  - Signature: `pub struct GraphContextOptions {`
  - Purpose: Indexed class `GraphContextOptions` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:8-11]
- `GraphContextOptions` (class) component `GraphContextOptions [class]` (`57bf3270-4dc6-5fed-b931-ce44e5a81668`) lines 13-29 [crates/gwiki/src/graph/context.rs:13-29]
  - Signature: `impl GraphContextOptions {`
  - Purpose: Indexed class `GraphContextOptions` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:13-29]
- `GraphContextOptions.available` (method) component `GraphContextOptions.available [method]` (`ab54c7a8-455e-527e-82db-17c7e366cbd2`) lines 14-16 [crates/gwiki/src/graph/context.rs:14-16]
  - Signature: `pub fn available() -> Self {`
  - Purpose: Indexed method `GraphContextOptions.available` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:14-16]
- `GraphContextOptions.degraded` (method) component `GraphContextOptions.degraded [method]` (`efaf4f24-0dbc-5da1-9760-f4ec1ae31fc2`) lines 18-23 [crates/gwiki/src/graph/context.rs:18-23]
  - Signature: `pub fn degraded(degraded_sources: Vec<String>) -> Self {`
  - Purpose: Indexed method `GraphContextOptions.degraded` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:18-23]
- `GraphContextOptions.with_truncated_components` (method) component `GraphContextOptions.with_truncated_components [method]` (`00aa606b-8887-508d-bd4a-76d562bfdfef`) lines 25-28 [crates/gwiki/src/graph/context.rs:25-28]
  - Signature: `pub fn with_truncated_components(mut self, truncated_components: Vec<String>) -> Self {`
  - Purpose: Indexed method `GraphContextOptions.with_truncated_components` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:25-28]
- `GraphContextPack` (class) component `GraphContextPack [class]` (`085f1593-8267-50e2-9788-b8672653e4cf`) lines 32-39 [crates/gwiki/src/graph/context.rs:32-39]
  - Signature: `pub struct GraphContextPack {`
  - Purpose: Indexed class `GraphContextPack` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:32-39]
- `GraphContextScope` (class) component `GraphContextScope [class]` (`81940199-14f2-52f7-b553-a043a46cb99e`) lines 42-45 [crates/gwiki/src/graph/context.rs:42-45]
  - Signature: `pub struct GraphContextScope {`
  - Purpose: Indexed class `GraphContextScope` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:42-45]
- `GraphContextDegradation` (class) component `GraphContextDegradation [class]` (`8d3dc1e2-3854-5ea4-9faf-d87cc94769c6`) lines 48-53 [crates/gwiki/src/graph/context.rs:48-53]
  - Signature: `pub struct GraphContextDegradation {`
  - Purpose: Indexed class `GraphContextDegradation` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:48-53]
- `GraphContextWarning` (class) component `GraphContextWarning [class]` (`dae1bbc5-3b4c-5c33-8cd1-671ee6f706c3`) lines 56-61 [crates/gwiki/src/graph/context.rs:56-61]
  - Signature: `pub struct GraphContextWarning {`
  - Purpose: Indexed class `GraphContextWarning` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:56-61]
- `GraphContextNeighborhood` (class) component `GraphContextNeighborhood [class]` (`94a7851c-1c7a-5287-bae1-9b4239062561`) lines 64-73 [crates/gwiki/src/graph/context.rs:64-73]
  - Signature: `pub struct GraphContextNeighborhood {`
  - Purpose: Indexed class `GraphContextNeighborhood` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:64-73]
- `GraphContextNeighbor` (class) component `GraphContextNeighbor [class]` (`839ccabb-30c6-5660-8b60-12001f3fcaed`) lines 76-80 [crates/gwiki/src/graph/context.rs:76-80]
  - Signature: `pub struct GraphContextNeighbor {`
  - Purpose: Indexed class `GraphContextNeighbor` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:76-80]
- `GraphContextDocLink` (class) component `GraphContextDocLink [class]` (`bb150b11-0bd9-5a7b-90d1-d37a443367cb`) lines 83-88 [crates/gwiki/src/graph/context.rs:83-88]
  - Signature: `pub struct GraphContextDocLink {`
  - Purpose: Indexed class `GraphContextDocLink` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:83-88]
- `GraphContextCodeEdge` (class) component `GraphContextCodeEdge [class]` (`23901316-3853-5209-9121-4dcf36bc096a`) lines 91-99 [crates/gwiki/src/graph/context.rs:91-99]
  - Signature: `pub struct GraphContextCodeEdge {`
  - Purpose: Indexed class `GraphContextCodeEdge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:91-99]
- `GraphContextRecommendation` (class) component `GraphContextRecommendation [class]` (`3c9d1ab6-770b-5794-9f13-4e51a0170bd2`) lines 102-105 [crates/gwiki/src/graph/context.rs:102-105]
  - Signature: `pub struct GraphContextRecommendation {`
  - Purpose: Indexed class `GraphContextRecommendation` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:102-105]
- `build_context_pack` (function) component `build_context_pack [function]` (`390af12e-a48d-51ee-a2c3-b48f854f1065`) lines 107-153 [crates/gwiki/src/graph/context.rs:107-153]
  - Signature: `pub fn build_context_pack(`
  - Purpose: Indexed function `build_context_pack` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:107-153]
- `context_scope` (function) component `context_scope [function]` (`031478d6-2bba-5920-ac6a-ee17c2d497eb`) lines 155-172 [crates/gwiki/src/graph/context.rs:155-172]
  - Signature: `fn context_scope(facts: &WikiGraphFacts) -> GraphContextScope {`
  - Purpose: Indexed function `context_scope` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:155-172]
- `citations_by_document` (function) component `citations_by_document [function]` (`2289f8d2-db5f-589b-9812-e444b861ebb4`) lines 174-183 [crates/gwiki/src/graph/context.rs:174-183]
  - Signature: `fn citations_by_document(facts: &WikiGraphFacts) -> BTreeMap<PathBuf, BTreeSet<String>> {`
  - Purpose: Indexed function `citations_by_document` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:174-183]
- `degradation_warnings` (function) component `degradation_warnings [function]` (`3188ca19-45e3-5d82-a48b-a862e1b9c7ec`) lines 185-201 [crates/gwiki/src/graph/context.rs:185-201]
  - Signature: `fn degradation_warnings(`
  - Purpose: Indexed function `degradation_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:185-201]
- `capped_graph_warning` (function) component `capped_graph_warning [function]` (`daab9c99-4bfe-5408-a14d-a19d4058753a`) lines 203-212 [crates/gwiki/src/graph/context.rs:203-212]
  - Signature: `fn capped_graph_warning(truncated_components: &[String]) -> String {`
  - Purpose: Indexed function `capped_graph_warning` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:203-212]
- `stale_link_warnings` (function) component `stale_link_warnings [function]` (`927e84de-831c-546f-b888-34afec7daa35`) lines 214-227 [crates/gwiki/src/graph/context.rs:214-227]
  - Signature: `fn stale_link_warnings(facts: &WikiGraphFacts) -> Vec<GraphContextWarning> {`
  - Purpose: Indexed function `stale_link_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:214-227]
- `audit_warnings` (function) component `audit_warnings [function]` (`3c908a9e-7ec0-5316-ab44-9748bf8d4cf2`) lines 229-242 [crates/gwiki/src/graph/context.rs:229-242]
  - Signature: `fn audit_warnings(`
  - Purpose: Indexed function `audit_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:229-242]
- `neighbors_for_path` (function) component `neighbors_for_path [function]` (`116bd1b0-a85d-5eb3-b701-758669e4d90a`) lines 244-272 [crates/gwiki/src/graph/context.rs:244-272]
  - Signature: `fn neighbors_for_path(facts: &WikiGraphFacts, path: &Path) -> Vec<GraphContextNeighbor> {`
  - Purpose: Indexed function `neighbors_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:244-272]
- `doc_links_for_path` (function) component `doc_links_for_path [function]` (`f9eca0d4-d6cd-593e-a78a-0def53a2921c`) lines 274-311 [crates/gwiki/src/graph/context.rs:274-311]
  - Signature: `fn doc_links_for_path(facts: &WikiGraphFacts, path: &Path) -> Vec<GraphContextDocLink> {`
  - Purpose: Indexed function `doc_links_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:274-311]
- `code_calls_for_path` (function) component `code_calls_for_path [function]` (`c5de296b-0fa5-5040-9908-f12f668eeb58`) lines 313-320 [crates/gwiki/src/graph/context.rs:313-320]
  - Signature: `fn code_calls_for_path(facts: &WikiGraphFacts, path: &Path) -> Vec<GraphContextCodeEdge> {`
  - Purpose: Indexed function `code_calls_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:313-320]
- `code_imports_for_path` (function) component `code_imports_for_path [function]` (`7cc6251b-6f6e-5110-8e0f-76e13187f226`) lines 322-329 [crates/gwiki/src/graph/context.rs:322-329]
  - Signature: `fn code_imports_for_path(facts: &WikiGraphFacts, path: &Path) -> Vec<GraphContextCodeEdge> {`
  - Purpose: Indexed function `code_imports_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:322-329]
- `graph_context_code_edge` (function) component `graph_context_code_edge [function]` (`c56def57-c58a-5054-9681-a828f60fb30b`) lines 331-340 [crates/gwiki/src/graph/context.rs:331-340]
  - Signature: `fn graph_context_code_edge(edge: &WikiGraphCodeEdge) -> GraphContextCodeEdge {`
  - Purpose: Indexed function `graph_context_code_edge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:331-340]
- `recommendations` (function) component `recommendations [function]` (`c6d13b57-41a9-5bc9-80b8-7c9136cba20d`) lines 342-390 [crates/gwiki/src/graph/context.rs:342-390]
  - Signature: `fn recommendations(`
  - Purpose: Indexed function `recommendations` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:342-390]
- `display_path` (function) component `display_path [function]` (`44fb0018-7548-564f-8e8b-15854ccf489e`) lines 392-394 [crates/gwiki/src/graph/context.rs:392-394]
  - Signature: `fn display_path(path: &Path) -> String {`
  - Purpose: Indexed function `display_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:392-394]
- `graph_context_json_includes_neighborhoods_and_empty_code_edges` (function) component `graph_context_json_includes_neighborhoods_and_empty_code_edges [function]` (`2a674ccf-433f-591a-b751-8bba0c39eddc`) lines 407-502 [crates/gwiki/src/graph/context.rs:407-502]
  - Signature: `fn graph_context_json_includes_neighborhoods_and_empty_code_edges() {`
  - Purpose: Indexed function `graph_context_json_includes_neighborhoods_and_empty_code_edges` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:407-502]
- `graph_context_json_reports_truncated_shared_code_as_capped_data` (function) component `graph_context_json_reports_truncated_shared_code_as_capped_data [function]` (`4c042788-2347-572d-84c9-86c85fbc31fb`) lines 505-557 [crates/gwiki/src/graph/context.rs:505-557]
  - Signature: `fn graph_context_json_reports_truncated_shared_code_as_capped_data() {`
  - Purpose: Indexed function `graph_context_json_reports_truncated_shared_code_as_capped_data` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:505-557]
- `ask_unified_graph_context_merges_wiki_and_code_edges` (function) component `ask_unified_graph_context_merges_wiki_and_code_edges [function]` (`e9bbaf7b-c48c-5cc3-8300-7804712fd68a`) lines 560-654 [crates/gwiki/src/graph/context.rs:560-654]
  - Signature: `fn ask_unified_graph_context_merges_wiki_and_code_edges() {`
  - Purpose: Indexed function `ask_unified_graph_context_merges_wiki_and_code_edges` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:560-654]
- `doc` (function) component `doc [function]` (`1fe41e41-9221-5863-8ebe-e33434d242ab`) lines 656-662 [crates/gwiki/src/graph/context.rs:656-662]
  - Signature: `fn doc(scope: SearchScope, path: &str, title: Option<&str>) -> WikiGraphDocument {`
  - Purpose: Indexed function `doc` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:656-662]
- `source` (function) component `source [function]` (`a344636d-27a7-584c-a4f8-657e8830da01`) lines 664-670 [crates/gwiki/src/graph/context.rs:664-670]
  - Signature: `fn source(scope: SearchScope, source_path: &str, document_path: &str) -> WikiGraphSource {`
  - Purpose: Indexed function `source` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:664-670]
- `resolved_link` (function) component `resolved_link [function]` (`86eae7bb-ed54-5a36-9f34-dfe81a217197`) lines 672-684 [crates/gwiki/src/graph/context.rs:672-684]
  - Signature: `fn resolved_link(`
  - Purpose: Indexed function `resolved_link` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:672-684]
- `unresolved_link` (function) component `unresolved_link [function]` (`c40a8ac3-c381-53ee-9768-4a1a61f3b35a`) lines 686-693 [crates/gwiki/src/graph/context.rs:686-693]
  - Signature: `fn unresolved_link(scope: SearchScope, source_path: &str, raw_target: &str) -> WikiGraphLink {`
  - Purpose: Indexed function `unresolved_link` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:686-693]
- `code_edge` (function) component `code_edge [function]` (`cc789d4c-c904-5cba-8d63-b5b3aae6fe21`) lines 695-714 [crates/gwiki/src/graph/context.rs:695-714]
  - Signature: `fn code_edge(`
  - Purpose: Indexed function `code_edge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:695-714]

