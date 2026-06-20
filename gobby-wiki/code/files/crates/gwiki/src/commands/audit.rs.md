---
title: crates/gwiki/src/commands/audit.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/audit.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/audit.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

`crates/gwiki/src/commands/audit.rs` exposes 1 indexed API symbol.

## How it fits

`crates/gwiki/src/commands/audit.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Delegates execution of the '"audit"' analysis command to 'super::run_analysis_command', passing the selected scope, an '"serialize audit report"' description, 'audit::AuditOptions::from_env()' as the runner configuration, and 'audit::render_text' as the renderer. [crates/gwiki/src/commands/audit.rs:3-13] |

