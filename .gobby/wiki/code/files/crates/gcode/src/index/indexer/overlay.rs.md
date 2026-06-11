---
title: crates/gcode/src/index/indexer/overlay.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/overlay.rs
  ranges:
  - 32-35
  - 38-44
  - 46-82
  - 84-255
  - 257-288
  - 290-299
  - 301-321
  - 323-375
  - 377-393
  - 395-400
  - 402-407
  - 409-414
  - 416-429
  - 431-447
  - 455-462
  - 466-470
  - 474-483
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/overlay.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

`crates/gcode/src/index/indexer/overlay.rs` exposes 17 indexed API symbols.
[crates/gcode/src/index/indexer/overlay.rs:32-35]
[crates/gcode/src/index/indexer/overlay.rs:38-44]
[crates/gcode/src/index/indexer/overlay.rs:46-82]
[crates/gcode/src/index/indexer/overlay.rs:84-255]
[crates/gcode/src/index/indexer/overlay.rs:257-288]

## API Symbols

- `IndexedFileState` (class) component `IndexedFileState [class]` (`ac812838-0378-5a0c-b089-0b10d8c497c8`) lines 32-35 [crates/gcode/src/index/indexer/overlay.rs:32-35]
  - Signature: `pub(super) struct IndexedFileState {`
  - Purpose: IndexedFileState is a module-private struct that stores a content hash and language identifier for an indexed file. [crates/gcode/src/index/indexer/overlay.rs:32-35]
- `OverlayReconcileAction` (type) component `OverlayReconcileAction [type]` (`6be8f7b3-67d5-5a31-9d4d-5e27f5ddc9f0`) lines 38-44 [crates/gcode/src/index/indexer/overlay.rs:38-44]
  - Signature: `pub(super) enum OverlayReconcileAction {`
  - Purpose: Indexed type `OverlayReconcileAction` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:38-44]
- `overlay_reconcile_action` (function) component `overlay_reconcile_action [function]` (`be1729cf-c48d-5d6e-8ccf-bfee68ce411e`) lines 46-82 [crates/gcode/src/index/indexer/overlay.rs:46-82]
  - Signature: `pub(super) fn overlay_reconcile_action(`
  - Purpose: Determines the overlay reconciliation action by evaluating file existence, parent content hash consistency, indexability, and parent/overlay state configurations to decide whether to skip, tombstone, delete, inherit, or index the file. [crates/gcode/src/index/indexer/overlay.rs:46-82]
- `index_overlay_files` (function) component `index_overlay_files [function]` (`01ec77cc-48df-5af6-ad42-b9d5800cf9ad`) lines 84-255 [crates/gcode/src/index/indexer/overlay.rs:84-255]
  - Signature: `pub(super) fn index_overlay_files(`
  - Purpose: Discovers and indexes overlay project files by reconciling candidates against parent and overlay indexed file states, applies optional path filtering, and separates files for AST parsing versus content-only processing. [crates/gcode/src/index/indexer/overlay.rs:84-255]
- `overlay_reconcile_candidates` (function) component `overlay_reconcile_candidates [function]` (`d8a9fdbf-e6be-5cef-ba09-479c03c7e522`) lines 257-288 [crates/gcode/src/index/indexer/overlay.rs:257-288]
  - Signature: `fn overlay_reconcile_candidates(`
  - Purpose: Reconciles candidate file paths from multiple indices (AST, content, parent, overlay) into a sorted, deduplicated vector of relative paths according to the IndexRequest's selection mode: explicit files, full scope, git-tracked changes, or all files as fallback. [crates/gcode/src/index/indexer/overlay.rs:257-288]
- `paths_by_relative` (function) component `paths_by_relative [function]` (`d0c535c9-f938-5584-99a0-02a2a7c3c113`) lines 290-299 [crates/gcode/src/index/indexer/overlay.rs:290-299]
  - Signature: `fn paths_by_relative(root_path: &Path, paths: &[PathBuf]) -> HashMap<String, PathBuf> {`
  - Purpose: # paths_by_relative

Constructs a HashMap mapping relative path strings (derived from each input path relative to root_path) to their original PathBuf values, filtering out paths that fail relative resolution. [crates/gcode/src/index/indexer/overlay.rs:290-299]
- `indexed_file_states` (function) component `indexed_file_states [function]` (`10340c10-e576-5d26-badb-81bc9e42948a`) lines 301-321 [crates/gcode/src/index/indexer/overlay.rs:301-321]
  - Signature: `fn indexed_file_states(`
  - Purpose: Queries the `code_indexed_files` table to construct and return a HashMap mapping file paths to their IndexedFileState records (content hash and language) for a given project ID. [crates/gcode/src/index/indexer/overlay.rs:301-321]
- `git_status_relative_paths` (function) component `git_status_relative_paths [function]` (`4b108bd2-677f-5b6f-baae-1a9687543be0`) lines 323-375 [crates/gcode/src/index/indexer/overlay.rs:323-375]
  - Signature: `fn git_status_relative_paths(root_path: &Path) -> anyhow::Result<HashSet<String>> {`
  - Purpose: Returns a HashSet of relative file paths representing modified and untracked files by parsing the NUL-delimited `git status --porcelain=v1` output with timeout and error handling. [crates/gcode/src/index/indexer/overlay.rs:323-375]
