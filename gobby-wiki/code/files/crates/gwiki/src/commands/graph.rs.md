---
title: crates/gwiki/src/commands/graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/graph.rs
  ranges:
  - 13-52
  - 54-67
  - 69-90
  - 93-118
  - 129-131
  - 134-137
  - 141-143
  - 145-147
  - 150-158
  - 160-162
  - 164-168
  - 172-180
  - 184-186
  - 190-195
  - 199-204
  - 208-217
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/graph.rs:13-52](crates/gwiki/src/commands/graph.rs#L13-L52), [crates/gwiki/src/commands/graph.rs:54-67](crates/gwiki/src/commands/graph.rs#L54-L67), [crates/gwiki/src/commands/graph.rs:69-90](crates/gwiki/src/commands/graph.rs#L69-L90), [crates/gwiki/src/commands/graph.rs:93-118](crates/gwiki/src/commands/graph.rs#L93-L118), [crates/gwiki/src/commands/graph.rs:129-131](crates/gwiki/src/commands/graph.rs#L129-L131), [crates/gwiki/src/commands/graph.rs:134-137](crates/gwiki/src/commands/graph.rs#L134-L137), [crates/gwiki/src/commands/graph.rs:141-143](crates/gwiki/src/commands/graph.rs#L141-L143), [crates/gwiki/src/commands/graph.rs:145-147](crates/gwiki/src/commands/graph.rs#L145-L147), [crates/gwiki/src/commands/graph.rs:150-158](crates/gwiki/src/commands/graph.rs#L150-L158), [crates/gwiki/src/commands/graph.rs:160-162](crates/gwiki/src/commands/graph.rs#L160-L162), [crates/gwiki/src/commands/graph.rs:164-168](crates/gwiki/src/commands/graph.rs#L164-L168), [crates/gwiki/src/commands/graph.rs:172-180](crates/gwiki/src/commands/graph.rs#L172-L180), [crates/gwiki/src/commands/graph.rs:184-186](crates/gwiki/src/commands/graph.rs#L184-L186), [crates/gwiki/src/commands/graph.rs:190-195](crates/gwiki/src/commands/graph.rs#L190-L195), [crates/gwiki/src/commands/graph.rs:199-204](crates/gwiki/src/commands/graph.rs#L199-L204), [crates/gwiki/src/commands/graph.rs:208-217](crates/gwiki/src/commands/graph.rs#L208-L217)

</details>

# crates/gwiki/src/commands/graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the `gwiki graph` command. `execute` resolves the selected scope, connects to PostgreSQL, checks which optional graph services are degraded, loads wiki graph facts, chooses normal or degraded export options, and writes graph export artifacts into the scoped command outcome.

The helper functions break that validation into pieces: `degraded_optional_sources` and `degraded_optional_sources_from_config` inspect config sources for missing FalkorDB, embedding, Qdrant, and related semantic-relations support, while `has_embedding_capability` determines whether an embedding provider is actually available. The `TestConfigSource` helper and the `degraded_markers`/fixture constructors support tests that verify missing-service reporting and acceptance of present or blank optional settings.
[crates/gwiki/src/commands/graph.rs:13-52]
[crates/gwiki/src/commands/graph.rs:54-67]
[crates/gwiki/src/commands/graph.rs:69-90]
[crates/gwiki/src/commands/graph.rs:93-118]
[crates/gwiki/src/commands/graph.rs:129-131]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `243729ba-cdd5-53a7-85c1-11deca29beb1` | 13-52 [crates/gwiki/src/commands/graph.rs:13-52] | Indexed function `execute` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:13-52] |
| `degraded_optional_sources` | function | `fn degraded_optional_sources(conn: &mut postgres::Client) -> Result<Vec<String>, WikiError> {` | `degraded_optional_sources [function]` | `81fdd806-cf1b-5f24-a89a-f4176c2f80a8` | 54-67 [crates/gwiki/src/commands/graph.rs:54-67] | Indexed function `degraded_optional_sources` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:54-67] |
| `degraded_optional_sources_from_config` | function | `fn degraded_optional_sources_from_config(source: &mut impl ConfigSource) -> Vec<String> {` | `degraded_optional_sources_from_config [function]` | `9e8c7582-87e2-5c66-82c6-8c8dd628d614` | 69-90 [crates/gwiki/src/commands/graph.rs:69-90] | Indexed function `degraded_optional_sources_from_config` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:69-90] |
| `has_embedding_capability` | function | `fn has_embedding_capability(routing: AiRouting, source: &mut impl ConfigSource) -> bool {` | `has_embedding_capability [function]` | `cba08437-a959-5782-ae54-29033a6b5e1c` | 93-118 [crates/gwiki/src/commands/graph.rs:93-118] | Indexed function `has_embedding_capability` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:93-118] |
| `TestConfigSource` | class | `struct TestConfigSource {` | `TestConfigSource [class]` | `ae13ec2c-fe46-59cf-95e1-3c99785b8400` | 129-131 [crates/gwiki/src/commands/graph.rs:129-131] | Indexed class `TestConfigSource` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:129-131] |
| `TestConfigSource::with` | method | `fn with(mut self, key: &'static str, value: &'static str) -> Self {` | `TestConfigSource::with [method]` | `195d5436-4d45-5b6d-8c08-4c3bbeba0a1d` | 134-137 [crates/gwiki/src/commands/graph.rs:134-137] | Indexed method `TestConfigSource::with` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:134-137] |
| `TestConfigSource::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `TestConfigSource::config_value [method]` | `a1bcae0c-6916-5dcd-bb81-ebed85f967c3` | 141-143 [crates/gwiki/src/commands/graph.rs:141-143] | Indexed method `TestConfigSource::config_value` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:141-143] |
| `TestConfigSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `TestConfigSource::resolve_value [method]` | `67fe4c3e-21e6-519f-89d4-803fd3b9ee80` | 145-147 [crates/gwiki/src/commands/graph.rs:145-147] | Indexed method `TestConfigSource::resolve_value` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:145-147] |
| `degraded_markers` | function | `fn degraded_markers(mut source: TestConfigSource) -> Vec<String> {` | `degraded_markers [function]` | `c259dc39-44a0-5546-9714-65836c7dfa44` | 150-158 [crates/gwiki/src/commands/graph.rs:150-158] | Indexed function `degraded_markers` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:150-158] |
| `falkor_config` | function | `fn falkor_config() -> TestConfigSource {` | `falkor_config [function]` | `751ac09d-734c-511c-9b9f-bfd30a931dbc` | 160-162 [crates/gwiki/src/commands/graph.rs:160-162] | Indexed function `falkor_config` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:160-162] |
| `with_embedding_and_qdrant` | function | `fn with_embedding_and_qdrant(source: TestConfigSource) -> TestConfigSource {` | `with_embedding_and_qdrant [function]` | `2d8ff279-a767-53ac-8e14-c6c549944cb8` | 164-168 [crates/gwiki/src/commands/graph.rs:164-168] | Indexed function `with_embedding_and_qdrant` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:164-168] |
| `degraded_optional_sources_reports_all_missing_optional_services` | function | `fn degraded_optional_sources_reports_all_missing_optional_services() {` | `degraded_optional_sources_reports_all_missing_optional_services [function]` | `d6da738a-d9cf-5ca4-8062-b6a5896c4306` | 172-180 [crates/gwiki/src/commands/graph.rs:172-180] | Indexed function `degraded_optional_sources_reports_all_missing_optional_services` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:172-180] |
| `degraded_optional_sources_accepts_present_falkor_embedding_and_qdrant` | function | `fn degraded_optional_sources_accepts_present_falkor_embedding_and_qdrant() {` | `degraded_optional_sources_accepts_present_falkor_embedding_and_qdrant [function]` | `536c53a1-d88e-5ec9-9570-4d2e49b60df0` | 184-186 [crates/gwiki/src/commands/graph.rs:184-186] | Indexed function `degraded_optional_sources_accepts_present_falkor_embedding_and_qdrant` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:184-186] |
| `degraded_optional_sources_reports_missing_falkor_only` | function | `fn degraded_optional_sources_reports_missing_falkor_only() {` | `degraded_optional_sources_reports_missing_falkor_only [function]` | `96de6f16-779e-5b82-9ec1-382599d4539b` | 190-195 [crates/gwiki/src/commands/graph.rs:190-195] | Indexed function `degraded_optional_sources_reports_missing_falkor_only` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:190-195] |
| `degraded_optional_sources_reports_missing_semantic_relations` | function | `fn degraded_optional_sources_reports_missing_semantic_relations() {` | `degraded_optional_sources_reports_missing_semantic_relations [function]` | `dbb4f580-c079-5d64-aafa-f8bc4f76aa2c` | 199-204 [crates/gwiki/src/commands/graph.rs:199-204] | Indexed function `degraded_optional_sources_reports_missing_semantic_relations` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:199-204] |
| `degraded_optional_sources_treats_blank_qdrant_url_as_missing` | function | `fn degraded_optional_sources_treats_blank_qdrant_url_as_missing() {` | `degraded_optional_sources_treats_blank_qdrant_url_as_missing [function]` | `6ddc31d4-0b70-5ce8-bb2f-cb3b8c6ebc7f` | 208-217 [crates/gwiki/src/commands/graph.rs:208-217] | Indexed function `degraded_optional_sources_treats_blank_qdrant_url_as_missing` in `crates/gwiki/src/commands/graph.rs`. [crates/gwiki/src/commands/graph.rs:208-217] |
