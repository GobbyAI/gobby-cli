---
title: crates/gcode/src/commands/codewiki/run.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/run.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/run.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/run.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/run.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run` | function | # Summary This function loads and assembles scoped code files and symbols from a read-only database, constructs their dependency graph up to a specified edge limit, and packages the results into a 'CodewikiInput' structure for downstream code analysis or documentation generation. [crates/gcode/src/commands/codewiki/run.rs:23-235] |
| `run_repair` | function | Queries a read-only database for visible files and symbols, repairs citations in the specified output directory, and outputs the repair summary in JSON or text format. [crates/gcode/src/commands/codewiki/run.rs:242-262] |
| `validate_edge_limit` | function | Validates that the 'edge_limit' parameter falls within the inclusive range [1, MAX_EDGE_LIMIT], returning an error if the value is out of bounds. [crates/gcode/src/commands/codewiki/run.rs:264-269] |
| `git_changed_files` | function | This function executes 'git diff --name-only' against a specified Git reference in the given project directory and returns the resulting changed file names as a sorted, deduplicated set of strings. [crates/gcode/src/commands/codewiki/run.rs:275-297] |
| `documents_file` | function | This function returns 'true' if language detection succeeds for the given file path, otherwise 'false'. [crates/gcode/src/commands/codewiki/run.rs:302-304] |
| `should_document_file` | function | Returns 'true' if either the global documentation flag 'include_docs' is enabled or the file is marked for documentation via the 'documents_file()' function. [crates/gcode/src/commands/codewiki/run.rs:308-310] |
| `load_symbols_for_codewiki` | function | Loads symbols from a list of files via a provided closure while emitting progress updates to a progress tracker. [crates/gcode/src/commands/codewiki/run.rs:312-319] |
| `load_leading_chunks` | function | Retrieves the first code chunks (chunk_index = 0) for specified files from PostgreSQL across the configured project scope(s), returning a sorted map of file paths to LeadingChunk objects containing content and line number metadata. [crates/gcode/src/commands/codewiki/run.rs:324-370] |

