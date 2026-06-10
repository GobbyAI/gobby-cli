---
title: crates/gwiki/src/research/model.rs
type: code_file
provenance:
- file: crates/gwiki/src/research/model.rs
  ranges:
  - 21-24
  - 26-33
  - 27-32
  - 35-96
  - 36-95
  - 103-105
  - 107-129
  - 108-114
  - 116-128
  - 131-142
  - 144-146
  - 148-159
  - 149-158
  - 161-163
  - 165-181
  - 166-180
  - 183-204
  - 206-208
  - 210-218
  - 211-217
  - 220-222
  - 224-254
  - 225-233
  - 235-253
  - 256-259
  - 262-269
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research/model.rs

Module: [[code/modules/crates/gwiki/src/research|crates/gwiki/src/research]]

## Purpose

`crates/gwiki/src/research/model.rs` exposes 26 indexed API symbols.
[crates/gwiki/src/research/model.rs:21-24]
[crates/gwiki/src/research/model.rs:26-33]
[crates/gwiki/src/research/model.rs:27-32]
[crates/gwiki/src/research/model.rs:35-96]
[crates/gwiki/src/research/model.rs:36-95]
[crates/gwiki/src/research/model.rs:103-105]
[crates/gwiki/src/research/model.rs:107-129]
[crates/gwiki/src/research/model.rs:108-114]
[crates/gwiki/src/research/model.rs:116-128]
[crates/gwiki/src/research/model.rs:131-142]
[crates/gwiki/src/research/model.rs:144-146]
[crates/gwiki/src/research/model.rs:148-159]
[crates/gwiki/src/research/model.rs:149-158]
[crates/gwiki/src/research/model.rs:161-163]
[crates/gwiki/src/research/model.rs:165-181]
[crates/gwiki/src/research/model.rs:166-180]
[crates/gwiki/src/research/model.rs:183-204]
[crates/gwiki/src/research/model.rs:206-208]
[crates/gwiki/src/research/model.rs:210-218]
[crates/gwiki/src/research/model.rs:211-217]
[crates/gwiki/src/research/model.rs:220-222]
[crates/gwiki/src/research/model.rs:224-254]
[crates/gwiki/src/research/model.rs:225-233]
[crates/gwiki/src/research/model.rs:235-253]
[crates/gwiki/src/research/model.rs:256-259]
[crates/gwiki/src/research/model.rs:262-269]

## API Symbols

- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`b1dfc6dd-5168-54a2-afa3-49c24d5147c8`) lines 21-24 [crates/gwiki/src/research/model.rs:21-24]
  - Signature: `pub(crate) struct GcoreResearchModel {`
  - Purpose: `GcoreResearchModel` is a crate-scoped struct that encapsulates an AI routing selection and a boolean flag indicating whether AI processing is required. [crates/gwiki/src/research/model.rs:21-24]
- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`3ee55bc7-7354-547e-ba42-a0cc7cf5f563`) lines 26-33 [crates/gwiki/src/research/model.rs:26-33]
  - Signature: `impl GcoreResearchModel {`
  - Purpose: `GcoreResearchModel` implements the `ai_unavailable` method, a generic error handler that returns a `WikiError::Config` when AI is required, or a `ResearchModelError::AiUnavailable` error otherwise. [crates/gwiki/src/research/model.rs:26-33]
- `GcoreResearchModel.ai_unavailable` (method) component `GcoreResearchModel.ai_unavailable [method]` (`3e30be16-a998-5e22-ba40-a8bc4e7daeb9`) lines 27-32 [crates/gwiki/src/research/model.rs:27-32]
  - Signature: `fn ai_unavailable<T>(&self, message: String) -> Result<T, ResearchModelError> {`
  - Purpose: Returns a `ResearchModelError` representing AI unavailability as a `WikiError::Config` if AI is required, or as an `AiUnavailable` variant otherwise, both carrying the provided message. [crates/gwiki/src/research/model.rs:27-32]
- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`cfca1604-d73b-54b7-b92d-82ed622e3acf`) lines 35-96 [crates/gwiki/src/research/model.rs:35-96]
  - Signature: `impl ResearchModel for GcoreResearchModel {`
  - Purpose: GcoreResearchModel implements ResearchModel::next_action to route text generation requests through configurable AI backends (Direct or Daemon) with token budget validation and parses responses into model decisions. [crates/gwiki/src/research/model.rs:35-96]
- `GcoreResearchModel.next_action` (method) component `GcoreResearchModel.next_action [method]` (`b732a8bd-725c-5999-a9c3-d4f4b5d6c512`) lines 36-95 [crates/gwiki/src/research/model.rs:36-95]
  - Signature: `fn next_action(`
  - Purpose: # Summary

This method routes a text generation request through a configured AI backend (Direct or Daemon), enforces token budget constraints, and parses the generated response into a `ModelAction`. [crates/gwiki/src/research/model.rs:36-95]
- `ResearchHubPrimary` (class) component `ResearchHubPrimary [class]` (`64ba9cc6-80e9-5a27-9a57-330fb449554a`) lines 103-105 [crates/gwiki/src/research/model.rs:103-105]
  - Signature: `pub(crate) struct ResearchHubPrimary {`
  - Purpose: ResearchHubPrimary is a crate-scoped struct that encapsulates an optional PostgreSQL client connection. [crates/gwiki/src/research/model.rs:103-105]
