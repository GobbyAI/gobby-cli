---
title: crates/gcode/src/commands/codewiki/render.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-33
  - 35-67
  - 69-83
  - 85-108
  - 110-198
  - 200-229
  - 231-281
  - 283-296
  - 298-308
  - 310-325
  - 327-375
  - 377-405
  - 407-433
  - 435-471
  - 473-501
  - 503-545
  - 547-606
  - 608-646
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/render.rs` exposes 18 indexed API symbols.
[crates/gcode/src/commands/codewiki/render.rs:5-33] [crates/gcode/src/commands/codewiki/render.rs:35-67] [crates/gcode/src/commands/codewiki/render.rs:69-83] [crates/gcode/src/commands/codewiki/render.rs:85-108]
[crates/gcode/src/commands/codewiki/render.rs:110-198] [crates/gcode/src/commands/codewiki/render.rs:200-229] [crates/gcode/src/commands/codewiki/render.rs:231-281] [crates/gcode/src/commands/codewiki/render.rs:283-296]
[crates/gcode/src/commands/codewiki/render.rs:298-308] [crates/gcode/src/commands/codewiki/render.rs:310-325] [crates/gcode/src/commands/codewiki/render.rs:327-375] [crates/gcode/src/commands/codewiki/render.rs:377-405]
[crates/gcode/src/commands/codewiki/render.rs:407-433] [crates/gcode/src/commands/codewiki/render.rs:435-471] [crates/gcode/src/commands/codewiki/render.rs:473-501] [crates/gcode/src/commands/codewiki/render.rs:503-545]
[crates/gcode/src/commands/codewiki/render.rs:547-606] [crates/gcode/src/commands/codewiki/render.rs:608-646]

## API Symbols

- `render_module_dependency_mermaid` (function) component `render_module_dependency_mermaid [function]` (`b7b35534-a8ba-5c4b-a97d-2c70814ae8bd`) lines 5-33 [crates/gcode/src/commands/codewiki/render.rs:5-33]
  - Signature: `pub(crate) fn render_module_dependency_mermaid(`
  - Purpose: Indexed function `render_module_dependency_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:5-33]
- `render_architecture_dependency_mermaid` (function) component `render_architecture_dependency_mermaid [function]` (`838dfd5f-c9ac-5214-846b-f6bd9cb1e54a`) lines 35-67 [crates/gcode/src/commands/codewiki/render.rs:35-67]
  - Signature: `pub(crate) fn render_architecture_dependency_mermaid(`
  - Purpose: Indexed function `render_architecture_dependency_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:35-67]
- `repo_mermaid_seed_modules` (function) component `repo_mermaid_seed_modules [function]` (`981b3e96-566a-5c60-930f-493f9de8bbe8`) lines 69-83 [crates/gcode/src/commands/codewiki/render.rs:69-83]
  - Signature: `fn repo_mermaid_seed_modules(edges: &BTreeSet<(String, String)>) -> BTreeSet<String> {`
  - Purpose: Indexed function `repo_mermaid_seed_modules` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:69-83]
- `collect_import_module_edges` (function) component `collect_import_module_edges [function]` (`ed9c2fd0-a610-5f3a-afd8-3827206f1e06`) lines 85-108 [crates/gcode/src/commands/codewiki/render.rs:85-108]
  - Signature: `fn collect_import_module_edges(`
  - Purpose: Indexed function `collect_import_module_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:85-108]
- `render_module_call_mermaid` (function) component `render_module_call_mermaid [function]` (`c2042344-0373-58bd-adb2-9e2623eaa652`) lines 110-198 [crates/gcode/src/commands/codewiki/render.rs:110-198]
  - Signature: `pub(crate) fn render_module_call_mermaid(`
  - Purpose: Indexed function `render_module_call_mermaid` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:110-198]
- `bounded_module_dependency_edges` (function) component `bounded_module_dependency_edges [function]` (`a6e1f308-eade-51eb-9869-248fac1b8dde`) lines 200-229 [crates/gcode/src/commands/codewiki/render.rs:200-229]
  - Signature: `pub(crate) fn bounded_module_dependency_edges(`
  - Purpose: Indexed function `bounded_module_dependency_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:200-229]
- `bounded_component_edges` (function) component `bounded_component_edges [function]` (`eabba8b1-1928-5986-bb71-2caa6b0375e6`) lines 231-281 [crates/gcode/src/commands/codewiki/render.rs:231-281]
  - Signature: `pub(crate) fn bounded_component_edges(`
  - Purpose: Indexed function `bounded_component_edges` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:231-281]
- `dependency_neighbors` (function) component `dependency_neighbors [function]` (`67f904ce-e09a-5c42-a79d-103cf4d5405f`) lines 283-296 [crates/gcode/src/commands/codewiki/render.rs:283-296]
  - Signature: `pub(crate) fn dependency_neighbors<'a>(`
  - Purpose: Indexed function `dependency_neighbors` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:283-296]
