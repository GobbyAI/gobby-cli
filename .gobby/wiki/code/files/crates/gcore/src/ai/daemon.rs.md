---
title: crates/gcore/src/ai/daemon.rs
type: code_file
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
  - 239-246
  - 248-264
  - 266-268
  - 270-272
  - 274-294
  - 296-305
  - 307-332
  - 334-351
  - 353-357
  - 359-361
  - 363-365
  - 367-403
  - 405-424
  - 438-489
  - 492-511
  - 514-531
  - 534-556
  - 559-580
  - 583-606
  - 609-639
  - 642-657
  - 660-695
  - 698-751
  - 753-762
  - 764-767
  - 769-776
  - 778-780
  - 782-784
  - 786-795
  - 797-814
  - 816-829
  - 831-835
  - 837-855
  - 838-854
  - 857-873
  - 858-872
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

`crates/gcore/src/ai/daemon.rs` exposes 46 indexed API symbols.
[crates/gcore/src/ai/daemon.rs:19-24]
[crates/gcore/src/ai/daemon.rs:27-31]
[crates/gcore/src/ai/daemon.rs:34-41]
[crates/gcore/src/ai/daemon.rs:44-96]
[crates/gcore/src/ai/daemon.rs:98-136]

## API Symbols

- `DaemonTranscriptionOptions` (class) component `DaemonTranscriptionOptions [class]` (`fe2b6abe-325a-5b65-987c-5494d8de2245`) lines 19-24 [crates/gcore/src/ai/daemon.rs:19-24]
  - Signature: `pub struct DaemonTranscriptionOptions<'a> {`
  - Purpose: `DaemonTranscriptionOptions` is a configuration struct that specifies an AI capability selection along with optional borrowed string references for source language, target language, and custom prompt parameters for transcription operations. [crates/gcore/src/ai/daemon.rs:19-24]
- `DaemonEmbeddingResult` (class) component `DaemonEmbeddingResult [class]` (`37bfcc0e-6619-5f90-91f9-c3910c81e82d`) lines 27-31 [crates/gcore/src/ai/daemon.rs:27-31]
  - Signature: `pub struct DaemonEmbeddingResult {`
  - Purpose: `DaemonEmbeddingResult` is a struct that encapsulates embedding computation results, containing a collection of floating-point vectors, the identifier of the model that generated them, and the embedding dimension. [crates/gcore/src/ai/daemon.rs:27-31]
- `default` (function) component `default [function]` (`9e9d7634-b2f2-5ee0-8608-cf9c74922d62`) lines 34-41 [crates/gcore/src/ai/daemon.rs:34-41]
  - Signature: `fn default() -> Self {`
  - Purpose: This function implements the `Default` trait to construct a Self instance with `AudioTranscribe` as the capability and all optional fields (`language`, `target_lang`, `prompt`) initialized to `None`. [crates/gcore/src/ai/daemon.rs:34-41]
- `transcribe_via_daemon` (function) component `transcribe_via_daemon [function]` (`e9f2ba09-f1c6-5a87-8884-c48c0e955a54`) lines 44-96 [crates/gcore/src/ai/daemon.rs:44-96]
  - Signature: `pub fn transcribe_via_daemon(`
  - Purpose: Transcribes audio by submitting file data and configuration parameters to a daemon service via authenticated multipart HTTP POST request with exponential backoff retry logic. [crates/gcore/src/ai/daemon.rs:44-96]
- `describe_image_via_daemon` (function) component `describe_image_via_daemon [function]` (`3994d8af-6946-5c94-9d15-b13a669b4205`) lines 98-136 [crates/gcore/src/ai/daemon.rs:98-136]
  - Signature: `pub fn describe_image_via_daemon(`
  - Purpose: Sends image bytes to an AI daemon service via authenticated multipart POST request to perform vision extraction with configurable provider/model bindings, automatic retry with backoff, and rate limiting. [crates/gcore/src/ai/daemon.rs:98-136]
- `generate_via_daemon` (function) component `generate_via_daemon [function]` (`79897c3c-a54c-5605-9155-ac311297092d`) lines 138-144 [crates/gcore/src/ai/daemon.rs:138-144]
  - Signature: `pub fn generate_via_daemon(`
  - Purpose: Generates AI text via a daemon service given an AI context, prompt, and optional system prompt by delegating to `generate_via_daemon_with_max_tokens` with unbounded token limits. [crates/gcore/src/ai/daemon.rs:138-144]
