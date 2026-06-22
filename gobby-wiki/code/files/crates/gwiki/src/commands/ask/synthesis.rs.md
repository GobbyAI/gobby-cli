---
title: crates/gwiki/src/commands/ask/synthesis.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/synthesis.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/synthesis.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/ask/synthesis.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/ask/synthesis.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `synthesize` | function | Initializes AI context and routing for a text-generation request, records the requested and effective route in 'output.ai', and dispatches to direct, daemon, or unavailable handling based on the resolved 'AiRouting' while propagating any 'WikiError'. [crates/gwiki/src/commands/ask/synthesis.rs:15-45] |
| `generate_direct` | function | Calls 'text::generate_text' with the plan prompt and synthesis system prompt, records the returned text and model as a direct synthesis on success, and otherwise marks AI as unavailable, propagating the resulting 'WikiError' state via 'Result<(), WikiError>'. [crates/gwiki/src/commands/ask/synthesis.rs:47-60] |
| `generate_daemon` | function | Attempts to generate a synthesis via 'daemon::generate_via_daemon' using the plan prompt and system prompt, records the returned text/model into 'output' on success, and otherwise marks AI as unavailable based on 'require_ai'. [crates/gwiki/src/commands/ask/synthesis.rs:62-75] |
| `record_synthesis` | function | Normalizes the synthesized answer, marks the 'AskOutput' as answered with 'ai' metadata and available status, runs citation validation against the retrieved evidence, appends warnings for any unsupported claims, and stores the final answer, model, and citation check in 'output.synthesis'. [crates/gwiki/src/commands/ask/synthesis.rs:77-111] |
| `mark_ai_unavailable` | function | Sets 'AskOutput' to a degraded partial state when AI synthesis is unavailable, deduplicates the corresponding degraded-source and warning markers, propagates an optional AI error, and returns a configuration error instead if AI is required. [crates/gwiki/src/commands/ask/synthesis.rs:113-145] |
| `synthesis_system` | function | Returns a static instruction string directing answers to use only provided evidence excerpts and code citations, with a concise final-only response and an explicit note when evidence is insufficient. [crates/gwiki/src/commands/ask/synthesis.rs:147-149] |
| `routing_label` | function | Returns the static string label corresponding to an 'AiRouting' variant: '"auto"', '"daemon"', '"direct"', or '"off"'. [crates/gwiki/src/commands/ask/synthesis.rs:151-158] |

_Verified by 5 in-file unit tests._

