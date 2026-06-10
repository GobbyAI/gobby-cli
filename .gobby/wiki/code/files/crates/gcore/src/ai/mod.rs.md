---
title: crates/gcore/src/ai/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/mod.rs
  ranges:
  - 26-30
  - 32-43
  - 45-57
  - 59-71
  - 74-77
  - 80-84
  - 86-103
  - 105-130
  - 132-137
  - 139-141
  - 143-145
  - 147-164
  - 166-196
  - 199-204
  - 206-212
  - 214-229
  - 231-242
  - 244-252
  - 254-256
  - 258-291
  - 293-304
  - 306-312
  - 314-316
  - 318-336
  - 338-341
  - 343-353
  - 355-361
  - 364-368
  - 370-387
  - 396-412
  - 415-437
  - 440-453
  - 456-460
  - 463-476
  - 479-499
  - 502-541
  - 544-579
  - 582-612
  - 614-626
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/mod.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

`crates/gcore/src/ai/mod.rs` exposes 39 indexed API symbols.
[crates/gcore/src/ai/mod.rs:26-30]
[crates/gcore/src/ai/mod.rs:32-43]
[crates/gcore/src/ai/mod.rs:45-57]
[crates/gcore/src/ai/mod.rs:59-71]
[crates/gcore/src/ai/mod.rs:74-77]
[crates/gcore/src/ai/mod.rs:80-84]
[crates/gcore/src/ai/mod.rs:86-103]
[crates/gcore/src/ai/mod.rs:105-130]
[crates/gcore/src/ai/mod.rs:132-137]
[crates/gcore/src/ai/mod.rs:139-141]
[crates/gcore/src/ai/mod.rs:143-145]
[crates/gcore/src/ai/mod.rs:147-164]
[crates/gcore/src/ai/mod.rs:166-196]
[crates/gcore/src/ai/mod.rs:199-204]
[crates/gcore/src/ai/mod.rs:206-212]
[crates/gcore/src/ai/mod.rs:214-229]
[crates/gcore/src/ai/mod.rs:231-242]
[crates/gcore/src/ai/mod.rs:244-252]
[crates/gcore/src/ai/mod.rs:254-256]
[crates/gcore/src/ai/mod.rs:258-291]
[crates/gcore/src/ai/mod.rs:293-304]
[crates/gcore/src/ai/mod.rs:306-312]
[crates/gcore/src/ai/mod.rs:314-316]
[crates/gcore/src/ai/mod.rs:318-336]
[crates/gcore/src/ai/mod.rs:338-341]
[crates/gcore/src/ai/mod.rs:343-353]
[crates/gcore/src/ai/mod.rs:355-361]
[crates/gcore/src/ai/mod.rs:364-368]
[crates/gcore/src/ai/mod.rs:370-387]
[crates/gcore/src/ai/mod.rs:396-412]
[crates/gcore/src/ai/mod.rs:415-437]
[crates/gcore/src/ai/mod.rs:440-453]
[crates/gcore/src/ai/mod.rs:456-460]
[crates/gcore/src/ai/mod.rs:463-476]
[crates/gcore/src/ai/mod.rs:479-499]
[crates/gcore/src/ai/mod.rs:502-541]
[crates/gcore/src/ai/mod.rs:544-579]
[crates/gcore/src/ai/mod.rs:582-612]
[crates/gcore/src/ai/mod.rs:614-626]

## API Symbols

- `effective_route` (function) component `effective_route [function]` (`fd18e8f6-8ca8-55ce-afa0-8e80d97160e6`) lines 26-30 [crates/gcore/src/ai/mod.rs:26-30]
  - Signature: `pub fn effective_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `effective_route` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:26-30]
- `effective_route_with_probe` (function) component `effective_route_with_probe [function]` (`b33cfcb9-5338-57b9-81b6-18086d4195c0`) lines 32-43 [crates/gcore/src/ai/mod.rs:32-43]
  - Signature: `fn effective_route_with_probe(`
  - Purpose: Indexed function `effective_route_with_probe` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:32-43]
- `daemon_route_or_fallback` (function) component `daemon_route_or_fallback [function]` (`39fd8dff-50bb-5c9b-9363-a1e7337d82bd`) lines 45-57 [crates/gcore/src/ai/mod.rs:45-57]
  - Signature: `fn daemon_route_or_fallback(`
  - Purpose: Indexed function `daemon_route_or_fallback` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:45-57]
- `direct_route_or_off` (function) component `direct_route_or_off [function]` (`c51842d9-0e85-51ee-9620-3604dc740254`) lines 59-71 [crates/gcore/src/ai/mod.rs:59-71]
  - Signature: `fn direct_route_or_off(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `direct_route_or_off` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:59-71]
- `AiTransport` (class) component `AiTransport [class]` (`1b90b36d-bf0d-539a-8e7c-a9be8659f88f`) lines 74-77 [crates/gcore/src/ai/mod.rs:74-77]
  - Signature: `pub struct AiTransport<'a> {`
  - Purpose: Indexed class `AiTransport` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:74-77]
- `new` (function) component `new [function]` (`36e134c2-abbe-565f-93cd-be7ece2a2d70`) lines 80-84 [crates/gcore/src/ai/mod.rs:80-84]
  - Signature: `pub fn new(context: &'a AiContext) -> Result<Self, AiError> {`
  - Purpose: Indexed function `new` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:80-84]
