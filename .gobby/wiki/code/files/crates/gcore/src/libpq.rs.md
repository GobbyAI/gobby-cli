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

# crates/gcore/src/libpq.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file provides a single helper for parsing libpq-style keyword DSN strings into whitespace-separated tokens while respecting quoting and escaping. `split_keyword_dsn_tokens` scans the input by character index, skips leading whitespace, tracks whether it is inside single quotes, honors backslash escapes, and only splits on whitespace when not quoted. It returns string slices into the original DSN so callers can process the parsed tokens without allocating new substrings. [crates/gcore/src/libpq.rs:1-39]

## API Symbols

- `split_keyword_dsn_tokens` (function) component `split_keyword_dsn_tokens [function]` (`820514e7-917e-52ce-b2ae-db0371ba575e`) lines 1-39 [crates/gcore/src/libpq.rs:1-39]
  - Signature: `pub(crate) fn split_keyword_dsn_tokens(database_url: &str) -> Vec<&str> {`
  - Purpose: Indexed function `split_keyword_dsn_tokens` in `crates/gcore/src/libpq.rs`. [crates/gcore/src/libpq.rs:1-39]

