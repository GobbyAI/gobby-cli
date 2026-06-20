---
title: crates/gcode/src/graph/code_graph/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/lifecycle.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Overview

`crates/gcode/src/graph/code_graph/lifecycle.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/lifecycle.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphLifecycleAction` | type | Indexed type `GraphLifecycleAction` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21] |
| `GraphLifecycleAction::cli_command` | method | Returns the static CLI subcommand string for the enum variant, mapping 'Clear' to '"gcode graph clear"' and 'Rebuild' to '"gcode graph rebuild"'. [crates/gcode/src/graph/code_graph/lifecycle.rs:24-29] |
| `GraphLifecycleAction::endpoint_path` | method | Returns the static API route string for the enum variant, mapping 'Clear' to '/api/code-index/graph/clear' and 'Rebuild' to '/api/code-index/graph/rebuild'. [crates/gcode/src/graph/code_graph/lifecycle.rs:31-36] |
| `GraphLifecycleAction::success_prefix` | method | Returns a '&'static str' status prefix for the enum variant, mapping 'Clear' to '"Cleared code-index graph"' and 'Rebuild' to '"Rebuilt code-index graph"'. [crates/gcode/src/graph/code_graph/lifecycle.rs:38-43] |
| `GraphLifecycleRequest` | class | 'GraphLifecycleRequest' is a serialized request payload containing a required 'project_id', an optional 'daemon_url', and a 'timeouts' configuration that defaults via Serde. [crates/gcode/src/graph/code_graph/lifecycle.rs:47-52] |
| `GraphLifecycleRequest::from_context` | method | Constructs a new instance by cloning 'project_id' and 'daemon_url' from the provided 'Context' and initializing 'timeouts' from 'GraphLifecycleTimeouts::from_env()'. [crates/gcode/src/graph/code_graph/lifecycle.rs:55-61] |
| `GraphLifecycleTimeouts` | class | 'GraphLifecycleTimeouts' is a struct that stores two 'Duration' values, 'clear' and 'rebuild', for configuring timeouts of graph lifecycle operations. [crates/gcode/src/graph/code_graph/lifecycle.rs:65-68] |
| `GraphLifecycleTimeouts::default` | method | Constructs a 'Self' value with 'clear' set to 'Duration::from_secs(DEFAULT_GRAPH_CLEAR_TIMEOUT_SECS)' and 'rebuild' set to 'Duration::from_secs(DEFAULT_GRAPH_REBUILD_TIMEOUT_SECS)'. [crates/gcode/src/graph/code_graph/lifecycle.rs:71-76] |
| `GraphLifecycleTimeouts::from_env` | method | Constructs a 'Self' by populating 'clear' and 'rebuild' with timeout values loaded from their respective environment variables, falling back to the default graph clear and rebuild timeout constants when unset or invalid. [crates/gcode/src/graph/code_graph/lifecycle.rs:80-88] |
| `GraphLifecycleTimeouts::for_action` | method | Returns the 'Duration' associated with a 'GraphLifecycleAction' by matching 'Clear' to 'self.clear' and 'Rebuild' to 'self.rebuild'. [crates/gcode/src/graph/code_graph/lifecycle.rs:90-95] |
| `timeout_from_env` | function | Returns a 'Duration' from the 'u64' value of the environment variable 'key' if it exists, parses successfully, and is greater than zero, otherwise falls back to 'Duration::from_secs(default_secs)'. [crates/gcode/src/graph/code_graph/lifecycle.rs:98-105] |
| `GraphLifecycleOutput` | class | 'GraphLifecycleOutput' is a struct that captures a graph lifecycle event with a 'project_id', an 'action' of type 'GraphLifecycleAction', a human-readable 'summary', and an arbitrary JSON 'payload' stored as 'Value'. [crates/gcode/src/graph/code_graph/lifecycle.rs:108-113] |
| `GraphReadRequest` | class | 'GraphReadRequest' is a request struct that specifies a project and symbol identifier plus pagination and traversal parameters ('offset', 'limit', and 'depth') for reading a graph-backed symbol view. [crates/gcode/src/graph/code_graph/lifecycle.rs:116-122] |
| `GraphReadError` | type | Indexed type `GraphReadError` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:125-130] |
| `GraphReadError::fmt` | method | Implements 'fmt::Display' for the type by matching each variant and writing a variant-specific FalkorDB error message to the formatter, including embedded 'message' text where present. [crates/gcode/src/graph/code_graph/lifecycle.rs:133-149] |
| `require_daemon_url` | function | Returns the provided 'daemon_url' as 'Ok(&str)' when present, otherwise returns an 'anyhow::Error' stating that the Gobby daemon URL is not configured and naming the CLI command from 'action.cli_command()'. [crates/gcode/src/graph/code_graph/lifecycle.rs:154-164] |
| `build_lifecycle_url` | function | Constructs a 'reqwest::Url' for a graph lifecycle endpoint by trimming any trailing slash from 'base_url', appending 'action.endpoint_path()', and adding a 'project_id' query parameter, returning an error if the base URL is invalid. [crates/gcode/src/graph/code_graph/lifecycle.rs:166-176] |
| `compact_detail` | function | Normalizes 'body' by collapsing all whitespace to single spaces and trimming ends, then returns it unchanged if it is at most 240 Unicode scalar values long or truncates it to 237 characters and appends '...' otherwise. [crates/gcode/src/graph/code_graph/lifecycle.rs:178-191] |
| `format_http_error` | function | Formats a human-readable error string for a failed 'GraphLifecycleAction', including the action’s CLI command, HTTP status, request URL, and an optional compacted response-body detail when present. [crates/gcode/src/graph/code_graph/lifecycle.rs:193-211] |
| `parse_success_payload` | function | Parses the response body as JSON into a 'serde_json::Value', returning it on success and otherwise wrapping the JSON parse error in an 'anyhow::Error' that includes the action name, HTTP status, and a compacted response snippet when available. [crates/gcode/src/graph/code_graph/lifecycle.rs:213-232] |
| `extract_summary_text` | function | Returns a trimmed non-empty summary string from a 'Value' by accepting either a direct string or the first non-empty string found under 'summary', 'message', 'detail', or 'status' in an object, otherwise 'None'. [crates/gcode/src/graph/code_graph/lifecycle.rs:234-248] |
| `run_lifecycle_action` | function | Sends a blocking POST request to the daemon’s lifecycle endpoint for the given project/action with an action-specific timeout, converts non-2xx responses into formatted errors, parses the success payload, derives a summary string, and returns a 'GraphLifecycleOutput' containing the project ID, action, summary, and raw payload. [crates/gcode/src/graph/code_graph/lifecycle.rs:250-286] |

