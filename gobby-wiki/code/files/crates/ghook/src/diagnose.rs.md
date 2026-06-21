---
title: crates/ghook/src/diagnose.rs
type: code_file
provenance:
- file: crates/ghook/src/diagnose.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/diagnose.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/diagnose.rs` exposes 20 indexed API symbols.

## How it fits

`crates/ghook/src/diagnose.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DiagnoseOutput` | class | 'DiagnoseOutput' is a struct aggregating diagnostic and configuration metadata for a git hook system, including version information, CLI/daemon parameters, project context, and installation details. [crates/ghook/src/diagnose.rs:15-32] |
| `InstallSidecar` | class | InstallSidecar is a struct containing two optional String fields that store metadata about a sidecar's installation method and source URL. [crates/ghook/src/diagnose.rs:42-45] |
| `read_install_provenance` | function | This function reads and deserializes a JSON sidecar file from a specified directory, returning a tuple of optional installation method and source URL strings, or '(None, None)' if the read or deserialization operation fails. [crates/ghook/src/diagnose.rs:51-60] |
| `install_provenance_for_running_binary` | function | Attempts to read installation provenance metadata from the parent directory of the currently executing binary, returning a tuple of optional strings or (None, None) if directory resolution fails. [crates/ghook/src/diagnose.rs:62-70] |
| `diagnose` | function | # Summary The 'diagnose' function collects and returns diagnostic metadata about a git hook execution, including CLI configuration validation, daemon connectivity details, project identification, hook criticality status, and terminal context state. [crates/ghook/src/diagnose.rs:72-120] |
| `compile_v2_schema` | function | Compiles an embedded diagnose-output.v2 JSON schema (Draft 7) into a jsonschema::JSONSchema validator object. [crates/ghook/src/diagnose.rs:181-188] |
| `assert_validates` | function | This function validates a JSON value against a JSON schema and panics with formatted validation error messages if the value fails to conform to the schema. [crates/ghook/src/diagnose.rs:190-195] |

_Verified by 13 in-file unit tests._

