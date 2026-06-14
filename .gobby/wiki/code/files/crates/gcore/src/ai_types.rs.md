---
title: crates/gcore/src/ai_types.rs
type: code_file
provenance:
- file: crates/gcore/src/ai_types.rs
  ranges:
  - 9-13
  - 17-26
  - 28-34
  - 38-44
  - 46-51
  - 55-64
  - 67-74
  - 76-89
  - 91-96
  - 100-126
  - 128-191
  - 193-209
  - '211'
  - 214-231
  - 234-238
  - 240-261
  - 263-280
  - 282-295
  - 297-299
  - 306-313
  - 316-324
  - 327-341
  - 344-375
  - 378-389
  - 392-404
  - 407-419
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai_types.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Defines shared AI result and error types for gcore. It models normalized transcription output, vision analysis output, and text-generation output, plus token-usage accounting, and provides `from_wire_json` helpers to deserialize transport-specific JSON into these domain structs. The file also defines `AiError` constructors and accessors for capability, configuration, transport, rate-limit, HTTP-status, and parse failures, along with conversion helpers that normalize transcription segment timestamps from floating-point seconds into validated integer milliseconds.
[crates/gcore/src/ai_types.rs:9-13]
[crates/gcore/src/ai_types.rs:17-26]
[crates/gcore/src/ai_types.rs:28-34]
[crates/gcore/src/ai_types.rs:29-33]
[crates/gcore/src/ai_types.rs:38-44]

## API Symbols

- `TranscriptionSegment` (class) component `TranscriptionSegment [class]` (`767d119e-ef07-5ccb-8e0d-c2c3420d048e`) lines 9-13 [crates/gcore/src/ai_types.rs:9-13]
  - Signature: `pub struct TranscriptionSegment {`
  - Purpose: `TranscriptionSegment` is a struct that represents a transcribed text segment with millisecond-precision start and end timestamps. [crates/gcore/src/ai_types.rs:9-13]
- `TranscriptionResult` (class) component `TranscriptionResult [class]` (`57be7c5a-f027-55f2-ace4-659f8eca66d2`) lines 17-26 [crates/gcore/src/ai_types.rs:17-26]
  - Signature: `pub struct TranscriptionResult {`
  - Purpose: `TranscriptionResult` is a struct that encapsulates transcribed audio text with segment-level details and optional metadata including source/target language, model identifier, task type, and translation state. [crates/gcore/src/ai_types.rs:17-26]
- `TranscriptionResult` (class) component `TranscriptionResult [class]` (`c55c9a90-e096-5d32-98f6-39525fb17de0`) lines 28-34 [crates/gcore/src/ai_types.rs:28-34]
  - Signature: `impl TranscriptionResult {`
  - Purpose: **TranscriptionResult::from_wire_json deserializes a JSON value into an intermediate WireTranscriptionResult and converts it to Self via TryFrom, with serde errors mapped to AiError parse failures.** [crates/gcore/src/ai_types.rs:28-34]
- `TranscriptionResult.from_wire_json` (method) component `TranscriptionResult.from_wire_json [method]` (`85f039c8-555b-5bd6-8b01-9203aee145df`) lines 29-33 [crates/gcore/src/ai_types.rs:29-33]
  - Signature: `pub fn from_wire_json(value: serde_json::Value) -> Result<Self, AiError> {`
  - Purpose: Deserializes a JSON value into an intermediate `WireTranscriptionResult` wire type, maps deserialization errors to `AiError`, and performs a fallible `TryFrom` conversion to `Self`. [crates/gcore/src/ai_types.rs:29-33]
- `VisionResult` (class) component `VisionResult [class]` (`02e5bf90-4663-50f9-bda1-83a18d989422`) lines 38-44 [crates/gcore/src/ai_types.rs:38-44]
  - Signature: `pub struct VisionResult {`
  - Purpose: `VisionResult` is a serializable struct that encapsulates vision analysis output, containing a mandatory description, optional OCR text and model identifier, and a flexible metadata map. [crates/gcore/src/ai_types.rs:38-44]
- `VisionResult` (class) component `VisionResult [class]` (`e6ba5478-21f2-58db-9bfa-41fc851035b9`) lines 46-51 [crates/gcore/src/ai_types.rs:46-51]
  - Signature: `impl VisionResult {`
  - Purpose: `VisionResult` provides a `from_wire_json` factory method that deserializes a `serde_json::Value` into a `VisionResult` instance, mapping JSON parse failures to `AiError`. [crates/gcore/src/ai_types.rs:46-51]
