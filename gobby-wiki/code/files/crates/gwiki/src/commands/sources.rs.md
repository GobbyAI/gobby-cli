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
  - 149-155
  - 157-163
  - 165-171
  - 175-181
  - 184-192
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/sources.rs:15-23](crates/gwiki/src/commands/sources.rs#L15-L23), [crates/gwiki/src/commands/sources.rs:25-122](crates/gwiki/src/commands/sources.rs#L25-L122), [crates/gwiki/src/commands/sources.rs:125-138](crates/gwiki/src/commands/sources.rs#L125-L138), [crates/gwiki/src/commands/sources.rs:141-146](crates/gwiki/src/commands/sources.rs#L141-L146), [crates/gwiki/src/commands/sources.rs:149-155](crates/gwiki/src/commands/sources.rs#L149-L155), [crates/gwiki/src/commands/sources.rs:157-163](crates/gwiki/src/commands/sources.rs#L157-L163), [crates/gwiki/src/commands/sources.rs:165-171](crates/gwiki/src/commands/sources.rs#L165-L171), [crates/gwiki/src/commands/sources.rs:175-181](crates/gwiki/src/commands/sources.rs#L175-L181), [crates/gwiki/src/commands/sources.rs:184-192](crates/gwiki/src/commands/sources.rs#L184-L192), [crates/gwiki/src/commands/sources.rs:195-205](crates/gwiki/src/commands/sources.rs#L195-L205), [crates/gwiki/src/commands/sources.rs:208-213](crates/gwiki/src/commands/sources.rs#L208-L213), [crates/gwiki/src/commands/sources.rs:216-219](crates/gwiki/src/commands/sources.rs#L216-L219), [crates/gwiki/src/commands/sources.rs:221-230](crates/gwiki/src/commands/sources.rs#L221-L230), [crates/gwiki/src/commands/sources.rs:232-260](crates/gwiki/src/commands/sources.rs#L232-L260), [crates/gwiki/src/commands/sources.rs:262-301](crates/gwiki/src/commands/sources.rs#L262-L301), [crates/gwiki/src/commands/sources.rs:303-316](crates/gwiki/src/commands/sources.rs#L303-L316), [crates/gwiki/src/commands/sources.rs:318-340](crates/gwiki/src/commands/sources.rs#L318-L340), [crates/gwiki/src/commands/sources.rs:342-363](crates/gwiki/src/commands/sources.rs#L342-L363), [crates/gwiki/src/commands/sources.rs:365-396](crates/gwiki/src/commands/sources.rs#L365-L396), [crates/gwiki/src/commands/sources.rs:398-441](crates/gwiki/src/commands/sources.rs#L398-L441), [crates/gwiki/src/commands/sources.rs:443-462](crates/gwiki/src/commands/sources.rs#L443-L462), [crates/gwiki/src/commands/sources.rs:464-486](crates/gwiki/src/commands/sources.rs#L464-L486), [crates/gwiki/src/commands/sources.rs:488-490](crates/gwiki/src/commands/sources.rs#L488-L490), [crates/gwiki/src/commands/sources.rs:492-525](crates/gwiki/src/commands/sources.rs#L492-L525), [crates/gwiki/src/commands/sources.rs:527-566](crates/gwiki/src/commands/sources.rs#L527-L566), [crates/gwiki/src/commands/sources.rs:568-573](crates/gwiki/src/commands/sources.rs#L568-L573), [crates/gwiki/src/commands/sources.rs:575-585](crates/gwiki/src/commands/sources.rs#L575-L585), [crates/gwiki/src/commands/sources.rs:587-593](crates/gwiki/src/commands/sources.rs#L587-L593), [crates/gwiki/src/commands/sources.rs:595-616](crates/gwiki/src/commands/sources.rs#L595-L616), [crates/gwiki/src/commands/sources.rs:618-657](crates/gwiki/src/commands/sources.rs#L618-L657), [crates/gwiki/src/commands/sources.rs:659-661](crates/gwiki/src/commands/sources.rs#L659-L661), [crates/gwiki/src/commands/sources.rs:669-695](crates/gwiki/src/commands/sources.rs#L669-L695), [crates/gwiki/src/commands/sources.rs:698-716](crates/gwiki/src/commands/sources.rs#L698-L716), [crates/gwiki/src/commands/sources.rs:719-730](crates/gwiki/src/commands/sources.rs#L719-L730), [crates/gwiki/src/commands/sources.rs:733-738](crates/gwiki/src/commands/sources.rs#L733-L738), [crates/gwiki/src/commands/sources.rs:741-767](crates/gwiki/src/commands/sources.rs#L741-L767), [crates/gwiki/src/commands/sources.rs:770-812](crates/gwiki/src/commands/sources.rs#L770-L812), [crates/gwiki/src/commands/sources.rs:815-828](crates/gwiki/src/commands/sources.rs#L815-L828), [crates/gwiki/src/commands/sources.rs:831-839](crates/gwiki/src/commands/sources.rs#L831-L839), [crates/gwiki/src/commands/sources.rs:841-857](crates/gwiki/src/commands/sources.rs#L841-L857), [crates/gwiki/src/commands/sources.rs:859-874](crates/gwiki/src/commands/sources.rs#L859-L874)

</details>

# crates/gwiki/src/commands/sources.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `sources` command workflow for a wiki scope: `execute` loads the scope’s source manifest, gathers each source entry, and renders a source listing, while `execute_remove` drives removal of a named source with optional dry-run and asset retention. The helper types track listing state, indexed counts, removal rendering, path changes, and staged removals, and the supporting functions resolve raw and asset paths, validate them against scope roots, stage file and manifest changes, and roll back or restore files if removal fails. The rendering functions then turn the collected source and removal state into command output, and the tests cover listing, path safety, manifest updates, degradation handling, restoration after failures, and rollback behavior.
[crates/gwiki/src/commands/sources.rs:15-23]
[crates/gwiki/src/commands/sources.rs:25-122]
[crates/gwiki/src/commands/sources.rs:125-138]
[crates/gwiki/src/commands/sources.rs:141-146]
[crates/gwiki/src/commands/sources.rs:149-155]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `167ef934-b63a-5eca-aec7-0c5f22e01d97` | 15-23 [crates/gwiki/src/commands/sources.rs:15-23] | Indexed function `execute` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:15-23] |
| `execute_remove` | function | `pub(crate) fn execute_remove(` | `execute_remove [function]` | `dbe5d905-40d7-530e-b9c6-3faae16c138c` | 25-122 [crates/gwiki/src/commands/sources.rs:25-122] | Indexed function `execute_remove` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:25-122] |
| `SourceListEntry` | class | `struct SourceListEntry {` | `SourceListEntry [class]` | `8918d9e3-b725-5e08-9d4b-c1333a590fa0` | 125-138 [crates/gwiki/src/commands/sources.rs:125-138] | Indexed class `SourceListEntry` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:125-138] |
| `IndexStatus` | class | `struct IndexStatus {` | `IndexStatus [class]` | `e773f602-c402-50a2-bd91-57b14bfa10f7` | 141-146 [crates/gwiki/src/commands/sources.rs:141-146] | Indexed class `IndexStatus` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:141-146] |
| `IndexStatus::not_run` | method | `fn not_run() -> Self {` | `IndexStatus::not_run [method]` | `de0e5e0f-5317-54d4-abcc-fb01f5f10e7a` | 149-155 [crates/gwiki/src/commands/sources.rs:149-155] | Indexed method `IndexStatus::not_run` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:149-155] |
| `IndexStatus::indexed` | method | `fn indexed(counts: IndexCounts) -> Self {` | `IndexStatus::indexed [method]` | `47b8b301-51d1-537a-bd5f-348f8b39d20f` | 157-163 [crates/gwiki/src/commands/sources.rs:157-163] | Indexed method `IndexStatus::indexed` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:157-163] |
| `IndexStatus::degraded` | method | `fn degraded() -> Self {` | `IndexStatus::degraded [method]` | `9905546e-9da0-55c4-9ec8-ed7c751d33d8` | 165-171 [crates/gwiki/src/commands/sources.rs:165-171] | Indexed method `IndexStatus::degraded` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:165-171] |
| `IndexedCounts` | class | `struct IndexedCounts {` | `IndexedCounts [class]` | `fe9bb971-5ef2-5469-9da9-999c18e4c0e1` | 175-181 [crates/gwiki/src/commands/sources.rs:175-181] | Indexed class `IndexedCounts` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:175-181] |
| `IndexedCounts::from` | method | `fn from(counts: IndexCounts) -> Self {` | `IndexedCounts::from [method]` | `c7befe9b-6b20-57d1-b231-1151a10dbd92` | 184-192 [crates/gwiki/src/commands/sources.rs:184-192] | Indexed method `IndexedCounts::from` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:184-192] |
| `RemoveSourceRender` | class | `struct RemoveSourceRender {` | `RemoveSourceRender [class]` | `140d9da0-befb-53a7-9080-3799cc8e022d` | 195-205 [crates/gwiki/src/commands/sources.rs:195-205] | Indexed class `RemoveSourceRender` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:195-205] |
| `PathChanges` | class | `struct PathChanges {` | `PathChanges [class]` | `d1ed86ea-c31f-51f4-bec7-6afa749273be` | 208-213 [crates/gwiki/src/commands/sources.rs:208-213] | Indexed class `PathChanges` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:208-213] |
| `StagedRemoval` | class | `struct StagedRemoval {` | `StagedRemoval [class]` | `83449710-11c0-52a3-b8c8-b10c1a33204b` | 216-219 [crates/gwiki/src/commands/sources.rs:216-219] | Indexed class `StagedRemoval` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:216-219] |
| `source_entries` | function | `fn source_entries(` | `source_entries [function]` | `25b16f6b-d64c-5cbe-95b4-e826d910be13` | 221-230 [crates/gwiki/src/commands/sources.rs:221-230] | Indexed function `source_entries` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:221-230] |
| `source_entry` | function | `fn source_entry(` | `source_entry [function]` | `0a5764ea-fd4a-5845-be2c-12402c7c056a` | 232-260 [crates/gwiki/src/commands/sources.rs:232-260] | Indexed function `source_entry` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:232-260] |
| `read_source_asset` | function | `fn read_source_asset(` | `read_source_asset [function]` | `2db59a9d-6f61-5685-828d-27626cb26cc3` | 262-301 [crates/gwiki/src/commands/sources.rs:262-301] | Indexed function `read_source_asset` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:262-301] |
| `stage_raw_source` | function | `fn stage_raw_source(` | `stage_raw_source [function]` | `6155ff77-813a-5eec-8b77-d0e4b5de4c13` | 303-316 [crates/gwiki/src/commands/sources.rs:303-316] | Indexed function `stage_raw_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:303-316] |
| `stage_source_asset` | function | `fn stage_source_asset(` | `stage_source_asset [function]` | `04a320e4-7c1f-538b-b5f1-cecdbc496e5c` | 318-340 [crates/gwiki/src/commands/sources.rs:318-340] | Indexed function `stage_source_asset` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:318-340] |
| `stage_source_removal` | function | `fn stage_source_removal(` | `stage_source_removal [function]` | `9c58c938-e5bf-52bb-89c3-12635742da40` | 342-363 [crates/gwiki/src/commands/sources.rs:342-363] | Indexed function `stage_source_removal` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:342-363] |
| `remove_staged_source_files` | function | `fn remove_staged_source_files(` | `remove_staged_source_files [function]` | `4206c29c-562d-5f1f-955b-2b128ca7a17c` | 365-396 [crates/gwiki/src/commands/sources.rs:365-396] | Indexed function `remove_staged_source_files` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:365-396] |
| `restore_removed_source_files` | function | `fn restore_removed_source_files(` | `restore_removed_source_files [function]` | `3aaf390e-414f-5ab9-b57e-f6d902aa136b` | 398-441 [crates/gwiki/src/commands/sources.rs:398-441] | Indexed function `restore_removed_source_files` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:398-441] |
| `rollback_removed_source_state` | function | `fn rollback_removed_source_state(` | `rollback_removed_source_state [function]` | `e0c548de-92c2-51df-b9e7-8afaecf308be` | 443-462 [crates/gwiki/src/commands/sources.rs:443-462] | Indexed function `rollback_removed_source_state` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:443-462] |
| `rollback_removed_source` | function | `fn rollback_removed_source(` | `rollback_removed_source [function]` | `a4856219-1bda-59b4-9ea5-3232c19f0316` | 464-486 [crates/gwiki/src/commands/sources.rs:464-486] | Indexed function `rollback_removed_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:464-486] |
| `raw_source_path` | function | `fn raw_source_path(id: &str) -> Result<PathBuf, WikiError> {` | `raw_source_path [function]` | `1d3a56df-c8f1-535d-82ad-63bcc3577694` | 488-490 [crates/gwiki/src/commands/sources.rs:488-490] | Indexed function `raw_source_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:488-490] |
| `source_asset_path` | function | `fn source_asset_path(vault_root: &Path, value: &str) -> Result<PathBuf, WikiError> {` | `source_asset_path [function]` | `a32c7141-942d-5e71-a0a3-5af5b52b1029` | 492-525 [crates/gwiki/src/commands/sources.rs:492-525] | Indexed function `source_asset_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:492-525] |
| `safe_vault_relative_path` | function | `fn safe_vault_relative_path(field: &'static str, value: &str) -> Result<PathBuf, WikiError> {` | `safe_vault_relative_path [function]` | `1a6f2012-20ca-5dda-8b31-d51fc0183004` | 527-566 [crates/gwiki/src/commands/sources.rs:527-566] | Indexed function `safe_vault_relative_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:527-566] |
| `is_raw_asset_path` | function | `fn is_raw_asset_path(path: &Path) -> bool {` | `is_raw_asset_path [function]` | `82ebddb6-0324-50c8-85ed-bf1deade3b97` | 568-573 [crates/gwiki/src/commands/sources.rs:568-573] | Indexed function `is_raw_asset_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:568-573] |
| `ensure_scope_root` | function | `fn ensure_scope_root(root: &Path) -> Result<(), WikiError> {` | `ensure_scope_root [function]` | `a42e2107-589b-5133-b665-b82c632db8fa` | 575-585 [crates/gwiki/src/commands/sources.rs:575-585] | Indexed function `ensure_scope_root` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:575-585] |
| `follow_up_for_removed_source` | function | `fn follow_up_for_removed_source(record: &SourceRecord) -> Vec<&'static str> {` | `follow_up_for_removed_source [function]` | `92c0eca5-908b-5c59-b059-8c9d792a8114` | 587-593 [crates/gwiki/src/commands/sources.rs:587-593] | Indexed function `follow_up_for_removed_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:587-593] |
| `render_sources` | function | `fn render_sources(` | `render_sources [function]` | `370097f7-06a9-54c4-9a4a-f058bcb72c5b` | 595-616 [crates/gwiki/src/commands/sources.rs:595-616] | Indexed function `render_sources` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:595-616] |
| `render_remove_source` | function | `fn render_remove_source(render: RemoveSourceRender) -> CommandOutcome {` | `render_remove_source [function]` | `ce352531-6184-5c31-9171-c6f2547d20db` | 618-657 [crates/gwiki/src/commands/sources.rs:618-657] | Indexed function `render_remove_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:618-657] |
| `display_path` | function | `fn display_path(path: &Path) -> String {` | `display_path [function]` | `5f8b3c2f-05cc-54c1-942f-7ec0b0943520` | 659-661 [crates/gwiki/src/commands/sources.rs:659-661] | Indexed function `display_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:659-661] |
| `source_listing_reads_manifest_raw_path_and_asset` | function | `fn source_listing_reads_manifest_raw_path_and_asset() {` | `source_listing_reads_manifest_raw_path_and_asset [function]` | `21312e15-3e43-5528-a961-c32706c92ecd` | 669-695 [crates/gwiki/src/commands/sources.rs:669-695] | Indexed function `source_listing_reads_manifest_raw_path_and_asset` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:669-695] |
| `missing_raw_file_degrades_without_failing_source_listing` | function | `fn missing_raw_file_degrades_without_failing_source_listing() {` | `missing_raw_file_degrades_without_failing_source_listing [function]` | `a07ac043-cdd3-5464-96b6-e19b5ad08c16` | 698-716 [crates/gwiki/src/commands/sources.rs:698-716] | Indexed function `missing_raw_file_degrades_without_failing_source_listing` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:698-716] |
| `source_asset_path_rejects_traversal_absolute_and_non_raw_assets` | function | `fn source_asset_path_rejects_traversal_absolute_and_non_raw_assets() {` | `source_asset_path_rejects_traversal_absolute_and_non_raw_assets [function]` | `4f5cf1d6-4f02-5eed-9284-99d4570e18cf` | 719-730 [crates/gwiki/src/commands/sources.rs:719-730] | Indexed function `source_asset_path_rejects_traversal_absolute_and_non_raw_assets` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:719-730] |
| `raw_source_path_trims_source_ids_before_building_path` | function | `fn raw_source_path_trims_source_ids_before_building_path() {` | `raw_source_path_trims_source_ids_before_building_path [function]` | `e25b38e0-3370-50c2-b52a-758e6c8c985e` | 733-738 [crates/gwiki/src/commands/sources.rs:733-738] | Indexed function `raw_source_path_trims_source_ids_before_building_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:733-738] |
| `manifest_remove_deletes_only_matching_source_record` | function | `fn manifest_remove_deletes_only_matching_source_record() {` | `manifest_remove_deletes_only_matching_source_record [function]` | `0d0ab174-357e-54b8-9491-e34fe1ad5bb2` | 741-767 [crates/gwiki/src/commands/sources.rs:741-767] | Indexed function `manifest_remove_deletes_only_matching_source_record` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:741-767] |
| `removed_source_files_restore_after_later_failure` | function | `fn removed_source_files_restore_after_later_failure() {` | `removed_source_files_restore_after_later_failure [function]` | `acced69f-abbb-5ca6-9dba-c8ab0bfdb371` | 770-812 [crates/gwiki/src/commands/sources.rs:770-812] | Indexed function `removed_source_files_restore_after_later_failure` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:770-812] |
| `rollback_removed_source_reports_manifest_race` | function | `fn rollback_removed_source_reports_manifest_race() {` | `rollback_removed_source_reports_manifest_race [function]` | `0a8d327d-259c-51be-ade0-98eb40c069a4` | 815-828 [crates/gwiki/src/commands/sources.rs:815-828] | Indexed function `rollback_removed_source_reports_manifest_race` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:815-828] |
| `compiled_source_requests_audit_follow_up` | function | `fn compiled_source_requests_audit_follow_up() {` | `compiled_source_requests_audit_follow_up [function]` | `73352dc8-2d1d-51d6-91a9-872df62ea01c` | 831-839 [crates/gwiki/src/commands/sources.rs:831-839] | Indexed function `compiled_source_requests_audit_follow_up` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:831-839] |
| `seed_manifest_source` | function | `fn seed_manifest_source(root: &Path, compile_status: CompileStatus) -> SourceRecord {` | `seed_manifest_source [function]` | `379f6256-1fc9-586d-9383-6ca5fb30b562` | 841-857 [crates/gwiki/src/commands/sources.rs:841-857] | Indexed function `seed_manifest_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:841-857] |
| `write_raw_source` | function | `fn write_raw_source(root: &Path, id: &str, extra_frontmatter: &str) {` | `write_raw_source [function]` | `0cb76e39-f33d-55a6-a351-c7f8121477cb` | 859-874 [crates/gwiki/src/commands/sources.rs:859-874] | Indexed function `write_raw_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:859-874] |
