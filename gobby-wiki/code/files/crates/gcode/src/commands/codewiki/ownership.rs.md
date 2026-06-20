---
title: crates/gcode/src/commands/codewiki/ownership.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/ownership.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/ownership.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/ownership.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `OwnershipOptions` | class | 'OwnershipOptions' is a crate-private configuration struct that controls blame analysis limits via a maximum file-capacity ('blame_file_cap: usize') and a timeout ('blame_timeout: Duration'). [crates/gcode/src/commands/codewiki/ownership.rs:20-23] |
| `OwnershipOptions::default` | method | Returns a 'Self' instance initialized with 'blame_file_cap' set to '200' and 'blame_timeout' set to 'Duration::from_secs(20)'. [crates/gcode/src/commands/codewiki/ownership.rs:26-31] |
| `OwnershipMeta` | class | 'OwnershipMeta' is a crate-private Serde-deserializable metadata struct that stores a 'BTreeMap<String, CachedBlameSummary>' keyed by file path, defaulting to an empty map when omitted. [crates/gcode/src/commands/codewiki/ownership.rs:35-38] |
| `CachedBlameSummary` | class | 'CachedBlameSummary' is an internal cache record that stores a content hash and the corresponding list of 'OwnershipContributor' entries used to summarize blame ownership for that content. [crates/gcode/src/commands/codewiki/ownership.rs:41-44] |
| `OwnershipContributor` | class | 'OwnershipContributor' is a crate-visible serializable/deserializable data struct that records a contributor’s identifier, display name, optional email (ignored on serialization), and owned line count. [crates/gcode/src/commands/codewiki/ownership.rs:47-53] |
| `OwnershipStatus` | class | 'OwnershipStatus' is a status struct that reports whether CODEOWNERS data and blame data are available, whether blame retrieval encountered errors, and whether the ownership information is partial. [crates/gcode/src/commands/codewiki/ownership.rs:56-61] |
| `FileOwnership` | class | 'FileOwnership' is a struct that models file ownership metadata as explicitly declared owner identifiers ('declared') plus an inferred set of ownership contributors ('derived'). [crates/gcode/src/commands/codewiki/ownership.rs:64-67] |
| `build_ownership_doc` | function | Builds a Markdown ownership document for the given files by loading 'CODEOWNERS', deriving per-file declared and blame-based owners, tracking partial/degraded status, and then rendering either an unknown-ownership notice or module/file ownership sections. [crates/gcode/src/commands/codewiki/ownership.rs:69-114] |

