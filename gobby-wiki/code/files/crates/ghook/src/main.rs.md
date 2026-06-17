---
title: crates/ghook/src/main.rs
type: code_file
provenance:
- file: crates/ghook/src/main.rs
  ranges:
  - 40-63
  - 65-81
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/main.rs:40-63](crates/ghook/src/main.rs#L40-L63), [crates/ghook/src/main.rs:65-81](crates/ghook/src/main.rs#L65-L81)

</details>

# crates/ghook/src/main.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Entry point for `ghook`, a sandbox-tolerant hook dispatcher that routes the process into version, diagnostics, or gobby-owned dispatch mode based on parsed CLI flags. `main` handles top-level mode selection and nonfatal version stamp writing, while `run_diagnose` enforces required `--cli` and `--type` inputs, calls the diagnostics module, and emits pretty-printed JSON to stdout or an error exit on failure.
[crates/ghook/src/main.rs:40-63]
[crates/ghook/src/main.rs:65-81]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `main` | function | `fn main() -> ExitCode {` | `main [function]` | `dee4d56b-3252-5af3-b9d2-b1548601bf33` | 40-63 [crates/ghook/src/main.rs:40-63] | Indexed function `main` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:40-63] |
| `run_diagnose` | function | `fn run_diagnose(args: &Args) -> ExitCode {` | `run_diagnose [function]` | `80fd2295-eda8-5a6e-88af-12217cc3aa17` | 65-81 [crates/ghook/src/main.rs:65-81] | Indexed function `run_diagnose` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:65-81] |
