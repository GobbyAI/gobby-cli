---
title: crates/gcode/src/commands/scope.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/scope.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/scope.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/scope.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gcode/src/commands/scope.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ProjectMatch` | class | 'ProjectMatch' is a crate-visible struct that identifies a project by storing its 'id' and filesystem 'root_path', both as 'String' values. [crates/gcode/src/commands/scope.rs:9-12] |
| `normalize_file_arg` | function | Returns a cleaned relative path for 'file', stripping 'ctx.project_root' from absolute paths when possible (or from their canonicalized forms as a fallback) and otherwise normalizing the input path directly. [crates/gcode/src/commands/scope.rs:14-27] |
| `path_exists_in_current_project` | function | Returns 'true' if 'file_path' exists under the current project root or, when the index scope is an overlay, under either the overlay root or the parent root; otherwise returns 'false'. [crates/gcode/src/commands/scope.rs:29-45] |
| `path_exists_under_root` | function | Returns 'true' only if 'root.join(file_path)' exists and its canonicalized absolute path is within the canonicalized 'root' directory, otherwise 'false'. [crates/gcode/src/commands/scope.rs:47-60] |
| `current_indexed_path_is_valid` | function | Returns 'true' only when the indexed file exists in visibility state for the given connection/context and the path also exists in the current project, otherwise 'false'. [crates/gcode/src/commands/scope.rs:62-69] |
| `other_project_for_path` | function | Returns the first indexed project other than the current one whose root path contains 'file_path' as an existing joined path, skipping any project whose canonicalized root matches the current project root, and falls back to 'None' if no match is found. [crates/gcode/src/commands/scope.rs:71-109] |
| `indexed_project_for_file_path` | function | Queries the indexed project table for a file path and returns the first matching 'ProjectMatch' from a different project than 'current_project_id', ordered by 'root_path', or 'None' if no row is found or the query/mapping fails. [crates/gcode/src/commands/scope.rs:111-133] |
| `clean_relative_path` | function | Returns a normalized relative path string by dropping '.'/root/prefix components, preserving '..' segments, joining normal components into a 'PathBuf', and converting the result to a UTF-8-lossy forward-slash-separated string. [crates/gcode/src/commands/scope.rs:135-146] |
| `context_for` | function | Creates and returns a 'Context' initialized with the given 'root' as 'project_root', hard-coded test database URL and project ID, 'quiet' set to 'false', all optional service URLs/configs unset, and default code-vector/indexing settings with 'ProjectIndexScope::Single'. [crates/gcode/src/commands/scope.rs:153-167] |

_Verified by 3 in-file unit tests._

