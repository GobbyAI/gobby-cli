---
title: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/architecture_diagrams.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/architecture_diagrams.rs` exposes 35 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/architecture_diagrams.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_architecture_diagrams` | function | The 'render_architecture_diagrams' function compiles validated Mermaid-formatted topology flowcharts and runtime flow sequences rendered from a 'SystemModel' into a structured Markdown section, returning 'None' if no valid diagrams are generated. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:40-81] |
| `render_service_matrix` | function | The 'render_service_matrix' function generates a Markdown-formatted section and table summarizing the name, requirement level, and origin of each service in a 'SystemModel', returning 'Some(String)' if services exist or 'None' if the list is empty. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:88-120] |
| `service_requirement` | function | The 'service_requirement' function maps a given 'ServiceKind' enum variant to a static string slice describing its operational necessity and status within the system. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:125-137] |
| `render_topology_flowchart` | function | The 'render_topology_flowchart' function generates a Mermaid TD flowchart as a string, mapping workspace crates and service boundaries as nodes within separate subgraphs connected by dependency edges, or returns 'None' if the system model contains no crates. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:142-238] |
| `render_runtime_flow_sequence` | function | This function returns the rendered AI generation flow for the provided 'SystemModel' if it exists, falling back to the rendered ghook enqueue flow otherwise. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:250-255] |
| `render_ai_generation_flow` | function | The function 'render_ai_generation_flow' evaluates a system model for the presence of embedding and daemon services to conditionally construct, validate, and return a Mermaid sequence diagram representing the AI context resolution and generation routing flow. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:259-290] |
| `render_ghook_enqueue_flow` | function | The function generates and returns a markdown-fenced Mermaid sequence diagram illustrating the ghook envelope enqueuing flow, conditionally including Gobby daemon interactions based on the services defined in the 'SystemModel', provided that a 'GhookInbox' service is present and the generated diagram passes validation. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:295-320] |
| `has_mode` | function | The 'has_mode' function determines whether a specified 'RuntimeMode' is present within the 'runtime_modes' collection of a given 'SystemModel' reference, returning a boolean result. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:323-325] |
| `ai_feature_crate` | function | This function searches the given 'SystemModel' and returns the name of the first crate containing the "ai" feature as an optional string slice. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:329-335] |
| `provenance_crate` | function | Extracts the trimmed substring preceding the first open parenthesis in a provenance string and returns it if it is present in the specified set of crate names. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:341-344] |
| `node_id` | function | The 'node_id' function generates a sanitized identifier string by prefixing the input with '"c_"' and replacing all non-ASCII-alphanumeric characters with underscores. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:349-359] |
| `service_node_id` | function | The 'service_node_id' function maps a 'ServiceKind' enum variant to its corresponding static string identifier. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:362-374] |
| `service_edge_label` | function | The 'service_edge_label' function maps a 'ServiceKind' enum variant to a static string slice representing its corresponding service dependency classification label. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:384-394] |
| `mermaid_label` | function | The 'mermaid_label' function sanitizes a string slice for safe use in Mermaid diagram labels by escaping backslashes and encoding structural characters—including double quotes, brackets, parentheses, braces, and vertical bars—into their corresponding HTML entities, returning the result as a new 'String'. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:398-408] |
| `fence` | function | The 'fence' function trims trailing newlines from the input string slice and formats it into a triple-single-quoted Mermaid code block ending with a newline. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:411-414] |
| `is_valid_mermaid` | function | This function validates that a string slice is a properly structured Mermaid block by ensuring it is enclosed in triple-single-quote fences (beginning with ''''mermaid' and ending with '''''), contains a valid Mermaid header followed by at least one non-empty content line, and has balanced delimiters across its interior lines. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:433-478] |
| `balanced_delimiters` | function | This function determines whether parentheses, brackets, and braces are balanced and properly nested across a slice of string lines, ignoring any delimiters located inside double quotes and returning 'false' if any quote spans across line boundaries or if any delimiter counter drops below zero. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:482-513] |
| `sample_model` | function | The 'sample_model' function constructs and returns a hardcoded 'SystemModel' containing predefined 'Crate' metadata, inter-crate dependency 'Edge' definitions, and service boundaries with their associated enabled features. [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:525-589] |

_Verified by 17 in-file unit tests._

