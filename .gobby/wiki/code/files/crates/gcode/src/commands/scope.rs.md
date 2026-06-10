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

# crates/gcode/src/commands/scope.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/scope.rs` exposes 12 indexed API symbols.
[crates/gcode/src/commands/scope.rs:9-12]
[crates/gcode/src/commands/scope.rs:14-27]
[crates/gcode/src/commands/scope.rs:29-45]
[crates/gcode/src/commands/scope.rs:47-60]
[crates/gcode/src/commands/scope.rs:62-69]
[crates/gcode/src/commands/scope.rs:71-109]
[crates/gcode/src/commands/scope.rs:111-133]
[crates/gcode/src/commands/scope.rs:135-146]
[crates/gcode/src/commands/scope.rs:153-167]
[crates/gcode/src/commands/scope.rs:170-182]
[crates/gcode/src/commands/scope.rs:185-190]
[crates/gcode/src/commands/scope.rs:193-208]

## API Symbols

- `ProjectMatch` (class) component `ProjectMatch [class]` (`c5f4af9f-e5e2-5f91-94b1-f84a537c3519`) lines 9-12 [crates/gcode/src/commands/scope.rs:9-12]
  - Signature: `pub(crate) struct ProjectMatch {`
  - Purpose: `ProjectMatch` is a crate-internal struct that pairs a project identifier with its root filesystem path. [crates/gcode/src/commands/scope.rs:9-12]
- `normalize_file_arg` (function) component `normalize_file_arg [function]` (`2b5cb0d6-435f-5628-b32d-56d21830ef86`) lines 14-27 [crates/gcode/src/commands/scope.rs:14-27]
  - Signature: `pub(crate) fn normalize_file_arg(ctx: &Context, file: &str) -> String {`
  - Purpose: Normalizes a file path argument to a cleaned relative path from the project root, with canonicalization as a fallback for absolute paths. [crates/gcode/src/commands/scope.rs:14-27]
- `path_exists_in_current_project` (function) component `path_exists_in_current_project [function]` (`5ae4ac2e-7d6a-5186-9c1e-aabc0511eb89`) lines 29-45 [crates/gcode/src/commands/scope.rs:29-45]
  - Signature: `pub(crate) fn path_exists_in_current_project(ctx: &Context, file_path: &str) -> bool {`
  - Purpose: Checks whether a file path exists under the current project root or, if the index scope is configured as an Overlay, under either the overlay or parent root. [crates/gcode/src/commands/scope.rs:29-45]
- `path_exists_under_root` (function) component `path_exists_under_root [function]` (`0c4fe9ea-00da-56d3-809d-e6ec5730b527`) lines 47-60 [crates/gcode/src/commands/scope.rs:47-60]
  - Signature: `fn path_exists_under_root(root: &Path, file_path: &str) -> bool {`
  - Purpose: Confirms that a file exists and is located within a specified root directory by verifying the canonicalized absolute path is prefixed by the canonicalized root path. [crates/gcode/src/commands/scope.rs:47-60]
- `current_indexed_path_is_valid` (function) component `current_indexed_path_is_valid [function]` (`9adda441-01c3-5af5-9e3c-ff8b1f4dd075`) lines 62-69 [crates/gcode/src/commands/scope.rs:62-69]
  - Signature: `pub(crate) fn current_indexed_path_is_valid(`
  - Purpose: Verifies that a file path is both indexed in the database and exists within the current project context. [crates/gcode/src/commands/scope.rs:62-69]
- `other_project_for_path` (function) component `other_project_for_path [function]` (`3c6c8f86-0784-59a2-9637-dbc84345ada7`) lines 71-109 [crates/gcode/src/commands/scope.rs:71-109]
  - Signature: `pub(crate) fn other_project_for_path(`
  - Purpose: Returns the first indexed project (other than the current one) whose filesystem root contains the specified file path. [crates/gcode/src/commands/scope.rs:71-109]
- `indexed_project_for_file_path` (function) component `indexed_project_for_file_path [function]` (`de1879e6-045a-5749-b421-5509cebac207`) lines 111-133 [crates/gcode/src/commands/scope.rs:111-133]
  - Signature: `fn indexed_project_for_file_path(`
  - Purpose: Queries the database to retrieve the ID and root path of the first indexed project containing the specified file path, excluding the current project. [crates/gcode/src/commands/scope.rs:111-133]
- `clean_relative_path` (function) component `clean_relative_path [function]` (`04752993-633e-5e0c-b1b3-487a7076ecca`) lines 135-146 [crates/gcode/src/commands/scope.rs:135-146]
  - Signature: `fn clean_relative_path(path: &Path) -> String {`
  - Purpose: Normalizes a path into a relative string representation by omitting root and current-directory components while preserving normal path segments and parent-directory references, with backslashes converted to forward slashes. [crates/gcode/src/commands/scope.rs:135-146]
- `context_for` (function) component `context_for [function]` (`7808a652-8f5d-5a8d-ac48-7c9b6419a561`) lines 153-167 [crates/gcode/src/commands/scope.rs:153-167]
  - Signature: `fn context_for(root: PathBuf) -> Context {`
  - Purpose: Initializes a `Context` struct with a hardcoded PostgreSQL test database URL, the provided project root path, and default configuration values for indexing, embedding, and vector settings. [crates/gcode/src/commands/scope.rs:153-167]
- `normalizes_absolute_path_inside_project` (function) component `normalizes_absolute_path_inside_project [function]` (`0b01faac-d7b4-54e8-ba2f-beeaa4a59bdd`) lines 170-182 [crates/gcode/src/commands/scope.rs:170-182]
  - Signature: `fn normalizes_absolute_path_inside_project() {`
  - Purpose: Asserts that `normalize_file_arg` correctly converts an absolute file path to a relative path within the project root context. [crates/gcode/src/commands/scope.rs:170-182]
- `clean_relative_path_drops_absolute_root_components` (function) component `clean_relative_path_drops_absolute_root_components [function]` (`23898ad3-c36e-5cf8-91c7-97114cd11c8f`) lines 185-190 [crates/gcode/src/commands/scope.rs:185-190]
  - Signature: `fn clean_relative_path_drops_absolute_root_components() {`
  - Purpose: This test verifies that `clean_relative_path()` removes the leading root separator from absolute filesystem paths, converting them to relative path strings. [crates/gcode/src/commands/scope.rs:185-190]
- `path_exists_accepts_overlay_parent_files` (function) component `path_exists_accepts_overlay_parent_files [function]` (`f1c5865b-9662-55fc-a25a-bdd20df6d657`) lines 193-208 [crates/gcode/src/commands/scope.rs:193-208]
  - Signature: `fn path_exists_accepts_overlay_parent_files() {`
  - Purpose: Tests that `path_exists_in_current_project` correctly resolves file paths from a parent project within an overlay project index scope configuration. [crates/gcode/src/commands/scope.rs:193-208]

