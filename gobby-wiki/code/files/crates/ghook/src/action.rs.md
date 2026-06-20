---
title: crates/ghook/src/action.rs
type: code_file
provenance:
- file: crates/ghook/src/action.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/action.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/action.rs` exposes 28 indexed API symbols.

## How it fits

`crates/ghook/src/action.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `HookAction` | class | 'HookAction' is a crate-visible struct that encapsulates the result of a hook execution, storing an 8-bit unsigned integer exit code alongside optional JSON-formatted standard output and standard error message strings. [crates/ghook/src/action.rs:9-13] |
| `continue_action` | function | The crate-private 'continue_action' function returns a 'HookAction' configured with an exit code of '0', no error message, and a JSON-serialized stdout containing '{"continue": true}'. [crates/ghook/src/action.rs:15-21] |
| `emit_empty_json` | function | The 'emit_empty_json' function writes an empty JSON object followed by a newline character to the standard output. [crates/ghook/src/action.rs:23-25] |
| `emit_action` | function | The 'emit_action' function conditionally outputs the JSON payload to stdout and a trimmed error message to stderr if they are present in the provided 'HookAction' struct, and returns the action's exit code converted into an 'ExitCode' type. [crates/ghook/src/action.rs:27-35] |
| `action_from_success_response` | function | The 'action_from_success_response' function parses a JSON-formatted hook response body and maps it to a 'HookAction' containing an exit code, stdout, and stderr, applying specialized routing and transformation logic based on the specified canonical source and hook type. [crates/ghook/src/action.rs:37-107] |
| `action_from_droid_success` | function | This function evaluates a JSON 'result' to return a 'HookAction' with an exit code of 2 and an extracted error reason if the 'continue' property is explicitly false, and otherwise returns an exit code of 0 with the serialized output conditionally included based on the truthiness of the result. [crates/ghook/src/action.rs:109-128] |
| `action_from_failure` | function | This function maps a transport delivery failure kind and its contextual details into a structured 'HookAction' containing a specific exit code and error message, varying the severity and output based on the CLI source configuration and the hook's criticality. [crates/ghook/src/action.rs:130-190] |
| `is_blocked` | function | The 'is_blocked' function determines if a JSON 'Value' object represents a blocked or denied state by returning 'true' if the 'continue' field is 'false', the 'decision' field is ''deny'' or ''block'', or the top-level or nested 'hookSpecificOutput' 'permissionDecision' field is ''deny''; otherwise, it returns 'false'. [crates/ghook/src/action.rs:192-214] |
| `extract_reason` | function | The 'extract_reason' function extracts and returns a non-empty explanation string from a JSON 'Value' object by checking for designated keys ("stopReason", "user_message", "reason") at the top level or nested within "hookSpecificOutput" ("permissionDecisionReason", "reason"), falling back to "Blocked by hook" if no match is found or if the input is not an object. [crates/ghook/src/action.rs:216-244] |

_Verified by 19 in-file unit tests._