- `post_json` (function) component `post_json [function]` (`e16f753b-cf76-5124-91ff-68789a9c8451`) lines 86-103 [crates/gcore/src/ai/mod.rs:86-103]
  - Signature: `pub fn post_json<T>(`
  - Purpose: Indexed function `post_json` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:86-103]
- `post_multipart` (function) component `post_multipart [function]` (`00b7e2c2-a976-569d-ae62-8d9397c8d528`) lines 105-130 [crates/gcore/src/ai/mod.rs:105-130]
  - Signature: `pub fn post_multipart(`
  - Purpose: Indexed function `post_multipart` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:105-130]
- `parse_transcription` (function) component `parse_transcription [function]` (`7dda0313-d33d-5142-b0d7-89a54ce6553e`) lines 132-137 [crates/gcore/src/ai/mod.rs:132-137]
  - Signature: `pub fn parse_transcription(`
  - Purpose: Indexed function `parse_transcription` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:132-137]
- `parse_vision` (function) component `parse_vision [function]` (`8b114ce9-028c-5fca-b68e-b4061323903d`) lines 139-141 [crates/gcore/src/ai/mod.rs:139-141]
  - Signature: `pub fn parse_vision(&self, value: serde_json::Value) -> Result<VisionResult, AiError> {`
  - Purpose: Indexed function `parse_vision` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:139-141]
- `parse_text` (function) component `parse_text [function]` (`7a18e1e6-3cfb-5aa9-8810-328bf3b76784`) lines 143-145 [crates/gcore/src/ai/mod.rs:143-145]
  - Signature: `pub fn parse_text(&self, value: serde_json::Value) -> Result<TextResult, AiError> {`
  - Purpose: Indexed function `parse_text` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:143-145]
- `build_json_request` (function) component `build_json_request [function]` (`d67a3cee-1742-5437-8b1c-207bf7c3a267`) lines 147-164 [crates/gcore/src/ai/mod.rs:147-164]
  - Signature: `pub fn build_json_request<T>(`
  - Purpose: Indexed function `build_json_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:147-164]
- `build_multipart_request` (function) component `build_multipart_request [function]` (`08eb1ac1-2c5d-5b1b-85c7-6b0beeb3cc28`) lines 166-196 [crates/gcore/src/ai/mod.rs:166-196]
  - Signature: `pub fn build_multipart_request(`
  - Purpose: Indexed function `build_multipart_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:166-196]
- `apply_api_key` (function) component `apply_api_key [function]` (`5b575d6f-8650-5e4f-9991-d0590dbc8913`) lines 199-204 [crates/gcore/src/ai/mod.rs:199-204]
  - Signature: `fn apply_api_key(request: RequestBuilder, binding: &CapabilityBinding) -> RequestBuilder {`
  - Purpose: Indexed function `apply_api_key` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:199-204]
- `timeout_for` (function) component `timeout_for [function]` (`ed9aacab-cc4b-5c75-9828-4a60a503074e`) lines 206-212 [crates/gcore/src/ai/mod.rs:206-212]
  - Signature: `fn timeout_for(capability: AiCapability) -> Duration {`
  - Purpose: Indexed function `timeout_for` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:206-212]
- `retry_with_backoff` (function) component `retry_with_backoff [function]` (`5fdb4a5f-fa52-5c01-86be-574bca317324`) lines 214-229 [crates/gcore/src/ai/mod.rs:214-229]
  - Signature: `pub fn retry_with_backoff<T>(`
  - Purpose: Indexed function `retry_with_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:214-229]
- `is_retryable` (function) component `is_retryable [function]` (`11c11e1f-7e43-549e-9fd2-3ff035c9dc5d`) lines 231-242 [crates/gcore/src/ai/mod.rs:231-242]
  - Signature: `fn is_retryable(error: &AiError) -> bool {`
  - Purpose: Indexed function `is_retryable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:231-242]
