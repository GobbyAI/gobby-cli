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

# crates/gwiki/src/ingest/document/office.rs

Module: [[code/modules/crates/gwiki/src/ingest/document|crates/gwiki/src/ingest/document]]

## Purpose

This file implements office-document ingestion and bounded extraction for `.docx`, `.pptx`, `.xlsx`, `.xls`, and `.ods` inputs. The top-level dispatcher routes by file extension, while helpers load ZIP entries, parse XML paragraphs, and convert spreadsheet rows into Markdown tables. It also centralizes configurable size/shape limits through environment-backed accessors, emits warnings when text is ignored or content is empty, and reports truncation or unsupported formats as `WikiError`s.
[crates/gwiki/src/ingest/document/office.rs:39-52]
[crates/gwiki/src/ingest/document/office.rs:54-56]
[crates/gwiki/src/ingest/document/office.rs:58-60]
[crates/gwiki/src/ingest/document/office.rs:62-64]
[crates/gwiki/src/ingest/document/office.rs:66-68]

## API Symbols

- `extract_office_document` (function) component `extract_office_document [function]` (`f6161534-7863-5f87-8c69-5e008789fad6`) lines 39-52 [crates/gwiki/src/ingest/document/office.rs:39-52]
  - Signature: `pub(crate) fn extract_office_document(`
  - Purpose: Dispatches office-document extraction by file extension, routing 'docx' to 'extract_docx', 'pptx' to 'extract_pptx', spreadsheet formats ('xlsx', 'xls', 'ods') to 'extract_spreadsheet', and returning a 'WikiError' for missing or unsupported extensions. [crates/gwiki/src/ingest/document/office.rs:39-52]
- `office_max_entry_bytes` (function) component `office_max_entry_bytes [function]` (`a92d90b8-571c-5a73-b884-4921f7826f7e`) lines 54-56 [crates/gwiki/src/ingest/document/office.rs:54-56]
  - Signature: `fn office_max_entry_bytes() -> u64 {`
  - Purpose: Returns the 'u64' value referenced by 'OFFICE_MAX_ENTRY_BYTES', exposing the configured maximum office entry size in bytes. [crates/gwiki/src/ingest/document/office.rs:54-56]
- `office_max_slides` (function) component `office_max_slides [function]` (`e4bce69a-0c0c-536d-a55d-c34139798481`) lines 58-60 [crates/gwiki/src/ingest/document/office.rs:58-60]
  - Signature: `fn office_max_slides() -> usize {`
  - Purpose: Returns the current maximum number of office slides by dereferencing the 'OFFICE_MAX_SLIDES' static and yielding it as a 'usize'. [crates/gwiki/src/ingest/document/office.rs:58-60]
- `office_max_rows_per_sheet` (function) component `office_max_rows_per_sheet [function]` (`23189033-d651-57ed-a216-4419f035a28b`) lines 62-64 [crates/gwiki/src/ingest/document/office.rs:62-64]
  - Signature: `fn office_max_rows_per_sheet() -> usize {`
  - Purpose: Returns the dereferenced value of 'OFFICE_MAX_ROWS_PER_SHEET' as the maximum number of rows allowed per office sheet. [crates/gwiki/src/ingest/document/office.rs:62-64]
- `office_max_columns_per_sheet` (function) component `office_max_columns_per_sheet [function]` (`4d7b2039-b0d6-5a21-b380-c0c0621979da`) lines 66-68 [crates/gwiki/src/ingest/document/office.rs:66-68]
  - Signature: `fn office_max_columns_per_sheet() -> usize {`
  - Purpose: Returns the configured maximum number of columns allowed per office spreadsheet sheet by dereferencing the 'OFFICE_MAX_COLUMNS_PER_SHEET' constant. [crates/gwiki/src/ingest/document/office.rs:66-68]
- `office_env_u64` (function) component `office_env_u64 [function]` (`7db65dba-79f9-59a6-a0e9-798b6630c6ca`) lines 70-81 [crates/gwiki/src/ingest/document/office.rs:70-81]
  - Signature: `fn office_env_u64(name: &str, default: u64) -> u64 {`
  - Purpose: Returns a positive 'u64' parsed from the named environment variable after trimming whitespace, or logs a warning and falls back to 'default' if the variable is missing, non-numeric, zero, or invalid. [crates/gwiki/src/ingest/document/office.rs:70-81]
