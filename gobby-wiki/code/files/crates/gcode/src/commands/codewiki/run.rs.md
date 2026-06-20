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
| `run` | function | The 'run' function connects to a read-only database to load and filter visible files and symbols within the provided scopes, fetches their associated graph edges and leading content chunks, and constructs a system model from cargo manifests to prepare the input structure for codewiki generation. [crates/gcode/src/commands/codewiki/run.rs:23-223] |
| `run_repair` | function | The 'run_repair' function retrieves visible workspace symbols from a read-only database connection, repairs citation files in a specified or default output directory using those symbols, and outputs the resulting repair summary in JSON or text format. [crates/gcode/src/commands/codewiki/run.rs:230-250] |
| `validate_edge_limit` | function | The 'validate_edge_limit' function validates whether the provided 'edge_limit' falls within the inclusive range of 1 to 'MAX_EDGE_LIMIT', returning an 'Ok(())' result if valid or an error if the value is out of bounds. [crates/gcode/src/commands/codewiki/run.rs:252-257] |
| `git_changed_files` | function | The 'git_changed_files' function executes a 'git diff --name-only' command under the specified project root directory to retrieve and return a sorted set of file paths changed since the given git reference. [crates/gcode/src/commands/codewiki/run.rs:263-285] |
| `documents_file` | function | The 'documents_file' function returns a boolean indicating whether a programming or markup language can be successfully detected for the given file path. [crates/gcode/src/commands/codewiki/run.rs:290-292] |
| `should_document_file` | function | Returns 'true' if either the 'include_docs' parameter is true or the file at 'file_path' satisfies the 'documents_file' predicate, indicating whether the file should be documented. [crates/gcode/src/commands/codewiki/run.rs:296-298] |
| `load_symbols_for_codewiki` | function | The 'load_symbols_for_codewiki' function emits a progress update detailing the number of files to be processed and then invokes a provided callback closure to load and return a vector of symbols for those files. [crates/gcode/src/commands/codewiki/run.rs:300-307] |
| `load_leading_chunks` | function | This function queries a PostgreSQL database to retrieve the initial chunk (index 0) for a list of file paths across project IDs determined by the context's index scope, returning a map of file paths to their respective leading chunks while prioritizing overlay project entries over parent project entries. [crates/gcode/src/commands/codewiki/run.rs:312-358] |

