---
title: crates/gcode/src/commands/codewiki/ownership/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
  ranges:
  - 8-35
  - 38-62
  - 65-82
  - 85-106
  - 109-131
  - 134-153
  - 156-191
  - 194-218
  - 220-225
  - 227-246
  - 248-257
  - 259-275
  - 277-285
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35](crates/gcode/src/commands/codewiki/ownership/tests.rs#L8-L35), [crates/gcode/src/commands/codewiki/ownership/tests.rs:38-62](crates/gcode/src/commands/codewiki/ownership/tests.rs#L38-L62), [crates/gcode/src/commands/codewiki/ownership/tests.rs:65-82](crates/gcode/src/commands/codewiki/ownership/tests.rs#L65-L82), [crates/gcode/src/commands/codewiki/ownership/tests.rs:85-106](crates/gcode/src/commands/codewiki/ownership/tests.rs#L85-L106), [crates/gcode/src/commands/codewiki/ownership/tests.rs:109-131](crates/gcode/src/commands/codewiki/ownership/tests.rs#L109-L131), [crates/gcode/src/commands/codewiki/ownership/tests.rs:134-153](crates/gcode/src/commands/codewiki/ownership/tests.rs#L134-L153), [crates/gcode/src/commands/codewiki/ownership/tests.rs:156-191](crates/gcode/src/commands/codewiki/ownership/tests.rs#L156-L191), [crates/gcode/src/commands/codewiki/ownership/tests.rs:194-218](crates/gcode/src/commands/codewiki/ownership/tests.rs#L194-L218), [crates/gcode/src/commands/codewiki/ownership/tests.rs:220-225](crates/gcode/src/commands/codewiki/ownership/tests.rs#L220-L225), [crates/gcode/src/commands/codewiki/ownership/tests.rs:227-246](crates/gcode/src/commands/codewiki/ownership/tests.rs#L227-L246), [crates/gcode/src/commands/codewiki/ownership/tests.rs:248-257](crates/gcode/src/commands/codewiki/ownership/tests.rs#L248-L257), [crates/gcode/src/commands/codewiki/ownership/tests.rs:259-275](crates/gcode/src/commands/codewiki/ownership/tests.rs#L259-L275), [crates/gcode/src/commands/codewiki/ownership/tests.rs:277-285](crates/gcode/src/commands/codewiki/ownership/tests.rs#L277-L285)

</details>

# crates/gcode/src/commands/codewiki/ownership/tests.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Purpose

This file contains unit tests for the codewiki ownership document builder. The tests cover the main ownership sources and fallback behavior: mapping declared owners from CODEOWNERS, deriving top contributors from `git blame`, requiring cached contributor IDs in serialized metadata, preferring declared owners over blame-derived committers, degrading to unknown when no ownership sources are available, and marking partial results when blame is capped or fails. The helper functions at the bottom set up temporary git projects, authors, and module mappings so each test can exercise `build_ownership_doc` against controlled repository histories and verify the resulting document and metadata.
[crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:38-62]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:65-82]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:85-106]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:109-131]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `codewiki_ownership_codeowners_only_maps_declared_owners` | function | `fn codewiki_ownership_codeowners_only_maps_declared_owners() {` | `codewiki_ownership_codeowners_only_maps_declared_owners [function]` | `8868388a-17b9-5429-90d1-068471c60938` | 8-35 [crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35] | Indexed function `codewiki_ownership_codeowners_only_maps_declared_owners` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35] |
| `codewiki_ownership_derives_top_committers_from_git_blame` | function | `fn codewiki_ownership_derives_top_committers_from_git_blame() {` | `codewiki_ownership_derives_top_committers_from_git_blame [function]` | `c4913545-2e66-5e25-b960-d9f95925f400` | 38-62 [crates/gcode/src/commands/codewiki/ownership/tests.rs:38-62] | Indexed function `codewiki_ownership_derives_top_committers_from_git_blame` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:38-62] |
| `codewiki_ownership_requires_cached_contributor_ids` | function | `fn codewiki_ownership_requires_cached_contributor_ids() {` | `codewiki_ownership_requires_cached_contributor_ids [function]` | `88a1e44a-c005-5f5b-a375-dad9a8f6db0d` | 65-82 [crates/gcode/src/commands/codewiki/ownership/tests.rs:65-82] | Indexed function `codewiki_ownership_requires_cached_contributor_ids` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:65-82] |
| `codewiki_ownership_declared_owners_take_primary_precedence` | function | `fn codewiki_ownership_declared_owners_take_primary_precedence() {` | `codewiki_ownership_declared_owners_take_primary_precedence [function]` | `b471fa49-9e2a-517c-9172-053bc6135ce1` | 85-106 [crates/gcode/src/commands/codewiki/ownership/tests.rs:85-106] | Indexed function `codewiki_ownership_declared_owners_take_primary_precedence` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:85-106] |
| `codewiki_ownership_without_sources_degrades_to_unknown` | function | `fn codewiki_ownership_without_sources_degrades_to_unknown() {` | `codewiki_ownership_without_sources_degrades_to_unknown [function]` | `13288144-4044-50dd-b2d6-2b8851b516e1` | 109-131 [crates/gcode/src/commands/codewiki/ownership/tests.rs:109-131] | Indexed function `codewiki_ownership_without_sources_degrades_to_unknown` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:109-131] |
| `codewiki_ownership_file_cap_marks_partial` | function | `fn codewiki_ownership_file_cap_marks_partial() {` | `codewiki_ownership_file_cap_marks_partial [function]` | `d1e9fd00-55ee-5c6b-83c7-ff285623897b` | 134-153 [crates/gcode/src/commands/codewiki/ownership/tests.rs:134-153] | Indexed function `codewiki_ownership_file_cap_marks_partial` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:134-153] |
| `codewiki_ownership_file_cap_counts_only_cache_misses` | function | `fn codewiki_ownership_file_cap_counts_only_cache_misses() {` | `codewiki_ownership_file_cap_counts_only_cache_misses [function]` | `a1343272-7b2a-5c89-a49e-da510e0e8f6e` | 156-191 [crates/gcode/src/commands/codewiki/ownership/tests.rs:156-191] | Indexed function `codewiki_ownership_file_cap_counts_only_cache_misses` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:156-191] |
| `codewiki_ownership_blame_error_marks_partial_without_caching` | function | `fn codewiki_ownership_blame_error_marks_partial_without_caching() {` | `codewiki_ownership_blame_error_marks_partial_without_caching [function]` | `156596e0-3ae6-5225-b8cd-0f3f2e625c51` | 194-218 [crates/gcode/src/commands/codewiki/ownership/tests.rs:194-218] | Indexed function `codewiki_ownership_blame_error_marks_partial_without_caching` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:194-218] |
| `modules` | function | `fn modules<const N: usize>(items: [(&str, &str); N]) -> HashMap<String, String> {` | `modules [function]` | `5cc4dab4-5ea3-5dc4-8bc3-313129bfb514` | 220-225 [crates/gcode/src/commands/codewiki/ownership/tests.rs:220-225] | Indexed function `modules` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:220-225] |
| `git_project_with_history` | function | `fn git_project_with_history() -> tempfile::TempDir {` | `git_project_with_history [function]` | `c83cd9cd-1a0a-5c86-ba58-a092d2295ad1` | 227-246 [crates/gcode/src/commands/codewiki/ownership/tests.rs:227-246] | Indexed function `git_project_with_history` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:227-246] |
| `git_project_with_two_files` | function | `fn git_project_with_two_files() -> tempfile::TempDir {` | `git_project_with_two_files [function]` | `5fd30f97-c918-55f9-963a-8a9b84690aaa` | 248-257 [crates/gcode/src/commands/codewiki/ownership/tests.rs:248-257] | Indexed function `git_project_with_two_files` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:248-257] |
| `git_author` | function | `fn git_author(repo: &Path, name: &str, email: &str, message: &str) {` | `git_author [function]` | `854c6843-8078-548a-bffc-b1688e8e2175` | 259-275 [crates/gcode/src/commands/codewiki/ownership/tests.rs:259-275] | Indexed function `git_author` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:259-275] |
| `git` | function | `fn git(repo: &Path, args: &[&str]) {` | `git [function]` | `035a98ba-934d-5f68-902a-8c66479e1121` | 277-285 [crates/gcode/src/commands/codewiki/ownership/tests.rs:277-285] | Indexed function `git` in `crates/gcode/src/commands/codewiki/ownership/tests.rs`. [crates/gcode/src/commands/codewiki/ownership/tests.rs:277-285] |
