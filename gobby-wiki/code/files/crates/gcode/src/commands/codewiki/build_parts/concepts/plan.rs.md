---
title: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `curated_navigation_prompt` | function | This function constructs and returns a prompt string that requests a JSON-formatted codewiki navigation layer by appending formatted structural and summary metadata from up to 40 modules and 80 representative files. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38] |
| `parse_plan` | function | The 'parse_plan' function trims a raw string slice, strips optional triple-single-quote code block fences (with or without a 'json' specifier), and deserializes the resulting JSON string into a 'CuratedNavigationPlan' struct, returning 'Some' on success or 'None' if deserialization fails. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:40-49] |
| `fallback_plan` | function | The 'fallback_plan' function constructs a 'CuratedNavigationPlan' containing a "System Tour" 'ConceptSection' populated by mapping input modules into a structured collection of 'ConceptModule's, alongside representative file paths and an introductory narrative page. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:51-138] |
| `normalize_concepts` | function | The 'normalize_concepts' function sanitizes, slugifies, and filters a vector of concept modules, retaining only their associations to known modules and files up to a defined limit, and returns a list capped at 'MAX_CONCEPT_MODULES' of valid concepts that possess non-empty titles and at least one active association. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:140-181] |
| `normalize_sections` | function | The 'normalize_sections' function sanitizes and filters a vector of concept sections by trimming titles and summaries, retaining only valid concepts mapped from the provided modules, discarding sections with empty titles or concepts, and falling back to a default 'System Tour' section containing all concepts if the resulting collection is empty. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:183-217] |
| `normalize_narrative_pages` | function | The 'normalize_narrative_pages' function processes and filters a sequence of narrative pages by normalizing their text fields, resolving concept references against a lookup map, retaining only known module and file paths, and discarding any pages that lack a title or summary. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:219-306] |
| `concept_key_map` | function | The 'concept_key_map' function iterates over a slice of 'ConceptModule' structs to construct and return a 'BTreeMap' where both the title and the slug of each module map to its cloned slug value. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:308-315] |

