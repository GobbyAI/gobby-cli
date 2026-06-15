---
title: crates/gcore/src/degradation.rs
type: code_file
provenance:
- file: crates/gcore/src/degradation.rs
  ranges:
  - 12-22
  - 24-29
  - 33-40
  - 46-53
  - 57-91
  - 93-98
  - 100-115
  - 117-132
  - 134-139
  - 150-171
  - 173-189
  - 191-195
  - 199-233
  - 240-261
  - 264-293
  - 296-309
  - 312-354
  - 357-382
  - 385-397
  - 400-417
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/degradation.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file defines the shared degradation and error vocabulary for `gcore`: it models service availability (`ServiceState`), structured setup problems (`SetupIssue` and `Guidance`), and fatal core errors (`CoreError`) so callers can represent partial outages without treating every failure as fatal. It also includes database URL redaction helpers used by error serialization and display to strip credentials, queries, fragments, and sensitive keyword-style DSN values, plus `ModalityDegradationReason` and `DegradationKind` enums for stable, serde-compatible degradation codes. The tests verify these contracts stay aligned, especially that serialization, `Display`, availability checks, and URL redaction all preserve the intended semantics.
[crates/gcore/src/degradation.rs:12-22]
[crates/gcore/src/degradation.rs:24-29]
[crates/gcore/src/degradation.rs:26-28]
[crates/gcore/src/degradation.rs:33-40]
[crates/gcore/src/degradation.rs:46-53]

## API Symbols

- `ServiceState` (type) component `ServiceState [type]` (`2462c7a5-a92b-5d45-bb86-ccbb27e05a60`) lines 12-22 [crates/gcore/src/degradation.rs:12-22]
  - Signature: `pub enum ServiceState {`
  - Purpose: Indexed type `ServiceState` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:12-22]
- `ServiceState` (class) component `ServiceState [class]` (`95ee6ca7-e36c-5f41-ae66-9a2da2f4b117`) lines 24-29 [crates/gcore/src/degradation.rs:24-29]
  - Signature: `impl ServiceState {`
  - Purpose: `ServiceState` is a state enum wrapper that exposes `is_available()` to return `true` only when the value is the `Available` variant, meaning the backing service is connected and responding. [crates/gcore/src/degradation.rs:24-29]
- `ServiceState.is_available` (method) component `ServiceState.is_available [method]` (`84d5aeb3-ab3a-538b-a53b-c2135b216a08`) lines 26-28 [crates/gcore/src/degradation.rs:26-28]
  - Signature: `pub fn is_available(&self) -> bool {`
  - Purpose: Returns `true` exactly when `self` is `Self::Available`, and `false` for all other variants. [crates/gcore/src/degradation.rs:26-28]
- `SetupIssue` (class) component `SetupIssue [class]` (`57eb0d59-a536-5452-a7eb-89d4eaa7bb85`) lines 33-40 [crates/gcore/src/degradation.rs:33-40]
  - Signature: `pub struct SetupIssue {`
  - Purpose: `SetupIssue` is a structured diagnostic record for a missing, invalid, or degraded resource, identifying the affected object, its owning store/service, and machine-renderable remediation guidance. [crates/gcore/src/degradation.rs:33-40]
- `Guidance` (class) component `Guidance [class]` (`80052eba-9f9e-5043-b0dc-de0259d30bea`) lines 46-53 [crates/gcore/src/degradation.rs:46-53]
  - Signature: `pub struct Guidance {`
  - Purpose: `Guidance` is a structured diagnostic record that captures what is wrong or missing, the corrective action the user should take, and an optional command hint to execute that action. [crates/gcore/src/degradation.rs:46-53]
- `CoreError` (type) component `CoreError [type]` (`8923218a-870e-5580-bd10-10129700ae85`) lines 57-91 [crates/gcore/src/degradation.rs:57-91]
  - Signature: `pub enum CoreError {`
  - Purpose: Indexed type `CoreError` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:57-91]
- `serialize_redacted_database_url` (function) component `serialize_redacted_database_url [function]` (`502a1e5f-8d2b-5de4-b015-739c996efa2e`) lines 93-98 [crates/gcore/src/degradation.rs:93-98]
  - Signature: `fn serialize_redacted_database_url<S>(database_url: &str, serializer: S) -> Result<S::Ok, S::Error>`
  - Purpose: Serializes `database_url` as a `serde` string after passing it through `redact_database_url`, so the emitted value excludes sensitive URL components such as credentials. [crates/gcore/src/degradation.rs:93-98]
