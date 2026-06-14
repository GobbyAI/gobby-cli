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

# crates/gcore/src/ai/embeddings.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

Blocking OpenAI-compatible embeddings client for direct, non-daemon routes. It builds a fixed `EmbeddingConfig` for the `embed-small` model, sends single-text or batched `/embeddings` requests with optional bearer auth and a per-request timeout, then parses and validates the returned vectors so `embed_one` and `embed_batch` return ordered `Vec<f32>` results or `AiError` parse/http failures when the response is missing, malformed, duplicated, or status-failing.
[crates/gcore/src/ai/embeddings.rs:19-38]
[crates/gcore/src/ai/embeddings.rs:42-92]
[crates/gcore/src/ai/embeddings.rs:94-105]
[crates/gcore/src/ai/embeddings.rs:107-133]
[crates/gcore/src/ai/embeddings.rs:140-148]

## API Symbols

- `embed_one` (function) component `embed_one [function]` (`d0d7979c-9bb2-539d-a1d3-3ad97583ebbe`) lines 19-38 [crates/gcore/src/ai/embeddings.rs:19-38]
  - Signature: `pub fn embed_one(`
  - Purpose: Sends an embedding request for `text` using `config.model`, then returns the parsed first vector from `response["data"][0]` or an `AiError` if that entry is missing or malformed. [crates/gcore/src/ai/embeddings.rs:19-38]
- `embed_batch` (function) component `embed_batch [function]` (`f7e5c845-5e5c-59a6-820d-36a4bfd3a762`) lines 42-92 [crates/gcore/src/ai/embeddings.rs:42-92]
  - Signature: `pub fn embed_batch(`
  - Purpose: `embed_batch` sends the batch of input strings to the embedding API with the configured model, then validates that the response contains exactly one embedding per input and reorders/parses them by returned `index` into `Vec<Vec<f32>>`, returning a parse error on any missing, duplicate, or invalid index. [crates/gcore/src/ai/embeddings.rs:42-92]
- `send_request` (function) component `send_request [function]` (`f4099757-dc15-5968-bc5d-0c7bb369416e`) lines 94-105 [crates/gcore/src/ai/embeddings.rs:94-105]
  - Signature: `fn send_request(client: &Client, config: &EmbeddingConfig, body: Value) -> Result<Value, AiError> {`
  - Purpose: Sends a JSON `POST` request to `{api_base}/embeddings` with the configured timeout and optional bearer authentication, then returns the parsed JSON response or a mapped `AiError` if the request fails. [crates/gcore/src/ai/embeddings.rs:94-105]
- `parse_embedding` (function) component `parse_embedding [function]` (`32bf8302-449f-5124-9a03-b41911acec6d`) lines 107-133 [crates/gcore/src/ai/embeddings.rs:107-133]
  - Signature: `fn parse_embedding(item: &Value, index: usize) -> Result<Vec<f32>, AiError> {`
  - Purpose: Parses `item["embedding"]` as a non-empty JSON array of finite numeric values, converts each element to `f32`, and returns an indexed `AiError::parse_failure` if the array is missing, contains a non-number, overflows `f32`, or is empty. [crates/gcore/src/ai/embeddings.rs:107-133]
- `config` (function) component `config [function]` (`ba5055d0-6975-5a42-8852-37f2289afaf1`) lines 140-148 [crates/gcore/src/ai/embeddings.rs:140-148]
  - Signature: `fn config(api_base: String, api_key: Option<&str>) -> EmbeddingConfig {`
  - Purpose: Constructs an `EmbeddingConfig` from the provided `api_base` and optional `api_key`, using the fixed model `"embed-small"`, no `query_prefix`, and a `timeout_seconds` value of `5`. [crates/gcore/src/ai/embeddings.rs:140-148]
