---
title: crates/gcode/src/commands/codewiki/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/mod.rs
  ranges:
  - 81-86
  - 89-93
  - 95-117
  - 96-105
  - 107-116
  - 120-123
  - 126-129
  - 131-152
  - 132-137
  - 139-144
  - 146-151
  - 155-159
  - 162-169
  - 172-178
  - 181-191
  - 194-199
  - 202-206
  - 209-214
  - 217-221
  - 224-229
  - 232-238
  - 241-247
  - 250-257
  - 260-264
  - 267-271
  - 274-278
  - 281-293
  - 296-301
  - 304-306
  - 309-316
  - 319-322
  - 325-331
  - '333'
  - 335-355
  - 336-342
  - 344-350
  - 352-354
  - 357-472
  - 474-479
  - 481-498
  - 500-505
  - 507-519
  - 521-534
  - 537-549
  - 551-668
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/mod.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/mod.rs` exposes 45 indexed API symbols.
[crates/gcode/src/commands/codewiki/mod.rs:81-86] [crates/gcode/src/commands/codewiki/mod.rs:89-93] [crates/gcode/src/commands/codewiki/mod.rs:95-117] [crates/gcode/src/commands/codewiki/mod.rs:96-105]
[crates/gcode/src/commands/codewiki/mod.rs:107-116] [crates/gcode/src/commands/codewiki/mod.rs:120-123] [crates/gcode/src/commands/codewiki/mod.rs:126-129] [crates/gcode/src/commands/codewiki/mod.rs:131-152]
[crates/gcode/src/commands/codewiki/mod.rs:132-137] [crates/gcode/src/commands/codewiki/mod.rs:139-144] [crates/gcode/src/commands/codewiki/mod.rs:146-151] [crates/gcode/src/commands/codewiki/mod.rs:155-159]
[crates/gcode/src/commands/codewiki/mod.rs:162-169] [crates/gcode/src/commands/codewiki/mod.rs:172-178] [crates/gcode/src/commands/codewiki/mod.rs:181-191] [crates/gcode/src/commands/codewiki/mod.rs:194-199]
[crates/gcode/src/commands/codewiki/mod.rs:202-206] [crates/gcode/src/commands/codewiki/mod.rs:209-214] [crates/gcode/src/commands/codewiki/mod.rs:217-221] [crates/gcode/src/commands/codewiki/mod.rs:224-229]
[crates/gcode/src/commands/codewiki/mod.rs:232-238] [crates/gcode/src/commands/codewiki/mod.rs:241-247] [crates/gcode/src/commands/codewiki/mod.rs:250-257] [crates/gcode/src/commands/codewiki/mod.rs:260-264]
[crates/gcode/src/commands/codewiki/mod.rs:267-271] [crates/gcode/src/commands/codewiki/mod.rs:274-278] [crates/gcode/src/commands/codewiki/mod.rs:281-293] [crates/gcode/src/commands/codewiki/mod.rs:296-301]
[crates/gcode/src/commands/codewiki/mod.rs:304-306] [crates/gcode/src/commands/codewiki/mod.rs:309-316] [crates/gcode/src/commands/codewiki/mod.rs:319-322] [crates/gcode/src/commands/codewiki/mod.rs:325-331]
[crates/gcode/src/commands/codewiki/mod.rs:333] [crates/gcode/src/commands/codewiki/mod.rs:335-355] [crates/gcode/src/commands/codewiki/mod.rs:336-342] [crates/gcode/src/commands/codewiki/mod.rs:344-350]
[crates/gcode/src/commands/codewiki/mod.rs:352-354] [crates/gcode/src/commands/codewiki/mod.rs:357-472] [crates/gcode/src/commands/codewiki/mod.rs:474-479] [crates/gcode/src/commands/codewiki/mod.rs:481-498]
[crates/gcode/src/commands/codewiki/mod.rs:500-505] [crates/gcode/src/commands/codewiki/mod.rs:507-519] [crates/gcode/src/commands/codewiki/mod.rs:521-534] [crates/gcode/src/commands/codewiki/mod.rs:537-549]
[crates/gcode/src/commands/codewiki/mod.rs:551-668]

## API Symbols

- `CodewikiInput` (class) component `CodewikiInput [class]` (`80a7b818-ac46-5c38-a8d1-8907d2ce1589`) lines 81-86 [crates/gcode/src/commands/codewiki/mod.rs:81-86]
  - Signature: `pub struct CodewikiInput {`
  - Purpose: `CodewikiInput` is a struct that aggregates source file paths, directed graph edges with availability metadata, and code symbols for dependency or documentation analysis. [crates/gcode/src/commands/codewiki/mod.rs:81-86]
- `CodewikiGraphEdge` (class) component `CodewikiGraphEdge [class]` (`b98e75b7-dc79-53ec-80b4-df34b303609e`) lines 89-93 [crates/gcode/src/commands/codewiki/mod.rs:89-93]
  - Signature: `pub struct CodewikiGraphEdge {`
  - Purpose: `CodewikiGraphEdge` is a typed directed edge connecting two code components by their string identifiers, with the relationship kind specified by a `CodewikiGraphEdgeKind` discriminant. [crates/gcode/src/commands/codewiki/mod.rs:89-93]
- `CodewikiGraphEdge` (class) component `CodewikiGraphEdge [class]` (`1fae1e39-eb9d-5c9f-9d19-01004d1a7713`) lines 95-117 [crates/gcode/src/commands/codewiki/mod.rs:95-117]
  - Signature: `impl CodewikiGraphEdge {`
  - Purpose: CodewikiGraphEdge provides factory methods to construct typed edges representing call and import relationships between source and target code components. [crates/gcode/src/commands/codewiki/mod.rs:95-117]
- `CodewikiGraphEdge.call` (method) component `CodewikiGraphEdge.call [method]` (`b1a09341-9f1e-5bbc-bef3-088794dbaa75`) lines 96-105 [crates/gcode/src/commands/codewiki/mod.rs:96-105]
  - Signature: `pub fn call(`
  - Purpose: Creates a graph edge representing a function call relationship between two components, converting the provided source and target identifiers into strings and assigning them to a `CodewikiGraphEdgeKind::Call` edge. [crates/gcode/src/commands/codewiki/mod.rs:96-105]
- `CodewikiGraphEdge.import` (method) component `CodewikiGraphEdge.import [method]` (`9b04ba17-a2d1-5ab7-b558-8f6c822e08c8`) lines 107-116 [crates/gcode/src/commands/codewiki/mod.rs:107-116]
  - Signature: `pub fn import(`
  - Purpose: Creates a Self instance representing an import edge between source and target components, converting the provided component IDs into strings. [crates/gcode/src/commands/codewiki/mod.rs:107-116]
- `CodewikiGraphEdgeKind` (type) component `CodewikiGraphEdgeKind [type]` (`8c9ca666-c6a6-588b-a923-8d28f67da3e1`) lines 120-123 [crates/gcode/src/commands/codewiki/mod.rs:120-123]
  - Signature: `pub enum CodewikiGraphEdgeKind {`
  - Purpose: Indexed type `CodewikiGraphEdgeKind` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:120-123]
- `CodewikiGraph` (class) component `CodewikiGraph [class]` (`dc51db4d-c423-5980-afcd-637cee80b160`) lines 126-129 [crates/gcode/src/commands/codewiki/mod.rs:126-129]
  - Signature: `pub(crate) struct CodewikiGraph {`
  - Purpose: `CodewikiGraph` is a crate-private graph data structure that maintains a collection of directed edges and tracks their availability state. [crates/gcode/src/commands/codewiki/mod.rs:126-129]
- `CodewikiGraph` (class) component `CodewikiGraph [class]` (`0960cd36-df69-51fd-932a-efbfed510448`) lines 131-152 [crates/gcode/src/commands/codewiki/mod.rs:131-152]
  - Signature: `impl CodewikiGraph {`
  - Purpose: `CodewikiGraph` implements three factory constructors that instantiate the struct with distinct availability states (Available, Truncated, or Unavailable) and corresponding edge vectors. [crates/gcode/src/commands/codewiki/mod.rs:131-152]
- `CodewikiGraph.available` (method) component `CodewikiGraph.available [method]` (`ff8ee7d0-bf18-5ddf-b264-d643d891a1f3`) lines 132-137 [crates/gcode/src/commands/codewiki/mod.rs:132-137]
  - Signature: `fn available(edges: Vec<CodewikiGraphEdge>) -> Self {`
  - Purpose: Constructs a new instance with the provided edges and availability status initialized to `Available`. [crates/gcode/src/commands/codewiki/mod.rs:132-137]
- `CodewikiGraph.truncated` (method) component `CodewikiGraph.truncated [method]` (`32d1dc8b-de44-5908-8c7f-a6b19ed64857`) lines 139-144 [crates/gcode/src/commands/codewiki/mod.rs:139-144]
  - Signature: `fn truncated(edges: Vec<CodewikiGraphEdge>) -> Self {`
  - Purpose: Creates a new instance with the provided edges vector and sets its availability status to `Truncated`. [crates/gcode/src/commands/codewiki/mod.rs:139-144]
- `CodewikiGraph.unavailable` (method) component `CodewikiGraph.unavailable [method]` (`5573e446-d06c-5443-85cc-f5bd4f8f2bbd`) lines 146-151 [crates/gcode/src/commands/codewiki/mod.rs:146-151]
  - Signature: `fn unavailable() -> Self {`
  - Purpose: Creates a new instance of the struct with an empty edges vector and an `Unavailable` availability status. [crates/gcode/src/commands/codewiki/mod.rs:146-151]
- `CodewikiGraphAvailability` (type) component `CodewikiGraphAvailability [type]` (`7867e5cb-2656-5f2a-9e6b-9f5732cb2b27`) lines 155-159 [crates/gcode/src/commands/codewiki/mod.rs:155-159]
  - Signature: `pub enum CodewikiGraphAvailability {`
  - Purpose: Indexed type `CodewikiGraphAvailability` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:155-159]
- `FileDoc` (class) component `FileDoc [class]` (`01c62318-63e2-5501-ac4c-8adebc38db49`) lines 162-169 [crates/gcode/src/commands/codewiki/mod.rs:162-169]
  - Signature: `pub(crate) struct FileDoc {`
  - Purpose: `FileDoc` is a crate-private struct that aggregates documentation metadata for a source file, including its path, module name, summary, source spans, documented symbols, and component identifiers. [crates/gcode/src/commands/codewiki/mod.rs:162-169]
- `SymbolDoc` (class) component `SymbolDoc [class]` (`aea6ea25-2f18-5029-b314-46f61dd3d5ef`) lines 172-178 [crates/gcode/src/commands/codewiki/mod.rs:172-178]
  - Signature: `pub(crate) struct SymbolDoc {`
  - Purpose: `SymbolDoc` is a crate-private struct that associates a symbol with its documentation metadata, including its purpose, component identifier and label, and source code location. [crates/gcode/src/commands/codewiki/mod.rs:172-178]
- `ModuleDoc` (class) component `ModuleDoc [class]` (`f7097151-eeb1-5eae-8d9c-1319151c8722`) lines 181-191 [crates/gcode/src/commands/codewiki/mod.rs:181-191]
  - Signature: `pub(crate) struct ModuleDoc {`
  - Purpose: `ModuleDoc` is a crate-private struct that encapsulates comprehensive module documentation metadata, including the module's summary, source code locations, constituent files and submodules, component identifiers, and optional dependency and call diagrams. [crates/gcode/src/commands/codewiki/mod.rs:181-191]
- `ArchitectureDoc` (class) component `ArchitectureDoc [class]` (`92b069b8-f948-5bee-ae6a-f0bcbcf86c27`) lines 194-199 [crates/gcode/src/commands/codewiki/mod.rs:194-199]
  - Signature: `pub(crate) struct ArchitectureDoc {`
  - Purpose: `ArchitectureDoc` is a crate-private struct that aggregates architectural documentation metadata, containing source code spans, subsystems, an optional dependency diagram, and a list of degraded sources. [crates/gcode/src/commands/codewiki/mod.rs:194-199]
- `ArchitectureSubsystem` (class) component `ArchitectureSubsystem [class]` (`626e9528-a992-5247-9cd0-d91c09202fea`) lines 202-206 [crates/gcode/src/commands/codewiki/mod.rs:202-206]
  - Signature: `pub(crate) struct ArchitectureSubsystem {`
  - Purpose: `ArchitectureSubsystem` is a crate-private struct that represents an architectural component by associating a named module with its responsibility description and the source code spans where it appears. [crates/gcode/src/commands/codewiki/mod.rs:202-206]
- `OnboardingDoc` (class) component `OnboardingDoc [class]` (`fa7e7768-bdae-5c95-9ccf-2f1e3ee8e550`) lines 209-214 [crates/gcode/src/commands/codewiki/mod.rs:209-214]
  - Signature: `pub(crate) struct OnboardingDoc {`
  - Purpose: `OnboardingDoc` is a crate-private struct that encapsulates onboarding documentation with source spans, multiple entry points, a defined reading sequence, and degraded source tracking. [crates/gcode/src/commands/codewiki/mod.rs:209-214]
- `OnboardingEntryPoint` (class) component `OnboardingEntryPoint [class]` (`df28db7d-12fd-57eb-8de0-cea23dbc2292`) lines 217-221 [crates/gcode/src/commands/codewiki/mod.rs:217-221]
  - Signature: `pub(crate) struct OnboardingEntryPoint {`
  - Purpose: A crate-internal struct that encapsulates an onboarding entry point with its associated link, description text, and source code span location. [crates/gcode/src/commands/codewiki/mod.rs:217-221]
- `OnboardingStep` (class) component `OnboardingStep [class]` (`95b235c4-21b3-5f1e-a8cd-090c6f0c3013`) lines 224-229 [crates/gcode/src/commands/codewiki/mod.rs:224-229]
  - Signature: `pub(crate) struct OnboardingStep {`
  - Purpose: `OnboardingStep` is a crate-private struct that encapsulates an onboarding workflow unit with module identification, descriptive summary, degree value, and numeric score. [crates/gcode/src/commands/codewiki/mod.rs:224-229]
- `HotspotsDoc` (class) component `HotspotsDoc [class]` (`35d40cb5-0848-5737-a300-0c1d57c082b2`) lines 232-238 [crates/gcode/src/commands/codewiki/mod.rs:232-238]
  - Signature: `pub(crate) struct HotspotsDoc {`
  - Purpose: HotspotsDoc is a crate-private struct that aggregates code quality anti-pattern findings (hotspots, god nodes, bridges) with their associated source code spans and degraded source metadata. [crates/gcode/src/commands/codewiki/mod.rs:232-238]
- `HotspotFinding` (class) component `HotspotFinding [class]` (`4c3de805-0de4-5c0e-a0ec-e0f7f27170bf`) lines 241-247 [crates/gcode/src/commands/codewiki/mod.rs:241-247]
  - Signature: `pub(crate) struct HotspotFinding {`
  - Purpose: A crate-private struct that pairs a `HotspotNode` with optional degree, score, frequency, and weight metrics. [crates/gcode/src/commands/codewiki/mod.rs:241-247]
- `HotspotNode` (class) component `HotspotNode [class]` (`0552ca03-caf9-5d99-b059-a98842bd1209`) lines 250-257 [crates/gcode/src/commands/codewiki/mod.rs:250-257]
  - Signature: `pub(crate) struct HotspotNode {`
  - Purpose: `HotspotNode` is a crate-private struct that encapsulates metadata for a cross-referenceable documentation node, including an identifier, type classification, display label, wikilinks, and optional source location information. [crates/gcode/src/commands/codewiki/mod.rs:250-257]
- `FileLink` (class) component `FileLink [class]` (`c0819c4d-d149-5e10-a5bb-160575c57304`) lines 260-264 [crates/gcode/src/commands/codewiki/mod.rs:260-264]
  - Signature: `pub(crate) struct FileLink {`
  - Purpose: `FileLink` is a crate-private struct that associates a file path with a textual summary and a collection of source code spans. [crates/gcode/src/commands/codewiki/mod.rs:260-264]
- `ModuleLink` (class) component `ModuleLink [class]` (`ba8bb878-ce91-5d98-b441-a87b847e84e9`) lines 267-271 [crates/gcode/src/commands/codewiki/mod.rs:267-271]
  - Signature: `pub(crate) struct ModuleLink {`
  - Purpose: ModuleLink is a crate-private struct that associates a module identifier with a textual summary and a collection of source code span locations referencing that module. [crates/gcode/src/commands/codewiki/mod.rs:267-271]
- `SourceSpan` (class) component `SourceSpan [class]` (`602c8b30-c9ac-5ba9-98db-d2d2a0ef61ea`) lines 274-278 [crates/gcode/src/commands/codewiki/mod.rs:274-278]
  - Signature: `pub(crate) struct SourceSpan {`
  - Purpose: `SourceSpan` is a crate-private struct that represents a contiguous range of source code within a file, bounded by start and end line numbers. [crates/gcode/src/commands/codewiki/mod.rs:274-278]
- `CodewikiRunSummary` (class) component `CodewikiRunSummary [class]` (`f9bee112-60d7-5f5a-b70c-688873be2d38`) lines 281-293 [crates/gcode/src/commands/codewiki/mod.rs:281-293]
  - Signature: `pub struct CodewikiRunSummary {`
  - Purpose: `CodewikiRunSummary` is a struct that captures execution statistics and metadata from a codewiki documentation generation run, including project identification, output directory, artifact counts (pages, files, modules, symbols), processing results (changed paths, skipped items), and AI enablement state. [crates/gcode/src/commands/codewiki/mod.rs:281-293]
- `CodewikiMeta` (class) component `CodewikiMeta [class]` (`d6ba1895-5909-555b-a386-65ddd7fc5c97`) lines 296-301 [crates/gcode/src/commands/codewiki/mod.rs:296-301]
  - Signature: `pub(crate) struct CodewikiMeta {`
  - Purpose: `CodewikiMeta` is a crate-private struct that aggregates code wiki documentation metadata as a sorted map of `CodewikiDocMeta` entries, tracks generated documentation names, and optionally maintains a serializable index snapshot. [crates/gcode/src/commands/codewiki/mod.rs:296-301]
- `CodewikiDocMeta` (class) component `CodewikiDocMeta [class]` (`0cbf235a-984b-5581-ba70-1033a469cfed`) lines 304-306 [crates/gcode/src/commands/codewiki/mod.rs:304-306]
  - Signature: `pub(crate) struct CodewikiDocMeta {`
  - Purpose: `CodewikiDocMeta` is a crate-private struct that maintains a sorted map of source code hash values keyed by string identifiers. [crates/gcode/src/commands/codewiki/mod.rs:304-306]
- `CodewikiIndexSnapshot` (class) component `CodewikiIndexSnapshot [class]` (`634be8b2-c623-5ceb-accd-3097fc558c58`) lines 309-316 [crates/gcode/src/commands/codewiki/mod.rs:309-316]
  - Signature: `pub(crate) struct CodewikiIndexSnapshot {`
  - Purpose: CodewikiIndexSnapshot is a crate-private, serializable struct that maintains a snapshot of a code index containing ordered mappings of files and symbols, optional graph neighborhood data, and a list of degraded source identifiers. [crates/gcode/src/commands/codewiki/mod.rs:309-316]
- `CodewikiFileSnapshot` (class) component `CodewikiFileSnapshot [class]` (`439869e1-3e74-5aa3-9c94-de4418c984b2`) lines 319-322 [crates/gcode/src/commands/codewiki/mod.rs:319-322]
  - Signature: `pub(crate) struct CodewikiFileSnapshot {`
  - Purpose: `CodewikiFileSnapshot` is a crate-private struct that stores a file's content hash and symbol count for snapshot comparison or change detection. [crates/gcode/src/commands/codewiki/mod.rs:319-322]
- `CodewikiSymbolSnapshot` (class) component `CodewikiSymbolSnapshot [class]` (`07ea5a1f-1d96-5abd-adfe-3dbb078961b3`) lines 325-331 [crates/gcode/src/commands/codewiki/mod.rs:325-331]
  - Signature: `pub(crate) struct CodewikiSymbolSnapshot {`
  - Purpose: # CodewikiSymbolSnapshot

A crate-internal struct that captures point-in-time metadata for a code symbol, storing its file path, simple and qualified names, symbol kind, and starting line number. [crates/gcode/src/commands/codewiki/mod.rs:325-331]
- `TextGenerator` (type) component `TextGenerator [type]` (`75134eae-175e-50bd-99f1-adedc7771d45`) lines 333-333 [crates/gcode/src/commands/codewiki/mod.rs:333]
  - Signature: `pub type TextGenerator<'a> = dyn FnMut(&str, &str) -> Option<String> + 'a;`
  - Purpose: Indexed type `TextGenerator` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:333]
- `SourceSpan` (class) component `SourceSpan [class]` (`700dd111-f947-51ed-a114-7063b9cd1fd6`) lines 335-355 [crates/gcode/src/commands/codewiki/mod.rs:335-355]
  - Signature: `impl SourceSpan {`
  - Purpose: `SourceSpan` encapsulates a source code location (file path and line range) with methods to construct it from a Symbol, format it as a citation string, and test spatial containment. [crates/gcode/src/commands/codewiki/mod.rs:335-355]
- `SourceSpan.from_symbol` (method) component `SourceSpan.from_symbol [method]` (`1c5fd17f-3dee-56b7-8113-8799e916eda2`) lines 336-342 [crates/gcode/src/commands/codewiki/mod.rs:336-342]
  - Signature: `fn from_symbol(symbol: &Symbol) -> Self {`
  - Purpose: Constructs a Self instance from a Symbol reference by cloning its file path and copying its line start and end positions. [crates/gcode/src/commands/codewiki/mod.rs:336-342]
- `SourceSpan.citation` (method) component `SourceSpan.citation [method]` (`814fa2e2-db64-5600-ab71-817c78916abd`) lines 344-350 [crates/gcode/src/commands/codewiki/mod.rs:344-350]
  - Signature: `fn citation(&self) -> String {`
  - Purpose: This method generates a citation string formatted as `[file:line]` for single-line references or `[file:line_start-line_end]` for multi-line ranges. [crates/gcode/src/commands/codewiki/mod.rs:344-350]
- `SourceSpan.contains` (method) component `SourceSpan.contains [method]` (`60640222-b112-56e2-bd21-ec760b24ceda`) lines 352-354 [crates/gcode/src/commands/codewiki/mod.rs:352-354]
  - Signature: `fn contains(&self, file: &str, line_start: usize, line_end: usize) -> bool {`
  - Purpose: Returns true if the specified file matches and the provided line range is fully contained within the object's line range. [crates/gcode/src/commands/codewiki/mod.rs:352-354]
- `run` (function) component `run [function]` (`03cf1230-5305-5f39-87ea-49441b6295e7`) lines 357-472 [crates/gcode/src/commands/codewiki/mod.rs:357-472]
  - Signature: `pub fn run(`
  - Purpose: Loads scope-filtered visible files and symbols from a read-only database, constructs a constrained code dependency graph, and assembles them into a CodewikiInput structure for text generation. [crates/gcode/src/commands/codewiki/mod.rs:357-472]
- `validate_edge_limit` (function) component `validate_edge_limit [function]` (`55eea91a-a992-5bb9-a6e5-c77c1943068f`) lines 474-479 [crates/gcode/src/commands/codewiki/mod.rs:474-479]
  - Signature: `fn validate_edge_limit(edge_limit: usize) -> anyhow::Result<()> {`
  - Purpose: Validates that the `edge_limit` parameter falls within the inclusive range [1, MAX_EDGE_LIMIT], returning an anyhow error if out of bounds. [crates/gcode/src/commands/codewiki/mod.rs:474-479]
- `write_codewiki_docs` (function) component `write_codewiki_docs [function]` (`d46a6800-777e-50b5-ba90-7b596bf81fb0`) lines 481-498 [crates/gcode/src/commands/codewiki/mod.rs:481-498]
  - Signature: `fn write_codewiki_docs(`
  - Purpose: Writes a set of documentation pages incrementally to disk with optional index snapshot support, persists associated ownership metadata, and returns the list of changed file paths. [crates/gcode/src/commands/codewiki/mod.rs:481-498]
- `generate_hierarchical_docs` (function) component `generate_hierarchical_docs [function]` (`0cbbd7f0-bfa6-5310-ae2b-ae14e723898e`) lines 500-505 [crates/gcode/src/commands/codewiki/mod.rs:500-505]
  - Signature: `pub fn generate_hierarchical_docs(`
  - Purpose: This function generates hierarchical documentation from a `CodewikiInput` and optional `TextGenerator`, returning a vector of string tuple pairs by delegating to `generate_hierarchical_docs_with_graph_availability`. [crates/gcode/src/commands/codewiki/mod.rs:500-505]
- `generate_hierarchical_docs_with_graph_availability` (function) component `generate_hierarchical_docs_with_graph_availability [function]` (`159bbb42-e720-5c7d-9fd8-aa09bc6d5a2a`) lines 507-519 [crates/gcode/src/commands/codewiki/mod.rs:507-519]
  - Signature: `fn generate_hierarchical_docs_with_graph_availability(`
  - Purpose: Generates hierarchical documentation string pairs from CodewikiInput with optional TextGenerator support, gracefully returning an empty vector and logging a warning when generation fails due to missing ownership metadata. [crates/gcode/src/commands/codewiki/mod.rs:507-519]
- `generate_hierarchical_docs_with_ownership` (function) component `generate_hierarchical_docs_with_ownership [function]` (`b8648359-b291-5977-b1ac-31e7422a5f57`) lines 521-534 [crates/gcode/src/commands/codewiki/mod.rs:521-534]
  - Signature: `fn generate_hierarchical_docs_with_ownership(`
  - Purpose: Generates hierarchical documentation as string-tuple pairs by delegating to the core implementation with project root and ownership metadata context. [crates/gcode/src/commands/codewiki/mod.rs:521-534]
- `generate_hierarchical_docs_with_progress` (function) component `generate_hierarchical_docs_with_progress [function]` (`b2dcaf54-6ff1-5c5f-bb72-863ad01830e4`) lines 537-549 [crates/gcode/src/commands/codewiki/mod.rs:537-549]
  - Signature: `fn generate_hierarchical_docs_with_progress(`
  - Purpose: Generates hierarchical documentation from a CodewikiInput with progress tracking, returning a vector of string pairs and gracefully handling errors by returning an empty vector with logged warnings. [crates/gcode/src/commands/codewiki/mod.rs:537-549]
- `generate_hierarchical_docs_core` (function) component `generate_hierarchical_docs_core [function]` (`a04cbd7b-34ed-5104-ac7d-76b6ac7746da`) lines 551-668 [crates/gcode/src/commands/codewiki/mod.rs:551-668]
  - Signature: `fn generate_hierarchical_docs_core(`
  - Purpose: Generates hierarchical documentation for core files by organizing symbols, clustering files into modules, and producing a vector of name-content string pairs for file-level and module-level documentation. [crates/gcode/src/commands/codewiki/mod.rs:551-668]

