---
title: crates/gcode/src/commands/codewiki/progress.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/progress.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/progress.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/progress.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/progress.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodewikiProgressSink` | type | Indexed type `CodewikiProgressSink` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:2-7] |
| `CodewikiProgress` | class | 'CodewikiProgress' is a crate-visible wrapper struct containing a single 'sink: CodewikiProgressSink' field. [crates/gcode/src/commands/codewiki/progress.rs:10-12] |
| `CodewikiProgress::silent` | method | Constructs and returns a 'Self' instance with its 'sink' field set to 'CodewikiProgressSink::Silent'. [crates/gcode/src/commands/codewiki/progress.rs:15-19] |
| `CodewikiProgress::stderr` | method | Constructs a progress sink that targets standard error when 'enabled' is 'true', otherwise returns a silent sink. [crates/gcode/src/commands/codewiki/progress.rs:21-29] |
| `CodewikiProgress::capture` | method | Constructs a new instance with 'sink' initialized to 'CodewikiProgressSink::Capture(Vec::new())', i.e. an empty in-memory capture buffer. [crates/gcode/src/commands/codewiki/progress.rs:32-36] |
| `CodewikiProgress::emit` | method | Formats the input as 'codewiki: {message}' and dispatches it to the configured progress sink by dropping it for 'Silent', printing to stderr for 'Stderr', or appending the formatted line to the test 'Capture' buffer. [crates/gcode/src/commands/codewiki/progress.rs:38-46] |
| `CodewikiProgress::into_lines` | method | Consumes 'self' and returns the captured progress lines as a 'Vec<String>', yielding an empty vector for 'Silent' and 'Stderr' sinks. [crates/gcode/src/commands/codewiki/progress.rs:49-54] |

