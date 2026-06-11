---
title: crates/gcore/src/ai/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/mod.rs
  ranges:
  - 30-34
  - 36-47
  - 49-61
  - 63-75
  - 78-81
  - 84-88
  - 90-107
  - 109-134
  - 136-141
  - 143-145
  - 147-149
  - 151-168
  - 170-200
  - 203-208
  - 210-217
  - 219-234
  - 236-247
  - 249-257
  - 259-261
  - 263-296
  - 298-309
  - 311-317
  - 319-321
  - 323-341
  - 343-346
  - 348-358
  - 360-366
  - 369-373
  - 375-392
  - 401-417
  - 420-442
  - 445-458
  - 461-465
  - 468-475
  - 478-491
  - 494-514
  - 517-556
  - 559-594
  - 597-627
  - 629-642
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/mod.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

`crates/gcore/src/ai/mod.rs` exposes 40 indexed API symbols.
[crates/gcore/src/ai/mod.rs:30-34]
[crates/gcore/src/ai/mod.rs:36-47]
[crates/gcore/src/ai/mod.rs:49-61]
[crates/gcore/src/ai/mod.rs:63-75]
[crates/gcore/src/ai/mod.rs:78-81]

## API Symbols

- `effective_route` (function) component `effective_route [function]` (`1d1d0d89-a9c1-582f-ab80-915b25aefa53`) lines 30-34 [crates/gcore/src/ai/mod.rs:30-34]
  - Signature: `pub fn effective_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `effective_route` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:30-34]
- `effective_route_with_probe` (function) component `effective_route_with_probe [function]` (`b34e7711-5869-55b9-9575-b7d62dbeb638`) lines 36-47 [crates/gcore/src/ai/mod.rs:36-47]
  - Signature: `fn effective_route_with_probe(`
  - Purpose: Indexed function `effective_route_with_probe` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:36-47]
- `daemon_route_or_fallback` (function) component `daemon_route_or_fallback [function]` (`7ac3caa0-64bd-538f-8655-a126bcd11d99`) lines 49-61 [crates/gcore/src/ai/mod.rs:49-61]
  - Signature: `fn daemon_route_or_fallback(`
  - Purpose: Indexed function `daemon_route_or_fallback` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:49-61]
- `direct_route_or_off` (function) component `direct_route_or_off [function]` (`4fe7c3e2-223b-50d7-868c-4bf6f663463c`) lines 63-75 [crates/gcore/src/ai/mod.rs:63-75]
  - Signature: `fn direct_route_or_off(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `direct_route_or_off` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:63-75]
- `AiTransport` (class) component `AiTransport [class]` (`d26b891b-cc06-5b8e-a3f5-e5d84ef97d54`) lines 78-81 [crates/gcore/src/ai/mod.rs:78-81]
  - Signature: `pub struct AiTransport<'a> {`
  - Purpose: Indexed class `AiTransport` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:78-81]
- `new` (function) component `new [function]` (`53688775-43ae-55f0-9379-44144f5a3e94`) lines 84-88 [crates/gcore/src/ai/mod.rs:84-88]
  - Signature: `pub fn new(context: &'a AiContext) -> Result<Self, AiError> {`
  - Purpose: Indexed function `new` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:84-88]
- `post_json` (function) component `post_json [function]` (`55fbf56f-d8bf-52eb-b025-9c2029036720`) lines 90-107 [crates/gcore/src/ai/mod.rs:90-107]
  - Signature: `pub fn post_json<T>(`
  - Purpose: Indexed function `post_json` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:90-107]
- `post_multipart` (function) component `post_multipart [function]` (`0018671e-1bf6-5f64-84e3-f7bb31b64397`) lines 109-134 [crates/gcore/src/ai/mod.rs:109-134]
  - Signature: `pub fn post_multipart(`
  - Purpose: Indexed function `post_multipart` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:109-134]
- `parse_transcription` (function) component `parse_transcription [function]` (`d8d288d4-ac54-592b-b459-e12733229ca5`) lines 136-141 [crates/gcore/src/ai/mod.rs:136-141]
  - Signature: `pub fn parse_transcription(`
  - Purpose: Indexed function `parse_transcription` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:136-141]
