---
title: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts|crates/gcode/src/commands/codewiki/build_parts/concepts]]

## Overview
The types.rs file defines the core, deserializable data structures used to build and model the conceptual navigation and content framework for a code wiki. It serves as the primary schema definition file for parsing raw, structural metadata and managing the subsequent state of narrative components and concept layouts.

The top-level container, `CuratedNavigationPlan` [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:4-11], aggregates multiple curated collections of content. These collections include structured modules, sections, and individual pages, allowing the system to represent the broader navigational map of the code wiki.

Within this plan, `ConceptSection` [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:36-42] organizes concepts into logical groups with summaries and associated lists. The actual documentation pages are represented by `ConceptModule` [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:14-33] and `NarrativePage` [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:45-63]. Both track target files, related code modules, and summary information.

During the initial structure-pass parsing, structures like `ConceptModule` [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:14-33] and `NarrativePage` [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:45-63] use Serde attributes to skip fields like `body` and `body_degraded`. This design prevents external configuration from perturbing or overriding the actual content generation phase.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CuratedNavigationPlan` | class | 'CuratedNavigationPlan' is a serde-deserializable, module-private aggregate struct that groups three ordered collections of curated navigation content: concept modules, concept sections, and narrative pages. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:4-11] |
| `ConceptModule` | class | 'ConceptModule' is a serde-backed internal data model for a concept page that stores a required 'title', optional 'slug', 'summary', 'modules', and 'files', plus skipped post-normalization state for the multi-section 'body' and a 'body_degraded' flag indicating fallback content generation. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:14-33] |
| `ConceptSection` | class | 'ConceptSection' is a serde-deserializable struct with a 'title' plus defaulted 'summary' and 'concepts' fields, where 'summary' is a 'String' and 'concepts' is a 'Vec<String>'. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:36-42] |
| `NarrativePage` | class | 'NarrativePage' is a serialized page metadata struct holding a slug, title, summary, concept/module/file lists, and a skipped optional chapter body with a degraded-content flag. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:45-63] |

