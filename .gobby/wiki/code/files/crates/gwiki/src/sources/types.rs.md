---
title: crates/gwiki/src/sources/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/types.rs
  ranges:
  - 12-29
  - 31-51
  - 32-50
  - 55-58
  - 60-67
  - 61-66
  - 71-74
  - 76-83
  - 77-82
  - 86-96
  - 98-150
  - 99-116
  - 118-124
  - 126-129
  - 131-134
  - 136-139
  - 141-144
  - 146-149
  - 152-162
  - 165-179
  - 183-189
  - 191-198
  - 192-197
  - 201-216
  - 218-245
  - 219-229
  - 231-244
  - 247-249
  - 251-259
  - 261-274
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/types.rs

Module: [[code/modules/crates/gwiki/src/sources|crates/gwiki/src/sources]]

## Purpose

`crates/gwiki/src/sources/types.rs` exposes 30 indexed API symbols.
[crates/gwiki/src/sources/types.rs:12-29]
[crates/gwiki/src/sources/types.rs:31-51]
[crates/gwiki/src/sources/types.rs:32-50]
[crates/gwiki/src/sources/types.rs:55-58]
[crates/gwiki/src/sources/types.rs:60-67]

## API Symbols

- `SourceKind` (type) component `SourceKind [type]` (`8b758196-f7d8-5d59-b91b-dddde418094a`) lines 12-29 [crates/gwiki/src/sources/types.rs:12-29]
  - Signature: `pub enum SourceKind {`
  - Purpose: Indexed type `SourceKind` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:12-29]
- `SourceKind` (class) component `SourceKind [class]` (`5936801e-9940-56ea-931a-6cbe08780739`) lines 31-51 [crates/gwiki/src/sources/types.rs:31-51]
  - Signature: `impl fmt::Display for SourceKind {`
  - Purpose: Implements the `fmt::Display` trait for `SourceKind`, mapping each enum variant to its corresponding lowercase string representation via pattern matching. [crates/gwiki/src/sources/types.rs:31-51]
- `SourceKind.fmt` (method) component `SourceKind.fmt [method]` (`c7ff205b-8363-5c43-8450-0c766e6347d8`) lines 32-50 [crates/gwiki/src/sources/types.rs:32-50]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: This method implements the `Display` trait by matching on enum variants and writing each variant's corresponding lowercase string representation to the formatter. [crates/gwiki/src/sources/types.rs:32-50]
- `IngestionMethod` (type) component `IngestionMethod [type]` (`c17769c3-5495-562b-86fb-521153c39217`) lines 55-58 [crates/gwiki/src/sources/types.rs:55-58]
  - Signature: `pub enum IngestionMethod {`
  - Purpose: Indexed type `IngestionMethod` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:55-58]
- `IngestionMethod` (class) component `IngestionMethod [class]` (`f46961b7-60e2-5227-9362-772c87807c2c`) lines 60-67 [crates/gwiki/src/sources/types.rs:60-67]
  - Signature: `impl fmt::Display for IngestionMethod {`
  - Purpose: Implements the `Display` trait for the `IngestionMethod` enum, mapping its `Manual` and `Research` variants to their respective string representations ("manual" and "research"). [crates/gwiki/src/sources/types.rs:60-67]
- `IngestionMethod.fmt` (method) component `IngestionMethod.fmt [method]` (`4bc9987b-89ce-5327-96a8-9530c6a82262`) lines 61-66 [crates/gwiki/src/sources/types.rs:61-66]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: This method implements custom string formatting for an enum by pattern matching on self and writing the corresponding string literal ("manual" or "research") to the provided formatter. [crates/gwiki/src/sources/types.rs:61-66]
- `CompileStatus` (type) component `CompileStatus [type]` (`fca71646-4457-548a-9c90-d339db8d7f57`) lines 71-74 [crates/gwiki/src/sources/types.rs:71-74]
  - Signature: `pub enum CompileStatus {`
  - Purpose: Indexed type `CompileStatus` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:71-74]