- `retry_delay` (function) component `retry_delay [function]` (`a4d1ef4a-1332-5a91-a3dd-e12680f25498`) lines 244-252 [crates/gcore/src/ai/mod.rs:244-252]
  - Signature: `fn retry_delay(error: &AiError, retry_index: usize) -> Duration {`
  - Purpose: Indexed function `retry_delay` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:244-252]
- `jitter` (function) component `jitter [function]` (`c25e45e9-52f3-5b83-8b28-183a5525f038`) lines 254-256 [crates/gcore/src/ai/mod.rs:254-256]
  - Signature: `fn jitter() -> Duration {`
  - Purpose: Indexed function `jitter` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:254-256]
- `parse_json_response` (function) component `parse_json_response [function]` (`deb71d50-da13-558c-bbf0-4f243ab2d8b1`) lines 258-291 [crates/gcore/src/ai/mod.rs:258-291]
  - Signature: `fn parse_json_response(response: Response) -> Result<serde_json::Value, AiError> {`
  - Purpose: Indexed function `parse_json_response` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:258-291]
- `parse_retry_after` (function) component `parse_retry_after [function]` (`0cad887f-5768-51d4-b8e8-ccc91a2b2f82`) lines 293-304 [crates/gcore/src/ai/mod.rs:293-304]
  - Signature: `fn parse_retry_after(value: &str) -> Option<Duration> {`
  - Purpose: Indexed function `parse_retry_after` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:293-304]
- `reqwest_error` (function) component `reqwest_error [function]` (`6a785960-3b5c-5a30-b792-6f4a3f8a341f`) lines 306-312 [crates/gcore/src/ai/mod.rs:306-312]
  - Signature: `fn reqwest_error(error: reqwest::Error) -> AiError {`
  - Purpose: Indexed function `reqwest_error` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:306-312]
- `duration_to_ms` (function) component `duration_to_ms [function]` (`09ae9823-97b5-5c40-8762-5d692ee8a16d`) lines 314-316 [crates/gcore/src/ai/mod.rs:314-316]
  - Signature: `fn duration_to_ms(duration: Duration) -> u64 {`
  - Purpose: Indexed function `duration_to_ms` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:314-316]
- `chat_completions_url` (function) component `chat_completions_url [function]` (`46dd96ed-13f8-561c-851f-d85ceb155ae9`) lines 318-336 [crates/gcore/src/ai/mod.rs:318-336]
  - Signature: `fn chat_completions_url(cfg: &AiContext, capability: AiCapability) -> Result<String, AiError> {`
  - Purpose: Indexed function `chat_completions_url` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:318-336]
- `chat_api_root` (function) component `chat_api_root [function]` (`eaa03480-83bc-5e31-a481-4403ad2506a8`) lines 338-341 [crates/gcore/src/ai/mod.rs:338-341]
  - Signature: `fn chat_api_root(api_base: &str) -> &str {`
  - Purpose: Indexed function `chat_api_root` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:338-341]
- `chat_completion_content` (function) component `chat_completion_content [function]` (`6c3eaa9e-df86-523d-a52c-74379c9c98c6`) lines 343-353 [crates/gcore/src/ai/mod.rs:343-353]
  - Signature: `fn chat_completion_content(value: &serde_json::Value) -> Result<String, AiError> {`
  - Purpose: Indexed function `chat_completion_content` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:343-353]
- `chat_completion_model` (function) component `chat_completion_model [function]` (`2e8aacca-e650-56fd-bb68-44c22ae4af7e`) lines 355-361 [crates/gcore/src/ai/mod.rs:355-361]
  - Signature: `fn chat_completion_model(value: &serde_json::Value) -> Option<String> {`
  - Purpose: Indexed function `chat_completion_model` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:355-361]
- `LocalBackendProbe` (class) component `LocalBackendProbe [class]` (`15351bf6-ea55-536d-a66d-529a2e7c21e9`) lines 364-368 [crates/gcore/src/ai/mod.rs:364-368]
  - Signature: `pub struct LocalBackendProbe {`
  - Purpose: Indexed class `LocalBackendProbe` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:364-368]
- `probe_local_backend` (function) component `probe_local_backend [function]` (`393d3832-f82d-5c24-87b3-f30935fd35d6`) lines 370-387 [crates/gcore/src/ai/mod.rs:370-387]
  - Signature: `pub fn probe_local_backend(api_base: &str) -> Result<LocalBackendProbe, AiError> {`
  - Purpose: Indexed function `probe_local_backend` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:370-387]