- `parse_vision` (function) component `parse_vision [function]` (`a9b615d0-68d2-5f7d-b273-bd171f254ad9`) lines 143-145 [crates/gcore/src/ai/mod.rs:143-145]
  - Signature: `pub fn parse_vision(&self, value: serde_json::Value) -> Result<VisionResult, AiError> {`
  - Purpose: Indexed function `parse_vision` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:143-145]
- `parse_text` (function) component `parse_text [function]` (`31ac76f5-4048-5ca7-9c40-dc4a762b811c`) lines 147-149 [crates/gcore/src/ai/mod.rs:147-149]
  - Signature: `pub fn parse_text(&self, value: serde_json::Value) -> Result<TextResult, AiError> {`
  - Purpose: Indexed function `parse_text` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:147-149]
- `build_json_request` (function) component `build_json_request [function]` (`7f405bcf-9303-57e0-8b4b-22d3b7063db7`) lines 151-168 [crates/gcore/src/ai/mod.rs:151-168]
  - Signature: `pub fn build_json_request<T>(`
  - Purpose: Indexed function `build_json_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:151-168]
- `build_multipart_request` (function) component `build_multipart_request [function]` (`5ad14028-eee9-5187-89d7-98bbd4d0e30b`) lines 170-200 [crates/gcore/src/ai/mod.rs:170-200]
  - Signature: `pub fn build_multipart_request(`
  - Purpose: Indexed function `build_multipart_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:170-200]
- `apply_api_key` (function) component `apply_api_key [function]` (`a434752b-eb5e-5871-9705-8047e358b820`) lines 203-208 [crates/gcore/src/ai/mod.rs:203-208]
  - Signature: `fn apply_api_key(request: RequestBuilder, binding: &CapabilityBinding) -> RequestBuilder {`
  - Purpose: Indexed function `apply_api_key` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:203-208]
- `timeout_for` (function) component `timeout_for [function]` (`0b788c42-cd46-5e53-8d5c-0b0373e3225a`) lines 210-217 [crates/gcore/src/ai/mod.rs:210-217]
  - Signature: `fn timeout_for(capability: AiCapability) -> Duration {`
  - Purpose: Indexed function `timeout_for` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:210-217]
- `retry_with_backoff` (function) component `retry_with_backoff [function]` (`2ececf02-86d2-579e-b67f-be87fe34be70`) lines 219-234 [crates/gcore/src/ai/mod.rs:219-234]
  - Signature: `pub fn retry_with_backoff<T>(`
  - Purpose: Indexed function `retry_with_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:219-234]
- `is_retryable` (function) component `is_retryable [function]` (`5c0027dc-e773-510c-bec6-1de51bd6ce96`) lines 236-247 [crates/gcore/src/ai/mod.rs:236-247]
  - Signature: `fn is_retryable(error: &AiError) -> bool {`
  - Purpose: Indexed function `is_retryable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:236-247]
- `retry_delay` (function) component `retry_delay [function]` (`549f2359-b022-5a51-a0ab-e035a28c2c36`) lines 249-257 [crates/gcore/src/ai/mod.rs:249-257]
  - Signature: `fn retry_delay(error: &AiError, retry_index: usize) -> Duration {`
  - Purpose: Indexed function `retry_delay` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:249-257]
- `jitter` (function) component `jitter [function]` (`cfc58b79-32d9-579f-8e5e-8840dbb4bfce`) lines 259-261 [crates/gcore/src/ai/mod.rs:259-261]
  - Signature: `fn jitter() -> Duration {`
  - Purpose: Indexed function `jitter` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:259-261]
- `parse_json_response` (function) component `parse_json_response [function]` (`d666aa1a-0c17-5bfd-9dd4-6edb842360e5`) lines 263-296 [crates/gcore/src/ai/mod.rs:263-296]
  - Signature: `fn parse_json_response(response: Response) -> Result<serde_json::Value, AiError> {`
  - Purpose: Indexed function `parse_json_response` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:263-296]