- `mermaid_node_id` (function) component `mermaid_node_id [function]` (`98ac6b3b-aa18-582c-a4af-d949abec6296`) lines 298-308 [crates/gcode/src/commands/codewiki/render.rs:298-308]
  - Signature: `pub(crate) fn mermaid_node_id(module: &str) -> String {`
  - Purpose: Indexed function `mermaid_node_id` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:298-308]
- `mermaid_label` (function) component `mermaid_label [function]` (`4e13e14a-df53-52a7-81b2-70a3c0a92a84`) lines 310-325 [crates/gcode/src/commands/codewiki/render.rs:310-325]
  - Signature: `pub(crate) fn mermaid_label(module: &str) -> String {`
  - Purpose: Indexed function `mermaid_label` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:310-325]
- `build_repo_doc` (function) component `build_repo_doc [function]` (`93c90c64-d9e2-5a16-97b7-d07c84b8292c`) lines 327-375 [crates/gcode/src/commands/codewiki/render.rs:327-375]
  - Signature: `pub(crate) fn build_repo_doc(`
  - Purpose: Indexed function `build_repo_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:327-375]
- `render_repo_doc` (function) component `render_repo_doc [function]` (`672d2c89-f629-5a6c-85ed-13b27b8d583e`) lines 377-405 [crates/gcode/src/commands/codewiki/render.rs:377-405]
  - Signature: `pub(crate) fn render_repo_doc(`
  - Purpose: Indexed function `render_repo_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:377-405]
- `render_architecture_doc` (function) component `render_architecture_doc [function]` (`1aa7d949-cfcc-5f2e-b5f5-ba2f5feb45c3`) lines 407-433 [crates/gcode/src/commands/codewiki/render.rs:407-433]
  - Signature: `pub(crate) fn render_architecture_doc(architecture: &ArchitectureDoc) -> String {`
  - Purpose: Indexed function `render_architecture_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:407-433]
- `render_onboarding_doc` (function) component `render_onboarding_doc [function]` (`d4236b41-943c-5175-862e-382972d09ec6`) lines 435-471 [crates/gcode/src/commands/codewiki/render.rs:435-471]
  - Signature: `pub(crate) fn render_onboarding_doc(onboarding: &OnboardingDoc) -> String {`
  - Purpose: Indexed function `render_onboarding_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:435-471]
- `render_hotspots_doc` (function) component `render_hotspots_doc [function]` (`c34f0e42-9b1d-5dad-ab4f-561147f244e9`) lines 473-501 [crates/gcode/src/commands/codewiki/render.rs:473-501]
  - Signature: `pub(crate) fn render_hotspots_doc(hotspots: &HotspotsDoc) -> String {`
  - Purpose: Indexed function `render_hotspots_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:473-501]
- `write_hotspot_section` (function) component `write_hotspot_section [function]` (`36a527eb-06db-529a-baf9-228e5334b93a`) lines 503-545 [crates/gcode/src/commands/codewiki/render.rs:503-545]
  - Signature: `fn write_hotspot_section(doc: &mut String, title: &str, findings: &[HotspotFinding]) {`
  - Purpose: Indexed function `write_hotspot_section` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:503-545]
- `render_module_doc` (function) component `render_module_doc [function]` (`1858c9e0-58f4-501e-9b91-4ec1a1b1efc1`) lines 547-606 [crates/gcode/src/commands/codewiki/render.rs:547-606]
  - Signature: `pub(crate) fn render_module_doc(module: &ModuleDoc) -> String {`
  - Purpose: Indexed function `render_module_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:547-606]
- `render_file_doc` (function) component `render_file_doc [function]` (`0c834adf-79e6-5082-8a1c-11d8b00b9d44`) lines 608-646 [crates/gcode/src/commands/codewiki/render.rs:608-646]
  - Signature: `pub(crate) fn render_file_doc(file: &FileDoc) -> String {`
  - Purpose: Indexed function `render_file_doc` in `crates/gcode/src/commands/codewiki/render.rs`. [crates/gcode/src/commands/codewiki/render.rs:608-646]

