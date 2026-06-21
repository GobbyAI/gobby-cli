---
title: crates/gcore/src/bootstrap.rs
type: code_file
provenance:
- file: crates/gcore/src/bootstrap.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/bootstrap.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/bootstrap.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcore/src/bootstrap.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DaemonEndpoint` | class | 'DaemonEndpoint' is a public struct that encapsulates a daemon's network address, consisting of a 'String' host and a 'u16' port number. [crates/gcore/src/bootstrap.rs:33-36] |
| `DaemonEndpoint::default` | method | Instantiates a default configuration object with the host set to 'DEFAULT_BIND_HOST' (converted to String) and port set to 'DEFAULT_DAEMON_PORT'. [crates/gcore/src/bootstrap.rs:39-44] |
| `bootstrap_path` | function | This function returns an 'Option<PathBuf>' to the bootstrap file located in the gobby home directory, or 'None' if the home directory path resolution fails. [crates/gcore/src/bootstrap.rs:52-54] |
| `read_daemon_endpoint` | function | Retrieves a DaemonEndpoint by reading from a bootstrap path if available, or returns the default DaemonEndpoint instance if the path does not exist. [crates/gcore/src/bootstrap.rs:60-65] |
| `read_daemon_endpoint_at` | function | Reads a YAML configuration file from the given path and constructs a 'DaemonEndpoint' by extracting 'daemon_port' and 'bind_host' fields, returning default values if the file is inaccessible, malformed, or fields are missing/invalid. [crates/gcore/src/bootstrap.rs:71-92] |

_Verified by 8 in-file unit tests._

