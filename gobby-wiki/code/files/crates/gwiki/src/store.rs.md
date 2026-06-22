---
title: crates/gwiki/src/store.rs
type: code_file
provenance:
- file: crates/gwiki/src/store.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/store.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/store.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `configured_memory_index_limit_bytes` | function | Returns the configured memory index limit in bytes by delegating to 'helpers::configured_memory_index_limit_bytes()', or 'None' if no limit is configured. [crates/gwiki/src/store.rs:15-17] |
| `link_kind` | function | 'link_kind' delegates to 'helpers::link_kind(target)' and returns the resulting static string describing the kind of link for the given target. [crates/gwiki/src/store.rs:19-21] |

_Verified by 5 in-file unit tests._