- `CompileStatus` (class) component `CompileStatus [class]` (`3edcac4c-01dc-5407-bf0a-902911710861`) lines 76-83 [crates/gwiki/src/sources/types.rs:76-83]
  - Signature: `impl fmt::Display for CompileStatus {`
  - Purpose: Implements the `fmt::Display` trait for `CompileStatus` to render its enum variants (`Pending`, `Compiled`) as lowercase string representations. [crates/gwiki/src/sources/types.rs:76-83]
- `CompileStatus.fmt` (method) component `CompileStatus.fmt [method]` (`38236796-e917-5b3c-809b-b2453104fde3`) lines 77-82 [crates/gwiki/src/sources/types.rs:77-82]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: This method implements the `Display` trait by writing the string representation of an enum variant (`"pending"` or `"compiled"`) to the provided formatter. [crates/gwiki/src/sources/types.rs:77-82]
- `SourceDraft` (class) component `SourceDraft [class]` (`a500f118-4197-5ad9-9cdc-d124c17571d7`) lines 86-96 [crates/gwiki/src/sources/types.rs:86-96]
  - Signature: `pub struct SourceDraft {`
  - Purpose: SourceDraft encapsulates a fetched source's byte content with associated metadata (location, kind, fetch timestamp, optional title/citation/license) and processing state (ingestion method, compile status). [crates/gwiki/src/sources/types.rs:86-96]
- `SourceDraft` (class) component `SourceDraft [class]` (`33b03758-0364-5ba8-a747-f65ee307de8b`) lines 98-150 [crates/gwiki/src/sources/types.rs:98-150]
  - Signature: `impl SourceDraft {`
  - Purpose: `SourceDraft` implements a builder pattern with a primary constructor and convenience factory method (`url`) for creating source objects, plus chainable setter methods for optional metadata and configuration fields. [crates/gwiki/src/sources/types.rs:98-150]
- `SourceDraft.new` (method) component `SourceDraft.new [method]` (`9ba6bea9-28bb-528c-b810-54d3747b1555`) lines 99-116 [crates/gwiki/src/sources/types.rs:99-116]
  - Signature: `pub fn new(`
  - Purpose: Constructs a new instance with the provided location, source kind, fetch timestamp, and byte content, initializing optional metadata fields (title, citation, license) as None and compile status as Pending. [crates/gwiki/src/sources/types.rs:99-116]
- `SourceDraft.url` (method) component `SourceDraft.url [method]` (`27bf00ef-04d3-5a91-86e1-baf0dedc5620`) lines 118-124 [crates/gwiki/src/sources/types.rs:118-124]
  - Signature: `pub fn url(`
  - Purpose: Constructs a URL-typed Source instance with the given location string, fetch timestamp, and content bytes. [crates/gwiki/src/sources/types.rs:118-124]
- `SourceDraft.with_title` (method) component `SourceDraft.with_title [method]` (`38657335-7c91-59d6-b891-4799a00dc930`) lines 126-129 [crates/gwiki/src/sources/types.rs:126-129]
  - Signature: `pub fn with_title(mut self, title: impl Into<String>) -> Self {`
  - Purpose: A builder method that accepts a type implementing `Into<String>`, converts and wraps it as `Some` in the title field, and returns `self` for method chaining. [crates/gwiki/src/sources/types.rs:126-129]
- `SourceDraft.with_citation` (method) component `SourceDraft.with_citation [method]` (`64e1473c-540b-524b-87d9-a2e17e79e115`) lines 131-134 [crates/gwiki/src/sources/types.rs:131-134]
  - Signature: `pub fn with_citation(mut self, citation: impl Into<String>) -> Self {`
  - Purpose: Sets the `citation` field to a `Some` variant containing the converted String parameter and returns `self` to enable method chaining. [crates/gwiki/src/sources/types.rs:131-134]
