---
title: crates/gwiki/src/ingest/pdf/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/render.rs
  ranges:
  - 23-39
  - 42-94
  - 97-100
  - 103-114
  - 117-128
  - 131-133
  - 136-144
  - 147-166
  - 169-174
  - 181-191
  - 195-202
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/render.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

This file handles PDF ingestion for document documents by extracting the text layer into 1-indexed `PdfPage` values and rendering page snapshots into PNG-encoded `PdfRenderedPage` images. It enforces hard limits on rendered page count and total byte budget, uses helper functions to convert sizes and wrap Pdfium/PNG failures into `WikiError::InvalidInput`, and includes tests that verify the byte-budget and bitmap-dimension checks fail safely before overflow or invalid casts.
[crates/gwiki/src/ingest/pdf/render.rs:23-39]
[crates/gwiki/src/ingest/pdf/render.rs:42-94]
[crates/gwiki/src/ingest/pdf/render.rs:97-100]
[crates/gwiki/src/ingest/pdf/render.rs:103-114]
[crates/gwiki/src/ingest/pdf/render.rs:117-128]

## API Symbols

- `extract_text_layer_pages` (function) component `extract_text_layer_pages [function]` (`078c2eba-2bec-5f7b-ba3f-8ffad07d5a3b`) lines 23-39 [crates/gwiki/src/ingest/pdf/render.rs:23-39]
  - Signature: `pub(crate) fn extract_text_layer_pages(bytes: &[u8]) -> Result<Vec<PdfPage>, WikiError> {`
  - Purpose: Extracts text from an in-memory PDF byte slice into a 1-indexed 'Vec<PdfPage>' and converts any extraction failure into 'WikiError::InvalidInput' for the 'pdf' field with a formatted error message. [crates/gwiki/src/ingest/pdf/render.rs:23-39]
- `render_pdf_pages` (function) component `render_pdf_pages [function]` (`22444081-e1c9-5009-9694-9b16b53c3b67`) lines 42-94 [crates/gwiki/src/ingest/pdf/render.rs:42-94]
  - Signature: `pub(crate) fn render_pdf_pages(`
  - Purpose: Renders up to 'MAX_RENDERED_PDF_PAGES' pages from a PDF snapshot into PNG-encoded 'PdfRenderedPage' entries at the requested DPI, tracking a byte budget and returning a 'PdfRenderOutcome' with optional degradation metadata if rendering is truncated. [crates/gwiki/src/ingest/pdf/render.rs:42-94]
- `next_rendered_byte_total` (function) component `next_rendered_byte_total [function]` (`ff706ec2-a5fc-531c-8b49-b717a4d9ca49`) lines 97-100 [crates/gwiki/src/ingest/pdf/render.rs:97-100]
  - Signature: `fn next_rendered_byte_total(current: usize, page_bytes: usize) -> Option<usize> {`
  - Purpose: Returns 'Some(current + page_bytes)' when the addition does not overflow and the result is at most 'MAX_RENDERED_PDF_TOTAL_BYTES'; otherwise returns 'None'. [crates/gwiki/src/ingest/pdf/render.rs:97-100]
- `pdf_render_budget_degradation` (function) component `pdf_render_budget_degradation [function]` (`3716ca39-bc6b-58f0-a4c0-a751755ee228`) lines 103-114 [crates/gwiki/src/ingest/pdf/render.rs:103-114]
  - Signature: `pub(crate) fn pdf_render_budget_degradation(`
  - Purpose: Constructs a 'DocumentDegradation' reporting 'PdfRenderBudgetExceeded' for a PDF whose page-rendering budget was exhausted, recording the total page count and a message that rendering stopped after the configured page or byte limit while preserving the original asset. [crates/gwiki/src/ingest/pdf/render.rs:103-114]
- `bundled_pdfium` (function) component `bundled_pdfium [function]` (`f9ef1ddb-ff8e-5820-87ac-46bc6e59b01e`) lines 117-128 [crates/gwiki/src/ingest/pdf/render.rs:117-128]
  - Signature: `fn bundled_pdfium() -> Result<Pdfium, WikiError> {`
  - Purpose: Ensures the bundled Pdfium library is available, binds 'Pdfium' to that library path, and converts any initialization or binding failure into 'WikiError::InvalidInput' for the 'pdf' field. [crates/gwiki/src/ingest/pdf/render.rs:117-128]
