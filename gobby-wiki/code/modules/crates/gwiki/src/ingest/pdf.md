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

The `crates/gwiki/src/ingest/pdf` module owns PDF ingestion into wiki content: it accepts PDF snapshots, extracts page text when available, optionally renders pages for document/vision handling, and produces markdown plus assets for indexing. Its ingestion entry points connect to the wider ingest/store layer through `IngestResult`, `index_after_ingest`, `write_asset`, `write_raw_markdown`, `WikiIndexStore`, and source manifests, while sharing scope and vision contracts through `ScopeIdentity` and `VisionEndpoint` (`crates/gwiki/src/ingest/pdf/ingest.rs:4-20`).

The key flow starts with `ingest_pages`, which delegates to `ingest_pages_with_vision` using no rendered pages and an unavailable vision endpoint (`crates/gwiki/src/ingest/pdf/ingest.rs:22-37`). With the `documents` feature, `ingest_pdf_file` wraps `ingest_pdf_file_without_index`, then indexes the vault via `index_after_ingest` (`crates/gwiki/src/ingest/pdf/ingest.rs:39-52`). The lower-level ingest path attempts text-layer extraction and records a `PdfTextLayerError` degradation if extraction fails, preserving the original asset as fallback context (`crates/gwiki/src/ingest/pdf/ingest.rs:54-70`).

Rendering and markdown generation are split by concern. `render.rs` calls `pdf_extract` for per-page text and `pdfium_render` for bitmap rendering, capping rendered pages and byte budget under the `documents` feature (`crates/gwiki/src/ingest/pdf/render.rs:17-45`, `crates/gwiki/src/ingest/pdf/render.rs:56-69`). `markdown.rs` formats the final document with source, hash, asset, page, model, scope, and degradation metadata, then emits a visible degradation section when fallbacks were used (`crates/gwiki/src/ingest/pdf/markdown.rs:24-65`).

Tests exercise the collaboration boundary with vision: the fake vision client asserts PNG requests, dimensions, asset/file-name consistency, and returns OCR plus metadata (`crates/gwiki/src/ingest/pdf/tests.rs:29-58`). They also pin the public ingest render default DPI at `150` (`crates/gwiki/src/ingest/pdf/tests.rs:62-65`).

| Public symbol | Role | Source |
| --- | --- | --- |
| `ingest_pages` | Public page-snapshot ingestion entry point | `crates/gwiki/src/ingest/pdf/ingest.rs:22-37` |
| `ingest_pdf_file` | Feature-gated PDF-file ingestion plus indexing | `crates/gwiki/src/ingest/pdf/ingest.rs:39-52` |
| `ingest_pdf_file_without_index` | Feature-gated ingestion core before indexing | `crates/gwiki/src/ingest/pdf/ingest.rs:54-70` |
| `render_pdf_markdown` | Builds markdown body and metadata | `crates/gwiki/src/ingest/pdf/markdown.rs:14-65` |
| `extract_text_layer_pages` | Extracts per-page text via `pdf_extract` | `crates/gwiki/src/ingest/pdf/render.rs:22-39` |
| `render_pdf_pages` | Renders PDF pages via PDFium | `crates/gwiki/src/ingest/pdf/render.rs:41-69` |

| Constant / metadata | Value or fields | Source |
| --- | --- | --- |
| `DEFAULT_PDF_RENDER_DPI` | `150` | `crates/gwiki/src/ingest/pdf/tests.rs:62-65` |
| `MAX_RENDERED_PDF_PAGES` | `32` | `crates/gwiki/src/ingest/pdf/render.rs:17-18` |
| `MAX_RENDERED_PDF_TOTAL_BYTES` | `32 * 1024 * 1024` | `crates/gwiki/src/ingest/pdf/render.rs:19-20` |
| Markdown metadata | `source_kind`, `source_location`, `fetched_at`, `source_hash`, `source_asset`, `file_size_bytes`, `page_count`, `has_text_layer`, `vision_used`, `model`, `scope_kind`, `scope_id`, `media_degradation` | `crates/gwiki/src/ingest/pdf/markdown.rs:24-50` |

| Stable component | ID |
| --- | --- |
| `PdfPageMarkdown` | `2021a76a-b2b1-532a-8dd0-5615e7b55741` |
| `PdfMarkdownSummary` | `39ec77cb-ca8d-51b8-9930-d61f4bc795bc` |
| `PdfRenderOutcome` | `3c26316a-01a4-5e2e-b1f7-a3745019079a` |

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

