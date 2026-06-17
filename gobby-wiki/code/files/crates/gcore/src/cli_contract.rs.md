---
title: crates/gcore/src/cli_contract.rs
type: code_file
provenance:
- file: crates/gcore/src/cli_contract.rs
  ranges:
  - 4-12
  - 15-30
  - 33-51
  - 55-58
  - 61-68
  - 71-75
  - 78-82
  - 85-94
  - 96-105
  - 107-112
  - 114-117
  - 119-122
  - 126-132
  - 134-140
  - 150-178
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/cli_contract.rs:4-12](crates/gcore/src/cli_contract.rs#L4-L12), [crates/gcore/src/cli_contract.rs:15-30](crates/gcore/src/cli_contract.rs#L15-L30), [crates/gcore/src/cli_contract.rs:33-51](crates/gcore/src/cli_contract.rs#L33-L51), [crates/gcore/src/cli_contract.rs:55-58](crates/gcore/src/cli_contract.rs#L55-L58), [crates/gcore/src/cli_contract.rs:61-68](crates/gcore/src/cli_contract.rs#L61-L68), [crates/gcore/src/cli_contract.rs:71-75](crates/gcore/src/cli_contract.rs#L71-L75), [crates/gcore/src/cli_contract.rs:78-82](crates/gcore/src/cli_contract.rs#L78-L82), [crates/gcore/src/cli_contract.rs:85-94](crates/gcore/src/cli_contract.rs#L85-L94), [crates/gcore/src/cli_contract.rs:96-105](crates/gcore/src/cli_contract.rs#L96-L105), [crates/gcore/src/cli_contract.rs:107-112](crates/gcore/src/cli_contract.rs#L107-L112), [crates/gcore/src/cli_contract.rs:114-117](crates/gcore/src/cli_contract.rs#L114-L117), [crates/gcore/src/cli_contract.rs:119-122](crates/gcore/src/cli_contract.rs#L119-L122), [crates/gcore/src/cli_contract.rs:126-132](crates/gcore/src/cli_contract.rs#L126-L132), [crates/gcore/src/cli_contract.rs:134-140](crates/gcore/src/cli_contract.rs#L134-L140), [crates/gcore/src/cli_contract.rs:150-178](crates/gcore/src/cli_contract.rs#L150-L178)

</details>

# crates/gcore/src/cli_contract.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Defines the serializable contract model for a CLI: `CliContract` describes the tool’s top-level metadata, global flags, scope, commands, and error codes, while `CommandContract` captures each command’s summary, daemon behavior, arguments, flags, dependencies, and optional multimodal/degradation metadata. The helper structs `FlagContract`, `PositionalContract`, `ScopeContract`, and `DegradationContract` model the smaller pieces, and the builder-style methods enforce valid construction and set common flag/positional variants. The included test verifies that command contracts serialize into the expected builder-shaped JSON and omit empty optional fields.
[crates/gcore/src/cli_contract.rs:4-12]
[crates/gcore/src/cli_contract.rs:15-30]
[crates/gcore/src/cli_contract.rs:33-51]
[crates/gcore/src/cli_contract.rs:55-58]
[crates/gcore/src/cli_contract.rs:61-68]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CliContract` | class | `pub struct CliContract {` | `CliContract [class]` | `b72631c7-3e9b-5815-b859-d3bedb4e01d9` | 4-12 [crates/gcore/src/cli_contract.rs:4-12] | Indexed class `CliContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:4-12] |
| `CommandContract` | class | `pub struct CommandContract {` | `CommandContract [class]` | `45311237-6562-5e5e-b7cd-fc12d62a1403` | 15-30 [crates/gcore/src/cli_contract.rs:15-30] | Indexed class `CommandContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:15-30] |
| `CommandContract::new` | method | `pub fn new(name: &'static str, summary: &'static str) -> Self {` | `CommandContract::new [method]` | `ba79c980-4cf3-5050-8cf3-eed853918639` | 33-51 [crates/gcore/src/cli_contract.rs:33-51] | Indexed method `CommandContract::new` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:33-51] |
| `DegradationContract` | class | `pub struct DegradationContract {` | `DegradationContract [class]` | `5f0e7662-0700-5b37-a9e2-3416ed890048` | 55-58 [crates/gcore/src/cli_contract.rs:55-58] | Indexed class `DegradationContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:55-58] |
| `FlagContract` | class | `pub struct FlagContract {` | `FlagContract [class]` | `1b3f84cf-68d3-5bab-ac56-9dc98ecda6bf` | 61-68 [crates/gcore/src/cli_contract.rs:61-68] | Indexed class `FlagContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:61-68] |
| `PositionalContract` | class | `pub struct PositionalContract {` | `PositionalContract [class]` | `6d9b35ce-2156-5f38-ae7c-e5739e890627` | 71-75 [crates/gcore/src/cli_contract.rs:71-75] | Indexed class `PositionalContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:71-75] |
| `ScopeContract` | class | `pub struct ScopeContract {` | `ScopeContract [class]` | `b86c7235-8c21-5567-a01d-9fbce777dd7f` | 78-82 [crates/gcore/src/cli_contract.rs:78-82] | Indexed class `ScopeContract` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:78-82] |
| `FlagContract::switch` | method | `pub fn switch(name: &'static str) -> Self {` | `FlagContract::switch [method]` | `8ddbe2ee-5a21-5b0a-8e59-86c8777b5f40` | 85-94 [crates/gcore/src/cli_contract.rs:85-94] | Indexed method `FlagContract::switch` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:85-94] |
| `FlagContract::value` | method | `pub fn value(name: &'static str, value_name: &'static str) -> Self {` | `FlagContract::value [method]` | `3eed10ea-5822-5b40-a1b6-4fca04bc5c29` | 96-105 [crates/gcore/src/cli_contract.rs:96-105] | Indexed method `FlagContract::value` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:96-105] |
| `FlagContract::repeatable_value` | method | `pub fn repeatable_value(name: &'static str, value_name: &'static str) -> Self {` | `FlagContract::repeatable_value [method]` | `86d661a6-6ae0-5542-a351-2bea245e09e4` | 107-112 [crates/gcore/src/cli_contract.rs:107-112] | Indexed method `FlagContract::repeatable_value` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:107-112] |
| `FlagContract::required` | method | `pub fn required(mut self) -> Self {` | `FlagContract::required [method]` | `84c3ee7a-ebce-57fa-8129-4974e75bb71c` | 114-117 [crates/gcore/src/cli_contract.rs:114-117] | Indexed method `FlagContract::required` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:114-117] |
| `FlagContract::allowed` | method | `pub fn allowed(mut self, values: Vec<&'static str>) -> Self {` | `FlagContract::allowed [method]` | `2034c0e0-3a5c-5d31-a96a-81378d7cdf55` | 119-122 [crates/gcore/src/cli_contract.rs:119-122] | Indexed method `FlagContract::allowed` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:119-122] |
| `PositionalContract::required` | method | `pub fn required(name: &'static str) -> Self {` | `PositionalContract::required [method]` | `376e382f-fedf-50fc-a11e-d1880ed2c134` | 126-132 [crates/gcore/src/cli_contract.rs:126-132] | Indexed method `PositionalContract::required` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:126-132] |
| `PositionalContract::repeatable` | method | `pub fn repeatable(name: &'static str) -> Self {` | `PositionalContract::repeatable [method]` | `eac0dcf4-bc91-5b2b-8051-b45827c22cc4` | 134-140 [crates/gcore/src/cli_contract.rs:134-140] | Indexed method `PositionalContract::repeatable` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:134-140] |
| `command_contract_serializes_builder_shape_and_skips_empty_optional_fields` | function | `fn command_contract_serializes_builder_shape_and_skips_empty_optional_fields() {` | `command_contract_serializes_builder_shape_and_skips_empty_optional_fields [function]` | `4b4280ad-68b4-539e-b649-a6aa4c237983` | 150-178 [crates/gcore/src/cli_contract.rs:150-178] | Indexed function `command_contract_serializes_builder_shape_and_skips_empty_optional_fields` in `crates/gcore/src/cli_contract.rs`. [crates/gcore/src/cli_contract.rs:150-178] |
