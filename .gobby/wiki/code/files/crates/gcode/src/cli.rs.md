---
title: crates/gcode/src/cli.rs
type: code_file
provenance:
- file: crates/gcode/src/cli.rs
  ranges:
  - 21-44
  - 47-52
  - 54-63
  - 66-71
  - 74-80
  - 84-385
  - 388-450
  - 453-464
  - 467-470
  - 472-478
  - 480-482
  - 484-486
  - 488-499
  - 501-509
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file defines the `gcode` CLI surface: a clap-parsed `Cli` root that carries global flags for project root, output format, verbosity, warnings, and freshness checks, then dispatches into the `Command` subcommand tree. It also defines value-enum argument types for AI routing and AI depth with `From` conversions into the core config types, plus validation helpers for non-empty grep patterns and bounded positive integers, and a formatter helper that chooses a default output format when the user does not specify one.
[crates/gcode/src/cli.rs:21-44]
[crates/gcode/src/cli.rs:47-52]
[crates/gcode/src/cli.rs:54-63]
[crates/gcode/src/cli.rs:55-62]
[crates/gcode/src/cli.rs:66-71]

## API Symbols

- `Cli` (class) component `Cli [class]` (`264e54c1-0bbe-53b8-ad64-ac66790dfc6e`) lines 21-44 [crates/gcode/src/cli.rs:21-44]
  - Signature: `pub(crate) struct Cli {`
  - Purpose: A clap-derived argument struct that aggregates global options for project root, output format, verbosity control, and cache freshness validation with subcommand dispatch. [crates/gcode/src/cli.rs:21-44]
- `AiRouteArg` (type) component `AiRouteArg [type]` (`1d24b3ac-3dd1-52f1-87f7-0f7d018182e3`) lines 47-52 [crates/gcode/src/cli.rs:47-52]
  - Signature: `pub(crate) enum AiRouteArg {`
  - Purpose: Indexed type `AiRouteArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:47-52]
- `AiRouting` (class) component `AiRouting [class]` (`5c82f871-9f53-5f10-9238-84bb92784779`) lines 54-63 [crates/gcode/src/cli.rs:54-63]
  - Signature: `impl From<AiRouteArg> for AiRouting {`
  - Purpose: Implements the `From<AiRouteArg>` trait to enable infallible conversion from the `AiRouteArg` enum to `AiRouting` by mapping each variant to its corresponding homonymous counterpart. [crates/gcode/src/cli.rs:54-63]
- `AiRouting.from` (method) component `AiRouting.from [method]` (`cecbe8f5-b5c6-539f-a1ab-cc3537f03968`) lines 55-62 [crates/gcode/src/cli.rs:55-62]
  - Signature: `fn from(value: AiRouteArg) -> Self {`
  - Purpose: Implements the `From` trait to convert an `AiRouteArg` enum value into its corresponding `AiRouting` variant through exhaustive pattern matching. [crates/gcode/src/cli.rs:55-62]
- `AiDepthArg` (type) component `AiDepthArg [type]` (`f38f3121-6b12-5aef-8091-7dd5fd749e1a`) lines 66-71 [crates/gcode/src/cli.rs:66-71]
  - Signature: `pub(crate) enum AiDepthArg {`
  - Purpose: Indexed type `AiDepthArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:66-71]
- `from` (function) component `from [function]` (`41201313-ba7e-58f2-8e2b-4342ce3238e1`) lines 74-80 [crates/gcode/src/cli.rs:74-80]
  - Signature: `fn from(value: AiDepthArg) -> Self {`
  - Purpose: Implements the `From<AiDepthArg>` trait to convert each variant of the input enum to the corresponding variant of `Self` via exhaustive pattern matching. [crates/gcode/src/cli.rs:74-80]
- `Command` (type) component `Command [type]` (`b894d587-5257-5619-a169-0f99c19b2ee1`) lines 84-385 [crates/gcode/src/cli.rs:84-385]
  - Signature: `pub(crate) enum Command {`
  - Purpose: Indexed type `Command` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:84-385]
- `GraphCommand` (type) component `GraphCommand [type]` (`8a2bb2a8-1daa-5e86-8dab-93b4052ed2b7`) lines 388-450 [crates/gcode/src/cli.rs:388-450]
  - Signature: `pub(crate) enum GraphCommand {`
  - Purpose: Indexed type `GraphCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:388-450]
- `VectorCommand` (type) component `VectorCommand [type]` (`3b477146-180a-5533-8b10-b53f3694d2ef`) lines 453-464 [crates/gcode/src/cli.rs:453-464]
  - Signature: `pub(crate) enum VectorCommand {`
  - Purpose: Indexed type `VectorCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:453-464]
- `EmbeddingsCommand` (type) component `EmbeddingsCommand [type]` (`e8375ffb-7f0c-57ad-8210-320375431816`) lines 467-470 [crates/gcode/src/cli.rs:467-470]
  - Signature: `pub(crate) enum EmbeddingsCommand {`
  - Purpose: Indexed type `EmbeddingsCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:467-470]
- `non_empty_grep_pattern` (function) component `non_empty_grep_pattern [function]` (`7e0340cb-36b4-599d-b0b6-a71c0dfb3744`) lines 472-478 [crates/gcode/src/cli.rs:472-478]
  - Signature: `fn non_empty_grep_pattern(value: &str) -> Result<String, String> {`
  - Purpose: Returns 'Ok' with a cloned 'String' when 'value' is non-empty, otherwise returns 'Err("gcode grep pattern cannot be empty")'. [crates/gcode/src/cli.rs:472-478]
- `positive_usize` (function) component `positive_usize [function]` (`1d85ee7d-2cd8-5ff9-bd34-05aa1f5dece8`) lines 480-482 [crates/gcode/src/cli.rs:480-482]
  - Signature: `fn positive_usize(value: &str) -> Result<usize, String> {`
  - Purpose: Parses 'value' into a 'usize' and returns a bounded-validation 'Result', delegating to 'bounded_positive_usize' with 'MAX_POSITIVE_USIZE_ARG' and the field name '"value"'. [crates/gcode/src/cli.rs:480-482]
- `grep_max_count` (function) component `grep_max_count [function]` (`a4090ed9-4aca-5e39-9761-619ba1becedc`) lines 484-486 [crates/gcode/src/cli.rs:484-486]
  - Signature: `fn grep_max_count(value: &str) -> Result<usize, String> {`
  - Purpose: Parses 'value' as a bounded positive 'usize' using 'bounded_positive_usize', enforcing 'MAX_GREP_MAX_COUNT' as the upper limit and labeling validation errors with '--max-count'. [crates/gcode/src/cli.rs:484-486]
- `bounded_positive_usize` (function) component `bounded_positive_usize [function]` (`55113a99-7ecb-5781-be1d-649abf191a52`) lines 488-499 [crates/gcode/src/cli.rs:488-499]
  - Signature: `fn bounded_positive_usize(value: &str, max: usize, name: &str) -> Result<usize, String> {`
  - Purpose: Parses 'value' as a 'usize' and returns it only if it is greater than zero and less than or equal to 'max', otherwise returns a formatted error naming 'name'. [crates/gcode/src/cli.rs:488-499]
- `effective_format` (function) component `effective_format [function]` (`231651c1-aa08-5915-91ab-724aa68e1656`) lines 501-509 [crates/gcode/src/cli.rs:501-509]
  - Signature: `pub(crate) fn effective_format(`
  - Purpose: Returns the caller-provided 'output::Format' when present, otherwise defaults to 'Text' for 'Command::Grep' and 'Json' for all other commands. [crates/gcode/src/cli.rs:501-509]

