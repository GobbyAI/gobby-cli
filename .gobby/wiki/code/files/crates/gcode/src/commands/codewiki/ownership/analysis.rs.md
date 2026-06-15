---
title: crates/gcode/src/commands/codewiki/ownership/analysis.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/analysis.rs
  ranges:
  - 17-21
  - 23-87
  - 89-91
  - 93-104
  - 106-110
  - 112-133
  - 135-165
  - 167-172
  - 174-227
  - 229-236
  - 238-247
  - 249-263
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/ownership/analysis.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Purpose

This file computes derived file owners from `git blame`, with caching and timeout safeguards. `derived_owners_for_files` discovers the repo head, then walks the requested files, reuses cached contributor summaries when the file content hash matches, and otherwise blames the file until a global timeout or file-cap is reached, updating `OwnershipMeta` and `OwnershipStatus` as it goes. The blame path is split into helpers that hash file contents, run blame with a per-file timeout, read the temporary blame output, parse porcelain blame into `OwnershipContributor` values, and normalize contributor identity from email so results stay deterministic across runs.
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110]

## API Symbols

- `BlameContributorsOutcome` (type) component `BlameContributorsOutcome [type]` (`ebcedf2b-be5c-5460-9f9e-6deb2a944e6e`) lines 17-21 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]
  - Signature: `enum BlameContributorsOutcome {`
  - Purpose: Indexed type `BlameContributorsOutcome` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]
- `derived_owners_for_files` (function) component `derived_owners_for_files [function]` (`4f1a211e-0fdf-5619-8fa5-0828eedaea66`) lines 23-87 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87]
  - Signature: `pub(super) fn derived_owners_for_files(`
  - Purpose: Indexed function `derived_owners_for_files` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87]
- `content_hash` (function) component `content_hash [function]` (`05167b87-03e8-56c8-9df6-6630e14dd0e5`) lines 89-91 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91]
  - Signature: `pub(super) fn content_hash(project_root: &Path, file: &str) -> Option<String> {`
  - Purpose: Indexed function `content_hash` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91]
- `blame_file_contributors_with_timeout` (function) component `blame_file_contributors_with_timeout [function]` (`438ec0f8-35e0-5581-9b0d-07597214d73c`) lines 93-104 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104]
  - Signature: `fn blame_file_contributors_with_timeout(`
  - Purpose: Indexed function `blame_file_contributors_with_timeout` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104]
- `GitBlameOutput` (class) component `GitBlameOutput [class]` (`ccc1801c-f787-535b-8a50-78c8f15358fc`) lines 106-110 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110]
  - Signature: `pub(super) struct GitBlameOutput {`
  - Purpose: Indexed class `GitBlameOutput` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110]
- `blame_file_contributors` (function) component `blame_file_contributors [function]` (`3f911ae1-3be8-5693-b98e-67f901338e31`) lines 112-133 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:112-133]
  - Signature: `fn blame_file_contributors(`
  - Purpose: Indexed function `blame_file_contributors` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:112-133]
- `git_blame_output_with_timeout` (function) component `git_blame_output_with_timeout [function]` (`e132c505-a271-50b2-8fa1-c5012afe083a`) lines 135-165 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:135-165]
  - Signature: `pub(super) fn git_blame_output_with_timeout(`
  - Purpose: Indexed function `git_blame_output_with_timeout` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:135-165]
- `read_tempfile` (function) component `read_tempfile [function]` (`5d61c431-4141-514a-8403-9f527775051b`) lines 167-172 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:167-172]
  - Signature: `fn read_tempfile(file: &mut std::fs::File) -> anyhow::Result<String> {`
  - Purpose: Indexed function `read_tempfile` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:167-172]
- `parse_git_blame_porcelain` (function) component `parse_git_blame_porcelain [function]` (`d437db11-049e-5584-ab00-ffc688206ea2`) lines 174-227 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:174-227]
  - Signature: `fn parse_git_blame_porcelain(raw: &str) -> Vec<OwnershipContributor> {`
  - Purpose: Indexed function `parse_git_blame_porcelain` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:174-227]
- `git_blame_email` (function) component `git_blame_email [function]` (`968c84b7-4e63-5b58-ba01-876a47f68af0`) lines 229-236 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:229-236]
  - Signature: `fn git_blame_email(value: &str) -> Option<String> {`
  - Purpose: Indexed function `git_blame_email` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:229-236]
- `contributor_id` (function) component `contributor_id [function]` (`34c46854-9d66-5474-a49c-b860b0fedfea`) lines 238-247 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:238-247]
  - Signature: `fn contributor_id(name: &str, email: Option<&str>) -> String {`
  - Purpose: Indexed function `contributor_id` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:238-247]
- `retain_deterministic_identity` (function) component `retain_deterministic_identity [function]` (`572e1000-3966-50e1-9430-3836a2a00d1e`) lines 249-263 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:249-263]
  - Signature: `pub(super) fn retain_deterministic_identity(`
  - Purpose: Indexed function `retain_deterministic_identity` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:249-263]

