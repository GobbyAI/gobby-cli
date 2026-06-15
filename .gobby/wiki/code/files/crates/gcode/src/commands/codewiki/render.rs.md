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
  - 829-876
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Builds the Codewiki rendering layer for repository documentation: it turns graph and index data into Markdown pages for repo, architecture, onboarding, hotspots, module, and file views, and generates Mermaid dependency/call diagrams when available. The helper functions support that output by collecting and bounding import/call edges, aggregating paths to the current page depth, formatting safe node IDs and labels, and assembling hotspot sections, source excerpts, and degradation metadata into the final documents.
[crates/gcode/src/commands/codewiki/render.rs:5-60]
[crates/gcode/src/commands/codewiki/render.rs:65-85]
[crates/gcode/src/commands/codewiki/render.rs:90-120]
[crates/gcode/src/commands/codewiki/render.rs:124-151]
[crates/gcode/src/commands/codewiki/render.rs:153-176]

## API Symbols

- `render_module_dependency_mermaid` (function) component `render_module_dependency_mermaid [function]` (`b7b35534-a8ba-5c4b-a97d-2c70814ae8bd`) lines 5-60 [crates/gcode/src/commands/codewiki/render.rs:5-60]
  - Signature: `pub(crate) fn render_module_dependency_mermaid(`
  - Purpose: Aggregates module import edges relative to the requested page, filters out self-loops, selects a bounded subset for Mermaid rendering with a fallback to intra-page child edges when no direct edges exist, and returns a left-to-right dependency graph string or 'None' if no renderable edges remain. [crates/gcode/src/commands/codewiki/render.rs:5-60]
- `aggregate_module_for_page` (function) component `aggregate_module_for_page [function]` (`b759f847-9559-5f01-9f33-80abffa8cdf5`) lines 65-85 [crates/gcode/src/commands/codewiki/render.rs:65-85]
  - Signature: `pub(crate) fn aggregate_module_for_page(page: &str, module: &str) -> String {`
  - Purpose: Returns the page itself when 'module' equals or is nested directly under 'page', otherwise derives an aggregated module path by taking up to 'max(module_depth(page), 1)' non-empty path segments from 'module' and joining them with '/'. [crates/gcode/src/commands/codewiki/render.rs:65-85]
- `render_subsystem_dependency_mermaid` (function) component `render_subsystem_dependency_mermaid [function]` (`4282bdf2-f04c-5639-9623-bcb694df654d`) lines 90-120 [crates/gcode/src/commands/codewiki/render.rs:90-120]
  - Signature: `pub(crate) fn render_subsystem_dependency_mermaid(`
  - Purpose: Builds and returns an optional Mermaid left-to-right dependency graph for subsystem edges collected from the given roots, files, and graph edges, truncating to 'MAX_MERMAID_EDGES' and annotating any omitted edges with a partial-import comment. [crates/gcode/src/commands/codewiki/render.rs:90-120]
- `collect_subsystem_dependency_edges` (function) component `collect_subsystem_dependency_edges [function]` (`c5156a57-fdf0-5cf7-83da-bc37dcaaa118`) lines 124-151 [crates/gcode/src/commands/codewiki/render.rs:124-151]
  - Signature: `pub(crate) fn collect_subsystem_dependency_edges(`
  - Purpose: Builds a 'BTreeSet' of unique cross-subsystem import edges by mapping each file component to its subsystem root and retaining only 'CodewikiGraphEdgeKind::Import' edges whose source and target components belong to different roots. [crates/gcode/src/commands/codewiki/render.rs:124-151]
- `collect_import_module_edges` (function) component `collect_import_module_edges [function]` (`8eb318ca-4f87-50d8-bac5-803639140ff6`) lines 153-176 [crates/gcode/src/commands/codewiki/render.rs:153-176]
  - Signature: `fn collect_import_module_edges(`
  - Purpose: Builds a 'BTreeSet' of unique '(source_module, target_module)' pairs for all 'Import' graph edges whose source and target components map to different modules via the provided file component index. [crates/gcode/src/commands/codewiki/render.rs:153-176]
- `write_partial_import_graph_comment` (function) component `write_partial_import_graph_comment [function]` (`eb5f66c4-b93c-5dfa-a323-7a0a5d8d09fb`) lines 178-185 [crates/gcode/src/commands/codewiki/render.rs:178-185]
  - Signature: `fn write_partial_import_graph_comment(diagram: &mut String, omitted_edges: usize) {`
  - Purpose: Appends a Mermaid-style comment line to 'diagram' stating how many import-graph edges were omitted by bounds, but only when 'omitted_edges > 0'. [crates/gcode/src/commands/codewiki/render.rs:178-185]
- `render_module_call_mermaid` (function) component `render_module_call_mermaid [function]` (`7bdfe3c1-3ab9-52f2-a7be-9cc05ff2f22b`) lines 187-277 [crates/gcode/src/commands/codewiki/render.rs:187-277]
  - Signature: `pub(crate) fn render_module_call_mermaid(`
  - Purpose: Builds a bounded Mermaid call graph for a module by mapping components to files/modules, filtering 'Call' edges to those relevant to the module or its descendants, trimming them with hop/edge limits, and returning 'None' when no edges remain. [crates/gcode/src/commands/codewiki/render.rs:187-277]
