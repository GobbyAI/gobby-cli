---
title: crates/ghook/src/terminal_context.rs
type: code_file
provenance:
- file: crates/ghook/src/terminal_context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/terminal_context.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/terminal_context.rs` exposes 17 indexed API symbols.

## How it fits

`crates/ghook/src/terminal_context.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `capture` | function | Constructs and returns a 'Value' by passing the optional TMUX and TMUX_PANE environment variables to the 'build_context()' function. [crates/ghook/src/terminal_context.rs:18-23] |
| `enabled_for_hook` | function | Returns true if the provided hook_type string, after removing hyphens and underscores and converting to lowercase, equals "sessionstart". [crates/ghook/src/terminal_context.rs:25-32] |
| `build_context` | function | Constructs and returns a JSON object aggregating system and environment context including parent process ID, TTY name, validated tmux session/pane details, and gobby workflow metadata environment variables. [crates/ghook/src/terminal_context.rs:34-65] |
| `inject` | function | Conditionally inserts a "terminal_context" key-value pair into a mutable Value object by invoking 'capture()', only if the key does not already exist. [crates/ghook/src/terminal_context.rs:71-77] |
| `env_or_null` | function | Retrieves an environment variable by key, returning it as a 'Value::String' if present, or 'Value::Null' if the environment variable does not exist. [crates/ghook/src/terminal_context.rs:79-84] |
| `parent_pid_or_null` | function | Returns the calling process's parent process ID as a Value on Unix via unsafe 'libc::getppid()', or returns 'Value::Null' on Windows where direct parent-PID syscalls are unavailable. [crates/ghook/src/terminal_context.rs:86-102] |
| `tty_name_or_null` | function | Retrieves the terminal name of standard input (file descriptor 0) on Unix systems via 'libc::ttyname()', returning it as a 'Value::String' if successfully decoded as UTF-8 or 'Value::Null' otherwise, and unconditionally returns 'Value::Null' on Windows. [crates/ghook/src/terminal_context.rs:104-126] |
| `is_valid_tmux_pane` | function | Returns 'true' if and only if the input string matches the pattern '%[0-9]+' (a '%' character followed by one or more ASCII digits), validating tmux pane identifier format. [crates/ghook/src/terminal_context.rs:128-133] |
| `parse_tmux_socket_path` | function | Extracts the first comma-delimited token from the input string after trimming whitespace, returning 'Some(token)' if non-empty or 'None' otherwise. [crates/ghook/src/terminal_context.rs:138-145] |

_Verified by 8 in-file unit tests._

