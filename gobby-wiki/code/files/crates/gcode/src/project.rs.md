---
title: crates/gcode/src/project.rs
type: code_file
provenance:
- file: crates/gcode/src/project.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/project.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/project.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gcode/src/project.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IsolationMarker` | class | 'IsolationMarker' is a Rust struct that optionally records a parent project’s path and ID as 'String' values for isolation or provenance tracking. [crates/gcode/src/project.rs:15-18] |
| `read_gcode_json` | function | Reads '<project_root>/.gobby/gcode.json', parses it as JSON, and returns the '"id"' field as a 'String', failing with contextual errors if the file cannot be read, parsed, or lacks a string 'id'. [crates/gcode/src/project.rs:21-30] |
| `code_index_id_for_root` | function | Computes a deterministic code index ID for a root path by canonicalizing it, falling back to an absolute path if canonicalization fails, and generating a UUID v5 in the 'CODE_INDEX_UUID_NAMESPACE' from the path string. [crates/gcode/src/project.rs:35-44] |
| `read_isolation_marker` | function | Reads 'project_root/.gobby/project.json', parses it as JSON, and returns an 'IsolationMarker' containing any non-empty 'parent_project_path' and/or 'parent_project_id' strings, or 'None' if the file is missing, invalid, or neither field is present. [crates/gcode/src/project.rs:47-70] |
| `ensure_gcode_json` | function | Ensures a '.gobby/gcode.json' project metadata file exists by preferring an existing '.gobby/project.json' or 'gcode.json' to read the project ID, otherwise creating '.gobby', generating a new JSON file with 'id', 'name', and 'created_at', and returning the project ID plus a boolean indicating whether the file was created. [crates/gcode/src/project.rs:78-115] |
| `has_identity_file` | function | Returns 'true' if the project’s '.gobby' directory contains either 'project.json' or 'gcode.json', and 'false' otherwise. [crates/gcode/src/project.rs:118-121] |
| `now_iso8601` | function | Returns the current UTC timestamp as a 'String' formatted in RFC 3339/ISO 8601 with microsecond precision and a trailing 'Z' offset. [crates/gcode/src/project.rs:126-128] |
| `absolute_fallback` | function | Returns 'path' unchanged if it is already absolute, otherwise prefixes it with the current working directory, falling back to the system temp directory if 'current_dir()' fails. [crates/gcode/src/project.rs:130-138] |

_Verified by 8 in-file unit tests._

