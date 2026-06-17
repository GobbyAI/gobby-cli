---
title: crates/gcode/src/vector/code_symbols/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/tests.rs
  ranges:
  - 20-41
  - 43-51
  - 53-67
  - 69-98
  - 100-120
  - 122-162
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/vector/code_symbols/tests.rs:20-41](crates/gcode/src/vector/code_symbols/tests.rs#L20-L41), [crates/gcode/src/vector/code_symbols/tests.rs:43-51](crates/gcode/src/vector/code_symbols/tests.rs#L43-L51), [crates/gcode/src/vector/code_symbols/tests.rs:53-67](crates/gcode/src/vector/code_symbols/tests.rs#L53-L67), [crates/gcode/src/vector/code_symbols/tests.rs:69-98](crates/gcode/src/vector/code_symbols/tests.rs#L69-L98), [crates/gcode/src/vector/code_symbols/tests.rs:100-120](crates/gcode/src/vector/code_symbols/tests.rs#L100-L120), [crates/gcode/src/vector/code_symbols/tests.rs:122-162](crates/gcode/src/vector/code_symbols/tests.rs#L122-L162)

</details>

# crates/gcode/src/vector/code_symbols/tests.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

This test support file provides shared fixtures and helpers for the `code_symbols` vector tests. It defines small constructors for sample `Symbol` values and a test `Context`, then adds HTTP test-server utilities for spawning canned responses, accepting connections with a timeout, and reading raw requests. The companion submodules (`collection`, `deletion`, `embedding`, `module_scope`, `payload`, `sync`) use these helpers to exercise indexing, transport, and payload behavior consistently.
[crates/gcode/src/vector/code_symbols/tests.rs:20-41]
[crates/gcode/src/vector/code_symbols/tests.rs:43-51]
[crates/gcode/src/vector/code_symbols/tests.rs:53-67]
[crates/gcode/src/vector/code_symbols/tests.rs:69-98]
[crates/gcode/src/vector/code_symbols/tests.rs:100-120]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `test_symbol` | function | `fn test_symbol(summary: Option<String>) -> Symbol {` | `test_symbol [function]` | `36c0a6fd-6714-55a7-b782-849121b553c1` | 20-41 [crates/gcode/src/vector/code_symbols/tests.rs:20-41] | Indexed function `test_symbol` in `crates/gcode/src/vector/code_symbols/tests.rs`. [crates/gcode/src/vector/code_symbols/tests.rs:20-41] |
| `test_symbol_with_index` | function | `fn test_symbol_with_index(index: usize) -> Symbol {` | `test_symbol_with_index [function]` | `14f1aeb3-0e63-5585-be0e-6155b73488e0` | 43-51 [crates/gcode/src/vector/code_symbols/tests.rs:43-51] | Indexed function `test_symbol_with_index` in `crates/gcode/src/vector/code_symbols/tests.rs`. [crates/gcode/src/vector/code_symbols/tests.rs:43-51] |
| `test_context` | function | `fn test_context(qdrant: Option<QdrantConfig>) -> Context {` | `test_context [function]` | `ea1dbdf2-93c0-5562-842f-5aa83d919331` | 53-67 [crates/gcode/src/vector/code_symbols/tests.rs:53-67] | Indexed function `test_context` in `crates/gcode/src/vector/code_symbols/tests.rs`. [crates/gcode/src/vector/code_symbols/tests.rs:53-67] |
| `spawn_http_responses` | function | `fn spawn_http_responses(responses: Vec<(u16, Value)>) -> (String, thread::JoinHandle<Vec<String>>) {` | `spawn_http_responses [function]` | `f09b6ee9-d58c-55ae-ba0b-1612b4eb0a84` | 69-98 [crates/gcode/src/vector/code_symbols/tests.rs:69-98] | Indexed function `spawn_http_responses` in `crates/gcode/src/vector/code_symbols/tests.rs`. [crates/gcode/src/vector/code_symbols/tests.rs:69-98] |
| `accept_with_timeout` | function | `fn accept_with_timeout(listener: &TcpListener, timeout: Duration) -> std::io::Result<TcpStream> {` | `accept_with_timeout [function]` | `55342d89-3342-5d45-9094-0f4e52315b33` | 100-120 [crates/gcode/src/vector/code_symbols/tests.rs:100-120] | Indexed function `accept_with_timeout` in `crates/gcode/src/vector/code_symbols/tests.rs`. [crates/gcode/src/vector/code_symbols/tests.rs:100-120] |
| `read_http_request` | function | `fn read_http_request(stream: &mut TcpStream) -> String {` | `read_http_request [function]` | `9cf0790d-400b-5a4a-a567-b6260929a9b4` | 122-162 [crates/gcode/src/vector/code_symbols/tests.rs:122-162] | Indexed function `read_http_request` in `crates/gcode/src/vector/code_symbols/tests.rs`. [crates/gcode/src/vector/code_symbols/tests.rs:122-162] |
