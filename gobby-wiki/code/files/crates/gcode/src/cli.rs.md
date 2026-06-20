---
title: crates/gcode/src/cli.rs
type: code_file
provenance:
- file: crates/gcode/src/cli.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/cli.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcode/src/cli.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Cli` | class | 'Cli' is a crate-private Clap-parsed top-level command-line configuration struct that provides global flags for project root, output format, quiet/verbose logging, and freshness checks, plus a required 'Command' subcommand. [crates/gcode/src/cli.rs:23-46] |
| `AiRouteArg` | type | Indexed type `AiRouteArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:49-54] |
| `AiRouting::from` | method | Converts an 'AiRouteArg' enum variant into the corresponding 'AiRouting' variant by direct one-to-one matching ('Auto', 'Daemon', 'Direct', or 'Off'). [crates/gcode/src/cli.rs:57-64] |
| `AiDepthArg` | type | Indexed type `AiDepthArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:68-73] |
| `from` | function | Converts an 'AiDepthArg' into the corresponding 'Self' enum variant by preserving 'Sections', 'Files', and 'Symbols' one-to-one. [crates/gcode/src/cli.rs:76-82] |
| `AiProseDepthArg` | type | Indexed type `AiProseDepthArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:86-91] |
| `from` | function | This function implements a conversion that maps the 'Brief', 'Standard', and 'Deep' variants of the 'AiProseDepthArg' enum directly to their matching counterpart variants of the target type 'Self'. [crates/gcode/src/cli.rs:94-100] |
| `AiRegisterArg` | type | Indexed type `AiRegisterArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:104-108] |
| `from` | function | This function maps variants of the 'AiRegisterArg' enum to their corresponding equivalent variants in the implementing type 'Self'. [crates/gcode/src/cli.rs:111-117] |
| `Command` | type | Indexed type `Command` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:121-469] |
| `GraphCommand` | type | Indexed type `GraphCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:472-536] |
| `VectorCommand` | type | Indexed type `VectorCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:539-555] |
| `EmbeddingsCommand` | type | Indexed type `EmbeddingsCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:558-561] |
| `non_empty_grep_pattern` | function | The 'non_empty_grep_pattern' function validates whether a given string slice is non-empty, returning a 'Result' containing the owned string on success or an error message if the input is empty. [crates/gcode/src/cli.rs:563-569] |
| `positive_usize` | function | The 'positive_usize' function parses a string slice into a 'usize' by delegating to 'bounded_positive_usize' to validate that the parsed value is a positive integer bounded by 'MAX_POSITIVE_USIZE_ARG'. [crates/gcode/src/cli.rs:571-573] |
| `grep_max_count` | function | The 'grep_max_count' function parses a string slice into a positive 'usize' up to 'MAX_GREP_MAX_COUNT' representing the '--max-count' parameter, returning the parsed value or an error message on failure. [crates/gcode/src/cli.rs:575-577] |
| `bounded_positive_usize` | function | Parses a string slice into a 'usize', validating that it is greater than zero and does not exceed a specified maximum value 'max', and returns the parsed value or a formatted error message. [crates/gcode/src/cli.rs:579-590] |
| `effective_format` | function | This function returns the explicitly provided output format if present, or defaults to 'output::Format::Text' for grep commands and 'output::Format::Json' for all other commands. [crates/gcode/src/cli.rs:592-600] |

