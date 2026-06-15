---
title: crates/gcode/src/cli
type: code_module
provenance:
- file: crates/gcode/src/cli/tests.rs
  ranges:
  - 1-9
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

This module contains the CLI-focused test harness for the `gcode` crate. Its visible responsibility is to bring the parent CLI definitions into scope and import the `clap` traits needed to construct and parse command definitions during tests, via `use super::*` and `use clap::{CommandFactory, Parser};` [crates/gcode/src/cli/tests.rs:1-2].

The module delegates actual behavioral coverage to focused test submodules rather than defining tests inline. Those submodules cover command areas for `codewiki`, `grep`, `projection`, `search`, and top-level CLI behavior, letting the CLI test suite stay organized around command surfaces while sharing the same parent imports and CLI context [crates/gcode/src/cli/tests.rs:4-8].

## Files

- [[code/files/crates/gcode/src/cli/tests.rs|crates/gcode/src/cli/tests.rs]] - CLI test module for the `gcode` crate. It imports the CLI definitions and `clap` helpers, then organizes the test suite into submodules for `codewiki`, `grep`, `projection`, `search`, and `top_level` command behavior. [crates/gcode/src/cli/tests.rs:1-9]

