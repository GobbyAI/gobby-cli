---
title: crates/gcore/src/lib.rs
type: code_file
provenance:
- file: crates/gcore/src/lib.rs
  ranges:
  - 25-32
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/lib.rs:25-32](crates/gcore/src/lib.rs#L25-L32)

</details>

# crates/gcore/src/lib.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This crate is the shared core for Gobby CLI tools, exposing always-available modules for bootstrap, CLI contracts, daemon URLs, project handling, provisioning, config, setup, and lightweight AI/foundation types. It keeps heavier datastore and indexing integrations behind feature gates so small consumers only pull in the primitives they need. The `gobby_home` helper centralizes home-directory discovery by honoring `GOBBY_HOME` first and otherwise falling back to `~/.gobby`, providing the common base path used by the rest of the crate. [crates/gcore/src/lib.rs:25-32]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `gobby_home` | function | `pub fn gobby_home() -> anyhow::Result<std::path::PathBuf> {` | `gobby_home [function]` | `449e84dc-0571-5b91-b75d-250efb86d0a6` | 25-32 [crates/gcore/src/lib.rs:25-32] | Indexed function `gobby_home` in `crates/gcore/src/lib.rs`. [crates/gcore/src/lib.rs:25-32] |
