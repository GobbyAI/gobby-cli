---
title: crates/gwiki/src/ingest/pdf/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/pdf/render.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/pdf/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `extract_text_layer_pages` | function | This function extracts the text layer from an in-memory PDF byte slice, maps each page to a 1-indexed 'PdfPage' struct, and returns a vector of these pages or a 'WikiError::InvalidInput' error upon failure. [crates/gwiki/src/ingest/pdf/render.rs:23-39] |
| `render_pdf_pages` | function | This function loads a PDF document from a byte snapshot using Pdfium, renders its pages up to a maximum page and byte budget as PNG images at the specified DPI, and returns a 'PdfRenderOutcome' containing the successfully rendered pages and any budget degradation status. [crates/gwiki/src/ingest/pdf/render.rs:42-94] |
| `next_rendered_byte_total` | function | Computes the sum of the current byte count and additional page bytes using overflow-safe addition, returning the new total wrapped in 'Some' if it is less than or equal to 'MAX_RENDERED_PDF_TOTAL_BYTES', and 'None' on overflow or limit violation. [crates/gwiki/src/ingest/pdf/render.rs:97-100] |
| `pdf_render_budget_degradation` | function | This function constructs and returns a 'DocumentDegradation' instance indicating that the PDF rendering budget was exceeded, populated with a page-based unit count and a formatted message detailing the rendered byte count and budget limitations. [crates/gwiki/src/ingest/pdf/render.rs:103-114] |
| `bundled_pdfium` | function | This function ensures the availability of the bundled Pdfium library, dynamically binds to its binary path, and returns an initialized 'Pdfium' instance, mapping any resolution or library binding errors to a 'WikiError::InvalidInput'. [crates/gwiki/src/ingest/pdf/render.rs:117-128] |
| `points_to_pixels` | function | The 'points_to_pixels' function converts a measurement in points to its pixel equivalent based on a specified dots per inch (DPI), rounding the result to the nearest integer with a guaranteed minimum value of 1. [crates/gwiki/src/ingest/pdf/render.rs:131-133] |
| `bitmap_dimension_to_u32` | function | The 'bitmap_dimension_to_u32' function validates and converts a signed 32-bit integer representing a bitmap dimension to an unsigned 32-bit integer, returning a 'WikiError' if the input is non-positive or exceeds the maximum value of a 'u32'. [crates/gwiki/src/ingest/pdf/render.rs:136-144] |
| `encode_png_rgba` | function | The 'encode_png_rgba' function encodes raw 8-bit RGBA image byte data of the specified dimensions into a PNG-formatted byte vector, returning a 'WikiError' if the encoding process fails. [crates/gwiki/src/ingest/pdf/render.rs:147-166] |
| `pdfium_error` | function | The 'pdfium_error' function converts any error type implementing 'std::fmt::Display' into a 'WikiError::InvalidInput' enum variant with the 'field' set to '"pdf"' and a formatted message indicating that the PDF page rendering failed. [crates/gwiki/src/ingest/pdf/render.rs:169-174] |

_Verified by 2 in-file unit tests._

