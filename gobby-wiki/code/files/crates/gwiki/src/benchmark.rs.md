---
title: crates/gwiki/src/benchmark.rs
type: code_file
provenance:
- file: crates/gwiki/src/benchmark.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/benchmark.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/benchmark.rs` exposes 52 indexed API symbols.

## How it fits

`crates/gwiki/src/benchmark.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `BenchmarkReport` | class | Indexed class `BenchmarkReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:30-39] |
| `TokenCompressionReport` | class | Indexed class `TokenCompressionReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:42-48] |
| `GraphCoverageReport` | class | Indexed class `GraphCoverageReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:51-58] |
| `RetrievalPrecisionReport` | class | Indexed class `RetrievalPrecisionReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:61-67] |
| `RetrievalPrecisionExample` | class | Indexed class `RetrievalPrecisionExample` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:70-75] |
| `SourceMixReport` | class | Indexed class `SourceMixReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:78-85] |
| `AvailabilityReport` | class | Indexed class `AvailabilityReport` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:88-91] |
| `OptionalBenchmarkSources` | class | Indexed class `OptionalBenchmarkSources` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:94-99] |
| `BenchmarkRows` | class | Indexed class `BenchmarkRows` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:104-114] |
| `RetrievalPrecisionCandidate` | class | Indexed class `RetrievalPrecisionCandidate` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:117-120] |
| `report_from_postgres` | function | Indexed function `report_from_postgres` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:122-145] |
| `resolve_optional_sources` | function | Indexed function `resolve_optional_sources` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:147-157] |
| `build_report` | function | Indexed function `build_report` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:159-193] |
| `load_benchmark_rows` | function | Indexed function `load_benchmark_rows` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:195-249] |
| `query_scoped_or_global` | function | Indexed function `query_scoped_or_global` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:251-264] |
| `grouped_counts` | function | Indexed function `grouped_counts` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:266-281] |
| `scalar_count` | function | Indexed function `scalar_count` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:283-299] |
| `count_to_u64` | function | Indexed function `count_to_u64` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:301-305] |
| `token_compression` | function | Indexed function `token_compression` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:307-331] |
| `source_mix` | function | Indexed function `source_mix` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:333-342] |
| `graph_coverage` | function | Indexed function `graph_coverage` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:344-377] |
| `retrieval_precision` | function | Indexed function `retrieval_precision` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:379-395] |
| `retrieval_precision_with_backends` | function | Indexed function `retrieval_precision_with_backends` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:397-489] |
| `unavailable_retrieval_precision` | function | Indexed function `unavailable_retrieval_precision` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:491-501] |
| `semantic_degraded_sources` | function | Indexed function `semantic_degraded_sources` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:503-509] |
| `qdrant_source_configured` | function | Indexed function `qdrant_source_configured` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:511-513] |
| `resolve_benchmark_embedding` | function | Indexed function `resolve_benchmark_embedding` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:515-534] |
| `seeded_retrieval_candidates` | function | Indexed function `seeded_retrieval_candidates` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:536-554] |
| `benchmark_query` | function | Indexed function `benchmark_query` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:556-562] |
| `model_provider` | function | Indexed function `model_provider` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:564-570] |
| `model_provider_available` | function | Indexed function `model_provider_available` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:572-584] |
| `query_graph_counts` | function | Indexed function `query_graph_counts` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:586-602] |
| `graph_scope_params` | function | Indexed function `graph_scope_params` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:604-611] |
| `falkor_count` | function | Indexed function `falkor_count` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:613-626] |
| `i64_count_to_u64` | function | Indexed function `i64_count_to_u64` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:628-631] |
| `token_count` | function | Indexed function `token_count` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:633-635] |
| `round_ratio` | function | Indexed function `round_ratio` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:637-639] |
| `non_empty` | function | Indexed function `non_empty` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:641-643] |
| `postgres_error` | function | Indexed function `postgres_error` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:645-649] |
| `FixedEmbedder` | class | Indexed class `FixedEmbedder` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:657] |
| `FixedEmbedder::embed_query` | method | Indexed method `FixedEmbedder::embed_query` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:660-666] |
| `SequenceVectorBackend` | class | Indexed class `SequenceVectorBackend` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:669-671] |
| `SequenceVectorBackend::new` | method | Indexed method `SequenceVectorBackend::new` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:674-678] |
| `SequenceVectorBackend::search` | method | Indexed method `SequenceVectorBackend::search` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:682-701] |
| `rows` | function | Indexed function `rows` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:704-719] |
| `configured_optional_sources` | function | Indexed function `configured_optional_sources` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:721-737] |
| `retrieval_precision_available_path_includes_examples` | function | Indexed function `retrieval_precision_available_path_includes_examples` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:740-771] |
| `benchmark_report_marks_optional_sources_degraded_without_zero_fill` | function | Indexed function `benchmark_report_marks_optional_sources_degraded_without_zero_fill` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:774-818] |
| `benchmark_report_does_not_degrade_configured_backends_without_examples` | function | Indexed function `benchmark_report_does_not_degrade_configured_backends_without_examples` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:821-860] |
| `retrieval_precision_candidate_count_is_configurable` | function | Indexed function `retrieval_precision_candidate_count_is_configurable` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:863-873] |
| `count_to_u64_rejects_negative_counts` | function | Indexed function `count_to_u64_rejects_negative_counts` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:876-881] |
| `falkor_count_rejects_negative_counts` | function | Indexed function `falkor_count_rejects_negative_counts` in `crates/gwiki/src/benchmark.rs`. [crates/gwiki/src/benchmark.rs:884-893] |

