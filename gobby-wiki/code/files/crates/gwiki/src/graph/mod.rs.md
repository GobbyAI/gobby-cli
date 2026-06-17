---
title: crates/gwiki/src/graph/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/mod.rs
  ranges:
  - 22-26
  - 29-33
  - 36-39
  - 42-47
  - 50-59
  - 62-67
  - 70-72
  - 75-77
  - 79-81
  - 85-92
  - 95-103
  - 106-113
  - 116-122
  - 125-127
  - 130-135
  - 138-143
  - 146-148
  - 151-155
  - 158-239
  - 242-244
  - 247-249
  - 252-254
  - 256-290
  - 292-334
  - 336-343
  - 345-405
  - 407-413
  - 416-418
  - 420-422
  - 424-426
  - 428-430
  - 432-440
  - 442-449
  - 451-453
  - 455-464
  - 466-475
  - 477-486
  - 488-497
  - 499-501
  - 503-505
  - 507-513
  - 515-517
  - 519-521
  - 523-532
  - 534-554
  - 556-565
  - 567-593
  - 595-599
  - 601-606
  - 613-679
  - 682-715
  - 718-725
  - 728-771
  - 774-817
  - 820-862
  - 864-870
  - 872-884
  - 886-893
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/graph/mod.rs:22-26](crates/gwiki/src/graph/mod.rs#L22-L26), [crates/gwiki/src/graph/mod.rs:29-33](crates/gwiki/src/graph/mod.rs#L29-L33), [crates/gwiki/src/graph/mod.rs:36-39](crates/gwiki/src/graph/mod.rs#L36-L39), [crates/gwiki/src/graph/mod.rs:42-47](crates/gwiki/src/graph/mod.rs#L42-L47), [crates/gwiki/src/graph/mod.rs:50-59](crates/gwiki/src/graph/mod.rs#L50-L59), [crates/gwiki/src/graph/mod.rs:62-67](crates/gwiki/src/graph/mod.rs#L62-L67), [crates/gwiki/src/graph/mod.rs:70-72](crates/gwiki/src/graph/mod.rs#L70-L72), [crates/gwiki/src/graph/mod.rs:75-77](crates/gwiki/src/graph/mod.rs#L75-L77), [crates/gwiki/src/graph/mod.rs:79-81](crates/gwiki/src/graph/mod.rs#L79-L81), [crates/gwiki/src/graph/mod.rs:85-92](crates/gwiki/src/graph/mod.rs#L85-L92), [crates/gwiki/src/graph/mod.rs:95-103](crates/gwiki/src/graph/mod.rs#L95-L103), [crates/gwiki/src/graph/mod.rs:106-113](crates/gwiki/src/graph/mod.rs#L106-L113), [crates/gwiki/src/graph/mod.rs:116-122](crates/gwiki/src/graph/mod.rs#L116-L122), [crates/gwiki/src/graph/mod.rs:125-127](crates/gwiki/src/graph/mod.rs#L125-L127), [crates/gwiki/src/graph/mod.rs:130-135](crates/gwiki/src/graph/mod.rs#L130-L135), [crates/gwiki/src/graph/mod.rs:138-143](crates/gwiki/src/graph/mod.rs#L138-L143), [crates/gwiki/src/graph/mod.rs:146-148](crates/gwiki/src/graph/mod.rs#L146-L148), [crates/gwiki/src/graph/mod.rs:151-155](crates/gwiki/src/graph/mod.rs#L151-L155), [crates/gwiki/src/graph/mod.rs:158-239](crates/gwiki/src/graph/mod.rs#L158-L239), [crates/gwiki/src/graph/mod.rs:242-244](crates/gwiki/src/graph/mod.rs#L242-L244), [crates/gwiki/src/graph/mod.rs:247-249](crates/gwiki/src/graph/mod.rs#L247-L249), [crates/gwiki/src/graph/mod.rs:252-254](crates/gwiki/src/graph/mod.rs#L252-L254), [crates/gwiki/src/graph/mod.rs:256-290](crates/gwiki/src/graph/mod.rs#L256-L290), [crates/gwiki/src/graph/mod.rs:292-334](crates/gwiki/src/graph/mod.rs#L292-L334), [crates/gwiki/src/graph/mod.rs:336-343](crates/gwiki/src/graph/mod.rs#L336-L343), [crates/gwiki/src/graph/mod.rs:345-405](crates/gwiki/src/graph/mod.rs#L345-L405), [crates/gwiki/src/graph/mod.rs:407-413](crates/gwiki/src/graph/mod.rs#L407-L413), [crates/gwiki/src/graph/mod.rs:416-418](crates/gwiki/src/graph/mod.rs#L416-L418), [crates/gwiki/src/graph/mod.rs:420-422](crates/gwiki/src/graph/mod.rs#L420-L422), [crates/gwiki/src/graph/mod.rs:424-426](crates/gwiki/src/graph/mod.rs#L424-L426), [crates/gwiki/src/graph/mod.rs:428-430](crates/gwiki/src/graph/mod.rs#L428-L430), [crates/gwiki/src/graph/mod.rs:432-440](crates/gwiki/src/graph/mod.rs#L432-L440), [crates/gwiki/src/graph/mod.rs:442-449](crates/gwiki/src/graph/mod.rs#L442-L449), [crates/gwiki/src/graph/mod.rs:451-453](crates/gwiki/src/graph/mod.rs#L451-L453), [crates/gwiki/src/graph/mod.rs:455-464](crates/gwiki/src/graph/mod.rs#L455-L464), [crates/gwiki/src/graph/mod.rs:466-475](crates/gwiki/src/graph/mod.rs#L466-L475), [crates/gwiki/src/graph/mod.rs:477-486](crates/gwiki/src/graph/mod.rs#L477-L486), [crates/gwiki/src/graph/mod.rs:488-497](crates/gwiki/src/graph/mod.rs#L488-L497), [crates/gwiki/src/graph/mod.rs:499-501](crates/gwiki/src/graph/mod.rs#L499-L501), [crates/gwiki/src/graph/mod.rs:503-505](crates/gwiki/src/graph/mod.rs#L503-L505), [crates/gwiki/src/graph/mod.rs:507-513](crates/gwiki/src/graph/mod.rs#L507-L513), [crates/gwiki/src/graph/mod.rs:515-517](crates/gwiki/src/graph/mod.rs#L515-L517), [crates/gwiki/src/graph/mod.rs:519-521](crates/gwiki/src/graph/mod.rs#L519-L521), [crates/gwiki/src/graph/mod.rs:523-532](crates/gwiki/src/graph/mod.rs#L523-L532), [crates/gwiki/src/graph/mod.rs:534-554](crates/gwiki/src/graph/mod.rs#L534-L554), [crates/gwiki/src/graph/mod.rs:556-565](crates/gwiki/src/graph/mod.rs#L556-L565), [crates/gwiki/src/graph/mod.rs:567-593](crates/gwiki/src/graph/mod.rs#L567-L593), [crates/gwiki/src/graph/mod.rs:595-599](crates/gwiki/src/graph/mod.rs#L595-L599), [crates/gwiki/src/graph/mod.rs:601-606](crates/gwiki/src/graph/mod.rs#L601-L606), [crates/gwiki/src/graph/mod.rs:613-679](crates/gwiki/src/graph/mod.rs#L613-L679), [crates/gwiki/src/graph/mod.rs:682-715](crates/gwiki/src/graph/mod.rs#L682-L715), [crates/gwiki/src/graph/mod.rs:718-725](crates/gwiki/src/graph/mod.rs#L718-L725), [crates/gwiki/src/graph/mod.rs:728-771](crates/gwiki/src/graph/mod.rs#L728-L771), [crates/gwiki/src/graph/mod.rs:774-817](crates/gwiki/src/graph/mod.rs#L774-L817), [crates/gwiki/src/graph/mod.rs:820-862](crates/gwiki/src/graph/mod.rs#L820-L862), [crates/gwiki/src/graph/mod.rs:864-870](crates/gwiki/src/graph/mod.rs#L864-L870), [crates/gwiki/src/graph/mod.rs:872-884](crates/gwiki/src/graph/mod.rs#L872-L884), [crates/gwiki/src/graph/mod.rs:886-893](crates/gwiki/src/graph/mod.rs#L886-L893)

</details>

# crates/gwiki/src/graph/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the wiki graph domain model and in-memory graph operations for `gwiki`. It introduces the core data types for documents, sources, links, code edges, and aggregate facts, plus `GraphExport`/node/edge wrappers and `GraphExportOptions` for producing exportable graph output. `MemoryWikiGraph` stores and queries those facts to generate backlinks, link suggestions, and related paths, while the helper functions build labels, scoped IDs, node IDs, and Mermaid-friendly names consistently across the export and query logic. The file also re-exports `render_graph_report` from the export module and includes tests that lock down label ownership, missing-document filtering, scoped hashing, and scoring/filtering behavior.
[crates/gwiki/src/graph/mod.rs:22-26]
[crates/gwiki/src/graph/mod.rs:29-33]
[crates/gwiki/src/graph/mod.rs:36-39]
[crates/gwiki/src/graph/mod.rs:42-47]
[crates/gwiki/src/graph/mod.rs:50-59]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WikiGraphDocument` | class | `pub struct WikiGraphDocument {` | `WikiGraphDocument [class]` | `ae3abb0d-9d89-53d0-9f77-bd19629bbd71` | 22-26 [crates/gwiki/src/graph/mod.rs:22-26] | Indexed class `WikiGraphDocument` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:22-26] |
| `WikiGraphSource` | class | `pub struct WikiGraphSource {` | `WikiGraphSource [class]` | `23ac1c98-2c08-572e-b5b7-a14206627c82` | 29-33 [crates/gwiki/src/graph/mod.rs:29-33] | Indexed class `WikiGraphSource` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:29-33] |
| `WikiGraphLinkTarget` | type | `pub enum WikiGraphLinkTarget {` | `WikiGraphLinkTarget [type]` | `fe3f6a2f-b7a2-56c0-b7c9-fe9775f112f0` | 36-39 [crates/gwiki/src/graph/mod.rs:36-39] | Indexed type `WikiGraphLinkTarget` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:36-39] |
| `WikiGraphLink` | class | `pub struct WikiGraphLink {` | `WikiGraphLink [class]` | `6b8d5203-ecb9-5370-9a9c-05284911f23c` | 42-47 [crates/gwiki/src/graph/mod.rs:42-47] | Indexed class `WikiGraphLink` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:42-47] |
| `WikiGraphCodeEdge` | class | `pub struct WikiGraphCodeEdge {` | `WikiGraphCodeEdge [class]` | `98827567-d658-5c0c-b1c9-264af462d85e` | 50-59 [crates/gwiki/src/graph/mod.rs:50-59] | Indexed class `WikiGraphCodeEdge` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:50-59] |
| `WikiGraphFacts` | class | `pub struct WikiGraphFacts {` | `WikiGraphFacts [class]` | `a5370d6c-9459-5382-bdd5-152a94de302e` | 62-67 [crates/gwiki/src/graph/mod.rs:62-67] | Indexed class `WikiGraphFacts` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:62-67] |
| `GraphExportOptions` | class | `pub struct GraphExportOptions {` | `GraphExportOptions [class]` | `e44cdaf1-94de-54c4-9d08-5b270d746a8b` | 70-72 [crates/gwiki/src/graph/mod.rs:70-72] | Indexed class `GraphExportOptions` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:70-72] |
| `GraphExportOptions::available` | method | `pub fn available() -> Self {` | `GraphExportOptions::available [method]` | `2cc9cd06-73db-572c-a36e-eb8ba2c81965` | 75-77 [crates/gwiki/src/graph/mod.rs:75-77] | Indexed method `GraphExportOptions::available` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:75-77] |
| `GraphExportOptions::degraded` | method | `pub fn degraded(degraded_sources: Vec<String>) -> Self {` | `GraphExportOptions::degraded [method]` | `ccd5801a-c85d-5474-801c-b3f54d6bd654` | 79-81 [crates/gwiki/src/graph/mod.rs:79-81] | Indexed method `GraphExportOptions::degraded` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:79-81] |
| `GraphExport` | class | `pub struct GraphExport {` | `GraphExport [class]` | `f0f5a353-0a96-566e-bff2-f5c41eaf0684` | 85-92 [crates/gwiki/src/graph/mod.rs:85-92] | Indexed class `GraphExport` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:85-92] |
| `GraphExportNode` | class | `pub struct GraphExportNode {` | `GraphExportNode [class]` | `22e6ba9d-3a8d-5fb5-b566-4b9d3046aefa` | 95-103 [crates/gwiki/src/graph/mod.rs:95-103] | Indexed class `GraphExportNode` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:95-103] |
| `GraphExportEdges` | class | `pub struct GraphExportEdges {` | `GraphExportEdges [class]` | `08ac016d-d912-5509-a0a9-a85565487bc7` | 106-113 [crates/gwiki/src/graph/mod.rs:106-113] | Indexed class `GraphExportEdges` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:106-113] |
| `GraphExportEdge` | class | `pub struct GraphExportEdge {` | `GraphExportEdge [class]` | `a5ef95bb-bac2-5680-974c-7f7587e82138` | 116-122 [crates/gwiki/src/graph/mod.rs:116-122] | Indexed class `GraphExportEdge` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:116-122] |
| `GraphStatement` | class | `pub struct GraphStatement {` | `GraphStatement [class]` | `b81e41d4-1540-5197-a578-04aff61df132` | 125-127 [crates/gwiki/src/graph/mod.rs:125-127] | Indexed class `GraphStatement` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:125-127] |
| `WikiBacklink` | class | `pub struct WikiBacklink {` | `WikiBacklink [class]` | `3c471dab-f9fe-5d01-95d3-e849ada407f6` | 130-135 [crates/gwiki/src/graph/mod.rs:130-135] | Indexed class `WikiBacklink` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:130-135] |
| `LinkSuggestion` | class | `pub struct LinkSuggestion {` | `LinkSuggestion [class]` | `9d7ae669-dfd8-5790-b926-27175f6077a6` | 138-143 [crates/gwiki/src/graph/mod.rs:138-143] | Indexed class `LinkSuggestion` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:138-143] |
| `RelatedPathOptions` | class | `pub struct RelatedPathOptions {` | `RelatedPathOptions [class]` | `5ef1a36d-9f7f-59e0-87bd-1571c4abd7cb` | 146-148 [crates/gwiki/src/graph/mod.rs:146-148] | Indexed class `RelatedPathOptions` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:146-148] |
| `RelatedPathOptions::default` | method | `fn default() -> Self {` | `RelatedPathOptions::default [method]` | `b103dac5-1f0d-5835-82c6-78550850f358` | 151-155 [crates/gwiki/src/graph/mod.rs:151-155] | Indexed method `RelatedPathOptions::default` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:151-155] |
| `graph_write_statements` | function | `pub fn graph_write_statements(facts: &WikiGraphFacts) -> Vec<GraphStatement> {` | `graph_write_statements [function]` | `e7fb4b80-5bd1-536c-9ed8-18ad5c3b536c` | 158-239 [crates/gwiki/src/graph/mod.rs:158-239] | Indexed function `graph_write_statements` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:158-239] |
| `MemoryWikiGraph` | class | `pub struct MemoryWikiGraph {` | `MemoryWikiGraph [class]` | `0ed3333f-6cb2-5f58-9fc4-1ce345e396c3` | 242-244 [crates/gwiki/src/graph/mod.rs:242-244] | Indexed class `MemoryWikiGraph` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:242-244] |
| `MemoryWikiGraph::replace_facts` | method | `pub fn replace_facts(&mut self, facts: WikiGraphFacts) {` | `MemoryWikiGraph::replace_facts [method]` | `b30def02-4991-528d-b788-f1cef3b98edf` | 247-249 [crates/gwiki/src/graph/mod.rs:247-249] | Indexed method `MemoryWikiGraph::replace_facts` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:247-249] |
| `MemoryWikiGraph::graph_facts_for_tests` | method | `pub(crate) fn graph_facts_for_tests(&self) -> &WikiGraphFacts {` | `MemoryWikiGraph::graph_facts_for_tests [method]` | `d83faf5b-dce0-5a3e-a62a-4a8bf97da070` | 252-254 [crates/gwiki/src/graph/mod.rs:252-254] | Indexed method `MemoryWikiGraph::graph_facts_for_tests` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:252-254] |
| `MemoryWikiGraph::backlinks` | method | `pub fn backlinks(` | `MemoryWikiGraph::backlinks [method]` | `3d858d66-f687-552c-bcaf-7c0de1ed61ed` | 256-290 [crates/gwiki/src/graph/mod.rs:256-290] | Indexed method `MemoryWikiGraph::backlinks` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:256-290] |
| `MemoryWikiGraph::link_suggestions` | method | `pub fn link_suggestions(&self, scope: &SearchScope, limit: usize) -> Vec<LinkSuggestion> {` | `MemoryWikiGraph::link_suggestions [method]` | `fb9fbf25-409d-52c4-a646-ca4240fe89fc` | 292-334 [crates/gwiki/src/graph/mod.rs:292-334] | Indexed method `MemoryWikiGraph::link_suggestions` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:292-334] |
| `MemoryWikiGraph::Accumulator` | class | `struct Accumulator {` | `MemoryWikiGraph::Accumulator [class]` | `34bbc1c2-a884-5aa9-9c57-4fc5db3608a8` | 298-301 [crates/gwiki/src/graph/mod.rs:298-301] | Indexed class `MemoryWikiGraph::Accumulator` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:298-301] |
| `MemoryWikiGraph::related_paths` | method | `pub fn related_paths(` | `MemoryWikiGraph::related_paths [method]` | `87577f54-820d-5073-9fa8-74921f0ec1a2` | 336-343 [crates/gwiki/src/graph/mod.rs:336-343] | Indexed method `MemoryWikiGraph::related_paths` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:336-343] |
| `MemoryWikiGraph::related_paths_with_options` | method | `pub fn related_paths_with_options(` | `MemoryWikiGraph::related_paths_with_options [method]` | `21bb4330-85ee-5c20-b5e2-f5f52c922695` | 345-405 [crates/gwiki/src/graph/mod.rs:345-405] | Indexed method `MemoryWikiGraph::related_paths_with_options` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:345-405] |
| `MemoryWikiGraph::document_keys` | method | `fn document_keys(&self) -> BTreeSet<(SearchScope, PathBuf)> {` | `MemoryWikiGraph::document_keys [method]` | `f2ecf981-f9fe-5b89-ae3c-624c772c387e` | 407-413 [crates/gwiki/src/graph/mod.rs:407-413] | Indexed method `MemoryWikiGraph::document_keys` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:407-413] |
| `label` | function | `fn label(value: &str) -> String {` | `label [function]` | `8ebce724-afcb-555d-ab2c-b44b37028d6d` | 416-418 [crates/gwiki/src/graph/mod.rs:416-418] | Indexed function `label` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:416-418] |
| `rel` | function | `fn rel(value: &str) -> String {` | `rel [function]` | `0c9536ff-594d-5897-b36f-d5a8370c0a07` | 420-422 [crates/gwiki/src/graph/mod.rs:420-422] | Indexed function `rel` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:420-422] |
| `property` | function | `fn property(value: &str) -> String {` | `property [function]` | `384294d3-bfb3-5c56-8294-61a1e0f335e8` | 424-426 [crates/gwiki/src/graph/mod.rs:424-426] | Indexed function `property` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:424-426] |
| `string` | function | `fn string(value: &str) -> String {` | `string [function]` | `6ea5885d-0c8f-5bb0-bbb3-a2b573ee67c8` | 428-430 [crates/gwiki/src/graph/mod.rs:428-430] | Indexed function `string` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:428-430] |
| `scope_properties` | function | `fn scope_properties(scope: &SearchScope) -> String {` | `scope_properties [function]` | `2a80359d-8836-5099-b790-24b620889645` | 432-440 [crates/gwiki/src/graph/mod.rs:432-440] | Indexed function `scope_properties` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:432-440] |
| `scoped_path_properties` | function | `fn scoped_path_properties(scope: &SearchScope, path: &Path) -> String {` | `scoped_path_properties [function]` | `12d8cd19-262d-587e-8cd3-17b2818f3a07` | 442-449 [crates/gwiki/src/graph/mod.rs:442-449] | Indexed function `scoped_path_properties` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:442-449] |
| `graph_path` | function | `fn graph_path(path: &Path) -> String {` | `graph_path [function]` | `1ae31f01-1c99-55c7-af0c-0e0807245c97` | 451-453 [crates/gwiki/src/graph/mod.rs:451-453] | Indexed function `graph_path` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:451-453] |
| `document_node` | function | `fn document_node(document: &WikiGraphDocument) -> GraphExportNode {` | `document_node [function]` | `f47d6394-06c6-5a86-8292-ed612ea5a5f0` | 455-464 [crates/gwiki/src/graph/mod.rs:455-464] | Indexed function `document_node` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:455-464] |
| `source_node` | function | `fn source_node(source: &WikiGraphSource) -> GraphExportNode {` | `source_node [function]` | `b07698c6-990b-55a1-a75a-7739b8dd3f33` | 466-475 [crates/gwiki/src/graph/mod.rs:466-475] | Indexed function `source_node` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:466-475] |
| `citation_node` | function | `fn citation_node(source: &WikiGraphSource) -> GraphExportNode {` | `citation_node [function]` | `631a8fb3-e4b5-5c5d-9788-941aac064976` | 477-486 [crates/gwiki/src/graph/mod.rs:477-486] | Indexed function `citation_node` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:477-486] |
| `unresolved_target_node` | function | `fn unresolved_target_node(scope: &SearchScope, target: &str) -> GraphExportNode {` | `unresolved_target_node [function]` | `24dce42f-d268-57bf-a2fd-b868e9457c5f` | 488-497 [crates/gwiki/src/graph/mod.rs:488-497] | Indexed function `unresolved_target_node` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:488-497] |
| `document_id` | function | `fn document_id(scope: &SearchScope, path: &Path) -> String {` | `document_id [function]` | `3c0afb87-6378-5d56-9459-8fa2b6d22aff` | 499-501 [crates/gwiki/src/graph/mod.rs:499-501] | Indexed function `document_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:499-501] |
| `source_node_id` | function | `fn source_node_id(scope: &SearchScope, path: &Path) -> String {` | `source_node_id [function]` | `8505e829-a76a-53ee-bc0b-508940f9bc39` | 503-505 [crates/gwiki/src/graph/mod.rs:503-505] | Indexed function `source_node_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:503-505] |
| `citation_node_id` | function | `fn citation_node_id(scope: &SearchScope, source_path: &Path, document_path: &Path) -> String {` | `citation_node_id [function]` | `6bee331e-0220-53b2-9bdc-fee7ff6a4983` | 507-513 [crates/gwiki/src/graph/mod.rs:507-513] | Indexed function `citation_node_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:507-513] |
| `unresolved_target_id` | function | `fn unresolved_target_id(scope: &SearchScope, target: &str) -> String {` | `unresolved_target_id [function]` | `3045da76-83ae-5e87-be99-9a644230d5de` | 515-517 [crates/gwiki/src/graph/mod.rs:515-517] | Indexed function `unresolved_target_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:515-517] |
| `code_endpoint_id` | function | `fn code_endpoint_id(scope: &SearchScope, endpoint: &str) -> String {` | `code_endpoint_id [function]` | `974a41df-d9c8-578d-8254-b86b9b623780` | 519-521 [crates/gwiki/src/graph/mod.rs:519-521] | Indexed function `code_endpoint_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:519-521] |
| `scoped_id` | function | `fn scoped_id(scope: &SearchScope, kind: &str, value: &str) -> String {` | `scoped_id [function]` | `550ceffc-d141-565f-9c7f-538e7664f092` | 523-532 [crates/gwiki/src/graph/mod.rs:523-532] | Indexed function `scoped_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:523-532] |
| `readable_id_prefix` | function | `fn readable_id_prefix(value: &str) -> String {` | `readable_id_prefix [function]` | `b0dd8401-9883-5733-9e2d-875c444ff232` | 534-554 [crates/gwiki/src/graph/mod.rs:534-554] | Indexed function `readable_id_prefix` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:534-554] |
| `document_kind` | function | `fn document_kind(path: &Path) -> &'static str {` | `document_kind [function]` | `3b8f3ab9-33d9-56c4-9b70-e8d86d5b83f1` | 556-565 [crates/gwiki/src/graph/mod.rs:556-565] | Indexed function `document_kind` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:556-565] |
| `is_code_path` | function | `fn is_code_path(path: &Path) -> bool {` | `is_code_path [function]` | `3fdfe00d-0f4e-537e-8995-3598676a192e` | 567-593 [crates/gwiki/src/graph/mod.rs:567-593] | Indexed function `is_code_path` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:567-593] |
| `mermaid_node_id` | function | `fn mermaid_node_id(id: &str) -> String {` | `mermaid_node_id [function]` | `c51b8f74-b8a7-536c-b3c6-fc074dbc9bad` | 595-599 [crates/gwiki/src/graph/mod.rs:595-599] | Indexed function `mermaid_node_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:595-599] |
| `mermaid_label` | function | `fn mermaid_label(node: &GraphExportNode) -> String {` | `mermaid_label [function]` | `e5b9d33c-9cd5-5bfd-8cc9-830d118d25d4` | 601-606 [crates/gwiki/src/graph/mod.rs:601-606] | Indexed function `mermaid_label` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:601-606] |
| `graph_labels_are_wiki_owned` | function | `fn graph_labels_are_wiki_owned() {` | `graph_labels_are_wiki_owned [function]` | `ea8b41f6-61d3-5f14-a251-f0fe3fe8ae30` | 613-679 [crates/gwiki/src/graph/mod.rs:613-679] | Indexed function `graph_labels_are_wiki_owned` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:613-679] |
| `graph_write_skips_relationships_to_missing_documents` | function | `fn graph_write_skips_relationships_to_missing_documents() {` | `graph_write_skips_relationships_to_missing_documents [function]` | `ce0fbd0b-2b64-573f-b428-92d87c66590c` | 682-715 [crates/gwiki/src/graph/mod.rs:682-715] | Indexed function `graph_write_skips_relationships_to_missing_documents` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:682-715] |
| `scoped_graph_ids_hash_structured_values` | function | `fn scoped_graph_ids_hash_structured_values() {` | `scoped_graph_ids_hash_structured_values [function]` | `3bb5f40e-4065-5517-a19b-e2221a3834cd` | 718-725 [crates/gwiki/src/graph/mod.rs:718-725] | Indexed function `scoped_graph_ids_hash_structured_values` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:718-725] |
| `backlinks_are_scope_filtered` | function | `fn backlinks_are_scope_filtered() {` | `backlinks_are_scope_filtered [function]` | `c3a548e7-f1ea-521c-903c-698bddf9ed2e` | 728-771 [crates/gwiki/src/graph/mod.rs:728-771] | Indexed function `backlinks_are_scope_filtered` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:728-771] |
| `link_suggest_is_read_only` | function | `fn link_suggest_is_read_only() {` | `link_suggest_is_read_only [function]` | `09b5d54f-729b-5869-a4b0-09277b078d16` | 774-817 [crates/gwiki/src/graph/mod.rs:774-817] | Indexed function `link_suggest_is_read_only` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:774-817] |
| `related_paths_support_weight_options_and_skip_non_finite_scores` | function | `fn related_paths_support_weight_options_and_skip_non_finite_scores() {` | `related_paths_support_weight_options_and_skip_non_finite_scores [function]` | `b10d9cc3-44ac-55cd-b08f-9ace8ccba07b` | 820-862 [crates/gwiki/src/graph/mod.rs:820-862] | Indexed function `related_paths_support_weight_options_and_skip_non_finite_scores` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:820-862] |
| `doc` | function | `fn doc(scope: SearchScope, path: &str) -> WikiGraphDocument {` | `doc [function]` | `37f4fe95-ae89-55cc-b264-f944c92007cc` | 864-870 [crates/gwiki/src/graph/mod.rs:864-870] | Indexed function `doc` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:864-870] |
| `resolved_link` | function | `fn resolved_link(` | `resolved_link [function]` | `8321713e-3c32-5398-9ae2-bf5895be5554` | 872-884 [crates/gwiki/src/graph/mod.rs:872-884] | Indexed function `resolved_link` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:872-884] |
| `unresolved_link` | function | `fn unresolved_link(scope: SearchScope, source_path: &str, target: &str) -> WikiGraphLink {` | `unresolved_link [function]` | `ac5e6d40-2304-507a-ade6-473ed49dede5` | 886-893 [crates/gwiki/src/graph/mod.rs:886-893] | Indexed function `unresolved_link` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:886-893] |
