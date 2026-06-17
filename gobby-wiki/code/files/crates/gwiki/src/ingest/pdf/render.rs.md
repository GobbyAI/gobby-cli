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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/pdf/render.rs:23-39](crates/gwiki/src/ingest/pdf/render.rs#L23-L39), [crates/gwiki/src/ingest/pdf/render.rs:42-94](crates/gwiki/src/ingest/pdf/render.rs#L42-L94), [crates/gwiki/src/ingest/pdf/render.rs:97-100](crates/gwiki/src/ingest/pdf/render.rs#L97-L100), [crates/gwiki/src/ingest/pdf/render.rs:103-114](crates/gwiki/src/ingest/pdf/render.rs#L103-L114), [crates/gwiki/src/ingest/pdf/render.rs:117-128](crates/gwiki/src/ingest/pdf/render.rs#L117-L128), [crates/gwiki/src/ingest/pdf/render.rs:131-133](crates/gwiki/src/ingest/pdf/render.rs#L131-L133), [crates/gwiki/src/ingest/pdf/render.rs:136-144](crates/gwiki/src/ingest/pdf/render.rs#L136-L144), [crates/gwiki/src/ingest/pdf/render.rs:147-166](crates/gwiki/src/ingest/pdf/render.rs#L147-L166), [crates/gwiki/src/ingest/pdf/render.rs:169-174](crates/gwiki/src/ingest/pdf/render.rs#L169-L174), [crates/gwiki/src/ingest/pdf/render.rs:181-191](crates/gwiki/src/ingest/pdf/render.rs#L181-L191), [crates/gwiki/src/ingest/pdf/render.rs:195-202](crates/gwiki/src/ingest/pdf/render.rs#L195-L202)

</details>

# crates/gwiki/src/ingest/pdf/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements PDF ingestion rendering helpers for the `documents` feature: it can extract per-page text from a PDF’s text layer, render PDF pages to images with bundled Pdfium, and package the results into `PdfRenderOutcome`. The helper functions support that pipeline by loading the embedded Pdfium runtime, converting page sizes from points to pixels, validating bitmap dimensions, encoding rendered RGBA bitmaps as PNG, and translating Pdfium failures into `WikiError`. The budget functions enforce limits on how many pages and bytes can be rendered, and the test helpers verify overflow and invalid-dimension rejection before totals are updated or values are cast.
[crates/gwiki/src/ingest/pdf/render.rs:23-39]
[crates/gwiki/src/ingest/pdf/render.rs:42-94]
[crates/gwiki/src/ingest/pdf/render.rs:97-100]
[crates/gwiki/src/ingest/pdf/render.rs:103-114]
[crates/gwiki/src/ingest/pdf/render.rs:117-128]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `extract_text_layer_pages` | function | `pub(crate) fn extract_text_layer_pages(bytes: &[u8]) -> Result<Vec<PdfPage>, WikiError> {` | `extract_text_layer_pages [function]` | `078c2eba-2bec-5f7b-ba3f-8ffad07d5a3b` | 23-39 [crates/gwiki/src/ingest/pdf/render.rs:23-39] | Indexed function `extract_text_layer_pages` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:23-39] |
| `render_pdf_pages` | function | `pub(crate) fn render_pdf_pages(` | `render_pdf_pages [function]` | `22444081-e1c9-5009-9694-9b16b53c3b67` | 42-94 [crates/gwiki/src/ingest/pdf/render.rs:42-94] | Indexed function `render_pdf_pages` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:42-94] |
| `next_rendered_byte_total` | function | `fn next_rendered_byte_total(current: usize, page_bytes: usize) -> Option<usize> {` | `next_rendered_byte_total [function]` | `ff706ec2-a5fc-531c-8b49-b717a4d9ca49` | 97-100 [crates/gwiki/src/ingest/pdf/render.rs:97-100] | Indexed function `next_rendered_byte_total` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:97-100] |
| `pdf_render_budget_degradation` | function | `pub(crate) fn pdf_render_budget_degradation(` | `pdf_render_budget_degradation [function]` | `3716ca39-bc6b-58f0-a4c0-a751755ee228` | 103-114 [crates/gwiki/src/ingest/pdf/render.rs:103-114] | Indexed function `pdf_render_budget_degradation` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:103-114] |
| `bundled_pdfium` | function | `fn bundled_pdfium() -> Result<Pdfium, WikiError> {` | `bundled_pdfium [function]` | `f9ef1ddb-ff8e-5820-87ac-46bc6e59b01e` | 117-128 [crates/gwiki/src/ingest/pdf/render.rs:117-128] | Indexed function `bundled_pdfium` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:117-128] |
| `points_to_pixels` | function | `fn points_to_pixels(points: f32, dpi: u16) -> i32 {` | `points_to_pixels [function]` | `82620d3f-f256-5280-a998-c75e1e574b2b` | 131-133 [crates/gwiki/src/ingest/pdf/render.rs:131-133] | Indexed function `points_to_pixels` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:131-133] |
| `bitmap_dimension_to_u32` | function | `fn bitmap_dimension_to_u32(name: &str, value: i32) -> Result<u32, WikiError> {` | `bitmap_dimension_to_u32 [function]` | `3bbbf0c9-0582-5b42-b8c8-a30c260370a9` | 136-144 [crates/gwiki/src/ingest/pdf/render.rs:136-144] | Indexed function `bitmap_dimension_to_u32` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:136-144] |
| `encode_png_rgba` | function | `fn encode_png_rgba(width: u32, height: u32, rgba: &[u8]) -> Result<Vec<u8>, WikiError> {` | `encode_png_rgba [function]` | `5aa764aa-8fe1-56ef-969d-e8b83d3fbbda` | 147-166 [crates/gwiki/src/ingest/pdf/render.rs:147-166] | Indexed function `encode_png_rgba` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:147-166] |
| `pdfium_error` | function | `fn pdfium_error(error: impl std::fmt::Display) -> WikiError {` | `pdfium_error [function]` | `f8fb3dd3-beb0-5b2f-9095-fe582da03cb5` | 169-174 [crates/gwiki/src/ingest/pdf/render.rs:169-174] | Indexed function `pdfium_error` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:169-174] |
| `render_byte_budget_rejects_overflow_before_updating_total` | function | `fn render_byte_budget_rejects_overflow_before_updating_total() {` | `render_byte_budget_rejects_overflow_before_updating_total [function]` | `b8530802-7791-52a6-bf37-e1a6fe0dee3c` | 181-191 [crates/gwiki/src/ingest/pdf/render.rs:181-191] | Indexed function `render_byte_budget_rejects_overflow_before_updating_total` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:181-191] |
| `bitmap_dimensions_reject_non_positive_values_before_cast` | function | `fn bitmap_dimensions_reject_non_positive_values_before_cast() {` | `bitmap_dimensions_reject_non_positive_values_before_cast [function]` | `73b03882-8e07-5e33-a8a3-aadedc3ff349` | 195-202 [crates/gwiki/src/ingest/pdf/render.rs:195-202] | Indexed function `bitmap_dimensions_reject_non_positive_values_before_cast` in `crates/gwiki/src/ingest/pdf/render.rs`. [crates/gwiki/src/ingest/pdf/render.rs:195-202] |
