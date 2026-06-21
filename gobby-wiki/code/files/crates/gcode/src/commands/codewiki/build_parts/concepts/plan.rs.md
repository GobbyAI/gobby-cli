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

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts|crates/gcode/src/commands/codewiki/build_parts/concepts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` exposes 10 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `curated_navigation_prompt` | function | This function constructs and returns a prompt string that requests a JSON-formatted codewiki navigation layer by appending formatted structural and summary metadata from up to 40 modules and 80 representative files. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38] |
| `parse_plan` | function | The 'parse_plan' function trims a raw string slice, strips optional triple-single-quote code block fences (with or without a 'json' specifier), and deserializes the resulting JSON string into a 'CuratedNavigationPlan' struct, returning 'Some' on success or 'None' if deserialization fails. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:40-49] |
| `fallback_plan` | function | The 'fallback_plan' function constructs a 'CuratedNavigationPlan' containing a "System Tour" 'ConceptSection' populated by mapping input modules into a structured collection of 'ConceptModule's, alongside representative file paths and an introductory narrative page. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:51-138] |
| `normalize_concepts` | function | Normalizes a collection of concepts by validating module and file references against known sets, sanitizing text fields, filtering invalid entries, and generating deterministic slugs derived from the lexicographically smallest member to maintain cross-page link stability. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:140-201] |
| `normalize_sections` | function | Normalizes and filters concept sections by trimming text fields, validating concept references against a concept key map, and generating a default "System Tour" section if no valid sections remain. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:203-237] |
| `normalize_narrative_pages` | function | # Summary Normalizes and validates narrative pages by sanitizing text fields, generating URL slugs, filtering references to known modules/files/concepts, and excluding pages with empty required fields. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:239-350] |
| `concept_key_map` | function | Constructs a BTreeMap that maps each concept's title, slugified title, and slug to its final slug, enabling multi-key concept lookup and reference resolution across multiple identifier formats. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:352-366] |
| `narrative_page` | function | This function instantiates a 'NarrativePage' struct with the provided 'slug' and 'title' parameters, initializing remaining fields to empty vectors, 'None' for the body field, and 'false' for body_degraded. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:372-384] |

_Verified by 2 in-file unit tests._

