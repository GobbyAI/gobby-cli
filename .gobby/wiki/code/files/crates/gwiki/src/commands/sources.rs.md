---
title: crates/gwiki/src/commands/sources.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/sources.rs
  ranges:
  - 15-23
  - 25-122
  - 125-138
  - 141-146
  - 148-172
  - 175-181
  - 183-193
  - 195-205
  - 208-213
  - 216-219
  - 221-230
  - 232-260
  - 262-301
  - 303-316
  - 318-340
  - 342-363
  - 365-396
  - 398-441
  - 443-462
  - 464-486
  - 488-490
  - 492-525
  - 527-566
  - 568-573
  - 575-585
  - 587-593
  - 595-616
  - 618-657
  - 659-661
  - 669-695
  - 698-716
  - 719-730
  - 733-738
  - 741-767
  - 770-812
  - 815-828
  - 831-839
  - 841-857
  - 859-874
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/sources.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `gwiki` source-management commands for a resolved scope: `execute` reads the source manifest, expands each manifest record into a renderable source entry, and returns a combined listing with any degradation notices, while `execute_remove` finds a source by ID, resolves its raw and asset paths, stages their deletion, updates the manifest and index state, and rolls everything back on failure or dry-run. The rest of the file is supporting machinery for that flow: small data types for listing/index status and path-change tracking, helpers for reading frontmatter and constructing safe vault-relative paths, staging/removal/rollback routines, rendering functions for normal and remove output, and tests that cover listing, path validation, manifest updates, and rollback behavior.
[crates/gwiki/src/commands/sources.rs:15-23]
[crates/gwiki/src/commands/sources.rs:25-122]
[crates/gwiki/src/commands/sources.rs:125-138]
[crates/gwiki/src/commands/sources.rs:141-146]
[crates/gwiki/src/commands/sources.rs:148-172]

## API Symbols

- `execute` (function) component `execute [function]` (`167ef934-b63a-5eca-aec7-0c5f22e01d97`) lines 15-23 [crates/gwiki/src/commands/sources.rs:15-23]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves and validates a command scope from a selection, reads its source manifest, collects source entries while tracking degradations, and renders the aggregated sources to a CommandOutcome. [crates/gwiki/src/commands/sources.rs:15-23]
- `execute_remove` (function) component `execute_remove [function]` (`dbe5d905-40d7-530e-b9c6-3faae16c138c`) lines 25-122 [crates/gwiki/src/commands/sources.rs:25-122]
  - Signature: `pub(crate) fn execute_remove(`
  - Purpose: Removes a source entry by ID from the manifest and stages its associated raw source and asset files for deletion, with atomic rollback on failure and optional dry-run mode. [crates/gwiki/src/commands/sources.rs:25-122]
- `SourceListEntry` (class) component `SourceListEntry [class]` (`8918d9e3-b725-5e08-9d4b-c1333a590fa0`) lines 125-138 [crates/gwiki/src/commands/sources.rs:125-138]
  - Signature: `struct SourceListEntry {`
  - Purpose: Indexed class `SourceListEntry` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:125-138]
- `IndexStatus` (class) component `IndexStatus [class]` (`e773f602-c402-50a2-bd91-57b14bfa10f7`) lines 141-146 [crates/gwiki/src/commands/sources.rs:141-146]
  - Signature: `struct IndexStatus {`
  - Purpose: Indexed class `IndexStatus` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:141-146]
- `IndexStatus` (class) component `IndexStatus [class]` (`58a59908-ef07-5d1e-83f9-e6b7dc55d4eb`) lines 148-172 [crates/gwiki/src/commands/sources.rs:148-172]
  - Signature: `impl IndexStatus {`
  - Purpose: Indexed class `IndexStatus` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:148-172]
- `IndexStatus.not_run` (method) component `IndexStatus.not_run [method]` (`de0e5e0f-5317-54d4-abcc-fb01f5f10e7a`) lines 149-155 [crates/gwiki/src/commands/sources.rs:149-155]
  - Signature: `fn not_run() -> Self {`
  - Purpose: Indexed method `IndexStatus.not_run` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:149-155]
- `IndexStatus.indexed` (method) component `IndexStatus.indexed [method]` (`47b8b301-51d1-537a-bd5f-348f8b39d20f`) lines 157-163 [crates/gwiki/src/commands/sources.rs:157-163]
  - Signature: `fn indexed(counts: IndexCounts) -> Self {`
  - Purpose: Indexed method `IndexStatus.indexed` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:157-163]
- `IndexStatus.degraded` (method) component `IndexStatus.degraded [method]` (`9905546e-9da0-55c4-9ec8-ed7c751d33d8`) lines 165-171 [crates/gwiki/src/commands/sources.rs:165-171]
  - Signature: `fn degraded() -> Self {`
  - Purpose: Indexed method `IndexStatus.degraded` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:165-171]
