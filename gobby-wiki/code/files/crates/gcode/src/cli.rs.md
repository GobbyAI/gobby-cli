---
title: crates/gcode/src/cli.rs
type: code_file
provenance:
- file: crates/gcode/src/cli.rs
  ranges:
  - 23-46
  - 49-54
  - 57-64
  - 68-73
  - 76-82
  - 86-408
  - 411-475
  - 478-491
  - 494-497
  - 499-505
  - 507-509
  - 511-513
  - 515-526
  - 528-536
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/cli.rs:23-46](crates/gcode/src/cli.rs#L23-L46), [crates/gcode/src/cli.rs:49-54](crates/gcode/src/cli.rs#L49-L54), [crates/gcode/src/cli.rs:57-64](crates/gcode/src/cli.rs#L57-L64), [crates/gcode/src/cli.rs:68-73](crates/gcode/src/cli.rs#L68-L73), [crates/gcode/src/cli.rs:76-82](crates/gcode/src/cli.rs#L76-L82), [crates/gcode/src/cli.rs:86-408](crates/gcode/src/cli.rs#L86-L408), [crates/gcode/src/cli.rs:411-475](crates/gcode/src/cli.rs#L411-L475), [crates/gcode/src/cli.rs:478-491](crates/gcode/src/cli.rs#L478-L491), [crates/gcode/src/cli.rs:494-497](crates/gcode/src/cli.rs#L494-L497), [crates/gcode/src/cli.rs:499-505](crates/gcode/src/cli.rs#L499-L505), [crates/gcode/src/cli.rs:507-509](crates/gcode/src/cli.rs#L507-L509), [crates/gcode/src/cli.rs:511-513](crates/gcode/src/cli.rs#L511-L513), [crates/gcode/src/cli.rs:515-526](crates/gcode/src/cli.rs#L515-L526), [crates/gcode/src/cli.rs:528-536](crates/gcode/src/cli.rs#L528-L536)

</details>

# crates/gcode/src/cli.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Defines the `gcode` CLI schema with `clap`: a top-level `Cli` parser for global flags like project root, output format, quiet/verbose, and freshness checks, plus a `Command` subcommand tree for the tool’s operations. It also includes small option enums for AI routing and AI depth that map into internal `gobby_core`/`gobby_code` types, along with helper validators and defaults for numeric bounds, grep limits, and effective output format selection.
[crates/gcode/src/cli.rs:23-46]
[crates/gcode/src/cli.rs:49-54]
[crates/gcode/src/cli.rs:57-64]
[crates/gcode/src/cli.rs:68-73]
[crates/gcode/src/cli.rs:76-82]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Cli` | class | `pub(crate) struct Cli {` | `Cli [class]` | `bebd32f4-3dee-5dc0-847a-8a3c62480610` | 23-46 [crates/gcode/src/cli.rs:23-46] | Indexed class `Cli` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:23-46] |
| `AiRouteArg` | type | `pub(crate) enum AiRouteArg {` | `AiRouteArg [type]` | `0701d7de-391c-5737-ae93-1453af54f239` | 49-54 [crates/gcode/src/cli.rs:49-54] | Indexed type `AiRouteArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:49-54] |
| `AiRouting::from` | method | `fn from(value: AiRouteArg) -> Self {` | `AiRouting::from [method]` | `70e909b2-b8b5-5965-a427-6ec9d33c551e` | 57-64 [crates/gcode/src/cli.rs:57-64] | Indexed method `AiRouting::from` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:57-64] |
| `AiDepthArg` | type | `pub(crate) enum AiDepthArg {` | `AiDepthArg [type]` | `3929437d-3d51-5c28-91da-28b9858e5210` | 68-73 [crates/gcode/src/cli.rs:68-73] | Indexed type `AiDepthArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:68-73] |
| `from` | function | `fn from(value: AiDepthArg) -> Self {` | `from [function]` | `1c78361a-c5e7-5bf4-818e-cbab2bb6c7f2` | 76-82 [crates/gcode/src/cli.rs:76-82] | Indexed function `from` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:76-82] |
| `Command` | type | `pub(crate) enum Command {` | `Command [type]` | `586b6ce6-6378-5146-b45f-7e9ca0bfa3c2` | 86-408 [crates/gcode/src/cli.rs:86-408] | Indexed type `Command` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:86-408] |
| `GraphCommand` | type | `pub(crate) enum GraphCommand {` | `GraphCommand [type]` | `fb7e1878-fdff-58e7-8d14-a7872efacd7c` | 411-475 [crates/gcode/src/cli.rs:411-475] | Indexed type `GraphCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:411-475] |
| `VectorCommand` | type | `pub(crate) enum VectorCommand {` | `VectorCommand [type]` | `a1c60369-4663-5b80-b201-076961cf0a0d` | 478-491 [crates/gcode/src/cli.rs:478-491] | Indexed type `VectorCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:478-491] |
| `EmbeddingsCommand` | type | `pub(crate) enum EmbeddingsCommand {` | `EmbeddingsCommand [type]` | `afdb5102-dbbd-5fff-a644-634982c08aa0` | 494-497 [crates/gcode/src/cli.rs:494-497] | Indexed type `EmbeddingsCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:494-497] |
| `non_empty_grep_pattern` | function | `fn non_empty_grep_pattern(value: &str) -> Result<String, String> {` | `non_empty_grep_pattern [function]` | `3430a5da-cf40-5f7f-974e-faf375c081f6` | 499-505 [crates/gcode/src/cli.rs:499-505] | Indexed function `non_empty_grep_pattern` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:499-505] |
| `positive_usize` | function | `fn positive_usize(value: &str) -> Result<usize, String> {` | `positive_usize [function]` | `6822eff6-77a8-5146-9508-c6e713f3b806` | 507-509 [crates/gcode/src/cli.rs:507-509] | Indexed function `positive_usize` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:507-509] |
| `grep_max_count` | function | `fn grep_max_count(value: &str) -> Result<usize, String> {` | `grep_max_count [function]` | `fa5c3f0d-e2f1-5a01-8bac-351a07ebe247` | 511-513 [crates/gcode/src/cli.rs:511-513] | Indexed function `grep_max_count` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:511-513] |
| `bounded_positive_usize` | function | `fn bounded_positive_usize(value: &str, max: usize, name: &str) -> Result<usize, String> {` | `bounded_positive_usize [function]` | `9b43dc34-d6c8-57c3-bcee-402c5cd8319e` | 515-526 [crates/gcode/src/cli.rs:515-526] | Indexed function `bounded_positive_usize` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:515-526] |
| `effective_format` | function | `pub(crate) fn effective_format(` | `effective_format [function]` | `6eef1815-bb2b-5c64-8c92-e907c7205cbb` | 528-536 [crates/gcode/src/cli.rs:528-536] | Indexed function `effective_format` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:528-536] |