- `parse_retry_after` (function) component `parse_retry_after [function]` (`61e1ad83-2dfc-58ad-a003-8329aafadb01`) lines 298-309 [crates/gcore/src/ai/mod.rs:298-309]
  - Signature: `fn parse_retry_after(value: &str) -> Option<Duration> {`
  - Purpose: Indexed function `parse_retry_after` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:298-309]
- `reqwest_error` (function) component `reqwest_error [function]` (`fdc7c636-2564-53dd-b089-69877ef97366`) lines 311-317 [crates/gcore/src/ai/mod.rs:311-317]
  - Signature: `fn reqwest_error(error: reqwest::Error) -> AiError {`
  - Purpose: Indexed function `reqwest_error` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:311-317]
- `duration_to_ms` (function) component `duration_to_ms [function]` (`6e566e2d-75e8-5a93-b76b-12a99507dffb`) lines 319-321 [crates/gcore/src/ai/mod.rs:319-321]
  - Signature: `fn duration_to_ms(duration: Duration) -> u64 {`
  - Purpose: Indexed function `duration_to_ms` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:319-321]
- `chat_completions_url` (function) component `chat_completions_url [function]` (`69420957-e9b4-548b-b149-3316b92e9d97`) lines 323-341 [crates/gcore/src/ai/mod.rs:323-341]
  - Signature: `fn chat_completions_url(cfg: &AiContext, capability: AiCapability) -> Result<String, AiError> {`
  - Purpose: Indexed function `chat_completions_url` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:323-341]
- `chat_api_root` (function) component `chat_api_root [function]` (`08c141ca-1096-56e0-b4de-4f51ca7190d0`) lines 343-346 [crates/gcore/src/ai/mod.rs:343-346]
  - Signature: `fn chat_api_root(api_base: &str) -> &str {`
  - Purpose: Indexed function `chat_api_root` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:343-346]
- `chat_completion_content` (function) component `chat_completion_content [function]` (`874e9aed-f4e4-5dc3-9867-e66130320bc9`) lines 348-358 [crates/gcore/src/ai/mod.rs:348-358]
  - Signature: `fn chat_completion_content(value: &serde_json::Value) -> Result<String, AiError> {`
  - Purpose: Indexed function `chat_completion_content` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:348-358]
- `chat_completion_model` (function) component `chat_completion_model [function]` (`05de862b-e895-5ee5-8bd7-675205da4d77`) lines 360-366 [crates/gcore/src/ai/mod.rs:360-366]
  - Signature: `fn chat_completion_model(value: &serde_json::Value) -> Option<String> {`
  - Purpose: Indexed function `chat_completion_model` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:360-366]
- `LocalBackendProbe` (class) component `LocalBackendProbe [class]` (`35f30b57-9fc0-5191-8c8f-7d924d51b9d7`) lines 369-373 [crates/gcore/src/ai/mod.rs:369-373]
  - Signature: `pub struct LocalBackendProbe {`
  - Purpose: Indexed class `LocalBackendProbe` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:369-373]
- `probe_local_backend` (function) component `probe_local_backend [function]` (`0b7b4c60-9dbe-535b-b313-6855a30cf7aa`) lines 375-392 [crates/gcore/src/ai/mod.rs:375-392]
  - Signature: `pub fn probe_local_backend(api_base: &str) -> Result<LocalBackendProbe, AiError> {`
  - Purpose: Indexed function `probe_local_backend` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:375-392]
- `retry_caps_at_two` (function) component `retry_caps_at_two [function]` (`fd54f973-0ccf-5052-8bb7-13ec1b0e427d`) lines 401-417 [crates/gcore/src/ai/mod.rs:401-417]
  - Signature: `fn retry_caps_at_two() {`
  - Purpose: Indexed function `retry_caps_at_two` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:401-417]
