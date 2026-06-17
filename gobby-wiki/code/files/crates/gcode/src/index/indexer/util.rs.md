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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/util.rs:28-66](crates/gcode/src/index/indexer/util.rs#L28-L66), [crates/gcode/src/index/indexer/util.rs:70-93](crates/gcode/src/index/indexer/util.rs#L70-L93), [crates/gcode/src/index/indexer/util.rs:95-101](crates/gcode/src/index/indexer/util.rs#L95-L101), [crates/gcode/src/index/indexer/util.rs:103-111](crates/gcode/src/index/indexer/util.rs#L103-L111), [crates/gcode/src/index/indexer/util.rs:113-142](crates/gcode/src/index/indexer/util.rs#L113-L142), [crates/gcode/src/index/indexer/util.rs:144-154](crates/gcode/src/index/indexer/util.rs#L144-L154), [crates/gcode/src/index/indexer/util.rs:156-160](crates/gcode/src/index/indexer/util.rs#L156-L160), [crates/gcode/src/index/indexer/util.rs:162-169](crates/gcode/src/index/indexer/util.rs#L162-L169), [crates/gcode/src/index/indexer/util.rs:176-186](crates/gcode/src/index/indexer/util.rs#L176-L186), [crates/gcode/src/index/indexer/util.rs:189-194](crates/gcode/src/index/indexer/util.rs#L189-L194), [crates/gcode/src/index/indexer/util.rs:197-205](crates/gcode/src/index/indexer/util.rs#L197-L205), [crates/gcode/src/index/indexer/util.rs:209-214](crates/gcode/src/index/indexer/util.rs#L209-L214), [crates/gcode/src/index/indexer/util.rs:218-223](crates/gcode/src/index/indexer/util.rs#L218-L223), [crates/gcode/src/index/indexer/util.rs:227-232](crates/gcode/src/index/indexer/util.rs#L227-L232)

</details>

# crates/gcode/src/index/indexer/util.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file provides utility helpers for the GCode indexer’s path and file-type handling. `DEFAULT_EXCLUDES` defines the standard directory patterns the indexer skips, `filter_discovered_paths` keeps discovered paths that fall under a requested filter using lexical matching first and canonicalization as a fallback, and the `unsupported_file_types`/`unsupported_file_type_label` helpers group unsupported inputs by extension while collecting a few example files per type. The path helpers (`requested_relative_path`, `lexical_relative_path`, `normalized_components`, `relative_path`) turn absolute or relative paths into stable, human-readable relative forms across platforms, including UNC roots, mixed separators, and cross-drive cases, and `epoch_secs_str` formats timestamps as epoch seconds. The accompanying tests exercise the tricky path-filtering and relative-path edge cases to ensure the helpers behave consistently.
[crates/gcode/src/index/indexer/util.rs:28-66]
[crates/gcode/src/index/indexer/util.rs:70-93]
[crates/gcode/src/index/indexer/util.rs:95-101]
[crates/gcode/src/index/indexer/util.rs:103-111]
[crates/gcode/src/index/indexer/util.rs:113-142]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `filter_discovered_paths` | function | `pub(super) fn filter_discovered_paths(` | `filter_discovered_paths [function]` | `5c2ff8bb-3bed-50a9-ad92-ab66a0a34c28` | 28-66 [crates/gcode/src/index/indexer/util.rs:28-66] | Indexed function `filter_discovered_paths` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:28-66] |
| `unsupported_file_types` | function | `pub(super) fn unsupported_file_types(` | `unsupported_file_types [function]` | `f3a89c34-7edf-5690-ba9c-92c07901cf9e` | 70-93 [crates/gcode/src/index/indexer/util.rs:70-93] | Indexed function `unsupported_file_types` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:70-93] |
| `unsupported_file_type_label` | function | `fn unsupported_file_type_label(path: &Path) -> String {` | `unsupported_file_type_label [function]` | `21ee0949-01a8-5b35-b124-7a3e12a280d1` | 95-101 [crates/gcode/src/index/indexer/util.rs:95-101] | Indexed function `unsupported_file_type_label` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:95-101] |
| `requested_relative_path` | function | `pub(super) fn requested_relative_path(root_path: &Path, requested_path: &Path) -> String {` | `requested_relative_path [function]` | `2c3d5dde-70fb-517d-9a30-a57fc029d55a` | 103-111 [crates/gcode/src/index/indexer/util.rs:103-111] | Indexed function `requested_relative_path` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:103-111] |
| `lexical_relative_path` | function | `fn lexical_relative_path(root_path: &Path, requested_path: &Path) -> String {` | `lexical_relative_path [function]` | `1f671963-1e36-5bcb-8b36-35136e72d054` | 113-142 [crates/gcode/src/index/indexer/util.rs:113-142] | Indexed function `lexical_relative_path` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:113-142] |
| `normalized_components` | function | `fn normalized_components(path: &Path) -> Vec<OsString> {` | `normalized_components [function]` | `7c9b4b5f-c2f2-5a8a-a844-5837e9288643` | 144-154 [crates/gcode/src/index/indexer/util.rs:144-154] | Indexed function `normalized_components` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:144-154] |
| `relative_path` | function | `pub(super) fn relative_path(path: &Path, root: &Path) -> anyhow::Result<String> {` | `relative_path [function]` | `134005ee-5574-5385-9b33-18f72d9de8bb` | 156-160 [crates/gcode/src/index/indexer/util.rs:156-160] | Indexed function `relative_path` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:156-160] |
| `epoch_secs_str` | function | `pub(super) fn epoch_secs_str() -> String {` | `epoch_secs_str [function]` | `80ceb895-29f8-566e-b983-c292429f5278` | 162-169 [crates/gcode/src/index/indexer/util.rs:162-169] | Indexed function `epoch_secs_str` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:162-169] |
| `filter_discovered_paths_uses_lexical_match_before_canonicalizing` | function | `fn filter_discovered_paths_uses_lexical_match_before_canonicalizing() {` | `filter_discovered_paths_uses_lexical_match_before_canonicalizing [function]` | `745d791b-9ff5-5a66-acc5-84f77ba6796d` | 176-186 [crates/gcode/src/index/indexer/util.rs:176-186] | Indexed function `filter_discovered_paths_uses_lexical_match_before_canonicalizing` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:176-186] |
| `requested_relative_path_uses_relative_diff_for_absolute_paths_outside_root` | function | `fn requested_relative_path_uses_relative_diff_for_absolute_paths_outside_root() {` | `requested_relative_path_uses_relative_diff_for_absolute_paths_outside_root [function]` | `11da72a1-c6bc-5d09-b79c-f9ba71a8ad1b` | 189-194 [crates/gcode/src/index/indexer/util.rs:189-194] | Indexed function `requested_relative_path_uses_relative_diff_for_absolute_paths_outside_root` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:189-194] |
| `requested_relative_path_preserves_absolute_root_separator` | function | `fn requested_relative_path_preserves_absolute_root_separator() {` | `requested_relative_path_preserves_absolute_root_separator [function]` | `56916c1b-faee-5acd-9f09-68af8ccb74cb` | 197-205 [crates/gcode/src/index/indexer/util.rs:197-205] | Indexed function `requested_relative_path_preserves_absolute_root_separator` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:197-205] |
| `lexical_relative_path_preserves_cross_drive_absolute_path` | function | `fn lexical_relative_path_preserves_cross_drive_absolute_path() {` | `lexical_relative_path_preserves_cross_drive_absolute_path [function]` | `1f800663-4932-5759-add5-3b7173a3506c` | 209-214 [crates/gcode/src/index/indexer/util.rs:209-214] | Indexed function `lexical_relative_path_preserves_cross_drive_absolute_path` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:209-214] |
| `lexical_relative_path_handles_unc_roots` | function | `fn lexical_relative_path_handles_unc_roots() {` | `lexical_relative_path_handles_unc_roots [function]` | `4980e3bc-72a2-52fa-a5bd-9884d5659412` | 218-223 [crates/gcode/src/index/indexer/util.rs:218-223] | Indexed function `lexical_relative_path_handles_unc_roots` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:218-223] |
| `lexical_relative_path_handles_mixed_separators` | function | `fn lexical_relative_path_handles_mixed_separators() {` | `lexical_relative_path_handles_mixed_separators [function]` | `e0a54663-b2b3-53fc-acda-5f3c78028f84` | 227-232 [crates/gcode/src/index/indexer/util.rs:227-232] | Indexed function `lexical_relative_path_handles_mixed_separators` in `crates/gcode/src/index/indexer/util.rs`. [crates/gcode/src/index/indexer/util.rs:227-232] |
