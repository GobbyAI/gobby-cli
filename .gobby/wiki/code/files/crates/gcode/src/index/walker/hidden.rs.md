---
title: crates/gcode/src/index/walker/hidden.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/hidden.rs
  ranges:
  - 13-15
  - 17-64
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

# crates/gcode/src/index/walker/hidden.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

This file defines the hidden-path allowlist used by the index walker to decide which otherwise hidden files should be included. `HiddenPathAllowlist` loads a default set of glob patterns plus any project overrides from `.gobby/gcode.json`, normalizes and validates them, expands zero-depth globstars, and then can both discover matching hidden files under a root and test whether a specific path matches an allowed hidden-path pattern. The helper functions enforce safe pattern shapes, read project config, and classify special cases like hidden metadata and generated wiki files.
[crates/gcode/src/index/walker/hidden.rs:13-15]
[crates/gcode/src/index/walker/hidden.rs:17-64]
[crates/gcode/src/index/walker/hidden.rs:18-25]
[crates/gcode/src/index/walker/hidden.rs:27-35]
[crates/gcode/src/index/walker/hidden.rs:37-53]

## API Symbols

- `HiddenPathAllowlist` (class) component `HiddenPathAllowlist [class]` (`8c90ddbd-76d1-537e-965e-bfb5b6bad7e7`) lines 13-15 [crates/gcode/src/index/walker/hidden.rs:13-15]
  - Signature: `pub(super) struct HiddenPathAllowlist {`
  - Purpose: 'HiddenPathAllowlist' is a 'pub(super)' struct that stores a 'Vec<String>' of path-matching patterns used to permit otherwise hidden paths. [crates/gcode/src/index/walker/hidden.rs:13-15]
- `HiddenPathAllowlist` (class) component `HiddenPathAllowlist [class]` (`2f77c030-8d68-5fa6-b774-6455bc1dd62f`) lines 17-64 [crates/gcode/src/index/walker/hidden.rs:17-64]
  - Signature: `impl HiddenPathAllowlist {`
  - Purpose: 'HiddenPathAllowlist' loads and normalizes default plus project-defined allowlist glob patterns, validates and expands them, then uses them to discover hidden files under a root and test whether a given path matches any allowed hidden-path pattern. [crates/gcode/src/index/walker/hidden.rs:17-64]
- `HiddenPathAllowlist.load` (method) component `HiddenPathAllowlist.load [method]` (`564c1378-4034-5029-98d6-a99ba06facb5`) lines 18-25 [crates/gcode/src/index/walker/hidden.rs:18-25]
  - Signature: `pub(super) fn load(root: &Path) -> Self {`
  - Purpose: Constructs the value by cloning the default hidden-allowlist patterns, extending them with project-specific patterns read from 'root', and then delegating to 'Self::from_patterns(patterns)'. [crates/gcode/src/index/walker/hidden.rs:18-25]
- `HiddenPathAllowlist.from_patterns` (method) component `HiddenPathAllowlist.from_patterns [method]` (`16cf2279-1d9b-5be4-8298-44ac12773c32`) lines 27-35 [crates/gcode/src/index/walker/hidden.rs:27-35]
  - Signature: `fn from_patterns(patterns: Vec<String>) -> Self {`
  - Purpose: 'from_patterns' normalizes each input pattern by trimming whitespace and converting backslashes to forward slashes, filters out invalid allowlist patterns, expands zero-depth globstars into equivalent patterns, and collects the result into 'Self { patterns }'. [crates/gcode/src/index/walker/hidden.rs:27-35]
- `HiddenPathAllowlist.discover` (method) component `HiddenPathAllowlist.discover [method]` (`a436b4d1-f4bf-5bb9-808d-548a0b519cff`) lines 37-53 [crates/gcode/src/index/walker/hidden.rs:37-53]
  - Signature: `pub(super) fn discover(&self, root: &Path) -> Vec<PathBuf> {`
  - Purpose: Iterates over configured glob patterns, expands each to an absolute glob rooted at 'root', collects only entries that resolve to files and satisfy 'is_hidden_path(root, &entry)', deduplicates them via a 'BTreeSet', and returns the sorted results as a 'Vec<PathBuf>'. [crates/gcode/src/index/walker/hidden.rs:37-53]
- `HiddenPathAllowlist.matches` (method) component `HiddenPathAllowlist.matches [method]` (`e46fdcfb-4ce4-562c-bb65-e7f9d49fd653`) lines 55-63 [crates/gcode/src/index/walker/hidden.rs:55-63]
  - Signature: `pub(super) fn matches(&self, root: &Path, path: &Path) -> bool {`
  - Purpose: It computes 'path' relative to 'root' when possible, normalizes separators to '/', and returns 'true' if any stored glob pattern parses successfully and matches that normalized path, otherwise 'false'. [crates/gcode/src/index/walker/hidden.rs:55-63]
