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

This file builds the Markdown output for ingested PDFs and the supporting page-level content used to assemble it. `render_pdf_markdown` writes document metadata, degradation notes, the title, and the rendered page sections or a no-text fallback, while `merge_pdf_pages`, `merge_page_markdown`, `dedupe_ocr_text`, and the vision helpers combine OCR and vision extraction into per-page Markdown. The remaining helpers keep the output safe and consistent by sanitizing page text, neutralizing `gwiki-page` marker variants, detecting Markdown horizontal rules, deriving page asset names and paths, and exposing tests that lock in the sanitization and OCR deduplication behavior.
[crates/gwiki/src/ingest/pdf/markdown.rs:15-89]
[crates/gwiki/src/ingest/pdf/markdown.rs:92-107]
[crates/gwiki/src/ingest/pdf/markdown.rs:110-135]
[crates/gwiki/src/ingest/pdf/markdown.rs:138-156]
[crates/gwiki/src/ingest/pdf/markdown.rs:159-239]

## API Symbols

- `render_pdf_markdown` (function) component `render_pdf_markdown [function]` (`498013f6-0417-5d77-884f-5dc728e46394`) lines 15-89 [crates/gwiki/src/ingest/pdf/markdown.rs:15-89]
  - Signature: `pub(crate) fn render_pdf_markdown(`
  - Purpose: 'render_pdf_markdown' assembles a Markdown representation of a PDF snapshot by emitting metadata fields, the document title, optional degradation notes, and the per-page extracted text content, or a no-text message when no pages are extractable. [crates/gwiki/src/ingest/pdf/markdown.rs:15-89]
- `sanitize_pdf_page_markdown` (function) component `sanitize_pdf_page_markdown [function]` (`017e301e-e617-58cc-b179-cb2195a4f3f0`) lines 92-107 [crates/gwiki/src/ingest/pdf/markdown.rs:92-107]
  - Signature: `pub(crate) fn sanitize_pdf_page_markdown(markdown: &str) -> String {`
  - Purpose: Processes each line of Markdown, escaping any line that would render as a horizontal rule and neutralizing all 'gwiki' page-marker variants, then rejoins the lines with '\n'. [crates/gwiki/src/ingest/pdf/markdown.rs:92-107]
- `neutralize_gwiki_page_marker_variants` (function) component `neutralize_gwiki_page_marker_variants [function]` (`6a95a7e1-e58c-55a8-ac11-94f20e7abbc5`) lines 110-135 [crates/gwiki/src/ingest/pdf/markdown.rs:110-135]
  - Signature: `fn neutralize_gwiki_page_marker_variants(line: &str) -> String {`
  - Purpose: Returns a copy of 'line' with any case-insensitive '<!--' comment opener followed by optional whitespace and 'gwiki-page' rewritten to '<! --' to neutralize that marker variant, while leaving all other text unchanged. [crates/gwiki/src/ingest/pdf/markdown.rs:110-135]
- `is_markdown_horizontal_rule` (function) component `is_markdown_horizontal_rule [function]` (`4a3322af-f8bc-5dc0-a366-6e5523d13c7c`) lines 138-156 [crates/gwiki/src/ingest/pdf/markdown.rs:138-156]
  - Signature: `fn is_markdown_horizontal_rule(trimmed: &str) -> bool {`
  - Purpose: Returns 'true' only if 'trimmed' consists of at least three non-whitespace characters, all identical and each one '-', '_', or '*', making it a valid Markdown horizontal rule. [crates/gwiki/src/ingest/pdf/markdown.rs:138-156]
- `merge_pdf_pages` (function) component `merge_pdf_pages [function]` (`b2c5f605-b695-5f0e-9527-409a696011cf`) lines 159-239 [crates/gwiki/src/ingest/pdf/markdown.rs:159-239]
  - Signature: `pub(crate) fn merge_pdf_pages(`
  - Purpose: Merges OCR text and per-page vision extraction for all PDF page numbers into 'PdfPageMarkdown' outputs, while tracking whether vision was used, which vision models were involved, and any extraction failures for the returned 'PdfMarkdownSummary'. [crates/gwiki/src/ingest/pdf/markdown.rs:159-239]
- `extract_vision_for_page` (function) component `extract_vision_for_page [function]` (`d3218dfc-d267-5f83-a82d-8ce61012bf30`) lines 242-264 [crates/gwiki/src/ingest/pdf/markdown.rs:242-264]
  - Signature: `fn extract_vision_for_page(`
  - Purpose: Returns 'Ok(None)' when the vision endpoint is unavailable, otherwise builds the rendered page’s asset/file metadata and forwards the page image bytes, dimensions, and MIME type to 'client.extract', wrapping the resulting 'VisionExtraction' in 'Some' on success. [crates/gwiki/src/ingest/pdf/markdown.rs:242-264]