- `IndexedCounts` (class) component `IndexedCounts [class]` (`fe9bb971-5ef2-5469-9da9-999c18e4c0e1`) lines 175-181 [crates/gwiki/src/commands/sources.rs:175-181]
  - Signature: `struct IndexedCounts {`
  - Purpose: Indexed class `IndexedCounts` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:175-181]
- `IndexedCounts` (class) component `IndexedCounts [class]` (`1f6e5e6c-0978-5e0d-8ec6-428a3d4daaf1`) lines 183-193 [crates/gwiki/src/commands/sources.rs:183-193]
  - Signature: `impl From<IndexCounts> for IndexedCounts {`
  - Purpose: Indexed class `IndexedCounts` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:183-193]
- `IndexedCounts.from` (method) component `IndexedCounts.from [method]` (`c7befe9b-6b20-57d1-b231-1151a10dbd92`) lines 184-192 [crates/gwiki/src/commands/sources.rs:184-192]
  - Signature: `fn from(counts: IndexCounts) -> Self {`
  - Purpose: Indexed method `IndexedCounts.from` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:184-192]
- `RemoveSourceRender` (class) component `RemoveSourceRender [class]` (`140d9da0-befb-53a7-9080-3799cc8e022d`) lines 195-205 [crates/gwiki/src/commands/sources.rs:195-205]
  - Signature: `struct RemoveSourceRender {`
  - Purpose: Indexed class `RemoveSourceRender` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:195-205]
- `PathChanges` (class) component `PathChanges [class]` (`d1ed86ea-c31f-51f4-bec7-6afa749273be`) lines 208-213 [crates/gwiki/src/commands/sources.rs:208-213]
  - Signature: `struct PathChanges {`
  - Purpose: `PathChanges` is a struct that partitions file paths into four categories: removed, kept, missing, and staged-for-removal. [crates/gwiki/src/commands/sources.rs:208-213]
- `StagedRemoval` (class) component `StagedRemoval [class]` (`83449710-11c0-52a3-b8c8-b10c1a33204b`) lines 216-219 [crates/gwiki/src/commands/sources.rs:216-219]
  - Signature: `struct StagedRemoval {`
  - Purpose: `StagedRemoval` is a struct that stores a file's relative path and binary contents for staged deletion operations. [crates/gwiki/src/commands/sources.rs:216-219]
- `source_entries` (function) component `source_entries [function]` (`25b16f6b-d64c-5cbe-95b4-e826d910be13`) lines 221-230 [crates/gwiki/src/commands/sources.rs:221-230]
  - Signature: `fn source_entries(`
  - Purpose: Maps each `SourceRecord` to a `SourceListEntry` by applying `source_entry` to each record while accumulating degradation information, returning a `Result` that either contains the transformed list or a `WikiError`. [crates/gwiki/src/commands/sources.rs:221-230]
- `source_entry` (function) component `source_entry [function]` (`0a5764ea-fd4a-5845-be2c-12402c7c056a`) lines 232-260 [crates/gwiki/src/commands/sources.rs:232-260]
  - Signature: `fn source_entry(`
  - Purpose: Converts a `SourceRecord` into a `SourceListEntry` by loading the corresponding raw source asset file from the vault root directory, or recording a degradation message if the file is missing. [crates/gwiki/src/commands/sources.rs:232-260]
- `read_source_asset` (function) component `read_source_asset [function]` (`2db59a9d-6f61-5685-828d-27626cb26cc3`) lines 262-301 [crates/gwiki/src/commands/sources.rs:262-301]
  - Signature: `fn read_source_asset(`
  - Purpose: Reads a markdown file, parses its frontmatter, and returns the `source_asset` field as a non-empty trimmed string if present and valid, or None otherwise, while collecting validation errors into a degradations vector. [crates/gwiki/src/commands/sources.rs:262-301]
- `stage_raw_source` (function) component `stage_raw_source [function]` (`6155ff77-813a-5eec-8b77-d0e4b5de4c13`) lines 303-316 [crates/gwiki/src/commands/sources.rs:303-316]
  - Signature: `fn stage_raw_source(`
  - Purpose: Stages removal of an existing raw source file or records its path as missing, contingent on the `raw_exists` parameter. [crates/gwiki/src/commands/sources.rs:303-316]
- `stage_source_asset` (function) component `stage_source_asset [function]` (`04a320e4-7c1f-538b-b5f1-cecdbc496e5c`) lines 318-340 [crates/gwiki/src/commands/sources.rs:318-340]
  - Signature: `fn stage_source_asset(`
  - Purpose: Indexed function `stage_source_asset` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:318-340]