- `office_env_usize` (function) component `office_env_usize [function]` (`f0f05d5f-7520-5f81-a290-39135561bbff`) lines 83-94 [crates/gwiki/src/ingest/document/office.rs:83-94]
  - Signature: `fn office_env_usize(name: &str, default: usize) -> usize {`
  - Purpose: Reads the named environment variable, returns its trimmed positive 'usize' value if parsing succeeds, and otherwise logs a warning and falls back to 'default'. [crates/gwiki/src/ingest/document/office.rs:83-94]
- `extract_docx` (function) component `extract_docx [function]` (`038959ea-6f68-51a7-b28d-9b857beca386`) lines 96-109 [crates/gwiki/src/ingest/document/office.rs:96-109]
  - Signature: `pub(crate) fn extract_docx(bytes: &[u8]) -> Result<DocumentExtraction, WikiError> {`
  - Purpose: 'extract_docx' reads 'word/document.xml' from a DOCX ZIP payload, extracts XML paragraphs, errors if none are found, and returns a 'DocumentExtraction' whose title is the first paragraph and whose markdown is the paragraphs joined by blank lines with 'paragraph_count' metadata. [crates/gwiki/src/ingest/document/office.rs:96-109]
- `extract_pptx` (function) component `extract_pptx [function]` (`8d146c2e-c344-5b4e-84a1-f4ddd0d3aa53`) lines 111-176 [crates/gwiki/src/ingest/document/office.rs:111-176]
  - Signature: `pub(crate) fn extract_pptx(bytes: &[u8]) -> Result<DocumentExtraction, WikiError> {`
  - Purpose: Parses a PPTX ZIP archive, orders 'ppt/slides/slide*.xml' files by slide number, extracts non-empty paragraph text into markdown with per-slide headings while capturing the first slide’s first paragraph as the title, truncates to 'office_max_slides()' with a bounded-extraction degradation note, and errors if the archive has no slides or no extractable text. [crates/gwiki/src/ingest/document/office.rs:111-176]
- `extract_spreadsheet` (function) component `extract_spreadsheet [function]` (`b88b4196-0117-5f51-bf3a-f660e788f80b`) lines 178-262 [crates/gwiki/src/ingest/document/office.rs:178-262]
  - Signature: `fn extract_spreadsheet(bytes: &[u8]) -> Result<DocumentExtraction, WikiError> {`
  - Purpose: Parses the input bytes as a spreadsheet, rejects workbooks with no sheets, renders up to 'MAX_SHEETS' non-empty sheets into Markdown tables while enforcing per-sheet row and column limits, and returns a 'DocumentExtraction' with truncation flagged when limits are exceeded. [crates/gwiki/src/ingest/document/office.rs:178-262]
- `read_zip_entry` (function) component `read_zip_entry [function]` (`9076381c-f935-5c44-bf48-257b15ba9c62`) lines 264-267 [crates/gwiki/src/ingest/document/office.rs:264-267]
  - Signature: `fn read_zip_entry(bytes: &[u8], name: &str) -> Result<String, WikiError> {`
  - Purpose: Parses the provided ZIP bytes into an archive and returns the specified entry as a 'String' via 'read_zip_entry_from_archive', propagating any 'WikiError' from archive creation or entry reading. [crates/gwiki/src/ingest/document/office.rs:264-267]
- `read_zip_entry_from_archive` (function) component `read_zip_entry_from_archive [function]` (`bfad9649-0ea9-533e-9a58-053bf3f73079`) lines 269-309 [crates/gwiki/src/ingest/document/office.rs:269-309]
  - Signature: `fn read_zip_entry_from_archive(`
  - Purpose: Opens a named ZIP archive entry, enforces a maximum entry size while streaming it in chunks, and returns its UTF-8 contents as a 'String' or a wrapped 'WikiError' on lookup, I/O, size-limit, or decode failure. [crates/gwiki/src/ingest/document/office.rs:269-309]
