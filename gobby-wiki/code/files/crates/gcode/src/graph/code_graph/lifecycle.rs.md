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

`crates/gcode/src/graph/code_graph/lifecycle.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphLifecycleAction` | type | Indexed type `GraphLifecycleAction` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21] |
| `GraphLifecycleAction::cli_command` | method | Indexed method `GraphLifecycleAction::cli_command` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:24-29] |
| `GraphLifecycleAction::endpoint_path` | method | Indexed method `GraphLifecycleAction::endpoint_path` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:31-36] |
| `GraphLifecycleAction::success_prefix` | method | Indexed method `GraphLifecycleAction::success_prefix` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:38-43] |
| `GraphLifecycleRequest` | class | Indexed class `GraphLifecycleRequest` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:47-52] |
| `GraphLifecycleRequest::from_context` | method | Indexed method `GraphLifecycleRequest::from_context` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:55-61] |
| `GraphLifecycleTimeouts` | class | Indexed class `GraphLifecycleTimeouts` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:65-68] |
| `GraphLifecycleTimeouts::default` | method | Indexed method `GraphLifecycleTimeouts::default` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:71-76] |
| `GraphLifecycleTimeouts::from_env` | method | Indexed method `GraphLifecycleTimeouts::from_env` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:80-88] |
| `GraphLifecycleTimeouts::for_action` | method | Indexed method `GraphLifecycleTimeouts::for_action` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:90-95] |
| `timeout_from_env` | function | Indexed function `timeout_from_env` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:98-105] |
| `GraphLifecycleOutput` | class | Indexed class `GraphLifecycleOutput` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:108-113] |
| `GraphReadRequest` | class | Indexed class `GraphReadRequest` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:116-122] |
| `GraphReadError` | type | Indexed type `GraphReadError` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:125-130] |
| `GraphReadError::fmt` | method | Indexed method `GraphReadError::fmt` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:133-149] |
| `require_daemon_url` | function | Indexed function `require_daemon_url` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:154-164] |
| `build_lifecycle_url` | function | Indexed function `build_lifecycle_url` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:166-176] |
| `compact_detail` | function | Indexed function `compact_detail` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:178-191] |
| `format_http_error` | function | Indexed function `format_http_error` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:193-211] |
| `parse_success_payload` | function | Indexed function `parse_success_payload` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:213-232] |
| `extract_summary_text` | function | Indexed function `extract_summary_text` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:234-248] |
| `run_lifecycle_action` | function | Indexed function `run_lifecycle_action` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:250-286] |

