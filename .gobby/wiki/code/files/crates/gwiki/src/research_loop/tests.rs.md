---
title: crates/gwiki/src/research_loop/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/research_loop/tests.rs
  ranges:
  - 12-14
  - 16-22
  - 17-21
  - 24-33
  - 25-32
  - '35'
  - 37-44
  - 38-43
  - '46'
  - 48-57
  - 49-56
  - '59'
  - 61-68
  - 62-67
  - '70'
  - 72-76
  - 73-75
  - '78'
  - 80-85
  - 81-84
  - '87'
  - 89-100
  - 90-92
  - 94-99
  - 103-106
  - 108-122
  - 109-121
  - 124-141
  - 144-168
  - 171-200
  - 202-210
  - 213-299
  - '214'
  - 216-234
  - 217-233
  - 302-363
  - '303'
  - 305-323
  - 306-322
  - 366-444
  - '367'
  - 369-379
  - 370-378
  - 447-503
  - 506-561
  - 564-601
  - 604-614
  - 617-628
  - 631-642
  - 645-656
  - 659-662
  - 665-668
  - 671-688
  - 692-706
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research_loop/tests.rs

Module: [[code/modules/crates/gwiki/src/research_loop|crates/gwiki/src/research_loop]]

## Purpose

`crates/gwiki/src/research_loop/tests.rs` exposes 54 indexed API symbols.
[crates/gwiki/src/research_loop/tests.rs:12-14]
[crates/gwiki/src/research_loop/tests.rs:16-22]
[crates/gwiki/src/research_loop/tests.rs:17-21]
[crates/gwiki/src/research_loop/tests.rs:24-33]
[crates/gwiki/src/research_loop/tests.rs:25-32]

## API Symbols

- `FakeModel` (class) component `FakeModel [class]` (`868b2217-5d95-55f7-8f85-ed8326e12078`) lines 12-14 [crates/gwiki/src/research_loop/tests.rs:12-14]
  - Signature: `struct FakeModel {`
  - Purpose: FakeModel is a struct that encapsulates a `VecDeque<ModelDecision>` for managing a double-ended queue of model decisions. [crates/gwiki/src/research_loop/tests.rs:12-14]
- `FakeModel` (class) component `FakeModel [class]` (`dca03cfa-e89e-540b-aa6c-f9a7d92fc012`) lines 16-22 [crates/gwiki/src/research_loop/tests.rs:16-22]
  - Signature: `impl FakeModel {`
  - Purpose: `FakeModel::new` is a constructor that initializes a `FakeModel` instance by converting a `Vec<ModelDecision>` into the `decisions` field via the `Into` trait. [crates/gwiki/src/research_loop/tests.rs:16-22]
- `FakeModel.new` (method) component `FakeModel.new [method]` (`1cd24e1b-b512-5735-8f14-fe8e82fef050`) lines 17-21 [crates/gwiki/src/research_loop/tests.rs:17-21]
  - Signature: `fn new(decisions: Vec<ModelDecision>) -> Self {`
  - Purpose: Constructs a new instance by converting the provided `Vec<ModelDecision>` into the `decisions` field via the `Into` trait. [crates/gwiki/src/research_loop/tests.rs:17-21]
- `FakeModel` (class) component `FakeModel [class]` (`1e6ececa-0fe5-588c-b325-3df05b2bd832`) lines 24-33 [crates/gwiki/src/research_loop/tests.rs:24-33]
  - Signature: `impl ResearchModel for FakeModel {`
  - Purpose: `FakeModel` implements `ResearchModel` by sequentially dequeuing prequeued `ModelDecision` values, returning an `InvalidResponse` error when the queue is exhausted. [crates/gwiki/src/research_loop/tests.rs:24-33]
- `FakeModel.next_action` (method) component `FakeModel.next_action [method]` (`2570ba48-e22d-5e49-93d2-895acfdb88c2`) lines 25-32 [crates/gwiki/src/research_loop/tests.rs:25-32]
  - Signature: `fn next_action(`
  - Purpose: This method dequeues and returns the next `ModelDecision` from an internal queue, or returns an `InvalidResponse` error if the queue is empty. [crates/gwiki/src/research_loop/tests.rs:25-32]
