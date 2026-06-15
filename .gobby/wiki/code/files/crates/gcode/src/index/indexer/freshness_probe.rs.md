---
title: crates/gcode/src/index/indexer/freshness_probe.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/freshness_probe.rs
  ranges:
  - 37-81
  - 89-96
  - 98-105
  - 109-111
  - 113-115
  - 118-138
  - 141-156
  - 159-176
  - 179-195
  - 198-235
  - 238-265
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/freshness_probe.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file implements a lock-free freshness pre-gate for the indexer: `project_changed_since` quickly decides whether a project has changed since the last index by comparing discovered file mtimes against a skew-adjusted threshold and by checking whether any previously indexed paths have disappeared. It mirrors the indexer’s discovery rules, including default excludes and optional discovery settings, so the “needs refresh” decision stays aligned with what the indexer actually sees. The small helpers support the tests by creating files, forcing mtimes, and providing a fixed base timestamp, and the test cases cover the main change-detection paths: unchanged trees, modified or newly added files, deleted indexed files, skew-margin behavior, and `.gitignore` handling.
[crates/gcode/src/index/indexer/freshness_probe.rs:37-81]
[crates/gcode/src/index/indexer/freshness_probe.rs:89-96]
[crates/gcode/src/index/indexer/freshness_probe.rs:98-105]
[crates/gcode/src/index/indexer/freshness_probe.rs:109-111]
[crates/gcode/src/index/indexer/freshness_probe.rs:113-115]

## API Symbols

- `project_changed_since` (function) component `project_changed_since [function]` (`d30b24ca-520a-57b2-885f-fb0f1d2fe538`) lines 37-81 [crates/gcode/src/index/indexer/freshness_probe.rs:37-81]
  - Signature: `pub fn project_changed_since(`
  - Purpose: Returns `true` if the project has been modified since a timestamp by detecting files with mtime newer than a skew-adjusted threshold or by discovering that previously-indexed paths no longer exist on disk. [crates/gcode/src/index/indexer/freshness_probe.rs:37-81]
- `write_file` (function) component `write_file [function]` (`d4fc0ae1-b01a-5027-9c1c-91ce4e5a2e64`) lines 89-96 [crates/gcode/src/index/indexer/freshness_probe.rs:89-96]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &[u8]) -> PathBuf {`
  - Purpose: Writes byte contents to a file at the path formed by joining a root directory with a relative path, creating all necessary parent directories, and returns the resulting PathBuf. [crates/gcode/src/index/indexer/freshness_probe.rs:89-96]
- `set_mtime` (function) component `set_mtime [function]` (`2b097022-1ca0-54ab-9167-230f31715fe8`) lines 98-105 [crates/gcode/src/index/indexer/freshness_probe.rs:98-105]
  - Signature: `fn set_mtime(path: &Path, time: SystemTime) {`
  - Purpose: Opens a file at the given path in write mode and sets its modification timestamp to the specified `SystemTime`, panicking if either operation fails. [crates/gcode/src/index/indexer/freshness_probe.rs:98-105]
- `base_time` (function) component `base_time [function]` (`4d80ef56-1326-501d-ad99-6e76e8e39313`) lines 109-111 [crates/gcode/src/index/indexer/freshness_probe.rs:109-111]
  - Signature: `fn base_time() -> SystemTime {`
  - Purpose: `base_time()` returns a `SystemTime` representing 1,700,000,000 seconds after the Unix epoch. [crates/gcode/src/index/indexer/freshness_probe.rs:109-111]
- `default_options` (function) component `default_options [function]` (`3cced7cf-62ab-5c52-8e0f-591a88557847`) lines 113-115 [crates/gcode/src/index/indexer/freshness_probe.rs:113-115]
  - Signature: `fn default_options() -> walker::DiscoveryOptions {`
  - Purpose: Returns a default-initialized `walker::DiscoveryOptions` instance by delegating to its `Default` trait implementation. [crates/gcode/src/index/indexer/freshness_probe.rs:113-115]
- `reports_no_change_when_everything_predates_last_index` (function) component `reports_no_change_when_everything_predates_last_index [function]` (`dcaf9766-7e19-519d-adc8-445c84c6402d`) lines 118-138 [crates/gcode/src/index/indexer/freshness_probe.rs:118-138]
  - Signature: `fn reports_no_change_when_everything_predates_last_index() {`
  - Purpose: This test verifies that `project_changed_since()` correctly returns `false` when all indexed files have modification times earlier than the last indexing timestamp. [crates/gcode/src/index/indexer/freshness_probe.rs:118-138]
- `reports_change_when_a_file_is_modified_after_last_index` (function) component `reports_change_when_a_file_is_modified_after_last_index [function]` (`9cac490e-8989-5a1b-a5fc-e393f19f9aac`) lines 141-156 [crates/gcode/src/index/indexer/freshness_probe.rs:141-156]
  - Signature: `fn reports_change_when_a_file_is_modified_after_last_index() {`
  - Purpose: This test verifies that `project_changed_since` correctly returns `true` when a tracked file's modification timestamp exceeds the specified last indexing timestamp. [crates/gcode/src/index/indexer/freshness_probe.rs:141-156]
- `reports_change_for_newly_added_file` (function) component `reports_change_for_newly_added_file [function]` (`b8ca0cd0-0cde-5646-866f-ff724633a2c9`) lines 159-176 [crates/gcode/src/index/indexer/freshness_probe.rs:159-176]
  - Signature: `fn reports_change_for_newly_added_file() {`
  - Purpose: This test verifies that `project_changed_since` correctly detects an unindexed file with a recent modification time as a project change. [crates/gcode/src/index/indexer/freshness_probe.rs:159-176]
- `reports_change_when_indexed_file_is_deleted` (function) component `reports_change_when_indexed_file_is_deleted [function]` (`8452e4b9-b88a-5e12-af81-285c2aaf39fe`) lines 179-195 [crates/gcode/src/index/indexer/freshness_probe.rs:179-195]
  - Signature: `fn reports_change_when_indexed_file_is_deleted() {`
  - Purpose: This test verifies that `project_changed_since` correctly detects a project change when an indexed file is deleted from disk. [crates/gcode/src/index/indexer/freshness_probe.rs:179-195]
- `skew_margin_boundary_only_ever_makes_the_gate_more_eager` (function) component `skew_margin_boundary_only_ever_makes_the_gate_more_eager [function]` (`06f747c0-d77a-5408-802b-60d142616c74`) lines 198-235 [crates/gcode/src/index/indexer/freshness_probe.rs:198-235]
  - Signature: `fn skew_margin_boundary_only_ever_makes_the_gate_more_eager() {`
  - Purpose: This test verifies that the `project_changed_since` change-detection gate correctly applies SKEW_MARGIN thresholding, detecting changes within the margin while treating files at or beyond the boundary as unchanged. [crates/gcode/src/index/indexer/freshness_probe.rs:198-235]
- `gitignored_new_files_follow_respect_gitignore_setting` (function) component `gitignored_new_files_follow_respect_gitignore_setting [function]` (`4fc2ee8c-d38a-51cf-97de-7c9fa10bf90c`) lines 238-265 [crates/gcode/src/index/indexer/freshness_probe.rs:238-265]
  - Signature: `fn gitignored_new_files_follow_respect_gitignore_setting() {`
  - Purpose: This test asserts that new files matching `.gitignore` rules are excluded from `project_changed_since` detection when `respect_gitignore: true` and included when `respect_gitignore: false`. [crates/gcode/src/index/indexer/freshness_probe.rs:238-265]

