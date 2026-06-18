---
title: crates/gcode/src/commands/codewiki/run.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/run.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/run.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The primary entry point, `run`, coordinates loading files in-scope, retrieving symbols, pulling leading code chunks, and building the necessary context structure. [crates/gcode/src/commands/codewiki/run.rs:22-188]

## How it fits

This file sits at the boundary between database query mechanisms and documentation generation workflows. It serves as the orchestrator that structures physical code data into logical inputs for downstream processing.

The process begins with validating execution constraints like the graph edge limit using `validate_edge_limit`. [crates/gcode/src/commands/codewiki/run.rs:217-222]

The initial contents of these files are loaded via `load_leading_chunks`. [crates/gcode/src/commands/codewiki/run.rs:249-295]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run` | function | 'run' validates 'edge_limit', opens the database read-only, normalizes and applies scope filters to visible files, loads matching symbols, leading chunks, and graph edges, then assembles a 'CodewikiInput' and initializes the text generator/verifier and output path for documentation generation. [crates/gcode/src/commands/codewiki/run.rs:22-188] |
| `run_repair` | function | 'run_repair' opens a read-only database connection, collects visible file paths and symbols for the current context, runs citation repair into the specified or default output directory, and prints the resulting summary as JSON or human-readable text. [crates/gcode/src/commands/codewiki/run.rs:195-215] |
| `validate_edge_limit` | function | Returns 'Ok(())' only when 'edge_limit' is in the inclusive range '1..=MAX_EDGE_LIMIT', otherwise returns an 'anyhow' error stating that '--edge-limit' is out of bounds. [crates/gcode/src/commands/codewiki/run.rs:217-222] |
| `documents_file` | function | Returns 'true' if 'crate::index::languages::detect_language(file_path)' detects a language for the given path, and 'false' otherwise. [crates/gcode/src/commands/codewiki/run.rs:227-229] |
| `should_document_file` | function | Returns 'true' when 'include_docs' is 'true', or otherwise when 'documents_file(file_path)' reports that the path is a document file. [crates/gcode/src/commands/codewiki/run.rs:233-235] |
| `load_symbols_for_codewiki` | function | Emits a progress message indicating how many files are being processed, then delegates to the provided 'load_symbols' closure with the file list and returns its 'Result<Vec<Symbol>>' unchanged. [crates/gcode/src/commands/codewiki/run.rs:237-244] |
| `load_leading_chunks` | function | Fetches the first code-content chunk ('chunk_index = 0') for each requested file across the current project scope (single or overlay), returning a 'BTreeMap<String, LeadingChunk>' keyed by file path and skipping duplicate paths after the first match. [crates/gcode/src/commands/codewiki/run.rs:249-295] |

