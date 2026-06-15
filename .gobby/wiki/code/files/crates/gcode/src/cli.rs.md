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
  - 388-452
  - 455-468
  - 471-474
  - 476-482
  - 484-486
  - 488-490
  - 492-503
  - 505-513
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Defines the `gcode` command-line interface with clap. `Cli` collects global flags for project root, output format, verbosity, warning suppression, and freshness checks, then dispatches into a large `Command` subcommand tree. The file also declares value-enum adapters for AI routing and AI depth so CLI choices can be converted into the core config types, plus validation helpers for non-empty grep patterns and bounded positive counts. `effective_format` ties the top-level format flag to command-specific defaults, using text for grep and JSON for other commands unless the user overrides it.
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
- `GraphCommand` (type) component `GraphCommand [type]` (`80b173c7-197c-56e3-99a3-44fbeb56d48b`) lines 388-452 [crates/gcode/src/cli.rs:388-452]
  - Signature: `pub(crate) enum GraphCommand {`
  - Purpose: Indexed type `GraphCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:388-452]
- `VectorCommand` (type) component `VectorCommand [type]` (`0d5bf8f2-0040-54a0-9937-9eb4591a3f6c`) lines 455-468 [crates/gcode/src/cli.rs:455-468]
  - Signature: `pub(crate) enum VectorCommand {`
  - Purpose: Indexed type `VectorCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:455-468]
- `EmbeddingsCommand` (type) component `EmbeddingsCommand [type]` (`1aac8d0c-ccd5-52bc-99af-45274f6b3eda`) lines 471-474 [crates/gcode/src/cli.rs:471-474]
  - Signature: `pub(crate) enum EmbeddingsCommand {`
  - Purpose: Indexed type `EmbeddingsCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:471-474]
- `non_empty_grep_pattern` (function) component `non_empty_grep_pattern [function]` (`b8c4d442-b005-5049-b736-cf94e5dc77aa`) lines 476-482 [crates/gcode/src/cli.rs:476-482]
  - Signature: `fn non_empty_grep_pattern(value: &str) -> Result<String, String> {`
  - Purpose: Returns 'Ok(value.to_string())' when the input string is non-empty, otherwise returns 'Err("gcode grep pattern cannot be empty")'. [crates/gcode/src/cli.rs:476-482]
- `positive_usize` (function) component `positive_usize [function]` (`74d9964a-be52-559f-a7a8-95790610f093`) lines 484-486 [crates/gcode/src/cli.rs:484-486]
  - Signature: `fn positive_usize(value: &str) -> Result<usize, String> {`
  - Purpose: Validates and returns 'value' as a 'usize' by delegating to 'bounded_positive_usize' with 'MAX_POSITIVE_USIZE_ARG' and the argument label '"value"'. [crates/gcode/src/cli.rs:484-486]
- `grep_max_count` (function) component `grep_max_count [function]` (`8228f9b8-85b6-52f2-80c0-1b211c070c8c`) lines 488-490 [crates/gcode/src/cli.rs:488-490]
  - Signature: `fn grep_max_count(value: &str) -> Result<usize, String> {`
  - Purpose: Parses 'value' as a positive 'usize' bounded by 'MAX_GREP_MAX_COUNT' for the '--max-count' option, returning an error string on validation failure. [crates/gcode/src/cli.rs:488-490]
- `bounded_positive_usize` (function) component `bounded_positive_usize [function]` (`7ce5fa8a-341a-599a-bd36-d6069bdf7040`) lines 492-503 [crates/gcode/src/cli.rs:492-503]
  - Signature: `fn bounded_positive_usize(value: &str, max: usize, name: &str) -> Result<usize, String> {`
  - Purpose: Parses 'value' as a 'usize' and returns it only if it is greater than zero and less than or equal to 'max', otherwise returning an error message naming the field. [crates/gcode/src/cli.rs:492-503]
- `effective_format` (function) component `effective_format [function]` (`715f73ac-4341-5a5b-8a3a-12f7db514bbe`) lines 505-513 [crates/gcode/src/cli.rs:505-513]
  - Signature: `pub(crate) fn effective_format(`
  - Purpose: Returns the explicit 'output::Format' when provided, otherwise defaults to 'Text' for 'Command::Grep' and 'Json' for all other commands. [crates/gcode/src/cli.rs:505-513]