- `redact_database_url` (function) component `redact_database_url [function]` (`824828a9-f529-5938-a6fb-f1096a58df3f`) lines 100-115 [crates/gcore/src/degradation.rs:100-115]
  - Signature: `pub fn redact_database_url(database_url: &str) -> String {`
  - Purpose: Removes any `#fragment` and `?query` from the input, strips optional userinfo before `@` for `scheme://` URLs, and otherwise delegates to `redact_keyword_database_url` for non-URL keyword-style connection strings. [crates/gcore/src/degradation.rs:100-115]
- `redact_keyword_database_url` (function) component `redact_keyword_database_url [function]` (`ac093e1c-83dd-5b93-b9de-ab2f86bb3aa7`) lines 117-132 [crates/gcore/src/degradation.rs:117-132]
  - Signature: `fn redact_keyword_database_url(database_url: &str) -> String {`
  - Purpose: Splits a keyword-style DSN into space-delimited tokens, preserves non-`key=value` tokens unchanged, redacts the values of tokens whose keys are sensitive, and rejoins the result with spaces. [crates/gcore/src/degradation.rs:117-132]
- `is_sensitive_keyword_dsn_key` (function) component `is_sensitive_keyword_dsn_key [function]` (`3b74c48b-25b7-5f9a-81c4-6dd15a5b1dd1`) lines 134-139 [crates/gcore/src/degradation.rs:134-139]
  - Signature: `fn is_sensitive_keyword_dsn_key(key: &str) -> bool {`
  - Purpose: Returns `true` if `key`, case-insensitively, is exactly `"password"`, `"passfile"`, or `"sslpassword"`, and `false` otherwise. [crates/gcore/src/degradation.rs:134-139]
- `ModalityDegradationReason` (type) component `ModalityDegradationReason [type]` (`088bd219-2f55-5dfe-b778-09063412d1a5`) lines 150-171 [crates/gcore/src/degradation.rs:150-171]
  - Signature: `pub enum ModalityDegradationReason {`
  - Purpose: Indexed type `ModalityDegradationReason` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:150-171]
- `ModalityDegradationReason` (class) component `ModalityDegradationReason [class]` (`4f844584-7387-5be0-b95e-03067fcfd534`) lines 173-189 [crates/gcore/src/degradation.rs:173-189]
  - Signature: `impl ModalityDegradationReason {`
  - Purpose: This `impl` defines `as_str(self) -> &'static str`, which maps each `ModalityDegradationReason` variant to its stable serde-compatible lowercase string identifier for serialization and diagnostics. [crates/gcore/src/degradation.rs:173-189]
- `ModalityDegradationReason.as_str` (method) component `ModalityDegradationReason.as_str [method]` (`2be1386a-d5e8-5450-bd48-5feba555328c`) lines 175-188 [crates/gcore/src/degradation.rs:175-188]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Consumes the enum value and returns the corresponding `&'static str` error code string for each variant. [crates/gcore/src/degradation.rs:175-188]
- `ModalityDegradationReason` (class) component `ModalityDegradationReason [class]` (`ce5eba83-0696-5fe0-8425-73f501e55583`) lines 191-195 [crates/gcore/src/degradation.rs:191-195]
  - Signature: `impl std::fmt::Display for ModalityDegradationReason {`
  - Purpose: This `Display` implementation renders `ModalityDegradationReason` by writing the exact string returned by `self.as_str()` to the formatter with no extra formatting or allocation. [crates/gcore/src/degradation.rs:191-195]
- `ModalityDegradationReason.fmt` (method) component `ModalityDegradationReason.fmt [method]` (`74268ee9-36a9-5c0f-b98b-386a83a28296`) lines 192-194 [crates/gcore/src/degradation.rs:192-194]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Formats `self` by delegating to `self.as_str()` and writing that string directly into the provided formatter. [crates/gcore/src/degradation.rs:192-194]
- `DegradationKind` (type) component `DegradationKind [type]` (`5b166686-41ff-5c30-b3b4-efd7f247b450`) lines 199-233 [crates/gcore/src/degradation.rs:199-233]
  - Signature: `pub enum DegradationKind {`
  - Purpose: Indexed type `DegradationKind` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:199-233]
