---
title: crates/gwiki/src/ingest/document/office.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/office.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/document/office.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/document/office.rs` exposes 26 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/document/office.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `extract_office_document` | function | The 'extract_office_document' function parses the extension of a given file name to delegate the extraction of office document bytes to format-specific parser functions, returning either a 'DocumentExtraction' or a 'WikiError'. [crates/gwiki/src/ingest/document/office.rs:39-52] |
| `office_max_entry_bytes` | function | The 'office_max_entry_bytes' function returns the dereferenced value of the 'OFFICE_MAX_ENTRY_BYTES' global static or constant as a 64-bit unsigned integer. [crates/gwiki/src/ingest/document/office.rs:54-56] |
| `office_max_slides` | function | The 'office_max_slides' function dereferences and returns the value of the static 'OFFICE_MAX_SLIDES' variable as a 'usize'. [crates/gwiki/src/ingest/document/office.rs:58-60] |
| `office_max_rows_per_sheet` | function | The 'office_max_rows_per_sheet' function returns the dereferenced value of the 'OFFICE_MAX_ROWS_PER_SHEET' static variable as a 'usize', representing the maximum number of rows allowed per sheet. [crates/gwiki/src/ingest/document/office.rs:62-64] |
| `office_max_columns_per_sheet` | function | The 'office_max_columns_per_sheet' function returns the maximum number of columns permitted per sheet as a 'usize' value by dereferencing the static reference 'OFFICE_MAX_COLUMNS_PER_SHEET'. [crates/gwiki/src/ingest/document/office.rs:66-68] |
| `office_env_u64` | function | The function retrieves the environment variable specified by 'name', returning its trimmed value parsed as a strictly positive 'u64', or logs a warning and returns the provided 'default' if the variable is unset, fails to parse, or evaluates to zero. [crates/gwiki/src/ingest/document/office.rs:70-81] |
| `office_env_usize` | function | The 'office_env_usize' function retrieves a specified environment variable, parses its trimmed value as a non-zero 'usize', and returns either this successfully parsed value or the provided 'default' value (logging a warning if parsing fails or the parsed value is zero). [crates/gwiki/src/ingest/document/office.rs:83-94] |
| `extract_docx` | function | The 'extract_docx' function extracts and parses paragraph text from the 'word/document.xml' entry inside a DOCX zip byte slice, returning a 'DocumentExtraction' struct containing the first paragraph as the title, the paragraphs joined by double-newlines as markdown, and the paragraph count, or a 'WikiError' if no paragraphs are found. [crates/gwiki/src/ingest/document/office.rs:96-109] |
| `extract_pptx` | function | This function extracts text paragraphs from the XML slide files of a zipped PPTX document byte slice, formats them sequentially into a Markdown representation up to a configurable maximum slide count, and returns the resulting document extraction structure or a wiki error. [crates/gwiki/src/ingest/document/office.rs:111-176] |
| `extract_spreadsheet` | function | The 'extract_spreadsheet' function parses raw spreadsheet bytes, extracts sheet and cell data within configured limits, and formats the content into Markdown tables returned as a 'DocumentExtraction' struct. [crates/gwiki/src/ingest/document/office.rs:178-262] |
| `read_zip_entry` | function | The 'read_zip_entry' function parses a ZIP archive from a byte slice and retrieves the string content of a specified entry by its name, returning a 'Result' containing either the content or a 'WikiError'. [crates/gwiki/src/ingest/document/office.rs:264-267] |
| `read_zip_entry_from_archive` | function | This function retrieves a named entry from a ZIP archive, validates its size against a configured maximum limit before and during a chunked read process, and decodes its contents into a UTF-8 string, returning a 'WikiError' upon any failure. [crates/gwiki/src/ingest/document/office.rs:269-309] |
| `zip_archive` | function | The 'zip_archive' function wraps a byte slice in an in-memory 'Cursor' to construct and return a 'ZipArchive', mapping any zip format initialization errors to a 'WikiError'. [crates/gwiki/src/ingest/document/office.rs:311-314] |
| `extract_xml_paragraphs` | function | The 'extract_xml_paragraphs' function parses an XML input string using a streaming reader to extract and decode the text content of paragraph ('<p>') elements, returning a collection of non-empty, single-line strings while tracking element state to issue warnings for empty paragraphs. [crates/gwiki/src/ingest/document/office.rs:316-393] |
| `spreadsheet_row_text` | function | The function converts up to 'max_columns' cells from a 'Data' slice into a vector of string representations using 'cell_text' and returns 'Some' of that vector if it contains at least one non-empty string, otherwise returning 'None'. [crates/gwiki/src/ingest/document/office.rs:395-402] |
| `warn_ignored_office_text` | function | This function sets the 'saw_ignored_text' flag to true and logs a warning if a non-empty, lossily-decoded UTF-8 byte slice is encountered while inside an XML paragraph. [crates/gwiki/src/ingest/document/office.rs:404-414] |
| `warn_empty_office_paragraph` | function | This function logs a warning describing the specific structural anomaly or reason for emptiness in an office XML paragraph based on boolean flags indicating the presence of ignored text, recognized text elements, or unknown XML. [crates/gwiki/src/ingest/document/office.rs:416-430] |
| `markdown_table` | function | The 'markdown_table' function filters out completely empty rows from a slice of string vectors and formats the remaining rows into a Markdown table string consisting of a header, a separator line, and data rows sized to the maximum column count. [crates/gwiki/src/ingest/document/office.rs:432-450] |
| `push_table_row` | function | The 'push_table_row' function appends a formatted Markdown table row to a mutable string buffer by escaping and formatting up to 'column_count' cell values from a string slice, terminating the row with a newline character. [crates/gwiki/src/ingest/document/office.rs:452-462] |
| `cell_text` | function | The 'cell_text' function returns an empty 'String' if the provided 'Data' reference is 'Data::Empty', and otherwise converts the data to a string representation and formats it as a single line using the 'single_line' function. [crates/gwiki/src/ingest/document/office.rs:464-469] |
| `escape_table_cell` | function | The 'escape_table_cell' function formats a string slice into a single line and escapes pipe characters ('\|') by replacing them with backslash-escaped pipes ('\\|'). [crates/gwiki/src/ingest/document/office.rs:471-473] |
| `local_name` | function | The 'local_name' function takes a byte slice and returns the subslice starting immediately after the first colon byte ('b':''), or the original byte slice if no colon is found. [crates/gwiki/src/ingest/document/office.rs:475-479] |
| `slide_number` | function | This function parses and returns a slide number as a 'usize' wrapped in an 'Option' from a PowerPoint slide XML file path by stripping the '"ppt/slides/slide"' prefix and the '".xml"' suffix. [crates/gwiki/src/ingest/document/office.rs:481-486] |

_Verified by 3 in-file unit tests._

