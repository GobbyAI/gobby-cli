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

`crates/gcode/src/commands/codewiki/prompts.rs` exposes 41 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/prompts.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `symbol_prompt` | function | Constructs a multi-line prompt string describing a symbol’s file path, qualified name, kind, and line range, and conditionally appends its non-empty signature and docstring as 'Signature:' and 'Existing docs:' sections. [crates/gcode/src/commands/codewiki/prompts.rs:19-41] |
| `file_prompt` | function | Constructs and returns a Markdown prompt string for generating a narrative explainer page for a source file by listing the file name, rendering either a symbols table or a “No indexed symbols” note, appending source excerpts, and returning the assembled text. [crates/gcode/src/commands/codewiki/prompts.rs:43-77] |
| `content_file_prompt` | function | Builds a prompt string instructing the model to write a narrative explainer page for a repository file, then appends a single 'SourceExcerpt' section for the given file path. [crates/gcode/src/commands/codewiki/prompts.rs:82-88] |
| `module_prompt` | function | 'module_prompt' builds and returns a module documentation brief by delegating the module name, file and child-module summaries, component names, and source excerpts to 'build_entity_prompt' with a module-specific instruction string. [crates/gcode/src/commands/codewiki/prompts.rs:90-106] |
| `repo_prompt` | function | Builds and returns a repository-overview prompt string by appending table guidance, a module summary section, a root-file summary section, and source-excerpt content, using “No modules”/“No root files” placeholders when the corresponding inputs are empty. [crates/gcode/src/commands/codewiki/prompts.rs:108-131] |
| `append_child_summary_table` | function | Appends a Markdown table of child summaries to 'prompt' by writing the provided header row and then one row per 'ChildSummary', consisting of the child name and a truncated excerpt of its summary. [crates/gcode/src/commands/codewiki/prompts.rs:133-141] |
| `append_component_table` | function | Appends a one-column Markdown table labeled 'Component' to 'prompt', with one row per string in 'components'. [crates/gcode/src/commands/codewiki/prompts.rs:143-148] |
| `append_table_guidance` | function | Appends a “Table guidance:” header, the 'ENUMERABLE_FACTS_GUIDANCE' text, and two trailing newline characters to the provided prompt string. [crates/gcode/src/commands/codewiki/prompts.rs:150-154] |
| `architecture_prompt` | function | Builds and returns a repository architecture overview prompt for a given subsystem by delegating the subsystem name, file and module summaries, component names, and source excerpts to 'build_entity_prompt'. [crates/gcode/src/commands/codewiki/prompts.rs:156-172] |
| `architecture_narrative_prompt` | function | Builds a 'String' prompt for an architecture narrative by listing each subsystem’s name and summarized responsibility plus the repository’s cross-subsystem dependency edges, with explicit fallback lines when either list is empty. [crates/gcode/src/commands/codewiki/prompts.rs:176-204] |
| `PageEvidenceRow` | class | 'PageEvidenceRow' is a data record struct containing four string fields'name', 'kind', 'citation', and 'summary' for representing a page-level evidence entry. [crates/gcode/src/commands/codewiki/prompts.rs:212-217] |
| `concept_page_prompt` | function | Builds and returns a curated prompt string for writing a reference explainer page about a concept by forwarding the title, summary, evidence rows, and sources to 'build_curated_page_prompt' with the concept-page instruction and 'CONCEPT_PAGE_SOURCE_EXCERPTS'. [crates/gcode/src/commands/codewiki/prompts.rs:221-237] |
| `narrative_page_prompt` | function | Builds and returns a curated guided-tour chapter prompt for a codebase page by forwarding the title, summary, evidence rows, and source excerpts to 'build_curated_page_prompt' with the narrative page excerpt limit. [crates/gcode/src/commands/codewiki/prompts.rs:241-257] |
| `verify_prompt` | function | Builds and returns an audit prompt string that lists each trimmed draft block with 1-based numbering and then appends a bounded source-excerpt section using 'append_source_excerpt_section_n' and 'VERIFY_SOURCE_EXCERPTS'. [crates/gcode/src/commands/codewiki/prompts.rs:264-273] |
| `build_curated_page_prompt` | function | Constructs and returns a curated page prompt string by combining a header, page title, summarized working summary, table-formatting guidance, evidence tables for members and symbols with file:line citations, and a capped source-excerpt section. [crates/gcode/src/commands/codewiki/prompts.rs:275-311] |
| `append_evidence_table` | function | Appends a markdown table to 'prompt' by writing the provided 4-column header and then one row per 'PageEvidenceRow', using each row’s 'name', 'kind', 'citation', and a summarized excerpt of 'summary'. [crates/gcode/src/commands/codewiki/prompts.rs:313-326] |
| `build_entity_prompt` | function | Constructs a prompt string by combining the header, a labeled entity identifier, table guidance, a “Files” section populated from child summaries, and a source excerpt section. [crates/gcode/src/commands/codewiki/prompts.rs:328-343] |
| `append_child_summary_sections` | function | Appends three formatted subsections to 'prompt' describing direct files, child modules, and stable component IDs, using summary tables when each collection is non-empty and inserting explicit “none” markers otherwise. [crates/gcode/src/commands/codewiki/prompts.rs:345-368] |
| `append_source_excerpt_section` | function | Appends a source excerpt section to 'prompt' by delegating to 'append_source_excerpt_section_n' with 'MAX_PROMPT_SOURCE_EXCERPTS' as the excerpt limit. [crates/gcode/src/commands/codewiki/prompts.rs:370-372] |
| `append_source_excerpt_section_n` | function | Appends a '"Source excerpts:"' section to 'prompt', emits '"- No source excerpts.\n"' and returns when 'sources' is empty, otherwise writes up to 'take' excerpt headers of the form '--- <path> (lines <start>-<end>)' followed by each excerpt and a trailing newline. [crates/gcode/src/commands/codewiki/prompts.rs:377-392] |
| `summary_excerpt` | function | Returns a normalized excerpt of the first paragraph in 'summary' by trimming, collapsing all whitespace to single spaces, and truncating to 'CHILD_SUMMARY_EXCERPT_MAX_CHARS' characters with a trailing '…' if needed. [crates/gcode/src/commands/codewiki/prompts.rs:422-442] |
| `bounded_excerpt` | function | Returns a right-trimmed copy of 'excerpt', truncating it at 'SOURCE_EXCERPT_MAX_CHARS' Unicode scalar values if longer and appending an ellipsis ('…'), otherwise returning the trimmed string unchanged. [crates/gcode/src/commands/codewiki/prompts.rs:446-460] |
| `SymbolSummary` | class | 'SymbolSummary' is a Rust struct that stores a symbol’s identity, classification, owning component metadata, source line range, and a free-text purpose description. [crates/gcode/src/commands/codewiki/prompts.rs:463-471] |
| `ChildSummary` | class | 'ChildSummary' is a public struct containing two owned 'String' fields, 'name' and 'summary', for storing a child's identifier and its textual summary. [crates/gcode/src/commands/codewiki/prompts.rs:474-477] |
| `SourceExcerpt` | class | 'SourceExcerpt' is a data-only struct that represents a quoted range from a source file by storing the file 'path', inclusive 'line_start' and 'line_end' bounds, and the extracted 'excerpt' text. [crates/gcode/src/commands/codewiki/prompts.rs:482-487] |
| `oversized_child` | function | Constructs a 'ChildSummary' whose 'name' is a clone of the input and whose 'summary' is '"One real sentence."' followed by 2,000 newline-separated '"[src/lib.rs:{line}]"' citations generated from the range '0..2_000'. [crates/gcode/src/commands/codewiki/prompts.rs:493-502] |
| `aggregate_prompts_bound_each_child_summary` | function | Creates three oversized child summaries and asserts that every '\| src/… \|' line in the module, architecture, and repo prompts is bounded to the configured excerpt limit plus row overhead and contains an ellipsis to indicate truncation. [crates/gcode/src/commands/codewiki/prompts.rs:505-525] |
| `short_summaries_pass_through_untruncated` | function | Verifies that 'module_prompt' includes an untruncated child summary verbatim in the generated prompt when the summary is already concise. [crates/gcode/src/commands/codewiki/prompts.rs:528-535] |
| `summary_excerpt_includes_ellipsis_inside_hard_cap` | function | Verifies that 'summary_excerpt' returns an excerpt whose character count never exceeds 'CHILD_SUMMARY_EXCERPT_MAX_CHARS', and that when the input is longer than the limit the truncated result ends with an ellipsis ('…'). [crates/gcode/src/commands/codewiki/prompts.rs:538-549] |
| `excerpt_flattens_multiline_summaries_to_one_line` | function | Verifies that 'module_prompt' flattens a child summary containing embedded newlines into a single-line table excerpt by replacing line breaks with spaces. [crates/gcode/src/commands/codewiki/prompts.rs:552-561] |
| `aggregate_prompts_request_tables_for_enumerable_facts` | function | Verifies that 'repo_prompt' generates compact Markdown table guidance for enumerable facts, including a module summary row and references to configuration keys, environment variables, and public API symbols. [crates/gcode/src/commands/codewiki/prompts.rs:564-579] |
| `file_prompt_lists_symbols_as_markdown_table` | function | Verifies that 'file_prompt' renders symbol summaries into a Markdown table with the expected columns and escapes pipe characters in symbol and component identifiers. [crates/gcode/src/commands/codewiki/prompts.rs:582-597] |
| `excerpt` | function | Constructs and returns a 'SourceExcerpt' from the given 'path' and 'content', setting 'path' to an owned string, 'line_start' to '1', 'line_end' to '40', and 'excerpt' to the full content string. [crates/gcode/src/commands/codewiki/prompts.rs:599-606] |
| `aggregate_prompts_embed_bounded_source_excerpts` | function | Verifies that 'module_prompt' caps the number of embedded source excerpt headers at 'MAX_PROMPT_SOURCE_EXCERPTS' and keeps each excerpt block within a bounded character limit, even when given oversized excerpts. [crates/gcode/src/commands/codewiki/prompts.rs:609-633] |
| `prompts_without_excerpts_state_their_absence` | function | Constructs an empty repository prompt and asserts that it explicitly includes the 'Source excerpts' section indicating 'No source excerpts.' [crates/gcode/src/commands/codewiki/prompts.rs:636-639] |
| `content_file_prompt_carries_leading_content` | function | Verifies that 'content_file_prompt' includes the target filename header, the expected line-range label, and the leading excerpt content for 'README.md'. [crates/gcode/src/commands/codewiki/prompts.rs:642-650] |
| `architecture_narrative_prompt_lists_subsystems_and_edges` | function | Builds an architecture narrative prompt from subsystem summaries and dependency edges, rendering each subsystem as a bullet and either listing cross-subsystem edges or explicitly stating that none exist. [crates/gcode/src/commands/codewiki/prompts.rs:653-673] |
| `evidence` | function | Constructs and returns a 'PageEvidenceRow' by cloning the four '&str' inputs into owned 'String' fields for 'name', 'kind', 'citation', and 'summary'. [crates/gcode/src/commands/codewiki/prompts.rs:675-682] |
| `concept_page_prompt_embeds_evidence_anchors_and_extra_excerpts` | function | Tests that 'concept_page_prompt' includes evidence anchors for members and symbols and preserves per-page source excerpts up to its local budget, including a fifth excerpt that would be excluded by the shared aggregate cap. [crates/gcode/src/commands/codewiki/prompts.rs:685-718] |
| `narrative_page_prompt_grounds_with_members_and_symbols` | function | Verifies that 'narrative_page_prompt("Introduction", "Start here.", ...)' renders the supplied member and symbol evidence into the prompt and includes the “No source excerpts.” notice when no excerpts are provided. [crates/gcode/src/commands/codewiki/prompts.rs:721-743] |
| `curated_page_systems_demand_grounded_multi_section_output` | function | Verifies that the concept and narrative page system templates contain required section headings and the literals 'file:line' and 'No markdown fences.' to enforce grounded, multi-section output. [crates/gcode/src/commands/codewiki/prompts.rs:746-766] |

