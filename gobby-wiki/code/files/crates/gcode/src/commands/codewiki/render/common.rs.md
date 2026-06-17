---
title: crates/gcode/src/commands/codewiki/render/common.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/common.rs
  ranges:
  - 1-7
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/render/common.rs:1-7](crates/gcode/src/commands/codewiki/render/common.rs#L1-L7)

</details>

# crates/gcode/src/commands/codewiki/render/common.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Purpose

Provides a small helper for render code that turns a degraded-model flag into the list of source tags to report: it returns `["model-unavailable"]` when degraded is true, and an empty vector otherwise. [crates/gcode/src/commands/codewiki/render/common.rs:1-7]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `model_degraded_sources` | function | `pub(crate) fn model_degraded_sources(degraded: bool) -> Vec<String> {` | `model_degraded_sources [function]` | `6fa7713c-5f00-5792-ac68-bd5c6ce05b1c` | 1-7 [crates/gcode/src/commands/codewiki/render/common.rs:1-7] | Indexed function `model_degraded_sources` in `crates/gcode/src/commands/codewiki/render/common.rs`. [crates/gcode/src/commands/codewiki/render/common.rs:1-7] |