- `VisionResult.from_wire_json` (method) component `VisionResult.from_wire_json [method]` (`d2c43d85-dc89-5183-98c6-aec5736c146c`) lines 47-50 [crates/gcore/src/ai_types.rs:47-50]
  - Signature: `pub fn from_wire_json(value: serde_json::Value) -> Result<Self, AiError> {`
  - Purpose: Deserializes a `serde_json::Value` into `Self` using serde deserialization, converting any JSON parse errors into `AiError::parse_failure`. [crates/gcore/src/ai_types.rs:47-50]
- `TextResult` (class) component `TextResult [class]` (`425bac43-5b8e-50d6-8947-9ee67e512bb5`) lines 55-64 [crates/gcore/src/ai_types.rs:55-64]
  - Signature: `pub struct TextResult {`
  - Purpose: TextResult is a serializable struct that encapsulates a text generation response, containing the generated text, an optional model identifier and token usage metrics, and provider-specific diagnostic metadata. [crates/gcore/src/ai_types.rs:55-64]
- `TokenUsage` (class) component `TokenUsage [class]` (`8bb157d4-4733-5140-b15c-321579a35a57`) lines 67-74 [crates/gcore/src/ai_types.rs:67-74]
  - Signature: `pub struct TokenUsage {`
  - Purpose: `TokenUsage` is a serializable struct that tracks token consumption across input, output, and total categories as optional unsigned integer fields. [crates/gcore/src/ai_types.rs:67-74]
- `TokenUsage` (class) component `TokenUsage [class]` (`f9782744-96f6-5338-9aa3-8844330c805c`) lines 76-89 [crates/gcore/src/ai_types.rs:76-89]
  - Signature: `impl TokenUsage {`
  - Purpose: `TokenUsage::token_count()` returns an `Option<usize>` representing the total token count, prioritizing the provider-reported total, falling back to the sum of input and output tokens when both are present, or `None` for incomplete metadata. [crates/gcore/src/ai_types.rs:76-89]
- `TokenUsage.token_count` (method) component `TokenUsage.token_count [method]` (`519bc810-46e1-54f4-8eea-0130b1e3a76a`) lines 82-88 [crates/gcore/src/ai_types.rs:82-88]
  - Signature: `pub fn token_count(&self) -> Option<usize> {`
  - Purpose: Returns the total token count if cached, otherwise computes it as the saturating sum of input and output tokens, or `None` if the latter pair are unavailable. [crates/gcore/src/ai_types.rs:82-88]
- `TextResult` (class) component `TextResult [class]` (`f4183060-d268-5580-ac69-cf104078d424`) lines 91-96 [crates/gcore/src/ai_types.rs:91-96]
  - Signature: `impl TextResult {`
  - Purpose: `TextResult` implements a `from_wire_json` deserialization method that converts a `serde_json::Value` into a `TextResult` instance, mapping JSON parse errors to `AiError::parse_failure`. [crates/gcore/src/ai_types.rs:91-96]
- `TextResult.from_wire_json` (method) component `TextResult.from_wire_json [method]` (`f1c1172a-b6ab-5e6e-994c-9c40b5346e95`) lines 92-95 [crates/gcore/src/ai_types.rs:92-95]
  - Signature: `pub fn from_wire_json(value: serde_json::Value) -> Result<Self, AiError> {`
  - Purpose: Deserializes a `serde_json::Value` into `Self`, mapping any JSON deserialization errors to `AiError::parse_failure`. [crates/gcore/src/ai_types.rs:92-95]
- `AiError` (type) component `AiError [type]` (`4efd76ec-58f5-53dc-a23f-8c0fdc00655b`) lines 100-126 [crates/gcore/src/ai_types.rs:100-126]
  - Signature: `pub enum AiError {`
  - Purpose: Indexed type `AiError` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:100-126]
- `AiError` (class) component `AiError [class]` (`b2e1a136-d17c-5f12-a2e4-b1a5d626afd3`) lines 128-191 [crates/gcore/src/ai_types.rs:128-191]
  - Signature: `impl AiError {`
  - Purpose: `AiError` impl provides factory methods for constructing five error variants (capability unavailable, not configured, transport failure, rate-limited, parse failure) and accessors to extract HTTP status codes and retry-after durations. [crates/gcore/src/ai_types.rs:128-191]
- `AiError.capability_unavailable` (method) component `AiError.capability_unavailable [method]` (`c6f7a28a-bccc-51c1-81ae-4b895f6424fe`) lines 129-137 [crates/gcore/src/ai_types.rs:129-137]
  - Signature: `pub fn capability_unavailable(`
  - Purpose: Constructs and returns a `CapabilityUnavailable` enum variant by converting the provided capability and message parameters into owned `String` instances. [crates/gcore/src/ai_types.rs:129-137]
