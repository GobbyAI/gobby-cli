---
title: crates/gwiki/src/collect.rs
type: code_file
provenance:
- file: crates/gwiki/src/collect.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/collect.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/collect.rs` exposes 43 indexed API symbols.

## How it fits

`crates/gwiki/src/collect.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CollectReport` | class | Indexed class `CollectReport` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:18-21] |
| `CollectAction` | class | Indexed class `CollectAction` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:24-30] |
| `CollectStatus` | type | Indexed type `CollectStatus` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:34-37] |
| `InboxKind` | type | Indexed type `InboxKind` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:39-42] |
| `collect_inbox` | function | Indexed function `collect_inbox` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:44-46] |
| `collect_inbox_with_limit` | function | Indexed function `collect_inbox_with_limit` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:48-140] |
| `collect_inbox_and_index` | function | Indexed function `collect_inbox_and_index` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:142-152] |
| `read_inbox_item_limited` | function | Indexed function `read_inbox_item_limited` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:154-165] |
| `ensure_collect_paths` | function | Indexed function `ensure_collect_paths` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:167-179] |
| `classify_inbox_item` | function | Indexed function `classify_inbox_item` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:181-204] |
| `accept_item` | function | Indexed function `accept_item` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:206-327] |
| `rollback_registered_collect_source` | function | Indexed function `rollback_registered_collect_source` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:329-352] |
| `cleanup_collect_file` | function | Indexed function `cleanup_collect_file` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:354-361] |
| `collect_error_with_cleanup` | function | Indexed function `collect_error_with_cleanup` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:363-390] |
| `collect_cleanup_detail` | function | Indexed function `collect_cleanup_detail` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:392-398] |
| `skip_item` | function | Indexed function `skip_item` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:400-418] |
| `render_url_markdown` | function | Indexed function `render_url_markdown` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:420-433] |
| `render_file_markdown` | function | Indexed function `render_file_markdown` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:435-480] |
| `write_status_sidecar` | function | Indexed function `write_status_sidecar` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:482-501] |
| `append_log` | function | Indexed function `append_log` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:503-550] |
| `extract_url` | function | Indexed function `extract_url` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:552-572] |
| `urls_from_embedded_text` | function | Indexed function `urls_from_embedded_text` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:574-588] |
| `is_http_url` | function | Indexed function `is_http_url` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:590-592] |
| `parse_embedded_http_url` | function | Indexed function `parse_embedded_http_url` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:594-604] |
| `trim_trailing_url_punctuation` | function | Indexed function `trim_trailing_url_punctuation` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:606-610] |
| `parse_http_url` | function | Indexed function `parse_http_url` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:612-615] |
| `should_store_asset` | function | Indexed function `should_store_asset` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:617-622] |
| `is_status_sidecar` | function | Indexed function `is_status_sidecar` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:624-628] |
| `status_sidecar_path` | function | Indexed function `status_sidecar_path` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:630-636] |
| `relative_to_vault` | function | Indexed function `relative_to_vault` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:638-642] |
| `path_to_string` | function | Indexed function `path_to_string` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:644-646] |
| `io_error` | function | Indexed function `io_error` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:648-654] |
| `write_file` | function | Indexed function `write_file` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:665-671] |
| `collect_routes_known_items` | function | Indexed function `collect_routes_known_items` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:674-736] |
| `collect_indexes_accepted_sources` | function | Indexed function `collect_indexes_accepted_sources` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:739-768] |
| `embedded_url_parser_returns_all_urls_in_order` | function | Indexed function `embedded_url_parser_returns_all_urls_in_order` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:771-781] |
| `embedded_url_parser_preserves_valid_punctuation_before_trimming` | function | Indexed function `embedded_url_parser_preserves_valid_punctuation_before_trimming` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:784-789] |
| `embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds` | function | Indexed function `embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:792-797] |
| `ambiguous_items_remain_in_inbox` | function | Indexed function `ambiguous_items_remain_in_inbox` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:800-815] |
| `collect_logs_actions` | function | Indexed function `collect_logs_actions` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:818-830] |
| `oversized_items_are_skipped_before_reading` | function | Indexed function `oversized_items_are_skipped_before_reading` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:833-847] |
| `collect_cleanup_context_preserves_config_error_variant` | function | Indexed function `collect_cleanup_context_preserves_config_error_variant` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:850-866] |
| `collect_cleanup_context_preserves_io_error_variant` | function | Indexed function `collect_cleanup_context_preserves_io_error_variant` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:869-892] |

