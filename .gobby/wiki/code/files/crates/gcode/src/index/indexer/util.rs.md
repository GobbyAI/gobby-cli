---
title: crates/gcode/src/index/indexer/util.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/util.rs
  ranges:
  - 28-66
  - 70-93
  - 95-101
  - 103-111
  - 113-142
  - 144-154
  - 156-160
  - 162-169
  - 176-186
  - 189-194
  - 197-205
  - 209-214
  - 218-223
  - 227-232
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/util.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

`crates/gcode/src/index/indexer/util.rs` exposes 14 indexed API symbols.
[crates/gcode/src/index/indexer/util.rs:28-66]
[crates/gcode/src/index/indexer/util.rs:70-93]
[crates/gcode/src/index/indexer/util.rs:95-101]
[crates/gcode/src/index/indexer/util.rs:103-111]
[crates/gcode/src/index/indexer/util.rs:113-142]

## API Symbols

- `filter_discovered_paths` (function) component `filter_discovered_paths [function]` (`5c2ff8bb-3bed-50a9-ad92-ab66a0a34c28`) lines 28-66 [crates/gcode/src/index/indexer/util.rs:28-66]
  - Signature: `pub(super) fn filter_discovered_paths(`
  - Purpose: Filters paths to include only those that are descendants of a specified filter directory, using absolute path prefix matching with canonical path comparison as a fallback for symlink resolution. [crates/gcode/src/index/indexer/util.rs:28-66]
- `unsupported_file_types` (function) component `unsupported_file_types [function]` (`f3a89c34-7edf-5690-ba9c-92c07901cf9e`) lines 70-93 [crates/gcode/src/index/indexer/util.rs:70-93]
  - Signature: `pub(super) fn unsupported_file_types(`
  - Purpose: This function aggregates unsupported file paths by extension, counting total files per type and collecting up to a configurable number of relative path examples for each type. [crates/gcode/src/index/indexer/util.rs:70-93]
- `unsupported_file_type_label` (function) component `unsupported_file_type_label [function]` (`21ee0949-01a8-5b35-b124-7a3e12a280d1`) lines 95-101 [crates/gcode/src/index/indexer/util.rs:95-101]
  - Signature: `fn unsupported_file_type_label(path: &Path) -> String {`
  - Purpose: Returns a file's lowercase extension prefixed with a dot, or the string "extensionless" if the file has no extension. [crates/gcode/src/index/indexer/util.rs:95-101]
- `requested_relative_path` (function) component `requested_relative_path [function]` (`2c3d5dde-70fb-517d-9a30-a57fc029d55a`) lines 103-111 [crates/gcode/src/index/indexer/util.rs:103-111]
  - Signature: `pub(super) fn requested_relative_path(root_path: &Path, requested_path: &Path) -> String {`
  - Purpose: Converts a requested path to a relative path string by stripping the root prefix if the path is absolute and contained within the root directory, otherwise computing a lexical relative path. [crates/gcode/src/index/indexer/util.rs:103-111]
- `lexical_relative_path` (function) component `lexical_relative_path [function]` (`1f671963-1e36-5bcb-8b36-35136e72d054`) lines 113-142 [crates/gcode/src/index/indexer/util.rs:113-142]
  - Signature: `fn lexical_relative_path(root_path: &Path, requested_path: &Path) -> String {`
  - Purpose: Constructs a lexical relative path from `root_path` to `requested_path` by finding their longest common path component prefix, then appending ".." segments for each diverging root component followed by the remaining target path components. [crates/gcode/src/index/indexer/util.rs:113-142]
- `normalized_components` (function) component `normalized_components [function]` (`7c9b4b5f-c2f2-5a8a-a844-5837e9288643`) lines 144-154 [crates/gcode/src/index/indexer/util.rs:144-154]
  - Signature: `fn normalized_components(path: &Path) -> Vec<OsString> {`
  - Purpose: Converts a path into a normalized vector of `OsString` components, filtering out current-directory references and replacing root and parent-directory components with their string representations. [crates/gcode/src/index/indexer/util.rs:144-154]
- `relative_path` (function) component `relative_path [function]` (`134005ee-5574-5385-9b33-18f72d9de8bb`) lines 156-160 [crates/gcode/src/index/indexer/util.rs:156-160]
  - Signature: `pub(super) fn relative_path(path: &Path, root: &Path) -> anyhow::Result<String> {`
  - Purpose: Computes the relative path of a given path with respect to a root directory by canonicalizing both to absolute paths and removing the root prefix. [crates/gcode/src/index/indexer/util.rs:156-160]
