---
title: crates/gwiki/src/ingest/pdf/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/mod.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Overview

`crates/gwiki/src/ingest/pdf/mod.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/pdf/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `PdfPageMarkdown` | class | The 'PdfPageMarkdown' struct represents a single page of a PDF document, containing its 1-based page number and the corresponding Markdown representation of its content. [crates/gwiki/src/ingest/pdf/mod.rs:22-25] |
| `PdfMarkdownSummary` | class | The 'PdfMarkdownSummary' struct represents metadata for a processed PDF-to-Markdown document, capturing its page count, text layer and vision utilization status, the optional model identifier, and a vector of detected document degradations. [crates/gwiki/src/ingest/pdf/mod.rs:28-34] |
| `PdfRenderOutcome` | class | The 'PdfRenderOutcome' struct represents the result of a PDF rendering operation, containing a vector of rendered pages and an optional document degradation descriptor. [crates/gwiki/src/ingest/pdf/mod.rs:37-40] |

