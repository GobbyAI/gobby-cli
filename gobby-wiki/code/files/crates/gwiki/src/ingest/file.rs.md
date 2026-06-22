---
title: crates/gwiki/src/ingest/file.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/file.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/file.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `StdinSnapshot` | class | The 'StdinSnapshot' struct represents a captured snapshot of standard input, containing a descriptive label, a timestamp of when it was fetched, and the raw input data stored as a vector of bytes. [crates/gwiki/src/ingest/file.rs:34-38] |
| `LocalFileIngestResult` | class | The 'LocalFileIngestResult' struct represents the outcome of a local file ingestion operation, containing a primary 'IngestResult' and a list of strings detailing any associated degradations. [crates/gwiki/src/ingest/file.rs:41-44] |
| `ingest_path` | function | The 'ingest_path' function ingests a specified file path under a vault root, updates the associated 'WikiIndexStore' after ingestion, and returns the resulting 'IngestResult'. [crates/gwiki/src/ingest/file.rs:46-59] |
| `ingest_stdin` | function | The 'ingest_stdin' function registers a standard input snapshot as a source draft in the manifest, renders its payload into raw markdown, writes the markdown file to the vault root, updates the wiki index store, and returns an 'IngestResult' containing the registration record and the markdown file path. [crates/gwiki/src/ingest/file.rs:62-94] |

