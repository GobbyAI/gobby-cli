---
title: crates/gcode/src/graph/code_graph/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
  ranges:
  - 18-21
  - 23-44
  - 47-52
  - 54-62
  - 65-68
  - 70-77
  - 79-96
  - 98-105
  - 108-113
  - 116-122
  - 125-130
  - 132-150
  - '152'
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

# crates/gcode/src/graph/code_graph/lifecycle.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

This file manages graph lifecycle operations (clear and rebuild) for a code-indexing system. GraphLifecycleAction is an enum that maps two operations to their CLI commands, REST API endpoints, and success messages. GraphLifecycleRequest encapsulates the project context and timeout configuration needed for lifecycle operations, constructible from environment variables via from_context. GraphLifecycleTimeouts provides configurable timeout durations loaded from environment variables with sensible defaults, and maps actions to their corresponding timeout values. The file includes helper functions that handle HTTP communication with a Gobby daemon: require_daemon_url validates daemon configuration, build_lifecycle_url constructs request URLs, format_http_error and parse_success_payload handle responses, extract_summary_text finds summary information in JSON payloads, and run_lifecycle_action orchestrates the full HTTP POST workflow. GraphReadRequest and GraphReadError support querying graph data and reporting read failures respectively. Together these components enable remote execution of graph lifecycle operations with configurable timeouts and detailed error reporting.
[crates/gcode/src/graph/code_graph/lifecycle.rs:18-21]
[crates/gcode/src/graph/code_graph/lifecycle.rs:23-44]
[crates/gcode/src/graph/code_graph/lifecycle.rs:24-29]
[crates/gcode/src/graph/code_graph/lifecycle.rs:31-36]
[crates/gcode/src/graph/code_graph/lifecycle.rs:38-43]

## API Symbols

- `GraphLifecycleAction` (type) component `GraphLifecycleAction [type]` (`786b4b51-b899-5a98-b62b-c5e50ceebd5e`) lines 18-21 [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21]
  - Signature: `pub enum GraphLifecycleAction {`
  - Purpose: Indexed type `GraphLifecycleAction` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21]
- `GraphLifecycleAction` (class) component `GraphLifecycleAction [class]` (`af583299-8f0c-50f9-858e-aef0c1514c70`) lines 23-44 [crates/gcode/src/graph/code_graph/lifecycle.rs:23-44]
  - Signature: `impl GraphLifecycleAction {`
  - Purpose: `GraphLifecycleAction` implementation maps enum variants (Clear/Rebuild) to their corresponding CLI commands, REST API endpoint paths, and success message prefixes via static string returns. [crates/gcode/src/graph/code_graph/lifecycle.rs:23-44]
- `GraphLifecycleAction.cli_command` (method) component `GraphLifecycleAction.cli_command [method]` (`0184b10e-ae6b-570e-b52d-cd07712d63ef`) lines 24-29 [crates/gcode/src/graph/code_graph/lifecycle.rs:24-29]
  - Signature: `pub fn cli_command(self) -> &'static str {`
  - Purpose: Returns the static CLI command string (`"gcode graph clear"` or `"gcode graph rebuild"`) corresponding to the enum variant. [crates/gcode/src/graph/code_graph/lifecycle.rs:24-29]
- `GraphLifecycleAction.endpoint_path` (method) component `GraphLifecycleAction.endpoint_path [method]` (`67ec3bc8-acfc-5ea8-a633-1c8ce684abf3`) lines 31-36 [crates/gcode/src/graph/code_graph/lifecycle.rs:31-36]
  - Signature: `pub fn endpoint_path(self) -> &'static str {`
  - Purpose: This method maps the enum variant to its corresponding static API endpoint path string reference via exhaustive pattern matching. [crates/gcode/src/graph/code_graph/lifecycle.rs:31-36]
- `GraphLifecycleAction.success_prefix` (method) component `GraphLifecycleAction.success_prefix [method]` (`44c0e7bc-fa77-5430-85d1-96418fe782bb`) lines 38-43 [crates/gcode/src/graph/code_graph/lifecycle.rs:38-43]
  - Signature: `pub fn success_prefix(self) -> &'static str {`
  - Purpose: Returns a static string success message prefix corresponding to the enum variant: "Cleared code-index graph" for `Clear` or "Rebuilt code-index graph" for `Rebuild`. [crates/gcode/src/graph/code_graph/lifecycle.rs:38-43]
