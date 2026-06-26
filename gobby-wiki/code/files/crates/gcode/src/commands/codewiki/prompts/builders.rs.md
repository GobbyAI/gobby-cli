---
title: crates/gcode/src/commands/codewiki/prompts/builders.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/prompts/builders.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/prompts/builders.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/prompts|crates/gcode/src/commands/codewiki/prompts]]

## Overview

`crates/gcode/src/commands/codewiki/prompts/builders.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/prompts/builders.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `with_register` | function | Returns a copy-on-write string that borrows the input system string if no register is provided, or allocates and returns a new string concatenating it with the guidance text corresponding to the given ProseRegister variant otherwise. [crates/gcode/src/commands/codewiki/prompts/builders.rs:24-39] |
| `symbol_prompt` | function | Constructs a formatted string prompt from a 'Symbol' containing its file path, qualified name, kind, line range, and optional signature and docstring fields. [crates/gcode/src/commands/codewiki/prompts/builders.rs:41-63] |
| `file_prompt` | function | 'file_prompt' constructs a prompt string that aggregates AST symbol summaries, cross-file relationships, and source code excerpts into a structured format for narrative documentation generation. [crates/gcode/src/commands/codewiki/prompts/builders.rs:65-78] |
| `content_file_prompt` | function | This function constructs a prompt string for documentation generation by combining a narrative instruction template with a given filename and source code excerpt. [crates/gcode/src/commands/codewiki/prompts/builders.rs:83-89] |
| `module_prompt` | function | Constructs a documentation prompt string for a module by delegating to 'build_entity_prompt' with the module name, file and child module summaries, components, source excerpts, and relationship metadata. [crates/gcode/src/commands/codewiki/prompts/builders.rs:91-109] |
| `repo_prompt` | function | Constructs and returns a prompt string that aggregates module summaries, file summaries, and source excerpts formatted for repository overview brief generation. [crates/gcode/src/commands/codewiki/prompts/builders.rs:111-134] |
| `architecture_prompt` | function | Generates a prompt string for summarizing a subsystem's architectural responsibilities from its constituent files, modules, components, and source code excerpts by delegating to 'build_entity_prompt'. [crates/gcode/src/commands/codewiki/prompts/builders.rs:136-153] |
| `architecture_narrative_prompt` | function | Constructs a formatted prompt string from subsystem metadata and inter-subsystem dependencies for generating a layered architecture narrative. [crates/gcode/src/commands/codewiki/prompts/builders.rs:157-185] |
| `concept_page_prompt` | function | Constructs a prompt string for generating a reference explainer page by delegating to 'build_curated_page_prompt' with the concept's title, summary, members, symbols, and source excerpts. [crates/gcode/src/commands/codewiki/prompts/builders.rs:189-205] |
| `narrative_page_prompt` | function | This function constructs a prompt string for generating guided-tour narrative documentation by delegating to 'build_curated_page_prompt' with provided codebase metadata, evidence rows, and source excerpts. [crates/gcode/src/commands/codewiki/prompts/builders.rs:209-225] |
| `verify_prompt` | function | Constructs a verification prompt string that lists numbered draft blocks and conditionally appends symbol summaries, cross-file relationships, and source excerpts based on their availability for auditing purposes. [crates/gcode/src/commands/codewiki/prompts/builders.rs:234-258] |
| `build_curated_page_prompt` | function | # Summary This function constructs a formatted prompt string by aggregating page metadata (header, title, summary), member and symbol evidence tables with file:line anchor citations, and source code excerpts for documentation generation. [crates/gcode/src/commands/codewiki/prompts/builders.rs:260-296] |
| `build_entity_prompt` | function | Constructs a formatted prompt string by sequentially concatenating an entity header, metadata, guidance, child entity summaries (files, modules, components), relationship facts, and source code excerpts. [crates/gcode/src/commands/codewiki/prompts/builders.rs:299-316] |
| `append_child_summary_sections` | function | This function appends formatted summary sections for child files, child modules, and stable component IDs to a prompt string, rendering either summary tables or empty-state messages for each section. [crates/gcode/src/commands/codewiki/prompts/builders.rs:318-341] |

