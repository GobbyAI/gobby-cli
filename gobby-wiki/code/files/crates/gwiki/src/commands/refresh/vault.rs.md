---
title: crates/gwiki/src/commands/refresh/vault.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/vault.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/vault.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Overview

`crates/gwiki/src/commands/refresh/vault.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/refresh/vault.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `raw_source_path` | function | Returns 'paths::raw_source_path(id)', forwarding the given identifier to resolve and return a raw source 'PathBuf' or propagate a 'WikiError'. [crates/gwiki/src/commands/refresh/vault.rs:7-9] |
| `source_asset_paths_for_id` | function | Returns all relative paths under 'raw/assets' whose filename stem exactly matches the trimmed 'id' and whose extension is non-empty, or an empty vector if the asset directory does not exist. [crates/gwiki/src/commands/refresh/vault.rs:16-49] |
| `remove_relative_file` | function | Removes the file at 'vault_root.join(safe_refresh_relative_path(relative_path)?)', returning 'Ok(true)' on successful deletion, 'Ok(false)' if the file does not exist, and 'Err(WikiError::Io { ... })' for any other I/O failure. [crates/gwiki/src/commands/refresh/vault.rs:51-66] |
| `safe_refresh_relative_path` | function | Validates a vault-relative path by rejecting empty, absolute, prefix/root, or parent-directory components, discarding '.' segments, and returning the normalized 'PathBuf' only if it still contains at least one non-empty file-name component. [crates/gwiki/src/commands/refresh/vault.rs:68-101] |
| `ensure_scope_root` | function | Returns 'Ok(())' when 'root' exists as a directory, otherwise returns 'WikiError::NotFound' identifying the missing wiki scope by the path string. [crates/gwiki/src/commands/refresh/vault.rs:103-112] |

