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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/url/render.rs:12-37](crates/gwiki/src/ingest/url/render.rs#L12-L37), [crates/gwiki/src/ingest/url/render.rs:39-66](crates/gwiki/src/ingest/url/render.rs#L39-L66), [crates/gwiki/src/ingest/url/render.rs:68-74](crates/gwiki/src/ingest/url/render.rs#L68-L74), [crates/gwiki/src/ingest/url/render.rs:76-88](crates/gwiki/src/ingest/url/render.rs#L76-L88), [crates/gwiki/src/ingest/url/render.rs:90-97](crates/gwiki/src/ingest/url/render.rs#L90-L97), [crates/gwiki/src/ingest/url/render.rs:99-105](crates/gwiki/src/ingest/url/render.rs#L99-L105), [crates/gwiki/src/ingest/url/render.rs:107-123](crates/gwiki/src/ingest/url/render.rs#L107-L123), [crates/gwiki/src/ingest/url/render.rs:125-135](crates/gwiki/src/ingest/url/render.rs#L125-L135), [crates/gwiki/src/ingest/url/render.rs:137-146](crates/gwiki/src/ingest/url/render.rs#L137-L146), [crates/gwiki/src/ingest/url/render.rs:148-182](crates/gwiki/src/ingest/url/render.rs#L148-L182), [crates/gwiki/src/ingest/url/render.rs:184-199](crates/gwiki/src/ingest/url/render.rs#L184-L199), [crates/gwiki/src/ingest/url/render.rs:201-207](crates/gwiki/src/ingest/url/render.rs#L201-L207), [crates/gwiki/src/ingest/url/render.rs:209-211](crates/gwiki/src/ingest/url/render.rs#L209-L211), [crates/gwiki/src/ingest/url/render.rs:213-233](crates/gwiki/src/ingest/url/render.rs#L213-L233), [crates/gwiki/src/ingest/url/render.rs:235-244](crates/gwiki/src/ingest/url/render.rs#L235-L244)

</details>

# crates/gwiki/src/ingest/url/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file turns a fetched URL snapshot into markdown, with separate paths for HTML and non-HTML responses. `render_url_markdown` builds metadata, writes a title heading, and converts the HTML document into plain markdown-like text, while `render_non_html_url_markdown` records the response as a preserved asset and emits a short note instead of body content.

The helper functions support that split by classifying snapshots from content type and body heuristics, deriving a filename and title, and extracting visible text from HTML. `html_to_markdownish_text`, `collect_visible_text`, `collect_inline_text`, `push_inline_part`, `is_hidden_element`, `is_text_block`, and `normalize_markdown_text` work together to walk the DOM, skip hidden elements, preserve block structure, and clean up the extracted text.
[crates/gwiki/src/ingest/url/render.rs:12-37]
[crates/gwiki/src/ingest/url/render.rs:39-66]
[crates/gwiki/src/ingest/url/render.rs:68-74]
[crates/gwiki/src/ingest/url/render.rs:76-88]
[crates/gwiki/src/ingest/url/render.rs:90-97]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_url_markdown` | function | `pub(super) fn render_url_markdown(` | `render_url_markdown [function]` | `21aefa28-d570-59c8-9cd7-9a6aea6ddc06` | 12-37 [crates/gwiki/src/ingest/url/render.rs:12-37] | Indexed function `render_url_markdown` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:12-37] |
| `render_non_html_url_markdown` | function | `pub(super) fn render_non_html_url_markdown(` | `render_non_html_url_markdown [function]` | `1a8b4668-73f8-5f9a-8ddb-2989ddfdd97e` | 39-66 [crates/gwiki/src/ingest/url/render.rs:39-66] | Indexed function `render_non_html_url_markdown` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:39-66] |
| `snapshot_is_html` | function | `pub(super) fn snapshot_is_html(snapshot: &UrlSnapshot) -> bool {` | `snapshot_is_html [function]` | `80694710-9018-5f4c-a213-8e4b695502a0` | 68-74 [crates/gwiki/src/ingest/url/render.rs:68-74] | Indexed function `snapshot_is_html` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:68-74] |
| `source_kind_for_url_response` | function | `pub(super) fn source_kind_for_url_response(content_type: Option<&str>) -> SourceKind {` | `source_kind_for_url_response [function]` | `d5a13fd7-9757-5672-967e-1a175cdc83c9` | 76-88 [crates/gwiki/src/ingest/url/render.rs:76-88] | Indexed function `source_kind_for_url_response` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:76-88] |
| `content_type_media_type` | function | `fn content_type_media_type(content_type: Option<&str>) -> Option<String> {` | `content_type_media_type [function]` | `b0ff2069-d800-598c-aaf0-e675340fa595` | 90-97 [crates/gwiki/src/ingest/url/render.rs:90-97] | Indexed function `content_type_media_type` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:90-97] |
| `body_looks_like_html` | function | `fn body_looks_like_html(body: &[u8]) -> bool {` | `body_looks_like_html [function]` | `7cca9fea-6099-5172-920a-305501b65dbf` | 99-105 [crates/gwiki/src/ingest/url/render.rs:99-105] | Indexed function `body_looks_like_html` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:99-105] |
| `file_name_for_url_response` | function | `pub(super) fn file_name_for_url_response(snapshot: &UrlSnapshot, kind: &SourceKind) -> String {` | `file_name_for_url_response [function]` | `1fabf794-8ac6-5eb7-a26d-b420746682ea` | 107-123 [crates/gwiki/src/ingest/url/render.rs:107-123] | Indexed function `file_name_for_url_response` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:107-123] |
| `extract_title` | function | `pub(super) fn extract_title(document: &Html) -> Option<String> {` | `extract_title [function]` | `b852b1ce-8398-5ee7-af3e-9baf14841659` | 125-135 [crates/gwiki/src/ingest/url/render.rs:125-135] | Indexed function `extract_title` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:125-135] |
| `html_to_markdownish_text` | function | `pub(super) fn html_to_markdownish_text(document: &Html) -> String {` | `html_to_markdownish_text [function]` | `8c7a1d45-5b61-5a3c-b0ca-9a0e2c55f319` | 137-146 [crates/gwiki/src/ingest/url/render.rs:137-146] | Indexed function `html_to_markdownish_text` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:137-146] |
| `collect_visible_text` | function | `fn collect_visible_text(element: ElementRef<'_>, parts: &mut Vec<String>) {` | `collect_visible_text [function]` | `ea4a3a39-f2ad-515b-b02d-72e369879180` | 148-182 [crates/gwiki/src/ingest/url/render.rs:148-182] | Indexed function `collect_visible_text` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:148-182] |
| `collect_inline_text` | function | `fn collect_inline_text(element: ElementRef<'_>, output: &mut String) {` | `collect_inline_text [function]` | `cb2147a6-c18f-5e8e-871e-73ecd2ea802b` | 184-199 [crates/gwiki/src/ingest/url/render.rs:184-199] | Indexed function `collect_inline_text` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:184-199] |
| `push_inline_part` | function | `fn push_inline_part(inline: &mut String, parts: &mut Vec<String>) {` | `push_inline_part [function]` | `af995ab1-a4e4-5fb5-a6ef-0876089a588a` | 201-207 [crates/gwiki/src/ingest/url/render.rs:201-207] | Indexed function `push_inline_part` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:201-207] |
| `is_hidden_element` | function | `fn is_hidden_element(name: &str) -> bool {` | `is_hidden_element [function]` | `b9a03989-bd23-5f82-b710-d4dd34ff75a3` | 209-211 [crates/gwiki/src/ingest/url/render.rs:209-211] | Indexed function `is_hidden_element` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:209-211] |
| `is_text_block` | function | `fn is_text_block(name: &str) -> bool {` | `is_text_block [function]` | `1c21bd86-ef5d-5c09-bf50-b7936810284a` | 213-233 [crates/gwiki/src/ingest/url/render.rs:213-233] | Indexed function `is_text_block` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:213-233] |
| `normalize_markdown_text` | function | `fn normalize_markdown_text(text: &str) -> String {` | `normalize_markdown_text [function]` | `e2022f11-057b-5922-9402-f00b897dd499` | 235-244 [crates/gwiki/src/ingest/url/render.rs:235-244] | Indexed function `normalize_markdown_text` in `crates/gwiki/src/ingest/url/render.rs`. [crates/gwiki/src/ingest/url/render.rs:235-244] |
