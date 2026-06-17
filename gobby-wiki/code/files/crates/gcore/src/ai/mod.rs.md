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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/mod.rs:31-35](crates/gcore/src/ai/mod.rs#L31-L35), [crates/gcore/src/ai/mod.rs:37-48](crates/gcore/src/ai/mod.rs#L37-L48), [crates/gcore/src/ai/mod.rs:50-62](crates/gcore/src/ai/mod.rs#L50-L62), [crates/gcore/src/ai/mod.rs:64-76](crates/gcore/src/ai/mod.rs#L64-L76), [crates/gcore/src/ai/mod.rs:79-82](crates/gcore/src/ai/mod.rs#L79-L82), [crates/gcore/src/ai/mod.rs:85-89](crates/gcore/src/ai/mod.rs#L85-L89), [crates/gcore/src/ai/mod.rs:91-108](crates/gcore/src/ai/mod.rs#L91-L108), [crates/gcore/src/ai/mod.rs:110-135](crates/gcore/src/ai/mod.rs#L110-L135), [crates/gcore/src/ai/mod.rs:137-142](crates/gcore/src/ai/mod.rs#L137-L142), [crates/gcore/src/ai/mod.rs:144-146](crates/gcore/src/ai/mod.rs#L144-L146), [crates/gcore/src/ai/mod.rs:148-150](crates/gcore/src/ai/mod.rs#L148-L150), [crates/gcore/src/ai/mod.rs:152-169](crates/gcore/src/ai/mod.rs#L152-L169), [crates/gcore/src/ai/mod.rs:171-201](crates/gcore/src/ai/mod.rs#L171-L201), [crates/gcore/src/ai/mod.rs:204-209](crates/gcore/src/ai/mod.rs#L204-L209), [crates/gcore/src/ai/mod.rs:211-218](crates/gcore/src/ai/mod.rs#L211-L218), [crates/gcore/src/ai/mod.rs:220-235](crates/gcore/src/ai/mod.rs#L220-L235), [crates/gcore/src/ai/mod.rs:237-248](crates/gcore/src/ai/mod.rs#L237-L248), [crates/gcore/src/ai/mod.rs:250-258](crates/gcore/src/ai/mod.rs#L250-L258), [crates/gcore/src/ai/mod.rs:260-262](crates/gcore/src/ai/mod.rs#L260-L262), [crates/gcore/src/ai/mod.rs:264-297](crates/gcore/src/ai/mod.rs#L264-L297), [crates/gcore/src/ai/mod.rs:299-310](crates/gcore/src/ai/mod.rs#L299-L310), [crates/gcore/src/ai/mod.rs:312-318](crates/gcore/src/ai/mod.rs#L312-L318), [crates/gcore/src/ai/mod.rs:320-322](crates/gcore/src/ai/mod.rs#L320-L322), [crates/gcore/src/ai/mod.rs:324-342](crates/gcore/src/ai/mod.rs#L324-L342), [crates/gcore/src/ai/mod.rs:344-347](crates/gcore/src/ai/mod.rs#L344-L347), [crates/gcore/src/ai/mod.rs:349-359](crates/gcore/src/ai/mod.rs#L349-L359), [crates/gcore/src/ai/mod.rs:361-367](crates/gcore/src/ai/mod.rs#L361-L367), [crates/gcore/src/ai/mod.rs:376-392](crates/gcore/src/ai/mod.rs#L376-L392), [crates/gcore/src/ai/mod.rs:395-417](crates/gcore/src/ai/mod.rs#L395-L417), [crates/gcore/src/ai/mod.rs:420-433](crates/gcore/src/ai/mod.rs#L420-L433), [crates/gcore/src/ai/mod.rs:436-440](crates/gcore/src/ai/mod.rs#L436-L440), [crates/gcore/src/ai/mod.rs:443-450](crates/gcore/src/ai/mod.rs#L443-L450), [crates/gcore/src/ai/mod.rs:453-466](crates/gcore/src/ai/mod.rs#L453-L466), [crates/gcore/src/ai/mod.rs:469-508](crates/gcore/src/ai/mod.rs#L469-L508), [crates/gcore/src/ai/mod.rs:511-546](crates/gcore/src/ai/mod.rs#L511-L546), [crates/gcore/src/ai/mod.rs:549-579](crates/gcore/src/ai/mod.rs#L549-L579), [crates/gcore/src/ai/mod.rs:581-594](crates/gcore/src/ai/mod.rs#L581-L594)

</details>

# crates/gcore/src/ai/mod.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This module centralizes AI transport and routing for `gcore`: it picks the effective route for each capability from `AiContext` and `AiRouting`, preferring daemon when available and otherwise falling back to direct or off, with explicit handling for bindings and probe results. It also builds and sends JSON or multipart requests, applies API keys and capability-specific timeouts, parses text/transcription/vision and chat-completions responses, and implements retry logic with backoff and `Retry-After` support; the module re-exports the capability-specific submodules for daemon, embeddings, probe, text, transcription, and vision.
[crates/gcore/src/ai/mod.rs:31-35]
[crates/gcore/src/ai/mod.rs:37-48]
[crates/gcore/src/ai/mod.rs:50-62]
[crates/gcore/src/ai/mod.rs:64-76]
[crates/gcore/src/ai/mod.rs:79-82]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `effective_route` | function | `pub fn effective_route(context: &AiContext, capability: AiCapability) -> AiRouting {` | `effective_route [function]` | `7f89060f-a6e2-567f-8875-ecc1d63bb8f0` | 31-35 [crates/gcore/src/ai/mod.rs:31-35] | Indexed function `effective_route` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:31-35] |
| `effective_route_with_probe` | function | `fn effective_route_with_probe(` | `effective_route_with_probe [function]` | `ba15d92b-546d-5fba-84af-962924e83744` | 37-48 [crates/gcore/src/ai/mod.rs:37-48] | Indexed function `effective_route_with_probe` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:37-48] |
| `daemon_route_or_fallback` | function | `fn daemon_route_or_fallback(` | `daemon_route_or_fallback [function]` | `d748e96c-668a-5e85-a419-39df03dc7534` | 50-62 [crates/gcore/src/ai/mod.rs:50-62] | Indexed function `daemon_route_or_fallback` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:50-62] |
| `direct_route_or_off` | function | `fn direct_route_or_off(context: &AiContext, capability: AiCapability) -> AiRouting {` | `direct_route_or_off [function]` | `5c23eaa1-07fb-5c1a-b22f-d4490145b0b7` | 64-76 [crates/gcore/src/ai/mod.rs:64-76] | Indexed function `direct_route_or_off` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:64-76] |
| `AiTransport` | class | `pub struct AiTransport<'a> {` | `AiTransport [class]` | `180a310a-8d01-53ee-a9ae-ed6f8f7e7f27` | 79-82 [crates/gcore/src/ai/mod.rs:79-82] | Indexed class `AiTransport` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:79-82] |
| `new` | function | `pub fn new(context: &'a AiContext) -> Result<Self, AiError> {` | `new [function]` | `f2706583-a628-5ffe-966d-bd49cec75939` | 85-89 [crates/gcore/src/ai/mod.rs:85-89] | Indexed function `new` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:85-89] |
| `post_json` | function | `pub fn post_json<T>(` | `post_json [function]` | `e082eff8-11d3-57f6-b9a8-701d46711e66` | 91-108 [crates/gcore/src/ai/mod.rs:91-108] | Indexed function `post_json` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:91-108] |
| `post_multipart` | function | `pub fn post_multipart(` | `post_multipart [function]` | `294ff439-365a-561b-a659-4850992be683` | 110-135 [crates/gcore/src/ai/mod.rs:110-135] | Indexed function `post_multipart` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:110-135] |
| `parse_transcription` | function | `pub fn parse_transcription(` | `parse_transcription [function]` | `f34172c1-25a5-5f04-9884-382b86cdd0a5` | 137-142 [crates/gcore/src/ai/mod.rs:137-142] | Indexed function `parse_transcription` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:137-142] |
| `parse_vision` | function | `pub fn parse_vision(&self, value: serde_json::Value) -> Result<VisionResult, AiError> {` | `parse_vision [function]` | `586d5323-0a44-5219-9128-f5131b14fbab` | 144-146 [crates/gcore/src/ai/mod.rs:144-146] | Indexed function `parse_vision` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:144-146] |
| `parse_text` | function | `pub fn parse_text(&self, value: serde_json::Value) -> Result<TextResult, AiError> {` | `parse_text [function]` | `0a3c1953-81c4-5755-a522-8fafb180f32c` | 148-150 [crates/gcore/src/ai/mod.rs:148-150] | Indexed function `parse_text` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:148-150] |
| `build_json_request` | function | `pub fn build_json_request<T>(` | `build_json_request [function]` | `89ec5e8e-cd53-5e8a-b9d2-5e35a45f196c` | 152-169 [crates/gcore/src/ai/mod.rs:152-169] | Indexed function `build_json_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:152-169] |
| `build_multipart_request` | function | `pub fn build_multipart_request(` | `build_multipart_request [function]` | `8b11e1be-5b59-539e-a4f6-f0d507fa3768` | 171-201 [crates/gcore/src/ai/mod.rs:171-201] | Indexed function `build_multipart_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:171-201] |
| `apply_api_key` | function | `fn apply_api_key(request: RequestBuilder, binding: &CapabilityBinding) -> RequestBuilder {` | `apply_api_key [function]` | `7b88d6da-e416-571d-acf7-30f2983a0213` | 204-209 [crates/gcore/src/ai/mod.rs:204-209] | Indexed function `apply_api_key` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:204-209] |
| `timeout_for` | function | `fn timeout_for(capability: AiCapability) -> Duration {` | `timeout_for [function]` | `288cea22-62db-5cd7-8d81-47a5b927d621` | 211-218 [crates/gcore/src/ai/mod.rs:211-218] | Indexed function `timeout_for` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:211-218] |
| `retry_with_backoff` | function | `pub fn retry_with_backoff<T>(` | `retry_with_backoff [function]` | `94e6bc19-a8a2-5e4c-bd8a-da355a23f463` | 220-235 [crates/gcore/src/ai/mod.rs:220-235] | Indexed function `retry_with_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:220-235] |
| `is_retryable` | function | `fn is_retryable(error: &AiError) -> bool {` | `is_retryable [function]` | `0034cc07-303d-5381-9144-11591a1833d4` | 237-248 [crates/gcore/src/ai/mod.rs:237-248] | Indexed function `is_retryable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:237-248] |
| `retry_delay` | function | `fn retry_delay(error: &AiError, retry_index: usize) -> Duration {` | `retry_delay [function]` | `b973fc1b-5383-5f7b-9b52-cb80df401c30` | 250-258 [crates/gcore/src/ai/mod.rs:250-258] | Indexed function `retry_delay` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:250-258] |
| `jitter` | function | `fn jitter() -> Duration {` | `jitter [function]` | `20c216cb-9f02-5325-9bf3-d1ed06dd6f91` | 260-262 [crates/gcore/src/ai/mod.rs:260-262] | Indexed function `jitter` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:260-262] |
| `parse_json_response` | function | `fn parse_json_response(response: Response) -> Result<serde_json::Value, AiError> {` | `parse_json_response [function]` | `a3239c25-8ddc-538e-baa3-ece77b66908c` | 264-297 [crates/gcore/src/ai/mod.rs:264-297] | Indexed function `parse_json_response` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:264-297] |
| `parse_retry_after` | function | `fn parse_retry_after(value: &str) -> Option<Duration> {` | `parse_retry_after [function]` | `0fa3fced-36c4-59d0-b42d-7123046d90d7` | 299-310 [crates/gcore/src/ai/mod.rs:299-310] | Indexed function `parse_retry_after` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:299-310] |
| `reqwest_error` | function | `fn reqwest_error(error: reqwest::Error) -> AiError {` | `reqwest_error [function]` | `c1ba8fce-c141-5eec-abad-7f6c7b720f3d` | 312-318 [crates/gcore/src/ai/mod.rs:312-318] | Indexed function `reqwest_error` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:312-318] |
| `duration_to_ms` | function | `fn duration_to_ms(duration: Duration) -> u64 {` | `duration_to_ms [function]` | `72821b0b-9b72-5d9e-a06c-956a8bfae21d` | 320-322 [crates/gcore/src/ai/mod.rs:320-322] | Indexed function `duration_to_ms` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:320-322] |
| `chat_completions_url` | function | `fn chat_completions_url(cfg: &AiContext, capability: AiCapability) -> Result<String, AiError> {` | `chat_completions_url [function]` | `b08e9691-7526-5f85-a51a-d8034d39322f` | 324-342 [crates/gcore/src/ai/mod.rs:324-342] | Indexed function `chat_completions_url` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:324-342] |
| `chat_api_root` | function | `fn chat_api_root(api_base: &str) -> &str {` | `chat_api_root [function]` | `99b40713-77a1-523b-8538-bc4a91de2f8e` | 344-347 [crates/gcore/src/ai/mod.rs:344-347] | Indexed function `chat_api_root` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:344-347] |
| `chat_completion_content` | function | `fn chat_completion_content(value: &serde_json::Value) -> Result<String, AiError> {` | `chat_completion_content [function]` | `a58e079f-24c0-5e54-8ab1-4b06408a953d` | 349-359 [crates/gcore/src/ai/mod.rs:349-359] | Indexed function `chat_completion_content` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:349-359] |
| `chat_completion_model` | function | `fn chat_completion_model(value: &serde_json::Value) -> Option<String> {` | `chat_completion_model [function]` | `ce22a089-c955-53d2-b87b-77c57900350c` | 361-367 [crates/gcore/src/ai/mod.rs:361-367] | Indexed function `chat_completion_model` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:361-367] |
| `retry_caps_at_two` | function | `fn retry_caps_at_two() {` | `retry_caps_at_two [function]` | `143aa9a9-113a-58d6-8646-298ca7675e6d` | 376-392 [crates/gcore/src/ai/mod.rs:376-392] | Indexed function `retry_caps_at_two` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:376-392] |
| `retry_honors_retry_after_before_exponential_backoff` | function | `fn retry_honors_retry_after_before_exponential_backoff() {` | `retry_honors_retry_after_before_exponential_backoff [function]` | `1c37eb23-5d40-580d-ad00-0bc37f768176` | 395-417 [crates/gcore/src/ai/mod.rs:395-417] | Indexed function `retry_honors_retry_after_before_exponential_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:395-417] |
| `parse_retry_after_accepts_http_dates_and_clamps` | function | `fn parse_retry_after_accepts_http_dates_and_clamps() {` | `parse_retry_after_accepts_http_dates_and_clamps [function]` | `c42531d7-b6b0-5b1a-8489-bba7f9608c68` | 420-433 [crates/gcore/src/ai/mod.rs:420-433] | Indexed function `parse_retry_after_accepts_http_dates_and_clamps` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:420-433] |
| `embeddings_use_shorter_timeout_than_generation` | function | `fn embeddings_use_shorter_timeout_than_generation() {` | `embeddings_use_shorter_timeout_than_generation [function]` | `eb4791f6-4ac7-5942-9f69-327dde783e18` | 436-440 [crates/gcore/src/ai/mod.rs:436-440] | Indexed function `embeddings_use_shorter_timeout_than_generation` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:436-440] |
| `text_generation_outlasts_vision_for_local_reasoning_models` | function | `fn text_generation_outlasts_vision_for_local_reasoning_models() {` | `text_generation_outlasts_vision_for_local_reasoning_models [function]` | `b1b17622-92e4-58d1-b212-b6035106f379` | 443-450 [crates/gcore/src/ai/mod.rs:443-450] | Indexed function `text_generation_outlasts_vision_for_local_reasoning_models` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:443-450] |
| `chat_api_root_trims_trailing_v1_segment` | function | `fn chat_api_root_trims_trailing_v1_segment() {` | `chat_api_root_trims_trailing_v1_segment [function]` | `ab19bf8e-6883-5513-9091-b66a14a42988` | 453-466 [crates/gcore/src/ai/mod.rs:453-466] | Indexed function `chat_api_root_trims_trailing_v1_segment` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:453-466] |
| `effective_route_auto_falls_through_per_capability` | function | `fn effective_route_auto_falls_through_per_capability() {` | `effective_route_auto_falls_through_per_capability [function]` | `da14e39f-b323-51c7-afff-c507513a5b0c` | 469-508 [crates/gcore/src/ai/mod.rs:469-508] | Indexed function `effective_route_auto_falls_through_per_capability` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:469-508] |
| `effective_route_explicit_routing_modes_are_forced` | function | `fn effective_route_explicit_routing_modes_are_forced() {` | `effective_route_explicit_routing_modes_are_forced [function]` | `d0e67e30-a452-5c3a-98b2-37b54b69188e` | 511-546 [crates/gcore/src/ai/mod.rs:511-546] | Indexed function `effective_route_explicit_routing_modes_are_forced` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:511-546] |
| `auto_uses_explicit_direct_config_when_daemon_unavailable` | function | `fn auto_uses_explicit_direct_config_when_daemon_unavailable() {` | `auto_uses_explicit_direct_config_when_daemon_unavailable [function]` | `4ac9e6c1-3dd5-5bde-8acc-ae6b49965dac` | 549-579 [crates/gcore/src/ai/mod.rs:549-579] | Indexed function `auto_uses_explicit_direct_config_when_daemon_unavailable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:549-579] |
| `binding` | function | `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {` | `binding [function]` | `546e5000-7aaf-5018-91d1-86626b20c60a` | 581-594 [crates/gcore/src/ai/mod.rs:581-594] | Indexed function `binding` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:581-594] |
