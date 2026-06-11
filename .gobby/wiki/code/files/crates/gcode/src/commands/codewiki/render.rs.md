---
title: crates/gcode/src/commands/codewiki/render.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-35
  - 37-71
  - 73-87
  - 89-112
  - 114-121
  - 123-211
  - 213-242
  - 244-294
  - 296-309
  - 311-321
  - 323-338
  - 340-410
  - 412-446
  - 448-474
  - 476-512
  - 514-557
  - 559-561
  - 563-622
  - 625-631
  - 633-697
  - 699-742
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/render.rs` exposes 21 indexed API symbols.
[crates/gcode/src/commands/codewiki/render.rs:5-35]
[crates/gcode/src/commands/codewiki/render.rs:37-71]
[crates/gcode/src/commands/codewiki/render.rs:73-87]
[crates/gcode/src/commands/codewiki/render.rs:89-112]
[crates/gcode/src/commands/codewiki/render.rs:114-121]

## API Symbols

- `render_module_dependency_mermaid` (function) component `render_module_dependency_mermaid [function]` (`b7b35534-a8ba-5c4b-a97d-2c70814ae8bd`) lines 5-35 [crates/gcode/src/commands/codewiki/render.rs:5-35]
  - Signature: `pub(crate) fn render_module_dependency_mermaid(`
  - Purpose: Indexed function `render_module_dependency_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:5-35]
- `render_architecture_dependency_mermaid` (function) component `render_architecture_dependency_mermaid [function]` (`f01dacd0-759a-57d4-af1a-ba8425a39ab8`) lines 37-71 [crates/gcode/src/commands/codewiki/render.rs:37-71]
  - Signature: `pub(crate) fn render_architecture_dependency_mermaid(`
  - Purpose: Indexed function `render_architecture_dependency_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:37-71]
- `repo_mermaid_seed_modules` (function) component `repo_mermaid_seed_modules [function]` (`35a8f69a-945d-5b9f-abe4-a2c43f26a889`) lines 73-87 [crates/gcode/src/commands/codewiki/render.rs:73-87]
  - Signature: `fn repo_mermaid_seed_modules(edges: &BTreeSet<(String, String)>) -> BTreeSet<String> {`
  - Purpose: Indexed function `repo_mermaid_seed_modules` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:73-87]
- `collect_import_module_edges` (function) component `collect_import_module_edges [function]` (`5001a88d-9d21-58e6-9d0a-e4ec4f234375`) lines 89-112 [crates/gcode/src/commands/codewiki/render.rs:89-112]
  - Signature: `fn collect_import_module_edges(`
  - Purpose: Indexed function `collect_import_module_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:89-112]
- `write_partial_import_graph_comment` (function) component `write_partial_import_graph_comment [function]` (`0573641e-bc7d-5668-a21f-7d180b53a6be`) lines 114-121 [crates/gcode/src/commands/codewiki/render.rs:114-121]
  - Signature: `fn write_partial_import_graph_comment(diagram: &mut String, omitted_edges: usize) {`
  - Purpose: Indexed function `write_partial_import_graph_comment` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:114-121]
- `render_module_call_mermaid` (function) component `render_module_call_mermaid [function]` (`98788570-6558-5d0b-8776-0550d11ef9b2`) lines 123-211 [crates/gcode/src/commands/codewiki/render.rs:123-211]
  - Signature: `pub(crate) fn render_module_call_mermaid(`
  - Purpose: Indexed function `render_module_call_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:123-211]
- `bounded_module_dependency_edges` (function) component `bounded_module_dependency_edges [function]` (`1aa33a46-a03c-5222-8d23-5be1393b2ad1`) lines 213-242 [crates/gcode/src/commands/codewiki/render.rs:213-242]
  - Signature: `pub(crate) fn bounded_module_dependency_edges(`
  - Purpose: Indexed function `bounded_module_dependency_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:213-242]
- `bounded_component_edges` (function) component `bounded_component_edges [function]` (`d2001392-7d38-5840-96e5-8541ca4f71fd`) lines 244-294 [crates/gcode/src/commands/codewiki/render.rs:244-294]
  - Signature: `pub(crate) fn bounded_component_edges(`
  - Purpose: Indexed function `bounded_component_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:244-294]
- `dependency_neighbors` (function) component `dependency_neighbors [function]` (`18207b0a-bc23-53ec-9eab-5a0574ffdea1`) lines 296-309 [crates/gcode/src/commands/codewiki/render.rs:296-309]
  - Signature: `pub(crate) fn dependency_neighbors<'a>(`
  - Purpose: Indexed function `dependency_neighbors` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:296-309]