- `modality_reason_markers_match_serde_names` (function) component `modality_reason_markers_match_serde_names [function]` (`9484d2ed-60df-5db2-a853-b7316c893e0d`) lines 240-261 [crates/gcore/src/degradation.rs:240-261]
  - Signature: `fn modality_reason_markers_match_serde_names() {`
  - Purpose: This test verifies that every `ModalityDegradationReason` variant serializes via `serde_json` to the exact string returned by `as_str()`, and that `Display`/`to_string()` also matches that same marker, preventing drift between serde and textual representations. [crates/gcore/src/degradation.rs:240-261]
- `service_unavailable_degradation_is_not_fatal` (function) component `service_unavailable_degradation_is_not_fatal [function]` (`bbd1eb1b-d7d6-51a3-ad88-37192672bf26`) lines 264-293 [crates/gcore/src/degradation.rs:264-293]
  - Signature: `fn service_unavailable_degradation_is_not_fatal() {`
  - Purpose: This test verifies that both `ServiceState::NotConfigured` and `ServiceState::Unreachable` report unavailable, that a `DegradationKind::ServiceUnavailable` can carry a `NotConfigured` service state without being treated as fatal, and that `CoreError::RequiredServiceUnavailable` formats to the expected error string. [crates/gcore/src/degradation.rs:264-293]
- `guidance_is_structured` (function) component `guidance_is_structured [function]` (`69100e53-e4da-5896-9f33-a6a92a9ab764`) lines 296-309 [crates/gcore/src/degradation.rs:296-309]
  - Signature: `fn guidance_is_structured() {`
  - Purpose: This unit test constructs a `Guidance` instance with `problem`, `action`, and `command_hint` values, then verifies those fields are preserved exactly as assigned. [crates/gcore/src/degradation.rs:296-309]
- `core_error_serialization_roundtrip` (function) component `core_error_serialization_roundtrip [function]` (`8f583f2d-b6ba-5503-8bb6-f3f7e91c33bf`) lines 312-354 [crates/gcore/src/degradation.rs:312-354]
  - Signature: `fn core_error_serialization_roundtrip() {`
  - Purpose: Verifies that `CoreError` JSON serialization round-trips back to the same enum variants and field values for `InvalidConfig`, `RequiredServiceUnavailable`, and `HubConflict`. [crates/gcore/src/degradation.rs:312-354]
- `hub_conflict_display_and_json_redact_database_urls` (function) component `hub_conflict_display_and_json_redact_database_urls [function]` (`1fd4d940-c539-59e8-9946-20e7d509753b`) lines 357-382 [crates/gcore/src/degradation.rs:357-382]
  - Signature: `fn hub_conflict_display_and_json_redact_database_urls() {`
  - Purpose: Verifies that `CoreError::HubConflict` renders identities but redacts database URL credentials, query parameters, and fragments in both `Display` output and JSON serialization while preserving the non-sensitive URL scheme/host/path. [crates/gcore/src/degradation.rs:357-382]
- `keyword_database_url_redacts_sensitive_values_case_insensitively` (function) component `keyword_database_url_redacts_sensitive_values_case_insensitively [function]` (`237f0958-7c8f-5408-b14f-d63e87601a19`) lines 385-397 [crates/gcore/src/degradation.rs:385-397]
  - Signature: `fn keyword_database_url_redacts_sensitive_values_case_insensitively() {`
  - Purpose: Verifies that `redact_database_url` preserves non-sensitive connection fields while redacting password-like parameters case-insensitively, replacing their values with `<redacted>` and omitting the original secrets. [crates/gcore/src/degradation.rs:385-397]
- `hub_conflict_json_redacts_keyword_database_urls` (function) component `hub_conflict_json_redacts_keyword_database_urls [function]` (`e9d03dce-181c-50df-9924-9ab3fe0b21ad`) lines 400-417 [crates/gcore/src/degradation.rs:400-417]
  - Signature: `fn hub_conflict_json_redacts_keyword_database_urls() {`
  - Purpose: Tests that serializing a `CoreError::HubConflict` JSON-redacts sensitive database URL parameters like `password` and `PASSFILE` while preserving non-sensitive fields such as the host and database name. [crates/gcore/src/degradation.rs:400-417]