- `SourceDraft.with_license` (method) component `SourceDraft.with_license [method]` (`4668cd27-42ca-5fb3-89df-d7b7456cb832`) lines 136-139 [crates/gwiki/src/sources/types.rs:136-139]
  - Signature: `pub fn with_license(mut self, license: impl Into<String>) -> Self {`
  - Purpose: Consumes self, sets its license field to `Some(license.into())`, and returns the modified instance to enable method chaining. [crates/gwiki/src/sources/types.rs:136-139]
- `SourceDraft.with_ingestion_method` (method) component `SourceDraft.with_ingestion_method [method]` (`e077a26c-d43f-5210-88f3-206bf697f0f0`) lines 141-144 [crates/gwiki/src/sources/types.rs:141-144]
  - Signature: `pub fn with_ingestion_method(mut self, method: IngestionMethod) -> Self {`
  - Purpose: This is a builder pattern method that mutates the ingestion_method field and returns self to enable fluent method chaining. [crates/gwiki/src/sources/types.rs:141-144]
- `SourceDraft.with_compile_status` (method) component `SourceDraft.with_compile_status [method]` (`f0707ea8-0ecc-5f5c-addd-c0d9767290c5`) lines 146-149 [crates/gwiki/src/sources/types.rs:146-149]
  - Signature: `pub fn with_compile_status(mut self, status: CompileStatus) -> Self {`
  - Purpose: This is a builder pattern method that sets the `compile_status` field to the provided `CompileStatus` value and returns `self` to enable fluent method chaining. [crates/gwiki/src/sources/types.rs:146-149]
- `SourceDraftRef` (class) component `SourceDraftRef [class]` (`e575ee1c-8cf3-573d-bd82-22095636f6ae`) lines 152-162 [crates/gwiki/src/sources/types.rs:152-162]
  - Signature: `pub(crate) struct SourceDraftRef<'a> {`
  - Purpose: `SourceDraftRef<'a>` is a crate-internal struct that wraps a borrowed byte slice of source content with associated metadata including location, kind, ingestion method, compilation status, and optional attribution fields. [crates/gwiki/src/sources/types.rs:152-162]
- `SourceRecord` (class) component `SourceRecord [class]` (`875299cc-ea97-543e-87b2-6d73cec4bd98`) lines 165-179 [crates/gwiki/src/sources/types.rs:165-179]
  - Signature: `pub struct SourceRecord {`
  - Purpose: SourceRecord is a serializable struct that aggregates source document metadata—identity, location, content hash, and optional bibliographic fields—alongside processing state including ingestion method and compilation status. [crates/gwiki/src/sources/types.rs:165-179]
- `SourceReplay` (type) component `SourceReplay [type]` (`240f8474-f1e0-52c8-a89a-7ce7577dd9ca`) lines 183-189 [crates/gwiki/src/sources/types.rs:183-189]
  - Signature: `pub enum SourceReplay {`
  - Purpose: Indexed type `SourceReplay` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:183-189]
- `SourceReplay` (class) component `SourceReplay [class]` (`fae6c226-9b73-5179-ad5d-661bcc9e8d69`) lines 191-198 [crates/gwiki/src/sources/types.rs:191-198]
  - Signature: `impl SourceReplay {`
  - Purpose: SourceReplay implements a `local_file` factory method that constructs a LocalFile enum variant from a filesystem path and IngestFileOptions. [crates/gwiki/src/sources/types.rs:191-198]
- `SourceReplay.local_file` (method) component `SourceReplay.local_file [method]` (`87011e0f-70f4-597b-9438-867b7de96945`) lines 192-197 [crates/gwiki/src/sources/types.rs:192-197]
  - Signature: `pub(crate) fn local_file(path: PathBuf, options: &IngestFileOptions) -> Self {`
  - Purpose: Creates a `LocalFile` enum variant that encapsulates a file path and converts the provided `IngestFileOptions` into `SourceReplayOptions`. [crates/gwiki/src/sources/types.rs:192-197]