- `mermaid_node_id` (function) component `mermaid_node_id [function]` (`522deb7c-b9d8-56d9-b250-15a62d7e116e`) lines 311-321 [crates/gcode/src/commands/codewiki/render.rs:311-321]
  - Signature: `pub(crate) fn mermaid_node_id(module: &str) -> String {`
  - Purpose: Indexed function `mermaid_node_id` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:311-321]
- `mermaid_label` (function) component `mermaid_label [function]` (`3b6bb0e5-2666-54e5-82c7-69818b1ab9b9`) lines 323-338 [crates/gcode/src/commands/codewiki/render.rs:323-338]
  - Signature: `pub(crate) fn mermaid_label(module: &str) -> String {`
  - Purpose: Indexed function `mermaid_label` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:323-338]
- `build_repo_doc` (function) component `build_repo_doc [function]` (`ec73f37c-6b87-5bca-8444-c27fa612fcf9`) lines 340-410 [crates/gcode/src/commands/codewiki/render.rs:340-410]
  - Signature: `pub(crate) fn build_repo_doc(`
  - Purpose: Indexed function `build_repo_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:340-410]
- `render_repo_doc` (function) component `render_repo_doc [function]` (`7477fd1e-0d0b-59f0-bf94-f68470575d0c`) lines 412-446 [crates/gcode/src/commands/codewiki/render.rs:412-446]
  - Signature: `pub(crate) fn render_repo_doc(`
  - Purpose: Indexed function `render_repo_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:412-446]
- `render_architecture_doc` (function) component `render_architecture_doc [function]` (`e82f70ce-4d96-5db8-8646-04d2c5164faa`) lines 448-474 [crates/gcode/src/commands/codewiki/render.rs:448-474]
  - Signature: `pub(crate) fn render_architecture_doc(architecture: &ArchitectureDoc) -> String {`
  - Purpose: Indexed function `render_architecture_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:448-474]
- `render_onboarding_doc` (function) component `render_onboarding_doc [function]` (`22109196-3b67-5b13-89cc-9e6859a82a3a`) lines 476-512 [crates/gcode/src/commands/codewiki/render.rs:476-512]
  - Signature: `pub(crate) fn render_onboarding_doc(onboarding: &OnboardingDoc) -> String {`
  - Purpose: Indexed function `render_onboarding_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:476-512]
- `render_hotspots_doc` (function) component `render_hotspots_doc [function]` (`74487b38-9883-56e2-acc1-0942ddfa2fb8`) lines 514-557 [crates/gcode/src/commands/codewiki/render.rs:514-557]
  - Signature: `pub(crate) fn render_hotspots_doc(hotspots: &HotspotsDoc) -> String {`
  - Purpose: Indexed function `render_hotspots_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:514-557]
- `write_hotspot_section` (function) component `write_hotspot_section [function]` (`fc28d2df-5f0b-5a47-a2a1-3a6e9df3478e`) lines 559-561 [crates/gcode/src/commands/codewiki/render.rs:559-561]
  - Signature: `fn write_hotspot_section(doc: &mut String, title: &str, findings: &[HotspotFinding]) {`
  - Purpose: Indexed function `write_hotspot_section` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:559-561]
- `write_hotspot_section_with_cross_refs` (function) component `write_hotspot_section_with_cross_refs [function]` (`2177a5e9-cb82-577e-961f-d4f857e295a5`) lines 563-622 [crates/gcode/src/commands/codewiki/render.rs:563-622]
  - Signature: `fn write_hotspot_section_with_cross_refs(`
  - Purpose: Indexed function `write_hotspot_section_with_cross_refs` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:563-622]
- `model_degraded_sources` (function) component `model_degraded_sources [function]` (`3fc8e84a-e67d-510a-9130-398c2609cb21`) lines 625-631 [crates/gcode/src/commands/codewiki/render.rs:625-631]
  - Signature: `pub(crate) fn model_degraded_sources(degraded: bool) -> Vec<String> {`
  - Purpose: Indexed function `model_degraded_sources` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:625-631]
- `render_module_doc` (function) component `render_module_doc [function]` (`533750d8-0d81-5f11-bf13-6a8c212eef94`) lines 633-697 [crates/gcode/src/commands/codewiki/render.rs:633-697]
  - Signature: `pub(crate) fn render_module_doc(module: &ModuleDoc) -> String {`
  - Purpose: Indexed function `render_module_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:633-697]
- `render_file_doc` (function) component `render_file_doc [function]` (`aa70b8b6-ef5e-5352-973e-94f8b2a9b7c8`) lines 699-742 [crates/gcode/src/commands/codewiki/render.rs:699-742]
  - Signature: `pub(crate) fn render_file_doc(file: &FileDoc) -> String {`
  - Purpose: Indexed function `render_file_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:699-742]

