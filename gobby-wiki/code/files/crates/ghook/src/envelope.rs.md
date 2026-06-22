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

`crates/ghook/src/envelope.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Envelope` | class | 'Envelope' is a Rust data carrier struct representing a queued hook event, with schema/version metadata, enqueue timestamp, criticality flag, hook type, arbitrary input payload, source identifier, and ordered string headers. [crates/ghook/src/envelope.rs:24-32] |
| `Envelope::new` | method | Constructs a new instance with the current UTC RFC3339 'enqueued_at' timestamp, the fixed 'SCHEMA_VERSION', and the provided 'critical', 'hook_type', 'input_data', 'source', and 'headers' fields. [crates/ghook/src/envelope.rs:35-51] |
| `example_envelope` | function | Constructs and returns an 'Envelope' for a '"session-start"' event with JSON payload '{"session_id":"sess-abc"}', provider '"claude"', 'true' as the first flag, and headers containing 'X-Gobby-Project-Id: proj-123' and 'X-Gobby-Session-Id: sess-abc'. [crates/ghook/src/envelope.rs:59-70] |

_Verified by 5 in-file unit tests._

