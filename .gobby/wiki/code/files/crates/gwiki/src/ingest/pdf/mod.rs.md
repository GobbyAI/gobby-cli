---
title: crates/gwiki/src/ingest/pdf/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/mod.rs
  ranges:
  - 21-24
  - 26-32
  - 35-38
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/mod.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

`crates/gwiki/src/ingest/pdf/mod.rs` exposes 3 indexed API symbols.
[crates/gwiki/src/ingest/pdf/mod.rs:21-24]
[crates/gwiki/src/ingest/pdf/mod.rs:26-32]
[crates/gwiki/src/ingest/pdf/mod.rs:35-38]

## API Symbols

- `PdfPageMarkdown` (class) component `PdfPageMarkdown [class]` (`30281de0-d088-5f9e-824f-0c0e7a576ee0`) lines 21-24 [crates/gwiki/src/ingest/pdf/mod.rs:21-24]
  - Signature: `struct PdfPageMarkdown {`
  - Purpose: PdfPageMarkdown is a struct that pairs a PDF page number with its markdown-formatted textual representation. [crates/gwiki/src/ingest/pdf/mod.rs:21-24]
- `PdfMarkdownSummary` (class) component `PdfMarkdownSummary [class]` (`649603d2-fe46-5603-b101-da3338ecd4f1`) lines 26-32 [crates/gwiki/src/ingest/pdf/mod.rs:26-32]
  - Signature: `struct PdfMarkdownSummary {`
  - Purpose: `PdfMarkdownSummary` is a metadata struct that records PDF processing results, including page count, text layer presence, vision model usage, and detected document degradations. [crates/gwiki/src/ingest/pdf/mod.rs:26-32]
- `PdfRenderOutcome` (class) component `PdfRenderOutcome [class]` (`fedd563a-dc81-5a0a-8822-0018a1961ec8`) lines 35-38 [crates/gwiki/src/ingest/pdf/mod.rs:35-38]
  - Signature: `struct PdfRenderOutcome {`
  - Purpose: `PdfRenderOutcome` is a struct that encapsulates the result of rendering a PDF document, containing a vector of rendered pages and optional metadata describing any document degradation encountered. [crates/gwiki/src/ingest/pdf/mod.rs:35-38]

