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

Central AI support module for `gcore`: it resolves the effective route for each `AiCapability`, choosing between `Off`, `Direct`, `Daemon`, or `Auto` based on the current `AiContext`, daemon probing, and whether a direct `api_base` is configured. It also defines `AiTransport`, which owns a `reqwest` client plus a borrowed context, and uses shared helpers to build authenticated JSON or multipart requests, apply capability-specific timeouts, send them with retry/backoff, and parse responses into the typed transcription, vision, or text results. The remaining helpers handle URL normalization, API-key injection, retryability and `Retry-After` parsing, plus test coverage for routing, timeout, and retry behavior.
[crates/gcore/src/ai/mod.rs:31-35]
[crates/gcore/src/ai/mod.rs:37-48]
[crates/gcore/src/ai/mod.rs:50-62]
[crates/gcore/src/ai/mod.rs:64-76]
[crates/gcore/src/ai/mod.rs:79-82]

## API Symbols

- `effective_route` (function) component `effective_route [function]` (`7f89060f-a6e2-567f-8875-ecc1d63bb8f0`) lines 31-35 [crates/gcore/src/ai/mod.rs:31-35]
  - Signature: `pub fn effective_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: 'effective_route' computes the routing decision for a given 'AiCapability' in an 'AiContext' by delegating to 'effective_route_with_probe' with a probe that marks the capability available based on 'probe::probe_daemon_capability(capability).available'. [crates/gcore/src/ai/mod.rs:31-35]
- `effective_route_with_probe` (function) component `effective_route_with_probe [function]` (`ba15d92b-546d-5fba-84af-962924e83744`) lines 37-48 [crates/gcore/src/ai/mod.rs:37-48]
  - Signature: `fn effective_route_with_probe(`
  - Purpose: Returns the route bound in 'context' for the given 'capability', preserving 'Off', 'Direct', and 'Daemon' as-is, and resolving 'Auto' by calling 'daemon_route_or_fallback' with the provided daemon-availability probe. [crates/gcore/src/ai/mod.rs:37-48]
- `daemon_route_or_fallback` (function) component `daemon_route_or_fallback [function]` (`d748e96c-668a-5e85-a419-39df03dc7534`) lines 50-62 [crates/gcore/src/ai/mod.rs:50-62]
  - Signature: `fn daemon_route_or_fallback(`
  - Purpose: Returns 'AiRouting::Daemon' when 'daemon_available(capability)' is true, otherwise delegates to 'direct_route_or_off(context, capability)' to select a direct route or 'Off'. [crates/gcore/src/ai/mod.rs:50-62]
- `direct_route_or_off` (function) component `direct_route_or_off [function]` (`5c23eaa1-07fb-5c1a-b22f-d4490145b0b7`) lines 64-76 [crates/gcore/src/ai/mod.rs:64-76]
  - Signature: `fn direct_route_or_off(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Returns 'AiRouting::Direct' when the selected capability binding has a non-empty trimmed 'api_base', otherwise returns 'AiRouting::Off'. [crates/gcore/src/ai/mod.rs:64-76]
- `AiTransport` (class) component `AiTransport [class]` (`180a310a-8d01-53ee-a9ae-ed6f8f7e7f27`) lines 79-82 [crates/gcore/src/ai/mod.rs:79-82]
  - Signature: `pub struct AiTransport<'a> {`
  - Purpose: 'AiTransport<'a>' is a transport object that owns an HTTP 'Client' and a borrowed 'AiContext', allowing AI-related requests to be executed using shared contextual state without taking ownership. [crates/gcore/src/ai/mod.rs:79-82]
- `new` (function) component `new [function]` (`f2706583-a628-5ffe-966d-bd49cec75939`) lines 85-89 [crates/gcore/src/ai/mod.rs:85-89]
  - Signature: `pub fn new(context: &'a AiContext) -> Result<Self, AiError> {`
  - Purpose: Constructs a new instance by creating a default 'reqwest::Client', converting any builder failure into 'AiError', and storing it together with the provided 'AiContext' reference. [crates/gcore/src/ai/mod.rs:85-89]
- `post_json` (function) component `post_json [function]` (`e082eff8-11d3-57f6-b9a8-701d46711e66`) lines 91-108 [crates/gcore/src/ai/mod.rs:91-108]
  - Signature: `pub fn post_json<T>(`
  - Purpose: Sends a serialized body as a JSON POST request for the given capability and URL, then retries with backoff while acquiring a rate-limit permit and returns the parsed 'serde_json::Value' or an 'AiError'. [crates/gcore/src/ai/mod.rs:91-108]
- `post_multipart` (function) component `post_multipart [function]` (`294ff439-365a-561b-a659-4850992be683`) lines 110-135 [crates/gcore/src/ai/mod.rs:110-135]
  - Signature: `pub fn post_multipart(`
  - Purpose: Acquires a concurrency permit, converts the provided byte buffer into shared 'Bytes', builds a multipart request with the given capability, URL, file field/name, and form fields, then sends it with retry/backoff and returns the parsed JSON response or 'AiError'. [crates/gcore/src/ai/mod.rs:110-135]
- `parse_transcription` (function) component `parse_transcription [function]` (`f34172c1-25a5-5f04-9884-382b86cdd0a5`) lines 137-142 [crates/gcore/src/ai/mod.rs:137-142]
  - Signature: `pub fn parse_transcription(`
  - Purpose: Parses a 'serde_json::Value' transcription payload by delegating to 'TranscriptionResult::from_wire_json' and returning either a 'TranscriptionResult' or an 'AiError'. [crates/gcore/src/ai/mod.rs:137-142]
- `parse_vision` (function) component `parse_vision [function]` (`586d5323-0a44-5219-9128-f5131b14fbab`) lines 144-146 [crates/gcore/src/ai/mod.rs:144-146]
  - Signature: `pub fn parse_vision(&self, value: serde_json::Value) -> Result<VisionResult, AiError> {`
  - Purpose: 'parse_vision' deserializes a 'serde_json::Value' into a 'VisionResult' by delegating to 'VisionResult::from_wire_json', returning an 'AiError' on failure. [crates/gcore/src/ai/mod.rs:144-146]
- `parse_text` (function) component `parse_text [function]` (`0a3c1953-81c4-5755-a522-8fafb180f32c`) lines 148-150 [crates/gcore/src/ai/mod.rs:148-150]
  - Signature: `pub fn parse_text(&self, value: serde_json::Value) -> Result<TextResult, AiError> {`
  - Purpose: Delegates deserialization of the provided 'serde_json::Value' to 'TextResult::from_wire_json' and returns the resulting 'TextResult' or 'AiError'. [crates/gcore/src/ai/mod.rs:148-150]
- `build_json_request` (function) component `build_json_request [function]` (`89ec5e8e-cd53-5e8a-b9d2-5e35a45f196c`) lines 152-169 [crates/gcore/src/ai/mod.rs:152-169]
  - Signature: `pub fn build_json_request<T>(`
  - Purpose: Builds a 'RequestBuilder' for a JSON 'POST' to the given URL with the serialized 'body', applies the capability-specific timeout, and injects the API key binding before returning 'Result<RequestBuilder, AiError>'. [crates/gcore/src/ai/mod.rs:152-169]
- `build_multipart_request` (function) component `build_multipart_request [function]` (`8b11e1be-5b59-539e-a4f6-f0d507fa3768`) lines 171-201 [crates/gcore/src/ai/mod.rs:171-201]
  - Signature: `pub fn build_multipart_request(`
  - Purpose: Builds an authenticated 'reqwest::RequestBuilder' for a multipart 'POST' to 'url' by attaching the provided bytes as a file part with the given field/name, appending each extra text field, enforcing a 'u64' length conversion, and returning a parse error if the payload is too large. [crates/gcore/src/ai/mod.rs:171-201]
- `apply_api_key` (function) component `apply_api_key [function]` (`7b88d6da-e416-571d-acf7-30f2983a0213`) lines 204-209 [crates/gcore/src/ai/mod.rs:204-209]
  - Signature: `fn apply_api_key(request: RequestBuilder, binding: &CapabilityBinding) -> RequestBuilder {`
  - Purpose: 'apply_api_key' returns the given 'RequestBuilder' unchanged unless 'binding.api_key' is present, in which case it adds an 'Authorization: Bearer <api_key>' header and returns the modified builder. [crates/gcore/src/ai/mod.rs:204-209]
- `timeout_for` (function) component `timeout_for [function]` (`288cea22-62db-5cd7-8d81-47a5b927d621`) lines 211-218 [crates/gcore/src/ai/mod.rs:211-218]
  - Signature: `fn timeout_for(capability: AiCapability) -> Duration {`
  - Purpose: Returns the 'Duration' timeout constant associated with an 'AiCapability', mapping audio transcription/translation to 'STT_CHUNK_TIMEOUT', embeddings to 'EMBEDDINGS_TIMEOUT', vision extraction to 'VISION_TIMEOUT', and text generation to 'TEXT_GENERATE_TIMEOUT'. [crates/gcore/src/ai/mod.rs:211-218]
- `retry_with_backoff` (function) component `retry_with_backoff [function]` (`94e6bc19-a8a2-5e4c-bd8a-da355a23f463`) lines 220-235 [crates/gcore/src/ai/mod.rs:220-235]
  - Signature: `pub fn retry_with_backoff<T>(`
  - Purpose: Executes 'operation' until it succeeds or a non-retryable error occurs, sleeping between attempts with an error- and attempt-dependent backoff delay for at most 'MAX_RETRIES' retries before returning the final 'AiError'. [crates/gcore/src/ai/mod.rs:220-235]
- `is_retryable` (function) component `is_retryable [function]` (`0034cc07-303d-5381-9144-11591a1833d4`) lines 237-248 [crates/gcore/src/ai/mod.rs:237-248]
  - Signature: `fn is_retryable(error: &AiError) -> bool {`
  - Purpose: 'is_retryable' returns 'true' for rate limits, transport failures with no status or with HTTP 408, 429, or any 5xx status, and HTTP status errors for 429 or any 5xx status, and returns 'false' for capability-unavailable, not-configured, and parse-failure errors. [crates/gcore/src/ai/mod.rs:237-248]
- `retry_delay` (function) component `retry_delay [function]` (`b973fc1b-5383-5f7b-9b52-cb80df401c30`) lines 250-258 [crates/gcore/src/ai/mod.rs:250-258]
  - Signature: `fn retry_delay(error: &AiError, retry_index: usize) -> Duration {`
  - Purpose: Returns the retry backoff duration by honoring an error-provided 'Retry-After' value capped at 'MAX_BACKOFF', otherwise computing 'BASE_BACKOFF << min(retry_index, 16)' plus jitter, saturating on overflow and capping the result at 'MAX_BACKOFF'. [crates/gcore/src/ai/mod.rs:250-258]
- `jitter` (function) component `jitter [function]` (`20c216cb-9f02-5325-9bf3-d1ed06dd6f91`) lines 260-262 [crates/gcore/src/ai/mod.rs:260-262]
  - Signature: `fn jitter() -> Duration {`
  - Purpose: Returns a 'Duration' of 0 to 49 milliseconds by generating a random 'u8', taking it modulo 50, and converting the result to milliseconds. [crates/gcore/src/ai/mod.rs:260-262]
- `parse_json_response` (function) component `parse_json_response [function]` (`a3239c25-8ddc-538e-baa3-ece77b66908c`) lines 264-297 [crates/gcore/src/ai/mod.rs:264-297]
  - Signature: `fn parse_json_response(response: Response) -> Result<serde_json::Value, AiError> {`
  - Purpose: Parses an HTTP 'Response' into 'serde_json::Value', mapping '429' to 'AiError::RateLimited' with optional 'Retry-After', '5xx' or '408' to a transport failure, other non-success statuses to 'AiError::HttpStatus', and successful but invalid JSON to 'AiError::parse_failure'. [crates/gcore/src/ai/mod.rs:264-297]
- `parse_retry_after` (function) component `parse_retry_after [function]` (`0fa3fced-36c4-59d0-b42d-7123046d90d7`) lines 299-310 [crates/gcore/src/ai/mod.rs:299-310]
  - Signature: `fn parse_retry_after(value: &str) -> Option<Duration> {`
  - Purpose: Parses a 'Retry-After' header value as either a trimmed integer delay in seconds or an HTTP date, returning the nonnegative duration until that date, both capped at 'MAX_BACKOFF', or 'None' if parsing fails. [crates/gcore/src/ai/mod.rs:299-310]
- `reqwest_error` (function) component `reqwest_error [function]` (`c1ba8fce-c141-5eec-abad-7f6c7b720f3d`) lines 312-318 [crates/gcore/src/ai/mod.rs:312-318]
  - Signature: `fn reqwest_error(error: reqwest::Error) -> AiError {`
  - Purpose: Converts a 'reqwest::Error' into an 'AiError::transport_failure', preserving the optional HTTP status code as 'u16', leaving the secondary context 'None', and using the error's string representation as the failure message. [crates/gcore/src/ai/mod.rs:312-318]
- `duration_to_ms` (function) component `duration_to_ms [function]` (`72821b0b-9b72-5d9e-a06c-956a8bfae21d`) lines 320-322 [crates/gcore/src/ai/mod.rs:320-322]
  - Signature: `fn duration_to_ms(duration: Duration) -> u64 {`
  - Purpose: Converts a 'Duration' to milliseconds and clamps the result to 'u64::MAX' before casting to 'u64'. [crates/gcore/src/ai/mod.rs:320-322]
- `chat_completions_url` (function) component `chat_completions_url [function]` (`b08e9691-7526-5f85-a51a-d8034d39322f`) lines 324-342 [crates/gcore/src/ai/mod.rs:324-342]
  - Signature: `fn chat_completions_url(cfg: &AiContext, capability: AiCapability) -> Result<String, AiError> {`
  - Purpose: Returns the configured provider API base for the given capability, validating that 'api_base' is present and non-empty, and appends '/v1/chat/completions' to the normalized chat API root. [crates/gcore/src/ai/mod.rs:324-342]
- `chat_api_root` (function) component `chat_api_root [function]` (`99b40713-77a1-523b-8538-bc4a91de2f8e`) lines 344-347 [crates/gcore/src/ai/mod.rs:344-347]
  - Signature: `fn chat_api_root(api_base: &str) -> &str {`
  - Purpose: Returns the API base URL with any trailing slash removed and a final '/v1' suffix stripped if present. [crates/gcore/src/ai/mod.rs:344-347]
- `chat_completion_content` (function) component `chat_completion_content [function]` (`a58e079f-24c0-5e54-8ab1-4b06408a953d`) lines 349-359 [crates/gcore/src/ai/mod.rs:349-359]
  - Signature: `fn chat_completion_content(value: &serde_json::Value) -> Result<String, AiError> {`
  - Purpose: Extracts and clones the first choice’s 'message.content' string from a chat-completion JSON response, returning 'AiError::parse_failure("chat completion response missing message content")' if any expected field is absent or not a string. [crates/gcore/src/ai/mod.rs:349-359]
- `chat_completion_model` (function) component `chat_completion_model [function]` (`ce22a089-c955-53d2-b87b-77c57900350c`) lines 361-367 [crates/gcore/src/ai/mod.rs:361-367]
  - Signature: `fn chat_completion_model(value: &serde_json::Value) -> Option<String> {`
  - Purpose: Returns the non-empty '"model"' string from a 'serde_json::Value' as an owned 'String', or 'None' if the field is missing, not a string, or empty. [crates/gcore/src/ai/mod.rs:361-367]
- `retry_caps_at_two` (function) component `retry_caps_at_two [function]` (`143aa9a9-113a-58d6-8646-298ca7675e6d`) lines 376-392 [crates/gcore/src/ai/mod.rs:376-392]
  - Signature: `fn retry_caps_at_two() {`
  - Purpose: Verifies that 'retry_with_backoff' makes exactly three attempts total (the initial call plus two retries) on a persistent 'AiError::TransportFailure' and then returns the final transport failure error. [crates/gcore/src/ai/mod.rs:376-392]
- `retry_honors_retry_after_before_exponential_backoff` (function) component `retry_honors_retry_after_before_exponential_backoff [function]` (`1c37eb23-5d40-580d-ad00-0bc37f768176`) lines 395-417 [crates/gcore/src/ai/mod.rs:395-417]
  - Signature: `fn retry_honors_retry_after_before_exponential_backoff() {`
  - Purpose: Verifies that 'retry_with_backoff' uses the server-provided 'Retry-After' delay of 750 ms on the first rate-limited failure, retries exactly once, and succeeds without falling back to exponential backoff. [crates/gcore/src/ai/mod.rs:395-417]
- `parse_retry_after_accepts_http_dates_and_clamps` (function) component `parse_retry_after_accepts_http_dates_and_clamps [function]` (`c42531d7-b6b0-5b1a-8489-bba7f9608c68`) lines 420-433 [crates/gcore/src/ai/mod.rs:420-433]
  - Signature: `fn parse_retry_after_accepts_http_dates_and_clamps() {`
  - Purpose: Verifies that 'parse_retry_after' parses HTTP-date retry values, clamps future dates to 'MAX_BACKOFF', clamps past dates to 'Duration::ZERO', and also caps numeric seconds above the maximum backoff. [crates/gcore/src/ai/mod.rs:420-433]
- `embeddings_use_shorter_timeout_than_generation` (function) component `embeddings_use_shorter_timeout_than_generation [function]` (`eb4791f6-4ac7-5942-9f69-327dde783e18`) lines 436-440 [crates/gcore/src/ai/mod.rs:436-440]
  - Signature: `fn embeddings_use_shorter_timeout_than_generation() {`
  - Purpose: Verifies that 'AiCapability::Embed' uses 'EMBEDDINGS_TIMEOUT' and that this embedding timeout is strictly shorter than the timeouts for 'AiCapability::TextGenerate' and 'AiCapability::VisionExtract'. [crates/gcore/src/ai/mod.rs:436-440]
- `text_generation_outlasts_vision_for_local_reasoning_models` (function) component `text_generation_outlasts_vision_for_local_reasoning_models [function]` (`b1b17622-92e4-58d1-b212-b6035106f379`) lines 443-450 [crates/gcore/src/ai/mod.rs:443-450]
  - Signature: `fn text_generation_outlasts_vision_for_local_reasoning_models() {`
  - Purpose: Verifies that 'timeout_for(AiCapability::TextGenerate)' equals 'TEXT_GENERATE_TIMEOUT', 'timeout_for(AiCapability::VisionExtract)' equals 'VISION_TIMEOUT', and that the vision timeout is strictly shorter than the text-generation timeout. [crates/gcore/src/ai/mod.rs:443-450]
- `chat_api_root_trims_trailing_v1_segment` (function) component `chat_api_root_trims_trailing_v1_segment [function]` (`ab19bf8e-6883-5513-9091-b66a14a42988`) lines 453-466 [crates/gcore/src/ai/mod.rs:453-466]
  - Signature: `fn chat_api_root_trims_trailing_v1_segment() {`
  - Purpose: Verifies that 'chat_api_root' strips a trailing '/v1' or '/v1/' path segment from the input URL while leaving non-'v1' paths, such as '/v10', unchanged. [crates/gcore/src/ai/mod.rs:453-466]
- `effective_route_auto_falls_through_per_capability` (function) component `effective_route_auto_falls_through_per_capability [function]` (`da14e39f-b323-51c7-afff-c507513a5b0c`) lines 469-508 [crates/gcore/src/ai/mod.rs:469-508]
  - Signature: `fn effective_route_auto_falls_through_per_capability() {`
  - Purpose: Verifies that 'effective_route_with_probe' resolves 'AiRouting::Auto' to the correct effective route per capability, falling through to 'Daemon' when no direct binding exists and the probe succeeds, 'Direct' when a direct endpoint is bound, and 'Off' when neither is available. [crates/gcore/src/ai/mod.rs:469-508]
- `effective_route_explicit_routing_modes_are_forced` (function) component `effective_route_explicit_routing_modes_are_forced [function]` (`d0e67e30-a452-5c3a-98b2-37b54b69188e`) lines 511-546 [crates/gcore/src/ai/mod.rs:511-546]
  - Signature: `fn effective_route_explicit_routing_modes_are_forced() {`
  - Purpose: Verifies that 'effective_route_with_probe' returns the explicitly configured routing mode for each capability, including forced 'Daemon', 'Direct', and 'Off' values regardless of probe results. [crates/gcore/src/ai/mod.rs:511-546]
- `auto_uses_explicit_direct_config_when_daemon_unavailable` (function) component `auto_uses_explicit_direct_config_when_daemon_unavailable [function]` (`4ac9e6c1-3dd5-5bde-8acc-ae6b49965dac`) lines 549-579 [crates/gcore/src/ai/mod.rs:549-579]
  - Signature: `fn auto_uses_explicit_direct_config_when_daemon_unavailable() {`
  - Purpose: Verifies that when daemon probing fails, a 'TextGenerate' binding configured with 'AiRouting::Auto' but an explicit direct API base resolves to 'AiRouting::Direct' and preserves that direct base URL. [crates/gcore/src/ai/mod.rs:549-579]
- `binding` (function) component `binding [function]` (`546e5000-7aaf-5018-91d1-86626b20c60a`) lines 581-594 [crates/gcore/src/ai/mod.rs:581-594]
  - Signature: `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {`
  - Purpose: Constructs and returns a 'CapabilityBinding' initialized with the provided 'routing', 'api_base' converted to an owned 'String' when present, and all other fields set to 'None'. [crates/gcore/src/ai/mod.rs:581-594]

