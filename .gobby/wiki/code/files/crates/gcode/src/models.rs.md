---
title: crates/gcode/src/models.rs
type: code_file
provenance:
- file: crates/gcode/src/models.rs
  ranges:
  - 18-22
  - 24-33
  - 37-50
  - 52-108
  - 112-138
  - 140-217
  - 219-222
  - 224-232
  - 236-245
  - 247-252
  - 256-266
  - 268-273
  - 277-280
  - 284-288
  - 290-298
  - 302-310
  - 312-346
  - 350-359
  - 363-381
  - 385-396
  - 399-405
  - 409-416
  - 421-429
  - 433-441
  - 445-452
  - 459-507
  - 510-523
  - 525-536
  - 539-553
  - 556-590
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/models.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Defines the core data models for the gcode indexer and graph/search pipeline. It establishes a stable UUID5 namespace and source-system constant, then provides projection provenance and `ProjectionMetadata` helpers for labeling derived facts with confidence and source attribution. The rest of the file models indexed symbols, files, chunks, imports, call relations, projects, search and graph results, parse/index outcomes, and pagination envelopes, with conversion helpers that build DTOs, deterministic IDs, and database-row mappings. The tests lock in UUID determinism and JSON contracts so these models stay compatible across Rust and Python consumers.
[crates/gcode/src/models.rs:18-22]
[crates/gcode/src/models.rs:24-33]
[crates/gcode/src/models.rs:25-32]
[crates/gcode/src/models.rs:37-50]
[crates/gcode/src/models.rs:52-108]

## API Symbols

- `ProjectionProvenance` (type) component `ProjectionProvenance [type]` (`65ba8ecd-b178-5ce9-a1cc-c9c3058b8a1e`) lines 18-22 [crates/gcode/src/models.rs:18-22]
  - Signature: `pub enum ProjectionProvenance {`
  - Purpose: Indexed type `ProjectionProvenance` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:18-22]
- `ProjectionProvenance` (class) component `ProjectionProvenance [class]` (`cc08f8f9-225a-54f0-93d7-98b263534eb5`) lines 24-33 [crates/gcode/src/models.rs:24-33]
  - Signature: `impl ProjectionProvenance {`
  - Purpose: Implements a case-insensitive parser that deserializes wire format string values into `ProjectionProvenance` enum variants (Extracted, Inferred, or Ambiguous), returning `None` for unrecognized inputs. [crates/gcode/src/models.rs:24-33]
- `ProjectionProvenance.from_wire_value` (method) component `ProjectionProvenance.from_wire_value [method]` (`e815c658-062b-5f76-a149-5ea6e6e3a259`) lines 25-32 [crates/gcode/src/models.rs:25-32]
  - Signature: `pub fn from_wire_value(value: &str) -> Option<Self> {`
  - Purpose: Performs case-insensitive deserialization of a wire format string into a corresponding enum variant, returning `Option<Self>`. [crates/gcode/src/models.rs:25-32]
- `ProjectionMetadata` (class) component `ProjectionMetadata [class]` (`dbbd701a-2d56-5862-b22d-0e1240010134`) lines 37-50 [crates/gcode/src/models.rs:37-50]
  - Signature: `pub struct ProjectionMetadata {`
  - Purpose: `ProjectionMetadata` is a serde-serializable struct that combines required projection provenance and source system attribution with optional confidence scoring and source location/matching metadata for data lineage tracking. [crates/gcode/src/models.rs:37-50]
- `ProjectionMetadata` (class) component `ProjectionMetadata [class]` (`c1cbda8c-46b1-5afc-b83b-cfef08fe42d0`) lines 52-108 [crates/gcode/src/models.rs:52-108]
  - Signature: `impl ProjectionMetadata {`
  - Purpose: ProjectionMetadata impl implements a builder pattern for constructing metadata objects that track code projection provenance, source system attribution, confidence levels, and source location details (file path, line number, symbol ID, and matching method). [crates/gcode/src/models.rs:52-108]
- `ProjectionMetadata.new` (method) component `ProjectionMetadata.new [method]` (`ef487a81-db35-5a05-ab47-78684b8ebc80`) lines 53-63 [crates/gcode/src/models.rs:53-63]
  - Signature: `pub fn new(provenance: ProjectionProvenance, source_system: impl Into<String>) -> Self {`
  - Purpose: Constructs a new instance with the specified `ProjectionProvenance` and `source_system`, initializing all remaining fields to `None`. [crates/gcode/src/models.rs:53-63]
