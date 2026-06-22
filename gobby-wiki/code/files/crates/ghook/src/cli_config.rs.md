---
title: crates/ghook/src/cli_config.rs
type: code_file
provenance:
- file: crates/ghook/src/cli_config.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/cli_config.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/cli_config.rs` exposes 12 indexed API symbols.

## How it fits

`crates/ghook/src/cli_config.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CliConfig` | class | 'CliConfig' is a Rust struct that holds configuration settings for a CLI, specifically a daemon source identifier, a set of critical hooks that enforce fail-closed behavior, and a custom exit code for handling malformed JSON inputs. [crates/ghook/src/cli_config.rs:11-18] |
| `CliConfig::for_cli` | method | The 'for_cli' method parses a case-insensitive command-line interface name and returns 'Some' instance of the struct configured with provider-specific source identifiers, critical hooks, and JSON error exit codes, or 'None' if the provider is unrecognized. [crates/ghook/src/cli_config.rs:21-59] |
| `CliConfig::for_dispatch` | method | The 'for_dispatch' method instantiates and returns 'Self' by attempting to retrieve configuration for the provided 'cli' identifier, falling back to the default ''claude'' configuration if the retrieval fails. [crates/ghook/src/cli_config.rs:61-63] |
| `CliConfig::is_critical_hook` | method | The 'is_critical_hook' method checks if the specified hook type string slice is contained within the instance's internal 'critical_hooks' collection and returns a boolean value. [crates/ghook/src/cli_config.rs:65-67] |

_Verified by 8 in-file unit tests._

