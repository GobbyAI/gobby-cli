---
title: crates/ghook/src/json_value.rs
type: code_file
provenance:
- file: crates/ghook/src/json_value.rs
  ranges:
  - 3-20
  - 28-52
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/json_value.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Provides a small JSON utility for ghook that evaluates `serde_json::Value` using Python-style truthiness: `null`, `false`, zero numbers, empty strings, empty arrays, and empty objects are false, while booleans, nonzero numbers, nonempty strings, and nonempty collections are true. The test module confirms these dispatcher semantics with representative falsy and truthy cases.
[crates/ghook/src/json_value.rs:3-20]
[crates/ghook/src/json_value.rs:28-52]

## API Symbols

- `is_python_truthy` (function) component `is_python_truthy [function]` (`5d14c0ef-39c5-5653-9867-265c50d0ac2b`) lines 3-20 [crates/ghook/src/json_value.rs:3-20]
  - Signature: `pub(crate) fn is_python_truthy(value: &Value) -> bool {`
  - Purpose: Returns the Python-style truthiness of a 'serde_json::Value', treating 'Null' and zero/empty values as false and booleans, nonzero numbers, nonempty strings, nonempty arrays, and nonempty objects as true. [crates/ghook/src/json_value.rs:3-20]
- `python_truthiness_matches_dispatcher_semantics` (function) component `python_truthiness_matches_dispatcher_semantics [function]` (`ff170581-95ff-5889-acf6-7e3482709df8`) lines 28-52 [crates/ghook/src/json_value.rs:28-52]
  - Signature: `fn python_truthiness_matches_dispatcher_semantics() {`
  - Purpose: Verifies that 'is_python_truthy' matches Python-style truthiness by asserting standard falsy JSON values ('null', 'false', numeric zero, empty string/array/object) are false and non-empty/non-zero values are true. [crates/ghook/src/json_value.rs:28-52]

