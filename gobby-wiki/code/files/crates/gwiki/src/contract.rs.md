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
| `contract` | function | Constructs and returns a 'CliContract' for the 'gwiki' local-first wiki CLI, defining contract version 5, global flags, project/topic scope defaults, and the command set and their JSON output schemas. [crates/gwiki/src/contract.rs:6-494] |
| `format_flag` | function | Creates a 'FlagContract' for the '--format' flag with the value spec '"json\|text"' and restricts allowed values to 'json' and 'text'. [crates/gwiki/src/contract.rs:496-498] |
| `ingest_file_flags` | function | Returns a vector of 'FlagContract' definitions for ingest-file CLI options, including two switches, two value flags, and three AI-related routing flags. [crates/gwiki/src/contract.rs:500-510] |
| `ai_flag` | function | Creates a 'FlagContract' for the given static flag name with a string value schema '"auto\|daemon\|direct\|off"' and constrains the accepted values to exactly 'auto', 'daemon', 'direct', or 'off'. [crates/gwiki/src/contract.rs:512-515] |
| `optional_positional` | function | Constructs and returns a 'PositionalContract' for the given 'name' that is always marked 'required: false' and uses the provided 'repeatable' flag. [crates/gwiki/src/contract.rs:517-523] |
| `scoped_keys` | function | Prepends the fixed keys '"command"' and '"scope"' to the input 'Vec<&'static str>' by appending the input vector onto a new vector containing those two values, then returns the combined vector. [crates/gwiki/src/contract.rs:525-529] |
| `contract_keys` | function | Returns a vector of static string keys identifying the contract fields: 'tool', 'contract_version', 'summary', 'global_flags', 'scope', 'commands', and 'error_codes'. [crates/gwiki/src/contract.rs:531-541] |

