---
title: crates/gwiki/src/ingest/pdf/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/types.rs
  ranges:
  - 11-14
  - 18-24
  - 28-33
  - 37-43
  - 47-49
  - 52-56
  - 60-81
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/pdf/types.rs:11-14](crates/gwiki/src/ingest/pdf/types.rs#L11-L14), [crates/gwiki/src/ingest/pdf/types.rs:18-24](crates/gwiki/src/ingest/pdf/types.rs#L18-L24), [crates/gwiki/src/ingest/pdf/types.rs:28-33](crates/gwiki/src/ingest/pdf/types.rs#L28-L33), [crates/gwiki/src/ingest/pdf/types.rs:37-43](crates/gwiki/src/ingest/pdf/types.rs#L37-L43), [crates/gwiki/src/ingest/pdf/types.rs:47-49](crates/gwiki/src/ingest/pdf/types.rs#L47-L49), [crates/gwiki/src/ingest/pdf/types.rs:52-56](crates/gwiki/src/ingest/pdf/types.rs#L52-L56), [crates/gwiki/src/ingest/pdf/types.rs:60-81](crates/gwiki/src/ingest/pdf/types.rs#L60-L81)

</details>

# crates/gwiki/src/ingest/pdf/types.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the core PDF ingest data model and timestamp parsing used by the PDF pipeline. It provides `PdfPage` for numbered extracted text, `PdfSnapshot` and `PdfFileSnapshot` for storing PDF metadata plus bytes and, in the full snapshot, parsed pages, `PdfRenderedPage` for rasterized page images with optional dimensions, and `PdfIngestOptions` with a default render DPI of 150. The `pdf_fetched_at` helper, enabled under the `documents` feature, normalizes configured fetch times from either `unix-ms:` values or RFC3339 strings into `DateTime<Utc>`, returning config errors when parsing fails.
[crates/gwiki/src/ingest/pdf/types.rs:11-14]
[crates/gwiki/src/ingest/pdf/types.rs:18-24]
[crates/gwiki/src/ingest/pdf/types.rs:28-33]
[crates/gwiki/src/ingest/pdf/types.rs:37-43]
[crates/gwiki/src/ingest/pdf/types.rs:47-49]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `PdfPage` | class | `pub struct PdfPage {` | `PdfPage [class]` | `06e7b5af-6295-5454-9a0c-135ef30fb656` | 11-14 [crates/gwiki/src/ingest/pdf/types.rs:11-14] | Indexed class `PdfPage` in `crates/gwiki/src/ingest/pdf/types.rs`. [crates/gwiki/src/ingest/pdf/types.rs:11-14] |
| `PdfSnapshot` | class | `pub struct PdfSnapshot {` | `PdfSnapshot [class]` | `119c895c-c437-5ba5-bff3-6ae273577bcd` | 18-24 [crates/gwiki/src/ingest/pdf/types.rs:18-24] | Indexed class `PdfSnapshot` in `crates/gwiki/src/ingest/pdf/types.rs`. [crates/gwiki/src/ingest/pdf/types.rs:18-24] |
| `PdfFileSnapshot` | class | `pub struct PdfFileSnapshot {` | `PdfFileSnapshot [class]` | `ba06730f-3be5-5ca5-a1d2-59c0ff9bebdf` | 28-33 [crates/gwiki/src/ingest/pdf/types.rs:28-33] | Indexed class `PdfFileSnapshot` in `crates/gwiki/src/ingest/pdf/types.rs`. [crates/gwiki/src/ingest/pdf/types.rs:28-33] |
| `PdfRenderedPage` | class | `pub struct PdfRenderedPage {` | `PdfRenderedPage [class]` | `b17a4ad9-249b-56c7-886d-2facf08acb1d` | 37-43 [crates/gwiki/src/ingest/pdf/types.rs:37-43] | Indexed class `PdfRenderedPage` in `crates/gwiki/src/ingest/pdf/types.rs`. [crates/gwiki/src/ingest/pdf/types.rs:37-43] |
| `PdfIngestOptions` | class | `pub struct PdfIngestOptions {` | `PdfIngestOptions [class]` | `04751078-7613-5241-bda8-4cb2d1b12860` | 47-49 [crates/gwiki/src/ingest/pdf/types.rs:47-49] | Indexed class `PdfIngestOptions` in `crates/gwiki/src/ingest/pdf/types.rs`. [crates/gwiki/src/ingest/pdf/types.rs:47-49] |
| `PdfIngestOptions::default` | method | `fn default() -> Self {` | `PdfIngestOptions::default [method]` | `05f36e35-34fa-5a36-b3aa-944c4e78bf21` | 52-56 [crates/gwiki/src/ingest/pdf/types.rs:52-56] | Indexed method `PdfIngestOptions::default` in `crates/gwiki/src/ingest/pdf/types.rs`. [crates/gwiki/src/ingest/pdf/types.rs:52-56] |
| `pdf_fetched_at` | function | `pub(crate) fn pdf_fetched_at(value: &str) -> Result<DateTime<Utc>, crate::WikiError> {` | `pdf_fetched_at [function]` | `26d96b42-6ba7-5ef7-b4a4-9915f3170db0` | 60-81 [crates/gwiki/src/ingest/pdf/types.rs:60-81] | Indexed function `pdf_fetched_at` in `crates/gwiki/src/ingest/pdf/types.rs`. [crates/gwiki/src/ingest/pdf/types.rs:60-81] |
