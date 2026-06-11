---
title: crates/gwiki/src/events.rs
type: code_file
provenance:
- file: crates/gwiki/src/events.rs
  ranges:
  - 14-20
  - 23-25
  - 27-75
  - 28-32
  - 34-74
  - 77-105
  - 114-147
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/events.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/events.rs` exposes 7 indexed API symbols.
[crates/gwiki/src/events.rs:14-20]
[crates/gwiki/src/events.rs:23-25]
[crates/gwiki/src/events.rs:27-75]
[crates/gwiki/src/events.rs:28-32]
[crates/gwiki/src/events.rs:34-74]

## API Symbols

- `SessionEvent` (class) component `SessionEvent [class]` (`c9fd7598-f0e1-5081-a47e-61304fa867c9`) lines 14-20 [crates/gwiki/src/events.rs:14-20]
  - Signature: `pub struct SessionEvent {`
  - Purpose: # SessionEvent

`SessionEvent` is a struct that encapsulates a categorized message event scoped to a session with an optional dispatch association and millisecond-precision timestamp. [crates/gwiki/src/events.rs:14-20]
- `EventMonitor` (class) component `EventMonitor [class]` (`b79a58ed-9c21-55c1-88c6-27b6c2beab5b`) lines 23-25 [crates/gwiki/src/events.rs:23-25]
  - Signature: `pub struct EventMonitor {`
  - Purpose: `EventMonitor` is a public Rust struct that wraps a `PathBuf` to represent a file system path used for monitoring events. [crates/gwiki/src/events.rs:23-25]
- `EventMonitor` (class) component `EventMonitor [class]` (`508d296c-5da1-543a-9c88-dfe3f0c8a135`) lines 27-75 [crates/gwiki/src/events.rs:27-75]
  - Signature: `impl EventMonitor {`
  - Purpose: **EventMonitor appends SessionEvent objects to a JSONL log file with advisory file locking and fsync-guaranteed durability.** [crates/gwiki/src/events.rs:27-75]
- `EventMonitor.for_vault` (method) component `EventMonitor.for_vault [method]` (`c4e3c11e-651e-5645-8d8d-977b7467acaf`) lines 28-32 [crates/gwiki/src/events.rs:28-32]
  - Signature: `pub fn for_vault(vault_root: &Path) -> Self {`
  - Purpose: This factory method constructs an instance with the `path` field set to `.gwiki/session-events.jsonl` relative to the provided vault root directory. [crates/gwiki/src/events.rs:28-32]
- `EventMonitor.append_event` (method) component `EventMonitor.append_event [method]` (`74434d8d-c267-57e9-9b96-c435808a0a78`) lines 34-74 [crates/gwiki/src/events.rs:34-74]
  - Signature: `pub fn append_event(&self, event: &SessionEvent) -> Result<(), WikiError> {`
  - Purpose: Serializes and appends a SessionEvent as a newline-delimited JSON entry to a locked log file with fsync durability guarantees. [crates/gwiki/src/events.rs:34-74]
- `lock_event_log` (function) component `lock_event_log [function]` (`6e6fb070-3347-53ea-a4ce-88fc7cf80a01`) lines 77-105 [crates/gwiki/src/events.rs:77-105]
  - Signature: `fn lock_event_log(file: &fs::File, path: &Path) -> Result<(), WikiError> {`
  - Purpose: Attempts to acquire an exclusive lock on an event log file using polling with a configurable timeout, returning a `WikiError` if the lock cannot be obtained within the time limit or if a lock error occurs. [crates/gwiki/src/events.rs:77-105]
- `events_append_jsonl` (function) component `events_append_jsonl [function]` (`1f193b69-c5b2-5395-a4cf-335016f1f569`) lines 114-147 [crates/gwiki/src/events.rs:114-147]
  - Signature: `fn events_append_jsonl() {`
  - Purpose: Tests that `EventMonitor.append_event()` persists `SessionEvent` objects as newline-delimited JSON with correct field serialization and integrity. [crates/gwiki/src/events.rs:114-147]

