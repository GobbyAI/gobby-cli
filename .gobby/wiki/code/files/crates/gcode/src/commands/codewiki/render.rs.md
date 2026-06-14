---
title: crates/gcode/src/commands/codewiki/render.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-60
  - 65-85
  - 90-120
  - 124-151
  - 153-176
  - 178-185
  - 187-277
  - 279-308
  - 310-360
  - 362-375
  - 377-387
  - 389-404
  - 406-492
  - 497-517
  - 519-568
  - 570-604
  - 606-642
  - 644-687
  - 689-691
  - 693-752
  - 755-761
  - 763-827
  - 829-872
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file renders various forms of code documentation and dependency visualizations for a code wiki system. It generates Mermaid diagrams for module and subsystem dependencies, call graphs, and comprehensive documentation pages covering repository structure, architecture, onboarding guides, and code hotspots. The functions work together by: collecting and filtering dependency edges from code graph data (collect_import_module_edges, collect_subsystem_dependency_edges), aggregating modules for relevant page contexts (aggregate_module_for_page), bounding edge counts to manageable sizes (bounded_module_dependency_edges, bounded_component_edges), formatting these edges as Mermaid diagram syntax with proper node IDs and labels (mermaid_node_id, mermaid_label), and finally rendering complete documentation pages that combine these diagrams with extracted source excerpts and cross-referenced analysis (render_repo_doc, render_module_doc, render_file_doc, and specialized doc generators). The rendering functions apply different aggregation and filtering strategies depending on diagram type and context to balance comprehensiveness with readability.
[crates/gcode/src/commands/codewiki/render.rs:5-60]
[crates/gcode/src/commands/codewiki/render.rs:65-85]
[crates/gcode/src/commands/codewiki/render.rs:90-120]
[crates/gcode/src/commands/codewiki/render.rs:124-151]
[crates/gcode/src/commands/codewiki/render.rs:153-176]

## API Symbols

- `render_module_dependency_mermaid` (function) component `render_module_dependency_mermaid [function]` (`b7b35534-a8ba-5c4b-a97d-2c70814ae8bd`) lines 5-60 [crates/gcode/src/commands/codewiki/render.rs:5-60]
  - Signature: `pub(crate) fn render_module_dependency_mermaid(`
  - Purpose: Indexed function `render_module_dependency_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:5-60]
- `aggregate_module_for_page` (function) component `aggregate_module_for_page [function]` (`b759f847-9559-5f01-9f33-80abffa8cdf5`) lines 65-85 [crates/gcode/src/commands/codewiki/render.rs:65-85]
  - Signature: `pub(crate) fn aggregate_module_for_page(page: &str, module: &str) -> String {`
  - Purpose: Indexed function `aggregate_module_for_page` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:65-85]
- `render_subsystem_dependency_mermaid` (function) component `render_subsystem_dependency_mermaid [function]` (`4282bdf2-f04c-5639-9623-bcb694df654d`) lines 90-120 [crates/gcode/src/commands/codewiki/render.rs:90-120]
  - Signature: `pub(crate) fn render_subsystem_dependency_mermaid(`
  - Purpose: Indexed function `render_subsystem_dependency_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:90-120]
- `collect_subsystem_dependency_edges` (function) component `collect_subsystem_dependency_edges [function]` (`c5156a57-fdf0-5cf7-83da-bc37dcaaa118`) lines 124-151 [crates/gcode/src/commands/codewiki/render.rs:124-151]
  - Signature: `pub(crate) fn collect_subsystem_dependency_edges(`
  - Purpose: Indexed function `collect_subsystem_dependency_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:124-151]
- `collect_import_module_edges` (function) component `collect_import_module_edges [function]` (`8eb318ca-4f87-50d8-bac5-803639140ff6`) lines 153-176 [crates/gcode/src/commands/codewiki/render.rs:153-176]
  - Signature: `fn collect_import_module_edges(`
  - Purpose: Indexed function `collect_import_module_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:153-176]
- `write_partial_import_graph_comment` (function) component `write_partial_import_graph_comment [function]` (`eb5f66c4-b93c-5dfa-a323-7a0a5d8d09fb`) lines 178-185 [crates/gcode/src/commands/codewiki/render.rs:178-185]
  - Signature: `fn write_partial_import_graph_comment(diagram: &mut String, omitted_edges: usize) {`
  - Purpose: Indexed function `write_partial_import_graph_comment` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:178-185]
- `render_module_call_mermaid` (function) component `render_module_call_mermaid [function]` (`7bdfe3c1-3ab9-52f2-a7be-9cc05ff2f22b`) lines 187-277 [crates/gcode/src/commands/codewiki/render.rs:187-277]
  - Signature: `pub(crate) fn render_module_call_mermaid(`
  - Purpose: Indexed function `render_module_call_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:187-277]
- `bounded_module_dependency_edges` (function) component `bounded_module_dependency_edges [function]` (`211d3808-d9f7-5f6c-a20b-61786257aa92`) lines 279-308 [crates/gcode/src/commands/codewiki/render.rs:279-308]
  - Signature: `pub(crate) fn bounded_module_dependency_edges(`
  - Purpose: Indexed function `bounded_module_dependency_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:279-308]
