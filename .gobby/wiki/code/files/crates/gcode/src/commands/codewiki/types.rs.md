---
title: crates/gcode/src/commands/codewiki/types.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/types.rs
  ranges:
  - 11-21
  - 26-30
  - 33-45
  - 50-62
  - 65-69
  - 71-93
  - 96-99
  - 102-105
  - 107-128
  - 131-135
  - 138-150
  - 153-159
  - 162-177
  - 180-186
  - 189-194
  - 197-202
  - 205-209
  - 212-217
  - 220-226
  - 229-235
  - 238-245
  - 248-252
  - 255-259
  - 262-266
  - 269-281
  - 284-291
  - 294-310
  - 315-322
  - 324-333
  - 336-343
  - 346-349
  - 352-358
  - '360'
  - 367-371
  - 376-384
  - 386-402
  - 405-411
  - 413-433
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/types.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Defines the data model and small helper routines for codewiki generation. `CodewikiInput` bundles the files, symbols, graph edges, graph availability, and per-file leading chunks that feed prompt assembly. `LeadingChunk`, `source_excerpt_for_file`, and `ranked_source_excerpts` turn indexed file content into prompt excerpts, preferring symbol-dense files and falling back to summaries when content is missing. The rest of the file is a set of serde-friendly document and snapshot types for graph metadata, architecture and onboarding docs, hotspots, build/run summaries, AI depth/options, and `SourceSpan` utilities so generated codewiki output can carry structured provenance, citations, and availability state.
[crates/gcode/src/commands/codewiki/types.rs:11-21]
[crates/gcode/src/commands/codewiki/types.rs:26-30]
[crates/gcode/src/commands/codewiki/types.rs:33-45]
[crates/gcode/src/commands/codewiki/types.rs:50-62]
[crates/gcode/src/commands/codewiki/types.rs:65-69]

## API Symbols

- `CodewikiInput` (class) component `CodewikiInput [class]` (`b6d93a42-87d9-5f50-8b57-7c348d37760b`) lines 11-21 [crates/gcode/src/commands/codewiki/types.rs:11-21]
  - Signature: `pub struct CodewikiInput {`
  - Purpose: 'CodewikiInput' is a data container for codewiki generation that bundles file paths, graph edges and availability, discovered symbols, and a per-file leading content map used to enrich aggregate prompts with indexed source text or fall back to summaries when content is missing. [crates/gcode/src/commands/codewiki/types.rs:11-21]
- `LeadingChunk` (class) component `LeadingChunk [class]` (`e6ff09c9-e115-545b-b60e-57571e920938`) lines 26-30 [crates/gcode/src/commands/codewiki/types.rs:26-30]
  - Signature: `pub struct LeadingChunk {`
  - Purpose: 'LeadingChunk' is a Rust struct that stores a leading text fragment as 'content' along with its inclusive line range via 'line_start' and 'line_end'. [crates/gcode/src/commands/codewiki/types.rs:26-30]
- `source_excerpt_for_file` (function) component `source_excerpt_for_file [function]` (`c4a94f1e-8ff9-570f-9607-04ed9b695c6b`) lines 33-45 [crates/gcode/src/commands/codewiki/types.rs:33-45]
  - Signature: `pub(crate) fn source_excerpt_for_file(`
  - Purpose: Returns an optional 'prompts::SourceExcerpt' for the given file by looking up its 'LeadingChunk' in 'leading_chunks' and, if found, copying the file path, line range, and chunk content into the excerpt. [crates/gcode/src/commands/codewiki/types.rs:33-45]
- `ranked_source_excerpts` (function) component `ranked_source_excerpts [function]` (`290bf764-4b55-5161-a203-1e366182a74e`) lines 50-62 [crates/gcode/src/commands/codewiki/types.rs:50-62]
  - Signature: `pub(crate) fn ranked_source_excerpts<'a>(`
  - Purpose: Collects candidate 'FileDoc's into a vector, sorts them by descending symbol count then ascending path, maps each to a 'SourceExcerpt' via 'source_excerpt_for_file' when leading chunks exist, and returns the first 'limit' excerpts. [crates/gcode/src/commands/codewiki/types.rs:50-62]
- `CodewikiGraphEdge` (class) component `CodewikiGraphEdge [class]` (`06869467-725b-5860-a126-1cfee1947014`) lines 65-69 [crates/gcode/src/commands/codewiki/types.rs:65-69]
  - Signature: `pub struct CodewikiGraphEdge {`
  - Purpose: 'CodewikiGraphEdge' is a struct representing a directed graph edge between two components, identified by 'source_component_id' and 'target_component_id', with an associated 'kind' of type 'CodewikiGraphEdgeKind'. [crates/gcode/src/commands/codewiki/types.rs:65-69]
