---
title: crates/gcore/src/ai/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/mod.rs
  ranges:
  - 31-35
  - 37-48
  - 50-62
  - 64-76
  - 79-82
  - 85-89
  - 91-108
  - 110-135
  - 137-142
  - 144-146
  - 148-150
  - 152-169
  - 171-201
  - 204-209
  - 211-218
  - 220-235
  - 237-248
  - 250-258
  - 260-262
  - 264-297
  - 299-310
  - 312-318
  - 320-322
  - 324-342
  - 344-347
  - 349-359
  - 361-367
  - 376-392
  - 395-417
  - 420-433
  - 436-440
  - 443-450
  - 453-466
  - 469-508
  - 511-546
  - 549-579
  - 581-594
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/mod.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

`crates/gcore/src/ai/mod.rs` exposes 37 indexed API symbols.
[crates/gcore/src/ai/mod.rs:31-35]
[crates/gcore/src/ai/mod.rs:37-48]
[crates/gcore/src/ai/mod.rs:50-62]
[crates/gcore/src/ai/mod.rs:64-76]
[crates/gcore/src/ai/mod.rs:79-82]

## API Symbols

- `effective_route` (function) component `effective_route [function]` (`7f89060f-a6e2-567f-8875-ecc1d63bb8f0`) lines 31-35 [crates/gcore/src/ai/mod.rs:31-35]
  - Signature: `pub fn effective_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `effective_route` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:31-35]
- `effective_route_with_probe` (function) component `effective_route_with_probe [function]` (`ba15d92b-546d-5fba-84af-962924e83744`) lines 37-48 [crates/gcore/src/ai/mod.rs:37-48]
  - Signature: `fn effective_route_with_probe(`
  - Purpose: Indexed function `effective_route_with_probe` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:37-48]
- `daemon_route_or_fallback` (function) component `daemon_route_or_fallback [function]` (`d748e96c-668a-5e85-a419-39df03dc7534`) lines 50-62 [crates/gcore/src/ai/mod.rs:50-62]
  - Signature: `fn daemon_route_or_fallback(`
  - Purpose: Indexed function `daemon_route_or_fallback` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:50-62]
- `direct_route_or_off` (function) component `direct_route_or_off [function]` (`5c23eaa1-07fb-5c1a-b22f-d4490145b0b7`) lines 64-76 [crates/gcore/src/ai/mod.rs:64-76]
  - Signature: `fn direct_route_or_off(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `direct_route_or_off` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:64-76]
- `AiTransport` (class) component `AiTransport [class]` (`180a310a-8d01-53ee-a9ae-ed6f8f7e7f27`) lines 79-82 [crates/gcore/src/ai/mod.rs:79-82]
  - Signature: `pub struct AiTransport<'a> {`
  - Purpose: Indexed class `AiTransport` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:79-82]
- `new` (function) component `new [function]` (`f2706583-a628-5ffe-966d-bd49cec75939`) lines 85-89 [crates/gcore/src/ai/mod.rs:85-89]
  - Signature: `pub fn new(context: &'a AiContext) -> Result<Self, AiError> {`
  - Purpose: Indexed function `new` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:85-89]
- `post_json` (function) component `post_json [function]` (`e082eff8-11d3-57f6-b9a8-701d46711e66`) lines 91-108 [crates/gcore/src/ai/mod.rs:91-108]
  - Signature: `pub fn post_json<T>(`
  - Purpose: Indexed function `post_json` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:91-108]
- `post_multipart` (function) component `post_multipart [function]` (`294ff439-365a-561b-a659-4850992be683`) lines 110-135 [crates/gcore/src/ai/mod.rs:110-135]
  - Signature: `pub fn post_multipart(`
  - Purpose: Indexed function `post_multipart` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:110-135]
- `parse_transcription` (function) component `parse_transcription [function]` (`f34172c1-25a5-5f04-9884-382b86cdd0a5`) lines 137-142 [crates/gcore/src/ai/mod.rs:137-142]
  - Signature: `pub fn parse_transcription(`
  - Purpose: Indexed function `parse_transcription` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:137-142]
- `parse_vision` (function) component `parse_vision [function]` (`586d5323-0a44-5219-9128-f5131b14fbab`) lines 144-146 [crates/gcore/src/ai/mod.rs:144-146]
  - Signature: `pub fn parse_vision(&self, value: serde_json::Value) -> Result<VisionResult, AiError> {`
  - Purpose: Indexed function `parse_vision` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:144-146]
- `parse_text` (function) component `parse_text [function]` (`0a3c1953-81c4-5755-a522-8fafb180f32c`) lines 148-150 [crates/gcore/src/ai/mod.rs:148-150]
  - Signature: `pub fn parse_text(&self, value: serde_json::Value) -> Result<TextResult, AiError> {`
  - Purpose: Indexed function `parse_text` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:148-150]
