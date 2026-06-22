---
title: crates/gwiki/src/ingest/pdf
type: code_module
provenance:
- file: crates/gwiki/src/ingest/pdf/ingest.rs
- file: crates/gwiki/src/ingest/pdf/markdown.rs
- file: crates/gwiki/src/ingest/pdf/mod.rs
- file: crates/gwiki/src/ingest/pdf/render.rs
- file: crates/gwiki/src/ingest/pdf/tests.rs
- file: crates/gwiki/src/ingest/pdf/text.rs
- file: crates/gwiki/src/ingest/pdf/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

## crates/gwiki/src/ingest/pdf

This module is the PDF ingestion pipeline for gwiki. It accepts a raw PDF byte snapshot and produces an indexed Markdown document stored in the wiki vault. The pipeline has two operating modes: a lightweight text-layer-only path available in all builds, and a full render path that is gated behind the `documents` Cargo feature. When `documents` is active the module uses the `pdfium_render` crate to rasterise each page into PNG images, then feeds those images to an optional vision/OCR endpoint before normalising and merging all per-page content into a single Markdown artifact. Hard limits guard resource consumption: no more than 32 pages are rendered and the total rendered byte budget is capped at 32 MiB (render.rs:16-18). Pages beyond those limits are recorded as `DocumentDegradation` entries that surface in the final Markdown output and in the index.

The ingestion flow is layered across four files. `render.rs` owns the pdfium interaction, calling `extract_text_layer_pages` then `render_pdf_pages` to produce `PdfRenderedPage` values (render.rs:22-56). `ingest.rs` orchestrates the overall flow: `ingest_pdf_file_without_index` calls into render, dispatches rendered pages to the vision endpoint when one is configured, delegates text normalisation to `text.rs`, and then calls `merge_pdf_pages` in `markdown.rs` to assemble per-page `PdfPageMarkdown` structs (ingest.rs:54-100). `render_pdf_markdown` in `markdown.rs` finalises the document by prepending a structured YAML-style metadata block that records provenance fields such as `source_kind`, `source_location`, `fetched_at`, `source_hash`, `page_count`, `has_text_layer`, `vision_used`, and any `media_degradation` reasons (markdown.rs:14-62). The top-level entry points in `ingest.rs` call `index_after_ingest` from the parent `crate::ingest` module to update the wiki store before returning.

The module re-exports three types from `mod.rs` as the stable public surface consumed by callers inside the wider `crates/gwiki` crate.

| Public type | Stable component ID | Role |
|---|---|---|
| `PdfPageMarkdown` | 2021a76a-b2b1-532a-8dd0-5615e7b55741 | Per-page text + vision content carrier |
| `PdfMarkdownSummary` | 39ec77cb-ca8d-51b8-9930-d61f4bc795bc | Aggregated metadata for the whole document |
| `PdfRenderOutcome` | 3c26316a-01a4-5e2e-b1f7-a3745019079a | Result of pdfium page rendering |

| Public function | Feature gate | Purpose |
|---|---|---|
| `ingest_pages` | — | Ingest pre-rendered pages without vision (ingest.rs:22-34) |
| `ingest_pages_with_vision` | — | Ingest pre-rendered pages with an optional vision endpoint (ingest.rs) |
| `ingest_pdf_file` | `documents` | Full file ingest: render + vision + index (ingest.rs:38-47) |
| `ingest_pdf_file_without_index` | `documents` | Same but defers index update to the caller (ingest.rs:50-100) |

| Internal helper | File | Purpose |
|---|---|---|
| `extract_text_layer_pages` | render.rs:22 | Extract embedded text via `pdf_extract` |
| `render_pdf_pages` | render.rs:41 | Rasterise pages with pdfium at configurable DPI |
| `pdf_render_budget_degradation` | render.rs | Build degradation record when page/byte limits are hit |
| `normalize_page_text` | text.rs | Clean and normalise extracted text strings |
| `render_pdf_markdown` | markdown.rs:14 | Compose final Markdown document with metadata header |
| `sanitize_pdf_page_markdown` | markdown.rs | Sanitise per-page markdown fragments |
| `merge_pdf_pages` | markdown.rs | Merge page-level structs into document-level summary |
| `pdf_fetched_at` | types.rs | Parse `unix-ms:` and RFC 3339 timestamp formats |

| Constant | Value | Scope |
|---|---|---|
| `DEFAULT_PDF_RENDER_DPI` | `150` | Public; validated in tests.rs:63 |
| `MAX_RENDERED_PDF_PAGES` | `32` | `documents` feature only (render.rs:16) |
| `MAX_RENDERED_PDF_TOTAL_BYTES` | `33 554 432` (32 MiB) | `documents` or `test` (render.rs:18) |

The module collaborates closely with several sibling packages. It imports `ScopeIdentity` and `WikiError` from `crate` (ingest.rs:5-6), the `WikiIndexStore` trait from `crate::store` (ingest.rs:11), `DocumentDegradation` / `DocumentFailureMode` / `DocumentUnitCount` from `crate::document` (ingest.rs:7), and the `VisionClient` / `VisionEndpoint` / `VisionRequest` / `VisionExtraction` traits from `crate::vision` (ingest.rs:12, markdown.rs:8). Shared ingest utilities — `markdown_metadata`, `path_to_string`, `single_line`, `index_after_ingest`, `write_asset`, and `write_raw_markdown` — come from the parent `crate::ingest` module (ingest.rs:9-10, markdown.rs:5). The test suite (`tests.rs`) satisfies the `VisionClient` contract with a `FakePdfVisionClient` stub that validates PNG image dimensions and returns deterministic OCR text, confirming the vision integration contract expected by `ingest_pages_with_vision` (tests.rs:22-55).
[crates/gwiki/src/ingest/pdf/markdown.rs:15-89]
[crates/gwiki/src/ingest/pdf/mod.rs:22-25]
[crates/gwiki/src/ingest/pdf/render.rs:23-39]
[crates/gwiki/src/ingest/pdf/tests.rs:21]
[crates/gwiki/src/ingest/pdf/text.rs:4-25]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/pdf/ingest.rs\|crates/gwiki/src/ingest/pdf/ingest.rs]] | `crates/gwiki/src/ingest/pdf/ingest.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/markdown.rs\|crates/gwiki/src/ingest/pdf/markdown.rs]] | `crates/gwiki/src/ingest/pdf/markdown.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/mod.rs\|crates/gwiki/src/ingest/pdf/mod.rs]] | `crates/gwiki/src/ingest/pdf/mod.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/render.rs\|crates/gwiki/src/ingest/pdf/render.rs]] | `crates/gwiki/src/ingest/pdf/render.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/tests.rs\|crates/gwiki/src/ingest/pdf/tests.rs]] | `crates/gwiki/src/ingest/pdf/tests.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/text.rs\|crates/gwiki/src/ingest/pdf/text.rs]] | `crates/gwiki/src/ingest/pdf/text.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/types.rs\|crates/gwiki/src/ingest/pdf/types.rs]] | `crates/gwiki/src/ingest/pdf/types.rs` exposes 7 indexed API symbols. |

