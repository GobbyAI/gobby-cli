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

# crates/gcode/src/vector/code_symbols/tests.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

This file is a test support module for `crates/gcode` code-symbol behavior. It defines reusable fixtures for constructing sample `Symbol` and `Context` values, plus small HTTP test-server helpers for exercising request/response flows, while the submodules (`collection`, `deletion`, `embedding`, `module_scope`, `payload`, `sync`) hold the actual test cases that consume those fixtures.
[crates/gcode/src/vector/code_symbols/tests.rs:20-41]
[crates/gcode/src/vector/code_symbols/tests.rs:43-51]
[crates/gcode/src/vector/code_symbols/tests.rs:53-67]
[crates/gcode/src/vector/code_symbols/tests.rs:69-98]
[crates/gcode/src/vector/code_symbols/tests.rs:100-120]

## API Symbols

- `test_symbol` (function) component `test_symbol [function]` (`36c0a6fd-6714-55a7-b782-849121b553c1`) lines 20-41 [crates/gcode/src/vector/code_symbols/tests.rs:20-41]
  - Signature: `fn test_symbol(summary: Option<String>) -> Symbol {`
  - Purpose: Constructs and returns a 'Symbol' record for a Rust function named 'run' in 'src/lib.rs', populating fixed metadata fields and passing through the optional 'summary' argument. [crates/gcode/src/vector/code_symbols/tests.rs:20-41]
- `test_symbol_with_index` (function) component `test_symbol_with_index [function]` (`14f1aeb3-0e63-5585-be0e-6155b73488e0`) lines 43-51 [crates/gcode/src/vector/code_symbols/tests.rs:43-51]
  - Signature: `fn test_symbol_with_index(index: usize) -> Symbol {`
  - Purpose: Creates a 'Symbol' from 'test_symbol(None)' and deterministically overwrites its identifier, name, qualified name, and byte range using the provided 'index', then returns the modified symbol. [crates/gcode/src/vector/code_symbols/tests.rs:43-51]
- `test_context` (function) component `test_context [function]` (`ea1dbdf2-93c0-5562-842f-5aa83d919331`) lines 53-67 [crates/gcode/src/vector/code_symbols/tests.rs:53-67]
  - Signature: `fn test_context(qdrant: Option<QdrantConfig>) -> Context {`
  - Purpose: Constructs a 'Context' test fixture with fixed nonexistent PostgreSQL and project-root paths, a hardcoded project ID, quiet mode enabled, default code-vector and indexing settings, 'falkordb', 'embedding', and 'daemon_url' unset, 'index_scope' set to 'Single', and the supplied optional 'qdrant' configuration propagated as-is. [crates/gcode/src/vector/code_symbols/tests.rs:53-67]
- `spawn_http_responses` (function) component `spawn_http_responses [function]` (`f09b6ee9-d58c-55ae-ba0b-1612b4eb0a84`) lines 69-98 [crates/gcode/src/vector/code_symbols/tests.rs:69-98]
  - Signature: `fn spawn_http_responses(responses: Vec<(u16, Value)>) -> (String, thread::JoinHandle<Vec<String>>) {`
  - Purpose: Binds a local nonblocking TCP listener, spawns a thread that accepts one HTTP request per supplied '(status, JSON body)' pair and replies with a corresponding 'HTTP/1.1' response, and returns the base URL plus a join handle that yields the captured raw requests. [crates/gcode/src/vector/code_symbols/tests.rs:69-98]
- `accept_with_timeout` (function) component `accept_with_timeout [function]` (`55342d89-3342-5d45-9094-0f4e52315b33`) lines 100-120 [crates/gcode/src/vector/code_symbols/tests.rs:100-120]
  - Signature: `fn accept_with_timeout(listener: &TcpListener, timeout: Duration) -> std::io::Result<TcpStream> {`
  - Purpose: Attempts to accept an incoming connection on 'listener' until 'timeout' elapses, polling every 10 ms on 'WouldBlock', returning a blocking 'TcpStream' on success or a 'TimedOut' I/O error if no connection arrives in time. [crates/gcode/src/vector/code_symbols/tests.rs:100-120]
- `read_http_request` (function) component `read_http_request [function]` (`9cf0790d-400b-5a4a-a567-b6260929a9b4`) lines 122-162 [crates/gcode/src/vector/code_symbols/tests.rs:122-162]
  - Signature: `fn read_http_request(stream: &mut TcpStream) -> String {`
  - Purpose: Reads bytes from a 'TcpStream' with a 2-second timeout, accumulates the request until either the full 'Content-Length' body has been received or the stream times out/ends, and returns the captured request as a 'String'. [crates/gcode/src/vector/code_symbols/tests.rs:122-162]

