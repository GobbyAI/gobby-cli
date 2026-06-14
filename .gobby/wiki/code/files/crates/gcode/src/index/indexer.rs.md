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

This module is a full and incremental indexing orchestrator that writes files, symbols, imports, calls, unresolved targets, and content chunks to PostgreSQL. It coordinates indexing operations across multiple submodules (file, freshness_probe, lifecycle, overlay, pipeline, sink, types, util) and delegates external synchronization with Qdrant vectors and FalkorDB graph to other components. It exposes public APIs for checking project freshness, invalidating indexes, and performing file indexing operations. [crates/gcode/src/index/indexer.rs:1-27]

## API Symbols

No indexed symbols.
