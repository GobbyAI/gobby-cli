---
title: crates/gcode/src/output.rs
type: code_file
provenance:
- file: crates/gcode/src/output.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/output.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/output.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/output.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Format` | type | Indexed type `Format` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:5-8] |
| `print_json` | function | Serializes 'value' to pretty-printed JSON with 'serde_json::to_string_pretty', writes it to stdout via 'println!', and returns 'Ok(())' or any serialization error as 'anyhow::Result<()>'. [crates/gcode/src/output.rs:11-14] |
| `print_json_compact` | function | Serializes the given 'Serialize' value to a compact JSON string, prints it to standard output with a trailing newline, and returns 'Ok(())' or propagates serialization errors via 'anyhow::Result'. [crates/gcode/src/output.rs:17-20] |
| `print_text` | function | Prints the provided '&str' to standard output with 'println!' and returns 'Ok(())' as an 'anyhow::Result<()>'. [crates/gcode/src/output.rs:23-26] |