- `retry_caps_at_two` (function) component `retry_caps_at_two [function]` (`071af6b9-8f23-5f10-8a6d-d3497f8ab5e9`) lines 396-412 [crates/gcore/src/ai/mod.rs:396-412]
  - Signature: `fn retry_caps_at_two() {`
  - Purpose: Indexed function `retry_caps_at_two` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:396-412]
- `retry_honors_retry_after_before_exponential_backoff` (function) component `retry_honors_retry_after_before_exponential_backoff [function]` (`92bfdb8e-22c1-5cff-ab73-c966fc054887`) lines 415-437 [crates/gcore/src/ai/mod.rs:415-437]
  - Signature: `fn retry_honors_retry_after_before_exponential_backoff() {`
  - Purpose: Indexed function `retry_honors_retry_after_before_exponential_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:415-437]
- `parse_retry_after_accepts_http_dates_and_clamps` (function) component `parse_retry_after_accepts_http_dates_and_clamps [function]` (`4da35601-b766-516f-93bf-c45456afa521`) lines 440-453 [crates/gcore/src/ai/mod.rs:440-453]
  - Signature: `fn parse_retry_after_accepts_http_dates_and_clamps() {`
  - Purpose: Indexed function `parse_retry_after_accepts_http_dates_and_clamps` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:440-453]
- `embeddings_use_shorter_timeout_than_generation` (function) component `embeddings_use_shorter_timeout_than_generation [function]` (`661cd0e6-6902-54cc-9ec7-f91b1376f9d1`) lines 456-460 [crates/gcore/src/ai/mod.rs:456-460]
  - Signature: `fn embeddings_use_shorter_timeout_than_generation() {`
  - Purpose: Indexed function `embeddings_use_shorter_timeout_than_generation` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:456-460]
- `chat_api_root_trims_trailing_v1_segment` (function) component `chat_api_root_trims_trailing_v1_segment [function]` (`ddaee463-31c0-5562-97fd-91eaa8cd3174`) lines 463-476 [crates/gcore/src/ai/mod.rs:463-476]
  - Signature: `fn chat_api_root_trims_trailing_v1_segment() {`
  - Purpose: Indexed function `chat_api_root_trims_trailing_v1_segment` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:463-476]
- `probe_local_backend_returns_non_success_status` (function) component `probe_local_backend_returns_non_success_status [function]` (`20442fc0-f1f1-5e59-8f13-e94f5b7b28db`) lines 479-499 [crates/gcore/src/ai/mod.rs:479-499]
  - Signature: `fn probe_local_backend_returns_non_success_status() {`
  - Purpose: Indexed function `probe_local_backend_returns_non_success_status` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:479-499]
- `effective_route_auto_falls_through_per_capability` (function) component `effective_route_auto_falls_through_per_capability [function]` (`091b8105-73e2-511d-9ea2-e39522ebf5bd`) lines 502-541 [crates/gcore/src/ai/mod.rs:502-541]
  - Signature: `fn effective_route_auto_falls_through_per_capability() {`
  - Purpose: Indexed function `effective_route_auto_falls_through_per_capability` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:502-541]
- `effective_route_explicit_routing_modes_are_forced` (function) component `effective_route_explicit_routing_modes_are_forced [function]` (`83418144-4d48-56df-8e85-fb76ee42ec5a`) lines 544-579 [crates/gcore/src/ai/mod.rs:544-579]
  - Signature: `fn effective_route_explicit_routing_modes_are_forced() {`
  - Purpose: Indexed function `effective_route_explicit_routing_modes_are_forced` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:544-579]
- `auto_uses_explicit_direct_config_when_daemon_unavailable` (function) component `auto_uses_explicit_direct_config_when_daemon_unavailable [function]` (`986a14c0-407a-559c-b6cc-0314d5e88e56`) lines 582-612 [crates/gcore/src/ai/mod.rs:582-612]
  - Signature: `fn auto_uses_explicit_direct_config_when_daemon_unavailable() {`
  - Purpose: Indexed function `auto_uses_explicit_direct_config_when_daemon_unavailable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:582-612]
- `binding` (function) component `binding [function]` (`8b40854a-bfac-57bf-a297-f5c392f59b9c`) lines 614-626 [crates/gcore/src/ai/mod.rs:614-626]
  - Signature: `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {`
  - Purpose: Indexed function `binding` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:614-626]

