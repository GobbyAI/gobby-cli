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
  - 133-138
  - 140-148
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

# crates/gwiki/src/commands/graph.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file implements the `gwiki graph` command: it resolves the requested scope, opens a readonly PostgreSQL connection, loads wiki graph facts, and exports graph artifacts, returning a scoped `CommandOutcome` with artifact payload and file paths. It also contains helper logic to detect degraded optional sources by wiring PostgreSQL-backed AI config resolution through Gobby home settings, then checking whether FalkorDB, embeddings, and Qdrant are available. The test-only `TestConfigSource` and its helpers provide an in-memory config source for verifying the degraded-source detection behavior across missing, present, and blank configuration cases.
[crates/gwiki/src/commands/graph.rs:13-52]
[crates/gwiki/src/commands/graph.rs:54-67]
[crates/gwiki/src/commands/graph.rs:69-90]
[crates/gwiki/src/commands/graph.rs:93-118]
[crates/gwiki/src/commands/graph.rs:129-131]

## API Symbols

- `execute` (function) component `execute [function]` (`243729ba-cdd5-53a7-85c1-11deca29beb1`) lines 13-52 [crates/gwiki/src/commands/graph.rs:13-52]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves a scope selection, loads wiki graph facts from a readonly PostgreSQL connection, exports artifacts with optional degradation handling based on source availability, and returns a `CommandOutcome` containing the exported artifacts and their paths. [crates/gwiki/src/commands/graph.rs:13-52]
- `degraded_optional_sources` (function) component `degraded_optional_sources [function]` (`81fdd806-cf1b-5f24-a89a-f4176c2f80a8`) lines 54-67 [crates/gwiki/src/commands/graph.rs:54-67]
  - Signature: `fn degraded_optional_sources(conn: &mut postgres::Client) -> Result<Vec<String>, WikiError> {`
  - Purpose: Extracts optional Wiki graph configuration sources by constructing an `AiConfigSource` from a PostgreSQL primary source and Gobby home directory configuration, with error propagation for resolution failures. [crates/gwiki/src/commands/graph.rs:54-67]
- `degraded_optional_sources_from_config` (function) component `degraded_optional_sources_from_config [function]` (`9e8c7582-87e2-5c66-82c6-8c8dd628d614`) lines 69-90 [crates/gwiki/src/commands/graph.rs:69-90]
  - Signature: `fn degraded_optional_sources_from_config(source: &mut impl ConfigSource) -> Vec<String> {`
  - Purpose: # Summary

This function checks configuration availability for optional backend services and returns a vector of feature names that are unavailable or degraded: FalkorDB (if unresolved) and semantic relations (if either AI embedding capability or Qdrant vector database is missing). [crates/gwiki/src/commands/graph.rs:69-90]
- `has_embedding_capability` (function) component `has_embedding_capability [function]` (`cba08437-a959-5782-ae54-29033a6b5e1c`) lines 93-118 [crates/gwiki/src/commands/graph.rs:93-118]
  - Signature: `fn has_embedding_capability(routing: AiRouting, source: &mut impl ConfigSource) -> bool {`
  - Purpose: Returns whether embedding capability is available for the given `AiRouting` mode, determined by either feature-gated compilation (daemon/auto modes) or configuration source resolution (direct/auto modes). [crates/gwiki/src/commands/graph.rs:93-118]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`ae13ec2c-fe46-59cf-95e1-3c99785b8400`) lines 129-131 [crates/gwiki/src/commands/graph.rs:129-131]
  - Signature: `struct TestConfigSource {`
  - Purpose: `TestConfigSource` is a struct that encapsulates a `BTreeMap<&'static str, &'static str>` to store and manage static string key-value pairs for test configuration. [crates/gwiki/src/commands/graph.rs:129-131]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`ee2586dd-65ff-5014-b48a-ed3d9201655e`) lines 133-138 [crates/gwiki/src/commands/graph.rs:133-138]
  - Signature: `impl TestConfigSource {`
  - Purpose: `TestConfigSource::with` is a fluent builder method that inserts a static string key-value pair into the configuration map and returns `self` for method chaining. [crates/gwiki/src/commands/graph.rs:133-138]
- `TestConfigSource.with` (method) component `TestConfigSource.with [method]` (`195d5436-4d45-5b6d-8c08-4c3bbeba0a1d`) lines 134-137 [crates/gwiki/src/commands/graph.rs:134-137]
  - Signature: `fn with(mut self, key: &'static str, value: &'static str) -> Self {`
  - Purpose: Inserts a static string key-value pair into the instance's internal map and returns self to enable method chaining. [crates/gwiki/src/commands/graph.rs:134-137]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`fb74c183-b1f8-56c8-9a1f-c52447eef504`) lines 140-148 [crates/gwiki/src/commands/graph.rs:140-148]
  - Signature: `impl ConfigSource for TestConfigSource {`
  - Purpose: `TestConfigSource` implements the `ConfigSource` trait by retrieving configuration values from an internal map and performing no-op identity resolution of string values. [crates/gwiki/src/commands/graph.rs:140-148]
