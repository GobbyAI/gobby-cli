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
  - 98-100
  - 102-113
  - 103-112
  - 115-117
  - 119-135
  - 120-134
  - 137-158
  - 160-162
  - 164-172
  - 165-171
  - 174-176
  - 178-208
  - 179-187
  - 189-207
  - 210-213
  - 216-223
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research/model.rs

Module: [[code/modules/crates/gwiki/src/research|crates/gwiki/src/research]]

## Purpose

`crates/gwiki/src/research/model.rs` exposes 21 indexed API symbols.
[crates/gwiki/src/research/model.rs:21-24]
[crates/gwiki/src/research/model.rs:26-33]
[crates/gwiki/src/research/model.rs:27-32]
[crates/gwiki/src/research/model.rs:35-96]
[crates/gwiki/src/research/model.rs:36-95]
[crates/gwiki/src/research/model.rs:98-100]
[crates/gwiki/src/research/model.rs:102-113]
[crates/gwiki/src/research/model.rs:103-112]
[crates/gwiki/src/research/model.rs:115-117]
[crates/gwiki/src/research/model.rs:119-135]
[crates/gwiki/src/research/model.rs:120-134]
[crates/gwiki/src/research/model.rs:137-158]
[crates/gwiki/src/research/model.rs:160-162]
[crates/gwiki/src/research/model.rs:164-172]
[crates/gwiki/src/research/model.rs:165-171]
[crates/gwiki/src/research/model.rs:174-176]
[crates/gwiki/src/research/model.rs:178-208]
[crates/gwiki/src/research/model.rs:179-187]
[crates/gwiki/src/research/model.rs:189-207]
[crates/gwiki/src/research/model.rs:210-213]
[crates/gwiki/src/research/model.rs:216-223]

## API Symbols

- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`caf20e91-0840-562e-ac35-5058d3ecad26`) lines 21-24 [crates/gwiki/src/research/model.rs:21-24]
  - Signature: `pub(crate) struct GcoreResearchModel {`
  - Purpose: GcoreResearchModel is a crate-internal struct that pairs an AI routing strategy with a boolean flag indicating whether AI processing is mandatory. [crates/gwiki/src/research/model.rs:21-24]
- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`7b6646f4-1914-51e3-9377-2fa387936279`) lines 26-33 [crates/gwiki/src/research/model.rs:26-33]
  - Signature: `impl GcoreResearchModel {`
  - Purpose: `GcoreResearchModel` implements a generic error handler method that conditionally returns a configuration error if AI is required, otherwise returns an `AiUnavailable` error based on the `require_ai` flag. [crates/gwiki/src/research/model.rs:26-33]
- `GcoreResearchModel.ai_unavailable` (method) component `GcoreResearchModel.ai_unavailable [method]` (`18f3ae85-60d6-590f-b07e-8fae11641408`) lines 27-32 [crates/gwiki/src/research/model.rs:27-32]
  - Signature: `fn ai_unavailable<T>(&self, message: String) -> Result<T, ResearchModelError> {`
  - Purpose: Returns a `ResearchModelError` that is either a converted `WikiError::Config` (if `require_ai` is true) or `ResearchModelError::AiUnavailable` (otherwise). [crates/gwiki/src/research/model.rs:27-32]
- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`32d9f475-2599-5454-acdc-0ced8e80fb47`) lines 35-96 [crates/gwiki/src/research/model.rs:35-96]
  - Signature: `impl ResearchModel for GcoreResearchModel {`
  - Purpose: `GcoreResearchModel` implements the `ResearchModel` trait to orchestrate text generation through configurable AI routing (Direct/Daemon), enforce token budget constraints, and parse responses into structured `ModelDecision` outputs. [crates/gwiki/src/research/model.rs:35-96]
- `GcoreResearchModel.next_action` (method) component `GcoreResearchModel.next_action [method]` (`68c822f1-60d4-50a5-95ee-6c55eb050e06`) lines 36-95 [crates/gwiki/src/research/model.rs:36-95]
  - Signature: `fn next_action(`
  - Purpose: Resolves AI context with routing preferences, generates text through the appropriate backend (Direct or Daemon) within token budget constraints, parses the response into a ModelAction, and returns the result as a ModelDecision. [crates/gwiki/src/research/model.rs:36-95]
