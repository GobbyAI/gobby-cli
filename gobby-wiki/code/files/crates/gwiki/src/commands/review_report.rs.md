---
title: crates/gwiki/src/commands/review_report.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/review_report.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/review_report.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/review_report.rs` exposes 36 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/review_report.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Indexed function `execute` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:28-105] |
| `ChangeSetInput` | class | Indexed class `ChangeSetInput` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:108-113] |
| `ChangeSetInput::from_options` | method | Indexed method `ChangeSetInput::from_options` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:116-135] |
| `ChangeSetInput::as_code_change_set` | method | Indexed method `ChangeSetInput::as_code_change_set` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:137-142] |
| `ReportParts` | class | Indexed class `ReportParts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:146-154] |
| `ReviewReport` | class | Indexed class `ReviewReport` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:157-167] |
| `ReviewAffectedPage` | class | Indexed class `ReviewAffectedPage` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:170-174] |
| `RiskyDependencyShift` | class | Indexed class `RiskyDependencyShift` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:177-183] |
| `build_report_from_parts` | function | Indexed function `build_report_from_parts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:185-211] |
| `render_markdown` | function | Indexed function `render_markdown` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:213-229] |
| `render_changes` | function | Indexed function `render_changes` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:231-241] |
| `render_affected_pages` | function | Indexed function `render_affected_pages` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:243-260] |
| `render_stale_docs` | function | Indexed function `render_stale_docs` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:262-266] |
| `render_neighborhoods` | function | Indexed function `render_neighborhoods` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:268-294] |
| `render_risky_shifts` | function | Indexed function `render_risky_shifts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:296-321] |
| `graph_neighborhoods` | function | Indexed function `graph_neighborhoods` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:323-362] |
| `analytics_graph_from_edges` | function | Indexed function `analytics_graph_from_edges` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:364-399] |
| `risky_dependency_shifts` | function | Indexed function `risky_dependency_shifts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:401-430] |
| `risk_from_score` | function | Indexed function `risk_from_score` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:432-456] |
| `changed_node_ids` | function | Indexed function `changed_node_ids` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:458-471] |
| `changed_node_ids_from_graph` | function | Indexed function `changed_node_ids_from_graph` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:473-484] |
| `changed_files_from_diff` | function | Indexed function `changed_files_from_diff` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:486-493] |
| `parse_unified_diff_files` | function | Indexed function `parse_unified_diff_files` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:495-530] |
| `trim_diff_path` | function | Indexed function `trim_diff_path` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:532-534] |
| `review_affected_page` | function | Indexed function `review_affected_page` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:536-546] |
| `render_string_list` | function | Indexed function `render_string_list` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:548-562] |
| `unique_non_empty` | function | Indexed function `unique_non_empty` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:564-572] |
| `unique_edges` | function | Indexed function `unique_edges` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:574-588] |
| `degradation_source` | function | Indexed function `degradation_source` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:590-603] |
| `is_graph_blocking_degraded_source` | function | Indexed function `is_graph_blocking_degraded_source` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:605-612] |
| `optional_falkor_config` | function | Indexed function `optional_falkor_config` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:614-626] |
| `review_report_renders_markdown_with_risks_and_metadata` | function | Indexed function `review_report_renders_markdown_with_risks_and_metadata` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:642-711] |
| `review_report_degrades_without_graph_analytics` | function | Indexed function `review_report_degrades_without_graph_analytics` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:714-736] |
| `review_report_maps_semantic_partial_data_degradation` | function | Indexed function `review_report_maps_semantic_partial_data_degradation` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:739-746] |
| `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` | function | Indexed function `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:749-760] |
| `parse_unified_diff_files_sanitizes_unsafe_paths` | function | Indexed function `parse_unified_diff_files_sanitizes_unsafe_paths` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:763-776] |

