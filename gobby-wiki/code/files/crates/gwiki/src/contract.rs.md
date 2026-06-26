---
title: crates/gwiki/src/contract.rs
type: code_file
provenance:
- file: crates/gwiki/src/contract.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/contract.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/contract.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/contract.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `contract` | function | Returns a 'CliContract' that specifies the command-line interface schema for gwiki, a local-first wiki tool, including global flags, scope configuration, and command contracts for operations like indexing and search. [crates/gwiki/src/contract.rs:6-496] |
| `format_flag` | function | The 'format_flag' function creates and returns a 'FlagContract' that defines a '--format' command-line flag accepting "json" or "text" as mutually allowed values. [crates/gwiki/src/contract.rs:498-500] |
| `ingest_file_flags` | function | Returns a vector of command-line flag contracts defining switches and parameters for file processing, language translation, video sampling, and AI routing options. [crates/gwiki/src/contract.rs:502-512] |
| `ai_flag` | function | Creates a FlagContract for a named flag with validation restricting its value to one of four allowed options: "auto", "daemon", "direct", or "off". [crates/gwiki/src/contract.rs:514-517] |
| `optional_positional` | function | Constructs a 'PositionalContract' for an optional positional argument with the specified name and repeatability setting. [crates/gwiki/src/contract.rs:519-525] |
| `scoped_keys` | function | Prepends the static string references "command" and "scope" to an input vector of static strings and returns the combined vector. [crates/gwiki/src/contract.rs:527-531] |
| `contract_keys` | function | Returns a vector of static string slice references representing the canonical field identifiers for a contract schema. [crates/gwiki/src/contract.rs:533-543] |

