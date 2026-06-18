---
title: crates/gcode/src/commands/codewiki/ownership/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/ownership/tests.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Overview

`crates/gcode/src/commands/codewiki/ownership/tests.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/ownership/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `codewiki_ownership_codeowners_only_maps_declared_owners` | function | Verifies that 'build_ownership_doc' for 'src/api/mod.rs' produces a degraded 'code_ownership' document marked 'git_blame_unavailable' that includes the 'src/api' module, the declared CODEOWNERS entry '@platform', and the source path. [crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35] |
| `codewiki_ownership_derives_top_committers_from_git_blame` | function | Verifies that ownership documentation built from 'git blame' on 'src/lib.rs' lists the top contributors, excludes raw blame-unavailable markers and email addresses from serialized metadata, and records exactly one file in 'OwnershipMeta'. [crates/gcode/src/commands/codewiki/ownership/tests.rs:38-62] |
| `codewiki_ownership_requires_cached_contributor_ids` | function | Verifies that deserializing legacy ownership metadata without 'contributor_id' fields fails with an error containing 'missing field 'contributor_id''. [crates/gcode/src/commands/codewiki/ownership/tests.rs:65-82] |
| `codewiki_ownership_declared_owners_take_primary_precedence` | function | Verifies that when a 'CODEOWNERS' entry declares an owner for 'src/lib.rs', the generated ownership doc reports the declared owner and suppresses the file’s top contributor from being labeled as a primary owner. [crates/gcode/src/commands/codewiki/ownership/tests.rs:85-106] |
| `codewiki_ownership_without_sources_degrades_to_unknown` | function | Builds an ownership document for a source file and, when codeowners and git-blame data are unavailable, marks it 'degraded: true' with 'codeowners_unavailable', 'git_blame_unavailable', and 'Unknown ownership'. [crates/gcode/src/commands/codewiki/ownership/tests.rs:109-131] |
| `codewiki_ownership_file_cap_marks_partial` | function | Builds an ownership document for a two-file project with 'blame_file_cap = 1' and verifies that the result is marked partial ('partial: true', “Ownership is partial”) and that only one file is recorded in 'meta.files'. [crates/gcode/src/commands/codewiki/ownership/tests.rs:134-153] |
| `codewiki_ownership_file_cap_counts_only_cache_misses` | function | Verifies that 'blame_file_cap' is enforced only for uncached ownership lookups by confirming a cached file remains in 'meta', a second file is added, and the generated document is not marked partial. [crates/gcode/src/commands/codewiki/ownership/tests.rs:156-191] |
| `codewiki_ownership_blame_error_marks_partial_without_caching` | function | Builds ownership docs for an untracked source file with blame enabled, and verifies that a blame failure marks the document partial, records 'git_blame_errors', and does not cache any file metadata. [crates/gcode/src/commands/codewiki/ownership/tests.rs:194-218] |
| `modules` | function | Converts a fixed-size array of '(&str, &str)' pairs into a 'HashMap<String, String>' by allocating owned 'String' keys and values for each entry and collecting them. [crates/gcode/src/commands/codewiki/ownership/tests.rs:220-225] |
| `git_project_with_history` | function | Creates a temporary Git repository containing 'src/lib.rs' with two committed revisions by different authors: an initial commit from Alice defining 'one' and 'two', followed by a second commit from Bob changing 'two' to 'two_changed'. [crates/gcode/src/commands/codewiki/ownership/tests.rs:227-246] |
| `git_project_with_two_files` | function | Creates a temporary Git repository with a 'src' directory containing two Rust source files ('src/a.rs' and 'src/b.rs'), stages them, records an initial author identity, and returns the temp directory handle. [crates/gcode/src/commands/codewiki/ownership/tests.rs:248-257] |
| `git_author` | function | Runs 'git commit -m <message>' in the specified repository with temporary 'user.name' and 'user.email' config overrides, then asserts that the commit succeeds. [crates/gcode/src/commands/codewiki/ownership/tests.rs:259-275] |
| `git` | function | Runs 'git -C <repo> <args...>' as a child process, panics if the command cannot be started, and asserts that it exits successfully. [crates/gcode/src/commands/codewiki/ownership/tests.rs:277-285] |

