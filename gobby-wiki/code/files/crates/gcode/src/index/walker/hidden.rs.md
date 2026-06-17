---
title: crates/gcode/src/index/walker/hidden.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/hidden.rs
  ranges:
  - 13-15
  - 18-25
  - 27-35
  - 37-53
  - 55-63
  - 66-80
  - 82-94
  - 96-102
  - 104-107
  - 109-117
  - 119-149
  - 151-176
  - 178-186
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/walker/hidden.rs:13-15](crates/gcode/src/index/walker/hidden.rs#L13-L15), [crates/gcode/src/index/walker/hidden.rs:18-25](crates/gcode/src/index/walker/hidden.rs#L18-L25), [crates/gcode/src/index/walker/hidden.rs:27-35](crates/gcode/src/index/walker/hidden.rs#L27-L35), [crates/gcode/src/index/walker/hidden.rs:37-53](crates/gcode/src/index/walker/hidden.rs#L37-L53), [crates/gcode/src/index/walker/hidden.rs:55-63](crates/gcode/src/index/walker/hidden.rs#L55-L63), [crates/gcode/src/index/walker/hidden.rs:66-80](crates/gcode/src/index/walker/hidden.rs#L66-L80), [crates/gcode/src/index/walker/hidden.rs:82-94](crates/gcode/src/index/walker/hidden.rs#L82-L94), [crates/gcode/src/index/walker/hidden.rs:96-102](crates/gcode/src/index/walker/hidden.rs#L96-L102), [crates/gcode/src/index/walker/hidden.rs:104-107](crates/gcode/src/index/walker/hidden.rs#L104-L107), [crates/gcode/src/index/walker/hidden.rs:109-117](crates/gcode/src/index/walker/hidden.rs#L109-L117), [crates/gcode/src/index/walker/hidden.rs:119-149](crates/gcode/src/index/walker/hidden.rs#L119-L149), [crates/gcode/src/index/walker/hidden.rs:151-176](crates/gcode/src/index/walker/hidden.rs#L151-L176), [crates/gcode/src/index/walker/hidden.rs:178-186](crates/gcode/src/index/walker/hidden.rs#L178-L186)

</details>

# crates/gcode/src/index/walker/hidden.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

Defines a hidden-path allowlist for indexing: `HiddenPathAllowlist::load` starts with built-in glob patterns for `.gobby` plans/wiki content and GitHub workflow files, then merges any project-specific patterns from `.gobby/gcode.json`. The allowlist is normalized and validated by `from_patterns`, which trims entries, converts separators, filters invalid globs, and expands zero-depth `**` cases. `discover` uses the stored patterns to glob under the project root and collect hidden files into a deduplicated list, while `matches` checks whether a given path falls under any allowlisted pattern. Supporting helpers parse the config, validate patterns, expand glob variants, build absolute glob paths, and detect hidden files or metadata-only/generated wiki content by extension and path shape.
[crates/gcode/src/index/walker/hidden.rs:13-15]
[crates/gcode/src/index/walker/hidden.rs:18-25]
[crates/gcode/src/index/walker/hidden.rs:27-35]
[crates/gcode/src/index/walker/hidden.rs:37-53]
[crates/gcode/src/index/walker/hidden.rs:55-63]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `HiddenPathAllowlist` | class | `pub(super) struct HiddenPathAllowlist {` | `HiddenPathAllowlist [class]` | `8c90ddbd-76d1-537e-965e-bfb5b6bad7e7` | 13-15 [crates/gcode/src/index/walker/hidden.rs:13-15] | Indexed class `HiddenPathAllowlist` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:13-15] |
| `HiddenPathAllowlist::load` | method | `pub(super) fn load(root: &Path) -> Self {` | `HiddenPathAllowlist::load [method]` | `564c1378-4034-5029-98d6-a99ba06facb5` | 18-25 [crates/gcode/src/index/walker/hidden.rs:18-25] | Indexed method `HiddenPathAllowlist::load` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:18-25] |
| `HiddenPathAllowlist::from_patterns` | method | `fn from_patterns(patterns: Vec<String>) -> Self {` | `HiddenPathAllowlist::from_patterns [method]` | `16cf2279-1d9b-5be4-8298-44ac12773c32` | 27-35 [crates/gcode/src/index/walker/hidden.rs:27-35] | Indexed method `HiddenPathAllowlist::from_patterns` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:27-35] |
| `HiddenPathAllowlist::discover` | method | `pub(super) fn discover(&self, root: &Path) -> Vec<PathBuf> {` | `HiddenPathAllowlist::discover [method]` | `a436b4d1-f4bf-5bb9-808d-548a0b519cff` | 37-53 [crates/gcode/src/index/walker/hidden.rs:37-53] | Indexed method `HiddenPathAllowlist::discover` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:37-53] |
| `HiddenPathAllowlist::matches` | method | `pub(super) fn matches(&self, root: &Path, path: &Path) -> bool {` | `HiddenPathAllowlist::matches [method]` | `e46fdcfb-4ce4-562c-bb65-e7f9d49fd653` | 55-63 [crates/gcode/src/index/walker/hidden.rs:55-63] | Indexed method `HiddenPathAllowlist::matches` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:55-63] |
| `read_project_hidden_allowlist` | function | `fn read_project_hidden_allowlist(root: &Path) -> Vec<String> {` | `read_project_hidden_allowlist [function]` | `fcc61879-e2e0-565d-b48b-66e80ec60933` | 66-80 [crates/gcode/src/index/walker/hidden.rs:66-80] | Indexed function `read_project_hidden_allowlist` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:66-80] |
| `is_valid_allowlist_pattern` | function | `fn is_valid_allowlist_pattern(pattern: &str) -> bool {` | `is_valid_allowlist_pattern [function]` | `04d3e0ad-4aea-5464-8fbd-8105f151e398` | 82-94 [crates/gcode/src/index/walker/hidden.rs:82-94] | Indexed function `is_valid_allowlist_pattern` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:82-94] |
| `expand_zero_depth_globstar` | function | `fn expand_zero_depth_globstar(pattern: &str) -> Vec<String> {` | `expand_zero_depth_globstar [function]` | `597f0149-1a1c-59d6-ba8f-a47a427f0f7e` | 96-102 [crates/gcode/src/index/walker/hidden.rs:96-102] | Indexed function `expand_zero_depth_globstar` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:96-102] |
| `absolute_glob_pattern` | function | `fn absolute_glob_pattern(root: &Path, pattern: &str) -> Option<String> {` | `absolute_glob_pattern [function]` | `f03ad5be-5b7c-549f-af03-280f872c9c85` | 104-107 [crates/gcode/src/index/walker/hidden.rs:104-107] | Indexed function `absolute_glob_pattern` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:104-107] |
| `is_hidden_path` | function | `pub(super) fn is_hidden_path(root: &Path, path: &Path) -> bool {` | `is_hidden_path [function]` | `1227d293-56e1-5c87-85f6-642341778536` | 109-117 [crates/gcode/src/index/walker/hidden.rs:109-117] | Indexed function `is_hidden_path` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:109-117] |
| `is_hidden_metadata_content_only` | function | `pub(super) fn is_hidden_metadata_content_only(root: &Path, path: &Path) -> bool {` | `is_hidden_metadata_content_only [function]` | `fc1e5b3d-30da-5977-aa73-739a188a2f0d` | 119-149 [crates/gcode/src/index/walker/hidden.rs:119-149] | Indexed function `is_hidden_metadata_content_only` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:119-149] |
| `is_generated_wiki_metadata` | function | `pub(super) fn is_generated_wiki_metadata(root: &Path, path: &Path) -> bool {` | `is_generated_wiki_metadata [function]` | `026d93b6-5269-50a4-8329-f8ef6bcb4cbd` | 151-176 [crates/gcode/src/index/walker/hidden.rs:151-176] | Indexed function `is_generated_wiki_metadata` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:151-176] |
| `path_has_extension` | function | `fn path_has_extension(path: &Path, extensions: &[&str]) -> bool {` | `path_has_extension [function]` | `aaa9b53c-0433-555e-afec-4bdc24232427` | 178-186 [crates/gcode/src/index/walker/hidden.rs:178-186] | Indexed function `path_has_extension` in `crates/gcode/src/index/walker/hidden.rs`. [crates/gcode/src/index/walker/hidden.rs:178-186] |
