---
title: crates/gcode/src/commands/codewiki/text
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/text/citations.rs
  ranges:
  - 26-34
  - 38-44
  - 46-51
  - 58-98
  - 100-106
  - 108-128
  - 130-142
  - 144-153
  - 155-161
  - 166-179
  - 181-197
  - 199-225
  - 227-244
  - 246-259
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
  ranges:
  - 7-21
  - 24-28
  - 36-38
  - 42-49
  - 51-58
  - 60-91
  - 93-130
  - 132-178
  - 180-204
  - 206-212
  - 214-223
  - 225-230
- file: crates/gcode/src/commands/codewiki/text/generation.rs
  ranges:
  - 20-68
  - 73-87
  - 89-97
  - 99-112
  - 119-123
  - 126-128
  - 132-141
  - 144-158
  - 167-177
  - 179-182
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
  ranges:
  - 7-10
  - 12-17
  - 19-27
  - 29-37
  - 39-62
  - 64-69
  - 71-75
  - 77-81
  - 83-102
  - 105-108
  - 111-114
  - 116-156
  - 158-162
  - 164-186
  - 188-194
  - 196-206
  - 208-211
  - 213-217
  - 225-231
  - 234-249
  - 252-264
  - 267-279
  - 282-293
  - 296-303
  - 306-313
  - 316-326
  - 329-333
