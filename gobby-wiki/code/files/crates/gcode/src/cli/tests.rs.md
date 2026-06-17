---
title: crates/gcode/src/cli/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/cli/tests.rs
  ranges:
  - 12-30
  - 32-36
  - 38-55
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/cli/tests.rs:12-30](crates/gcode/src/cli/tests.rs#L12-L30), [crates/gcode/src/cli/tests.rs:32-36](crates/gcode/src/cli/tests.rs#L32-L36), [crates/gcode/src/cli/tests.rs:38-55](crates/gcode/src/cli/tests.rs#L38-L55)

</details>

# crates/gcode/src/cli/tests.rs

Module: [[code/modules/crates/gcode/src/cli|crates/gcode/src/cli]]

## Purpose

Defines CLI tests that verify every leaf subcommand exposed by `Cli::command()` is present in the gobby contract. The test builds the set of documented contract command names, computes the set of clap leaf command paths with `clap_command_leaves`, and fails if any are missing. `collect_clap_command_leaves` walks the command tree recursively, tracking parent prefixes so nested subcommands are recorded as full space-separated paths, while `clap_command_leaves` just seeds the traversal and returns the collected set.
[crates/gcode/src/cli/tests.rs:12-30]
[crates/gcode/src/cli/tests.rs:32-36]
[crates/gcode/src/cli/tests.rs:38-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `clap_command_leaves_are_documented_in_contract` | function | `fn clap_command_leaves_are_documented_in_contract() {` | `clap_command_leaves_are_documented_in_contract [function]` | `8e9bd73b-e477-5325-ba1b-d43006c09621` | 12-30 [crates/gcode/src/cli/tests.rs:12-30] | Indexed function `clap_command_leaves_are_documented_in_contract` in `crates/gcode/src/cli/tests.rs`. [crates/gcode/src/cli/tests.rs:12-30] |
| `clap_command_leaves` | function | `fn clap_command_leaves(command: &clap::Command) -> BTreeSet<String> {` | `clap_command_leaves [function]` | `0adf76bf-f9c4-5bb3-bcc5-eae11cd5f490` | 32-36 [crates/gcode/src/cli/tests.rs:32-36] | Indexed function `clap_command_leaves` in `crates/gcode/src/cli/tests.rs`. [crates/gcode/src/cli/tests.rs:32-36] |
| `collect_clap_command_leaves` | function | `fn collect_clap_command_leaves(` | `collect_clap_command_leaves [function]` | `037841cb-7122-5c2a-af85-dd106dc9b6c5` | 38-55 [crates/gcode/src/cli/tests.rs:38-55] | Indexed function `collect_clap_command_leaves` in `crates/gcode/src/cli/tests.rs`. [crates/gcode/src/cli/tests.rs:38-55] |
