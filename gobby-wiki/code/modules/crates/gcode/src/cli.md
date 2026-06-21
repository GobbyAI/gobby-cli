---
title: crates/gcode/src/cli
type: code_module
provenance:
- file: crates/gcode/src/cli/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

## crates/gcode/src/cli

This module houses the CLI layer for the `gcode` crate, built on top of [clap](https://docs.rs/clap). The `tests.rs` file is the sole file directly present, but it pulls in five subtest modules — `codewiki`, `grep`, `projection`, `search`, and `top_level` — that collectively cover the full surface of the command hierarchy. The parent module exposes a `Cli` struct that implements both `clap::Parser` and `clap::CommandFactory`, serving as the root of the command tree tests.rs:1-2.

The primary contract-enforcement responsibility lives in `clap_command_leaves_are_documented_in_contract`. It constructs the live `Cli` command graph, walks it to collect every leaf subcommand (i.e., commands with no further subcommands), and then diffs that set against the authoritative list published by `gobby_code::contract::contract()`. Any clap-registered leaf command that lacks a matching contract entry causes the test to fail with a descriptive message listing the offenders tests.rs:11-29. This ensures the CLI and its external contract specification never drift apart.

The two helper functions implement a depth-first traversal of the clap command tree. `clap_command_leaves` initialises a `BTreeSet` and delegates to `collect_clap_command_leaves` tests.rs:31-35. The recursive helper builds a space-joined path string as it descends (e.g., `"search query"`), inserting only terminal nodes into the leaf set tests.rs:37-54. The use of `BTreeSet` throughout guarantees deterministic ordering in both the collected leaves and the diff output.

| Symbol | Kind | Role |
|---|---|---|
| `clap_command_leaves_are_documented_in_contract` | `#[test]` fn | Asserts every clap leaf command appears in `gobby_code::contract` tests.rs:11 |
| `clap_command_leaves` | fn | Entry point — returns `BTreeSet<String>` of all leaf command paths tests.rs:31 |
| `collect_clap_command_leaves` | fn | Recursive depth-first collector; builds space-delimited path strings tests.rs:37 |

| External dependency | Usage |
|---|---|
| `clap::{CommandFactory, Parser}` | Materialises the live command graph from `Cli` tests.rs:2 |
| `gobby_code::contract::contract()` | Provides the canonical set of documented command names for diffing tests.rs:14-18 |
| `std::collections::BTreeSet` | Sorted, diffable set used for leaf collection and contract comparison tests.rs:3 |
[crates/gcode/src/cli/tests.rs:12-30]
[crates/gcode/src/cli/tests.rs:32-36]
[crates/gcode/src/cli/tests.rs:38-55]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/cli/tests.rs\|crates/gcode/src/cli/tests.rs]] | `crates/gcode/src/cli/tests.rs` exposes 3 indexed API symbols. |

