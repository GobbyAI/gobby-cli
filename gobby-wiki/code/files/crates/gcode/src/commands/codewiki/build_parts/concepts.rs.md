---
title: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
  ranges:
  - 8-48
  - 50-108
  - 110-155
  - 157-187
  - 189-234
  - 236-268
  - 270-279
  - 281-356
  - 358-399
  - 401-435
  - 437-500
  - 502-509
  - 511-520
  - 522-549
  - 551-569
  - 571-577
  - 579-595
  - 597-599
  - 601-603
  - 605-607
  - 609-623
  - 626-633
  - 636-646
  - 649-655
  - 658-670
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:8-48](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L8-L48), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:50-108](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L50-L108), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:110-155](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L110-L155), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:157-187](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L157-L187), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:189-234](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L189-L234), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:236-268](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L236-L268), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:270-279](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L270-L279), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:281-356](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L281-L356), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:358-399](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L358-L399), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:401-435](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L401-L435), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:437-500](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L437-L500), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:502-509](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L502-L509), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:511-520](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L511-L520), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:522-549](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L522-L549), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:551-569](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L551-L569), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:571-577](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L571-L577), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:579-595](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L579-L595), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:597-599](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L597-L599), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:601-603](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L601-L603), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:605-607](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L605-L607), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:609-623](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L609-L623), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:626-633](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L626-L633), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:636-646](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L636-L646), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:649-655](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L649-L655), [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:658-670](crates/gcode/src/commands/codewiki/build_parts/concepts.rs#L658-L670)

</details>

# crates/gcode/src/commands/codewiki/build_parts/concepts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds and renders the curated codewiki navigation docs for concepts and narratives. `build_curated_navigation_docs` gathers all source spans, tries to reuse previously built pages when inputs are unchanged, otherwise generates a navigation plan from a prompt, parses it or falls back to a deterministic plan, and hands that plan to the renderer.

The rendering path normalizes the planned concept modules, sections, and narrative pages against the available files/modules, then uses lookup maps and span helpers to produce the final docs. The remaining helpers handle prompt construction, plan parsing and fallback, span collection, title/path/slug derivation, and the data types that describe the curated navigation structure.
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:8-48]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:50-108]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:110-155]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:157-187]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:189-234]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_curated_navigation_docs` | function | `pub(crate) fn build_curated_navigation_docs(` | `build_curated_navigation_docs [function]` | `722003dd-daa6-5e28-95de-6fbf262d4a25` | 8-48 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:8-48] | Indexed function `build_curated_navigation_docs` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:8-48] |
| `render_curated_navigation_docs` | function | `fn render_curated_navigation_docs(` | `render_curated_navigation_docs [function]` | `e659bd3b-10e9-5bf8-a4e2-212b343bd3d8` | 50-108 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:50-108] | Indexed function `render_curated_navigation_docs` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:50-108] |
| `render_concept_tree` | function | `fn render_concept_tree(` | `render_concept_tree [function]` | `cb742d93-2cd9-56fd-8bef-811ca6e759dc` | 110-155 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:110-155] | Indexed function `render_concept_tree` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:110-155] |
| `render_concept_page` | function | `fn render_concept_page(concept: &ConceptModule, spans: &[SourceSpan], degraded: bool) -> String {` | `render_concept_page [function]` | `dccac6ac-b89b-5b4c-b2d1-c4c121bac1e5` | 157-187 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:157-187] | Indexed function `render_concept_page` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:157-187] |
| `render_narrative_page` | function | `fn render_narrative_page(` | `render_narrative_page [function]` | `d578b022-5fb3-590f-b72e-16a188e871f1` | 189-234 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:189-234] | Indexed function `render_narrative_page` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:189-234] |
| `curated_navigation_prompt` | function | `fn curated_navigation_prompt(files: &[FileDoc], modules: &[ModuleDoc]) -> String {` | `curated_navigation_prompt [function]` | `f9aa66aa-40c3-5e09-b279-51e7fcf5a411` | 236-268 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:236-268] | Indexed function `curated_navigation_prompt` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:236-268] |
| `parse_plan` | function | `fn parse_plan(raw: &str) -> Option<CuratedNavigationPlan> {` | `parse_plan [function]` | `9d6f0f18-b795-5392-8794-dc02d56ef7c9` | 270-279 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:270-279] | Indexed function `parse_plan` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:270-279] |
| `fallback_plan` | function | `fn fallback_plan(files: &[FileDoc], modules: &[ModuleDoc]) -> CuratedNavigationPlan {` | `fallback_plan [function]` | `b3ad01b8-0a4b-50d5-99c1-77d6e81e017e` | 281-356 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:281-356] | Indexed function `fallback_plan` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:281-356] |
| `normalize_concepts` | function | `fn normalize_concepts(` | `normalize_concepts [function]` | `ffbf7329-53b4-55b0-b098-6b2f04c9da9f` | 358-399 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:358-399] | Indexed function `normalize_concepts` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:358-399] |
| `normalize_sections` | function | `fn normalize_sections(` | `normalize_sections [function]` | `ef2d414e-aa84-5619-bbf9-d85d917d922d` | 401-435 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:401-435] | Indexed function `normalize_sections` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:401-435] |
| `normalize_narrative_pages` | function | `fn normalize_narrative_pages(` | `normalize_narrative_pages [function]` | `3c506f8d-b55a-5aac-b0f6-2feaa010ce5a` | 437-500 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:437-500] | Indexed function `normalize_narrative_pages` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:437-500] |
| `concept_key_map` | function | `fn concept_key_map(concepts: &[ConceptModule]) -> std::collections::BTreeMap<&str, String> {` | `concept_key_map [function]` | `2d4df8c0-a462-5ce7-8c65-3d283d9ae227` | 502-509 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:502-509] | Indexed function `concept_key_map` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:502-509] |
| `all_input_spans` | function | `fn all_input_spans(files: &[FileDoc], modules: &[ModuleDoc]) -> Vec<SourceSpan> {` | `all_input_spans [function]` | `d0905aa5-47e8-5913-b406-9528e1e46b64` | 511-520 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:511-520] | Indexed function `all_input_spans` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:511-520] |
| `narrative_spans` | function | `fn narrative_spans(` | `narrative_spans [function]` | `5777028d-d2a7-58c9-9d0b-24b840ef7947` | 522-549 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:522-549] | Indexed function `narrative_spans` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:522-549] |
| `item_spans` | function | `fn item_spans(` | `item_spans [function]` | `f7fa179b-b970-5f85-8d81-059a3eeebc1b` | 551-569 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:551-569] | Indexed function `item_spans` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:551-569] |
| `degraded_sources` | function | `fn degraded_sources(degraded: bool) -> Vec<String> {` | `degraded_sources [function]` | `47dffaa6-05b7-5270-ae85-20c3c8bfe987` | 571-577 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:571-577] | Indexed function `degraded_sources` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:571-577] |
| `concept_title` | function | `fn concept_title(module: &str) -> String {` | `concept_title [function]` | `e2b2742b-7b27-50b3-9fa9-f2fb8260672b` | 579-595 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:579-595] | Indexed function `concept_title` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:579-595] |
| `concept_doc_path` | function | `fn concept_doc_path(slug: &str) -> String {` | `concept_doc_path [function]` | `280d4949-ff80-52fa-a745-5a72de08c1c7` | 597-599 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:597-599] | Indexed function `concept_doc_path` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:597-599] |
| `concept_doc_stem` | function | `fn concept_doc_stem(slug: &str) -> String {` | `concept_doc_stem [function]` | `2573b221-8288-51a2-aa29-1e39c5f4706f` | 601-603 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:601-603] | Indexed function `concept_doc_stem` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:601-603] |
| `narrative_doc_path` | function | `fn narrative_doc_path(slug: &str) -> String {` | `narrative_doc_path [function]` | `663c1bdf-ed20-5cd3-98ab-b5684b4a713f` | 605-607 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:605-607] | Indexed function `narrative_doc_path` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:605-607] |
| `slugify` | function | `fn slugify(value: &str) -> String {` | `slugify [function]` | `adcdb73d-c3ca-5e91-ae4b-29d8b0baa600` | 609-623 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:609-623] | Indexed function `slugify` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:609-623] |
| `CuratedNavigationPlan` | class | `struct CuratedNavigationPlan {` | `CuratedNavigationPlan [class]` | `08a626bf-cec9-593b-8132-acddb101f35d` | 626-633 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:626-633] | Indexed class `CuratedNavigationPlan` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:626-633] |
| `ConceptModule` | class | `struct ConceptModule {` | `ConceptModule [class]` | `d0b05976-1c29-5b18-b2da-f2a0456601f7` | 636-646 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:636-646] | Indexed class `ConceptModule` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:636-646] |
| `ConceptSection` | class | `struct ConceptSection {` | `ConceptSection [class]` | `e16ff8c9-f8ab-52d3-9a57-b71e88e0ad2e` | 649-655 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:649-655] | Indexed class `ConceptSection` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:649-655] |
| `NarrativePage` | class | `struct NarrativePage {` | `NarrativePage [class]` | `72409af8-a97a-5f5f-842b-37a6cb035994` | 658-670 [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:658-670] | Indexed class `NarrativePage` in `crates/gcode/src/commands/codewiki/build_parts/concepts.rs`. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:658-670] |
