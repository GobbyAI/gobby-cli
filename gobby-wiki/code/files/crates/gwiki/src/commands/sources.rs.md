---
title: crates/gwiki/src/commands/sources.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/sources.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/sources.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/sources.rs` exposes 41 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/sources.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Indexed function `execute` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:15-23] |
| `execute_remove` | function | Indexed function `execute_remove` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:25-122] |
| `SourceListEntry` | class | Indexed class `SourceListEntry` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:125-138] |
| `IndexStatus` | class | Indexed class `IndexStatus` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:141-146] |
| `IndexStatus::not_run` | method | Indexed method `IndexStatus::not_run` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:149-155] |
| `IndexStatus::indexed` | method | Indexed method `IndexStatus::indexed` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:157-163] |
| `IndexStatus::degraded` | method | Indexed method `IndexStatus::degraded` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:165-171] |
| `IndexedCounts` | class | Indexed class `IndexedCounts` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:175-181] |
| `IndexedCounts::from` | method | Indexed method `IndexedCounts::from` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:184-192] |
| `RemoveSourceRender` | class | Indexed class `RemoveSourceRender` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:195-205] |
| `PathChanges` | class | Indexed class `PathChanges` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:208-213] |
| `StagedRemoval` | class | Indexed class `StagedRemoval` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:216-219] |
| `source_entries` | function | Indexed function `source_entries` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:221-230] |
| `source_entry` | function | Indexed function `source_entry` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:232-260] |
| `read_source_asset` | function | Indexed function `read_source_asset` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:262-301] |
| `stage_raw_source` | function | Indexed function `stage_raw_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:303-316] |
| `stage_source_asset` | function | Indexed function `stage_source_asset` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:318-340] |
| `stage_source_removal` | function | Indexed function `stage_source_removal` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:342-363] |
| `remove_staged_source_files` | function | Indexed function `remove_staged_source_files` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:365-396] |
| `restore_removed_source_files` | function | Indexed function `restore_removed_source_files` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:398-441] |
| `rollback_removed_source_state` | function | Indexed function `rollback_removed_source_state` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:443-462] |
| `rollback_removed_source` | function | Indexed function `rollback_removed_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:464-486] |
| `raw_source_path` | function | Indexed function `raw_source_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:488-490] |
| `source_asset_path` | function | Indexed function `source_asset_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:492-525] |
| `safe_vault_relative_path` | function | Indexed function `safe_vault_relative_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:527-566] |
| `is_raw_asset_path` | function | Indexed function `is_raw_asset_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:568-573] |
| `ensure_scope_root` | function | Indexed function `ensure_scope_root` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:575-585] |
| `follow_up_for_removed_source` | function | Indexed function `follow_up_for_removed_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:587-593] |
| `render_sources` | function | Indexed function `render_sources` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:595-616] |
| `render_remove_source` | function | Indexed function `render_remove_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:618-657] |
| `display_path` | function | Indexed function `display_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:659-661] |
| `source_listing_reads_manifest_raw_path_and_asset` | function | Indexed function `source_listing_reads_manifest_raw_path_and_asset` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:669-695] |
| `missing_raw_file_degrades_without_failing_source_listing` | function | Indexed function `missing_raw_file_degrades_without_failing_source_listing` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:698-716] |
| `source_asset_path_rejects_traversal_absolute_and_non_raw_assets` | function | Indexed function `source_asset_path_rejects_traversal_absolute_and_non_raw_assets` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:719-730] |
| `raw_source_path_trims_source_ids_before_building_path` | function | Indexed function `raw_source_path_trims_source_ids_before_building_path` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:733-738] |
| `manifest_remove_deletes_only_matching_source_record` | function | Indexed function `manifest_remove_deletes_only_matching_source_record` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:741-767] |
| `removed_source_files_restore_after_later_failure` | function | Indexed function `removed_source_files_restore_after_later_failure` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:770-812] |
| `rollback_removed_source_reports_manifest_race` | function | Indexed function `rollback_removed_source_reports_manifest_race` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:815-828] |
| `compiled_source_requests_audit_follow_up` | function | Indexed function `compiled_source_requests_audit_follow_up` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:831-839] |
| `seed_manifest_source` | function | Indexed function `seed_manifest_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:841-857] |
| `write_raw_source` | function | Indexed function `write_raw_source` in `crates/gwiki/src/commands/sources.rs`. [crates/gwiki/src/commands/sources.rs:859-874] |

