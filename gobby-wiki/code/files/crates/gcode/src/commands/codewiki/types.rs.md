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
  - 72-81
  - 83-92
  - 96-99
  - 102-105
  - 108-113
  - 115-120
  - 122-127
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
  - 294-314
  - 319-326
  - 329-336
  - 340-347
  - 350-353
  - 356-362
  - '364'
  - 371-375
  - 380-388
  - 391-393
  - 395-397
  - 399-405
  - 409-415
  - 418-424
  - 426-432
  - 434-436
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/types.rs:11-21](crates/gcode/src/commands/codewiki/types.rs#L11-L21), [crates/gcode/src/commands/codewiki/types.rs:26-30](crates/gcode/src/commands/codewiki/types.rs#L26-L30), [crates/gcode/src/commands/codewiki/types.rs:33-45](crates/gcode/src/commands/codewiki/types.rs#L33-L45), [crates/gcode/src/commands/codewiki/types.rs:50-62](crates/gcode/src/commands/codewiki/types.rs#L50-L62), [crates/gcode/src/commands/codewiki/types.rs:65-69](crates/gcode/src/commands/codewiki/types.rs#L65-L69), [crates/gcode/src/commands/codewiki/types.rs:72-81](crates/gcode/src/commands/codewiki/types.rs#L72-L81), [crates/gcode/src/commands/codewiki/types.rs:83-92](crates/gcode/src/commands/codewiki/types.rs#L83-L92), [crates/gcode/src/commands/codewiki/types.rs:96-99](crates/gcode/src/commands/codewiki/types.rs#L96-L99), [crates/gcode/src/commands/codewiki/types.rs:102-105](crates/gcode/src/commands/codewiki/types.rs#L102-L105), [crates/gcode/src/commands/codewiki/types.rs:108-113](crates/gcode/src/commands/codewiki/types.rs#L108-L113), [crates/gcode/src/commands/codewiki/types.rs:115-120](crates/gcode/src/commands/codewiki/types.rs#L115-L120), [crates/gcode/src/commands/codewiki/types.rs:122-127](crates/gcode/src/commands/codewiki/types.rs#L122-L127), [crates/gcode/src/commands/codewiki/types.rs:131-135](crates/gcode/src/commands/codewiki/types.rs#L131-L135), [crates/gcode/src/commands/codewiki/types.rs:138-150](crates/gcode/src/commands/codewiki/types.rs#L138-L150), [crates/gcode/src/commands/codewiki/types.rs:153-159](crates/gcode/src/commands/codewiki/types.rs#L153-L159), [crates/gcode/src/commands/codewiki/types.rs:162-177](crates/gcode/src/commands/codewiki/types.rs#L162-L177), [crates/gcode/src/commands/codewiki/types.rs:180-186](crates/gcode/src/commands/codewiki/types.rs#L180-L186), [crates/gcode/src/commands/codewiki/types.rs:189-194](crates/gcode/src/commands/codewiki/types.rs#L189-L194), [crates/gcode/src/commands/codewiki/types.rs:197-202](crates/gcode/src/commands/codewiki/types.rs#L197-L202), [crates/gcode/src/commands/codewiki/types.rs:205-209](crates/gcode/src/commands/codewiki/types.rs#L205-L209), [crates/gcode/src/commands/codewiki/types.rs:212-217](crates/gcode/src/commands/codewiki/types.rs#L212-L217), [crates/gcode/src/commands/codewiki/types.rs:220-226](crates/gcode/src/commands/codewiki/types.rs#L220-L226), [crates/gcode/src/commands/codewiki/types.rs:229-235](crates/gcode/src/commands/codewiki/types.rs#L229-L235), [crates/gcode/src/commands/codewiki/types.rs:238-245](crates/gcode/src/commands/codewiki/types.rs#L238-L245), [crates/gcode/src/commands/codewiki/types.rs:248-252](crates/gcode/src/commands/codewiki/types.rs#L248-L252), [crates/gcode/src/commands/codewiki/types.rs:255-259](crates/gcode/src/commands/codewiki/types.rs#L255-L259), [crates/gcode/src/commands/codewiki/types.rs:262-266](crates/gcode/src/commands/codewiki/types.rs#L262-L266), [crates/gcode/src/commands/codewiki/types.rs:269-281](crates/gcode/src/commands/codewiki/types.rs#L269-L281), [crates/gcode/src/commands/codewiki/types.rs:284-291](crates/gcode/src/commands/codewiki/types.rs#L284-L291), [crates/gcode/src/commands/codewiki/types.rs:294-314](crates/gcode/src/commands/codewiki/types.rs#L294-L314), [crates/gcode/src/commands/codewiki/types.rs:319-326](crates/gcode/src/commands/codewiki/types.rs#L319-L326), [crates/gcode/src/commands/codewiki/types.rs:329-336](crates/gcode/src/commands/codewiki/types.rs#L329-L336), [crates/gcode/src/commands/codewiki/types.rs:340-347](crates/gcode/src/commands/codewiki/types.rs#L340-L347), [crates/gcode/src/commands/codewiki/types.rs:350-353](crates/gcode/src/commands/codewiki/types.rs#L350-L353), [crates/gcode/src/commands/codewiki/types.rs:356-362](crates/gcode/src/commands/codewiki/types.rs#L356-L362), [crates/gcode/src/commands/codewiki/types.rs:364](crates/gcode/src/commands/codewiki/types.rs#L364), [crates/gcode/src/commands/codewiki/types.rs:371-375](crates/gcode/src/commands/codewiki/types.rs#L371-L375), [crates/gcode/src/commands/codewiki/types.rs:380-388](crates/gcode/src/commands/codewiki/types.rs#L380-L388), [crates/gcode/src/commands/codewiki/types.rs:391-393](crates/gcode/src/commands/codewiki/types.rs#L391-L393), [crates/gcode/src/commands/codewiki/types.rs:395-397](crates/gcode/src/commands/codewiki/types.rs#L395-L397), [crates/gcode/src/commands/codewiki/types.rs:399-405](crates/gcode/src/commands/codewiki/types.rs#L399-L405), [crates/gcode/src/commands/codewiki/types.rs:409-415](crates/gcode/src/commands/codewiki/types.rs#L409-L415), [crates/gcode/src/commands/codewiki/types.rs:418-424](crates/gcode/src/commands/codewiki/types.rs#L418-L424), [crates/gcode/src/commands/codewiki/types.rs:426-432](crates/gcode/src/commands/codewiki/types.rs#L426-L432), [crates/gcode/src/commands/codewiki/types.rs:434-436](crates/gcode/src/commands/codewiki/types.rs#L434-L436)

</details>

# crates/gcode/src/commands/codewiki/types.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file defines the core data types and helper methods used to build Codewiki prompts and document snapshots from indexed code. It starts with input and source-citation plumbing, including leading source chunks, excerpt extraction, and ranking excerpts from file docs by symbol density so the most informative files are chosen first.

It also models graph structure and availability, document types for files, symbols, modules, architecture, onboarding, hotspots, and build/run summaries, plus metadata and snapshot records for persisted index state. The remaining helpers classify AI depth and routing options, and `SourceSpan` ties symbols back to line-based citations and containment checks for provenance-aware output.
[crates/gcode/src/commands/codewiki/types.rs:11-21]
[crates/gcode/src/commands/codewiki/types.rs:26-30]
[crates/gcode/src/commands/codewiki/types.rs:33-45]
[crates/gcode/src/commands/codewiki/types.rs:50-62]
[crates/gcode/src/commands/codewiki/types.rs:65-69]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CodewikiInput` | class | `pub struct CodewikiInput {` | `CodewikiInput [class]` | `b6d93a42-87d9-5f50-8b57-7c348d37760b` | 11-21 [crates/gcode/src/commands/codewiki/types.rs:11-21] | Indexed class `CodewikiInput` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:11-21] |
| `LeadingChunk` | class | `pub struct LeadingChunk {` | `LeadingChunk [class]` | `e6ff09c9-e115-545b-b60e-57571e920938` | 26-30 [crates/gcode/src/commands/codewiki/types.rs:26-30] | Indexed class `LeadingChunk` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:26-30] |
| `source_excerpt_for_file` | function | `pub(crate) fn source_excerpt_for_file(` | `source_excerpt_for_file [function]` | `c4a94f1e-8ff9-570f-9607-04ed9b695c6b` | 33-45 [crates/gcode/src/commands/codewiki/types.rs:33-45] | Indexed function `source_excerpt_for_file` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:33-45] |
| `ranked_source_excerpts` | function | `pub(crate) fn ranked_source_excerpts<'a>(` | `ranked_source_excerpts [function]` | `290bf764-4b55-5161-a203-1e366182a74e` | 50-62 [crates/gcode/src/commands/codewiki/types.rs:50-62] | Indexed function `ranked_source_excerpts` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:50-62] |
| `CodewikiGraphEdge` | class | `pub struct CodewikiGraphEdge {` | `CodewikiGraphEdge [class]` | `06869467-725b-5860-a126-1cfee1947014` | 65-69 [crates/gcode/src/commands/codewiki/types.rs:65-69] | Indexed class `CodewikiGraphEdge` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:65-69] |
| `CodewikiGraphEdge::call` | method | `pub fn call(` | `CodewikiGraphEdge::call [method]` | `7abffc1a-d8d6-5d9c-81e3-d4a386d22a1e` | 72-81 [crates/gcode/src/commands/codewiki/types.rs:72-81] | Indexed method `CodewikiGraphEdge::call` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:72-81] |
| `CodewikiGraphEdge::import` | method | `pub fn import(` | `CodewikiGraphEdge::import [method]` | `5e433050-7f6e-5d16-be55-99acacb43556` | 83-92 [crates/gcode/src/commands/codewiki/types.rs:83-92] | Indexed method `CodewikiGraphEdge::import` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:83-92] |
| `CodewikiGraphEdgeKind` | type | `pub enum CodewikiGraphEdgeKind {` | `CodewikiGraphEdgeKind [type]` | `ccf65d27-9f18-583f-ba34-20f48cc9233a` | 96-99 [crates/gcode/src/commands/codewiki/types.rs:96-99] | Indexed type `CodewikiGraphEdgeKind` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:96-99] |
| `CodewikiGraph` | class | `pub(crate) struct CodewikiGraph {` | `CodewikiGraph [class]` | `0e5f4ca7-1e31-5ae4-b7c5-237e470fefa5` | 102-105 [crates/gcode/src/commands/codewiki/types.rs:102-105] | Indexed class `CodewikiGraph` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:102-105] |
| `CodewikiGraph::available` | method | `pub(crate) fn available(edges: Vec<CodewikiGraphEdge>) -> Self {` | `CodewikiGraph::available [method]` | `15350b7d-e950-5162-ada0-df93298aa283` | 108-113 [crates/gcode/src/commands/codewiki/types.rs:108-113] | Indexed method `CodewikiGraph::available` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:108-113] |
| `CodewikiGraph::truncated` | method | `pub(crate) fn truncated(edges: Vec<CodewikiGraphEdge>) -> Self {` | `CodewikiGraph::truncated [method]` | `2d7b0f06-205b-5ea7-b4e2-dd7713944d6d` | 115-120 [crates/gcode/src/commands/codewiki/types.rs:115-120] | Indexed method `CodewikiGraph::truncated` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:115-120] |
| `CodewikiGraph::unavailable` | method | `pub(crate) fn unavailable() -> Self {` | `CodewikiGraph::unavailable [method]` | `38f1ee1d-3d9f-5f3a-89ad-6d31a73b8007` | 122-127 [crates/gcode/src/commands/codewiki/types.rs:122-127] | Indexed method `CodewikiGraph::unavailable` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:122-127] |
| `CodewikiGraphAvailability` | type | `pub enum CodewikiGraphAvailability {` | `CodewikiGraphAvailability [type]` | `03b9a581-2471-5a6a-8627-5a02fe1dbe01` | 131-135 [crates/gcode/src/commands/codewiki/types.rs:131-135] | Indexed type `CodewikiGraphAvailability` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:131-135] |
| `FileDoc` | class | `pub(crate) struct FileDoc {` | `FileDoc [class]` | `ccb940b9-5f60-5baa-803b-62aa7cb17627` | 138-150 [crates/gcode/src/commands/codewiki/types.rs:138-150] | Indexed class `FileDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:138-150] |
| `SymbolDoc` | class | `pub(crate) struct SymbolDoc {` | `SymbolDoc [class]` | `0712afd5-bfac-5b8d-90c6-952f393d33a5` | 153-159 [crates/gcode/src/commands/codewiki/types.rs:153-159] | Indexed class `SymbolDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:153-159] |
| `ModuleDoc` | class | `pub(crate) struct ModuleDoc {` | `ModuleDoc [class]` | `4bcaa055-ec29-57ec-bc24-be7dce48a12d` | 162-177 [crates/gcode/src/commands/codewiki/types.rs:162-177] | Indexed class `ModuleDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:162-177] |
| `ArchitectureDoc` | class | `pub(crate) struct ArchitectureDoc {` | `ArchitectureDoc [class]` | `37d25365-97db-5f59-b3f4-85d69cb7b66c` | 180-186 [crates/gcode/src/commands/codewiki/types.rs:180-186] | Indexed class `ArchitectureDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:180-186] |
| `ArchitectureSubsystem` | class | `pub(crate) struct ArchitectureSubsystem {` | `ArchitectureSubsystem [class]` | `0bd3c2b3-21f7-52ac-9d62-ae2163ba8010` | 189-194 [crates/gcode/src/commands/codewiki/types.rs:189-194] | Indexed class `ArchitectureSubsystem` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:189-194] |
| `OnboardingDoc` | class | `pub(crate) struct OnboardingDoc {` | `OnboardingDoc [class]` | `a7be7f75-cbaa-53fd-89d8-023e0e759ccf` | 197-202 [crates/gcode/src/commands/codewiki/types.rs:197-202] | Indexed class `OnboardingDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:197-202] |
| `OnboardingEntryPoint` | class | `pub(crate) struct OnboardingEntryPoint {` | `OnboardingEntryPoint [class]` | `17fbb5db-f369-5962-935c-dc929ff6071a` | 205-209 [crates/gcode/src/commands/codewiki/types.rs:205-209] | Indexed class `OnboardingEntryPoint` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:205-209] |
| `OnboardingStep` | class | `pub(crate) struct OnboardingStep {` | `OnboardingStep [class]` | `86c92c70-bb58-5f4b-8fbd-a0fb7b45c49e` | 212-217 [crates/gcode/src/commands/codewiki/types.rs:212-217] | Indexed class `OnboardingStep` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:212-217] |
| `HotspotsDoc` | class | `pub(crate) struct HotspotsDoc {` | `HotspotsDoc [class]` | `3541c462-4f7a-5228-b8d9-f105727b08b0` | 220-226 [crates/gcode/src/commands/codewiki/types.rs:220-226] | Indexed class `HotspotsDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:220-226] |
| `HotspotFinding` | class | `pub(crate) struct HotspotFinding {` | `HotspotFinding [class]` | `ed07f8f0-0b4e-5789-ba2b-2b2a942eb825` | 229-235 [crates/gcode/src/commands/codewiki/types.rs:229-235] | Indexed class `HotspotFinding` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:229-235] |
| `HotspotNode` | class | `pub(crate) struct HotspotNode {` | `HotspotNode [class]` | `633440f2-54ae-581a-be45-b0d660da08c2` | 238-245 [crates/gcode/src/commands/codewiki/types.rs:238-245] | Indexed class `HotspotNode` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:238-245] |
| `FileLink` | class | `pub(crate) struct FileLink {` | `FileLink [class]` | `a894167d-5cc7-5cce-812d-9b1d4a66cdfc` | 248-252 [crates/gcode/src/commands/codewiki/types.rs:248-252] | Indexed class `FileLink` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:248-252] |
| `ModuleLink` | class | `pub(crate) struct ModuleLink {` | `ModuleLink [class]` | `63896419-ca38-5388-8809-7ee9235e872d` | 255-259 [crates/gcode/src/commands/codewiki/types.rs:255-259] | Indexed class `ModuleLink` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:255-259] |
| `SourceSpan` | class | `pub(crate) struct SourceSpan {` | `SourceSpan [class]` | `8b708ae7-f26b-5ad2-bc7b-91c9ab89818a` | 262-266 [crates/gcode/src/commands/codewiki/types.rs:262-266] | Indexed class `SourceSpan` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:262-266] |
| `CodewikiRunSummary` | class | `pub struct CodewikiRunSummary {` | `CodewikiRunSummary [class]` | `f56f0cea-c2df-533f-8dc5-03ff0c2a7c65` | 269-281 [crates/gcode/src/commands/codewiki/types.rs:269-281] | Indexed class `CodewikiRunSummary` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:269-281] |
| `CodewikiMeta` | class | `pub(crate) struct CodewikiMeta {` | `CodewikiMeta [class]` | `504f3a78-3d37-549f-a6aa-fcaf42792837` | 284-291 [crates/gcode/src/commands/codewiki/types.rs:284-291] | Indexed class `CodewikiMeta` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:284-291] |
| `CodewikiDocMeta` | class | `pub(crate) struct CodewikiDocMeta {` | `CodewikiDocMeta [class]` | `f7061147-bbcb-53e2-92f5-ae21acd3606d` | 294-314 [crates/gcode/src/commands/codewiki/types.rs:294-314] | Indexed class `CodewikiDocMeta` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:294-314] |
| `BuiltDoc` | class | `pub(crate) struct BuiltDoc {` | `BuiltDoc [class]` | `ccaa3743-3c5a-5494-a404-efc37b205245` | 319-326 [crates/gcode/src/commands/codewiki/types.rs:319-326] | Indexed class `BuiltDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:319-326] |
| `BuiltDoc::healthy` | method | `pub(crate) fn healthy(path: impl Into<String>, content: String) -> Self {` | `BuiltDoc::healthy [method]` | `3a814d08-7656-50e8-958b-cead1cccd2eb` | 329-336 [crates/gcode/src/commands/codewiki/types.rs:329-336] | Indexed method `BuiltDoc::healthy` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:329-336] |
| `CodewikiIndexSnapshot` | class | `pub(crate) struct CodewikiIndexSnapshot {` | `CodewikiIndexSnapshot [class]` | `c36c41c1-e8d2-51bb-9b5b-414de9a0c0fe` | 340-347 [crates/gcode/src/commands/codewiki/types.rs:340-347] | Indexed class `CodewikiIndexSnapshot` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:340-347] |
| `CodewikiFileSnapshot` | class | `pub(crate) struct CodewikiFileSnapshot {` | `CodewikiFileSnapshot [class]` | `80c79020-f171-5afd-bbfa-cb699ede9f7c` | 350-353 [crates/gcode/src/commands/codewiki/types.rs:350-353] | Indexed class `CodewikiFileSnapshot` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:350-353] |
| `CodewikiSymbolSnapshot` | class | `pub(crate) struct CodewikiSymbolSnapshot {` | `CodewikiSymbolSnapshot [class]` | `147def03-d3ac-5deb-be87-ddb00d427725` | 356-362 [crates/gcode/src/commands/codewiki/types.rs:356-362] | Indexed class `CodewikiSymbolSnapshot` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:356-362] |
| `TextGenerator` | type | `pub type TextGenerator<'a> = dyn FnMut(&str, &str, PromptTier) -> Option<String> + 'a;` | `TextGenerator [type]` | `23ad346b-458e-5a95-b8bc-4d1dfd7b3a01` | 364-364 [crates/gcode/src/commands/codewiki/types.rs:364] | Indexed type `TextGenerator` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:364] |
| `PromptTier` | type | `pub enum PromptTier {` | `PromptTier [type]` | `253a839e-f70d-5708-a3cc-52d2b5067543` | 371-375 [crates/gcode/src/commands/codewiki/types.rs:371-375] | Indexed type `PromptTier` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:371-375] |
| `AiDepth` | type | `pub enum AiDepth {` | `AiDepth [type]` | `1a8ee948-e40e-5f9a-a273-655ecebf258e` | 380-388 [crates/gcode/src/commands/codewiki/types.rs:380-388] | Indexed type `AiDepth` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:380-388] |
| `AiDepth::includes_files` | method | `pub(crate) fn includes_files(self) -> bool {` | `AiDepth::includes_files [method]` | `0f67992c-40b3-514b-bf43-1c9f8c2cc0d5` | 391-393 [crates/gcode/src/commands/codewiki/types.rs:391-393] | Indexed method `AiDepth::includes_files` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:391-393] |
| `AiDepth::includes_symbols` | method | `pub(crate) fn includes_symbols(self) -> bool {` | `AiDepth::includes_symbols [method]` | `fe2ae5fd-cc7e-5562-a2dc-e2c30d55b5a5` | 395-397 [crates/gcode/src/commands/codewiki/types.rs:395-397] | Indexed method `AiDepth::includes_symbols` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:395-397] |
| `AiDepth::mode_label` | method | `pub(crate) fn mode_label(self) -> &'static str {` | `AiDepth::mode_label [method]` | `8983d67e-dd64-5db5-ac60-61cfac436d32` | 399-405 [crates/gcode/src/commands/codewiki/types.rs:399-405] | Indexed method `AiDepth::mode_label` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:399-405] |
| `CodewikiAiOptions` | class | `pub struct CodewikiAiOptions {` | `CodewikiAiOptions [class]` | `f94b35e8-470e-5fc7-9669-da9a89715e51` | 409-415 [crates/gcode/src/commands/codewiki/types.rs:409-415] | Indexed class `CodewikiAiOptions` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:409-415] |
| `SourceSpan::from_symbol` | method | `pub(crate) fn from_symbol(symbol: &Symbol) -> Self {` | `SourceSpan::from_symbol [method]` | `cb0e24c7-e27e-5b19-a2b1-bb05dd999aea` | 418-424 [crates/gcode/src/commands/codewiki/types.rs:418-424] | Indexed method `SourceSpan::from_symbol` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:418-424] |
| `SourceSpan::citation` | method | `pub(crate) fn citation(&self) -> String {` | `SourceSpan::citation [method]` | `d7a970dd-88da-5030-abc3-0ac5f9869f61` | 426-432 [crates/gcode/src/commands/codewiki/types.rs:426-432] | Indexed method `SourceSpan::citation` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:426-432] |
| `SourceSpan::contains` | method | `pub(crate) fn contains(&self, file: &str, line_start: usize, line_end: usize) -> bool {` | `SourceSpan::contains [method]` | `17bdb9c1-30ff-5686-b283-43b9968a13ab` | 434-436 [crates/gcode/src/commands/codewiki/types.rs:434-436] | Indexed method `SourceSpan::contains` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:434-436] |
