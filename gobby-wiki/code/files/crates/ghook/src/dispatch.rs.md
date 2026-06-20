---
title: crates/ghook/src/dispatch.rs
type: code_file
provenance:
- file: crates/ghook/src/dispatch.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/dispatch.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/dispatch.rs` exposes 8 indexed API symbols.

## How it fits

`crates/ghook/src/dispatch.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run_gobby_owned` | function | This function orchestrates the dispatch of CLI hook executions by validating arguments, checking environment constraints and shutdown statuses, handling statusline updates, and resolving project context and stdin prior to background process detachment. [crates/ghook/src/dispatch.rs:16-179] |
| `hooks_disabled_by_env` | function | This function checks the environment variable 'GOBBY_HOOKS_DISABLED' and returns 'true' if it is set to '1', and 'false' otherwise. [crates/ghook/src/dispatch.rs:181-183] |
| `build_dispatch_envelope` | function | This function constructs and returns an 'Envelope' by conditionally injecting terminal context into the provided 'input_data', building a map of project and session HTTP headers if they are present, and resolving the payload's critical status and source via the 'CliConfig'. [crates/ghook/src/dispatch.rs:185-213] |
| `with_tmux_env` | function | This function thread-safely executes a closure within a temporary environment where the 'TMUX' and 'TMUX_PANE' environment variables are set to the provided optional values while holding a global environment lock. [crates/ghook/src/dispatch.rs:223-226] |

_Verified by 4 in-file unit tests._

