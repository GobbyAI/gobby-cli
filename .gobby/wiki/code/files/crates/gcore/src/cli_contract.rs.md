---
title: crates/gcore/src/cli_contract.rs
type: code_file
provenance:
- file: crates/gcore/src/cli_contract.rs
  ranges:
  - 4-12
  - 15-30
  - 32-52
  - 55-58
  - 61-68
  - 71-75
  - 78-82
  - 84-123
  - 125-141
  - 150-178
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/cli_contract.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file defines the serializable data model for a CLI contract: a top-level `CliContract` that describes a tool, its version, summary, global flags, scope, commands, and error codes, plus nested contract types for commands, flags, positionals, scope, and degradation metadata. `CommandContract::new` provides a validated base builder with empty defaults, and the `FlagContract` and `PositionalContract` helper constructors encode common CLI argument shapes while serde skip rules omit empty optional fields; the included test verifies that command contracts serialize to the expected builder-shaped JSON and leave out empty optional sections.
[crates/gcore/src/cli_contract.rs:4-12]
[crates/gcore/src/cli_contract.rs:15-30]
[crates/gcore/src/cli_contract.rs:32-52]
[crates/gcore/src/cli_contract.rs:33-51]
[crates/gcore/src/cli_contract.rs:55-58]

## API Symbols

- `CliContract` (class) component `CliContract [class]` (`b72631c7-3e9b-5815-b859-d3bedb4e01d9`) lines 4-12 [crates/gcore/src/cli_contract.rs:4-12]
  - Signature: `pub struct CliContract {`
  - Purpose: Indexed class `CliContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:4-12]
- `CommandContract` (class) component `CommandContract [class]` (`45311237-6562-5e5e-b7cd-fc12d62a1403`) lines 15-30 [crates/gcore/src/cli_contract.rs:15-30]
  - Signature: `pub struct CommandContract {`
  - Purpose: Indexed class `CommandContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:15-30]
- `CommandContract` (class) component `CommandContract [class]` (`852f8975-80a3-591d-a944-479caef38b7d`) lines 32-52 [crates/gcore/src/cli_contract.rs:32-52]
  - Signature: `impl CommandContract {`
  - Purpose: Indexed class `CommandContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:32-52]
- `CommandContract.new` (method) component `CommandContract.new [method]` (`ba79c980-4cf3-5050-8cf3-eed853918639`) lines 33-51 [crates/gcore/src/cli_contract.rs:33-51]
  - Signature: `pub fn new(name: &'static str, summary: &'static str) -> Self {`
  - Purpose: Indexed method `CommandContract.new` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:33-51]
- `DegradationContract` (class) component `DegradationContract [class]` (`5f0e7662-0700-5b37-a9e2-3416ed890048`) lines 55-58 [crates/gcore/src/cli_contract.rs:55-58]
  - Signature: `pub struct DegradationContract {`
  - Purpose: Indexed class `DegradationContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:55-58]
- `FlagContract` (class) component `FlagContract [class]` (`1b3f84cf-68d3-5bab-ac56-9dc98ecda6bf`) lines 61-68 [crates/gcore/src/cli_contract.rs:61-68]
  - Signature: `pub struct FlagContract {`
  - Purpose: Indexed class `FlagContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:61-68]
- `PositionalContract` (class) component `PositionalContract [class]` (`6d9b35ce-2156-5f38-ae7c-e5739e890627`) lines 71-75 [crates/gcore/src/cli_contract.rs:71-75]
  - Signature: `pub struct PositionalContract {`
  - Purpose: Indexed class `PositionalContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:71-75]
- `ScopeContract` (class) component `ScopeContract [class]` (`b86c7235-8c21-5567-a01d-9fbce777dd7f`) lines 78-82 [crates/gcore/src/cli_contract.rs:78-82]
  - Signature: `pub struct ScopeContract {`
  - Purpose: Indexed class `ScopeContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:78-82]
- `FlagContract` (class) component `FlagContract [class]` (`27d3feb9-fb6b-5b7e-8d74-b590d71b2c7d`) lines 84-123 [crates/gcore/src/cli_contract.rs:84-123]
  - Signature: `impl FlagContract {`
  - Purpose: Indexed class `FlagContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:84-123]
- `FlagContract.switch` (method) component `FlagContract.switch [method]` (`8ddbe2ee-5a21-5b0a-8e59-86c8777b5f40`) lines 85-94 [crates/gcore/src/cli_contract.rs:85-94]
  - Signature: `pub fn switch(name: &'static str) -> Self {`
  - Purpose: Indexed method `FlagContract.switch` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:85-94]