- `ResearchHubPrimary` (class) component `ResearchHubPrimary [class]` (`75e47f3c-8b22-57e6-8940-19f53300c15a`) lines 107-129 [crates/gwiki/src/research/model.rs:107-129]
  - Signature: `impl gobby_core::config::ConfigSource for ResearchHubPrimary {`
  - Purpose: `ResearchHubPrimary` implements the `ConfigSource` trait to fetch configuration values from PostgreSQL and resolve secrets, with fallback handling for non-secret literal values when the database connection is unavailable. [crates/gwiki/src/research/model.rs:107-129]
- `ResearchHubPrimary.config_value` (method) component `ResearchHubPrimary.config_value [method]` (`d88e1e01-7d30-5d3b-b183-885529b5e9c1`) lines 108-114 [crates/gwiki/src/research/model.rs:108-114]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Retrieves a configuration value from PostgreSQL by key, decodes the raw value, and returns the decoded string or None if the connection is unavailable, the query fails, or decoding fails. [crates/gwiki/src/research/model.rs:108-114]
- `ResearchHubPrimary.resolve_value` (method) component `ResearchHubPrimary.resolve_value [method]` (`bbb0f800-11ca-5198-b641-da93f5ab2e64`) lines 116-128 [crates/gwiki/src/research/model.rs:116-128]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Resolves configuration values through a database-backed secret resolver if a connection exists, or returns the literal value if no secret prefix is present, raising an error if secret resolution is required without a connection. [crates/gwiki/src/research/model.rs:116-128]
- `research_ai_config_source` (function) component `research_ai_config_source [function]` (`87ca6721-3c00-52c5-82a7-2e59d7d17529`) lines 131-142 [crates/gwiki/src/research/model.rs:131-142]
  - Signature: `pub(crate) fn research_ai_config_source() -> Result<AiConfigSource<ResearchHubPrimary>, WikiError> {`
  - Purpose: Initializes an `AiConfigSource` for the `ResearchHubPrimary` research hub by resolving the Gobby home directory and establishing an optional read-write database connection. [crates/gwiki/src/research/model.rs:131-142]
- `CommandAsk` (class) component `CommandAsk [class]` (`ffd5be04-2b79-5830-b991-a7777464b837`) lines 144-146 [crates/gwiki/src/research/model.rs:144-146]
  - Signature: `pub(crate) struct CommandAsk {`
  - Purpose: `CommandAsk` is a crate-private struct that wraps a `ScopeSelection` to encapsulate a scoped command query. [crates/gwiki/src/research/model.rs:144-146]
- `CommandAsk` (class) component `CommandAsk [class]` (`50174e5a-60d9-5ba2-b6a4-e17d2d94c959`) lines 148-159 [crates/gwiki/src/research/model.rs:148-159]
  - Signature: `impl WikiAsk for CommandAsk {`
  - Purpose: `CommandAsk` implements the `WikiAsk` trait by executing queries through the `ask` module with AI routing disabled, converting the outcomes to `ResearchObservation` results. [crates/gwiki/src/research/model.rs:148-159]
- `CommandAsk.ask` (method) component `CommandAsk.ask [method]` (`410da895-6404-58a3-b146-11bb37b8b5ef`) lines 149-158 [crates/gwiki/src/research/model.rs:149-158]
  - Signature: `fn ask(&mut self, query: &str) -> Result<ResearchObservation, WikiError> {`
  - Purpose: This method executes a query through the `ask::execute` function with the current selection state and transforms the outcome into a `ResearchObservation`. [crates/gwiki/src/research/model.rs:149-158]
- `CommandSearch` (class) component `CommandSearch [class]` (`c1ff3510-efe1-5dc6-bbf3-5bfb1891a02d`) lines 161-163 [crates/gwiki/src/research/model.rs:161-163]
  - Signature: `pub(crate) struct CommandSearch {`
  - Purpose: `CommandSearch` is a crate-internal struct that encapsulates a `ScopeSelection` to represent the scope context for a command search operation. [crates/gwiki/src/research/model.rs:161-163]
- `CommandSearch` (class) component `CommandSearch [class]` (`234865bd-d25d-5fb5-bc01-b37a5ec218d4`) lines 165-181 [crates/gwiki/src/research/model.rs:165-181]
  - Signature: `impl WikiSearch for CommandSearch {`
  - Purpose: CommandSearch is a WikiSearch implementation that executes searches, aggregates and deduplicates source paths with extracted code citations, and returns the results wrapped in a ResearchObservation. [crates/gwiki/src/research/model.rs:165-181]
