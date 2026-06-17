---
title: crates/gcode/src/commands/codewiki/progress.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/progress.rs
  ranges:
  - 2-7
  - 10-12
  - 15-19
  - 21-29
  - 32-36
  - 38-46
  - 49-54
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/progress.rs:2-7](crates/gcode/src/commands/codewiki/progress.rs#L2-L7), [crates/gcode/src/commands/codewiki/progress.rs:10-12](crates/gcode/src/commands/codewiki/progress.rs#L10-L12), [crates/gcode/src/commands/codewiki/progress.rs:15-19](crates/gcode/src/commands/codewiki/progress.rs#L15-L19), [crates/gcode/src/commands/codewiki/progress.rs:21-29](crates/gcode/src/commands/codewiki/progress.rs#L21-L29), [crates/gcode/src/commands/codewiki/progress.rs:32-36](crates/gcode/src/commands/codewiki/progress.rs#L32-L36), [crates/gcode/src/commands/codewiki/progress.rs:38-46](crates/gcode/src/commands/codewiki/progress.rs#L38-L46), [crates/gcode/src/commands/codewiki/progress.rs:49-54](crates/gcode/src/commands/codewiki/progress.rs#L49-L54)

</details>

# crates/gcode/src/commands/codewiki/progress.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Defines a small progress-reporting helper for codewiki commands with three sink modes: silent, stderr, and a test-only capture buffer. `CodewikiProgress` chooses the sink, formats every emitted message with a `codewiki: ` prefix, writes to stderr when enabled, and exposes captured lines in tests via `into_lines()`.
[crates/gcode/src/commands/codewiki/progress.rs:2-7]
[crates/gcode/src/commands/codewiki/progress.rs:10-12]
[crates/gcode/src/commands/codewiki/progress.rs:15-19]
[crates/gcode/src/commands/codewiki/progress.rs:21-29]
[crates/gcode/src/commands/codewiki/progress.rs:32-36]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CodewikiProgressSink` | type | `enum CodewikiProgressSink {` | `CodewikiProgressSink [type]` | `8f203f7d-2cb3-528c-8962-75f40313065c` | 2-7 [crates/gcode/src/commands/codewiki/progress.rs:2-7] | Indexed type `CodewikiProgressSink` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:2-7] |
| `CodewikiProgress` | class | `pub(crate) struct CodewikiProgress {` | `CodewikiProgress [class]` | `5e6101ee-775f-5fc8-9ea6-38fbb8994290` | 10-12 [crates/gcode/src/commands/codewiki/progress.rs:10-12] | Indexed class `CodewikiProgress` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:10-12] |
| `CodewikiProgress::silent` | method | `pub(crate) fn silent() -> Self {` | `CodewikiProgress::silent [method]` | `3fa6722b-8389-524c-8dee-953471ee4475` | 15-19 [crates/gcode/src/commands/codewiki/progress.rs:15-19] | Indexed method `CodewikiProgress::silent` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:15-19] |
| `CodewikiProgress::stderr` | method | `pub(crate) fn stderr(enabled: bool) -> Self {` | `CodewikiProgress::stderr [method]` | `99a28788-b80a-57e0-a1c3-3d4b8455e4a0` | 21-29 [crates/gcode/src/commands/codewiki/progress.rs:21-29] | Indexed method `CodewikiProgress::stderr` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:21-29] |
| `CodewikiProgress::capture` | method | `pub(crate) fn capture() -> Self {` | `CodewikiProgress::capture [method]` | `34ee3cfc-a921-5e43-a3d7-df4f2e0e32e1` | 32-36 [crates/gcode/src/commands/codewiki/progress.rs:32-36] | Indexed method `CodewikiProgress::capture` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:32-36] |
| `CodewikiProgress::emit` | method | `pub(crate) fn emit(&mut self, message: impl AsRef<str>) {` | `CodewikiProgress::emit [method]` | `9afc96e8-7b7b-5802-8b15-ac7cab4cc8f6` | 38-46 [crates/gcode/src/commands/codewiki/progress.rs:38-46] | Indexed method `CodewikiProgress::emit` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:38-46] |
| `CodewikiProgress::into_lines` | method | `pub(crate) fn into_lines(self) -> Vec<String> {` | `CodewikiProgress::into_lines [method]` | `5d13726f-3982-5c25-a86c-dbe7ded9ddbd` | 49-54 [crates/gcode/src/commands/codewiki/progress.rs:49-54] | Indexed method `CodewikiProgress::into_lines` in `crates/gcode/src/commands/codewiki/progress.rs`. [crates/gcode/src/commands/codewiki/progress.rs:49-54] |
