---
title: crates/gcode/src/setup/types.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/types.rs
  ranges:
  - '5'
  - 7-23
  - 25-29
  - 31-38
  - 41-66
  - 68-88
  - 95-110
  - 114-118
  - 121-129
  - 132-135
  - 138-147
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/types.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

This file defines setup-time data types for standalone Gobby provisioning, centered on a `Redacted` newtype that wraps optional secrets and hides their contents in `Debug` output while still allowing basic access and cloning. It then uses that wrapper in `StandaloneSetupRequest`, which collects standalone mode, database, embedding, and FalkorDB/Qdrant configuration, with a constructor that fills defaults like `DEFAULT_SCHEMA` and leaves optional fields unset unless provided. The rest of the file defines status and error structs for reporting provisioning progress and outcomes, including service health, embedding configuration, individual failures, and the overall setup result.
[crates/gcode/src/setup/types.rs:5]
[crates/gcode/src/setup/types.rs:7-23]
[crates/gcode/src/setup/types.rs:8-10]
[crates/gcode/src/setup/types.rs:12-14]
[crates/gcode/src/setup/types.rs:16-18]

## API Symbols

- `Redacted` (class) component `Redacted [class]` (`d9102a69-174a-5828-a221-b7ed718b7f84`) lines 5-5 [crates/gcode/src/setup/types.rs:5]
  - Signature: `pub struct Redacted(Option<String>);`
  - Purpose: A public newtype struct that wraps an optional `String` value. [crates/gcode/src/setup/types.rs:5]
- `Redacted` (class) component `Redacted [class]` (`f0bb5422-09a0-5671-98f6-92353cb94270`) lines 7-23 [crates/gcode/src/setup/types.rs:7-23]
  - Signature: `impl Redacted {`
  - Purpose: A newtype wrapper around `Option<String>` that provides delegated methods for querying, dereferencing, and cloning the wrapped optional string value. [crates/gcode/src/setup/types.rs:7-23]
- `Redacted.new` (method) component `Redacted.new [method]` (`fd79f391-2ac6-5180-aa28-de8243988bf8`) lines 8-10 [crates/gcode/src/setup/types.rs:8-10]
  - Signature: `pub fn new(value: Option<String>) -> Self {`
  - Purpose: This constructor wraps an `Option<String>` value in a newtype struct, returning an instance of the containing type. [crates/gcode/src/setup/types.rs:8-10]
- `Redacted.as_deref` (method) component `Redacted.as_deref [method]` (`43b0536b-6236-5396-828a-d849d6703daa`) lines 12-14 [crates/gcode/src/setup/types.rs:12-14]
  - Signature: `pub fn as_deref(&self) -> Option<&str> {`
  - Purpose: This method dereferences the wrapped value in the first field and returns an optional reference to a string. [crates/gcode/src/setup/types.rs:12-14]
- `Redacted.is_some` (method) component `Redacted.is_some [method]` (`e45dd2f8-8bcc-5120-8b51-1a67b7cbc0f0`) lines 16-18 [crates/gcode/src/setup/types.rs:16-18]
  - Signature: `pub fn is_some(&self) -> bool {`
  - Purpose: Returns `true` if the wrapped value is `Some`, delegating to the inner field's `is_some()` method. [crates/gcode/src/setup/types.rs:16-18]
- `Redacted.clone_inner` (method) component `Redacted.clone_inner [method]` (`0e070884-c0bf-5219-8746-be194be599c9`) lines 20-22 [crates/gcode/src/setup/types.rs:20-22]
  - Signature: `pub fn clone_inner(&self) -> Option<String> {`
  - Purpose: Clones and returns the inner `Option<String>` field wrapped in this tuple struct. [crates/gcode/src/setup/types.rs:20-22]
- `Redacted` (class) component `Redacted [class]` (`26444efe-1e2b-54ce-9677-302488bfff9b`) lines 25-29 [crates/gcode/src/setup/types.rs:25-29]
  - Signature: `impl From<Option<String>> for Redacted {`
  - Purpose: Implements the `From<Option<String>>` trait for `Redacted`, enabling infallible conversion from optional strings to `Redacted` instances via the constructor. [crates/gcode/src/setup/types.rs:25-29]
- `Redacted.from` (method) component `Redacted.from [method]` (`20fe4d82-3311-55dd-83d3-882fb96c9499`) lines 26-28 [crates/gcode/src/setup/types.rs:26-28]
  - Signature: `fn from(value: Option<String>) -> Self {`
  - Purpose: Implements a `From` trait conversion that converts `Option<String>` to `Self` by delegating to the `new` constructor. [crates/gcode/src/setup/types.rs:26-28]
- `Redacted` (class) component `Redacted [class]` (`8e954e72-4a2f-51ff-a5d7-ebc5b2742c2a`) lines 31-38 [crates/gcode/src/setup/types.rs:31-38]
  - Signature: `impl std::fmt::Debug for Redacted {`
  - Purpose: This `Debug` implementation for `Redacted` obfuscates the inner `Option` value by displaying `"<redacted>"` for `Some` variants while preserving the `None` case. [crates/gcode/src/setup/types.rs:31-38]
