---
title: crates/gcore/src/lib.rs
type: code_file
provenance:
- file: crates/gcore/src/lib.rs
  ranges:
  - 27-34
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/lib.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Root library for the Gobby shared primitives crate. It exposes always-available modules for bootstrap, CLI contracts, daemon URLs, project/provisioning, config, AI/context types, backend setup, and related foundation code, while keeping datastore/search/indexing integrations behind feature gates so lightweight consumers avoid extra dependencies. The one utility function, `gobby_home`, resolves the app data directory by preferring `GOBBY_HOME` and otherwise falling back to `~/.gobby`, returning an error if no home directory can be determined. [crates/gcore/src/lib.rs:27-34]

## API Symbols

- `gobby_home` (function) component `gobby_home [function]` (`7be10c65-7ad1-53f1-b7f7-51baa21a6df7`) lines 27-34 [crates/gcore/src/lib.rs:27-34]
  - Signature: `pub fn gobby_home() -> anyhow::Result<std::path::PathBuf> {`
  - Purpose: Returns the 'GOBBY_HOME' environment variable as a 'PathBuf' if set, otherwise resolves the user’s home directory and appends '.gobby', failing with an error if no home directory can be determined. [crates/gcore/src/lib.rs:27-34]

