---
title: crates/gcore/src/project.rs
type: code_file
provenance:
- file: crates/gcore/src/project.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/project.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/project.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcore/src/project.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `find_project_root` | function | # Summary This function iteratively traverses parent directories from a given start path to locate the project root directory, identified by the presence of a '.gobby' folder containing either 'project.json' or 'gcode.json', returning 'Some(PathBuf)' if found or 'None' if no such directory exists in the hierarchy. [crates/gcore/src/project.rs:12-24] |
| `read_project_id` | function | Reads a project ID string from '.gobby/project.json' in the specified project root, with fallback to '.gobby/gcode.json' if the primary file is unavailable or unreadable. [crates/gcore/src/project.rs:28-51] |
| `read_project_id_from` | function | Reads a JSON file from the given path and extracts the 'id' field as a 'String', returning an 'anyhow::Result' with contextual error messages if file reading, JSON parsing, or field extraction fails. [crates/gcore/src/project.rs:53-62] |

_Verified by 5 in-file unit tests._

