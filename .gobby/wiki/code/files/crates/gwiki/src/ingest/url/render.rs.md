---
title: crates/gwiki/src/ingest/url/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/url/render.rs
  ranges:
  - 12-37
  - 39-66
  - 68-74
  - 76-88
  - 90-97
  - 99-105
  - 107-123
  - 125-135
  - 137-146
  - 148-182
  - 184-199
  - 201-207
  - 209-211
  - 213-233
  - 235-244
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/url/render.rs

Module: [[code/modules/crates/gwiki/src/ingest/url|crates/gwiki/src/ingest/url]]

## Purpose

Builds markdown for ingested URL snapshots. It has one path for HTML responses and another for non-HTML assets: both attach source metadata such as URLs, fetch time, hash, and content type, then emit a title header. The HTML path converts the document into “markdownish” visible text, while the non-HTML path records the asset location and notes that the response was preserved as a source asset. The helper functions classify snapshots by content type and body shape, derive a source kind and filename, extract titles, walk the HTML tree to collect visible inline/block text, skip hidden elements, and normalize whitespace so the rendered output is consistent.
[crates/gwiki/src/ingest/url/render.rs:12-37]
[crates/gwiki/src/ingest/url/render.rs:39-66]
[crates/gwiki/src/ingest/url/render.rs:68-74]
[crates/gwiki/src/ingest/url/render.rs:76-88]
[crates/gwiki/src/ingest/url/render.rs:90-97]

## API Symbols

- `render_url_markdown` (function) component `render_url_markdown [function]` (`21aefa28-d570-59c8-9cd7-9a6aea6ddc06`) lines 12-37 [crates/gwiki/src/ingest/url/render.rs:12-37]
  - Signature: `pub(super) fn render_url_markdown(`
  - Purpose: Indexed function `render_url_markdown` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:12-37]
- `render_non_html_url_markdown` (function) component `render_non_html_url_markdown [function]` (`1a8b4668-73f8-5f9a-8ddb-2989ddfdd97e`) lines 39-66 [crates/gwiki/src/ingest/url/render.rs:39-66]
  - Signature: `pub(super) fn render_non_html_url_markdown(`
  - Purpose: Indexed function `render_non_html_url_markdown` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:39-66]
- `snapshot_is_html` (function) component `snapshot_is_html [function]` (`80694710-9018-5f4c-a213-8e4b695502a0`) lines 68-74 [crates/gwiki/src/ingest/url/render.rs:68-74]
  - Signature: `pub(super) fn snapshot_is_html(snapshot: &UrlSnapshot) -> bool {`
  - Purpose: Indexed function `snapshot_is_html` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:68-74]
- `source_kind_for_url_response` (function) component `source_kind_for_url_response [function]` (`d5a13fd7-9757-5672-967e-1a175cdc83c9`) lines 76-88 [crates/gwiki/src/ingest/url/render.rs:76-88]
  - Signature: `pub(super) fn source_kind_for_url_response(content_type: Option<&str>) -> SourceKind {`
  - Purpose: Indexed function `source_kind_for_url_response` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:76-88]
- `content_type_media_type` (function) component `content_type_media_type [function]` (`b0ff2069-d800-598c-aaf0-e675340fa595`) lines 90-97 [crates/gwiki/src/ingest/url/render.rs:90-97]
  - Signature: `fn content_type_media_type(content_type: Option<&str>) -> Option<String> {`
  - Purpose: Indexed function `content_type_media_type` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:90-97]
- `body_looks_like_html` (function) component `body_looks_like_html [function]` (`7cca9fea-6099-5172-920a-305501b65dbf`) lines 99-105 [crates/gwiki/src/ingest/url/render.rs:99-105]
  - Signature: `fn body_looks_like_html(body: &[u8]) -> bool {`
  - Purpose: Indexed function `body_looks_like_html` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:99-105]
- `file_name_for_url_response` (function) component `file_name_for_url_response [function]` (`1fabf794-8ac6-5eb7-a26d-b420746682ea`) lines 107-123 [crates/gwiki/src/ingest/url/render.rs:107-123]
  - Signature: `pub(super) fn file_name_for_url_response(snapshot: &UrlSnapshot, kind: &SourceKind) -> String {`
  - Purpose: Indexed function `file_name_for_url_response` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:107-123]
- `extract_title` (function) component `extract_title [function]` (`b852b1ce-8398-5ee7-af3e-9baf14841659`) lines 125-135 [crates/gwiki/src/ingest/url/render.rs:125-135]
  - Signature: `pub(super) fn extract_title(document: &Html) -> Option<String> {`
  - Purpose: Indexed function `extract_title` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:125-135]
- `html_to_markdownish_text` (function) component `html_to_markdownish_text [function]` (`8c7a1d45-5b61-5a3c-b0ca-9a0e2c55f319`) lines 137-146 [crates/gwiki/src/ingest/url/render.rs:137-146]
  - Signature: `pub(super) fn html_to_markdownish_text(document: &Html) -> String {`
  - Purpose: Indexed function `html_to_markdownish_text` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:137-146]
- `collect_visible_text` (function) component `collect_visible_text [function]` (`ea4a3a39-f2ad-515b-b02d-72e369879180`) lines 148-182 [crates/gwiki/src/ingest/url/render.rs:148-182]
  - Signature: `fn collect_visible_text(element: ElementRef<'_>, parts: &mut Vec<String>) {`
  - Purpose: Indexed function `collect_visible_text` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:148-182]
- `collect_inline_text` (function) component `collect_inline_text [function]` (`cb2147a6-c18f-5e8e-871e-73ecd2ea802b`) lines 184-199 [crates/gwiki/src/ingest/url/render.rs:184-199]
  - Signature: `fn collect_inline_text(element: ElementRef<'_>, output: &mut String) {`
  - Purpose: Indexed function `collect_inline_text` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:184-199]
- `push_inline_part` (function) component `push_inline_part [function]` (`af995ab1-a4e4-5fb5-a6ef-0876089a588a`) lines 201-207 [crates/gwiki/src/ingest/url/render.rs:201-207]
  - Signature: `fn push_inline_part(inline: &mut String, parts: &mut Vec<String>) {`
  - Purpose: Indexed function `push_inline_part` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:201-207]
- `is_hidden_element` (function) component `is_hidden_element [function]` (`b9a03989-bd23-5f82-b710-d4dd34ff75a3`) lines 209-211 [crates/gwiki/src/ingest/url/render.rs:209-211]
  - Signature: `fn is_hidden_element(name: &str) -> bool {`
  - Purpose: Indexed function `is_hidden_element` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:209-211]
- `is_text_block` (function) component `is_text_block [function]` (`1c21bd86-ef5d-5c09-bf50-b7936810284a`) lines 213-233 [crates/gwiki/src/ingest/url/render.rs:213-233]
  - Signature: `fn is_text_block(name: &str) -> bool {`
  - Purpose: Indexed function `is_text_block` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:213-233]
- `normalize_markdown_text` (function) component `normalize_markdown_text [function]` (`e2022f11-057b-5922-9402-f00b897dd499`) lines 235-244 [crates/gwiki/src/ingest/url/render.rs:235-244]
  - Signature: `fn normalize_markdown_text(text: &str) -> String {`
  - Purpose: Indexed function `normalize_markdown_text` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:235-244]

