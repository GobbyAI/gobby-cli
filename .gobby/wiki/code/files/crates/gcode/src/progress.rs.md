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

This file implements a lightweight stderr progress bar for indexing operations. `ProgressBar::new` decides whether rendering is enabled based on `quiet`, a nonzero total, and whether stderr is a TTY, then initializes a fixed 20-character bar. `tick` advances the counter, and when enabled it computes the filled versus empty bar segments, formats a `current/total` counter, left-truncates long file paths to fit an 80-character line, and overwrites the same terminal line with carriage-return and erase-to-end-of-line sequences. `finish` clears that line at completion and flushes stderr.
[crates/gcode/src/progress.rs:9-14]
[crates/gcode/src/progress.rs:16-71]
[crates/gcode/src/progress.rs:18-26]
[crates/gcode/src/progress.rs:29-62]
[crates/gcode/src/progress.rs:65-70]

## API Symbols

- `ProgressBar` (class) component `ProgressBar [class]` (`d4e541e2-9540-5d12-a80a-1d987cc26336`) lines 9-14 [crates/gcode/src/progress.rs:9-14]
  - Signature: `pub struct ProgressBar {`
  - Purpose: 'ProgressBar' is a struct that tracks a bounded progress indicator with a total count, current count, enabled flag, and configurable bar width for rendering. [crates/gcode/src/progress.rs:9-14]
- `ProgressBar` (class) component `ProgressBar [class]` (`f124d912-62b1-5972-81a3-e00c3d1854ad`) lines 16-71 [crates/gcode/src/progress.rs:16-71]
  - Signature: `impl ProgressBar {`
  - Purpose: 'ProgressBar' is a TTY-gated stderr progress indicator that tracks 'current' against 'total', renders a fixed-width 20-character bar with truncated file paths on each 'tick', and clears the line on 'finish'. [crates/gcode/src/progress.rs:16-71]
- `ProgressBar.new` (method) component `ProgressBar.new [method]` (`2edd7e40-6ffc-50e3-8726-da1c8d6b5e86`) lines 18-26 [crates/gcode/src/progress.rs:18-26]
  - Signature: `pub fn new(total: usize, quiet: bool) -> Self {`
  - Purpose: Constructs a progress-tracker instance with 'current' initialized to '0', 'bar_width' fixed at '20', and 'enabled' set only when 'quiet' is false, 'total > 0', and 'stderr' is a terminal. [crates/gcode/src/progress.rs:18-26]
- `ProgressBar.tick` (method) component `ProgressBar.tick [method]` (`ae9d43b2-7f45-5576-8b7b-9be3f49a9c57`) lines 29-62 [crates/gcode/src/progress.rs:29-62]
  - Signature: `pub fn tick(&mut self, file_path: &str) {`
  - Purpose: 'tick' increments the progress counter, returns early if disabled, computes and renders a terminal progress bar with current/total counts, left-truncates the file path to fit an 80-character line, writes the updated status to stderr with carriage-return line overwrite and clears the remainder, then flushes stderr. [crates/gcode/src/progress.rs:29-62]
- `ProgressBar.finish` (method) component `ProgressBar.finish [method]` (`200c306f-5de1-57d1-82ee-ca5703cff633`) lines 65-70 [crates/gcode/src/progress.rs:65-70]
  - Signature: `pub fn finish(&self) {`
  - Purpose: If 'self.enabled' is true, this method clears the current terminal line on stderr using a carriage return and ANSI erase sequence, then flushes stderr. [crates/gcode/src/progress.rs:65-70]