- `BudgetModel` (class) component `BudgetModel [class]` (`20cb03c3-f881-5291-abc8-74aea3e103b8`) lines 35-35 [crates/gwiki/src/research_loop/tests.rs:35]
  - Signature: `struct BudgetModel;`
  - Purpose: BudgetModel is a zero-sized Rust struct with no fields or visible implementation. [crates/gwiki/src/research_loop/tests.rs:35]
- `BudgetModel` (class) component `BudgetModel [class]` (`04c33b0e-d324-5acc-82f0-3e600685ed55`) lines 37-44 [crates/gwiki/src/research_loop/tests.rs:37-44]
  - Signature: `impl ResearchModel for BudgetModel {`
  - Purpose: BudgetModel is a ResearchModel implementation that unconditionally returns a `BudgetExceeded` error from its `next_action` method, serving as a sentinel state when resource budgets are exhausted. [crates/gwiki/src/research_loop/tests.rs:37-44]
- `BudgetModel.next_action` (method) component `BudgetModel.next_action [method]` (`abb726db-3ebf-5fb0-85da-bb47292a69d8`) lines 38-43 [crates/gwiki/src/research_loop/tests.rs:38-43]
  - Signature: `fn next_action(`
  - Purpose: This method unconditionally returns a `ResearchModelError::BudgetExceeded` error, indicating that the research model's computational or decision budget has been exhausted. [crates/gwiki/src/research_loop/tests.rs:38-43]
- `AiUnavailableModel` (class) component `AiUnavailableModel [class]` (`7a802989-d790-50cb-98b4-0be3a91af333`) lines 46-46 [crates/gwiki/src/research_loop/tests.rs:46]
  - Signature: `struct AiUnavailableModel;`
  - Purpose: `AiUnavailableModel` is a zero-sized marker struct used to represent the state or type of an unavailable AI model. [crates/gwiki/src/research_loop/tests.rs:46]
- `AiUnavailableModel` (class) component `AiUnavailableModel [class]` (`9e836069-8fda-5b9d-b38f-b3af22e1ff3e`) lines 48-57 [crates/gwiki/src/research_loop/tests.rs:48-57]
  - Signature: `impl ResearchModel for AiUnavailableModel {`
  - Purpose: `AiUnavailableModel` is a `ResearchModel` implementation that unconditionally returns an `AiUnavailable` error for all `next_action` requests, serving as a stub when the text generation service is disabled. [crates/gwiki/src/research_loop/tests.rs:48-57]
- `AiUnavailableModel.next_action` (method) component `AiUnavailableModel.next_action [method]` (`3de4015c-374a-51ac-a83e-307a66edc20d`) lines 49-56 [crates/gwiki/src/research_loop/tests.rs:49-56]
  - Signature: `fn next_action(`
  - Purpose: The `next_action` method unconditionally returns a `ResearchModelError::AiUnavailable` error, indicating that the text generation route is disabled. [crates/gwiki/src/research_loop/tests.rs:49-56]
- `FakeSearch` (class) component `FakeSearch [class]` (`f669f3c7-4b47-5425-91cd-db497e5c9c75`) lines 59-59 [crates/gwiki/src/research_loop/tests.rs:59]
  - Signature: `struct FakeSearch;`
  - Purpose: `FakeSearch` is a zero-sized empty struct type with no fields or associated methods. [crates/gwiki/src/research_loop/tests.rs:59]
- `FakeSearch` (class) component `FakeSearch [class]` (`3a8ff63e-be78-50f3-a28c-cd895e82da30`) lines 61-68 [crates/gwiki/src/research_loop/tests.rs:61-68]
  - Signature: `impl WikiSearch for FakeSearch {`
  - Purpose: FakeSearch is a mock implementation of the WikiSearch trait that returns a dummy ResearchObservation echoing the input query and a hardcoded source reference, used for testing without actual search functionality. [crates/gwiki/src/research_loop/tests.rs:61-68]
- `FakeSearch.search` (method) component `FakeSearch.search [method]` (`20696c09-b5e1-5b60-9b6e-b257b696964d`) lines 62-67 [crates/gwiki/src/research_loop/tests.rs:62-67]
  - Signature: `fn search(&mut self, query: &str, _limit: usize) -> Result<ResearchObservation, WikiError> {`
  - Purpose: This method returns a `ResearchObservation` containing the search query and a hardcoded source reference, implementing a search operation without executing actual search logic. [crates/gwiki/src/research_loop/tests.rs:62-67]
