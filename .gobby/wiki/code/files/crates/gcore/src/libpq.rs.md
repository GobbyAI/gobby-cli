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

This file provides `split_keyword_dsn_tokens`, a small parser for PostgreSQL-style keyword DSN strings. It scans the input once, skipping leading whitespace, then splits on unescaped whitespace that occurs outside single-quoted sections while preserving backslash-escaped characters and quoted spaces. The function returns borrowed `&str` slices into the original URL string, so it can tokenize without allocating new substrings. [crates/gcore/src/libpq.rs:1-39]

## API Symbols

- `split_keyword_dsn_tokens` (function) component `split_keyword_dsn_tokens [function]` (`820514e7-917e-52ce-b2ae-db0371ba575e`) lines 1-39 [crates/gcore/src/libpq.rs:1-39]
  - Signature: `pub(crate) fn split_keyword_dsn_tokens(database_url: &str) -> Vec<&str> {`
  - Purpose: Splits a database URL/keyword DSN string into borrowed tokens by treating unescaped whitespace outside single-quoted sections as delimiters, while preserving backslash-escaped characters and quoted whitespace. [crates/gcore/src/libpq.rs:1-39]

