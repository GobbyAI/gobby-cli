---
title: crates/gcode/src/cli/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/cli/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/cli/tests.rs

Module: [[code/modules/crates/gcode/src/cli|crates/gcode/src/cli]]

## Overview

## How it fits

The file bridges the runtime command-line parser with the system's external interface contract. The main test function, clap_command_leaves_are_documented_in_contract [crates/gcode/src/cli/tests.rs:12-30], generates the active command structure using the clap parser and extracts its leaves.

To retrieve these leaves, the test utilizes clap_command_leaves [crates/gcode/src/cli/tests.rs:32-36], which delegates to collect_clap_command_leaves [crates/gcode/src/cli/tests.rs:38-55]. This helper function recursively traverses the subcommand hierarchy, constructing space-delimited string paths for each leaf command.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `clap_command_leaves_are_documented_in_contract` | function | Verifies that every leaf command exposed by 'Cli::command()' via 'clap_command_leaves' has a corresponding entry in the Gobby contract, failing with a list of missing command names if any are absent. [crates/gcode/src/cli/tests.rs:12-30] |
| `clap_command_leaves` | function | Returns the set of leaf command names reachable from the given 'clap::Command' by recursively collecting them into a 'BTreeSet<String>'. [crates/gcode/src/cli/tests.rs:32-36] |
| `collect_clap_command_leaves` | function | Recursively traverses a 'clap::Command' subtree, building space-delimited subcommand paths from an optional prefix and inserting the full paths of all leaf subcommands into the provided 'BTreeSet<String>'. [crates/gcode/src/cli/tests.rs:38-55] |