- `ProjectionMetadata.gcode_extracted` (method) component `ProjectionMetadata.gcode_extracted [method]` (`e2e44548-3aca-5c71-98f1-69c66fb4f477`) lines 65-67 [crates/gcode/src/models.rs:65-67]
  - Signature: `pub fn gcode_extracted() -> Self {`
  - Purpose: Constructs a Self instance with `ProjectionProvenance::Extracted` provenance, `SOURCE_SYSTEM_GCODE` as the source, and maximum confidence (1.0). [crates/gcode/src/models.rs:65-67]
- `ProjectionMetadata.inferred` (method) component `ProjectionMetadata.inferred [method]` (`3b9073c2-95da-5c40-9d52-749c36c03f12`) lines 69-71 [crates/gcode/src/models.rs:69-71]
  - Signature: `pub fn inferred(source_system: impl Into<String>, confidence: Option<f64>) -> Self {`
  - Purpose: Constructs a new instance with `ProjectionProvenance::Inferred` status, the specified source system, and an optional confidence value. [crates/gcode/src/models.rs:69-71]
- `ProjectionMetadata.ambiguous` (method) component `ProjectionMetadata.ambiguous [method]` (`91e5910d-4dc4-5702-b7ba-7ee5f89d5bf9`) lines 73-75 [crates/gcode/src/models.rs:73-75]
  - Signature: `pub fn ambiguous(source_system: impl Into<String>, confidence: Option<f64>) -> Self {`
  - Purpose: Creates an instance with `ProjectionProvenance::Ambiguous` provenance, derived from the provided source system identifier and optional confidence metric. [crates/gcode/src/models.rs:73-75]
- `ProjectionMetadata.with_confidence` (method) component `ProjectionMetadata.with_confidence [method]` (`d364c373-f668-5d5b-99f7-8b7f56ba6115`) lines 77-80 [crates/gcode/src/models.rs:77-80]
  - Signature: `pub fn with_confidence(mut self, confidence: Option<f64>) -> Self {`
  - Purpose: Sets the `confidence` field to the provided `Option<f64>` value and returns `self` to enable method chaining in the builder pattern. [crates/gcode/src/models.rs:77-80]
- `ProjectionMetadata.with_source_file_path` (method) component `ProjectionMetadata.with_source_file_path [method]` (`13632e87-ef67-5106-a7d4-5b8e35884394`) lines 82-85 [crates/gcode/src/models.rs:82-85]
  - Signature: `pub fn with_source_file_path(mut self, file_path: impl Into<String>) -> Self {`
  - Purpose: A builder method that sets the optional `source_file_path` field by converting the input parameter into a `String` and returns `self` to enable method chaining. [crates/gcode/src/models.rs:82-85]
- `ProjectionMetadata.with_source_line` (method) component `ProjectionMetadata.with_source_line [method]` (`a804e0af-891c-59ea-8ceb-0438b1d705bf`) lines 87-90 [crates/gcode/src/models.rs:87-90]
  - Signature: `pub fn with_source_line(mut self, line: usize) -> Self {`
  - Purpose: A builder method that sets the `source_line` field to the provided `usize` value and returns `self` to enable method chaining. [crates/gcode/src/models.rs:87-90]
- `ProjectionMetadata.with_source_symbol_id` (method) component `ProjectionMetadata.with_source_symbol_id [method]` (`c0158985-b601-584e-9e67-8f20ec5c8fac`) lines 92-95 [crates/gcode/src/models.rs:92-95]
  - Signature: `pub fn with_source_symbol_id(mut self, symbol_id: impl Into<String>) -> Self {`
  - Purpose: Sets the optional `source_symbol_id` field from an `Into<String>` value and returns `self` for fluent builder chaining. [crates/gcode/src/models.rs:92-95]
- `ProjectionMetadata.with_matching_method` (method) component `ProjectionMetadata.with_matching_method [method]` (`8df62a74-4966-5ffb-9ec5-596c7f76d5f9`) lines 97-100 [crates/gcode/src/models.rs:97-100]
  - Signature: `pub fn with_matching_method(mut self, matching_method: impl Into<String>) -> Self {`
  - Purpose: # Summary

