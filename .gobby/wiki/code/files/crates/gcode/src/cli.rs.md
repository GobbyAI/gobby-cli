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
  - 84-380
  - 383-445
  - 448-459
  - 462-465
  - 467-473
  - 475-477
  - 479-481
  - 483-494
  - 496-504
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
- `Command` (type) component `Command [type]` (`b894d587-5257-5619-a169-0f99c19b2ee1`) lines 84-380 [crates/gcode/src/cli.rs:84-380]
  - Signature: `pub(crate) enum Command {`
  - Purpose: Indexed type `Command` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:84-380]
- `GraphCommand` (type) component `GraphCommand [type]` (`0960d853-f42d-5796-bf40-1436d600ccd5`) lines 383-445 [crates/gcode/src/cli.rs:383-445]
  - Signature: `pub(crate) enum GraphCommand {`
  - Purpose: Indexed type `GraphCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:383-445]
- `VectorCommand` (type) component `VectorCommand [type]` (`003669f9-f244-5d23-a7c6-b5b07dba5381`) lines 448-459 [crates/gcode/src/cli.rs:448-459]
  - Signature: `pub(crate) enum VectorCommand {`
  - Purpose: Indexed type `VectorCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:448-459]
- `EmbeddingsCommand` (type) component `EmbeddingsCommand [type]` (`2f7c95c0-1fcf-593e-8321-e83bb1598564`) lines 462-465 [crates/gcode/src/cli.rs:462-465]
  - Signature: `pub(crate) enum EmbeddingsCommand {`
  - Purpose: Indexed type `EmbeddingsCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:462-465]
- `non_empty_grep_pattern` (function) component `non_empty_grep_pattern [function]` (`e0bd14f8-43d3-57e5-8551-678b9cc3be03`) lines 467-473 [crates/gcode/src/cli.rs:467-473]
  - Signature: `fn non_empty_grep_pattern(value: &str) -> Result<String, String> {`
  - Purpose: Indexed function `non_empty_grep_pattern` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:467-473]
- `positive_usize` (function) component `positive_usize [function]` (`467bbc7c-52d2-5eb9-bfca-74b47d7a5ff0`) lines 475-477 [crates/gcode/src/cli.rs:475-477]
  - Signature: `fn positive_usize(value: &str) -> Result<usize, String> {`
  - Purpose: Indexed function `positive_usize` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:475-477]
- `grep_max_count` (function) component `grep_max_count [function]` (`ce0a2e00-a68c-5c73-a0c5-96dd1e7b814c`) lines 479-481 [crates/gcode/src/cli.rs:479-481]
  - Signature: `fn grep_max_count(value: &str) -> Result<usize, String> {`
  - Purpose: Indexed function `grep_max_count` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:479-481]
- `bounded_positive_usize` (function) component `bounded_positive_usize [function]` (`e6e960ab-26f4-5111-a271-5931638cf9da`) lines 483-494 [crates/gcode/src/cli.rs:483-494]
  - Signature: `fn bounded_positive_usize(value: &str, max: usize, name: &str) -> Result<usize, String> {`
  - Purpose: Indexed function `bounded_positive_usize` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:483-494]
- `effective_format` (function) component `effective_format [function]` (`c3786b05-e88a-56a7-b1c4-51b5ac889074`) lines 496-504 [crates/gcode/src/cli.rs:496-504]
  - Signature: `pub(crate) fn effective_format(`
  - Purpose: Indexed function `effective_format` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:496-504]

