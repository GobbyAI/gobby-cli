---
title: crates/gcode/src/commands/codewiki/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/mod.rs
  ranges:
  - 84-89
  - 92-96
  - 98-120
  - 99-108
  - 110-119
  - 123-126
  - 129-132
  - 134-155
  - 135-140
  - 142-147
  - 149-154
  - 158-162
  - 165-172
  - 175-181
  - 184-194
  - 197-202
  - 205-209
  - 212-217
  - 220-224
  - 227-232
  - 235-241
  - 244-250
  - 253-260
  - 263-267
  - 270-274
  - 277-281
  - 284-296
  - 299-306
  - 309-311
  - 314-321
  - 324-327
  - 330-336
  - '338'
  - 343-351
  - 353-369
  - 354-356
  - 358-360
  - 362-368
  - 372-375
  - 377-397
  - 378-384
  - 386-392
  - 394-396
  - 399-522
  - 524-529
  - 531-554
  - 556-561
  - 563-581
  - 583-598
  - 601-614
  - 616-742
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/mod.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/mod.rs` exposes 51 indexed API symbols.
[crates/gcode/src/commands/codewiki/mod.rs:84-89]
[crates/gcode/src/commands/codewiki/mod.rs:92-96]
[crates/gcode/src/commands/codewiki/mod.rs:98-120]
[crates/gcode/src/commands/codewiki/mod.rs:99-108]
[crates/gcode/src/commands/codewiki/mod.rs:110-119]
[crates/gcode/src/commands/codewiki/mod.rs:123-126]
[crates/gcode/src/commands/codewiki/mod.rs:129-132]
[crates/gcode/src/commands/codewiki/mod.rs:134-155]
[crates/gcode/src/commands/codewiki/mod.rs:135-140]
[crates/gcode/src/commands/codewiki/mod.rs:142-147]
[crates/gcode/src/commands/codewiki/mod.rs:149-154]
[crates/gcode/src/commands/codewiki/mod.rs:158-162]
[crates/gcode/src/commands/codewiki/mod.rs:165-172]
[crates/gcode/src/commands/codewiki/mod.rs:175-181]
[crates/gcode/src/commands/codewiki/mod.rs:184-194]
[crates/gcode/src/commands/codewiki/mod.rs:197-202]
[crates/gcode/src/commands/codewiki/mod.rs:205-209]
[crates/gcode/src/commands/codewiki/mod.rs:212-217]
[crates/gcode/src/commands/codewiki/mod.rs:220-224]
[crates/gcode/src/commands/codewiki/mod.rs:227-232]
[crates/gcode/src/commands/codewiki/mod.rs:235-241]
[crates/gcode/src/commands/codewiki/mod.rs:244-250]
[crates/gcode/src/commands/codewiki/mod.rs:253-260]
[crates/gcode/src/commands/codewiki/mod.rs:263-267]
[crates/gcode/src/commands/codewiki/mod.rs:270-274]
[crates/gcode/src/commands/codewiki/mod.rs:277-281]
[crates/gcode/src/commands/codewiki/mod.rs:284-296]
[crates/gcode/src/commands/codewiki/mod.rs:299-306]
[crates/gcode/src/commands/codewiki/mod.rs:309-311]
[crates/gcode/src/commands/codewiki/mod.rs:314-321]
[crates/gcode/src/commands/codewiki/mod.rs:324-327]
[crates/gcode/src/commands/codewiki/mod.rs:330-336]
[crates/gcode/src/commands/codewiki/mod.rs:338]
[crates/gcode/src/commands/codewiki/mod.rs:343-351]
[crates/gcode/src/commands/codewiki/mod.rs:353-369]
[crates/gcode/src/commands/codewiki/mod.rs:354-356]
[crates/gcode/src/commands/codewiki/mod.rs:358-360]
[crates/gcode/src/commands/codewiki/mod.rs:362-368]
[crates/gcode/src/commands/codewiki/mod.rs:372-375]
[crates/gcode/src/commands/codewiki/mod.rs:377-397]
[crates/gcode/src/commands/codewiki/mod.rs:378-384]
[crates/gcode/src/commands/codewiki/mod.rs:386-392]
[crates/gcode/src/commands/codewiki/mod.rs:394-396]
[crates/gcode/src/commands/codewiki/mod.rs:399-522]
[crates/gcode/src/commands/codewiki/mod.rs:524-529]
[crates/gcode/src/commands/codewiki/mod.rs:531-554]
[crates/gcode/src/commands/codewiki/mod.rs:556-561]
[crates/gcode/src/commands/codewiki/mod.rs:563-581]
[crates/gcode/src/commands/codewiki/mod.rs:583-598]
[crates/gcode/src/commands/codewiki/mod.rs:601-614]
[crates/gcode/src/commands/codewiki/mod.rs:616-742]

## API Symbols

- `CodewikiInput` (class) component `CodewikiInput [class]` (`264f0b1e-40af-5b4b-a308-2f2b158209d6`) lines 84-89 [crates/gcode/src/commands/codewiki/mod.rs:84-89]
  - Signature: `pub struct CodewikiInput {`
  - Purpose: `CodewikiInput` is a struct that aggregates source files, their inter-dependency graph edges, graph availability metadata, and symbol definitions for code indexing and documentation purposes. [crates/gcode/src/commands/codewiki/mod.rs:84-89]
- `CodewikiGraphEdge` (class) component `CodewikiGraphEdge [class]` (`71f20874-5e07-5cbd-9714-3d1a4ed6951c`) lines 92-96 [crates/gcode/src/commands/codewiki/mod.rs:92-96]
  - Signature: `pub struct CodewikiGraphEdge {`
  - Purpose: `CodewikiGraphEdge` represents a typed directed edge in a code graph that connects a source component to a target component via a specified edge kind. [crates/gcode/src/commands/codewiki/mod.rs:92-96]
- `CodewikiGraphEdge` (class) component `CodewikiGraphEdge [class]` (`0c58bd7d-b2cd-579a-87d4-a370373ce37a`) lines 98-120 [crates/gcode/src/commands/codewiki/mod.rs:98-120]
  - Signature: `impl CodewikiGraphEdge {`
  - Purpose: CodewikiGraphEdge provides factory constructors for creating directed edges in a code dependency graph, with `call()` and `import()` methods that instantiate edges representing either function call or import relationships between source and target code components. [crates/gcode/src/commands/codewiki/mod.rs:98-120]
- `CodewikiGraphEdge.call` (method) component `CodewikiGraphEdge.call [method]` (`5529f342-becb-5147-ab99-ac4b099fc241`) lines 99-108 [crates/gcode/src/commands/codewiki/mod.rs:99-108]
  - Signature: `pub fn call(`
  - Purpose: Constructs and returns a new graph edge of kind `Call` connecting two components by converting their provided IDs into strings. [crates/gcode/src/commands/codewiki/mod.rs:99-108]
- `CodewikiGraphEdge.import` (method) component `CodewikiGraphEdge.import [method]` (`2231bc10-a53f-5c92-ad98-ebea2da95bd0`) lines 110-119 [crates/gcode/src/commands/codewiki/mod.rs:110-119]
  - Signature: `pub fn import(`
  - Purpose: Constructs an instance representing an import graph edge relationship between a source and target component. [crates/gcode/src/commands/codewiki/mod.rs:110-119]
- `CodewikiGraphEdgeKind` (type) component `CodewikiGraphEdgeKind [type]` (`21b3a27e-d757-5cea-bf5d-8ba1b7d22a87`) lines 123-126 [crates/gcode/src/commands/codewiki/mod.rs:123-126]
  - Signature: `pub enum CodewikiGraphEdgeKind {`
  - Purpose: Indexed type `CodewikiGraphEdgeKind` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:123-126]
- `CodewikiGraph` (class) component `CodewikiGraph [class]` (`048edc83-3d56-5252-bbd9-51f11e1cdbde`) lines 129-132 [crates/gcode/src/commands/codewiki/mod.rs:129-132]
  - Signature: `pub(crate) struct CodewikiGraph {`
  - Purpose: CodewikiGraph is a crate-private struct that encapsulates a collection of directed graph edges and their associated availability metadata. [crates/gcode/src/commands/codewiki/mod.rs:129-132]
- `CodewikiGraph` (class) component `CodewikiGraph [class]` (`1435f60d-ff63-5839-9108-e5012e17a14d`) lines 134-155 [crates/gcode/src/commands/codewiki/mod.rs:134-155]
  - Signature: `impl CodewikiGraph {`
  - Purpose: `CodewikiGraph` provides three factory constructors that instantiate instances with edge collections indexed by availability state (`Available`, `Truncated`, or `Unavailable`). [crates/gcode/src/commands/codewiki/mod.rs:134-155]
- `CodewikiGraph.available` (method) component `CodewikiGraph.available [method]` (`2c0a806b-f18b-52cd-bf72-4e91a439afdb`) lines 135-140 [crates/gcode/src/commands/codewiki/mod.rs:135-140]
  - Signature: `fn available(edges: Vec<CodewikiGraphEdge>) -> Self {`
  - Purpose: This is a constructor method that instantiates `Self` with the provided `edges` vector and initializes its `availability` field to `CodewikiGraphAvailability::Available`. [crates/gcode/src/commands/codewiki/mod.rs:135-140]
- `CodewikiGraph.truncated` (method) component `CodewikiGraph.truncated [method]` (`3ce657b8-ff40-50e1-851a-4ca259612b02`) lines 142-147 [crates/gcode/src/commands/codewiki/mod.rs:142-147]
  - Signature: `fn truncated(edges: Vec<CodewikiGraphEdge>) -> Self {`
  - Purpose: Constructs a new instance with the provided edges vector and sets its availability status to `CodewikiGraphAvailability::Truncated`. [crates/gcode/src/commands/codewiki/mod.rs:142-147]
- `CodewikiGraph.unavailable` (method) component `CodewikiGraph.unavailable [method]` (`e9961dcc-7a15-51b6-b5ad-b73cefc089a4`) lines 149-154 [crates/gcode/src/commands/codewiki/mod.rs:149-154]
  - Signature: `fn unavailable() -> Self {`
  - Purpose: This factory method creates a new instance of the struct with an empty edges vector and the availability status set to `Unavailable`. [crates/gcode/src/commands/codewiki/mod.rs:149-154]
- `CodewikiGraphAvailability` (type) component `CodewikiGraphAvailability [type]` (`6c40a2eb-287a-577c-900e-765d3344c02d`) lines 158-162 [crates/gcode/src/commands/codewiki/mod.rs:158-162]
  - Signature: `pub enum CodewikiGraphAvailability {`
  - Purpose: Indexed type `CodewikiGraphAvailability` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:158-162]
- `FileDoc` (class) component `FileDoc [class]` (`cac9d777-2aaf-5018-a9fa-e63056a9671c`) lines 165-172 [crates/gcode/src/commands/codewiki/mod.rs:165-172]
  - Signature: `pub(crate) struct FileDoc {`
  - Purpose: FileDoc is a crate-private struct that aggregates documentation metadata for a source file, including its path, module name, summary, source code spans, documented symbols, and component identifiers. [crates/gcode/src/commands/codewiki/mod.rs:165-172]
- `SymbolDoc` (class) component `SymbolDoc [class]` (`255e196e-320b-51c7-a7d2-8ca302277c8f`) lines 175-181 [crates/gcode/src/commands/codewiki/mod.rs:175-181]
  - Signature: `pub(crate) struct SymbolDoc {`
  - Purpose: SymbolDoc is a crate-private struct that binds a symbol to its documentation metadata, including its purpose, associated component context (id and label), and source code location. [crates/gcode/src/commands/codewiki/mod.rs:175-181]
- `ModuleDoc` (class) component `ModuleDoc [class]` (`d4e1f871-115a-5f37-9af2-00ba8385b716`) lines 184-194 [crates/gcode/src/commands/codewiki/mod.rs:184-194]
  - Signature: `pub(crate) struct ModuleDoc {`
  - Purpose: `ModuleDoc` is a crate-internal struct that aggregates module documentation metadata including source locations, file and child module references, component identifiers, and optional dependency/call diagrams with their availability status. [crates/gcode/src/commands/codewiki/mod.rs:184-194]
- `ArchitectureDoc` (class) component `ArchitectureDoc [class]` (`52bf052a-8b7f-5204-929e-49c0178626dd`) lines 197-202 [crates/gcode/src/commands/codewiki/mod.rs:197-202]
  - Signature: `pub(crate) struct ArchitectureDoc {`
  - Purpose: `ArchitectureDoc` is a crate-internal struct that aggregates source code spans, subsystem definitions, an optional dependency diagram, and a registry of degraded sources for architectural documentation. [crates/gcode/src/commands/codewiki/mod.rs:197-202]
- `ArchitectureSubsystem` (class) component `ArchitectureSubsystem [class]` (`94bb24ac-d847-50b6-a6ad-b762f2d9e020`) lines 205-209 [crates/gcode/src/commands/codewiki/mod.rs:205-209]
  - Signature: `pub(crate) struct ArchitectureSubsystem {`
  - Purpose: `ArchitectureSubsystem` is a crate-private struct that represents an architectural subsystem component, tracking its module name, responsibility description, and associated source code spans. [crates/gcode/src/commands/codewiki/mod.rs:205-209]
- `OnboardingDoc` (class) component `OnboardingDoc [class]` (`182e85ce-704a-5c19-ae91-44258c2c69e2`) lines 212-217 [crates/gcode/src/commands/codewiki/mod.rs:212-217]
  - Signature: `pub(crate) struct OnboardingDoc {`
  - Purpose: `OnboardingDoc` is a crate-private struct that encapsulates an onboarding documentation structure containing source code spans, entry points, an ordered sequence of steps, and references to degraded sources. [crates/gcode/src/commands/codewiki/mod.rs:212-217]
- `OnboardingEntryPoint` (class) component `OnboardingEntryPoint [class]` (`93439864-62c2-5ad7-a3fc-8c03a85e5283`) lines 220-224 [crates/gcode/src/commands/codewiki/mod.rs:220-224]
  - Signature: `pub(crate) struct OnboardingEntryPoint {`
  - Purpose: `OnboardingEntryPoint` is a crate-internal struct that encapsulates an onboarding navigation entry with a URL link, descriptive text, and source code span metadata. [crates/gcode/src/commands/codewiki/mod.rs:220-224]
- `OnboardingStep` (class) component `OnboardingStep [class]` (`7db62319-de52-5826-b662-83e1b3fec011`) lines 227-232 [crates/gcode/src/commands/codewiki/mod.rs:227-232]
  - Signature: `pub(crate) struct OnboardingStep {`
  - Purpose: `OnboardingStep` is a crate-private struct that encapsulates metadata for an onboarding step, comprising a module identifier, summary description, numeric degree, and floating-point score. [crates/gcode/src/commands/codewiki/mod.rs:227-232]
- `HotspotsDoc` (class) component `HotspotsDoc [class]` (`079e8393-56f3-58fe-bedc-1330c6dc08bb`) lines 235-241 [crates/gcode/src/commands/codewiki/mod.rs:235-241]
  - Signature: `pub(crate) struct HotspotsDoc {`
  - Purpose: HotspotsDoc is a crate-private struct that aggregates code quality analysis findings, combining source spans with categorized hotspot detections (hotspots, god nodes, bridges) and degraded source identifiers. [crates/gcode/src/commands/codewiki/mod.rs:235-241]
- `HotspotFinding` (class) component `HotspotFinding [class]` (`bbe5ed19-ab16-5432-b8a6-af65f0540515`) lines 244-250 [crates/gcode/src/commands/codewiki/mod.rs:244-250]
  - Signature: `pub(crate) struct HotspotFinding {`
  - Purpose: HotspotFinding is a crate-private struct that pairs a HotspotNode with optional graph metrics (degree, score, frequency, and weight). [crates/gcode/src/commands/codewiki/mod.rs:244-250]
- `HotspotNode` (class) component `HotspotNode [class]` (`6ec3f131-8035-5a79-afca-35c20640e91b`) lines 253-260 [crates/gcode/src/commands/codewiki/mod.rs:253-260]
  - Signature: `pub(crate) struct HotspotNode {`
  - Purpose: `HotspotNode` is a crate-internal struct that encapsulates a wiki node with an identifier, kind classifier, label, wikilinks, and optional source span information. [crates/gcode/src/commands/codewiki/mod.rs:253-260]
- `FileLink` (class) component `FileLink [class]` (`91b99737-520d-53e1-90f6-ab3cd869a73d`) lines 263-267 [crates/gcode/src/commands/codewiki/mod.rs:263-267]
  - Signature: `pub(crate) struct FileLink {`
  - Purpose: `FileLink` is a crate-private struct that associates a file path with a summary description and a collection of source code spans indicating specific locations within that file. [crates/gcode/src/commands/codewiki/mod.rs:263-267]
- `ModuleLink` (class) component `ModuleLink [class]` (`3b999ec8-7f7b-5bb6-86d0-21cfe6ac773d`) lines 270-274 [crates/gcode/src/commands/codewiki/mod.rs:270-274]
  - Signature: `pub(crate) struct ModuleLink {`
  - Purpose: `ModuleLink` is a crate-private struct that associates a module identifier with a textual summary and a collection of source code spans. [crates/gcode/src/commands/codewiki/mod.rs:270-274]
- `SourceSpan` (class) component `SourceSpan [class]` (`61b67532-22c6-5a7a-93d8-81e2fc73d73d`) lines 277-281 [crates/gcode/src/commands/codewiki/mod.rs:277-281]
  - Signature: `pub(crate) struct SourceSpan {`
  - Purpose: `SourceSpan` is a crate-private struct that represents a contiguous line range within a source file, defined by a file path and inclusive start/end line numbers. [crates/gcode/src/commands/codewiki/mod.rs:277-281]
- `CodewikiRunSummary` (class) component `CodewikiRunSummary [class]` (`b9de8627-2f91-588d-9268-cfa78d1079af`) lines 284-296 [crates/gcode/src/commands/codewiki/mod.rs:284-296]
  - Signature: `pub struct CodewikiRunSummary {`
  - Purpose: `CodewikiRunSummary` is a struct that captures execution metadata, project context, output configuration, and aggregate metrics (pages generated, files/modules/symbols processed, and skipped counts) from a code documentation generation run. [crates/gcode/src/commands/codewiki/mod.rs:284-296]
- `CodewikiMeta` (class) component `CodewikiMeta [class]` (`46b7204e-129b-5e10-91a2-ff7270ac2d9a`) lines 299-306 [crates/gcode/src/commands/codewiki/mod.rs:299-306]
  - Signature: `pub(crate) struct CodewikiMeta {`
  - Purpose: `CodewikiMeta` is a crate-private struct that maintains sorted documentation metadata, generated documentation references, an optional index snapshot, and AI mode configuration for a code wiki system. [crates/gcode/src/commands/codewiki/mod.rs:299-306]
- `CodewikiDocMeta` (class) component `CodewikiDocMeta [class]` (`cf33d74b-6fae-5c35-9b43-63be94aef8b5`) lines 309-311 [crates/gcode/src/commands/codewiki/mod.rs:309-311]
  - Signature: `pub(crate) struct CodewikiDocMeta {`
  - Purpose: CodewikiDocMeta is a crate-private struct that maintains an ordered mapping of source identifiers to their hash values via a BTreeMap. [crates/gcode/src/commands/codewiki/mod.rs:309-311]
- `CodewikiIndexSnapshot` (class) component `CodewikiIndexSnapshot [class]` (`ac307735-3319-5a51-97f5-8b5d61b6f706`) lines 314-321 [crates/gcode/src/commands/codewiki/mod.rs:314-321]
  - Signature: `pub(crate) struct CodewikiIndexSnapshot {`
  - Purpose: CodewikiIndexSnapshot is a crate-private, serde-compatible struct that stores a snapshot of an indexed codebase with BTreeMap indices of files and symbols, optional graph neighborhoods, and a vector of degraded sources. [crates/gcode/src/commands/codewiki/mod.rs:314-321]
- `CodewikiFileSnapshot` (class) component `CodewikiFileSnapshot [class]` (`01474d36-9553-5679-a37d-00ae4c431cd7`) lines 324-327 [crates/gcode/src/commands/codewiki/mod.rs:324-327]
  - Signature: `pub(crate) struct CodewikiFileSnapshot {`
  - Purpose: `CodewikiFileSnapshot` is a crate-private struct that stores a content hash and symbol count to represent the immutable state of a codewiki file. [crates/gcode/src/commands/codewiki/mod.rs:324-327]
- `CodewikiSymbolSnapshot` (class) component `CodewikiSymbolSnapshot [class]` (`c53c9f78-9b53-5688-aa31-a1c0e7d6d1ab`) lines 330-336 [crates/gcode/src/commands/codewiki/mod.rs:330-336]
  - Signature: `pub(crate) struct CodewikiSymbolSnapshot {`
  - Purpose: `CodewikiSymbolSnapshot` is a crate-private struct that encapsulates metadata for a code symbol, capturing its file path, simple and qualified names, symbol classification, and starting line number. [crates/gcode/src/commands/codewiki/mod.rs:330-336]
- `TextGenerator` (type) component `TextGenerator [type]` (`debd9316-3c45-5ec5-89b7-6f8a590725a0`) lines 338-338 [crates/gcode/src/commands/codewiki/mod.rs:338]
  - Signature: `pub type TextGenerator<'a> = dyn FnMut(&str, &str) -> Option<String> + 'a;`
  - Purpose: Indexed type `TextGenerator` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:338]
- `AiDepth` (type) component `AiDepth [type]` (`f6e77c42-2835-5463-ad70-d94487b2da9f`) lines 343-351 [crates/gcode/src/commands/codewiki/mod.rs:343-351]
  - Signature: `pub enum AiDepth {`
  - Purpose: Indexed type `AiDepth` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:343-351]
- `AiDepth` (class) component `AiDepth [class]` (`8e7b891f-07cb-5fcf-9533-adde32746ff2`) lines 353-369 [crates/gcode/src/commands/codewiki/mod.rs:353-369]
  - Signature: `impl AiDepth {`
  - Purpose: AiDepth is an ordered enumeration of three AI analysis depth levels (Sections, Files, Symbols) that provides threshold-checking methods to query depth capabilities and retrieve string labels for each level. [crates/gcode/src/commands/codewiki/mod.rs:353-369]
- `AiDepth.includes_files` (method) component `AiDepth.includes_files [method]` (`79fdaf99-3ed2-588b-b653-d082cbb4dcbf`) lines 354-356 [crates/gcode/src/commands/codewiki/mod.rs:354-356]
  - Signature: `pub(crate) fn includes_files(self) -> bool {`
  - Purpose: Returns true if the current `AiDepth` value is greater than or equal to `AiDepth::Files`, indicating that the depth level includes file-level access. [crates/gcode/src/commands/codewiki/mod.rs:354-356]
- `AiDepth.includes_symbols` (method) component `AiDepth.includes_symbols [method]` (`2e8b7241-516b-53af-8bf3-acfb003292de`) lines 358-360 [crates/gcode/src/commands/codewiki/mod.rs:358-360]
  - Signature: `pub(crate) fn includes_symbols(self) -> bool {`
  - Purpose: Returns `true` if the current `AiDepth` value is greater than or equal to the `Symbols` variant, otherwise `false`. [crates/gcode/src/commands/codewiki/mod.rs:358-360]
- `AiDepth.mode_label` (method) component `AiDepth.mode_label [method]` (`a8798aeb-dd2f-5d90-a33a-8c6104eda6fe`) lines 362-368 [crates/gcode/src/commands/codewiki/mod.rs:362-368]
  - Signature: `fn mode_label(self) -> &'static str {`
  - Purpose: Returns a static string label corresponding to the `AiDepth` enum variant (either "sections", "files", or "symbols"). [crates/gcode/src/commands/codewiki/mod.rs:362-368]
- `CodewikiAiOptions` (class) component `CodewikiAiOptions [class]` (`babbcb4c-ea6d-50e0-b152-f78e90452862`) lines 372-375 [crates/gcode/src/commands/codewiki/mod.rs:372-375]
  - Signature: `pub struct CodewikiAiOptions {`
  - Purpose: `CodewikiAiOptions` is a configuration struct that specifies optional AI routing behavior and a required analysis depth level for codewiki AI operations. [crates/gcode/src/commands/codewiki/mod.rs:372-375]
- `SourceSpan` (class) component `SourceSpan [class]` (`05adeece-93a0-57e9-8cd0-fea4e10cbfe1`) lines 377-397 [crates/gcode/src/commands/codewiki/mod.rs:377-397]
  - Signature: `impl SourceSpan {`
  - Purpose: SourceSpan implements symbol-to-span conversion, formatted source location citation generation, and spatial containment validation for tracking source code locations. [crates/gcode/src/commands/codewiki/mod.rs:377-397]
- `SourceSpan.from_symbol` (method) component `SourceSpan.from_symbol [method]` (`5859004e-cb7f-559f-9eab-b19423977c3a`) lines 378-384 [crates/gcode/src/commands/codewiki/mod.rs:378-384]
  - Signature: `fn from_symbol(symbol: &Symbol) -> Self {`
  - Purpose: Constructs a new instance of `Self` from a `Symbol` by cloning its file path and copying its line start and end fields. [crates/gcode/src/commands/codewiki/mod.rs:378-384]
- `SourceSpan.citation` (method) component `SourceSpan.citation [method]` (`bd5a5ccf-fcf6-5275-8947-ab550a349ee2`) lines 386-392 [crates/gcode/src/commands/codewiki/mod.rs:386-392]
  - Signature: `fn citation(&self) -> String {`
  - Purpose: Returns a formatted citation string as `[file:line]` for single-line or `[file:start-end]` for multi-line ranges. [crates/gcode/src/commands/codewiki/mod.rs:386-392]
- `SourceSpan.contains` (method) component `SourceSpan.contains [method]` (`fc44d1a9-6dd8-5774-8d07-475de91b81fa`) lines 394-396 [crates/gcode/src/commands/codewiki/mod.rs:394-396]
  - Signature: `fn contains(&self, file: &str, line_start: usize, line_end: usize) -> bool {`
  - Purpose: Checks whether a specified file and line range [line_start, line_end] are completely contained within the span's boundaries. [crates/gcode/src/commands/codewiki/mod.rs:394-396]
- `run` (function) component `run [function]` (`145ba7e3-1427-52d7-8cb4-e0d669063f45`) lines 399-522 [crates/gcode/src/commands/codewiki/mod.rs:399-522]
  - Signature: `pub fn run(`
  - Purpose: Queries a read-only database to extract scoped code files and symbols, constructs a bounded dependency graph with configurable edge limits, and prepares CodewikiInput with AI generation configuration for code analysis. [crates/gcode/src/commands/codewiki/mod.rs:399-522]
- `validate_edge_limit` (function) component `validate_edge_limit [function]` (`394a92b1-a8d3-5d04-a09d-4186fd357389`) lines 524-529 [crates/gcode/src/commands/codewiki/mod.rs:524-529]
  - Signature: `fn validate_edge_limit(edge_limit: usize) -> anyhow::Result<()> {`
  - Purpose: Validates that the `edge_limit` parameter falls within the inclusive range [1, MAX_EDGE_LIMIT], returning `Ok(())` on success or an `anyhow::Error` with a descriptive message on failure. [crates/gcode/src/commands/codewiki/mod.rs:524-529]
- `write_codewiki_docs` (function) component `write_codewiki_docs [function]` (`1aec054a-f201-5b6e-8019-79e42648b3e5`) lines 531-554 [crates/gcode/src/commands/codewiki/mod.rs:531-554]
  - Signature: `fn write_codewiki_docs(`
  - Purpose: Writes codewiki documentation pages incrementally to disk with ownership metadata tracking, returning a list of modified file paths. [crates/gcode/src/commands/codewiki/mod.rs:531-554]
- `generate_hierarchical_docs` (function) component `generate_hierarchical_docs [function]` (`e5f6e08c-3a3c-5d78-9e1c-5074bbfd84e7`) lines 556-561 [crates/gcode/src/commands/codewiki/mod.rs:556-561]
  - Signature: `pub fn generate_hierarchical_docs(`
  - Purpose: This function is a wrapper that generates hierarchical documentation by delegating to `generate_hierarchical_docs_with_graph_availability`, accepting a CodewikiInput and optional TextGenerator reference, returning a vector of string tuples. [crates/gcode/src/commands/codewiki/mod.rs:556-561]
- `generate_hierarchical_docs_with_graph_availability` (function) component `generate_hierarchical_docs_with_graph_availability [function]` (`7e4e152e-6079-5f65-8e99-7a7d708c3157`) lines 563-581 [crates/gcode/src/commands/codewiki/mod.rs:563-581]
  - Signature: `fn generate_hierarchical_docs_with_graph_availability(`
  - Purpose: Generates hierarchical symbol-level documentation from code input via a core generation function, returning string pairs or an empty vector on failure. [crates/gcode/src/commands/codewiki/mod.rs:563-581]
- `generate_hierarchical_docs_with_ownership` (function) component `generate_hierarchical_docs_with_ownership [function]` (`9ae4a3d2-39de-52be-8d75-e7073ccdab20`) lines 583-598 [crates/gcode/src/commands/codewiki/mod.rs:583-598]
  - Signature: `fn generate_hierarchical_docs_with_ownership(`
  - Purpose: Generates hierarchical project documentation with integrated code ownership metadata by delegating to the core generation function with project context. [crates/gcode/src/commands/codewiki/mod.rs:583-598]
- `generate_hierarchical_docs_with_progress` (function) component `generate_hierarchical_docs_with_progress [function]` (`690ec5ef-c1cb-57bd-89e4-2567a057ab6e`) lines 601-614 [crates/gcode/src/commands/codewiki/mod.rs:601-614]
  - Signature: `fn generate_hierarchical_docs_with_progress(`
  - Purpose: Generates a vector of string tuple pairs representing hierarchical documentation from CodewikiInput, delegating to a core function with optional text generation and specified AI depth while handling errors by logging and returning an empty vector. [crates/gcode/src/commands/codewiki/mod.rs:601-614]
- `generate_hierarchical_docs_core` (function) component `generate_hierarchical_docs_core [function]` (`c8057477-4bbb-5509-962f-ac214ca07c21`) lines 616-742 [crates/gcode/src/commands/codewiki/mod.rs:616-742]
  - Signature: `fn generate_hierarchical_docs_core(`
  - Purpose: Generates hierarchical documentation for core files by filtering and organizing input symbols by file, building file-level documentation with optional AI-powered generation, and returning a vector of (filepath, documentation) string pairs. [crates/gcode/src/commands/codewiki/mod.rs:616-742]