This builder-pattern method sets the `matching_method` field to the provided value (converted to `String`) wrapped in `Some`, then returns `self` to enable method chaining. [crates/gcode/src/models.rs:97-100]
- `ProjectionMetadata.is_hypothesis` (method) component `ProjectionMetadata.is_hypothesis [method]` (`6b3e7eba-64a7-5d47-99fc-4b2fe47c2d9b`) lines 102-107 [crates/gcode/src/models.rs:102-107]
  - Signature: `pub fn is_hypothesis(&self) -> bool {`
  - Purpose: This method returns `true` if the projection's provenance is either `Inferred` or `Ambiguous`, indicating the projection is a hypothesis rather than confirmed. [crates/gcode/src/models.rs:102-107]
- `Symbol` (class) component `Symbol [class]` (`11b7a2b8-1e16-5c3e-934e-5d96fddb57fa`) lines 112-138 [crates/gcode/src/models.rs:112-138]
  - Signature: `pub struct Symbol {`
  - Purpose: A struct that records indexed code symbol metadata including file location, language-specific kind, fully-qualified name, optional signature and documentation, and content versioning. [crates/gcode/src/models.rs:112-138]
- `Symbol` (class) component `Symbol [class]` (`599d85f4-c220-575b-9a05-763e2538de33`) lines 140-217 [crates/gcode/src/models.rs:140-217]
  - Signature: `impl Symbol {`
  - Purpose: Symbol implements deterministic UUID5 ID generation and PostgreSQL row deserialization for code symbol metadata (including location, language, and documentation). [crates/gcode/src/models.rs:140-217]
- `Symbol.make_id` (method) component `Symbol.make_id [method]` (`df0df6cd-9bbb-5f1d-82d3-989dff8c944f`) lines 143-152 [crates/gcode/src/models.rs:143-152]
  - Signature: `pub fn make_id(`
  - Purpose: Generates a deterministic UUID v5 from a colon-delimited composite key of project ID, file path, symbol name, kind, and byte offset hashed against a fixed namespace. [crates/gcode/src/models.rs:143-152]
- `Symbol.from_row` (method) component `Symbol.from_row [method]` (`d6b73a92-07ce-58e7-b26d-14b59a47b6e7`) lines 158-185 [crates/gcode/src/models.rs:158-185]
  - Signature: `pub fn from_row(row: &Row) -> anyhow::Result<Self> {`
  - Purpose: Constructs Self by extracting and type-converting database row columns to struct fields, with error propagation and default values for optional fields. [crates/gcode/src/models.rs:158-185]
- `Symbol.to_outline` (method) component `Symbol.to_outline [method]` (`aaa67eb8-755e-5fb5-b7e7-76e70a6b992e`) lines 188-197 [crates/gcode/src/models.rs:188-197]
  - Signature: `pub fn to_outline(&self) -> OutlineSymbol {`
  - Purpose: Converts `self` into an `OutlineSymbol` by cloning metadata fields (id, name, kind, signature) and copying line range information (line_start, line_end). [crates/gcode/src/models.rs:188-197]
- `Symbol.to_brief` (method) component `Symbol.to_brief [method]` (`d8c72666-c1ea-5209-9c4b-78d1c18bf1bc`) lines 200-216 [crates/gcode/src/models.rs:200-216]
  - Signature: `pub fn to_brief(&self) -> SearchResult {`
  - Purpose: Constructs a new `SearchResult` by cloning the instance's metadata fields while resetting score and source information to default values. [crates/gcode/src/models.rs:200-216]
- `make_unresolved_callee_id` (function) component `make_unresolved_callee_id [function]` (`0fcbe831-c8a9-59a2-8fa0-c5bb33dc9174`) lines 219-222 [crates/gcode/src/models.rs:219-222]
  - Signature: `pub fn make_unresolved_callee_id(project_id: &str, callee_name: &str) -> String {`
  - Purpose: Generates a deterministic UUIDv5-based identifier for an unresolved callee by hashing a namespaced key composed of the project ID and callee name. [crates/gcode/src/models.rs:219-222]
- `make_external_symbol_id` (function) component `make_external_symbol_id [function]` (`257f4d2d-3f5e-5087-b435-51e2f97413a0`) lines 224-232 [crates/gcode/src/models.rs:224-232]
  - Signature: `pub fn make_external_symbol_id(`
  - Purpose: Creates a deterministic UUID v5 identifier for an external symbol by hashing a composite key of project ID, optional module, and callee name within a fixed code index namespace. [crates/gcode/src/models.rs:224-232]
