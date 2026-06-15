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

# crates/gcode/src/commands/codewiki/ownership/tests.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Purpose

This file contains tests for `build_ownership_doc` in the codewiki ownership command. The tests cover the main ownership-resolution paths: declared CODEOWNERS entries, git-blame-derived top contributors, missing-source degradation to unknown ownership, partial results when blame is capped or errors, precedence rules between declared owners and contributors, and backward-compatibility failure when cached contributor IDs are absent. The helper functions create module-path maps and temporary Git repositories with controlled commit history so each test can exercise ownership synthesis and metadata serialization in isolation.
[crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:38-62]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:65-82]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:85-106]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:109-131]

## API Symbols

- `codewiki_ownership_codeowners_only_maps_declared_owners` (function) component `codewiki_ownership_codeowners_only_maps_declared_owners [function]` (`8868388a-17b9-5429-90d1-068471c60938`) lines 8-35 [crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35]
  - Signature: `fn codewiki_ownership_codeowners_only_maps_declared_owners() {`
  - Purpose: Verifies that 'build_ownership_doc' produces a degraded code-ownership document for 'src/api/mod.rs' that includes the declared CODEOWNERS owner '@platform', the module mapping 'src/api', and a 'git_blame_unavailable' indicator. [crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35]
- `codewiki_ownership_derives_top_committers_from_git_blame` (function) component `codewiki_ownership_derives_top_committers_from_git_blame [function]` (`c4913545-2e66-5e25-b960-d9f95925f400`) lines 38-62 [crates/gcode/src/commands/codewiki/ownership/tests.rs:38-62]
  - Signature: `fn codewiki_ownership_derives_top_committers_from_git_blame() {`
  - Purpose: Verifies that 'build_ownership_doc' uses 'git blame' to derive top contributors for 'src/lib.rs', emits them in the ownership doc without exposing raw email addresses, and records exactly one file in serialized 'OwnershipMeta' with contributor IDs present. [crates/gcode/src/commands/codewiki/ownership/tests.rs:38-62]
- `codewiki_ownership_requires_cached_contributor_ids` (function) component `codewiki_ownership_requires_cached_contributor_ids [function]` (`88a1e44a-c005-5f5b-a375-dad9a8f6db0d`) lines 65-82 [crates/gcode/src/commands/codewiki/ownership/tests.rs:65-82]
  - Signature: `fn codewiki_ownership_requires_cached_contributor_ids() {`
  - Purpose: Verifies that deserializing legacy 'OwnershipMeta' without per-contributor 'contributor_id' fields fails with an error containing 'missing field 'contributor_id''. [crates/gcode/src/commands/codewiki/ownership/tests.rs:65-82]
- `codewiki_ownership_declared_owners_take_primary_precedence` (function) component `codewiki_ownership_declared_owners_take_primary_precedence [function]` (`b471fa49-9e2a-517c-9172-053bc6135ce1`) lines 85-106 [crates/gcode/src/commands/codewiki/ownership/tests.rs:85-106]
  - Signature: `fn codewiki_ownership_declared_owners_take_primary_precedence() {`
  - Purpose: Builds an ownership document for 'src/lib.rs' and verifies that a 'CODEOWNERS' declaration is reported as the declared owner, while existing contributors are listed only as top contributors and not promoted to primary owners. [crates/gcode/src/commands/codewiki/ownership/tests.rs:85-106]
- `codewiki_ownership_without_sources_degrades_to_unknown` (function) component `codewiki_ownership_without_sources_degrades_to_unknown [function]` (`13288144-4044-50dd-b2d6-2b8851b516e1`) lines 109-131 [crates/gcode/src/commands/codewiki/ownership/tests.rs:109-131]
  - Signature: `fn codewiki_ownership_without_sources_degrades_to_unknown() {`
  - Purpose: Builds an ownership document for a source file with no available Codeowners or git blame data and verifies that ownership degrades to unknown with 'degraded: true', 'codeowners_unavailable', 'git_blame_unavailable', and 'Unknown ownership' markers. [crates/gcode/src/commands/codewiki/ownership/tests.rs:109-131]
- `codewiki_ownership_file_cap_marks_partial` (function) component `codewiki_ownership_file_cap_marks_partial [function]` (`d1e9fd00-55ee-5c6b-83c7-ff285623897b`) lines 134-153 [crates/gcode/src/commands/codewiki/ownership/tests.rs:134-153]
  - Signature: `fn codewiki_ownership_file_cap_marks_partial() {`
  - Purpose: Verifies that 'build_ownership_doc' respects 'blame_file_cap' by producing a partial ownership document marked 'partial: true' with the “Ownership is partial” message and recording only one blamed file in 'OwnershipMeta'. [crates/gcode/src/commands/codewiki/ownership/tests.rs:134-153]