- `Redacted.fmt` (method) component `Redacted.fmt [method]` (`0d04daf2-88d7-5f2b-8a4d-b9c48baa59b8`) lines 32-37 [crates/gcode/src/setup/types.rs:32-37]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: This method implements a custom formatter that displays `<redacted>` for `Some` values and `None` for `None`, redacting the contents of an `Option` type for privacy. [crates/gcode/src/setup/types.rs:32-37]
- `StandaloneSetupRequest` (class) component `StandaloneSetupRequest [class]` (`b279bd79-a219-57d7-bc04-36d63f20e8d4`) lines 41-66 [crates/gcode/src/setup/types.rs:41-66]
  - Signature: `pub struct StandaloneSetupRequest {`
  - Purpose: `StandaloneSetupRequest` is a configuration struct for initializing a standalone instance that aggregates PostgreSQL database, embedding provider, and vector database (FalkorDB/Qdrant) parameters while implementing secure credential handling through serde skip-serialization and `Redacted` field wrapping. [crates/gcode/src/setup/types.rs:41-66]
- `StandaloneSetupRequest` (class) component `StandaloneSetupRequest [class]` (`d1b50a04-d183-5657-bca3-fc088ea18258`) lines 68-88 [crates/gcode/src/setup/types.rs:68-88]
  - Signature: `impl StandaloneSetupRequest {`
  - Purpose: `StandaloneSetupRequest` implements a constructor that initializes the struct with specified standalone mode and optional database parameters, while defaulting embedding provider and vector database configurations to None or false. [crates/gcode/src/setup/types.rs:68-88]
- `StandaloneSetupRequest.new` (method) component `StandaloneSetupRequest.new [method]` (`03d9522b-e35c-5a9b-937c-d28a5ead26ba`) lines 69-87 [crates/gcode/src/setup/types.rs:69-87]
  - Signature: `pub fn new(standalone: bool, database_url: Option<String>, schema: Option<String>) -> Self {`
  - Purpose: Initializes a configuration struct with the provided standalone mode, redacted database URL, and schema (defaulting to `DEFAULT_SCHEMA` if not provided), while zero-initializing all remaining embedding and database connection fields. [crates/gcode/src/setup/types.rs:69-87]
- `standalone_setup_request_debug_redacts_secrets` (function) component `standalone_setup_request_debug_redacts_secrets [function]` (`5344ab63-d88d-58dc-afb1-b51833e80c6f`) lines 95-110 [crates/gcode/src/setup/types.rs:95-110]
  - Signature: `fn standalone_setup_request_debug_redacts_secrets() {`
  - Purpose: This test verifies that the `Debug` implementation of `StandaloneSetupRequest` correctly redacts sensitive credentials (database connection strings, API keys, and passwords) by confirming secrets are absent and `<redacted>` markers are present in the debug output. [crates/gcode/src/setup/types.rs:95-110]
- `StandaloneServicesStatus` (class) component `StandaloneServicesStatus [class]` (`6b4c781d-5548-5fc6-8d14-168f099846b9`) lines 114-118 [crates/gcode/src/setup/types.rs:114-118]
  - Signature: `pub struct StandaloneServicesStatus {`
  - Purpose: `StandaloneServicesStatus` is a struct that tracks the provisioning state, optional compose file reference, and collection of health check identifiers for standalone services. [crates/gcode/src/setup/types.rs:114-118]
- `StandaloneEmbeddingStatus` (class) component `StandaloneEmbeddingStatus [class]` (`462ba16e-8a64-5941-b13a-66d999b9f32e`) lines 121-129 [crates/gcode/src/setup/types.rs:121-129]
  - Signature: `pub struct StandaloneEmbeddingStatus {`
  - Purpose: `StandaloneEmbeddingStatus` stores configuration and authentication metadata for a standalone embedding API provider, including its endpoint, model name, vector dimensionality, and API key status. [crates/gcode/src/setup/types.rs:121-129]
- `StandaloneFailure` (class) component `StandaloneFailure [class]` (`ca7813b7-81f6-53c6-b47b-e7e53068b9e0`) lines 132-135 [crates/gcode/src/setup/types.rs:132-135]
  - Signature: `pub struct StandaloneFailure {`
  - Purpose: `StandaloneFailure` is a public struct that encapsulates a failure event with two String fields—`name` and `reason`—representing the failure's identifier and descriptive cause. [crates/gcode/src/setup/types.rs:132-135]
- `StandaloneSetupStatus` (class) component `StandaloneSetupStatus [class]` (`a3595622-bce4-5d52-bf8b-84c5862d5553`) lines 138-147 [crates/gcode/src/setup/types.rs:138-147]
  - Signature: `pub struct StandaloneSetupStatus {`
  - Purpose: `StandaloneSetupStatus` encapsulates the results of a standalone initialization process, tracking namespace, schema, successfully created and skipped resources, failures with details, and optional service and embedding configuration states. [crates/gcode/src/setup/types.rs:138-147]