- `AiError.not_configured` (method) component `AiError.not_configured [method]` (`b9d0d0d9-b63c-5882-848d-888cd548f373`) lines 139-144 [crates/gcore/src/ai_types.rs:139-144]
  - Signature: `pub fn not_configured(capability: Option<String>, message: impl Into<String>) -> Self {`
  - Purpose: # Summary

Constructs a `NotConfigured` enum variant with an optional capability identifier and a message parameter that is converted to `String` via the `Into` trait. [crates/gcore/src/ai_types.rs:139-144]
- `AiError.transport_failure` (method) component `AiError.transport_failure [method]` (`9befcacc-a788-5457-a9be-e95a6f5839c9`) lines 146-156 [crates/gcore/src/ai_types.rs:146-156]
  - Signature: `pub fn transport_failure(`
  - Purpose: Constructs a `TransportFailure` enum variant containing an optional HTTP status code, optional response body string, and a source string. [crates/gcore/src/ai_types.rs:146-156]
- `AiError.rate_limited` (method) component `AiError.rate_limited [method]` (`f36efb4d-7eb2-5b55-9150-836321e5c978`) lines 158-164 [crates/gcore/src/ai_types.rs:158-164]
  - Signature: `pub fn rate_limited(retry_after: Option<Duration>, body: Option<&str>) -> Self {`
  - Purpose: Constructs a `RateLimited` enum variant with HTTP 429 status code, converting an optional `Duration` to milliseconds and an optional string slice to an owned `String`. [crates/gcore/src/ai_types.rs:158-164]
- `AiError.parse_failure` (method) component `AiError.parse_failure [method]` (`fadd65c0-ae13-5807-8349-2a2801c3c1b0`) lines 166-170 [crates/gcore/src/ai_types.rs:166-170]
  - Signature: `pub fn parse_failure(source: impl Into<String>) -> Self {`
  - Purpose: Constructs and returns a `Self::ParseFailure` enum variant with the provided source converted to a `String`. [crates/gcore/src/ai_types.rs:166-170]
- `AiError.status` (method) component `AiError.status [method]` (`2d35c8e0-3ba5-5d77-a7c2-043070078e12`) lines 172-180 [crates/gcore/src/ai_types.rs:172-180]
  - Signature: `pub fn status(&self) -> Option<u16> {`
  - Purpose: This method extracts and returns the HTTP status code (u16) from error variants that contain one (TransportFailure, RateLimited, HttpStatus), or None for variants without a status field. [crates/gcore/src/ai_types.rs:172-180]
- `AiError.retry_after` (method) component `AiError.retry_after [method]` (`af34c24e-05c3-5d08-81c9-e532ffd88ed1`) lines 182-190 [crates/gcore/src/ai_types.rs:182-190]
  - Signature: `pub fn retry_after(&self) -> Option<Duration> {`
  - Purpose: Returns the retry-after duration as a `Duration` if `self` is a `RateLimited` variant with a defined `retry_after_ms` value, otherwise `None`. [crates/gcore/src/ai_types.rs:182-190]
- `AiError` (class) component `AiError [class]` (`fe414c8f-0bfc-5b1a-a3ff-4aa30a55468e`) lines 193-209 [crates/gcore/src/ai_types.rs:193-209]
  - Signature: `impl fmt::Display for AiError {`
  - Purpose: This Display trait implementation for AiError formats error messages across six failure modes: capability unavailability, misconfiguration, transport failures, rate limiting, HTTP status errors, and response parsing failures. [crates/gcore/src/ai_types.rs:193-209]
- `AiError.fmt` (method) component `AiError.fmt [method]` (`aaececef-a938-551b-a7e0-0659504380c2`) lines 194-208 [crates/gcore/src/ai_types.rs:194-208]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: # Summary

Implements the Display trait by pattern-matching on error enum variants to format human-readable diagnostic messages for AI-related failures into the provided Formatter. [crates/gcore/src/ai_types.rs:194-208]
- `AiError` (class) component `AiError [class]` (`0d66a852-00f2-5126-b9bf-9ae6d278bd0d`) lines 211-211 [crates/gcore/src/ai_types.rs:211]
  - Signature: `impl std::error::Error for AiError {}`
  - Purpose: AiError implements Rust's `std::error::Error` trait as a custom error type with default trait method implementations. [crates/gcore/src/ai_types.rs:211]
