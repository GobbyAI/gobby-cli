---
title: crates/gwiki/src/commands/session_sync.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/session_sync.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/session_sync.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/session_sync.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/session_sync.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the command scope, initializes vault paths, determines the archive directory and timestamp, syncs session transcript archives into either Postgres-backed or in-memory storage depending on database availability, conditionally refreshes vector and graph indexes for accepted items, and returns a rendered sync outcome with index counts. [crates/gwiki/src/commands/session_sync.rs:22-70] |
| `archive_dir_or_default` | function | Returns the provided archive directory unchanged, or otherwise resolves 'gobby_core::gobby_home()' and appends 'session_transcripts', converting any home-resolution failure into 'WikiError::Config' with a formatted detail message. [crates/gwiki/src/commands/session_sync.rs:72-83] |
| `render_sync_sessions` | function | 'render_sync_sessions' builds a structured JSON payload and human-readable summary for a 'sync-sessions' command by serializing accepted, skipped, and failed session-archive ingest results along with scope, archive metadata, scan counts, and index counts into a 'CommandOutcome'. [crates/gwiki/src/commands/session_sync.rs:85-162] |

