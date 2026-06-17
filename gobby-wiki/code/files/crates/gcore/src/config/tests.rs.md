---
title: crates/gcore/src/config/tests.rs
type: code_file
provenance:
- file: crates/gcore/src/config/tests.rs
  ranges:
  - 5-7
  - 15-17
  - 19-21
  - 23-27
  - 31-33
  - 35-40
  - '42'
  - 45-53
  - 57-59
  - 62-70
  - 72-88
  - 90-93
  - 97-99
  - 103-106
  - 109-117
  - 119-127
  - 131-133
  - 135-141
  - 145-148
  - 151-162
  - 166-168
  - 170-175
  - 179-182
  - 185-193
  - 197-201
  - 203-205
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/config/tests.rs:5-7](crates/gcore/src/config/tests.rs#L5-L7), [crates/gcore/src/config/tests.rs:15-17](crates/gcore/src/config/tests.rs#L15-L17), [crates/gcore/src/config/tests.rs:19-21](crates/gcore/src/config/tests.rs#L19-L21), [crates/gcore/src/config/tests.rs:23-27](crates/gcore/src/config/tests.rs#L23-L27), [crates/gcore/src/config/tests.rs:31-33](crates/gcore/src/config/tests.rs#L31-L33), [crates/gcore/src/config/tests.rs:35-40](crates/gcore/src/config/tests.rs#L35-L40), [crates/gcore/src/config/tests.rs:42](crates/gcore/src/config/tests.rs#L42), [crates/gcore/src/config/tests.rs:45-53](crates/gcore/src/config/tests.rs#L45-L53), [crates/gcore/src/config/tests.rs:57-59](crates/gcore/src/config/tests.rs#L57-L59), [crates/gcore/src/config/tests.rs:62-70](crates/gcore/src/config/tests.rs#L62-L70), [crates/gcore/src/config/tests.rs:72-88](crates/gcore/src/config/tests.rs#L72-L88), [crates/gcore/src/config/tests.rs:90-93](crates/gcore/src/config/tests.rs#L90-L93), [crates/gcore/src/config/tests.rs:97-99](crates/gcore/src/config/tests.rs#L97-L99), [crates/gcore/src/config/tests.rs:103-106](crates/gcore/src/config/tests.rs#L103-L106), [crates/gcore/src/config/tests.rs:109-117](crates/gcore/src/config/tests.rs#L109-L117), [crates/gcore/src/config/tests.rs:119-127](crates/gcore/src/config/tests.rs#L119-L127), [crates/gcore/src/config/tests.rs:131-133](crates/gcore/src/config/tests.rs#L131-L133), [crates/gcore/src/config/tests.rs:135-141](crates/gcore/src/config/tests.rs#L135-L141), [crates/gcore/src/config/tests.rs:145-148](crates/gcore/src/config/tests.rs#L145-L148), [crates/gcore/src/config/tests.rs:151-162](crates/gcore/src/config/tests.rs#L151-L162), [crates/gcore/src/config/tests.rs:166-168](crates/gcore/src/config/tests.rs#L166-L168), [crates/gcore/src/config/tests.rs:170-175](crates/gcore/src/config/tests.rs#L170-L175), [crates/gcore/src/config/tests.rs:179-182](crates/gcore/src/config/tests.rs#L179-L182), [crates/gcore/src/config/tests.rs:185-193](crates/gcore/src/config/tests.rs#L185-L193), [crates/gcore/src/config/tests.rs:197-201](crates/gcore/src/config/tests.rs#L197-L201), [crates/gcore/src/config/tests.rs:203-205](crates/gcore/src/config/tests.rs#L203-L205)

</details>

# crates/gcore/src/config/tests.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Purpose

Test support for `gcore` config resolution: it defines a scoped test logger plus helper wrappers for manipulating process environment and synthetic config sources, so config tests can run deterministically without leaking state. `TestLogger` captures warn-level log records for assertions, `EnvGuard` locks and clears the relevant `GOBBY_*` variables for the duration of a test, and the `TestSource`, `FailingResolveSource`, and `LayeredTestSource` fixtures provide configurable value lookup, failure injection, and layered precedence behavior for exercising config resolution paths.
[crates/gcore/src/config/tests.rs:5-7]
[crates/gcore/src/config/tests.rs:15-17]
[crates/gcore/src/config/tests.rs:19-21]
[crates/gcore/src/config/tests.rs:23-27]
[crates/gcore/src/config/tests.rs:31-33]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `TestLogger` | class | `struct TestLogger {` | `TestLogger [class]` | `54cb1441-fd79-5d32-aeab-e474b688fac6` | 5-7 [crates/gcore/src/config/tests.rs:5-7] | Indexed class `TestLogger` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:5-7] |
| `TestLogger::clear` | method | `fn clear(&self) {` | `TestLogger::clear [method]` | `92582fd3-ff7d-5d8e-9422-a7a90d1604f2` | 15-17 [crates/gcore/src/config/tests.rs:15-17] | Indexed method `TestLogger::clear` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:15-17] |
| `TestLogger::records` | method | `fn records(&self) -> Vec<String> {` | `TestLogger::records [method]` | `5c02df42-a074-586e-a3ea-3a0cbeeb0846` | 19-21 [crates/gcore/src/config/tests.rs:19-21] | Indexed method `TestLogger::records` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:19-21] |
| `TestLogger::lock_records` | method | `fn lock_records(&self) -> std::sync::MutexGuard<'_, Vec<String>> {` | `TestLogger::lock_records [method]` | `961fbc47-ebad-5d6a-8a8c-34548ce70129` | 23-27 [crates/gcore/src/config/tests.rs:23-27] | Indexed method `TestLogger::lock_records` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:23-27] |
| `TestLogger::enabled` | method | `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {` | `TestLogger::enabled [method]` | `d1e1448c-9382-5b69-8362-44c6fd5766ad` | 31-33 [crates/gcore/src/config/tests.rs:31-33] | Indexed method `TestLogger::enabled` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:31-33] |
| `TestLogger::log` | method | `fn log(&self, record: &log::Record<'_>) {` | `TestLogger::log [method]` | `ac99cd84-a06a-546e-8814-3a2f3e441fb4` | 35-40 [crates/gcore/src/config/tests.rs:35-40] | Indexed method `TestLogger::log` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:35-40] |
| `TestLogger::flush` | method | `fn flush(&self) {}` | `TestLogger::flush [method]` | `2cb144b2-df30-5d8e-bbe9-a1cf1038ef41` | 42-42 [crates/gcore/src/config/tests.rs:42] | Indexed method `TestLogger::flush` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:42] |
| `capture_warn_logs` | function | `fn capture_warn_logs<R>(f: impl FnOnce() -> R) -> (R, Vec<String>) {` | `capture_warn_logs [function]` | `4eb74720-221b-5075-82f6-089342a162b3` | 45-53 [crates/gcore/src/config/tests.rs:45-53] | Indexed function `capture_warn_logs` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:45-53] |
| `EnvGuard` | class | `struct EnvGuard {` | `EnvGuard [class]` | `2ceee697-a9c3-5817-99b5-b62aef1c2bad` | 57-59 [crates/gcore/src/config/tests.rs:57-59] | Indexed class `EnvGuard` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:57-59] |
| `EnvGuard::new` | method | `fn new() -> Self {` | `EnvGuard::new [method]` | `e074357c-ef01-58c1-a8c0-3acf3ee71e7f` | 62-70 [crates/gcore/src/config/tests.rs:62-70] | Indexed method `EnvGuard::new` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:62-70] |
| `EnvGuard::clear` | method | `fn clear(&self) {` | `EnvGuard::clear [method]` | `60cb3fb2-36c2-55f4-8334-dadb66dd4fcf` | 72-88 [crates/gcore/src/config/tests.rs:72-88] | Indexed method `EnvGuard::clear` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:72-88] |
| `EnvGuard::set` | method | `fn set(&self, key: &str, value: &str) {` | `EnvGuard::set [method]` | `76d236dd-4b18-597b-9762-6cd1a648b42d` | 90-93 [crates/gcore/src/config/tests.rs:90-93] | Indexed method `EnvGuard::set` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:90-93] |
| `EnvGuard::drop` | method | `fn drop(&mut self) {` | `EnvGuard::drop [method]` | `2db841ce-8b56-5272-b030-fe174f4a797e` | 97-99 [crates/gcore/src/config/tests.rs:97-99] | Indexed method `EnvGuard::drop` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:97-99] |
| `TestSource` | class | `struct TestSource {` | `TestSource [class]` | `8cf2cea3-ba6a-5a53-8d6e-f63a464ac9c3` | 103-106 [crates/gcore/src/config/tests.rs:103-106] | Indexed class `TestSource` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:103-106] |
| `TestSource::with_values` | method | `fn with_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {` | `TestSource::with_values [method]` | `28f1b392-b583-5f76-9047-c0569952cb2c` | 109-117 [crates/gcore/src/config/tests.rs:109-117] | Indexed method `TestSource::with_values` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:109-117] |
| `TestSource::with_raw_values` | method | `fn with_raw_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {` | `TestSource::with_raw_values [method]` | `75d2732f-f203-5bf4-8e38-7dfddb316728` | 119-127 [crates/gcore/src/config/tests.rs:119-127] | Indexed method `TestSource::with_raw_values` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:119-127] |
| `TestSource::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `TestSource::config_value [method]` | `b7dd7640-4901-5a4e-b6de-eeca84269c62` | 131-133 [crates/gcore/src/config/tests.rs:131-133] | Indexed method `TestSource::config_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:131-133] |
| `TestSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `TestSource::resolve_value [method]` | `a37d2b42-e464-5a39-8980-2b8a3884868c` | 135-141 [crates/gcore/src/config/tests.rs:135-141] | Indexed method `TestSource::resolve_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:135-141] |
| `FailingResolveSource` | class | `struct FailingResolveSource {` | `FailingResolveSource [class]` | `f503cb76-08ae-5f84-9f98-e75ac6b41b55` | 145-148 [crates/gcore/src/config/tests.rs:145-148] | Indexed class `FailingResolveSource` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:145-148] |
| `FailingResolveSource::with_values_and_failures` | method | `fn with_values_and_failures(` | `FailingResolveSource::with_values_and_failures [method]` | `dc5edda0-e798-5cbc-89ae-69ccca023e87` | 151-162 [crates/gcore/src/config/tests.rs:151-162] | Indexed method `FailingResolveSource::with_values_and_failures` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:151-162] |
| `FailingResolveSource::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `FailingResolveSource::config_value [method]` | `71538b30-8720-5dd7-81ba-eb60ef17fbf2` | 166-168 [crates/gcore/src/config/tests.rs:166-168] | Indexed method `FailingResolveSource::config_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:166-168] |
| `FailingResolveSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `FailingResolveSource::resolve_value [method]` | `baba1a5e-e35b-54d6-b801-da11796794db` | 170-175 [crates/gcore/src/config/tests.rs:170-175] | Indexed method `FailingResolveSource::resolve_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:170-175] |
| `LayeredTestSource` | class | `struct LayeredTestSource {` | `LayeredTestSource [class]` | `0eee1644-d484-5829-ac94-ae4b3168f183` | 179-182 [crates/gcore/src/config/tests.rs:179-182] | Indexed class `LayeredTestSource` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:179-182] |
| `LayeredTestSource::with_layers` | method | `fn with_layers(` | `LayeredTestSource::with_layers [method]` | `93165376-8483-50e7-a129-13e47a69ec2e` | 185-193 [crates/gcore/src/config/tests.rs:185-193] | Indexed method `LayeredTestSource::with_layers` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:185-193] |
| `LayeredTestSource::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `LayeredTestSource::config_value [method]` | `2bb025b8-4abf-5fa6-a6d7-5b2576cf5075` | 197-201 [crates/gcore/src/config/tests.rs:197-201] | Indexed method `LayeredTestSource::config_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:197-201] |
| `LayeredTestSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `LayeredTestSource::resolve_value [method]` | `00fcb270-174d-5305-b915-713696c44cd6` | 203-205 [crates/gcore/src/config/tests.rs:203-205] | Indexed method `LayeredTestSource::resolve_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:203-205] |
