---
title: crates/gcode/src/dispatch.rs
type: code_file
provenance:
- file: crates/gcode/src/dispatch.rs
  ranges:
  - '8'
  - 11-13
  - 15-19
  - '21'
  - 24-28
  - 30-37
  - 39-47
  - 49-61
  - 63-65
  - 67-72
  - 74-78
  - 80-122
  - 124-209
  - 211-237
  - 239-586
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/dispatch.rs:8](crates/gcode/src/dispatch.rs#L8), [crates/gcode/src/dispatch.rs:11-13](crates/gcode/src/dispatch.rs#L11-L13), [crates/gcode/src/dispatch.rs:15-19](crates/gcode/src/dispatch.rs#L15-L19), [crates/gcode/src/dispatch.rs:21](crates/gcode/src/dispatch.rs#L21), [crates/gcode/src/dispatch.rs:24-28](crates/gcode/src/dispatch.rs#L24-L28), [crates/gcode/src/dispatch.rs:30-37](crates/gcode/src/dispatch.rs#L30-L37), [crates/gcode/src/dispatch.rs:39-47](crates/gcode/src/dispatch.rs#L39-L47), [crates/gcode/src/dispatch.rs:49-61](crates/gcode/src/dispatch.rs#L49-L61), [crates/gcode/src/dispatch.rs:63-65](crates/gcode/src/dispatch.rs#L63-L65), [crates/gcode/src/dispatch.rs:67-72](crates/gcode/src/dispatch.rs#L67-L72), [crates/gcode/src/dispatch.rs:74-78](crates/gcode/src/dispatch.rs#L74-L78), [crates/gcode/src/dispatch.rs:80-122](crates/gcode/src/dispatch.rs#L80-L122), [crates/gcode/src/dispatch.rs:124-209](crates/gcode/src/dispatch.rs#L124-L209), [crates/gcode/src/dispatch.rs:211-237](crates/gcode/src/dispatch.rs#L211-L237), [crates/gcode/src/dispatch.rs:239-586](crates/gcode/src/dispatch.rs#L239-L586)

</details>

# crates/gcode/src/dispatch.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Sets up the `gcode` CLI dispatch path: it installs a simple stderr logger, derives log verbosity from `quiet` and `RUST_LOG`, and provides helpers that gate freshness checks for the project, files, or a symbol, warning when the index is already being refreshed. It also contains service-config selection and early-command dispatch logic, then the main `run` flow that routes CLI commands and returns an appropriate exit code.
[crates/gcode/src/dispatch.rs:8]
[crates/gcode/src/dispatch.rs:11-13]
[crates/gcode/src/dispatch.rs:15-19]
[crates/gcode/src/dispatch.rs:21]
[crates/gcode/src/dispatch.rs:24-28]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `StderrLogger` | class | `struct StderrLogger;` | `StderrLogger [class]` | `2d71eb13-2869-5f4a-920c-da64de430437` | 8-8 [crates/gcode/src/dispatch.rs:8] | Indexed class `StderrLogger` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:8] |
| `StderrLogger::enabled` | method | `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {` | `StderrLogger::enabled [method]` | `2383f1c4-c756-5611-8934-d7cb282e6e22` | 11-13 [crates/gcode/src/dispatch.rs:11-13] | Indexed method `StderrLogger::enabled` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:11-13] |
| `StderrLogger::log` | method | `fn log(&self, record: &log::Record<'_>) {` | `StderrLogger::log [method]` | `396f55d1-22db-5f92-9b10-c8908210073f` | 15-19 [crates/gcode/src/dispatch.rs:15-19] | Indexed method `StderrLogger::log` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:15-19] |
| `StderrLogger::flush` | method | `fn flush(&self) {}` | `StderrLogger::flush [method]` | `1bbd68fd-8e89-55da-9283-3e831c777121` | 21-21 [crates/gcode/src/dispatch.rs:21] | Indexed method `StderrLogger::flush` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:21] |
| `init_logger` | function | `fn init_logger(quiet: bool) {` | `init_logger [function]` | `ab252d2e-fc3b-5ad8-b1f0-b7241e7efa2f` | 24-28 [crates/gcode/src/dispatch.rs:24-28] | Indexed function `init_logger` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:24-28] |
| `stderr_log_level` | function | `fn stderr_log_level(quiet: bool, rust_log: Option<&str>) -> log::LevelFilter {` | `stderr_log_level [function]` | `370f2735-75cf-5a9e-ab25-f05cb782fe67` | 30-37 [crates/gcode/src/dispatch.rs:30-37] | Indexed function `stderr_log_level` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:30-37] |
| `ensure_project_fresh` | function | `fn ensure_project_fresh(ctx: &config::Context, disabled: bool) -> anyhow::Result<()> {` | `ensure_project_fresh [function]` | `bc6b40ac-1c6f-5750-b1a5-34a9f37b8158` | 39-47 [crates/gcode/src/dispatch.rs:39-47] | Indexed function `ensure_project_fresh` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:39-47] |
| `ensure_files_fresh` | function | `fn ensure_files_fresh(` | `ensure_files_fresh [function]` | `029a8312-9dd7-5dc3-a5bb-b810ceecb892` | 49-61 [crates/gcode/src/dispatch.rs:49-61] | Indexed function `ensure_files_fresh` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:49-61] |
| `ensure_file_fresh` | function | `fn ensure_file_fresh(ctx: &config::Context, disabled: bool, file: &str) -> anyhow::Result<()> {` | `ensure_file_fresh [function]` | `998c5487-2667-5815-bdbd-1f410e0c2781` | 63-65 [crates/gcode/src/dispatch.rs:63-65] | Indexed function `ensure_file_fresh` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:63-65] |
| `ensure_symbol_fresh` | function | `fn ensure_symbol_fresh(ctx: &config::Context, disabled: bool, id: &str) -> anyhow::Result<()> {` | `ensure_symbol_fresh [function]` | `eec2bd7d-b774-5d4f-ba03-72ca48b941da` | 67-72 [crates/gcode/src/dispatch.rs:67-72] | Indexed function `ensure_symbol_fresh` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:67-72] |
| `warn_if_busy` | function | `fn warn_if_busy(ctx: &config::Context, status: freshness::FreshnessStatus) {` | `warn_if_busy [function]` | `842ac6aa-35d2-5a1b-b8bd-f032a923d79f` | 74-78 [crates/gcode/src/dispatch.rs:74-78] | Indexed function `warn_if_busy` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:74-78] |
| `service_config_selection` | function | `fn service_config_selection(command: &Command) -> config::ServiceConfigSelection {` | `service_config_selection [function]` | `9d1a225e-8c4f-53b5-ba2f-eba4be26d2cc` | 80-122 [crates/gcode/src/dispatch.rs:80-122] | Indexed function `service_config_selection` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:80-122] |
| `dispatch_early_command` | function | `fn dispatch_early_command<F>(` | `dispatch_early_command [function]` | `200cdcd8-4d44-5c05-8c4c-bb78e703ddaa` | 124-209 [crates/gcode/src/dispatch.rs:124-209] | Indexed function `dispatch_early_command` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:124-209] |
| `run_with_exit_code` | function | `pub(crate) fn run_with_exit_code() -> std::process::ExitCode {` | `run_with_exit_code [function]` | `2ee50031-ec25-5ce4-8bbc-276f046fd4a4` | 211-237 [crates/gcode/src/dispatch.rs:211-237] | Indexed function `run_with_exit_code` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:211-237] |
| `run` | function | `fn run() -> anyhow::Result<()> {` | `run [function]` | `dc3f8710-dcff-5f69-9f84-66661cd02d56` | 239-586 [crates/gcode/src/dispatch.rs:239-586] | Indexed function `run` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:239-586] |
