---
title: crates/gcode/src/models.rs
type: code_file
provenance:
- file: crates/gcode/src/models.rs
  ranges:
  - 19-24
  - 27-33
  - 35-42
  - 46-48
  - 53-66
  - 69-79
  - 81-83
  - 85-87
  - 89-91
  - 93-96
  - 98-101
  - 103-106
  - 108-111
  - 113-116
  - 118-123
  - 128-154
  - 159-168
  - 174-201
  - 204-213
  - 216-232
  - 235-238
  - 240-248
  - 252-261
  - 264-267
  - 272-282
  - 285-288
  - 293-296
  - 300-310
  - 313-320
  - 325-333
  - 336-351
  - 353-357
  - 359-368
  - 382-392
  - 394-408
  - 410-417
  - 421-435
  - 446-455
  - 459-477
  - 481-495
  - 498-504
  - 507-513
  - 517-524
  - 529-537
  - 541-549
  - 553-560
  - 567-615
  - 618-631
  - 633-644
  - 647-663
  - 666-702
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/models.rs:19-24](crates/gcode/src/models.rs#L19-L24), [crates/gcode/src/models.rs:27-33](crates/gcode/src/models.rs#L27-L33), [crates/gcode/src/models.rs:35-42](crates/gcode/src/models.rs#L35-L42), [crates/gcode/src/models.rs:46-48](crates/gcode/src/models.rs#L46-L48), [crates/gcode/src/models.rs:53-66](crates/gcode/src/models.rs#L53-L66), [crates/gcode/src/models.rs:69-79](crates/gcode/src/models.rs#L69-L79), [crates/gcode/src/models.rs:81-83](crates/gcode/src/models.rs#L81-L83), [crates/gcode/src/models.rs:85-87](crates/gcode/src/models.rs#L85-L87), [crates/gcode/src/models.rs:89-91](crates/gcode/src/models.rs#L89-L91), [crates/gcode/src/models.rs:93-96](crates/gcode/src/models.rs#L93-L96), [crates/gcode/src/models.rs:98-101](crates/gcode/src/models.rs#L98-L101), [crates/gcode/src/models.rs:103-106](crates/gcode/src/models.rs#L103-L106), [crates/gcode/src/models.rs:108-111](crates/gcode/src/models.rs#L108-L111), [crates/gcode/src/models.rs:113-116](crates/gcode/src/models.rs#L113-L116), [crates/gcode/src/models.rs:118-123](crates/gcode/src/models.rs#L118-L123), [crates/gcode/src/models.rs:128-154](crates/gcode/src/models.rs#L128-L154), [crates/gcode/src/models.rs:159-168](crates/gcode/src/models.rs#L159-L168), [crates/gcode/src/models.rs:174-201](crates/gcode/src/models.rs#L174-L201), [crates/gcode/src/models.rs:204-213](crates/gcode/src/models.rs#L204-L213), [crates/gcode/src/models.rs:216-232](crates/gcode/src/models.rs#L216-L232), [crates/gcode/src/models.rs:235-238](crates/gcode/src/models.rs#L235-L238), [crates/gcode/src/models.rs:240-248](crates/gcode/src/models.rs#L240-L248), [crates/gcode/src/models.rs:252-261](crates/gcode/src/models.rs#L252-L261), [crates/gcode/src/models.rs:264-267](crates/gcode/src/models.rs#L264-L267), [crates/gcode/src/models.rs:272-282](crates/gcode/src/models.rs#L272-L282), [crates/gcode/src/models.rs:285-288](crates/gcode/src/models.rs#L285-L288), [crates/gcode/src/models.rs:293-296](crates/gcode/src/models.rs#L293-L296), [crates/gcode/src/models.rs:300-310](crates/gcode/src/models.rs#L300-L310), [crates/gcode/src/models.rs:313-320](crates/gcode/src/models.rs#L313-L320), [crates/gcode/src/models.rs:325-333](crates/gcode/src/models.rs#L325-L333), [crates/gcode/src/models.rs:336-351](crates/gcode/src/models.rs#L336-L351), [crates/gcode/src/models.rs:353-357](crates/gcode/src/models.rs#L353-L357), [crates/gcode/src/models.rs:359-368](crates/gcode/src/models.rs#L359-L368), [crates/gcode/src/models.rs:382-392](crates/gcode/src/models.rs#L382-L392), [crates/gcode/src/models.rs:394-408](crates/gcode/src/models.rs#L394-L408), [crates/gcode/src/models.rs:410-417](crates/gcode/src/models.rs#L410-L417), [crates/gcode/src/models.rs:421-435](crates/gcode/src/models.rs#L421-L435), [crates/gcode/src/models.rs:446-455](crates/gcode/src/models.rs#L446-L455), [crates/gcode/src/models.rs:459-477](crates/gcode/src/models.rs#L459-L477), [crates/gcode/src/models.rs:481-495](crates/gcode/src/models.rs#L481-L495), [crates/gcode/src/models.rs:498-504](crates/gcode/src/models.rs#L498-L504), [crates/gcode/src/models.rs:507-513](crates/gcode/src/models.rs#L507-L513), [crates/gcode/src/models.rs:517-524](crates/gcode/src/models.rs#L517-L524), [crates/gcode/src/models.rs:529-537](crates/gcode/src/models.rs#L529-L537), [crates/gcode/src/models.rs:541-549](crates/gcode/src/models.rs#L541-L549), [crates/gcode/src/models.rs:553-560](crates/gcode/src/models.rs#L553-L560), [crates/gcode/src/models.rs:567-615](crates/gcode/src/models.rs#L567-L615), [crates/gcode/src/models.rs:618-631](crates/gcode/src/models.rs#L618-L631), [crates/gcode/src/models.rs:633-644](crates/gcode/src/models.rs#L633-L644), [crates/gcode/src/models.rs:647-663](crates/gcode/src/models.rs#L647-L663), [crates/gcode/src/models.rs:666-702](crates/gcode/src/models.rs#L666-L702)

</details>

# crates/gcode/src/models.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Defines the core gcode data models used for indexing, graph/search results, and serialization contracts. It establishes a stable UUID namespace and source-system tag, then uses `ProjectionProvenance` and `ProjectionMetadata` to label graph/projection facts with provenance, confidence, and source-location fields. `Symbol`, `IndexedFile`, `ContentChunk`, `CallRelation`, and related helpers build deterministic IDs and convert database rows into structured records, while utility types like `IndexedProject`, `SearchResult`, `GraphResult`, `ParseResult`, `IndexResult`, `PagedResponse`, and `ContentSearchHit` shape API responses. The file also includes logic for call-target classification and import resolution, plus tests that verify UUID generation and JSON serialization behavior.
[crates/gcode/src/models.rs:19-24]
[crates/gcode/src/models.rs:27-33]
[crates/gcode/src/models.rs:35-42]
[crates/gcode/src/models.rs:46-48]
[crates/gcode/src/models.rs:53-66]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ProjectionProvenance` | type | `pub enum ProjectionProvenance {` | `ProjectionProvenance [type]` | `65ccd34b-e019-5739-9cde-edef70f0a2a5` | 19-24 [crates/gcode/src/models.rs:19-24] | Indexed type `ProjectionProvenance` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:19-24] |
| `ProjectionProvenance::as_str` | method | `pub fn as_str(self) -> &'static str {` | `ProjectionProvenance::as_str [method]` | `4e40ca68-1054-5243-8beb-75063fd161c4` | 27-33 [crates/gcode/src/models.rs:27-33] | Indexed method `ProjectionProvenance::as_str` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:27-33] |
| `ProjectionProvenance::from_wire_value` | method | `pub fn from_wire_value(value: &str) -> Option<Self> {` | `ProjectionProvenance::from_wire_value [method]` | `1aa3144f-dfde-5afe-8ef8-9134669c4c7a` | 35-42 [crates/gcode/src/models.rs:35-42] | Indexed method `ProjectionProvenance::from_wire_value` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:35-42] |
| `ProjectionProvenance::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `ProjectionProvenance::fmt [method]` | `6832a695-9e8d-5630-b52e-e5df9d7d30a4` | 46-48 [crates/gcode/src/models.rs:46-48] | Indexed method `ProjectionProvenance::fmt` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:46-48] |
| `ProjectionMetadata` | class | `pub struct ProjectionMetadata {` | `ProjectionMetadata [class]` | `ce4a4518-a240-5a63-8380-9e364236e588` | 53-66 [crates/gcode/src/models.rs:53-66] | Indexed class `ProjectionMetadata` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:53-66] |
| `ProjectionMetadata::new` | method | `pub fn new(provenance: ProjectionProvenance, source_system: impl Into<String>) -> Self {` | `ProjectionMetadata::new [method]` | `e733a615-7c2f-573c-835f-3c19db6ac96e` | 69-79 [crates/gcode/src/models.rs:69-79] | Indexed method `ProjectionMetadata::new` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:69-79] |
| `ProjectionMetadata::gcode_extracted` | method | `pub fn gcode_extracted() -> Self {` | `ProjectionMetadata::gcode_extracted [method]` | `ce62374e-5b96-554c-8895-132d89aada79` | 81-83 [crates/gcode/src/models.rs:81-83] | Indexed method `ProjectionMetadata::gcode_extracted` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:81-83] |
| `ProjectionMetadata::inferred` | method | `pub fn inferred(source_system: impl Into<String>, confidence: Option<f64>) -> Self {` | `ProjectionMetadata::inferred [method]` | `1d043993-a026-51e3-b599-a6f1ac92973b` | 85-87 [crates/gcode/src/models.rs:85-87] | Indexed method `ProjectionMetadata::inferred` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:85-87] |
| `ProjectionMetadata::ambiguous` | method | `pub fn ambiguous(source_system: impl Into<String>, confidence: Option<f64>) -> Self {` | `ProjectionMetadata::ambiguous [method]` | `655f6768-1212-5883-822b-84236805dd56` | 89-91 [crates/gcode/src/models.rs:89-91] | Indexed method `ProjectionMetadata::ambiguous` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:89-91] |
| `ProjectionMetadata::with_confidence` | method | `pub fn with_confidence(mut self, confidence: Option<f64>) -> Self {` | `ProjectionMetadata::with_confidence [method]` | `3f643fc3-42b9-5b33-a11b-17b646a2bc8e` | 93-96 [crates/gcode/src/models.rs:93-96] | Indexed method `ProjectionMetadata::with_confidence` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:93-96] |
| `ProjectionMetadata::with_source_file_path` | method | `pub fn with_source_file_path(mut self, file_path: impl Into<String>) -> Self {` | `ProjectionMetadata::with_source_file_path [method]` | `53255549-0e88-5e5a-bb6b-a1874aaf24fa` | 98-101 [crates/gcode/src/models.rs:98-101] | Indexed method `ProjectionMetadata::with_source_file_path` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:98-101] |
| `ProjectionMetadata::with_source_line` | method | `pub fn with_source_line(mut self, line: usize) -> Self {` | `ProjectionMetadata::with_source_line [method]` | `009fa4fc-e82f-5aea-990e-d4ad32172be6` | 103-106 [crates/gcode/src/models.rs:103-106] | Indexed method `ProjectionMetadata::with_source_line` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:103-106] |
| `ProjectionMetadata::with_source_symbol_id` | method | `pub fn with_source_symbol_id(mut self, symbol_id: impl Into<String>) -> Self {` | `ProjectionMetadata::with_source_symbol_id [method]` | `9edeaf7e-b1ac-5471-ad83-681785dad650` | 108-111 [crates/gcode/src/models.rs:108-111] | Indexed method `ProjectionMetadata::with_source_symbol_id` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:108-111] |
| `ProjectionMetadata::with_matching_method` | method | `pub fn with_matching_method(mut self, matching_method: impl Into<String>) -> Self {` | `ProjectionMetadata::with_matching_method [method]` | `82ed3d0c-232e-5e36-bb2b-b31a9db3a18b` | 113-116 [crates/gcode/src/models.rs:113-116] | Indexed method `ProjectionMetadata::with_matching_method` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:113-116] |
| `ProjectionMetadata::is_hypothesis` | method | `pub fn is_hypothesis(&self) -> bool {` | `ProjectionMetadata::is_hypothesis [method]` | `bf387905-6ca7-5866-becc-fc2d6590fdf1` | 118-123 [crates/gcode/src/models.rs:118-123] | Indexed method `ProjectionMetadata::is_hypothesis` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:118-123] |
| `Symbol` | class | `pub struct Symbol {` | `Symbol [class]` | `4cf2b313-146b-50c6-a3a1-2530dd2fbccf` | 128-154 [crates/gcode/src/models.rs:128-154] | Indexed class `Symbol` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:128-154] |
| `Symbol::make_id` | method | `pub fn make_id(` | `Symbol::make_id [method]` | `69cd4f83-808b-5822-a42f-51888f85915f` | 159-168 [crates/gcode/src/models.rs:159-168] | Indexed method `Symbol::make_id` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:159-168] |
| `Symbol::from_row` | method | `pub fn from_row(row: &Row) -> anyhow::Result<Self> {` | `Symbol::from_row [method]` | `7343ea28-d6b2-50dc-817d-cede6934d43c` | 174-201 [crates/gcode/src/models.rs:174-201] | Indexed method `Symbol::from_row` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:174-201] |
| `Symbol::to_outline` | method | `pub fn to_outline(&self) -> OutlineSymbol {` | `Symbol::to_outline [method]` | `33c52759-cf52-5e40-92ad-15e365409804` | 204-213 [crates/gcode/src/models.rs:204-213] | Indexed method `Symbol::to_outline` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:204-213] |
| `Symbol::to_brief` | method | `pub fn to_brief(&self) -> SearchResult {` | `Symbol::to_brief [method]` | `051e002c-a497-5735-bd28-b770876082dd` | 216-232 [crates/gcode/src/models.rs:216-232] | Indexed method `Symbol::to_brief` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:216-232] |
| `make_unresolved_callee_id` | function | `pub fn make_unresolved_callee_id(project_id: &str, callee_name: &str) -> String {` | `make_unresolved_callee_id [function]` | `40af6c3e-7b6a-5ec7-bd16-98be94813782` | 235-238 [crates/gcode/src/models.rs:235-238] | Indexed function `make_unresolved_callee_id` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:235-238] |
| `make_external_symbol_id` | function | `pub fn make_external_symbol_id(` | `make_external_symbol_id [function]` | `6e65c431-6c2e-51c8-8343-797cee114f19` | 240-248 [crates/gcode/src/models.rs:240-248] | Indexed function `make_external_symbol_id` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:240-248] |
| `IndexedFile` | class | `pub struct IndexedFile {` | `IndexedFile [class]` | `2dda5582-b4a6-5c45-ae38-13b71785850f` | 252-261 [crates/gcode/src/models.rs:252-261] | Indexed class `IndexedFile` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:252-261] |
| `IndexedFile::make_id` | method | `pub fn make_id(project_id: &str, file_path: &str) -> String {` | `IndexedFile::make_id [method]` | `c489688b-3589-53a6-baaa-202c9cc68663` | 264-267 [crates/gcode/src/models.rs:264-267] | Indexed method `IndexedFile::make_id` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:264-267] |
| `ContentChunk` | class | `pub struct ContentChunk {` | `ContentChunk [class]` | `3ac0e7fb-336e-50bb-867c-3c1918a5d164` | 272-282 [crates/gcode/src/models.rs:272-282] | Indexed class `ContentChunk` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:272-282] |
| `ContentChunk::make_id` | method | `pub fn make_id(project_id: &str, file_path: &str, chunk_index: usize) -> String {` | `ContentChunk::make_id [method]` | `89be2fa1-34c4-5fb3-bb3c-6e0caee95fea` | 285-288 [crates/gcode/src/models.rs:285-288] | Indexed method `ContentChunk::make_id` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:285-288] |
| `ImportRelation` | class | `pub struct ImportRelation {` | `ImportRelation [class]` | `27713270-8bee-5fb7-b22e-5fad2d05869b` | 293-296 [crates/gcode/src/models.rs:293-296] | Indexed class `ImportRelation` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:293-296] |
| `CallTargetKind` | type | `pub enum CallTargetKind {` | `CallTargetKind [type]` | `5eead4ae-9888-5f39-9c6e-d2686716f00a` | 300-310 [crates/gcode/src/models.rs:300-310] | Indexed type `CallTargetKind` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:300-310] |
| `CallTargetKind::as_str` | method | `pub fn as_str(self) -> &'static str {` | `CallTargetKind::as_str [method]` | `93067c1c-dbcd-5892-82d6-8001f429a0f0` | 313-320 [crates/gcode/src/models.rs:313-320] | Indexed method `CallTargetKind::as_str` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:313-320] |
| `CallRelation` | class | `pub struct CallRelation {` | `CallRelation [class]` | `23714f18-cf43-5ebc-bb4c-223ae9aeda8c` | 325-333 [crates/gcode/src/models.rs:325-333] | Indexed class `CallRelation` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:325-333] |
| `CallRelation::new` | method | `pub fn new(` | `CallRelation::new [method]` | `e54a8202-4d10-5a12-88b6-35e69edfe12b` | 336-351 [crates/gcode/src/models.rs:336-351] | Indexed method `CallRelation::new` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:336-351] |
| `CallRelation::with_symbol_target` | method | `pub fn with_symbol_target(mut self, callee_symbol_id: String) -> Self {` | `CallRelation::with_symbol_target [method]` | `5b0bae27-54a8-5efa-a77b-dd13d68c8a8a` | 353-357 [crates/gcode/src/models.rs:353-357] | Indexed method `CallRelation::with_symbol_target` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:353-357] |
| `CallRelation::with_external_target` | method | `pub fn with_external_target(` | `CallRelation::with_external_target [method]` | `79927e75-6f97-5150-a1b9-966901e133c5` | 359-368 [crates/gcode/src/models.rs:359-368] | Indexed method `CallRelation::with_external_target` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:359-368] |
| `CallRelation::with_local_import_target` | method | `pub fn with_local_import_target(` | `CallRelation::with_local_import_target [method]` | `7b767e82-bddc-51f4-9e73-ac6ef8c8e9d2` | 382-392 [crates/gcode/src/models.rs:382-392] | Indexed method `CallRelation::with_local_import_target` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:382-392] |
| `CallRelation::with_local_default_import_target` | method | `pub fn with_local_default_import_target(` | `CallRelation::with_local_default_import_target [method]` | `7ba8ebc0-3a60-55e0-8d67-8fd9f772736b` | 394-408 [crates/gcode/src/models.rs:394-408] | Indexed method `CallRelation::with_local_default_import_target` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:394-408] |
| `CallRelation::local_import_uses_default_export_fallback` | method | `pub fn local_import_uses_default_export_fallback(&self) -> bool {` | `CallRelation::local_import_uses_default_export_fallback [method]` | `085a4f3b-a8dc-5475-a940-e2df7884b9bf` | 410-417 [crates/gcode/src/models.rs:410-417] | Indexed method `CallRelation::local_import_uses_default_export_fallback` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:410-417] |
| `CallRelation::local_import_candidate_files` | method | `pub fn local_import_candidate_files(&self) -> Vec<String> {` | `CallRelation::local_import_candidate_files [method]` | `1f474929-fd38-5d24-9854-9b9e884652ae` | 421-435 [crates/gcode/src/models.rs:421-435] | Indexed method `CallRelation::local_import_candidate_files` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:421-435] |
| `IndexedProject` | class | `pub struct IndexedProject {` | `IndexedProject [class]` | `477dcee9-d994-5b44-8ca2-c738de27860f` | 446-455 [crates/gcode/src/models.rs:446-455] | Indexed class `IndexedProject` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:446-455] |
| `SearchResult` | class | `pub struct SearchResult {` | `SearchResult [class]` | `608aef87-4925-5616-9ffc-34606eb94672` | 459-477 [crates/gcode/src/models.rs:459-477] | Indexed class `SearchResult` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:459-477] |
| `GraphResult` | class | `pub struct GraphResult {` | `GraphResult [class]` | `4cd77c7d-0110-56a7-a4ec-785b659c2388` | 481-495 [crates/gcode/src/models.rs:481-495] | Indexed class `GraphResult` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:481-495] |
| `GraphPathStep` | class | `pub struct GraphPathStep {` | `GraphPathStep [class]` | `16ccd2fe-329d-54c3-a9bd-77d797ea0be6` | 498-504 [crates/gcode/src/models.rs:498-504] | Indexed class `GraphPathStep` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:498-504] |
| `ParseResult` | class | `pub struct ParseResult {` | `ParseResult [class]` | `a4181d30-d152-56f6-a8c1-29b21997c454` | 507-513 [crates/gcode/src/models.rs:507-513] | Indexed class `ParseResult` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:507-513] |
| `IndexResult` | class | `pub struct IndexResult {` | `IndexResult [class]` | `3d001e7d-86f9-5a85-9cea-58564c7dbb9b` | 517-524 [crates/gcode/src/models.rs:517-524] | Indexed class `IndexResult` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:517-524] |
| `PagedResponse` | class | `pub struct PagedResponse<T: Serialize> {` | `PagedResponse [class]` | `cd1ebb2f-ac0b-5f0f-9c89-8e8fc420a62b` | 529-537 [crates/gcode/src/models.rs:529-537] | Indexed class `PagedResponse` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:529-537] |
| `OutlineSymbol` | class | `pub struct OutlineSymbol {` | `OutlineSymbol [class]` | `3734cef0-3ce7-5fa0-a606-50a20d67f0a9` | 541-549 [crates/gcode/src/models.rs:541-549] | Indexed class `OutlineSymbol` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:541-549] |
| `ContentSearchHit` | class | `pub struct ContentSearchHit {` | `ContentSearchHit [class]` | `de87f525-a6f0-55b5-aa3b-3649fa5f4383` | 553-560 [crates/gcode/src/models.rs:553-560] | Indexed class `ContentSearchHit` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:553-560] |
| `symbol_make_id_matches_python_uuid5_golden_vectors` | function | `fn symbol_make_id_matches_python_uuid5_golden_vectors() {` | `symbol_make_id_matches_python_uuid5_golden_vectors [function]` | `dc859626-9832-5d09-9c2a-fc2c3ed31ab8` | 567-615 [crates/gcode/src/models.rs:567-615] | Indexed function `symbol_make_id_matches_python_uuid5_golden_vectors` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:567-615] |
| `unresolved_and_external_ids_match_python_uuid5_golden_vectors` | function | `fn unresolved_and_external_ids_match_python_uuid5_golden_vectors() {` | `unresolved_and_external_ids_match_python_uuid5_golden_vectors [function]` | `12862e17-1fe0-5941-9343-74cb9aba6554` | 618-631 [crates/gcode/src/models.rs:618-631] | Indexed function `unresolved_and_external_ids_match_python_uuid5_golden_vectors` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:618-631] |
| `test_call_relation_promotes_symbol_targets` | function | `fn test_call_relation_promotes_symbol_targets() {` | `test_call_relation_promotes_symbol_targets [function]` | `8de1722e-77ff-5f89-9e07-191300e04cdf` | 633-644 [crates/gcode/src/models.rs:633-644] | Indexed function `test_call_relation_promotes_symbol_targets` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:633-644] |
| `graph_result_metadata_remains_optional_in_json_contract` | function | `fn graph_result_metadata_remains_optional_in_json_contract() {` | `graph_result_metadata_remains_optional_in_json_contract [function]` | `9c8cf734-e086-5701-bb34-d8f3596de1e2` | 647-663 [crates/gcode/src/models.rs:647-663] | Indexed function `graph_result_metadata_remains_optional_in_json_contract` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:647-663] |
| `graph_result_without_metadata_omits_metadata_when_serialized` | function | `fn graph_result_without_metadata_omits_metadata_when_serialized() {` | `graph_result_without_metadata_omits_metadata_when_serialized [function]` | `31192111-35da-5b57-9e8a-eea1e76bd021` | 666-702 [crates/gcode/src/models.rs:666-702] | Indexed function `graph_result_without_metadata_omits_metadata_when_serialized` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:666-702] |
