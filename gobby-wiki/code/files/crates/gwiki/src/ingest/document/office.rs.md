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

`crates/gwiki/src/ingest/document/office.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `extract_office_document` | function | Indexed function `extract_office_document` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:39-52] |
| `office_max_entry_bytes` | function | Indexed function `office_max_entry_bytes` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:54-56] |
| `office_max_slides` | function | Indexed function `office_max_slides` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:58-60] |
| `office_max_rows_per_sheet` | function | Indexed function `office_max_rows_per_sheet` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:62-64] |
| `office_max_columns_per_sheet` | function | Indexed function `office_max_columns_per_sheet` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:66-68] |
| `office_env_u64` | function | Indexed function `office_env_u64` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:70-81] |
| `office_env_usize` | function | Indexed function `office_env_usize` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:83-94] |
| `extract_docx` | function | Indexed function `extract_docx` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:96-109] |
| `extract_pptx` | function | Indexed function `extract_pptx` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:111-176] |
| `extract_spreadsheet` | function | Indexed function `extract_spreadsheet` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:178-262] |
| `read_zip_entry` | function | Indexed function `read_zip_entry` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:264-267] |
| `read_zip_entry_from_archive` | function | Indexed function `read_zip_entry_from_archive` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:269-309] |
| `zip_archive` | function | Indexed function `zip_archive` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:311-314] |
| `extract_xml_paragraphs` | function | Indexed function `extract_xml_paragraphs` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:316-393] |
| `spreadsheet_row_text` | function | Indexed function `spreadsheet_row_text` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:395-402] |
| `warn_ignored_office_text` | function | Indexed function `warn_ignored_office_text` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:404-414] |
| `warn_empty_office_paragraph` | function | Indexed function `warn_empty_office_paragraph` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:416-430] |
| `markdown_table` | function | Indexed function `markdown_table` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:432-450] |
| `push_table_row` | function | Indexed function `push_table_row` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:452-462] |
| `cell_text` | function | Indexed function `cell_text` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:464-469] |
| `escape_table_cell` | function | Indexed function `escape_table_cell` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:471-473] |
| `local_name` | function | Indexed function `local_name` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:475-479] |
| `slide_number` | function | Indexed function `slide_number` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:481-486] |
| `spreadsheet_row_text_filters_fully_empty_rows` | function | Indexed function `spreadsheet_row_text_filters_fully_empty_rows` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:493-502] |
| `markdown_table_filters_fully_empty_rows` | function | Indexed function `markdown_table_filters_fully_empty_rows` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:505-513] |
| `xml_paragraphs_ignore_text_outside_t_without_api_change` | function | Indexed function `xml_paragraphs_ignore_text_outside_t_without_api_change` in `crates/gwiki/src/ingest/document/office.rs`. [crates/gwiki/src/ingest/document/office.rs:516-521] |

