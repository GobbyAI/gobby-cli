---
title: crates/gwiki/src/ingest/wayback.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/wayback.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/wayback.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/wayback.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/wayback.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WaybackCaptureSnapshot` | class | Indexed class `WaybackCaptureSnapshot` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:18-25] |
| `ingest_capture` | function | Indexed function `ingest_capture` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:28-47] |
| `decode_wayback_html` | function | Indexed function `decode_wayback_html` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:50-60] |
| `ensure_html_content_type` | function | Indexed function `ensure_html_content_type` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:63-75] |
| `decode_html_bytes` | function | Indexed function `decode_html_bytes` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:78-98] |
| `content_type_media_type` | function | Indexed function `content_type_media_type` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:101-108] |
| `charset_from_content_type` | function | Indexed function `charset_from_content_type` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:111-118] |
| `charset_from_html_meta` | function | Indexed function `charset_from_html_meta` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:121-129] |
| `trim_charset_label` | function | Indexed function `trim_charset_label` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:132-139] |
| `html_looks_like_document` | function | Indexed function `html_looks_like_document` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:142-145] |
| `wayback_title` | function | Indexed function `wayback_title` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:148-153] |
| `html_title` | function | Indexed function `html_title` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:156-163] |
| `title_from_url_path` | function | Indexed function `title_from_url_path` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:166-171] |
| `url_host` | function | Indexed function `url_host` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:174-180] |
| `percent_decode_lossy` | function | Indexed function `percent_decode_lossy` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:183-185] |
| `render_wayback_markdown` | function | Indexed function `render_wayback_markdown` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:188-215] |
| `html_to_text` | function | Indexed function `html_to_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:218-226] |
| `extract_html_text` | function | Indexed function `extract_html_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:229-238] |
| `collect_visible_text` | function | Indexed function `collect_visible_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:241-266] |
| `collect_inline_text` | function | Indexed function `collect_inline_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:269-292] |
| `append_inline_text` | function | Indexed function `append_inline_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:295-304] |
| `push_text_part` | function | Indexed function `push_text_part` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:307-313] |
| `is_block_boundary` | function | Indexed function `is_block_boundary` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:316-352] |
| `wayback_records_capture_metadata` | function | Indexed function `wayback_records_capture_metadata` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:361-400] |
| `wayback_extracts_body_text_without_head_metadata` | function | Indexed function `wayback_extracts_body_text_without_head_metadata` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:403-413] |
| `wayback_groups_inline_text_per_block` | function | Indexed function `wayback_groups_inline_text_per_block` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:416-430] |
| `wayback_prefers_html_title_then_decoded_url_path_then_host` | function | Indexed function `wayback_prefers_html_title_then_decoded_url_path_then_host` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:433-465] |
| `wayback_does_not_decode_entities_twice` | function | Indexed function `wayback_does_not_decode_entities_twice` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:468-475] |
| `wayback_decodes_declared_charset` | function | Indexed function `wayback_decodes_declared_charset` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:478-491] |
| `wayback_rejects_non_html_content_type` | function | Indexed function `wayback_rejects_non_html_content_type` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:494-511] |
| `document_for` | function | Indexed function `document_for` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:513-516] |

