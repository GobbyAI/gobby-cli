---
title: crates/gcore/src/ai
type: code_module
provenance:
- file: crates/gcore/src/ai/daemon.rs
  ranges:
  - 19-24
  - 27-31
  - 34-41
  - 44-96
  - 98-136
  - 138-144
  - 149-187
  - 189-223
  - 225-233
  - 235-237
  - 239-245
  - 247-263
  - 265-267
  - 269-271
  - 273-293
  - 295-304
  - 306-331
  - 333-350
  - 352-356
  - 358-360
  - 362-364
  - 366-402
  - 404-423
  - 437-488
  - 491-510
  - 513-530
  - 533-555
  - 558-579
  - 582-605
  - 608-638
  - 641-656
  - 659-694
  - 697-750
  - 753-770
  - 772-781
  - 783-786
  - 788-795
  - 797-799
  - 801-803
  - 805-814
  - 816-833
  - 835-848
  - 850-856
  - 858-881
  - 883-902
- file: crates/gcore/src/ai/embeddings.rs
  ranges:
  - 19-38
  - 42-92
  - 94-105
  - 107-133
  - 140-148
  - 151-166
  - 169-190
  - 193-197
  - 200-217
  - 220-242
  - 245-258
  - 261-273
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
- file: crates/gcore/src/ai/probe.rs
  ranges:
  - 20-23
  - 26-34
  - 37-42
  - 45-50
  - 53-56
  - 58-64
  - 66-78
  - 80-82
  - 84-89
  - 91-93
  - 95-97
  - 99-110
  - 112-176
  - 178-241
  - 243-251
  - 253-271
  - 274-277
  - 279-281
  - '283'
  - 285-300
  - 309-361
  - 364-377
  - 380-389
  - 392-418
  - 421-444
  - 447-466
  - 469-495
  - 497-500
  - 502-515
  - 517-530
- file: crates/gcore/src/ai/text.rs
  ranges:
  - 9-15
  - 17-35
  - 37-67
  - 69-87
  - 98-120
  - 123-134
  - 136-138
  - 140-143
  - 145-152
  - 154-171
  - 173-186
- file: crates/gcore/src/ai/transcription.rs
  ranges:
  - 11-14
  - 16-37
  - 39-73
  - 75-99
  - 101-142
  - 152-178
  - 181-201
  - 203-205
  - 207-214
  - 216-233
  - 235-248
- file: crates/gcore/src/ai/vision.rs
  ranges:
  - 14-17
  - 19-35
  - 37-63
  - 65-90
  - 92-104
  - 106-121
  - 123-156
  - 158-173
  - 175-179
  - 190-222
  - 225-234
  - 237-246
  - 248-250
  - 252-255
  - 257-264
  - 266-283
  - 285-298
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai

Parent: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

The `crates/gcore/src/ai` module is the AI transport and routing layer for `gcore`. Its root module exposes the daemon, direct embeddings, probing, text, transcription, and vision submodules, while `effective_route` resolves each capability from `AiContext`: explicit `Off`, `Direct`, and `Daemon` bindings are honored, and `Auto` probes daemon availability before falling back to a configured direct route or `Off`  . It also centralizes shared transport concerns such as capability-specific timeouts, retry limits, and backoff constants for generation, vision, embeddings, and speech-to-text paths .

The daemon path adapts local Gobby daemon APIs into typed AI results. `daemon.rs` defines daemon endpoint paths for voice transcription, vision extraction, text generation, and embeddings, reads the local CLI token, builds authenticated multipart or JSON requests, applies the context limiter, retries with backoff, and parses daemon replies into transcription, vision, text, or embedding outputs   . Direct provider flows use the shared `AiTransport`: text generation builds chat-completions payloads with optional system context, model, and max-token limits, then normalizes returned content and usage; vision sends a base64 data URI plus a structured extraction prompt and parses JSON, delimited, or plain text responses; transcription switches between transcribe and translate tasks using a task enum that owns the operation name, capability, and endpoint path   .

