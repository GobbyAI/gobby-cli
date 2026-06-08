---
title: crates/gcode/src/commands/codewiki/render.rs
type: code_file
source_files:
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-51
  - 53-141
  - 143-172
  - 174-224
  - 226-239
  - 241-251
  - 253-268
  - 270-318
  - 320-349
  - 351-410
  - 412-450
---

# crates/gcode/src/commands/codewiki/render.rs

Module: [[modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/render.rs` exposes 11 indexed API symbols. [crates/gcode/src/commands/codewiki/render.rs:5-51] [crates/gcode/src/commands/codewiki/render.rs:53-141] [crates/gcode/src/commands/codewiki/render.rs:143-172] [crates/gcode/src/commands/codewiki/render.rs:174-224] [crates/gcode/src/commands/codewiki/render.rs:226-239] [crates/gcode/src/commands/codewiki/render.rs:241-251] [crates/gcode/src/commands/codewiki/render.rs:253-268] [crates/gcode/src/commands/codewiki/render.rs:270-318] [crates/gcode/src/commands/codewiki/render.rs:320-349] [crates/gcode/src/commands/codewiki/render.rs:351-410] [crates/gcode/src/commands/codewiki/render.rs:412-450]

## API Symbols

- `render_module_dependency_mermaid` (function) component `render_module_dependency_mermaid [function]` (`b7b35534-a8ba-5c4b-a97d-2c70814ae8bd`) lines 5-51 [crates/gcode/src/commands/codewiki/render.rs:5-51]
  - Signature: `pub(crate) fn render_module_dependency_mermaid(`
  - Purpose: Generates a Mermaid diagram visualizing cross-module import dependencies bounded by maximum hop distance from the specified module, excluding intra-module edges. [crates/gcode/src/commands/codewiki/render.rs:5-51]
- `render_module_call_mermaid` (function) component `render_module_call_mermaid [function]` (`807f6db8-51b5-5c72-b0ce-2ec09ea21721`) lines 53-141 [crates/gcode/src/commands/codewiki/render.rs:53-141]
  - Signature: `pub(crate) fn render_module_call_mermaid(`
  - Purpose: Generates a Mermaid diagram source string representing bounded call dependencies for a specified module, filtered to include only call edges involving that module or its ancestors and constrained by maximum hop count and edge limits. [crates/gcode/src/commands/codewiki/render.rs:53-141]
- `bounded_module_dependency_edges` (function) component `bounded_module_dependency_edges [function]` (`caae7c80-f0c1-59b9-a5c0-eff0722991f1`) lines 143-172 [crates/gcode/src/commands/codewiki/render.rs:143-172]
  - Signature: `pub(crate) fn bounded_module_dependency_edges(`
  - Purpose: Returns the induced subgraph of dependency edges where both endpoints are reachable within `max_hops` distance from a specified module, computed via breadth-first search. [crates/gcode/src/commands/codewiki/render.rs:143-172]
- `bounded_component_edges` (function) component `bounded_component_edges [function]` (`8f58cd28-4bad-58f5-b7d5-f546837dbfdc`) lines 174-224 [crates/gcode/src/commands/codewiki/render.rs:174-224]
  - Signature: `pub(crate) fn bounded_component_edges(`
  - Purpose: Returns up to `max_edges` edges incident to components reachable within `max_hops` distance from seed components via breadth-first search, prioritized by proximity to the seed set. [crates/gcode/src/commands/codewiki/render.rs:174-224]
- `dependency_neighbors` (function) component `dependency_neighbors [function]` (`cbe6811a-36d9-5646-a5c7-d886217b664e`) lines 226-239 [crates/gcode/src/commands/codewiki/render.rs:226-239]
  - Signature: `pub(crate) fn dependency_neighbors<'a>(`
  - Purpose: # Summary

Returns the modules directly adjacent to a given module in a dependency graph by collecting the opposite endpoint(s) from source-target pairs where the module appears as either source or target. [crates/gcode/src/commands/codewiki/render.rs:226-239]
- `mermaid_node_id` (function) component `mermaid_node_id [function]` (`7441c004-f44e-5efb-95a0-c8612e9c3084`) lines 241-251 [crates/gcode/src/commands/codewiki/render.rs:241-251]
  - Signature: `pub(crate) fn mermaid_node_id(module: &str) -> String {`
  - Purpose: Converts a module name into a Mermaid diagram node identifier by prefixing `m_` and replacing all non-ASCII-alphanumeric characters with underscores. [crates/gcode/src/commands/codewiki/render.rs:241-251]
- `mermaid_label` (function) component `mermaid_label [function]` (`2766b70b-ffb4-5ed3-9fa1-efcc6e510dd2`) lines 253-268 [crates/gcode/src/commands/codewiki/render.rs:253-268]
  - Signature: `pub(crate) fn mermaid_label(module: &str) -> String {`
  - Purpose: Escapes special characters in a module name for safe use in Mermaid diagram syntax, returning "repo" if the input is empty. [crates/gcode/src/commands/codewiki/render.rs:253-268]
- `build_repo_doc` (function) component `build_repo_doc [function]` (`4e05c5b1-6583-5a88-8463-88cd2b19f116`) lines 270-318 [crates/gcode/src/commands/codewiki/render.rs:270-318]
  - Signature: `pub(crate) fn build_repo_doc(`
  - Purpose: Generates a repository documentation string by filtering top-level modules and root files, optionally synthesizing an LLM-generated summary with source-span citations, and rendering the aggregated content. [crates/gcode/src/commands/codewiki/render.rs:270-318]
- `render_repo_doc` (function) component `render_repo_doc [function]` (`ed4fdb4f-9eaf-5599-bd2b-65f055d54a44`) lines 320-349 [crates/gcode/src/commands/codewiki/render.rs:320-349]
  - Signature: `pub(crate) fn render_repo_doc(`
  - Purpose: Constructs a markdown documentation string aggregating repository metadata with frontmatter, a summary section, and optional wikilinked module and file listings with descriptions. [crates/gcode/src/commands/codewiki/render.rs:320-349]
- `render_module_doc` (function) component `render_module_doc [function]` (`4bbe2f5a-c57a-5439-9fa4-2bee4b35dd3d`) lines 351-410 [crates/gcode/src/commands/codewiki/render.rs:351-410]
  - Signature: `pub(crate) fn render_module_doc(module: &ModuleDoc) -> String {`
  - Purpose: # Summary

`render_module_doc` generates a markdown String document from a ModuleDoc by rendering module metadata, parent-child hierarchy, dependency and call diagrams, and associated child modules and files. [crates/gcode/src/commands/codewiki/render.rs:351-410]
- `render_file_doc` (function) component `render_file_doc [function]` (`759f062c-c6f9-5f3c-9b61-3a42cfa6eda5`) lines 412-450 [crates/gcode/src/commands/codewiki/render.rs:412-450]
  - Signature: `pub(crate) fn render_file_doc(file: &FileDoc) -> String {`
  - Purpose: Renders a markdown document for a source code file containing its metadata, module reference, purpose description, and indexed API symbols with their signatures and line locations. [crates/gcode/src/commands/codewiki/render.rs:412-450]