- `IndexedFile` (class) component `IndexedFile [class]` (`78a1121a-d51a-5a41-8449-ceefdd468b44`) lines 236-245 [crates/gcode/src/models.rs:236-245]
  - Signature: `pub struct IndexedFile {`
  - Purpose: `IndexedFile` is a struct that stores metadata for an indexed source code file, including its project association, path, language, content hash, symbol count, byte size, and indexing timestamp. [crates/gcode/src/models.rs:236-245]
- `IndexedFile` (class) component `IndexedFile [class]` (`b542c0bf-0746-53d5-bc4b-2e1d073f2f3d`) lines 247-252 [crates/gcode/src/models.rs:247-252]
  - Signature: `impl IndexedFile {`
  - Purpose: `IndexedFile::make_id` generates a deterministic UUIDv5 by hashing a concatenated `project_id:file_path` string against a fixed CODE_INDEX_UUID_NAMESPACE. [crates/gcode/src/models.rs:247-252]
- `IndexedFile.make_id` (method) component `IndexedFile.make_id [method]` (`a6a95e5a-42e2-5cab-85cb-e7555a110b62`) lines 248-251 [crates/gcode/src/models.rs:248-251]
  - Signature: `pub fn make_id(project_id: &str, file_path: &str) -> String {`
  - Purpose: Generates a deterministic UUIDv5 from a colon-delimited concatenation of `project_id` and `file_path` using a fixed namespace. [crates/gcode/src/models.rs:248-251]
- `ContentChunk` (class) component `ContentChunk [class]` (`8116f271-0a9e-5349-8bae-3574fa9444a8`) lines 256-266 [crates/gcode/src/models.rs:256-266]
  - Signature: `pub struct ContentChunk {`
  - Purpose: `ContentChunk` is a Rust struct representing a delimited segment of source code with positional metadata (file path, line range, chunk index), language identifier, and project/temporal context. [crates/gcode/src/models.rs:256-266]
- `ContentChunk` (class) component `ContentChunk [class]` (`2e88d547-0941-55bd-9d26-1e699a7c3a04`) lines 268-273 [crates/gcode/src/models.rs:268-273]
  - Signature: `impl ContentChunk {`
  - Purpose: ContentChunk generates deterministic UUIDs for code chunks by computing a v5 UUID from a composite key containing project ID, file path, and chunk index. [crates/gcode/src/models.rs:268-273]
- `ContentChunk.make_id` (method) component `ContentChunk.make_id [method]` (`5ae833e5-abd9-5482-b739-a78626a2fc2d`) lines 269-272 [crates/gcode/src/models.rs:269-272]
  - Signature: `pub fn make_id(project_id: &str, file_path: &str, chunk_index: usize) -> String {`
  - Purpose: Creates a UUID v5 from a namespaced hash of a colon-separated key combining project ID, file path, and chunk index. [crates/gcode/src/models.rs:269-272]
- `ImportRelation` (class) component `ImportRelation [class]` (`efa58848-4833-5a75-851c-1292983d42dd`) lines 277-280 [crates/gcode/src/models.rs:277-280]
  - Signature: `pub struct ImportRelation {`
  - Purpose: ImportRelation is a public struct that represents a mapping between a file path and its associated module name. [crates/gcode/src/models.rs:277-280]
- `CallTargetKind` (type) component `CallTargetKind [type]` (`d13c3917-80ca-5eb9-bb83-1c83c53187be`) lines 284-288 [crates/gcode/src/models.rs:284-288]
  - Signature: `pub enum CallTargetKind {`
  - Purpose: Indexed type `CallTargetKind` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:284-288]
- `CallTargetKind` (class) component `CallTargetKind [class]` (`2fd5a984-be13-5dd8-b0cd-daee949e0307`) lines 290-298 [crates/gcode/src/models.rs:290-298]
  - Signature: `impl CallTargetKind {`
  - Purpose: `CallTargetKind` is an enum implementation that converts its three variants (Symbol, Unresolved, External) into their corresponding static string representations via the `as_str` method. [crates/gcode/src/models.rs:290-298]
- `CallTargetKind.as_str` (method) component `CallTargetKind.as_str [method]` (`d375a7d1-bbe3-50c7-a706-d19bcfc27244`) lines 291-297 [crates/gcode/src/models.rs:291-297]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Consumes self and returns a static string slice corresponding to the matched enum variant via exhaustive pattern matching. [crates/gcode/src/models.rs:291-297]
- `CallRelation` (class) component `CallRelation [class]` (`25113b69-019e-56ab-9ee8-1c7e30eb1c84`) lines 302-310 [crates/gcode/src/models.rs:302-310]
  - Signature: `pub struct CallRelation {`
  - Purpose: CallRelation is a struct representing a directed call edge between a caller symbol and a callee, capturing the callee's identity/name, call target kind, optional external module, and source location. [crates/gcode/src/models.rs:302-310]