- `generate_via_daemon_with_max_tokens` (function) component `generate_via_daemon_with_max_tokens [function]` (`d6439506-5ad9-5288-83c2-debaf42a28a3`) lines 149-187 [crates/gcore/src/ai/daemon.rs:149-187]
  - Signature: `pub fn generate_via_daemon_with_max_tokens(`
  - Purpose: Executes a text generation request to a daemon service with configurable model binding and max tokens, applying rate limiting and exponential backoff retry logic, then returns the parsed TextResult. [crates/gcore/src/ai/daemon.rs:149-187]
- `embed_via_daemon` (function) component `embed_via_daemon [function]` (`1e34ffe6-d101-5f82-b5c5-984af336254c`) lines 189-223 [crates/gcore/src/ai/daemon.rs:189-223]
  - Signature: `pub fn embed_via_daemon(`
  - Purpose: Generates embeddings for input strings by making an authenticated HTTP POST request to a local daemon service with rate limiting and exponential backoff retry logic, parsing and returning the results. [crates/gcore/src/ai/daemon.rs:189-223]
- `audio_capability` (function) component `audio_capability [function]` (`49b51891-f2c1-5926-b509-c693f53b8a61`) lines 225-233 [crates/gcore/src/ai/daemon.rs:225-233]
  - Signature: `fn audio_capability(capability: AiCapability) -> Result<AiCapability, AiError> {`
  - Purpose: Validates that the input `AiCapability` is either `AudioTranscribe` or `AudioTranslate`, returning the capability on success or an `AiError` for unsupported capabilities. [crates/gcore/src/ai/daemon.rs:225-233]
- `daemon_client` (function) component `daemon_client [function]` (`7237a9f5-0474-58d5-8bf0-2c5a05cc84c5`) lines 235-237 [crates/gcore/src/ai/daemon.rs:235-237]
  - Signature: `fn daemon_client() -> Result<Client, AiError> {`
  - Purpose: Constructs a new HTTP Client using the builder pattern, converting any reqwest errors to AiError. [crates/gcore/src/ai/daemon.rs:235-237]
- `daemon_url` (function) component `daemon_url [function]` (`76288d26-6ac2-5efa-aa96-267bf0b370a8`) lines 239-246 [crates/gcore/src/ai/daemon.rs:239-246]
  - Signature: `fn daemon_url(path: &str) -> Result<String, AiError> {`
  - Purpose: Concatenates a provided path to the base daemon URL (read from bootstrap.yaml) after removing trailing slashes, returning the fully-qualified endpoint URL. [crates/gcore/src/ai/daemon.rs:239-246]
- `read_local_cli_token` (function) component `read_local_cli_token [function]` (`2e8672fc-9c21-56b7-8c7d-e17398fda00c`) lines 248-264 [crates/gcore/src/ai/daemon.rs:248-264]
  - Signature: `fn read_local_cli_token() -> Result<String, AiError> {`
  - Purpose: Reads a local CLI token from the gobby home directory, validates it is non-empty after trimming whitespace, and returns it or an `AiError` if the file is missing or empty. [crates/gcore/src/ai/daemon.rs:248-264]
