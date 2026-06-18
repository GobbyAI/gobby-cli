---
title: crates/gcode/src/git.rs
type: code_file
provenance:
- file: crates/gcode/src/git.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/git.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The file `crates/gcode/src/git.rs` is responsible for querying, resolving, and classifying Git worktree metadata for a given path. It provides a structured way to determine whether a particular directory belongs to a main Git worktree, a linked worktree, or is not part of a Git repository at all.

To model this, the file defines structural types such as the `WorktreeKind` enum [crates/gcode/src/git.rs:5-9] and the `WorktreeInfo` struct [crates/gcode/src/git.rs:12-17]. These structures store canonicalized paths for the project top-level, the Git directory, and the shared common Git directory, providing a structured description of a Git environment.

## How it fits

The primary entry point is the `worktree_info` function [crates/gcode/src/git.rs:19-51]. When invoked, it triggers a low-level helper `git_output` [crates/gcode/src/git.rs:53-63] to run commands like `git rev-parse` against the target path. If the command fails, the module safely falls back to classifying the path as `WorktreeKind::NotGit` [crates/gcode/src/git.rs:21-32].

## Key components

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
| `detects_normal_repo_as_main_worktree` | function | Initializes a normal Git repository in a temporary directory and verifies that 'worktree_info' identifies it as the main worktree, with 'top_level' equal to the canonical repo path and 'git_dir' matching 'git_common_dir'. [crates/gcode/src/git.rs:121-132] |
| `detects_linked_worktree` | function | Creates a temporary Git repository, adds a linked worktree, and verifies that 'worktree_info' classifies it as 'WorktreeKind::Linked' with a canonicalized top-level path different from the common Git directory. [crates/gcode/src/git.rs:135-158] |
| `separate_git_dir_is_main_worktree` | function | Verifies that a repository initialized with 'git init --separate-git-dir' is reported as the main worktree and that both 'git_dir' and 'git_common_dir' resolve to the canonicalized separate git directory. [crates/gcode/src/git.rs:161-181] |