- `CommandSearch.search` (method) component `CommandSearch.search [method]` (`9170e976-9638-53ea-aa9c-988a1e590b4e`) lines 166-180 [crates/gwiki/src/research/model.rs:166-180]
  - Signature: `fn search(&mut self, query: &str, limit: usize) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Executes a parameterized search query, aggregates and deduplicates source paths and citations from results, and returns a `ResearchObservation` containing hit count, sources, code citations, and degradation metadata. [crates/gwiki/src/research/model.rs:166-180]
- `code_citations_from_search_results` (function) component `code_citations_from_search_results [function]` (`bfb54443-4e66-57d4-8134-96488a726413`) lines 183-204 [crates/gwiki/src/research/model.rs:183-204]
  - Signature: `fn code_citations_from_search_results(`
  - Purpose: Transforms code-type search results into deduplicated `ResearchCodeCitation` objects by extracting and mapping source path, title, and provenance metadata (defaulting to "search" when sources are empty). [crates/gwiki/src/research/model.rs:183-204]
- `CommandRead` (class) component `CommandRead [class]` (`ad2c4899-e097-58b1-99f9-909c76105ede`) lines 206-208 [crates/gwiki/src/research/model.rs:206-208]
  - Signature: `pub(crate) struct CommandRead {`
  - Purpose: `CommandRead` is a crate-internal struct that encapsulates a `ScopeSelection` to represent a read command targeting a specific scope. [crates/gwiki/src/research/model.rs:206-208]
- `CommandRead` (class) component `CommandRead [class]` (`f1affbbb-7143-519e-af0b-daf6e5edeed7`) lines 210-218 [crates/gwiki/src/research/model.rs:210-218]
  - Signature: `impl WikiRead for CommandRead {`
  - Purpose: CommandRead implements WikiRead by executing a path-targeted read operation and returning a deduplicated ResearchObservation containing the read outcome and source path. [crates/gwiki/src/research/model.rs:210-218]
- `CommandRead.read` (method) component `CommandRead.read [method]` (`6ece662b-3dd0-58e5-9577-70edc92245b1`) lines 211-217 [crates/gwiki/src/research/model.rs:211-217]
  - Signature: `fn read(&mut self, path: &Path) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Executes a read operation on the specified file path with the current selection state, converts the outcome to a `ResearchObservation`, tracks the source path, and deduplicates it before returning. [crates/gwiki/src/research/model.rs:211-217]
- `CommandIngestor` (class) component `CommandIngestor [class]` (`822e30b8-608e-58f1-bb26-7ce8289b5520`) lines 220-222 [crates/gwiki/src/research/model.rs:220-222]
  - Signature: `pub(crate) struct CommandIngestor {`
  - Purpose: CommandIngestor is a crate-internal struct that wraps a ScopeSelection field to manage scope-aware command input processing. [crates/gwiki/src/research/model.rs:220-222]
- `CommandIngestor` (class) component `CommandIngestor [class]` (`f9476f6f-462f-580f-9d87-e67a4aba1c05`) lines 224-254 [crates/gwiki/src/research/model.rs:224-254]
  - Signature: `impl SourceIngestor for CommandIngestor {`
  - Purpose: CommandIngestor implements SourceIngestor to ingest URLs and files through delegated index operations, conditionally appending sources to deduplicated ResearchObservations upon successful execution. [crates/gwiki/src/research/model.rs:224-254]
- `CommandIngestor.ingest_url` (method) component `CommandIngestor.ingest_url [method]` (`a7e137f4-8613-542f-a902-d5cd8d1df29d`) lines 225-233 [crates/gwiki/src/research/model.rs:225-233]
  - Signature: `fn ingest_url(&mut self, url: &str) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Ingests a URL through the index module, appends it to the observation's sources if the operation succeeds and the URL is not already present, deduplicates the sources list, and returns the resulting `ResearchObservation`. [crates/gwiki/src/research/model.rs:225-233]
- `CommandIngestor.ingest_file` (method) component `CommandIngestor.ingest_file [method]` (`a37a0133-d303-5e31-b6b6-091941ee99a9`) lines 235-253 [crates/gwiki/src/research/model.rs:235-253]
  - Signature: `fn ingest_file(&mut self, path: &Path) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Delegates file ingestion to the index module and conditionally appends the file path to the resulting observation's deduplicated sources list if the operation succeeds. [crates/gwiki/src/research/model.rs:235-253]
- `AcceptedNoteWriter` (class) component `AcceptedNoteWriter [class]` (`80cb32ae-b2e5-5539-bbad-de692b503db3`) lines 256-259 [crates/gwiki/src/research/model.rs:256-259]
  - Signature: `pub(crate) struct AcceptedNoteWriter<'a> {`
  - Purpose: `AcceptedNoteWriter<'a>` is a crate-private struct that holds borrowed references to a root filesystem path and session identifier with a shared lifetime `'a`. [crates/gwiki/src/research/model.rs:256-259]
- `write_note` (function) component `write_note [function]` (`47d24729-4808-5a0e-b215-87e2f82ead30`) lines 262-269 [crates/gwiki/src/research/model.rs:262-269]
  - Signature: `fn write_note(&mut self, note: &AcceptedNoteDraft) -> Result<NoteWriteOutcome, WikiError> {`
  - Purpose: Writes an accepted note draft to storage and returns a NoteWriteOutcome containing the persisted note, creation status, and write conflict information, or a WikiError on failure. [crates/gwiki/src/research/model.rs:262-269]