- `rendered_page_asset_path` (function) component `rendered_page_asset_path [function]` (`faefec51-786e-56f5-8905-c2b0856b3c9f`) lines 267-272 [crates/gwiki/src/ingest/pdf/markdown.rs:267-272]
  - Signature: `fn rendered_page_asset_path(asset_path: &Path, file_name: &str) -> PathBuf {`
  - Purpose: Returns a path to 'file_name' in 'asset_path''s parent directory, or a standalone 'PathBuf' from 'file_name' if 'asset_path' has no parent. [crates/gwiki/src/ingest/pdf/markdown.rs:267-272]
- `merge_page_markdown` (function) component `merge_page_markdown [function]` (`bfd548d1-adf4-5a06-bac3-e9f999a00d48`) lines 275-295 [crates/gwiki/src/ingest/pdf/markdown.rs:275-295]
  - Signature: `fn merge_page_markdown(text_layer: &str, vision: Option<&VisionExtraction>) -> String {`
  - Purpose: Normalizes the page text, then concatenates it with optional deduplicated OCR text and a single-line visual description from 'VisionExtraction' as markdown sections separated by blank lines. [crates/gwiki/src/ingest/pdf/markdown.rs:275-295]
- `dedupe_ocr_text` (function) component `dedupe_ocr_text [function]` (`dca13354-ce5c-5155-a62f-8f8d836c3ca0`) lines 298-319 [crates/gwiki/src/ingest/pdf/markdown.rs:298-319]
  - Signature: `fn dedupe_ocr_text(text_layer: &str, ocr_text: &str) -> Option<String> {`
  - Purpose: Returns normalized OCR text only when it is nonempty and not fully covered by overlapping content in 'text_layer', otherwise 'None', and it can also drop any OCR paragraphs whose overlap key is already contained in the text layer. [crates/gwiki/src/ingest/pdf/markdown.rs:298-319]
- `overlap_key` (function) component `overlap_key [function]` (`f14789d1-bb08-5469-86d7-0cb0cdcc0ffb`) lines 322-328 [crates/gwiki/src/ingest/pdf/markdown.rs:322-328]
  - Signature: `fn overlap_key(value: &str) -> String {`
  - Purpose: 'overlap_key' returns a normalized string key by removing all whitespace from 'value' and lowercasing the remaining characters. [crates/gwiki/src/ingest/pdf/markdown.rs:322-328]
- `vision_model` (function) component `vision_model [function]` (`98b04f8c-8306-5266-a988-fa98f0fae810`) lines 331-335 [crates/gwiki/src/ingest/pdf/markdown.rs:331-335]
  - Signature: `fn vision_model(vision: &VisionExtraction) -> Option<&str> {`
  - Purpose: Returns the first non-empty '"model"' metadata value from 'vision.metadata' as 'Some(&str)', or 'None' if no such entry exists. [crates/gwiki/src/ingest/pdf/markdown.rs:331-335]
- `rendered_page_file_name` (function) component `rendered_page_file_name [function]` (`81e990f6-f1a7-566f-888e-496dbbdd5eba`) lines 338-344 [crates/gwiki/src/ingest/pdf/markdown.rs:338-344]
  - Signature: `fn rendered_page_file_name(file_name: &str, page_number: usize) -> String {`
  - Purpose: Returns a PNG output filename by taking the input path’s stem when available (otherwise the original name) and appending '-page-{page_number}.png'. [crates/gwiki/src/ingest/pdf/markdown.rs:338-344]
- `page_markdown_neutralizes_marker_variants` (function) component `page_markdown_neutralizes_marker_variants [function]` (`c226bd7c-7995-5f04-a7f7-c03947c53a93`) lines 351-360 [crates/gwiki/src/ingest/pdf/markdown.rs:351-360]
  - Signature: `fn page_markdown_neutralizes_marker_variants() {`
  - Purpose: Verifies that 'sanitize_pdf_page_markdown' neutralizes all case and spacing variants of the 'gwiki-page' HTML comment marker by inserting a space after '<!' so the comments are no longer recognized as page markers. [crates/gwiki/src/ingest/pdf/markdown.rs:351-360]
- `ocr_overlap_key_preserves_punctuation_collisions` (function) component `ocr_overlap_key_preserves_punctuation_collisions [function]` (`fed949bf-d648-5140-b960-e6c28587c8f6`) lines 363-375 [crates/gwiki/src/ingest/pdf/markdown.rs:363-375]
  - Signature: `fn ocr_overlap_key_preserves_punctuation_collisions() {`
  - Purpose: Verifies that OCR overlap keys preserve punctuation-sensitive distinctions (e.g., '/', '-', '@') so deduplication does not conflate strings that differ only by punctuation, while identical text is deduped to 'None'. [crates/gwiki/src/ingest/pdf/markdown.rs:363-375]

