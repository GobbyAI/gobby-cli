---
title: crates/gcode/src/graph/code_graph.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph.rs
  ranges:
  - 1-46
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph.rs

Module: [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]

## Purpose

This file is the public interface module for a code graph system. It aggregates and re-exports functionality from submodules (connection, lifecycle, payload, read, write) to provide a unified API for creating, managing, and querying code dependency graphs. The exports include data structures for graph nodes and links, lifecycle management functions for the graph, query operations to find callers/callees/usages and analyze blast radius, and write operations to synchronize and manipulate the code graph. It serves as the main entry point for code analysis and graph manipulation functionality. [crates/gcode/src/graph/code_graph.rs:1-46]

## API Symbols

No indexed symbols.
