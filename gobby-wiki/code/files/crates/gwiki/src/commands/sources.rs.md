---
title: crates/gwiki/src/commands/sources.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/sources.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/sources.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/sources.rs` exposes 41 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/sources.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the selected command scope, validates its root, reads the source manifest and source entries while collecting degradations, and returns a rendered 'CommandOutcome' for the resolved scope. [crates/gwiki/src/commands/sources.rs:15-23] |
| `execute_remove` | function | Stages removal of a source identified by 'id' within the resolved scope, optionally performing a dry run and preserving the asset, by updating raw/asset file paths, deleting the manifest entry, and rolling back staged filesystem changes if cleanup fails. [crates/gwiki/src/commands/sources.rs:25-122] |
| `SourceListEntry` | class | 'SourceListEntry' is a serializable Rust struct that records metadata for a source item, including its identity, kind, title, location, citation, content hash, fetch timestamp, compile status, raw file path/existence, and optional source asset reference. [crates/gwiki/src/commands/sources.rs:125-138] |
| `IndexStatus` | class | 'IndexStatus' is a serializable struct that reports an index’s current status string, whether indexing is required, and an optional 'IndexedCounts' payload included only when present. [crates/gwiki/src/commands/sources.rs:141-146] |
| `IndexStatus::not_run` | method | Constructs and returns a 'Self' instance initialized with 'status' set to '"not_run"', 'index_required' set to 'false', and 'indexed' set to 'None'. [crates/gwiki/src/commands/sources.rs:149-155] |
| `IndexStatus::indexed` | method | Constructs a 'Self' value with 'status' set to '"indexed"', 'index_required' set to 'false', and 'indexed' populated with 'Some(IndexedCounts::from(counts))'. [crates/gwiki/src/commands/sources.rs:157-163] |
| `IndexStatus::degraded` | method | Constructs and returns a 'Self' value with 'status' set to '"degraded"', 'index_required' set to 'true', and 'indexed' set to 'None'. [crates/gwiki/src/commands/sources.rs:165-171] |
| `IndexedCounts` | class | 'IndexedCounts' is a struct of five 'usize' counters tracking the number of 'documents', 'chunks', 'links', 'sources', and 'ingestions' in an index. [crates/gwiki/src/commands/sources.rs:175-181] |
| `IndexedCounts::from` | method | Constructs 'Self' by moving the 'documents', 'chunks', 'links', 'sources', and 'ingestions' counts from the provided 'IndexCounts' into the corresponding fields. [crates/gwiki/src/commands/sources.rs:184-192] |
| `RemoveSourceRender` | class | 'RemoveSourceRender' is a render-state struct that captures the scope, dry-run mode, source entry, path removal outcomes, index status, degradations, and follow-up actions for a source-removal operation. [crates/gwiki/src/commands/sources.rs:195-205] |
| `PathChanges` | class | 'PathChanges' is a record of path-state transitions containing the paths removed, kept, and missing, plus staged removal metadata in 'staged_removals'. [crates/gwiki/src/commands/sources.rs:208-213] |
| `StagedRemoval` | class | 'StagedRemoval' is a data-only struct that represents a staged file deletion or replacement payload by pairing a relative path with an associated byte buffer. [crates/gwiki/src/commands/sources.rs:216-219] |
| `source_entries` | function | Maps each 'SourceRecord' in 'records' through 'source_entry(vault_root, ...)', accumulating any degradation messages in 'degradations', and collects the results into a 'Vec<SourceListEntry>' or returns the first 'WikiError' encountered. [crates/gwiki/src/commands/sources.rs:221-230] |
| `source_entry` | function | Constructs a 'SourceListEntry' from a 'SourceRecord' by resolving its raw path under 'vault_root', optionally loading the corresponding source asset if the raw file exists, recording a 'raw_missing:<path>' degradation when it does not, and copying the record fields into the returned entry. [crates/gwiki/src/commands/sources.rs:232-260] |
| `read_source_asset` | function | Reads the file at 'raw_full_path', parses its frontmatter, and returns the trimmed 'source_asset' metadata string if it exists and is non-empty, otherwise records a degradation on parse/type errors and returns 'Ok(None)', propagating I/O failures as 'WikiError::Io'. [crates/gwiki/src/commands/sources.rs:262-301] |
| `stage_raw_source` | function | 'stage_raw_source' stages the removal of an existing raw source file by delegating to 'stage_source_removal' when 'raw_exists' is true, otherwise records the raw path as missing in 'path_changes', and always returns 'Ok(())' unless the delegated removal staging fails. [crates/gwiki/src/commands/sources.rs:303-316] |
| `stage_source_asset` | function | Stages a source asset by recording it as kept when 'keep_asset' is true, otherwise removing it if the resolved file exists under 'vault_root' or marking it missing and logging a 'source_asset_missing' degradation. [crates/gwiki/src/commands/sources.rs:318-340] |
| `stage_source_removal` | function | Records a source path as removed in 'path_changes', and if 'cache_bytes' is true, reads the file from 'vault_root' and stages its contents in 'staged_removals', returning any I/O error encountered while reading. [crates/gwiki/src/commands/sources.rs:342-363] |
| `remove_staged_source_files` | function | Deletes each staged source file under 'vault_root', records successfully removed relative paths in 'path_changes.removed_paths', moves missing files to 'path_changes.missing_paths', preserves successfully processed removals in 'path_changes.staged_removals', and returns an 'Io'-wrapped 'WikiError' on any non-'NotFound' filesystem error after restoring partial progress. [crates/gwiki/src/commands/sources.rs:365-396] |
| `restore_removed_source_files` | function | Attempts to restore each staged removal whose relative path still appears in 'path_changes.removed_paths' by recreating parent directories and rewriting the original bytes under 'vault_root', collecting any I/O failures and returning a 'WikiError::Config' summarizing the restoration errors if any occur. [crates/gwiki/src/commands/sources.rs:398-441] |
| `rollback_removed_source_state` | function | Attempts to roll back a removed source by restoring both the manifest entry and affected files, returning 'Ok(())' if both succeed, propagating a single rollback error if only one fails, or wrapping both failures in a 'WikiError::Config' if neither rollback step succeeds. [crates/gwiki/src/commands/sources.rs:443-462] |
| `rollback_removed_source` | function | Appends the removed 'SourceRecord' back into the source manifest at 'vault_root' unless the manifest already contains that source ID, and converts any rollback failure into a 'WikiError::Config' that includes both the rollback and original errors. [crates/gwiki/src/commands/sources.rs:464-486] |
| `raw_source_path` | function | Returns the result of 'paths::raw_source_path(id)', forwarding the given 'id' to produce a 'PathBuf' or 'WikiError'. [crates/gwiki/src/commands/sources.rs:488-490] |
| `source_asset_path` | function | Validates that 'value' is a vault-relative raw asset path under 'raw/assets', and if the target exists, canonicalizes both vault and target to reject symlink-resolved paths that escape the vault, returning the relative 'PathBuf' or a 'WikiError'. [crates/gwiki/src/commands/sources.rs:492-525] |

_9 more symbol(s) not shown — run `gcode outline crates/gwiki/src/commands/sources.rs` for the full list._

_Verified by 8 in-file unit tests._