- `zip_archive` (function) component `zip_archive [function]` (`07e625e6-677d-5f31-9ed1-6712de978c93`) lines 311-314 [crates/gwiki/src/ingest/document/office.rs:311-314]
  - Signature: `fn zip_archive(bytes: &[u8]) -> Result<ZipArchive<Cursor<&[u8]>>, WikiError> {`
  - Purpose: Creates a 'ZipArchive' over an in-memory byte slice by wrapping it in 'Cursor' and converting any ZIP-open failure into a 'WikiError' labeled 'open zip: ...'. [crates/gwiki/src/ingest/document/office.rs:311-314]
- `extract_xml_paragraphs` (function) component `extract_xml_paragraphs [function]` (`67b04ae9-5316-58ad-8c9e-4345e12cef0e`) lines 316-393 [crates/gwiki/src/ingest/document/office.rs:316-393]
  - Signature: `fn extract_xml_paragraphs(xml: &str) -> Result<Vec<String>, WikiError> {`
  - Purpose: Streams the XML and returns a 'Vec<String>' of non-empty paragraph texts by collecting '<t>' content inside each '<p>', decoding XML entities, normalizing each paragraph to a single line, and warning when an Office paragraph is empty. [crates/gwiki/src/ingest/document/office.rs:316-393]
- `spreadsheet_row_text` (function) component `spreadsheet_row_text [function]` (`0ed06427-e515-5a86-893e-a64f1bf21762`) lines 395-402 [crates/gwiki/src/ingest/document/office.rs:395-402]
  - Signature: `fn spreadsheet_row_text(row: &[Data], max_columns: usize) -> Option<Vec<String>> {`
  - Purpose: Builds a 'Vec<String>' of text for up to 'max_columns' cells in 'row' using 'cell_text', and returns it only if at least one resulting cell string is non-empty, otherwise 'None'. [crates/gwiki/src/ingest/document/office.rs:395-402]
- `warn_ignored_office_text` (function) component `warn_ignored_office_text [function]` (`da78855e-7ec0-5777-967c-41b0fe4c08d8`) lines 404-414 [crates/gwiki/src/ingest/document/office.rs:404-414]
  - Signature: `fn warn_ignored_office_text(text: &[u8], in_paragraph: bool, saw_ignored_text: &mut bool) {`
  - Purpose: If currently inside a paragraph and the byte slice decodes to a non-empty single-line string, it marks 'saw_ignored_text' true and emits a warning that office XML paragraph text outside a '<t>' element was ignored. [crates/gwiki/src/ingest/document/office.rs:404-414]
- `warn_empty_office_paragraph` (function) component `warn_empty_office_paragraph [function]` (`00bf0f7d-829e-5e70-b512-33f562274178`) lines 416-430 [crates/gwiki/src/ingest/document/office.rs:416-430]
  - Signature: `fn warn_empty_office_paragraph(`
  - Purpose: Logs a warning describing why an Office XML paragraph yielded no usable text, choosing among ignored text, empty after extraction, no recognized text runs, or fully empty based on the provided boolean flags. [crates/gwiki/src/ingest/document/office.rs:416-430]
- `markdown_table` (function) component `markdown_table [function]` (`a6eec892-8230-5d6d-8464-9ad0b5c4a6c2`) lines 432-450 [crates/gwiki/src/ingest/document/office.rs:432-450]
  - Signature: `pub(crate) fn markdown_table(rows: &[Vec<String>]) -> String {`
  - Purpose: Builds a Markdown table string from non-empty rows by using the first row as the header, emitting a separator row, padding to the maximum column count via 'push_table_row', and returning an empty string when no nonblank rows remain. [crates/gwiki/src/ingest/document/office.rs:432-450]
- `push_table_row` (function) component `push_table_row [function]` (`691382bb-6d34-523f-a32d-a10173803043`) lines 452-462 [crates/gwiki/src/ingest/document/office.rs:452-462]
  - Signature: `fn push_table_row(markdown: &mut String, row: &[String], column_count: usize) {`
  - Purpose: Appends a Markdown table row to 'markdown' by writing a leading '|', then 'column_count' cells separated by ' |' with each present 'row' entry escaped via 'escape_table_cell' and missing cells left empty, followed by a trailing newline. [crates/gwiki/src/ingest/document/office.rs:452-462]