- `GraphLifecycleRequest` (class) component `GraphLifecycleRequest [class]` (`5e637503-5ab6-5fcc-9f40-2a9b8ccfcf2b`) lines 47-52 [crates/gcode/src/graph/code_graph/lifecycle.rs:47-52]
  - Signature: `pub struct GraphLifecycleRequest {`
  - Purpose: `GraphLifecycleRequest` is a serializable struct that encapsulates a project ID, optional daemon URL, and timeout configuration for graph lifecycle operations. [crates/gcode/src/graph/code_graph/lifecycle.rs:47-52]
- `GraphLifecycleRequest` (class) component `GraphLifecycleRequest [class]` (`dc8c2aa0-94fb-5a60-b3dc-19ee581f658a`) lines 54-62 [crates/gcode/src/graph/code_graph/lifecycle.rs:54-62]
  - Signature: `impl GraphLifecycleRequest {`
  - Purpose: `GraphLifecycleRequest::from_context` is a factory method that instantiates a `GraphLifecycleRequest` by extracting `project_id` and `daemon_url` from a provided `Context` and loading timeout configuration from environment variables. [crates/gcode/src/graph/code_graph/lifecycle.rs:54-62]
- `GraphLifecycleRequest.from_context` (method) component `GraphLifecycleRequest.from_context [method]` (`c0c431b5-c75c-5ff2-866d-ee2b4937bdd4`) lines 55-61 [crates/gcode/src/graph/code_graph/lifecycle.rs:55-61]
  - Signature: `pub fn from_context(ctx: &Context) -> Self {`
  - Purpose: Factory method that constructs a new instance by cloning `project_id` and `daemon_url` from the provided `Context` while initializing `timeouts` from environment variables. [crates/gcode/src/graph/code_graph/lifecycle.rs:55-61]
- `GraphLifecycleTimeouts` (class) component `GraphLifecycleTimeouts [class]` (`a5e0498e-d7e7-5117-8175-0f992597baf6`) lines 65-68 [crates/gcode/src/graph/code_graph/lifecycle.rs:65-68]
  - Signature: `pub struct GraphLifecycleTimeouts {`
  - Purpose: `GraphLifecycleTimeouts` is a public struct that encapsulates timeout duration configurations for two graph lifecycle operations: clearing and rebuilding. [crates/gcode/src/graph/code_graph/lifecycle.rs:65-68]
- `GraphLifecycleTimeouts` (class) component `GraphLifecycleTimeouts [class]` (`40f0d784-f925-5724-8a5c-c975fab13494`) lines 70-77 [crates/gcode/src/graph/code_graph/lifecycle.rs:70-77]
  - Signature: `impl Default for GraphLifecycleTimeouts {`
  - Purpose: Implements the `Default` trait for `GraphLifecycleTimeouts`, initializing its `clear` and `rebuild` timeout durations from predefined constant values. [crates/gcode/src/graph/code_graph/lifecycle.rs:70-77]
- `GraphLifecycleTimeouts.default` (method) component `GraphLifecycleTimeouts.default [method]` (`6afd25f6-d670-51a0-9403-517d9305c867`) lines 71-76 [crates/gcode/src/graph/code_graph/lifecycle.rs:71-76]
  - Signature: `fn default() -> Self {`
  - Purpose: This method implements the `Default` trait by returning a new instance with `clear` and `rebuild` Duration fields initialized to predefined timeout constants. [crates/gcode/src/graph/code_graph/lifecycle.rs:71-76]
- `GraphLifecycleTimeouts` (class) component `GraphLifecycleTimeouts [class]` (`45f94756-b0d4-5f60-bc27-8f878e347d37`) lines 79-96 [crates/gcode/src/graph/code_graph/lifecycle.rs:79-96]
  - Signature: `impl GraphLifecycleTimeouts {`
  - Purpose: This implementation provides environment-variable-based configuration of graph lifecycle timeouts and maps lifecycle actions (clear/rebuild) to their corresponding `Duration` values. [crates/gcode/src/graph/code_graph/lifecycle.rs:79-96]