- `FlagContract.value` (method) component `FlagContract.value [method]` (`3eed10ea-5822-5b40-a1b6-4fca04bc5c29`) lines 96-105 [crates/gcore/src/cli_contract.rs:96-105]
  - Signature: `pub fn value(name: &'static str, value_name: &'static str) -> Self {`
  - Purpose: Indexed method `FlagContract.value` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:96-105]
- `FlagContract.repeatable_value` (method) component `FlagContract.repeatable_value [method]` (`86d661a6-6ae0-5542-a351-2bea245e09e4`) lines 107-112 [crates/gcore/src/cli_contract.rs:107-112]
  - Signature: `pub fn repeatable_value(name: &'static str, value_name: &'static str) -> Self {`
  - Purpose: Indexed method `FlagContract.repeatable_value` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:107-112]
- `FlagContract.required` (method) component `FlagContract.required [method]` (`84c3ee7a-ebce-57fa-8129-4974e75bb71c`) lines 114-117 [crates/gcore/src/cli_contract.rs:114-117]
  - Signature: `pub fn required(mut self) -> Self {`
  - Purpose: Indexed method `FlagContract.required` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:114-117]
- `FlagContract.allowed` (method) component `FlagContract.allowed [method]` (`2034c0e0-3a5c-5d31-a96a-81378d7cdf55`) lines 119-122 [crates/gcore/src/cli_contract.rs:119-122]
  - Signature: `pub fn allowed(mut self, values: Vec<&'static str>) -> Self {`
  - Purpose: Indexed method `FlagContract.allowed` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:119-122]
- `PositionalContract` (class) component `PositionalContract [class]` (`6d23d8c4-47b2-5f1c-bf38-91a4ce2951db`) lines 125-141 [crates/gcore/src/cli_contract.rs:125-141]
  - Signature: `impl PositionalContract {`
  - Purpose: Indexed class `PositionalContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:125-141]
- `PositionalContract.required` (method) component `PositionalContract.required [method]` (`376e382f-fedf-50fc-a11e-d1880ed2c134`) lines 126-132 [crates/gcore/src/cli_contract.rs:126-132]
  - Signature: `pub fn required(name: &'static str) -> Self {`
  - Purpose: Indexed method `PositionalContract.required` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:126-132]
- `PositionalContract.repeatable` (method) component `PositionalContract.repeatable [method]` (`eac0dcf4-bc91-5b2b-8051-b45827c22cc4`) lines 134-140 [crates/gcore/src/cli_contract.rs:134-140]
  - Signature: `pub fn repeatable(name: &'static str) -> Self {`
  - Purpose: Indexed method `PositionalContract.repeatable` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:134-140]
- `command_contract_serializes_builder_shape_and_skips_empty_optional_fields` (function) component `command_contract_serializes_builder_shape_and_skips_empty_optional_fields [function]` (`4b4280ad-68b4-539e-b649-a6aa4c237983`) lines 150-178 [crates/gcore/src/cli_contract.rs:150-178]
  - Signature: `fn command_contract_serializes_builder_shape_and_skips_empty_optional_fields() {`
  - Purpose: Indexed function `command_contract_serializes_builder_shape_and_skips_empty_optional_fields` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:150-178]