- `CallRelation` (class) component `CallRelation [class]` (`1a071893-b076-53c0-9a5e-f6b5c67c90b8`) lines 312-346 [crates/gcode/src/models.rs:312-346]
  - Signature: `impl CallRelation {`
  - Purpose: CallRelation represents a function call graph edge between a caller and callee, with a fluent builder interface to resolve the callee target to either an internal symbol or external module. [crates/gcode/src/models.rs:312-346]
- `CallRelation.new` (method) component `CallRelation.new [method]` (`94c39b90-4750-5d95-a450-35e8021184f0`) lines 313-328 [crates/gcode/src/models.rs:313-328]
  - Signature: `pub fn new(`
  - Purpose: Creates a new Call instance with the provided caller symbol ID, callee name, and source location, initializing callee resolution metadata to unresolved states. [crates/gcode/src/models.rs:313-328]
- `CallRelation.with_symbol_target` (method) component `CallRelation.with_symbol_target [method]` (`e5cf659f-e7b7-5c8a-87b8-28332b93fead`) lines 330-334 [crates/gcode/src/models.rs:330-334]
  - Signature: `pub fn with_symbol_target(mut self, callee_symbol_id: String) -> Self {`
  - Purpose: Sets the call target to invoke a named symbol by identifier and returns `self` to enable builder-pattern method chaining. [crates/gcode/src/models.rs:330-334]
- `CallRelation.with_external_target` (method) component `CallRelation.with_external_target [method]` (`5a1e3f34-d250-5547-bbe0-7d0735450d61`) lines 336-345 [crates/gcode/src/models.rs:336-345]
  - Signature: `pub fn with_external_target(`
  - Purpose: Configures this instance as a call to an external function by setting the callee name and external module reference, marking the target kind as External, and returning self for method chaining. [crates/gcode/src/models.rs:336-345]
- `IndexedProject` (class) component `IndexedProject [class]` (`98fd2de6-ed7a-51dc-9135-9a3385537d26`) lines 350-359 [crates/gcode/src/models.rs:350-359]
  - Signature: `pub struct IndexedProject {`
  - Purpose: `IndexedProject` is a serializable struct that encapsulates metadata for an indexed code project, storing its identifier, root path, file and symbol counts, indexing timestamp, duration, and an optional eligible file count. [crates/gcode/src/models.rs:350-359]
- `SearchResult` (class) component `SearchResult [class]` (`7013aa55-9921-5cbf-a9bc-307e8fcb6d68`) lines 363-381 [crates/gcode/src/models.rs:363-381]
  - Signature: `pub struct SearchResult {`
  - Purpose: A struct representing a ranked code search result that encapsulates a code element's identity, location, language, scoring metrics, and optional metadata (summary, signature, sources). [crates/gcode/src/models.rs:363-381]
- `GraphResult` (class) component `GraphResult [class]` (`32c47c4e-d103-5b6e-ba77-09c7981c0cdc`) lines 385-396 [crates/gcode/src/models.rs:385-396]
  - Signature: `pub struct GraphResult {`
  - Purpose: GraphResult is a serializable struct representing a single code entity result from a dependency graph query, containing required identification and file location data with optional relationship distance and metadata fields. [crates/gcode/src/models.rs:385-396]
- `ParseResult` (class) component `ParseResult [class]` (`711f06fd-686b-5b96-8712-8babd8c9f55d`) lines 399-405 [crates/gcode/src/models.rs:399-405]
  - Signature: `pub struct ParseResult {`
  - Purpose: ParseResult is a struct that encapsulates the output of source code parsing: extracted symbols, import/call relations, and raw source bytes for downstream analysis and embedding-time snippet extraction. [crates/gcode/src/models.rs:399-405]
- `IndexResult` (class) component `IndexResult [class]` (`5e6fd04c-bef6-5e8c-8c5b-4e95ffdcc7c5`) lines 409-416 [crates/gcode/src/models.rs:409-416]
  - Signature: `pub struct IndexResult {`
  - Purpose: `IndexResult` is a metrics struct that encapsulates the outcome of a code indexing operation, reporting the count of indexed and skipped files, discovered symbols, any errors encountered, and execution duration in milliseconds. [crates/gcode/src/models.rs:409-416]
