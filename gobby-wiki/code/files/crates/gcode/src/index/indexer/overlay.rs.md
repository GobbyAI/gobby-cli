---
title: crates/gcode/src/index/indexer/overlay.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/overlay.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/overlay.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/overlay.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/overlay.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexedFileState` | class | 'IndexedFileState' is a package-visible struct that stores the indexed file’s 'content_hash' and detected 'language' as 'String' values. [crates/gcode/src/index/indexer/overlay.rs:33-36] |
| `OverlayReconcileAction` | type | Indexed type `OverlayReconcileAction` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:39-45] |
| `overlay_reconcile_action` | function | 'overlay_reconcile_action' decides the next 'OverlayReconcileAction' for a file by comparing file existence, the parent’s content hash against 'current_hash', overlay presence and tombstone language, and indexability, returning 'Skip', 'DeleteOverlay', 'Tombstone', 'Inherit', or 'Index' according to those state transitions. [crates/gcode/src/index/indexer/overlay.rs:47-83] |
| `index_overlay_files` | function | Indexes an overlay project by validating overlay context, discovering candidate files under the project root, reconciling overlay and parent indexed file states into a relative-path set, optionally filtering by request path, and populating overlay metadata in the returned 'IndexOutcome'. [crates/gcode/src/index/indexer/overlay.rs:85-260] |
| `overlay_reconcile_candidates` | function | 'overlay_reconcile_candidates' builds a deduplicated, sorted list of relative file paths to reconcile by preferring explicitly requested files, otherwise all indexed/overlay files for full requests or git-status plus overlay files when available, and falling back to all known AST/content/parent/overlay paths. [crates/gcode/src/index/indexer/overlay.rs:262-293] |
| `paths_by_relative` | function | Builds a 'HashMap' from each input 'PathBuf' that can be relativized to 'root_path', using the relative path string as the key and a cloned 'PathBuf' as the value, while skipping paths that fail 'relative_path'. [crates/gcode/src/index/indexer/overlay.rs:295-304] |
| `indexed_file_states` | function | Queries 'code_indexed_files' for the given 'project_id' and returns a 'HashMap' keyed by 'file_path' whose values contain each file’s 'content_hash' and 'language' as 'IndexedFileState' records. [crates/gcode/src/index/indexer/overlay.rs:306-326] |
| `git_status_relative_paths` | function | Runs 'git status --porcelain=v1 -z --untracked-files=all --no-renames' in 'root_path' with a timeout, returning the set of non-empty relative paths parsed from successful NUL-delimited porcelain status entries or an error if git fails or times out. [crates/gcode/src/index/indexer/overlay.rs:328-380] |
| `git_status_timeout` | function | Returns the git status timeout as a 'Duration', using 'GCODE_GIT_STATUS_TIMEOUT_SECS' if it is set to a positive integer number of seconds, otherwise falling back to the default and emitting a warning for invalid values. [crates/gcode/src/index/indexer/overlay.rs:382-398] |
| `compact_stderr` | function | Converts 'stderr' bytes to a lossy UTF-8 string, collapses all whitespace-separated runs into single spaces, and returns the normalized text. [crates/gcode/src/index/indexer/overlay.rs:400-405] |
| `is_porcelain_status_entry` | function | Returns 'true' only when the byte slice is at least 4 bytes long, its first two bytes are valid porcelain status bytes, and the third byte is a space character. [crates/gcode/src/index/indexer/overlay.rs:407-412] |
| `valid_porcelain_status_byte` | function | Returns 'true' if 'byte' is one of the accepted Git porcelain status codes: space, 'M', 'A', 'D', 'R', 'C', 'U', '?', or '!'. [crates/gcode/src/index/indexer/overlay.rs:414-419] |
| `rel_matches_filter` | function | Returns 'true' when the canonicalized absolute path of 'root_path.join(rel)' begins with the canonicalized absolute filter path derived from 'path_filter' (or 'root_path.join(path_filter)' if relative), otherwise 'false'. [crates/gcode/src/index/indexer/overlay.rs:421-434] |
| `write_tombstone` | function | Starts a database transaction, deletes existing code facts for the given project-relative file, inserts a tombstone 'IndexedFile' record with tombstone language/hash and zero counts, then commits the transaction. [crates/gcode/src/index/indexer/overlay.rs:436-452] |

_Verified by 3 in-file unit tests._