- `CodewikiGraphEdge` (class) component `CodewikiGraphEdge [class]` (`7b2662e7-c5ec-53a2-b840-b18c7f5cd82b`) lines 71-93 [crates/gcode/src/commands/codewiki/types.rs:71-93]
  - Signature: `impl CodewikiGraphEdge {`
  - Purpose: Indexed class `CodewikiGraphEdge` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:71-93]
- `CodewikiGraphEdge.call` (method) component `CodewikiGraphEdge.call [method]` (`7abffc1a-d8d6-5d9c-81e3-d4a386d22a1e`) lines 72-81 [crates/gcode/src/commands/codewiki/types.rs:72-81]
  - Signature: `pub fn call(`
  - Purpose: Indexed method `CodewikiGraphEdge.call` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:72-81]
- `CodewikiGraphEdge.import` (method) component `CodewikiGraphEdge.import [method]` (`5e433050-7f6e-5d16-be55-99acacb43556`) lines 83-92 [crates/gcode/src/commands/codewiki/types.rs:83-92]
  - Signature: `pub fn import(`
  - Purpose: Indexed method `CodewikiGraphEdge.import` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:83-92]
- `CodewikiGraphEdgeKind` (type) component `CodewikiGraphEdgeKind [type]` (`ccf65d27-9f18-583f-ba34-20f48cc9233a`) lines 96-99 [crates/gcode/src/commands/codewiki/types.rs:96-99]
  - Signature: `pub enum CodewikiGraphEdgeKind {`
  - Purpose: Indexed type `CodewikiGraphEdgeKind` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:96-99]
- `CodewikiGraph` (class) component `CodewikiGraph [class]` (`0e5f4ca7-1e31-5ae4-b7c5-237e470fefa5`) lines 102-105 [crates/gcode/src/commands/codewiki/types.rs:102-105]
  - Signature: `pub(crate) struct CodewikiGraph {`
  - Purpose: Indexed class `CodewikiGraph` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:102-105]
- `CodewikiGraph` (class) component `CodewikiGraph [class]` (`32c38a11-747d-5bdf-bfaf-884842979097`) lines 107-128 [crates/gcode/src/commands/codewiki/types.rs:107-128]
  - Signature: `impl CodewikiGraph {`
  - Purpose: Indexed class `CodewikiGraph` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:107-128]
- `CodewikiGraph.available` (method) component `CodewikiGraph.available [method]` (`15350b7d-e950-5162-ada0-df93298aa283`) lines 108-113 [crates/gcode/src/commands/codewiki/types.rs:108-113]
  - Signature: `pub(crate) fn available(edges: Vec<CodewikiGraphEdge>) -> Self {`
  - Purpose: Indexed method `CodewikiGraph.available` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:108-113]
- `CodewikiGraph.truncated` (method) component `CodewikiGraph.truncated [method]` (`2d7b0f06-205b-5ea7-b4e2-dd7713944d6d`) lines 115-120 [crates/gcode/src/commands/codewiki/types.rs:115-120]
  - Signature: `pub(crate) fn truncated(edges: Vec<CodewikiGraphEdge>) -> Self {`
  - Purpose: Indexed method `CodewikiGraph.truncated` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:115-120]
- `CodewikiGraph.unavailable` (method) component `CodewikiGraph.unavailable [method]` (`38f1ee1d-3d9f-5f3a-89ad-6d31a73b8007`) lines 122-127 [crates/gcode/src/commands/codewiki/types.rs:122-127]
  - Signature: `pub(crate) fn unavailable() -> Self {`
  - Purpose: Indexed method `CodewikiGraph.unavailable` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:122-127]
- `CodewikiGraphAvailability` (type) component `CodewikiGraphAvailability [type]` (`03b9a581-2471-5a6a-8627-5a02fe1dbe01`) lines 131-135 [crates/gcode/src/commands/codewiki/types.rs:131-135]
  - Signature: `pub enum CodewikiGraphAvailability {`
  - Purpose: Indexed type `CodewikiGraphAvailability` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:131-135]
