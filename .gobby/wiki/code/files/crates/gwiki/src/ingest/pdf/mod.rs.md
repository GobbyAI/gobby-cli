---
title: crates/gwiki/src/ingest/pdf/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/mod.rs
  ranges:
  - 22-25
  - 28-34
  - 37-40
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/mod.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

This module is the PDF ingestion entry point for gwiki, wiring together text-layer extraction, page rendering, and vision-based Markdown merging. It exposes the document-feature-gated ingest API and shared PDF types, while the internal `PdfPageMarkdown` and `PdfMarkdownSummary` structs capture per-page Markdown plus extraction metadata, and `PdfRenderOutcome` bundles rendered pages with any degradation reported during rendering.
[crates/gwiki/src/ingest/pdf/mod.rs:22-25]
[crates/gwiki/src/ingest/pdf/mod.rs:28-34]
[crates/gwiki/src/ingest/pdf/mod.rs:37-40]

## API Symbols

- `PdfPageMarkdown` (class) component `PdfPageMarkdown [class]` (`2021a76a-b2b1-532a-8dd0-5615e7b55741`) lines 22-25 [crates/gwiki/src/ingest/pdf/mod.rs:22-25]
  - Signature: `struct PdfPageMarkdown {`
  - Purpose: 'PdfPageMarkdown' is a data structure that pairs a PDF page number ('usize') with the page’s extracted Markdown content ('String'). [crates/gwiki/src/ingest/pdf/mod.rs:22-25]
- `PdfMarkdownSummary` (class) component `PdfMarkdownSummary [class]` (`39ec77cb-ca8d-51b8-9930-d61f4bc795bc`) lines 28-34 [crates/gwiki/src/ingest/pdf/mod.rs:28-34]
  - Signature: `struct PdfMarkdownSummary {`
  - Purpose: 'PdfMarkdownSummary' is a struct that records PDF-to-Markdown extraction metadata: the page count, whether a text layer was present, whether vision fallback was used, the optional model name, and a list of document degradations encountered. [crates/gwiki/src/ingest/pdf/mod.rs:28-34]
- `PdfRenderOutcome` (class) component `PdfRenderOutcome [class]` (`3c26316a-01a4-5e2e-b1f7-a3745019079a`) lines 37-40 [crates/gwiki/src/ingest/pdf/mod.rs:37-40]
  - Signature: `struct PdfRenderOutcome {`
  - Purpose: 'PdfRenderOutcome' is a result struct that aggregates the rendered PDF pages as 'Vec<PdfRenderedPage>' and an optional 'DocumentDegradation' describing any quality loss or fallback during rendering. [crates/gwiki/src/ingest/pdf/mod.rs:37-40]

