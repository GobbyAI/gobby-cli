---
title: crates/gwiki/src/ingest/pdf/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/types.rs
  ranges:
  - 9-12
  - 15-21
  - 24-29
  - 32-38
  - 41-43
  - 45-51
  - 46-50
  - 54-75
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/types.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

`crates/gwiki/src/ingest/pdf/types.rs` exposes 8 indexed API symbols.
[crates/gwiki/src/ingest/pdf/types.rs:9-12]
[crates/gwiki/src/ingest/pdf/types.rs:15-21]
[crates/gwiki/src/ingest/pdf/types.rs:24-29]
[crates/gwiki/src/ingest/pdf/types.rs:32-38]
[crates/gwiki/src/ingest/pdf/types.rs:41-43]
[crates/gwiki/src/ingest/pdf/types.rs:45-51]
[crates/gwiki/src/ingest/pdf/types.rs:46-50]
[crates/gwiki/src/ingest/pdf/types.rs:54-75]

## API Symbols

- `PdfPage` (class) component `PdfPage [class]` (`4f0eb0c1-f87f-588e-a28f-2540a3975703`) lines 9-12 [crates/gwiki/src/ingest/pdf/types.rs:9-12]
  - Signature: `pub struct PdfPage {`
  - Purpose: PdfPage is a public struct that pairs a page number (usize) with its extracted text content (String), representing a single page from a PDF document. [crates/gwiki/src/ingest/pdf/types.rs:9-12]
- `PdfSnapshot` (class) component `PdfSnapshot [class]` (`5d53ed2e-f282-5b8f-8bf9-94fa46694cd9`) lines 15-21 [crates/gwiki/src/ingest/pdf/types.rs:15-21]
  - Signature: `pub struct PdfSnapshot {`
  - Purpose: `PdfSnapshot` is a struct that encapsulates a fetched PDF document, storing its raw bytes, parsed pages, and metadata including the source location, filename, and UTC timestamp of when it was retrieved. [crates/gwiki/src/ingest/pdf/types.rs:15-21]
- `PdfFileSnapshot` (class) component `PdfFileSnapshot [class]` (`39d2a6b7-1785-577c-9a00-5cc225f4de59`) lines 24-29 [crates/gwiki/src/ingest/pdf/types.rs:24-29]
  - Signature: `pub struct PdfFileSnapshot {`
  - Purpose: `PdfFileSnapshot` is a struct that captures a PDF file's binary contents along with metadata including its location, filename, and UTC timestamp of when it was fetched. [crates/gwiki/src/ingest/pdf/types.rs:24-29]
- `PdfRenderedPage` (class) component `PdfRenderedPage [class]` (`652ac145-594b-5365-bc62-b95d83012ed9`) lines 32-38 [crates/gwiki/src/ingest/pdf/types.rs:32-38]
  - Signature: `pub struct PdfRenderedPage {`
  - Purpose: `PdfRenderedPage` is a struct that encapsulates a single rendered PDF page with its binary image data, MIME type, page number, and optional dimensions. [crates/gwiki/src/ingest/pdf/types.rs:32-38]
- `PdfIngestOptions` (class) component `PdfIngestOptions [class]` (`30250ed2-6bfc-5d20-b864-1d84e8db3545`) lines 41-43 [crates/gwiki/src/ingest/pdf/types.rs:41-43]
  - Signature: `pub struct PdfIngestOptions {`
  - Purpose: `PdfIngestOptions` is a configuration struct that specifies the DPI resolution for rendering PDFs during ingestion via a single `u16` field. [crates/gwiki/src/ingest/pdf/types.rs:41-43]
- `PdfIngestOptions` (class) component `PdfIngestOptions [class]` (`16cd75be-b206-5d66-a1d5-cdcc6ccb0316`) lines 45-51 [crates/gwiki/src/ingest/pdf/types.rs:45-51]
  - Signature: `impl Default for PdfIngestOptions {`
  - Purpose: Implements the `Default` trait for `PdfIngestOptions`, initializing the `render_dpi` field to `DEFAULT_PDF_RENDER_DPI`. [crates/gwiki/src/ingest/pdf/types.rs:45-51]
- `PdfIngestOptions.default` (method) component `PdfIngestOptions.default [method]` (`f6b4906e-b089-5636-b201-572e5586be0c`) lines 46-50 [crates/gwiki/src/ingest/pdf/types.rs:46-50]
  - Signature: `fn default() -> Self {`
  - Purpose: This method implements the `Default` trait to construct a struct instance with the `render_dpi` field initialized to the constant `DEFAULT_PDF_RENDER_DPI`. [crates/gwiki/src/ingest/pdf/types.rs:46-50]
- `pdf_fetched_at` (function) component `pdf_fetched_at [function]` (`aac75659-363b-5f88-a13a-2cb4082c56f6`) lines 54-75 [crates/gwiki/src/ingest/pdf/types.rs:54-75]
  - Signature: `pub(crate) fn pdf_fetched_at(value: &str) -> Result<DateTime<Utc>, crate::WikiError> {`
  - Purpose: Parses a PDF fetch timestamp from either a "unix-ms:"-prefixed Unix millisecond string or an RFC3339 datetime string into a DateTime<Utc>. [crates/gwiki/src/ingest/pdf/types.rs:54-75]

