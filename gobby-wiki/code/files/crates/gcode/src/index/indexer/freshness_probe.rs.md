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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/freshness_probe.rs:37-81](crates/gcode/src/index/indexer/freshness_probe.rs#L37-L81), [crates/gcode/src/index/indexer/freshness_probe.rs:89-96](crates/gcode/src/index/indexer/freshness_probe.rs#L89-L96), [crates/gcode/src/index/indexer/freshness_probe.rs:98-105](crates/gcode/src/index/indexer/freshness_probe.rs#L98-L105), [crates/gcode/src/index/indexer/freshness_probe.rs:109-111](crates/gcode/src/index/indexer/freshness_probe.rs#L109-L111), [crates/gcode/src/index/indexer/freshness_probe.rs:113-115](crates/gcode/src/index/indexer/freshness_probe.rs#L113-L115), [crates/gcode/src/index/indexer/freshness_probe.rs:118-138](crates/gcode/src/index/indexer/freshness_probe.rs#L118-L138), [crates/gcode/src/index/indexer/freshness_probe.rs:141-156](crates/gcode/src/index/indexer/freshness_probe.rs#L141-L156), [crates/gcode/src/index/indexer/freshness_probe.rs:159-176](crates/gcode/src/index/indexer/freshness_probe.rs#L159-L176), [crates/gcode/src/index/indexer/freshness_probe.rs:179-195](crates/gcode/src/index/indexer/freshness_probe.rs#L179-L195), [crates/gcode/src/index/indexer/freshness_probe.rs:198-235](crates/gcode/src/index/indexer/freshness_probe.rs#L198-L235), [crates/gcode/src/index/indexer/freshness_probe.rs:238-265](crates/gcode/src/index/indexer/freshness_probe.rs#L238-L265)

</details>

# crates/gcode/src/index/indexer/freshness_probe.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

Implements a lock-free, hash-free freshness pre-gate for the indexer: `project_changed_since` compares discovered on-disk files against the recorded index and last index time to quickly decide whether the caller can skip the advisory lock and incremental reconcile, or must fall through to a full refresh. It mirrors the indexer’s discovery rules via `walker::discover_files_with_options` and `DEFAULT_EXCLUDES`, applies a small skew margin so it only errs toward refreshing, and treats newer, newly added, or missing previously indexed paths as change. The helper functions (`write_file`, `set_mtime`, `base_time`, `default_options`) support the test cases, which cover unchanged trees, modified files, added files, deletions, skew-boundary behavior, and gitignore-respecting discovery.
[crates/gcode/src/index/indexer/freshness_probe.rs:37-81]
[crates/gcode/src/index/indexer/freshness_probe.rs:89-96]
[crates/gcode/src/index/indexer/freshness_probe.rs:98-105]
[crates/gcode/src/index/indexer/freshness_probe.rs:109-111]
[crates/gcode/src/index/indexer/freshness_probe.rs:113-115]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `project_changed_since` | function | `pub fn project_changed_since(` | `project_changed_since [function]` | `d30b24ca-520a-57b2-885f-fb0f1d2fe538` | 37-81 [crates/gcode/src/index/indexer/freshness_probe.rs:37-81] | Indexed function `project_changed_since` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:37-81] |
| `write_file` | function | `fn write_file(root: &Path, rel: &str, contents: &[u8]) -> PathBuf {` | `write_file [function]` | `d4fc0ae1-b01a-5027-9c1c-91ce4e5a2e64` | 89-96 [crates/gcode/src/index/indexer/freshness_probe.rs:89-96] | Indexed function `write_file` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:89-96] |
| `set_mtime` | function | `fn set_mtime(path: &Path, time: SystemTime) {` | `set_mtime [function]` | `2b097022-1ca0-54ab-9167-230f31715fe8` | 98-105 [crates/gcode/src/index/indexer/freshness_probe.rs:98-105] | Indexed function `set_mtime` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:98-105] |
| `base_time` | function | `fn base_time() -> SystemTime {` | `base_time [function]` | `4d80ef56-1326-501d-ad99-6e76e8e39313` | 109-111 [crates/gcode/src/index/indexer/freshness_probe.rs:109-111] | Indexed function `base_time` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:109-111] |
| `default_options` | function | `fn default_options() -> walker::DiscoveryOptions {` | `default_options [function]` | `3cced7cf-62ab-5c52-8e0f-591a88557847` | 113-115 [crates/gcode/src/index/indexer/freshness_probe.rs:113-115] | Indexed function `default_options` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:113-115] |
| `reports_no_change_when_everything_predates_last_index` | function | `fn reports_no_change_when_everything_predates_last_index() {` | `reports_no_change_when_everything_predates_last_index [function]` | `dcaf9766-7e19-519d-adc8-445c84c6402d` | 118-138 [crates/gcode/src/index/indexer/freshness_probe.rs:118-138] | Indexed function `reports_no_change_when_everything_predates_last_index` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:118-138] |
| `reports_change_when_a_file_is_modified_after_last_index` | function | `fn reports_change_when_a_file_is_modified_after_last_index() {` | `reports_change_when_a_file_is_modified_after_last_index [function]` | `9cac490e-8989-5a1b-a5fc-e393f19f9aac` | 141-156 [crates/gcode/src/index/indexer/freshness_probe.rs:141-156] | Indexed function `reports_change_when_a_file_is_modified_after_last_index` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:141-156] |
| `reports_change_for_newly_added_file` | function | `fn reports_change_for_newly_added_file() {` | `reports_change_for_newly_added_file [function]` | `b8ca0cd0-0cde-5646-866f-ff724633a2c9` | 159-176 [crates/gcode/src/index/indexer/freshness_probe.rs:159-176] | Indexed function `reports_change_for_newly_added_file` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:159-176] |
| `reports_change_when_indexed_file_is_deleted` | function | `fn reports_change_when_indexed_file_is_deleted() {` | `reports_change_when_indexed_file_is_deleted [function]` | `8452e4b9-b88a-5e12-af81-285c2aaf39fe` | 179-195 [crates/gcode/src/index/indexer/freshness_probe.rs:179-195] | Indexed function `reports_change_when_indexed_file_is_deleted` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:179-195] |
| `skew_margin_boundary_only_ever_makes_the_gate_more_eager` | function | `fn skew_margin_boundary_only_ever_makes_the_gate_more_eager() {` | `skew_margin_boundary_only_ever_makes_the_gate_more_eager [function]` | `06f747c0-d77a-5408-802b-60d142616c74` | 198-235 [crates/gcode/src/index/indexer/freshness_probe.rs:198-235] | Indexed function `skew_margin_boundary_only_ever_makes_the_gate_more_eager` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:198-235] |
| `gitignored_new_files_follow_respect_gitignore_setting` | function | `fn gitignored_new_files_follow_respect_gitignore_setting() {` | `gitignored_new_files_follow_respect_gitignore_setting [function]` | `4fc2ee8c-d38a-51cf-97de-7c9fa10bf90c` | 238-265 [crates/gcode/src/index/indexer/freshness_probe.rs:238-265] | Indexed function `gitignored_new_files_follow_respect_gitignore_setting` in `crates/gcode/src/index/indexer/freshness_probe.rs`. [crates/gcode/src/index/indexer/freshness_probe.rs:238-265] |
