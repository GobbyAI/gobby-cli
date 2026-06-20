---
title: crates/ghook/src/transport.rs
type: code_file
provenance:
- file: crates/ghook/src/transport.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/transport.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/transport.rs` exposes 23 indexed API symbols.

## How it fits

`crates/ghook/src/transport.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DeliveryOutcome` | type | Indexed type `DeliveryOutcome` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:31-36] |
| `DeliveryFailureKind` | type | Indexed type `DeliveryFailureKind` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:40-45] |
| `DeliveryReport` | class | The 'DeliveryReport' struct represents the outcome of a delivery attempt, encapsulating its delivery outcome, optional failure classification, HTTP status code, response body, and transport-level error details. [crates/ghook/src/transport.rs:49-55] |
| `inbox_dir` | function | The 'inbox_dir' function returns a 'Result' containing the 'PathBuf' path to the 'hooks/inbox' directory located within the Gobby home directory. [crates/ghook/src/transport.rs:58-60] |
| `quarantine_dir` | function | The 'quarantine_dir' function returns a 'Result' containing the 'PathBuf' for the "quarantine" subdirectory nested within the directory path returned by 'inbox_dir()'. [crates/ghook/src/transport.rs:63-65] |
| `ts13` | function | The 'ts13' function returns a 13-character, zero-padded string representing the current system time in milliseconds elapsed since the Unix epoch. [crates/ghook/src/transport.rs:68-74] |
| `envelope_filename` | function | The 'envelope_filename' function generates and returns a JSON filename string formatted as '{prefix}-{timestamp}-{uuid}.json', where the prefix is 'c' if 'critical' is true or 'n' otherwise, the timestamp is obtained from 'ts13()', and the UUID is a newly generated version 4 UUID. [crates/ghook/src/transport.rs:77-81] |
| `atomic_write` | function | The 'atomic_write' function atomically writes data to a target path by creating any missing parent directories, writing and fsyncing the bytes to a temporary '.tmp' file, renaming that temporary file to the final path, and performing a best-effort fsync on the parent directory. [crates/ghook/src/transport.rs:87-114] |
| `enqueue_to` | function | The 'enqueue_to' function serializes a given 'Envelope' to pretty-printed JSON and atomically writes it to a file path generated from the 'inbox' directory and the envelope's criticality-based filename, returning the resulting 'PathBuf' on success. [crates/ghook/src/transport.rs:119-125] |
| `envelope_id_from_path` | function | The function extracts and returns the file stem of a given path as an optional string slice, returning 'None' if the file stem is missing or does not contain valid UTF-8. [crates/ghook/src/transport.rs:127-129] |
| `post_and_cleanup` | function | This function serializes a given 'Envelope' to a JSON string, POSTs it to a daemon endpoint with the envelope's headers and ID, deletes the file at 'enqueued_path' if the request completes with a successful 2xx status code, and returns a 'DeliveryReport' detailing the outcome. [crates/ghook/src/transport.rs:137-204] |
| `classify_transport_error` | function | This function classifies a 'ureq::Transport' error and its accompanying text into a specific 'DeliveryFailureKind' enum variant by mapping connection, DNS, and proxy failures to 'Connect', timeout-related substrings to 'Timeout', and any other failures to 'Other'. [crates/ghook/src/transport.rs:206-221] |
| `quarantine_malformed` | function | The 'quarantine_malformed' function resolves the default quarantine directory and saves malformed input bytes, their associated JSON error description, and criticality flag to that directory, returning the file path of the quarantined data. [crates/ghook/src/transport.rs:225-232] |
| `quarantine_malformed_at` | function | The function base64-encodes malformed stdin bytes and atomically writes them, along with associated parsing error metadata, into uniquely named, criticality-prefixed JSON and metadata files within the specified directory, returning the path to the written body file. [crates/ghook/src/transport.rs:242-273] |

_Verified by 9 in-file unit tests._