- `retry_honors_retry_after_before_exponential_backoff` (function) component `retry_honors_retry_after_before_exponential_backoff [function]` (`e2312c8c-82f5-59f1-ad18-47afef870497`) lines 420-442 [crates/gcore/src/ai/mod.rs:420-442]
  - Signature: `fn retry_honors_retry_after_before_exponential_backoff() {`
  - Purpose: Indexed function `retry_honors_retry_after_before_exponential_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:420-442]
- `parse_retry_after_accepts_http_dates_and_clamps` (function) component `parse_retry_after_accepts_http_dates_and_clamps [function]` (`55f30a2a-202b-5b93-bb53-b330f90b6f81`) lines 445-458 [crates/gcore/src/ai/mod.rs:445-458]
  - Signature: `fn parse_retry_after_accepts_http_dates_and_clamps() {`
  - Purpose: Indexed function `parse_retry_after_accepts_http_dates_and_clamps` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:445-458]
- `embeddings_use_shorter_timeout_than_generation` (function) component `embeddings_use_shorter_timeout_than_generation [function]` (`fc1cad30-445e-5c46-a8a5-d40f72b2032a`) lines 461-465 [crates/gcore/src/ai/mod.rs:461-465]
  - Signature: `fn embeddings_use_shorter_timeout_than_generation() {`
  - Purpose: Indexed function `embeddings_use_shorter_timeout_than_generation` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:461-465]
- `text_generation_outlasts_vision_for_local_reasoning_models` (function) component `text_generation_outlasts_vision_for_local_reasoning_models [function]` (`cee3a472-d975-5a4f-81ac-4ca2bd989ce6`) lines 468-475 [crates/gcore/src/ai/mod.rs:468-475]
  - Signature: `fn text_generation_outlasts_vision_for_local_reasoning_models() {`
  - Purpose: Indexed function `text_generation_outlasts_vision_for_local_reasoning_models` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:468-475]
- `chat_api_root_trims_trailing_v1_segment` (function) component `chat_api_root_trims_trailing_v1_segment [function]` (`2323068f-992f-5061-95b0-59abc52266be`) lines 478-491 [crates/gcore/src/ai/mod.rs:478-491]
  - Signature: `fn chat_api_root_trims_trailing_v1_segment() {`
  - Purpose: Indexed function `chat_api_root_trims_trailing_v1_segment` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:478-491]
- `probe_local_backend_returns_non_success_status` (function) component `probe_local_backend_returns_non_success_status [function]` (`315ab23c-ff83-542a-9b02-0656f56433e5`) lines 494-514 [crates/gcore/src/ai/mod.rs:494-514]
  - Signature: `fn probe_local_backend_returns_non_success_status() {`
  - Purpose: Indexed function `probe_local_backend_returns_non_success_status` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:494-514]
- `effective_route_auto_falls_through_per_capability` (function) component `effective_route_auto_falls_through_per_capability [function]` (`d2217cf5-e110-5896-aaf9-b1149f3596d9`) lines 517-556 [crates/gcore/src/ai/mod.rs:517-556]
  - Signature: `fn effective_route_auto_falls_through_per_capability() {`
  - Purpose: Indexed function `effective_route_auto_falls_through_per_capability` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:517-556]
- `effective_route_explicit_routing_modes_are_forced` (function) component `effective_route_explicit_routing_modes_are_forced [function]` (`1011bfa8-deef-5104-ae3c-083e282f55a3`) lines 559-594 [crates/gcore/src/ai/mod.rs:559-594]
  - Signature: `fn effective_route_explicit_routing_modes_are_forced() {`
  - Purpose: Indexed function `effective_route_explicit_routing_modes_are_forced` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:559-594]
- `auto_uses_explicit_direct_config_when_daemon_unavailable` (function) component `auto_uses_explicit_direct_config_when_daemon_unavailable [function]` (`10fd6471-8d82-556b-8c85-9ddf3ce3e87a`) lines 597-627 [crates/gcore/src/ai/mod.rs:597-627]
  - Signature: `fn auto_uses_explicit_direct_config_when_daemon_unavailable() {`
  - Purpose: Indexed function `auto_uses_explicit_direct_config_when_daemon_unavailable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:597-627]
- `binding` (function) component `binding [function]` (`2b002f39-70c7-5bf2-add4-86a4bd0e9fcc`) lines 629-642 [crates/gcore/src/ai/mod.rs:629-642]
  - Signature: `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {`
  - Purpose: Indexed function `binding` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:629-642]

