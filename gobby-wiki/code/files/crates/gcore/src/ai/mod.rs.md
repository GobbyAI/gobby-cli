---
title: crates/gcore/src/ai/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/mod.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Overview

`crates/gcore/src/ai/mod.rs` exposes 37 indexed API symbols.

## How it fits

`crates/gcore/src/ai/mod.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `effective_route` | function | Indexed function `effective_route` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:31-35] |
| `effective_route_with_probe` | function | Indexed function `effective_route_with_probe` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:37-48] |
| `daemon_route_or_fallback` | function | Indexed function `daemon_route_or_fallback` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:50-62] |
| `direct_route_or_off` | function | Indexed function `direct_route_or_off` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:64-76] |
| `AiTransport` | class | Indexed class `AiTransport` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:79-82] |
| `new` | function | Indexed function `new` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:85-89] |
| `post_json` | function | Indexed function `post_json` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:91-108] |
| `post_multipart` | function | Indexed function `post_multipart` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:110-135] |
| `parse_transcription` | function | Indexed function `parse_transcription` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:137-142] |
| `parse_vision` | function | Indexed function `parse_vision` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:144-146] |
| `parse_text` | function | Indexed function `parse_text` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:148-150] |
| `build_json_request` | function | Indexed function `build_json_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:152-169] |
| `build_multipart_request` | function | Indexed function `build_multipart_request` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:171-201] |
| `apply_api_key` | function | Indexed function `apply_api_key` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:204-209] |
| `timeout_for` | function | Indexed function `timeout_for` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:211-218] |
| `retry_with_backoff` | function | Indexed function `retry_with_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:220-235] |
| `is_retryable` | function | Indexed function `is_retryable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:237-248] |
| `retry_delay` | function | Indexed function `retry_delay` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:250-258] |
| `jitter` | function | Indexed function `jitter` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:260-262] |
| `parse_json_response` | function | Indexed function `parse_json_response` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:264-297] |
| `parse_retry_after` | function | Indexed function `parse_retry_after` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:299-310] |
| `reqwest_error` | function | Indexed function `reqwest_error` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:312-318] |
| `duration_to_ms` | function | Indexed function `duration_to_ms` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:320-322] |
| `chat_completions_url` | function | Indexed function `chat_completions_url` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:324-342] |
| `chat_api_root` | function | Indexed function `chat_api_root` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:344-347] |
| `chat_completion_content` | function | Indexed function `chat_completion_content` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:349-359] |
| `chat_completion_model` | function | Indexed function `chat_completion_model` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:361-367] |
| `retry_caps_at_two` | function | Indexed function `retry_caps_at_two` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:376-392] |
| `retry_honors_retry_after_before_exponential_backoff` | function | Indexed function `retry_honors_retry_after_before_exponential_backoff` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:395-417] |
| `parse_retry_after_accepts_http_dates_and_clamps` | function | Indexed function `parse_retry_after_accepts_http_dates_and_clamps` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:420-433] |
| `embeddings_use_shorter_timeout_than_generation` | function | Indexed function `embeddings_use_shorter_timeout_than_generation` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:436-440] |
| `text_generation_outlasts_vision_for_local_reasoning_models` | function | Indexed function `text_generation_outlasts_vision_for_local_reasoning_models` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:443-450] |
| `chat_api_root_trims_trailing_v1_segment` | function | Indexed function `chat_api_root_trims_trailing_v1_segment` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:453-466] |
| `effective_route_auto_falls_through_per_capability` | function | Indexed function `effective_route_auto_falls_through_per_capability` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:469-508] |
| `effective_route_explicit_routing_modes_are_forced` | function | Indexed function `effective_route_explicit_routing_modes_are_forced` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:511-546] |
| `auto_uses_explicit_direct_config_when_daemon_unavailable` | function | Indexed function `auto_uses_explicit_direct_config_when_daemon_unavailable` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:549-579] |
| `binding` | function | Indexed function `binding` in `crates/gcore/src/ai/mod.rs`. [crates/gcore/src/ai/mod.rs:581-597] |