- `WireTranscriptionResult` (class) component `WireTranscriptionResult [class]` (`5fcc92da-0578-5689-86ac-93a107ba9aac`) lines 214-231 [crates/gcore/src/ai_types.rs:214-231]
  - Signature: `struct WireTranscriptionResult {`
  - Purpose: `WireTranscriptionResult` is a serde-serializable struct representing audio transcription output, containing segmented text, source/target language metadata, model information, and translation state. [crates/gcore/src/ai_types.rs:214-231]
- `WireTranscriptionSegment` (class) component `WireTranscriptionSegment [class]` (`d09ffb0a-4a4c-5f56-af51-c46401b72e94`) lines 234-238 [crates/gcore/src/ai_types.rs:234-238]
  - Signature: `struct WireTranscriptionSegment {`
  - Purpose: `WireTranscriptionSegment` is a struct that represents a time-bounded transcription segment, pairing a text string with floating-point start and end timestamps. [crates/gcore/src/ai_types.rs:234-238]
- `TranscriptionResult` (class) component `TranscriptionResult [class]` (`d6b96fb3-c10f-56b3-8ba2-0a045a23932a`) lines 240-261 [crates/gcore/src/ai_types.rs:240-261]
  - Signature: `impl TryFrom<WireTranscriptionResult> for TranscriptionResult {`
  - Purpose: Implements `TryFrom` to convert a wire protocol `TranscriptionResult` to a domain model by applying fallible `TranscriptionSegment` conversion to each segment and propagating errors via the `?` operator. [crates/gcore/src/ai_types.rs:240-261]
- `TranscriptionResult.Error` (type) component `TranscriptionResult.Error [type]` (`efd674b1-38b9-5b80-b986-0875efcadf98`) lines 241-241 [crates/gcore/src/ai_types.rs:241]
  - Signature: `type Error = AiError;`
  - Purpose: Indexed type `TranscriptionResult.Error` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:241]
- `TranscriptionResult.try_from` (method) component `TranscriptionResult.try_from [method]` (`610a4538-1324-5f66-9ce5-892278f6f8f2`) lines 243-260 [crates/gcore/src/ai_types.rs:243-260]
  - Signature: `fn try_from(value: WireTranscriptionResult) -> Result<Self, Self::Error> {`
  - Purpose: Implements `TryFrom<WireTranscriptionResult>` by transforming each segment through `TranscriptionSegment::try_from` and propagating conversion errors while preserving other fields. [crates/gcore/src/ai_types.rs:243-260]
- `TranscriptionSegment` (class) component `TranscriptionSegment [class]` (`d4e3f3f0-a3de-5e0e-b1e4-409559260409`) lines 263-280 [crates/gcore/src/ai_types.rs:263-280]
  - Signature: `impl TryFrom<WireTranscriptionSegment> for TranscriptionSegment {`
  - Purpose: Implements fallible conversion from `WireTranscriptionSegment` to `TranscriptionSegment`, converting start and end times from seconds to milliseconds and validating that the end timestamp does not precede the start timestamp. [crates/gcore/src/ai_types.rs:263-280]
- `TranscriptionSegment.Error` (type) component `TranscriptionSegment.Error [type]` (`dbbb70ea-87b8-55ab-af23-6fd337281af8`) lines 264-264 [crates/gcore/src/ai_types.rs:264]
  - Signature: `type Error = AiError;`
  - Purpose: Indexed type `TranscriptionSegment.Error` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:264]
- `TranscriptionSegment.try_from` (method) component `TranscriptionSegment.try_from [method]` (`a7df87ec-e91f-56c8-840d-43dc5ce7e096`) lines 266-279 [crates/gcore/src/ai_types.rs:266-279]
  - Signature: `fn try_from(value: WireTranscriptionSegment) -> Result<Self, Self::Error> {`
  - Purpose: This method implements `TryFrom` to convert a `WireTranscriptionSegment` into Self by converting start and end times from seconds to milliseconds and validating that the end time does not precede the start time. [crates/gcore/src/ai_types.rs:266-279]
- `seconds_to_ms` (function) component `seconds_to_ms [function]` (`7827e238-c2bc-512c-92dd-5ed2abc9f2ca`) lines 282-295 [crates/gcore/src/ai_types.rs:282-295]
  - Signature: `fn seconds_to_ms(seconds: f64) -> Result<u64, AiError> {`
  - Purpose: Converts a non-negative finite floating-point seconds value to milliseconds as a `u64`, validating against overflow and returning an `AiError` on invalid input. [crates/gcore/src/ai_types.rs:282-295]
