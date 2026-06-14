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

Shared foundation crate for Gobby CLI tools. It exposes the always-available primitives for bootstrap, CLI contracts, daemon URLs, project handling, provisioning, config, and local backend/setup logic, while keeping heavier datastore and indexing integrations behind feature flags. The one concrete utility here is `gobby_home`, which resolves the Gobby home directory by honoring `GOBBY_HOME` first and otherwise falling back to `~/.gobby`, so the rest of the crate can share a consistent state location. [crates/gcore/src/lib.rs:27-34]

## API Symbols

- `gobby_home` (function) component `gobby_home [function]` (`7be10c65-7ad1-53f1-b7f7-51baa21a6df7`) lines 27-34 [crates/gcore/src/lib.rs:27-34]
  - Signature: `pub fn gobby_home() -> anyhow::Result<std::path::PathBuf> {`
  - Purpose: Indexed function `gobby_home` in `crates/gcore/src/lib.rs`. [crates/gcore/src/lib.rs:27-34]

