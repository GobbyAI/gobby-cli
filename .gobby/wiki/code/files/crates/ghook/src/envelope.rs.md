---
title: crates/ghook/src/envelope.rs
type: code_file
provenance:
- file: crates/ghook/src/envelope.rs
  ranges:
  - 24-32
  - 34-52
  - 59-70
  - 73-84
  - 87-109
  - 112-123
  - 126-140
  - 143-162
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/envelope.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Defines the v1 inbox envelope format that ghook enqueues and the daemon replays, with a fixed schema version, enqueue timestamp, priority flag, hook type, raw JSON input, source, and ordered headers. `Envelope::new` builds instances with the current UTC RFC3339 timestamp and constant schema version, while the test module checks serialization and schema validation, including correct handling of optional headers as an omitted object rather than empty strings.
[crates/ghook/src/envelope.rs:24-32]
[crates/ghook/src/envelope.rs:34-52]
[crates/ghook/src/envelope.rs:35-51]
[crates/ghook/src/envelope.rs:59-70]
[crates/ghook/src/envelope.rs:73-84]

## API Symbols

- `Envelope` (class) component `Envelope [class]` (`134b0274-548a-57f1-a2ae-2e1ade34d42b`) lines 24-32 [crates/ghook/src/envelope.rs:24-32]
  - Signature: `pub struct Envelope {`
  - Purpose: Envelope is a struct that wraps a queued webhook event payload with metadata including schema version, enqueue timestamp, priority flag, hook type, JSON input data, source origin, and ordered headers. [crates/ghook/src/envelope.rs:24-32]
- `Envelope` (class) component `Envelope [class]` (`a20c2033-1b4a-5cbf-a028-ad84070bc7c9`) lines 34-52 [crates/ghook/src/envelope.rs:34-52]
  - Signature: `impl Envelope {`
  - Purpose: **The `Envelope::new` constructor instantiates an Envelope with provided hook metadata and input data while automatically recording the current UTC timestamp in RFC3339 format.** [crates/ghook/src/envelope.rs:34-52]
- `Envelope.new` (method) component `Envelope.new [method]` (`e9dd6b5a-9f95-533d-9247-b9d353b78915`) lines 35-51 [crates/ghook/src/envelope.rs:35-51]
  - Signature: `pub fn new(`
  - Purpose: Creates a new instance with the provided hook configuration parameters, automatically initializing `schema_version` to a constant and `enqueued_at` to the current UTC timestamp in RFC3339 format. [crates/ghook/src/envelope.rs:35-51]
- `example_envelope` (function) component `example_envelope [function]` (`fba1baf1-58c9-5e8e-bea3-2f6922eb5a59`) lines 59-70 [crates/ghook/src/envelope.rs:59-70]
  - Signature: `fn example_envelope() -> Envelope {`
  - Purpose: Returns an Envelope instance for a session-start event with a JSON payload containing the session ID and custom headers carrying project and session identifiers. [crates/ghook/src/envelope.rs:59-70]
- `envelope_serializes_with_expected_fields` (function) component `envelope_serializes_with_expected_fields [function]` (`69839c0d-7b5b-53c8-b485-7e62790725d5`) lines 73-84 [crates/ghook/src/envelope.rs:73-84]
  - Signature: `fn envelope_serializes_with_expected_fields() {`
  - Purpose: This test verifies that an Envelope serializes to JSON with the correct schema version (1), metadata fields (critical flag, hook type, source), X-Gobby headers (project/session IDs), input data, and ISO 8601-formatted timestamp. [crates/ghook/src/envelope.rs:73-84]
- `droid_envelope_preserves_pascal_hook_and_source` (function) component `droid_envelope_preserves_pascal_hook_and_source [function]` (`e08d73f1-796c-53fe-8bf3-1d8ace9895f5`) lines 87-109 [crates/ghook/src/envelope.rs:87-109]
  - Signature: `fn droid_envelope_preserves_pascal_hook_and_source() {`
  - Purpose: This test verifies that an Envelope structure correctly serializes to JSON while preserving the hook type, source identifier, and nested input_data fields including the hook event name and tool parameters. [crates/ghook/src/envelope.rs:87-109]
- `empty_headers_serialize_as_empty_object` (function) component `empty_headers_serialize_as_empty_object [function]` (`b5f5f2dd-0b5a-5f09-8e6f-39d40a4f98fc`) lines 112-123 [crates/ghook/src/envelope.rs:112-123]
  - Signature: `fn empty_headers_serialize_as_empty_object() {`
  - Purpose: This function is a unit test that verifies an `Envelope` with empty headers (an empty `BTreeMap`) serializes to a JSON object with zero entries. [crates/ghook/src/envelope.rs:112-123]
- `envelope_validates_against_v1_schema` (function) component `envelope_validates_against_v1_schema [function]` (`829b6804-81c4-5be6-b434-5246a5915eac`) lines 126-140 [crates/ghook/src/envelope.rs:126-140]
  - Signature: `fn envelope_validates_against_v1_schema() {`
  - Purpose: Validates that an example inbox envelope instance conforms to an embedded Draft 7 JSON schema, panicking if validation errors occur. [crates/ghook/src/envelope.rs:126-140]
- `envelope_without_headers_validates_against_v1_schema` (function) component `envelope_without_headers_validates_against_v1_schema [function]` (`2361477e-62f9-5d3e-bb73-98b600aea6fa`) lines 143-162 [crates/ghook/src/envelope.rs:143-162]
  - Signature: `fn envelope_without_headers_validates_against_v1_schema() {`
  - Purpose: This test verifies that a headerless `Envelope` instance, when serialized to JSON, validates against the inbox-envelope v1 JSON Schema (Draft 7). [crates/ghook/src/envelope.rs:143-162]

