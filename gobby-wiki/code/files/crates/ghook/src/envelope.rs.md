---
title: crates/ghook/src/envelope.rs
type: code_file
provenance:
- file: crates/ghook/src/envelope.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/envelope.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/envelope.rs` exposes 8 indexed API symbols.

## How it fits

`crates/ghook/src/envelope.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Envelope` | class | 'Envelope' is a Rust data carrier struct representing a queued hook event, with schema/version metadata, enqueue timestamp, criticality flag, hook type, arbitrary input payload, source identifier, and ordered string headers. [crates/ghook/src/envelope.rs:24-32] |
| `Envelope::new` | method | Constructs a new instance with the current UTC RFC3339 'enqueued_at' timestamp, the fixed 'SCHEMA_VERSION', and the provided 'critical', 'hook_type', 'input_data', 'source', and 'headers' fields. [crates/ghook/src/envelope.rs:35-51] |
| `example_envelope` | function | Constructs and returns an 'Envelope' for a '"session-start"' event with JSON payload '{"session_id":"sess-abc"}', provider '"claude"', 'true' as the first flag, and headers containing 'X-Gobby-Project-Id: proj-123' and 'X-Gobby-Session-Id: sess-abc'. [crates/ghook/src/envelope.rs:59-70] |
| `envelope_serializes_with_expected_fields` | function | Verifies that 'example_envelope()' serializes to JSON with the expected schema version, critical flag, hook type, source, header values, embedded session ID, and an ISO-like 'enqueued_at' timestamp containing 'T'. [crates/ghook/src/envelope.rs:73-84] |
| `droid_envelope_preserves_pascal_hook_and_source` | function | Verifies that serializing a 'droid' 'Envelope' preserves the PascalCase 'hook_type' and 'input_data.hook_event_name', along with the 'source' field and nested tool input path. [crates/ghook/src/envelope.rs:87-109] |
| `empty_headers_serialize_as_empty_object` | function | Verifies that serializing an 'Envelope' constructed with empty 'BTreeMap' headers produces a JSON 'headers' field encoded as an empty object rather than 'null' or another type. [crates/ghook/src/envelope.rs:112-123] |
| `envelope_validates_against_v1_schema` | function | Compiles the 'inbox-envelope.v1.schema.json' JSON Schema as Draft 7 and asserts that 'example_envelope()' serializes to a JSON instance that validates against it, panicking with collected validation errors if not. [crates/ghook/src/envelope.rs:126-140] |
| `envelope_without_headers_validates_against_v1_schema` | function | Builds the 'inbox-envelope.v1.schema.json' JSON Schema as Draft 7, serializes an 'Envelope' with empty headers, and panics with collected validation errors if the instance does not validate. [crates/ghook/src/envelope.rs:143-162] |

