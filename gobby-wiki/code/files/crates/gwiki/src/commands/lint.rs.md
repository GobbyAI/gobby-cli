---
title: crates/gwiki/src/commands/lint.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/lint.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/lint.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

`crates/gwiki/src/commands/lint.rs` exposes 1 indexed API symbol.

## How it fits

`crates/gwiki/src/commands/lint.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Delegates to 'super::run_analysis_command' to run the '"lint"' analysis for the given 'ScopeSelection', using 'lint::run' to produce results and 'lint::render_text' to serialize the lint report into a 'CommandOutcome' or 'WikiError'. [crates/gwiki/src/commands/lint.rs:3-11] |

