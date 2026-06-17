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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/document/tests.rs:9-18](crates/gwiki/src/ingest/document/tests.rs#L9-L18), [crates/gwiki/src/ingest/document/tests.rs:20-25](crates/gwiki/src/ingest/document/tests.rs#L20-L25), [crates/gwiki/src/ingest/document/tests.rs:27-38](crates/gwiki/src/ingest/document/tests.rs#L27-L38), [crates/gwiki/src/ingest/document/tests.rs:40-53](crates/gwiki/src/ingest/document/tests.rs#L40-L53), [crates/gwiki/src/ingest/document/tests.rs:55-59](crates/gwiki/src/ingest/document/tests.rs#L55-L59), [crates/gwiki/src/ingest/document/tests.rs:61-70](crates/gwiki/src/ingest/document/tests.rs#L61-L70), [crates/gwiki/src/ingest/document/tests.rs:72-96](crates/gwiki/src/ingest/document/tests.rs#L72-L96), [crates/gwiki/src/ingest/document/tests.rs:98-118](crates/gwiki/src/ingest/document/tests.rs#L98-L118), [crates/gwiki/src/ingest/document/tests.rs:121-200](crates/gwiki/src/ingest/document/tests.rs#L121-L200), [crates/gwiki/src/ingest/document/tests.rs:203-258](crates/gwiki/src/ingest/document/tests.rs#L203-L258), [crates/gwiki/src/ingest/document/tests.rs:261-263](crates/gwiki/src/ingest/document/tests.rs#L261-L263), [crates/gwiki/src/ingest/document/tests.rs:266-273](crates/gwiki/src/ingest/document/tests.rs#L266-L273), [crates/gwiki/src/ingest/document/tests.rs:276-294](crates/gwiki/src/ingest/document/tests.rs#L276-L294), [crates/gwiki/src/ingest/document/tests.rs:297-317](crates/gwiki/src/ingest/document/tests.rs#L297-L317), [crates/gwiki/src/ingest/document/tests.rs:320-327](crates/gwiki/src/ingest/document/tests.rs#L320-L327), [crates/gwiki/src/ingest/document/tests.rs:330-337](crates/gwiki/src/ingest/document/tests.rs#L330-L337)

</details>

# crates/gwiki/src/ingest/document/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/document|crates/gwiki/src/ingest/document]]

## Purpose

Test module for document ingestion, focused on Office file extraction and guardrails. It defines small ZIP-based fixture builders for DOCX, PPTX, and XLSX inputs, then uses them in tests that check text extraction, uniform degradation metadata, empty-table handling, bounded ZIP and slide reads, table-bound degradation reporting, and HTML text joining/quoting behavior.
[crates/gwiki/src/ingest/document/tests.rs:9-18]
[crates/gwiki/src/ingest/document/tests.rs:20-25]
[crates/gwiki/src/ingest/document/tests.rs:27-38]
[crates/gwiki/src/ingest/document/tests.rs:40-53]
[crates/gwiki/src/ingest/document/tests.rs:55-59]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `zip_bytes` | function | `fn zip_bytes(entries: &[(&str, &str)]) -> Vec<u8> {` | `zip_bytes [function]` | `e159808c-c939-572e-a119-bfac3b926927` | 9-18 [crates/gwiki/src/ingest/document/tests.rs:9-18] | Indexed function `zip_bytes` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:9-18] |
| `sample_docx` | function | `fn sample_docx() -> Vec<u8> {` | `sample_docx [function]` | `91e776d2-ed03-5f6a-9489-59442936e068` | 20-25 [crates/gwiki/src/ingest/document/tests.rs:20-25] | Indexed function `sample_docx` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:20-25] |
| `sample_pptx` | function | `fn sample_pptx() -> Vec<u8> {` | `sample_pptx [function]` | `ade42d9a-89bb-5429-9754-b236cc69eb71` | 27-38 [crates/gwiki/src/ingest/document/tests.rs:27-38] | Indexed function `sample_pptx` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:27-38] |
| `oversized_pptx` | function | `fn oversized_pptx(slide_count: usize) -> Vec<u8> {` | `oversized_pptx [function]` | `f7443137-71ba-573f-bcf4-04fd4fdc0966` | 40-53 [crates/gwiki/src/ingest/document/tests.rs:40-53] | Indexed function `oversized_pptx` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:40-53] |
| `sample_xlsx` | function | `fn sample_xlsx() -> Vec<u8> {` | `sample_xlsx [function]` | `8a341812-03b3-56d0-9543-e128a11a545b` | 55-59 [crates/gwiki/src/ingest/document/tests.rs:55-59] | Indexed function `sample_xlsx` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:55-59] |
| `oversized_xlsx` | function | `fn oversized_xlsx(row_count: usize) -> Vec<u8> {` | `oversized_xlsx [function]` | `b11dcdf9-dd7d-5e03-bc0e-ea1015f543fe` | 61-70 [crates/gwiki/src/ingest/document/tests.rs:61-70] | Indexed function `oversized_xlsx` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:61-70] |
| `xlsx_with_sheet_data` | function | `fn xlsx_with_sheet_data(sheet_data: &str) -> Vec<u8> {` | `xlsx_with_sheet_data [function]` | `40f28995-bdf8-5e67-b4ad-2d17c3849718` | 72-96 [crates/gwiki/src/ingest/document/tests.rs:72-96] | Indexed function `xlsx_with_sheet_data` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:72-96] |
| `ingest_sample` | function | `fn ingest_sample(` | `ingest_sample [function]` | `6b25f6cf-427b-5105-8748-49b761667c39` | 98-118 [crates/gwiki/src/ingest/document/tests.rs:98-118] | Indexed function `ingest_sample` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:98-118] |
| `extracts_office_html_and_degrades` | function | `fn extracts_office_html_and_degrades() {` | `extracts_office_html_and_degrades [function]` | `7c3e9394-57e3-5625-a4f9-e0a3adeba928` | 121-200 [crates/gwiki/src/ingest/document/tests.rs:121-200] | Indexed function `extracts_office_html_and_degrades` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:121-200] |
| `office_html_degradation_uses_uniform_metadata` | function | `fn office_html_degradation_uses_uniform_metadata() {` | `office_html_degradation_uses_uniform_metadata [function]` | `a2ffb9eb-7e85-5fd7-add1-8964468f09c4` | 203-258 [crates/gwiki/src/ingest/document/tests.rs:203-258] | Indexed function `office_html_degradation_uses_uniform_metadata` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:203-258] |
| `markdown_table_handles_empty_rows` | function | `fn markdown_table_handles_empty_rows() {` | `markdown_table_handles_empty_rows [function]` | `83c6550a-1061-580c-8253-739d6c8277ef` | 261-263 [crates/gwiki/src/ingest/document/tests.rs:261-263] | Indexed function `markdown_table_handles_empty_rows` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:261-263] |
| `office_zip_reads_are_bounded` | function | `fn office_zip_reads_are_bounded() {` | `office_zip_reads_are_bounded [function]` | `b2fb557d-9a8e-5a02-a338-0e6e73bce9db` | 266-273 [crates/gwiki/src/ingest/document/tests.rs:266-273] | Indexed function `office_zip_reads_are_bounded` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:266-273] |
| `pptx_slide_count_is_bounded` | function | `fn pptx_slide_count_is_bounded() {` | `pptx_slide_count_is_bounded [function]` | `d1600852-8553-5f7c-b959-f7981c57e00f` | 276-294 [crates/gwiki/src/ingest/document/tests.rs:276-294] | Indexed function `pptx_slide_count_is_bounded` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:276-294] |
| `xlsx_table_bounds_report_degradation` | function | `fn xlsx_table_bounds_report_degradation() {` | `xlsx_table_bounds_report_degradation [function]` | `ce934271-3de0-5398-9600-979b8243ea36` | 297-317 [crates/gwiki/src/ingest/document/tests.rs:297-317] | Indexed function `xlsx_table_bounds_report_degradation` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:297-317] |
| `html_extraction_combines_inline_text_nodes` | function | `fn html_extraction_combines_inline_text_nodes() {` | `html_extraction_combines_inline_text_nodes [function]` | `d537b31f-c128-5940-bc98-6c57e084622e` | 320-327 [crates/gwiki/src/ingest/document/tests.rs:320-327] | Indexed function `html_extraction_combines_inline_text_nodes` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:320-327] |
| `html_extraction_avoids_spaces_before_closing_quotes` | function | `fn html_extraction_avoids_spaces_before_closing_quotes() {` | `html_extraction_avoids_spaces_before_closing_quotes [function]` | `9607b55d-3e88-55cc-aeee-8c66cc0e88f9` | 330-337 [crates/gwiki/src/ingest/document/tests.rs:330-337] | Indexed function `html_extraction_avoids_spaces_before_closing_quotes` in `crates/gwiki/src/ingest/document/tests.rs`. [crates/gwiki/src/ingest/document/tests.rs:330-337] |