- `git_status_timeout` (function) component `git_status_timeout [function]` (`4024a0a6-07dc-543a-9b66-60e72d24e7d8`) lines 377-393 [crates/gcode/src/index/indexer/overlay.rs:377-393]
  - Signature: `fn git_status_timeout() -> Duration {`
  - Purpose: Returns a `Duration` for git status operations by parsing the `GIT_STATUS_TIMEOUT_ENV` environment variable as seconds, with fallback to `DEFAULT_GIT_STATUS_TIMEOUT_SECS` on invalid or missing values. [crates/gcode/src/index/indexer/overlay.rs:377-393]
- `compact_stderr` (function) component `compact_stderr [function]` (`af592e27-20e6-5df0-b6b1-1ca5703f5d03`) lines 395-400 [crates/gcode/src/index/indexer/overlay.rs:395-400]
  - Signature: `fn compact_stderr(stderr: &[u8]) -> String {`
  - Purpose: Converts stderr bytes to UTF-8 and collapses consecutive whitespace into single spaces. [crates/gcode/src/index/indexer/overlay.rs:395-400]
- `is_porcelain_status_entry` (function) component `is_porcelain_status_entry [function]` (`271a6fa6-20dd-501e-bd1a-35ee1d99229f`) lines 402-407 [crates/gcode/src/index/indexer/overlay.rs:402-407]
  - Signature: `fn is_porcelain_status_entry(entry: &[u8]) -> bool {`
  - Purpose: Checks if a byte slice conforms to the porcelain status format by validating it has at least 4 bytes with two consecutive valid status bytes followed by a space character. [crates/gcode/src/index/indexer/overlay.rs:402-407]
- `valid_porcelain_status_byte` (function) component `valid_porcelain_status_byte [function]` (`ea312341-5b87-59ce-b013-88a15ba48909`) lines 409-414 [crates/gcode/src/index/indexer/overlay.rs:409-414]
  - Signature: `fn valid_porcelain_status_byte(byte: u8) -> bool {`
  - Purpose: Returns `true` if the input byte is a valid git porcelain status code (space, M, A, D, R, C, U, ?, or !). [crates/gcode/src/index/indexer/overlay.rs:409-414]
- `rel_matches_filter` (function) component `rel_matches_filter [function]` (`f6a4f46d-0e79-54eb-b222-2cd0b7d7fb2d`) lines 416-429 [crates/gcode/src/index/indexer/overlay.rs:416-429]
  - Signature: `fn rel_matches_filter(root_path: &Path, path_filter: &Path, rel: &str) -> bool {`
  - Purpose: Determines whether a relative path, when resolved to an absolute path, is contained within a canonicalized filter path, falling back to lexical comparison for non-existent files. [crates/gcode/src/index/indexer/overlay.rs:416-429]
- `write_tombstone` (function) component `write_tombstone [function]` (`c37b5340-8902-5b1c-a469-944a66f25bf7`) lines 431-447 [crates/gcode/src/index/indexer/overlay.rs:431-447]
  - Signature: `fn write_tombstone(conn: &mut Client, project_id: &str, rel: &str) -> anyhow::Result<()> {`
  - Purpose: Performs a transactional soft delete by removing all indexed code facts for a file and replacing it with a tombstone record marked with special deletion metadata. [crates/gcode/src/index/indexer/overlay.rs:431-447]
- `porcelain_status_byte_validation_matches_git_v1_codes` (function) component `porcelain_status_byte_validation_matches_git_v1_codes [function]` (`a63915cd-692d-554d-8c7f-dd8ea3ea7ee5`) lines 455-462 [crates/gcode/src/index/indexer/overlay.rs:455-462]
  - Signature: `fn porcelain_status_byte_validation_matches_git_v1_codes() {`
  - Purpose: Unit test that validates the `valid_porcelain_status_byte` function correctly recognizes all nine Git v1 porcelain status codes (space, M, A, D, R, C, U, ?, !) and rejects invalid bytes. [crates/gcode/src/index/indexer/overlay.rs:455-462]
- `git_status_timeout_reads_positive_env_seconds` (function) component `git_status_timeout_reads_positive_env_seconds [function]` (`c9bef015-43b7-5f85-a5cc-342eed480209`) lines 466-470 [crates/gcode/src/index/indexer/overlay.rs:466-470]
  - Signature: `fn git_status_timeout_reads_positive_env_seconds() {`
  - Purpose: This test verifies that `git_status_timeout()` correctly reads and converts the `GCODE_GIT_STATUS_TIMEOUT_SECS` environment variable to a Duration object. [crates/gcode/src/index/indexer/overlay.rs:466-470]
- `git_status_timeout_rejects_invalid_env_values` (function) component `git_status_timeout_rejects_invalid_env_values [function]` (`02ff068b-adbd-5741-8b94-ffcdbb71daa9`) lines 474-483 [crates/gcode/src/index/indexer/overlay.rs:474-483]
  - Signature: `fn git_status_timeout_rejects_invalid_env_values() {`
  - Purpose: This test asserts that `git_status_timeout()` returns the default timeout duration when the `GCODE_GIT_STATUS_TIMEOUT_SECS` environment variable is set to invalid values (zero, negative, or non-numeric strings). [crates/gcode/src/index/indexer/overlay.rs:474-483]

