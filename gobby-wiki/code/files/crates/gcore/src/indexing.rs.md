---
title: crates/gcore/src/indexing.rs
type: code_file
provenance:
- file: crates/gcore/src/indexing.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/indexing.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/indexing.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gcore/src/indexing.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WalkerSettings` | class | WalkerSettings is a configuration struct that parameterizes filesystem traversal with a root directory, gitignore respect flag, optional maximum file size filter, and custom ignore patterns. [crates/gcore/src/indexing.rs:17-26] |
| `WalkerSettings::new` | method | This constructor creates a new instance with the provided root path (converted to 'PathBuf') and default configuration: gitignore respect enabled, no file size limit, and an empty extra ignores list. [crates/gcore/src/indexing.rs:30-37] |
| `WalkerSettings::into_walker` | method | This method consumes 'self' and converts it into a 'WalkBuilder' by unwrapping the result of 'try_into_walker()', panicking if the conversion fails due to an invalid extra ignore pattern. [crates/gcore/src/indexing.rs:43-46] |
| `WalkerSettings::try_into_walker` | method | Constructs a WalkBuilder configured with git ignore settings, maximum file size limits, and negated extra ignore pattern overrides. [crates/gcore/src/indexing.rs:49-66] |
| `content_hash` | function | This function returns the hexadecimal-encoded SHA-256 hash of the input byte slice. [crates/gcore/src/indexing.rs:70-74] |
| `file_content_hash` | function | Computes the SHA256 cryptographic hash of a file's contents and returns it as a hexadecimal-encoded string, using buffered streaming reads to efficiently handle files of arbitrary size. [crates/gcore/src/indexing.rs:77-91] |
| `hex_digest` | function | Encodes a byte slice as a lowercase hexadecimal string with zero-padded two-digit representation per byte. [crates/gcore/src/indexing.rs:93-100] |
| `Chunk` | class | The 'Chunk' struct represents a byte-range-delimited segment of a source file, identified by its file path and start/end byte offsets, with optional heading and opaque domain-specific metadata. [crates/gcore/src/indexing.rs:104-115] |
| `ChunkIdentity` | class | 'ChunkIdentity' is a struct that identifies a contiguous byte range within a source file by storing the file path and inclusive/exclusive byte offset boundaries. [crates/gcore/src/indexing.rs:119-126] |
| `Chunk::identity` | method | The 'identity' method returns a new 'ChunkIdentity' struct containing the chunk's file path (cloned) and byte range boundaries (start and end positions). [crates/gcore/src/indexing.rs:130-136] |
| `IndexEvent` | type | Indexed type `IndexEvent` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:141-147] |
| `index_events_from_hashes` | function | Compares two file path-to-hash mappings and generates a vector of IndexEvent objects classifying each path's status as Added, Changed, Unchanged, or Deleted based on presence and hash equality. [crates/gcore/src/indexing.rs:150-173] |
| `write_file` | function | Writes a byte slice to a file at the path formed by joining a root directory with a relative path component, creating all necessary parent directories if they don't exist. [crates/gcore/src/indexing.rs:183-189] |
| `rels` | function | This function recursively enumerates files in a directory tree using a configured walker, strips the root path prefix from each file's path, and returns a sorted vector of relative path strings. [crates/gcore/src/indexing.rs:191-208] |

_Verified by 10 in-file unit tests._

