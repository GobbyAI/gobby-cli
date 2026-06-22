---
title: crates/gcode/src/setup/types.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/types.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Overview

`crates/gcode/src/setup/types.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gcode/src/setup/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Redacted` | class | A newtype wrapper around 'Option<String>' that encapsulates an optionally present redacted string value. [crates/gcode/src/setup/types.rs:5] |
| `Redacted::new` | method | Constructs a new instance by wrapping the provided 'Option<String>' directly in 'Self'. [crates/gcode/src/setup/types.rs:8-10] |
| `Redacted::as_deref` | method | Returns 'self.0' converted through 'AsDeref', yielding an 'Option<&str>' reference to the underlying string slice without cloning or allocating. [crates/gcode/src/setup/types.rs:12-14] |
| `Redacted::is_some` | method | Returns 'true' if the wrapped value is 'Some' and 'false' if it is 'None', by delegating to 'self.0.is_some()'. [crates/gcode/src/setup/types.rs:16-18] |
| `Redacted::clone_inner` | method | Returns a cloned 'Option<String>' of the struct’s inner value by calling 'clone' on 'self.0'. [crates/gcode/src/setup/types.rs:20-22] |
| `Redacted::from` | method | Constructs 'Self' by delegating to 'Self::new(value)' with the provided 'Option<String>'. [crates/gcode/src/setup/types.rs:26-28] |
| `Redacted::fmt` | method | Formats the value as '"<redacted>"' when the inner option is 'Some(_)', and as '"None"' when it is 'None'. [crates/gcode/src/setup/types.rs:32-37] |
| `StandaloneSetupRequest` | class | 'StandaloneSetupRequest' is a setup/provisioning request struct that configures standalone mode, service disabling, code-index overwriting, schema and embedding settings, and optional FalkorDB/Qdrant connection details while keeping sensitive setup-only credentials redacted and out of JSON serialization. [crates/gcode/src/setup/types.rs:41-66] |
| `StandaloneSetupRequest::new` | method | Constructs and returns a 'Self' configuration with 'standalone' set from the argument, 'database_url' wrapped in 'Redacted', 'schema' defaulting to 'DEFAULT_SCHEMA' when 'None', and all other fields initialized to their disabled/empty defaults. [crates/gcode/src/setup/types.rs:69-87] |
| `StandaloneServicesStatus` | class | 'StandaloneServicesStatus' tracks whether standalone services are provisioned, an optional compose file path, and a list of health-check identifiers. [crates/gcode/src/setup/types.rs:114-118] |
| `StandaloneEmbeddingStatus` | class | 'StandaloneEmbeddingStatus' is a status record for a standalone embedding provider configuration, capturing the provider name, API base URL, model identifier, optional query prefix, embedding vector dimension, and whether an API key is present along with an optional key fingerprint. [crates/gcode/src/setup/types.rs:121-129] |
| `StandaloneFailure` | class | 'StandaloneFailure' is a public Rust struct representing a standalone failure record with two owned string fields, 'name' and 'reason'. [crates/gcode/src/setup/types.rs:132-135] |
| `StandaloneSetupStatus` | class | 'StandaloneSetupStatus' records the outcome of a standalone setup run, including the target namespace and schema, lists of created/skipped/failed items, an optional config file path, and optional status details for services and embedding. [crates/gcode/src/setup/types.rs:138-147] |

_Verified by 1 in-file unit test._

