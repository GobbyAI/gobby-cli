---
title: crates/gcode/src/commands/scope.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/scope.rs
  ranges:
  - 9-12
  - 14-27
  - 29-45
  - 47-60
  - 62-69
  - 71-109
  - 111-133
  - 135-146
  - 153-167
  - 170-182
  - 185-190
  - 193-208
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/scope.rs:9-12](crates/gcode/src/commands/scope.rs#L9-L12), [crates/gcode/src/commands/scope.rs:14-27](crates/gcode/src/commands/scope.rs#L14-L27), [crates/gcode/src/commands/scope.rs:29-45](crates/gcode/src/commands/scope.rs#L29-L45), [crates/gcode/src/commands/scope.rs:47-60](crates/gcode/src/commands/scope.rs#L47-L60), [crates/gcode/src/commands/scope.rs:62-69](crates/gcode/src/commands/scope.rs#L62-L69), [crates/gcode/src/commands/scope.rs:71-109](crates/gcode/src/commands/scope.rs#L71-L109), [crates/gcode/src/commands/scope.rs:111-133](crates/gcode/src/commands/scope.rs#L111-L133), [crates/gcode/src/commands/scope.rs:135-146](crates/gcode/src/commands/scope.rs#L135-L146), [crates/gcode/src/commands/scope.rs:153-167](crates/gcode/src/commands/scope.rs#L153-L167), [crates/gcode/src/commands/scope.rs:170-182](crates/gcode/src/commands/scope.rs#L170-L182), [crates/gcode/src/commands/scope.rs:185-190](crates/gcode/src/commands/scope.rs#L185-L190), [crates/gcode/src/commands/scope.rs:193-208](crates/gcode/src/commands/scope.rs#L193-L208)

</details>

# crates/gcode/src/commands/scope.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

This module centralizes file-scope handling for gcode commands: it normalizes user-supplied file arguments against the current project root, cleans relative paths, and checks whether a path exists and is valid within the active project or an overlay scope. It also queries indexed projects to find a matching project for a file path, with `ProjectMatch` carrying the matched project id and root path. The helpers work together so callers can resolve paths, verify they stay under the intended root, and confirm the file is both present on disk and indexed; the tests exercise absolute-path normalization, root-component stripping, and overlay parent-file acceptance.
[crates/gcode/src/commands/scope.rs:9-12]
[crates/gcode/src/commands/scope.rs:14-27]
[crates/gcode/src/commands/scope.rs:29-45]
[crates/gcode/src/commands/scope.rs:47-60]
[crates/gcode/src/commands/scope.rs:62-69]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ProjectMatch` | class | `pub(crate) struct ProjectMatch {` | `ProjectMatch [class]` | `c5f4af9f-e5e2-5f91-94b1-f84a537c3519` | 9-12 [crates/gcode/src/commands/scope.rs:9-12] | Indexed class `ProjectMatch` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:9-12] |
| `normalize_file_arg` | function | `pub(crate) fn normalize_file_arg(ctx: &Context, file: &str) -> String {` | `normalize_file_arg [function]` | `2b5cb0d6-435f-5628-b32d-56d21830ef86` | 14-27 [crates/gcode/src/commands/scope.rs:14-27] | Indexed function `normalize_file_arg` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:14-27] |
| `path_exists_in_current_project` | function | `pub(crate) fn path_exists_in_current_project(ctx: &Context, file_path: &str) -> bool {` | `path_exists_in_current_project [function]` | `5ae4ac2e-7d6a-5186-9c1e-aabc0511eb89` | 29-45 [crates/gcode/src/commands/scope.rs:29-45] | Indexed function `path_exists_in_current_project` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:29-45] |
| `path_exists_under_root` | function | `fn path_exists_under_root(root: &Path, file_path: &str) -> bool {` | `path_exists_under_root [function]` | `0c4fe9ea-00da-56d3-809d-e6ec5730b527` | 47-60 [crates/gcode/src/commands/scope.rs:47-60] | Indexed function `path_exists_under_root` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:47-60] |
| `current_indexed_path_is_valid` | function | `pub(crate) fn current_indexed_path_is_valid(` | `current_indexed_path_is_valid [function]` | `9adda441-01c3-5af5-9e3c-ff8b1f4dd075` | 62-69 [crates/gcode/src/commands/scope.rs:62-69] | Indexed function `current_indexed_path_is_valid` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:62-69] |
| `other_project_for_path` | function | `pub(crate) fn other_project_for_path(` | `other_project_for_path [function]` | `3c6c8f86-0784-59a2-9637-dbc84345ada7` | 71-109 [crates/gcode/src/commands/scope.rs:71-109] | Indexed function `other_project_for_path` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:71-109] |
| `indexed_project_for_file_path` | function | `fn indexed_project_for_file_path(` | `indexed_project_for_file_path [function]` | `de1879e6-045a-5749-b421-5509cebac207` | 111-133 [crates/gcode/src/commands/scope.rs:111-133] | Indexed function `indexed_project_for_file_path` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:111-133] |
| `clean_relative_path` | function | `fn clean_relative_path(path: &Path) -> String {` | `clean_relative_path [function]` | `04752993-633e-5e0c-b1b3-487a7076ecca` | 135-146 [crates/gcode/src/commands/scope.rs:135-146] | Indexed function `clean_relative_path` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:135-146] |
| `context_for` | function | `fn context_for(root: PathBuf) -> Context {` | `context_for [function]` | `7808a652-8f5d-5a8d-ac48-7c9b6419a561` | 153-167 [crates/gcode/src/commands/scope.rs:153-167] | Indexed function `context_for` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:153-167] |
| `normalizes_absolute_path_inside_project` | function | `fn normalizes_absolute_path_inside_project() {` | `normalizes_absolute_path_inside_project [function]` | `0b01faac-d7b4-54e8-ba2f-beeaa4a59bdd` | 170-182 [crates/gcode/src/commands/scope.rs:170-182] | Indexed function `normalizes_absolute_path_inside_project` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:170-182] |
| `clean_relative_path_drops_absolute_root_components` | function | `fn clean_relative_path_drops_absolute_root_components() {` | `clean_relative_path_drops_absolute_root_components [function]` | `23898ad3-c36e-5cf8-91c7-97114cd11c8f` | 185-190 [crates/gcode/src/commands/scope.rs:185-190] | Indexed function `clean_relative_path_drops_absolute_root_components` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:185-190] |
| `path_exists_accepts_overlay_parent_files` | function | `fn path_exists_accepts_overlay_parent_files() {` | `path_exists_accepts_overlay_parent_files [function]` | `f1c5865b-9662-55fc-a25a-bdd20df6d657` | 193-208 [crates/gcode/src/commands/scope.rs:193-208] | Indexed function `path_exists_accepts_overlay_parent_files` in `crates/gcode/src/commands/scope.rs`. [crates/gcode/src/commands/scope.rs:193-208] |
