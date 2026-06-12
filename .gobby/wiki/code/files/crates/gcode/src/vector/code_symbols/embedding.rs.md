---
title: crates/gcode/src/vector/code_symbols/embedding.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/embedding.rs
  ranges:
  - 21-23
  - 26-29
  - 31-35
  - 37-41
  - 44-47
  - 49-121
  - 123-126
  - 128-140
  - 142-145
  - 147-179
  - 181-203
  - 205-211
  - 213-216
  - 218-224
  - 226-247
  - 249-270
  - 272-287
  - 289-320
  - 331-333
  - 335-341
  - 343-354
  - 357-391
  - 394-416
  - 419-442
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/embedding.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

`crates/gcode/src/vector/code_symbols/embedding.rs` exposes 33 indexed API symbols.
[crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
[crates/gcode/src/vector/code_symbols/embedding.rs:26-29]
[crates/gcode/src/vector/code_symbols/embedding.rs:31-35]
[crates/gcode/src/vector/code_symbols/embedding.rs:32-34]
[crates/gcode/src/vector/code_symbols/embedding.rs:37-41]

## API Symbols

- `dimension_probe_text` (function) component `dimension_probe_text [function]` (`3479b8a3-530f-55b0-a148-2d5196e2fead`) lines 21-23 [crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
  - Signature: `pub(super) fn dimension_probe_text() -> &'static str {`
  - Purpose: This function returns a static string reference to the `DIMENSION_PROBE_TEXT` constant, providing crate-internal access to probe-related text data. [crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
- `EmbeddingSource` (type) component `EmbeddingSource [type]` (`16c7b9d8-2dd0-54ab-9ff8-df68956d3555`) lines 26-29 [crates/gcode/src/vector/code_symbols/embedding.rs:26-29]
  - Signature: `pub enum EmbeddingSource {`
  - Purpose: Indexed type `EmbeddingSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:26-29]
- `EmbeddingSource` (class) component `EmbeddingSource [class]` (`50ac7fe7-1277-5756-ae69-737e85d9f944`) lines 31-35 [crates/gcode/src/vector/code_symbols/embedding.rs:31-35]
  - Signature: `impl From<EmbeddingConfig> for EmbeddingSource {`
  - Purpose: This implementation defines an infallible conversion from `EmbeddingConfig` to `EmbeddingSource` that wraps the configuration in the `Direct` enum variant. [crates/gcode/src/vector/code_symbols/embedding.rs:31-35]
- `EmbeddingSource.from` (method) component `EmbeddingSource.from [method]` (`40458da6-e52c-5dd1-bd78-7d075bcdb622`) lines 32-34 [crates/gcode/src/vector/code_symbols/embedding.rs:32-34]
  - Signature: `fn from(config: EmbeddingConfig) -> Self {`
  - Purpose: This method constructs a `Self` instance by wrapping the provided `EmbeddingConfig` in the `Direct` enum variant. [crates/gcode/src/vector/code_symbols/embedding.rs:32-34]
- `EmbeddingSource` (class) component `EmbeddingSource [class]` (`a6a2b4b0-9074-5263-9ad6-45e7a540bdef`) lines 37-41 [crates/gcode/src/vector/code_symbols/embedding.rs:37-41]
  - Signature: `impl From<AiContext> for EmbeddingSource {`
  - Purpose: This `From` trait implementation converts `AiContext` into `EmbeddingSource` by boxing the context and wrapping it in the `Daemon` variant, enabling implicit type conversion. [crates/gcode/src/vector/code_symbols/embedding.rs:37-41]
- `EmbeddingSource.from` (method) component `EmbeddingSource.from [method]` (`7b3bd09e-f7d6-50fe-a24f-565dc0df0de4`) lines 38-40 [crates/gcode/src/vector/code_symbols/embedding.rs:38-40]
  - Signature: `fn from(context: AiContext) -> Self {`
  - Purpose: Implements the `From` trait to construct a `Self::Daemon` variant by heap-allocating the `AiContext` in a `Box`. [crates/gcode/src/vector/code_symbols/embedding.rs:38-40]
- `EmbeddingBackend` (class) component `EmbeddingBackend [class]` (`f98d857e-5d58-5f52-a11f-10471124b252`) lines 44-47 [crates/gcode/src/vector/code_symbols/embedding.rs:44-47]
  - Signature: `pub struct EmbeddingBackend {`
  - Purpose: `EmbeddingBackend` is a struct that encapsulates an `EmbeddingSource` and an optional `reqwest::blocking::Client` for executing embedding operations. [crates/gcode/src/vector/code_symbols/embedding.rs:44-47]
- `EmbeddingBackend` (class) component `EmbeddingBackend [class]` (`ceda3800-7153-533a-b404-f9e10992ca14`) lines 49-121 [crates/gcode/src/vector/code_symbols/embedding.rs:49-121]
  - Signature: `impl EmbeddingBackend {`
  - Purpose: EmbeddingBackend abstracts text embedding generation across configurable Direct (HTTP) and Daemon backend sources, with optional query prefix injection for queries. [crates/gcode/src/vector/code_symbols/embedding.rs:49-121]
- `EmbeddingBackend.new` (method) component `EmbeddingBackend.new [method]` (`1e1583c9-745e-5c42-856e-5e1b261b64fd`) lines 50-64 [crates/gcode/src/vector/code_symbols/embedding.rs:50-64]
  - Signature: `pub fn new(source: EmbeddingSource) -> Result<Self, VectorLifecycleError> {`
  - Purpose: This constructor instantiates a new instance by conditionally creating an embedding client for `Direct` sources (after validating non-empty `api_base`), or setting `direct_client` to `None` for `Daemon` sources. [crates/gcode/src/vector/code_symbols/embedding.rs:50-64]
- `EmbeddingBackend.embed_text` (method) component `EmbeddingBackend.embed_text [method]` (`e74362f5-35b4-5fed-a03c-ad2f49f90010`) lines 66-72 [crates/gcode/src/vector/code_symbols/embedding.rs:66-72]
  - Signature: `pub fn embed_text(&self, text: &str) -> Result<Vec<f32>, VectorLifecycleError> {`
  - Purpose: This method generates a single embedding vector for the input text by wrapping it in a batch, delegating to `embed_text_batch`, and extracting the result or returning an error if the response is empty. [crates/gcode/src/vector/code_symbols/embedding.rs:66-72]
- `EmbeddingBackend.embed_query` (method) component `EmbeddingBackend.embed_query [method]` (`1f50a91c-c517-5871-bfc4-868d7dd0ab8f`) lines 74-101 [crates/gcode/src/vector/code_symbols/embedding.rs:74-101]
  - Signature: `pub fn embed_query(&self, text: &str) -> Result<Vec<f32>, VectorLifecycleError> {`
  - Purpose: Embeds a text query by routing it through either a direct embedding client with optional prefix prepending or a daemon service, returning a floating-point vector embedding or an error. [crates/gcode/src/vector/code_symbols/embedding.rs:74-101]
- `EmbeddingBackend.embed_text_batch` (method) component `EmbeddingBackend.embed_text_batch [method]` (`619f225c-4d00-5abe-9a44-450310d704eb`) lines 103-120 [crates/gcode/src/vector/code_symbols/embedding.rs:103-120]
  - Signature: `pub fn embed_text_batch(`
  - Purpose: Routes a batch of text strings to either a direct in-process embedding client or a daemon service and returns the corresponding f32 embedding vectors. [crates/gcode/src/vector/code_symbols/embedding.rs:103-120]
- `embedding_source_from_context` (function) component `embedding_source_from_context [function]` (`39317108-df4d-5b14-beaf-e702c0a04cb8`) lines 123-126 [crates/gcode/src/vector/code_symbols/embedding.rs:123-126]
  - Signature: `pub fn embedding_source_from_context(ctx: &Context) -> Option<EmbeddingSource> {`
  - Purpose: Resolves an embedding AI context from the provided context and derives an optional `EmbeddingSource` using the resolved context and direct configuration. [crates/gcode/src/vector/code_symbols/embedding.rs:123-126]
- `embedding_source_from_resolved_ai_context` (function) component `embedding_source_from_resolved_ai_context [function]` (`701ba072-c2f3-5035-8c2f-eca788ac5617`) lines 128-140 [crates/gcode/src/vector/code_symbols/embedding.rs:128-140]
  - Signature: `fn embedding_source_from_resolved_ai_context(`
  - Purpose: Resolves an `AiContext` to an `EmbeddingSource` based on the effective embedding routing configuration, returning either a daemon-wrapped context, the direct configuration, or `None` depending on the routing mode. [crates/gcode/src/vector/code_symbols/embedding.rs:128-140]
- `ResolvedEmbeddingAiContext` (class) component `ResolvedEmbeddingAiContext [class]` (`7d30df26-d4f3-578a-92f0-ef350b47fe53`) lines 142-145 [crates/gcode/src/vector/code_symbols/embedding.rs:142-145]
  - Signature: `struct ResolvedEmbeddingAiContext {`
  - Purpose: ResolvedEmbeddingAiContext encapsulates an AiContext with an optional EmbeddingConfig override for resolved embedding operations. [crates/gcode/src/vector/code_symbols/embedding.rs:142-145]
- `resolve_embedding_ai_context` (function) component `resolve_embedding_ai_context [function]` (`4823c87d-a6d3-59cf-b6af-37e143e37284`) lines 147-179 [crates/gcode/src/vector/code_symbols/embedding.rs:147-179]
  - Signature: `fn resolve_embedding_ai_context(ctx: &Context) -> ResolvedEmbeddingAiContext {`
  - Purpose: Resolves embedding AI configuration by attempting to load project-scoped bindings from a PostgreSQL database, falling back to standalone and context-provided sources when database access fails. [crates/gcode/src/vector/code_symbols/embedding.rs:147-179]
- `embedding_client` (function) component `embedding_client [function]` (`f036e431-77ef-5476-a9a5-af731616f618`) lines 181-203 [crates/gcode/src/vector/code_symbols/embedding.rs:181-203]
  - Signature: `pub fn embedding_client(`
  - Purpose: Returns a timeout-keyed cached `reqwest::blocking::Client` from a static map, creating and inserting it if absent. [crates/gcode/src/vector/code_symbols/embedding.rs:181-203]
- `embed_text` (function) component `embed_text [function]` (`bba395d6-6bd8-519f-8e32-6da5f7352b16`) lines 205-211 [crates/gcode/src/vector/code_symbols/embedding.rs:205-211]
  - Signature: `pub fn embed_text(`
  - Purpose: Converts text to a floating-point vector embedding using a blocking HTTP client and configuration, translating embedding errors to `VectorLifecycleError`. [crates/gcode/src/vector/code_symbols/embedding.rs:205-211]
- `probe_embedding_dim` (function) component `probe_embedding_dim [function]` (`deee3be0-f99f-5e4c-9649-af9fba6c2e1c`) lines 213-216 [crates/gcode/src/vector/code_symbols/embedding.rs:213-216]
  - Signature: `pub fn probe_embedding_dim(config: &EmbeddingConfig) -> Result<usize, VectorLifecycleError> {`
  - Purpose: Determines the embedding dimensionality by instantiating an embedding client from the provided configuration, embedding a probe text, and returning the resulting vector's length. [crates/gcode/src/vector/code_symbols/embedding.rs:213-216]
- `embed_text_batch` (function) component `embed_text_batch [function]` (`7d21b1a4-6053-545a-a2de-a93d090eaae9`) lines 218-224 [crates/gcode/src/vector/code_symbols/embedding.rs:218-224]
  - Signature: `pub fn embed_text_batch(`
  - Purpose: Embeds a batch of text strings using a blocking HTTP client, delegating to `gobby_core::ai::embeddings::embed_batch` and converting embedding errors to `VectorLifecycleError`. [crates/gcode/src/vector/code_symbols/embedding.rs:218-224]
- `embedding_error` (function) component `embedding_error [function]` (`5165ad64-d7c1-597b-886d-e745f3894276`) lines 226-247 [crates/gcode/src/vector/code_symbols/embedding.rs:226-247]
  - Signature: `fn embedding_error(error: AiError) -> VectorLifecycleError {`
  - Purpose: Converts an `AiError` to a `VectorLifecycleError`, mapping HTTP-status, rate-limit, and transport errors to `EmbeddingHttp` variants and all other errors to `EmbeddingResponse`. [crates/gcode/src/vector/code_symbols/embedding.rs:226-247]
- `embed_query` (function) component `embed_query [function]` (`5f44552d-f51c-5f1c-9abd-d6cea42e8ac4`) lines 249-270 [crates/gcode/src/vector/code_symbols/embedding.rs:249-270]
  - Signature: `pub fn embed_query(config: &EmbeddingConfig, text: &str) -> Option<Vec<f32>> {`
  - Purpose: Embeds a query string (with an optional configured prefix) using an embedding client, returning the resulting vector embedding or None on client/embedding errors. [crates/gcode/src/vector/code_symbols/embedding.rs:249-270]
- `embed_query_with_source` (function) component `embed_query_with_source [function]` (`4e0145e7-80dd-5d3c-92a2-404922cc9b0b`) lines 272-287 [crates/gcode/src/vector/code_symbols/embedding.rs:272-287]
  - Signature: `pub fn embed_query_with_source(source: &EmbeddingSource, text: &str) -> Option<Vec<f32>> {`
  - Purpose: Embeds a text query into an f32 vector using the specified embedding source, returning None if backend initialization or embedding fails. [crates/gcode/src/vector/code_symbols/embedding.rs:272-287]
- `vector_text_for_symbol` (function) component `vector_text_for_symbol [function]` (`326ce52f-fd0e-5cca-babf-586d8daae36b`) lines 289-320 [crates/gcode/src/vector/code_symbols/embedding.rs:289-320]
  - Signature: `pub fn vector_text_for_symbol(symbol: &Symbol) -> String {`
  - Purpose: Converts a `Symbol` struct into a newline-separated string representation containing its core metadata fields and any non-empty optional fields (signature, docstring, summary). [crates/gcode/src/vector/code_symbols/embedding.rs:289-320]
- `TestSource` (class) component `TestSource [class]` (`d0dd2dbb-06bf-5257-b6e7-7550d8ff539f`) lines 331-333 [crates/gcode/src/vector/code_symbols/embedding.rs:331-333]
  - Signature: `struct TestSource {`
  - Purpose: TestSource is a struct that wraps a HashMap mapping static string references to static string references for test data storage. [crates/gcode/src/vector/code_symbols/embedding.rs:331-333]
- `TestSource` (class) component `TestSource [class]` (`464e0451-985a-5806-84f7-dfa21f2e51f7`) lines 335-341 [crates/gcode/src/vector/code_symbols/embedding.rs:335-341]
  - Signature: `impl TestSource {`
  - Purpose: `TestSource::with_values` is a generic constructor that accepts any type implementing `IntoIterator` over `(&'static str, &'static str)` tuples and collects them into the instance's `values` field. [crates/gcode/src/vector/code_symbols/embedding.rs:335-341]
- `TestSource.with_values` (method) component `TestSource.with_values [method]` (`e7e59da2-9ce4-5552-85a2-1cd4573c46f2`) lines 336-340 [crates/gcode/src/vector/code_symbols/embedding.rs:336-340]
  - Signature: `fn with_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {`
  - Purpose: This method constructs Self by collecting an iterable of static string key-value tuples into its `values` field. [crates/gcode/src/vector/code_symbols/embedding.rs:336-340]
- `TestSource` (class) component `TestSource [class]` (`88f1625e-be18-5e7a-917d-e7f23356d3ae`) lines 343-354 [crates/gcode/src/vector/code_symbols/embedding.rs:343-354]
  - Signature: `impl ConfigSource for TestSource {`
  - Purpose: `TestSource` is a `ConfigSource` implementation that retrieves configuration values from an internal map and resolves the `$secret:EMBEDDING_KEY` placeholder to a test value while passing through other values unchanged. [crates/gcode/src/vector/code_symbols/embedding.rs:343-354]
- `TestSource.config_value` (method) component `TestSource.config_value [method]` (`77a1beba-ba90-5801-bc38-bc65b593932f`) lines 344-346 [crates/gcode/src/vector/code_symbols/embedding.rs:344-346]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Retrieves a configuration value from the values map by key and returns it as an Optional String, converting the dereferenced value via `to_string()`. [crates/gcode/src/vector/code_symbols/embedding.rs:344-346]
- `TestSource.resolve_value` (method) component `TestSource.resolve_value [method]` (`3bcab959-8918-5f4b-937b-76e536ef1b3b`) lines 348-353 [crates/gcode/src/vector/code_symbols/embedding.rs:348-353]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Resolves the `$secret:EMBEDDING_KEY` placeholder to a hardcoded string value, otherwise returns the input unchanged. [crates/gcode/src/vector/code_symbols/embedding.rs:348-353]
- `resolves_via_shared_routing` (function) component `resolves_via_shared_routing [function]` (`b4217f9f-8828-5ea3-a9a2-e95e0bdd8e6b`) lines 357-391 [crates/gcode/src/vector/code_symbols/embedding.rs:357-391]
  - Signature: `fn resolves_via_shared_routing() {`
  - Purpose: Tests that `resolve_embedding_config_from_source` successfully resolves embeddings configuration only when routing mode is "auto" (using the provided API base), while returning None for "daemon" and "off" routing modes. [crates/gcode/src/vector/code_symbols/embedding.rs:357-391]
- `reads_endpoint_from_shared_binding` (function) component `reads_endpoint_from_shared_binding [function]` (`1a57e3b9-6d82-5299-bdee-469c8d64a6b6`) lines 394-416 [crates/gcode/src/vector/code_symbols/embedding.rs:394-416]
  - Signature: `fn reads_endpoint_from_shared_binding() {`
  - Purpose: This test verifies that `resolve_embedding_config_from_source()` correctly resolves embedding configuration from a shared binding source, including API endpoint, model, secret key resolution, query prefix, and timeout parameters. [crates/gcode/src/vector/code_symbols/embedding.rs:394-416]
- `direct_source_uses_resolved_embedding_config` (function) component `direct_source_uses_resolved_embedding_config [function]` (`11d61977-239b-50f6-bf35-94bb6e9f1977`) lines 419-442 [crates/gcode/src/vector/code_symbols/embedding.rs:419-442]
  - Signature: `fn direct_source_uses_resolved_embedding_config() {`
  - Purpose: This test verifies that `embedding_source_from_resolved_ai_context` correctly returns an `EmbeddingSource::Direct` variant containing the expected `EmbeddingConfig` when supplied a resolved `AiContext` with direct embedding routing configuration. [crates/gcode/src/vector/code_symbols/embedding.rs:419-442]

