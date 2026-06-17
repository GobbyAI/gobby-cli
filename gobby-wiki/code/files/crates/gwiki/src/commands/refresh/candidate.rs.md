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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/refresh/candidate.rs:15-74](crates/gwiki/src/commands/refresh/candidate.rs#L15-L74), [crates/gwiki/src/commands/refresh/candidate.rs:76-173](crates/gwiki/src/commands/refresh/candidate.rs#L76-L173), [crates/gwiki/src/commands/refresh/candidate.rs:175-214](crates/gwiki/src/commands/refresh/candidate.rs#L175-L214), [crates/gwiki/src/commands/refresh/candidate.rs:216-224](crates/gwiki/src/commands/refresh/candidate.rs#L216-L224), [crates/gwiki/src/commands/refresh/candidate.rs:226-245](crates/gwiki/src/commands/refresh/candidate.rs#L226-L245), [crates/gwiki/src/commands/refresh/candidate.rs:247-273](crates/gwiki/src/commands/refresh/candidate.rs#L247-L273), [crates/gwiki/src/commands/refresh/candidate.rs:275-310](crates/gwiki/src/commands/refresh/candidate.rs#L275-L310)

</details>

# crates/gwiki/src/commands/refresh/candidate.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

Implements the refresh pipeline for candidate sources, handling both URL-backed and local-file-backed records. `refresh_url_candidate` and `refresh_local_candidate` fetch or replay source content, compare hashes against the stored record, and route each candidate into unchanged, refreshed, or failed outputs. The helper functions support this flow by hashing local files, converting local read failures into refresh failures, rebuilding changed source records, and finalizing the result by updating paths and source metadata.
[crates/gwiki/src/commands/refresh/candidate.rs:15-74]
[crates/gwiki/src/commands/refresh/candidate.rs:76-173]
[crates/gwiki/src/commands/refresh/candidate.rs:175-214]
[crates/gwiki/src/commands/refresh/candidate.rs:216-224]
[crates/gwiki/src/commands/refresh/candidate.rs:226-245]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `refresh_url_candidate` | function | `pub(crate) fn refresh_url_candidate(` | `refresh_url_candidate [function]` | `a7c9fd4c-051e-5770-9312-3bc6c06b84f9` | 15-74 [crates/gwiki/src/commands/refresh/candidate.rs:15-74] | Indexed function `refresh_url_candidate` in `crates/gwiki/src/commands/refresh/candidate.rs`. [crates/gwiki/src/commands/refresh/candidate.rs:15-74] |
| `refresh_local_candidate` | function | `pub(crate) fn refresh_local_candidate(` | `refresh_local_candidate [function]` | `48af8e2b-650e-5dc6-bf51-9b4ed587c3f5` | 76-173 [crates/gwiki/src/commands/refresh/candidate.rs:76-173] | Indexed function `refresh_local_candidate` in `crates/gwiki/src/commands/refresh/candidate.rs`. [crates/gwiki/src/commands/refresh/candidate.rs:76-173] |
| `local_file_hash` | function | `fn local_file_hash(record: &SourceRecord, path: &Path) -> Result<String, RefreshFailure> {` | `local_file_hash [function]` | `c2499481-b616-52a5-b31f-4718867fc6f2` | 175-214 [crates/gwiki/src/commands/refresh/candidate.rs:175-214] | Indexed function `local_file_hash` in `crates/gwiki/src/commands/refresh/candidate.rs`. [crates/gwiki/src/commands/refresh/candidate.rs:175-214] |
| `local_file_failure` | function | `fn local_file_failure(record: &SourceRecord, code: &str, message: String) -> RefreshFailure {` | `local_file_failure [function]` | `127f7552-2e11-530b-ae47-f15b8e508c33` | 216-224 [crates/gwiki/src/commands/refresh/candidate.rs:216-224] | Indexed function `local_file_failure` in `crates/gwiki/src/commands/refresh/candidate.rs`. [crates/gwiki/src/commands/refresh/candidate.rs:216-224] |
| `refresh_changed_url_source` | function | `fn refresh_changed_url_source(` | `refresh_changed_url_source [function]` | `0617c338-79c5-5ba3-8339-0cbf68291f33` | 226-245 [crates/gwiki/src/commands/refresh/candidate.rs:226-245] | Indexed function `refresh_changed_url_source` in `crates/gwiki/src/commands/refresh/candidate.rs`. [crates/gwiki/src/commands/refresh/candidate.rs:226-245] |
| `refresh_changed_local_source` | function | `fn refresh_changed_local_source(` | `refresh_changed_local_source [function]` | `83f8620d-bb18-5b19-a613-960b9176b15a` | 247-273 [crates/gwiki/src/commands/refresh/candidate.rs:247-273] | Indexed function `refresh_changed_local_source` in `crates/gwiki/src/commands/refresh/candidate.rs`. [crates/gwiki/src/commands/refresh/candidate.rs:247-273] |
| `finalize_changed_refresh` | function | `fn finalize_changed_refresh(` | `finalize_changed_refresh [function]` | `9c9623fa-6398-5989-ac54-83c7fee1fd7a` | 275-310 [crates/gwiki/src/commands/refresh/candidate.rs:275-310] | Indexed function `finalize_changed_refresh` in `crates/gwiki/src/commands/refresh/candidate.rs`. [crates/gwiki/src/commands/refresh/candidate.rs:275-310] |