- `bounded_component_edges` (function) component `bounded_component_edges [function]` (`8bd3aa34-88e5-5433-a693-ee1be68cc644`) lines 310-360 [crates/gcode/src/commands/codewiki/render.rs:310-360]
  - Signature: `pub(crate) fn bounded_component_edges(`
  - Purpose: Indexed function `bounded_component_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:310-360]
- `dependency_neighbors` (function) component `dependency_neighbors [function]` (`12deeef0-dc28-587f-a7ea-99aec86bee8a`) lines 362-375 [crates/gcode/src/commands/codewiki/render.rs:362-375]
  - Signature: `pub(crate) fn dependency_neighbors<'a>(`
  - Purpose: Indexed function `dependency_neighbors` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:362-375]
- `mermaid_node_id` (function) component `mermaid_node_id [function]` (`e37426f1-2bad-590f-a070-378937b643a7`) lines 377-387 [crates/gcode/src/commands/codewiki/render.rs:377-387]
  - Signature: `pub(crate) fn mermaid_node_id(module: &str) -> String {`
  - Purpose: Indexed function `mermaid_node_id` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:377-387]
- `mermaid_label` (function) component `mermaid_label [function]` (`5a33f4cc-a919-5f7b-90e0-9859b24a1ab9`) lines 389-404 [crates/gcode/src/commands/codewiki/render.rs:389-404]
  - Signature: `pub(crate) fn mermaid_label(module: &str) -> String {`
  - Purpose: Indexed function `mermaid_label` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:389-404]
- `build_repo_doc` (function) component `build_repo_doc [function]` (`9c0764be-a2df-5e3a-9fcb-4f1650d1d2c7`) lines 406-492 [crates/gcode/src/commands/codewiki/render.rs:406-492]
  - Signature: `pub(crate) fn build_repo_doc(`
  - Purpose: Indexed function `build_repo_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:406-492]
- `repo_source_excerpts` (function) component `repo_source_excerpts [function]` (`81bae339-1a71-5969-a8ff-9e393ed3ff51`) lines 497-517 [crates/gcode/src/commands/codewiki/render.rs:497-517]
  - Signature: `fn repo_source_excerpts(`
  - Purpose: Indexed function `repo_source_excerpts` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:497-517]
- `render_repo_doc` (function) component `render_repo_doc [function]` (`4da76d87-734b-5018-8fbf-27937a3b231d`) lines 519-568 [crates/gcode/src/commands/codewiki/render.rs:519-568]
  - Signature: `pub(crate) fn render_repo_doc(`
  - Purpose: Indexed function `render_repo_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:519-568]
- `render_architecture_doc` (function) component `render_architecture_doc [function]` (`533a1b1f-4ea0-54bd-8cde-a9ff85424ed7`) lines 570-604 [crates/gcode/src/commands/codewiki/render.rs:570-604]
  - Signature: `pub(crate) fn render_architecture_doc(architecture: &ArchitectureDoc) -> String {`
  - Purpose: Indexed function `render_architecture_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:570-604]
- `render_onboarding_doc` (function) component `render_onboarding_doc [function]` (`ea44d5ac-d6a6-5f72-91f0-105a60f97dde`) lines 606-642 [crates/gcode/src/commands/codewiki/render.rs:606-642]
  - Signature: `pub(crate) fn render_onboarding_doc(onboarding: &OnboardingDoc) -> String {`
  - Purpose: Indexed function `render_onboarding_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:606-642]
- `render_hotspots_doc` (function) component `render_hotspots_doc [function]` (`1682064a-d77e-5fe5-83a6-f98ae8223308`) lines 644-687 [crates/gcode/src/commands/codewiki/render.rs:644-687]
  - Signature: `pub(crate) fn render_hotspots_doc(hotspots: &HotspotsDoc) -> String {`
  - Purpose: Indexed function `render_hotspots_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:644-687]
- `write_hotspot_section` (function) component `write_hotspot_section [function]` (`7956b170-5fdf-53d6-a346-4e145348c943`) lines 689-691 [crates/gcode/src/commands/codewiki/render.rs:689-691]
  - Signature: `fn write_hotspot_section(doc: &mut String, title: &str, findings: &[HotspotFinding]) {`
  - Purpose: Indexed function `write_hotspot_section` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:689-691]
- `write_hotspot_section_with_cross_refs` (function) component `write_hotspot_section_with_cross_refs [function]` (`19b093ab-6a44-5d93-b901-6bba04a9cffc`) lines 693-752 [crates/gcode/src/commands/codewiki/render.rs:693-752]
  - Signature: `fn write_hotspot_section_with_cross_refs(`
  - Purpose: Indexed function `write_hotspot_section_with_cross_refs` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:693-752]
- `model_degraded_sources` (function) component `model_degraded_sources [function]` (`77486849-9a8c-52bf-86ba-865da53e0b74`) lines 755-761 [crates/gcode/src/commands/codewiki/render.rs:755-761]
  - Signature: `pub(crate) fn model_degraded_sources(degraded: bool) -> Vec<String> {`
  - Purpose: Indexed function `model_degraded_sources` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:755-761]
- `render_module_doc` (function) component `render_module_doc [function]` (`06031d7b-3b13-58a4-909d-07b21071ee19`) lines 763-827 [crates/gcode/src/commands/codewiki/render.rs:763-827]
  - Signature: `pub(crate) fn render_module_doc(module: &ModuleDoc) -> String {`
  - Purpose: Indexed function `render_module_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:763-827]
- `render_file_doc` (function) component `render_file_doc [function]` (`ceac175d-6fb9-5d09-ba71-8fb1d017c69d`) lines 829-872 [crates/gcode/src/commands/codewiki/render.rs:829-872]
  - Signature: `pub(crate) fn render_file_doc(file: &FileDoc) -> String {`
  - Purpose: Indexed function `render_file_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:829-872]

