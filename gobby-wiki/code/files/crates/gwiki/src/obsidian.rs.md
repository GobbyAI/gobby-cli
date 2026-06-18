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

`crates/gwiki/src/obsidian.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `state_filter` | function | Returns a 'String' containing 'STATE_ROOT' formatted with a trailing '/' suffix. [crates/gwiki/src/obsidian.rs:21-23] |
| `seed_app_json` | function | Reads or creates '.obsidian/app.json' under 'vault_root', ensures the 'userIgnoreFilters' array contains 'state_filter()' exactly once, and writes the pretty-serialized JSON back while mapping read/parse/serialize/write failures into 'WikiError'. [crates/gwiki/src/obsidian.rs:33-84] |
| `ensure_gitignore_obsidian` | function | Ensures the repository’s '.gitignore' at the detected git root contains the three Obsidian workspace ignore entries, creating or appending them if missing, and returns early if no git root exists or all entries are already present. [crates/gwiki/src/obsidian.rs:93-141] |
| `find_git_root` | function | Walks up from 'start' through its parent directories and returns the first directory whose '.git' entry exists, or 'None' if no such ancestor is found. [crates/gwiki/src/obsidian.rs:145-154] |
| `seed_app_json_creates_filter_when_absent` | function | Verifies that 'seed_app_json(vault)' creates '.obsidian/app.json' with a 'userIgnoreFilters' entry containing '_gwiki/' when the file is initially absent. [crates/gwiki/src/obsidian.rs:161-169] |
| `seed_app_json_is_idempotent_and_preserves_keys` | function | Verifies that 'seed_app_json' can be run repeatedly without duplication, adding '_gwiki/' to 'userIgnoreFilters' exactly once while preserving existing filters and unrelated keys such as 'promptDelete'. [crates/gwiki/src/obsidian.rs:172-203] |
| `gitignore_noop_outside_git_work_tree` | function | Verifies that 'ensure_gitignore_obsidian' is a no-op when run outside a Git work tree by creating a temporary directory, invoking it, and asserting that no '.gitignore' file is created. [crates/gwiki/src/obsidian.rs:206-210] |
| `gitignore_appends_workspace_state_once_and_preserves_existing` | function | Verifies that 'ensure_gitignore_obsidian' appends the three 'gobby-wiki/.obsidian/workspace*.json' ignore rules exactly once to an existing '.gitignore', preserves preexisting entries like '/target', leaves '.obsidian/' unignored, and places the workspace rules at the end of the file. [crates/gwiki/src/obsidian.rs:213-244] |
| `gitignore_created_when_absent_in_git_tree` | function | Creates a '.gitignore' in the repository root when one is absent and verifies it contains the three Obsidian workspace paths for 'gobby-wiki' exactly. [crates/gwiki/src/obsidian.rs:247-261] |

