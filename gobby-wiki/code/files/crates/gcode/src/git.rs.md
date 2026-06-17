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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/git.rs:5-9](crates/gcode/src/git.rs#L5-L9), [crates/gcode/src/git.rs:12-17](crates/gcode/src/git.rs#L12-L17), [crates/gcode/src/git.rs:19-51](crates/gcode/src/git.rs#L19-L51), [crates/gcode/src/git.rs:53-63](crates/gcode/src/git.rs#L53-L63), [crates/gcode/src/git.rs:65-77](crates/gcode/src/git.rs#L65-L77), [crates/gcode/src/git.rs:79-87](crates/gcode/src/git.rs#L79-L87), [crates/gcode/src/git.rs:93-101](crates/gcode/src/git.rs#L93-L101), [crates/gcode/src/git.rs:103-118](crates/gcode/src/git.rs#L103-L118), [crates/gcode/src/git.rs:121-132](crates/gcode/src/git.rs#L121-L132), [crates/gcode/src/git.rs:135-158](crates/gcode/src/git.rs#L135-L158), [crates/gcode/src/git.rs:161-181](crates/gcode/src/git.rs#L161-L181)

</details>

# crates/gcode/src/git.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file inspects a filesystem path with `git` and classifies it as a normal repository, a linked worktree, or not a git repo. `worktree_info` is the entry point: it asks `git rev-parse` for the top-level, git dir, and common dir, falls back to an absolute path if the path is not under git, and returns a `WorktreeInfo` record with the resolved locations and `WorktreeKind`. The helper functions handle the subprocess call, resolve relative git paths against either the worktree root or git dir, and provide an absolute-path fallback when canonicalization is unavailable. The tests verify the three main cases: a standard repo, a linked worktree, and a repo with a separate git dir that should still count as the main worktree.
[crates/gcode/src/git.rs:5-9]
[crates/gcode/src/git.rs:12-17]
[crates/gcode/src/git.rs:19-51]
[crates/gcode/src/git.rs:53-63]
[crates/gcode/src/git.rs:65-77]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WorktreeKind` | type | `pub enum WorktreeKind {` | `WorktreeKind [type]` | `63bb9aec-16fc-5ad9-a688-0860d4308d52` | 5-9 [crates/gcode/src/git.rs:5-9] | Indexed type `WorktreeKind` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:5-9] |
| `WorktreeInfo` | class | `pub struct WorktreeInfo {` | `WorktreeInfo [class]` | `d19e4784-7058-56e5-935c-839bad7b4ba8` | 12-17 [crates/gcode/src/git.rs:12-17] | Indexed class `WorktreeInfo` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:12-17] |
| `worktree_info` | function | `pub fn worktree_info(path: &Path) -> anyhow::Result<WorktreeInfo> {` | `worktree_info [function]` | `4b64c580-012c-5152-bc7f-77b063ea1f16` | 19-51 [crates/gcode/src/git.rs:19-51] | Indexed function `worktree_info` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:19-51] |
| `git_output` | function | `fn git_output(path: &Path, args: &[&str]) -> anyhow::Result<String> {` | `git_output [function]` | `c6c9952c-f499-59f1-a3a7-228af73775c0` | 53-63 [crates/gcode/src/git.rs:53-63] | Indexed function `git_output` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:53-63] |
| `resolve_git_path` | function | `fn resolve_git_path(top_level: &Path, git_dir: &Path, raw: &str) -> anyhow::Result<PathBuf> {` | `resolve_git_path [function]` | `a08cf2db-7372-5dfe-a89b-bd91a7718832` | 65-77 [crates/gcode/src/git.rs:65-77] | Indexed function `resolve_git_path` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:65-77] |
| `absolute_fallback` | function | `fn absolute_fallback(path: &Path) -> PathBuf {` | `absolute_fallback [function]` | `157847af-48e7-5d92-bad8-81587335dc7d` | 79-87 [crates/gcode/src/git.rs:79-87] | Indexed function `absolute_fallback` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:79-87] |
| `run_git` | function | `fn run_git(dir: &Path, args: &[&str]) {` | `run_git [function]` | `6369616b-6763-5839-8398-6e5919931a66` | 93-101 [crates/gcode/src/git.rs:93-101] | Indexed function `run_git` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:93-101] |
| `commit_initial` | function | `fn commit_initial(repo: &Path) {` | `commit_initial [function]` | `a0e3ea24-d249-5435-a042-1c1868843b27` | 103-118 [crates/gcode/src/git.rs:103-118] | Indexed function `commit_initial` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:103-118] |
| `detects_normal_repo_as_main_worktree` | function | `fn detects_normal_repo_as_main_worktree() {` | `detects_normal_repo_as_main_worktree [function]` | `6220f704-f110-57b1-a0c0-2899a36f789c` | 121-132 [crates/gcode/src/git.rs:121-132] | Indexed function `detects_normal_repo_as_main_worktree` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:121-132] |
| `detects_linked_worktree` | function | `fn detects_linked_worktree() {` | `detects_linked_worktree [function]` | `b87cdc42-5bcc-585e-9b08-637867a3a64e` | 135-158 [crates/gcode/src/git.rs:135-158] | Indexed function `detects_linked_worktree` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:135-158] |
| `separate_git_dir_is_main_worktree` | function | `fn separate_git_dir_is_main_worktree() {` | `separate_git_dir_is_main_worktree [function]` | `e66daca7-0fa1-5221-ad7c-5ef33df84450` | 161-181 [crates/gcode/src/git.rs:161-181] | Indexed function `separate_git_dir_is_main_worktree` in `crates/gcode/src/git.rs`. [crates/gcode/src/git.rs:161-181] |
