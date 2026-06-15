---
title: crates/gcode/src/index/indexer.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer.rs
  ranges:
  - 1-27
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Orchestrator for full and incremental indexing. It coordinates writing files, symbols, imports, calls, unresolved targets, and content chunks to the PostgreSQL hub, while leaving external sync to other layers; it also re-exports the main indexing, invalidation, freshness, and outcome types. [crates/gcode/src/index/indexer.rs:1-27]

## API Symbols

No indexed symbols.
