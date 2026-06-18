---
title: crates/gcode/build.rs
type: code_file
provenance:
- file: crates/gcode/build.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/build.rs

Module: [[code/modules/crates/gcode|crates/gcode]]

## Overview
This file serves as the Cargo build script for the `gcode` crate, managing compile-time environment configuration and feature flags crates/gcode/build.rs:1-8. Its primary role is to set up conditional compilation based on the presence of a test database.

The script ensures that the build is re-evaluated whenever the `GCODE_POSTGRES_TEST_DATABASE_URL` environment variable changes crates/gcode/build.rs:2. It also registers the custom `gcode_postgres_tests` configuration flag with the compiler to prevent unexpected configuration warnings crates/gcode/build.rs:3. [crates/gcode/build.rs:1-8]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `main` | function | Emits Cargo build-script directives to rerun when 'GCODE_POSTGRES_TEST_DATABASE_URL' changes, register the 'gcode_postgres_tests' cfg for check-cfg, and enable that cfg when the environment variable is set. [crates/gcode/build.rs:1-8] |

