---
title: Concepts
type: code_concept
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs)

</details>

# Concepts

## Purpose

Concepts groups the related modules and files listed below; read the key components for the grounded detail.

## Key components

| Symbol | Kind | Source | Role |
| --- | --- | --- | --- |
| ConceptModule | class | [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:14-33] | 'ConceptModule' is a serde-backed internal data model for a concept page that stores a required 'title', optional 'slug', 'summary', 'modules', and 'files', plus skipped post-normalization state for the multi-section 'body' and a 'body_degraded' flag indicating fallback content generation. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:14-33] |
| ConceptSection | class | [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:36-42] | 'ConceptSection' is a serde-deserializable struct with a 'title' plus defaulted 'summary' and 'concepts' fields, where 'summary' is a 'String' and 'concepts' is a 'Vec<String>'. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:36-42] |
| CuratedNavigationPlan | class | [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:4-11] | 'CuratedNavigationPlan' is a serde-deserializable, module-private aggregate struct that groups three ordered collections of curated navigation content: concept modules, concept sections, and narrative pages. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:4-11] |
| NarrativePage | class | [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:45-63] | 'NarrativePage' is a serialized page metadata struct holding a slug, title, summary, concept/module/file lists, and a skipped optional chapter body with a degraded-content flag. [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:45-63] |
| all_input_spans | function | [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13] | Returns a deduplicated, sorted 'Vec<SourceSpan>' containing the union of all 'source_spans' from the provided 'files' and 'modules' by inserting them into a 'BTreeSet' and collecting the result. [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13] |
| append_curated_body | function | [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:265-281] | Appends a non-empty 'body' string to 'doc', ensuring it ends with two newlines, or otherwise appends a fallback section built from 'fallback_heading' and 'fallback_text' via 'write_section'. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:265-281] |
| append_dependency_diagram | function | [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:340-356] | Appends an "Architecture diagram" section to 'doc' containing the module's dependency diagram, but only when 'module' exists, has a diagram, and graph availability is not 'Unavailable', adding a 'degraded: graph-truncated' marker first if availability is 'Truncated'. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:340-356] |
| append_explore_section | function | [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:288-309] | Appends an '## Explore' section to 'doc' containing up to 'MAX_CURATED_KEY_COMPONENTS' wiki links for 'modules', or if none exist, for 'files', and returns without modification if both inputs yield no links. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:288-309] |
| chapter_link | function | [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:141-143] | Returns a tuple of string slices containing the page’s slug and title, in that order. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:141-143] |
| concept_doc_path | function | [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:27-29] | Returns the concept document path for a given slug by appending '.md' to the result of 'concept_doc_stem(slug)'. [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:27-29] |
| concept_doc_stem | function | [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:31-33] | Returns a 'String' containing the concept documentation path stem 'code/concepts/{slug}' by formatting the provided slug into that template. [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:31-33] |
| concept_key_map | function | [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:323-330] | Builds a 'BTreeMap' that maps each concept’s title and slug string slices to a cloned copy of that concept’s slug. [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:323-330] |

## Members

- `crates/gcode/src/commands/codewiki/build_parts/concepts` (module) [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:10-24]
- `crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:10-24]
- `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:12-138]
- `crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13]
- `crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:1-7]
- `crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:4-11]


## Explore

- [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts|crates/gcode/src/commands/codewiki/build_parts/concepts]]

