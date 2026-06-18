---
title: crates/gcode/src/commands/codewiki/ownership/codeowners.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/codeowners.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/ownership/codeowners.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/ownership/codeowners.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/ownership/codeowners.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Codeowners` | class | 'Codeowners' is an internal struct that stores an ordered 'Vec<CodeownersEntry>' representing CODEOWNERS entries. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7] |
| `CodeownersEntry` | class | 'CodeownersEntry' is a struct that represents a CODEOWNERS rule by pairing a path pattern string with a list of owner identifiers. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13] |
| `read_codeowners` | function | Reads the first existing CODEOWNERS file from 'project_root' in priority order ('CODEOWNERS', '.github/CODEOWNERS', 'docs/CODEOWNERS'), parses it into a 'Codeowners', returns 'Ok(None)' if none exist, and propagates any non-'NotFound' I/O error. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:15-25] |
| `parse_codeowners` | function | Parses a CODEOWNERS-formatted string into a 'Codeowners' by trimming each non-empty, non-comment line, taking the first whitespace-delimited token as the pattern, collecting subsequent owner tokens up to any inline '#' comment, and discarding lines without owners. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:27-45] |
| `declared_owners_for_files` | function | Returns a 'BTreeMap' from each input file path to the owner list from the last matching CODEOWNERS entry, or an empty map if no 'Codeowners' is provided. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:47-66] |
| `codeowners_pattern_matches` | function | 'codeowners_pattern_matches' normalizes a CODEOWNERS pattern by stripping a leading '/', then matches directory prefixes, glob patterns, or exact path/basename equality against 'file' depending on whether the pattern ends with '/', contains wildcard metacharacters, or includes '/', returning 'false' and logging a warning if glob parsing fails. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:68-103] |

