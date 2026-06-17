---
title: crates/gwiki/src/ingest/wayback.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/wayback.rs
  ranges:
  - 18-25
  - 28-47
  - 50-60
  - 63-75
  - 78-98
  - 101-108
  - 111-118
  - 121-129
  - 132-139
  - 142-145
  - 148-153
  - 156-163
  - 166-171
  - 174-180
  - 183-185
  - 188-215
  - 218-226
  - 229-238
  - 241-266
  - 269-292
  - 295-304
  - 307-313
  - 316-352
  - 361-400
  - 403-413
  - 416-430
  - 433-465
  - 468-475
  - 478-491
  - 494-511
  - 513-516
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/wayback.rs:18-25](crates/gwiki/src/ingest/wayback.rs#L18-L25), [crates/gwiki/src/ingest/wayback.rs:28-47](crates/gwiki/src/ingest/wayback.rs#L28-L47), [crates/gwiki/src/ingest/wayback.rs:50-60](crates/gwiki/src/ingest/wayback.rs#L50-L60), [crates/gwiki/src/ingest/wayback.rs:63-75](crates/gwiki/src/ingest/wayback.rs#L63-L75), [crates/gwiki/src/ingest/wayback.rs:78-98](crates/gwiki/src/ingest/wayback.rs#L78-L98), [crates/gwiki/src/ingest/wayback.rs:101-108](crates/gwiki/src/ingest/wayback.rs#L101-L108), [crates/gwiki/src/ingest/wayback.rs:111-118](crates/gwiki/src/ingest/wayback.rs#L111-L118), [crates/gwiki/src/ingest/wayback.rs:121-129](crates/gwiki/src/ingest/wayback.rs#L121-L129), [crates/gwiki/src/ingest/wayback.rs:132-139](crates/gwiki/src/ingest/wayback.rs#L132-L139), [crates/gwiki/src/ingest/wayback.rs:142-145](crates/gwiki/src/ingest/wayback.rs#L142-L145), [crates/gwiki/src/ingest/wayback.rs:148-153](crates/gwiki/src/ingest/wayback.rs#L148-L153), [crates/gwiki/src/ingest/wayback.rs:156-163](crates/gwiki/src/ingest/wayback.rs#L156-L163), [crates/gwiki/src/ingest/wayback.rs:166-171](crates/gwiki/src/ingest/wayback.rs#L166-L171), [crates/gwiki/src/ingest/wayback.rs:174-180](crates/gwiki/src/ingest/wayback.rs#L174-L180), [crates/gwiki/src/ingest/wayback.rs:183-185](crates/gwiki/src/ingest/wayback.rs#L183-L185), [crates/gwiki/src/ingest/wayback.rs:188-215](crates/gwiki/src/ingest/wayback.rs#L188-L215), [crates/gwiki/src/ingest/wayback.rs:218-226](crates/gwiki/src/ingest/wayback.rs#L218-L226), [crates/gwiki/src/ingest/wayback.rs:229-238](crates/gwiki/src/ingest/wayback.rs#L229-L238), [crates/gwiki/src/ingest/wayback.rs:241-266](crates/gwiki/src/ingest/wayback.rs#L241-L266), [crates/gwiki/src/ingest/wayback.rs:269-292](crates/gwiki/src/ingest/wayback.rs#L269-L292), [crates/gwiki/src/ingest/wayback.rs:295-304](crates/gwiki/src/ingest/wayback.rs#L295-L304), [crates/gwiki/src/ingest/wayback.rs:307-313](crates/gwiki/src/ingest/wayback.rs#L307-L313), [crates/gwiki/src/ingest/wayback.rs:316-352](crates/gwiki/src/ingest/wayback.rs#L316-L352), [crates/gwiki/src/ingest/wayback.rs:361-400](crates/gwiki/src/ingest/wayback.rs#L361-L400), [crates/gwiki/src/ingest/wayback.rs:403-413](crates/gwiki/src/ingest/wayback.rs#L403-L413), [crates/gwiki/src/ingest/wayback.rs:416-430](crates/gwiki/src/ingest/wayback.rs#L416-L430), [crates/gwiki/src/ingest/wayback.rs:433-465](crates/gwiki/src/ingest/wayback.rs#L433-L465), [crates/gwiki/src/ingest/wayback.rs:468-475](crates/gwiki/src/ingest/wayback.rs#L468-L475), [crates/gwiki/src/ingest/wayback.rs:478-491](crates/gwiki/src/ingest/wayback.rs#L478-L491), [crates/gwiki/src/ingest/wayback.rs:494-511](crates/gwiki/src/ingest/wayback.rs#L494-L511), [crates/gwiki/src/ingest/wayback.rs:513-516](crates/gwiki/src/ingest/wayback.rs#L513-L516)

</details>

# crates/gwiki/src/ingest/wayback.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file ingests archived Wayback captures into gwiki by validating the snapshot as HTML, decoding the body with the declared charset when present, extracting a title and visible text, and writing the result into the wiki index store. `WaybackCaptureSnapshot` carries the capture metadata and bytes; `ingest_capture` drives the pipeline from snapshot to stored draft and rendered markdown, while the helper functions handle content-type and charset parsing, HTML detection, title fallback logic, text extraction and block grouping, and the tests verify metadata capture, body text extraction, title preference, charset decoding, entity handling, and rejection of non-HTML input.
[crates/gwiki/src/ingest/wayback.rs:18-25]
[crates/gwiki/src/ingest/wayback.rs:28-47]
[crates/gwiki/src/ingest/wayback.rs:50-60]
[crates/gwiki/src/ingest/wayback.rs:63-75]
[crates/gwiki/src/ingest/wayback.rs:78-98]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WaybackCaptureSnapshot` | class | `pub struct WaybackCaptureSnapshot {` | `WaybackCaptureSnapshot [class]` | `ceb67b01-2212-5c09-80d9-6cc5686bb87b` | 18-25 [crates/gwiki/src/ingest/wayback.rs:18-25] | Indexed class `WaybackCaptureSnapshot` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:18-25] |
| `ingest_capture` | function | `pub fn ingest_capture(` | `ingest_capture [function]` | `64b0c162-7265-5858-b461-95e60f8dd46d` | 28-47 [crates/gwiki/src/ingest/wayback.rs:28-47] | Indexed function `ingest_capture` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:28-47] |
| `decode_wayback_html` | function | `fn decode_wayback_html(snapshot: &WaybackCaptureSnapshot) -> Result<String, WikiError> {` | `decode_wayback_html [function]` | `74aa7287-4f63-5b76-b031-5476596e6de6` | 50-60 [crates/gwiki/src/ingest/wayback.rs:50-60] | Indexed function `decode_wayback_html` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:50-60] |
| `ensure_html_content_type` | function | `fn ensure_html_content_type(content_type: Option<&str>) -> Result<(), WikiError> {` | `ensure_html_content_type [function]` | `63d89456-50e7-5784-954e-868577d872ba` | 63-75 [crates/gwiki/src/ingest/wayback.rs:63-75] | Indexed function `ensure_html_content_type` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:63-75] |
| `decode_html_bytes` | function | `fn decode_html_bytes(bytes: &[u8], content_type: Option<&str>) -> String {` | `decode_html_bytes [function]` | `2fbf37d2-86ce-5b78-9ef9-123d039786df` | 78-98 [crates/gwiki/src/ingest/wayback.rs:78-98] | Indexed function `decode_html_bytes` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:78-98] |
| `content_type_media_type` | function | `fn content_type_media_type(content_type: Option<&str>) -> Option<String> {` | `content_type_media_type [function]` | `bbe86f9f-d0dd-5b58-a712-225a48c1e80e` | 101-108 [crates/gwiki/src/ingest/wayback.rs:101-108] | Indexed function `content_type_media_type` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:101-108] |
| `charset_from_content_type` | function | `fn charset_from_content_type(content_type: Option<&str>) -> Option<String> {` | `charset_from_content_type [function]` | `429d497d-d280-5e0e-a700-be67336aeb74` | 111-118 [crates/gwiki/src/ingest/wayback.rs:111-118] | Indexed function `charset_from_content_type` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:111-118] |
| `charset_from_html_meta` | function | `fn charset_from_html_meta(bytes: &[u8]) -> Option<String> {` | `charset_from_html_meta [function]` | `1cc71d43-27e3-51f4-88b0-1945b184c7c4` | 121-129 [crates/gwiki/src/ingest/wayback.rs:121-129] | Indexed function `charset_from_html_meta` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:121-129] |
| `trim_charset_label` | function | `fn trim_charset_label(value: &str) -> String {` | `trim_charset_label [function]` | `7a3a3a8d-7036-5b0b-9dec-628897fb0215` | 132-139 [crates/gwiki/src/ingest/wayback.rs:132-139] | Indexed function `trim_charset_label` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:132-139] |
| `html_looks_like_document` | function | `fn html_looks_like_document(html: &str) -> bool {` | `html_looks_like_document [function]` | `b9157707-ea6a-5d17-aad3-840932a7783f` | 142-145 [crates/gwiki/src/ingest/wayback.rs:142-145] | Indexed function `html_looks_like_document` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:142-145] |
| `wayback_title` | function | `fn wayback_title(snapshot: &WaybackCaptureSnapshot, document: &Html) -> String {` | `wayback_title [function]` | `a46c9b3c-1cc8-512c-9bdd-439dc4eeed15` | 148-153 [crates/gwiki/src/ingest/wayback.rs:148-153] | Indexed function `wayback_title` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:148-153] |
| `html_title` | function | `fn html_title(document: &Html) -> Option<String> {` | `html_title [function]` | `983cc05c-c50f-5d44-b58c-157e91ef49a8` | 156-163 [crates/gwiki/src/ingest/wayback.rs:156-163] | Indexed function `html_title` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:156-163] |
| `title_from_url_path` | function | `fn title_from_url_path(url: &str) -> Option<String> {` | `title_from_url_path [function]` | `74d345fa-9c9b-5add-a8a6-d07bfe193f5f` | 166-171 [crates/gwiki/src/ingest/wayback.rs:166-171] | Indexed function `title_from_url_path` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:166-171] |
| `url_host` | function | `fn url_host(url: &str) -> Option<String> {` | `url_host [function]` | `5cfab864-7609-5f52-b29e-0d2eb99aacd5` | 174-180 [crates/gwiki/src/ingest/wayback.rs:174-180] | Indexed function `url_host` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:174-180] |
| `percent_decode_lossy` | function | `fn percent_decode_lossy(value: &str) -> String {` | `percent_decode_lossy [function]` | `e6fc6764-8a2c-5687-92d1-6f6806110fca` | 183-185 [crates/gwiki/src/ingest/wayback.rs:183-185] | Indexed function `percent_decode_lossy` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:183-185] |
| `render_wayback_markdown` | function | `fn render_wayback_markdown(` | `render_wayback_markdown [function]` | `3be24ac8-55f8-5e35-8d9c-e6e0494de09f` | 188-215 [crates/gwiki/src/ingest/wayback.rs:188-215] | Indexed function `render_wayback_markdown` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:188-215] |
| `html_to_text` | function | `fn html_to_text(document: &Html) -> String {` | `html_to_text [function]` | `8e64392c-e5fd-5aa3-b61d-9a93c43fd092` | 218-226 [crates/gwiki/src/ingest/wayback.rs:218-226] | Indexed function `html_to_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:218-226] |
| `extract_html_text` | function | `fn extract_html_text(document: &Html) -> String {` | `extract_html_text [function]` | `ffdc2350-229a-58aa-b35b-a4baae81c8ec` | 229-238 [crates/gwiki/src/ingest/wayback.rs:229-238] | Indexed function `extract_html_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:229-238] |
| `collect_visible_text` | function | `fn collect_visible_text(element: ElementRef<'_>, parts: &mut Vec<String>) {` | `collect_visible_text [function]` | `84e1fe88-0ea4-5e19-a54d-55c7935ed31d` | 241-266 [crates/gwiki/src/ingest/wayback.rs:241-266] | Indexed function `collect_visible_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:241-266] |
| `collect_inline_text` | function | `fn collect_inline_text(element: ElementRef<'_>, parts: &mut Vec<String>, inline: &mut String) {` | `collect_inline_text [function]` | `3dda53fa-58b8-53e7-b90b-c5ce8ff79b57` | 269-292 [crates/gwiki/src/ingest/wayback.rs:269-292] | Indexed function `collect_inline_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:269-292] |
| `append_inline_text` | function | `fn append_inline_text(inline: &mut String, text: &str) {` | `append_inline_text [function]` | `87d78bce-d102-50f3-b1e9-e47b376f80c0` | 295-304 [crates/gwiki/src/ingest/wayback.rs:295-304] | Indexed function `append_inline_text` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:295-304] |
| `push_text_part` | function | `fn push_text_part(parts: &mut Vec<String>, inline: &mut String) {` | `push_text_part [function]` | `79d78a00-1ad0-5c4a-91c7-668c833e1d58` | 307-313 [crates/gwiki/src/ingest/wayback.rs:307-313] | Indexed function `push_text_part` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:307-313] |
| `is_block_boundary` | function | `fn is_block_boundary(name: &str) -> bool {` | `is_block_boundary [function]` | `fdf6e74d-b4f3-5bbb-9924-e0cb0facb3ed` | 316-352 [crates/gwiki/src/ingest/wayback.rs:316-352] | Indexed function `is_block_boundary` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:316-352] |
| `wayback_records_capture_metadata` | function | `fn wayback_records_capture_metadata() {` | `wayback_records_capture_metadata [function]` | `1b535367-6c76-569d-a85f-f7e9362ecae4` | 361-400 [crates/gwiki/src/ingest/wayback.rs:361-400] | Indexed function `wayback_records_capture_metadata` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:361-400] |
| `wayback_extracts_body_text_without_head_metadata` | function | `fn wayback_extracts_body_text_without_head_metadata() {` | `wayback_extracts_body_text_without_head_metadata [function]` | `e4fd5946-35c5-52a2-94f0-a26791ab96e4` | 403-413 [crates/gwiki/src/ingest/wayback.rs:403-413] | Indexed function `wayback_extracts_body_text_without_head_metadata` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:403-413] |
| `wayback_groups_inline_text_per_block` | function | `fn wayback_groups_inline_text_per_block() {` | `wayback_groups_inline_text_per_block [function]` | `43692c99-259f-5ccc-9320-3230f7e19ebd` | 416-430 [crates/gwiki/src/ingest/wayback.rs:416-430] | Indexed function `wayback_groups_inline_text_per_block` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:416-430] |
| `wayback_prefers_html_title_then_decoded_url_path_then_host` | function | `fn wayback_prefers_html_title_then_decoded_url_path_then_host() {` | `wayback_prefers_html_title_then_decoded_url_path_then_host [function]` | `e68e6ece-a42f-5663-8080-9ded3c72cdf5` | 433-465 [crates/gwiki/src/ingest/wayback.rs:433-465] | Indexed function `wayback_prefers_html_title_then_decoded_url_path_then_host` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:433-465] |
| `wayback_does_not_decode_entities_twice` | function | `fn wayback_does_not_decode_entities_twice() {` | `wayback_does_not_decode_entities_twice [function]` | `83ecc2ee-e393-5ad0-a1a7-46e649d9da37` | 468-475 [crates/gwiki/src/ingest/wayback.rs:468-475] | Indexed function `wayback_does_not_decode_entities_twice` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:468-475] |
| `wayback_decodes_declared_charset` | function | `fn wayback_decodes_declared_charset() {` | `wayback_decodes_declared_charset [function]` | `b0348520-a7e0-5b7b-b803-252980536758` | 478-491 [crates/gwiki/src/ingest/wayback.rs:478-491] | Indexed function `wayback_decodes_declared_charset` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:478-491] |
| `wayback_rejects_non_html_content_type` | function | `fn wayback_rejects_non_html_content_type() {` | `wayback_rejects_non_html_content_type [function]` | `8f244255-fb17-54c0-99b8-dcd36feecb42` | 494-511 [crates/gwiki/src/ingest/wayback.rs:494-511] | Indexed function `wayback_rejects_non_html_content_type` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:494-511] |
| `document_for` | function | `fn document_for(bytes: &[u8]) -> Html {` | `document_for [function]` | `24eac95d-9a8b-5a3f-842c-a3eba4a478af` | 513-516 [crates/gwiki/src/ingest/wayback.rs:513-516] | Indexed function `document_for` in `crates/gwiki/src/ingest/wayback.rs`. [crates/gwiki/src/ingest/wayback.rs:513-516] |