- `epoch_secs_str` (function) component `epoch_secs_str [function]` (`80ceb895-29f8-566e-b983-c292429f5278`) lines 162-169 [crates/gcode/src/index/indexer/util.rs:162-169]
  - Signature: `pub(super) fn epoch_secs_str() -> String {`
  - Purpose: Returns the current system time as seconds elapsed since the Unix epoch in String format, with a default fallback of "0" if system time cannot be determined. [crates/gcode/src/index/indexer/util.rs:162-169]
- `filter_discovered_paths_uses_lexical_match_before_canonicalizing` (function) component `filter_discovered_paths_uses_lexical_match_before_canonicalizing [function]` (`745d791b-9ff5-5a66-acc5-84f77ba6796d`) lines 176-186 [crates/gcode/src/index/indexer/util.rs:176-186]
  - Signature: `fn filter_discovered_paths_uses_lexical_match_before_canonicalizing() {`
  - Purpose: This test asserts that `filter_discovered_paths` correctly filters a set of discovered paths by applying lexical string matching on the path component before canonicalization. [crates/gcode/src/index/indexer/util.rs:176-186]
- `requested_relative_path_uses_relative_diff_for_absolute_paths_outside_root` (function) component `requested_relative_path_uses_relative_diff_for_absolute_paths_outside_root [function]` (`11da72a1-c6bc-5d09-b79c-f9ba71a8ad1b`) lines 189-194 [crates/gcode/src/index/indexer/util.rs:189-194]
  - Signature: `fn requested_relative_path_uses_relative_diff_for_absolute_paths_outside_root() {`
  - Purpose: Verifies that `requested_relative_path` correctly converts an absolute path outside the root directory into a relative path using parent directory traversal (`../`). [crates/gcode/src/index/indexer/util.rs:189-194]
- `requested_relative_path_preserves_absolute_root_separator` (function) component `requested_relative_path_preserves_absolute_root_separator [function]` (`56916c1b-faee-5acd-9f09-68af8ccb74cb`) lines 197-205 [crates/gcode/src/index/indexer/util.rs:197-205]
  - Signature: `fn requested_relative_path_preserves_absolute_root_separator() {`
  - Purpose: This test verifies that `requested_relative_path` returns an absolute path unchanged when the root parameter is relative, preserving the absolute root separator (leading slash). [crates/gcode/src/index/indexer/util.rs:197-205]
- `lexical_relative_path_preserves_cross_drive_absolute_path` (function) component `lexical_relative_path_preserves_cross_drive_absolute_path [function]` (`1f800663-4932-5759-add5-3b7173a3506c`) lines 209-214 [crates/gcode/src/index/indexer/util.rs:209-214]
  - Signature: `fn lexical_relative_path_preserves_cross_drive_absolute_path() {`
  - Purpose: This test verifies that `lexical_relative_path` returns the absolute path unchanged when the root and requested paths reside on different Windows drives, since cross-drive relative paths are impossible. [crates/gcode/src/index/indexer/util.rs:209-214]
- `lexical_relative_path_handles_unc_roots` (function) component `lexical_relative_path_handles_unc_roots [function]` (`4980e3bc-72a2-52fa-a5bd-9884d5659412`) lines 218-223 [crates/gcode/src/index/indexer/util.rs:218-223]
  - Signature: `fn lexical_relative_path_handles_unc_roots() {`
  - Purpose: Verifies that `lexical_relative_path` correctly computes the relative path suffix from a UNC root directory to a target file within the same network share. [crates/gcode/src/index/indexer/util.rs:218-223]
- `lexical_relative_path_handles_mixed_separators` (function) component `lexical_relative_path_handles_mixed_separators [function]` (`e0a54663-b2b3-53fc-acda-5f3c78028f84`) lines 227-232 [crates/gcode/src/index/indexer/util.rs:227-232]
  - Signature: `fn lexical_relative_path_handles_mixed_separators() {`
  - Purpose: This test verifies that `lexical_relative_path` correctly computes the relative path from a root directory when the requested path contains mixed forward and backward slash separators. [crates/gcode/src/index/indexer/util.rs:227-232]

