---
title: crates/gcode/src/git.rs
type: code_file
provenance:
- file: crates/gcode/src/git.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/git.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/git.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcode/src/git.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WorktreeKind` | type | Indexed type `WorktreeKind` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:5-9] |
| `WorktreeInfo` | class | 'WorktreeInfo' is a data structure that describes a Git worktree by storing its top-level path, optional per-worktree '.git' directory, optional shared common Git directory, and its 'WorktreeKind'. [crates/gcode/src/git.rs:12-17] |
| `worktree_info` | function | Returns the canonicalized repository top-level and Git metadata for 'path', classifying it as 'NotGit' if 'rev-parse --show-toplevel' fails, otherwise resolving 'git_dir' and 'git_common_dir' and marking the worktree as 'Main' when they match or 'Linked' when they differ. [crates/gcode/src/git.rs:19-51] |
| `git_output` | function | Runs 'git -C <path> <args...>', returns the trimmed UTF-8-lossy stdout as a 'String' on success, and bails with 'git command failed' if the command exits unsuccessfully. [crates/gcode/src/git.rs:53-63] |
| `resolve_git_path` | function | Resolves 'raw' to a canonical absolute path by returning it directly if already absolute, otherwise preferring 'top_level/raw' when that path exists and falling back to 'git_dir/raw', canonicalizing the chosen path before returning it. [crates/gcode/src/git.rs:65-77] |
| `absolute_fallback` | function | Returns 'path' unchanged if it is already absolute, otherwise prefixes it with the current working directory, falling back to the process temp directory if 'current_dir()' fails. [crates/gcode/src/git.rs:79-87] |
| `run_git` | function | Runs 'git -C <dir> <args...>', panics if the command cannot be started, and asserts that the git process exits successfully. [crates/gcode/src/git.rs:93-101] |
| `commit_initial` | function | Creates a 'README.md' containing 'hello\n' in the given repository, stages it with Git, and makes an initial commit using fixed author identity settings and the message 'initial'. [crates/gcode/src/git.rs:103-118] |

_Verified by 3 in-file unit tests._

