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

# crates/gcode/src/search/mod.rs

Module: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Purpose

Top-level search module that wires together full-text search, semantic vector search, and graph boosting, with reciprocal rank fusion for ranking. It exposes the `fts`, `graph_boost`, and `rrf` submodules and is designed to degrade gracefully when some configured search services are unavailable. [crates/gcode/src/search/mod.rs:1-11]

## API Symbols

No indexed symbols.