- `build_json_request` (function) component `build_json_request [function]` (`89ec5e8e-cd53-5e8a-b9d2-5e35a45f196c`) lines 152-169 [crates/gcore/src/ai/mod.rs:152-169]
  - Signature: `pub fn build_json_request<T>(`
  - Purpose: Indexed function `build_json_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:152-169]
- `build_multipart_request` (function) component `build_multipart_request [function]` (`8b11e1be-5b59-539e-a4f6-f0d507fa3768`) lines 171-201 [crates/gcore/src/ai/mod.rs:171-201]
  - Signature: `pub fn build_multipart_request(`
  - Purpose: Indexed function `build_multipart_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:171-201]
- `apply_api_key` (function) component `apply_api_key [function]` (`7b88d6da-e416-571d-acf7-30f2983a0213`) lines 204-209 [crates/gcore/src/ai/mod.rs:204-209]
  - Signature: `fn apply_api_key(request: RequestBuilder, binding: &CapabilityBinding) -> RequestBuilder {`
  - Purpose: Indexed function `apply_api_key` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:204-209]
- `timeout_for` (function) component `timeout_for [function]` (`288cea22-62db-5cd7-8d81-47a5b927d621`) lines 211-218 [crates/gcore/src/ai/mod.rs:211-218]
  - Signature: `fn timeout_for(capability: AiCapability) -> Duration {`
  - Purpose: Indexed function `timeout_for` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:211-218]
- `retry_with_backoff` (function) component `retry_with_backoff [function]` (`94e6bc19-a8a2-5e4c-bd8a-da355a23f463`) lines 220-235 [crates/gcore/src/ai/mod.rs:220-235]
  - Signature: `pub fn retry_with_backoff<T>(`
  - Purpose: Indexed function `retry_with_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:220-235]
- `is_retryable` (function) component `is_retryable [function]` (`0034cc07-303d-5381-9144-11591a1833d4`) lines 237-248 [crates/gcore/src/ai/mod.rs:237-248]
  - Signature: `fn is_retryable(error: &AiError) -> bool {`
  - Purpose: Indexed function `is_retryable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:237-248]
- `retry_delay` (function) component `retry_delay [function]` (`b973fc1b-5383-5f7b-9b52-cb80df401c30`) lines 250-258 [crates/gcore/src/ai/mod.rs:250-258]
  - Signature: `fn retry_delay(error: &AiError, retry_index: usize) -> Duration {`
  - Purpose: Indexed function `retry_delay` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:250-258]
- `jitter` (function) component `jitter [function]` (`20c216cb-9f02-5325-9bf3-d1ed06dd6f91`) lines 260-262 [crates/gcore/src/ai/mod.rs:260-262]
  - Signature: `fn jitter() -> Duration {`
  - Purpose: Indexed function `jitter` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:260-262]
- `parse_json_response` (function) component `parse_json_response [function]` (`a3239c25-8ddc-538e-baa3-ece77b66908c`) lines 264-297 [crates/gcore/src/ai/mod.rs:264-297]
  - Signature: `fn parse_json_response(response: Response) -> Result<serde_json::Value, AiError> {`
  - Purpose: Indexed function `parse_json_response` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:264-297]
- `parse_retry_after` (function) component `parse_retry_after [function]` (`0fa3fced-36c4-59d0-b42d-7123046d90d7`) lines 299-310 [crates/gcore/src/ai/mod.rs:299-310]
  - Signature: `fn parse_retry_after(value: &str) -> Option<Duration> {`
  - Purpose: Indexed function `parse_retry_after` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:299-310]
- `reqwest_error` (function) component `reqwest_error [function]` (`c1ba8fce-c141-5eec-abad-7f6c7b720f3d`) lines 312-318 [crates/gcore/src/ai/mod.rs:312-318]
  - Signature: `fn reqwest_error(error: reqwest::Error) -> AiError {`
  - Purpose: Indexed function `reqwest_error` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:312-318]
- `duration_to_ms` (function) component `duration_to_ms [function]` (`72821b0b-9b72-5d9e-a06c-956a8bfae21d`) lines 320-322 [crates/gcore/src/ai/mod.rs:320-322]
  - Signature: `fn duration_to_ms(duration: Duration) -> u64 {`
  - Purpose: Indexed function `duration_to_ms` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:320-322]
- `chat_completions_url` (function) component `chat_completions_url [function]` (`b08e9691-7526-5f85-a51a-d8034d39322f`) lines 324-342 [crates/gcore/src/ai/mod.rs:324-342]
  - Signature: `fn chat_completions_url(cfg: &AiContext, capability: AiCapability) -> Result<String, AiError> {`
  - Purpose: Indexed function `chat_completions_url` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:324-342]
- `chat_api_root` (function) component `chat_api_root [function]` (`99b40713-77a1-523b-8538-bc4a91de2f8e`) lines 344-347 [crates/gcore/src/ai/mod.rs:344-347]
  - Signature: `fn chat_api_root(api_base: &str) -> &str {`
  - Purpose: Indexed function `chat_api_root` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:344-347]