Capability probing ties the router and daemon transport together. `probe.rs` maps each `AiCapability` to a daemon status endpoint, probes those routes with a short timeout, and records either availability or structured degradation reasons such as unauthorized, unreachable, not advertised, or invalid status body   . The direct embeddings client fills the non-daemon embedding path by posting OpenAI-compatible `/embeddings` requests for single or batched inputs, preserving response order and rejecting malformed, missing, duplicate, or failed responses before returning `Vec<f32>` vectors [crates/gcore/src/ai/embeddings.rs:19-38] .

## Call Diagram

```mermaid
sequenceDiagram
    participant m_03177fc3_a65a_553d_89df_cae5f70ccc6f as probe_daemon_capability_with &#91;function&#93;
    participant m_09f6bb39_7d40_5fc9_b75c_86642c544ea9 as explicit_provider_model_suppresses_profile_override &#91;function&#93;
    participant m_0c92d3d6_d4b8_5aba_bc76_1828a1193b9c as non_empty &#91;function&#93;
    participant m_0fcc2a50_b69d_5539_a83c_b340710a09d2 as capability_status_route &#91;function&#93;
    participant m_1046d96e_a58d_5957_928b_7fa50a164102 as parse_daemon_embeddings &#91;function&#93;
    participant m_105fdbc7_4236_5718_a78a_9c5d67ff92d1 as empty_embedding_batch_parses_daemon_model_and_dim &#91;function&#93;
    participant m_13e8b8b5_4f2e_53a2_8766_fca00c5d8a3d as status_route_is_availability_truth &#91;function&#93;
    participant m_140a3d79_8513_56bb_801d_abc6d2c3f055 as add_optional_text &#91;function&#93;
    participant m_143aa9a9_113a_58d6_8646_298ca7675e6d as retry_caps_at_two &#91;function&#93;
    participant m_1c37eb23_5d40_580d_ad00_0bc37f768176 as retry_honors_retry_after_before_exponential_backoff &#91;function&#93;
    participant m_2c4f50e8_a084_5f3a_96da_34b5e3586b3c as spawn_server &#91;function&#93;
    participant m_4b57ee25_c217_531b_912e_8d2fec0a4168 as unavailable &#91;function&#93;
    participant m_4dd15874_95ea_5090_a1af_a5a7feee5644 as request_body_json &#91;function&#93;
    participant m_51653529_1ebf_5764_8485_705de7077402 as test_context &#91;function&#93;
    participant m_603a96e1_c01d_512b_9e6c_ddfbfd10c60f as embed_via_daemon &#91;function&#93;
    participant m_639814da_47a4_528f_9763_5d60e7bbfae9 as write_daemon_files &#91;function&#93;
    participant m_94e6bc19_a8a2_5e4c_bd8a_da355a23f463 as retry_with_backoff &#91;function&#93;
    participant m_cc963b53_c2ac_5943_8e93_686cbc5e9e52 as probe_daemon_capabilities_with &#91;function&#93;
    participant m_d05d6301_bbec_50aa_94b7_4887e115e98d as parse_daemon_embedding &#91;function&#93;
    participant m_f475c60b_885a_5c8f_b098_6857aacba69b as temp_home &#91;function&#93;
    participant m_f5b1ae31_d8ba_5980_98a9_a916753b17c8 as status_body_advertises &#91;function&#93;
    participant m_fc924f08_7212_584c_994d_5ec9121f6793 as generate_via_daemon_with_max_tokens &#91;function&#93;
    m_03177fc3_a65a_553d_89df_cae5f70ccc6f->>m_0fcc2a50_b69d_5539_a83c_b340710a09d2: calls
    m_03177fc3_a65a_553d_89df_cae5f70ccc6f->>m_4b57ee25_c217_531b_912e_8d2fec0a4168: calls
    m_03177fc3_a65a_553d_89df_cae5f70ccc6f->>m_f5b1ae31_d8ba_5980_98a9_a916753b17c8: calls
    m_09f6bb39_7d40_5fc9_b75c_86642c544ea9->>m_2c4f50e8_a084_5f3a_96da_34b5e3586b3c: calls
    m_09f6bb39_7d40_5fc9_b75c_86642c544ea9->>m_4dd15874_95ea_5090_a1af_a5a7feee5644: calls
    m_09f6bb39_7d40_5fc9_b75c_86642c544ea9->>m_51653529_1ebf_5764_8485_705de7077402: calls
    m_09f6bb39_7d40_5fc9_b75c_86642c544ea9->>m_639814da_47a4_528f_9763_5d60e7bbfae9: calls
    m_09f6bb39_7d40_5fc9_b75c_86642c544ea9->>m_f475c60b_885a_5c8f_b098_6857aacba69b: calls
    m_09f6bb39_7d40_5fc9_b75c_86642c544ea9->>m_fc924f08_7212_584c_994d_5ec9121f6793: calls
    m_1046d96e_a58d_5957_928b_7fa50a164102->>m_d05d6301_bbec_50aa_94b7_4887e115e98d: calls
    m_105fdbc7_4236_5718_a78a_9c5d67ff92d1->>m_2c4f50e8_a084_5f3a_96da_34b5e3586b3c: calls
    m_105fdbc7_4236_5718_a78a_9c5d67ff92d1->>m_4dd15874_95ea_5090_a1af_a5a7feee5644: calls
    m_105fdbc7_4236_5718_a78a_9c5d67ff92d1->>m_51653529_1ebf_5764_8485_705de7077402: calls
    m_105fdbc7_4236_5718_a78a_9c5d67ff92d1->>m_603a96e1_c01d_512b_9e6c_ddfbfd10c60f: calls
    m_105fdbc7_4236_5718_a78a_9c5d67ff92d1->>m_639814da_47a4_528f_9763_5d60e7bbfae9: calls
    m_105fdbc7_4236_5718_a78a_9c5d67ff92d1->>m_f475c60b_885a_5c8f_b098_6857aacba69b: calls
    m_13e8b8b5_4f2e_53a2_8766_fca00c5d8a3d->>m_cc963b53_c2ac_5943_8e93_686cbc5e9e52: calls
    m_140a3d79_8513_56bb_801d_abc6d2c3f055->>m_0c92d3d6_d4b8_5aba_bc76_1828a1193b9c: calls
    m_143aa9a9_113a_58d6_8646_298ca7675e6d->>m_94e6bc19_a8a2_5e4c_bd8a_da355a23f463: calls
    m_1c37eb23_5d40_580d_ad00_0bc37f768176->>m_94e6bc19_a8a2_5e4c_bd8a_da355a23f463: calls
```