- `TestConfigSource.config_value` (method) component `TestConfigSource.config_value [method]` (`a1bcae0c-6916-5dcd-bb81-ebed85f967c3`) lines 141-143 [crates/gwiki/src/commands/graph.rs:141-143]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Retrieves a configuration value from the internal values map by key, converts it to a String, and returns `Some(String)` if present or `None` if absent. [crates/gwiki/src/commands/graph.rs:141-143]
- `TestConfigSource.resolve_value` (method) component `TestConfigSource.resolve_value [method]` (`67fe4c3e-21e6-519f-89d4-803fd3b9ee80`) lines 145-147 [crates/gwiki/src/commands/graph.rs:145-147]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: This method converts a string reference to an owned `String` and wraps it in an `anyhow::Result`, returning `Ok` unconditionally. [crates/gwiki/src/commands/graph.rs:145-147]
- `degraded_markers` (function) component `degraded_markers [function]` (`c259dc39-44a0-5546-9714-65836c7dfa44`) lines 150-158 [crates/gwiki/src/commands/graph.rs:150-158]
  - Signature: `fn degraded_markers(mut source: TestConfigSource) -> Vec<String> {`
  - Purpose: Extracts degraded optional source markers from a test configuration after temporarily unsetting FalkorDB and Qdrant environment variables via an environment guard. [crates/gwiki/src/commands/graph.rs:150-158]
- `falkor_config` (function) component `falkor_config [function]` (`751ac09d-734c-511c-9b9f-bfd30a931dbc`) lines 160-162 [crates/gwiki/src/commands/graph.rs:160-162]
  - Signature: `fn falkor_config() -> TestConfigSource {`
  - Purpose: Returns a `TestConfigSource` configured with the FalkorDB host set to the loopback address 127.0.0.1. [crates/gwiki/src/commands/graph.rs:160-162]
- `with_embedding_and_qdrant` (function) component `with_embedding_and_qdrant [function]` (`2d8ff279-a767-53ac-8e14-c6c549944cb8`) lines 164-168 [crates/gwiki/src/commands/graph.rs:164-168]
  - Signature: `fn with_embedding_and_qdrant(source: TestConfigSource) -> TestConfigSource {`
  - Purpose: Configures a TestConfigSource with local HTTP endpoints for an embeddings API base and Qdrant database, returning the modified source object. [crates/gwiki/src/commands/graph.rs:164-168]
- `degraded_optional_sources_reports_all_missing_optional_services` (function) component `degraded_optional_sources_reports_all_missing_optional_services [function]` (`d6da738a-d9cf-5ca4-8062-b6a5896c4306`) lines 172-180 [crates/gwiki/src/commands/graph.rs:172-180]
  - Signature: `fn degraded_optional_sources_reports_all_missing_optional_services() {`
  - Purpose: Unit test asserting that `degraded_markers()` returns degradation markers for all missing optional services (FalkorDB and semantic relations) when initialized with a default test configuration source. [crates/gwiki/src/commands/graph.rs:172-180]
- `degraded_optional_sources_accepts_present_falkor_embedding_and_qdrant` (function) component `degraded_optional_sources_accepts_present_falkor_embedding_and_qdrant [function]` (`536c53a1-d88e-5ec9-9570-4d2e49b60df0`) lines 184-186 [crates/gwiki/src/commands/graph.rs:184-186]
  - Signature: `fn degraded_optional_sources_accepts_present_falkor_embedding_and_qdrant() {`
  - Purpose: Asserts that a Falkor configuration with embedding and Qdrant sources present produces no degraded markers. [crates/gwiki/src/commands/graph.rs:184-186]
- `degraded_optional_sources_reports_missing_falkor_only` (function) component `degraded_optional_sources_reports_missing_falkor_only [function]` (`96de6f16-779e-5b82-9ec1-382599d4539b`) lines 190-195 [crates/gwiki/src/commands/graph.rs:190-195]
  - Signature: `fn degraded_optional_sources_reports_missing_falkor_only() {`
  - Purpose: This test verifies that when Qdrant and embedding sources are configured, the `degraded_markers` function reports only FalkorDB as unavailable. [crates/gwiki/src/commands/graph.rs:190-195]
- `degraded_optional_sources_reports_missing_semantic_relations` (function) component `degraded_optional_sources_reports_missing_semantic_relations [function]` (`dbb4f580-c079-5d64-aafa-f8bc4f76aa2c`) lines 199-204 [crates/gwiki/src/commands/graph.rs:199-204]
  - Signature: `fn degraded_optional_sources_reports_missing_semantic_relations() {`
  - Purpose: This test asserts that `degraded_markers()` called with a Falkor configuration returns a vector containing "semantic_relations_unavailable", verifying that the system correctly reports missing semantic relations as a degradation marker when optional sources are unavailable. [crates/gwiki/src/commands/graph.rs:199-204]
- `degraded_optional_sources_treats_blank_qdrant_url_as_missing` (function) component `degraded_optional_sources_treats_blank_qdrant_url_as_missing [function]` (`6ddc31d4-0b70-5ce8-bb2f-cb3b8c6ebc7f`) lines 208-217 [crates/gwiki/src/commands/graph.rs:208-217]
  - Signature: `fn degraded_optional_sources_treats_blank_qdrant_url_as_missing() {`
  - Purpose: Verifies that a blank Qdrant URL configuration is treated as missing and correctly triggers the `semantic_relations_unavailable` degradation marker. [crates/gwiki/src/commands/graph.rs:208-217]

