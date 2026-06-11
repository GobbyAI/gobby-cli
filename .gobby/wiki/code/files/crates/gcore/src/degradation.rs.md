---
title: crates/gcore/src/degradation.rs
type: code_file
provenance:
- file: crates/gcore/src/degradation.rs
  ranges:
  - 12-22
  - 24-29
  - 26-28
  - 33-40
  - 46-53
  - 57-91
  - 93-98
  - 100-115
  - 117-132
  - 134-172
  - 174-179
  - 183-217
  - 224-253
  - 256-269
  - 272-314
  - 317-342
  - 345-357
  - 360-377
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/degradation.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/degradation.rs` exposes 18 indexed API symbols.
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
  - Purpose: ServiceState provides a public `is_available()` method that returns true exclusively when the enum variant is `Self::Available`. [crates/gcore/src/degradation.rs:24-29]
- `ServiceState.is_available` (method) component `ServiceState.is_available [method]` (`84d5aeb3-ab3a-538b-a53b-c2135b216a08`) lines 26-28 [crates/gcore/src/degradation.rs:26-28]
  - Signature: `pub fn is_available(&self) -> bool {`
  - Purpose: Returns `true` if the enum variant is `Available`, `false` otherwise. [crates/gcore/src/degradation.rs:26-28]
- `SetupIssue` (class) component `SetupIssue [class]` (`57eb0d59-a536-5452-a7eb-89d4eaa7bb85`) lines 33-40 [crates/gcore/src/degradation.rs:33-40]
  - Signature: `pub struct SetupIssue {`
  - Purpose: `SetupIssue` is a struct that encapsulates diagnostic information about a missing, invalid, or degraded resource, including the resource's name, its owning store or service, and structured remediation guidance. [crates/gcore/src/degradation.rs:33-40]
- `Guidance` (class) component `Guidance [class]` (`80052eba-9f9e-5043-b0dc-de0259d30bea`) lines 46-53 [crates/gcore/src/degradation.rs:46-53]
  - Signature: `pub struct Guidance {`
  - Purpose: A struct that encapsulates user guidance by combining a problem description, recommended action, and optional command suggestion. [crates/gcore/src/degradation.rs:46-53]
- `CoreError` (type) component `CoreError [type]` (`8923218a-870e-5580-bd10-10129700ae85`) lines 57-91 [crates/gcore/src/degradation.rs:57-91]
  - Signature: `pub enum CoreError {`
  - Purpose: Indexed type `CoreError` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:57-91]
- `serialize_redacted_database_url` (function) component `serialize_redacted_database_url [function]` (`502a1e5f-8d2b-5de4-b015-739c996efa2e`) lines 93-98 [crates/gcore/src/degradation.rs:93-98]
  - Signature: `fn serialize_redacted_database_url<S>(database_url: &str, serializer: S) -> Result<S::Ok, S::Error>`
  - Purpose: This function is a custom Serde serializer that serializes a database URL string with sensitive credentials redacted via the `redact_database_url` function. [crates/gcore/src/degradation.rs:93-98]
- `redact_database_url` (function) component `redact_database_url [function]` (`824828a9-f529-5938-a6fb-f1096a58df3f`) lines 100-115 [crates/gcore/src/degradation.rs:100-115]
  - Signature: `pub fn redact_database_url(database_url: &str) -> String {`
  - Purpose: Removes credentials (userinfo), query parameters, and fragments from a database URL while preserving the scheme and host/path components. [crates/gcore/src/degradation.rs:100-115]
- `redact_keyword_database_url` (function) component `redact_keyword_database_url [function]` (`ac093e1c-83dd-5b93-b9de-ab2f86bb3aa7`) lines 117-132 [crates/gcore/src/degradation.rs:117-132]
  - Signature: `fn redact_keyword_database_url(database_url: &str) -> String {`
  - Purpose: Redacts sensitive key values in a space-delimited DSN-formatted database URL by replacing their values with the literal string `<redacted>`. [crates/gcore/src/degradation.rs:117-132]
- `split_keyword_dsn_tokens` (function) component `split_keyword_dsn_tokens [function]` (`3171bfc0-271c-5e9f-8ec4-bb326ea5752d`) lines 134-172 [crates/gcore/src/degradation.rs:134-172]
  - Signature: `fn split_keyword_dsn_tokens(database_url: &str) -> Vec<&str> {`
  - Purpose: # Summary

Splits a database URL string on unquoted whitespace into token slices, while preserving single-quoted literals and handling backslash-escaped characters. [crates/gcore/src/degradation.rs:134-172]
- `is_sensitive_keyword_dsn_key` (function) component `is_sensitive_keyword_dsn_key [function]` (`8ebd4f98-14d3-5d30-8567-6f07f36f5713`) lines 174-179 [crates/gcore/src/degradation.rs:174-179]
  - Signature: `fn is_sensitive_keyword_dsn_key(key: &str) -> bool {`
  - Purpose: This function returns true if the input key matches any of three sensitive password-related DSN keywords ("password", "passfile", or "sslpassword") using case-insensitive comparison. [crates/gcore/src/degradation.rs:174-179]
- `DegradationKind` (type) component `DegradationKind [type]` (`5ec5928f-7d9d-56d8-9b46-77688b097b34`) lines 183-217 [crates/gcore/src/degradation.rs:183-217]
  - Signature: `pub enum DegradationKind {`
  - Purpose: Indexed type `DegradationKind` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:183-217]
- `service_unavailable_degradation_is_not_fatal` (function) component `service_unavailable_degradation_is_not_fatal [function]` (`5163cad9-df08-580d-9280-fd81ed1b752c`) lines 224-253 [crates/gcore/src/degradation.rs:224-253]
  - Signature: `fn service_unavailable_degradation_is_not_fatal() {`
  - Purpose: Verifies that optional service unavailability is categorized as non-fatal degradation, contrasting with required service unavailability which is treated as a fatal error. [crates/gcore/src/degradation.rs:224-253]
- `guidance_is_structured` (function) component `guidance_is_structured [function]` (`6a567f73-57f9-5a04-aa6b-7b642c658605`) lines 256-269 [crates/gcore/src/degradation.rs:256-269]
  - Signature: `fn guidance_is_structured() {`
  - Purpose: This unit test verifies that a `Guidance` struct instance is correctly initialized with a BM25 index problem description, its corresponding remediation action, and an optional command hint for setup validation. [crates/gcore/src/degradation.rs:256-269]
- `core_error_serialization_roundtrip` (function) component `core_error_serialization_roundtrip [function]` (`4927ebce-24e2-5a22-956c-7925c45d0c5b`) lines 272-314 [crates/gcore/src/degradation.rs:272-314]
  - Signature: `fn core_error_serialization_roundtrip() {`
  - Purpose: This test validates that multiple `CoreError` enum variants correctly roundtrip through JSON serialization and deserialization using `serde_json` without data loss. [crates/gcore/src/degradation.rs:272-314]
- `hub_conflict_display_and_json_redact_database_urls` (function) component `hub_conflict_display_and_json_redact_database_urls [function]` (`243d9957-03ea-5ee5-9896-258ef2f043f2`) lines 317-342 [crates/gcore/src/degradation.rs:317-342]
  - Signature: `fn hub_conflict_display_and_json_redact_database_urls() {`
  - Purpose: Tests that `HubConflict` errors redact database URLs and credentials entirely from string display while JSON serialization preserves URLs with sensitive components (credentials, query parameters, fragments) stripped. [crates/gcore/src/degradation.rs:317-342]
- `keyword_database_url_redacts_sensitive_values_case_insensitively` (function) component `keyword_database_url_redacts_sensitive_values_case_insensitively [function]` (`de3fc1b7-2730-55fd-b653-a17e37e88c9a`) lines 345-357 [crates/gcore/src/degradation.rs:345-357]
  - Signature: `fn keyword_database_url_redacts_sensitive_values_case_insensitively() {`
  - Purpose: Tests that `redact_database_url` performs case-insensitive redaction of sensitive credential keywords (PASSWORD, sslpassword) while preserving non-sensitive connection parameters. [crates/gcore/src/degradation.rs:345-357]
- `hub_conflict_json_redacts_keyword_database_urls` (function) component `hub_conflict_json_redacts_keyword_database_urls [function]` (`eb2ad722-10a6-5acf-99ff-e7c89d4a9ea8`) lines 360-377 [crates/gcore/src/degradation.rs:360-377]
  - Signature: `fn hub_conflict_json_redacts_keyword_database_urls() {`
  - Purpose: This test verifies that `CoreError::HubConflict` JSON serialization redacts sensitive database credentials (`password` and `PASSFILE` values) while preserving non-sensitive connection parameters. [crates/gcore/src/degradation.rs:360-377]