- `codewiki_ownership_file_cap_counts_only_cache_misses` (function) component `codewiki_ownership_file_cap_counts_only_cache_misses [function]` (`a1343272-7b2a-5c89-a49e-da510e0e8f6e`) lines 156-191 [crates/gcode/src/commands/codewiki/ownership/tests.rs:156-191]
  - Signature: `fn codewiki_ownership_file_cap_counts_only_cache_misses() {`
  - Purpose: Verifies that 'blame_file_cap' is applied only to cache misses, so a pre-cached file does not consume the cap and ownership generation for both files remains non-partial. [crates/gcode/src/commands/codewiki/ownership/tests.rs:156-191]
- `codewiki_ownership_blame_error_marks_partial_without_caching` (function) component `codewiki_ownership_blame_error_marks_partial_without_caching [function]` (`156596e0-3ae6-5225-b8cd-0f3f2e625c51`) lines 194-218 [crates/gcode/src/commands/codewiki/ownership/tests.rs:194-218]
  - Signature: `fn codewiki_ownership_blame_error_marks_partial_without_caching() {`
  - Purpose: Verifies that when ownership document generation encounters a 'git blame' error on an untracked file, it marks the result as partial, records 'git_blame_errors', and leaves 'OwnershipMeta.files' uncached. [crates/gcode/src/commands/codewiki/ownership/tests.rs:194-218]
- `modules` (function) component `modules [function]` (`5cc4dab4-5ea3-5dc4-8bc3-313129bfb514`) lines 220-225 [crates/gcode/src/commands/codewiki/ownership/tests.rs:220-225]
  - Signature: `fn modules<const N: usize>(items: [(&str, &str); N]) -> HashMap<String, String> {`
  - Purpose: Converts a fixed-size array of '(&str, &str)' pairs into a 'HashMap<String, String>' by cloning each file and module string into owned 'String' keys and values. [crates/gcode/src/commands/codewiki/ownership/tests.rs:220-225]
- `git_project_with_history` (function) component `git_project_with_history [function]` (`c83cd9cd-1a0a-5c86-ba58-a092d2295ad1`) lines 227-246 [crates/gcode/src/commands/codewiki/ownership/tests.rs:227-246]
  - Signature: `fn git_project_with_history() -> tempfile::TempDir {`
  - Purpose: Creates a temporary Git repository with 'src/lib.rs' initialized and committed twice, first by Alice with 'one' and 'two', then rewritten and staged again for a second commit by Bob with 'two_changed', and returns the tempdir. [crates/gcode/src/commands/codewiki/ownership/tests.rs:227-246]
- `git_project_with_two_files` (function) component `git_project_with_two_files [function]` (`5fd30f97-c918-55f9-963a-8a9b84690aaa`) lines 248-257 [crates/gcode/src/commands/codewiki/ownership/tests.rs:248-257]
  - Signature: `fn git_project_with_two_files() -> tempfile::TempDir {`
  - Purpose: Creates a temporary Git repository with 'src/' containing 'a.rs' and 'b.rs', stages both files, and makes an initial commit authored by Alice before returning the temp directory. [crates/gcode/src/commands/codewiki/ownership/tests.rs:248-257]
- `git_author` (function) component `git_author [function]` (`854c6843-8078-548a-bffc-b1688e8e2175`) lines 259-275 [crates/gcode/src/commands/codewiki/ownership/tests.rs:259-275]
  - Signature: `fn git_author(repo: &Path, name: &str, email: &str, message: &str) {`
  - Purpose: Runs 'git commit -m <message>' in the given repository with per-invocation 'user.name' and 'user.email' set from the provided arguments, then panics if the commit command fails. [crates/gcode/src/commands/codewiki/ownership/tests.rs:259-275]
- `git` (function) component `git [function]` (`035a98ba-934d-5f68-902a-8c66479e1121`) lines 277-285 [crates/gcode/src/commands/codewiki/ownership/tests.rs:277-285]
  - Signature: `fn git(repo: &Path, args: &[&str]) {`
  - Purpose: Runs 'git' in the specified repository by invoking 'git -C <repo> <args...>', expects the command to start successfully, and asserts that it exits with a success status. [crates/gcode/src/commands/codewiki/ownership/tests.rs:277-285]

