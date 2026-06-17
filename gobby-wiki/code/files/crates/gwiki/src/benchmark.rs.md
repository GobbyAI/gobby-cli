---
title: crates/gwiki/src/benchmark.rs
type: code_file
provenance:
- file: crates/gwiki/src/benchmark.rs
  ranges:
  - 30-39
  - 42-48
  - 51-58
  - 61-67
  - 70-75
  - 78-85
  - 88-91
  - 94-99
  - 104-114
  - 117-120
  - 122-145
  - 147-157
  - 159-193
  - 195-249
  - 251-264
  - 266-281
  - 283-299
  - 301-305
  - 307-331
  - 333-342
  - 344-377
  - 379-395
  - 397-489
  - 491-501
  - 503-509
  - 511-513
  - 515-534
  - 536-554
  - 556-562
  - 564-570
  - 572-584
  - 586-602
  - 604-611
  - 613-626
  - 628-631
  - 633-635
  - 637-639
  - 641-643
  - 645-649
  - '657'
  - 660-666
  - 669-671
  - 674-678
  - 682-701
  - 704-719
  - 721-737
  - 740-771
  - 774-818
  - 821-860
  - 863-873
  - 876-881
  - 884-893
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/benchmark.rs:30-39](crates/gwiki/src/benchmark.rs#L30-L39), [crates/gwiki/src/benchmark.rs:42-48](crates/gwiki/src/benchmark.rs#L42-L48), [crates/gwiki/src/benchmark.rs:51-58](crates/gwiki/src/benchmark.rs#L51-L58), [crates/gwiki/src/benchmark.rs:61-67](crates/gwiki/src/benchmark.rs#L61-L67), [crates/gwiki/src/benchmark.rs:70-75](crates/gwiki/src/benchmark.rs#L70-L75), [crates/gwiki/src/benchmark.rs:78-85](crates/gwiki/src/benchmark.rs#L78-L85), [crates/gwiki/src/benchmark.rs:88-91](crates/gwiki/src/benchmark.rs#L88-L91), [crates/gwiki/src/benchmark.rs:94-99](crates/gwiki/src/benchmark.rs#L94-L99), [crates/gwiki/src/benchmark.rs:104-114](crates/gwiki/src/benchmark.rs#L104-L114), [crates/gwiki/src/benchmark.rs:117-120](crates/gwiki/src/benchmark.rs#L117-L120), [crates/gwiki/src/benchmark.rs:122-145](crates/gwiki/src/benchmark.rs#L122-L145), [crates/gwiki/src/benchmark.rs:147-157](crates/gwiki/src/benchmark.rs#L147-L157), [crates/gwiki/src/benchmark.rs:159-193](crates/gwiki/src/benchmark.rs#L159-L193), [crates/gwiki/src/benchmark.rs:195-249](crates/gwiki/src/benchmark.rs#L195-L249), [crates/gwiki/src/benchmark.rs:251-264](crates/gwiki/src/benchmark.rs#L251-L264), [crates/gwiki/src/benchmark.rs:266-281](crates/gwiki/src/benchmark.rs#L266-L281), [crates/gwiki/src/benchmark.rs:283-299](crates/gwiki/src/benchmark.rs#L283-L299), [crates/gwiki/src/benchmark.rs:301-305](crates/gwiki/src/benchmark.rs#L301-L305), [crates/gwiki/src/benchmark.rs:307-331](crates/gwiki/src/benchmark.rs#L307-L331), [crates/gwiki/src/benchmark.rs:333-342](crates/gwiki/src/benchmark.rs#L333-L342), [crates/gwiki/src/benchmark.rs:344-377](crates/gwiki/src/benchmark.rs#L344-L377), [crates/gwiki/src/benchmark.rs:379-395](crates/gwiki/src/benchmark.rs#L379-L395), [crates/gwiki/src/benchmark.rs:397-489](crates/gwiki/src/benchmark.rs#L397-L489), [crates/gwiki/src/benchmark.rs:491-501](crates/gwiki/src/benchmark.rs#L491-L501), [crates/gwiki/src/benchmark.rs:503-509](crates/gwiki/src/benchmark.rs#L503-L509), [crates/gwiki/src/benchmark.rs:511-513](crates/gwiki/src/benchmark.rs#L511-L513), [crates/gwiki/src/benchmark.rs:515-534](crates/gwiki/src/benchmark.rs#L515-L534), [crates/gwiki/src/benchmark.rs:536-554](crates/gwiki/src/benchmark.rs#L536-L554), [crates/gwiki/src/benchmark.rs:556-562](crates/gwiki/src/benchmark.rs#L556-L562), [crates/gwiki/src/benchmark.rs:564-570](crates/gwiki/src/benchmark.rs#L564-L570), [crates/gwiki/src/benchmark.rs:572-584](crates/gwiki/src/benchmark.rs#L572-L584), [crates/gwiki/src/benchmark.rs:586-602](crates/gwiki/src/benchmark.rs#L586-L602), [crates/gwiki/src/benchmark.rs:604-611](crates/gwiki/src/benchmark.rs#L604-L611), [crates/gwiki/src/benchmark.rs:613-626](crates/gwiki/src/benchmark.rs#L613-L626), [crates/gwiki/src/benchmark.rs:628-631](crates/gwiki/src/benchmark.rs#L628-L631), [crates/gwiki/src/benchmark.rs:633-635](crates/gwiki/src/benchmark.rs#L633-L635), [crates/gwiki/src/benchmark.rs:637-639](crates/gwiki/src/benchmark.rs#L637-L639), [crates/gwiki/src/benchmark.rs:641-643](crates/gwiki/src/benchmark.rs#L641-L643), [crates/gwiki/src/benchmark.rs:645-649](crates/gwiki/src/benchmark.rs#L645-L649), [crates/gwiki/src/benchmark.rs:657](crates/gwiki/src/benchmark.rs#L657), [crates/gwiki/src/benchmark.rs:660-666](crates/gwiki/src/benchmark.rs#L660-L666), [crates/gwiki/src/benchmark.rs:669-671](crates/gwiki/src/benchmark.rs#L669-L671), [crates/gwiki/src/benchmark.rs:674-678](crates/gwiki/src/benchmark.rs#L674-L678), [crates/gwiki/src/benchmark.rs:682-701](crates/gwiki/src/benchmark.rs#L682-L701), [crates/gwiki/src/benchmark.rs:704-719](crates/gwiki/src/benchmark.rs#L704-L719), [crates/gwiki/src/benchmark.rs:721-737](crates/gwiki/src/benchmark.rs#L721-L737), [crates/gwiki/src/benchmark.rs:740-771](crates/gwiki/src/benchmark.rs#L740-L771), [crates/gwiki/src/benchmark.rs:774-818](crates/gwiki/src/benchmark.rs#L774-L818), [crates/gwiki/src/benchmark.rs:821-860](crates/gwiki/src/benchmark.rs#L821-L860), [crates/gwiki/src/benchmark.rs:863-873](crates/gwiki/src/benchmark.rs#L863-L873), [crates/gwiki/src/benchmark.rs:876-881](crates/gwiki/src/benchmark.rs#L876-L881), [crates/gwiki/src/benchmark.rs:884-893](crates/gwiki/src/benchmark.rs#L884-L893)

</details>

# crates/gwiki/src/benchmark.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file assembles benchmark reporting for wiki search and graph systems. It defines the top-level `BenchmarkReport` plus subreports for token compression, graph coverage, retrieval precision, source mix, and model-provider availability, then uses helper routines to load benchmark rows, query PostgreSQL and graph backends, resolve optional sources and embeddings, and compute ratios, counts, and degradation status into a single report.

It also includes test-only support types and backend shims (`FixedEmbedder`, `SequenceVectorBackend`) to make retrieval benchmarks deterministic, along with tests that verify degraded-source handling, configurable candidate counts, and count-validation behavior.
[crates/gwiki/src/benchmark.rs:30-39]
[crates/gwiki/src/benchmark.rs:42-48]
[crates/gwiki/src/benchmark.rs:51-58]
[crates/gwiki/src/benchmark.rs:61-67]
[crates/gwiki/src/benchmark.rs:70-75]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `BenchmarkReport` | class | `pub struct BenchmarkReport {` | `BenchmarkReport [class]` | `dc3ebecc-2146-5e02-8d18-1006f660f755` | 30-39 [crates/gwiki/src/benchmark.rs:30-39] | Indexed class `BenchmarkReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:30-39] |
| `TokenCompressionReport` | class | `pub struct TokenCompressionReport {` | `TokenCompressionReport [class]` | `69f3524f-b33b-53da-beda-f01f202e997b` | 42-48 [crates/gwiki/src/benchmark.rs:42-48] | Indexed class `TokenCompressionReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:42-48] |
| `GraphCoverageReport` | class | `pub struct GraphCoverageReport {` | `GraphCoverageReport [class]` | `a75c5987-536a-5f92-b7cc-0962118c024a` | 51-58 [crates/gwiki/src/benchmark.rs:51-58] | Indexed class `GraphCoverageReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:51-58] |
| `RetrievalPrecisionReport` | class | `pub struct RetrievalPrecisionReport {` | `RetrievalPrecisionReport [class]` | `2e27830e-0112-5219-be8f-12120ff0d21f` | 61-67 [crates/gwiki/src/benchmark.rs:61-67] | Indexed class `RetrievalPrecisionReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:61-67] |
| `RetrievalPrecisionExample` | class | `pub struct RetrievalPrecisionExample {` | `RetrievalPrecisionExample [class]` | `9d87475c-12ea-5858-a02b-c2b43e40229d` | 70-75 [crates/gwiki/src/benchmark.rs:70-75] | Indexed class `RetrievalPrecisionExample` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:70-75] |
| `SourceMixReport` | class | `pub struct SourceMixReport {` | `SourceMixReport [class]` | `aa999454-a443-529c-a468-5b390bd16d36` | 78-85 [crates/gwiki/src/benchmark.rs:78-85] | Indexed class `SourceMixReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:78-85] |
| `AvailabilityReport` | class | `pub struct AvailabilityReport {` | `AvailabilityReport [class]` | `14cda561-b0fa-594b-a066-6c6a4d2c7087` | 88-91 [crates/gwiki/src/benchmark.rs:88-91] | Indexed class `AvailabilityReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:88-91] |
| `OptionalBenchmarkSources` | class | `pub struct OptionalBenchmarkSources {` | `OptionalBenchmarkSources [class]` | `e8a6fbe3-b92d-5cf6-bb30-e35a7575f49f` | 94-99 [crates/gwiki/src/benchmark.rs:94-99] | Indexed class `OptionalBenchmarkSources` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:94-99] |
| `BenchmarkRows` | class | `struct BenchmarkRows {` | `BenchmarkRows [class]` | `bea10379-8027-5c5b-b2af-07c4d65ac9fe` | 104-114 [crates/gwiki/src/benchmark.rs:104-114] | Indexed class `BenchmarkRows` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:104-114] |
| `RetrievalPrecisionCandidate` | class | `struct RetrievalPrecisionCandidate {` | `RetrievalPrecisionCandidate [class]` | `91c4cc32-cfa3-584f-a0ac-594d9fd228c8` | 117-120 [crates/gwiki/src/benchmark.rs:117-120] | Indexed class `RetrievalPrecisionCandidate` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:117-120] |
| `report_from_postgres` | function | `pub fn report_from_postgres(` | `report_from_postgres [function]` | `e1deb6c0-02f5-5275-bb15-0e7e808b1083` | 122-145 [crates/gwiki/src/benchmark.rs:122-145] | Indexed function `report_from_postgres` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:122-145] |
| `resolve_optional_sources` | function | `pub fn resolve_optional_sources(` | `resolve_optional_sources [function]` | `821da7a0-d172-528f-8f11-06f2175d702f` | 147-157 [crates/gwiki/src/benchmark.rs:147-157] | Indexed function `resolve_optional_sources` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:147-157] |
| `build_report` | function | `fn build_report(` | `build_report [function]` | `67485ffa-d2bc-5bda-9e01-d4de2223db6e` | 159-193 [crates/gwiki/src/benchmark.rs:159-193] | Indexed function `build_report` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:159-193] |
| `load_benchmark_rows` | function | `fn load_benchmark_rows(conn: &mut Client, scope: &SearchScope) -> Result<BenchmarkRows, WikiError> {` | `load_benchmark_rows [function]` | `fc7adc22-d8ea-53ed-9951-aee353499e75` | 195-249 [crates/gwiki/src/benchmark.rs:195-249] | Indexed function `load_benchmark_rows` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:195-249] |
| `query_scoped_or_global` | function | `fn query_scoped_or_global(` | `query_scoped_or_global [function]` | `73a4f5ee-fce3-5729-9d36-a7e723ce8e6f` | 251-264 [crates/gwiki/src/benchmark.rs:251-264] | Indexed function `query_scoped_or_global` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:251-264] |
| `grouped_counts` | function | `fn grouped_counts(` | `grouped_counts [function]` | `9df6a6f1-158a-5725-8b54-c9ee780ad126` | 266-281 [crates/gwiki/src/benchmark.rs:266-281] | Indexed function `grouped_counts` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:266-281] |
| `scalar_count` | function | `fn scalar_count(` | `scalar_count [function]` | `af2a9545-b2c0-5a02-9ac8-a945e940a771` | 283-299 [crates/gwiki/src/benchmark.rs:283-299] | Indexed function `scalar_count` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:283-299] |
| `count_to_u64` | function | `fn count_to_u64(count: i64, action: &'static str) -> Result<u64, WikiError> {` | `count_to_u64 [function]` | `670429ea-2066-59b0-a7e9-0d91d65cc056` | 301-305 [crates/gwiki/src/benchmark.rs:301-305] | Indexed function `count_to_u64` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:301-305] |
| `token_compression` | function | `fn token_compression(rows: &BenchmarkRows) -> TokenCompressionReport {` | `token_compression [function]` | `fd4b61e8-3841-5160-afed-aedd7aefc9f4` | 307-331 [crates/gwiki/src/benchmark.rs:307-331] | Indexed function `token_compression` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:307-331] |
| `source_mix` | function | `fn source_mix(rows: &BenchmarkRows) -> SourceMixReport {` | `source_mix [function]` | `cc68181e-1213-5ee6-ba23-df2988a063a5` | 333-342 [crates/gwiki/src/benchmark.rs:333-342] | Indexed function `source_mix` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:333-342] |
| `graph_coverage` | function | `fn graph_coverage(` | `graph_coverage [function]` | `e0db096c-94eb-5675-8e85-e741adc30267` | 344-377 [crates/gwiki/src/benchmark.rs:344-377] | Indexed function `graph_coverage` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:344-377] |
| `retrieval_precision` | function | `fn retrieval_precision(` | `retrieval_precision [function]` | `d24b58ff-daef-501d-a209-d562bbb04ddc` | 379-395 [crates/gwiki/src/benchmark.rs:379-395] | Indexed function `retrieval_precision` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:379-395] |
| `retrieval_precision_with_backends` | function | `fn retrieval_precision_with_backends<E, V>(` | `retrieval_precision_with_backends [function]` | `3a0d94e5-67c1-560a-ac41-486201ee5806` | 397-489 [crates/gwiki/src/benchmark.rs:397-489] | Indexed function `retrieval_precision_with_backends` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:397-489] |
| `unavailable_retrieval_precision` | function | `fn unavailable_retrieval_precision(` | `unavailable_retrieval_precision [function]` | `7a948f5d-68ec-5b3e-be16-dd4f26768d03` | 491-501 [crates/gwiki/src/benchmark.rs:491-501] | Indexed function `unavailable_retrieval_precision` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:491-501] |
| `semantic_degraded_sources` | function | `fn semantic_degraded_sources(degradation: &DegradationKind) -> Vec<String> {` | `semantic_degraded_sources [function]` | `e7c671ba-dd06-5638-b8fa-32e62f2317c0` | 503-509 [crates/gwiki/src/benchmark.rs:503-509] | Indexed function `semantic_degraded_sources` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:503-509] |
| `qdrant_source_configured` | function | `fn qdrant_source_configured(optional: &OptionalBenchmarkSources) -> bool {` | `qdrant_source_configured [function]` | `1c3d1859-1720-543e-845e-7f64963c5119` | 511-513 [crates/gwiki/src/benchmark.rs:511-513] | Indexed function `qdrant_source_configured` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:511-513] |
| `resolve_benchmark_embedding` | function | `fn resolve_benchmark_embedding(` | `resolve_benchmark_embedding [function]` | `019603f0-3413-58b6-ac27-7f12031c6c45` | 515-534 [crates/gwiki/src/benchmark.rs:515-534] | Indexed function `resolve_benchmark_embedding` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:515-534] |
| `seeded_retrieval_candidates` | function | `fn seeded_retrieval_candidates(` | `seeded_retrieval_candidates [function]` | `0e45e0da-1248-553c-bcfd-816d56a7314b` | 536-554 [crates/gwiki/src/benchmark.rs:536-554] | Indexed function `seeded_retrieval_candidates` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:536-554] |
| `benchmark_query` | function | `fn benchmark_query(content: &str) -> String {` | `benchmark_query [function]` | `24eb17c4-fb28-5a47-ac4e-815c8b4f5bf8` | 556-562 [crates/gwiki/src/benchmark.rs:556-562] | Indexed function `benchmark_query` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:556-562] |
| `model_provider` | function | `fn model_provider(optional: &OptionalBenchmarkSources) -> AvailabilityReport {` | `model_provider [function]` | `e3382820-f4ea-515d-a0dd-8894096fd1d5` | 564-570 [crates/gwiki/src/benchmark.rs:564-570] | Indexed function `model_provider` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:564-570] |
| `model_provider_available` | function | `fn model_provider_available(context: &AiContext) -> bool {` | `model_provider_available [function]` | `15bfaf4b-694d-5b7a-a167-d07cc768bc97` | 572-584 [crates/gwiki/src/benchmark.rs:572-584] | Indexed function `model_provider_available` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:572-584] |
| `query_graph_counts` | function | `fn query_graph_counts(config: &FalkorConfig, scope: &SearchScope) -> anyhow::Result<(u64, u64)> {` | `query_graph_counts [function]` | `74cca271-7296-5435-bd4c-174233b539a1` | 586-602 [crates/gwiki/src/benchmark.rs:586-602] | Indexed function `query_graph_counts` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:586-602] |
| `graph_scope_params` | function | `fn graph_scope_params(scope: &SearchScope) -> Option<HashMap<String, String>> {` | `graph_scope_params [function]` | `5768972f-9628-5805-929a-5e4ad2f2c15d` | 604-611 [crates/gwiki/src/benchmark.rs:604-611] | Indexed function `graph_scope_params` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:604-611] |
| `falkor_count` | function | `fn falkor_count(rows: &[HashMap<String, Value>]) -> anyhow::Result<u64> {` | `falkor_count [function]` | `22b76c11-d475-563d-87ac-2a0cd3eca820` | 613-626 [crates/gwiki/src/benchmark.rs:613-626] | Indexed function `falkor_count` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:613-626] |
| `i64_count_to_u64` | function | `fn i64_count_to_u64(count: i64) -> anyhow::Result<u64> {` | `i64_count_to_u64 [function]` | `ccb17156-eaff-59a3-8849-4118c608df30` | 628-631 [crates/gwiki/src/benchmark.rs:628-631] | Indexed function `i64_count_to_u64` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:628-631] |
| `token_count` | function | `fn token_count(text: &str) -> u64 {` | `token_count [function]` | `762e2c25-cdc4-55ae-85db-499ebf33dfd5` | 633-635 [crates/gwiki/src/benchmark.rs:633-635] | Indexed function `token_count` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:633-635] |
| `round_ratio` | function | `fn round_ratio(value: f64) -> f64 {` | `round_ratio [function]` | `56fc1640-f377-5b5a-8970-41ae702a31e1` | 637-639 [crates/gwiki/src/benchmark.rs:637-639] | Indexed function `round_ratio` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:637-639] |
| `non_empty` | function | `fn non_empty(value: &str) -> bool {` | `non_empty [function]` | `18ac5935-db2f-5e5d-8e8a-3fe9c967a5fe` | 641-643 [crates/gwiki/src/benchmark.rs:641-643] | Indexed function `non_empty` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:641-643] |
| `postgres_error` | function | `fn postgres_error(action: &'static str) -> impl FnOnce(postgres::Error) -> WikiError {` | `postgres_error [function]` | `6d67b0e0-611f-5a4f-bd3a-c8d3e7ee1ae5` | 645-649 [crates/gwiki/src/benchmark.rs:645-649] | Indexed function `postgres_error` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:645-649] |
| `FixedEmbedder` | class | `struct FixedEmbedder;` | `FixedEmbedder [class]` | `a6f6a98a-f25d-5ca2-99cc-a1aac34921c8` | 657-657 [crates/gwiki/src/benchmark.rs:657] | Indexed class `FixedEmbedder` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:657] |
| `FixedEmbedder::embed_query` | method | `fn embed_query(` | `FixedEmbedder::embed_query [method]` | `8fefb24b-2d21-58fb-8b15-bce0619eb839` | 660-666 [crates/gwiki/src/benchmark.rs:660-666] | Indexed method `FixedEmbedder::embed_query` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:660-666] |
| `SequenceVectorBackend` | class | `struct SequenceVectorBackend {` | `SequenceVectorBackend [class]` | `9e50876b-6b59-57c5-a37c-cd26f5ac32c5` | 669-671 [crates/gwiki/src/benchmark.rs:669-671] | Indexed class `SequenceVectorBackend` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:669-671] |
| `SequenceVectorBackend::new` | method | `fn new(paths: Vec<&str>) -> Self {` | `SequenceVectorBackend::new [method]` | `5203b03d-8924-5968-9220-4b98e296a8d0` | 674-678 [crates/gwiki/src/benchmark.rs:674-678] | Indexed method `SequenceVectorBackend::new` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:674-678] |
| `SequenceVectorBackend::search` | method | `fn search(` | `SequenceVectorBackend::search [method]` | `728325e2-d73a-583e-84c9-eec9486fb2b6` | 682-701 [crates/gwiki/src/benchmark.rs:682-701] | Indexed method `SequenceVectorBackend::search` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:682-701] |
| `rows` | function | `fn rows() -> BenchmarkRows {` | `rows [function]` | `fea8cada-6972-5bbd-8a09-71095f0b4d5b` | 704-719 [crates/gwiki/src/benchmark.rs:704-719] | Indexed function `rows` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:704-719] |
| `configured_optional_sources` | function | `fn configured_optional_sources() -> OptionalBenchmarkSources {` | `configured_optional_sources [function]` | `b68d0a8b-f52d-5002-ac4e-772025781ade` | 721-737 [crates/gwiki/src/benchmark.rs:721-737] | Indexed function `configured_optional_sources` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:721-737] |
| `retrieval_precision_available_path_includes_examples` | function | `fn retrieval_precision_available_path_includes_examples() {` | `retrieval_precision_available_path_includes_examples [function]` | `bee98aa7-0d07-568e-aae0-d3612b8edf51` | 740-771 [crates/gwiki/src/benchmark.rs:740-771] | Indexed function `retrieval_precision_available_path_includes_examples` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:740-771] |
| `benchmark_report_marks_optional_sources_degraded_without_zero_fill` | function | `fn benchmark_report_marks_optional_sources_degraded_without_zero_fill() {` | `benchmark_report_marks_optional_sources_degraded_without_zero_fill [function]` | `16c5e92e-bb06-5a58-a0f0-5d37df68d97f` | 774-818 [crates/gwiki/src/benchmark.rs:774-818] | Indexed function `benchmark_report_marks_optional_sources_degraded_without_zero_fill` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:774-818] |
| `benchmark_report_does_not_degrade_configured_backends_without_examples` | function | `fn benchmark_report_does_not_degrade_configured_backends_without_examples() {` | `benchmark_report_does_not_degrade_configured_backends_without_examples [function]` | `45a2bbf0-ae36-5291-b19e-6e0a2a7618e4` | 821-860 [crates/gwiki/src/benchmark.rs:821-860] | Indexed function `benchmark_report_does_not_degrade_configured_backends_without_examples` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:821-860] |
| `retrieval_precision_candidate_count_is_configurable` | function | `fn retrieval_precision_candidate_count_is_configurable() {` | `retrieval_precision_candidate_count_is_configurable [function]` | `369190f8-f893-5123-9348-4b40d37eb085` | 863-873 [crates/gwiki/src/benchmark.rs:863-873] | Indexed function `retrieval_precision_candidate_count_is_configurable` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:863-873] |
| `count_to_u64_rejects_negative_counts` | function | `fn count_to_u64_rejects_negative_counts() {` | `count_to_u64_rejects_negative_counts [function]` | `6b989364-950f-55d0-84f0-57be4fe41737` | 876-881 [crates/gwiki/src/benchmark.rs:876-881] | Indexed function `count_to_u64_rejects_negative_counts` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:876-881] |
| `falkor_count_rejects_negative_counts` | function | `fn falkor_count_rejects_negative_counts() {` | `falkor_count_rejects_negative_counts [function]` | `c8b9f82a-1f7e-5268-917e-04e7774a4049` | 884-893 [crates/gwiki/src/benchmark.rs:884-893] | Indexed function `falkor_count_rejects_negative_counts` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:884-893] |
