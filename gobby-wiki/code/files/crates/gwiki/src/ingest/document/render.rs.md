---
title: crates/gwiki/src/ingest/document/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/document/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/document/render.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/document/render.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_raw_document_markdown` | function | Builds a Markdown string by prepending metadata for the document’s kind, location, fetch time, source hash, and asset path, then adds an H1 title derived from 'snapshot.file_name' and a note stating the original document is stored at the given asset path. [crates/gwiki/src/ingest/document/render.rs:11-33] |
| `write_document_derived_markdown` | function | Builds the derived-markdown file path for a source record under 'vault_root', ensures its parent directory exists, renders and normalizes document-derived Markdown from the provided snapshot/extraction/degradation context, writes it atomically to disk, and returns the relative output path. [crates/gwiki/src/ingest/document/render.rs:36-67] |
| `write_document_markdown_atomic` | function | Writes 'contents' to 'path' atomically by creating a temporary file in the target location, writing and 'sync_all'-ing the bytes, persisting the temp file over 'path', and then syncing the parent directory, returning 'WikiError::Io' on any I/O failure. [crates/gwiki/src/ingest/document/render.rs:69-93] |
| `create_document_temp_file` | function | Creates a temporary file in 'path'’s non-empty parent directory using a '.{file_name}.' prefix and '.tmp' suffix, or returns a 'WikiError::Io' if the path has no valid parent or temp-file creation fails. [crates/gwiki/src/ingest/document/render.rs:95-122] |
| `render_document_derived_markdown` | function | Constructs a markdown document string by collecting document, source, scope, extraction, and degradation metadata into front matter via 'markdown_metadata', then appending an H1 title heading. [crates/gwiki/src/ingest/document/render.rs:124-211] |
| `document_degradation_for_error` | function | Maps a 'DocumentRequest' parse failure into a 'DocumentDegradation' by selecting a 'DocumentFailureMode' from 'request.kind', computing the affected unit count from the file name and kind, and emitting a message that parsing failed while preserving the original asset. [crates/gwiki/src/ingest/document/render.rs:213-228] |
| `document_unit_count_for_failure` | function | 'document_unit_count_for_failure' returns a zero-count 'DocumentUnitCount' matching the source’s unit type on failure, except HTML which defaults to 'pages(1)', PDF to 'pages(0)', and Office files to 'slides(0)' for '.pptx', 'sheets(0)' for spreadsheet extensions, or 'pages(0)' otherwise. [crates/gwiki/src/ingest/document/render.rs:230-241] |
| `document_degradation_maps_pdf_failure_to_pdf_mode` | function | Verifies that 'document_degradation_for_error' maps a 'SourceKind::Pdf' request with missing text to a degradation reason of 'pdf_text_layer_error' and a unit count keyed by 'page_count'. [crates/gwiki/src/ingest/document/render.rs:248-260] |
| `document_degradation_uses_unsupported_source_for_non_documents` | function | Verifies that 'document_degradation_for_error' returns a degradation whose reason is '"unsupported_source"' when given a non-document 'DocumentRequest' with 'SourceKind::Text'. [crates/gwiki/src/ingest/document/render.rs:263-274] |