- file: crates/gcode/src/commands/codewiki/text/structural.rs
  ranges:
  - 7-22
  - 24-33
  - 38-41
  - 43-55
  - 57-63
  - 65-67
  - 69-78
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/text/citations.rs:26-34](crates/gcode/src/commands/codewiki/text/citations.rs#L26-L34), [crates/gcode/src/commands/codewiki/text/citations.rs:38-44](crates/gcode/src/commands/codewiki/text/citations.rs#L38-L44), [crates/gcode/src/commands/codewiki/text/citations.rs:46-51](crates/gcode/src/commands/codewiki/text/citations.rs#L46-L51), [crates/gcode/src/commands/codewiki/text/citations.rs:58-98](crates/gcode/src/commands/codewiki/text/citations.rs#L58-L98), [crates/gcode/src/commands/codewiki/text/citations.rs:100-106](crates/gcode/src/commands/codewiki/text/citations.rs#L100-L106), [crates/gcode/src/commands/codewiki/text/citations.rs:108-128](crates/gcode/src/commands/codewiki/text/citations.rs#L108-L128), [crates/gcode/src/commands/codewiki/text/citations.rs:130-142](crates/gcode/src/commands/codewiki/text/citations.rs#L130-L142), [crates/gcode/src/commands/codewiki/text/citations.rs:144-153](crates/gcode/src/commands/codewiki/text/citations.rs#L144-L153), [crates/gcode/src/commands/codewiki/text/citations.rs:155-161](crates/gcode/src/commands/codewiki/text/citations.rs#L155-L161), [crates/gcode/src/commands/codewiki/text/citations.rs:166-179](crates/gcode/src/commands/codewiki/text/citations.rs#L166-L179), [crates/gcode/src/commands/codewiki/text/citations.rs:181-197](crates/gcode/src/commands/codewiki/text/citations.rs#L181-L197), [crates/gcode/src/commands/codewiki/text/citations.rs:199-225](crates/gcode/src/commands/codewiki/text/citations.rs#L199-L225), [crates/gcode/src/commands/codewiki/text/citations.rs:227-244](crates/gcode/src/commands/codewiki/text/citations.rs#L227-L244), [crates/gcode/src/commands/codewiki/text/citations.rs:246-259](crates/gcode/src/commands/codewiki/text/citations.rs#L246-L259)
- [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-21](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L7-L21), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:24-28](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L24-L28), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:36-38](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L36-L38), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:42-49](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L42-L49), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:51-58](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L51-L58), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:60-91](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L60-L91), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:93-130](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L93-L130), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:132-178](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L132-L178), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:180-204](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L180-L204), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:206-212](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L206-L212), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:214-223](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L214-L223), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:225-230](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L225-L230)
- [crates/gcode/src/commands/codewiki/text/generation.rs:20-68](crates/gcode/src/commands/codewiki/text/generation.rs#L20-L68), [crates/gcode/src/commands/codewiki/text/generation.rs:73-87](crates/gcode/src/commands/codewiki/text/generation.rs#L73-L87), [crates/gcode/src/commands/codewiki/text/generation.rs:89-97](crates/gcode/src/commands/codewiki/text/generation.rs#L89-L97), [crates/gcode/src/commands/codewiki/text/generation.rs:99-112](crates/gcode/src/commands/codewiki/text/generation.rs#L99-L112), [crates/gcode/src/commands/codewiki/text/generation.rs:119-123](crates/gcode/src/commands/codewiki/text/generation.rs#L119-L123), [crates/gcode/src/commands/codewiki/text/generation.rs:126-128](crates/gcode/src/commands/codewiki/text/generation.rs#L126-L128), [crates/gcode/src/commands/codewiki/text/generation.rs:132-141](crates/gcode/src/commands/codewiki/text/generation.rs#L132-L141), [crates/gcode/src/commands/codewiki/text/generation.rs:144-158](crates/gcode/src/commands/codewiki/text/generation.rs#L144-L158), [crates/gcode/src/commands/codewiki/text/generation.rs:167-177](crates/gcode/src/commands/codewiki/text/generation.rs#L167-L177), [crates/gcode/src/commands/codewiki/text/generation.rs:179-182](crates/gcode/src/commands/codewiki/text/generation.rs#L179-L182)
- [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10](crates/gcode/src/commands/codewiki/text/sanitize.rs#L7-L10), [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17](crates/gcode/src/commands/codewiki/text/sanitize.rs#L12-L17), [crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27](crates/gcode/src/commands/codewiki/text/sanitize.rs#L19-L27), [crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37](crates/gcode/src/commands/codewiki/text/sanitize.rs#L29-L37), [crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62](crates/gcode/src/commands/codewiki/text/sanitize.rs#L39-L62), [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-69](crates/gcode/src/commands/codewiki/text/sanitize.rs#L64-L69), [crates/gcode/src/commands/codewiki/text/sanitize.rs:71-75](crates/gcode/src/commands/codewiki/text/sanitize.rs#L71-L75), [crates/gcode/src/commands/codewiki/text/sanitize.rs:77-81](crates/gcode/src/commands/codewiki/text/sanitize.rs#L77-L81), [crates/gcode/src/commands/codewiki/text/sanitize.rs:83-102](crates/gcode/src/commands/codewiki/text/sanitize.rs#L83-L102), [crates/gcode/src/commands/codewiki/text/sanitize.rs:105-108](crates/gcode/src/commands/codewiki/text/sanitize.rs#L105-L108), [crates/gcode/src/commands/codewiki/text/sanitize.rs:111-114](crates/gcode/src/commands/codewiki/text/sanitize.rs#L111-L114), [crates/gcode/src/commands/codewiki/text/sanitize.rs:116-156](crates/gcode/src/commands/codewiki/text/sanitize.rs#L116-L156), [crates/gcode/src/commands/codewiki/text/sanitize.rs:158-162](crates/gcode/src/commands/codewiki/text/sanitize.rs#L158-L162), [crates/gcode/src/commands/codewiki/text/sanitize.rs:164-186](crates/gcode/src/commands/codewiki/text/sanitize.rs#L164-L186), [crates/gcode/src/commands/codewiki/text/sanitize.rs:188-194](crates/gcode/src/commands/codewiki/text/sanitize.rs#L188-L194), [crates/gcode/src/commands/codewiki/text/sanitize.rs:196-206](crates/gcode/src/commands/codewiki/text/sanitize.rs#L196-L206), [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-211](crates/gcode/src/commands/codewiki/text/sanitize.rs#L208-L211), [crates/gcode/src/commands/codewiki/text/sanitize.rs:213-217](crates/gcode/src/commands/codewiki/text/sanitize.rs#L213-L217), [crates/gcode/src/commands/codewiki/text/sanitize.rs:225-231](crates/gcode/src/commands/codewiki/text/sanitize.rs#L225-L231), [crates/gcode/src/commands/codewiki/text/sanitize.rs:234-249](crates/gcode/src/commands/codewiki/text/sanitize.rs#L234-L249), [crates/gcode/src/commands/codewiki/text/sanitize.rs:252-264](crates/gcode/src/commands/codewiki/text/sanitize.rs#L252-L264), [crates/gcode/src/commands/codewiki/text/sanitize.rs:267-279](crates/gcode/src/commands/codewiki/text/sanitize.rs#L267-L279), [crates/gcode/src/commands/codewiki/text/sanitize.rs:282-293](crates/gcode/src/commands/codewiki/text/sanitize.rs#L282-L293), [crates/gcode/src/commands/codewiki/text/sanitize.rs:296-303](crates/gcode/src/commands/codewiki/text/sanitize.rs#L296-L303), [crates/gcode/src/commands/codewiki/text/sanitize.rs:306-313](crates/gcode/src/commands/codewiki/text/sanitize.rs#L306-L313), [crates/gcode/src/commands/codewiki/text/sanitize.rs:316-326](crates/gcode/src/commands/codewiki/text/sanitize.rs#L316-L326), [crates/gcode/src/commands/codewiki/text/sanitize.rs:329-333](crates/gcode/src/commands/codewiki/text/sanitize.rs#L329-L333)
- [crates/gcode/src/commands/codewiki/text/structural.rs:7-22](crates/gcode/src/commands/codewiki/text/structural.rs#L7-L22), [crates/gcode/src/commands/codewiki/text/structural.rs:24-33](crates/gcode/src/commands/codewiki/text/structural.rs#L24-L33), [crates/gcode/src/commands/codewiki/text/structural.rs:38-41](crates/gcode/src/commands/codewiki/text/structural.rs#L38-L41), [crates/gcode/src/commands/codewiki/text/structural.rs:43-55](crates/gcode/src/commands/codewiki/text/structural.rs#L43-L55), [crates/gcode/src/commands/codewiki/text/structural.rs:57-63](crates/gcode/src/commands/codewiki/text/structural.rs#L57-L63), [crates/gcode/src/commands/codewiki/text/structural.rs:65-67](crates/gcode/src/commands/codewiki/text/structural.rs#L65-L67), [crates/gcode/src/commands/codewiki/text/structural.rs:69-78](crates/gcode/src/commands/codewiki/text/structural.rs#L69-L78)

</details>

# crates/gcode/src/commands/codewiki/text

Parent: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The crates/gcode/src/commands/codewiki/text module is responsible for the end-to-end generation, cleaning, and formatting of CodeWiki documentation pages. It coordinates with AI-backed text generators, employing a bounded retry loop to robustly handle transient failures and fall back to degraded states with AST-only contents when generation is unavailable [crates/gcode/src/commands/codewiki/text/generation.rs:20-68]. To keep documentation clean, safe, and readable, the module cleans prompt echoes [crates/gcode/src/commands/codewiki/text/generation.rs:119-123], neutralizes unsafe or literal markdown and wikilinks into neutralized inline-code [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17], and filters out malformed or irrelevant citations [crates/gcode/src/commands/codewiki/text/citations.rs:100-106].

Additionally, the module structures CodeWiki pages by generating serialized YAML frontmatter metadata—optionally indicating when the inputs or graphs are degraded—while capping the number of listed provenance source files [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-21, 42-49]. It constructs structural summaries of files, modules, and repositories by choosing symbol purposes from docstrings, generating file overview strings, and gathering unique source spans from linked files to support navigation [crates/gcode/src/commands/codewiki/text/structural.rs:7-22, 57-63].

### Module Constants
| Constant | Description | Supporting Span |
| --- | --- | --- |
| MAX_FALLBACK_CITATIONS | Hard cap (value: 5) on fallback citations to prevent extremely large citation walls in downstream prompts. | crates/gcode/src/commands/codewiki/text/citations.rs:26-34 |
| MAX_FRONTMATTER_PROVENANCE_FILES | Maximum cap (value: 30) of listed provenance files within the page frontmatter. | crates/gcode/src/commands/codewiki/text/frontmatter.rs:36-38 |
| GENERATION_RETRY_BACKOFF | Array of backoff durations used to pace bounded retry loops for retryable generation errors. | crates/gcode/src/commands/codewiki/text/generation.rs:20-68 |

### Public & Crate API Symbols
| Symbol | Type | Description | Supporting Span |
| --- | --- | --- | --- |
| resolve_text_generator | Function | Resolves an AI-backed text generator from routing settings and the current context. | crates/gcode/src/commands/codewiki/text/generation.rs:20-68 |
| frontmatter_with_degradation | Function | Builds serialized frontmatter including optional degradation fields and source listings. | crates/gcode/src/commands/codewiki/text/frontmatter.rs:42-49 |
| neutralize_symbol_purpose_links | Function | Scans text and replaces literal markdown links and wikilinks with inline code blocks. | crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17 |
| fallback_spans | Function | Scores and returns fallback citation spans, preferring representative entries from distinct files. | crates/gcode/src/commands/codewiki/text/citations.rs:58-98 |
| structural_symbol_purpose | Function | Selects a symbol's purpose from its summary, docstring, or an indexed fallback string. | crates/gcode/src/commands/codewiki/text/structural.rs:7-22 |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/text/citations.rs\|crates/gcode/src/commands/codewiki/text/citations.rs]] | Implements citation handling for codewiki text generation: it scores source spans against generated prose, prefers representative fallback citations from distinct source files, and deprioritizes asset/data files unless they are the only provenance available. It also builds citation lists, wraps and replaces inline citations with markers, writes a references section, grounds text against available spans, and strips or validates malformed citations by parsing citation parts and checking whether any valid citation remains. [crates/gcode/src/commands/codewiki/text/citations.rs:26-34] [crates/gcode/src/commands/codewiki/text/citations.rs:38-44] [crates/gcode/src/commands/codewiki/text/citations.rs:46-51] [crates/gcode/src/commands/codewiki/text/citations.rs:58-98] [crates/gcode/src/commands/codewiki/text/citations.rs:100-106] |
| [[code/files/crates/gcode/src/commands/codewiki/text/frontmatter.rs\|crates/gcode/src/commands/codewiki/text/frontmatter.rs]] | Builds the serialized frontmatter for codewiki pages, combining a title, page type, provenance, and fixed metadata like generated_by, trust, and freshness, with optional degradation fields when inputs are incomplete. The core builder `frontmatter_with_options` gathers and caps provenance files from source spans, optionally includes range links, and relies on helpers to format ranges and safely encode markdown paths and link labels. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-21] [crates/gcode/src/commands/codewiki/text/frontmatter.rs:24-28] [crates/gcode/src/commands/codewiki/text/frontmatter.rs:36-38] [crates/gcode/src/commands/codewiki/text/frontmatter.rs:42-49] [crates/gcode/src/commands/codewiki/text/frontmatter.rs:51-58] |
| [[code/files/crates/gcode/src/commands/codewiki/text/generation.rs\|crates/gcode/src/commands/codewiki/text/generation.rs]] | This file wires codewiki text generation end to end: it resolves an AI-backed text generator from the current context and routing settings, wraps model calls in a bounded retry loop for retryable errors, and falls back cleanly when generation is unavailable or fails. The `Generation` type tracks successful or degraded generation results, `maybe_generate` decides whether generation should run, and the cleanup helpers filter out prompt echoes and normalize generated text before it is returned or recorded. [crates/gcode/src/commands/codewiki/text/generation.rs:20-68] [crates/gcode/src/commands/codewiki/text/generation.rs:73-87] [crates/gcode/src/commands/codewiki/text/generation.rs:89-97] [crates/gcode/src/commands/codewiki/text/generation.rs:99-112] [crates/gcode/src/commands/codewiki/text/generation.rs:119-123] |
| [[code/files/crates/gcode/src/commands/codewiki/text/sanitize.rs\|crates/gcode/src/commands/codewiki/text/sanitize.rs]] | Sanitizes link-like text in CodeWiki content by scanning Markdown, identifying link and code ranges, and replacing unsafe or literal links with neutralized inline-code text. `sanitize_model_markdown_links` is the top-level entry point for model text, while `neutralize_symbol_purpose_links` combines Markdown-link and wikilink detection, skips code spans and fenced code blocks, and applies the collected replacements. The helper functions break that work into parsing link/code ranges, finding wikilink targets, checking whether ranges overlap or are contained, classifying unsafe targets such as absolute paths or URI schemes, and building the replacement text from the original label. [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10] [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17] [crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27] [crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37] [crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62] |
| [[code/files/crates/gcode/src/commands/codewiki/text/structural.rs\|crates/gcode/src/commands/codewiki/text/structural.rs]] | Builds structural summary text for codewiki documentation. It chooses a symbol’s purpose from its own summary, then docstring, then a fallback “Indexed …” sentence; generates file, module, and repository overview strings with plural-aware counts; suppresses the generic empty-file filler in child listings; writes formatted markdown sections; and collects unique source spans from linked files and modules, likely to support aggregated navigation or highlighting. [crates/gcode/src/commands/codewiki/text/structural.rs:7-22] [crates/gcode/src/commands/codewiki/text/structural.rs:24-33] [crates/gcode/src/commands/codewiki/text/structural.rs:38-41] [crates/gcode/src/commands/codewiki/text/structural.rs:43-55] [crates/gcode/src/commands/codewiki/text/structural.rs:57-63] |

## Components

| Component ID |
| --- |
| `fa943380-0501-5373-a714-5ab4987af8b7` |
| `c02cf790-b9de-5278-9fa8-5777daa87eca` |
| `a4e632c0-3e80-5fc7-90c3-616b20540091` |
| `ba5263ac-e540-51e0-a016-a88d65285fb9` |
| `3259ccdb-4bbb-5ca5-8a94-1672a0888c7e` |
| `d14e37d2-ce3c-533e-9bf7-ebb42cef4aa2` |
| `1bd8f5f4-499b-5e57-b8e6-55e2a27e6bd7` |
| `2da98224-d432-58ca-b667-5d59e63082e4` |
| `88b1c0c3-5b9a-544c-8f02-85353cbd72ef` |
| `c2f3f5c4-e3cf-5a98-9300-273ba3e26af1` |
| `8ca67329-d972-5fbf-9ff1-927845074c11` |
| `c52bbeb5-443f-5293-9ee1-d48ed1c4eb91` |
| `0dc90579-6e54-5bc4-964e-47624afcd042` |
| `c26c2e95-c4af-53b5-8b8e-106e5065ccc1` |
| `2dbefc28-73f8-5576-ba77-caad49f10b19` |
| `a07d25fa-911d-5052-8ad2-9e59577e9de0` |
| `343c9901-569b-5506-9d88-739c18e80a0c` |
| `2757dfe1-7833-59cd-83c3-7ec4715793c1` |
| `8cf33b97-9ec5-5160-9fb6-655951e15b22` |
| `9d20e8cc-ed24-50bc-9913-a7f67e8e1725` |
| `73b0f073-3628-5541-bb2c-1786719fb919` |
| `88d2dc3a-c34b-5513-997c-1b5d037dfe08` |
| `e3bb590f-9aaa-5363-b9fe-53b6457b7259` |
| `ff740c94-a578-5053-a88f-484c1da6900e` |
| `59516e4b-f55e-50ab-b80a-6534b9607174` |
| `8088ded6-e281-5a00-822c-ad718fd1df5c` |
| `a95a6d74-34aa-5df0-926d-eb4a49ccaead` |
| `7283cd8c-8a0b-58bd-afa2-d484e6011f15` |
| `891be826-d36f-552e-bcac-2405f3e3d5bd` |
| `870f6403-ab78-5e3f-9e56-c2694de1b5a7` |
| `caf23a4d-82c8-5286-94da-826e50c96869` |
| `ee94bbce-49a4-5d50-9713-9576829c4ad6` |
| `64c617e6-f233-56d6-87b4-2ff280cca315` |
| `8a4c98bc-11c2-548f-904b-798e6d45daaa` |
| `7752da58-8d5a-5b90-824d-92773829b337` |
| `03cbe5bf-ebc7-5e5a-8775-8738d3d5ff4f` |
| `ecb7b1b5-c702-56ff-ae9c-0b1ed393ad12` |
| `db6bcba6-bb62-5c6c-a896-81e73ccbcd87` |
| `9211fd49-090a-5e0f-9001-a4571c881563` |
| `55cf6a57-0936-5e0c-bd7f-3782705320b3` |
| `b6b139f4-73a9-5448-9a34-b2d859d41518` |
| `796b0f08-23b8-5038-8890-4d75602e8f92` |
| `cb4f7495-89f3-513f-b67a-1b4b01a072b1` |
| `3f648b8a-1625-530f-a2ed-b5627efa58bb` |
| `cf9428f2-a22e-59e7-bf6c-7822e69d4393` |
| `09affee9-e168-511f-b1e1-e20c6523556a` |
| `7ae53d93-79f3-51f4-90e3-6cbf4b0b97db` |
| `7c8c580f-762a-5ed4-865f-96dec151660a` |
| `d62c5e6c-5d65-5a4b-bb57-f1944c6b2c64` |
| `16ed05cb-f0ea-5d15-b151-f8a5bb191548` |
| `b2017898-cf41-5719-973f-42e381dfec57` |
| `485b0a91-7b90-5150-83cd-3daedfcdaa7c` |
| `509b1b6c-9fa0-50a5-9032-e7cc2466c478` |
| `ed367e4e-8304-5624-82a7-279b95149d47` |
| `fbdbb4f0-9e51-5b01-ac7a-6a6b61cb5248` |
| `ff81065f-9165-522c-8a33-e44eeee2f445` |
| `2f77300c-c0ee-56a5-9647-a305a1ba001f` |
| `2f3b2ef9-885f-5f2c-990c-88af4b8e53e5` |
| `ecbfc74a-7b8a-5df3-b07a-1a7c9d9f1d7c` |
| `8a299454-c5ef-5f8b-81a4-2108f5e9e084` |
| `64ea0b9e-7a54-5e5c-bcd1-6390134c1f00` |
| `3ff7b766-e91a-5acc-9f6e-c0ea42c8230f` |
| `4eb90fec-2fc4-58af-8adc-a2bd1693cec8` |
| `08c689ee-2680-5227-9833-f389907b0d39` |
| `b7650a83-1deb-5c2a-be4d-8cf288ac70ca` |
| `549d8297-848c-57c5-a259-5ba0d6895f6b` |
| `1e9f1190-f3d0-520d-8779-4f9c4952c293` |
| `11a45104-8d40-571e-bac0-4fe317017823` |
| `67ca6480-45b2-5bba-984a-5a93d04ed906` |
| `a1844f77-7674-5b7f-aa17-d5fbd34bd53a` |
