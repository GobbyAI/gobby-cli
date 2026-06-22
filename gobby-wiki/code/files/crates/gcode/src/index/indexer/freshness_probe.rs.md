---
title: crates/gcode/src/index/indexer/freshness_probe.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/freshness_probe.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/freshness_probe.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/freshness_probe.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/freshness_probe.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `project_changed_since` | function | Returns 'true' if any discovered file under 'project_root' has a modification time newer than 'last_indexed_at' minus 'SKEW_MARGIN', if any file’s metadata or mtime cannot be read, or if any previously indexed path no longer exists on disk. [crates/gcode/src/index/indexer/freshness_probe.rs:37-81] |
| `write_file` | function | Joins 'rel' to 'root', creates any missing parent directories, writes 'contents' to the resulting path, and returns that 'PathBuf'. [crates/gcode/src/index/indexer/freshness_probe.rs:89-96] |
| `set_mtime` | function | Opens the file at 'path' with write access and updates its last-modified timestamp to 'time', panicking if either the open or timestamp update fails. [crates/gcode/src/index/indexer/freshness_probe.rs:98-105] |
| `base_time` | function | Returns a 'SystemTime' equal to the Unix epoch plus '1_700_000_000' seconds, i.e. a fixed timestamp. [crates/gcode/src/index/indexer/freshness_probe.rs:109-111] |
| `default_options` | function | Returns the default 'walker::DiscoveryOptions' by invoking 'walker::DiscoveryOptions::default()'. [crates/gcode/src/index/indexer/freshness_probe.rs:113-115] |

_Verified by 6 in-file unit tests._

