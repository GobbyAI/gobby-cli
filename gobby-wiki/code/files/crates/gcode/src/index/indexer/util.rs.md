---
title: crates/gcode/src/index/indexer/util.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/util.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/util.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/util.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/util.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `filter_discovered_paths` | function | Returns the subset of 'paths' whose absolute form lies under 'path_filter' relative to 'root_path', using a canonicalized-prefix fallback to handle symlinks or other cases where the non-canonical path prefix check fails. [crates/gcode/src/index/indexer/util.rs:28-66] |
| `unsupported_file_types` | function | Groups the input paths by unsupported file-type label into a 'BTreeMap', counts files per extension, collects up to 'UNSUPPORTED_EXAMPLES_PER_TYPE' relative-path examples for each group, and returns the grouped 'UnsupportedFileType' values as a 'Vec'. [crates/gcode/src/index/indexer/util.rs:70-93] |
| `unsupported_file_type_label` | function | Returns the file extension as a lowercase dot-prefixed label when 'path' has a non-empty UTF-8 extension, otherwise returns '"extensionless"'. [crates/gcode/src/index/indexer/util.rs:95-101] |
| `requested_relative_path` | function | Returns the requested path as a string, preserving relative inputs verbatim and, for absolute inputs, converting them to a path relative to 'root_path' via 'strip_prefix' or falling back to 'lexical_relative_path' if the prefix cannot be removed. [crates/gcode/src/index/indexer/util.rs:103-111] |
| `lexical_relative_path` | function | Computes a lexical relative path from 'root_path' to 'requested_path' by comparing normalized components, returning the requested path unchanged if they share no common prefix, otherwise prepending the necessary '..' segments and appending the non-shared suffix, or '"."' when both paths normalize to the same location. [crates/gcode/src/index/indexer/util.rs:113-142] |
| `normalized_components` | function | Returns a 'Vec<OsString>' of the path’s components after normalization, preserving prefix, root, parent-directory, and normal segments while discarding '.' ('CurDir') components. [crates/gcode/src/index/indexer/util.rs:144-154] |
| `relative_path` | function | Canonicalizes 'path' and 'root', then returns 'path' as a UTF-8-lossy string relative to the canonicalized 'root' by stripping the root prefix, propagating any I/O or prefix errors via 'anyhow::Result'. [crates/gcode/src/index/indexer/util.rs:156-160] |
| `epoch_secs_str` | function | Returns the current Unix epoch time in whole seconds as a decimal 'String', defaulting to '0' if the system clock is before 'UNIX_EPOCH'. [crates/gcode/src/index/indexer/util.rs:162-169] |

_Verified by 6 in-file unit tests._

