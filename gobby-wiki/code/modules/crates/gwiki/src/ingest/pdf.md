---
title: crates/gwiki/src/ingest/pdf
type: code_module
provenance:
- file: crates/gwiki/src/ingest/pdf/ingest.rs
  ranges:
  - 23-37
  - 41-52
  - 55-108
  - 111-128
  - 131-146
  - 149-220
  - 223-247
  - 250-257
  - 260-266
- file: crates/gwiki/src/ingest/pdf/markdown.rs
  ranges:
  - 15-89
  - 92-107
  - 110-135
  - 138-156
  - 159-239
  - 242-264
  - 267-272
  - 275-295
  - 298-319
  - 322-328
  - 331-335
  - 338-344
  - 351-360
  - 363-375
- file: crates/gwiki/src/ingest/pdf/mod.rs
  ranges:
  - 22-25
  - 28-34
  - 37-40
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
- file: crates/gwiki/src/ingest/pdf/tests.rs
  ranges:
  - '21'
  - 23-27
  - 30-59
  - 63-65
  - 69-74
  - 77-137
  - 140-175
  - 178-182
  - 185-231
  - 234-289
  - 292-324
  - 327-331
  - 334-442
  - 446-453
- file: crates/gwiki/src/ingest/pdf/text.rs
  ranges:
  - 4-25
  - 32-36
  - 39-49
  - 52-54
  - 57-59
  - 62-64
  - 67-69
  - 72-74
  - 77-82
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

