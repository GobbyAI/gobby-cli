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

`crates/gcore/src/degradation.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ServiceState` | type | Indexed type `ServiceState` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:12-22] |
| `ServiceState::is_available` | method | Indexed method `ServiceState::is_available` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:26-28] |
| `SetupIssue` | class | Indexed class `SetupIssue` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:33-40] |
| `Guidance` | class | Indexed class `Guidance` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:46-53] |
| `CoreError` | type | Indexed type `CoreError` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:57-91] |
| `serialize_redacted_database_url` | function | Indexed function `serialize_redacted_database_url` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:93-98] |
| `redact_database_url` | function | Indexed function `redact_database_url` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:100-115] |
| `redact_keyword_database_url` | function | Indexed function `redact_keyword_database_url` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:117-132] |
| `is_sensitive_keyword_dsn_key` | function | Indexed function `is_sensitive_keyword_dsn_key` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:134-139] |
| `ModalityDegradationReason` | type | Indexed type `ModalityDegradationReason` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:150-171] |
| `ModalityDegradationReason::as_str` | method | Indexed method `ModalityDegradationReason::as_str` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:175-188] |
| `ModalityDegradationReason::fmt` | method | Indexed method `ModalityDegradationReason::fmt` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:192-194] |
| `DegradationKind` | type | Indexed type `DegradationKind` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:199-233] |
| `modality_reason_markers_match_serde_names` | function | Indexed function `modality_reason_markers_match_serde_names` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:240-261] |
| `service_unavailable_degradation_is_not_fatal` | function | Indexed function `service_unavailable_degradation_is_not_fatal` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:264-293] |
| `guidance_is_structured` | function | Indexed function `guidance_is_structured` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:296-309] |
| `core_error_serialization_roundtrip` | function | Indexed function `core_error_serialization_roundtrip` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:312-354] |
| `hub_conflict_display_and_json_redact_database_urls` | function | Indexed function `hub_conflict_display_and_json_redact_database_urls` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:357-382] |
| `keyword_database_url_redacts_sensitive_values_case_insensitively` | function | Indexed function `keyword_database_url_redacts_sensitive_values_case_insensitively` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:385-397] |
| `hub_conflict_json_redacts_keyword_database_urls` | function | Indexed function `hub_conflict_json_redacts_keyword_database_urls` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:400-417] |