- `PagedResponse` (class) component `PagedResponse [class]` (`f396a671-73e8-58f5-91a2-dabae7a4d16e`) lines 421-429 [crates/gcode/src/models.rs:421-429]
  - Signature: `pub struct PagedResponse<T: Serialize> {`
  - Purpose: `PagedResponse<T>` is a generic pagination envelope that wraps a slice of serializable results with offset/limit pagination metadata, total item count, project scoping, and an optional hint field. [crates/gcode/src/models.rs:421-429]
- `OutlineSymbol` (class) component `OutlineSymbol [class]` (`b28a285c-d5ab-53d1-a58b-b4e29a992d8d`) lines 433-441 [crates/gcode/src/models.rs:433-441]
  - Signature: `pub struct OutlineSymbol {`
  - Purpose: `OutlineSymbol` is a Serde-compatible struct that encapsulates metadata for a source code symbol, including its identifier, name, kind, line range, and optional type signature. [crates/gcode/src/models.rs:433-441]
- `ContentSearchHit` (class) component `ContentSearchHit [class]` (`f96eb98d-9d70-5a7d-9c80-e5a4789bdc62`) lines 445-452 [crates/gcode/src/models.rs:445-452]
  - Signature: `pub struct ContentSearchHit {`
  - Purpose: `ContentSearchHit` is a struct representing a single content search result with file path, line number bounds, matched code snippet, and optional language identifier. [crates/gcode/src/models.rs:445-452]
- `symbol_make_id_matches_python_uuid5_golden_vectors` (function) component `symbol_make_id_matches_python_uuid5_golden_vectors [function]` (`4533ee40-6423-5279-8785-15875d6f7fc9`) lines 459-507 [crates/gcode/src/models.rs:459-507]
  - Signature: `fn symbol_make_id_matches_python_uuid5_golden_vectors() {`
  - Purpose: This test function validates that the Rust `Symbol::make_id()` implementation produces deterministic UUID5 hashes matching golden vectors, ensuring compatibility with Python's UUID5 algorithm across varying symbol metadata combinations. [crates/gcode/src/models.rs:459-507]
- `unresolved_and_external_ids_match_python_uuid5_golden_vectors` (function) component `unresolved_and_external_ids_match_python_uuid5_golden_vectors [function]` (`ac941e96-b083-5250-8a28-68695123b0a0`) lines 510-523 [crates/gcode/src/models.rs:510-523]
  - Signature: `fn unresolved_and_external_ids_match_python_uuid5_golden_vectors() {`
  - Purpose: Tests that `make_unresolved_callee_id` and `make_external_symbol_id` functions generate UUID5 values matching predefined golden vector assertions. [crates/gcode/src/models.rs:510-523]
- `test_call_relation_promotes_symbol_targets` (function) component `test_call_relation_promotes_symbol_targets [function]` (`6947ce0d-faca-5753-98ed-17486a1fa73b`) lines 525-536 [crates/gcode/src/models.rs:525-536]
  - Signature: `fn test_call_relation_promotes_symbol_targets() {`
  - Purpose: This test verifies that invoking `with_symbol_target` on a `CallRelation` instance correctly populates the `callee_symbol_id` field and sets `callee_target_kind` to `CallTargetKind::Symbol`. [crates/gcode/src/models.rs:525-536]
- `graph_result_metadata_remains_optional_in_json_contract` (function) component `graph_result_metadata_remains_optional_in_json_contract [function]` (`5178ee0f-859e-5c13-81db-4ad63fb170e2`) lines 539-553 [crates/gcode/src/models.rs:539-553]
  - Signature: `fn graph_result_metadata_remains_optional_in_json_contract() {`
  - Purpose: This test verifies that the `metadata` field of a `GraphResult` struct remains optional in JSON serialization, correctly deserializing its absence as `None` and excluding it from the serialized output. [crates/gcode/src/models.rs:539-553]
- `graph_result_without_metadata_omits_metadata_when_serialized` (function) component `graph_result_without_metadata_omits_metadata_when_serialized [function]` (`7eb9f494-a44f-5b90-878b-0aea097637e0`) lines 556-590 [crates/gcode/src/models.rs:556-590]
  - Signature: `fn graph_result_without_metadata_omits_metadata_when_serialized() {`
  - Purpose: This property-based test verifies that a `GraphResult` struct's JSON serialization omits the `metadata` field when its value is `None`. [crates/gcode/src/models.rs:556-590]