- `stage_source_removal` (function) component `stage_source_removal [function]` (`9c58c938-e5bf-52bb-89c3-12635742da40`) lines 342-363 [crates/gwiki/src/commands/sources.rs:342-363]
  - Signature: `fn stage_source_removal(`
  - Purpose: Indexed function `stage_source_removal` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:342-363]
- `remove_staged_source_files` (function) component `remove_staged_source_files [function]` (`4206c29c-562d-5f1f-955b-2b128ca7a17c`) lines 365-396 [crates/gwiki/src/commands/sources.rs:365-396]
  - Signature: `fn remove_staged_source_files(`
  - Purpose: Indexed function `remove_staged_source_files` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:365-396]
- `restore_removed_source_files` (function) component `restore_removed_source_files [function]` (`3aaf390e-414f-5ab9-b57e-f6d902aa136b`) lines 398-441 [crates/gwiki/src/commands/sources.rs:398-441]
  - Signature: `fn restore_removed_source_files(`
  - Purpose: Indexed function `restore_removed_source_files` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:398-441]
- `rollback_removed_source_state` (function) component `rollback_removed_source_state [function]` (`e0c548de-92c2-51df-b9e7-8afaecf308be`) lines 443-462 [crates/gwiki/src/commands/sources.rs:443-462]
  - Signature: `fn rollback_removed_source_state(`
  - Purpose: Indexed function `rollback_removed_source_state` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:443-462]
