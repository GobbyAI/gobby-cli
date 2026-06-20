---
title: crates/gwiki/src/ingest/document
type: code_module
provenance:
- file: crates/gwiki/src/ingest/document/html.rs
- file: crates/gwiki/src/ingest/document/mod.rs
- file: crates/gwiki/src/ingest/document/office.rs
- file: crates/gwiki/src/ingest/document/render.rs
- file: crates/gwiki/src/ingest/document/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/document

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

The `ingest/document` module turns fetched document bytes into wiki-ingestable content while preserving the original asset. Its core types model the ingest boundary: `DocumentSnapshot` carries the source bytes and metadata, `DocumentRequest` is passed to extractors, `DocumentExtraction` returns markdown/title/unit/degradation details, and `DocumentIngestResult` links the source record with raw, asset, and derived paths (`crates/gwiki/src/ingest/document/mod.rs:1-100`). The ingest path collaborates with `crate::ingest` helpers such as `write_asset`, `write_raw_markdown`, `markdown_title`, and `index_after_ingest`, and with source/store types including `SourceManifest`, `SourceKind`, `SourceRecord`, and `WikiIndexStore` (`crates/gwiki/src/ingest/document/mod.rs:1-100`).

Extraction is split by document family. HTML ingestion decodes bytes as lossy UTF-8, parses with `scraper`, extracts a `<title>`, walks visible body text while skipping non-content regions, normalizes it to markdown text, and reports an `HtmlNoContent` degradation if nothing readable is found (`crates/gwiki/src/ingest/document/html.rs:1-100`). Office ingestion dispatches by extension: `.docx`, `.pptx`, and spreadsheet formats are extracted locally, while unsupported or missing extensions return document errors (`crates/gwiki/src/ingest/document/office.rs:1-100`). Office parsing imports ZIP, XML, and spreadsheet readers (`zip`, `quick_xml`, `calamine`) and reports degradation metadata through `crate::document::{DocumentDegradation, DocumentFailureMode, DocumentUnitCount}` (`crates/gwiki/src/ingest/document/office.rs:1-100`).

The module’s bounded extraction rules are explicit: spreadsheet sheets, rows, columns, PPTX slides, and ZIP entry bytes all have caps, with selected caps overridable through environment variables (`crates/gwiki/src/ingest/document/office.rs:14-35`). Tests construct in-memory DOCX/PPTX/XLSX-like ZIPs, exercise sample ingestion, verify HTML text joining/quote spacing, and cover degradation paths for bounded reads, slide counts, and table truncation (`crates/gwiki/src/ingest/document/tests.rs:1-100`).

| Public symbol | Role |
| --- | --- |
| `DocumentSnapshot` | Captured document source bytes and metadata |
| `DocumentIngestResult` | Ingest output paths, source record, and optional degradation |
| `DocumentRequest<'a>` | Extractor input view over filename, kind, and bytes |
| `DocumentExtraction` | Extracted title, markdown, units, and degradation |
| `DocumentExtractor` | Trait for pluggable document extraction |
| `DocumentEndpoint<'a>` | Available/unavailable extractor endpoint |
| `ingest_document` | Ingest plus index refresh |
| `ingest_document_without_index` | Ingest without reindexing |

| Bound / env key | Purpose | Default |
| --- | --- | --- |
| `MAX_SHEETS` | Spreadsheet sheets rendered | `8` |
| `MAX_ROWS_PER_SHEET` / `OFFICE_MAX_ROWS_PER_SHEET` | Rows rendered per sheet | `64` |
| `MAX_COLUMNS_PER_SHEET` / `OFFICE_MAX_COLUMNS_PER_SHEET` | Columns rendered per sheet | `16` |
| `MAX_SLIDES` / `OFFICE_MAX_SLIDES` | PPTX slides parsed | `200` |
| `MAX_ENTRY_BYTES` / `OFFICE_MAX_ENTRY_BYTES` | Uncompressed XML bytes per ZIP entry | `5 * 1024 * 1024` |
[crates/gwiki/src/ingest/document/html.rs:8-39]
[crates/gwiki/src/ingest/document/mod.rs:21-27]
[crates/gwiki/src/ingest/document/office.rs:39-52]
[crates/gwiki/src/ingest/document/tests.rs:9-18]
[crates/gwiki/src/ingest/document/render.rs:11-33]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/document/html.rs\|crates/gwiki/src/ingest/document/html.rs]] | `crates/gwiki/src/ingest/document/html.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/mod.rs\|crates/gwiki/src/ingest/document/mod.rs]] | `crates/gwiki/src/ingest/document/mod.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/office.rs\|crates/gwiki/src/ingest/document/office.rs]] | `crates/gwiki/src/ingest/document/office.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/render.rs\|crates/gwiki/src/ingest/document/render.rs]] | `crates/gwiki/src/ingest/document/render.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/tests.rs\|crates/gwiki/src/ingest/document/tests.rs]] | `crates/gwiki/src/ingest/document/tests.rs` exposes 16 indexed API symbols. |

