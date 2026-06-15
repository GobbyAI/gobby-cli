---
title: crates/gwiki/src/ingest/file/dispatch.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/dispatch.rs
  ranges:
  - 42-224
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file/dispatch.rs

Module: [[code/modules/crates/gwiki/src/ingest/file|crates/gwiki/src/ingest/file]]

## Purpose

Dispatches local source files to the correct no-index ingestion pipeline based on detected `SourceKind`, then attaches replay metadata and returns a unified `LocalFileIngestResult`. `ingest_path_without_index` resolves the file name and vault-relative location, reads the file when needed, and routes audio, image, video, document, PDF, or generic content through the corresponding ingest helpers, using AI context and feature-gated document/vision logic where available. After ingestion it computes the appropriate degradation or transcription summaries and preserves the fetched-at/source metadata so callers get a single normalized result regardless of file type. [crates/gwiki/src/ingest/file/dispatch.rs:42-224]

## API Symbols

- `ingest_path_without_index` (function) component `ingest_path_without_index [function]` (`fe5e6054-2c45-5357-bfbb-427c3064b3e3`) lines 42-224 [crates/gwiki/src/ingest/file/dispatch.rs:42-224]
  - Signature: `pub(crate) fn ingest_path_without_index(`
  - Purpose: Reads a local file at 'path', infers its 'SourceKind', and dispatches to the corresponding no-index ingestion pipeline (such as audio transcription or image vision), returning a 'LocalFileIngestResult' with any transcription/degradation summaries. [crates/gwiki/src/ingest/file/dispatch.rs:42-224]

