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

`crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CuratedNavigationPlan` | class | 'CuratedNavigationPlan' is a serde-deserializable, module-private aggregate struct that groups three ordered collections of curated navigation content: concept modules, concept sections, and narrative pages. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:4-11] |
| `ConceptModule` | class | 'ConceptModule' is a serde-backed internal data model for a concept page that stores a required 'title', optional 'slug', 'summary', 'modules', and 'files', plus skipped post-normalization state for the multi-section 'body' and a 'body_degraded' flag indicating fallback content generation. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:14-33] |
| `ConceptSection` | class | 'ConceptSection' is a serde-deserializable struct with a 'title' plus defaulted 'summary' and 'concepts' fields, where 'summary' is a 'String' and 'concepts' is a 'Vec<String>'. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:36-42] |
| `NarrativePage` | class | 'NarrativePage' is a serialized page metadata struct holding a slug, title, summary, concept/module/file lists, and a skipped optional chapter body with a degraded-content flag. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:45-63] |