- `FakeAsk` (class) component `FakeAsk [class]` (`eefd9137-f916-54d7-9ac9-396ad24c724c`) lines 70-70 [crates/gwiki/src/research_loop/tests.rs:70]
  - Signature: `struct FakeAsk;`
  - Purpose: FakeAsk is a zero-sized unit struct in Rust with no fields or associated methods defined. [crates/gwiki/src/research_loop/tests.rs:70]
- `FakeAsk` (class) component `FakeAsk [class]` (`8c429fc5-cc0e-5a39-9eb0-f0a07738dace`) lines 72-76 [crates/gwiki/src/research_loop/tests.rs:72-76]
  - Signature: `impl WikiAsk for FakeAsk {`
  - Purpose: FakeAsk is a mock implementation of the WikiAsk trait that returns a dummy ResearchObservation echoing the input query without performing actual research. [crates/gwiki/src/research_loop/tests.rs:72-76]
- `FakeAsk.ask` (method) component `FakeAsk.ask [method]` (`f97f5aed-7785-57f8-abf9-050ded606d75`) lines 73-75 [crates/gwiki/src/research_loop/tests.rs:73-75]
  - Signature: `fn ask(&mut self, query: &str) -> Result<ResearchObservation, WikiError> {`
  - Purpose: This method accepts a query string and returns a `ResearchObservation` result containing a formatted message that prefixes the query with "asked". [crates/gwiki/src/research_loop/tests.rs:73-75]
- `FakeRead` (class) component `FakeRead [class]` (`a4944f7e-f68f-5e24-8086-e85aa0f30cea`) lines 78-78 [crates/gwiki/src/research_loop/tests.rs:78]
  - Signature: `struct FakeRead;`
  - Purpose: FakeRead is a zero-sized unit struct (a struct with no fields), typically used as a mock implementation for testing read operations. [crates/gwiki/src/research_loop/tests.rs:78]
- `FakeRead` (class) component `FakeRead [class]` (`67a6b069-c3c9-5ce0-80db-ad1a47ca5ebb`) lines 80-85 [crates/gwiki/src/research_loop/tests.rs:80-85]
  - Signature: `impl WikiRead for FakeRead {`
  - Purpose: **FakeRead** is a mock implementation of the `WikiRead` trait that wraps a file path into a `ResearchObservation` without performing actual I/O, returning the path as both the operation name and source. [crates/gwiki/src/research_loop/tests.rs:80-85]
