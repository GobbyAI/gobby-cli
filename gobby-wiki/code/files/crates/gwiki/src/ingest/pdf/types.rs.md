---
title: crates/gwiki/src/ingest/pdf/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/types.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/pdf/types.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/pdf/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `PdfPage` | class | The 'PdfPage' struct represents a single page of a PDF document, containing its page number as a 'usize' and its extracted textual content as a 'String'. [crates/gwiki/src/ingest/pdf/types.rs:11-14] |
| `PdfSnapshot` | class | The 'PdfSnapshot' struct represents a retrieved PDF file, capturing metadata including its location, file name, and UTC fetch timestamp, alongside the raw document bytes and a collection of its parsed pages. [crates/gwiki/src/ingest/pdf/types.rs:18-24] |
| `PdfFileSnapshot` | class | The 'PdfFileSnapshot' struct represents a self-contained snapshot of a PDF file, capturing its location, file name, UTC fetch timestamp, and raw binary content as a byte vector. [crates/gwiki/src/ingest/pdf/types.rs:28-33] |
| `PdfRenderedPage` | class | The 'PdfRenderedPage' struct represents a single rendered page of a PDF document, containing its page number, raw image data bytes, associated MIME type, and optional width and height dimensions. [crates/gwiki/src/ingest/pdf/types.rs:37-43] |
| `PdfIngestOptions` | class | 'PdfIngestOptions' is a public Rust structure containing a single 'render_dpi' field of type 'u16' that specifies the target resolution in dots per inch for rendering PDF pages during ingestion. [crates/gwiki/src/ingest/pdf/types.rs:47-49] |
| `PdfIngestOptions::default` | method | The 'default' method instantiates and returns an instance of 'Self' with its 'render_dpi' field initialized to 'DEFAULT_PDF_RENDER_DPI'. [crates/gwiki/src/ingest/pdf/types.rs:52-56] |
| `pdf_fetched_at` | function | The 'pdf_fetched_at' function parses a trimmed string slice into a UTC 'DateTime', supporting both a millisecond Unix epoch timestamp prefixed with "unix-ms:" and an RFC 3339 formatted string, returning a 'WikiError' if the input is invalid or out of range. [crates/gwiki/src/ingest/pdf/types.rs:60-81] |

