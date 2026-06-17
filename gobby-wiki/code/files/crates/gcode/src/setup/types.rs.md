---
title: crates/gcode/src/setup/types.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/types.rs
  ranges:
  - '5'
  - 8-10
  - 12-14
  - 16-18
  - 20-22
  - 26-28
  - 32-37
  - 41-66
  - 69-87
  - 95-110
  - 114-118
  - 121-129
  - 132-135
  - 138-147
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/setup/types.rs:5](crates/gcode/src/setup/types.rs#L5), [crates/gcode/src/setup/types.rs:8-10](crates/gcode/src/setup/types.rs#L8-L10), [crates/gcode/src/setup/types.rs:12-14](crates/gcode/src/setup/types.rs#L12-L14), [crates/gcode/src/setup/types.rs:16-18](crates/gcode/src/setup/types.rs#L16-L18), [crates/gcode/src/setup/types.rs:20-22](crates/gcode/src/setup/types.rs#L20-L22), [crates/gcode/src/setup/types.rs:26-28](crates/gcode/src/setup/types.rs#L26-L28), [crates/gcode/src/setup/types.rs:32-37](crates/gcode/src/setup/types.rs#L32-L37), [crates/gcode/src/setup/types.rs:41-66](crates/gcode/src/setup/types.rs#L41-L66), [crates/gcode/src/setup/types.rs:69-87](crates/gcode/src/setup/types.rs#L69-L87), [crates/gcode/src/setup/types.rs:95-110](crates/gcode/src/setup/types.rs#L95-L110), [crates/gcode/src/setup/types.rs:114-118](crates/gcode/src/setup/types.rs#L114-L118), [crates/gcode/src/setup/types.rs:121-129](crates/gcode/src/setup/types.rs#L121-L129), [crates/gcode/src/setup/types.rs:132-135](crates/gcode/src/setup/types.rs#L132-L135), [crates/gcode/src/setup/types.rs:138-147](crates/gcode/src/setup/types.rs#L138-L147)

</details>

# crates/gcode/src/setup/types.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

Defines setup-related data types for standalone GCode provisioning. `Redacted` wraps optional secret strings and provides accessors plus a custom `Debug` impl that hides the value. `StandaloneSetupRequest` groups the inputs needed for setup, including service flags, schema, embedding configuration, and secret fields that are skipped during serialization and redacted in debug output; its constructor fills in defaults such as the schema fallback. The remaining status and failure types model the setup lifecycle and outcomes for services, embeddings, and the overall standalone setup flow, and the test helper verifies that request debugging does not leak secrets.
[crates/gcode/src/setup/types.rs:5]
[crates/gcode/src/setup/types.rs:8-10]
[crates/gcode/src/setup/types.rs:12-14]
[crates/gcode/src/setup/types.rs:16-18]
[crates/gcode/src/setup/types.rs:20-22]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Redacted` | class | `pub struct Redacted(Option<String>);` | `Redacted [class]` | `d9102a69-174a-5828-a221-b7ed718b7f84` | 5-5 [crates/gcode/src/setup/types.rs:5] | Indexed class `Redacted` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:5] |
| `Redacted::new` | method | `pub fn new(value: Option<String>) -> Self {` | `Redacted::new [method]` | `fd79f391-2ac6-5180-aa28-de8243988bf8` | 8-10 [crates/gcode/src/setup/types.rs:8-10] | Indexed method `Redacted::new` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:8-10] |
| `Redacted::as_deref` | method | `pub fn as_deref(&self) -> Option<&str> {` | `Redacted::as_deref [method]` | `43b0536b-6236-5396-828a-d849d6703daa` | 12-14 [crates/gcode/src/setup/types.rs:12-14] | Indexed method `Redacted::as_deref` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:12-14] |
| `Redacted::is_some` | method | `pub fn is_some(&self) -> bool {` | `Redacted::is_some [method]` | `e45dd2f8-8bcc-5120-8b51-1a67b7cbc0f0` | 16-18 [crates/gcode/src/setup/types.rs:16-18] | Indexed method `Redacted::is_some` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:16-18] |
| `Redacted::clone_inner` | method | `pub fn clone_inner(&self) -> Option<String> {` | `Redacted::clone_inner [method]` | `0e070884-c0bf-5219-8746-be194be599c9` | 20-22 [crates/gcode/src/setup/types.rs:20-22] | Indexed method `Redacted::clone_inner` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:20-22] |
| `Redacted::from` | method | `fn from(value: Option<String>) -> Self {` | `Redacted::from [method]` | `20fe4d82-3311-55dd-83d3-882fb96c9499` | 26-28 [crates/gcode/src/setup/types.rs:26-28] | Indexed method `Redacted::from` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:26-28] |
| `Redacted::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `Redacted::fmt [method]` | `0d04daf2-88d7-5f2b-8a4d-b9c48baa59b8` | 32-37 [crates/gcode/src/setup/types.rs:32-37] | Indexed method `Redacted::fmt` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:32-37] |
| `StandaloneSetupRequest` | class | `pub struct StandaloneSetupRequest {` | `StandaloneSetupRequest [class]` | `b279bd79-a219-57d7-bc04-36d63f20e8d4` | 41-66 [crates/gcode/src/setup/types.rs:41-66] | Indexed class `StandaloneSetupRequest` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:41-66] |
| `StandaloneSetupRequest::new` | method | `pub fn new(standalone: bool, database_url: Option<String>, schema: Option<String>) -> Self {` | `StandaloneSetupRequest::new [method]` | `03d9522b-e35c-5a9b-937c-d28a5ead26ba` | 69-87 [crates/gcode/src/setup/types.rs:69-87] | Indexed method `StandaloneSetupRequest::new` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:69-87] |
| `standalone_setup_request_debug_redacts_secrets` | function | `fn standalone_setup_request_debug_redacts_secrets() {` | `standalone_setup_request_debug_redacts_secrets [function]` | `5344ab63-d88d-58dc-afb1-b51833e80c6f` | 95-110 [crates/gcode/src/setup/types.rs:95-110] | Indexed function `standalone_setup_request_debug_redacts_secrets` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:95-110] |
| `StandaloneServicesStatus` | class | `pub struct StandaloneServicesStatus {` | `StandaloneServicesStatus [class]` | `6b4c781d-5548-5fc6-8d14-168f099846b9` | 114-118 [crates/gcode/src/setup/types.rs:114-118] | Indexed class `StandaloneServicesStatus` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:114-118] |
| `StandaloneEmbeddingStatus` | class | `pub struct StandaloneEmbeddingStatus {` | `StandaloneEmbeddingStatus [class]` | `462ba16e-8a64-5941-b13a-66d999b9f32e` | 121-129 [crates/gcode/src/setup/types.rs:121-129] | Indexed class `StandaloneEmbeddingStatus` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:121-129] |
| `StandaloneFailure` | class | `pub struct StandaloneFailure {` | `StandaloneFailure [class]` | `ca7813b7-81f6-53c6-b47b-e7e53068b9e0` | 132-135 [crates/gcode/src/setup/types.rs:132-135] | Indexed class `StandaloneFailure` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:132-135] |
| `StandaloneSetupStatus` | class | `pub struct StandaloneSetupStatus {` | `StandaloneSetupStatus [class]` | `a3595622-bce4-5d52-bf8b-84c5862d5553` | 138-147 [crates/gcode/src/setup/types.rs:138-147] | Indexed class `StandaloneSetupStatus` in `crates/gcode/src/setup/types.rs`. [crates/gcode/src/setup/types.rs:138-147] |
