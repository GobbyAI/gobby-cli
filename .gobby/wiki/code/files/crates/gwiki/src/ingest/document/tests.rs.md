---
title: crates/gwiki/src/ingest/document/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/tests.rs
  ranges:
  - 9-18
  - 20-25
  - 27-38
  - 40-53
  - 55-59
  - 61-70
  - 72-96
  - 98-118
  - 121-200
  - 203-258
  - 261-263
  - 266-273
  - 276-294
  - 297-317
  - 320-327
  - 330-337
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/document/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/document|crates/gwiki/src/ingest/document]]

## Purpose

`crates/gwiki/src/ingest/document/tests.rs` exposes 16 indexed API symbols.
[crates/gwiki/src/ingest/document/tests.rs:9-18]
[crates/gwiki/src/ingest/document/tests.rs:20-25]
[crates/gwiki/src/ingest/document/tests.rs:27-38]
[crates/gwiki/src/ingest/document/tests.rs:40-53]
[crates/gwiki/src/ingest/document/tests.rs:55-59]

## API Symbols

- `zip_bytes` (function) component `zip_bytes [function]` (`e159808c-c939-572e-a119-bfac3b926927`) lines 9-18 [crates/gwiki/src/ingest/document/tests.rs:9-18]
  - Signature: `fn zip_bytes(entries: &[(&str, &str)]) -> Vec<u8> {`
  - Purpose: Serializes an array of file path-content string pairs into a ZIP archive and returns the resulting bytes as a Vec<u8>. [crates/gwiki/src/ingest/document/tests.rs:9-18]
- `sample_docx` (function) component `sample_docx [function]` (`91e776d2-ed03-5f6a-9489-59442936e068`) lines 20-25 [crates/gwiki/src/ingest/document/tests.rs:20-25]
  - Signature: `fn sample_docx() -> Vec<u8> {`
  - Purpose: Generates a minimal DOCX file as a ZIP-compressed byte vector containing a `word/document.xml` entry with two sample text paragraphs. [crates/gwiki/src/ingest/document/tests.rs:20-25]
- `sample_pptx` (function) component `sample_pptx [function]` (`ade42d9a-89bb-5429-9754-b236cc69eb71`) lines 27-38 [crates/gwiki/src/ingest/document/tests.rs:27-38]
  - Signature: `fn sample_pptx() -> Vec<u8> {`
  - Purpose: This function constructs and returns a PPTX file as a byte vector by zipping together XML definitions for two presentation slides with text content. [crates/gwiki/src/ingest/document/tests.rs:27-38]
- `oversized_pptx` (function) component `oversized_pptx [function]` (`f7443137-71ba-573f-bcf4-04fd4fdc0966`) lines 40-53 [crates/gwiki/src/ingest/document/tests.rs:40-53]
  - Signature: `fn oversized_pptx(slide_count: usize) -> Vec<u8> {`
  - Purpose: Generates a PPTX file (ZIP archive) as a byte vector containing the specified number of XML slide definitions. [crates/gwiki/src/ingest/document/tests.rs:40-53]
- `sample_xlsx` (function) component `sample_xlsx [function]` (`8a341812-03b3-56d0-9543-e128a11a545b`) lines 55-59 [crates/gwiki/src/ingest/document/tests.rs:55-59]
  - Signature: `fn sample_xlsx() -> Vec<u8> {`
  - Purpose: Generates and returns a `Vec<u8>` containing the serialized XLSX file bytes for a workbook with a single sheet holding a two-column table (City, Count) and one sample data row (Duluth, 3). [crates/gwiki/src/ingest/document/tests.rs:55-59]
- `oversized_xlsx` (function) component `oversized_xlsx [function]` (`b11dcdf9-dd7d-5e03-bc0e-ea1015f543fe`) lines 61-70 [crates/gwiki/src/ingest/document/tests.rs:61-70]
  - Signature: `fn oversized_xlsx(row_count: usize) -> Vec<u8> {`
  - Purpose: Generates an XLSX file as bytes containing `row_count` sequentially numbered rows, each with an inline string cell in column A containing the text "City {n}". [crates/gwiki/src/ingest/document/tests.rs:61-70]
- `xlsx_with_sheet_data` (function) component `xlsx_with_sheet_data [function]` (`40f28995-bdf8-5e67-b4ad-2d17c3849718`) lines 72-96 [crates/gwiki/src/ingest/document/tests.rs:72-96]
  - Signature: `fn xlsx_with_sheet_data(sheet_data: &str) -> Vec<u8> {`
  - Purpose: Generates a ZIP-compressed XLSX file in binary format by embedding the provided sheet data within the required Office Open XML structure. [crates/gwiki/src/ingest/document/tests.rs:72-96]
- `ingest_sample` (function) component `ingest_sample [function]` (`6b25f6cf-427b-5105-8748-49b761667c39`) lines 98-118 [crates/gwiki/src/ingest/document/tests.rs:98-118]
  - Signature: `fn ingest_sample(`
  - Purpose: Creates and ingests a DocumentSnapshot from provided bytes and metadata into a MemoryWikiStore scoped to project-123, panicking on ingest failure. [crates/gwiki/src/ingest/document/tests.rs:98-118]
