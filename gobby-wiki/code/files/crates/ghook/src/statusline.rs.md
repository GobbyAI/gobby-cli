---
title: crates/ghook/src/statusline.rs
type: code_file
provenance:
- file: crates/ghook/src/statusline.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/statusline.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/statusline.rs` exposes 22 indexed API symbols.

## How it fits

`crates/ghook/src/statusline.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `is_statusline_hook` | function | This function returns a boolean indicating whether the provided CLI name is case-insensitively equal to "claude" and the hook type is exactly "statusline". [crates/ghook/src/statusline.rs:25-27] |
| `handle` | function | The 'handle' function retrieves an optional downstream command from the 'GOBBY_STATUSLINE_DOWNSTREAM' environment variable and the daemon URL, locks standard output, and delegates the raw standard input to 'handle_with' to return an 'ExitCode'. [crates/ghook/src/statusline.rs:29-35] |
| `handle_with` | function | The 'handle_with' function parses raw input bytes as a JSON object, extracts and transmits a payload to a daemon URL, forwards the original raw input to an optional downstream command while writing the resulting output to a mutable writer, and returns a successful exit code. [crates/ghook/src/statusline.rs:37-67] |
| `extract_payload` | function | The 'extract_payload' function validates the presence of a truthy 'session_id' within a JSON 'Value' and, if found, extracts and structures nested model, token cost, and context window metrics into a new JSON object with fallback default values. [crates/ghook/src/statusline.rs:69-104] |
| `post_to_daemon_best_effort` | function | This function concurrently posts a JSON payload to a daemon's statusline endpoint on a spawned thread and blocks the caller until the HTTP request completes or a join timeout is reached. [crates/ghook/src/statusline.rs:106-119] |
| `forward_downstream` | function | The 'forward_downstream' function executes a downstream shell command, utilizing spawned threads to concurrently write raw bytes to its standard input and read from its standard output, returning the captured output if the process terminates successfully within a specified timeout or terminating the process and returning 'None' upon timeout or error. [crates/ghook/src/statusline.rs:121-168] |
| `terminate_downstream` | function | The 'terminate_downstream' function terminates the process group associated with a given child process, sends a kill signal to the child process itself, and blocks until the child process has exited, discarding any potential errors. [crates/ghook/src/statusline.rs:170-174] |
| `terminate_downstream_group` | function | The 'terminate_downstream_group' function terminates a downstream process group by sending a 'SIGKILL' signal to the process group whose PGID is equal to the given child process's PID. [crates/ghook/src/statusline.rs:177-183] |
| `terminate_downstream_group` | function | The 'terminate_downstream_group' function is a placeholder that accepts a reference to a child process but currently performs no actions, indicating an intended but unimplemented mechanism to terminate downstream process groups. [crates/ghook/src/statusline.rs:186] |
| `downstream_shell_command` | function | The 'downstream_shell_command' function constructs and returns a 'Command' configured to execute the specified 'OsStr' command via 'sh -c' in a new process group. [crates/ghook/src/statusline.rs:189-194] |
| `downstream_shell_command` | function | The 'downstream_shell_command' function constructs and returns a 'std::process::Command' configured to execute the specified OS string command via the Windows Command Prompt ('cmd') using the '/C' flag. [crates/ghook/src/statusline.rs:197-201] |

_Verified by 11 in-file unit tests._

