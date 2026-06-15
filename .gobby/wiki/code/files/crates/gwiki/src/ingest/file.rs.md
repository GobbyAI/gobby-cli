---
title: crates/gwiki/src/ingest/file.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file.rs
  ranges:
  - 34-38
  - 41-44
  - 46-59
  - 62-94
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

This file contains the local ingest entry points and small support types for turning filesystem or stdin input into wiki content. `StdinSnapshot` captures a labeled stdin payload with its fetch time, `LocalFileIngestResult` bundles an ingest result with any fidelity degradations, `ingest_path` runs path ingestion and then reindexes the store, and `ingest_stdin` registers a stdin-backed draft, writes its rendered raw markdown, reindexes, and returns the resulting record.
[crates/gwiki/src/ingest/file.rs:34-38]
[crates/gwiki/src/ingest/file.rs:41-44]
[crates/gwiki/src/ingest/file.rs:46-59]
[crates/gwiki/src/ingest/file.rs:62-94]

## API Symbols

- `StdinSnapshot` (class) component `StdinSnapshot [class]` (`b9ed125c-564c-56c9-9d5c-95c5e05d583e`) lines 34-38 [crates/gwiki/src/ingest/file.rs:34-38]
  - Signature: `pub struct StdinSnapshot {`
  - Purpose: 'StdinSnapshot' is a data container that records a labeled capture of standard input at a specific fetch time, storing the input as raw bytes. [crates/gwiki/src/ingest/file.rs:34-38]
- `LocalFileIngestResult` (class) component `LocalFileIngestResult [class]` (`8f47278b-b904-5d63-a869-3086d56965e6`) lines 41-44 [crates/gwiki/src/ingest/file.rs:41-44]
  - Signature: `pub(crate) struct LocalFileIngestResult {`
  - Purpose: 'LocalFileIngestResult' is a crate-private struct that pairs an 'IngestResult' with a list of degradation messages ('Vec<String>') describing any reduced-fidelity conditions encountered during local file ingestion. [crates/gwiki/src/ingest/file.rs:41-44]
- `ingest_path` (function) component `ingest_path [function]` (`e9e4425e-8125-53ae-bcf0-af650e5c1bdf`) lines 46-59 [crates/gwiki/src/ingest/file.rs:46-59]
  - Signature: `pub fn ingest_path(`
  - Purpose: 'ingest_path' ingests the specified path via 'ingest_path_without_index', then rebuilds the wiki index with 'index_after_ingest', returning the inner 'IngestResult' or propagating any 'WikiError'. [crates/gwiki/src/ingest/file.rs:46-59]
- `ingest_stdin` (function) component `ingest_stdin [function]` (`b860b1e3-9eba-5669-947a-9bcb5e68bb16`) lines 62-94 [crates/gwiki/src/ingest/file.rs:62-94]
  - Signature: `pub fn ingest_stdin(`
  - Purpose: Registers a stdin-backed source draft in the vault, renders and writes its raw Markdown representation, reindexes the store, and returns the resulting record and raw file path with no asset path. [crates/gwiki/src/ingest/file.rs:62-94]

