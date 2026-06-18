---
title: crates/gcode/src/index/walker/discovery.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/discovery.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/discovery.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Overview

`crates/gcode/src/index/walker/discovery.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/index/walker/discovery.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `discover_files` | function | Calls 'discover_files_with_options' with 'DiscoveryOptions::default()' to return the discovered files and directories under 'root', filtered by 'exclude_patterns'. [crates/gcode/src/index/walker/discovery.rs:12-17] |
| `discover_files_with_options` | function | Traverses 'root' with a hidden-file-aware walker configured with optional gitignore respect and a maximum file size, classifies each discovered file plus any files from the hidden-path allowlist via 'push_classified_file' while de-duplicating with 'seen', and returns the resulting '(candidates, content_only)' path lists. [crates/gcode/src/index/walker/discovery.rs:19-64] |
| `push_classified_file` | function | Deduplicates 'path' by canonicalized identity in 'seen', then classifies it relative to 'root' with 'exclude_patterns' and appends the original path to either 'candidates' for 'Ast' files or 'content_only' for 'ContentOnly' files. [crates/gcode/src/index/walker/discovery.rs:66-84] |