- `extracts_office_html_and_degrades` (function) component `extracts_office_html_and_degrades [function]` (`7c3e9394-57e3-5625-a4f9-e0a3adeba928`) lines 121-200 [crates/gwiki/src/ingest/document/tests.rs:121-200]
  - Signature: `fn extracts_office_html_and_degrades() {`
  - Purpose: This function tests that Office documents (XLSX, DOCX, PPTX) and HTML are extracted, converted to markdown, indexed in a wiki store, and gracefully degrade when encountering malformed input. [crates/gwiki/src/ingest/document/tests.rs:121-200]
- `office_html_degradation_uses_uniform_metadata` (function) component `office_html_degradation_uses_uniform_metadata [function]` (`a2ffb9eb-7e85-5fd7-add1-8964468f09c4`) lines 203-258 [crates/gwiki/src/ingest/document/tests.rs:203-258]
  - Signature: `fn office_html_degradation_uses_uniform_metadata() {`
  - Purpose: # Summary

Tests that degraded Office and HTML media files generate indexed documents with uniform metadata fields (media_degradation, file_size_bytes, and format-specific counts) despite ingestion failures. [crates/gwiki/src/ingest/document/tests.rs:203-258]
- `markdown_table_handles_empty_rows` (function) component `markdown_table_handles_empty_rows [function]` (`83c6550a-1061-580c-8253-739d6c8277ef`) lines 261-263 [crates/gwiki/src/ingest/document/tests.rs:261-263]
  - Signature: `fn markdown_table_handles_empty_rows() {`
  - Purpose: This test verifies that the `markdown_table` function returns an empty string when given an empty input slice. [crates/gwiki/src/ingest/document/tests.rs:261-263]
- `office_zip_reads_are_bounded` (function) component `office_zip_reads_are_bounded [function]` (`b2fb557d-9a8e-5a02-a338-0e6e73bce9db`) lines 266-273 [crates/gwiki/src/ingest/document/tests.rs:266-273]
  - Signature: `fn office_zip_reads_are_bounded() {`
  - Purpose: This test validates that `extract_docx` enforces a maximum XML entry size limit by rejecting DOCX files with oversized entries and raising a `WikiError::InvalidInput` with appropriate error messaging. [crates/gwiki/src/ingest/document/tests.rs:266-273]
- `pptx_slide_count_is_bounded` (function) component `pptx_slide_count_is_bounded [function]` (`d1600852-8553-5f7c-b959-f7981c57e00f`) lines 276-294 [crates/gwiki/src/ingest/document/tests.rs:276-294]
  - Signature: `fn pptx_slide_count_is_bounded() {`
  - Purpose: This test validates that PPTX extraction enforces a maximum slide count limit (`MAX_SLIDES`), truncating oversized presentations and documenting the truncation through degradation metadata with reason code `office_bounded_extraction` and a markdown notice. [crates/gwiki/src/ingest/document/tests.rs:276-294]
- `xlsx_table_bounds_report_degradation` (function) component `xlsx_table_bounds_report_degradation [function]` (`ce934271-3de0-5398-9600-979b8243ea36`) lines 297-317 [crates/gwiki/src/ingest/document/tests.rs:297-317]
  - Signature: `fn xlsx_table_bounds_report_degradation() {`
  - Purpose: Tests that bounded extraction of an XLSX file exceeding MAX_ROWS_PER_SHEET produces truncation warnings and generates proper office_bounded_extraction degradation metadata. [crates/gwiki/src/ingest/document/tests.rs:297-317]
- `html_extraction_combines_inline_text_nodes` (function) component `html_extraction_combines_inline_text_nodes [function]` (`d537b31f-c128-5940-bc98-6c57e084622e`) lines 320-327 [crates/gwiki/src/ingest/document/tests.rs:320-327]
  - Signature: `fn html_extraction_combines_inline_text_nodes() {`
  - Purpose: This test verifies that HTML-to-markdown extraction correctly combines inline text nodes with inline formatting elements (like `<strong>`) and preserves paragraph separation in the output. [crates/gwiki/src/ingest/document/tests.rs:320-327]
- `html_extraction_avoids_spaces_before_closing_quotes` (function) component `html_extraction_avoids_spaces_before_closing_quotes [function]` (`9607b55d-3e88-55cc-aeee-8c66cc0e88f9`) lines 330-337 [crates/gwiki/src/ingest/document/tests.rs:330-337]
  - Signature: `fn html_extraction_avoids_spaces_before_closing_quotes() {`
  - Purpose: This test verifies that `extract_html_document()` correctly converts HTML containing Unicode right double quotation marks (U+201D) to markdown without inserting spaces before the closing quote character. [crates/gwiki/src/ingest/document/tests.rs:330-337]

