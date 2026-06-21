---
title: crates/gwiki/src/video/timestamps.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/timestamps.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video/timestamps.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/video/timestamps.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gwiki/src/video/timestamps.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `transcript_start_seconds` | function | Converts a transcript segment's start time from milliseconds to seconds, returning a u32 value saturated at u32::MAX to prevent overflow. [crates/gwiki/src/video/timestamps.rs:3-6] |
| `parse_timestamp_seconds` | function | This function parses a colon-delimited timestamp string (supporting HH:MM:SS, MM:SS, or SS formats) and returns the total duration in seconds as a u32, or None if parsing fails or checked arithmetic overflows. [crates/gwiki/src/video/timestamps.rs:8-23] |
| `parse_timestamp_part` | function | Parses the integer seconds component of a timestamp string (extracting the substring before the first decimal point, trimming whitespace) and returns it as 'u32', or 'None' if parsing fails. [crates/gwiki/src/video/timestamps.rs:25-32] |
| `format_timestamp` | function | This function converts a u32 representing total seconds into a zero-padded HH:MM:SS duration string. [crates/gwiki/src/video/timestamps.rs:34-39] |
| `format_ranges_ms` | function | Transforms a slice of 'TranscriptionRange' objects into a comma-separated string where each range is formatted as "start_ms-end_ms". [crates/gwiki/src/video/timestamps.rs:41-47] |

