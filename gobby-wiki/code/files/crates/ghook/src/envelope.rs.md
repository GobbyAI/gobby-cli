---
title: crates/ghook/src/envelope.rs
type: code_file
provenance:
- file: crates/ghook/src/envelope.rs
  ranges:
  - 24-32
  - 35-51
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

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/envelope.rs:24-32](crates/ghook/src/envelope.rs#L24-L32), [crates/ghook/src/envelope.rs:35-51](crates/ghook/src/envelope.rs#L35-L51), [crates/ghook/src/envelope.rs:59-70](crates/ghook/src/envelope.rs#L59-L70), [crates/ghook/src/envelope.rs:73-84](crates/ghook/src/envelope.rs#L73-L84), [crates/ghook/src/envelope.rs:87-109](crates/ghook/src/envelope.rs#L87-L109), [crates/ghook/src/envelope.rs:112-123](crates/ghook/src/envelope.rs#L112-L123), [crates/ghook/src/envelope.rs:126-140](crates/ghook/src/envelope.rs#L126-L140), [crates/ghook/src/envelope.rs:143-162](crates/ghook/src/envelope.rs#L143-L162)

</details>

# crates/ghook/src/envelope.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Defines the frozen v1 inbox envelope type that ghook writes to `~/.gobby/hooks/inbox/` and the daemon replays. `Envelope` carries the schema version, enqueue timestamp, critical flag, hook type, raw input payload, source, and a string header map; `Envelope::new` fills in the fixed schema version and current RFC3339 time. The test helpers build an example envelope, then verify the serialized field shape, preserve the expected hook/source casing, ensure empty headers serialize as an empty object, and validate the output against the v1 JSON schema with and without headers.
[crates/ghook/src/envelope.rs:24-32]
[crates/ghook/src/envelope.rs:35-51]
[crates/ghook/src/envelope.rs:59-70]
[crates/ghook/src/envelope.rs:73-84]
[crates/ghook/src/envelope.rs:87-109]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Envelope` | class | `pub struct Envelope {` | `Envelope [class]` | `134b0274-548a-57f1-a2ae-2e1ade34d42b` | 24-32 [crates/ghook/src/envelope.rs:24-32] | Indexed class `Envelope` in `crates/ghook/src/envelope.rs`. [crates/ghook/src/envelope.rs:24-32] |
| `Envelope::new` | method | `pub fn new(` | `Envelope::new [method]` | `e9dd6b5a-9f95-533d-9247-b9d353b78915` | 35-51 [crates/ghook/src/envelope.rs:35-51] | Indexed method `Envelope::new` in `crates/ghook/src/envelope.rs`. [crates/ghook/src/envelope.rs:35-51] |
| `example_envelope` | function | `fn example_envelope() -> Envelope {` | `example_envelope [function]` | `fba1baf1-58c9-5e8e-bea3-2f6922eb5a59` | 59-70 [crates/ghook/src/envelope.rs:59-70] | Indexed function `example_envelope` in `crates/ghook/src/envelope.rs`. [crates/ghook/src/envelope.rs:59-70] |
| `envelope_serializes_with_expected_fields` | function | `fn envelope_serializes_with_expected_fields() {` | `envelope_serializes_with_expected_fields [function]` | `69839c0d-7b5b-53c8-b485-7e62790725d5` | 73-84 [crates/ghook/src/envelope.rs:73-84] | Indexed function `envelope_serializes_with_expected_fields` in `crates/ghook/src/envelope.rs`. [crates/ghook/src/envelope.rs:73-84] |
| `droid_envelope_preserves_pascal_hook_and_source` | function | `fn droid_envelope_preserves_pascal_hook_and_source() {` | `droid_envelope_preserves_pascal_hook_and_source [function]` | `e08d73f1-796c-53fe-8bf3-1d8ace9895f5` | 87-109 [crates/ghook/src/envelope.rs:87-109] | Indexed function `droid_envelope_preserves_pascal_hook_and_source` in `crates/ghook/src/envelope.rs`. [crates/ghook/src/envelope.rs:87-109] |
| `empty_headers_serialize_as_empty_object` | function | `fn empty_headers_serialize_as_empty_object() {` | `empty_headers_serialize_as_empty_object [function]` | `b5f5f2dd-0b5a-5f09-8e6f-39d40a4f98fc` | 112-123 [crates/ghook/src/envelope.rs:112-123] | Indexed function `empty_headers_serialize_as_empty_object` in `crates/ghook/src/envelope.rs`. [crates/ghook/src/envelope.rs:112-123] |
| `envelope_validates_against_v1_schema` | function | `fn envelope_validates_against_v1_schema() {` | `envelope_validates_against_v1_schema [function]` | `829b6804-81c4-5be6-b434-5246a5915eac` | 126-140 [crates/ghook/src/envelope.rs:126-140] | Indexed function `envelope_validates_against_v1_schema` in `crates/ghook/src/envelope.rs`. [crates/ghook/src/envelope.rs:126-140] |
| `envelope_without_headers_validates_against_v1_schema` | function | `fn envelope_without_headers_validates_against_v1_schema() {` | `envelope_without_headers_validates_against_v1_schema [function]` | `2361477e-62f9-5d3e-bb73-98b600aea6fa` | 143-162 [crates/ghook/src/envelope.rs:143-162] | Indexed function `envelope_without_headers_validates_against_v1_schema` in `crates/ghook/src/envelope.rs`. [crates/ghook/src/envelope.rs:143-162] |
