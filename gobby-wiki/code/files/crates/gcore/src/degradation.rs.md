---
title: crates/gcore/src/degradation.rs
type: code_file
provenance:
- file: crates/gcore/src/degradation.rs
  ranges:
  - 12-22
  - 26-28
  - 33-40
  - 46-53
  - 57-91
  - 93-98
  - 100-115
  - 117-132
  - 134-139
  - 150-171
  - 175-188
  - 192-194
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/degradation.rs:12-22](crates/gcore/src/degradation.rs#L12-L22), [crates/gcore/src/degradation.rs:26-28](crates/gcore/src/degradation.rs#L26-L28), [crates/gcore/src/degradation.rs:33-40](crates/gcore/src/degradation.rs#L33-L40), [crates/gcore/src/degradation.rs:46-53](crates/gcore/src/degradation.rs#L46-L53), [crates/gcore/src/degradation.rs:57-91](crates/gcore/src/degradation.rs#L57-L91), [crates/gcore/src/degradation.rs:93-98](crates/gcore/src/degradation.rs#L93-L98), [crates/gcore/src/degradation.rs:100-115](crates/gcore/src/degradation.rs#L100-L115), [crates/gcore/src/degradation.rs:117-132](crates/gcore/src/degradation.rs#L117-L132), [crates/gcore/src/degradation.rs:134-139](crates/gcore/src/degradation.rs#L134-L139), [crates/gcore/src/degradation.rs:150-171](crates/gcore/src/degradation.rs#L150-L171), [crates/gcore/src/degradation.rs:175-188](crates/gcore/src/degradation.rs#L175-L188), [crates/gcore/src/degradation.rs:192-194](crates/gcore/src/degradation.rs#L192-L194), [crates/gcore/src/degradation.rs:199-233](crates/gcore/src/degradation.rs#L199-L233), [crates/gcore/src/degradation.rs:240-261](crates/gcore/src/degradation.rs#L240-L261), [crates/gcore/src/degradation.rs:264-293](crates/gcore/src/degradation.rs#L264-L293), [crates/gcore/src/degradation.rs:296-309](crates/gcore/src/degradation.rs#L296-L309), [crates/gcore/src/degradation.rs:312-354](crates/gcore/src/degradation.rs#L312-L354), [crates/gcore/src/degradation.rs:357-382](crates/gcore/src/degradation.rs#L357-L382), [crates/gcore/src/degradation.rs:385-397](crates/gcore/src/degradation.rs#L385-L397), [crates/gcore/src/degradation.rs:400-417](crates/gcore/src/degradation.rs#L400-L417)

</details>

# crates/gcore/src/degradation.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Defines the shared “degradation” vocabulary for `gcore`: service availability states, structured setup guidance, and the error/degradation enums used to distinguish partial or degraded operation from fatal failure. `ServiceState` models whether an adapter is available, unconfigured, or unreachable; `SetupIssue` and `Guidance` package actionable remediation details; `CoreError` captures fatal configuration and conflict cases. The redaction helpers scrub database URLs and sensitive DSN keys before display or serialization, while the test functions verify serde naming, nonfatal handling of unavailable services, structured guidance, round-trip serialization, and URL redaction behavior.
[crates/gcore/src/degradation.rs:12-22]
[crates/gcore/src/degradation.rs:26-28]
[crates/gcore/src/degradation.rs:33-40]
[crates/gcore/src/degradation.rs:46-53]
[crates/gcore/src/degradation.rs:57-91]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ServiceState` | type | `pub enum ServiceState {` | `ServiceState [type]` | `2462c7a5-a92b-5d45-bb86-ccbb27e05a60` | 12-22 [crates/gcore/src/degradation.rs:12-22] | Indexed type `ServiceState` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:12-22] |
| `ServiceState::is_available` | method | `pub fn is_available(&self) -> bool {` | `ServiceState::is_available [method]` | `84d5aeb3-ab3a-538b-a53b-c2135b216a08` | 26-28 [crates/gcore/src/degradation.rs:26-28] | Indexed method `ServiceState::is_available` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:26-28] |
| `SetupIssue` | class | `pub struct SetupIssue {` | `SetupIssue [class]` | `57eb0d59-a536-5452-a7eb-89d4eaa7bb85` | 33-40 [crates/gcore/src/degradation.rs:33-40] | Indexed class `SetupIssue` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:33-40] |
| `Guidance` | class | `pub struct Guidance {` | `Guidance [class]` | `80052eba-9f9e-5043-b0dc-de0259d30bea` | 46-53 [crates/gcore/src/degradation.rs:46-53] | Indexed class `Guidance` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:46-53] |
| `CoreError` | type | `pub enum CoreError {` | `CoreError [type]` | `8923218a-870e-5580-bd10-10129700ae85` | 57-91 [crates/gcore/src/degradation.rs:57-91] | Indexed type `CoreError` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:57-91] |
| `serialize_redacted_database_url` | function | `fn serialize_redacted_database_url<S>(database_url: &str, serializer: S) -> Result<S::Ok, S::Error>` | `serialize_redacted_database_url [function]` | `502a1e5f-8d2b-5de4-b015-739c996efa2e` | 93-98 [crates/gcore/src/degradation.rs:93-98] | Indexed function `serialize_redacted_database_url` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:93-98] |
| `redact_database_url` | function | `pub fn redact_database_url(database_url: &str) -> String {` | `redact_database_url [function]` | `824828a9-f529-5938-a6fb-f1096a58df3f` | 100-115 [crates/gcore/src/degradation.rs:100-115] | Indexed function `redact_database_url` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:100-115] |
| `redact_keyword_database_url` | function | `fn redact_keyword_database_url(database_url: &str) -> String {` | `redact_keyword_database_url [function]` | `ac093e1c-83dd-5b93-b9de-ab2f86bb3aa7` | 117-132 [crates/gcore/src/degradation.rs:117-132] | Indexed function `redact_keyword_database_url` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:117-132] |
| `is_sensitive_keyword_dsn_key` | function | `fn is_sensitive_keyword_dsn_key(key: &str) -> bool {` | `is_sensitive_keyword_dsn_key [function]` | `3b74c48b-25b7-5f9a-81c4-6dd15a5b1dd1` | 134-139 [crates/gcore/src/degradation.rs:134-139] | Indexed function `is_sensitive_keyword_dsn_key` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:134-139] |
| `ModalityDegradationReason` | type | `pub enum ModalityDegradationReason {` | `ModalityDegradationReason [type]` | `088bd219-2f55-5dfe-b778-09063412d1a5` | 150-171 [crates/gcore/src/degradation.rs:150-171] | Indexed type `ModalityDegradationReason` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:150-171] |
| `ModalityDegradationReason::as_str` | method | `pub fn as_str(self) -> &'static str {` | `ModalityDegradationReason::as_str [method]` | `2be1386a-d5e8-5450-bd48-5feba555328c` | 175-188 [crates/gcore/src/degradation.rs:175-188] | Indexed method `ModalityDegradationReason::as_str` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:175-188] |
| `ModalityDegradationReason::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `ModalityDegradationReason::fmt [method]` | `74268ee9-36a9-5c0f-b98b-386a83a28296` | 192-194 [crates/gcore/src/degradation.rs:192-194] | Indexed method `ModalityDegradationReason::fmt` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:192-194] |
| `DegradationKind` | type | `pub enum DegradationKind {` | `DegradationKind [type]` | `5b166686-41ff-5c30-b3b4-efd7f247b450` | 199-233 [crates/gcore/src/degradation.rs:199-233] | Indexed type `DegradationKind` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:199-233] |
| `modality_reason_markers_match_serde_names` | function | `fn modality_reason_markers_match_serde_names() {` | `modality_reason_markers_match_serde_names [function]` | `9484d2ed-60df-5db2-a853-b7316c893e0d` | 240-261 [crates/gcore/src/degradation.rs:240-261] | Indexed function `modality_reason_markers_match_serde_names` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:240-261] |
| `service_unavailable_degradation_is_not_fatal` | function | `fn service_unavailable_degradation_is_not_fatal() {` | `service_unavailable_degradation_is_not_fatal [function]` | `bbd1eb1b-d7d6-51a3-ad88-37192672bf26` | 264-293 [crates/gcore/src/degradation.rs:264-293] | Indexed function `service_unavailable_degradation_is_not_fatal` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:264-293] |
| `guidance_is_structured` | function | `fn guidance_is_structured() {` | `guidance_is_structured [function]` | `69100e53-e4da-5896-9f33-a6a92a9ab764` | 296-309 [crates/gcore/src/degradation.rs:296-309] | Indexed function `guidance_is_structured` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:296-309] |
| `core_error_serialization_roundtrip` | function | `fn core_error_serialization_roundtrip() {` | `core_error_serialization_roundtrip [function]` | `8f583f2d-b6ba-5503-8bb6-f3f7e91c33bf` | 312-354 [crates/gcore/src/degradation.rs:312-354] | Indexed function `core_error_serialization_roundtrip` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:312-354] |
| `hub_conflict_display_and_json_redact_database_urls` | function | `fn hub_conflict_display_and_json_redact_database_urls() {` | `hub_conflict_display_and_json_redact_database_urls [function]` | `1fd4d940-c539-59e8-9946-20e7d509753b` | 357-382 [crates/gcore/src/degradation.rs:357-382] | Indexed function `hub_conflict_display_and_json_redact_database_urls` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:357-382] |
| `keyword_database_url_redacts_sensitive_values_case_insensitively` | function | `fn keyword_database_url_redacts_sensitive_values_case_insensitively() {` | `keyword_database_url_redacts_sensitive_values_case_insensitively [function]` | `237f0958-7c8f-5408-b14f-d63e87601a19` | 385-397 [crates/gcore/src/degradation.rs:385-397] | Indexed function `keyword_database_url_redacts_sensitive_values_case_insensitively` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:385-397] |
| `hub_conflict_json_redacts_keyword_database_urls` | function | `fn hub_conflict_json_redacts_keyword_database_urls() {` | `hub_conflict_json_redacts_keyword_database_urls [function]` | `e9d03dce-181c-50df-9924-9ab3fe0b21ad` | 400-417 [crates/gcore/src/degradation.rs:400-417] | Indexed function `hub_conflict_json_redacts_keyword_database_urls` in `crates/gcore/src/degradation.rs`. [crates/gcore/src/degradation.rs:400-417] |
