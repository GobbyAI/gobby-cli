---
title: crates/gcore/src/ai_types.rs
type: code_file
provenance:
- file: crates/gcore/src/ai_types.rs
  ranges:
  - 9-13
  - 17-26
  - 29-33
  - 38-44
  - 47-50
  - 55-64
  - 67-74
  - 82-88
  - 92-95
  - 100-126
  - 129-137
  - 139-144
  - 146-156
  - 158-164
  - 166-170
  - 172-180
  - 182-190
  - 194-208
  - 214-231
  - 234-238
  - '241'
  - 243-260
  - '264'
  - 266-279
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai_types.rs:9-13](crates/gcore/src/ai_types.rs#L9-L13), [crates/gcore/src/ai_types.rs:17-26](crates/gcore/src/ai_types.rs#L17-L26), [crates/gcore/src/ai_types.rs:29-33](crates/gcore/src/ai_types.rs#L29-L33), [crates/gcore/src/ai_types.rs:38-44](crates/gcore/src/ai_types.rs#L38-L44), [crates/gcore/src/ai_types.rs:47-50](crates/gcore/src/ai_types.rs#L47-L50), [crates/gcore/src/ai_types.rs:55-64](crates/gcore/src/ai_types.rs#L55-L64), [crates/gcore/src/ai_types.rs:67-74](crates/gcore/src/ai_types.rs#L67-L74), [crates/gcore/src/ai_types.rs:82-88](crates/gcore/src/ai_types.rs#L82-L88), [crates/gcore/src/ai_types.rs:92-95](crates/gcore/src/ai_types.rs#L92-L95), [crates/gcore/src/ai_types.rs:100-126](crates/gcore/src/ai_types.rs#L100-L126), [crates/gcore/src/ai_types.rs:129-137](crates/gcore/src/ai_types.rs#L129-L137), [crates/gcore/src/ai_types.rs:139-144](crates/gcore/src/ai_types.rs#L139-L144), [crates/gcore/src/ai_types.rs:146-156](crates/gcore/src/ai_types.rs#L146-L156), [crates/gcore/src/ai_types.rs:158-164](crates/gcore/src/ai_types.rs#L158-L164), [crates/gcore/src/ai_types.rs:166-170](crates/gcore/src/ai_types.rs#L166-L170), [crates/gcore/src/ai_types.rs:172-180](crates/gcore/src/ai_types.rs#L172-L180), [crates/gcore/src/ai_types.rs:182-190](crates/gcore/src/ai_types.rs#L182-L190), [crates/gcore/src/ai_types.rs:194-208](crates/gcore/src/ai_types.rs#L194-L208), [crates/gcore/src/ai_types.rs:214-231](crates/gcore/src/ai_types.rs#L214-L231), [crates/gcore/src/ai_types.rs:234-238](crates/gcore/src/ai_types.rs#L234-L238), [crates/gcore/src/ai_types.rs:241](crates/gcore/src/ai_types.rs#L241), [crates/gcore/src/ai_types.rs:243-260](crates/gcore/src/ai_types.rs#L243-L260), [crates/gcore/src/ai_types.rs:264](crates/gcore/src/ai_types.rs#L264), [crates/gcore/src/ai_types.rs:266-279](crates/gcore/src/ai_types.rs#L266-L279), [crates/gcore/src/ai_types.rs:282-295](crates/gcore/src/ai_types.rs#L282-L295), [crates/gcore/src/ai_types.rs:297-299](crates/gcore/src/ai_types.rs#L297-L299), [crates/gcore/src/ai_types.rs:306-313](crates/gcore/src/ai_types.rs#L306-L313), [crates/gcore/src/ai_types.rs:316-324](crates/gcore/src/ai_types.rs#L316-L324), [crates/gcore/src/ai_types.rs:327-341](crates/gcore/src/ai_types.rs#L327-L341), [crates/gcore/src/ai_types.rs:344-375](crates/gcore/src/ai_types.rs#L344-L375), [crates/gcore/src/ai_types.rs:378-389](crates/gcore/src/ai_types.rs#L378-L389), [crates/gcore/src/ai_types.rs:392-404](crates/gcore/src/ai_types.rs#L392-L404), [crates/gcore/src/ai_types.rs:407-419](crates/gcore/src/ai_types.rs#L407-L419)

</details>

# crates/gcore/src/ai_types.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Defines the shared AI response types and conversion logic for `gcore`: normalized transcription segments/results, vision extraction results, text-generation results, token usage, and a structured `AiError`. The file ties the pieces together with `from_wire_json` and `TryFrom` adapters that parse transport-specific wire JSON into the internal types, plus helper functions for time conversion, token accounting, and error classification/validation so different AI backends can be handled through one consistent schema.
[crates/gcore/src/ai_types.rs:9-13]
[crates/gcore/src/ai_types.rs:17-26]
[crates/gcore/src/ai_types.rs:29-33]
[crates/gcore/src/ai_types.rs:38-44]
[crates/gcore/src/ai_types.rs:47-50]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `TranscriptionSegment` | class | `pub struct TranscriptionSegment {` | `TranscriptionSegment [class]` | `767d119e-ef07-5ccb-8e0d-c2c3420d048e` | 9-13 [crates/gcore/src/ai_types.rs:9-13] | Indexed class `TranscriptionSegment` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:9-13] |
| `TranscriptionResult` | class | `pub struct TranscriptionResult {` | `TranscriptionResult [class]` | `57be7c5a-f027-55f2-ace4-659f8eca66d2` | 17-26 [crates/gcore/src/ai_types.rs:17-26] | Indexed class `TranscriptionResult` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:17-26] |
| `TranscriptionResult::from_wire_json` | method | `pub fn from_wire_json(value: serde_json::Value) -> Result<Self, AiError> {` | `TranscriptionResult::from_wire_json [method]` | `85f039c8-555b-5bd6-8b01-9203aee145df` | 29-33 [crates/gcore/src/ai_types.rs:29-33] | Indexed method `TranscriptionResult::from_wire_json` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:29-33] |
| `VisionResult` | class | `pub struct VisionResult {` | `VisionResult [class]` | `02e5bf90-4663-50f9-bda1-83a18d989422` | 38-44 [crates/gcore/src/ai_types.rs:38-44] | Indexed class `VisionResult` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:38-44] |
| `VisionResult::from_wire_json` | method | `pub fn from_wire_json(value: serde_json::Value) -> Result<Self, AiError> {` | `VisionResult::from_wire_json [method]` | `d2c43d85-dc89-5183-98c6-aec5736c146c` | 47-50 [crates/gcore/src/ai_types.rs:47-50] | Indexed method `VisionResult::from_wire_json` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:47-50] |
| `TextResult` | class | `pub struct TextResult {` | `TextResult [class]` | `425bac43-5b8e-50d6-8947-9ee67e512bb5` | 55-64 [crates/gcore/src/ai_types.rs:55-64] | Indexed class `TextResult` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:55-64] |
| `TokenUsage` | class | `pub struct TokenUsage {` | `TokenUsage [class]` | `8bb157d4-4733-5140-b15c-321579a35a57` | 67-74 [crates/gcore/src/ai_types.rs:67-74] | Indexed class `TokenUsage` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:67-74] |
| `TokenUsage::token_count` | method | `pub fn token_count(&self) -> Option<usize> {` | `TokenUsage::token_count [method]` | `519bc810-46e1-54f4-8eea-0130b1e3a76a` | 82-88 [crates/gcore/src/ai_types.rs:82-88] | Indexed method `TokenUsage::token_count` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:82-88] |
| `TextResult::from_wire_json` | method | `pub fn from_wire_json(value: serde_json::Value) -> Result<Self, AiError> {` | `TextResult::from_wire_json [method]` | `f1c1172a-b6ab-5e6e-994c-9c40b5346e95` | 92-95 [crates/gcore/src/ai_types.rs:92-95] | Indexed method `TextResult::from_wire_json` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:92-95] |
| `AiError` | type | `pub enum AiError {` | `AiError [type]` | `4efd76ec-58f5-53dc-a23f-8c0fdc00655b` | 100-126 [crates/gcore/src/ai_types.rs:100-126] | Indexed type `AiError` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:100-126] |
| `AiError::capability_unavailable` | method | `pub fn capability_unavailable(` | `AiError::capability_unavailable [method]` | `c6f7a28a-bccc-51c1-81ae-4b895f6424fe` | 129-137 [crates/gcore/src/ai_types.rs:129-137] | Indexed method `AiError::capability_unavailable` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:129-137] |
| `AiError::not_configured` | method | `pub fn not_configured(capability: Option<String>, message: impl Into<String>) -> Self {` | `AiError::not_configured [method]` | `b9d0d0d9-b63c-5882-848d-888cd548f373` | 139-144 [crates/gcore/src/ai_types.rs:139-144] | Indexed method `AiError::not_configured` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:139-144] |
| `AiError::transport_failure` | method | `pub fn transport_failure(` | `AiError::transport_failure [method]` | `9befcacc-a788-5457-a9be-e95a6f5839c9` | 146-156 [crates/gcore/src/ai_types.rs:146-156] | Indexed method `AiError::transport_failure` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:146-156] |
| `AiError::rate_limited` | method | `pub fn rate_limited(retry_after: Option<Duration>, body: Option<&str>) -> Self {` | `AiError::rate_limited [method]` | `f36efb4d-7eb2-5b55-9150-836321e5c978` | 158-164 [crates/gcore/src/ai_types.rs:158-164] | Indexed method `AiError::rate_limited` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:158-164] |
| `AiError::parse_failure` | method | `pub fn parse_failure(source: impl Into<String>) -> Self {` | `AiError::parse_failure [method]` | `fadd65c0-ae13-5807-8349-2a2801c3c1b0` | 166-170 [crates/gcore/src/ai_types.rs:166-170] | Indexed method `AiError::parse_failure` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:166-170] |
| `AiError::status` | method | `pub fn status(&self) -> Option<u16> {` | `AiError::status [method]` | `2d35c8e0-3ba5-5d77-a7c2-043070078e12` | 172-180 [crates/gcore/src/ai_types.rs:172-180] | Indexed method `AiError::status` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:172-180] |
| `AiError::retry_after` | method | `pub fn retry_after(&self) -> Option<Duration> {` | `AiError::retry_after [method]` | `af34c24e-05c3-5d08-81c9-e532ffd88ed1` | 182-190 [crates/gcore/src/ai_types.rs:182-190] | Indexed method `AiError::retry_after` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:182-190] |
| `AiError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `AiError::fmt [method]` | `aaececef-a938-551b-a7e0-0659504380c2` | 194-208 [crates/gcore/src/ai_types.rs:194-208] | Indexed method `AiError::fmt` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:194-208] |
| `WireTranscriptionResult` | class | `struct WireTranscriptionResult {` | `WireTranscriptionResult [class]` | `5fcc92da-0578-5689-86ac-93a107ba9aac` | 214-231 [crates/gcore/src/ai_types.rs:214-231] | Indexed class `WireTranscriptionResult` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:214-231] |
| `WireTranscriptionSegment` | class | `struct WireTranscriptionSegment {` | `WireTranscriptionSegment [class]` | `d09ffb0a-4a4c-5f56-af51-c46401b72e94` | 234-238 [crates/gcore/src/ai_types.rs:234-238] | Indexed class `WireTranscriptionSegment` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:234-238] |
| `TranscriptionResult::Error` | type | `type Error = AiError;` | `TranscriptionResult::Error [type]` | `efd674b1-38b9-5b80-b986-0875efcadf98` | 241-241 [crates/gcore/src/ai_types.rs:241] | Indexed type `TranscriptionResult::Error` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:241] |
| `TranscriptionResult::try_from` | method | `fn try_from(value: WireTranscriptionResult) -> Result<Self, Self::Error> {` | `TranscriptionResult::try_from [method]` | `610a4538-1324-5f66-9ce5-892278f6f8f2` | 243-260 [crates/gcore/src/ai_types.rs:243-260] | Indexed method `TranscriptionResult::try_from` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:243-260] |
| `TranscriptionSegment::Error` | type | `type Error = AiError;` | `TranscriptionSegment::Error [type]` | `dbbb70ea-87b8-55ab-af23-6fd337281af8` | 264-264 [crates/gcore/src/ai_types.rs:264] | Indexed type `TranscriptionSegment::Error` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:264] |
| `TranscriptionSegment::try_from` | method | `fn try_from(value: WireTranscriptionSegment) -> Result<Self, Self::Error> {` | `TranscriptionSegment::try_from [method]` | `a7df87ec-e91f-56c8-840d-43dc5ce7e096` | 266-279 [crates/gcore/src/ai_types.rs:266-279] | Indexed method `TranscriptionSegment::try_from` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:266-279] |
| `seconds_to_ms` | function | `fn seconds_to_ms(seconds: f64) -> Result<u64, AiError> {` | `seconds_to_ms [function]` | `7827e238-c2bc-512c-92dd-5ed2abc9f2ca` | 282-295 [crates/gcore/src/ai_types.rs:282-295] | Indexed function `seconds_to_ms` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:282-295] |
| `duration_to_ms` | function | `fn duration_to_ms(duration: Duration) -> u64 {` | `duration_to_ms [function]` | `934fee25-60ac-5048-8647-330a3ece0252` | 297-299 [crates/gcore/src/ai_types.rs:297-299] | Indexed function `duration_to_ms` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:297-299] |
| `ai_error_is_transport_neutral` | function | `fn ai_error_is_transport_neutral() {` | `ai_error_is_transport_neutral [function]` | `8897a8b8-99ef-5349-8383-7c57a9c15212` | 306-313 [crates/gcore/src/ai_types.rs:306-313] | Indexed function `ai_error_is_transport_neutral` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:306-313] |
| `token_usage_prefers_provider_total_over_component_sum` | function | `fn token_usage_prefers_provider_total_over_component_sum() {` | `token_usage_prefers_provider_total_over_component_sum [function]` | `27b1e3b2-01f6-54b4-8843-d91977acab6b` | 316-324 [crates/gcore/src/ai_types.rs:316-324] | Indexed function `token_usage_prefers_provider_total_over_component_sum` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:316-324] |
| `token_usage_sums_only_complete_component_counts` | function | `fn token_usage_sums_only_complete_component_counts() {` | `token_usage_sums_only_complete_component_counts [function]` | `47acf927-699c-5a4b-9f1b-3bb3f648f99f` | 327-341 [crates/gcore/src/ai_types.rs:327-341] | Indexed function `token_usage_sums_only_complete_component_counts` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:327-341] |
| `transcription_wire_seconds_round_to_integer_milliseconds` | function | `fn transcription_wire_seconds_round_to_integer_milliseconds() {` | `transcription_wire_seconds_round_to_integer_milliseconds [function]` | `3eb546a9-9b58-57aa-9246-b3e1e51da162` | 344-375 [crates/gcore/src/ai_types.rs:344-375] | Indexed function `transcription_wire_seconds_round_to_integer_milliseconds` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:344-375] |
| `transcription_wire_seconds_reject_overflowing_milliseconds` | function | `fn transcription_wire_seconds_reject_overflowing_milliseconds() {` | `transcription_wire_seconds_reject_overflowing_milliseconds [function]` | `3e2e5e6b-ceab-58e3-b867-2c38e5a961fd` | 378-389 [crates/gcore/src/ai_types.rs:378-389] | Indexed function `transcription_wire_seconds_reject_overflowing_milliseconds` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:378-389] |
| `transcription_wire_seconds_accept_negative_zero` | function | `fn transcription_wire_seconds_accept_negative_zero() {` | `transcription_wire_seconds_accept_negative_zero [function]` | `77c3c182-537d-5b19-a5f5-81dae984c8bf` | 392-404 [crates/gcore/src/ai_types.rs:392-404] | Indexed function `transcription_wire_seconds_accept_negative_zero` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:392-404] |
| `transcription_wire_seconds_reject_reversed_segments` | function | `fn transcription_wire_seconds_reject_reversed_segments() {` | `transcription_wire_seconds_reject_reversed_segments [function]` | `ea46ff6d-88d1-57ed-ac15-5fba2d00a593` | 407-419 [crates/gcore/src/ai_types.rs:407-419] | Indexed function `transcription_wire_seconds_reject_reversed_segments` in `crates/gcore/src/ai_types.rs`. [crates/gcore/src/ai_types.rs:407-419] |
