---
title: crates/gcode/src/commands/codewiki/progress.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/progress.rs
  ranges:
  - 2-7
  - 10-12
  - 14-55
  - 15-19
  - 21-29
  - 32-36
  - 38-46
  - 49-54
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/progress.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/progress.rs` exposes 8 indexed API symbols.
[crates/gcode/src/commands/codewiki/progress.rs:2-7]
[crates/gcode/src/commands/codewiki/progress.rs:10-12]
[crates/gcode/src/commands/codewiki/progress.rs:14-55]
[crates/gcode/src/commands/codewiki/progress.rs:15-19]
[crates/gcode/src/commands/codewiki/progress.rs:21-29]

## API Symbols

- `CodewikiProgressSink` (type) component `CodewikiProgressSink [type]` (`8f203f7d-2cb3-528c-8962-75f40313065c`) lines 2-7 [crates/gcode/src/commands/codewiki/progress.rs:2-7]
  - Signature: `enum CodewikiProgressSink {`
  - Purpose: Indexed type `CodewikiProgressSink` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:2-7]
- `CodewikiProgress` (class) component `CodewikiProgress [class]` (`5e6101ee-775f-5fc8-9ea6-38fbb8994290`) lines 10-12 [crates/gcode/src/commands/codewiki/progress.rs:10-12]
  - Signature: `pub(crate) struct CodewikiProgress {`
  - Purpose: A crate-private struct that wraps a `CodewikiProgressSink` instance for delegated progress reporting. [crates/gcode/src/commands/codewiki/progress.rs:10-12]
- `CodewikiProgress` (class) component `CodewikiProgress [class]` (`cf20f645-11d3-530b-8df4-155e3f3a48f7`) lines 14-55 [crates/gcode/src/commands/codewiki/progress.rs:14-55]
  - Signature: `impl CodewikiProgress {`
  - Purpose: `CodewikiProgress` is a configurable message sink that routes `'codewiki:'`-prefixed progress messages to silent, stderr, or in-memory capture outputs depending on initialization. [crates/gcode/src/commands/codewiki/progress.rs:14-55]
- `CodewikiProgress.silent` (method) component `CodewikiProgress.silent [method]` (`3fa6722b-8389-524c-8dee-953471ee4475`) lines 15-19 [crates/gcode/src/commands/codewiki/progress.rs:15-19]
  - Signature: `pub(crate) fn silent() -> Self {`
  - Purpose: A crate-internal factory method that instantiates `Self` with a `CodewikiProgressSink::Silent` variant to suppress progress output. [crates/gcode/src/commands/codewiki/progress.rs:15-19]
- `CodewikiProgress.stderr` (method) component `CodewikiProgress.stderr [method]` (`99a28788-b80a-57e0-a1c3-3d4b8455e4a0`) lines 21-29 [crates/gcode/src/commands/codewiki/progress.rs:21-29]
  - Signature: `pub(crate) fn stderr(enabled: bool) -> Self {`
  - Purpose: Conditionally constructs a progress reporter that outputs to stderr if enabled, or returns a silent instance if disabled. [crates/gcode/src/commands/codewiki/progress.rs:21-29]
- `CodewikiProgress.capture` (method) component `CodewikiProgress.capture [method]` (`34ee3cfc-a921-5e43-a3d7-df4f2e0e32e1`) lines 32-36 [crates/gcode/src/commands/codewiki/progress.rs:32-36]
  - Signature: `pub(crate) fn capture() -> Self {`
  - Purpose: Creates a new instance with a `sink` field initialized to the `Capture` variant of `CodewikiProgressSink` backed by an empty `Vec`. [crates/gcode/src/commands/codewiki/progress.rs:32-36]
- `CodewikiProgress.emit` (method) component `CodewikiProgress.emit [method]` (`9afc96e8-7b7b-5802-8b15-ac7cab4cc8f6`) lines 38-46 [crates/gcode/src/commands/codewiki/progress.rs:38-46]
  - Signature: `pub(crate) fn emit(&mut self, message: impl AsRef<str>) {`
  - Purpose: Formats a message with a "codewiki:" prefix and routes it to a configurable sink that either discards it (Silent), writes to stderr, or appends to a test capture buffer. [crates/gcode/src/commands/codewiki/progress.rs:38-46]
- `CodewikiProgress.into_lines` (method) component `CodewikiProgress.into_lines [method]` (`5d13726f-3982-5c25-a86c-dbe7ded9ddbd`) lines 49-54 [crates/gcode/src/commands/codewiki/progress.rs:49-54]
  - Signature: `pub(crate) fn into_lines(self) -> Vec<String> {`
  - Purpose: Returns the captured lines if the sink is in `Capture` mode, otherwise returns an empty vector. [crates/gcode/src/commands/codewiki/progress.rs:49-54]

