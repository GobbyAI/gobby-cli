---
title: crates/gcode/src/progress.rs
type: code_file
provenance:
- file: crates/gcode/src/progress.rs
  ranges:
  - 9-14
  - 16-71
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/progress.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file provides a lightweight, single-line progress bar for indexing operations that displays on stderr only when it's a TTY and quiet mode is disabled. The ProgressBar struct maintains state (total items, current position, enabled flag, display width) and exposes three methods: new() initializes the bar conditionally based on terminal capability, tick() increments progress and renders a visual bar with filled/empty characters plus file path information (truncating from the left to fit terminal width), and finish() clears the display line. The implementation uses ANSI escape codes for line overwriting and clearing, with no external dependencies.
[crates/gcode/src/progress.rs:9-14]
[crates/gcode/src/progress.rs:16-71]
[crates/gcode/src/progress.rs:18-26]
[crates/gcode/src/progress.rs:29-62]
[crates/gcode/src/progress.rs:65-70]

## API Symbols

- `ProgressBar` (class) component `ProgressBar [class]` (`d4e541e2-9540-5d12-a80a-1d987cc26336`) lines 9-14 [crates/gcode/src/progress.rs:9-14]
  - Signature: `pub struct ProgressBar {`
  - Purpose: Indexed class `ProgressBar` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:9-14]
- `ProgressBar` (class) component `ProgressBar [class]` (`f124d912-62b1-5972-81a3-e00c3d1854ad`) lines 16-71 [crates/gcode/src/progress.rs:16-71]
  - Signature: `impl ProgressBar {`
  - Purpose: Indexed class `ProgressBar` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:16-71]
- `ProgressBar.new` (method) component `ProgressBar.new [method]` (`2edd7e40-6ffc-50e3-8726-da1c8d6b5e86`) lines 18-26 [crates/gcode/src/progress.rs:18-26]
  - Signature: `pub fn new(total: usize, quiet: bool) -> Self {`
  - Purpose: Indexed method `ProgressBar.new` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:18-26]
- `ProgressBar.tick` (method) component `ProgressBar.tick [method]` (`ae9d43b2-7f45-5576-8b7b-9be3f49a9c57`) lines 29-62 [crates/gcode/src/progress.rs:29-62]
  - Signature: `pub fn tick(&mut self, file_path: &str) {`
  - Purpose: Indexed method `ProgressBar.tick` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:29-62]
- `ProgressBar.finish` (method) component `ProgressBar.finish [method]` (`200c306f-5de1-57d1-82ee-ca5703cff633`) lines 65-70 [crates/gcode/src/progress.rs:65-70]
  - Signature: `pub fn finish(&self) {`
  - Purpose: Indexed method `ProgressBar.finish` in `crates/gcode/src/progress.rs`. [crates/gcode/src/progress.rs:65-70]

