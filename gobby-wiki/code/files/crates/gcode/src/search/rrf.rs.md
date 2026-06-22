---
title: crates/gcode/src/search/rrf.rs
type: code_file
provenance:
- file: crates/gcode/src/search/rrf.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/rrf.rs

Module: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Overview

`crates/gcode/src/search/rrf.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/search/rrf.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `MergedResult` | type | Indexed type `MergedResult` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:7] |
| `merge` | function | Calls 'gobby_core::search::rrf_merge' on the provided '(source_name, results)' inputs, then converts each returned item into a 'MergedResult' by extracting its 'id', 'score', and 'sources'. [crates/gcode/src/search/rrf.rs:15-20] |

_Verified by 7 in-file unit tests._

