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

`crates/gcode/src/index/indexer/freshness_probe.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `project_changed_since` | function | Returns 'true' if any discovered file under 'project_root' has a modification time newer than 'last_indexed_at' minus 'SKEW_MARGIN', if any file’s metadata or mtime cannot be read, or if any previously indexed path no longer exists on disk. [crates/gcode/src/index/indexer/freshness_probe.rs:37-81] |
| `write_file` | function | Joins 'rel' to 'root', creates any missing parent directories, writes 'contents' to the resulting path, and returns that 'PathBuf'. [crates/gcode/src/index/indexer/freshness_probe.rs:89-96] |
| `set_mtime` | function | Opens the file at 'path' with write access and updates its last-modified timestamp to 'time', panicking if either the open or timestamp update fails. [crates/gcode/src/index/indexer/freshness_probe.rs:98-105] |
| `base_time` | function | Returns a 'SystemTime' equal to the Unix epoch plus '1_700_000_000' seconds, i.e. a fixed timestamp. [crates/gcode/src/index/indexer/freshness_probe.rs:109-111] |
| `default_options` | function | Returns the default 'walker::DiscoveryOptions' by invoking 'walker::DiscoveryOptions::default()'. [crates/gcode/src/index/indexer/freshness_probe.rs:113-115] |
| `reports_no_change_when_everything_predates_last_index` | function | Verifies that 'project_changed_since' returns 'false' when all indexed files have modification times earlier than 'last_indexed_at', indicating no project changes since the last index. [crates/gcode/src/index/indexer/freshness_probe.rs:118-138] |
| `reports_change_when_a_file_is_modified_after_last_index` | function | Creates a temporary project with an indexed 'src/lib.rs' whose modification time is advanced beyond the last index timestamp, then asserts that 'project_changed_since' returns 'true'. [crates/gcode/src/index/indexer/freshness_probe.rs:141-156] |
| `reports_change_for_newly_added_file` | function | It verifies that 'project_changed_since' returns 'true' when a newly created, unindexed file has an mtime newer than the 'last' timestamp, causing the modify/add scan to detect a change. [crates/gcode/src/index/indexer/freshness_probe.rs:159-176] |
| `reports_change_when_indexed_file_is_deleted` | function | Creates a temporary project where 'src/gone.rs' is listed as indexed but missing on disk, then asserts 'project_changed_since' returns 'true' for the given timestamp and index list. [crates/gcode/src/index/indexer/freshness_probe.rs:179-195] |
| `skew_margin_boundary_only_ever_makes_the_gate_more_eager` | function | Verifies that 'project_changed_since' treats an indexed file as changed only when its mtime falls strictly within the 2-second skew margin before 'last_indexed_at', while the exact margin boundary and older timestamps are considered unchanged. [crates/gcode/src/index/indexer/freshness_probe.rs:198-235] |
| `gitignored_new_files_follow_respect_gitignore_setting` | function | It verifies that 'project_changed_since' ignores a newly modified file matched by '.gitignore' when 'respect_gitignore' is 'true', but reports the project as changed when 'respect_gitignore' is 'false'. [crates/gcode/src/index/indexer/freshness_probe.rs:238-265] |