## Files

- [[code/files/crates/gcore/src/ai/daemon.rs|crates/gcore/src/ai/daemon.rs]] - Provides the local-daemon AI transport layer for Gobby: it builds authenticated requests to the daemon’s voice transcription, vision extraction, text generation, and embeddings endpoints, applies limiter/retry/backoff behavior, and parses daemon JSON replies into typed results. The file also contains small helpers for token and URL handling, multipart/JSON request construction, capability validation, and response parsing, plus test-only fixtures and guards that verify the request shapes, defaults, and environment setup.
[crates/gcore/src/ai/daemon.rs:19-24]
[crates/gcore/src/ai/daemon.rs:27-31]
[crates/gcore/src/ai/daemon.rs:34-41]
[crates/gcore/src/ai/daemon.rs:44-96]
[crates/gcore/src/ai/daemon.rs:98-136]
- [[code/files/crates/gcore/src/ai/embeddings.rs|crates/gcore/src/ai/embeddings.rs]] - Blocking OpenAI-compatible embeddings client for direct, non-daemon routes. It builds a fixed `EmbeddingConfig` for the `embed-small` model, sends single-text or batched `/embeddings` requests with optional bearer auth and a per-request timeout, then parses and validates the returned vectors so `embed_one` and `embed_batch` return ordered `Vec<f32>` results or `AiError` parse/http failures when the response is missing, malformed, duplicated, or status-failing.
[crates/gcore/src/ai/embeddings.rs:19-38]
[crates/gcore/src/ai/embeddings.rs:42-92]
[crates/gcore/src/ai/embeddings.rs:94-105]
[crates/gcore/src/ai/embeddings.rs:107-133]
[crates/gcore/src/ai/embeddings.rs:140-148]
- [[code/files/crates/gcore/src/ai/mod.rs|crates/gcore/src/ai/mod.rs]] - This module is the core AI transport/router layer for `gcore`: it wires together the daemon, direct, text, transcription, vision, embeddings, and probe submodules, and centralizes how an `AiContext` is turned into an effective `AiRouting` choice. Its routing helpers prefer explicit `Off`/`Direct`/`Daemon` settings, while `Auto` probes daemon availability first and otherwise falls back to a configured direct endpoint or `Off`.