- `bounded_module_dependency_edges` (function) component `bounded_module_dependency_edges [function]` (`211d3808-d9f7-5f6c-a20b-61786257aa92`) lines 279-308 [crates/gcode/src/commands/codewiki/render.rs:279-308]
  - Signature: `pub(crate) fn bounded_module_dependency_edges(`
  - Purpose: Performs a breadth-first search from 'module' over the directed dependency graph up to 'max_hops' and returns the subset of 'edges' whose source and target are both reachable within that bounded distance. [crates/gcode/src/commands/codewiki/render.rs:279-308]
- `bounded_component_edges` (function) component `bounded_component_edges [function]` (`8bd3aa34-88e5-5433-a693-ee1be68cc644`) lines 310-360 [crates/gcode/src/commands/codewiki/render.rs:310-360]
  - Signature: `pub(crate) fn bounded_component_edges(`
  - Purpose: Computes a hop-limited reachable subgraph from the given seed components by breadth-first expanding through 'edges', then returns up to 'max_edges' edges whose endpoints are both reachable, sorted by the greater endpoint distance. [crates/gcode/src/commands/codewiki/render.rs:310-360]
- `dependency_neighbors` (function) component `dependency_neighbors [function]` (`12deeef0-dc28-587f-a7ea-99aec86bee8a`) lines 362-375 [crates/gcode/src/commands/codewiki/render.rs:362-375]
  - Signature: `pub(crate) fn dependency_neighbors<'a>(`
  - Purpose: Returns a vector containing the opposite endpoint of each dependency edge incident to 'module', yielding 'target' when 'source == module' and 'source' when 'target == module'. [crates/gcode/src/commands/codewiki/render.rs:362-375]
- `mermaid_node_id` (function) component `mermaid_node_id [function]` (`e37426f1-2bad-590f-a070-378937b643a7`) lines 377-387 [crates/gcode/src/commands/codewiki/render.rs:377-387]
  - Signature: `pub(crate) fn mermaid_node_id(module: &str) -> String {`
  - Purpose: Returns a Mermaid-safe node identifier by prefixing 'm_' and replacing every non-ASCII-alphanumeric character in 'module' with '_'. [crates/gcode/src/commands/codewiki/render.rs:377-387]
- `mermaid_label` (function) component `mermaid_label [function]` (`5a33f4cc-a919-5f7b-90e0-9859b24a1ab9`) lines 389-404 [crates/gcode/src/commands/codewiki/render.rs:389-404]
  - Signature: `pub(crate) fn mermaid_label(module: &str) -> String {`
  - Purpose: Returns '"repo"' when 'module' is empty, otherwise escapes backslashes, double quotes, and Mermaid-sensitive bracket/brace/pipe characters so the module name is safe to use as a Mermaid label. [crates/gcode/src/commands/codewiki/render.rs:389-404]
- `build_repo_doc` (function) component `build_repo_doc [function]` (`9c0764be-a2df-5e3a-9fcb-4f1650d1d2c7`) lines 406-492 [crates/gcode/src/commands/codewiki/render.rs:406-492]
  - Signature: `pub(crate) fn build_repo_doc(`
  - Purpose: Builds the repository overview document by extracting top-level modules and root files into summary links, computing provenance spans and a structural fallback summary, and either reusing an unchanged cached 'code/repo.md' page or generating a new document, returning the rendered markdown plus a reuse flag. [crates/gcode/src/commands/codewiki/render.rs:406-492]
- `repo_source_excerpts` (function) component `repo_source_excerpts [function]` (`81bae339-1a71-5969-a8ff-9e393ed3ff51`) lines 497-517 [crates/gcode/src/commands/codewiki/render.rs:497-517]
  - Signature: `fn repo_source_excerpts(`
  - Purpose: Selects top-level files with no module, sorts them to prefer README-like files then files with more symbols and lexicographically by path, converts each to a source excerpt using 'leading_chunks', and returns up to 'prompts::MAX_PROMPT_SOURCE_EXCERPTS' excerpts. [crates/gcode/src/commands/codewiki/render.rs:497-517]
- `render_repo_doc` (function) component `render_repo_doc [function]` (`4da76d87-734b-5018-8fbf-27937a3b231d`) lines 519-568 [crates/gcode/src/commands/codewiki/render.rs:519-568]
  - Signature: `pub(crate) fn render_repo_doc(`
  - Purpose: Builds and returns a Markdown repository overview document with frontmatter, a title and summary section, optional module map, module and file bullet lists with citation markers resolved, and a references section. [crates/gcode/src/commands/codewiki/render.rs:519-568]