- `rollback_removed_source` (function) component `rollback_removed_source [function]` (`a4856219-1bda-59b4-9ea5-3232c19f0316`) lines 464-486 [crates/gwiki/src/commands/sources.rs:464-486]
  - Signature: `fn rollback_removed_source(`
  - Purpose: Indexed function `rollback_removed_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:464-486]
- `raw_source_path` (function) component `raw_source_path [function]` (`1d3a56df-c8f1-535d-82ad-63bcc3577694`) lines 488-490 [crates/gwiki/src/commands/sources.rs:488-490]
  - Signature: `fn raw_source_path(id: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `raw_source_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:488-490]
- `source_asset_path` (function) component `source_asset_path [function]` (`a32c7141-942d-5e71-a0a3-5af5b52b1029`) lines 492-525 [crates/gwiki/src/commands/sources.rs:492-525]
  - Signature: `fn source_asset_path(vault_root: &Path, value: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `source_asset_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:492-525]
- `safe_vault_relative_path` (function) component `safe_vault_relative_path [function]` (`1a6f2012-20ca-5dda-8b31-d51fc0183004`) lines 527-566 [crates/gwiki/src/commands/sources.rs:527-566]
  - Signature: `fn safe_vault_relative_path(field: &'static str, value: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `safe_vault_relative_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:527-566]
- `is_raw_asset_path` (function) component `is_raw_asset_path [function]` (`82ebddb6-0324-50c8-85ed-bf1deade3b97`) lines 568-573 [crates/gwiki/src/commands/sources.rs:568-573]
  - Signature: `fn is_raw_asset_path(path: &Path) -> bool {`
  - Purpose: Indexed function `is_raw_asset_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:568-573]
- `ensure_scope_root` (function) component `ensure_scope_root [function]` (`a42e2107-589b-5133-b665-b82c632db8fa`) lines 575-585 [crates/gwiki/src/commands/sources.rs:575-585]
  - Signature: `fn ensure_scope_root(root: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `ensure_scope_root` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:575-585]
- `follow_up_for_removed_source` (function) component `follow_up_for_removed_source [function]` (`92c0eca5-908b-5c59-b059-8c9d792a8114`) lines 587-593 [crates/gwiki/src/commands/sources.rs:587-593]
  - Signature: `fn follow_up_for_removed_source(record: &SourceRecord) -> Vec<&'static str> {`
  - Purpose: Indexed function `follow_up_for_removed_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:587-593]
- `render_sources` (function) component `render_sources [function]` (`370097f7-06a9-54c4-9a4a-f058bcb72c5b`) lines 595-616 [crates/gwiki/src/commands/sources.rs:595-616]
  - Signature: `fn render_sources(`
  - Purpose: Indexed function `render_sources` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:595-616]
- `render_remove_source` (function) component `render_remove_source [function]` (`ce352531-6184-5c31-9171-c6f2547d20db`) lines 618-657 [crates/gwiki/src/commands/sources.rs:618-657]
  - Signature: `fn render_remove_source(render: RemoveSourceRender) -> CommandOutcome {`
  - Purpose: Indexed function `render_remove_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:618-657]
- `display_path` (function) component `display_path [function]` (`5f8b3c2f-05cc-54c1-942f-7ec0b0943520`) lines 659-661 [crates/gwiki/src/commands/sources.rs:659-661]
  - Signature: `fn display_path(path: &Path) -> String {`
  - Purpose: Indexed function `display_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:659-661]
- `source_listing_reads_manifest_raw_path_and_asset` (function) component `source_listing_reads_manifest_raw_path_and_asset [function]` (`21312e15-3e43-5528-a961-c32706c92ecd`) lines 669-695 [crates/gwiki/src/commands/sources.rs:669-695]
  - Signature: `fn source_listing_reads_manifest_raw_path_and_asset() {`
  - Purpose: Indexed function `source_listing_reads_manifest_raw_path_and_asset` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:669-695]
- `missing_raw_file_degrades_without_failing_source_listing` (function) component `missing_raw_file_degrades_without_failing_source_listing [function]` (`a07ac043-cdd3-5464-96b6-e19b5ad08c16`) lines 698-716 [crates/gwiki/src/commands/sources.rs:698-716]
  - Signature: `fn missing_raw_file_degrades_without_failing_source_listing() {`
  - Purpose: Indexed function `missing_raw_file_degrades_without_failing_source_listing` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:698-716]
- `source_asset_path_rejects_traversal_absolute_and_non_raw_assets` (function) component `source_asset_path_rejects_traversal_absolute_and_non_raw_assets [function]` (`4f5cf1d6-4f02-5eed-9284-99d4570e18cf`) lines 719-730 [crates/gwiki/src/commands/sources.rs:719-730]
  - Signature: `fn source_asset_path_rejects_traversal_absolute_and_non_raw_assets() {`
  - Purpose: Indexed function `source_asset_path_rejects_traversal_absolute_and_non_raw_assets` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:719-730]
- `raw_source_path_trims_source_ids_before_building_path` (function) component `raw_source_path_trims_source_ids_before_building_path [function]` (`e25b38e0-3370-50c2-b52a-758e6c8c985e`) lines 733-738 [crates/gwiki/src/commands/sources.rs:733-738]
  - Signature: `fn raw_source_path_trims_source_ids_before_building_path() {`
  - Purpose: Indexed function `raw_source_path_trims_source_ids_before_building_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:733-738]
- `manifest_remove_deletes_only_matching_source_record` (function) component `manifest_remove_deletes_only_matching_source_record [function]` (`0d0ab174-357e-54b8-9491-e34fe1ad5bb2`) lines 741-767 [crates/gwiki/src/commands/sources.rs:741-767]
  - Signature: `fn manifest_remove_deletes_only_matching_source_record() {`
  - Purpose: Indexed function `manifest_remove_deletes_only_matching_source_record` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:741-767]
- `removed_source_files_restore_after_later_failure` (function) component `removed_source_files_restore_after_later_failure [function]` (`acced69f-abbb-5ca6-9dba-c8ab0bfdb371`) lines 770-812 [crates/gwiki/src/commands/sources.rs:770-812]
  - Signature: `fn removed_source_files_restore_after_later_failure() {`
  - Purpose: Indexed function `removed_source_files_restore_after_later_failure` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:770-812]
- `rollback_removed_source_reports_manifest_race` (function) component `rollback_removed_source_reports_manifest_race [function]` (`0a8d327d-259c-51be-ade0-98eb40c069a4`) lines 815-828 [crates/gwiki/src/commands/sources.rs:815-828]
  - Signature: `fn rollback_removed_source_reports_manifest_race() {`
  - Purpose: Indexed function `rollback_removed_source_reports_manifest_race` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:815-828]
- `compiled_source_requests_audit_follow_up` (function) component `compiled_source_requests_audit_follow_up [function]` (`73352dc8-2d1d-51d6-91a9-872df62ea01c`) lines 831-839 [crates/gwiki/src/commands/sources.rs:831-839]
  - Signature: `fn compiled_source_requests_audit_follow_up() {`
  - Purpose: Indexed function `compiled_source_requests_audit_follow_up` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:831-839]
- `seed_manifest_source` (function) component `seed_manifest_source [function]` (`379f6256-1fc9-586d-9383-6ca5fb30b562`) lines 841-857 [crates/gwiki/src/commands/sources.rs:841-857]
  - Signature: `fn seed_manifest_source(root: &Path, compile_status: CompileStatus) -> SourceRecord {`
  - Purpose: Indexed function `seed_manifest_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:841-857]
- `write_raw_source` (function) component `write_raw_source [function]` (`0cb76e39-f33d-55a6-a351-c7f8121477cb`) lines 859-874 [crates/gwiki/src/commands/sources.rs:859-874]
  - Signature: `fn write_raw_source(root: &Path, id: &str, extra_frontmatter: &str) {`
  - Purpose: Indexed function `write_raw_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:859-874]

