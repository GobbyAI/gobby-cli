---
title: crates/gcore/src/config/tests.rs
type: code_file
provenance:
- file: crates/gcore/src/config/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config/tests.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Overview

`crates/gcore/src/config/tests.rs` exposes 26 indexed API symbols.

## How it fits

`crates/gcore/src/config/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TestLogger` | class | Indexed class `TestLogger` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:5-7] |
| `TestLogger::clear` | method | Indexed method `TestLogger::clear` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:15-17] |
| `TestLogger::records` | method | Indexed method `TestLogger::records` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:19-21] |
| `TestLogger::lock_records` | method | Indexed method `TestLogger::lock_records` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:23-27] |
| `TestLogger::enabled` | method | Indexed method `TestLogger::enabled` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:31-33] |
| `TestLogger::log` | method | Indexed method `TestLogger::log` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:35-40] |
| `TestLogger::flush` | method | Indexed method `TestLogger::flush` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:42] |
| `capture_warn_logs` | function | Indexed function `capture_warn_logs` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:45-53] |
| `EnvGuard` | class | Indexed class `EnvGuard` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:57-59] |
| `EnvGuard::new` | method | Indexed method `EnvGuard::new` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:62-70] |
| `EnvGuard::clear` | method | Indexed method `EnvGuard::clear` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:72-88] |
| `EnvGuard::set` | method | Indexed method `EnvGuard::set` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:90-93] |
| `EnvGuard::drop` | method | Indexed method `EnvGuard::drop` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:97-99] |
| `TestSource` | class | Indexed class `TestSource` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:103-106] |
| `TestSource::with_values` | method | Indexed method `TestSource::with_values` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:109-117] |
| `TestSource::with_raw_values` | method | Indexed method `TestSource::with_raw_values` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:119-127] |
| `TestSource::config_value` | method | Indexed method `TestSource::config_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:131-133] |
| `TestSource::resolve_value` | method | Indexed method `TestSource::resolve_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:135-141] |
| `FailingResolveSource` | class | Indexed class `FailingResolveSource` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:145-148] |
| `FailingResolveSource::with_values_and_failures` | method | Indexed method `FailingResolveSource::with_values_and_failures` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:151-162] |
| `FailingResolveSource::config_value` | method | Indexed method `FailingResolveSource::config_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:166-168] |
| `FailingResolveSource::resolve_value` | method | Indexed method `FailingResolveSource::resolve_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:170-175] |
| `LayeredTestSource` | class | Indexed class `LayeredTestSource` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:179-182] |
| `LayeredTestSource::with_layers` | method | Indexed method `LayeredTestSource::with_layers` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:185-193] |
| `LayeredTestSource::config_value` | method | Indexed method `LayeredTestSource::config_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:197-201] |
| `LayeredTestSource::resolve_value` | method | Indexed method `LayeredTestSource::resolve_value` in `crates/gcore/src/config/tests.rs`. [crates/gcore/src/config/tests.rs:203-205] |

