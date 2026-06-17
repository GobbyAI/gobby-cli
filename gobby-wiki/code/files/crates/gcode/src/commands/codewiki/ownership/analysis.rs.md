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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L17-L21), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L23-L87), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L89-L91), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L93-L104), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L106-L110), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:112-133](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L112-L133), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:135-165](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L135-L165), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:167-172](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L167-L172), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:174-227](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L174-L227), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:229-236](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L229-L236), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:238-247](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L238-L247), [crates/gcode/src/commands/codewiki/ownership/analysis.rs:249-263](crates/gcode/src/commands/codewiki/ownership/analysis.rs#L249-L263)

</details>

# crates/gcode/src/commands/codewiki/ownership/analysis.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Purpose

Computes derived file ownership by combining cached blame results with fresh `git blame` lookups from the repository head, subject to per-run timeout and file-cap limits. It hashes file contents to reuse existing contributor summaries when the file is unchanged, otherwise it runs blame with a timeout, parses porcelain output into `OwnershipContributor` records, and normalizes contributor identity data so the ownership cache stays stable and deterministic.
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `BlameContributorsOutcome` | type | `enum BlameContributorsOutcome {` | `BlameContributorsOutcome [type]` | `ebcedf2b-be5c-5460-9f9e-6deb2a944e6e` | 17-21 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21] | Indexed type `BlameContributorsOutcome` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21] |
| `derived_owners_for_files` | function | `pub(super) fn derived_owners_for_files(` | `derived_owners_for_files [function]` | `4f1a211e-0fdf-5619-8fa5-0828eedaea66` | 23-87 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87] | Indexed function `derived_owners_for_files` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87] |
| `content_hash` | function | `pub(super) fn content_hash(project_root: &Path, file: &str) -> Option<String> {` | `content_hash [function]` | `05167b87-03e8-56c8-9df6-6630e14dd0e5` | 89-91 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91] | Indexed function `content_hash` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:89-91] |
| `blame_file_contributors_with_timeout` | function | `fn blame_file_contributors_with_timeout(` | `blame_file_contributors_with_timeout [function]` | `438ec0f8-35e0-5581-9b0d-07597214d73c` | 93-104 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104] | Indexed function `blame_file_contributors_with_timeout` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:93-104] |
| `GitBlameOutput` | class | `pub(super) struct GitBlameOutput {` | `GitBlameOutput [class]` | `ccc1801c-f787-535b-8a50-78c8f15358fc` | 106-110 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110] | Indexed class `GitBlameOutput` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:106-110] |
| `blame_file_contributors` | function | `fn blame_file_contributors(` | `blame_file_contributors [function]` | `3f911ae1-3be8-5693-b98e-67f901338e31` | 112-133 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:112-133] | Indexed function `blame_file_contributors` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:112-133] |
| `git_blame_output_with_timeout` | function | `pub(super) fn git_blame_output_with_timeout(` | `git_blame_output_with_timeout [function]` | `e132c505-a271-50b2-8fa1-c5012afe083a` | 135-165 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:135-165] | Indexed function `git_blame_output_with_timeout` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:135-165] |
| `read_tempfile` | function | `fn read_tempfile(file: &mut std::fs::File) -> anyhow::Result<String> {` | `read_tempfile [function]` | `5d61c431-4141-514a-8403-9f527775051b` | 167-172 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:167-172] | Indexed function `read_tempfile` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:167-172] |
| `parse_git_blame_porcelain` | function | `fn parse_git_blame_porcelain(raw: &str) -> Vec<OwnershipContributor> {` | `parse_git_blame_porcelain [function]` | `d437db11-049e-5584-ab00-ffc688206ea2` | 174-227 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:174-227] | Indexed function `parse_git_blame_porcelain` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:174-227] |
| `git_blame_email` | function | `fn git_blame_email(value: &str) -> Option<String> {` | `git_blame_email [function]` | `968c84b7-4e63-5b58-ba01-876a47f68af0` | 229-236 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:229-236] | Indexed function `git_blame_email` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:229-236] |
| `contributor_id` | function | `fn contributor_id(name: &str, email: Option<&str>) -> String {` | `contributor_id [function]` | `34c46854-9d66-5474-a49c-b860b0fedfea` | 238-247 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:238-247] | Indexed function `contributor_id` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:238-247] |
| `retain_deterministic_identity` | function | `pub(super) fn retain_deterministic_identity(` | `retain_deterministic_identity [function]` | `572e1000-3966-50e1-9430-3836a2a00d1e` | 249-263 [crates/gcode/src/commands/codewiki/ownership/analysis.rs:249-263] | Indexed function `retain_deterministic_identity` in `crates/gcode/src/commands/codewiki/ownership/analysis.rs`. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:249-263] |