- `cell_text` (function) component `cell_text [function]` (`297606c0-f447-58e6-8d59-a0e15e64bfb5`) lines 464-469 [crates/gwiki/src/ingest/document/office.rs:464-469]
  - Signature: `fn cell_text(cell: &Data) -> String {`
  - Purpose: Returns an empty 'String' for 'Data::Empty', otherwise converts the cell to a string and normalizes it to a single line with 'single_line'. [crates/gwiki/src/ingest/document/office.rs:464-469]
- `escape_table_cell` (function) component `escape_table_cell [function]` (`43e62dc1-b43f-5abc-9862-0faa90f8c654`) lines 471-473 [crates/gwiki/src/ingest/document/office.rs:471-473]
  - Signature: `fn escape_table_cell(cell: &str) -> String {`
  - Purpose: Returns a single-line version of 'cell' with every '|' character escaped as '\|' for safe table-cell rendering. [crates/gwiki/src/ingest/document/office.rs:471-473]
- `local_name` (function) component `local_name [function]` (`fcee01ba-27b2-50fa-9897-5b5851c066da`) lines 475-479 [crates/gwiki/src/ingest/document/office.rs:475-479]
  - Signature: `fn local_name(name: &[u8]) -> &[u8] {`
  - Purpose: Returns the input byte slice unchanged if it contains no ':' byte, otherwise returns the subslice after the first ':' character. [crates/gwiki/src/ingest/document/office.rs:475-479]
- `slide_number` (function) component `slide_number [function]` (`6175e9c7-964d-5eb5-8086-34858c64ace1`) lines 481-486 [crates/gwiki/src/ingest/document/office.rs:481-486]
  - Signature: `fn slide_number(name: &str) -> Option<usize> {`
  - Purpose: Returns the slide index parsed from a PPT slide XML path by stripping the 'ppt/slides/slide' prefix and '.xml' suffix, then converting the remaining digits to 'usize', or 'None' if any step fails. [crates/gwiki/src/ingest/document/office.rs:481-486]
- `spreadsheet_row_text_filters_fully_empty_rows` (function) component `spreadsheet_row_text_filters_fully_empty_rows [function]` (`0293eefa-ebf8-591f-8eff-365f417507da`) lines 493-502 [crates/gwiki/src/ingest/document/office.rs:493-502]
  - Signature: `fn spreadsheet_row_text_filters_fully_empty_rows() {`
  - Purpose: Verifies that 'spreadsheet_row_text' returns 'None' for a row containing only empty/whitespace cells, but returns a vector with preserved empty-string placeholders and non-empty text for a partially populated row. [crates/gwiki/src/ingest/document/office.rs:493-502]
- `markdown_table_filters_fully_empty_rows` (function) component `markdown_table_filters_fully_empty_rows [function]` (`c3723350-1530-5862-a41e-3863a5f97947`) lines 505-513 [crates/gwiki/src/ingest/document/office.rs:505-513]
  - Signature: `fn markdown_table_filters_fully_empty_rows() {`
  - Purpose: Verifies that 'markdown_table' omits rows whose cells are all empty or whitespace-only, producing a table that includes only the header and non-empty data rows. [crates/gwiki/src/ingest/document/office.rs:505-513]
- `xml_paragraphs_ignore_text_outside_t_without_api_change` (function) component `xml_paragraphs_ignore_text_outside_t_without_api_change [function]` (`2052c6f8-a3c6-5375-83a2-ed7b4eeb350f`) lines 516-521 [crates/gwiki/src/ingest/document/office.rs:516-521]
  - Signature: `fn xml_paragraphs_ignore_text_outside_t_without_api_change() {`
  - Purpose: Verifies that 'extract_xml_paragraphs' returns only text contained in '<w:t>' elements, ignoring surrounding non-'w:t' text within the same paragraph without changing the API. [crates/gwiki/src/ingest/document/office.rs:516-521]

