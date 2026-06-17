---
title: crates/gcore/src/libpq.rs
type: code_file
provenance:
- file: crates/gcore/src/libpq.rs
  ranges:
  - 1-39
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/libpq.rs:1-39](crates/gcore/src/libpq.rs#L1-L39)

</details>

# crates/gcore/src/libpq.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Provides a small parser for libpq-style keyword DSN strings by splitting a database URL into whitespace-delimited tokens while preserving quoted segments and backslash escapes. `split_keyword_dsn_tokens` scans the input once, tracks the start of each token, toggles single-quote state, honors escaped characters, and returns borrowed string slices for each parsed token. [crates/gcore/src/libpq.rs:1-39]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `split_keyword_dsn_tokens` | function | `pub(crate) fn split_keyword_dsn_tokens(database_url: &str) -> Vec<&str> {` | `split_keyword_dsn_tokens [function]` | `820514e7-917e-52ce-b2ae-db0371ba575e` | 1-39 [crates/gcore/src/libpq.rs:1-39] | Indexed function `split_keyword_dsn_tokens` in `crates/gcore/src/libpq.rs`. [crates/gcore/src/libpq.rs:1-39] |
