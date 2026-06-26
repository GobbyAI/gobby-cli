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
| `run` | function | The 'run' function loads scope-filtered code files and symbols from a read-only database, fetches their dependency graph edges, and aggregates the results into a 'CodewikiInput' structure for code analysis and documentation generation. [crates/gcode/src/commands/codewiki/run.rs:23-244] |
| `run_repair` | function | Performs citation repair on visible files and symbols retrieved from a read-only database connection, outputting the repair summary in either JSON or text format. [crates/gcode/src/commands/codewiki/run.rs:251-271] |
| `validate_edge_limit` | function | This function validates that the 'edge_limit' parameter falls within the inclusive range [1, MAX_EDGE_LIMIT], returning 'Ok(())' if valid or an error with a descriptive message if out of bounds. [crates/gcode/src/commands/codewiki/run.rs:273-278] |
| `git_changed_files` | function | Executes 'git diff --name-only' against a specified Git reference within a project directory and returns the changed file paths as a sorted set. [crates/gcode/src/commands/codewiki/run.rs:284-306] |
| `documents_file` | function | Returns 'true' if language detection successfully identifies a language for the given file path, 'false' otherwise. [crates/gcode/src/commands/codewiki/run.rs:311-313] |
| `should_document_file` | function | Returns a boolean indicating whether a file should be documented, determined by either the 'include_docs' flag being true or the result of a 'documents_file' check on the given file path. [crates/gcode/src/commands/codewiki/run.rs:317-319] |
| `load_symbols_for_codewiki` | function | This crate-public function emits a progress update and delegates symbol loading from a file list to a provided closure, returning 'anyhow::Result<Vec<Symbol>>'. [crates/gcode/src/commands/codewiki/run.rs:321-328] |
| `load_leading_chunks` | function | Fetches the first code chunk (chunk_index = 0) for specified files from a PostgreSQL database across applicable project scopes, returning a sorted map of file paths to LeadingChunk objects containing content and line number ranges. [crates/gcode/src/commands/codewiki/run.rs:333-379] |

