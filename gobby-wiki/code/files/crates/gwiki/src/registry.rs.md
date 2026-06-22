---
title: crates/gwiki/src/registry.rs
type: code_file
provenance:
- file: crates/gwiki/src/registry.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/registry.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/registry.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gwiki/src/registry.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Registry` | class | # Summary A public struct that maintains two ordered string-keyed mappings of 'TopicRegistration' and 'ProjectRegistration' objects with serde deserialization defaults. [crates/gwiki/src/registry.rs:15-20] |
| `TopicRegistration` | class | 'TopicRegistration' is a public struct containing two String fields—'name' and 'path'—for storing topic identification and location data. [crates/gwiki/src/registry.rs:23-26] |
| `ProjectRegistration` | class | # Summary 'ProjectRegistration' is a public struct that encapsulates three String fields—'project_id', 'project_root', and 'path'—to represent project metadata and file system location information. [crates/gwiki/src/registry.rs:29-33] |
| `register_scope` | function | # Summary Registers a ResolvedScope (Topic or Project variant) to a filesystem-based registry using file locking and atomic JSON serialization. [crates/gwiki/src/registry.rs:35-102] |
| `lock_registry` | function | Acquires an exclusive file lock via 'fs4' using exponential backoff retries up to a configured timeout, returning 'Ok' on success or 'WikiError' on timeout or IO error. [crates/gwiki/src/registry.rs:104-136] |
| `registry_lock_initial_delay` | function | This function returns a 25-millisecond 'Duration' representing the initial delay for registry lock acquisition. [crates/gwiki/src/registry.rs:138-140] |
| `next_registry_lock_delay` | function | This function computes an exponential backoff delay by doubling the input duration using saturating multiplication, then capping the result at a maximum of 250 milliseconds. [crates/gwiki/src/registry.rs:142-144] |
| `write_registry_atomically` | function | Writes byte contents to a file atomically via temporary file creation, explicit fsync operations, and atomic rename to ensure crash-safe persistence. [crates/gwiki/src/registry.rs:146-184] |
| `temp_registry_path` | function | Generates a unique temporary file path by appending the process ID, an atomically-incremented counter, and the current Unix timestamp in nanoseconds to the input filename. [crates/gwiki/src/registry.rs:186-203] |
| `registry_lock_path` | function | Constructs and returns a lock file path by appending '.lock' to the filename component of the input path, defaulting to '"wikis.json"' if no filename exists. [crates/gwiki/src/registry.rs:205-211] |
| `read_registry` | function | # Summary The 'read_registry' function deserializes a JSON registry file from the specified path into a 'Registry' struct, returning a default 'Registry' instance if the file is not found, or a 'WikiError' if file I/O or JSON parsing fails. [crates/gwiki/src/registry.rs:213-225] |

_Verified by 3 in-file unit tests._

