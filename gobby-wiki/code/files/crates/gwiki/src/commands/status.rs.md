---
title: crates/gwiki/src/commands/status.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/status.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/status.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/status.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/status.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the command scope from the provided 'ScopeSelection' and then renders the resolved scope identity, returning either a 'CommandOutcome' or a 'WikiError'. [crates/gwiki/src/commands/status.rs:6-9] |
| `render` | function | Builds a 'CommandOutcome' for the 'status' command by querying the daemon URL and runtime status, assembling them with the provided 'scope' into a JSON payload and formatted text, and wrapping both via 'super::scoped_outcome'. [crates/gwiki/src/commands/status.rs:11-30] |
| `RuntimeStatus` | class | 'RuntimeStatus' is a crate-visible struct that represents a runtime state snapshot with two static string fields, 'status' and 'mode', plus a 'serde_json::Value' payload for 'services'. [crates/gwiki/src/commands/status.rs:32-36] |
| `runtime_status_for` | function | Returns a 'RuntimeStatus' that reports 'shell-ready' in 'memory' mode when no database URL is available, otherwise establishes a read-only PostgreSQL connection, resolves runtime config from Gobby home, and returns 'datastore-ready' in 'postgres' mode with JSON status for Postgres, FalkorDB, Qdrant, and embeddings. [crates/gwiki/src/commands/status.rs:38-88] |
| `gobby_home` | function | Returns the 'gobby_core::gobby_home()' path as a 'Result<PathBuf, WikiError>', mapping any resolution failure into 'WikiError::Config' with a formatted '"failed to resolve Gobby home for gwiki status: {error}"' detail. [crates/gwiki/src/commands/status.rs:90-94] |

