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

`crates/gwiki/src/benchmark.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `BenchmarkReport` | class | 'BenchmarkReport' is an aggregate benchmark result struct that records the executed command, benchmark scope, token compression, graph coverage, retrieval precision, source mix, model provider availability, and a list of degraded source identifiers. [crates/gwiki/src/benchmark.rs:30-39] |
| `TokenCompressionReport` | class | 'TokenCompressionReport' is a status-and-metrics struct that records whether token compression is available, the original document token count, the compressed chunk token count, an optional compression ratio, and an optional reason when compression is unavailable or not applied. [crates/gwiki/src/benchmark.rs:42-48] |
| `GraphCoverageReport` | class | 'GraphCoverageReport' is a coverage summary for graph availability that records whether graph data is available, counts PostgreSQL documents and links, optionally counts graph documents and links, and optionally explains why graph coverage is unavailable. [crates/gwiki/src/benchmark.rs:51-58] |
| `RetrievalPrecisionReport` | class | 'RetrievalPrecisionReport' is a serializable report struct that indicates whether retrieval precision data is available, stores a list of 'RetrievalPrecisionExample' entries and an optional unavailability reason, and keeps a skipped 'backend_degraded_sources' list for internal use. [crates/gwiki/src/benchmark.rs:61-67] |
| `RetrievalPrecisionExample` | class | 'RetrievalPrecisionExample' is a data record for evaluating retrieval precision at rank 1, storing the search query, the expected path, an optional returned path, and an optional 'precision_at_1' score. [crates/gwiki/src/benchmark.rs:70-75] |
| `SourceMixReport` | class | 'SourceMixReport' is a report struct that captures whether source mixing is available, counts of total documents and sources, per-kind document and source tallies, and an optional unavailability reason. [crates/gwiki/src/benchmark.rs:78-85] |
| `AvailabilityReport` | class | 'AvailabilityReport' is a struct that records whether something is available via a 'bool' flag and, optionally, a 'String' explaining why it is not. [crates/gwiki/src/benchmark.rs:88-91] |
| `OptionalBenchmarkSources` | class | 'OptionalBenchmarkSources' is a configuration container that optionally holds Falkor, Qdrant, and semantic embedding sources for benchmarking, along with a flag indicating whether a model provider is available. [crates/gwiki/src/benchmark.rs:94-99] |
| `BenchmarkRows` | class | 'BenchmarkRows' is a data structure that aggregates benchmark input/output rows and counts for documents, links, sources, and per-kind frequencies, while storing the corresponding document and chunk paths and contents as string vectors. [crates/gwiki/src/benchmark.rs:104-114] |
| `RetrievalPrecisionCandidate` | class | 'RetrievalPrecisionCandidate' is a data-only struct that pairs a retrieval 'query' string with the 'expected_path' string used as the target result for precision evaluation. [crates/gwiki/src/benchmark.rs:117-120] |
| `report_from_postgres` | function | Loads benchmark rows from Postgres for the given search scope, computes token compression, source mix, graph coverage, retrieval precision, and model provider metadata, and returns a 'BenchmarkReport' assembled from those metrics. [crates/gwiki/src/benchmark.rs:122-145] |
| `resolve_optional_sources` | function | Builds and returns an 'OptionalBenchmarkSources' by resolving FalkorDB, Qdrant, and benchmark embedding configuration from the given 'ConfigSource', and by computing whether a model provider is available from 'AiContext'. [crates/gwiki/src/benchmark.rs:147-157] |
| `build_report` | function | 'build_report' constructs a 'BenchmarkReport' from the provided benchmark subreports and scope, while aggregating a sorted deduplicated 'degraded_sources' list based on unavailable graph coverage, missing Qdrant configuration, absent embeddings, backend-degraded retrieval sources, and an unavailable model provider. [crates/gwiki/src/benchmark.rs:159-193] |
| `load_benchmark_rows` | function | 'load_benchmark_rows' queries either scoped or global 'gwiki_documents', 'gwiki_chunks', 'gwiki_sources', and 'gwiki_links' data from the database, aggregates them into ordered row vectors and grouped/scalar counts, and returns the assembled 'BenchmarkRows' or a 'WikiError'. [crates/gwiki/src/benchmark.rs:195-249] |
| `query_scoped_or_global` | function | Executes 'scoped_sql' with 'scope_kind' and 'scope_id' parameters when 'scope.scope_filter()' returns 'Some', otherwise executes 'global_sql' with no parameters, and maps any PostgreSQL error through 'postgres_error(action)'. [crates/gwiki/src/benchmark.rs:251-264] |
| `grouped_counts` | function | Executes either the scoped or global SQL query, converts each returned '(kind, count)' row into '(String, u64)' using 'count_to_u64', and collects the results into a 'BTreeMap<String, u64>' or returns a 'WikiError' on failure. [crates/gwiki/src/benchmark.rs:266-281] |
| `scalar_count` | function | Executes either a scoped or global SQL count query based on 'scope.scope_filter()', converts the first row’s 'i64' count to 'u64', and returns it as 'Result<u64, WikiError>' with PostgreSQL errors wrapped using 'action'. [crates/gwiki/src/benchmark.rs:283-299] |
| `count_to_u64` | function | Converts an 'i64' count to 'u64', returning 'Ok(count as u64)' when nonnegative and a 'WikiError::Config' with a formatted message when the count is negative. [crates/gwiki/src/benchmark.rs:301-305] |
| `token_compression` | function | Computes total token counts for all document bodies and chunk contents, derives a rounded chunk-to-document compression ratio when document tokens are nonzero, and returns a 'TokenCompressionReport' indicating availability plus an explanatory reason when no document tokens exist. [crates/gwiki/src/benchmark.rs:307-331] |
| `source_mix` | function | 'source_mix' constructs and returns a 'SourceMixReport' marked available, copying the document and source counts and kind breakdowns from 'rows' and leaving 'reason' unset. [crates/gwiki/src/benchmark.rs:333-342] |
| `graph_coverage` | function | Returns a 'GraphCoverageReport' that always includes PostgreSQL document/link counts, and if FalkorDB is configured and 'query_graph_counts' succeeds marks coverage available with graph counts, otherwise marks it unavailable with a reason indicating either missing FalkorDB configuration or the query error. [crates/gwiki/src/benchmark.rs:344-377] |
| `retrieval_precision` | function | Constructs a default OpenAI embedding backend and Gobby Qdrant vector backend, then delegates to 'retrieval_precision_with_backends' to compute and return a 'RetrievalPrecisionReport' for the given benchmark rows, search scope, optional sources, and candidate limit. [crates/gwiki/src/benchmark.rs:379-395] |
| `retrieval_precision_with_backends` | function | Computes a retrieval-precision report by running seeded semantic searches against the configured Qdrant/embedding backends, returning an unavailable report on missing configuration, no candidates, search errors, or any degradation, and otherwise aggregating the per-query outcomes. [crates/gwiki/src/benchmark.rs:397-489] |
| `unavailable_retrieval_precision` | function | Constructs a 'RetrievalPrecisionReport' marked unavailable, with no examples, a supplied reason, and the provided list of backend degraded sources. [crates/gwiki/src/benchmark.rs:491-501] |

_22 more symbol(s) not shown — run `gcode outline crates/gwiki/src/benchmark.rs` for the full list._

_Verified by 6 in-file unit tests._

