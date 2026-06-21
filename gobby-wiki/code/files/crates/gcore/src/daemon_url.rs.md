---
title: crates/gcore/src/daemon_url.rs
type: code_file
provenance:
- file: crates/gcore/src/daemon_url.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/daemon_url.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/daemon_url.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gcore/src/daemon_url.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `daemon_url` | function | Returns a daemon URL string determined by the GOBBY_DAEMON_URL and GOBBY_PORT environment variables, or falls back to converting the configured daemon endpoint if those variables are unset. [crates/gcore/src/daemon_url.rs:28-34] |
| `daemon_url_at` | function | This function reads a daemon endpoint from the specified filesystem path and converts it to a URL string. [crates/gcore/src/daemon_url.rs:40-42] |
| `env_override` | function | This function returns a trimmed URL (with trailing slashes removed) if provided and non-empty, otherwise constructs and returns 'http://127.0.0.1:{port}' if the port parameter parses successfully as a u16, or None if both inputs are invalid. [crates/gcore/src/daemon_url.rs:47-59] |
| `endpoint_to_url` | function | Constructs an HTTP URL string from a 'DaemonEndpoint' by resolving its host through 'dial_host()' and combining it with the port number. [crates/gcore/src/daemon_url.rs:61-64] |
| `dial_host` | function | Normalizes a host address by converting wildcard/unspecified forms (empty, 0.0.0.0, ::, ::0, [::]) to 127.0.0.1, wrapping bare IPv6 addresses in brackets, and otherwise returning the input unchanged, using Cow<'_, str> to minimize allocations. [crates/gcore/src/daemon_url.rs:72-78] |
| `write_bootstrap` | function | Creates a temporary directory, writes the provided string contents to a 'bootstrap.yaml' file within it, and returns a tuple containing the 'TempDir' handle and the resulting file 'PathBuf'. [crates/gcore/src/daemon_url.rs:86-91] |

_Verified by 14 in-file unit tests._

