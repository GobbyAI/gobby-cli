---
title: crates/gwiki/src/ingest/file/generic.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/generic.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file/generic.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/file/generic.rs` exposes 1 indexed API symbol.

## How it fits

`crates/gwiki/src/ingest/file/generic.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ingest_generic_file_without_index` | function | This function reads a local source file, registers its metadata as a borrowed draft in the vault's source manifest, conditionally persists it as a binary asset, renders and writes its content as raw Markdown, and returns a 'LocalFileIngestResult' containing the manifest record and generated file paths. [crates/gwiki/src/ingest/file/generic.rs:11-57] |

