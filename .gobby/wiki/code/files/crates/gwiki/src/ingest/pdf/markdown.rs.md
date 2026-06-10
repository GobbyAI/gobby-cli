---
title: crates/gwiki/src/ingest/pdf/markdown.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/markdown.rs
  ranges:
  - 14-88
  - 90-105
  - 107-132
  - 134-152
  - 154-234
  - 236-258
  - 260-265
  - 267-287
  - 289-310
  - 312-318
  - 320-324
  - 326-332
  - 339-348
  - 351-363
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/markdown.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

`crates/gwiki/src/ingest/pdf/markdown.rs` exposes 14 indexed API symbols.
[crates/gwiki/src/ingest/pdf/markdown.rs:14-88]
[crates/gwiki/src/ingest/pdf/markdown.rs:90-105]
[crates/gwiki/src/ingest/pdf/markdown.rs:107-132]
[crates/gwiki/src/ingest/pdf/markdown.rs:134-152]
[crates/gwiki/src/ingest/pdf/markdown.rs:154-234]
[crates/gwiki/src/ingest/pdf/markdown.rs:236-258]
[crates/gwiki/src/ingest/pdf/markdown.rs:260-265]
[crates/gwiki/src/ingest/pdf/markdown.rs:267-287]
[crates/gwiki/src/ingest/pdf/markdown.rs:289-310]
[crates/gwiki/src/ingest/pdf/markdown.rs:312-318]
[crates/gwiki/src/ingest/pdf/markdown.rs:320-324]
[crates/gwiki/src/ingest/pdf/markdown.rs:326-332]
[crates/gwiki/src/ingest/pdf/markdown.rs:339-348]
[crates/gwiki/src/ingest/pdf/markdown.rs:351-363]

## API Symbols

- `render_pdf_markdown` (function) component `render_pdf_markdown [function]` (`8d7d56c6-08d3-5cab-8930-171c49d3a092`) lines 14-88 [crates/gwiki/src/ingest/pdf/markdown.rs:14-88]
  - Signature: `pub(crate) fn render_pdf_markdown(`
  - Purpose: Indexed function `render_pdf_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:14-88]
- `sanitize_pdf_page_markdown` (function) component `sanitize_pdf_page_markdown [function]` (`0b7af7cb-7b4a-5f37-87d5-36bb1146bf5f`) lines 90-105 [crates/gwiki/src/ingest/pdf/markdown.rs:90-105]
  - Signature: `pub(crate) fn sanitize_pdf_page_markdown(markdown: &str) -> String {`
  - Purpose: Indexed function `sanitize_pdf_page_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:90-105]
- `neutralize_gwiki_page_marker_variants` (function) component `neutralize_gwiki_page_marker_variants [function]` (`bdf90718-a0de-56ee-b66f-53a8f8241e0a`) lines 107-132 [crates/gwiki/src/ingest/pdf/markdown.rs:107-132]
  - Signature: `fn neutralize_gwiki_page_marker_variants(line: &str) -> String {`
  - Purpose: Indexed function `neutralize_gwiki_page_marker_variants` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:107-132]
- `is_markdown_horizontal_rule` (function) component `is_markdown_horizontal_rule [function]` (`8b4b8f8d-9f25-57cc-8e54-012e04db2978`) lines 134-152 [crates/gwiki/src/ingest/pdf/markdown.rs:134-152]
  - Signature: `fn is_markdown_horizontal_rule(trimmed: &str) -> bool {`
  - Purpose: Indexed function `is_markdown_horizontal_rule` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:134-152]
- `merge_pdf_pages` (function) component `merge_pdf_pages [function]` (`488ab16c-90e1-5099-8276-d1f298d35387`) lines 154-234 [crates/gwiki/src/ingest/pdf/markdown.rs:154-234]
  - Signature: `pub(crate) fn merge_pdf_pages(`
  - Purpose: Indexed function `merge_pdf_pages` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:154-234]
- `extract_vision_for_page` (function) component `extract_vision_for_page [function]` (`6065719f-acc2-5a93-92e2-9087ed3007b3`) lines 236-258 [crates/gwiki/src/ingest/pdf/markdown.rs:236-258]
  - Signature: `fn extract_vision_for_page(`
  - Purpose: Indexed function `extract_vision_for_page` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:236-258]
- `rendered_page_asset_path` (function) component `rendered_page_asset_path [function]` (`a043ad92-1f41-542e-becf-793d63c443db`) lines 260-265 [crates/gwiki/src/ingest/pdf/markdown.rs:260-265]
  - Signature: `fn rendered_page_asset_path(asset_path: &Path, file_name: &str) -> PathBuf {`
  - Purpose: Indexed function `rendered_page_asset_path` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:260-265]
- `merge_page_markdown` (function) component `merge_page_markdown [function]` (`ceb6a4fe-6ee4-5f68-ab33-c41f56e12d17`) lines 267-287 [crates/gwiki/src/ingest/pdf/markdown.rs:267-287]
  - Signature: `fn merge_page_markdown(text_layer: &str, vision: Option<&VisionExtraction>) -> String {`
  - Purpose: Indexed function `merge_page_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:267-287]
- `dedupe_ocr_text` (function) component `dedupe_ocr_text [function]` (`1b61b7b1-1974-55a8-9a8d-b6e92afe0129`) lines 289-310 [crates/gwiki/src/ingest/pdf/markdown.rs:289-310]
  - Signature: `fn dedupe_ocr_text(text_layer: &str, ocr_text: &str) -> Option<String> {`
  - Purpose: Indexed function `dedupe_ocr_text` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:289-310]
- `overlap_key` (function) component `overlap_key [function]` (`4fd5b650-6d67-54a2-9c74-f72e0621f6c6`) lines 312-318 [crates/gwiki/src/ingest/pdf/markdown.rs:312-318]
  - Signature: `fn overlap_key(value: &str) -> String {`
  - Purpose: Indexed function `overlap_key` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:312-318]
- `vision_model` (function) component `vision_model [function]` (`ed764084-bbb3-5da6-92b2-a2f2eb5df96c`) lines 320-324 [crates/gwiki/src/ingest/pdf/markdown.rs:320-324]
  - Signature: `fn vision_model(vision: &VisionExtraction) -> Option<&str> {`
  - Purpose: Indexed function `vision_model` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:320-324]
- `rendered_page_file_name` (function) component `rendered_page_file_name [function]` (`50586177-3d98-5217-9b5c-a4ce55a42622`) lines 326-332 [crates/gwiki/src/ingest/pdf/markdown.rs:326-332]
  - Signature: `fn rendered_page_file_name(file_name: &str, page_number: usize) -> String {`
  - Purpose: Indexed function `rendered_page_file_name` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:326-332]
- `page_markdown_neutralizes_marker_variants` (function) component `page_markdown_neutralizes_marker_variants [function]` (`9d95e79b-055e-541a-bc21-52246cbf491e`) lines 339-348 [crates/gwiki/src/ingest/pdf/markdown.rs:339-348]
  - Signature: `fn page_markdown_neutralizes_marker_variants() {`
  - Purpose: Indexed function `page_markdown_neutralizes_marker_variants` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:339-348]
- `ocr_overlap_key_preserves_punctuation_collisions` (function) component `ocr_overlap_key_preserves_punctuation_collisions [function]` (`08c28f21-627c-5404-bee2-8c6a0083301a`) lines 351-363 [crates/gwiki/src/ingest/pdf/markdown.rs:351-363]
  - Signature: `fn ocr_overlap_key_preserves_punctuation_collisions() {`
  - Purpose: Indexed function `ocr_overlap_key_preserves_punctuation_collisions` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:351-363]

