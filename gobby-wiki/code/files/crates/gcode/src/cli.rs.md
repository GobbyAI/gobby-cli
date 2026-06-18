---
title: crates/gcode/src/cli.rs
type: code_file
provenance:
- file: crates/gcode/src/cli.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/cli.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The crates/gcode/src/cli.rs file defines the command-line interface entry point and configuration structures for the gcode command-line utility. It acts as the user-facing gateway that parses CLI inputs, validates configuration parameters, and routes commands to the appropriate execution paths.

The main structure is the Cli struct, which is a crate-private Clap-parsed top-level command-line configuration struct (crates/gcode/src/cli.rs:23-46). This struct captures global settings like the project root, output format, verbose logging, quiet mode, and freshness checks.

## How it fits

This file serves as the translator between external CLI arguments and core library data types. By mapping command-line options into internal structures, it establishes the foundation for downstream data flow across Gobby crates.

It exposes several arguments and direct translation functions. The AiRouteArg enum (crates/gcode/src/cli.rs:49-54) and its From implementation (crates/gcode/src/cli.rs:57-64) map string-based user arguments directly onto Gobby's core AiRouting variants. Similarly, the AiDepthArg enum (crates/gcode/src/cli.rs:68-73) and its From converter (crates/gcode/src/cli.rs:76-82) translate command options into core Gobby code wiki parameters.
[crates/gcode/src/cli.rs:23-46]
[crates/gcode/src/cli.rs:49-54]
[crates/gcode/src/cli.rs:57-64]
[crates/gcode/src/cli.rs:68-73]
[crates/gcode/src/cli.rs:76-82]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Cli` | class | 'Cli' is a crate-private Clap-parsed top-level command-line configuration struct that provides global flags for project root, output format, quiet/verbose logging, and freshness checks, plus a required 'Command' subcommand. [crates/gcode/src/cli.rs:23-46] |
| `AiRouteArg` | type | Indexed type `AiRouteArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:49-54] |
| `AiRouting::from` | method | Converts an 'AiRouteArg' enum variant into the corresponding 'AiRouting' variant by direct one-to-one matching ('Auto', 'Daemon', 'Direct', or 'Off'). [crates/gcode/src/cli.rs:57-64] |
| `AiDepthArg` | type | Indexed type `AiDepthArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:68-73] |
| `from` | function | Converts an 'AiDepthArg' into the corresponding 'Self' enum variant by preserving 'Sections', 'Files', and 'Symbols' one-to-one. [crates/gcode/src/cli.rs:76-82] |
| `Command` | type | Indexed type `Command` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:86-414] |
| `GraphCommand` | type | Indexed type `GraphCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:417-481] |
| `VectorCommand` | type | Indexed type `VectorCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:484-500] |
| `EmbeddingsCommand` | type | Indexed type `EmbeddingsCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:503-506] |
| `non_empty_grep_pattern` | function | Returns 'Ok(value.to_string())' when 'value' is non-empty, otherwise returns 'Err("gcode grep pattern cannot be empty".to_string())'. [crates/gcode/src/cli.rs:508-514] |
| `positive_usize` | function | Parses 'value' into a 'usize' using 'bounded_positive_usize' with 'MAX_POSITIVE_USIZE_ARG' as the upper bound and '"value"' as the argument label, returning a 'Result<usize, String>'. [crates/gcode/src/cli.rs:516-518] |
| `grep_max_count` | function | Parses 'value' as a positive 'usize' bounded by 'MAX_GREP_MAX_COUNT' for the '--max-count' option by delegating to 'bounded_positive_usize', returning 'Result<usize, String>'. [crates/gcode/src/cli.rs:520-522] |
| `bounded_positive_usize` | function | Parses 'value' as a 'usize' and returns it only if it is nonzero and '<= max', otherwise returning a 'String' error stating that 'name' must be a positive integer or no more than 'max'. [crates/gcode/src/cli.rs:524-535] |
| `effective_format` | function | Returns the explicit 'output::Format' if provided, otherwise defaults to 'Text' for 'Command::Grep' and 'Json' for all other commands. [crates/gcode/src/cli.rs:537-545] |

