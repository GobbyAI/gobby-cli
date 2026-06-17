---
title: crates/gcode/src/index/indexer.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer.rs
  ranges:
  - 1-28
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer.rs:1-28](crates/gcode/src/index/indexer.rs#L1-L28)

</details>

# crates/gcode/src/index/indexer.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Orchestrates full and incremental indexing for the gcode crate, coordinating writes of files, symbols, imports, calls, unresolved targets, and content chunks to the PostgreSQL hub while leaving external sync work to other modules. It also exposes indexing-related helpers and request/outcome types for use elsewhere in the repository. [crates/gcode/src/index/indexer.rs:1-28]

## API Symbols

No indexed symbols.