- [crates/gwiki/src/ingest/pdf/ingest.rs:23-37](crates/gwiki/src/ingest/pdf/ingest.rs#L23-L37), [crates/gwiki/src/ingest/pdf/ingest.rs:41-52](crates/gwiki/src/ingest/pdf/ingest.rs#L41-L52), [crates/gwiki/src/ingest/pdf/ingest.rs:55-108](crates/gwiki/src/ingest/pdf/ingest.rs#L55-L108), [crates/gwiki/src/ingest/pdf/ingest.rs:111-128](crates/gwiki/src/ingest/pdf/ingest.rs#L111-L128), [crates/gwiki/src/ingest/pdf/ingest.rs:131-146](crates/gwiki/src/ingest/pdf/ingest.rs#L131-L146), [crates/gwiki/src/ingest/pdf/ingest.rs:149-220](crates/gwiki/src/ingest/pdf/ingest.rs#L149-L220), [crates/gwiki/src/ingest/pdf/ingest.rs:223-247](crates/gwiki/src/ingest/pdf/ingest.rs#L223-L247), [crates/gwiki/src/ingest/pdf/ingest.rs:250-257](crates/gwiki/src/ingest/pdf/ingest.rs#L250-L257), [crates/gwiki/src/ingest/pdf/ingest.rs:260-266](crates/gwiki/src/ingest/pdf/ingest.rs#L260-L266)
- [crates/gwiki/src/ingest/pdf/markdown.rs:15-89](crates/gwiki/src/ingest/pdf/markdown.rs#L15-L89), [crates/gwiki/src/ingest/pdf/markdown.rs:92-107](crates/gwiki/src/ingest/pdf/markdown.rs#L92-L107), [crates/gwiki/src/ingest/pdf/markdown.rs:110-135](crates/gwiki/src/ingest/pdf/markdown.rs#L110-L135), [crates/gwiki/src/ingest/pdf/markdown.rs:138-156](crates/gwiki/src/ingest/pdf/markdown.rs#L138-L156), [crates/gwiki/src/ingest/pdf/markdown.rs:159-239](crates/gwiki/src/ingest/pdf/markdown.rs#L159-L239), [crates/gwiki/src/ingest/pdf/markdown.rs:242-264](crates/gwiki/src/ingest/pdf/markdown.rs#L242-L264), [crates/gwiki/src/ingest/pdf/markdown.rs:267-272](crates/gwiki/src/ingest/pdf/markdown.rs#L267-L272), [crates/gwiki/src/ingest/pdf/markdown.rs:275-295](crates/gwiki/src/ingest/pdf/markdown.rs#L275-L295), [crates/gwiki/src/ingest/pdf/markdown.rs:298-319](crates/gwiki/src/ingest/pdf/markdown.rs#L298-L319), [crates/gwiki/src/ingest/pdf/markdown.rs:322-328](crates/gwiki/src/ingest/pdf/markdown.rs#L322-L328), [crates/gwiki/src/ingest/pdf/markdown.rs:331-335](crates/gwiki/src/ingest/pdf/markdown.rs#L331-L335), [crates/gwiki/src/ingest/pdf/markdown.rs:338-344](crates/gwiki/src/ingest/pdf/markdown.rs#L338-L344), [crates/gwiki/src/ingest/pdf/markdown.rs:351-360](crates/gwiki/src/ingest/pdf/markdown.rs#L351-L360), [crates/gwiki/src/ingest/pdf/markdown.rs:363-375](crates/gwiki/src/ingest/pdf/markdown.rs#L363-L375)
- [crates/gwiki/src/ingest/pdf/mod.rs:22-25](crates/gwiki/src/ingest/pdf/mod.rs#L22-L25), [crates/gwiki/src/ingest/pdf/mod.rs:28-34](crates/gwiki/src/ingest/pdf/mod.rs#L28-L34), [crates/gwiki/src/ingest/pdf/mod.rs:37-40](crates/gwiki/src/ingest/pdf/mod.rs#L37-L40)
- [crates/gwiki/src/ingest/pdf/render.rs:23-39](crates/gwiki/src/ingest/pdf/render.rs#L23-L39), [crates/gwiki/src/ingest/pdf/render.rs:42-94](crates/gwiki/src/ingest/pdf/render.rs#L42-L94), [crates/gwiki/src/ingest/pdf/render.rs:97-100](crates/gwiki/src/ingest/pdf/render.rs#L97-L100), [crates/gwiki/src/ingest/pdf/render.rs:103-114](crates/gwiki/src/ingest/pdf/render.rs#L103-L114), [crates/gwiki/src/ingest/pdf/render.rs:117-128](crates/gwiki/src/ingest/pdf/render.rs#L117-L128), [crates/gwiki/src/ingest/pdf/render.rs:131-133](crates/gwiki/src/ingest/pdf/render.rs#L131-L133), [crates/gwiki/src/ingest/pdf/render.rs:136-144](crates/gwiki/src/ingest/pdf/render.rs#L136-L144), [crates/gwiki/src/ingest/pdf/render.rs:147-166](crates/gwiki/src/ingest/pdf/render.rs#L147-L166), [crates/gwiki/src/ingest/pdf/render.rs:169-174](crates/gwiki/src/ingest/pdf/render.rs#L169-L174), [crates/gwiki/src/ingest/pdf/render.rs:181-191](crates/gwiki/src/ingest/pdf/render.rs#L181-L191), [crates/gwiki/src/ingest/pdf/render.rs:195-202](crates/gwiki/src/ingest/pdf/render.rs#L195-L202)
- [crates/gwiki/src/ingest/pdf/tests.rs:21](crates/gwiki/src/ingest/pdf/tests.rs#L21), [crates/gwiki/src/ingest/pdf/tests.rs:23-27](crates/gwiki/src/ingest/pdf/tests.rs#L23-L27), [crates/gwiki/src/ingest/pdf/tests.rs:30-59](crates/gwiki/src/ingest/pdf/tests.rs#L30-L59), [crates/gwiki/src/ingest/pdf/tests.rs:63-65](crates/gwiki/src/ingest/pdf/tests.rs#L63-L65), [crates/gwiki/src/ingest/pdf/tests.rs:69-74](crates/gwiki/src/ingest/pdf/tests.rs#L69-L74), [crates/gwiki/src/ingest/pdf/tests.rs:77-137](crates/gwiki/src/ingest/pdf/tests.rs#L77-L137), [crates/gwiki/src/ingest/pdf/tests.rs:140-175](crates/gwiki/src/ingest/pdf/tests.rs#L140-L175), [crates/gwiki/src/ingest/pdf/tests.rs:178-182](crates/gwiki/src/ingest/pdf/tests.rs#L178-L182), [crates/gwiki/src/ingest/pdf/tests.rs:185-231](crates/gwiki/src/ingest/pdf/tests.rs#L185-L231), [crates/gwiki/src/ingest/pdf/tests.rs:234-289](crates/gwiki/src/ingest/pdf/tests.rs#L234-L289), [crates/gwiki/src/ingest/pdf/tests.rs:292-324](crates/gwiki/src/ingest/pdf/tests.rs#L292-L324), [crates/gwiki/src/ingest/pdf/tests.rs:327-331](crates/gwiki/src/ingest/pdf/tests.rs#L327-L331), [crates/gwiki/src/ingest/pdf/tests.rs:334-442](crates/gwiki/src/ingest/pdf/tests.rs#L334-L442), [crates/gwiki/src/ingest/pdf/tests.rs:446-453](crates/gwiki/src/ingest/pdf/tests.rs#L446-L453)
- [crates/gwiki/src/ingest/pdf/text.rs:4-25](crates/gwiki/src/ingest/pdf/text.rs#L4-L25), [crates/gwiki/src/ingest/pdf/text.rs:32-36](crates/gwiki/src/ingest/pdf/text.rs#L32-L36), [crates/gwiki/src/ingest/pdf/text.rs:39-49](crates/gwiki/src/ingest/pdf/text.rs#L39-L49), [crates/gwiki/src/ingest/pdf/text.rs:52-54](crates/gwiki/src/ingest/pdf/text.rs#L52-L54), [crates/gwiki/src/ingest/pdf/text.rs:57-59](crates/gwiki/src/ingest/pdf/text.rs#L57-L59), [crates/gwiki/src/ingest/pdf/text.rs:62-64](crates/gwiki/src/ingest/pdf/text.rs#L62-L64), [crates/gwiki/src/ingest/pdf/text.rs:67-69](crates/gwiki/src/ingest/pdf/text.rs#L67-L69), [crates/gwiki/src/ingest/pdf/text.rs:72-74](crates/gwiki/src/ingest/pdf/text.rs#L72-L74), [crates/gwiki/src/ingest/pdf/text.rs:77-82](crates/gwiki/src/ingest/pdf/text.rs#L77-L82)
- [crates/gwiki/src/ingest/pdf/types.rs:11-14](crates/gwiki/src/ingest/pdf/types.rs#L11-L14), [crates/gwiki/src/ingest/pdf/types.rs:18-24](crates/gwiki/src/ingest/pdf/types.rs#L18-L24), [crates/gwiki/src/ingest/pdf/types.rs:28-33](crates/gwiki/src/ingest/pdf/types.rs#L28-L33), [crates/gwiki/src/ingest/pdf/types.rs:37-43](crates/gwiki/src/ingest/pdf/types.rs#L37-L43), [crates/gwiki/src/ingest/pdf/types.rs:47-49](crates/gwiki/src/ingest/pdf/types.rs#L47-L49), [crates/gwiki/src/ingest/pdf/types.rs:52-56](crates/gwiki/src/ingest/pdf/types.rs#L52-L56), [crates/gwiki/src/ingest/pdf/types.rs:60-81](crates/gwiki/src/ingest/pdf/types.rs#L60-L81)

</details>

# crates/gwiki/src/ingest/pdf

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

The `crates/gwiki/src/ingest/pdf` module manages the ingestion of PDF documents into the `gwiki` platform, transforming raw document bytes or page snapshots into structured, metadata-rich Markdown pages. Its primary responsibilities include native text-layer extraction, page rendering via a bundled Pdfium runtime, and vision-assisted OCR processing for visual or scanned pages [crates/gwiki/src/ingest/pdf/mod.rs:22-25, crates/gwiki/src/ingest/pdf/render.rs:42-94, crates/gwiki/src/ingest/pdf/tests.rs:30-59]. During extraction, page text is sanitized and normalized by grouping consecutive non-blank lines into cohesive paragraphs separated by double newlines [crates/gwiki/src/ingest/pdf/text.rs:4-25]. It enforces strict resource limits—including maximum page budgets and bitmap memory allocations—translating third-party library errors into standard wiki failures and tracking non-fatal document degradation notes in the final Markdown output [crates/gwiki/src/ingest/pdf/render.rs:23-39, crates/gwiki/src/ingest/pdf/render.rs:117-128, crates/gwiki/src/ingest/pdf/markdown.rs:1-12].

The ingestion flow is orchestrated within the `ingest` submodule via key entry points like `ingest_pages` or `ingest_pdf_file` . This pipeline coordinates document loading, text layer extraction, and image rendering before delegating final document layout and metadata assembly to the `markdown` submodule . The module relies on several crucial data carriers, such as `PdfPageMarkdown` and `PdfMarkdownSummary`, to share page content and pipeline degradation states across components [crates/gwiki/src/ingest/pdf/mod.rs:28-34]. It collaborates with `WikiIndexStore` to execute vault indexing operations  and utilizes `VisionClient` endpoints to obtain visual descriptions and OCR text [crates/gwiki/src/ingest/pdf/tests.rs:30-59].

### Public API Symbols and Components

| Public API Symbol | Category | Description | Citation |
| --- | --- | --- | --- |
| `ingest_pages` | Function | Ingests plain page snapshots and routes them with optional vision extraction |  |
| `ingest_pdf_file` | Function | Ingests complete PDF files, extracts text, handles rendering/OCR, and triggers vault re-indexing |  |
| `pdf_fetched_at` | Function | Normalizes timestamp configurations from unix-ms or RFC3339 format into a UTC DateTime | [crates/gwiki/src/ingest/pdf/types.rs:47-49] |
| `PdfPageMarkdown` | Struct | Data carrier holding the final Markdown output and metadata for a single PDF page | [crates/gwiki/src/ingest/pdf/mod.rs:28-34] |
| `PdfMarkdownSummary` | Struct | Data carrier representing overall ingestion results, including degradation and model notes | [crates/gwiki/src/ingest/pdf/mod.rs:28-34] |
| `PdfRenderOutcome` | Struct | Represents the final output of the rendering helper pipeline, detailing rendered page items | [crates/gwiki/src/ingest/pdf/mod.rs:37-40] |

### Internal Constants and Resource Budgets

| Constant / Limit | Value | Description | Citation |
| --- | --- | --- | --- |
| `DEFAULT_PDF_RENDER_DPI` | 150 | Default resolution in DPI for rasterizing PDF pages to images | [crates/gwiki/src/ingest/pdf/types.rs:47-49] |
| `MAX_RENDERED_PDF_PAGES` | 32 | Maximum page budget allowed for rendering operations in a single PDF | [crates/gwiki/src/ingest/pdf/render.rs:23-39] |
| `MAX_RENDERED_PDF_TOTAL_BYTES` | 33,554,432 (32 MB) | Upper memory allocation threshold for rendering operations | [crates/gwiki/src/ingest/pdf/render.rs:23-39] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/pdf/ingest.rs\|crates/gwiki/src/ingest/pdf/ingest.rs]] | This file implements the PDF ingestion flow for gwiki. It exposes entry points that ingest plain page snapshots or full PDF files, optionally re-indexing afterward, then routes through text-layer extraction or vision-assisted page processing to produce ingest results while collecting degradations and preserving raw assets as needed. The helpers split the work into “with index” and “without index” variants, combine rendered/normalized page content into markdown, and provide rollback and cleanup routines for undoing a registered PDF source and deleting temporary PDF artifacts with a small detail formatter for cleanup reporting. [crates/gwiki/src/ingest/pdf/ingest.rs:23-37] [crates/gwiki/src/ingest/pdf/ingest.rs:41-52] [crates/gwiki/src/ingest/pdf/ingest.rs:55-108] [crates/gwiki/src/ingest/pdf/ingest.rs:111-128] [crates/gwiki/src/ingest/pdf/ingest.rs:131-146] |
| [[code/files/crates/gwiki/src/ingest/pdf/markdown.rs\|crates/gwiki/src/ingest/pdf/markdown.rs]] | This file assembles the final Markdown representation for ingested PDFs. `render_pdf_markdown` builds a document-level Markdown page with metadata, title, degradation notes, and per-page content, while helper functions sanitize page Markdown, neutralize page-marker variants, detect horizontal rules, and merge page sections into a single coherent output. It also supports OCR/vision integration by selecting the vision model, extracting page-level vision data, deriving rendered asset names and paths, and deduplicating overlapping OCR text so repeated content is not emitted twice. The included tests cover marker neutralization and OCR overlap-key behavior. [crates/gwiki/src/ingest/pdf/markdown.rs:15-89] [crates/gwiki/src/ingest/pdf/markdown.rs:92-107] [crates/gwiki/src/ingest/pdf/markdown.rs:110-135] [crates/gwiki/src/ingest/pdf/markdown.rs:138-156] [crates/gwiki/src/ingest/pdf/markdown.rs:159-239] |
| [[code/files/crates/gwiki/src/ingest/pdf/mod.rs\|crates/gwiki/src/ingest/pdf/mod.rs]] | This module is the PDF ingestion entry point for `gwiki`, wiring together text-layer extraction, page rendering, and vision-assisted Markdown generation. It exposes documents-feature-gated ingest APIs and types, while the internal structs `PdfPageMarkdown`, `PdfMarkdownSummary`, and `PdfRenderOutcome` act as small data carriers for per-page Markdown, overall ingestion summary state, and rendered-page results with any degradation, tying the render, markdown, and ingest submodules together. [crates/gwiki/src/ingest/pdf/mod.rs:22-25] [crates/gwiki/src/ingest/pdf/mod.rs:28-34] [crates/gwiki/src/ingest/pdf/mod.rs:37-40] |
| [[code/files/crates/gwiki/src/ingest/pdf/render.rs\|crates/gwiki/src/ingest/pdf/render.rs]] | Implements PDF ingestion rendering helpers for the `documents` feature: it can extract per-page text from a PDF’s text layer, render PDF pages to images with bundled Pdfium, and package the results into `PdfRenderOutcome`. The helper functions support that pipeline by loading the embedded Pdfium runtime, converting page sizes from points to pixels, validating bitmap dimensions, encoding rendered RGBA bitmaps as PNG, and translating Pdfium failures into `WikiError`. The budget functions enforce limits on how many pages and bytes can be rendered, and the test helpers verify overflow and invalid-dimension rejection before totals are updated or values are cast. [crates/gwiki/src/ingest/pdf/render.rs:23-39] [crates/gwiki/src/ingest/pdf/render.rs:42-94] [crates/gwiki/src/ingest/pdf/render.rs:97-100] [crates/gwiki/src/ingest/pdf/render.rs:103-114] [crates/gwiki/src/ingest/pdf/render.rs:117-128] |
| [[code/files/crates/gwiki/src/ingest/pdf/tests.rs\|crates/gwiki/src/ingest/pdf/tests.rs]] | This file contains PDF-ingest tests for the `gwiki` pipeline. It defines fake `VisionClient` implementations and a timestamp helper to exercise page rendering, OCR/vision integration, markdown sanitization, page reference preservation, rollback behavior on write failures, and degradation/budget reporting, while also checking public defaults like render DPI and fetched-at parsing. [crates/gwiki/src/ingest/pdf/tests.rs:21] [crates/gwiki/src/ingest/pdf/tests.rs:23-27] [crates/gwiki/src/ingest/pdf/tests.rs:30-59] [crates/gwiki/src/ingest/pdf/tests.rs:63-65] [crates/gwiki/src/ingest/pdf/tests.rs:69-74] |
| [[code/files/crates/gwiki/src/ingest/pdf/text.rs\|crates/gwiki/src/ingest/pdf/text.rs]] | Provides PDF page-text normalization for ingestion. `normalize_page_text` runs each input line through `single_line`, drops empty or whitespace-only lines, groups consecutive nonblank lines into paragraphs joined with spaces, and emits those paragraphs separated by double newlines. The test module verifies the behavior across paragraph breaks, edge whitespace, multiple blank lines, trailing blanks, empty input, single-line input, and fully unbroken text. [crates/gwiki/src/ingest/pdf/text.rs:4-25] [crates/gwiki/src/ingest/pdf/text.rs:32-36] [crates/gwiki/src/ingest/pdf/text.rs:39-49] [crates/gwiki/src/ingest/pdf/text.rs:52-54] [crates/gwiki/src/ingest/pdf/text.rs:57-59] |
| [[code/files/crates/gwiki/src/ingest/pdf/types.rs\|crates/gwiki/src/ingest/pdf/types.rs]] | This file defines the core PDF ingest data model and timestamp parsing used by the PDF pipeline. It provides `PdfPage` for numbered extracted text, `PdfSnapshot` and `PdfFileSnapshot` for storing PDF metadata plus bytes and, in the full snapshot, parsed pages, `PdfRenderedPage` for rasterized page images with optional dimensions, and `PdfIngestOptions` with a default render DPI of 150. The `pdf_fetched_at` helper, enabled under the `documents` feature, normalizes configured fetch times from either `unix-ms:` values or RFC3339 strings into `DateTime<Utc>`, returning config errors when parsing fails. [crates/gwiki/src/ingest/pdf/types.rs:11-14] [crates/gwiki/src/ingest/pdf/types.rs:18-24] [crates/gwiki/src/ingest/pdf/types.rs:28-33] [crates/gwiki/src/ingest/pdf/types.rs:37-43] [crates/gwiki/src/ingest/pdf/types.rs:47-49] |

## Components

| Component ID |
| --- |
| `8ffb36c7-f2e2-56f3-a324-bb3c8f66a4dd` |
| `95c9dc97-74e0-5d87-a3c1-fe755428ff72` |
| `523df09f-79ca-5ea6-acf0-539f5d68ecb6` |
| `8ddf8eef-a485-5a2d-ba71-f896f29f42c6` |
| `8cf7e35a-c5a2-5626-b253-f54d87a3b81a` |
| `50cddb42-fe4a-5472-a9b8-334b7a0e7c10` |
| `4d86afff-2599-5414-9cf3-ce1e3272844f` |
| `69f90f69-6002-56a2-a801-863cff9b6905` |
| `0ecb051b-0d96-5dd6-8a20-889652d189cb` |
| `498013f6-0417-5d77-884f-5dc728e46394` |
| `017e301e-e617-58cc-b179-cb2195a4f3f0` |
| `6a95a7e1-e58c-55a8-ac11-94f20e7abbc5` |
| `4a3322af-f8bc-5dc0-a366-6e5523d13c7c` |
| `b2c5f605-b695-5f0e-9527-409a696011cf` |
| `d3218dfc-d267-5f83-a82d-8ce61012bf30` |
| `faefec51-786e-56f5-8905-c2b0856b3c9f` |
| `bfd548d1-adf4-5a06-bac3-e9f999a00d48` |
| `dca13354-ce5c-5155-a62f-8f8d836c3ca0` |
| `f14789d1-bb08-5469-86d7-0cb0cdcc0ffb` |
| `98b04f8c-8306-5266-a988-fa98f0fae810` |
| `81e990f6-f1a7-566f-888e-496dbbdd5eba` |
| `c226bd7c-7995-5f04-a7f7-c03947c53a93` |
| `fed949bf-d648-5140-b960-e6c28587c8f6` |
| `2021a76a-b2b1-532a-8dd0-5615e7b55741` |
| `39ec77cb-ca8d-51b8-9930-d61f4bc795bc` |
| `3c26316a-01a4-5e2e-b1f7-a3745019079a` |
| `078c2eba-2bec-5f7b-ba3f-8ffad07d5a3b` |
| `22444081-e1c9-5009-9694-9b16b53c3b67` |
| `ff706ec2-a5fc-531c-8b49-b717a4d9ca49` |
| `3716ca39-bc6b-58f0-a4c0-a751755ee228` |
| `f9ef1ddb-ff8e-5820-87ac-46bc6e59b01e` |
| `82620d3f-f256-5280-a998-c75e1e574b2b` |
| `3bbbf0c9-0582-5b42-b8c8-a30c260370a9` |
| `5aa764aa-8fe1-56ef-969d-e8b83d3fbbda` |
| `f8fb3dd3-beb0-5b2f-9095-fe582da03cb5` |
| `b8530802-7791-52a6-bf37-e1a6fe0dee3c` |
| `73b03882-8e07-5e33-a8a3-aadedc3ff349` |
| `be728204-9652-54d8-be56-194cd549312e` |
| `c2dc37b0-0f30-574d-800d-4e6337a5dc7e` |
| `4842ab69-0b66-5814-a7fa-c1e4a28b580f` |
| `de0178ec-0be4-5b54-968a-95dd771b403a` |
| `651c7a0e-8cc1-53c2-bbe6-52a6ad8a624c` |
| `a57807e9-26ae-5cc9-9731-cb76d1c417f3` |
| `a1621a35-c600-5cd5-a74c-fb33b24fbec1` |
| `cdd3baf6-20f1-55f7-82ad-536a53b02630` |
| `78e2f787-876d-5c9b-a1d3-960ac3859db5` |
| `fbba5051-b8e0-5e5b-a2f5-de83b98d2bca` |
| `915f2c72-e444-5f1b-bcea-44162ed440b8` |
| `c1dd5924-cdc4-5bc6-900f-f73532afc037` |
| `1e0be664-e79e-5c8c-984f-34315b94a355` |
| `8492045a-b975-52a0-a290-1b5d37027d9f` |
| `1af04065-a24d-5ec0-9a7b-1978a0f5934b` |
| `907a1b8c-f67b-5e65-8df7-7f7a2aa6e62a` |
| `4c7760f4-07a6-539a-a8d4-c84163b931ee` |
| `41bdf075-e195-5fd6-ab33-a7552152d06a` |
| `ce04a893-c469-5583-8a35-fbd456b30c8a` |
| `78c8c579-da08-566d-a140-56b096072a6a` |
| `cec6e7cb-44d8-527c-ab1c-f6f346ccd518` |
| `580faa00-90fb-5bed-a4a7-2a41b7b9b9f3` |
| `ae9d61ab-19d6-5116-a47e-126ab81e7268` |
| `cf4b7879-61e4-58a7-a115-4565247d9046` |
| `42d5bcb1-e10e-570f-bfa9-b0010ac3cad9` |
| `06e7b5af-6295-5454-9a0c-135ef30fb656` |
| `119c895c-c437-5ba5-bff3-6ae273577bcd` |
| `ba06730f-3be5-5ca5-a1d2-59c0ff9bebdf` |
| `b17a4ad9-249b-56c7-886d-2facf08acb1d` |
| `04751078-7613-5241-bda8-4cb2d1b12860` |
| `05f36e35-34fa-5a36-b3aa-944c4e78bf21` |
| `26d96b42-6ba7-5ef7-b4a4-9915f3170db0` |
