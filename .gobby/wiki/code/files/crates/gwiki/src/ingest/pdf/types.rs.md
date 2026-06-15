---
title: crates/gwiki/src/ingest/pdf/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/types.rs
  ranges:
  - 11-14
  - 18-24
  - 28-33
  - 37-43
  - 47-49
  - 51-57
  - 60-81
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/types.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

Defines the PDF ingest types used by gwiki: `PdfPage` holds per-page text, `PdfSnapshot` and `PdfFileSnapshot` capture fetched PDF metadata plus raw bytes, `PdfRenderedPage` stores rendered page images, and `PdfIngestOptions` configures rasterization via `render_dpi` with a default of `DEFAULT_PDF_RENDER_DPI`. The helper `pdf_fetched_at` normalizes configured fetch timestamps, accepting either `unix-ms:<i64>` or RFC3339 and converting them to `DateTime<Utc>`, returning a config error on invalid or out-of-range input.
[crates/gwiki/src/ingest/pdf/types.rs:11-14]
[crates/gwiki/src/ingest/pdf/types.rs:18-24]
[crates/gwiki/src/ingest/pdf/types.rs:28-33]
[crates/gwiki/src/ingest/pdf/types.rs:37-43]
[crates/gwiki/src/ingest/pdf/types.rs:47-49]

## API Symbols

- `PdfPage` (class) component `PdfPage [class]` (`06e7b5af-6295-5454-9a0c-135ef30fb656`) lines 11-14 [crates/gwiki/src/ingest/pdf/types.rs:11-14]
  - Signature: `pub struct PdfPage {`
  - Purpose: 'PdfPage' is a simple value type representing a PDF page by its zero-based 'number' and extracted 'text' content. [crates/gwiki/src/ingest/pdf/types.rs:11-14]
- `PdfSnapshot` (class) component `PdfSnapshot [class]` (`119c895c-c437-5ba5-bff3-6ae273577bcd`) lines 18-24 [crates/gwiki/src/ingest/pdf/types.rs:18-24]
  - Signature: `pub struct PdfSnapshot {`
  - Purpose: 'PdfSnapshot' is a data structure that captures a fetched PDF artifact’s source location, filename, retrieval timestamp, raw byte content, and parsed page list. [crates/gwiki/src/ingest/pdf/types.rs:18-24]
- `PdfFileSnapshot` (class) component `PdfFileSnapshot [class]` (`ba06730f-3be5-5ca5-a1d2-59c0ff9bebdf`) lines 28-33 [crates/gwiki/src/ingest/pdf/types.rs:28-33]
  - Signature: `pub struct PdfFileSnapshot {`
  - Purpose: 'PdfFileSnapshot' is a data container holding a PDF’s source location, file name, fetch timestamp ('DateTime<Utc>'), and raw file bytes ('Vec<u8>'). [crates/gwiki/src/ingest/pdf/types.rs:28-33]
- `PdfRenderedPage` (class) component `PdfRenderedPage [class]` (`b17a4ad9-249b-56c7-886d-2facf08acb1d`) lines 37-43 [crates/gwiki/src/ingest/pdf/types.rs:37-43]
  - Signature: `pub struct PdfRenderedPage {`
  - Purpose: 'PdfRenderedPage' is a PDF page render artifact that stores the page index, rendered image bytes, MIME type, and optional pixel dimensions. [crates/gwiki/src/ingest/pdf/types.rs:37-43]
- `PdfIngestOptions` (class) component `PdfIngestOptions [class]` (`04751078-7613-5241-bda8-4cb2d1b12860`) lines 47-49 [crates/gwiki/src/ingest/pdf/types.rs:47-49]
  - Signature: `pub struct PdfIngestOptions {`
  - Purpose: 'PdfIngestOptions' is a Rust configuration struct for PDF ingestion that currently contains a single 'u16' field, 'render_dpi', which specifies the render resolution in dots per inch. [crates/gwiki/src/ingest/pdf/types.rs:47-49]
- `PdfIngestOptions` (class) component `PdfIngestOptions [class]` (`24c2cdf2-a477-5b38-919c-f7f3dc9e0a18`) lines 51-57 [crates/gwiki/src/ingest/pdf/types.rs:51-57]
  - Signature: `impl Default for PdfIngestOptions {`
  - Purpose: 'PdfIngestOptions' is a defaultable configuration struct for PDF ingestion that initializes 'render_dpi' to 'DEFAULT_PDF_RENDER_DPI'. [crates/gwiki/src/ingest/pdf/types.rs:51-57]
- `PdfIngestOptions.default` (method) component `PdfIngestOptions.default [method]` (`05f36e35-34fa-5a36-b3aa-944c4e78bf21`) lines 52-56 [crates/gwiki/src/ingest/pdf/types.rs:52-56]
  - Signature: `fn default() -> Self {`
  - Purpose: Constructs and returns a 'Self' instance initialized with 'render_dpi' set to 'DEFAULT_PDF_RENDER_DPI'. [crates/gwiki/src/ingest/pdf/types.rs:52-56]
- `pdf_fetched_at` (function) component `pdf_fetched_at [function]` (`26d96b42-6ba7-5ef7-b4a4-9915f3170db0`) lines 60-81 [crates/gwiki/src/ingest/pdf/types.rs:60-81]
  - Signature: `pub(crate) fn pdf_fetched_at(value: &str) -> Result<DateTime<Utc>, crate::WikiError> {`
  - Purpose: Parses a trimmed PDF fetch timestamp string as either 'unix-ms:<i64>' into a UTC 'DateTime' via millisecond epoch conversion or as an RFC3339 timestamp converted to UTC, returning a 'WikiError::Config' on parse or range failure. [crates/gwiki/src/ingest/pdf/types.rs:60-81]