- `CommandAsk` (class) component `CommandAsk [class]` (`51c8007e-a780-5511-bff3-ce109d377c0d`) lines 98-100 [crates/gwiki/src/research/model.rs:98-100]
  - Signature: `pub(crate) struct CommandAsk {`
  - Purpose: CommandAsk is a crate-private struct that wraps a ScopeSelection to represent a scoped command query. [crates/gwiki/src/research/model.rs:98-100]
- `CommandAsk` (class) component `CommandAsk [class]` (`ea4ba7a4-ff71-5e49-a588-baa3e0ac52cd`) lines 102-113 [crates/gwiki/src/research/model.rs:102-113]
  - Signature: `impl WikiAsk for CommandAsk {`
  - Purpose: `CommandAsk` is a `WikiAsk` trait implementation that executes queries through `ask::execute` with AI routing disabled and converts the outcome to a `ResearchObservation`. [crates/gwiki/src/research/model.rs:102-113]
- `CommandAsk.ask` (method) component `CommandAsk.ask [method]` (`3ae8308d-6b4c-5864-a07e-7176ddd2cc4c`) lines 103-112 [crates/gwiki/src/research/model.rs:103-112]
  - Signature: `fn ask(&mut self, query: &str) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Executes a query against the current selection with AI routing disabled, converting the outcome to a ResearchObservation. [crates/gwiki/src/research/model.rs:103-112]
- `CommandSearch` (class) component `CommandSearch [class]` (`87e28c91-5cea-5a3a-b1d8-cba85094a3d0`) lines 115-117 [crates/gwiki/src/research/model.rs:115-117]
  - Signature: `pub(crate) struct CommandSearch {`
  - Purpose: `CommandSearch` is a crate-private struct that encapsulates a `ScopeSelection` field to define the scope parameters for a command search operation. [crates/gwiki/src/research/model.rs:115-117]
- `CommandSearch` (class) component `CommandSearch [class]` (`19bfaf22-ce62-5423-8bd0-012c5ced6749`) lines 119-135 [crates/gwiki/src/research/model.rs:119-135]
  - Signature: `impl WikiSearch for CommandSearch {`
  - Purpose: `CommandSearch` implements the `WikiSearch` trait to execute codebase searches via a retrieve function, aggregating results with deduplicated sources and code citations into a `ResearchObservation`. [crates/gwiki/src/research/model.rs:119-135]
- `CommandSearch.search` (method) component `CommandSearch.search [method]` (`10d9d236-11f8-5b81-b13b-bfd163b6a4ca`) lines 120-134 [crates/gwiki/src/research/model.rs:120-134]
  - Signature: `fn search(&mut self, query: &str, limit: usize) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Executes a codebase search query and returns a `ResearchObservation` containing deduplicated source paths, code citations extracted from search results, and any search degradations. [crates/gwiki/src/research/model.rs:120-134]
- `code_citations_from_search_results` (function) component `code_citations_from_search_results [function]` (`9974413e-c409-5639-a61a-6e66b1966abf`) lines 137-158 [crates/gwiki/src/research/model.rs:137-158]
  - Signature: `fn code_citations_from_search_results(`
  - Purpose: Filters search results by code type and transforms them into a deduplicated collection of `ResearchCodeCitation` objects, extracting source paths, titles, and provenance metadata (defaulting to "search" when sources are absent). [crates/gwiki/src/research/model.rs:137-158]
- `CommandRead` (class) component `CommandRead [class]` (`ab2d7649-3151-51de-94fd-c8db5e5f2494`) lines 160-162 [crates/gwiki/src/research/model.rs:160-162]
  - Signature: `pub(crate) struct CommandRead {`
  - Purpose: `CommandRead` is a crate-scoped struct that encapsulates a `ScopeSelection` to specify the scope for a read command operation. [crates/gwiki/src/research/model.rs:160-162]
- `CommandRead` (class) component `CommandRead [class]` (`ee3a9edd-b18a-58d6-8217-eb91f44e0e15`) lines 164-172 [crates/gwiki/src/research/model.rs:164-172]
  - Signature: `impl WikiRead for CommandRead {`
  - Purpose: CommandRead implements WikiRead to execute a read command at a specified path, convert the outcome to a ResearchObservation, and return it with deduplicated source tracking. [crates/gwiki/src/research/model.rs:164-172]
- `CommandRead.read` (method) component `CommandRead.read [method]` (`152b8b41-0c68-577b-89a3-af7309587791`) lines 165-171 [crates/gwiki/src/research/model.rs:165-171]
  - Signature: `fn read(&mut self, path: &Path) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Executes a read operation on the specified file path using the stored selection, converts the outcome to a ResearchObservation, appends and deduplicates the source path, then returns the result. [crates/gwiki/src/research/model.rs:165-171]
- `CommandIngestor` (class) component `CommandIngestor [class]` (`a7c6c81e-8a80-5912-acf2-fff3e1a06e27`) lines 174-176 [crates/gwiki/src/research/model.rs:174-176]
  - Signature: `pub(crate) struct CommandIngestor {`
  - Purpose: `CommandIngestor` is a crate-private struct that wraps a `ScopeSelection` to manage scoped command intake and processing. [crates/gwiki/src/research/model.rs:174-176]
- `CommandIngestor` (class) component `CommandIngestor [class]` (`212117c5-e034-5e04-86ef-a84ff11576df`) lines 178-208 [crates/gwiki/src/research/model.rs:178-208]
  - Signature: `impl SourceIngestor for CommandIngestor {`
  - Purpose: CommandIngestor implements SourceIngestor by delegating URL and file ingestion to index commands, converting execution outcomes to research observations, and maintaining deduplicated source lists. [crates/gwiki/src/research/model.rs:178-208]
- `CommandIngestor.ingest_url` (method) component `CommandIngestor.ingest_url [method]` (`c45898e3-f1d7-58a1-bbb5-29f14eb06693`) lines 179-187 [crates/gwiki/src/research/model.rs:179-187]
  - Signature: `fn ingest_url(&mut self, url: &str) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Executes URL ingestion via `index::execute_ingest_url`, converts the outcome to a ResearchObservation, conditionally appends the URL to de-duplicated sources if execution succeeds and the URL is not already present, and returns the observation. [crates/gwiki/src/research/model.rs:179-187]
- `CommandIngestor.ingest_file` (method) component `CommandIngestor.ingest_file [method]` (`11803cdc-dabc-5405-a22c-344e76cc57f5`) lines 189-207 [crates/gwiki/src/research/model.rs:189-207]
  - Signature: `fn ingest_file(&mut self, path: &Path) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Ingests a file via index operation and returns a research observation with the input path conditionally appended to its deduplicated sources if execution succeeds. [crates/gwiki/src/research/model.rs:189-207]
- `AcceptedNoteWriter` (class) component `AcceptedNoteWriter [class]` (`577432b1-8f0d-5185-9c43-d5456bf7f2c8`) lines 210-213 [crates/gwiki/src/research/model.rs:210-213]
  - Signature: `pub(crate) struct AcceptedNoteWriter<'a> {`
  - Purpose: `AcceptedNoteWriter` is a crate-internal struct that holds borrowed references to a filesystem root path and session identifier for writing accepted notes. [crates/gwiki/src/research/model.rs:210-213]
- `write_note` (function) component `write_note [function]` (`6087992c-db7e-5a6b-9c28-5d123d9b5517`) lines 216-223 [crates/gwiki/src/research/model.rs:216-223]
  - Signature: `fn write_note(&mut self, note: &AcceptedNoteDraft) -> Result<NoteWriteOutcome, WikiError> {`
  - Purpose: Persists an accepted note draft to storage via the session context and returns the resulting note with creation timestamp and write-conflict metadata, or a WikiError. [crates/gwiki/src/research/model.rs:216-223]

