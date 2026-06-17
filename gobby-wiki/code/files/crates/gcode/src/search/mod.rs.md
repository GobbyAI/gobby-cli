---
title: crates/gcode/src/search/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/search/mod.rs
  ranges:
  - 1-11
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/mod.rs:1-11](crates/gcode/src/search/mod.rs#L1-L11)

</details>

# crates/gcode/src/search/mod.rs

Module: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Purpose

Defines the search subsystem entry point and re-exports its submodules: full-text search, graph boosting, and Reciprocal Rank Fusion. It documents that top-level search combines FTS, semantic vectors, and graph boosting, while allowing hybrid callers to fall back to fewer sources when a configured service is unavailable. [crates/gcode/src/search/mod.rs:1-11]

## API Symbols

No indexed symbols.
