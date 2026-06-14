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

# crates/gwiki/src/paths.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides safe path construction for gwiki source files by validating source IDs before they are turned into filesystem paths. `validate_source_id` trims and rejects empty or traversal-like IDs, `raw_source_path` maps a safe ID to `raw/<id>.md`, and `derived_markdown_path` maps a safe `SourceRecord` ID to `knowledge/sources/<id>.md`; the tests cover trimming, rejection of unsafe inputs, and the derived-path case.
[crates/gwiki/src/paths.rs:6-22]
[crates/gwiki/src/paths.rs:24-27]
[crates/gwiki/src/paths.rs:29-34]
[crates/gwiki/src/paths.rs:42-47]
[crates/gwiki/src/paths.rs:50-55]

## API Symbols

- `validate_source_id` (function) component `validate_source_id [function]` (`f44ef678-8bc5-5370-aeb0-c042baf76495`) lines 6-22 [crates/gwiki/src/paths.rs:6-22]
  - Signature: `pub(crate) fn validate_source_id(id: &str) -> Result<&str, WikiError> {`
  - Purpose: Trims 'id' and returns it only if it is non-empty and does not contain path traversal or separator components ('..', '/', '\', or any non-'Component::Normal' path component), otherwise returns 'WikiError::InvalidInput' for 'source_id'. [crates/gwiki/src/paths.rs:6-22]
- `raw_source_path` (function) component `raw_source_path [function]` (`be470f5c-3563-57b3-97d4-c510585771ad`) lines 24-27 [crates/gwiki/src/paths.rs:24-27]
  - Signature: `pub(crate) fn raw_source_path(id: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Validates 'id' as a source identifier and returns the 'raw/<id>.md' path as a 'PathBuf', propagating 'WikiError' if validation fails. [crates/gwiki/src/paths.rs:24-27]
- `derived_markdown_path` (function) component `derived_markdown_path [function]` (`682eff63-2406-59e7-a292-72aabdbb5da9`) lines 29-34 [crates/gwiki/src/paths.rs:29-34]
  - Signature: `pub(crate) fn derived_markdown_path(record: &SourceRecord) -> Result<PathBuf, WikiError> {`
  - Purpose: Validates 'record.id' as a source ID and returns 'knowledge/sources/{id}.md' as a 'PathBuf', or a 'WikiError' if validation fails. [crates/gwiki/src/paths.rs:29-34]
- `source_paths_trim_safe_ids` (function) component `source_paths_trim_safe_ids [function]` (`7843c171-65c3-5f8c-ba04-733ed32600e8`) lines 42-47 [crates/gwiki/src/paths.rs:42-47]
  - Signature: `fn source_paths_trim_safe_ids() {`
  - Purpose: Verifies that 'raw_source_path' trims surrounding whitespace from a safe source ID like '" src-abc "' and resolves it to 'PathBuf::from("raw/src-abc.md")'. [crates/gwiki/src/paths.rs:42-47]
- `source_paths_reject_unsafe_ids` (function) component `source_paths_reject_unsafe_ids [function]` (`f52cee7f-848d-5095-b038-ca59e8bfa79b`) lines 50-55 [crates/gwiki/src/paths.rs:50-55]
  - Signature: `fn source_paths_reject_unsafe_ids() {`
  - Purpose: Verifies that 'raw_source_path' rejects unsafe source IDs such as empty, dot-segment, path-containing, backslash-containing, and dot-dot-containing strings by returning an 'invalid_input' error. [crates/gwiki/src/paths.rs:50-55]
- `derived_markdown_path_rejects_unsafe_source_ids` (function) component `derived_markdown_path_rejects_unsafe_source_ids [function]` (`069e17bb-32f3-537c-b781-9e6c4721dd68`) lines 58-69 [crates/gwiki/src/paths.rs:58-69]
  - Signature: `fn derived_markdown_path_rejects_unsafe_source_ids() {`
  - Purpose: Verifies that 'derived_markdown_path' rejects a source record with an unsafe ID containing '/' by returning 'invalid_input', and produces 'knowledge/sources/src-abc.md' once the ID is changed to a safe value. [crates/gwiki/src/paths.rs:58-69]
- `source_record` (function) component `source_record [function]` (`094d5f48-cc2e-56c7-ad86-c98d8dba0687`) lines 71-86 [crates/gwiki/src/paths.rs:71-86]
  - Signature: `fn source_record(id: &str) -> SourceRecord {`
  - Purpose: Constructs and returns a 'SourceRecord' for the given 'id' with both locations set to 'https://example.test/source', 'kind' set to 'SourceKind::Url', fixed fetched time and hash, no title/citation/license, manual ingestion, pending compile status, and no replay. [crates/gwiki/src/paths.rs:71-86]

