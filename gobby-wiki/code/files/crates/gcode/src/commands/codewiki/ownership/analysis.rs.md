---
title: crates/gcode/src/commands/codewiki/ownership/analysis.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/analysis.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/ownership/analysis.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

This source file provides the implementation details for analyzing file ownership in a Git repository by executing and parsing `git blame` results. It serves as an analysis engine that aggregates contribution metrics, attributing line changes to individual contributors and caching the outcomes to optimize performance.

At the core of the file is the `derived_owners_for_files` function crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87, which coordinates the overall analysis process. This function resolves the Git repository, checks file content hashes to utilize cached results, and enforces global blame timeouts and cap limits to avoid expensive processes on oversized tasks.

## How it fits

It relies on types defined in its parent module, such as `CachedBlameSummary`, `OwnershipContributor`, `OwnershipMeta`, `OwnershipOptions`, and `OwnershipStatus` crates/gcode/src/commands/codewiki/ownership/analysis.rs:11-14. During execution, it modifies the provided `OwnershipMeta` to insert freshly computed file summaries crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87, ensuring that subsequent requests do not re-run git commands for unchanged files.
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `BlameContributorsOutcome` | type | Indexed type `BlameContributorsOutcome` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21] |
| `derived_owners_for_files` | function | 'derived_owners_for_files' discovers the Git repository and HEAD for 'project_root', then for each requested file up to a global timeout and blame-file cap either reuses cached contributors when the content hash matches or computes and caches them via blame, returning a 'BTreeMap' of file paths to 'OwnershipContributor' lists while updating 'status' for blame availability and partial results. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87] |
| `content_hash` | function | Computes the content hash of the file at 'project_root.join(file)' using 'hasher::file_content_hash' and returns it as 'Some(String)' on success or 'None' if hashing fails. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91] |
| `blame_file_contributors_with_timeout` | function | Wraps 'blame_file_contributors' and converts its 'Result<Option<...>, _>' into 'BlameContributorsOutcome', returning 'Success(contributors)' on 'Ok(Some(...))', 'Timeout' on 'Ok(None)', and 'Error(error)' on 'Err(error)'. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104] |
| `GitBlameOutput` | class | 'GitBlameOutput' is a private module-visible struct that encapsulates the result of a 'git blame'-related process invocation, storing its 'ExitStatus' plus captured 'stdout' and 'stderr' as 'String's. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110] |
| `blame_file_contributors` | function | Runs 'git blame' with a timeout for the specified file at the given commit in 'project_root', returns 'Ok(None)' if the blame command times out or produces no output, bails on non-success exit status with stderr when available, and otherwise parses the porcelain blame output into 'Vec<OwnershipContributor>'. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:112-133] |
| `git_blame_output_with_timeout` | function | Spawns 'git blame --line-porcelain' for 'file' at 'head' in 'project_root', captures stdout/stderr to temp files, returns 'Ok(Some(GitBlameOutput))' with the exit status and captured output if the process finishes before 'timeout', and otherwise kills the child and returns 'Ok(None)'. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:135-165] |
| `read_tempfile` | function | Seeks the given file to the beginning, reads all bytes to EOF, and returns them as a UTF-8 lossy 'String' in an 'anyhow::Result'. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:167-172] |
| `parse_git_blame_porcelain` | function | Parses 'git blame --porcelain' output into per-contributor line counts keyed by a deterministic contributor ID, merges identity variants while preserving stable name/email selection, sorts contributors by descending lines then name then ID, and returns the top five 'OwnershipContributor' records. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:174-227] |
| `git_blame_email` | function | Returns 'Some' with the input trimmed of surrounding whitespace and, if present, a single leading '<' and trailing '>', otherwise returns 'None' for an empty result. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:229-236] |
| `contributor_id` | function | Returns the SHA-256 hex digest of the contributor’s normalized identity, using the trimmed non-empty email if provided or otherwise the trimmed name, converted to lowercase before hashing. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:238-247] |
| `retain_deterministic_identity` | function | Updates 'stored_name' and 'stored_email' in place to retain the lexicographically smallest non-'None' name and email seen so far, using deterministic ordering comparisons. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:249-263] |