- `GraphLifecycleTimeouts.from_env` (method) component `GraphLifecycleTimeouts.from_env [method]` (`9067ed3f-8a56-5e31-9fe5-574b31e3ea97`) lines 80-88 [crates/gcode/src/graph/code_graph/lifecycle.rs:80-88]
  - Signature: `pub fn from_env() -> Self {`
  - Purpose: Constructs an instance with `clear` and `rebuild` timeout fields populated from environment variables with default fallback values. [crates/gcode/src/graph/code_graph/lifecycle.rs:80-88]
- `GraphLifecycleTimeouts.for_action` (method) component `GraphLifecycleTimeouts.for_action [method]` (`1db818d9-630e-58e8-bc8d-de302703cc5a`) lines 90-95 [crates/gcode/src/graph/code_graph/lifecycle.rs:90-95]
  - Signature: `fn for_action(self, action: GraphLifecycleAction) -> Duration {`
  - Purpose: Returns the `Duration` field from `self` that corresponds to the given `GraphLifecycleAction` variant through pattern matching. [crates/gcode/src/graph/code_graph/lifecycle.rs:90-95]
- `timeout_from_env` (function) component `timeout_from_env [function]` (`992c9ac5-5710-5af9-9543-807ea9d0b769`) lines 98-105 [crates/gcode/src/graph/code_graph/lifecycle.rs:98-105]
  - Signature: `fn timeout_from_env(key: &str, default_secs: u64) -> Duration {`
  - Purpose: Parses a positive u64 from an environment variable identified by `key`, converts it to a `Duration` in seconds, or falls back to a `Duration` constructed from `default_secs` if parsing fails or the value is non-positive. [crates/gcode/src/graph/code_graph/lifecycle.rs:98-105]
- `GraphLifecycleOutput` (class) component `GraphLifecycleOutput [class]` (`49453eb9-1035-5032-8ac6-4ef2c6dd3824`) lines 108-113 [crates/gcode/src/graph/code_graph/lifecycle.rs:108-113]
  - Signature: `pub struct GraphLifecycleOutput {`
  - Purpose: GraphLifecycleOutput encapsulates a graph lifecycle event, containing the project identifier, action type, a summary description, and a serialized JSON payload. [crates/gcode/src/graph/code_graph/lifecycle.rs:108-113]
- `GraphReadRequest` (class) component `GraphReadRequest [class]` (`4ee0050d-487c-5845-b77d-2323fe91767b`) lines 116-122 [crates/gcode/src/graph/code_graph/lifecycle.rs:116-122]
  - Signature: `pub struct GraphReadRequest {`
  - Purpose: `GraphReadRequest` is a paginated query structure for retrieving a specific symbol's graph data within a project, with configurable traversal depth and result windowing via offset and limit parameters. [crates/gcode/src/graph/code_graph/lifecycle.rs:116-122]
- `GraphReadError` (type) component `GraphReadError [type]` (`9dc5b0fd-9df4-5435-8ed3-7182a5c093e5`) lines 125-130 [crates/gcode/src/graph/code_graph/lifecycle.rs:125-130]
  - Signature: `pub enum GraphReadError {`
  - Purpose: Indexed type `GraphReadError` in `crates/gcode/src/graph/code_graph/lifecycle.rs`. [crates/gcode/src/graph/code_graph/lifecycle.rs:125-130]
- `GraphReadError` (class) component `GraphReadError [class]` (`918919bf-1427-5626-ab1e-faae96d16af6`) lines 132-150 [crates/gcode/src/graph/code_graph/lifecycle.rs:132-150]
  - Signature: `impl fmt::Display for GraphReadError {`
  - Purpose: Implements `fmt::Display` for `GraphReadError` to format four error variants stemming from FalkorDB configuration, connectivity, query failures, and invalid targets. [crates/gcode/src/graph/code_graph/lifecycle.rs:132-150]
- `GraphReadError.fmt` (method) component `GraphReadError.fmt [method]` (`f40cd3e8-58be-531a-a3cc-383a9d73d2b1`) lines 133-149 [crates/gcode/src/graph/code_graph/lifecycle.rs:133-149]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Implements the `Display` trait for an error enum by pattern-matching on self and writing variant-specific error messages to the provided formatter. [crates/gcode/src/graph/code_graph/lifecycle.rs:133-149]
- `GraphReadError` (class) component `GraphReadError [class]` (`c47ad836-425d-59e0-ab47-cdb3723d6cd4`) lines 152-152 [crates/gcode/src/graph/code_graph/lifecycle.rs:152]
  - Signature: `impl std::error::Error for GraphReadError {}`
  - Purpose: `GraphReadError` is a type that implements the `std::error::Error` trait, conforming to Rust's standard error protocol for error propagation and handling. [crates/gcode/src/graph/code_graph/lifecycle.rs:152]
