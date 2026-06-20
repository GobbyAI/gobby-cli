---
title: crates/gcode/src/commands/codewiki/reuse.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/reuse.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/reuse.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/reuse.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/reuse.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ReusePlan` | class | The 'ReusePlan' struct manages the optimization and reuse of previously processed documentation files by comparing current and recorded content hashes, utilizing Git-reported changes since a given reference to avoid redundant disk I/O and re-hashing. [crates/gcode/src/commands/codewiki/reuse.rs:11-29] |
| `ReusePlan::load_with_since` | method | This method reads previous codewiki metadata from the output directory to construct an aggregated map of historical file hashes, returning an instance of the struct initialized with this state, the project and output paths, the AI mode, and an optional set of files modified 'since' a given point. [crates/gcode/src/commands/codewiki/reuse.rs:39-61] |
| `ReusePlan::reusable_page` | method | The 'reusable_page' method checks if a document is reusable based on its path and source dependencies, and if so, returns the file's content from its resolved safe output directory path as an 'Option<String>'. [crates/gcode/src/commands/codewiki/reuse.rs:66-76] |
| `ReusePlan::reusable_page_keyed` | method | The 'reusable_page_keyed' method returns the cached string content of a document page if its corresponding registry entry is not degraded, matches the active AI mode, render version, and specified invalidation key, and the compiled target file successfully reads from disk. [crates/gcode/src/commands/codewiki/reuse.rs:83-101] |
| `ReusePlan::reusable_page_with_summary` | method | The 'reusable_page_with_summary' method retrieves a reusable page and its summary for a given document path and set of sources by delegating to 'reusable_page_with_summary_and_neighbors' with an empty set of neighbors. [crates/gcode/src/commands/codewiki/reuse.rs:104-110] |
| `ReusePlan::reusable_page_with_summary_and_neighbors` | method | This method retrieves a document's summary, verifies if the built page can be reused based on its source and neighbor dependencies, and, if reusable, reads and returns the existing page content alongside the summary. [crates/gcode/src/commands/codewiki/reuse.rs:116-129] |
| `ReusePlan::reusable_pages_with_prefixes` | method | This method filters document paths by the specified prefixes, rebuilds each matching document using its source hashes via 'reusable_page', and returns a sorted vector of the resulting 'BuiltDoc' structs, or 'None' if no paths match or building any document fails. [crates/gcode/src/commands/codewiki/reuse.rs:131-162] |
| `ReusePlan::reusable` | method | The 'reusable' method determines if a generated document can be reused without regeneration by verifying that its metadata is valid and matches the current configuration, its source and neighbor file sets match exactly and have unchanged hashes, and the target file exists on disk. [crates/gcode/src/commands/codewiki/reuse.rs:164-210] |
| `ReusePlan::current_hash` | method | The 'current_hash' method retrieves a file's hash from an in-memory cache, or computes it by either cloning a previously recorded hash when the file is excluded from a git-based '--since' set, or reading and hashing the file contents on disk, storing the result in the cache before returning it. [crates/gcode/src/commands/codewiki/reuse.rs:212-230] |
| `span_files` | function | This function extracts and clones the file path string from a slice of 'SourceSpan' objects and collects them into a deduplicated, ordered 'BTreeSet'. [crates/gcode/src/commands/codewiki/reuse.rs:235-237] |
| `set_matches` | function | This function returns 'true' if the set of keys in the 'recorded' map is identical in size and membership to the elements of the 'current' set. [crates/gcode/src/commands/codewiki/reuse.rs:241-243] |

_Verified by 1 in-file unit test._

