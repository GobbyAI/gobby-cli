---
title: crates/gcode/src/graph/code_graph/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
  ranges:
  - 18-21
  - 24-29
  - 31-36
  - 38-43
  - 47-52
  - 55-61
  - 65-68
  - 71-76
  - 80-88
  - 90-95
  - 98-105
  - 108-113
  - 116-122
  - 125-130
  - 133-149
  - 154-164
  - 166-176
  - 178-191
  - 193-211
  - 213-232
  - 234-248
  - 250-286
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21](crates/gcode/src/graph/code_graph/lifecycle.rs#L18-L21), [crates/gcode/src/graph/code_graph/lifecycle.rs:24-29](crates/gcode/src/graph/code_graph/lifecycle.rs#L24-L29), [crates/gcode/src/graph/code_graph/lifecycle.rs:31-36](crates/gcode/src/graph/code_graph/lifecycle.rs#L31-L36), [crates/gcode/src/graph/code_graph/lifecycle.rs:38-43](crates/gcode/src/graph/code_graph/lifecycle.rs#L38-L43), [crates/gcode/src/graph/code_graph/lifecycle.rs:47-52](crates/gcode/src/graph/code_graph/lifecycle.rs#L47-L52), [crates/gcode/src/graph/code_graph/lifecycle.rs:55-61](crates/gcode/src/graph/code_graph/lifecycle.rs#L55-L61), [crates/gcode/src/graph/code_graph/lifecycle.rs:65-68](crates/gcode/src/graph/code_graph/lifecycle.rs#L65-L68), [crates/gcode/src/graph/code_graph/lifecycle.rs:71-76](crates/gcode/src/graph/code_graph/lifecycle.rs#L71-L76), [crates/gcode/src/graph/code_graph/lifecycle.rs:80-88](crates/gcode/src/graph/code_graph/lifecycle.rs#L80-L88), [crates/gcode/src/graph/code_graph/lifecycle.rs:90-95](crates/gcode/src/graph/code_graph/lifecycle.rs#L90-L95), [crates/gcode/src/graph/code_graph/lifecycle.rs:98-105](crates/gcode/src/graph/code_graph/lifecycle.rs#L98-L105), [crates/gcode/src/graph/code_graph/lifecycle.rs:108-113](crates/gcode/src/graph/code_graph/lifecycle.rs#L108-L113), [crates/gcode/src/graph/code_graph/lifecycle.rs:116-122](crates/gcode/src/graph/code_graph/lifecycle.rs#L116-L122), [crates/gcode/src/graph/code_graph/lifecycle.rs:125-130](crates/gcode/src/graph/code_graph/lifecycle.rs#L125-L130), [crates/gcode/src/graph/code_graph/lifecycle.rs:133-149](crates/gcode/src/graph/code_graph/lifecycle.rs#L133-L149), [crates/gcode/src/graph/code_graph/lifecycle.rs:154-164](crates/gcode/src/graph/code_graph/lifecycle.rs#L154-L164), [crates/gcode/src/graph/code_graph/lifecycle.rs:166-176](crates/gcode/src/graph/code_graph/lifecycle.rs#L166-L176), [crates/gcode/src/graph/code_graph/lifecycle.rs:178-191](crates/gcode/src/graph/code_graph/lifecycle.rs#L178-L191), [crates/gcode/src/graph/code_graph/lifecycle.rs:193-211](crates/gcode/src/graph/code_graph/lifecycle.rs#L193-L211), [crates/gcode/src/graph/code_graph/lifecycle.rs:213-232](crates/gcode/src/graph/code_graph/lifecycle.rs#L213-L232), [crates/gcode/src/graph/code_graph/lifecycle.rs:234-248](crates/gcode/src/graph/code_graph/lifecycle.rs#L234-L248), [crates/gcode/src/graph/code_graph/lifecycle.rs:250-286](crates/gcode/src/graph/code_graph/lifecycle.rs#L250-L286)

</details>

# crates/gcode/src/graph/code_graph/lifecycle.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

Implements the code-index graph lifecycle flow for clearing and rebuilding the graph. `GraphLifecycleAction` maps each action to its CLI command, daemon endpoint, and success message; `GraphLifecycleRequest` captures the project, optional daemon URL, and action-specific timeouts pulled from environment defaults via `GraphLifecycleTimeouts`. The remaining helpers validate the daemon URL, build the lifecycle request URL, format HTTP and read errors, extract summary text from successful responses, and `run_lifecycle_action` ties everything together by executing the request and producing a `GraphLifecycleOutput`.
[crates/gcode/src/graph/code_graph/lifecycle.rs:18-21]
[crates/gcode/src/graph/code_graph/lifecycle.rs:24-29]
[crates/gcode/src/graph/code_graph/lifecycle.rs:31-36]
[crates/gcode/src/graph/code_graph/lifecycle.rs:38-43]
[crates/gcode/src/graph/code_graph/lifecycle.rs:47-52]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GraphLifecycleAction` | type | `pub enum GraphLifecycleAction {` | `GraphLifecycleAction [type]` | `786b4b51-b899-5a98-b62b-c5e50ceebd5e` | 18-21 [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21] | Indexed type `GraphLifecycleAction` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21] |
| `GraphLifecycleAction::cli_command` | method | `pub fn cli_command(self) -> &'static str {` | `GraphLifecycleAction::cli_command [method]` | `0184b10e-ae6b-570e-b52d-cd07712d63ef` | 24-29 [crates/gcode/src/graph/code_graph/lifecycle.rs:24-29] | Indexed method `GraphLifecycleAction::cli_command` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:24-29] |
| `GraphLifecycleAction::endpoint_path` | method | `pub fn endpoint_path(self) -> &'static str {` | `GraphLifecycleAction::endpoint_path [method]` | `67ec3bc8-acfc-5ea8-a633-1c8ce684abf3` | 31-36 [crates/gcode/src/graph/code_graph/lifecycle.rs:31-36] | Indexed method `GraphLifecycleAction::endpoint_path` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:31-36] |
| `GraphLifecycleAction::success_prefix` | method | `pub fn success_prefix(self) -> &'static str {` | `GraphLifecycleAction::success_prefix [method]` | `44c0e7bc-fa77-5430-85d1-96418fe782bb` | 38-43 [crates/gcode/src/graph/code_graph/lifecycle.rs:38-43] | Indexed method `GraphLifecycleAction::success_prefix` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:38-43] |
| `GraphLifecycleRequest` | class | `pub struct GraphLifecycleRequest {` | `GraphLifecycleRequest [class]` | `5e637503-5ab6-5fcc-9f40-2a9b8ccfcf2b` | 47-52 [crates/gcode/src/graph/code_graph/lifecycle.rs:47-52] | Indexed class `GraphLifecycleRequest` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:47-52] |
| `GraphLifecycleRequest::from_context` | method | `pub fn from_context(ctx: &Context) -> Self {` | `GraphLifecycleRequest::from_context [method]` | `c0c431b5-c75c-5ff2-866d-ee2b4937bdd4` | 55-61 [crates/gcode/src/graph/code_graph/lifecycle.rs:55-61] | Indexed method `GraphLifecycleRequest::from_context` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:55-61] |
| `GraphLifecycleTimeouts` | class | `pub struct GraphLifecycleTimeouts {` | `GraphLifecycleTimeouts [class]` | `a5e0498e-d7e7-5117-8175-0f992597baf6` | 65-68 [crates/gcode/src/graph/code_graph/lifecycle.rs:65-68] | Indexed class `GraphLifecycleTimeouts` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:65-68] |
| `GraphLifecycleTimeouts::default` | method | `fn default() -> Self {` | `GraphLifecycleTimeouts::default [method]` | `6afd25f6-d670-51a0-9403-517d9305c867` | 71-76 [crates/gcode/src/graph/code_graph/lifecycle.rs:71-76] | Indexed method `GraphLifecycleTimeouts::default` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:71-76] |
| `GraphLifecycleTimeouts::from_env` | method | `pub fn from_env() -> Self {` | `GraphLifecycleTimeouts::from_env [method]` | `9067ed3f-8a56-5e31-9fe5-574b31e3ea97` | 80-88 [crates/gcode/src/graph/code_graph/lifecycle.rs:80-88] | Indexed method `GraphLifecycleTimeouts::from_env` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:80-88] |
| `GraphLifecycleTimeouts::for_action` | method | `fn for_action(self, action: GraphLifecycleAction) -> Duration {` | `GraphLifecycleTimeouts::for_action [method]` | `1db818d9-630e-58e8-bc8d-de302703cc5a` | 90-95 [crates/gcode/src/graph/code_graph/lifecycle.rs:90-95] | Indexed method `GraphLifecycleTimeouts::for_action` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:90-95] |
| `timeout_from_env` | function | `fn timeout_from_env(key: &str, default_secs: u64) -> Duration {` | `timeout_from_env [function]` | `992c9ac5-5710-5af9-9543-807ea9d0b769` | 98-105 [crates/gcode/src/graph/code_graph/lifecycle.rs:98-105] | Indexed function `timeout_from_env` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:98-105] |
| `GraphLifecycleOutput` | class | `pub struct GraphLifecycleOutput {` | `GraphLifecycleOutput [class]` | `49453eb9-1035-5032-8ac6-4ef2c6dd3824` | 108-113 [crates/gcode/src/graph/code_graph/lifecycle.rs:108-113] | Indexed class `GraphLifecycleOutput` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:108-113] |
| `GraphReadRequest` | class | `pub struct GraphReadRequest {` | `GraphReadRequest [class]` | `4ee0050d-487c-5845-b77d-2323fe91767b` | 116-122 [crates/gcode/src/graph/code_graph/lifecycle.rs:116-122] | Indexed class `GraphReadRequest` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:116-122] |
| `GraphReadError` | type | `pub enum GraphReadError {` | `GraphReadError [type]` | `9dc5b0fd-9df4-5435-8ed3-7182a5c093e5` | 125-130 [crates/gcode/src/graph/code_graph/lifecycle.rs:125-130] | Indexed type `GraphReadError` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:125-130] |
| `GraphReadError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `GraphReadError::fmt [method]` | `f40cd3e8-58be-531a-a3cc-383a9d73d2b1` | 133-149 [crates/gcode/src/graph/code_graph/lifecycle.rs:133-149] | Indexed method `GraphReadError::fmt` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:133-149] |
| `require_daemon_url` | function | `pub fn require_daemon_url(` | `require_daemon_url [function]` | `45a21f8f-94ab-56c8-9b13-6fb807f974b0` | 154-164 [crates/gcode/src/graph/code_graph/lifecycle.rs:154-164] | Indexed function `require_daemon_url` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:154-164] |
| `build_lifecycle_url` | function | `pub(crate) fn build_lifecycle_url(` | `build_lifecycle_url [function]` | `4453d99f-2fe2-5bc1-85ca-333d7d74a4e7` | 166-176 [crates/gcode/src/graph/code_graph/lifecycle.rs:166-176] | Indexed function `build_lifecycle_url` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:166-176] |
| `compact_detail` | function | `pub(crate) fn compact_detail(body: &str) -> String {` | `compact_detail [function]` | `960701ce-7cd6-5b9e-b83d-2b9cdb44976e` | 178-191 [crates/gcode/src/graph/code_graph/lifecycle.rs:178-191] | Indexed function `compact_detail` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:178-191] |
| `format_http_error` | function | `pub(crate) fn format_http_error(` | `format_http_error [function]` | `864a1f4a-cf4f-5883-b05e-dd0041dbc58f` | 193-211 [crates/gcode/src/graph/code_graph/lifecycle.rs:193-211] | Indexed function `format_http_error` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:193-211] |
| `parse_success_payload` | function | `pub(crate) fn parse_success_payload(` | `parse_success_payload [function]` | `4fb93f1c-f232-5c21-8be7-8d95aa2cd3ee` | 213-232 [crates/gcode/src/graph/code_graph/lifecycle.rs:213-232] | Indexed function `parse_success_payload` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:213-232] |
| `extract_summary_text` | function | `pub(crate) fn extract_summary_text(payload: &Value) -> Option<String> {` | `extract_summary_text [function]` | `3e63418d-91be-587f-b332-34986e97cdf6` | 234-248 [crates/gcode/src/graph/code_graph/lifecycle.rs:234-248] | Indexed function `extract_summary_text` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:234-248] |
| `run_lifecycle_action` | function | `pub fn run_lifecycle_action(` | `run_lifecycle_action [function]` | `3108b7ef-9759-5509-9018-0af9cfdc2368` | 250-286 [crates/gcode/src/graph/code_graph/lifecycle.rs:250-286] | Indexed function `run_lifecycle_action` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:250-286] |