- `require_daemon_url` (function) component `require_daemon_url [function]` (`45a21f8f-94ab-56c8-9b13-6fb807f974b0`) lines 154-164 [crates/gcode/src/graph/code_graph/lifecycle.rs:154-164]
  - Signature: `pub fn require_daemon_url(`
  - Purpose: Extracts and validates a required daemon URL option, returning an anyhow error that references the CLI command associated with the lifecycle action if the URL is not configured. [crates/gcode/src/graph/code_graph/lifecycle.rs:154-164]
- `build_lifecycle_url` (function) component `build_lifecycle_url [function]` (`4453d99f-2fe2-5bc1-85ca-333d7d74a4e7`) lines 166-176 [crates/gcode/src/graph/code_graph/lifecycle.rs:166-176]
  - Signature: `pub(crate) fn build_lifecycle_url(`
  - Purpose: This function constructs a `reqwest::Url` by combining a base URL with a `GraphLifecycleAction`'s endpoint path and appends a project_id query parameter. [crates/gcode/src/graph/code_graph/lifecycle.rs:166-176]
- `compact_detail` (function) component `compact_detail [function]` (`960701ce-7cd6-5b9e-b83d-2b9cdb44976e`) lines 178-191 [crates/gcode/src/graph/code_graph/lifecycle.rs:178-191]
  - Signature: `pub(crate) fn compact_detail(body: &str) -> String {`
  - Purpose: This function normalizes whitespace in the input string and truncates it to a maximum of 240 characters, appending "..." if the character count exceeds that limit. [crates/gcode/src/graph/code_graph/lifecycle.rs:178-191]
- `format_http_error` (function) component `format_http_error [function]` (`864a1f4a-cf4f-5883-b05e-dd0041dbc58f`) lines 193-211 [crates/gcode/src/graph/code_graph/lifecycle.rs:193-211]
  - Signature: `pub(crate) fn format_http_error(`
  - Purpose: Formats an error message combining the GraphLifecycleAction's CLI command, HTTP status code, request URL, and optionally compacted response body details. [crates/gcode/src/graph/code_graph/lifecycle.rs:193-211]
- `parse_success_payload` (function) component `parse_success_payload [function]` (`4fb93f1c-f232-5c21-8be7-8d95aa2cd3ee`) lines 213-232 [crates/gcode/src/graph/code_graph/lifecycle.rs:213-232]
  - Signature: `pub(crate) fn parse_success_payload(`
  - Purpose: Parses a JSON response body string into a `serde_json::Value`, returning the deserialized result or an anyhow error that includes the HTTP status code, failed CLI command, and JSON parse details. [crates/gcode/src/graph/code_graph/lifecycle.rs:213-232]
- `extract_summary_text` (function) component `extract_summary_text [function]` (`3e63418d-91be-587f-b332-34986e97cdf6`) lines 234-248 [crates/gcode/src/graph/code_graph/lifecycle.rs:234-248]
  - Signature: `pub(crate) fn extract_summary_text(payload: &Value) -> Option<String> {`
  - Purpose: Extracts and returns trimmed non-empty string content from a JSON `Value` by returning it directly if the value is a string, or by locating the first matching key among `["summary", "message", "detail", "status"]` if the value is an object. [crates/gcode/src/graph/code_graph/lifecycle.rs:234-248]
- `run_lifecycle_action` (function) component `run_lifecycle_action [function]` (`3108b7ef-9759-5509-9018-0af9cfdc2368`) lines 250-286 [crates/gcode/src/graph/code_graph/lifecycle.rs:250-286]
  - Signature: `pub fn run_lifecycle_action(`
  - Purpose: Sends a blocking HTTP POST request to a Gobby daemon to execute a lifecycle action on a specified project, returning the parsed JSON response payload with extracted summary text. [crates/gcode/src/graph/code_graph/lifecycle.rs:250-286]