- `embed_one_sends_string_input_with_bearer_auth` (function) component `embed_one_sends_string_input_with_bearer_auth [function]` (`e925bbea-0fa5-56d0-86c5-1e79377b9acb`) lines 151-166 [crates/gcore/src/ai/embeddings.rs:151-166]
  - Signature: `fn embed_one_sends_string_input_with_bearer_auth() {`
  - Purpose: This test verifies that `embed_one` posts a string input to `/v1/embeddings` using `Bearer` authentication, sends `model":"embed-small"` and `input":"dimension_probe"` in the JSON body, and correctly parses the returned embedding vector `[0.25, 0.5, 0.75]`. [crates/gcore/src/ai/embeddings.rs:151-166]
- `embed_batch_sends_array_input_and_reorders_by_index` (function) component `embed_batch_sends_array_input_and_reorders_by_index [function]` (`7728919a-760a-5f6d-aef9-1115c53a5c71`) lines 169-190 [crates/gcore/src/ai/embeddings.rs:169-190]
  - Signature: `fn embed_batch_sends_array_input_and_reorders_by_index() {`
  - Purpose: Verifies that `embed_batch` sends a JSON array of inputs to `POST /v1/embeddings` and returns embeddings reordered by the response `index` field so they match the original input order. [crates/gcore/src/ai/embeddings.rs:169-190]
- `embed_batch_with_no_inputs_skips_the_request` (function) component `embed_batch_with_no_inputs_skips_the_request [function]` (`962aace2-4f44-5772-a035-4b7c1ead8018`) lines 193-197 [crates/gcore/src/ai/embeddings.rs:193-197]
  - Signature: `fn embed_batch_with_no_inputs_skips_the_request() {`
  - Purpose: It verifies that `embed_batch` called with an empty input slice returns `Ok([])` against the configured embeddings endpoint, producing no embeddings and no error. [crates/gcore/src/ai/embeddings.rs:193-197]
- `embed_batch_rejects_vector_count_mismatch` (function) component `embed_batch_rejects_vector_count_mismatch [function]` (`4844d745-aade-55a0-a2a0-6b5c9b9632ca`) lines 200-217 [crates/gcore/src/ai/embeddings.rs:200-217]
  - Signature: `fn embed_batch_rejects_vector_count_mismatch() {`
  - Purpose: It asserts that `embed_batch` fails with `AiError::ParseFailure` when the embedding response returns a vector count that does not match the number of requested inputs, here `1 vector(s) for 2 input(s)`. [crates/gcore/src/ai/embeddings.rs:200-217]
- `embed_batch_rejects_duplicate_index` (function) component `embed_batch_rejects_duplicate_index [function]` (`87ec6256-1a32-5ca8-8f70-fdcb63101747`) lines 220-242 [crates/gcore/src/ai/embeddings.rs:220-242]
  - Signature: `fn embed_batch_rejects_duplicate_index() {`
  - Purpose: It verifies that `embed_batch` fails with `AiError::ParseFailure` when the embeddings response contains duplicate `index` values, specifically surfacing an `"invalid index"` parse error. [crates/gcore/src/ai/embeddings.rs:220-242]
- `non_success_status_surfaces_status_and_body` (function) component `non_success_status_surfaces_status_and_body [function]` (`6eee425b-26f1-5709-b431-c9a62443ea63`) lines 245-258 [crates/gcore/src/ai/embeddings.rs:245-258]
  - Signature: `fn non_success_status_surfaces_status_and_body() {`
  - Purpose: This test verifies that `embed_one` surfaces a non-success HTTP response as `AiError::HttpStatus`, preserving the `404` status code and the response body text `"no such model"`. [crates/gcore/src/ai/embeddings.rs:245-258]
- `non_numeric_embedding_values_are_rejected` (function) component `non_numeric_embedding_values_are_rejected [function]` (`e87f7552-91a0-5a49-916c-d67be76ff322`) lines 261-273 [crates/gcore/src/ai/embeddings.rs:261-273]
  - Signature: `fn non_numeric_embedding_values_are_rejected() {`
  - Purpose: This test verifies that `embed_one` rejects a response whose `data[0].embedding` array contains a non-numeric value by returning an `AiError::ParseFailure` with a message indicating the embedding element is not a number. [crates/gcore/src/ai/embeddings.rs:261-273]