- `read_project_hidden_allowlist` (function) component `read_project_hidden_allowlist [function]` (`fcc61879-e2e0-565d-b48b-66e80ec60933`) lines 66-80 [crates/gcode/src/index/walker/hidden.rs:66-80]
  - Signature: `fn read_project_hidden_allowlist(root: &Path) -> Vec<String> {`
  - Purpose: Reads 'root.join(GCODE_CONFIG_PATH)' as JSON and returns the 'index.hidden_allowlist' string array as owned 'Vec<String>', or an empty vector if the file cannot be read, parsed, or the field is missing or malformed. [crates/gcode/src/index/walker/hidden.rs:66-80]
- `is_valid_allowlist_pattern` (function) component `is_valid_allowlist_pattern [function]` (`04d3e0ad-4aea-5464-8fbd-8105f151e398`) lines 82-94 [crates/gcode/src/index/walker/hidden.rs:82-94]
  - Signature: `fn is_valid_allowlist_pattern(pattern: &str) -> bool {`
  - Purpose: Returns 'true' only for non-empty, non-absolute path strings whose parsed components contain no 'ParentDir', Windows 'Prefix', or 'RootDir' segments, and 'false' otherwise. [crates/gcode/src/index/walker/hidden.rs:82-94]
- `expand_zero_depth_globstar` (function) component `expand_zero_depth_globstar [function]` (`597f0149-1a1c-59d6-ba8f-a47a427f0f7e`) lines 96-102 [crates/gcode/src/index/walker/hidden.rs:96-102]
  - Signature: `fn expand_zero_depth_globstar(pattern: &str) -> Vec<String> {`
  - Purpose: Returns a vector containing the original glob pattern and, when the pattern contains '"/**/"', an additional variant with that globstar segment collapsed to a single '/' to represent a zero-depth match. [crates/gcode/src/index/walker/hidden.rs:96-102]
- `absolute_glob_pattern` (function) component `absolute_glob_pattern [function]` (`f03ad5be-5b7c-549f-af03-280f872c9c85`) lines 104-107 [crates/gcode/src/index/walker/hidden.rs:104-107]
  - Signature: `fn absolute_glob_pattern(root: &Path, pattern: &str) -> Option<String> {`
  - Purpose: Returns 'Some' containing the glob pattern formed by escaping 'root' as a literal path prefix and concatenating '/{pattern}', or 'None' if 'root' cannot be converted to UTF-8. [crates/gcode/src/index/walker/hidden.rs:104-107]
- `is_hidden_path` (function) component `is_hidden_path [function]` (`1227d293-56e1-5c87-85f6-642341778536`) lines 109-117 [crates/gcode/src/index/walker/hidden.rs:109-117]
  - Signature: `pub(super) fn is_hidden_path(root: &Path, path: &Path) -> bool {`
  - Purpose: Returns 'true' if 'path' is under 'root' and any of its relative path components is a UTF-8 name beginning with '.' other than '.' or '..', otherwise 'false'. [crates/gcode/src/index/walker/hidden.rs:109-117]
- `is_hidden_metadata_content_only` (function) component `is_hidden_metadata_content_only [function]` (`fc1e5b3d-30da-5977-aa73-739a188a2f0d`) lines 119-149 [crates/gcode/src/index/walker/hidden.rs:119-149]
  - Signature: `pub(super) fn is_hidden_metadata_content_only(root: &Path, path: &Path) -> bool {`
  - Purpose: Returns 'true' when 'path' is at least three normal components deep under 'root' and points to a Markdown file in '.gobby/plans' or '.gobby/wiki', or to a YAML workflow file in '.github/workflows'; otherwise returns 'false'. [crates/gcode/src/index/walker/hidden.rs:119-149]
- `is_generated_wiki_metadata` (function) component `is_generated_wiki_metadata [function]` (`026d93b6-5269-50a4-8329-f8ef6bcb4cbd`) lines 151-176 [crates/gcode/src/index/walker/hidden.rs:151-176]
  - Signature: `pub(super) fn is_generated_wiki_metadata(root: &Path, path: &Path) -> bool {`
  - Purpose: Returns 'true' when 'path' is under 'root' and refers either to a '.gobby/wiki/_meta' entry or to a '.gobby/wiki' file whose basename ends with '.json.lock', after normalizing to the relative path’s non-special components. [crates/gcode/src/index/walker/hidden.rs:151-176]
- `path_has_extension` (function) component `path_has_extension [function]` (`aaa9b53c-0433-555e-afec-4bdc24232427`) lines 178-186 [crates/gcode/src/index/walker/hidden.rs:178-186]
  - Signature: `fn path_has_extension(path: &Path, extensions: &[&str]) -> bool {`
  - Purpose: Returns 'true' when 'path' has a UTF-8 extension whose ASCII-lowercased value exactly matches one of the provided 'extensions', and 'false' otherwise. [crates/gcode/src/index/walker/hidden.rs:178-186]

