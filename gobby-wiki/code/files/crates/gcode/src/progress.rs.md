---
title: crates/gcode/src/progress.rs
type: code_file
provenance:
- file: crates/gcode/src/progress.rs
  ranges:
  - 9-14
  - 18-26
  - 29-62
  - 65-70
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/progress.rs:9-14](crates/gcode/src/progress.rs#L9-L14), [crates/gcode/src/progress.rs:18-26](crates/gcode/src/progress.rs#L18-L26), [crates/gcode/src/progress.rs:29-62](crates/gcode/src/progress.rs#L29-L62), [crates/gcode/src/progress.rs:65-70](crates/gcode/src/progress.rs#L65-L70)

</details>

# crates/gcode/src/progress.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Provides a lightweight stderr progress bar for indexing work, with no external dependencies. `ProgressBar::new` enables display only when progress is meaningful, quiet mode is off, and stderr is a TTY. `tick` advances the counter, computes a fixed-width bar and percentage-based fill, truncates long file paths from the left to fit the terminal, and overwrites the current line in place. `finish` clears the line after completion when rendering was enabled.
[crates/gcode/src/progress.rs:9-14]
[crates/gcode/src/progress.rs:18-26]
[crates/gcode/src/progress.rs:29-62]
[crates/gcode/src/progress.rs:65-70]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ProgressBar` | class | `pub struct ProgressBar {` | `ProgressBar [class]` | `d4e541e2-9540-5d12-a80a-1d987cc26336` | 9-14 [crates/gcode/src/progress.rs:9-14] | Indexed class `ProgressBar` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:9-14] |
| `ProgressBar::new` | method | `pub fn new(total: usize, quiet: bool) -> Self {` | `ProgressBar::new [method]` | `2edd7e40-6ffc-50e3-8726-da1c8d6b5e86` | 18-26 [crates/gcode/src/progress.rs:18-26] | Indexed method `ProgressBar::new` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:18-26] |
| `ProgressBar::tick` | method | `pub fn tick(&mut self, file_path: &str) {` | `ProgressBar::tick [method]` | `ae9d43b2-7f45-5576-8b7b-9be3f49a9c57` | 29-62 [crates/gcode/src/progress.rs:29-62] | Indexed method `ProgressBar::tick` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:29-62] |
| `ProgressBar::finish` | method | `pub fn finish(&self) {` | `ProgressBar::finish [method]` | `200c306f-5de1-57d1-82ee-ca5703cff633` | 65-70 [crates/gcode/src/progress.rs:65-70] | Indexed method `ProgressBar::finish` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:65-70] |
