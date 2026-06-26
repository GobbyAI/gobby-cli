---
title: crates/gcore/src/ai/daemon/transport.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/transport.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/transport.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Overview

`crates/gcore/src/ai/daemon/transport.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcore/src/ai/daemon/transport.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `daemon_client` | function | This function instantiates an HTTP 'Client' using the builder pattern and maps any construction errors to 'AiError'. [crates/gcore/src/ai/daemon/transport.rs:8-12] |
| `daemon_url` | function | This function concatenates a provided path to a base daemon URL obtained from 'crate::daemon_url::daemon_url()' after removing any trailing slashes from the base URL. [crates/gcore/src/ai/daemon/transport.rs:14-20] |
| `read_local_cli_token` | function | Reads a CLI authentication token from a local file in the gobby home directory, returning the trimmed string if non-empty, otherwise returns an 'AiError'. [crates/gcore/src/ai/daemon/transport.rs:22-38] |
| `gobby_home` | function | Wraps the internal 'crate::gobby_home()' function and converts any errors into 'AiError::not_configured' variants. [crates/gcore/src/ai/daemon/transport.rs:40-42] |
| `with_local_token` | function | Adds the provided token as the 'LOCAL_TOKEN_HEADER' HTTP header to a 'RequestBuilder' and returns the modified builder for method chaining. [crates/gcore/src/ai/daemon/transport.rs:44-46] |

