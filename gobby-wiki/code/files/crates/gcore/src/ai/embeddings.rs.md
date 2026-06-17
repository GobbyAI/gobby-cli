---
title: crates/gcore/src/ai/embeddings.rs
type: code_file
provenance:
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/embeddings.rs:19-38](crates/gcore/src/ai/embeddings.rs#L19-L38), [crates/gcore/src/ai/embeddings.rs:42-92](crates/gcore/src/ai/embeddings.rs#L42-L92), [crates/gcore/src/ai/embeddings.rs:94-105](crates/gcore/src/ai/embeddings.rs#L94-L105), [crates/gcore/src/ai/embeddings.rs:107-133](crates/gcore/src/ai/embeddings.rs#L107-L133), [crates/gcore/src/ai/embeddings.rs:140-148](crates/gcore/src/ai/embeddings.rs#L140-L148), [crates/gcore/src/ai/embeddings.rs:151-166](crates/gcore/src/ai/embeddings.rs#L151-L166), [crates/gcore/src/ai/embeddings.rs:169-190](crates/gcore/src/ai/embeddings.rs#L169-L190), [crates/gcore/src/ai/embeddings.rs:193-197](crates/gcore/src/ai/embeddings.rs#L193-L197), [crates/gcore/src/ai/embeddings.rs:200-217](crates/gcore/src/ai/embeddings.rs#L200-L217), [crates/gcore/src/ai/embeddings.rs:220-242](crates/gcore/src/ai/embeddings.rs#L220-L242), [crates/gcore/src/ai/embeddings.rs:245-258](crates/gcore/src/ai/embeddings.rs#L245-L258), [crates/gcore/src/ai/embeddings.rs:261-273](crates/gcore/src/ai/embeddings.rs#L261-L273)

</details>

# crates/gcore/src/ai/embeddings.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file implements a blocking OpenAI-compatible embeddings client for direct routes. It provides `embed_one` and `embed_batch` to send single-text or batched embedding requests with the configured model, bearer auth, and per-request timeout, then uses shared helpers to send the HTTP request, parse `data[*].embedding`, and enforce response validity. The batch path also reorders results by returned `index`, handles empty inputs without making a request, and rejects malformed responses such as missing data, mismatched counts, duplicate indices, non-success statuses, or non-numeric embedding values.
[crates/gcore/src/ai/embeddings.rs:19-38]
[crates/gcore/src/ai/embeddings.rs:42-92]
[crates/gcore/src/ai/embeddings.rs:94-105]
[crates/gcore/src/ai/embeddings.rs:107-133]
[crates/gcore/src/ai/embeddings.rs:140-148]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `embed_one` | function | `pub fn embed_one(` | `embed_one [function]` | `d0d7979c-9bb2-539d-a1d3-3ad97583ebbe` | 19-38 [crates/gcore/src/ai/embeddings.rs:19-38] | Indexed function `embed_one` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:19-38] |
| `embed_batch` | function | `pub fn embed_batch(` | `embed_batch [function]` | `f7e5c845-5e5c-59a6-820d-36a4bfd3a762` | 42-92 [crates/gcore/src/ai/embeddings.rs:42-92] | Indexed function `embed_batch` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:42-92] |
| `send_request` | function | `fn send_request(client: &Client, config: &EmbeddingConfig, body: Value) -> Result<Value, AiError> {` | `send_request [function]` | `f4099757-dc15-5968-bc5d-0c7bb369416e` | 94-105 [crates/gcore/src/ai/embeddings.rs:94-105] | Indexed function `send_request` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:94-105] |
| `parse_embedding` | function | `fn parse_embedding(item: &Value, index: usize) -> Result<Vec<f32>, AiError> {` | `parse_embedding [function]` | `32bf8302-449f-5124-9a03-b41911acec6d` | 107-133 [crates/gcore/src/ai/embeddings.rs:107-133] | Indexed function `parse_embedding` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:107-133] |
| `config` | function | `fn config(api_base: String, api_key: Option<&str>) -> EmbeddingConfig {` | `config [function]` | `ba5055d0-6975-5a42-8852-37f2289afaf1` | 140-148 [crates/gcore/src/ai/embeddings.rs:140-148] | Indexed function `config` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:140-148] |
| `embed_one_sends_string_input_with_bearer_auth` | function | `fn embed_one_sends_string_input_with_bearer_auth() {` | `embed_one_sends_string_input_with_bearer_auth [function]` | `e925bbea-0fa5-56d0-86c5-1e79377b9acb` | 151-166 [crates/gcore/src/ai/embeddings.rs:151-166] | Indexed function `embed_one_sends_string_input_with_bearer_auth` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:151-166] |
| `embed_batch_sends_array_input_and_reorders_by_index` | function | `fn embed_batch_sends_array_input_and_reorders_by_index() {` | `embed_batch_sends_array_input_and_reorders_by_index [function]` | `7728919a-760a-5f6d-aef9-1115c53a5c71` | 169-190 [crates/gcore/src/ai/embeddings.rs:169-190] | Indexed function `embed_batch_sends_array_input_and_reorders_by_index` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:169-190] |
| `embed_batch_with_no_inputs_skips_the_request` | function | `fn embed_batch_with_no_inputs_skips_the_request() {` | `embed_batch_with_no_inputs_skips_the_request [function]` | `962aace2-4f44-5772-a035-4b7c1ead8018` | 193-197 [crates/gcore/src/ai/embeddings.rs:193-197] | Indexed function `embed_batch_with_no_inputs_skips_the_request` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:193-197] |
| `embed_batch_rejects_vector_count_mismatch` | function | `fn embed_batch_rejects_vector_count_mismatch() {` | `embed_batch_rejects_vector_count_mismatch [function]` | `4844d745-aade-55a0-a2a0-6b5c9b9632ca` | 200-217 [crates/gcore/src/ai/embeddings.rs:200-217] | Indexed function `embed_batch_rejects_vector_count_mismatch` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:200-217] |
| `embed_batch_rejects_duplicate_index` | function | `fn embed_batch_rejects_duplicate_index() {` | `embed_batch_rejects_duplicate_index [function]` | `87ec6256-1a32-5ca8-8f70-fdcb63101747` | 220-242 [crates/gcore/src/ai/embeddings.rs:220-242] | Indexed function `embed_batch_rejects_duplicate_index` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:220-242] |
| `non_success_status_surfaces_status_and_body` | function | `fn non_success_status_surfaces_status_and_body() {` | `non_success_status_surfaces_status_and_body [function]` | `6eee425b-26f1-5709-b431-c9a62443ea63` | 245-258 [crates/gcore/src/ai/embeddings.rs:245-258] | Indexed function `non_success_status_surfaces_status_and_body` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:245-258] |
| `non_numeric_embedding_values_are_rejected` | function | `fn non_numeric_embedding_values_are_rejected() {` | `non_numeric_embedding_values_are_rejected [function]` | `e87f7552-91a0-5a49-916c-d67be76ff322` | 261-273 [crates/gcore/src/ai/embeddings.rs:261-273] | Indexed function `non_numeric_embedding_values_are_rejected` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:261-273] |
