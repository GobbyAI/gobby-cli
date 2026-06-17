---
title: crates/gcode/src/vector/code_symbols/embedding.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/embedding.rs
  ranges:
  - 21-23
  - 26-29
  - 32-34
  - 38-40
  - 44-47
  - 50-64
  - 66-72
  - 74-101
  - 103-120
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
  - 336-340
  - 344-346
  - 348-353
  - 357-391
  - 394-416
  - 419-442
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/vector/code_symbols/embedding.rs:21-23](crates/gcode/src/vector/code_symbols/embedding.rs#L21-L23), [crates/gcode/src/vector/code_symbols/embedding.rs:26-29](crates/gcode/src/vector/code_symbols/embedding.rs#L26-L29), [crates/gcode/src/vector/code_symbols/embedding.rs:32-34](crates/gcode/src/vector/code_symbols/embedding.rs#L32-L34), [crates/gcode/src/vector/code_symbols/embedding.rs:38-40](crates/gcode/src/vector/code_symbols/embedding.rs#L38-L40), [crates/gcode/src/vector/code_symbols/embedding.rs:44-47](crates/gcode/src/vector/code_symbols/embedding.rs#L44-L47), [crates/gcode/src/vector/code_symbols/embedding.rs:50-64](crates/gcode/src/vector/code_symbols/embedding.rs#L50-L64), [crates/gcode/src/vector/code_symbols/embedding.rs:66-72](crates/gcode/src/vector/code_symbols/embedding.rs#L66-L72), [crates/gcode/src/vector/code_symbols/embedding.rs:74-101](crates/gcode/src/vector/code_symbols/embedding.rs#L74-L101), [crates/gcode/src/vector/code_symbols/embedding.rs:103-120](crates/gcode/src/vector/code_symbols/embedding.rs#L103-L120), [crates/gcode/src/vector/code_symbols/embedding.rs:123-126](crates/gcode/src/vector/code_symbols/embedding.rs#L123-L126), [crates/gcode/src/vector/code_symbols/embedding.rs:128-140](crates/gcode/src/vector/code_symbols/embedding.rs#L128-L140), [crates/gcode/src/vector/code_symbols/embedding.rs:142-145](crates/gcode/src/vector/code_symbols/embedding.rs#L142-L145), [crates/gcode/src/vector/code_symbols/embedding.rs:147-179](crates/gcode/src/vector/code_symbols/embedding.rs#L147-L179), [crates/gcode/src/vector/code_symbols/embedding.rs:181-203](crates/gcode/src/vector/code_symbols/embedding.rs#L181-L203), [crates/gcode/src/vector/code_symbols/embedding.rs:205-211](crates/gcode/src/vector/code_symbols/embedding.rs#L205-L211), [crates/gcode/src/vector/code_symbols/embedding.rs:213-216](crates/gcode/src/vector/code_symbols/embedding.rs#L213-L216), [crates/gcode/src/vector/code_symbols/embedding.rs:218-224](crates/gcode/src/vector/code_symbols/embedding.rs#L218-L224), [crates/gcode/src/vector/code_symbols/embedding.rs:226-247](crates/gcode/src/vector/code_symbols/embedding.rs#L226-L247), [crates/gcode/src/vector/code_symbols/embedding.rs:249-270](crates/gcode/src/vector/code_symbols/embedding.rs#L249-L270), [crates/gcode/src/vector/code_symbols/embedding.rs:272-287](crates/gcode/src/vector/code_symbols/embedding.rs#L272-L287), [crates/gcode/src/vector/code_symbols/embedding.rs:289-320](crates/gcode/src/vector/code_symbols/embedding.rs#L289-L320), [crates/gcode/src/vector/code_symbols/embedding.rs:331-333](crates/gcode/src/vector/code_symbols/embedding.rs#L331-L333), [crates/gcode/src/vector/code_symbols/embedding.rs:336-340](crates/gcode/src/vector/code_symbols/embedding.rs#L336-L340), [crates/gcode/src/vector/code_symbols/embedding.rs:344-346](crates/gcode/src/vector/code_symbols/embedding.rs#L344-L346), [crates/gcode/src/vector/code_symbols/embedding.rs:348-353](crates/gcode/src/vector/code_symbols/embedding.rs#L348-L353), [crates/gcode/src/vector/code_symbols/embedding.rs:357-391](crates/gcode/src/vector/code_symbols/embedding.rs#L357-L391), [crates/gcode/src/vector/code_symbols/embedding.rs:394-416](crates/gcode/src/vector/code_symbols/embedding.rs#L394-L416), [crates/gcode/src/vector/code_symbols/embedding.rs:419-442](crates/gcode/src/vector/code_symbols/embedding.rs#L419-L442)

</details>

# crates/gcode/src/vector/code_symbols/embedding.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

Provides the embedding layer for vector code symbols. It defines `EmbeddingSource` and `EmbeddingBackend` so embeddings can come either from a direct `EmbeddingConfig` or from a daemon-backed `AiContext`, then wires that source into client creation and text/query embedding calls. The helper functions resolve embedding context and config, build the HTTP client, format symbol text for vectors, compute or probe embedding dimensions, and translate failures into `VectorLifecycleError`; the test-only `TestSource` and related tests verify the shared routing and config resolution paths.
[crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
[crates/gcode/src/vector/code_symbols/embedding.rs:26-29]
[crates/gcode/src/vector/code_symbols/embedding.rs:32-34]
[crates/gcode/src/vector/code_symbols/embedding.rs:38-40]
[crates/gcode/src/vector/code_symbols/embedding.rs:44-47]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `dimension_probe_text` | function | `pub(super) fn dimension_probe_text() -> &'static str {` | `dimension_probe_text [function]` | `3479b8a3-530f-55b0-a148-2d5196e2fead` | 21-23 [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] | Indexed function `dimension_probe_text` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] |
| `EmbeddingSource` | type | `pub enum EmbeddingSource {` | `EmbeddingSource [type]` | `16c7b9d8-2dd0-54ab-9ff8-df68956d3555` | 26-29 [crates/gcode/src/vector/code_symbols/embedding.rs:26-29] | Indexed type `EmbeddingSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:26-29] |
| `EmbeddingSource::from` | method | `fn from(config: EmbeddingConfig) -> Self {` | `EmbeddingSource::from [method]` | `40458da6-e52c-5dd1-bd78-7d075bcdb622` | 32-34 [crates/gcode/src/vector/code_symbols/embedding.rs:32-34] | Indexed method `EmbeddingSource::from` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:32-34] |
| `EmbeddingSource::from` | method | `fn from(context: AiContext) -> Self {` | `EmbeddingSource::from [method]` | `7b3bd09e-f7d6-50fe-a24f-565dc0df0de4` | 38-40 [crates/gcode/src/vector/code_symbols/embedding.rs:38-40] | Indexed method `EmbeddingSource::from` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:38-40] |
| `EmbeddingBackend` | class | `pub struct EmbeddingBackend {` | `EmbeddingBackend [class]` | `f98d857e-5d58-5f52-a11f-10471124b252` | 44-47 [crates/gcode/src/vector/code_symbols/embedding.rs:44-47] | Indexed class `EmbeddingBackend` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:44-47] |
| `EmbeddingBackend::new` | method | `pub fn new(source: EmbeddingSource) -> Result<Self, VectorLifecycleError> {` | `EmbeddingBackend::new [method]` | `1e1583c9-745e-5c42-856e-5e1b261b64fd` | 50-64 [crates/gcode/src/vector/code_symbols/embedding.rs:50-64] | Indexed method `EmbeddingBackend::new` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:50-64] |
| `EmbeddingBackend::embed_text` | method | `pub fn embed_text(&self, text: &str) -> Result<Vec<f32>, VectorLifecycleError> {` | `EmbeddingBackend::embed_text [method]` | `e74362f5-35b4-5fed-a03c-ad2f49f90010` | 66-72 [crates/gcode/src/vector/code_symbols/embedding.rs:66-72] | Indexed method `EmbeddingBackend::embed_text` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:66-72] |
| `EmbeddingBackend::embed_query` | method | `pub fn embed_query(&self, text: &str) -> Result<Vec<f32>, VectorLifecycleError> {` | `EmbeddingBackend::embed_query [method]` | `1f50a91c-c517-5871-bfc4-868d7dd0ab8f` | 74-101 [crates/gcode/src/vector/code_symbols/embedding.rs:74-101] | Indexed method `EmbeddingBackend::embed_query` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:74-101] |
| `EmbeddingBackend::embed_text_batch` | method | `pub fn embed_text_batch(` | `EmbeddingBackend::embed_text_batch [method]` | `619f225c-4d00-5abe-9a44-450310d704eb` | 103-120 [crates/gcode/src/vector/code_symbols/embedding.rs:103-120] | Indexed method `EmbeddingBackend::embed_text_batch` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:103-120] |
| `embedding_source_from_context` | function | `pub fn embedding_source_from_context(ctx: &Context) -> Option<EmbeddingSource> {` | `embedding_source_from_context [function]` | `39317108-df4d-5b14-beaf-e702c0a04cb8` | 123-126 [crates/gcode/src/vector/code_symbols/embedding.rs:123-126] | Indexed function `embedding_source_from_context` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:123-126] |
| `embedding_source_from_resolved_ai_context` | function | `fn embedding_source_from_resolved_ai_context(` | `embedding_source_from_resolved_ai_context [function]` | `701ba072-c2f3-5035-8c2f-eca788ac5617` | 128-140 [crates/gcode/src/vector/code_symbols/embedding.rs:128-140] | Indexed function `embedding_source_from_resolved_ai_context` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:128-140] |
| `ResolvedEmbeddingAiContext` | class | `struct ResolvedEmbeddingAiContext {` | `ResolvedEmbeddingAiContext [class]` | `7d30df26-d4f3-578a-92f0-ef350b47fe53` | 142-145 [crates/gcode/src/vector/code_symbols/embedding.rs:142-145] | Indexed class `ResolvedEmbeddingAiContext` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:142-145] |
| `resolve_embedding_ai_context` | function | `fn resolve_embedding_ai_context(ctx: &Context) -> ResolvedEmbeddingAiContext {` | `resolve_embedding_ai_context [function]` | `4823c87d-a6d3-59cf-b6af-37e143e37284` | 147-179 [crates/gcode/src/vector/code_symbols/embedding.rs:147-179] | Indexed function `resolve_embedding_ai_context` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:147-179] |
| `embedding_client` | function | `pub fn embedding_client(` | `embedding_client [function]` | `f036e431-77ef-5476-a9a5-af731616f618` | 181-203 [crates/gcode/src/vector/code_symbols/embedding.rs:181-203] | Indexed function `embedding_client` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:181-203] |
| `embed_text` | function | `pub fn embed_text(` | `embed_text [function]` | `bba395d6-6bd8-519f-8e32-6da5f7352b16` | 205-211 [crates/gcode/src/vector/code_symbols/embedding.rs:205-211] | Indexed function `embed_text` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:205-211] |
| `probe_embedding_dim` | function | `pub fn probe_embedding_dim(config: &EmbeddingConfig) -> Result<usize, VectorLifecycleError> {` | `probe_embedding_dim [function]` | `deee3be0-f99f-5e4c-9649-af9fba6c2e1c` | 213-216 [crates/gcode/src/vector/code_symbols/embedding.rs:213-216] | Indexed function `probe_embedding_dim` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:213-216] |
| `embed_text_batch` | function | `pub fn embed_text_batch(` | `embed_text_batch [function]` | `7d21b1a4-6053-545a-a2de-a93d090eaae9` | 218-224 [crates/gcode/src/vector/code_symbols/embedding.rs:218-224] | Indexed function `embed_text_batch` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:218-224] |
| `embedding_error` | function | `fn embedding_error(error: AiError) -> VectorLifecycleError {` | `embedding_error [function]` | `5165ad64-d7c1-597b-886d-e745f3894276` | 226-247 [crates/gcode/src/vector/code_symbols/embedding.rs:226-247] | Indexed function `embedding_error` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:226-247] |
| `embed_query` | function | `pub fn embed_query(config: &EmbeddingConfig, text: &str) -> Option<Vec<f32>> {` | `embed_query [function]` | `5f44552d-f51c-5f1c-9abd-d6cea42e8ac4` | 249-270 [crates/gcode/src/vector/code_symbols/embedding.rs:249-270] | Indexed function `embed_query` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:249-270] |
| `embed_query_with_source` | function | `pub fn embed_query_with_source(source: &EmbeddingSource, text: &str) -> Option<Vec<f32>> {` | `embed_query_with_source [function]` | `4e0145e7-80dd-5d3c-92a2-404922cc9b0b` | 272-287 [crates/gcode/src/vector/code_symbols/embedding.rs:272-287] | Indexed function `embed_query_with_source` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:272-287] |
| `vector_text_for_symbol` | function | `pub fn vector_text_for_symbol(symbol: &Symbol) -> String {` | `vector_text_for_symbol [function]` | `326ce52f-fd0e-5cca-babf-586d8daae36b` | 289-320 [crates/gcode/src/vector/code_symbols/embedding.rs:289-320] | Indexed function `vector_text_for_symbol` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:289-320] |
| `TestSource` | class | `struct TestSource {` | `TestSource [class]` | `d0dd2dbb-06bf-5257-b6e7-7550d8ff539f` | 331-333 [crates/gcode/src/vector/code_symbols/embedding.rs:331-333] | Indexed class `TestSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:331-333] |
| `TestSource::with_values` | method | `fn with_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {` | `TestSource::with_values [method]` | `e7e59da2-9ce4-5552-85a2-1cd4573c46f2` | 336-340 [crates/gcode/src/vector/code_symbols/embedding.rs:336-340] | Indexed method `TestSource::with_values` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:336-340] |
| `TestSource::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `TestSource::config_value [method]` | `77a1beba-ba90-5801-bc38-bc65b593932f` | 344-346 [crates/gcode/src/vector/code_symbols/embedding.rs:344-346] | Indexed method `TestSource::config_value` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:344-346] |
| `TestSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `TestSource::resolve_value [method]` | `3bcab959-8918-5f4b-937b-76e536ef1b3b` | 348-353 [crates/gcode/src/vector/code_symbols/embedding.rs:348-353] | Indexed method `TestSource::resolve_value` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:348-353] |
| `resolves_via_shared_routing` | function | `fn resolves_via_shared_routing() {` | `resolves_via_shared_routing [function]` | `b4217f9f-8828-5ea3-a9a2-e95e0bdd8e6b` | 357-391 [crates/gcode/src/vector/code_symbols/embedding.rs:357-391] | Indexed function `resolves_via_shared_routing` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:357-391] |
| `reads_endpoint_from_shared_binding` | function | `fn reads_endpoint_from_shared_binding() {` | `reads_endpoint_from_shared_binding [function]` | `1a57e3b9-6d82-5299-bdee-469c8d64a6b6` | 394-416 [crates/gcode/src/vector/code_symbols/embedding.rs:394-416] | Indexed function `reads_endpoint_from_shared_binding` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:394-416] |
| `direct_source_uses_resolved_embedding_config` | function | `fn direct_source_uses_resolved_embedding_config() {` | `direct_source_uses_resolved_embedding_config [function]` | `11d61977-239b-50f6-bf35-94bb6e9f1977` | 419-442 [crates/gcode/src/vector/code_symbols/embedding.rs:419-442] | Indexed function `direct_source_uses_resolved_embedding_config` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:419-442] |
