---
title: crates/gwiki/src/paths.rs
type: code_file
provenance:
- file: crates/gwiki/src/paths.rs
  ranges:
  - 6-22
  - 24-27
  - 29-34
  - 42-47
  - 50-55
  - 58-69
  - 71-86
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/paths.rs:6-22](crates/gwiki/src/paths.rs#L6-L22), [crates/gwiki/src/paths.rs:24-27](crates/gwiki/src/paths.rs#L24-L27), [crates/gwiki/src/paths.rs:29-34](crates/gwiki/src/paths.rs#L29-L34), [crates/gwiki/src/paths.rs:42-47](crates/gwiki/src/paths.rs#L42-L47), [crates/gwiki/src/paths.rs:50-55](crates/gwiki/src/paths.rs#L50-L55), [crates/gwiki/src/paths.rs:58-69](crates/gwiki/src/paths.rs#L58-L69), [crates/gwiki/src/paths.rs:71-86](crates/gwiki/src/paths.rs#L71-L86)

</details>

# crates/gwiki/src/paths.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file centralizes safe source-path handling for wiki imports: `validate_source_id` trims a source id and rejects empty or path-traversal/absolute-style values, `raw_source_path` turns a validated id into `raw/<id>.md`, and `derived_markdown_path` turns a `SourceRecord` into `knowledge/sources/<id>.md` using the same validation. The test helpers confirm that whitespace is trimmed, unsafe ids are rejected, and derived paths fail for unsafe records but succeed once the id is normalized.
[crates/gwiki/src/paths.rs:6-22]
[crates/gwiki/src/paths.rs:24-27]
[crates/gwiki/src/paths.rs:29-34]
[crates/gwiki/src/paths.rs:42-47]
[crates/gwiki/src/paths.rs:50-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `validate_source_id` | function | `pub(crate) fn validate_source_id(id: &str) -> Result<&str, WikiError> {` | `validate_source_id [function]` | `f44ef678-8bc5-5370-aeb0-c042baf76495` | 6-22 [crates/gwiki/src/paths.rs:6-22] | Indexed function `validate_source_id` in `crates/gwiki/src/paths.rs`. [crates/gwiki/src/paths.rs:6-22] |
| `raw_source_path` | function | `pub(crate) fn raw_source_path(id: &str) -> Result<PathBuf, WikiError> {` | `raw_source_path [function]` | `be470f5c-3563-57b3-97d4-c510585771ad` | 24-27 [crates/gwiki/src/paths.rs:24-27] | Indexed function `raw_source_path` in `crates/gwiki/src/paths.rs`. [crates/gwiki/src/paths.rs:24-27] |
| `derived_markdown_path` | function | `pub(crate) fn derived_markdown_path(record: &SourceRecord) -> Result<PathBuf, WikiError> {` | `derived_markdown_path [function]` | `682eff63-2406-59e7-a292-72aabdbb5da9` | 29-34 [crates/gwiki/src/paths.rs:29-34] | Indexed function `derived_markdown_path` in `crates/gwiki/src/paths.rs`. [crates/gwiki/src/paths.rs:29-34] |
| `source_paths_trim_safe_ids` | function | `fn source_paths_trim_safe_ids() {` | `source_paths_trim_safe_ids [function]` | `7843c171-65c3-5f8c-ba04-733ed32600e8` | 42-47 [crates/gwiki/src/paths.rs:42-47] | Indexed function `source_paths_trim_safe_ids` in `crates/gwiki/src/paths.rs`. [crates/gwiki/src/paths.rs:42-47] |
| `source_paths_reject_unsafe_ids` | function | `fn source_paths_reject_unsafe_ids() {` | `source_paths_reject_unsafe_ids [function]` | `f52cee7f-848d-5095-b038-ca59e8bfa79b` | 50-55 [crates/gwiki/src/paths.rs:50-55] | Indexed function `source_paths_reject_unsafe_ids` in `crates/gwiki/src/paths.rs`. [crates/gwiki/src/paths.rs:50-55] |
| `derived_markdown_path_rejects_unsafe_source_ids` | function | `fn derived_markdown_path_rejects_unsafe_source_ids() {` | `derived_markdown_path_rejects_unsafe_source_ids [function]` | `069e17bb-32f3-537c-b781-9e6c4721dd68` | 58-69 [crates/gwiki/src/paths.rs:58-69] | Indexed function `derived_markdown_path_rejects_unsafe_source_ids` in `crates/gwiki/src/paths.rs`. [crates/gwiki/src/paths.rs:58-69] |
| `source_record` | function | `fn source_record(id: &str) -> SourceRecord {` | `source_record [function]` | `094d5f48-cc2e-56c7-ad86-c98d8dba0687` | 71-86 [crates/gwiki/src/paths.rs:71-86] | Indexed function `source_record` in `crates/gwiki/src/paths.rs`. [crates/gwiki/src/paths.rs:71-86] |
