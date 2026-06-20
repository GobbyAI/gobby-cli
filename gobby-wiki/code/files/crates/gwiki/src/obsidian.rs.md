---
title: crates/gwiki/src/obsidian.rs
type: code_file
provenance:
- file: crates/gwiki/src/obsidian.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/obsidian.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/obsidian.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/obsidian.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `state_filter` | function | Returns a 'String' containing 'STATE_ROOT' formatted with a trailing '/' suffix. [crates/gwiki/src/obsidian.rs:21-23] |
| `seed_app_json` | function | Reads or creates '.obsidian/app.json' under 'vault_root', ensures the 'userIgnoreFilters' array contains 'state_filter()' exactly once, and writes the pretty-serialized JSON back while mapping read/parse/serialize/write failures into 'WikiError'. [crates/gwiki/src/obsidian.rs:33-84] |
| `ensure_gitignore_obsidian` | function | Ensures the repository’s '.gitignore' at the detected git root contains the three Obsidian workspace ignore entries, creating or appending them if missing, and returns early if no git root exists or all entries are already present. [crates/gwiki/src/obsidian.rs:93-141] |
| `find_git_root` | function | Walks up from 'start' through its parent directories and returns the first directory whose '.git' entry exists, or 'None' if no such ancestor is found. [crates/gwiki/src/obsidian.rs:145-154] |

_Verified by 5 in-file unit tests._

