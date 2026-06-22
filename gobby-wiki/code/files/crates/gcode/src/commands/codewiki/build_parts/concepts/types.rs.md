---
title: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts|crates/gcode/src/commands/codewiki/build_parts/concepts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CuratedNavigationPlan` | class | The 'CuratedNavigationPlan' struct is a super-module private Rust data structure that aggregates vectors of 'ConceptModule', 'ConceptSection', and 'NarrativePage' elements, with each field configured to use its default value during deserialization if absent. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13] |
| `ConceptModule` | class | 'ConceptModule' is a crate-private Rust struct representing a concept module, containing serializable metadata (slug, title, summary, sub-modules, and files) alongside deserialization-skipped fields for post-normalization body content, content degradation tracking, and verification notes. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:16-37] |
| `ConceptSection` | class | The 'ConceptSection' struct is a module-private ('pub(super)') Rust data structure consisting of a 'title' string, a 'summary' string, and a vector of 'concepts' strings, with the latter two fields defaulting to empty values during deserialization. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:40-46] |
| `NarrativePage` | class | The 'NarrativePage' struct is a module-private Rust data structure that aggregates serialized documentation metadata—including slug, title, and relationships to concepts, modules, and files—with deserialization-skipped fields for the page's body content, body degradation state, and verification notes. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:49-69] |