- `render_architecture_doc` (function) component `render_architecture_doc [function]` (`533a1b1f-4ea0-54bd-8cde-a9ff85424ed7`) lines 570-604 [crates/gcode/src/commands/codewiki/render.rs:570-604]
  - Signature: `pub(crate) fn render_architecture_doc(architecture: &ArchitectureDoc) -> String {`
  - Purpose: Builds a markdown architecture overview document by prepending frontmatter, emitting an H1 title, and conditionally appending narrative, dependency diagram, and subsystem/module listings from an 'ArchitectureDoc'. [crates/gcode/src/commands/codewiki/render.rs:570-604]
- `render_onboarding_doc` (function) component `render_onboarding_doc [function]` (`ea44d5ac-d6a6-5f72-91f0-105a60f97dde`) lines 606-642 [crates/gcode/src/commands/codewiki/render.rs:606-642]
  - Signature: `pub(crate) fn render_onboarding_doc(onboarding: &OnboardingDoc) -> String {`
  - Purpose: Builds a markdown onboarding document with degraded frontmatter, a '# Start Here' title, an optional 'Entry Points' list, and, when present, a numbered 'Recommended Reading Order' section that formats each module with its wikilink, degree, score, and summary. [crates/gcode/src/commands/codewiki/render.rs:606-642]
- `render_hotspots_doc` (function) component `render_hotspots_doc [function]` (`1682064a-d77e-5fe5-83a6-f98ae8223308`) lines 644-687 [crates/gcode/src/commands/codewiki/render.rs:644-687]
  - Signature: `pub(crate) fn render_hotspots_doc(hotspots: &HotspotsDoc) -> String {`
  - Purpose: Builds a Markdown hotspots report with frontmatter degradation metadata, emits a '# Hotspots' heading, short-circuits with an analytics-unavailable notice if graph analytics failed, otherwise renders 'hotspots', 'god_nodes', and 'bridges' sections with cross-references to hotspot IDs and appends a no-results message when all three collections are empty. [crates/gcode/src/commands/codewiki/render.rs:644-687]
- `write_hotspot_section` (function) component `write_hotspot_section [function]` (`7956b170-5fdf-53d6-a346-4e145348c943`) lines 689-691 [crates/gcode/src/commands/codewiki/render.rs:689-691]
  - Signature: `fn write_hotspot_section(doc: &mut String, title: &str, findings: &[HotspotFinding]) {`
  - Purpose: Delegates to 'write_hotspot_section_with_cross_refs' to append a hotspot section with the given 'title' and 'findings' to 'doc', passing 'None' for cross-references. [crates/gcode/src/commands/codewiki/render.rs:689-691]
- `write_hotspot_section_with_cross_refs` (function) component `write_hotspot_section_with_cross_refs [function]` (`19b093ab-6a44-5d93-b901-6bba04a9cffc`) lines 693-752 [crates/gcode/src/commands/codewiki/render.rs:693-752]
  - Signature: `fn write_hotspot_section_with_cross_refs(`
  - Purpose: Appends a Markdown hotspot section header to 'doc', emits 'None identified.' when 'findings' is empty, otherwise writes each finding as a bullet with label, metadata details, and optional cross-reference text when the node ID already appears in 'cross_ref'. [crates/gcode/src/commands/codewiki/render.rs:693-752]
- `model_degraded_sources` (function) component `model_degraded_sources [function]` (`77486849-9a8c-52bf-86ba-865da53e0b74`) lines 755-761 [crates/gcode/src/commands/codewiki/render.rs:755-761]
  - Signature: `pub(crate) fn model_degraded_sources(degraded: bool) -> Vec<String> {`
  - Purpose: Returns a single-element 'Vec<String>' containing '"model-unavailable"' when 'degraded' is 'true', otherwise returns an empty vector. [crates/gcode/src/commands/codewiki/render.rs:755-761]
- `render_module_doc` (function) component `render_module_doc [function]` (`06031d7b-3b13-58a4-909d-07b21071ee19`) lines 763-827 [crates/gcode/src/commands/codewiki/render.rs:763-827]
  - Signature: `pub(crate) fn render_module_doc(module: &ModuleDoc) -> String {`
  - Purpose: Builds a Markdown documentation string for a module by emitting frontmatter, the module title and parent link, an overview section, optional dependency/call diagrams with degraded markers based on graph availability, and listings for child modules and direct files. [crates/gcode/src/commands/codewiki/render.rs:763-827]
- `render_file_doc` (function) component `render_file_doc [function]` (`ceac175d-6fb9-5d09-ba71-8fb1d017c69d`) lines 829-876 [crates/gcode/src/commands/codewiki/render.rs:829-876]
  - Signature: `pub(crate) fn render_file_doc(file: &FileDoc) -> String {`
  - Purpose: Builds a markdown-like document string for a 'FileDoc', including frontmatter, file heading, module link, purpose section, and an API Symbols list with each symbol’s qualified name, kind, component metadata, line span, optional signature, and sanitized purpose, or a “No indexed symbols” notice when none exist. [crates/gcode/src/commands/codewiki/render.rs:829-876]

