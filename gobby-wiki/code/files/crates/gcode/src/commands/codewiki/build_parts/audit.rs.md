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

`crates/gcode/src/commands/codewiki/build_parts/audit.rs` exposes 27 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/audit.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AuditContext` | class | The 'AuditContext' struct encapsulates the project root path, deprecation index, test-gated symbol index, and contract-handler entry points required to analyze source files for deprecations, aggregate test coverage, and exclude CLI dispatch entry points from dead-code detection. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:38-51] |
| `build_audit_context` | function | The 'build_audit_context' function constructs and returns an 'AuditContext' struct containing the project root path, a deprecation index, a test index, and entry points resolved from the provided 'CodewikiInput' and optional 'FeatureCatalogDoc'. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:55-66] |
| `entry_points_from_catalog` | function | This function processes an optional 'FeatureCatalogDoc' to extract and return a 'HashSet' of unique pairs, each consisting of a handler file path and the final segment of its corresponding entry symbol path split by '::', skipping any entries with empty fields. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:87-106] |
| `build_deprecation_index` | function | The 'build_deprecation_index' function constructs a 'DeprecationIndex' mapping symbol IDs to their deprecation reasons by grouping input symbols by file path to minimize disk I/O, reading each file once, and extracting deprecation metadata for each symbol from its source lines. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:111-133] |
| `deprecation_reason` | function | The function determines a symbol's deprecation reason by checking preceding source lines for a deprecated attribute or a deprecation doc comment, falling back to extracting the first meaningful line of the symbol's docstring if it contains a case-insensitive "DEPRECATED" mention. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:137-154] |
| `lookback_lines` | function | The function 'lookback_lines' traverses backward from the line immediately preceding the 1-based 'line_start' index, collecting a contiguous block of non-empty preceding lines classified as attributes, comments, or attribute continuations up to a maximum limit, and returns them in their original chronological order. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:159-198] |
| `looks_like_attribute_continuation` ⚠️ **deprecated** | function | ⚠️ **deprecated** — ... The function evaluates whether a trimmed string slice resembles an attribute continuation by checking if it contains 'note' or 'since', starts with a closing parenthesis, or ends with a comma or a closing parenthesis. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:202-208] |
| `deprecated_attribute_reason` ⚠️ **deprecated** | function | ⚠️ **deprecated** — ... The 'deprecated_attribute_reason' function joins a slice of strings to detect a Rust deprecation attribute, returning 'None' if absent, or 'Some' containing either an extracted and formatted custom explanation or a default fallback of '"deprecated"'. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:213-222] |
| `extract_note` | function | Returns the first non-empty, trimmed double-quoted value following a 'note' key in 'joined' by substring search, or 'None' if any delimiter is missing or the extracted note is empty. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:226-240] |
| `doc_comment_deprecation` ⚠️ **deprecated** | function | ⚠️ **deprecated** — Detect a `///` / `//!` doc-comment line mentioning the word `DEPRECATED` This function searches a slice of string slices for the first doc comment line (starting with '///' or '//!') that case-insensitively contains 'DEPRECATED' and returns its trimmed text formatted by 'cap_reason' as 'Some(String)', or 'None' if no such line exists. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:244-257] |
| `first_meaningful_line` | function | The function iterates through the lines of a string slice, trimming leading and trailing whitespace from each line, and returns the first non-empty trimmed line as an owned 'String', defaulting to an empty string if no such line is found. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:259-265] |
| `cap_reason` | function | The 'cap_reason' function truncates an input string to a maximum of 'REASON_MAX' characters and appends an ellipsis ('…') if its character count exceeds that limit. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:267-273] |
| `build_deprecations_doc` ⚠️ **deprecated** | function | ⚠️ **deprecated** — deprecated symbol grouped by file (the renderer groups). Never degrades. This function filters symbols from a 'CodewikiInput' against a 'DeprecationIndex', maps matches to 'DeprecatedSymbol' instances with their deprecation reasons, sorts them lexicographically by file path, line number, and name, and returns a 'DeprecationsDoc' containing the sorted list and an empty list of degraded sources. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:277-304] |
| `build_dead_code_doc` | function | The 'build_dead_code_doc' function compiles a 'DeadCodeDoc' by filtering input symbols against inbound call targets and a local file cache to produce a sorted, capped list of dead code candidates while propagating graph availability and truncation metadata. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:311-364] |
| `inbound_call_targets` | function | This function filters a slice of graph edges for call-type edges and collects their unique target component IDs into a 'HashSet' of string slices. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:369-375] |
| `is_candidate` | function | The 'is_candidate' function determines whether a given symbol is a valid analysis candidate by verifying that it represents a real definition kind and is not a called target, an entry point, a trait implementation or method, or gated by a test. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:380-403] |
| `is_real_definition_kind` | function | The function 'is_real_definition_kind' returns 'true' if the provided string slice matches one of the designated programming definition kinds—"function", "struct", "enum", "trait", "class", "interface", "type", or "constant"—and 'false' otherwise. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:408-413] |
| `is_entry_point` | function | This function determines whether a given symbol is an execution entry point by checking if its name is "main" or if its file path and name tuple exists within the audit context's registered entry points. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:415-422] |
| `is_trait_impl_or_method` | function | The function returns 'true' if the given symbol's kind is '"method"' or if its signature starts with '"impl "' or '"unsafe impl "', and 'false' otherwise. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:427-434] |
| `is_test_path` | function | The 'is_test_path' function returns a boolean indicating whether the provided string slice represents a test path by checking if it contains the substring '"/tests"' or ends with the suffix '"tests.rs"' or '"test.rs"'. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:467-469] |
| `lines` | function | The 'lines' function splits a string slice by its line endings and collects the resulting line string slices into a vector. [crates/gcode/src/commands/codewiki/build_parts/audit.rs:475-477] |

_Verified by 6 in-file unit tests._

