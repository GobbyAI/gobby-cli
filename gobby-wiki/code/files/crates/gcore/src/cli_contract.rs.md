---
title: crates/gcore/src/cli_contract.rs
type: code_file
provenance:
- file: crates/gcore/src/cli_contract.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/cli_contract.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/cli_contract.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gcore/src/cli_contract.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CliContract` | class | 'CliContract' is a Rust struct that encapsulates a CLI application's interface specification, containing tool metadata, versioning, available commands, global flags, scope configuration, and error code definitions. [crates/gcore/src/cli_contract.rs:4-12] |
| `CommandContract` | class | 'CommandContract' is a struct that encapsulates the complete specification of a daemon command, including its metadata, positional and flag arguments, JSON output schema, hard and optional dependencies, and optional multimodal/degradation behavior configurations. [crates/gcore/src/cli_contract.rs:15-30] |
| `CommandContract::new` | method | Constructs a new command contract instance by validating non-empty 'name' and 'summary' static string literals, then initializing all remaining fields to empty or false default values. [crates/gcore/src/cli_contract.rs:33-51] |
| `DegradationContract` | class | 'DegradationContract' is a Rust struct that specifies a static output shape string and a collection of static metadata key strings for a degradation operation. [crates/gcore/src/cli_contract.rs:55-58] |
| `FlagContract` | class | 'FlagContract' is a struct that specifies the schema and constraints for a command-line flag, including its name, value requirements, allowed values, and whether it is required or repeatable. [crates/gcore/src/cli_contract.rs:61-68] |
| `PositionalContract` | class | 'PositionalContract' is a struct that defines the metadata for a positional parameter, consisting of a static string name and boolean flags specifying whether it is required and repeatable. [crates/gcore/src/cli_contract.rs:71-75] |
| `ScopeContract` | class | 'ScopeContract' is a Rust struct that defines a scope specification through a collection of flag contracts, a static default string value, and a vector of static string identity key references. [crates/gcore/src/cli_contract.rs:78-82] |
| `FlagContract::switch` | method | Creates a Self instance representing a valueless, non-required, non-repeatable flag with the specified name. [crates/gcore/src/cli_contract.rs:85-94] |
| `FlagContract::value` | method | Constructs an instance with the given 'name' that accepts a single optional value with the specified 'value_name', with no allowed-values restrictions or repeatability. [crates/gcore/src/cli_contract.rs:96-105] |
| `FlagContract::repeatable_value` | method | Creates an instance of 'Self' with the 'repeatable' field set to 'true' and other fields inherited from 'Self::value(name, value_name)'. [crates/gcore/src/cli_contract.rs:107-112] |
| `FlagContract::required` | method | This method sets the 'required' field to 'true' and returns 'self' to enable fluent builder pattern chaining. [crates/gcore/src/cli_contract.rs:114-117] |
| `FlagContract::allowed` | method | Mutates 'self' by setting the 'allowed_values' field to the provided vector of static string references and returns 'self' to enable method chaining in a builder pattern. [crates/gcore/src/cli_contract.rs:119-122] |
| `PositionalContract::required` | method | This method constructs and returns a Self instance initialized with the provided static string name, the 'required' field set to 'true', and the 'repeatable' field set to 'false'. [crates/gcore/src/cli_contract.rs:126-132] |
| `PositionalContract::repeatable` | method | Constructs a new instance with the given static string name, initializing both the 'required' and 'repeatable' fields to 'true'. [crates/gcore/src/cli_contract.rs:134-140] |

_Verified by 1 in-file unit test._