- `points_to_pixels` (function) component `points_to_pixels [function]` (`82620d3f-f256-5280-a998-c75e1e574b2b`) lines 131-133 [crates/gwiki/src/ingest/pdf/render.rs:131-133]
  - Signature: `fn points_to_pixels(points: f32, dpi: u16) -> i32 {`
  - Purpose: Converts a font size in points to integer pixels by scaling with 'dpi / 72', rounding to the nearest whole pixel, and clamping the result to a minimum of 1. [crates/gwiki/src/ingest/pdf/render.rs:131-133]
- `bitmap_dimension_to_u32` (function) component `bitmap_dimension_to_u32 [function]` (`3bbbf0c9-0582-5b42-b8c8-a30c260370a9`) lines 136-144 [crates/gwiki/src/ingest/pdf/render.rs:136-144]
  - Signature: `fn bitmap_dimension_to_u32(name: &str, value: i32) -> Result<u32, WikiError> {`
  - Purpose: Returns 'Ok(value as u32)' for strictly positive 'i32' bitmap dimensions, otherwise returns a 'WikiError' if the value is nonpositive or cannot fit in 'u32'. [crates/gwiki/src/ingest/pdf/render.rs:136-144]
- `encode_png_rgba` (function) component `encode_png_rgba [function]` (`5aa764aa-8fe1-56ef-969d-e8b83d3fbbda`) lines 147-166 [crates/gwiki/src/ingest/pdf/render.rs:147-166]
  - Signature: `fn encode_png_rgba(width: u32, height: u32, rgba: &[u8]) -> Result<Vec<u8>, WikiError> {`
  - Purpose: Encodes an RGBA8 pixel buffer into a PNG byte vector using the 'png' encoder with the specified dimensions, mapping any header or image-write failure to 'WikiError::InvalidInput' with field '"pdf"'. [crates/gwiki/src/ingest/pdf/render.rs:147-166]
- `pdfium_error` (function) component `pdfium_error [function]` (`f8fb3dd3-beb0-5b2f-9095-fe582da03cb5`) lines 169-174 [crates/gwiki/src/ingest/pdf/render.rs:169-174]
  - Signature: `fn pdfium_error(error: impl std::fmt::Display) -> WikiError {`
  - Purpose: Converts any displayable PDFium render error into a 'WikiError::InvalidInput' for the 'pdf' field with the message 'failed to render PDF page: {error}'. [crates/gwiki/src/ingest/pdf/render.rs:169-174]
- `render_byte_budget_rejects_overflow_before_updating_total` (function) component `render_byte_budget_rejects_overflow_before_updating_total [function]` (`b8530802-7791-52a6-bf37-e1a6fe0dee3c`) lines 181-191 [crates/gwiki/src/ingest/pdf/render.rs:181-191]
  - Signature: `fn render_byte_budget_rejects_overflow_before_updating_total() {`
  - Purpose: Verifies that 'next_rendered_byte_total' returns 'None' on 'usize::MAX + 1' overflow and when adding past 'MAX_RENDERED_PDF_TOTAL_BYTES', while still allowing an in-bounds increment to exactly reach the byte limit. [crates/gwiki/src/ingest/pdf/render.rs:181-191]
- `bitmap_dimensions_reject_non_positive_values_before_cast` (function) component `bitmap_dimensions_reject_non_positive_values_before_cast [function]` (`73b03882-8e07-5e33-a8a3-aadedc3ff349`) lines 195-202 [crates/gwiki/src/ingest/pdf/render.rs:195-202]
  - Signature: `fn bitmap_dimensions_reject_non_positive_values_before_cast() {`
  - Purpose: Verifies that converting a negative bitmap width with 'bitmap_dimension_to_u32' fails before any cast and returns an error whose message states the dimension must be positive. [crates/gwiki/src/ingest/pdf/render.rs:195-202]

