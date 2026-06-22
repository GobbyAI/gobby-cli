---
title: crates/gcode/src/commands/codewiki/prompts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/prompts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/prompts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/prompts.rs` exposes 51 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/prompts.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `with_register` | function | The 'with_register' function conditionally appends register-specific prose guidance to a system string based on the provided 'ProseRegister' option, returning the result as a clone-on-write 'Cow' string. [crates/gcode/src/commands/codewiki/prompts.rs:36-51] |
| `symbol_prompt` | function | The 'symbol_prompt' function constructs and returns a formatted string containing a 'Symbol''s file path, qualified name, kind, and line range, along with its signature and docstring if they are present. [crates/gcode/src/commands/codewiki/prompts.rs:53-75] |
| `file_prompt` | function | The 'file_prompt' function generates a structured prompt string used to write a narrative explainer page for a specified source file by aggregating its file path, AST symbol summaries, cross-file relationships, and source excerpts. [crates/gcode/src/commands/codewiki/prompts.rs:77-90] |
| `content_file_prompt` | function | The 'content_file_prompt' function constructs and returns a prompt string that instructs an AI to generate a narrative explainer page for a given repository file by formatting the file path and appending a section with the provided source excerpt. [crates/gcode/src/commands/codewiki/prompts.rs:95-101] |
| `module_prompt` | function | The 'module_prompt' function constructs a prompt string for generating a module documentation brief by delegating to 'build_entity_prompt' with a static instruction, the entity type "Module", and the provided module metadata, child summaries, components, source excerpts, and relationship facts. [crates/gcode/src/commands/codewiki/prompts.rs:103-121] |
| `repo_prompt` | function | The 'repo_prompt' function constructs and returns a prompt 'String' for generating a repository overview brief by aggregating formatting guidance, tables of module and root-file summaries, and source code excerpts. [crates/gcode/src/commands/codewiki/prompts.rs:123-146] |
| `append_child_summary_table` | function | The 'append_child_summary_table' function appends a formatted Markdown table to a mutable string buffer by writing the specified headers and generating rows containing the name and a summarized excerpt of each 'ChildSummary' item from the provided slice. [crates/gcode/src/commands/codewiki/prompts.rs:148-156] |
| `append_component_table` | function | Appends a single-column Markdown table with a "Component" header and a row for each string in the 'components' slice to the mutable 'String' prompt. [crates/gcode/src/commands/codewiki/prompts.rs:158-163] |
| `append_table_guidance` | function | The 'append_table_guidance' function mutates the provided 'String' buffer by appending a table guidance header, the 'ENUMERABLE_FACTS_GUIDANCE' constant value, and trailing newline characters. [crates/gcode/src/commands/codewiki/prompts.rs:165-169] |
| `architecture_prompt` | function | The 'architecture_prompt' function constructs a prompt string for a repository architecture overview of a specified subsystem by delegating to 'build_entity_prompt' with the subsystem's files, modules, components, source excerpts, and default relationship facts. [crates/gcode/src/commands/codewiki/prompts.rs:171-188] |
| `architecture_narrative_prompt` | function | This function constructs and returns a formatted prompt string instructing a model to write a layered architecture narrative by listing the names and summarized responsibilities of the provided subsystems alongside their cross-subsystem dependency edges. [crates/gcode/src/commands/codewiki/prompts.rs:192-220] |
| `PageEvidenceRow` | class | The 'PageEvidenceRow' struct is a public Rust data structure representing a record of page-associated evidence, containing public string fields for its name, kind, citation, and summary. [crates/gcode/src/commands/codewiki/prompts.rs:228-233] |
| `concept_page_prompt` | function | The 'concept_page_prompt' function constructs a prompt string for generating a reference explainer page for a concept by passing the provided title, summary, evidence members, symbols, and source excerpts, along with predefined concept-page source excerpts, to 'build_curated_page_prompt'. [crates/gcode/src/commands/codewiki/prompts.rs:237-253] |
| `narrative_page_prompt` | function | The 'narrative_page_prompt' function constructs and returns a guided-tour chapter prompt string for a section of the codebase by passing a specified instruction, metadata, and source excerpts to 'build_curated_page_prompt' along with the 'NARRATIVE_PAGE_SOURCE_EXCERPTS' constant. [crates/gcode/src/commands/codewiki/prompts.rs:257-273] |
| `verify_prompt` | function | The 'verify_prompt' function constructs a formatted audit prompt string by appending numbered draft blocks and conditionally interpolating a symbol summary table, relationship facts, and source excerpts based on their presence. [crates/gcode/src/commands/codewiki/prompts.rs:282-306] |
| `build_curated_page_prompt` | function | The 'build_curated_page_prompt' function constructs a formatted prompt string by aggregating a header, title, summary excerpt, table-formatted lists of member files and indexed symbols with evidence, and a specified number of source code excerpts. [crates/gcode/src/commands/codewiki/prompts.rs:308-344] |
| `append_evidence_table` | function | The function 'append_evidence_table' appends a Markdown-formatted table to a mutable string buffer, generating a header from a specified four-column array and populating the rows by iterating over a slice of 'PageEvidenceRow' structs to extract and format their respective name, kind, citation, and summary fields. [crates/gcode/src/commands/codewiki/prompts.rs:346-359] |
| `append_symbol_summary_table` | function | This function appends a formatted Markdown table detailing symbol metadata—such as name, kind, component, line range, and purpose—to a mutable 'String' buffer, falling back to a default message if the provided slice of 'SymbolSummary' structs is empty. [crates/gcode/src/commands/codewiki/prompts.rs:361-391] |
| `append_relationship_section` | function | This function appends a formatted Markdown section to a mutable string buffer detailing cross-file relationships—specifically inbound calls, outbound calls, and imported file dependencies—by reading from the provided 'RelationshipFacts' struct. [crates/gcode/src/commands/codewiki/prompts.rs:399-441] |
| `build_entity_prompt` | function | The 'build_entity_prompt' function constructs and returns a formatted prompt string by assembling a header, entity metadata, table layout guidance, child summaries for files, modules, and components, relationship facts, and source code excerpts. [crates/gcode/src/commands/codewiki/prompts.rs:444-461] |
| `append_child_summary_sections` | function | Appends formatted tabular sections or fallback messages for files, child modules, and stable component IDs to a mutable string prompt. [crates/gcode/src/commands/codewiki/prompts.rs:463-486] |
| `append_source_excerpt_section` | function | Appends a formatted section of source excerpts to a mutable prompt string, limiting the total number of processed excerpts to 'MAX_PROMPT_SOURCE_EXCERPTS' by delegating to 'append_source_excerpt_section_n'. [crates/gcode/src/commands/codewiki/prompts.rs:488-490] |
| `append_source_excerpt_section_n` | function | Appends a formatted section containing metadata and bounded content for up to a specified number of source excerpts to a mutable string buffer, or a placeholder message if the list of source excerpts is empty. [crates/gcode/src/commands/codewiki/prompts.rs:495-510] |
| `summary_excerpt` | function | This function extracts the first paragraph of the input string, normalizes its internal whitespace, and truncates the resulting text to a maximum of 'CHILD_SUMMARY_EXCERPT_MAX_CHARS' characters, appending an ellipsis ('…') if truncation is required. [crates/gcode/src/commands/codewiki/prompts.rs:540-560] |

_7 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/codewiki/prompts.rs` for the full list._

_Verified by 20 in-file unit tests._

