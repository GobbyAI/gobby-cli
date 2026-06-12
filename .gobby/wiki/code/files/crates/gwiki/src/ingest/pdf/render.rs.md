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

- `extract_text_layer_pages` (function) component `extract_text_layer_pages [function]` (`078c2eba-2bec-5f7b-ba3f-8ffad07d5a3b`) lines 23-39 [crates/gwiki/src/ingest/pdf/render.rs:23-39]
  - Signature: `pub(crate) fn extract_text_layer_pages(bytes: &[u8]) -> Result<Vec<PdfPage>, WikiError> {`
  - Purpose: Indexed function `extract_text_layer_pages` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:23-39]
- `render_pdf_pages` (function) component `render_pdf_pages [function]` (`22444081-e1c9-5009-9694-9b16b53c3b67`) lines 42-94 [crates/gwiki/src/ingest/pdf/render.rs:42-94]
  - Signature: `pub(crate) fn render_pdf_pages(`
  - Purpose: Indexed function `render_pdf_pages` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:42-94]
- `next_rendered_byte_total` (function) component `next_rendered_byte_total [function]` (`ff706ec2-a5fc-531c-8b49-b717a4d9ca49`) lines 97-100 [crates/gwiki/src/ingest/pdf/render.rs:97-100]
  - Signature: `fn next_rendered_byte_total(current: usize, page_bytes: usize) -> Option<usize> {`
  - Purpose: Indexed function `next_rendered_byte_total` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:97-100]
- `pdf_render_budget_degradation` (function) component `pdf_render_budget_degradation [function]` (`3716ca39-bc6b-58f0-a4c0-a751755ee228`) lines 103-114 [crates/gwiki/src/ingest/pdf/render.rs:103-114]
  - Signature: `pub(crate) fn pdf_render_budget_degradation(`
  - Purpose: Indexed function `pdf_render_budget_degradation` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:103-114]
- `bundled_pdfium` (function) component `bundled_pdfium [function]` (`f9ef1ddb-ff8e-5820-87ac-46bc6e59b01e`) lines 117-128 [crates/gwiki/src/ingest/pdf/render.rs:117-128]
  - Signature: `fn bundled_pdfium() -> Result<Pdfium, WikiError> {`
  - Purpose: Indexed function `bundled_pdfium` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:117-128]
- `points_to_pixels` (function) component `points_to_pixels [function]` (`82620d3f-f256-5280-a998-c75e1e574b2b`) lines 131-133 [crates/gwiki/src/ingest/pdf/render.rs:131-133]
  - Signature: `fn points_to_pixels(points: f32, dpi: u16) -> i32 {`
  - Purpose: Indexed function `points_to_pixels` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:131-133]
- `bitmap_dimension_to_u32` (function) component `bitmap_dimension_to_u32 [function]` (`3bbbf0c9-0582-5b42-b8c8-a30c260370a9`) lines 136-144 [crates/gwiki/src/ingest/pdf/render.rs:136-144]
  - Signature: `fn bitmap_dimension_to_u32(name: &str, value: i32) -> Result<u32, WikiError> {`
  - Purpose: Indexed function `bitmap_dimension_to_u32` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:136-144]
- `encode_png_rgba` (function) component `encode_png_rgba [function]` (`5aa764aa-8fe1-56ef-969d-e8b83d3fbbda`) lines 147-166 [crates/gwiki/src/ingest/pdf/render.rs:147-166]
  - Signature: `fn encode_png_rgba(width: u32, height: u32, rgba: &[u8]) -> Result<Vec<u8>, WikiError> {`
  - Purpose: Indexed function `encode_png_rgba` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:147-166]
- `pdfium_error` (function) component `pdfium_error [function]` (`f8fb3dd3-beb0-5b2f-9095-fe582da03cb5`) lines 169-174 [crates/gwiki/src/ingest/pdf/render.rs:169-174]
  - Signature: `fn pdfium_error(error: impl std::fmt::Display) -> WikiError {`
  - Purpose: Indexed function `pdfium_error` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:169-174]
- `render_byte_budget_rejects_overflow_before_updating_total` (function) component `render_byte_budget_rejects_overflow_before_updating_total [function]` (`b8530802-7791-52a6-bf37-e1a6fe0dee3c`) lines 181-191 [crates/gwiki/src/ingest/pdf/render.rs:181-191]
  - Signature: `fn render_byte_budget_rejects_overflow_before_updating_total() {`
  - Purpose: Indexed function `render_byte_budget_rejects_overflow_before_updating_total` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:181-191]
- `bitmap_dimensions_reject_non_positive_values_before_cast` (function) component `bitmap_dimensions_reject_non_positive_values_before_cast [function]` (`73b03882-8e07-5e33-a8a3-aadedc3ff349`) lines 195-202 [crates/gwiki/src/ingest/pdf/render.rs:195-202]
  - Signature: `fn bitmap_dimensions_reject_non_positive_values_before_cast() {`
  - Purpose: Indexed function `bitmap_dimensions_reject_non_positive_values_before_cast` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:195-202]

