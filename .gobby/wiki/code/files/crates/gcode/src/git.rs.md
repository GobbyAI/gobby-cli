---
title: crates/gcode/src/git.rs
type: code_file
provenance:
- file: crates/gcode/src/git.rs
  ranges:
  - 5-9
  - 12-17
  - 19-51
  - 53-63
  - 65-77
  - 79-87
  - 93-101
  - 103-118
  - 121-132
  - 135-158
  - 161-181
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/git.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/git.rs` exposes 11 indexed API symbols.
[crates/gcode/src/git.rs:5-9]
[crates/gcode/src/git.rs:12-17]
[crates/gcode/src/git.rs:19-51]
[crates/gcode/src/git.rs:53-63]
[crates/gcode/src/git.rs:65-77]
[crates/gcode/src/git.rs:79-87]
[crates/gcode/src/git.rs:93-101]
[crates/gcode/src/git.rs:103-118]
[crates/gcode/src/git.rs:121-132]
[crates/gcode/src/git.rs:135-158]
[crates/gcode/src/git.rs:161-181]

## API Symbols

- `WorktreeKind` (type) component `WorktreeKind [type]` (`63bb9aec-16fc-5ad9-a688-0860d4308d52`) lines 5-9 [crates/gcode/src/git.rs:5-9]
  - Signature: `pub enum WorktreeKind {`
  - Purpose: Indexed type `WorktreeKind` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:5-9]
- `WorktreeInfo` (class) component `WorktreeInfo [class]` (`d19e4784-7058-56e5-935c-839bad7b4ba8`) lines 12-17 [crates/gcode/src/git.rs:12-17]
  - Signature: `pub struct WorktreeInfo {`
  - Purpose: `WorktreeInfo` is a metadata container that stores the root directory path, optional git and common directory references, and type classification for a git worktree. [crates/gcode/src/git.rs:12-17]
- `worktree_info` (function) component `worktree_info [function]` (`4b64c580-012c-5152-bc7f-77b063ea1f16`) lines 19-51 [crates/gcode/src/git.rs:19-51]
  - Signature: `pub fn worktree_info(path: &Path) -> anyhow::Result<WorktreeInfo> {`
  - Purpose: Resolves and canonicalizes Git repository metadata (top-level directory, git directory, and common directory) for a given path, classifying it as a main worktree, linked worktree, or non-Git directory. [crates/gcode/src/git.rs:19-51]
- `git_output` (function) component `git_output [function]` (`c6c9952c-f499-59f1-a3a7-228af73775c0`) lines 53-63 [crates/gcode/src/git.rs:53-63]
  - Signature: `fn git_output(path: &Path, args: &[&str]) -> anyhow::Result<String> {`
  - Purpose: Executes a git command at a specified directory path with given arguments and returns the trimmed stdout output as a UTF-8 string, or an error if the command fails. [crates/gcode/src/git.rs:53-63]
- `resolve_git_path` (function) component `resolve_git_path [function]` (`a08cf2db-7372-5dfe-a89b-bd91a7718832`) lines 65-77 [crates/gcode/src/git.rs:65-77]
  - Signature: `fn resolve_git_path(top_level: &Path, git_dir: &Path, raw: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: Resolves a path string to a canonicalized absolute path by attempting resolution relative to the repository root first, falling back to the git directory if the path doesn't exist at the root. [crates/gcode/src/git.rs:65-77]
- `absolute_fallback` (function) component `absolute_fallback [function]` (`157847af-48e7-5d92-bad8-81587335dc7d`) lines 79-87 [crates/gcode/src/git.rs:79-87]
  - Signature: `fn absolute_fallback(path: &Path) -> PathBuf {`
  - Purpose: Converts a relative path to an absolute path by joining it with the current working directory, or falls back to the system temp directory if the current directory is inaccessible. [crates/gcode/src/git.rs:79-87]
- `run_git` (function) component `run_git [function]` (`6369616b-6763-5839-8398-6e5919931a66`) lines 93-101 [crates/gcode/src/git.rs:93-101]
  - Signature: `fn run_git(dir: &Path, args: &[&str]) {`
  - Purpose: Executes a git command in a specified directory with provided arguments and panics if the subprocess returns a non-zero exit status. [crates/gcode/src/git.rs:93-101]
- `commit_initial` (function) component `commit_initial [function]` (`a0e3ea24-d249-5435-a042-1c1868843b27`) lines 103-118 [crates/gcode/src/git.rs:103-118]
  - Signature: `fn commit_initial(repo: &Path) {`
  - Purpose: Creates a README.md file with "hello" content, stages it, and commits it to the repository with configured test user credentials. [crates/gcode/src/git.rs:103-118]
- `detects_normal_repo_as_main_worktree` (function) component `detects_normal_repo_as_main_worktree [function]` (`6220f704-f110-57b1-a0c0-2899a36f789c`) lines 121-132 [crates/gcode/src/git.rs:121-132]
  - Signature: `fn detects_normal_repo_as_main_worktree() {`
  - Purpose: This test asserts that a standard git repository initialized with `git init` is correctly detected as the main worktree with its git_dir equal to git_common_dir. [crates/gcode/src/git.rs:121-132]
- `detects_linked_worktree` (function) component `detects_linked_worktree [function]` (`b87cdc42-5bcc-585e-9b08-637867a3a64e`) lines 135-158 [crates/gcode/src/git.rs:135-158]
  - Signature: `fn detects_linked_worktree() {`
  - Purpose: This test function verifies that `worktree_info()` correctly identifies a git-linked worktree by asserting it returns `WorktreeKind::Linked`, the canonical worktree path, and separate git directory references. [crates/gcode/src/git.rs:135-158]
- `separate_git_dir_is_main_worktree` (function) component `separate_git_dir_is_main_worktree [function]` (`e66daca7-0fa1-5221-ad7c-5ef33df84450`) lines 161-181 [crates/gcode/src/git.rs:161-181]
  - Signature: `fn separate_git_dir_is_main_worktree() {`
  - Purpose: Tests that a Git repository initialized with `--separate-git-dir` is correctly identified as the main worktree with both `git_dir` and `git_common_dir` pointing to the separate git directory. [crates/gcode/src/git.rs:161-181]

