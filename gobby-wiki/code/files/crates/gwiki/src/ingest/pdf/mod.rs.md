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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/pdf/mod.rs:22-25](crates/gwiki/src/ingest/pdf/mod.rs#L22-L25), [crates/gwiki/src/ingest/pdf/mod.rs:28-34](crates/gwiki/src/ingest/pdf/mod.rs#L28-L34), [crates/gwiki/src/ingest/pdf/mod.rs:37-40](crates/gwiki/src/ingest/pdf/mod.rs#L37-L40)

</details>

# crates/gwiki/src/ingest/pdf/mod.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

This module is the PDF ingestion entry point for `gwiki`, wiring together text-layer extraction, page rendering, and vision-assisted Markdown generation. It exposes documents-feature-gated ingest APIs and types, while the internal structs `PdfPageMarkdown`, `PdfMarkdownSummary`, and `PdfRenderOutcome` act as small data carriers for per-page Markdown, overall ingestion summary state, and rendered-page results with any degradation, tying the render, markdown, and ingest submodules together.
[crates/gwiki/src/ingest/pdf/mod.rs:22-25]
[crates/gwiki/src/ingest/pdf/mod.rs:28-34]
[crates/gwiki/src/ingest/pdf/mod.rs:37-40]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `PdfPageMarkdown` | class | `struct PdfPageMarkdown {` | `PdfPageMarkdown [class]` | `2021a76a-b2b1-532a-8dd0-5615e7b55741` | 22-25 [crates/gwiki/src/ingest/pdf/mod.rs:22-25] | Indexed class `PdfPageMarkdown` in `crates/gwiki/src/ingest/pdf/mod.rs`. [crates/gwiki/src/ingest/pdf/mod.rs:22-25] |
| `PdfMarkdownSummary` | class | `struct PdfMarkdownSummary {` | `PdfMarkdownSummary [class]` | `39ec77cb-ca8d-51b8-9930-d61f4bc795bc` | 28-34 [crates/gwiki/src/ingest/pdf/mod.rs:28-34] | Indexed class `PdfMarkdownSummary` in `crates/gwiki/src/ingest/pdf/mod.rs`. [crates/gwiki/src/ingest/pdf/mod.rs:28-34] |
| `PdfRenderOutcome` | class | `struct PdfRenderOutcome {` | `PdfRenderOutcome [class]` | `3c26316a-01a4-5e2e-b1f7-a3745019079a` | 37-40 [crates/gwiki/src/ingest/pdf/mod.rs:37-40] | Indexed class `PdfRenderOutcome` in `crates/gwiki/src/ingest/pdf/mod.rs`. [crates/gwiki/src/ingest/pdf/mod.rs:37-40] |
