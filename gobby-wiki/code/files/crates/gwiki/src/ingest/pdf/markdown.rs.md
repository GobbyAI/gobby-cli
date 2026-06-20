---
title: crates/gwiki/src/ingest/pdf/markdown.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/markdown.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/markdown.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/pdf/markdown.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/pdf/markdown.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_pdf_markdown` | function | The 'render_pdf_markdown' function serializes PDF document metadata, scope identification, and degradation reports into a Markdown metadata block, and appends the document title, degradation warnings, and individual page contents to produce a unified Markdown representation of the PDF. [crates/gwiki/src/ingest/pdf/markdown.rs:15-89] |
| `sanitize_pdf_page_markdown` | function | This function processes the input markdown string line-by-line to escape horizontal rules and neutralize gwiki page marker variants, returning the collected sanitized lines joined by newlines. [crates/gwiki/src/ingest/pdf/markdown.rs:92-107] |
| `neutralize_gwiki_page_marker_variants` | function | This function processes an input string slice to neutralize HTML comment markers ('<!--') that are followed by optional ASCII whitespace and the case-insensitive prefix "gwiki-page" by replacing the '<!--' sequence with '<! --' while preserving the original casing of the surrounding text. [crates/gwiki/src/ingest/pdf/markdown.rs:110-135] |
| `is_markdown_horizontal_rule` | function | This function determines whether a trimmed string represents a Markdown horizontal rule by verifying that it consists entirely of whitespace and at least three repetitions of a single, uniform character from the set ''-'', ''_'', or ''*''. [crates/gwiki/src/ingest/pdf/markdown.rs:138-156] |
| `merge_pdf_pages` | function | The 'merge_pdf_pages' function merges extracted text layers from a PDF snapshot with vision-extracted content from rendered pages using a specified vision endpoint to generate a vector of page-by-page markdown structures and a document markdown summary. [crates/gwiki/src/ingest/pdf/markdown.rs:159-239] |
| `extract_vision_for_page` | function | The function extracts vision data from a rendered PDF page by constructing a 'VisionRequest' from the page's snapshot, asset path, and rendering metadata, and then submitting it to an available 'VisionEndpoint' client, or returns 'Ok(None)' if the endpoint is unavailable. [crates/gwiki/src/ingest/pdf/markdown.rs:242-264] |
| `rendered_page_asset_path` | function | The function returns a 'PathBuf' by joining the parent directory of 'asset_path' with the specified 'file_name', falling back to a 'PathBuf' created from 'file_name' if no parent directory exists. [crates/gwiki/src/ingest/pdf/markdown.rs:267-272] |
| `merge_page_markdown` | function | This function normalizes a primary text layer, deduplicates and formats optional OCR text from a vision extraction, appends a formatted single-line visual description, and joins all non-empty sections with double newlines. [crates/gwiki/src/ingest/pdf/markdown.rs:275-295] |
| `dedupe_ocr_text` | function | The 'dedupe_ocr_text' function normalizes the input OCR text and filters out paragraphs whose overlap keys are already present within the PDF text layer's overlap key, returning the retained paragraphs joined by double newlines, or 'None' if no unique content remains. [crates/gwiki/src/ingest/pdf/markdown.rs:298-319] |
| `overlap_key` | function | The 'overlap_key' function normalizes a string slice to a single line, filters out all whitespace, converts the remaining characters to lowercase, and collects them into a new 'String'. [crates/gwiki/src/ingest/pdf/markdown.rs:322-328] |
| `vision_model` | function | The 'vision_model' function searches the metadata of the provided 'VisionExtraction' reference and returns the first non-empty value corresponding to the key 'model' as an 'Option<&str>'. [crates/gwiki/src/ingest/pdf/markdown.rs:331-335] |
| `rendered_page_file_name` | function | The 'rendered_page_file_name' function extracts the base stem of a given file path (falling back to the input string if extraction fails) and formats it with a specified page number to generate a PNG filename string in the format '{stem}-page-{page_number}.png'. [crates/gwiki/src/ingest/pdf/markdown.rs:338-344] |

_Verified by 2 in-file unit tests._

