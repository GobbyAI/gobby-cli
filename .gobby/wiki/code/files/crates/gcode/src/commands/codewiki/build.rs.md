---
title: crates/gcode/src/commands/codewiki/build.rs
type: code_file
source:
- file: crates/gcode/src/commands/codewiki/build.rs
  ranges:
  - 5-83
  - 85-181
  - 183-253
  - 255-268
  - 270-303
  - 306-315
  - 317-338
  - 340-356
  - 358-363
  - 365-454
  - 456-551
  - 553-599
  - 601-727
  - 729-753
  - 755-810
  - 812-901
  - 903-918
  - 920-970
  - 972-978
  - 980-982
  - 984-989
provenance:
- file: crates/gcode/src/commands/codewiki/build.rs
  ranges:
  - 5-83
  - 85-181
  - 183-253
  - 255-268
  - 270-303
  - 306-315
  - 317-338
  - 340-356
  - 358-363
  - 365-454
  - 456-551
  - 553-599
  - 601-727
  - 729-753
  - 755-810
  - 812-901
  - 903-918
  - 920-970
  - 972-978
  - 980-982
  - 984-989
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/build.rs` exposes 21 indexed API symbols.
[crates/gcode/src/commands/codewiki/build.rs:5-83] [crates/gcode/src/commands/codewiki/build.rs:85-181] [crates/gcode/src/commands/codewiki/build.rs:183-253] [crates/gcode/src/commands/codewiki/build.rs:255-268]
[crates/gcode/src/commands/codewiki/build.rs:270-303] [crates/gcode/src/commands/codewiki/build.rs:306-315] [crates/gcode/src/commands/codewiki/build.rs:317-338] [crates/gcode/src/commands/codewiki/build.rs:340-356]
[crates/gcode/src/commands/codewiki/build.rs:358-363] [crates/gcode/src/commands/codewiki/build.rs:365-454] [crates/gcode/src/commands/codewiki/build.rs:456-551] [crates/gcode/src/commands/codewiki/build.rs:553-599]
[crates/gcode/src/commands/codewiki/build.rs:601-727] [crates/gcode/src/commands/codewiki/build.rs:729-753] [crates/gcode/src/commands/codewiki/build.rs:755-810] [crates/gcode/src/commands/codewiki/build.rs:812-901]
[crates/gcode/src/commands/codewiki/build.rs:903-918] [crates/gcode/src/commands/codewiki/build.rs:920-970] [crates/gcode/src/commands/codewiki/build.rs:972-978] [crates/gcode/src/commands/codewiki/build.rs:980-982]
[crates/gcode/src/commands/codewiki/build.rs:984-989]

## API Symbols

- `build_codewiki_index_snapshot` (function) component `build_codewiki_index_snapshot [function]` (`920c0a56-db4a-5ecb-83af-d844587be9a3`) lines 5-83 [crates/gcode/src/commands/codewiki/build.rs:5-83]
  - Signature: `pub(crate) fn build_codewiki_index_snapshot(`
  - Purpose: Generates a `CodewikiIndexSnapshot` by filtering core files and symbols from input, computing per-file content hashes and symbol counts, organizing symbol metadata, and conditionally including graph dependency neighborhoods based on availability. [crates/gcode/src/commands/codewiki/build.rs:5-83]
- `build_codewiki_changes_doc` (function) component `build_codewiki_changes_doc [function]` (`cf3285e1-b460-5737-b120-3b222951f89c`) lines 85-181 [crates/gcode/src/commands/codewiki/build.rs:85-181]
  - Signature: `pub(crate) fn build_codewiki_changes_doc(`
  - Purpose: Generates a markdown document comparing two `CodewikiIndexSnapshot` instances to report changes in files and symbols, or establishes the current snapshot as a baseline if no previous snapshot exists. [crates/gcode/src/commands/codewiki/build.rs:85-181]
- `build_file_doc` (function) component `build_file_doc [function]` (`c6366caa-bae9-55c0-8edd-b0c1fd1ea2b2`) lines 183-253 [crates/gcode/src/commands/codewiki/build.rs:183-253]
  - Signature: `pub(crate) fn build_file_doc(`
  - Purpose: Constructs a `FileDoc` by transforming symbols into documented components with AI-generated or structural purpose descriptions, source citations, and component metadata. [crates/gcode/src/commands/codewiki/build.rs:183-253]
- `hash_snapshot_file` (function) component `hash_snapshot_file [function]` (`7bac5d99-3bba-5e1a-ba6d-aa71c94ed209`) lines 255-268 [crates/gcode/src/commands/codewiki/build.rs:255-268]
  - Signature: `fn hash_snapshot_file(project_root: &Path, file: &str) -> anyhow::Result<String> {`
  - Purpose: Returns the content hash of a file after canonicalizing its path and verifying it resides within the project root. [crates/gcode/src/commands/codewiki/build.rs:255-268]
- `graph_neighborhood_fingerprints` (function) component `graph_neighborhood_fingerprints [function]` (`ff1b10dc-bdd0-5d09-8282-eb9da14656b2`) lines 270-303 [crates/gcode/src/commands/codewiki/build.rs:270-303]
  - Signature: `fn graph_neighborhood_fingerprints(`
  - Purpose: Computes deterministic content-hash fingerprints for each code symbol based on its sorted, bidirectional call and import edges in the dependency graph. [crates/gcode/src/commands/codewiki/build.rs:270-303]
- `ChangesFrontmatter` (class) component `ChangesFrontmatter [class]` (`60cf7d2d-8445-5eff-ad59-05eaa686fdf7`) lines 306-315 [crates/gcode/src/commands/codewiki/build.rs:306-315]
  - Signature: `struct ChangesFrontmatter<'a> {`
  - Purpose: A generic struct holding borrowed metadata about a change record, including its type, origin, quality metrics (trust and freshness), and degradation status with affected sources. [crates/gcode/src/commands/codewiki/build.rs:306-315]
- `changes_frontmatter` (function) component `changes_frontmatter [function]` (`46d31134-dcff-5512-93f2-1cb6d080f5c5`) lines 317-338 [crates/gcode/src/commands/codewiki/build.rs:317-338]
  - Signature: `fn changes_frontmatter(baseline: bool, degraded: bool, degraded_sources: &[String]) -> String {`
  - Purpose: Serializes code changes metadata (baseline status, degraded flags, and degraded sources) into a delimited YAML frontmatter string. [crates/gcode/src/commands/codewiki/build.rs:317-338]
- `write_bullet_section` (function) component `write_bullet_section [function]` (`6eb9acb7-cf07-5299-b5ed-1637d921cb7d`) lines 340-356 [crates/gcode/src/commands/codewiki/build.rs:340-356]
  - Signature: `fn write_bullet_section(`
  - Purpose: Appends a markdown bullet-point section to a mutable string with a heading, formatted items (each wrapped with configurable prefix/suffix), or "- None" if the items vector is empty. [crates/gcode/src/commands/codewiki/build.rs:340-356]
- `symbol_label` (function) component `symbol_label [function]` (`50188f0c-4048-5742-9a42-3e69dc1a2fb1`) lines 358-363 [crates/gcode/src/commands/codewiki/build.rs:358-363]
  - Signature: `fn symbol_label(symbol: &CodewikiSymbolSnapshot) -> String {`
  - Purpose: The `symbol_label` function returns a formatted string containing a code symbol's qualified name, kind, and file path for display purposes. [crates/gcode/src/commands/codewiki/build.rs:358-363]
- `build_module_docs` (function) component `build_module_docs [function]` (`9ef662f4-12d6-539a-828f-3e518abea1e0`) lines 365-454 [crates/gcode/src/commands/codewiki/build.rs:365-454]
  - Signature: `pub(crate) fn build_module_docs(`
  - Purpose: Constructs a hierarchical module documentation tree by aggregating files and child modules for each discovered module, sorted in reverse depth order. [crates/gcode/src/commands/codewiki/build.rs:365-454]
- `build_architecture_doc` (function) component `build_architecture_doc [function]` (`34363a23-f683-5bb5-aa67-65e268a2248a`) lines 456-551 [crates/gcode/src/commands/codewiki/build.rs:456-551]
  - Signature: `pub(crate) fn build_architecture_doc(`
  - Purpose: **Constructs an ArchitectureDoc by organizing modules into subsystems with file and child module summaries, optionally generating architectural descriptions via an LLM, while tracking graph data availability degradation.** [crates/gcode/src/commands/codewiki/build.rs:456-551]
- `build_onboarding_doc` (function) component `build_onboarding_doc [function]` (`e518ade6-5b00-5e50-b940-ac6581a71ee8`) lines 553-599 [crates/gcode/src/commands/codewiki/build.rs:553-599]
  - Signature: `pub(crate) fn build_onboarding_doc(`
  - Purpose: Constructs an `OnboardingDoc` by ranking onboarding steps from code graph metrics, aggregating source spans from entry points and reading steps, and tracking graph availability degradation states. [crates/gcode/src/commands/codewiki/build.rs:553-599]
- `build_hotspots_doc` (function) component `build_hotspots_doc [function]` (`f7e7a4c2-5948-5cac-83b1-2ebcbde5733b`) lines 601-727 [crates/gcode/src/commands/codewiki/build.rs:601-727]
  - Signature: `pub(crate) fn build_hotspots_doc(`
  - Purpose: Constructs a `HotspotsDoc` by analyzing file-level code dependencies as a directed graph to identify hotspots, architectural antipatterns (god nodes, bridges), and source spans while gracefully degrading on graph unavailability. [crates/gcode/src/commands/codewiki/build.rs:601-727]
- `hotspot_nodes` (function) component `hotspot_nodes [function]` (`f0d98230-97aa-5b1f-a70f-f391ad93206c`) lines 729-753 [crates/gcode/src/commands/codewiki/build.rs:729-753]
  - Signature: `fn hotspot_nodes(files: &[FileDoc]) -> BTreeMap<String, HotspotNode> {`
  - Purpose: Transforms file symbols into a `BTreeMap` mapping component IDs to `HotspotNode` structures, enriching each symbol with its kind, qualified name, and wiki link references. [crates/gcode/src/commands/codewiki/build.rs:729-753]
- `onboarding_entry_points` (function) component `onboarding_entry_points [function]` (`c1a5448f-0391-5681-b172-3f987651f355`) lines 755-810 [crates/gcode/src/commands/codewiki/build.rs:755-810]
  - Signature: `fn onboarding_entry_points(files: &[FileDoc]) -> Vec<OnboardingEntryPoint> {`
  - Purpose: Generates a deduplicated vector of `OnboardingEntryPoint` objects from Rust entry files and public API symbols, each with associated source spans and descriptions. [crates/gcode/src/commands/codewiki/build.rs:755-810]
- `ranked_onboarding_steps` (function) component `ranked_onboarding_steps [function]` (`4f028770-666c-55e4-bc7f-690ff3862291`) lines 812-901 [crates/gcode/src/commands/codewiki/build.rs:812-901]
  - Signature: `fn ranked_onboarding_steps(`
  - Purpose: Generates an ordered list of onboarding steps by ranking modules according to their centrality scores computed from the codebase's dependency graph. [crates/gcode/src/commands/codewiki/build.rs:812-901]
- `module_dependency_edges` (function) component `module_dependency_edges [function]` (`38f5abdf-bd5d-5bee-9448-fe0fbc4adfdd`) lines 903-918 [crates/gcode/src/commands/codewiki/build.rs:903-918]
  - Signature: `fn module_dependency_edges(`
  - Purpose: Extracts cross-module import dependencies from a code graph by resolving component-level import edges to their source and target modules, excluding intra-module imports. [crates/gcode/src/commands/codewiki/build.rs:903-918]
- `dependency_topology` (function) component `dependency_topology [function]` (`07391ea9-fa65-53e5-9fda-25f9c024fc2a`) lines 920-970 [crates/gcode/src/commands/codewiki/build.rs:920-970]
  - Signature: `fn dependency_topology(`
  - Purpose: Applies Kahn's algorithm to compute a topological sort of module dependencies, returning a BTreeMap that ranks each module by its processing order in a valid dependency resolution sequence, with cyclical modules assigned final ranks. [crates/gcode/src/commands/codewiki/build.rs:920-970]
- `step_source_spans` (function) component `step_source_spans [function]` (`88f91a38-40a2-556e-bd70-1feec6294da0`) lines 972-978 [crates/gcode/src/commands/codewiki/build.rs:972-978]
  - Signature: `fn step_source_spans(module: &str, modules: &[ModuleDoc]) -> Vec<SourceSpan> {`
  - Purpose: Retrieves and returns a cloned copy of the source spans from the `ModuleDoc` entry matching the specified module name, or an empty vector if no match is found. [crates/gcode/src/commands/codewiki/build.rs:972-978]
- `is_rust_entry_file` (function) component `is_rust_entry_file [function]` (`6b4e7d21-5b24-562f-b897-4cffdfa51c68`) lines 980-982 [crates/gcode/src/commands/codewiki/build.rs:980-982]
  - Signature: `fn is_rust_entry_file(file: &str) -> bool {`
  - Purpose: Returns `true` if the provided file path exactly matches or terminates with `main.rs` or `lib.rs`, identifying Rust crate entry points. [crates/gcode/src/commands/codewiki/build.rs:980-982]
- `is_public_api_symbol` (function) component `is_public_api_symbol [function]` (`efbeb594-fe2b-5fdf-a445-f1f52bb4d1b1`) lines 984-989 [crates/gcode/src/commands/codewiki/build.rs:984-989]
  - Signature: `fn is_public_api_symbol(symbol: &Symbol) -> bool {`
  - Purpose: Indexed function `is_public_api_symbol` in `crates/gcode/src/commands/codewiki/build.rs`. [crates/gcode/src/commands/codewiki/build.rs:984-989]

