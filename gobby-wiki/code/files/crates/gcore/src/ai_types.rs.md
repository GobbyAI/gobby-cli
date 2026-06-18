---
title: crates/gcore/src/ai_types.rs
type: code_file
provenance:
- file: crates/gcore/src/ai_types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai_types.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai_types.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gcore/src/ai_types.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TranscriptionSegment` | class | Indexed class `TranscriptionSegment` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:9-13] |
| `TranscriptionResult` | class | Indexed class `TranscriptionResult` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:17-26] |
| `TranscriptionResult::from_wire_json` | method | Indexed method `TranscriptionResult::from_wire_json` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:29-33] |
| `VisionResult` | class | Indexed class `VisionResult` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:38-44] |
| `VisionResult::from_wire_json` | method | Indexed method `VisionResult::from_wire_json` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:47-50] |
| `TextResult` | class | Indexed class `TextResult` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:55-64] |
| `TokenUsage` | class | Indexed class `TokenUsage` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:67-74] |
| `TokenUsage::token_count` | method | Indexed method `TokenUsage::token_count` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:82-88] |
| `TextResult::from_wire_json` | method | Indexed method `TextResult::from_wire_json` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:92-95] |
| `AiError` | type | Indexed type `AiError` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:100-126] |
| `AiError::capability_unavailable` | method | Indexed method `AiError::capability_unavailable` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:129-137] |
| `AiError::not_configured` | method | Indexed method `AiError::not_configured` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:139-144] |
| `AiError::transport_failure` | method | Indexed method `AiError::transport_failure` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:146-156] |
| `AiError::rate_limited` | method | Indexed method `AiError::rate_limited` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:158-164] |
| `AiError::parse_failure` | method | Indexed method `AiError::parse_failure` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:166-170] |
| `AiError::status` | method | Indexed method `AiError::status` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:172-180] |
| `AiError::retry_after` | method | Indexed method `AiError::retry_after` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:182-190] |
| `AiError::fmt` | method | Indexed method `AiError::fmt` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:194-208] |
| `WireTranscriptionResult` | class | Indexed class `WireTranscriptionResult` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:214-231] |
| `WireTranscriptionSegment` | class | Indexed class `WireTranscriptionSegment` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:234-238] |
| `TranscriptionResult::Error` | type | Indexed type `TranscriptionResult::Error` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:241] |
| `TranscriptionResult::try_from` | method | Indexed method `TranscriptionResult::try_from` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:243-260] |
| `TranscriptionSegment::Error` | type | Indexed type `TranscriptionSegment::Error` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:264] |
| `TranscriptionSegment::try_from` | method | Indexed method `TranscriptionSegment::try_from` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:266-279] |
| `seconds_to_ms` | function | Indexed function `seconds_to_ms` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:282-295] |
| `duration_to_ms` | function | Indexed function `duration_to_ms` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:297-299] |
| `ai_error_is_transport_neutral` | function | Indexed function `ai_error_is_transport_neutral` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:306-313] |
| `token_usage_prefers_provider_total_over_component_sum` | function | Indexed function `token_usage_prefers_provider_total_over_component_sum` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:316-324] |
| `token_usage_sums_only_complete_component_counts` | function | Indexed function `token_usage_sums_only_complete_component_counts` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:327-341] |
| `transcription_wire_seconds_round_to_integer_milliseconds` | function | Indexed function `transcription_wire_seconds_round_to_integer_milliseconds` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:344-375] |
| `transcription_wire_seconds_reject_overflowing_milliseconds` | function | Indexed function `transcription_wire_seconds_reject_overflowing_milliseconds` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:378-389] |
| `transcription_wire_seconds_accept_negative_zero` | function | Indexed function `transcription_wire_seconds_accept_negative_zero` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:392-404] |
| `transcription_wire_seconds_reject_reversed_segments` | function | Indexed function `transcription_wire_seconds_reject_reversed_segments` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:407-419] |