It also defines `AiTransport` and the request/response plumbing used by AI calls: building JSON and multipart requests, attaching API keys, choosing per-capability timeouts, retrying retryable failures with capped exponential backoff and jitter, parsing JSON and `Retry-After` headers, and extracting chat-completion URL, root, model, and content fields. The test functions at the bottom verify the routing fallback behavior, timeout choices, and retry/header parsing rules.
[crates/gcore/src/ai/mod.rs:31-35]
[crates/gcore/src/ai/mod.rs:37-48]
[crates/gcore/src/ai/mod.rs:50-62]
[crates/gcore/src/ai/mod.rs:64-76]
[crates/gcore/src/ai/mod.rs:79-82]
- [[code/files/crates/gcore/src/ai/probe.rs|crates/gcore/src/ai/probe.rs]] - This file defines the AI capability probing layer for a daemon: it maps each `AiCapability` to a status endpoint, probes those endpoints with a timeouted HTTP transport, and classifies the result into structured availability and degradation reports. `CapabilityAvailability`, `CapabilityDegradation`, and `CapabilityProbeReport` hold the probing outcome, while `CapabilityProbeReport::availability` provides a lookup by capability. The probing flow uses `capability_status_route` to choose the route, `probe_daemon_capability(_at/_with)` to execute a single check, `probe_daemon_capabilities(_at/_with)` to collect all predefined capabilities, and helpers like `status_body_advertises`, `bool_at_path`, and `unavailable` to interpret JSON status bodies and build failure reasons. `UreqProbeTransport` implements the transport interface for real HTTP requests, and `FakeTransport` supports tests that verify route mapping and status-body interpretation.
[crates/gcore/src/ai/probe.rs:20-23]
[crates/gcore/src/ai/probe.rs:26-34]
[crates/gcore/src/ai/probe.rs:37-42]
[crates/gcore/src/ai/probe.rs:45-50]
[crates/gcore/src/ai/probe.rs:53-56]
- [[code/files/crates/gcore/src/ai/text.rs|crates/gcore/src/ai/text.rs]] - This file provides the text-generation path for AI chat completions. `generate_text` is a thin convenience wrapper over `generate_text_with_max_tokens`, which creates an `AiTransport`, resolves the chat-completions URL for the `TextGenerate` capability, builds the JSON payload, sends the authenticated POST request, and assembles a `TextResult` from the returned content, model name, token usage, and empty metadata. The helper `request_body` formats the request messages from optional system context plus the required user prompt, while conditionally adding the binding’s model and a positive `max_tokens` limit. `chat_completion_usage` normalizes usage data from different provider field names into `TokenUsage`. The test helpers and unit tests spin up a stub server, inspect request headers and JSON body, and verify the request/response behavior and `max_tokens` forwarding.
[crates/gcore/src/ai/text.rs:9-15]
[crates/gcore/src/ai/text.rs:17-35]
[crates/gcore/src/ai/text.rs:37-67]
[crates/gcore/src/ai/text.rs:69-87]
[crates/gcore/src/ai/text.rs:98-120]
- [[code/files/crates/gcore/src/ai/transcription.rs|crates/gcore/src/ai/transcription.rs]] - This file implements the audio transcription/translation client for the AI layer. `TranscriptionTask` is the small task enum that centralizes the string name, required `AiCapability`, and REST path for each operation, so the rest of the code can switch between transcribe and translate consistently. `transcribe` orchestrates the call end to end: it builds an `AiTransport`, resolves the endpoint from config, acquires rate-limit permission, retries the request with backoff, and parses the JSON response into a `TranscriptionResult`. The helper functions split the work into URL resolution, multipart request construction, and low-level wiring such as filename, auth, and optional language handling, while the test helpers exercise multipart assembly and header behavior.
[crates/gcore/src/ai/transcription.rs:11-14]
[crates/gcore/src/ai/transcription.rs:16-37]
[crates/gcore/src/ai/transcription.rs:17-22]
[crates/gcore/src/ai/transcription.rs:24-29]
[crates/gcore/src/ai/transcription.rs:31-36]
- [[code/files/crates/gcore/src/ai/vision.rs|crates/gcore/src/ai/vision.rs]] - This file implements AI vision extraction for images: `describe_image` sends an image to the configured vision-capable chat-completions endpoint, and the rest of the module builds the request and normalizes the response into a `VisionResult`. `request_body` base64-encodes the image into a data URI, inserts the vision prompt, and optionally sets the bound model. `parse_content` is the main response handler, first trying structured JSON, then a delimited text fallback, and finally a plain-text fallback, using helpers like `parse_json_content`, `strip_json_fence`, `parse_delimited_content`, `parse_section_label`, and `clean_optional_text` to extract `description` and `ocr_text`. The test helpers and cases at the end verify request construction and parsing edge cases such as empty JSON descriptions and unterminated JSON fences.
[crates/gcore/src/ai/vision.rs:14-17]
[crates/gcore/src/ai/vision.rs:19-35]
[crates/gcore/src/ai/vision.rs:37-63]
[crates/gcore/src/ai/vision.rs:65-90]
[crates/gcore/src/ai/vision.rs:92-104]

