---
title: crates/gcode/src/commands/codewiki/cluster.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/cluster.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/cluster.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/cluster.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/cluster.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `subsystem_roots` | function | Returns the set of subsystem root identifiers derived from 'files' by grouping module paths on their top-level segment and, for each top-level group, emitting the top-level name if it has any direct files or no children, otherwise emitting each immediate child path as the root. [crates/gcode/src/commands/codewiki/cluster.rs:8-43] |
| `subsystem_root_for_file` | function | Returns the first root in 'roots' whose path scope contains the module derived from 'file', or 'None' if no such root exists. [crates/gcode/src/commands/codewiki/cluster.rs:46-55] |
| `module_is_within` | function | Returns 'true' if 'module' is exactly 'root' or is a path-like descendant of 'root' whose remaining suffix is empty or begins with '/', and 'false' otherwise. [crates/gcode/src/commands/codewiki/cluster.rs:57-61] |
| `cluster_file_modules` | function | Clusters files into module groups by mapping symbols to their owning files, unioning files connected by 'Call' edges that stay within the same subsystem root, and then assigning each connected set either a shared common module name or a per-file module path. [crates/gcode/src/commands/codewiki/cluster.rs:63-123] |
| `union_files` | function | Performs a union-by-rank merge of the equivalence classes containing 'left' and 'right' by linking the lower-rank root under the higher-rank root, breaking equal-rank ties deterministically by root string order and incrementing the chosen parent’s rank. [crates/gcode/src/commands/codewiki/cluster.rs:125-149] |
| `find_file_root` | function | Performs union-find root resolution for a file key in 'parents', with path compression back into the discovered root and cycle detection that collapses a detected parent loop to the lexicographically smallest node in the cycle. [crates/gcode/src/commands/codewiki/cluster.rs:158-199] |
| `common_module_for_files` | function | Returns the deepest shared slash-separated module path among all input files by computing each file’s module path via 'module_for_file', intersecting path components from the front, and joining the common prefix, or an empty string for no files. [crates/gcode/src/commands/codewiki/cluster.rs:201-225] |
| `symbols_by_file_component` | function | Returns a 'BTreeMap' grouping 'Symbol' IDs by their exact 'file_path' for symbols whose path satisfies 'is_core_file', omitting all others. [crates/gcode/src/commands/codewiki/cluster.rs:227-237] |
| `first_component_for_file` | function | Returns a cloned 'Option<String>' containing the first component associated with 'file' in 'symbols_by_file', or 'None' if the file is absent or has no components. [crates/gcode/src/commands/codewiki/cluster.rs:239-247] |
| `files_for_import_target` | function | Returns the subset of 'files' whose path components or derived module-name components contain the component sequence for 'target_module', or an empty vector if the target module has no components. [crates/gcode/src/commands/codewiki/cluster.rs:249-265] |
| `module_components` | function | 'module_components' normalizes a module path string by converting '::', '.' and '\' separators to '/', splitting on '/', discarding empty segments, and returning the remaining components as 'String's. [crates/gcode/src/commands/codewiki/cluster.rs:267-275] |
| `path_components` | function | Returns the non-empty normal path segments of 'file' as owned strings, stripping each segment’s file extension when present and ignoring non-normal components such as roots, prefixes, and '.'/'..'. [crates/gcode/src/commands/codewiki/cluster.rs:277-295] |
| `contains_component_sequence` | function | Returns 'true' if 'target' appears as a contiguous subsequence within 'components', and 'false' otherwise. [crates/gcode/src/commands/codewiki/cluster.rs:297-302] |
| `paths` | function | Converts a slice of string slices into a 'Vec<String>' by cloning each '&str' into an owned 'String'. [crates/gcode/src/commands/codewiki/cluster.rs:308-310] |

_Verified by 4 in-file unit tests._