- `gobby_home` (function) component `gobby_home [function]` (`e43a0c36-a77a-5ab1-a03e-9ba813eeffd0`) lines 266-268 [crates/gcore/src/ai/daemon.rs:266-268]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, AiError> {`
  - Purpose: This function wraps the internal `crate::gobby_home()` to return a directory `PathBuf`, converting any error to an `AiError::not_configured` variant. [crates/gcore/src/ai/daemon.rs:266-268]
- `with_local_token` (function) component `with_local_token [function]` (`a128c39c-e06a-5b0e-b5b3-1cbdff58789d`) lines 270-272 [crates/gcore/src/ai/daemon.rs:270-272]
  - Signature: `fn with_local_token(request: RequestBuilder, token: &str) -> RequestBuilder {`
  - Purpose: Adds a local authentication token to a `RequestBuilder` by setting the `LOCAL_TOKEN_HEADER` HTTP header and returns the modified builder for method chaining. [crates/gcore/src/ai/daemon.rs:270-272]
- `multipart_form_with_file` (function) component `multipart_form_with_file [function]` (`1075be87-707c-5178-bd57-2a28d62792b8`) lines 274-294 [crates/gcore/src/ai/daemon.rs:274-294]
  - Signature: `fn multipart_form_with_file(`
  - Purpose: Constructs a multipart form containing a file part from raw bytes, validating the byte length as u64 and the MIME type validity. [crates/gcore/src/ai/daemon.rs:274-294]
- `add_optional_text` (function) component `add_optional_text [function]` (`ee0128da-3cb5-5062-8ae1-42fbddb251a2`) lines 296-305 [crates/gcore/src/ai/daemon.rs:296-305]
  - Signature: `fn add_optional_text(`
  - Purpose: Conditionally appends a text field to a multipart form only if the provided optional string value is non-empty, otherwise returns the form unmodified. [crates/gcore/src/ai/daemon.rs:296-305]
- `text_request_body` (function) component `text_request_body [function]` (`c7682195-e6b0-5b60-8d93-a0d95f733ade`) lines 307-332 [crates/gcore/src/ai/daemon.rs:307-332]
  - Signature: `fn text_request_body(`
  - Purpose: # Summary

Constructs a JSON request object for text generation containing a required prompt and optional system prompt, provider, model, project ID, and max tokens, with a default profile applied when both provider and model are unspecified. [crates/gcore/src/ai/daemon.rs:307-332]
- `embeddings_request_body` (function) component `embeddings_request_body [function]` (`663b2e9b-4244-5dde-9077-b046bff7b9a3`) lines 334-351 [crates/gcore/src/ai/daemon.rs:334-351]
  - Signature: `fn embeddings_request_body(`
  - Purpose: Constructs a JSON object request body containing an input array of strings, a boolean query flag, and optional project_id, provider, and model configuration fields for an embeddings API call. [crates/gcore/src/ai/daemon.rs:334-351]
- `insert_optional` (function) component `insert_optional [function]` (`9f79bb23-320f-59e8-b1a6-eff4aa6975d3`) lines 353-357 [crates/gcore/src/ai/daemon.rs:353-357]
  - Signature: `fn insert_optional(body: &mut Map<String, Value>, name: &str, value: Option<&str>) {`
  - Purpose: Inserts a non-empty optional string value into a `Map<String, Value>` as a JSON string only if the input passes the `non_empty` filter. [crates/gcore/src/ai/daemon.rs:353-357]
- `non_empty` (function) component `non_empty [function]` (`d2a39e0d-8b83-54cc-8ace-34ac7bca077f`) lines 359-361 [crates/gcore/src/ai/daemon.rs:359-361]
  - Signature: `fn non_empty(value: Option<&str>) -> Option<&str> {`
  - Purpose: This function trims whitespace from an optional string reference and returns it only if the resulting string is non-empty, otherwise returns None. [crates/gcore/src/ai/daemon.rs:359-361]
- `parse_daemon_transcription` (function) component `parse_daemon_transcription [function]` (`5e832e72-f128-522e-81c7-2de834bd28f7`) lines 363-365 [crates/gcore/src/ai/daemon.rs:363-365]
  - Signature: `fn parse_daemon_transcription(value: Value) -> Result<TranscriptionResult, AiError> {`
  - Purpose: Deserializes a JSON `Value` into a `TranscriptionResult` via the `from_wire_json` method, returning a `Result` that propagates deserialization errors as `AiError`. [crates/gcore/src/ai/daemon.rs:363-365]
- `parse_daemon_embeddings` (function) component `parse_daemon_embeddings [function]` (`59b84bce-b665-5e2a-8c1a-16d3c4f5c116`) lines 367-403 [crates/gcore/src/ai/daemon.rs:367-403]
  - Signature: `fn parse_daemon_embeddings(`
  - Purpose: Parses a daemon embedding JSON response by extracting and validating the model metadata, embedding dimension, and vector arrays while ensuring the returned embedding count matches the expected length. [crates/gcore/src/ai/daemon.rs:367-403]
- `parse_daemon_embedding` (function) component `parse_daemon_embedding [function]` (`1fe73f28-18c0-5b8a-9efe-f34fc5195ca2`) lines 405-424 [crates/gcore/src/ai/daemon.rs:405-424]
  - Signature: `fn parse_daemon_embedding(value: &Value, dim: usize) -> Result<Vec<f32>, AiError> {`
  - Purpose: Converts a JSON array value into a dimension-validated f32 embedding vector, validating that the value is an array of numeric values with length matching the expected embedding dimension. [crates/gcore/src/ai/daemon.rs:405-424]
- `forwards_provider_model_and_optional_project_id` (function) component `forwards_provider_model_and_optional_project_id [function]` (`06ae781a-755e-5cba-91c7-bc6d7f03b6f9`) lines 438-489 [crates/gcore/src/ai/daemon.rs:438-489]
  - Signature: `fn forwards_provider_model_and_optional_project_id() {`
  - Purpose: This test function verifies that the provider, model, and optional project_id parameters are correctly forwarded in HTTP request bodies to the LLM daemon API endpoint for text generation, with and without a project context. [crates/gcore/src/ai/daemon.rs:438-489]
- `text_generation_defaults_to_feature_low_without_provider_model` (function) component `text_generation_defaults_to_feature_low_without_provider_model [function]` (`25ace869-f350-5741-90d1-780bfbd4ebdb`) lines 492-511 [crates/gcore/src/ai/daemon.rs:492-511]
  - Signature: `fn text_generation_defaults_to_feature_low_without_provider_model() {`
  - Purpose: This unit test verifies that text generation requests without configured provider and model parameters default to the "feature_low" profile and correctly construct the daemon request payload with the specified prompt, system_prompt, and project_id. [crates/gcore/src/ai/daemon.rs:492-511]
- `configured_binding_profile_replaces_feature_low_default` (function) component `configured_binding_profile_replaces_feature_low_default [function]` (`60199882-318a-56a5-b95e-94c939721c74`) lines 514-531 [crates/gcore/src/ai/daemon.rs:514-531]
  - Signature: `fn configured_binding_profile_replaces_feature_low_default() {`
  - Purpose: Tests that a text generation binding configuration with an explicit profile and null provider/model fields produces a daemon request containing only the profile parameter while excluding null fields. [crates/gcore/src/ai/daemon.rs:514-531]
- `per_call_profile_overrides_configured_binding_profile` (function) component `per_call_profile_overrides_configured_binding_profile [function]` (`f0317802-7c2c-501e-a32c-fae0e4ac4319`) lines 534-556 [crates/gcore/src/ai/daemon.rs:534-556]
  - Signature: `fn per_call_profile_overrides_configured_binding_profile() {`
  - Purpose: Verifies that per-call profile parameters override configured binding profiles by asserting that a runtime-provided "feature_mid" profile supersedes the configuration's "feature_high" profile in daemon-based text generation requests. [crates/gcore/src/ai/daemon.rs:534-556]
- `explicit_provider_model_suppresses_profile_override` (function) component `explicit_provider_model_suppresses_profile_override [function]` (`1552c005-f9c6-5d08-8268-e85f725b3228`) lines 559-580 [crates/gcore/src/ai/daemon.rs:559-580]
  - Signature: `fn explicit_provider_model_suppresses_profile_override() {`
  - Purpose: This test verifies that explicit daemon provider and model configurations suppress the profile field from being included in generated requests. [crates/gcore/src/ai/daemon.rs:559-580]
- `embeddings_post_preserves_batch_and_local_token` (function) component `embeddings_post_preserves_batch_and_local_token [function]` (`efbe8daf-cbdb-565d-a7b4-803f757a246d`) lines 583-606 [crates/gcore/src/ai/daemon.rs:583-606]
  - Signature: `fn embeddings_post_preserves_batch_and_local_token() {`
  - Purpose: Tests that `embed_via_daemon` correctly batches identical inputs, authenticates with a local token header, and properly deserializes the embedding daemon's response including model metadata and vector embeddings. [crates/gcore/src/ai/daemon.rs:583-606]
- `embedding_response_validates_count_and_dimension` (function) component `embedding_response_validates_count_and_dimension [function]` (`1f82c016-7c22-5126-b0da-eeaa124c98ce`) lines 609-639 [crates/gcore/src/ai/daemon.rs:609-639]
  - Signature: `fn embedding_response_validates_count_and_dimension() {`
  - Purpose: This test function verifies that `parse_daemon_embeddings` correctly rejects embedding responses with mismatched vector counts (1 returned vs. 2 expected) and dimensions (1 returned vs. 2 expected), raising appropriate validation errors for each case. [crates/gcore/src/ai/daemon.rs:609-639]
- `empty_embedding_batch_parses_daemon_model_and_dim` (function) component `empty_embedding_batch_parses_daemon_model_and_dim [function]` (`c1572ec6-d65c-5f2e-ae7c-fcbaf5e91616`) lines 642-657 [crates/gcore/src/ai/daemon.rs:642-657]
  - Signature: `fn empty_embedding_batch_parses_daemon_model_and_dim() {`
  - Purpose: This unit test verifies that `embed_via_daemon` correctly parses and returns the `model` and `dim` metadata fields from a daemon server response containing an empty embedding batch. [crates/gcore/src/ai/daemon.rs:642-657]
- `sends_local_token_and_multipart` (function) component `sends_local_token_and_multipart [function]` (`77dc010b-5748-5e32-97ac-8498c025bc45`) lines 660-695 [crates/gcore/src/ai/daemon.rs:660-695]
  - Signature: `fn sends_local_token_and_multipart() {`
  - Purpose: Verifies that image and audio daemon API requests authenticate with the local secret token via the `x-gobby-local-token` header and encode file uploads as multipart/form-data. [crates/gcore/src/ai/daemon.rs:660-695]
- `voice_multipart_carries_capability_fields` (function) component `voice_multipart_carries_capability_fields [function]` (`45772243-03b3-5bbe-83f8-489df9b21bf3`) lines 698-751 [crates/gcore/src/ai/daemon.rs:698-751]
  - Signature: `fn voice_multipart_carries_capability_fields() {`
  - Purpose: Verifies that `transcribe_via_daemon` correctly serializes `DaemonTranscriptionOptions`, including the `AiCapability` enum variant, into appropriately-named multipart form fields in the daemon request. [crates/gcore/src/ai/daemon.rs:698-751]
- `spawn_server` (function) component `spawn_server [function]` (`3ee0fb4d-cf88-5f67-8ee6-7afe5c56ce51`) lines 753-762 [crates/gcore/src/ai/daemon.rs:753-762]
  - Signature: `fn spawn_server(response: &'static str) -> (u16, RequestHandle) {`
  - Purpose: Spawns a test server with a static JSON response, extracts the numeric port from the server's base URL, and returns a tuple containing the port and server handle. [crates/gcore/src/ai/daemon.rs:753-762]
- `request_body_json` (function) component `request_body_json [function]` (`e3dfbd16-cdf8-5be4-b660-24d14f42f06f`) lines 764-767 [crates/gcore/src/ai/daemon.rs:764-767]
  - Signature: `fn request_body_json(request: &str) -> serde_json::Value {`
  - Purpose: This function extracts the HTTP message body from a request string by splitting at the CRLF double-line boundary (`\r\n\r\n`) and deserializes it as JSON into a `serde_json::Value`. [crates/gcore/src/ai/daemon.rs:764-767]
- `has_header` (function) component `has_header [function]` (`5f2f41f1-d0cd-59c0-aa0b-93c76d74e556`) lines 769-776 [crates/gcore/src/ai/daemon.rs:769-776]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: This function returns true if the request contains an HTTP header whose name matches the given name (case-insensitive ASCII) and whose trimmed value matches the given value (case-sensitive). [crates/gcore/src/ai/daemon.rs:769-776]
- `multipart_has_field` (function) component `multipart_has_field [function]` (`c30127c5-f3fb-50a8-941b-41db8bc5e751`) lines 778-780 [crates/gcore/src/ai/daemon.rs:778-780]
  - Signature: `fn multipart_has_field(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Checks whether a multipart request body contains a form field with the specified name and value by substring matching the multipart field format `name=\"{name}\"\r\n\r\n{value}`. [crates/gcore/src/ai/daemon.rs:778-780]
- `temp_home` (function) component `temp_home [function]` (`f55ca630-86e7-5f15-9bd9-2bec3a37af6e`) lines 782-784 [crates/gcore/src/ai/daemon.rs:782-784]
  - Signature: `fn temp_home() -> tempfile::TempDir {`
  - Purpose: Creates and returns a temporary directory from the `tempfile` crate, panicking if creation fails. [crates/gcore/src/ai/daemon.rs:782-784]
- `write_daemon_files` (function) component `write_daemon_files [function]` (`1dee5433-2483-5385-b504-76e3e2db6cff`) lines 786-795 [crates/gcore/src/ai/daemon.rs:786-795]
  - Signature: `fn write_daemon_files(home: &Path, port: u16, token: &str) {`
  - Purpose: Creates a `.gobby` configuration directory in the home path and writes daemon bootstrap settings (port and bind host) and a CLI authentication token to files. [crates/gcore/src/ai/daemon.rs:786-795]
- `test_context` (function) component `test_context [function]` (`4a81b62f-3833-566d-81d1-43cf40f800c6`) lines 797-814 [crates/gcore/src/ai/daemon.rs:797-814]
  - Signature: `fn test_context(project_id: Option<&str>) -> AiContext {`
  - Purpose: Constructs and returns an `AiContext` initialized with identical bindings across all five AI service operations, a concurrency limit of one, and an optional project identifier. [crates/gcore/src/ai/daemon.rs:797-814]
- `binding` (function) component `binding [function]` (`a029f3b4-0b70-5089-8806-0d05dfc85f37`) lines 816-829 [crates/gcore/src/ai/daemon.rs:816-829]
  - Signature: `fn binding() -> CapabilityBinding {`
  - Purpose: Returns a `CapabilityBinding` initialized with `AiRouting::Daemon` routing configured to use the "daemon-model" AI model from the "daemon-provider" provider, with all other optional fields set to `None`. [crates/gcore/src/ai/daemon.rs:816-829]
- `EnvGuard` (class) component `EnvGuard [class]` (`fe0cc51a-d67a-5ad6-9585-0b7fbd72902b`) lines 831-835 [crates/gcore/src/ai/daemon.rs:831-835]
  - Signature: `struct EnvGuard {`
  - Purpose: `EnvGuard` is an RAII wrapper that maintains a static mutex lock while encapsulating optional OS string paths for home and gobby_home directories. [crates/gcore/src/ai/daemon.rs:831-835]
- `EnvGuard` (class) component `EnvGuard [class]` (`c7f9c022-d9dc-50e9-9c11-27a0c2d33317`) lines 837-855 [crates/gcore/src/ai/daemon.rs:837-855]
  - Signature: `impl EnvGuard {`
  - Purpose: `EnvGuard` is a lock-guarded RAII wrapper that atomically replaces the HOME and GOBBY_HOME environment variables for the duration of a test and restores their original values when dropped. [crates/gcore/src/ai/daemon.rs:837-855]
- `EnvGuard.set_home` (method) component `EnvGuard.set_home [method]` (`c57a679a-8970-537f-9c79-8ece6cc60f43`) lines 838-854 [crates/gcore/src/ai/daemon.rs:838-854]
  - Signature: `fn set_home(home: &Path) -> Self {`
  - Purpose: Sets the HOME and GOBBY_HOME environment variables under mutex protection and returns an RAII guard that restores the original values upon drop. [crates/gcore/src/ai/daemon.rs:838-854]
- `EnvGuard` (class) component `EnvGuard [class]` (`73378adb-e8da-5688-a669-fe3364b7332d`) lines 857-873 [crates/gcore/src/ai/daemon.rs:857-873]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: `EnvGuard` is a RAII guard that restores the `HOME` and `GOBBY_HOME` environment variables to their original values upon being dropped, with concurrent access serialized by the `TEST_ENV_LOCK` mutex. [crates/gcore/src/ai/daemon.rs:857-873]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`d810ca29-9acb-5157-b0b6-dd1962a9c696`) lines 858-872 [crates/gcore/src/ai/daemon.rs:858-872]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Restores the HOME and GOBBY_HOME environment variables to their previously saved state (or removes them if they were unset) upon EnvGuard destruction. [crates/gcore/src/ai/daemon.rs:858-872]