- `duration_to_ms` (function) component `duration_to_ms [function]` (`934fee25-60ac-5048-8647-330a3ece0252`) lines 297-299 [crates/gcore/src/ai_types.rs:297-299]
  - Signature: `fn duration_to_ms(duration: Duration) -> u64 {`
  - Purpose: Converts a Duration to milliseconds as a u64, saturating any overflow at u64::MAX. [crates/gcore/src/ai_types.rs:297-299]
- `ai_error_is_transport_neutral` (function) component `ai_error_is_transport_neutral [function]` (`8897a8b8-99ef-5349-8383-7c57a9c15212`) lines 306-313 [crates/gcore/src/ai_types.rs:306-313]
  - Signature: `fn ai_error_is_transport_neutral() {`
  - Purpose: This test verifies that `AiError::transport_failure` produces a debug representation that excludes HTTP client library identifiers (reqwest/ureq), ensuring the error abstraction remains transport-neutral. [crates/gcore/src/ai_types.rs:306-313]
- `token_usage_prefers_provider_total_over_component_sum` (function) component `token_usage_prefers_provider_total_over_component_sum [function]` (`27b1e3b2-01f6-54b4-8843-d91977acab6b`) lines 316-324 [crates/gcore/src/ai_types.rs:316-324]
  - Signature: `fn token_usage_prefers_provider_total_over_component_sum() {`
  - Purpose: Unit test asserting that `TokenUsage::token_count()` returns the explicit `total_tokens` field value instead of computing the sum of `input_tokens` and `output_tokens` components. [crates/gcore/src/ai_types.rs:316-324]
- `token_usage_sums_only_complete_component_counts` (function) component `token_usage_sums_only_complete_component_counts [function]` (`47acf927-699c-5a4b-9f1b-3bb3f648f99f`) lines 327-341 [crates/gcore/src/ai_types.rs:327-341]
  - Signature: `fn token_usage_sums_only_complete_component_counts() {`
  - Purpose: This function tests that the `token_count()` method returns the sum of input and output tokens only when both components are present, otherwise returning `None`. [crates/gcore/src/ai_types.rs:327-341]
- `transcription_wire_seconds_round_to_integer_milliseconds` (function) component `transcription_wire_seconds_round_to_integer_milliseconds [function]` (`3eb546a9-9b58-57aa-9246-b3e1e51da162`) lines 344-375 [crates/gcore/src/ai_types.rs:344-375]
  - Signature: `fn transcription_wire_seconds_round_to_integer_milliseconds() {`
  - Purpose: # Summary

This is a unit test that validates `TranscriptionResult::from_wire_json()` correctly converts and rounds segment timestamps from floating-point seconds to integer milliseconds. [crates/gcore/src/ai_types.rs:344-375]
- `transcription_wire_seconds_reject_overflowing_milliseconds` (function) component `transcription_wire_seconds_reject_overflowing_milliseconds [function]` (`3e2e5e6b-ceab-58e3-b867-2c38e5a961fd`) lines 378-389 [crates/gcore/src/ai_types.rs:378-389]
  - Signature: `fn transcription_wire_seconds_reject_overflowing_milliseconds() {`
  - Purpose: Verifies that `TranscriptionResult::from_wire_json` rejects transcription segments whose end times overflow when converting from seconds to milliseconds. [crates/gcore/src/ai_types.rs:378-389]
- `transcription_wire_seconds_accept_negative_zero` (function) component `transcription_wire_seconds_accept_negative_zero [function]` (`77c3c182-537d-5b19-a5f5-81dae984c8bf`) lines 392-404 [crates/gcore/src/ai_types.rs:392-404]
  - Signature: `fn transcription_wire_seconds_accept_negative_zero() {`
  - Purpose: This test verifies that `TranscriptionResult::from_wire_json()` normalizes negative zero (-0.0) segment timings to zero milliseconds during deserialization. [crates/gcore/src/ai_types.rs:392-404]
- `transcription_wire_seconds_reject_reversed_segments` (function) component `transcription_wire_seconds_reject_reversed_segments [function]` (`ea46ff6d-88d1-57ed-ac15-5fba2d00a593`) lines 407-419 [crates/gcore/src/ai_types.rs:407-419]
  - Signature: `fn transcription_wire_seconds_reject_reversed_segments() {`
  - Purpose: Verifies that `TranscriptionResult::from_wire_json()` rejects transcription segments with reversed time intervals where the end time precedes the start time. [crates/gcore/src/ai_types.rs:407-419]