- `FakeRead.read` (method) component `FakeRead.read [method]` (`81667992-210f-5047-a391-0f965ff939e1`) lines 81-84 [crates/gwiki/src/research_loop/tests.rs:81-84]
  - Signature: `fn read(&mut self, path: &Path) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Constructs a ResearchObservation documenting a read operation on the specified file path, recording the path as the observation's source. [crates/gwiki/src/research_loop/tests.rs:81-84]
- `FakeIngest` (class) component `FakeIngest [class]` (`04e30e71-376a-5203-b379-eaed9eec89e0`) lines 87-87 [crates/gwiki/src/research_loop/tests.rs:87]
  - Signature: `struct FakeIngest;`
  - Purpose: FakeIngest is a unit struct with no fields, serving as a placeholder or mock implementation type. [crates/gwiki/src/research_loop/tests.rs:87]
- `FakeIngest` (class) component `FakeIngest [class]` (`fc342d7f-4083-5735-aa1c-a58ba422b2f8`) lines 89-100 [crates/gwiki/src/research_loop/tests.rs:89-100]
  - Signature: `impl SourceIngestor for FakeIngest {`
  - Purpose: FakeIngest is a mock implementation of the SourceIngestor trait that returns stub ResearchObservations with the ingested URL or file path as their sole source, without performing actual content ingestion. [crates/gwiki/src/research_loop/tests.rs:89-100]
- `FakeIngest.ingest_url` (method) component `FakeIngest.ingest_url [method]` (`b969ee74-a591-5b43-ba14-c0a23b51b1b1`) lines 90-92 [crates/gwiki/src/research_loop/tests.rs:90-92]
  - Signature: `fn ingest_url(&mut self, url: &str) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Creates a `ResearchObservation` for the provided URL and registers it as the observation's source, returning either the observation or a `WikiError`. [crates/gwiki/src/research_loop/tests.rs:90-92]
- `FakeIngest.ingest_file` (method) component `FakeIngest.ingest_file [method]` (`ffa466ce-2193-5ba7-8f73-4d3f022c7932`) lines 94-99 [crates/gwiki/src/research_loop/tests.rs:94-99]
  - Signature: `fn ingest_file(&mut self, path: &Path) -> Result<ResearchObservation, WikiError> {`
  - Purpose: # Summary

Constructs a `ResearchObservation` with the input file path as both its identifier and source, returning it wrapped in `Ok`. [crates/gwiki/src/research_loop/tests.rs:94-99]
- `FakeWriter` (class) component `FakeWriter [class]` (`f98a28b0-7250-50ed-979e-1888af530d87`) lines 103-106 [crates/gwiki/src/research_loop/tests.rs:103-106]
  - Signature: `struct FakeWriter {`
  - Purpose: FakeWriter is a struct that encapsulates a vector of `AcceptedNoteDraft` items and a boolean conflict flag. [crates/gwiki/src/research_loop/tests.rs:103-106]
- `FakeWriter` (class) component `FakeWriter [class]` (`2849f45a-8c31-5beb-bfb7-41c5a972d336`) lines 108-122 [crates/gwiki/src/research_loop/tests.rs:108-122]
  - Signature: `impl ResearchNoteWriter for FakeWriter {`
  - Purpose: FakeWriter is a test double implementing ResearchNoteWriter that appends note drafts to an internal collection and returns synthetic NoteWriteOutcome structs with configurable write_conflict semantics. [crates/gwiki/src/research_loop/tests.rs:108-122]
- `FakeWriter.write_note` (method) component `FakeWriter.write_note [method]` (`98b2d462-53c6-561e-9f74-ceabb4d03be6`) lines 109-121 [crates/gwiki/src/research_loop/tests.rs:109-121]
  - Signature: `fn write_note(&mut self, note: &AcceptedNoteDraft) -> Result<NoteWriteOutcome, WikiError> {`
  - Purpose: Appends an `AcceptedNoteDraft` to the notes collection and returns a `NoteWriteOutcome` containing the note's metadata (title, path, citations, degradation) and conflict-status flags. [crates/gwiki/src/research_loop/tests.rs:109-121]
- `test_deps` (function) component `test_deps [function]` (`c5f53028-e831-5797-b91a-b64979035d4b`) lines 124-141 [crates/gwiki/src/research_loop/tests.rs:124-141]
  - Signature: `fn test_deps<'a>(`
  - Purpose: Constructs a `ResearchLoopDeps<'a>` struct by aggregating six mutable trait object dependencies through the builder pattern. [crates/gwiki/src/research_loop/tests.rs:124-141]
- `research_loop_deps_builder_reports_missing_required_fields` (function) component `research_loop_deps_builder_reports_missing_required_fields [function]` (`1872caed-36e0-5803-8973-4ae9a4fc1e81`) lines 144-168 [crates/gwiki/src/research_loop/tests.rs:144-168]
  - Signature: `fn research_loop_deps_builder_reports_missing_required_fields() {`
  - Purpose: This function validates that `ResearchLoopDepsBuilder` correctly enforces `model` and `note_writer` as mandatory fields by asserting their absence raises the appropriate build errors. [crates/gwiki/src/research_loop/tests.rs:144-168]
- `model_budget_error_stops_as_budget_exhausted` (function) component `model_budget_error_stops_as_budget_exhausted [function]` (`c7a44012-f433-5299-9ea3-2dd3e24d97a9`) lines 171-200 [crates/gwiki/src/research_loop/tests.rs:171-200]
  - Signature: `fn model_budget_error_stops_as_budget_exhausted() {`
  - Purpose: This test verifies that a `ResearchLoop` terminates with `ResearchStopReason::BudgetExhausted` when the underlying `BudgetModel` exhausts its token allocation during query execution. [crates/gwiki/src/research_loop/tests.rs:171-200]
- `config` (function) component `config [function]` (`106ce7d0-abf8-546a-bdd2-eb877ce0fd2d`) lines 202-210 [crates/gwiki/src/research_loop/tests.rs:202-210]
  - Signature: `fn config() -> ResearchLoopConfig {`
  - Purpose: Returns a `ResearchLoopConfig` struct with hardcoded constraints: 12 max steps, 24,000 max tokens, 8 max sources, 900-second wall time limit, and 24,000-byte note size limit. [crates/gwiki/src/research_loop/tests.rs:202-210]
- `research_code_citations_flow_into_accepted_notes` (function) component `research_code_citations_flow_into_accepted_notes [function]` (`b739b691-6774-5c39-8db8-b3d87db5ad91`) lines 213-299 [crates/gwiki/src/research_loop/tests.rs:213-299]
  - Signature: `fn research_code_citations_flow_into_accepted_notes() {`
  - Purpose: Tests the integration of code search citations into research notes by verifying that code citations discovered during search are properly attached to notes when accepted by the research model in a simulated workflow. [crates/gwiki/src/research_loop/tests.rs:213-299]
- `CodeSearch` (class) component `CodeSearch [class]` (`8c3ec5a8-d751-5a12-bf0d-e14d34071699`) lines 214-214 [crates/gwiki/src/research_loop/tests.rs:214]
  - Signature: `struct CodeSearch;`
  - Purpose: `CodeSearch` is a forward-declared struct with no visible implementation details in the provided source code. [crates/gwiki/src/research_loop/tests.rs:214]
- `CodeSearch` (class) component `CodeSearch [class]` (`19160217-b7cb-5f88-a0f8-249de8d2f6ad`) lines 216-234 [crates/gwiki/src/research_loop/tests.rs:216-234]
  - Signature: `impl WikiSearch for CodeSearch {`
  - Purpose: CodeSearch implements the WikiSearch trait with a stub search method that ignores query parameters and returns a hardcoded ResearchObservation containing a single code citation to line 12 of src/handler.rs. [crates/gwiki/src/research_loop/tests.rs:216-234]
- `CodeSearch.search` (method) component `CodeSearch.search [method]` (`2035e60b-0b97-5219-897c-18e6eac473cb`) lines 217-233 [crates/gwiki/src/research_loop/tests.rs:217-233]
  - Signature: `fn search(`
  - Purpose: The method constructs and returns a hardcoded `ResearchObservation` containing a single code citation from `src/handler.rs` line 12, disregarding the provided `_query` and `_limit` parameters. [crates/gwiki/src/research_loop/tests.rs:217-233]
- `research_code_model_off_returns_retrieval_only_scaffold` (function) component `research_code_model_off_returns_retrieval_only_scaffold [function]` (`c51135d7-0605-5286-aebe-9f9987e44780`) lines 302-363 [crates/gwiki/src/research_loop/tests.rs:302-363]
  - Signature: `fn research_code_model_off_returns_retrieval_only_scaffold() {`
  - Purpose: This function tests that a ResearchLoop with an unavailable AI model can still retrieve and return code citations and source candidates, verifying graceful degradation to retrieval-only functionality. [crates/gwiki/src/research_loop/tests.rs:302-363]
- `ScaffoldSearch` (class) component `ScaffoldSearch [class]` (`2b356d02-2e24-55b9-907d-e733ccf4a85f`) lines 303-303 [crates/gwiki/src/research_loop/tests.rs:303]
  - Signature: `struct ScaffoldSearch;`
  - Purpose: ScaffoldSearch is a unit struct (zero-sized type) with no visible fields or methods in the provided declaration. [crates/gwiki/src/research_loop/tests.rs:303]
- `ScaffoldSearch` (class) component `ScaffoldSearch [class]` (`32aa93e1-0288-5b60-a6c9-5822333ffa77`) lines 305-323 [crates/gwiki/src/research_loop/tests.rs:305-323]
  - Signature: `impl WikiSearch for ScaffoldSearch {`
  - Purpose: ScaffoldSearch is a stub implementation of the WikiSearch trait that ignores input parameters and returns a hardcoded ResearchObservation with a single code citation to handler.rs for testing or scaffolding purposes. [crates/gwiki/src/research_loop/tests.rs:305-323]
- `ScaffoldSearch.search` (method) component `ScaffoldSearch.search [method]` (`db87db05-afc8-582d-990a-5b466ec73efc`) lines 306-322 [crates/gwiki/src/research_loop/tests.rs:306-322]
  - Signature: `fn search(`
  - Purpose: This method returns a hard-coded `ResearchObservation` with a single source from `src/handler.rs`'s `handle` function, ignoring the query and limit parameters. [crates/gwiki/src/research_loop/tests.rs:306-322]
- `research_code_graph_off_keeps_docs_only_degradation_on_notes` (function) component `research_code_graph_off_keeps_docs_only_degradation_on_notes [function]` (`d25e2d85-1245-562e-9d65-33d021ee603f`) lines 366-444 [crates/gwiki/src/research_loop/tests.rs:366-444]
  - Signature: `fn research_code_graph_off_keeps_docs_only_degradation_on_notes() {`
  - Purpose: Tests a research loop that generates notes from documentation-only searches while recording the unavailable code graph as a degradation annotation. [crates/gwiki/src/research_loop/tests.rs:366-444]
- `DocsOnlySearch` (class) component `DocsOnlySearch [class]` (`1023b11b-0203-5014-947a-a0c597d2a7e9`) lines 367-367 [crates/gwiki/src/research_loop/tests.rs:367]
  - Signature: `struct DocsOnlySearch;`
  - Purpose: DocsOnlySearch is a zero-sized marker struct type, likely used to configure or restrict search operations to documentation only. [crates/gwiki/src/research_loop/tests.rs:367]
- `DocsOnlySearch` (class) component `DocsOnlySearch [class]` (`e9750b24-cea5-501c-a4de-5a942eb36102`) lines 369-379 [crates/gwiki/src/research_loop/tests.rs:369-379]
  - Signature: `impl WikiSearch for DocsOnlySearch {`
  - Purpose: DocsOnlySearch is a WikiSearch trait implementation that returns a hardcoded single documentation result while ignoring query parameters and reporting the shared code graph as unavailable. [crates/gwiki/src/research_loop/tests.rs:369-379]
- `DocsOnlySearch.search` (method) component `DocsOnlySearch.search [method]` (`d943d02e-f007-5f87-91f5-d7a75d104550`) lines 370-378 [crates/gwiki/src/research_loop/tests.rs:370-378]
  - Signature: `fn search(`
  - Purpose: Unconditionally returns a hardcoded `ResearchObservation` reporting a single document hit from `raw/source.md` with a `shared_code_graph_unavailable` degradation, ignoring the query and limit parameters. [crates/gwiki/src/research_loop/tests.rs:370-378]
- `model_planned_note_is_written_after_source_is_observed` (function) component `model_planned_note_is_written_after_source_is_observed [function]` (`b1de196c-7253-5f73-867e-62645df2cc68`) lines 447-503 [crates/gwiki/src/research_loop/tests.rs:447-503]
  - Signature: `fn model_planned_note_is_written_after_source_is_observed() {`
  - Purpose: Verifies that a ResearchLoop correctly includes source file references in notes accepted by the model after those sources are observed during execution. [crates/gwiki/src/research_loop/tests.rs:447-503]
- `write_conflict_stops_the_run_without_recording_the_note` (function) component `write_conflict_stops_the_run_without_recording_the_note [function]` (`6a519a8c-977f-5548-b811-a4c2dfc83ccb`) lines 506-561 [crates/gwiki/src/research_loop/tests.rs:506-561]
  - Signature: `fn write_conflict_stops_the_run_without_recording_the_note() {`
  - Purpose: This test verifies that when a write conflict occurs during ResearchLoop execution, the run halts with `WriteConflict` stop reason and neither accepts nor records notes to the filesystem. [crates/gwiki/src/research_loop/tests.rs:506-561]
- `accepted_note_without_observed_source_is_blocked` (function) component `accepted_note_without_observed_source_is_blocked [function]` (`d2f0aa86-55b9-5724-8674-278f915ccaf6`) lines 564-601 [crates/gwiki/src/research_loop/tests.rs:564-601]
  - Signature: `fn accepted_note_without_observed_source_is_blocked() {`
  - Purpose: Tests that the ResearchLoop blocks acceptance of notes referencing non-existent sources and halts execution with a SourceBlocked stop reason. [crates/gwiki/src/research_loop/tests.rs:564-601]
- `parses_fenced_json_action` (function) component `parses_fenced_json_action [function]` (`18aa5282-ebee-51bd-a569-f12a92744ccf`) lines 604-614 [crates/gwiki/src/research_loop/tests.rs:604-614]
  - Signature: `fn parses_fenced_json_action() {`
  - Purpose: This test verifies that `parse_model_action` correctly parses markdown-fenced JSON containing a finish action into a `ResearchAction::Finish` enum variant with the extracted reason field. [crates/gwiki/src/research_loop/tests.rs:604-614]
- `parses_action_with_trailing_model_prose` (function) component `parses_action_with_trailing_model_prose [function]` (`d978539f-baba-53a1-a593-84d1186246c0`) lines 617-628 [crates/gwiki/src/research_loop/tests.rs:617-628]
  - Signature: `fn parses_action_with_trailing_model_prose() {`
  - Purpose: Tests that `parse_model_action` correctly parses a JSON action object even when followed by trailing prose text. [crates/gwiki/src/research_loop/tests.rs:617-628]
- `parses_action_with_trailing_prose_containing_braces` (function) component `parses_action_with_trailing_prose_containing_braces [function]` (`84012a09-0fa6-5896-8ff0-6b43aab113d1`) lines 631-642 [crates/gwiki/src/research_loop/tests.rs:631-642]
  - Signature: `fn parses_action_with_trailing_prose_containing_braces() {`
  - Purpose: Tests that `parse_model_action` correctly extracts the first complete JSON action object from prose text containing additional braced content. [crates/gwiki/src/research_loop/tests.rs:631-642]
- `parses_fenced_action_with_text_after_closing_fence` (function) component `parses_fenced_action_with_text_after_closing_fence [function]` (`f9857900-1a90-5d26-9e63-c2ea4ef63188`) lines 645-656 [crates/gwiki/src/research_loop/tests.rs:645-656]
  - Signature: `fn parses_fenced_action_with_text_after_closing_fence() {`
  - Purpose: This test verifies that `parse_model_action` correctly extracts and parses a JSON-fenced action block while ignoring text that appears after the closing fence delimiter. [crates/gwiki/src/research_loop/tests.rs:645-656]
- `rejects_response_without_json_object` (function) component `rejects_response_without_json_object [function]` (`3b63087c-f341-5d5d-affc-10340d6ac676`) lines 659-662 [crates/gwiki/src/research_loop/tests.rs:659-662]
  - Signature: `fn rejects_response_without_json_object() {`
  - Purpose: This test function verifies that `parse_model_action` rejects input strings without a JSON object and returns an error containing the message "did not include a JSON object". [crates/gwiki/src/research_loop/tests.rs:659-662]
- `rejects_malformed_json_object` (function) component `rejects_malformed_json_object [function]` (`2254fc00-5a6b-5659-b918-17f6e2700072`) lines 665-668 [crates/gwiki/src/research_loop/tests.rs:665-668]
  - Signature: `fn rejects_malformed_json_object() {`
  - Purpose: This unit test verifies that `parse_model_action` correctly rejects malformed JSON input (with a missing value for the "reason" key) and produces an error message containing "failed to parse action JSON". [crates/gwiki/src/research_loop/tests.rs:665-668]
- `file_url_source_references_use_path_scope_validation` (function) component `file_url_source_references_use_path_scope_validation [function]` (`ad08bc8c-cbbc-56cd-b278-1d29f938ac48`) lines 671-688 [crates/gwiki/src/research_loop/tests.rs:671-688]
  - Signature: `fn file_url_source_references_use_path_scope_validation() {`
  - Purpose: Tests that `validate_source_reference` properly enforces path scope validation by accepting file URLs within the wiki root directory and rejecting those outside it with an "outside the wiki scope" error. [crates/gwiki/src/research_loop/tests.rs:671-688]
- `source_reference_rejects_relative_symlink_escape` (function) component `source_reference_rejects_relative_symlink_escape [function]` (`4356b79a-2866-56e4-9f8e-99902720f371`) lines 692-706 [crates/gwiki/src/research_loop/tests.rs:692-706]
  - Signature: `fn source_reference_rejects_relative_symlink_escape() {`
  - Purpose: Tests that `validate_source_reference` correctly rejects relative symlink paths that point outside the wiki root directory scope. [crates/gwiki/src/research_loop/tests.rs:692-706]

