---
title: crates/gcode/src/commands/codewiki/render/diagrams.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/diagrams.rs
  ranges:
  - 5-67
  - 72-92
  - 97-127
  - 131-166
  - 170-197
  - 199-222
  - 224-231
  - 233-330
  - 332-349
  - 351-380
  - 382-432
  - 434-447
  - 449-459
  - 461-476
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67](crates/gcode/src/commands/codewiki/render/diagrams.rs#L5-L67), [crates/gcode/src/commands/codewiki/render/diagrams.rs:72-92](crates/gcode/src/commands/codewiki/render/diagrams.rs#L72-L92), [crates/gcode/src/commands/codewiki/render/diagrams.rs:97-127](crates/gcode/src/commands/codewiki/render/diagrams.rs#L97-L127), [crates/gcode/src/commands/codewiki/render/diagrams.rs:131-166](crates/gcode/src/commands/codewiki/render/diagrams.rs#L131-L166), [crates/gcode/src/commands/codewiki/render/diagrams.rs:170-197](crates/gcode/src/commands/codewiki/render/diagrams.rs#L170-L197), [crates/gcode/src/commands/codewiki/render/diagrams.rs:199-222](crates/gcode/src/commands/codewiki/render/diagrams.rs#L199-L222), [crates/gcode/src/commands/codewiki/render/diagrams.rs:224-231](crates/gcode/src/commands/codewiki/render/diagrams.rs#L224-L231), [crates/gcode/src/commands/codewiki/render/diagrams.rs:233-330](crates/gcode/src/commands/codewiki/render/diagrams.rs#L233-L330), [crates/gcode/src/commands/codewiki/render/diagrams.rs:332-349](crates/gcode/src/commands/codewiki/render/diagrams.rs#L332-L349), [crates/gcode/src/commands/codewiki/render/diagrams.rs:351-380](crates/gcode/src/commands/codewiki/render/diagrams.rs#L351-L380), [crates/gcode/src/commands/codewiki/render/diagrams.rs:382-432](crates/gcode/src/commands/codewiki/render/diagrams.rs#L382-L432), [crates/gcode/src/commands/codewiki/render/diagrams.rs:434-447](crates/gcode/src/commands/codewiki/render/diagrams.rs#L434-L447), [crates/gcode/src/commands/codewiki/render/diagrams.rs:449-459](crates/gcode/src/commands/codewiki/render/diagrams.rs#L449-L459), [crates/gcode/src/commands/codewiki/render/diagrams.rs:461-476](crates/gcode/src/commands/codewiki/render/diagrams.rs#L461-L476)

</details>

# crates/gcode/src/commands/codewiki/render/diagrams.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Purpose

Builds Mermaid diagrams for the codewiki’s dependency views. It collects import and dependency edges from `FileDoc` and `CodewikiGraphEdge` data, aggregates endpoints relative to the current page/module, and then renders bounded module, subsystem, architecture, and call graphs with truncation notes and partial-graph comments when edges are omitted. Helper functions handle edge collection, neighborhood filtering, module aggregation, and Mermaid-safe node IDs and labels so the diagrams stay readable and scoped to the page being rendered.
[crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:72-92]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:97-127]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:131-166]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:170-197]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_module_dependency_mermaid` | function | `pub(crate) fn render_module_dependency_mermaid(` | `render_module_dependency_mermaid [function]` | `549d1ee2-6881-510c-889e-6f62e3a56159` | 5-67 [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67] | Indexed function `render_module_dependency_mermaid` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67] |
| `aggregate_module_for_page` | function | `pub(crate) fn aggregate_module_for_page(page: &str, module: &str) -> String {` | `aggregate_module_for_page [function]` | `e0e523a6-4d26-5dd5-87e5-fb3099346e6b` | 72-92 [crates/gcode/src/commands/codewiki/render/diagrams.rs:72-92] | Indexed function `aggregate_module_for_page` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:72-92] |
| `render_subsystem_dependency_mermaid` | function | `pub(crate) fn render_subsystem_dependency_mermaid(` | `render_subsystem_dependency_mermaid [function]` | `7abed7bd-189b-5b96-a2c2-d12fb67d97ce` | 97-127 [crates/gcode/src/commands/codewiki/render/diagrams.rs:97-127] | Indexed function `render_subsystem_dependency_mermaid` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:97-127] |
| `render_architecture_structure_mermaid` | function | `pub(crate) fn render_architecture_structure_mermaid(` | `render_architecture_structure_mermaid [function]` | `ab0d093d-2922-55dd-b759-cc630c6013f5` | 131-166 [crates/gcode/src/commands/codewiki/render/diagrams.rs:131-166] | Indexed function `render_architecture_structure_mermaid` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:131-166] |
| `collect_subsystem_dependency_edges` | function | `pub(crate) fn collect_subsystem_dependency_edges(` | `collect_subsystem_dependency_edges [function]` | `0d99cf3d-e3ee-5f9d-b6d3-56325251a67d` | 170-197 [crates/gcode/src/commands/codewiki/render/diagrams.rs:170-197] | Indexed function `collect_subsystem_dependency_edges` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:170-197] |
| `collect_import_module_edges` | function | `fn collect_import_module_edges(` | `collect_import_module_edges [function]` | `9a025a96-c200-5993-8bae-aee3ac714b8f` | 199-222 [crates/gcode/src/commands/codewiki/render/diagrams.rs:199-222] | Indexed function `collect_import_module_edges` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:199-222] |
| `write_partial_import_graph_comment` | function | `fn write_partial_import_graph_comment(diagram: &mut String, omitted_edges: usize) {` | `write_partial_import_graph_comment [function]` | `f70327f9-ec20-58fb-87f3-4babd83c46db` | 224-231 [crates/gcode/src/commands/codewiki/render/diagrams.rs:224-231] | Indexed function `write_partial_import_graph_comment` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:224-231] |
| `render_module_call_mermaid` | function | `pub(crate) fn render_module_call_mermaid(` | `render_module_call_mermaid [function]` | `e96d176e-b4fb-52d6-9228-80a5570e698e` | 233-330 [crates/gcode/src/commands/codewiki/render/diagrams.rs:233-330] | Indexed function `render_module_call_mermaid` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:233-330] |
| `simplified_diagram_note` | function | `fn simplified_diagram_note(` | `simplified_diagram_note [function]` | `abbe7d47-fea3-59d6-893d-dc337f545c9e` | 332-349 [crates/gcode/src/commands/codewiki/render/diagrams.rs:332-349] | Indexed function `simplified_diagram_note` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:332-349] |
| `bounded_module_dependency_edges` | function | `pub(crate) fn bounded_module_dependency_edges(` | `bounded_module_dependency_edges [function]` | `b9fc8168-3f2d-50bc-b90f-ea84514c8aca` | 351-380 [crates/gcode/src/commands/codewiki/render/diagrams.rs:351-380] | Indexed function `bounded_module_dependency_edges` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:351-380] |
| `bounded_component_edges` | function | `pub(crate) fn bounded_component_edges(` | `bounded_component_edges [function]` | `7724626b-c47f-590b-a684-0282aea1d92d` | 382-432 [crates/gcode/src/commands/codewiki/render/diagrams.rs:382-432] | Indexed function `bounded_component_edges` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:382-432] |
| `dependency_neighbors` | function | `pub(crate) fn dependency_neighbors<'a>(` | `dependency_neighbors [function]` | `dcd7f0d2-4e32-5ef4-a773-f0ad9d774f7d` | 434-447 [crates/gcode/src/commands/codewiki/render/diagrams.rs:434-447] | Indexed function `dependency_neighbors` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:434-447] |
| `mermaid_node_id` | function | `pub(crate) fn mermaid_node_id(module: &str) -> String {` | `mermaid_node_id [function]` | `942443b2-6fa9-5c4b-a7ee-d605313eeadb` | 449-459 [crates/gcode/src/commands/codewiki/render/diagrams.rs:449-459] | Indexed function `mermaid_node_id` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:449-459] |
| `mermaid_label` | function | `pub(crate) fn mermaid_label(module: &str) -> String {` | `mermaid_label [function]` | `c908a55b-f241-5d1e-9501-64d550859042` | 461-476 [crates/gcode/src/commands/codewiki/render/diagrams.rs:461-476] | Indexed function `mermaid_label` in `crates/gcode/src/commands/codewiki/render/diagrams.rs`. [crates/gcode/src/commands/codewiki/render/diagrams.rs:461-476] |
