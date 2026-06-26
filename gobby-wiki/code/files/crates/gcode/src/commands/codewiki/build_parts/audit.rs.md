---
title: crates/gcode/src/commands/codewiki/build_parts/audit.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/audit.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/audit.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/audit.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AuditContext` | class | AuditContext is a crate-private struct aggregating DeprecationIndex and TestIndex indices constructed during bounded source code scanning for documentation auditing and page rendering. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:28-34] |
| `build_audit_context` | function | Constructs and returns an 'AuditContext' by building deprecation and test indices from the specified project root and 'CodewikiInput' configuration. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:38-43] |
| `build_deprecation_index` | function | Constructs a 'DeprecationIndex' by scanning project source files to extract and map deprecation reasons for input symbols, keyed by their IDs. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:63-85] |
| `deprecation_reason` | function | Returns an optional deprecation reason extracted from a symbol's deprecated attribute, doc comments, or docstring, checked in that order of precedence. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:89-106] |
| `lookback_lines` | function | Collects and returns preceding attribute and documentation comment lines before a 1-based line position, bounded by a maximum lookback iteration limit and terminated by blank or non-continuation code lines. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:111-150] |
| `looks_like_attribute_continuation` ⚠️ **deprecated** | function | ⚠️ **deprecated** — ... Returns true if the trimmed string contains "note" or "since", starts with ')', or ends with ',' or ')', which are heuristics for detecting attribute continuation lines. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:154-160] |
| `deprecated_attribute_reason` ⚠️ **deprecated** | function | ⚠️ **deprecated** — ... Parses a string slice for a '#[deprecated]' Rust attribute and returns an optional String containing either the extracted and capitalized deprecation note or a default "deprecated" message. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:165-174] |
| `extract_note` | function | This function parses a string to extract a non-empty, trimmed value from a 'note="..."' field, returning 'Some(String)' if found or 'None' otherwise. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:178-192] |
| `doc_comment_deprecation` ⚠️ **deprecated** | function | ⚠️ **deprecated** — Detect a `///` / `//!` doc-comment line mentioning the word `DEPRECATED` # Summary Searches a slice of lines for a documentation comment marked "DEPRECATED" (case-insensitive), extracts the reason text, applies capitalization via 'cap_reason()', and returns it as 'Option<String>', or 'None' if not found. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:196-209] |
| `first_meaningful_line` | function | This function returns the first non-empty line from the input string after trimming whitespace, or an empty string if no such line exists. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:211-217] |
| `cap_reason` | function | Truncates the input string to a maximum of 'REASON_MAX' characters and appends an ellipsis ('…') if the original exceeds that length. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:219-225] |
| `build_deprecations_doc` ⚠️ **deprecated** | function | ⚠️ **deprecated** — deprecated symbol grouped by file (the renderer groups). Never degrades. This function builds a 'DeprecationsDoc' by filtering input symbols against a 'DeprecationIndex', mapping each deprecated symbol to a 'DeprecatedSymbol' record with file path and line metadata, and sorting them lexicographically by file path, line number, and symbol name. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:229-256] |
| `is_test_path` | function | This function returns 'true' if the provided file path contains a '/tests' directory segment or ends with 'test.rs' or 'tests.rs', indicating whether the file is part of a Rust test module. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:289-291] |
| `lines` | function | This function splits a string reference into lines and returns a vector of string slices, each representing a line delimited by newlines. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:297-299] |

_Verified by 6 in-file unit tests._

