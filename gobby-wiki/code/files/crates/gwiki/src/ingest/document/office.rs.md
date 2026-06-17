---
title: crates/gwiki/src/ingest/document/office.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/office.rs
  ranges:
  - 39-52
  - 54-56
  - 58-60
  - 62-64
  - 66-68
  - 70-81
  - 83-94
  - 96-109
  - 111-176
  - 178-262
  - 264-267
  - 269-309
  - 311-314
  - 316-393
  - 395-402
  - 404-414
  - 416-430
  - 432-450
  - 452-462
  - 464-469
  - 471-473
  - 475-479
  - 481-486
  - 493-502
  - 505-513
  - 516-521
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/document/office.rs:39-52](crates/gwiki/src/ingest/document/office.rs#L39-L52), [crates/gwiki/src/ingest/document/office.rs:54-56](crates/gwiki/src/ingest/document/office.rs#L54-L56), [crates/gwiki/src/ingest/document/office.rs:58-60](crates/gwiki/src/ingest/document/office.rs#L58-L60), [crates/gwiki/src/ingest/document/office.rs:62-64](crates/gwiki/src/ingest/document/office.rs#L62-L64), [crates/gwiki/src/ingest/document/office.rs:66-68](crates/gwiki/src/ingest/document/office.rs#L66-L68), [crates/gwiki/src/ingest/document/office.rs:70-81](crates/gwiki/src/ingest/document/office.rs#L70-L81), [crates/gwiki/src/ingest/document/office.rs:83-94](crates/gwiki/src/ingest/document/office.rs#L83-L94), [crates/gwiki/src/ingest/document/office.rs:96-109](crates/gwiki/src/ingest/document/office.rs#L96-L109), [crates/gwiki/src/ingest/document/office.rs:111-176](crates/gwiki/src/ingest/document/office.rs#L111-L176), [crates/gwiki/src/ingest/document/office.rs:178-262](crates/gwiki/src/ingest/document/office.rs#L178-L262), [crates/gwiki/src/ingest/document/office.rs:264-267](crates/gwiki/src/ingest/document/office.rs#L264-L267), [crates/gwiki/src/ingest/document/office.rs:269-309](crates/gwiki/src/ingest/document/office.rs#L269-L309), [crates/gwiki/src/ingest/document/office.rs:311-314](crates/gwiki/src/ingest/document/office.rs#L311-L314), [crates/gwiki/src/ingest/document/office.rs:316-393](crates/gwiki/src/ingest/document/office.rs#L316-L393), [crates/gwiki/src/ingest/document/office.rs:395-402](crates/gwiki/src/ingest/document/office.rs#L395-L402), [crates/gwiki/src/ingest/document/office.rs:404-414](crates/gwiki/src/ingest/document/office.rs#L404-L414), [crates/gwiki/src/ingest/document/office.rs:416-430](crates/gwiki/src/ingest/document/office.rs#L416-L430), [crates/gwiki/src/ingest/document/office.rs:432-450](crates/gwiki/src/ingest/document/office.rs#L432-L450), [crates/gwiki/src/ingest/document/office.rs:452-462](crates/gwiki/src/ingest/document/office.rs#L452-L462), [crates/gwiki/src/ingest/document/office.rs:464-469](crates/gwiki/src/ingest/document/office.rs#L464-L469), [crates/gwiki/src/ingest/document/office.rs:471-473](crates/gwiki/src/ingest/document/office.rs#L471-L473), [crates/gwiki/src/ingest/document/office.rs:475-479](crates/gwiki/src/ingest/document/office.rs#L475-L479), [crates/gwiki/src/ingest/document/office.rs:481-486](crates/gwiki/src/ingest/document/office.rs#L481-L486), [crates/gwiki/src/ingest/document/office.rs:493-502](crates/gwiki/src/ingest/document/office.rs#L493-L502), [crates/gwiki/src/ingest/document/office.rs:505-513](crates/gwiki/src/ingest/document/office.rs#L505-L513), [crates/gwiki/src/ingest/document/office.rs:516-521](crates/gwiki/src/ingest/document/office.rs#L516-L521)

</details>

# crates/gwiki/src/ingest/document/office.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements bounded extraction of Office documents into wiki text: `extract_office_document` dispatches by file extension to DOCX, PPTX, or spreadsheet handlers, while unsupported or missing extensions return document errors. The rest of the file provides the limits and helpers that make that extraction safe and consistent, including environment-configured caps for ZIP entry size, slide count, and spreadsheet row/column bounds, ZIP/XML readers, paragraph and table rendering helpers, and warning/degradation hooks for ignored or empty content.
[crates/gwiki/src/ingest/document/office.rs:39-52]
[crates/gwiki/src/ingest/document/office.rs:54-56]
[crates/gwiki/src/ingest/document/office.rs:58-60]
[crates/gwiki/src/ingest/document/office.rs:62-64]
[crates/gwiki/src/ingest/document/office.rs:66-68]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `extract_office_document` | function | `pub(crate) fn extract_office_document(` | `extract_office_document [function]` | `f6161534-7863-5f87-8c69-5e008789fad6` | 39-52 [crates/gwiki/src/ingest/document/office.rs:39-52] | Indexed function `extract_office_document` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:39-52] |
| `office_max_entry_bytes` | function | `fn office_max_entry_bytes() -> u64 {` | `office_max_entry_bytes [function]` | `a92d90b8-571c-5a73-b884-4921f7826f7e` | 54-56 [crates/gwiki/src/ingest/document/office.rs:54-56] | Indexed function `office_max_entry_bytes` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:54-56] |
| `office_max_slides` | function | `fn office_max_slides() -> usize {` | `office_max_slides [function]` | `e4bce69a-0c0c-536d-a55d-c34139798481` | 58-60 [crates/gwiki/src/ingest/document/office.rs:58-60] | Indexed function `office_max_slides` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:58-60] |
| `office_max_rows_per_sheet` | function | `fn office_max_rows_per_sheet() -> usize {` | `office_max_rows_per_sheet [function]` | `23189033-d651-57ed-a216-4419f035a28b` | 62-64 [crates/gwiki/src/ingest/document/office.rs:62-64] | Indexed function `office_max_rows_per_sheet` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:62-64] |
| `office_max_columns_per_sheet` | function | `fn office_max_columns_per_sheet() -> usize {` | `office_max_columns_per_sheet [function]` | `4d7b2039-b0d6-5a21-b380-c0c0621979da` | 66-68 [crates/gwiki/src/ingest/document/office.rs:66-68] | Indexed function `office_max_columns_per_sheet` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:66-68] |
| `office_env_u64` | function | `fn office_env_u64(name: &str, default: u64) -> u64 {` | `office_env_u64 [function]` | `7db65dba-79f9-59a6-a0e9-798b6630c6ca` | 70-81 [crates/gwiki/src/ingest/document/office.rs:70-81] | Indexed function `office_env_u64` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:70-81] |
| `office_env_usize` | function | `fn office_env_usize(name: &str, default: usize) -> usize {` | `office_env_usize [function]` | `f0f05d5f-7520-5f81-a290-39135561bbff` | 83-94 [crates/gwiki/src/ingest/document/office.rs:83-94] | Indexed function `office_env_usize` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:83-94] |
| `extract_docx` | function | `pub(crate) fn extract_docx(bytes: &[u8]) -> Result<DocumentExtraction, WikiError> {` | `extract_docx [function]` | `038959ea-6f68-51a7-b28d-9b857beca386` | 96-109 [crates/gwiki/src/ingest/document/office.rs:96-109] | Indexed function `extract_docx` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:96-109] |
| `extract_pptx` | function | `pub(crate) fn extract_pptx(bytes: &[u8]) -> Result<DocumentExtraction, WikiError> {` | `extract_pptx [function]` | `8d146c2e-c344-5b4e-84a1-f4ddd0d3aa53` | 111-176 [crates/gwiki/src/ingest/document/office.rs:111-176] | Indexed function `extract_pptx` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:111-176] |
| `extract_spreadsheet` | function | `fn extract_spreadsheet(bytes: &[u8]) -> Result<DocumentExtraction, WikiError> {` | `extract_spreadsheet [function]` | `b88b4196-0117-5f51-bf3a-f660e788f80b` | 178-262 [crates/gwiki/src/ingest/document/office.rs:178-262] | Indexed function `extract_spreadsheet` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:178-262] |
| `read_zip_entry` | function | `fn read_zip_entry(bytes: &[u8], name: &str) -> Result<String, WikiError> {` | `read_zip_entry [function]` | `9076381c-f935-5c44-bf48-257b15ba9c62` | 264-267 [crates/gwiki/src/ingest/document/office.rs:264-267] | Indexed function `read_zip_entry` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:264-267] |
| `read_zip_entry_from_archive` | function | `fn read_zip_entry_from_archive(` | `read_zip_entry_from_archive [function]` | `bfad9649-0ea9-533e-9a58-053bf3f73079` | 269-309 [crates/gwiki/src/ingest/document/office.rs:269-309] | Indexed function `read_zip_entry_from_archive` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:269-309] |
| `zip_archive` | function | `fn zip_archive(bytes: &[u8]) -> Result<ZipArchive<Cursor<&[u8]>>, WikiError> {` | `zip_archive [function]` | `07e625e6-677d-5f31-9ed1-6712de978c93` | 311-314 [crates/gwiki/src/ingest/document/office.rs:311-314] | Indexed function `zip_archive` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:311-314] |
| `extract_xml_paragraphs` | function | `fn extract_xml_paragraphs(xml: &str) -> Result<Vec<String>, WikiError> {` | `extract_xml_paragraphs [function]` | `67b04ae9-5316-58ad-8c9e-4345e12cef0e` | 316-393 [crates/gwiki/src/ingest/document/office.rs:316-393] | Indexed function `extract_xml_paragraphs` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:316-393] |
| `spreadsheet_row_text` | function | `fn spreadsheet_row_text(row: &[Data], max_columns: usize) -> Option<Vec<String>> {` | `spreadsheet_row_text [function]` | `0ed06427-e515-5a86-893e-a64f1bf21762` | 395-402 [crates/gwiki/src/ingest/document/office.rs:395-402] | Indexed function `spreadsheet_row_text` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:395-402] |
| `warn_ignored_office_text` | function | `fn warn_ignored_office_text(text: &[u8], in_paragraph: bool, saw_ignored_text: &mut bool) {` | `warn_ignored_office_text [function]` | `da78855e-7ec0-5777-967c-41b0fe4c08d8` | 404-414 [crates/gwiki/src/ingest/document/office.rs:404-414] | Indexed function `warn_ignored_office_text` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:404-414] |
| `warn_empty_office_paragraph` | function | `fn warn_empty_office_paragraph(` | `warn_empty_office_paragraph [function]` | `00bf0f7d-829e-5e70-b512-33f562274178` | 416-430 [crates/gwiki/src/ingest/document/office.rs:416-430] | Indexed function `warn_empty_office_paragraph` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:416-430] |
| `markdown_table` | function | `pub(crate) fn markdown_table(rows: &[Vec<String>]) -> String {` | `markdown_table [function]` | `a6eec892-8230-5d6d-8464-9ad0b5c4a6c2` | 432-450 [crates/gwiki/src/ingest/document/office.rs:432-450] | Indexed function `markdown_table` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:432-450] |
| `push_table_row` | function | `fn push_table_row(markdown: &mut String, row: &[String], column_count: usize) {` | `push_table_row [function]` | `691382bb-6d34-523f-a32d-a10173803043` | 452-462 [crates/gwiki/src/ingest/document/office.rs:452-462] | Indexed function `push_table_row` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:452-462] |
| `cell_text` | function | `fn cell_text(cell: &Data) -> String {` | `cell_text [function]` | `297606c0-f447-58e6-8d59-a0e15e64bfb5` | 464-469 [crates/gwiki/src/ingest/document/office.rs:464-469] | Indexed function `cell_text` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:464-469] |
| `escape_table_cell` | function | `fn escape_table_cell(cell: &str) -> String {` | `escape_table_cell [function]` | `43e62dc1-b43f-5abc-9862-0faa90f8c654` | 471-473 [crates/gwiki/src/ingest/document/office.rs:471-473] | Indexed function `escape_table_cell` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:471-473] |
| `local_name` | function | `fn local_name(name: &[u8]) -> &[u8] {` | `local_name [function]` | `fcee01ba-27b2-50fa-9897-5b5851c066da` | 475-479 [crates/gwiki/src/ingest/document/office.rs:475-479] | Indexed function `local_name` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:475-479] |
| `slide_number` | function | `fn slide_number(name: &str) -> Option<usize> {` | `slide_number [function]` | `6175e9c7-964d-5eb5-8086-34858c64ace1` | 481-486 [crates/gwiki/src/ingest/document/office.rs:481-486] | Indexed function `slide_number` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:481-486] |
| `spreadsheet_row_text_filters_fully_empty_rows` | function | `fn spreadsheet_row_text_filters_fully_empty_rows() {` | `spreadsheet_row_text_filters_fully_empty_rows [function]` | `0293eefa-ebf8-591f-8eff-365f417507da` | 493-502 [crates/gwiki/src/ingest/document/office.rs:493-502] | Indexed function `spreadsheet_row_text_filters_fully_empty_rows` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:493-502] |
| `markdown_table_filters_fully_empty_rows` | function | `fn markdown_table_filters_fully_empty_rows() {` | `markdown_table_filters_fully_empty_rows [function]` | `c3723350-1530-5862-a41e-3863a5f97947` | 505-513 [crates/gwiki/src/ingest/document/office.rs:505-513] | Indexed function `markdown_table_filters_fully_empty_rows` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:505-513] |
| `xml_paragraphs_ignore_text_outside_t_without_api_change` | function | `fn xml_paragraphs_ignore_text_outside_t_without_api_change() {` | `xml_paragraphs_ignore_text_outside_t_without_api_change [function]` | `2052c6f8-a3c6-5375-83a2-ed7b4eeb350f` | 516-521 [crates/gwiki/src/ingest/document/office.rs:516-521] | Indexed function `xml_paragraphs_ignore_text_outside_t_without_api_change` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:516-521] |
