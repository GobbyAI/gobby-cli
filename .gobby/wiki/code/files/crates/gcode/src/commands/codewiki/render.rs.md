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
  - 340-390
  - 392-420
  - 422-448
  - 450-486
  - 488-531
  - 533-535
  - 537-596
  - 598-657
  - 659-697
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/render.rs` exposes 20 indexed API symbols.
[crates/gcode/src/commands/codewiki/render.rs:5-35] [crates/gcode/src/commands/codewiki/render.rs:37-71] [crates/gcode/src/commands/codewiki/render.rs:73-87] [crates/gcode/src/commands/codewiki/render.rs:89-112]
[crates/gcode/src/commands/codewiki/render.rs:114-121] [crates/gcode/src/commands/codewiki/render.rs:123-211] [crates/gcode/src/commands/codewiki/render.rs:213-242] [crates/gcode/src/commands/codewiki/render.rs:244-294]
[crates/gcode/src/commands/codewiki/render.rs:296-309] [crates/gcode/src/commands/codewiki/render.rs:311-321] [crates/gcode/src/commands/codewiki/render.rs:323-338] [crates/gcode/src/commands/codewiki/render.rs:340-390]
[crates/gcode/src/commands/codewiki/render.rs:392-420] [crates/gcode/src/commands/codewiki/render.rs:422-448] [crates/gcode/src/commands/codewiki/render.rs:450-486] [crates/gcode/src/commands/codewiki/render.rs:488-531]
[crates/gcode/src/commands/codewiki/render.rs:533-535] [crates/gcode/src/commands/codewiki/render.rs:537-596] [crates/gcode/src/commands/codewiki/render.rs:598-657] [crates/gcode/src/commands/codewiki/render.rs:659-697]

## API Symbols

- `render_module_dependency_mermaid` (function) component `render_module_dependency_mermaid [function]` (`b7b35534-a8ba-5c4b-a97d-2c70814ae8bd`) lines 5-35 [crates/gcode/src/commands/codewiki/render.rs:5-35]
  - Signature: `pub(crate) fn render_module_dependency_mermaid(`
  - Purpose: Generates a Mermaid left-to-right directed graph visualization of module import dependencies anchored to a specified module, bounded by maximum hop distance and accounting for any omitted edges. [crates/gcode/src/commands/codewiki/render.rs:5-35]
- `render_architecture_dependency_mermaid` (function) component `render_architecture_dependency_mermaid [function]` (`f01dacd0-759a-57d4-af1a-ba8425a39ab8`) lines 37-71 [crates/gcode/src/commands/codewiki/render.rs:37-71]
  - Signature: `pub(crate) fn render_architecture_dependency_mermaid(`
  - Purpose: Renders a Mermaid diagram visualizing module import dependencies bounded by maximum traversal depth and edge count limits. [crates/gcode/src/commands/codewiki/render.rs:37-71]
- `repo_mermaid_seed_modules` (function) component `repo_mermaid_seed_modules [function]` (`35a8f69a-945d-5b9f-abe4-a2c43f26a889`) lines 73-87 [crates/gcode/src/commands/codewiki/render.rs:73-87]
  - Signature: `fn repo_mermaid_seed_modules(edges: &BTreeSet<(String, String)>) -> BTreeSet<String> {`
  - Purpose: Extracts top-level modules (those without parent modules) from a dependency edge graph, or returns all modules if no parentless modules exist. [crates/gcode/src/commands/codewiki/render.rs:73-87]
- `collect_import_module_edges` (function) component `collect_import_module_edges [function]` (`5001a88d-9d21-58e6-9d0a-e4ec4f234375`) lines 89-112 [crates/gcode/src/commands/codewiki/render.rs:89-112]
  - Signature: `fn collect_import_module_edges(`
  - Purpose: Extracts inter-module import dependencies by mapping component-level import graph edges to their containing modules and filtering out intra-module imports, returning a set of unique module-to-module pairs. [crates/gcode/src/commands/codewiki/render.rs:89-112]
- `write_partial_import_graph_comment` (function) component `write_partial_import_graph_comment [function]` (`0573641e-bc7d-5668-a21f-7d180b53a6be`) lines 114-121 [crates/gcode/src/commands/codewiki/render.rs:114-121]
  - Signature: `fn write_partial_import_graph_comment(diagram: &mut String, omitted_edges: usize) {`
  - Purpose: Writes a comment line to a diagram string documenting the count of import graph edges omitted by bounds constraints, if any edges were omitted. [crates/gcode/src/commands/codewiki/render.rs:114-121]
- `render_module_call_mermaid` (function) component `render_module_call_mermaid [function]` (`98788570-6558-5d0b-8776-0550d11ef9b2`) lines 123-211 [crates/gcode/src/commands/codewiki/render.rs:123-211]
  - Signature: `pub(crate) fn render_module_call_mermaid(`
  - Purpose: Generates an optional Mermaid diagram string representing function call edges involving a specified module and its ancestors, bounded by maximum hop distance and edge count limits. [crates/gcode/src/commands/codewiki/render.rs:123-211]
- `bounded_module_dependency_edges` (function) component `bounded_module_dependency_edges [function]` (`1aa33a46-a03c-5222-8d23-5be1393b2ad1`) lines 213-242 [crates/gcode/src/commands/codewiki/render.rs:213-242]
  - Signature: `pub(crate) fn bounded_module_dependency_edges(`
  - Purpose: Filters a dependency edge set via breadth-first search to return only edges where both endpoints are reachable within a maximum hop distance from the starting module. [crates/gcode/src/commands/codewiki/render.rs:213-242]
- `bounded_component_edges` (function) component `bounded_component_edges [function]` (`d2001392-7d38-5840-96e5-8541ca4f71fd`) lines 244-294 [crates/gcode/src/commands/codewiki/render.rs:244-294]
  - Signature: `pub(crate) fn bounded_component_edges(`
  - Purpose: Performs bounded breadth-first search from seed components and returns up to `max_edges` edges where both endpoints are reachable within `max_hops` distance, prioritized by endpoint proximity. [crates/gcode/src/commands/codewiki/render.rs:244-294]
- `dependency_neighbors` (function) component `dependency_neighbors [function]` (`18207b0a-bc23-53ec-9eab-5a0574ffdea1`) lines 296-309 [crates/gcode/src/commands/codewiki/render.rs:296-309]
  - Signature: `pub(crate) fn dependency_neighbors<'a>(`
  - Purpose: Returns the peer module endpoint in a dependency relationship when the input module matches either the source or target of the given edge. [crates/gcode/src/commands/codewiki/render.rs:296-309]
- `mermaid_node_id` (function) component `mermaid_node_id [function]` (`522deb7c-b9d8-56d9-b250-15a62d7e116e`) lines 311-321 [crates/gcode/src/commands/codewiki/render.rs:311-321]
  - Signature: `pub(crate) fn mermaid_node_id(module: &str) -> String {`
  - Purpose: This function converts a module name string into a Mermaid-compatible node identifier by prepending "m_" and replacing all non-alphanumeric characters with underscores. [crates/gcode/src/commands/codewiki/render.rs:311-321]
- `mermaid_label` (function) component `mermaid_label [function]` (`3b6bb0e5-2666-54e5-82c7-69818b1ab9b9`) lines 323-338 [crates/gcode/src/commands/codewiki/render.rs:323-338]
  - Signature: `pub(crate) fn mermaid_label(module: &str) -> String {`
  - Purpose: Converts a module name into a Mermaid-safe label by HTML-entity-encoding special characters (brackets, parentheses, braces, pipes, quotes), or returns "repo" for empty input. [crates/gcode/src/commands/codewiki/render.rs:323-338]
- `build_repo_doc` (function) component `build_repo_doc [function]` (`ec73f37c-6b87-5bca-8444-c27fa612fcf9`) lines 340-390 [crates/gcode/src/commands/codewiki/render.rs:340-390]
  - Signature: `pub(crate) fn build_repo_doc(`
  - Purpose: # Summary

`build_repo_doc` generates and renders repository documentation by extracting top-level modules and root files, creating AI-generated or structural summaries, and grounding the output with source span citations. [crates/gcode/src/commands/codewiki/render.rs:340-390]
- `render_repo_doc` (function) component `render_repo_doc [function]` (`7ac7e37c-e831-5c91-9bf2-f0d7f6307265`) lines 392-420 [crates/gcode/src/commands/codewiki/render.rs:392-420]
  - Signature: `pub(crate) fn render_repo_doc(`
  - Purpose: Generates a markdown-formatted repository overview document containing a summary section, indexed modules and files lists with wikilink formatting, and source span citation markers. [crates/gcode/src/commands/codewiki/render.rs:392-420]
- `render_architecture_doc` (function) component `render_architecture_doc [function]` (`1cee6d29-a7d9-54df-88f4-06b109b121d0`) lines 422-448 [crates/gcode/src/commands/codewiki/render.rs:422-448]
  - Signature: `pub(crate) fn render_architecture_doc(architecture: &ArchitectureDoc) -> String {`
  - Purpose: Constructs a markdown document string from an ArchitectureDoc containing frontmatter, an optional dependency diagram, and a formatted list of subsystems with module wikilinks and responsibilities. [crates/gcode/src/commands/codewiki/render.rs:422-448]
- `render_onboarding_doc` (function) component `render_onboarding_doc [function]` (`65c0258b-f4d3-5d88-9d3b-0910a2d8d13e`) lines 450-486 [crates/gcode/src/commands/codewiki/render.rs:450-486]
  - Signature: `pub(crate) fn render_onboarding_doc(onboarding: &OnboardingDoc) -> String {`
  - Purpose: Renders an `OnboardingDoc` into a markdown-formatted string containing frontmatter, entry points, and a recommended reading order of modules ranked by centrality degree and score metrics. [crates/gcode/src/commands/codewiki/render.rs:450-486]
- `render_hotspots_doc` (function) component `render_hotspots_doc [function]` (`374cbaa6-bbea-5b20-98bb-2c572c73edb8`) lines 488-531 [crates/gcode/src/commands/codewiki/render.rs:488-531]
  - Signature: `pub(crate) fn render_hotspots_doc(hotspots: &HotspotsDoc) -> String {`
  - Purpose: Renders a `HotspotsDoc` into a markdown-formatted `String` containing frontmatter metadata, organized sections for hotspots/god nodes/bridges, and cross-references between identified structural findings. [crates/gcode/src/commands/codewiki/render.rs:488-531]
- `write_hotspot_section` (function) component `write_hotspot_section [function]` (`ee6cced2-9a96-5e07-ae9c-6d45d908ba70`) lines 533-535 [crates/gcode/src/commands/codewiki/render.rs:533-535]
  - Signature: `fn write_hotspot_section(doc: &mut String, title: &str, findings: &[HotspotFinding]) {`
  - Purpose: This function writes a hotspot findings section with a given title to a mutable document string by delegating to `write_hotspot_section_with_cross_refs` with `None` for cross-references. [crates/gcode/src/commands/codewiki/render.rs:533-535]
- `write_hotspot_section_with_cross_refs` (function) component `write_hotspot_section_with_cross_refs [function]` (`abf2f633-f99c-5c10-a679-952c992caa06`) lines 537-596 [crates/gcode/src/commands/codewiki/render.rs:537-596]
  - Signature: `fn write_hotspot_section_with_cross_refs(`
  - Purpose: This function appends a markdown section listing hotspot findings with optional cross-reference-based deduplication that either writes brief references to findings appearing in other sections or detailed entries with formatted metadata attributes. [crates/gcode/src/commands/codewiki/render.rs:537-596]
- `render_module_doc` (function) component `render_module_doc [function]` (`79775b73-f1db-5abe-b55d-19b26898d06e`) lines 598-657 [crates/gcode/src/commands/codewiki/render.rs:598-657]
  - Signature: `pub(crate) fn render_module_doc(module: &ModuleDoc) -> String {`
  - Purpose: Renders a `ModuleDoc` into a markdown-formatted string containing module metadata, frontmatter, hierarchical parent/child relationships, dependency and call diagrams, and child module/file listings. [crates/gcode/src/commands/codewiki/render.rs:598-657]
- `render_file_doc` (function) component `render_file_doc [function]` (`e74877fb-7cf2-550f-a395-28b3aff27bc1`) lines 659-697 [crates/gcode/src/commands/codewiki/render.rs:659-697]
  - Signature: `pub(crate) fn render_file_doc(file: &FileDoc) -> String {`
  - Purpose: Generates markdown documentation for a source file by formatting frontmatter, module hierarchy, purpose summary, and indexed API symbols with their signatures and source location ranges. [crates/gcode/src/commands/codewiki/render.rs:659-697]

