---
title: crates/gwiki/src/ingest/session/derived.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/derived.rs
  ranges:
  - 10-26
  - 28-52
  - 54-81
  - 83-105
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/derived.rs:10-26](crates/gwiki/src/ingest/session/derived.rs#L10-L26), [crates/gwiki/src/ingest/session/derived.rs:28-52](crates/gwiki/src/ingest/session/derived.rs#L28-L52), [crates/gwiki/src/ingest/session/derived.rs:54-81](crates/gwiki/src/ingest/session/derived.rs#L54-L81), [crates/gwiki/src/ingest/session/derived.rs:83-105](crates/gwiki/src/ingest/session/derived.rs#L83-L105)

</details>

# crates/gwiki/src/ingest/session/derived.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Writes derived session markdown files into a vault safely and atomically. `write_session_derived_markdown` computes the record’s derived markdown path, creates any missing parent directories under the vault root, and delegates to the atomic writer, returning the relative path on success. The lower-level helpers build a temporary file in the target directory, write and `sync` the contents, persist it over the destination, and then sync the parent directory so the on-disk update is durable.
[crates/gwiki/src/ingest/session/derived.rs:10-26]
[crates/gwiki/src/ingest/session/derived.rs:28-52]
[crates/gwiki/src/ingest/session/derived.rs:54-81]
[crates/gwiki/src/ingest/session/derived.rs:83-105]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `write_session_derived_markdown` | function | `pub(crate) fn write_session_derived_markdown(` | `write_session_derived_markdown [function]` | `82b642e1-4d58-5219-8a89-17488dd8dec4` | 10-26 [crates/gwiki/src/ingest/session/derived.rs:10-26] | Indexed function `write_session_derived_markdown` in `crates/gwiki/src/ingest/session/derived.rs`. [crates/gwiki/src/ingest/session/derived.rs:10-26] |
| `write_session_markdown_atomically` | function | `fn write_session_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {` | `write_session_markdown_atomically [function]` | `3338d0be-7796-5e7a-9fa4-00839f887ac7` | 28-52 [crates/gwiki/src/ingest/session/derived.rs:28-52] | Indexed function `write_session_markdown_atomically` in `crates/gwiki/src/ingest/session/derived.rs`. [crates/gwiki/src/ingest/session/derived.rs:28-52] |
| `create_session_temp_file` | function | `fn create_session_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {` | `create_session_temp_file [function]` | `032602f1-ad47-5140-8bd2-cd0feb01b5ed` | 54-81 [crates/gwiki/src/ingest/session/derived.rs:54-81] | Indexed function `create_session_temp_file` in `crates/gwiki/src/ingest/session/derived.rs`. [crates/gwiki/src/ingest/session/derived.rs:54-81] |
| `sync_parent_dir` | function | `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {` | `sync_parent_dir [function]` | `5898354c-8cb0-54fe-be64-8431c3445df4` | 83-105 [crates/gwiki/src/ingest/session/derived.rs:83-105] | Indexed function `sync_parent_dir` in `crates/gwiki/src/ingest/session/derived.rs`. [crates/gwiki/src/ingest/session/derived.rs:83-105] |
