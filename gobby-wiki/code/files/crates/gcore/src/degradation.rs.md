---
title: crates/gcore/src/degradation.rs
type: code_file
provenance:
- file: crates/gcore/src/degradation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/degradation.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/degradation.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gcore/src/degradation.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ServiceState` | type | Indexed type `ServiceState` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:12-22] |
| `ServiceState::is_available` | method | Returns 'true' if 'self' is the 'Self::Available' variant, and 'false' otherwise. [crates/gcore/src/degradation.rs:26-28] |
| `SetupIssue` | class | The 'SetupIssue' struct represents a degraded, invalid, or missing resource by encapsulating its name, its owning service or store, and structured remediation guidance for the caller to render. [crates/gcore/src/degradation.rs:33-40] |
| `Guidance` | class | The 'Guidance' struct represents structured diagnostic feedback containing a description of an issue, a recommended action for resolution, and an optional command hint suggestion. [crates/gcore/src/degradation.rs:46-53] |
| `CoreError` | type | Indexed type `CoreError` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:57-91] |
| `serialize_redacted_database_url` | function | Serializes a database URL as a redacted string by applying 'redact_database_url' and emitting the result through the provided 'serde::Serializer'. [crates/gcore/src/degradation.rs:93-98] |
| `redact_database_url` | function | Returns a database URL with any '#fragment' and '?query' removed, strips userinfo before '@' when the URL contains '://', and otherwise delegates to 'redact_keyword_database_url' for non-scheme-based URLs. [crates/gcore/src/degradation.rs:100-115] |
| `redact_keyword_database_url` | function | The 'redact_keyword_database_url' function parses a keyword-based database connection string into key-value tokens, redacts the values of any sensitive keys by replacing them with '<redacted>', and joins them back into a space-separated string. [crates/gcore/src/degradation.rs:117-132] |
| `is_sensitive_keyword_dsn_key` | function | The function 'is_sensitive_keyword_dsn_key' checks whether a case-insensitive string slice matches "password", "passfile", or "sslpassword", returning 'true' if it is a match and 'false' otherwise. [crates/gcore/src/degradation.rs:134-139] |
| `ModalityDegradationReason` | type | Indexed type `ModalityDegradationReason` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:150-171] |
| `ModalityDegradationReason::as_str` | method | Returns a ''static' string slice naming the enum variant by matching 'self' to its corresponding lowercase, underscore-separated status identifier. [crates/gcore/src/degradation.rs:175-188] |
| `ModalityDegradationReason::fmt` | method | Formats the type by writing the string slice returned by 'self.as_str()' directly to the provided formatter. [crates/gcore/src/degradation.rs:192-194] |
| `DegradationKind` | type | Indexed type `DegradationKind` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:199-233] |

_Verified by 7 in-file unit tests._

