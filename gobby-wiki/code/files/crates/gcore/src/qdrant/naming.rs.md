---
title: crates/gcore/src/qdrant/naming.rs
type: code_file
provenance:
- file: crates/gcore/src/qdrant/naming.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/qdrant/naming.rs

Module: [[code/modules/crates/gcore/src/qdrant|crates/gcore/src/qdrant]]

## Overview

`crates/gcore/src/qdrant/naming.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcore/src/qdrant/naming.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CollectionScope` | type | Indexed type `CollectionScope` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:3-10] |
| `CollectionNameError` | type | Indexed type `CollectionNameError` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:13-22] |
| `collection_name` | function | Generates a validated collection name by either combining a namespace with project/topic identifiers or returning a custom name unmodified, based on the provided CollectionScope variant. [crates/gcore/src/qdrant/naming.rs:25-43] |
| `validate_collection_name_component` | function | Validates that a collection name component is non-empty, lacks surrounding whitespace, is not a reserved name ('.' or '..'), and contains no ASCII control characters, whitespace, or special path characters ('/', '\', ':'). [crates/gcore/src/qdrant/naming.rs:45-70] |

_Verified by 3 in-file unit tests._

