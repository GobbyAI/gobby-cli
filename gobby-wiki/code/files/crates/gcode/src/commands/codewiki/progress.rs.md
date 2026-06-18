---
title: crates/gcode/src/commands/codewiki/progress.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/progress.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/progress.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The file `crates/gcode/src/commands/codewiki/progress.rs` provides a lightweight, unified mechanism for tracking and outputting progress messages during the execution of `codewiki` operations. It encapsulates the destination of these messages, decoupling the core logic of the command from the specific output medium.

At its core, the file defines the `CodewikiProgress` struct crates/gcode/src/commands/codewiki/progress.rs:10-12, which acts as a crate-visible wrapper around a progress sink. By providing a clean interface for emitting progress updates, it allows downstream operations to report status updates without managing stream handling directly.

## How it fits

Depending on configuration, the execution pipeline can instantiate a silent sink via `silent` crates/gcode/src/commands/codewiki/progress.rs:15-19 or route outputs to standard error via `stderr` crates/gcode/src/commands/codewiki/progress.rs:21-29. In testing environments, the flow captures progress lines into a list via `capture` crates/gcode/src/commands/codewiki/progress.rs:32-36, which can then be extracted using `into_lines` crates/gcode/src/commands/codewiki/progress.rs:49-54 to verify the sequence of emitted events.
[crates/gcode/src/commands/codewiki/progress.rs:2-7]
[crates/gcode/src/commands/codewiki/progress.rs:10-12]
[crates/gcode/src/commands/codewiki/progress.rs:15-19]
[crates/gcode/src/commands/codewiki/progress.rs:21-29]
[crates/gcode/src/commands/codewiki/progress.rs:32-36]

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

