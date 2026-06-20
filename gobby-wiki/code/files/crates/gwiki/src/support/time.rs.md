---
title: crates/gwiki/src/support/time.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/time.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/time.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/time.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/support/time.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `collect_timestamp` | function | Returns the current Unix timestamp in milliseconds, formatted as 'unix-ms:<millis>', or propagates a 'WikiError' if timestamp retrieval fails. [crates/gwiki/src/support/time.rs:3-6] |
| `unix_timestamp_ms` | function | Returns the current system time as milliseconds since the Unix epoch, or a 'WikiError::Config' if the clock is before the epoch or the millisecond count does not fit in 'u64'. [crates/gwiki/src/support/time.rs:8-17] |

_Verified by 1 in-file unit test._

