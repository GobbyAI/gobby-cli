---
title: crates/gwiki/src/commands/ask.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

`crates/gwiki/src/commands/ask.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/ask.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Validates that '--llm' is not used with '--ai off', retrieves evidence for the query and selection, builds an ask output from the retrieval plan, optionally synthesizes it with the AI routing settings, and renders the resulting 'CommandOutcome'. [crates/gwiki/src/commands/ask.rs:20-41] |

_Verified by 1 in-file unit test._

