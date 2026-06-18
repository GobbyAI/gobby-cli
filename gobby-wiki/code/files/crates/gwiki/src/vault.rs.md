---
title: crates/gwiki/src/vault.rs
type: code_file
provenance:
- file: crates/gwiki/src/vault.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/vault.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/vault.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gwiki/src/vault.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VaultPaths` | class | 'VaultPaths' is a data container holding a static slice of directory path strings and a vector of static file path strings. [crates/gwiki/src/vault.rs:24-27] |
| `CreatedVaultPaths` | class | 'CreatedVaultPaths' is a struct that records the vault paths created during an operation, split into two string lists: 'directories' and 'files'. [crates/gwiki/src/vault.rs:30-33] |
| `required_paths` | function | Returns a 'VaultPaths' struct populated with the compile-time 'DIRECTORIES' set and a 'files' collection containing only the path keys from 'DEFAULT_FILES'. [crates/gwiki/src/vault.rs:60-65] |
| `initialize` | function | Creates the vault’s required directory structure and default files under 'scope.root()', writes an atomic 'state_root/scope.json' containing the scope identity and root path, and returns the newly created directory/file paths. [crates/gwiki/src/vault.rs:67-104] |
| `cleanup_created` | function | Removes each path in 'created.files' with 'remove_file' and each path in 'created.directories' in reverse order with 'remove_dir', ignoring 'NotFound' for files and 'NotFound' or 'DirectoryNotEmpty' for directories, and wraps any other I/O failure in 'WikiError::Io'. [crates/gwiki/src/vault.rs:106-142] |
| `ScopeFile` | class | 'ScopeFile<'a>' is a borrowed data structure holding two string slices, 'identity' and 'root', both valid for lifetime ''a'. [crates/gwiki/src/vault.rs:145-148] |
| `create_dir` | function | Creates the directory at 'path' and any missing parent directories with 'std::fs::create_dir_all', converting any I/O failure into 'WikiError::Io' with action '"create directory"' and the path attached. [crates/gwiki/src/vault.rs:150-156] |
| `ensure_file` | function | Ensures the target file’s parent directory exists, then atomically creates the file only if it does not already exist, writes the provided contents, returns 'Ok(true)' when created, 'Ok(false)' when the file already exists, and converts I/O failures into 'WikiError::Io' while cleaning up any partially written file. [crates/gwiki/src/vault.rs:158-185] |
| `write_scope_file_atomically` | function | Creates the parent directory if needed, writes 'contents' to a sibling temp file, flushes and fsyncs it, renames it atomically into 'path', and returns a 'WikiError::Io' on any I/O failure while cleaning up the temp file. [crates/gwiki/src/vault.rs:187-223] |
| `temp_sibling_path` | function | Returns a sibling temporary-path 'PathBuf' beside the given path by taking its file name (defaulting to 'scope.json'), prefixing it with a dot, and appending the current process ID and a UNIX-epoch nanosecond timestamp before the '.tmp' suffix. [crates/gwiki/src/vault.rs:225-235] |
| `sync_parent_dir` | function | On Unix, 'sync_parent_dir' opens 'path'’s parent directory and calls 'sync_all()' to flush its metadata to disk, mapping I/O failures into 'WikiError::Io', while on non-Unix platforms it is a no-op and returns 'Ok(())' (and it also returns 'Ok(())' if the path has no parent). [crates/gwiki/src/vault.rs:237-256] |
| `vault_shape_lists_required_paths` | function | Asserts that 'required_paths()' includes the expected vault directory set ('raw/assets', 'code', 'knowledge', '_meta', 'knowledge/sources', 'knowledge/concepts', 'knowledge/topics', 'outputs', 'meta/health') and file set ('raw/INDEX.md', 'knowledge/INDEX.md', 'code/INDEX.md', '_index.md', 'log.md'). [crates/gwiki/src/vault.rs:263-280] |
| `default_files_drive_required_paths_and_contents` | function | Verifies that 'initialize(&scope)' creates every file in 'DEFAULT_FILES' under the topic root with the expected contents, and that 'required_paths().files' exactly matches the default file paths. [crates/gwiki/src/vault.rs:283-308] |
| `initialize_overwrites_scope_file` | function | Verifies that calling 'initialize' a second time for the same 'ResolvedScope' overwrites an existing stale 'scope.json' under 'STATE_ROOT' with the correct 'topic:rust' contents without reporting that file as newly created. [crates/gwiki/src/vault.rs:311-329] |
| `cleanup_created_removes_only_created_vault_paths` | function | Verifies that 'cleanup_created' deletes only the file and directory paths recorded in 'created' under the vault root, while leaving the root directory itself intact. [crates/gwiki/src/vault.rs:332-351] |

