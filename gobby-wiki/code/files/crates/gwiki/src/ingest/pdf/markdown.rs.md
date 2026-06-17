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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/pdf/markdown.rs:15-89](crates/gwiki/src/ingest/pdf/markdown.rs#L15-L89), [crates/gwiki/src/ingest/pdf/markdown.rs:92-107](crates/gwiki/src/ingest/pdf/markdown.rs#L92-L107), [crates/gwiki/src/ingest/pdf/markdown.rs:110-135](crates/gwiki/src/ingest/pdf/markdown.rs#L110-L135), [crates/gwiki/src/ingest/pdf/markdown.rs:138-156](crates/gwiki/src/ingest/pdf/markdown.rs#L138-L156), [crates/gwiki/src/ingest/pdf/markdown.rs:159-239](crates/gwiki/src/ingest/pdf/markdown.rs#L159-L239), [crates/gwiki/src/ingest/pdf/markdown.rs:242-264](crates/gwiki/src/ingest/pdf/markdown.rs#L242-L264), [crates/gwiki/src/ingest/pdf/markdown.rs:267-272](crates/gwiki/src/ingest/pdf/markdown.rs#L267-L272), [crates/gwiki/src/ingest/pdf/markdown.rs:275-295](crates/gwiki/src/ingest/pdf/markdown.rs#L275-L295), [crates/gwiki/src/ingest/pdf/markdown.rs:298-319](crates/gwiki/src/ingest/pdf/markdown.rs#L298-L319), [crates/gwiki/src/ingest/pdf/markdown.rs:322-328](crates/gwiki/src/ingest/pdf/markdown.rs#L322-L328), [crates/gwiki/src/ingest/pdf/markdown.rs:331-335](crates/gwiki/src/ingest/pdf/markdown.rs#L331-L335), [crates/gwiki/src/ingest/pdf/markdown.rs:338-344](crates/gwiki/src/ingest/pdf/markdown.rs#L338-L344), [crates/gwiki/src/ingest/pdf/markdown.rs:351-360](crates/gwiki/src/ingest/pdf/markdown.rs#L351-L360), [crates/gwiki/src/ingest/pdf/markdown.rs:363-375](crates/gwiki/src/ingest/pdf/markdown.rs#L363-L375)

</details>

# crates/gwiki/src/ingest/pdf/markdown.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file assembles the final Markdown representation for ingested PDFs. `render_pdf_markdown` builds a document-level Markdown page with metadata, title, degradation notes, and per-page content, while helper functions sanitize page Markdown, neutralize page-marker variants, detect horizontal rules, and merge page sections into a single coherent output.

It also supports OCR/vision integration by selecting the vision model, extracting page-level vision data, deriving rendered asset names and paths, and deduplicating overlapping OCR text so repeated content is not emitted twice. The included tests cover marker neutralization and OCR overlap-key behavior.
[crates/gwiki/src/ingest/pdf/markdown.rs:15-89]
[crates/gwiki/src/ingest/pdf/markdown.rs:92-107]
[crates/gwiki/src/ingest/pdf/markdown.rs:110-135]
[crates/gwiki/src/ingest/pdf/markdown.rs:138-156]
[crates/gwiki/src/ingest/pdf/markdown.rs:159-239]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_pdf_markdown` | function | `pub(crate) fn render_pdf_markdown(` | `render_pdf_markdown [function]` | `498013f6-0417-5d77-884f-5dc728e46394` | 15-89 [crates/gwiki/src/ingest/pdf/markdown.rs:15-89] | Indexed function `render_pdf_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:15-89] |
| `sanitize_pdf_page_markdown` | function | `pub(crate) fn sanitize_pdf_page_markdown(markdown: &str) -> String {` | `sanitize_pdf_page_markdown [function]` | `017e301e-e617-58cc-b179-cb2195a4f3f0` | 92-107 [crates/gwiki/src/ingest/pdf/markdown.rs:92-107] | Indexed function `sanitize_pdf_page_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:92-107] |
| `neutralize_gwiki_page_marker_variants` | function | `fn neutralize_gwiki_page_marker_variants(line: &str) -> String {` | `neutralize_gwiki_page_marker_variants [function]` | `6a95a7e1-e58c-55a8-ac11-94f20e7abbc5` | 110-135 [crates/gwiki/src/ingest/pdf/markdown.rs:110-135] | Indexed function `neutralize_gwiki_page_marker_variants` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:110-135] |
| `is_markdown_horizontal_rule` | function | `fn is_markdown_horizontal_rule(trimmed: &str) -> bool {` | `is_markdown_horizontal_rule [function]` | `4a3322af-f8bc-5dc0-a366-6e5523d13c7c` | 138-156 [crates/gwiki/src/ingest/pdf/markdown.rs:138-156] | Indexed function `is_markdown_horizontal_rule` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:138-156] |
| `merge_pdf_pages` | function | `pub(crate) fn merge_pdf_pages(` | `merge_pdf_pages [function]` | `b2c5f605-b695-5f0e-9527-409a696011cf` | 159-239 [crates/gwiki/src/ingest/pdf/markdown.rs:159-239] | Indexed function `merge_pdf_pages` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:159-239] |
| `extract_vision_for_page` | function | `fn extract_vision_for_page(` | `extract_vision_for_page [function]` | `d3218dfc-d267-5f83-a82d-8ce61012bf30` | 242-264 [crates/gwiki/src/ingest/pdf/markdown.rs:242-264] | Indexed function `extract_vision_for_page` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:242-264] |
| `rendered_page_asset_path` | function | `fn rendered_page_asset_path(asset_path: &Path, file_name: &str) -> PathBuf {` | `rendered_page_asset_path [function]` | `faefec51-786e-56f5-8905-c2b0856b3c9f` | 267-272 [crates/gwiki/src/ingest/pdf/markdown.rs:267-272] | Indexed function `rendered_page_asset_path` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:267-272] |
| `merge_page_markdown` | function | `fn merge_page_markdown(text_layer: &str, vision: Option<&VisionExtraction>) -> String {` | `merge_page_markdown [function]` | `bfd548d1-adf4-5a06-bac3-e9f999a00d48` | 275-295 [crates/gwiki/src/ingest/pdf/markdown.rs:275-295] | Indexed function `merge_page_markdown` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:275-295] |
| `dedupe_ocr_text` | function | `fn dedupe_ocr_text(text_layer: &str, ocr_text: &str) -> Option<String> {` | `dedupe_ocr_text [function]` | `dca13354-ce5c-5155-a62f-8f8d836c3ca0` | 298-319 [crates/gwiki/src/ingest/pdf/markdown.rs:298-319] | Indexed function `dedupe_ocr_text` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:298-319] |
| `overlap_key` | function | `fn overlap_key(value: &str) -> String {` | `overlap_key [function]` | `f14789d1-bb08-5469-86d7-0cb0cdcc0ffb` | 322-328 [crates/gwiki/src/ingest/pdf/markdown.rs:322-328] | Indexed function `overlap_key` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:322-328] |
| `vision_model` | function | `fn vision_model(vision: &VisionExtraction) -> Option<&str> {` | `vision_model [function]` | `98b04f8c-8306-5266-a988-fa98f0fae810` | 331-335 [crates/gwiki/src/ingest/pdf/markdown.rs:331-335] | Indexed function `vision_model` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:331-335] |
| `rendered_page_file_name` | function | `fn rendered_page_file_name(file_name: &str, page_number: usize) -> String {` | `rendered_page_file_name [function]` | `81e990f6-f1a7-566f-888e-496dbbdd5eba` | 338-344 [crates/gwiki/src/ingest/pdf/markdown.rs:338-344] | Indexed function `rendered_page_file_name` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:338-344] |
| `page_markdown_neutralizes_marker_variants` | function | `fn page_markdown_neutralizes_marker_variants() {` | `page_markdown_neutralizes_marker_variants [function]` | `c226bd7c-7995-5f04-a7f7-c03947c53a93` | 351-360 [crates/gwiki/src/ingest/pdf/markdown.rs:351-360] | Indexed function `page_markdown_neutralizes_marker_variants` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:351-360] |
| `ocr_overlap_key_preserves_punctuation_collisions` | function | `fn ocr_overlap_key_preserves_punctuation_collisions() {` | `ocr_overlap_key_preserves_punctuation_collisions [function]` | `fed949bf-d648-5140-b960-e6c28587c8f6` | 363-375 [crates/gwiki/src/ingest/pdf/markdown.rs:363-375] | Indexed function `ocr_overlap_key_preserves_punctuation_collisions` in `crates/gwiki/src/ingest/pdf/markdown.rs`. [crates/gwiki/src/ingest/pdf/markdown.rs:363-375] |
