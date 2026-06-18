---
title: crates/gcode/src/vector/code_symbols/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/tests.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Overview

`crates/gcode/src/vector/code_symbols/tests.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/vector/code_symbols/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `test_symbol` | function | Constructs and returns a 'Symbol' with fixed metadata for a Rust function named 'run' in 'src/lib.rs', using the provided 'summary' and leaving 'signature', 'docstring', 'parent_symbol_id', 'created_at', and 'updated_at' empty or 'None'. [crates/gcode/src/vector/code_symbols/tests.rs:20-41] |
| `test_symbol_with_index` | function | Constructs a 'Symbol' by starting from 'test_symbol(None)' and deterministically overriding its identifier, name, qualified name, and byte span to reflect the given 'index'. [crates/gcode/src/vector/code_symbols/tests.rs:43-51] |
| `test_context` | function | Constructs a 'Context' test fixture with hardcoded placeholder database and project paths/IDs, 'quiet' enabled, default code-vector and indexing settings, 'daemon_url' unset, 'index_scope' set to 'Single', 'falkordb'/'embedding' disabled, and the provided optional 'qdrant' configuration passed through. [crates/gcode/src/vector/code_symbols/tests.rs:53-67] |
| `spawn_http_responses` | function | Spawns a temporary nonblocking localhost TCP test server that, for each provided '(status, JSON body)' pair, accepts one HTTP request, records the raw request line/headers, and replies with a single 'HTTP/1.1' response using the given status code, canonical reason phrase, JSON content type, correct content length, and 'Connection: close', returning the server URL and a join handle for the captured requests. [crates/gcode/src/vector/code_symbols/tests.rs:69-98] |
| `accept_with_timeout` | function | Repeatedly calls 'listener.accept()' until a connection arrives or 'timeout' elapses, returning the accepted 'TcpStream' with blocking mode restored, or a 'TimedOut' I/O error on expiry. [crates/gcode/src/vector/code_symbols/tests.rs:100-120] |
| `read_http_request` | function | Reads an HTTP request from a 'TcpStream' with a 2-second read timeout, incrementally collecting bytes until either the full 'Content-Length' body has been received or the stream times out/ends, then returns the request as a UTF-8-lossy 'String'. [crates/gcode/src/vector/code_symbols/tests.rs:122-162] |

