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

`crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `largest_member_module` | function | Returns the 'ModuleDoc' among the named modules that has a dependency diagram and the largest combined count of direct files plus child modules, breaking ties by reverse lexicographic order of 'module'. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:10-24] |
| `curated_navigation_prompt` | function | Builds a prompt string instructing a model to emit a JSON-only curated codewiki navigation layer, then appends up to 40 module summaries and up to 80 representative file summaries as grounding context. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:26-58] |
| `parse_plan` | function | Trims the input, optionally strips a surrounding triple-quote JSON fence (''''json' or ''''' ... '''''), then attempts to deserialize the remaining text into 'CuratedNavigationPlan', returning 'None' on any parse error. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:60-69] |
| `fallback_plan` | function | 'fallback_plan' synthesizes a fallback 'CuratedNavigationPlan' from the supplied files and modules by selecting up to 'MAX_CONCEPT_MODULES' non-empty modules as concept pages with capped direct-file links, building a single “System Tour” section plus root-module/representative-file/title lists, and packaging them into the navigation plan. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:71-154] |
| `normalize_concepts` | function | Trims concept titles and summaries, slugifies each concept’s slug or title, filters module/file links to known entries, truncates links and concept count to configured maxima, and drops any concept with an empty title or no remaining links. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:156-197] |
| `normalize_sections` | function | Trims section titles and summaries, resolves each listed concept slug against a concept-key map, drops sections with empty titles or no valid concepts, and if nothing remains while concepts exist, returns a default “System Tour” section containing all concept slugs. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:199-233] |
| `normalize_narrative_pages` | function | Normalizes 'NarrativePage' entries by trimming titles and summaries, generating a slug from the existing slug or title, retaining only concepts/modules/files that match known docs, and dropping any page with an empty title or summary. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:235-321] |
| `concept_key_map` | function | Builds a 'BTreeMap' that maps each concept’s title and slug string slices to a cloned copy of that concept’s slug. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:323-330] |