- `SourceReplayOptions` (class) component `SourceReplayOptions [class]` (`077c4e82-e940-5261-beb2-13c25c6de786`) lines 201-216 [crates/gwiki/src/sources/types.rs:201-216]
  - Signature: `pub struct SourceReplayOptions {`
  - Purpose: A serializable configuration struct that specifies replay options including AI/translation toggles, target language, video frame sampling interval, and optional routing directives for transcription, vision, and text processing pipelines. [crates/gwiki/src/sources/types.rs:201-216]
- `SourceReplayOptions` (class) component `SourceReplayOptions [class]` (`947afab6-e15f-5dad-8125-a859db6b17a6`) lines 218-245 [crates/gwiki/src/sources/types.rs:218-245]
  - Signature: `impl SourceReplayOptions {`
  - Purpose: `SourceReplayOptions` implements bidirectional conversion with `IngestFileOptions`, serializing routing configurations to string names in one direction and parsing them back in the reverse direction. [crates/gwiki/src/sources/types.rs:218-245]
- `SourceReplayOptions.from_ingest_file_options` (method) component `SourceReplayOptions.from_ingest_file_options [method]` (`37489d9d-7d73-5174-bdba-72e54009a0d6`) lines 219-229 [crates/gwiki/src/sources/types.rs:219-229]
  - Signature: `pub(crate) fn from_ingest_file_options(options: &IngestFileOptions) -> Self {`
  - Purpose: This method constructs a `Self` instance from an `IngestFileOptions` reference by copying configuration fields directly while transforming optional routing fields through the `routing_name` function. [crates/gwiki/src/sources/types.rs:219-229]
- `SourceReplayOptions.to_ingest_file_options` (method) component `SourceReplayOptions.to_ingest_file_options [method]` (`ee4dfc2b-02bf-5315-b679-2455aaf542ba`) lines 231-244 [crates/gwiki/src/sources/types.rs:231-244]
  - Signature: `pub(crate) fn to_ingest_file_options(&self) -> Result<IngestFileOptions, WikiError> {`
  - Purpose: Converts the current instance into an `IngestFileOptions` struct by copying configuration fields and parsing three routing specifications (`transcription_routing`, `vision_routing`, `text_routing`), returning a `Result` that fails if any routing parse fails. [crates/gwiki/src/sources/types.rs:231-244]
- `is_false` (function) component `is_false [function]` (`3600fe38-8b85-546a-a9e3-4179e120c5dd`) lines 247-249 [crates/gwiki/src/sources/types.rs:247-249]
  - Signature: `fn is_false(value: &bool) -> bool {`
  - Purpose: Returns the logical negation of the dereferenced boolean reference. [crates/gwiki/src/sources/types.rs:247-249]
- `routing_name` (function) component `routing_name [function]` (`3e8b6526-3c4a-5bf9-9624-e5cd4cc5a8e0`) lines 251-259 [crates/gwiki/src/sources/types.rs:251-259]
  - Signature: `fn routing_name(routing: AiRouting) -> String {`
  - Purpose: Converts an `AiRouting` enum variant to its corresponding lowercase string representation via pattern matching. [crates/gwiki/src/sources/types.rs:251-259]
- `parse_routing` (function) component `parse_routing [function]` (`54fbd985-78bf-52a9-b8b5-ec10d2c683ce`) lines 261-274 [crates/gwiki/src/sources/types.rs:261-274]
  - Signature: `fn parse_routing(`
  - Purpose: Parses an optional string value into an `AiRouting` type using `from_str`, returning a `Result<Option<AiRouting>, WikiError>` that wraps parse failures with field-specific error context. [crates/gwiki/src/sources/types.rs:261-274]

