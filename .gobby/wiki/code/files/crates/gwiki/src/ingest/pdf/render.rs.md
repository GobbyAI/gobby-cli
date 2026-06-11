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

`crates/gwiki/src/ingest/pdf/render.rs` exposes 11 indexed API symbols.
[crates/gwiki/src/ingest/pdf/render.rs:23-39]
[crates/gwiki/src/ingest/pdf/render.rs:42-94]
[crates/gwiki/src/ingest/pdf/render.rs:97-100]
[crates/gwiki/src/ingest/pdf/render.rs:103-114]
[crates/gwiki/src/ingest/pdf/render.rs:117-128]

## API Symbols

- `extract_text_layer_pages` (function) component `extract_text_layer_pages [function]` (`aec8a060-5743-570b-b6f3-58b51ee0ec13`) lines 23-39 [crates/gwiki/src/ingest/pdf/render.rs:23-39]
  - Signature: `pub(crate) fn extract_text_layer_pages(bytes: &[u8]) -> Result<Vec<PdfPage>, WikiError> {`
  - Purpose: Extracts text content from a PDF byte array and returns a vector of `PdfPage` structs with 1-indexed page numbers and extracted text, or a `WikiError` if extraction fails. [crates/gwiki/src/ingest/pdf/render.rs:23-39]
- `render_pdf_pages` (function) component `render_pdf_pages [function]` (`b5f69178-bbd3-5486-aa78-706f3ff3a0e1`) lines 42-94 [crates/gwiki/src/ingest/pdf/render.rs:42-94]
  - Signature: `pub(crate) fn render_pdf_pages(`
  - Purpose: Renders PDF pages as DPI-scaled PNG-encoded images up to configurable page count and byte size budgets, returning the rendered pages with a degradation flag if limits are exceeded. [crates/gwiki/src/ingest/pdf/render.rs:42-94]
- `next_rendered_byte_total` (function) component `next_rendered_byte_total [function]` (`31ccbf77-12df-5f2e-a241-e04c8307cc67`) lines 97-100 [crates/gwiki/src/ingest/pdf/render.rs:97-100]
  - Signature: `fn next_rendered_byte_total(current: usize, page_bytes: usize) -> Option<usize> {`
  - Purpose: Returns `Some` of the sum of `current` and `page_bytes` only if addition succeeds without overflow and the total doesn't exceed `MAX_RENDERED_PDF_TOTAL_BYTES`, otherwise `None`. [crates/gwiki/src/ingest/pdf/render.rs:97-100]
- `pdf_render_budget_degradation` (function) component `pdf_render_budget_degradation [function]` (`92f2fd40-e9f7-54ef-acd7-5b0dc9b82b9c`) lines 103-114 [crates/gwiki/src/ingest/pdf/render.rs:103-114]
  - Signature: `pub(crate) fn pdf_render_budget_degradation(`
  - Purpose: Constructs a DocumentDegradation failure object indicating PDF page rendering terminated due to exceeding the configured page count or total byte budget limits. [crates/gwiki/src/ingest/pdf/render.rs:103-114]
- `bundled_pdfium` (function) component `bundled_pdfium [function]` (`fd9cfd58-390b-56bb-a056-29976930a306`) lines 117-128 [crates/gwiki/src/ingest/pdf/render.rs:117-128]
  - Signature: `fn bundled_pdfium() -> Result<Pdfium, WikiError> {`
  - Purpose: Initializes and returns a `Pdfium` instance by ensuring a bundled PDFium library is available, binding to its path, and mapping any initialization errors to `WikiError::InvalidInput`. [crates/gwiki/src/ingest/pdf/render.rs:117-128]
- `points_to_pixels` (function) component `points_to_pixels [function]` (`7a16a567-0288-506e-976b-b8ad76746647`) lines 131-133 [crates/gwiki/src/ingest/pdf/render.rs:131-133]
  - Signature: `fn points_to_pixels(points: f32, dpi: u16) -> i32 {`
  - Purpose: Converts typographic points to pixels by dividing by 72 (points per inch) and scaling by the specified DPI, with the result rounded and clamped to a minimum of 1. [crates/gwiki/src/ingest/pdf/render.rs:131-133]
- `bitmap_dimension_to_u32` (function) component `bitmap_dimension_to_u32 [function]` (`f5aa5e0e-b7eb-5b51-82dc-a99119a74c7e`) lines 136-144 [crates/gwiki/src/ingest/pdf/render.rs:136-144]
  - Signature: `fn bitmap_dimension_to_u32(name: &str, value: i32) -> Result<u32, WikiError> {`
  - Purpose: Converts a bitmap dimension from `i32` to `u32`, validating that the value is positive and does not exceed `u32`'s maximum range, returning a `WikiError` if either constraint is violated. [crates/gwiki/src/ingest/pdf/render.rs:136-144]
- `encode_png_rgba` (function) component `encode_png_rgba [function]` (`926e6705-b70a-513b-a0ef-32d3d06a855c`) lines 147-166 [crates/gwiki/src/ingest/pdf/render.rs:147-166]
  - Signature: `fn encode_png_rgba(width: u32, height: u32, rgba: &[u8]) -> Result<Vec<u8>, WikiError> {`
  - Purpose: Encodes raw RGBA pixel data of specified dimensions into a PNG-formatted byte vector, returning a `WikiError` on encoding failure. [crates/gwiki/src/ingest/pdf/render.rs:147-166]
- `pdfium_error` (function) component `pdfium_error [function]` (`e6710159-718a-505a-b81d-e86767a76d84`) lines 169-174 [crates/gwiki/src/ingest/pdf/render.rs:169-174]
  - Signature: `fn pdfium_error(error: impl std::fmt::Display) -> WikiError {`
  - Purpose: Wraps a Display-formattable error into a `WikiError::InvalidInput` variant with field `"pdf"` and a formatted message indicating PDF page rendering failure. [crates/gwiki/src/ingest/pdf/render.rs:169-174]
- `render_byte_budget_rejects_overflow_before_updating_total` (function) component `render_byte_budget_rejects_overflow_before_updating_total [function]` (`41a5d1da-3598-557a-ae5d-7aade5549399`) lines 181-191 [crates/gwiki/src/ingest/pdf/render.rs:181-191]
  - Signature: `fn render_byte_budget_rejects_overflow_before_updating_total() {`
  - Purpose: Unit test verifying that `next_rendered_byte_total` rejects overflow by returning `None` when the cumulative byte total would exceed `MAX_RENDERED_PDF_TOTAL_BYTES`. [crates/gwiki/src/ingest/pdf/render.rs:181-191]
- `bitmap_dimensions_reject_non_positive_values_before_cast` (function) component `bitmap_dimensions_reject_non_positive_values_before_cast [function]` (`12832ccc-165d-5f74-82aa-20c4a257b008`) lines 195-202 [crates/gwiki/src/ingest/pdf/render.rs:195-202]
  - Signature: `fn bitmap_dimensions_reject_non_positive_values_before_cast() {`
  - Purpose: A unit test that validates `bitmap_dimension_to_u32()` rejects negative width values and emits an error message containing "bitmap width must be positive" before type casting. [crates/gwiki/src/ingest/pdf/render.rs:195-202]

