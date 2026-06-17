---
title: crates/gwiki/src/sources/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/types.rs
  ranges:
  - 12-30
  - 33-52
  - 57-60
  - 63-68
  - 73-76
  - 79-84
  - 88-98
  - 101-118
  - 120-126
  - 128-131
  - 133-136
  - 138-141
  - 143-146
  - 148-151
  - 154-164
  - 167-181
  - 185-191
  - 194-199
  - 203-218
  - 221-231
  - 233-246
  - 249-251
  - 253-261
  - 263-276
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/sources/types.rs:12-30](crates/gwiki/src/sources/types.rs#L12-L30), [crates/gwiki/src/sources/types.rs:33-52](crates/gwiki/src/sources/types.rs#L33-L52), [crates/gwiki/src/sources/types.rs:57-60](crates/gwiki/src/sources/types.rs#L57-L60), [crates/gwiki/src/sources/types.rs:63-68](crates/gwiki/src/sources/types.rs#L63-L68), [crates/gwiki/src/sources/types.rs:73-76](crates/gwiki/src/sources/types.rs#L73-L76), [crates/gwiki/src/sources/types.rs:79-84](crates/gwiki/src/sources/types.rs#L79-L84), [crates/gwiki/src/sources/types.rs:88-98](crates/gwiki/src/sources/types.rs#L88-L98), [crates/gwiki/src/sources/types.rs:101-118](crates/gwiki/src/sources/types.rs#L101-L118), [crates/gwiki/src/sources/types.rs:120-126](crates/gwiki/src/sources/types.rs#L120-L126), [crates/gwiki/src/sources/types.rs:128-131](crates/gwiki/src/sources/types.rs#L128-L131), [crates/gwiki/src/sources/types.rs:133-136](crates/gwiki/src/sources/types.rs#L133-L136), [crates/gwiki/src/sources/types.rs:138-141](crates/gwiki/src/sources/types.rs#L138-L141), [crates/gwiki/src/sources/types.rs:143-146](crates/gwiki/src/sources/types.rs#L143-L146), [crates/gwiki/src/sources/types.rs:148-151](crates/gwiki/src/sources/types.rs#L148-L151), [crates/gwiki/src/sources/types.rs:154-164](crates/gwiki/src/sources/types.rs#L154-L164), [crates/gwiki/src/sources/types.rs:167-181](crates/gwiki/src/sources/types.rs#L167-L181), [crates/gwiki/src/sources/types.rs:185-191](crates/gwiki/src/sources/types.rs#L185-L191), [crates/gwiki/src/sources/types.rs:194-199](crates/gwiki/src/sources/types.rs#L194-L199), [crates/gwiki/src/sources/types.rs:203-218](crates/gwiki/src/sources/types.rs#L203-L218), [crates/gwiki/src/sources/types.rs:221-231](crates/gwiki/src/sources/types.rs#L221-L231), [crates/gwiki/src/sources/types.rs:233-246](crates/gwiki/src/sources/types.rs#L233-L246), [crates/gwiki/src/sources/types.rs:249-251](crates/gwiki/src/sources/types.rs#L249-L251), [crates/gwiki/src/sources/types.rs:253-261](crates/gwiki/src/sources/types.rs#L253-L261), [crates/gwiki/src/sources/types.rs:263-276](crates/gwiki/src/sources/types.rs#L263-L276)

</details>

# crates/gwiki/src/sources/types.rs

Module: [[code/modules/crates/gwiki/src/sources|crates/gwiki/src/sources]]

## Purpose

Defines the source metadata and replay types used by `gwiki` ingestion. It provides string-serialized enums for source kind, ingestion method, and compile status, plus `Display` impls so each maps to a stable lowercase name. It also defines `SourceDraft` as the mutable in-memory representation of an ingested source with builder-style setters, `SourceDraftRef` and `SourceRecord` for reference and persisted forms, and `SourceReplay`/`SourceReplayOptions` for reconstructing a source from local ingest-file settings. The small helper functions support serde defaults and routing-name parsing for AI routing configuration.
[crates/gwiki/src/sources/types.rs:12-30]
[crates/gwiki/src/sources/types.rs:33-52]
[crates/gwiki/src/sources/types.rs:57-60]
[crates/gwiki/src/sources/types.rs:63-68]
[crates/gwiki/src/sources/types.rs:73-76]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SourceKind` | type | `pub enum SourceKind {` | `SourceKind [type]` | `8b758196-f7d8-5d59-b91b-dddde418094a` | 12-30 [crates/gwiki/src/sources/types.rs:12-30] | Indexed type `SourceKind` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:12-30] |
| `SourceKind::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `SourceKind::fmt [method]` | `c70bbd60-68f0-5ad3-a472-d6e068b9c274` | 33-52 [crates/gwiki/src/sources/types.rs:33-52] | Indexed method `SourceKind::fmt` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:33-52] |
| `IngestionMethod` | type | `pub enum IngestionMethod {` | `IngestionMethod [type]` | `45a4625a-38e5-5ebd-ba9d-beb6e2b8e4a3` | 57-60 [crates/gwiki/src/sources/types.rs:57-60] | Indexed type `IngestionMethod` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:57-60] |
| `IngestionMethod::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `IngestionMethod::fmt [method]` | `69e035de-0392-50fb-9e3c-60b043fcbe5e` | 63-68 [crates/gwiki/src/sources/types.rs:63-68] | Indexed method `IngestionMethod::fmt` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:63-68] |
| `CompileStatus` | type | `pub enum CompileStatus {` | `CompileStatus [type]` | `37785b5b-aef1-5a6f-9f37-f03a9913b936` | 73-76 [crates/gwiki/src/sources/types.rs:73-76] | Indexed type `CompileStatus` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:73-76] |
| `CompileStatus::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `CompileStatus::fmt [method]` | `60b40a94-ee52-5e55-aaa6-75b6b8a632c8` | 79-84 [crates/gwiki/src/sources/types.rs:79-84] | Indexed method `CompileStatus::fmt` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:79-84] |
| `SourceDraft` | class | `pub struct SourceDraft {` | `SourceDraft [class]` | `d8037a4d-2645-58dd-9d8e-f3cb67bab0c9` | 88-98 [crates/gwiki/src/sources/types.rs:88-98] | Indexed class `SourceDraft` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:88-98] |
| `SourceDraft::new` | method | `pub fn new(` | `SourceDraft::new [method]` | `521189f6-f475-5b4c-95c0-ff67a9f4d95a` | 101-118 [crates/gwiki/src/sources/types.rs:101-118] | Indexed method `SourceDraft::new` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:101-118] |
| `SourceDraft::url` | method | `pub fn url(` | `SourceDraft::url [method]` | `e04bc6be-b85c-52f3-ae65-dd128c373b4c` | 120-126 [crates/gwiki/src/sources/types.rs:120-126] | Indexed method `SourceDraft::url` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:120-126] |
| `SourceDraft::with_title` | method | `pub fn with_title(mut self, title: impl Into<String>) -> Self {` | `SourceDraft::with_title [method]` | `01678433-e34e-5783-99dd-c24220eff5c6` | 128-131 [crates/gwiki/src/sources/types.rs:128-131] | Indexed method `SourceDraft::with_title` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:128-131] |
| `SourceDraft::with_citation` | method | `pub fn with_citation(mut self, citation: impl Into<String>) -> Self {` | `SourceDraft::with_citation [method]` | `e01fa1fc-42e3-58eb-b8af-c3a8debf05cd` | 133-136 [crates/gwiki/src/sources/types.rs:133-136] | Indexed method `SourceDraft::with_citation` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:133-136] |
| `SourceDraft::with_license` | method | `pub fn with_license(mut self, license: impl Into<String>) -> Self {` | `SourceDraft::with_license [method]` | `14913e01-5199-559d-96a9-03c76003ec30` | 138-141 [crates/gwiki/src/sources/types.rs:138-141] | Indexed method `SourceDraft::with_license` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:138-141] |
| `SourceDraft::with_ingestion_method` | method | `pub fn with_ingestion_method(mut self, method: IngestionMethod) -> Self {` | `SourceDraft::with_ingestion_method [method]` | `7ab804ac-3b7c-50e9-8c34-151744020e22` | 143-146 [crates/gwiki/src/sources/types.rs:143-146] | Indexed method `SourceDraft::with_ingestion_method` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:143-146] |
| `SourceDraft::with_compile_status` | method | `pub fn with_compile_status(mut self, status: CompileStatus) -> Self {` | `SourceDraft::with_compile_status [method]` | `9b49bc2a-9b23-53c1-95cc-41dfadb5a586` | 148-151 [crates/gwiki/src/sources/types.rs:148-151] | Indexed method `SourceDraft::with_compile_status` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:148-151] |
| `SourceDraftRef` | class | `pub(crate) struct SourceDraftRef<'a> {` | `SourceDraftRef [class]` | `8b50815c-0ea8-5353-82c1-247b267a0111` | 154-164 [crates/gwiki/src/sources/types.rs:154-164] | Indexed class `SourceDraftRef` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:154-164] |
| `SourceRecord` | class | `pub struct SourceRecord {` | `SourceRecord [class]` | `c14ad2df-751b-5b3b-a1c1-e702f06a205f` | 167-181 [crates/gwiki/src/sources/types.rs:167-181] | Indexed class `SourceRecord` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:167-181] |
| `SourceReplay` | type | `pub enum SourceReplay {` | `SourceReplay [type]` | `d928dd51-0e6d-5981-b3f2-06968f01f56a` | 185-191 [crates/gwiki/src/sources/types.rs:185-191] | Indexed type `SourceReplay` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:185-191] |
| `SourceReplay::local_file` | method | `pub(crate) fn local_file(path: PathBuf, options: &IngestFileOptions) -> Self {` | `SourceReplay::local_file [method]` | `f1754d33-8a99-5fee-86f8-e15c2c10397f` | 194-199 [crates/gwiki/src/sources/types.rs:194-199] | Indexed method `SourceReplay::local_file` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:194-199] |
| `SourceReplayOptions` | class | `pub struct SourceReplayOptions {` | `SourceReplayOptions [class]` | `89e805ef-4571-5838-814e-976ac47a7ee2` | 203-218 [crates/gwiki/src/sources/types.rs:203-218] | Indexed class `SourceReplayOptions` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:203-218] |
| `SourceReplayOptions::from_ingest_file_options` | method | `pub(crate) fn from_ingest_file_options(options: &IngestFileOptions) -> Self {` | `SourceReplayOptions::from_ingest_file_options [method]` | `ce11198a-0576-5e27-bcc7-8833478a0bab` | 221-231 [crates/gwiki/src/sources/types.rs:221-231] | Indexed method `SourceReplayOptions::from_ingest_file_options` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:221-231] |
| `SourceReplayOptions::to_ingest_file_options` | method | `pub(crate) fn to_ingest_file_options(&self) -> Result<IngestFileOptions, WikiError> {` | `SourceReplayOptions::to_ingest_file_options [method]` | `65c04634-c2d6-5b85-a5d4-7e42735aa281` | 233-246 [crates/gwiki/src/sources/types.rs:233-246] | Indexed method `SourceReplayOptions::to_ingest_file_options` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:233-246] |
| `is_false` | function | `fn is_false(value: &bool) -> bool {` | `is_false [function]` | `6f259c7c-6cce-5685-a48f-d79fe692a564` | 249-251 [crates/gwiki/src/sources/types.rs:249-251] | Indexed function `is_false` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:249-251] |
| `routing_name` | function | `fn routing_name(routing: AiRouting) -> String {` | `routing_name [function]` | `10f87276-d6dc-5321-aabb-4ea47b620d8e` | 253-261 [crates/gwiki/src/sources/types.rs:253-261] | Indexed function `routing_name` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:253-261] |
| `parse_routing` | function | `fn parse_routing(` | `parse_routing [function]` | `627ae794-d79e-5e9a-a3c9-48afbd81bb50` | 263-276 [crates/gwiki/src/sources/types.rs:263-276] | Indexed function `parse_routing` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:263-276] |