- `FileDoc` (class) component `FileDoc [class]` (`ccb940b9-5f60-5baa-803b-62aa7cb17627`) lines 138-150 [crates/gcode/src/commands/codewiki/types.rs:138-150]
  - Signature: `pub(crate) struct FileDoc {`
  - Purpose: Indexed class `FileDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:138-150]
- `SymbolDoc` (class) component `SymbolDoc [class]` (`0712afd5-bfac-5b8d-90c6-952f393d33a5`) lines 153-159 [crates/gcode/src/commands/codewiki/types.rs:153-159]
  - Signature: `pub(crate) struct SymbolDoc {`
  - Purpose: 'SymbolDoc' is a crate-visible record that associates a 'Symbol' with its documented purpose, owning component identifiers and labels, and the 'SourceSpan' where it is defined. [crates/gcode/src/commands/codewiki/types.rs:153-159]
- `ModuleDoc` (class) component `ModuleDoc [class]` (`4bcaa055-ec29-57ec-bc24-be7dce48a12d`) lines 162-177 [crates/gcode/src/commands/codewiki/types.rs:162-177]
  - Signature: `pub(crate) struct ModuleDoc {`
  - Purpose: Indexed class `ModuleDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:162-177]
- `ArchitectureDoc` (class) component `ArchitectureDoc [class]` (`37d25365-97db-5f59-b3f4-85d69cb7b66c`) lines 180-186 [crates/gcode/src/commands/codewiki/types.rs:180-186]
  - Signature: `pub(crate) struct ArchitectureDoc {`
  - Purpose: Indexed class `ArchitectureDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:180-186]
- `ArchitectureSubsystem` (class) component `ArchitectureSubsystem [class]` (`0bd3c2b3-21f7-52ac-9d62-ae2163ba8010`) lines 189-194 [crates/gcode/src/commands/codewiki/types.rs:189-194]
  - Signature: `pub(crate) struct ArchitectureSubsystem {`
  - Purpose: 'ArchitectureSubsystem' is an internal struct that models a subsystem of the architecture by storing its module name, responsibility description, child module names, and associated source spans. [crates/gcode/src/commands/codewiki/types.rs:189-194]
- `OnboardingDoc` (class) component `OnboardingDoc [class]` (`a7be7f75-cbaa-53fd-89d8-023e0e759ccf`) lines 197-202 [crates/gcode/src/commands/codewiki/types.rs:197-202]
  - Signature: `pub(crate) struct OnboardingDoc {`
  - Purpose: 'OnboardingDoc' is an internal onboarding-document container that groups source-span provenance, ordered entry points, a sequenced reading plan, and a list of degraded source identifiers. [crates/gcode/src/commands/codewiki/types.rs:197-202]
- `OnboardingEntryPoint` (class) component `OnboardingEntryPoint [class]` (`17fbb5db-f369-5962-935c-dc929ff6071a`) lines 205-209 [crates/gcode/src/commands/codewiki/types.rs:205-209]
  - Signature: `pub(crate) struct OnboardingEntryPoint {`
  - Purpose: Indexed class `OnboardingEntryPoint` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:205-209]
- `OnboardingStep` (class) component `OnboardingStep [class]` (`86c92c70-bb58-5f4b-8fbd-a0fb7b45c49e`) lines 212-217 [crates/gcode/src/commands/codewiki/types.rs:212-217]
  - Signature: `pub(crate) struct OnboardingStep {`
  - Purpose: Indexed class `OnboardingStep` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:212-217]
- `HotspotsDoc` (class) component `HotspotsDoc [class]` (`3541c462-4f7a-5228-b8d9-f105727b08b0`) lines 220-226 [crates/gcode/src/commands/codewiki/types.rs:220-226]
  - Signature: `pub(crate) struct HotspotsDoc {`
  - Purpose: Indexed class `HotspotsDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:220-226]
- `HotspotFinding` (class) component `HotspotFinding [class]` (`ed07f8f0-0b4e-5789-ba2b-2b2a942eb825`) lines 229-235 [crates/gcode/src/commands/codewiki/types.rs:229-235]
  - Signature: `pub(crate) struct HotspotFinding {`
  - Purpose: Indexed class `HotspotFinding` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:229-235]
- `HotspotNode` (class) component `HotspotNode [class]` (`633440f2-54ae-581a-be45-b0d660da08c2`) lines 238-245 [crates/gcode/src/commands/codewiki/types.rs:238-245]
  - Signature: `pub(crate) struct HotspotNode {`
  - Purpose: Indexed class `HotspotNode` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:238-245]
- `FileLink` (class) component `FileLink [class]` (`a894167d-5cc7-5cce-812d-9b1d4a66cdfc`) lines 248-252 [crates/gcode/src/commands/codewiki/types.rs:248-252]
  - Signature: `pub(crate) struct FileLink {`
  - Purpose: Indexed class `FileLink` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:248-252]
- `ModuleLink` (class) component `ModuleLink [class]` (`63896419-ca38-5388-8809-7ee9235e872d`) lines 255-259 [crates/gcode/src/commands/codewiki/types.rs:255-259]
  - Signature: `pub(crate) struct ModuleLink {`
  - Purpose: Indexed class `ModuleLink` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:255-259]
- `SourceSpan` (class) component `SourceSpan [class]` (`8b708ae7-f26b-5ad2-bc7b-91c9ab89818a`) lines 262-266 [crates/gcode/src/commands/codewiki/types.rs:262-266]
  - Signature: `pub(crate) struct SourceSpan {`
  - Purpose: Indexed class `SourceSpan` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:262-266]
