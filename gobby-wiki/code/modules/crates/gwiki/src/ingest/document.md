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

## `crates/gwiki/src/ingest/document`

This module is the document-ingestion layer for gwiki, responsible for converting raw binary assets — HTML pages, Word documents, PowerPoint presentations, and spreadsheets — into structured `DocumentExtraction` results that the wider wiki index can consume. The module root (`mod.rs`) declares the shared data model and the two primary entry points (`ingest_document` and `ingest_document_without_index`), then delegates format-specific work to three internal submodules: `html`, `office`, and `render`. The `DocumentExtractor` trait (mod.rs:62–64) provides an extension point for alternate extraction back-ends, and `DocumentEndpoint` (mod.rs:66–70) reserves a CLI/API split path without yet exposing it.

The ingestion flow begins when a caller passes a `DocumentSnapshot` — carrying the raw bytes, file name, fetched-at timestamp, and a `SourceKind` discriminator — to `ingest_document_without_index`. That function selects the appropriate extractor, writes the raw asset and a derived Markdown representation via `write_asset` / `write_raw_markdown`, and returns a `DocumentIngestResult` containing paths for the raw, asset, and derived files plus an optional `DocumentDegradation`. Callers that also need the search index updated use the top-level `ingest_document`, which additionally calls `index_after_ingest` (mod.rs:80–85). HTML extraction (`html.rs:8–39`) uses the `scraper` crate to walk visible DOM nodes, skipping `<head>`, `<script>`, and `<style>`, then joins text parts with newlines and normalises them. When the resulting Markdown is empty the extractor still succeeds but attaches a `DocumentDegradation` with failure mode `HtmlNoContent` (html.rs:20–29). Office extraction (`office.rs:40–52`) dispatches on file extension to `extract_docx`, `extract_pptx`, or `extract_spreadsheet`, all of which parse ZIP-based Office Open XML using `quick-xml` and `calamine`.

A key design concern in `office.rs` is **bounded reading**: every ZIP entry is capped to `MAX_ENTRY_BYTES` (5 MiB), slide count is capped to `MAX_SLIDES` (200), and spreadsheet dimensions are capped to `MAX_SHEETS × MAX_ROWS_PER_SHEET × MAX_COLUMNS_PER_SHEET`. Each limit ships with a compile-time default and can be overridden at process start via a `LazyLock`-backed environment variable (office.rs:29–36). Exceeding a bound produces a `DocumentDegradation` rather than a hard error, so partial content is still indexed. The `render` submodule (9 symbols) handles the conversion of extracted text into final Markdown, including the `markdown_table_handles_empty_rows` behaviour exercised in the test suite.

The test module (`tests.rs`) provides in-process ZIP builders (`zip_bytes`, `sample_docx`, `sample_pptx`, `sample_xlsx`) and adversarial fixtures (`oversized_pptx`, `oversized_xlsx`, `xlsx_with_sheet_data`) that exercise degradation paths. Key behavioural tests confirm that bounds produce uniform metadata (`office_html_degradation_uses_uniform_metadata`), that ZIP reads are capped (`office_zip_reads_are_bounded`), that slide and table truncation trigger degradation (`pptx_slide_count_is_bounded`, `xlsx_table_bounds_report_degradation`), and that HTML text nodes are correctly combined (`html_extraction_combines_inline_text_nodes`).

---

### Public API symbols (mod.rs)

| Symbol | Kind | Notes |
|---|---|---|
| `DocumentSnapshot` | struct | Raw bytes + metadata for a fetched document (mod.rs:21–28) |
| `DocumentIngestResult` | struct | Paths and optional degradation returned after ingest (mod.rs:30–37) |
| `DocumentExtraction` | struct | Extracted title, Markdown, unit counts, degradation (mod.rs:51–58) |
| `DocumentRequest<'a>` | struct | Borrowed view passed to an extractor (mod.rs:47–51) |
| `DocumentExtractor` | trait | Single `extract` method; implemented by `LocalDocumentExtractor` (mod.rs:62–64) |
| `DocumentEndpoint<'a>` | enum | `Available` / `Unavailable` split for CLI vs API paths (mod.rs:66–70) |
| `ingest_document` | fn | Full ingest + index rebuild (mod.rs:80–85) |
| `ingest_document_without_index` | fn | Ingest only, no index rebuild (mod.rs:87+) |

---

### Supported document formats (office.rs:40–52)

| Extension | Extractor |
|---|---|
| `.docx` | `extract_docx` |
| `.pptx` | `extract_pptx` |
| `.xlsx` / `.xls` / `.ods` | `extract_spreadsheet` |
| `.html` / `.htm` | `extract_html_document` (html.rs) |

---

### Extraction bounds and environment overrides (office.rs:14–36)

| Constant | Default | Environment variable |
|---|---|---|
| `MAX_ENTRY_BYTES` | 5 MiB | `OFFICE_MAX_ENTRY_BYTES` |
| `MAX_SLIDES` | 200 | `OFFICE_MAX_SLIDES` |
| `MAX_SHEETS` | 8 | *(no override; compile-time only)* |
| `MAX_ROWS_PER_SHEET` | 64 | `OFFICE_MAX_ROWS_PER_SHEET` |
| `MAX_COLUMNS_PER_SHEET` | 16 | `OFFICE_MAX_COLUMNS_PER_SHEET` |
[crates/gwiki/src/ingest/document/html.rs:8-39]
[crates/gwiki/src/ingest/document/mod.rs:21-27]
[crates/gwiki/src/ingest/document/office.rs:39-52]
[crates/gwiki/src/ingest/document/render.rs:11-33]
[crates/gwiki/src/ingest/document/tests.rs:9-18]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/document/html.rs\|crates/gwiki/src/ingest/document/html.rs]] | `crates/gwiki/src/ingest/document/html.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/mod.rs\|crates/gwiki/src/ingest/document/mod.rs]] | `crates/gwiki/src/ingest/document/mod.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/office.rs\|crates/gwiki/src/ingest/document/office.rs]] | `crates/gwiki/src/ingest/document/office.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/render.rs\|crates/gwiki/src/ingest/document/render.rs]] | `crates/gwiki/src/ingest/document/render.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/tests.rs\|crates/gwiki/src/ingest/document/tests.rs]] | `crates/gwiki/src/ingest/document/tests.rs` exposes 16 indexed API symbols. |

