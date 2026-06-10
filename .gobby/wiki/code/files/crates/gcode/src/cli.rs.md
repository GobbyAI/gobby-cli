---
title: crates/gcode/src/cli.rs
type: code_file
provenance:
- file: crates/gcode/src/cli.rs
  ranges:
  - 21-44
  - 47-52
  - 54-63
  - 55-62
  - 66-71
  - 74-80
  - 84-376
  - 379-441
  - 444-455
  - 458-461
  - 463-469
  - 471-473
  - 475-477
  - 479-490
  - 492-500
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/cli.rs` exposes 15 indexed API symbols.
[crates/gcode/src/cli.rs:21-44]
[crates/gcode/src/cli.rs:47-52]
[crates/gcode/src/cli.rs:54-63]
[crates/gcode/src/cli.rs:55-62]
[crates/gcode/src/cli.rs:66-71]
[crates/gcode/src/cli.rs:74-80]
[crates/gcode/src/cli.rs:84-376]
[crates/gcode/src/cli.rs:379-441]
[crates/gcode/src/cli.rs:444-455]
[crates/gcode/src/cli.rs:458-461]
[crates/gcode/src/cli.rs:463-469]
[crates/gcode/src/cli.rs:471-473]
[crates/gcode/src/cli.rs:475-477]
[crates/gcode/src/cli.rs:479-490]
[crates/gcode/src/cli.rs:492-500]

## API Symbols

- `Cli` (class) component `Cli [class]` (`264e54c1-0bbe-53b8-ad64-ac66790dfc6e`) lines 21-44 [crates/gcode/src/cli.rs:21-44]
  - Signature: `pub(crate) struct Cli {`
  - Purpose: Indexed class `Cli` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:21-44]
- `AiRouteArg` (type) component `AiRouteArg [type]` (`1d24b3ac-3dd1-52f1-87f7-0f7d018182e3`) lines 47-52 [crates/gcode/src/cli.rs:47-52]
  - Signature: `pub(crate) enum AiRouteArg {`
  - Purpose: Indexed type `AiRouteArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:47-52]
- `AiRouting` (class) component `AiRouting [class]` (`5c82f871-9f53-5f10-9238-84bb92784779`) lines 54-63 [crates/gcode/src/cli.rs:54-63]
  - Signature: `impl From<AiRouteArg> for AiRouting {`
  - Purpose: Indexed class `AiRouting` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:54-63]
- `AiRouting.from` (method) component `AiRouting.from [method]` (`cecbe8f5-b5c6-539f-a1ab-cc3537f03968`) lines 55-62 [crates/gcode/src/cli.rs:55-62]
  - Signature: `fn from(value: AiRouteArg) -> Self {`
  - Purpose: Indexed method `AiRouting.from` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:55-62]
- `AiDepthArg` (type) component `AiDepthArg [type]` (`f38f3121-6b12-5aef-8091-7dd5fd749e1a`) lines 66-71 [crates/gcode/src/cli.rs:66-71]
  - Signature: `pub(crate) enum AiDepthArg {`
  - Purpose: Indexed type `AiDepthArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:66-71]
- `from` (function) component `from [function]` (`41201313-ba7e-58f2-8e2b-4342ce3238e1`) lines 74-80 [crates/gcode/src/cli.rs:74-80]
  - Signature: `fn from(value: AiDepthArg) -> Self {`
  - Purpose: Indexed function `from` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:74-80]
- `Command` (type) component `Command [type]` (`b894d587-5257-5619-a169-0f99c19b2ee1`) lines 84-376 [crates/gcode/src/cli.rs:84-376]
  - Signature: `pub(crate) enum Command {`
  - Purpose: Indexed type `Command` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:84-376]
- `GraphCommand` (type) component `GraphCommand [type]` (`55532fb4-8ee7-5baa-8173-1f90ffc40e33`) lines 379-441 [crates/gcode/src/cli.rs:379-441]
  - Signature: `pub(crate) enum GraphCommand {`
  - Purpose: Indexed type `GraphCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:379-441]
- `VectorCommand` (type) component `VectorCommand [type]` (`9bd38e3c-05d0-568f-80f6-7cd701889219`) lines 444-455 [crates/gcode/src/cli.rs:444-455]
  - Signature: `pub(crate) enum VectorCommand {`
  - Purpose: Indexed type `VectorCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:444-455]
- `EmbeddingsCommand` (type) component `EmbeddingsCommand [type]` (`973f2011-a42a-5b18-b25f-1cec1b8c7de1`) lines 458-461 [crates/gcode/src/cli.rs:458-461]
  - Signature: `pub(crate) enum EmbeddingsCommand {`
  - Purpose: Indexed type `EmbeddingsCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:458-461]
- `non_empty_grep_pattern` (function) component `non_empty_grep_pattern [function]` (`b3a23d4c-07cf-555c-af7d-017aa1582cc4`) lines 463-469 [crates/gcode/src/cli.rs:463-469]
  - Signature: `fn non_empty_grep_pattern(value: &str) -> Result<String, String> {`
  - Purpose: Indexed function `non_empty_grep_pattern` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:463-469]
- `positive_usize` (function) component `positive_usize [function]` (`09db0dba-04fd-5f06-a81a-ddde0906e01b`) lines 471-473 [crates/gcode/src/cli.rs:471-473]
  - Signature: `fn positive_usize(value: &str) -> Result<usize, String> {`
  - Purpose: Indexed function `positive_usize` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:471-473]
- `grep_max_count` (function) component `grep_max_count [function]` (`528493e4-6d15-5963-acd9-f8413a35a286`) lines 475-477 [crates/gcode/src/cli.rs:475-477]
  - Signature: `fn grep_max_count(value: &str) -> Result<usize, String> {`
  - Purpose: Indexed function `grep_max_count` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:475-477]
- `bounded_positive_usize` (function) component `bounded_positive_usize [function]` (`159a8ac1-360b-5221-a8f5-75814730f5e2`) lines 479-490 [crates/gcode/src/cli.rs:479-490]
  - Signature: `fn bounded_positive_usize(value: &str, max: usize, name: &str) -> Result<usize, String> {`
  - Purpose: Indexed function `bounded_positive_usize` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:479-490]
- `effective_format` (function) component `effective_format [function]` (`4e9f58f1-4ea4-52b0-b34f-4a5e8b80edd3`) lines 492-500 [crates/gcode/src/cli.rs:492-500]
  - Signature: `pub(crate) fn effective_format(`
  - Purpose: Indexed function `effective_format` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:492-500]

