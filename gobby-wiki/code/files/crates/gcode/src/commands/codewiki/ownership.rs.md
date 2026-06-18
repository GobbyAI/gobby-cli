---
title: crates/gcode/src/commands/codewiki/ownership.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/ownership.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

This source file orchestrates code ownership analysis for a workspace. It brings together explicit configuration and git metadata to understand who owns and maintains different parts of the code.

The main driver is `build_ownership_doc` [crates/gcode/src/commands/codewiki/ownership.rs:69-114], which coordinates parsing configuration and rendering the results. The file models the underlying data using structures that track both declared static owners and dynamically derived git-blame contributors.

## How it fits

This file acts as the main entry point for the ownership portion of the codewiki command, delegating specialized operations to its internal modules: `analysis`, `codeowners`, and `render`.

During execution, `build_ownership_doc` [crates/gcode/src/commands/codewiki/ownership.rs:69-114] reads CODEOWNERS rules via `read_codeowners` to find declared owners. It resolves files to their declared lists [crates/gcode/src/commands/codewiki/ownership.rs:81] and invokes `derived_owners_for_files` to compute blame-based ownership contributors.

As calculations proceed, the code populates `OwnershipStatus` [crates/gcode/src/commands/codewiki/ownership.rs:56-61] to record integration health, such as blame availability or parsing failures. Each target file's metadata is structured under `FileOwnership` [crates/gcode/src/commands/codewiki/ownership.rs:64-67], pairing declared owner identifiers with derived `OwnershipContributor` records [crates/gcode/src/commands/codewiki/ownership.rs:47-53]. Finally, the data flow routes these structured models to the `render` submodule to compile the final document.

## Key components

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

