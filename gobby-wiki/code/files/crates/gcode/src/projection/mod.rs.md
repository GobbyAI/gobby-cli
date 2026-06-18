---
title: crates/gcode/src/projection/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/projection/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/projection/mod.rs

Module: [[code/modules/crates/gcode/src/projection|crates/gcode/src/projection]]

## Overview

`crates/gcode/src/projection/mod.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gcode/src/projection/mod.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ProjectionReconcileFailure` | class | 'ProjectionReconcileFailure' is a struct that represents a failed projection reconciliation attempt by pairing a 'sync::ProjectionTarget' with an error 'message' describing the failure. [crates/gcode/src/projection/mod.rs:8-11] |
| `reconcile_deleted_file` | function | Attempts to remove the deleted file’s graph projection from FalkorDB and its symbol vectors from Qdrant, returning a 'Vec<ProjectionReconcileFailure>' describing any per-backend deletion errors. [crates/gcode/src/projection/mod.rs:13-35] |

