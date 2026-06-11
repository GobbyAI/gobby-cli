---
title: crates/gwiki/src/commands/refresh/candidate.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/candidate.rs
  ranges:
  - 15-74
  - 76-173
  - 175-214
  - 216-224
  - 226-245
  - 247-273
  - 275-310
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/candidate.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

`crates/gwiki/src/commands/refresh/candidate.rs` exposes 7 indexed API symbols.
[crates/gwiki/src/commands/refresh/candidate.rs:15-74]
[crates/gwiki/src/commands/refresh/candidate.rs:76-173]
[crates/gwiki/src/commands/refresh/candidate.rs:175-214]
[crates/gwiki/src/commands/refresh/candidate.rs:216-224]
[crates/gwiki/src/commands/refresh/candidate.rs:226-245]

## API Symbols

- `refresh_url_candidate` (function) component `refresh_url_candidate [function]` (`a7c9fd4c-051e-5770-9312-3bc6c06b84f9`) lines 15-74 [crates/gwiki/src/commands/refresh/candidate.rs:15-74]
  - Signature: `pub(crate) fn refresh_url_candidate(`
  - Purpose: Fetches a URL source, compares its content hash to the stored record, and categorizes the outcome as unchanged, successfully refreshed with mutations persisted, or failed into respective result vectors. [crates/gwiki/src/commands/refresh/candidate.rs:15-74]
- `refresh_local_candidate` (function) component `refresh_local_candidate [function]` (`48af8e2b-650e-5dc6-bf51-9b4ed587c3f5`) lines 76-173 [crates/gwiki/src/commands/refresh/candidate.rs:76-173]
  - Signature: `pub(crate) fn refresh_local_candidate(`
  - Purpose: Validates a local candidate file by comparing its computed content hash against the stored record hash, staging changed files for re-ingestion with resolved ingest options and AI context. [crates/gwiki/src/commands/refresh/candidate.rs:76-173]
- `local_file_hash` (function) component `local_file_hash [function]` (`c2499481-b616-52a5-b31f-4718867fc6f2`) lines 175-214 [crates/gwiki/src/commands/refresh/candidate.rs:175-214]
  - Signature: `fn local_file_hash(record: &SourceRecord, path: &Path) -> Result<String, RefreshFailure> {`
  - Purpose: Validates that a file path exists and is readable, then returns its content hash or a `RefreshFailure` with contextual error details. [crates/gwiki/src/commands/refresh/candidate.rs:175-214]
- `local_file_failure` (function) component `local_file_failure [function]` (`127f7552-2e11-530b-ae47-f15b8e508c33`) lines 216-224 [crates/gwiki/src/commands/refresh/candidate.rs:216-224]
  - Signature: `fn local_file_failure(record: &SourceRecord, code: &str, message: String) -> RefreshFailure {`
  - Purpose: Constructs and returns a `RefreshFailure` struct by extracting the record's id, location, and kind while including the provided error code and message. [crates/gwiki/src/commands/refresh/candidate.rs:216-224]
- `refresh_changed_url_source` (function) component `refresh_changed_url_source [function]` (`0617c338-79c5-5ba3-8339-0cbf68291f33`) lines 226-245 [crates/gwiki/src/commands/refresh/candidate.rs:226-245]
  - Signature: `fn refresh_changed_url_source(`
  - Purpose: Refreshes a URL-sourced artifact by ingesting a new snapshot and finalizing the update with removal of previous asset paths. [crates/gwiki/src/commands/refresh/candidate.rs:226-245]
- `refresh_changed_local_source` (function) component `refresh_changed_local_source [function]` (`83f8620d-bb18-5b19-a613-960b9176b15a`) lines 247-273 [crates/gwiki/src/commands/refresh/candidate.rs:247-273]
  - Signature: `fn refresh_changed_local_source(`
  - Purpose: Refreshes a previously ingested local source by re-ingesting the file and computing the changeset relative to the prior SourceRecord. [crates/gwiki/src/commands/refresh/candidate.rs:247-273]
- `finalize_changed_refresh` (function) component `finalize_changed_refresh [function]` (`9c9623fa-6398-5989-ac54-83c7fee1fd7a`) lines 275-310 [crates/gwiki/src/commands/refresh/candidate.rs:275-310]
  - Signature: `fn finalize_changed_refresh(`
  - Purpose: Finalizes a source refresh by removing obsolete file paths (excluding current raw/asset paths), purging the previous manifest entry, and returning the updated ingest result with cleanup metadata. [crates/gwiki/src/commands/refresh/candidate.rs:275-310]

