---
title: crates/gcode/src/commands/symbols.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/symbols.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/symbols.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

This file implements command-line entry points and underlying logic for querying, rendering, and summarizing codebase symbol structures. Its primary role is to serve structural code information to users or integrations, allowing them to examine files as hierarchical outlines or high-level summaries instead of raw source code.

## How it fits
[crates/gcode/src/commands/symbols.rs:21-78]
[crates/gcode/src/commands/symbols.rs:80-103]
[crates/gcode/src/commands/symbols.rs:105-126]
[crates/gcode/src/commands/symbols.rs:128-142]
[crates/gcode/src/commands/symbols.rs:144-167]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `outline` | function | Reads visible symbols for a normalized file from the database, optionally emits a missing-file diagnostic or a text summary, reports outline-size savings against the full file, and then prints either JSON (full symbols or slim outline records) or rendered text outline. [crates/gcode/src/commands/symbols.rs:21-78] |
| `summarize_outline` | function | Reads the target file under 'ctx.project_root', skips it if its size exceeds 'OUTLINE_SUMMARY_MAX_BYTES', loads the file contents and AI context, selects the text-generation route, and returns 'summarize_outline_with(...)' fed by either daemon or direct AI-generated text, or 'None' on any failure or unsupported routing mode. [crates/gcode/src/commands/symbols.rs:80-103] |
| `resolve_outline_ai_context` | function | Resolves and returns an 'AiContext' for 'ctx.project_id' by constructing an 'AiConfigSource' from optional standalone config plus Postgres-backed config, using the provided mutable connection when available or otherwise opening a read-only database connection. [crates/gcode/src/commands/symbols.rs:105-126] |
| `summarize_outline_with` | function | Returns 'None' for empty trimmed 'code', otherwise builds an outline-summary prompt from 'file', 'code', and 'symbols', invokes 'generate' with that prompt and 'OUTLINE_SYSTEM_PROMPT', and returns the trimmed non-empty generated summary as 'Some(String)'. [crates/gcode/src/commands/symbols.rs:128-142] |
| `outline_summary_prompt` | function | Builds a formatted outline-summary prompt string containing the file path, an indexed-symbols section that lists each symbol’s qualified name, kind, line range, and optional nonempty signature (or a placeholder when none exist), followed by the full code body. [crates/gcode/src/commands/symbols.rs:144-167] |
| `render_outline_text` | function | Builds a newline-separated outline by mapping each symbol ID to its parent ID, computing each symbol’s nesting depth from that parent map, prefixing each formatted symbol line with two-space indentation per depth level, and joining the lines into a single 'String'. [crates/gcode/src/commands/symbols.rs:169-183] |
| `outline_depth` | function | Computes a symbol’s outline nesting depth by walking parent_symbol_id links through 'parent_by_id', incrementing for each reachable ancestor until a missing parent or cycle is encountered. [crates/gcode/src/commands/symbols.rs:185-200] |
| `outline_missing_diagnostic` | function | Returns the most specific missing-diagnostic string for a path by checking whether it exists in the current project, whether it is indexed, whether it belongs to a different indexed project, and whether indexed content exists despite the file being absent from the checkout. [crates/gcode/src/commands/symbols.rs:202-229] |
| `unsupported_file_type_diagnostic` | function | Returns 'None' when 'languages::detect_language(file)' recognizes the file, otherwise returns a diagnostic 'Some(String)' stating that the file type lacks AST parser support and will be indexed as text chunks only. [crates/gcode/src/commands/symbols.rs:231-239] |
| `format_outline_text_line` | function | Formats a 'Symbol' into a single outline text line containing its file path, start/end lines, kind, qualified name, and id, and appends 'sig=<signature>' only when a non-empty signature is present. [crates/gcode/src/commands/symbols.rs:241-256] |
| `symbol` | function | Looks up a visible symbol by id in the readonly database, reads the symbol’s source slice from the project file if it exists, optionally reports byte-savings telemetry, and prints either the symbol record with embedded source in JSON or the raw snippet/text fallback, otherwise errors if the symbol is missing. [crates/gcode/src/commands/symbols.rs:258-302] |
| `symbols` | function | Connects to the database read-only, returns immediately for empty input, resolves the visible symbols for the requested IDs, reports aggregate file-vs-symbol byte savings when applicable, and emits the results either as JSON or as formatted text lines. [crates/gcode/src/commands/symbols.rs:304-341] |
| `kinds` | function | Connects to the database in read-only mode, fetches the kinds visible to the current context, and prints them as JSON or newline-delimited text depending on the requested 'Format'. [crates/gcode/src/commands/symbols.rs:343-356] |
| `tree` | function | Connects to the database in read-only mode, builds a JSON-serializable list of visible files with 'file_path', 'language', and 'symbol_count', and prints it as either JSON or formatted text (suppressing empty text output). [crates/gcode/src/commands/symbols.rs:358-382] |
| `format_tree_text` | function | Formats a slice of JSON file records into a newline-separated directory tree text by grouping entries by parent directory, sorting groups lexicographically via 'BTreeMap', and rendering each file as 'basename [language] (symbol_count symbols)'. [crates/gcode/src/commands/symbols.rs:390-417] |
| `symbol` | function | Returns a 'Symbol' metadata record for the Rust 'outline' function in 'src/commands.rs', populated with fixed identifiers, location spans, language/kind, and its signature. [crates/gcode/src/commands/symbols.rs:423-444] |
| `outline_text_line_includes_id_range_and_signature` | function | Verifies that 'format_outline_text_line(&symbol())' produces a line containing the expected source path and line range, function kind/name, UUID identifier, and exact Rust signature. [crates/gcode/src/commands/symbols.rs:447-453] |
| `outline_text_indents_by_parent_chain_depth` | function | Verifies that 'render_outline_text' indents outline entries by parent-chain depth, producing progressively deeper two-space prefixes for parent, child, and grandchild symbols. [crates/gcode/src/commands/symbols.rs:456-478] |
| `unsupported_file_type_diagnostic_mentions_text_only_indexing` | function | Verifies that 'unsupported_file_type_diagnostic' returns a text-only indexing diagnostic for 'Dockerfile' and 'None' for a supported Rust source file like 'src/lib.rs'. [crates/gcode/src/commands/symbols.rs:481-490] |
| `summarizes_when_configured` | function | Verifies that 'summarize_outline_with' builds the expected prompt and system prompt from a source file and symbol list, invokes the callback to produce a natural-language summary, and returns that summary wrapped in 'Some'. [crates/gcode/src/commands/symbols.rs:493-511] |
| `outline_summary_size_cap_is_one_mib` | function | Verifies that 'OUTLINE_SUMMARY_MAX_BYTES' is exactly '1024 * 1024' bytes, i.e. one MiB. [crates/gcode/src/commands/symbols.rs:514-516] |
| `degrades_to_ast` | function | Verifies that 'summarize_outline_with' falls back to and returns the rendered AST outline when the summarization callback yields 'None'. [crates/gcode/src/commands/symbols.rs:519-531] |
| `tree_text_groups_files_by_directory` | function | It verifies that 'format_tree_text' groups file entries by directory, renders the root directory as '.', and outputs each file with its basename plus language and symbol count in a directory-ordered tree. [crates/gcode/src/commands/symbols.rs:534-557] |
| `tree_text_treats_absolute_root_files_as_root_group` | function | Verifies that 'format_tree_text' renders an absolute root-level file path like '"/lib.rs"' as a root-group entry named '"."', producing '".\n lib.rs [rust] (1 symbols)"'. [crates/gcode/src/commands/symbols.rs:560-568] |