- `chat_completion_content` (function) component `chat_completion_content [function]` (`a58e079f-24c0-5e54-8ab1-4b06408a953d`) lines 349-359 [crates/gcore/src/ai/mod.rs:349-359]
  - Signature: `fn chat_completion_content(value: &serde_json::Value) -> Result<String, AiError> {`
  - Purpose: Indexed function `chat_completion_content` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:349-359]
- `chat_completion_model` (function) component `chat_completion_model [function]` (`ce22a089-c955-53d2-b87b-77c57900350c`) lines 361-367 [crates/gcore/src/ai/mod.rs:361-367]
  - Signature: `fn chat_completion_model(value: &serde_json::Value) -> Option<String> {`
  - Purpose: Indexed function `chat_completion_model` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:361-367]
- `retry_caps_at_two` (function) component `retry_caps_at_two [function]` (`143aa9a9-113a-58d6-8646-298ca7675e6d`) lines 376-392 [crates/gcore/src/ai/mod.rs:376-392]
  - Signature: `fn retry_caps_at_two() {`
  - Purpose: Indexed function `retry_caps_at_two` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:376-392]
- `retry_honors_retry_after_before_exponential_backoff` (function) component `retry_honors_retry_after_before_exponential_backoff [function]` (`1c37eb23-5d40-580d-ad00-0bc37f768176`) lines 395-417 [crates/gcore/src/ai/mod.rs:395-417]
  - Signature: `fn retry_honors_retry_after_before_exponential_backoff() {`
  - Purpose: Indexed function `retry_honors_retry_after_before_exponential_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:395-417]
- `parse_retry_after_accepts_http_dates_and_clamps` (function) component `parse_retry_after_accepts_http_dates_and_clamps [function]` (`c42531d7-b6b0-5b1a-8489-bba7f9608c68`) lines 420-433 [crates/gcore/src/ai/mod.rs:420-433]
  - Signature: `fn parse_retry_after_accepts_http_dates_and_clamps() {`
  - Purpose: Indexed function `parse_retry_after_accepts_http_dates_and_clamps` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:420-433]
- `embeddings_use_shorter_timeout_than_generation` (function) component `embeddings_use_shorter_timeout_than_generation [function]` (`eb4791f6-4ac7-5942-9f69-327dde783e18`) lines 436-440 [crates/gcore/src/ai/mod.rs:436-440]
  - Signature: `fn embeddings_use_shorter_timeout_than_generation() {`
  - Purpose: Indexed function `embeddings_use_shorter_timeout_than_generation` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:436-440]
- `text_generation_outlasts_vision_for_local_reasoning_models` (function) component `text_generation_outlasts_vision_for_local_reasoning_models [function]` (`b1b17622-92e4-58d1-b212-b6035106f379`) lines 443-450 [crates/gcore/src/ai/mod.rs:443-450]
  - Signature: `fn text_generation_outlasts_vision_for_local_reasoning_models() {`
  - Purpose: Indexed function `text_generation_outlasts_vision_for_local_reasoning_models` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:443-450]
- `chat_api_root_trims_trailing_v1_segment` (function) component `chat_api_root_trims_trailing_v1_segment [function]` (`ab19bf8e-6883-5513-9091-b66a14a42988`) lines 453-466 [crates/gcore/src/ai/mod.rs:453-466]
  - Signature: `fn chat_api_root_trims_trailing_v1_segment() {`
  - Purpose: Indexed function `chat_api_root_trims_trailing_v1_segment` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:453-466]
- `effective_route_auto_falls_through_per_capability` (function) component `effective_route_auto_falls_through_per_capability [function]` (`da14e39f-b323-51c7-afff-c507513a5b0c`) lines 469-508 [crates/gcore/src/ai/mod.rs:469-508]
  - Signature: `fn effective_route_auto_falls_through_per_capability() {`
  - Purpose: Indexed function `effective_route_auto_falls_through_per_capability` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:469-508]
- `effective_route_explicit_routing_modes_are_forced` (function) component `effective_route_explicit_routing_modes_are_forced [function]` (`d0e67e30-a452-5c3a-98b2-37b54b69188e`) lines 511-546 [crates/gcore/src/ai/mod.rs:511-546]
  - Signature: `fn effective_route_explicit_routing_modes_are_forced() {`
  - Purpose: Indexed function `effective_route_explicit_routing_modes_are_forced` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:511-546]
- `auto_uses_explicit_direct_config_when_daemon_unavailable` (function) component `auto_uses_explicit_direct_config_when_daemon_unavailable [function]` (`4ac9e6c1-3dd5-5bde-8acc-ae6b49965dac`) lines 549-579 [crates/gcore/src/ai/mod.rs:549-579]
  - Signature: `fn auto_uses_explicit_direct_config_when_daemon_unavailable() {`
  - Purpose: Indexed function `auto_uses_explicit_direct_config_when_daemon_unavailable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:549-579]
- `binding` (function) component `binding [function]` (`546e5000-7aaf-5018-91d1-86626b20c60a`) lines 581-594 [crates/gcore/src/ai/mod.rs:581-594]
  - Signature: `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {`
  - Purpose: Indexed function `binding` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:581-594]

