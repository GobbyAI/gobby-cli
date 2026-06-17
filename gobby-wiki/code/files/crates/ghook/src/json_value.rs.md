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

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/json_value.rs:3-20](crates/ghook/src/json_value.rs#L3-L20), [crates/ghook/src/json_value.rs:28-52](crates/ghook/src/json_value.rs#L28-L52)

</details>

# crates/ghook/src/json_value.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

This file defines `is_python_truthy`, a helper that evaluates a `serde_json::Value` using Python-style truthiness rules: `null`, `false`, zero numbers, empty strings, empty arrays, and empty objects are falsy, while nonzero numbers and nonempty values are truthy. It also contains a test, `python_truthiness_matches_dispatcher_semantics`, which verifies those semantics against representative falsy and truthy JSON cases.
[crates/ghook/src/json_value.rs:3-20]
[crates/ghook/src/json_value.rs:28-52]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `is_python_truthy` | function | `pub(crate) fn is_python_truthy(value: &Value) -> bool {` | `is_python_truthy [function]` | `5d14c0ef-39c5-5653-9867-265c50d0ac2b` | 3-20 [crates/ghook/src/json_value.rs:3-20] | Indexed function `is_python_truthy` in `crates/ghook/src/json_value.rs`. [crates/ghook/src/json_value.rs:3-20] |
| `python_truthiness_matches_dispatcher_semantics` | function | `fn python_truthiness_matches_dispatcher_semantics() {` | `python_truthiness_matches_dispatcher_semantics [function]` | `ff170581-95ff-5889-acf6-7e3482709df8` | 28-52 [crates/ghook/src/json_value.rs:28-52] | Indexed function `python_truthiness_matches_dispatcher_semantics` in `crates/ghook/src/json_value.rs`. [crates/ghook/src/json_value.rs:28-52] |
