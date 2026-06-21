---
title: crates/gwiki/src/error.rs
type: code_file
provenance:
- file: crates/gwiki/src/error.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/error.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/error.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gwiki/src/error.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiError` | type | Indexed type `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:10-66] |
| `WikiError::code` | method | Returns a static string error code identifier by matching the enum variant to its corresponding string literal. [crates/gwiki/src/error.rs:69-86] |
| `WikiError::is_ffmpeg_unavailable` | method | This method determines whether an error represents ffmpeg unavailability by returning true if it matches a Config variant with "ffmpeg executable not found on PATH" detail or an Io variant with "run ffmpeg" action and NotFound error kind. [crates/gwiki/src/error.rs:88-99] |
| `WikiError::fmt` | method | Implements the 'Display' trait for an error enum by pattern-matching on each variant and writing formatted error messages with associated error codes to the provided formatter. [crates/gwiki/src/error.rs:103-158] |
| `format_action_error` | function | 'format_action_error' writes a formatted error message to a 'Formatter' that includes an action name, optional file path, error source, and error code. [crates/gwiki/src/error.rs:161-176] |
| `WikiError::source` | method | Returns an optional reference to the underlying 'std::error::Error' source for error variants that encapsulate one (Io, Json, Yaml, Index, Search, Setup), or 'None' for others. [crates/gwiki/src/error.rs:179-189] |
| `WikiError::from` | method | This method implements the 'From' trait to convert an 'indexer::IndexError' into 'Self' by wrapping it in the 'Index' enum variant with the error stored in the 'source' field. [crates/gwiki/src/error.rs:193-195] |
| `WikiError::from` | method | Implements the 'From' trait to convert 'search::SearchError' into 'Self' by wrapping it in the 'Search' enum variant with a 'source' field. [crates/gwiki/src/error.rs:199-201] |
| `WikiError::from` | method | This method implements the 'From' trait to convert a 'SetupError' into the implementing enum type by constructing a 'Setup' variant with the error wrapped in the 'source' field. [crates/gwiki/src/error.rs:205-207] |

_Verified by 5 in-file unit tests._

