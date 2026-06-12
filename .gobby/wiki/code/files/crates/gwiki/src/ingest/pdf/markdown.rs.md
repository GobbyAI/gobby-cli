---
title: crates/gwiki/src/ingest/pdf/markdown.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/markdown.rs
  ranges:
  - 15-89
  - 92-107
  - 110-135
  - 138-156
  - 159-239
  - 242-264
  - 267-272
  - 275-295
  - 298-319
  - 322-328
  - 331-335
  - 338-344
  - 351-360
  - 363-375
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/markdown.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

`crates/gwiki/src/ingest/pdf/markdown.rs` exposes 14 indexed API symbols.
[crates/gwiki/src/ingest/pdf/markdown.rs:15-89]
[crates/gwiki/src/ingest/pdf/markdown.rs:92-107]
[crates/gwiki/src/ingest/pdf/markdown.rs:110-135]
[crates/gwiki/src/ingest/pdf/markdown.rs:138-156]
[crates/gwiki/src/ingest/pdf/markdown.rs:159-239]

## API Symbols

- `render_pdf_markdown` (function) component `render_pdf_markdown [function]` (`498013f6-0417-5d77-884f-5dc728e46394`) lines 15-89 [crates/gwiki/src/ingest/pdf/markdown.rs:15-89]
  - Signature: `pub(crate) fn render_pdf_markdown(`
  - Purpose: Indexed function `render_pdf_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:15-89]
- `sanitize_pdf_page_markdown` (function) component `sanitize_pdf_page_markdown [function]` (`017e301e-e617-58cc-b179-cb2195a4f3f0`) lines 92-107 [crates/gwiki/src/ingest/pdf/markdown.rs:92-107]
  - Signature: `pub(crate) fn sanitize_pdf_page_markdown(markdown: &str) -> String {`
  - Purpose: Indexed function `sanitize_pdf_page_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:92-107]
- `neutralize_gwiki_page_marker_variants` (function) component `neutralize_gwiki_page_marker_variants [function]` (`6a95a7e1-e58c-55a8-ac11-94f20e7abbc5`) lines 110-135 [crates/gwiki/src/ingest/pdf/markdown.rs:110-135]
  - Signature: `fn neutralize_gwiki_page_marker_variants(line: &str) -> String {`
  - Purpose: Indexed function `neutralize_gwiki_page_marker_variants` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:110-135]
- `is_markdown_horizontal_rule` (function) component `is_markdown_horizontal_rule [function]` (`4a3322af-f8bc-5dc0-a366-6e5523d13c7c`) lines 138-156 [crates/gwiki/src/ingest/pdf/markdown.rs:138-156]
  - Signature: `fn is_markdown_horizontal_rule(trimmed: &str) -> bool {`
  - Purpose: Indexed function `is_markdown_horizontal_rule` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:138-156]
- `merge_pdf_pages` (function) component `merge_pdf_pages [function]` (`b2c5f605-b695-5f0e-9527-409a696011cf`) lines 159-239 [crates/gwiki/src/ingest/pdf/markdown.rs:159-239]
  - Signature: `pub(crate) fn merge_pdf_pages(`
  - Purpose: Indexed function `merge_pdf_pages` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:159-239]
- `extract_vision_for_page` (function) component `extract_vision_for_page [function]` (`d3218dfc-d267-5f83-a82d-8ce61012bf30`) lines 242-264 [crates/gwiki/src/ingest/pdf/markdown.rs:242-264]
  - Signature: `fn extract_vision_for_page(`
  - Purpose: Indexed function `extract_vision_for_page` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:242-264]
- `rendered_page_asset_path` (function) component `rendered_page_asset_path [function]` (`faefec51-786e-56f5-8905-c2b0856b3c9f`) lines 267-272 [crates/gwiki/src/ingest/pdf/markdown.rs:267-272]
  - Signature: `fn rendered_page_asset_path(asset_path: &Path, file_name: &str) -> PathBuf {`
  - Purpose: Indexed function `rendered_page_asset_path` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:267-272]
- `merge_page_markdown` (function) component `merge_page_markdown [function]` (`bfd548d1-adf4-5a06-bac3-e9f999a00d48`) lines 275-295 [crates/gwiki/src/ingest/pdf/markdown.rs:275-295]
  - Signature: `fn merge_page_markdown(text_layer: &str, vision: Option<&VisionExtraction>) -> String {`
  - Purpose: Indexed function `merge_page_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:275-295]
- `dedupe_ocr_text` (function) component `dedupe_ocr_text [function]` (`dca13354-ce5c-5155-a62f-8f8d836c3ca0`) lines 298-319 [crates/gwiki/src/ingest/pdf/markdown.rs:298-319]
  - Signature: `fn dedupe_ocr_text(text_layer: &str, ocr_text: &str) -> Option<String> {`
  - Purpose: Indexed function `dedupe_ocr_text` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:298-319]
- `overlap_key` (function) component `overlap_key [function]` (`f14789d1-bb08-5469-86d7-0cb0cdcc0ffb`) lines 322-328 [crates/gwiki/src/ingest/pdf/markdown.rs:322-328]
  - Signature: `fn overlap_key(value: &str) -> String {`
  - Purpose: Indexed function `overlap_key` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:322-328]
- `vision_model` (function) component `vision_model [function]` (`98b04f8c-8306-5266-a988-fa98f0fae810`) lines 331-335 [crates/gwiki/src/ingest/pdf/markdown.rs:331-335]
  - Signature: `fn vision_model(vision: &VisionExtraction) -> Option<&str> {`
  - Purpose: Indexed function `vision_model` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:331-335]
- `rendered_page_file_name` (function) component `rendered_page_file_name [function]` (`81e990f6-f1a7-566f-888e-496dbbdd5eba`) lines 338-344 [crates/gwiki/src/ingest/pdf/markdown.rs:338-344]
  - Signature: `fn rendered_page_file_name(file_name: &str, page_number: usize) -> String {`
  - Purpose: Indexed function `rendered_page_file_name` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:338-344]
- `page_markdown_neutralizes_marker_variants` (function) component `page_markdown_neutralizes_marker_variants [function]` (`c226bd7c-7995-5f04-a7f7-c03947c53a93`) lines 351-360 [crates/gwiki/src/ingest/pdf/markdown.rs:351-360]
  - Signature: `fn page_markdown_neutralizes_marker_variants() {`
  - Purpose: Indexed function `page_markdown_neutralizes_marker_variants` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:351-360]
- `ocr_overlap_key_preserves_punctuation_collisions` (function) component `ocr_overlap_key_preserves_punctuation_collisions [function]` (`fed949bf-d648-5140-b960-e6c28587c8f6`) lines 363-375 [crates/gwiki/src/ingest/pdf/markdown.rs:363-375]
  - Signature: `fn ocr_overlap_key_preserves_punctuation_collisions() {`
  - Purpose: Indexed function `ocr_overlap_key_preserves_punctuation_collisions` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:363-375]

