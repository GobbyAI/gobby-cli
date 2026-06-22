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

`crates/gcore/src/ai_types.rs` exposes 34 indexed API symbols.

## How it fits

`crates/gcore/src/ai_types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TranscriptionSegment` | class | 'TranscriptionSegment' is a data structure representing a time-bounded transcription span, with 'start_ms' and 'end_ms' timestamps in milliseconds and the associated transcribed 'text'. [crates/gcore/src/ai_types.rs:9-13] |
| `TranscriptionResult` | class | 'TranscriptionResult' is a struct that represents the output of a transcription or translation job, containing the full text, per-segment results, optional source and target language metadata, optional model and task identifiers, and a boolean indicating whether the text was translated. [crates/gcore/src/ai_types.rs:17-26] |
| `TranscriptionResult::from_wire_json` | method | Deserializes a 'serde_json::Value' into 'WireTranscriptionResult', maps any deserialization error to 'AiError::parse_failure', and then converts the wire type into 'Self' via 'TryFrom', returning 'Result<Self, AiError>'. [crates/gcore/src/ai_types.rs:29-33] |
| `VisionResult` | class | 'VisionResult' is a serializable Rust struct that stores a vision model’s textual description, optional OCR text, optional model identifier, and an arbitrary string-to-string metadata map. [crates/gcore/src/ai_types.rs:38-44] |
| `VisionResult::from_wire_json` | method | Deserializes the given 'serde_json::Value' into 'Self' with 'serde_json::from_value', returning 'Ok(Self)' on success or 'Err(AiError::parse_failure(error.to_string()))' if parsing fails. [crates/gcore/src/ai_types.rs:47-50] |
| `TextResult` | class | The 'TextResult' struct represents a model's generated text response, containing optional fields for the model identifier, applied reasoning effort, token usage, and arbitrary provider-specific diagnostic metadata stored in a key-value map. [crates/gcore/src/ai_types.rs:55-66] |
| `TokenUsage` | class | The 'TokenUsage' struct represents model token metrics using optional, unsigned-integer fields for input, output, and total tokens, configured with Serde attributes to default to 'None' and skip serialization when absent. [crates/gcore/src/ai_types.rs:69-76] |
| `TokenUsage::token_count` | method | The 'token_count' method returns the pre-computed total token count if available, or alternatively, the saturating sum of the input and output token counts if both are present. [crates/gcore/src/ai_types.rs:84-90] |
| `TextResult::from_wire_json` | method | The 'from_wire_json' method deserializes a 'serde_json::Value' into an instance of 'Self', mapping any deserialization errors to an 'AiError::parse_failure'. [crates/gcore/src/ai_types.rs:94-97] |
| `AiError` | type | Indexed type `AiError` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:102-128] |
| `AiError::capability_unavailable` | method | Constructs a 'Self::CapabilityUnavailable' enum variant by converting and encapsulating the provided capability and message parameters into owned 'String' fields. [crates/gcore/src/ai_types.rs:131-139] |
| `AiError::not_configured` | method | The 'not_configured' function is a public constructor that instantiates and returns the 'Self::NotConfigured' variant, initializing its fields with an optional capability string and a converted message string. [crates/gcore/src/ai_types.rs:141-146] |
| `AiError::transport_failure` | method | The 'transport_failure' method constructs and returns a 'Self::TransportFailure' enum variant, initializing it with an optional 'u16' status code, an optional response body converted to an owned 'String', and a source identifier converted into a 'String'. [crates/gcore/src/ai_types.rs:148-158] |
| `AiError::rate_limited` | method | This method constructs and returns a 'Self::RateLimited' enum variant with an HTTP 429 status code, mapping an optional 'Duration' into milliseconds and an optional string slice into an owned 'String'. [crates/gcore/src/ai_types.rs:160-166] |
| `AiError::parse_failure` | method | The 'parse_failure' associated function constructs and returns a 'Self' enum instance of the 'ParseFailure' variant by converting the provided 'source' parameter into a 'String'. [crates/gcore/src/ai_types.rs:168-172] |
| `AiError::status` | method | The 'status' method returns the HTTP or transport status code as an 'Option<u16>' extracted from the 'TransportFailure', 'RateLimited', or 'HttpStatus' variants, and returns 'None' for capability, configuration, or parsing failures. [crates/gcore/src/ai_types.rs:174-182] |
| `AiError::retry_after` | method | The 'retry_after' method returns 'Some(Duration)' representing the retry delay if the instance is the 'RateLimited' variant and contains a millisecond value, otherwise it returns 'None'. [crates/gcore/src/ai_types.rs:184-192] |
| `AiError::fmt` | method | This method implements string formatting for an error enum by pattern matching its variants—representing various AI capability, transport, status, and parsing failures—and writing a descriptive, structured error message to the formatter. [crates/gcore/src/ai_types.rs:196-210] |
| `WireTranscriptionResult` | class | 'WireTranscriptionResult' is a deserializable Rust struct representing a transcription output payload, containing the transcribed text, segments, model and task metadata, source and target language specifications, and a translation status flag, with all fields defaulting upon deserialization. [crates/gcore/src/ai_types.rs:216-233] |
| `WireTranscriptionSegment` | class | The 'WireTranscriptionSegment' structure represents a serialized transcription segment containing floating-point start and end timestamps and the associated transcribed text string. [crates/gcore/src/ai_types.rs:236-240] |
| `TranscriptionResult::Error` | type | Indexed type `TranscriptionResult::Error` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:243] |
| `TranscriptionResult::try_from` | method | This method fallibly converts a 'WireTranscriptionResult' into the implementing type by mapping and collecting its segments into a vector of 'TranscriptionSegment' instances while directly propagating all other fields. [crates/gcore/src/ai_types.rs:245-262] |
| `TranscriptionSegment::Error` | type | Indexed type `TranscriptionSegment::Error` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:266] |
| `TranscriptionSegment::try_from` | method | This method attempts to convert a 'WireTranscriptionSegment' into 'Self' by converting its start and end times from seconds to milliseconds, validating that the end time does not precede the start time, and returning either the constructed instance or a parse failure error. [crates/gcore/src/ai_types.rs:268-281] |

_2 more symbol(s) not shown — run `gcode outline crates/gcore/src/ai_types.rs` for the full list._

_Verified by 8 in-file unit tests._