- `CodewikiRunSummary` (class) component `CodewikiRunSummary [class]` (`f56f0cea-c2df-533f-8dc5-03ff0c2a7c65`) lines 269-281 [crates/gcode/src/commands/codewiki/types.rs:269-281]
  - Signature: `pub struct CodewikiRunSummary {`
  - Purpose: Indexed class `CodewikiRunSummary` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:269-281]
- `CodewikiMeta` (class) component `CodewikiMeta [class]` (`504f3a78-3d37-549f-a6aa-fcaf42792837`) lines 284-291 [crates/gcode/src/commands/codewiki/types.rs:284-291]
  - Signature: `pub(crate) struct CodewikiMeta {`
  - Purpose: Indexed class `CodewikiMeta` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:284-291]
- `CodewikiDocMeta` (class) component `CodewikiDocMeta [class]` (`f7061147-bbcb-53e2-92f5-ae21acd3606d`) lines 294-310 [crates/gcode/src/commands/codewiki/types.rs:294-310]
  - Signature: `pub(crate) struct CodewikiDocMeta {`
  - Purpose: Indexed class `CodewikiDocMeta` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:294-310]
- `BuiltDoc` (class) component `BuiltDoc [class]` (`d5d0d2ac-5f9b-54ab-abf3-6db45a8c4f3e`) lines 315-322 [crates/gcode/src/commands/codewiki/types.rs:315-322]
  - Signature: `pub(crate) struct BuiltDoc {`
  - Purpose: Indexed class `BuiltDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:315-322]
- `BuiltDoc` (class) component `BuiltDoc [class]` (`030cd5dd-5bcc-53c5-9017-2dcb5401ad4a`) lines 324-333 [crates/gcode/src/commands/codewiki/types.rs:324-333]
  - Signature: `impl BuiltDoc {`
  - Purpose: Indexed class `BuiltDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:324-333]
- `BuiltDoc.healthy` (method) component `BuiltDoc.healthy [method]` (`bd27cac4-5be6-5543-90cc-685e3c8d8d92`) lines 325-332 [crates/gcode/src/commands/codewiki/types.rs:325-332]
  - Signature: `pub(crate) fn healthy(path: impl Into<String>, content: String) -> Self {`
  - Purpose: Indexed method `BuiltDoc.healthy` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:325-332]
- `CodewikiIndexSnapshot` (class) component `CodewikiIndexSnapshot [class]` (`793ba19c-7242-593a-907b-4ad6b323efcb`) lines 336-343 [crates/gcode/src/commands/codewiki/types.rs:336-343]
  - Signature: `pub(crate) struct CodewikiIndexSnapshot {`
  - Purpose: Indexed class `CodewikiIndexSnapshot` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:336-343]
- `CodewikiFileSnapshot` (class) component `CodewikiFileSnapshot [class]` (`494dd863-11df-5506-9dad-48c6b877e7c1`) lines 346-349 [crates/gcode/src/commands/codewiki/types.rs:346-349]
  - Signature: `pub(crate) struct CodewikiFileSnapshot {`
  - Purpose: Indexed class `CodewikiFileSnapshot` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:346-349]
- `CodewikiSymbolSnapshot` (class) component `CodewikiSymbolSnapshot [class]` (`18fc5913-7e9e-57a4-bcba-4d2398ff5eff`) lines 352-358 [crates/gcode/src/commands/codewiki/types.rs:352-358]
  - Signature: `pub(crate) struct CodewikiSymbolSnapshot {`
  - Purpose: Indexed class `CodewikiSymbolSnapshot` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:352-358]