## Components

- `fe2b6abe-325a-5b65-987c-5494d8de2245`
- `37bfcc0e-6619-5f90-91f9-c3910c81e82d`
- `9e9d7634-b2f2-5ee0-8608-cf9c74922d62`
- `e9f2ba09-f1c6-5a87-8884-c48c0e955a54`
- `48017a1b-075c-5dbe-9269-323340b49c6d`
- `3575e0cd-f05d-5d20-90d2-8e3d02cc9a40`
- `fc924f08-7212-584c-994d-5ec9121f6793`
- `603a96e1-c01d-512b-9e6c-ddfbfd10c60f`
- `d51d0c9e-6a27-5522-a654-14444ab1c0e4`
- `1ac4b829-b376-5132-971e-b80c34d0b1a3`
- `8d162ca0-183b-5e09-b857-519683114dc3`
- `9097eb66-0a1d-5ddc-ba26-d478094936ea`
- `11e2a651-32d0-5ad9-93ec-3405ccf9ff7b`
- `4071c551-a34b-594d-b9e9-85864097d0ea`
- `e76b63fb-1a4f-5e8b-aaf4-a35137efebde`
- `140a3d79-8513-56bb-801d-abc6d2c3f055`
- `562b2429-576a-52b5-bbe1-885d9457d3e7`
- `5e23fec2-f487-5fd5-b3cd-66bf41d79dcd`
- `d9ac39f5-a35a-5c32-9d43-18a2d6019fe5`
- `0c92d3d6-d4b8-5aba-bc76-1828a1193b9c`
- `05808d65-c919-5b8c-9350-18f7947c00a3`
- `1046d96e-a58d-5957-928b-7fa50a164102`
- `d05d6301-bbec-50aa-94b7-4887e115e98d`
- `3973bc4e-c301-53b9-a1d3-e94ea03e6732`
- `3b0bce9b-06c9-585d-8879-938b9f41c8ca`
- `3ff1eade-8add-5bd6-a401-5550c7d0001d`
- `45e9aa3d-6fa9-5867-94d0-978b1012fd9a`
- `09f6bb39-7d40-5fc9-b75c-86642c544ea9`
- `d803c299-8c52-5095-9b32-ffb9a6d68e03`
- `5f3be6a0-edf9-5794-86b9-b0c7af28ac0f`
- `105fdbc7-4236-5718-a78a-9c5d67ff92d1`
- `6298e2ca-d1a8-5124-89f1-1f8e6e800843`
- `77571a21-d63c-5ae2-90ce-73834889e1b7`
- `842bfa7f-9938-5650-8f08-119c1c05cc4f`
- `2c4f50e8-a084-5f3a-96da-34b5e3586b3c`
- `4dd15874-95ea-5090-a1af-a5a7feee5644`
- `4b4f4ddc-1587-5a42-8a56-671bcb939a7b`
- `2d67bef1-b486-53e0-9cf0-18b28208f637`
- `f475c60b-885a-5c8f-b098-6857aacba69b`
- `639814da-47a4-528f-9763-5d60e7bbfae9`
- `51653529-1ebf-5764-8485-705de7077402`
- `913108dd-e5d5-52de-abcf-11b802236def`
- `c1f000a1-bfe4-5002-b75d-142552507f1c`
- `aa6cfc87-ccd4-5874-b010-b5c4a3839636`
- `65d08b11-ecae-52d9-8f65-b0f7664735fb`
- `3c19b4cf-1b6a-5027-b81d-0a9ff40b575c`
- `59aa653c-0579-5480-a8cc-3c30fed9b3d2`
- `d0d7979c-9bb2-539d-a1d3-3ad97583ebbe`
- `f7e5c845-5e5c-59a6-820d-36a4bfd3a762`
- `f4099757-dc15-5968-bc5d-0c7bb369416e`
- `32bf8302-449f-5124-9a03-b41911acec6d`
- `ba5055d0-6975-5a42-8852-37f2289afaf1`
- `e925bbea-0fa5-56d0-86c5-1e79377b9acb`
- `7728919a-760a-5f6d-aef9-1115c53a5c71`
- `962aace2-4f44-5772-a035-4b7c1ead8018`
- `4844d745-aade-55a0-a2a0-6b5c9b9632ca`
- `87ec6256-1a32-5ca8-8f70-fdcb63101747`
- `6eee425b-26f1-5709-b431-c9a62443ea63`
- `e87f7552-91a0-5a49-916c-d67be76ff322`
- `7f89060f-a6e2-567f-8875-ecc1d63bb8f0`
- `ba15d92b-546d-5fba-84af-962924e83744`
- `d748e96c-668a-5e85-a419-39df03dc7534`
- `5c23eaa1-07fb-5c1a-b22f-d4490145b0b7`
- `180a310a-8d01-53ee-a9ae-ed6f8f7e7f27`
- `f2706583-a628-5ffe-966d-bd49cec75939`
- `e082eff8-11d3-57f6-b9a8-701d46711e66`
- `294ff439-365a-561b-a659-4850992be683`
- `f34172c1-25a5-5f04-9884-382b86cdd0a5`
- `586d5323-0a44-5219-9128-f5131b14fbab`
- `0a3c1953-81c4-5755-a522-8fafb180f32c`
- `89ec5e8e-cd53-5e8a-b9d2-5e35a45f196c`
- `8b11e1be-5b59-539e-a4f6-f0d507fa3768`
- `7b88d6da-e416-571d-acf7-30f2983a0213`
- `288cea22-62db-5cd7-8d81-47a5b927d621`
- `94e6bc19-a8a2-5e4c-bd8a-da355a23f463`
- `0034cc07-303d-5381-9144-11591a1833d4`
- `b973fc1b-5383-5f7b-9b52-cb80df401c30`
- `20c216cb-9f02-5325-9bf3-d1ed06dd6f91`
- `a3239c25-8ddc-538e-baa3-ece77b66908c`
- `0fa3fced-36c4-59d0-b42d-7123046d90d7`
- `c1ba8fce-c141-5eec-abad-7f6c7b720f3d`
- `72821b0b-9b72-5d9e-a06c-956a8bfae21d`
- `b08e9691-7526-5f85-a51a-d8034d39322f`
- `99b40713-77a1-523b-8538-bc4a91de2f8e`
- `a58e079f-24c0-5e54-8ab1-4b06408a953d`
- `ce22a089-c955-53d2-b87b-77c57900350c`
- `143aa9a9-113a-58d6-8646-298ca7675e6d`
- `1c37eb23-5d40-580d-ad00-0bc37f768176`
- `c42531d7-b6b0-5b1a-8489-bba7f9608c68`
- `eb4791f6-4ac7-5942-9f69-327dde783e18`
- `b1b17622-92e4-58d1-b212-b6035106f379`
- `ab19bf8e-6883-5513-9091-b66a14a42988`
- `da14e39f-b323-51c7-afff-c507513a5b0c`
- `d0e67e30-a452-5c3a-98b2-37b54b69188e`
- `4ac9e6c1-3dd5-5bde-8acc-ae6b49965dac`
- `546e5000-7aaf-5018-91d1-86626b20c60a`
- `a6fd6091-6989-5495-bbf4-ee3bbfb68060`
- `26985c38-c0bb-55ac-9844-7f8dfa3af22b`
- `da7befb9-65bc-521f-af9a-28f36d32ff24`
- `22a523c4-daff-5e38-92eb-055ecbbfbfd9`
- `61d12cc3-d985-5a84-aa90-3d38dc8b4ef6`
- `14ae42c2-3f1c-5a18-a330-a7e6af0ee76e`
- `2519e391-063d-5f42-ba3e-64fcd9ac3574`
- `0fcc2a50-b69d-5539-a83c-b340710a09d2`
- `2bc2f797-0568-50c2-98cc-d7612ccd729d`
- `67450992-5bcf-5e64-bd07-1d21ee408767`
- `be1b5939-6f20-500f-b1a7-355d28015624`
- `5212eb3d-e62d-5c65-acde-2be543bfa4aa`
- `cc963b53-c2ac-5943-8e93-686cbc5e9e52`
- `03177fc3-a65a-553d-89df-cae5f70ccc6f`
- `f5b1ae31-d8ba-5980-98a9-a916753b17c8`
- `e651da20-dce3-5f23-8047-6e4f41b1dd2b`
- `4b57ee25-c217-531b-912e-8d2fec0a4168`
- `58f0d3fc-0fc7-50cd-b064-27617a4f5433`
- `219ed1ce-997d-57ba-95e4-c6e4c95a2190`
- `59dbc989-926e-5cd4-847a-ecb79baf5046`
- `2b1eb3a2-0cf5-5e23-ab32-f73ceb2693b4`
- `d0b58e63-6901-5d95-9134-2178335f8a3c`
- `c5eca7e7-9a74-504b-8447-f0c88b2290a4`
- `3cb85e98-2b51-569e-a47d-a6a3871814f7`
- `42a1d57f-97eb-5e5b-b52e-da0a2c5d568a`
- `817339ec-ff78-5493-af0d-ceab2c6faea8`
- `7f899121-46ec-53c4-9e93-48e13f5464a5`
- `a82ce35f-4497-5861-b38e-82e45de66830`
- `13e8b8b5-4f2e-53a2-8766-fca00c5d8a3d`
- `f56b5cb2-c56f-5de2-a35a-83eac89520ea`
- `686ee12e-8441-55d0-96d8-74c4e0d6f57f`
- `4f66b2af-08b9-539e-9c65-0ed291a7e9ac`
- `9354b95d-3554-5531-a95c-560505fe603d`
- `9e6dc112-f5f8-5e7d-b310-e7497215dfc4`
- `8a9f4c08-2405-5339-bdb0-a96c7d0e2ec8`
- `f9a32cf9-4865-5138-a433-c0f172863579`
- `7b004b07-cf59-5266-9ea7-80d74e487ca4`
- `c387c64f-53bb-5033-b20e-064f3d54844e`
- `178cb967-e3e0-51d3-9c54-c26a6c9b6b7e`
- `bd3408f4-9a83-5a88-9272-ec3b99641133`
- `5492543a-95a9-5200-bf21-1bddf5f8a06e`
- `f19aff3c-9f59-5289-8e66-e53454a81e6f`
- `92f24c15-e2d7-500e-91ce-03b2f5dacbc8`
- `2f8cf29c-4c28-556f-bac8-6f97f18f2929`
- `c0da1480-fcf6-59e5-9ed1-064a2011ccb8`
- `f138a8a7-4e65-545b-a963-ce997bf8ffde`
- `2d31804d-32b8-59c4-aad6-972384818f52`
- `ad36e36d-7b45-52a7-9aa4-4e08f2e3344c`
- `fbac3b0b-9e0f-510f-9fe6-4659a3d98cf0`
- `2774e0de-7150-5384-8c38-f6b5754db9dd`
- `681da7cf-e4a4-585f-9d2b-447a0325f4ff`
- `a229a57c-576d-5fb5-b2ef-097bdaa08ad7`
- `13438c66-b78b-5d57-b362-796b20d701d3`
- `9273aba4-408f-5e69-ada2-d90694cb3dda`
- `916ed16f-6c97-580d-927c-1f9c9c38530d`
- `2ad058a8-82bf-5c5c-beac-802c8ecb5b06`
- `e33b4635-422b-5e37-9fec-12eebb60586f`
- `f90102be-9d77-5eaf-a26b-b640da9b3891`
- `7cfc1bed-9dcb-5632-9987-bb6a565ab7b0`
- `ac0ebe19-faba-55c3-b5a0-6ad6eb79c1be`
- `5a39d581-a2c4-5414-b1fe-fa055ed01e26`
- `da280306-74aa-54d8-a56a-bc9f19ff9a9d`
- `8573a93a-a983-5869-8ee6-0e70c43302b7`
- `7670963e-2e4b-52fa-af31-078c4f7320bb`
- `7e24670a-7ed6-5793-a947-7b97283d512e`
- `bb746a09-7b5c-584a-bd28-525ac6a598e4`
- `35c80297-49e7-5e66-9f40-a5cfd322b377`
- `eaf22cda-d802-5c87-8320-da8bf0a3e9bd`
- `187d6eec-5ed7-5079-8f91-59dca52e6761`
- `98af5984-bc13-50fc-8075-266e6169d90a`
- `c5125678-2df4-5bbf-b65a-2e9b46a9de54`
- `68e90422-1644-5453-b932-7a013349ed27`
- `add5d0e2-954d-5f0c-a54c-25917626e112`
- `3ad0205a-e7d7-51da-9e36-c4c467003126`
- `ca792c6f-b010-5711-9d72-fe94dda683f5`
- `98467993-79b7-59ed-aef8-bd1899fc8bad`
- `567bf261-a3d2-5e8d-a35b-38c1f624a7a8`
- `fcf5de2c-4dc1-5a01-871a-1991d0fd599b`