- `TextGenerator` (type) component `TextGenerator [type]` (`171182a3-aba5-577e-bb4b-f01e9f2d081d`) lines 360-360 [crates/gcode/src/commands/codewiki/types.rs:360]
  - Signature: `pub type TextGenerator<'a> = dyn FnMut(&str, &str, PromptTier) -> Option<String> + 'a;`
  - Purpose: Indexed type `TextGenerator` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:360]
- `PromptTier` (type) component `PromptTier [type]` (`775ad8cb-114d-5e08-b108-759267d436a7`) lines 367-371 [crates/gcode/src/commands/codewiki/types.rs:367-371]
  - Signature: `pub enum PromptTier {`
  - Purpose: Indexed type `PromptTier` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:367-371]
- `AiDepth` (type) component `AiDepth [type]` (`76429f2b-9a3b-58a4-b596-b69d2e28ed0f`) lines 376-384 [crates/gcode/src/commands/codewiki/types.rs:376-384]
  - Signature: `pub enum AiDepth {`
  - Purpose: Indexed type `AiDepth` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:376-384]
- `AiDepth` (class) component `AiDepth [class]` (`6b40e790-5306-593a-a9a9-e71dcd29ee28`) lines 386-402 [crates/gcode/src/commands/codewiki/types.rs:386-402]
  - Signature: `impl AiDepth {`
  - Purpose: Indexed class `AiDepth` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:386-402]
- `AiDepth.includes_files` (method) component `AiDepth.includes_files [method]` (`251ce9e7-d898-5de7-8dfa-028259086f2a`) lines 387-389 [crates/gcode/src/commands/codewiki/types.rs:387-389]
  - Signature: `pub(crate) fn includes_files(self) -> bool {`
  - Purpose: Indexed method `AiDepth.includes_files` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:387-389]
- `AiDepth.includes_symbols` (method) component `AiDepth.includes_symbols [method]` (`8431e4de-af95-5aca-90c1-f84c941ec1de`) lines 391-393 [crates/gcode/src/commands/codewiki/types.rs:391-393]
  - Signature: `pub(crate) fn includes_symbols(self) -> bool {`
  - Purpose: Indexed method `AiDepth.includes_symbols` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:391-393]
- `AiDepth.mode_label` (method) component `AiDepth.mode_label [method]` (`bb847fd1-570b-54b4-b37f-8068f7a1ba43`) lines 395-401 [crates/gcode/src/commands/codewiki/types.rs:395-401]
  - Signature: `pub(crate) fn mode_label(self) -> &'static str {`
  - Purpose: Indexed method `AiDepth.mode_label` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:395-401]
- `CodewikiAiOptions` (class) component `CodewikiAiOptions [class]` (`3a3d4aa7-70ec-5909-ab11-086db68ceee7`) lines 405-411 [crates/gcode/src/commands/codewiki/types.rs:405-411]
  - Signature: `pub struct CodewikiAiOptions {`
  - Purpose: Indexed class `CodewikiAiOptions` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:405-411]
- `SourceSpan` (class) component `SourceSpan [class]` (`09f67506-3dbc-52a9-b829-52768fe243e2`) lines 413-433 [crates/gcode/src/commands/codewiki/types.rs:413-433]
  - Signature: `impl SourceSpan {`
  - Purpose: Indexed class `SourceSpan` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:413-433]
- `SourceSpan.from_symbol` (method) component `SourceSpan.from_symbol [method]` (`6f8366d7-bda3-5793-be52-e399e2ea7d5e`) lines 414-420 [crates/gcode/src/commands/codewiki/types.rs:414-420]
  - Signature: `pub(crate) fn from_symbol(symbol: &Symbol) -> Self {`
  - Purpose: Indexed method `SourceSpan.from_symbol` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:414-420]
- `SourceSpan.citation` (method) component `SourceSpan.citation [method]` (`9970adb8-373b-5a21-92dd-a78d5ae4ee58`) lines 422-428 [crates/gcode/src/commands/codewiki/types.rs:422-428]
  - Signature: `pub(crate) fn citation(&self) -> String {`
  - Purpose: Indexed method `SourceSpan.citation` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:422-428]
- `SourceSpan.contains` (method) component `SourceSpan.contains [method]` (`95d68642-1786-5da5-ad81-ff8ae5ed68da`) lines 430-432 [crates/gcode/src/commands/codewiki/types.rs:430-432]
  - Signature: `pub(crate) fn contains(&self, file: &str, line_start: usize, line_end: usize) -> bool {`
  - Purpose: Indexed method `SourceSpan.contains` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:430-432]

