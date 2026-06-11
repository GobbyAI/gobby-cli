---
title: crates/gwiki/src/research/model.rs
type: code_file
provenance:
- file: crates/gwiki/src/research/model.rs
  ranges:
  - 21-24
  - 26-33
  - 27-32
  - 35-97
  - 36-96
  - 99-101
  - 103-114
  - 104-113
  - 116-118
  - 120-136
  - 121-135
  - 138-159
  - 161-163
  - 165-173
  - 166-172
  - 175-177
  - 179-209
  - 180-188
  - 190-208
  - 211-214
  - 217-224
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
[crates/gwiki/src/research/model.rs:35-97]
[crates/gwiki/src/research/model.rs:36-96]

## API Symbols

- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`caf20e91-0840-562e-ac35-5058d3ecad26`) lines 21-24 [crates/gwiki/src/research/model.rs:21-24]
  - Signature: `pub(crate) struct GcoreResearchModel {`
  - Purpose: Indexed class `GcoreResearchModel` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:21-24]
- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`7b6646f4-1914-51e3-9377-2fa387936279`) lines 26-33 [crates/gwiki/src/research/model.rs:26-33]
  - Signature: `impl GcoreResearchModel {`
  - Purpose: Indexed class `GcoreResearchModel` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:26-33]
- `GcoreResearchModel.ai_unavailable` (method) component `GcoreResearchModel.ai_unavailable [method]` (`18f3ae85-60d6-590f-b07e-8fae11641408`) lines 27-32 [crates/gwiki/src/research/model.rs:27-32]
  - Signature: `fn ai_unavailable<T>(&self, message: String) -> Result<T, ResearchModelError> {`
  - Purpose: Indexed method `GcoreResearchModel.ai_unavailable` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:27-32]
- `GcoreResearchModel` (class) component `GcoreResearchModel [class]` (`32d9f475-2599-5454-acdc-0ced8e80fb47`) lines 35-97 [crates/gwiki/src/research/model.rs:35-97]
  - Signature: `impl ResearchModel for GcoreResearchModel {`
  - Purpose: Indexed class `GcoreResearchModel` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:35-97]
- `GcoreResearchModel.next_action` (method) component `GcoreResearchModel.next_action [method]` (`68c822f1-60d4-50a5-95ee-6c55eb050e06`) lines 36-96 [crates/gwiki/src/research/model.rs:36-96]
  - Signature: `fn next_action(`
  - Purpose: Indexed method `GcoreResearchModel.next_action` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:36-96]
- `CommandAsk` (class) component `CommandAsk [class]` (`199b4f61-404e-58e0-aaf7-5356e327614a`) lines 99-101 [crates/gwiki/src/research/model.rs:99-101]
  - Signature: `pub(crate) struct CommandAsk {`
  - Purpose: Indexed class `CommandAsk` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:99-101]
- `CommandAsk` (class) component `CommandAsk [class]` (`0defc143-92d3-5788-9a41-f52505179033`) lines 103-114 [crates/gwiki/src/research/model.rs:103-114]
  - Signature: `impl WikiAsk for CommandAsk {`
  - Purpose: Indexed class `CommandAsk` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:103-114]
- `CommandAsk.ask` (method) component `CommandAsk.ask [method]` (`87c4bed1-54f6-5402-ac2b-112b1914829f`) lines 104-113 [crates/gwiki/src/research/model.rs:104-113]
  - Signature: `fn ask(&mut self, query: &str) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Indexed method `CommandAsk.ask` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:104-113]
- `CommandSearch` (class) component `CommandSearch [class]` (`c96a0610-77a5-5e6f-83d8-439e8b658321`) lines 116-118 [crates/gwiki/src/research/model.rs:116-118]
  - Signature: `pub(crate) struct CommandSearch {`
  - Purpose: Indexed class `CommandSearch` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:116-118]
- `CommandSearch` (class) component `CommandSearch [class]` (`a4b282bf-7aae-570e-8f3a-ac0aeb4c61e5`) lines 120-136 [crates/gwiki/src/research/model.rs:120-136]
  - Signature: `impl WikiSearch for CommandSearch {`
  - Purpose: Indexed class `CommandSearch` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:120-136]
- `CommandSearch.search` (method) component `CommandSearch.search [method]` (`c498040b-70d6-57c7-83c5-a372b5507b37`) lines 121-135 [crates/gwiki/src/research/model.rs:121-135]
  - Signature: `fn search(&mut self, query: &str, limit: usize) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Indexed method `CommandSearch.search` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:121-135]
- `code_citations_from_search_results` (function) component `code_citations_from_search_results [function]` (`5e55ab52-3d18-55c1-b0a4-f56a0f93992b`) lines 138-159 [crates/gwiki/src/research/model.rs:138-159]
  - Signature: `fn code_citations_from_search_results(`
  - Purpose: Indexed function `code_citations_from_search_results` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:138-159]
- `CommandRead` (class) component `CommandRead [class]` (`7449352a-be6e-5d21-9804-2a84fda20333`) lines 161-163 [crates/gwiki/src/research/model.rs:161-163]
  - Signature: `pub(crate) struct CommandRead {`
  - Purpose: Indexed class `CommandRead` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:161-163]
- `CommandRead` (class) component `CommandRead [class]` (`eee82d72-1823-53a7-8122-b6e1619e2ca6`) lines 165-173 [crates/gwiki/src/research/model.rs:165-173]
  - Signature: `impl WikiRead for CommandRead {`
  - Purpose: Indexed class `CommandRead` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:165-173]
- `CommandRead.read` (method) component `CommandRead.read [method]` (`95cd6f85-56de-5680-ba28-8eaa55ded995`) lines 166-172 [crates/gwiki/src/research/model.rs:166-172]
  - Signature: `fn read(&mut self, path: &Path) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Indexed method `CommandRead.read` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:166-172]
- `CommandIngestor` (class) component `CommandIngestor [class]` (`be752102-45ba-5295-a0d0-e21f5aec7fed`) lines 175-177 [crates/gwiki/src/research/model.rs:175-177]
  - Signature: `pub(crate) struct CommandIngestor {`
  - Purpose: Indexed class `CommandIngestor` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:175-177]
- `CommandIngestor` (class) component `CommandIngestor [class]` (`a75a4611-2fb4-5351-881e-3107c055d273`) lines 179-209 [crates/gwiki/src/research/model.rs:179-209]
  - Signature: `impl SourceIngestor for CommandIngestor {`
  - Purpose: Indexed class `CommandIngestor` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:179-209]
- `CommandIngestor.ingest_url` (method) component `CommandIngestor.ingest_url [method]` (`880f0466-2bb2-5dfe-b251-5726e300b837`) lines 180-188 [crates/gwiki/src/research/model.rs:180-188]
  - Signature: `fn ingest_url(&mut self, url: &str) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Indexed method `CommandIngestor.ingest_url` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:180-188]
- `CommandIngestor.ingest_file` (method) component `CommandIngestor.ingest_file [method]` (`baaa9fd9-3842-5ee8-b697-0b8de264cdcf`) lines 190-208 [crates/gwiki/src/research/model.rs:190-208]
  - Signature: `fn ingest_file(&mut self, path: &Path) -> Result<ResearchObservation, WikiError> {`
  - Purpose: Indexed method `CommandIngestor.ingest_file` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:190-208]
- `AcceptedNoteWriter` (class) component `AcceptedNoteWriter [class]` (`3a10eb86-4960-506b-b4bd-c440f8e3ee81`) lines 211-214 [crates/gwiki/src/research/model.rs:211-214]
  - Signature: `pub(crate) struct AcceptedNoteWriter<'a> {`
  - Purpose: Indexed class `AcceptedNoteWriter` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:211-214]
- `write_note` (function) component `write_note [function]` (`f3dcb3c1-b82d-5e32-aa7f-f5aa7125381f`) lines 217-224 [crates/gwiki/src/research/model.rs:217-224]
  - Signature: `fn write_note(&mut self, note: &AcceptedNoteDraft) -> Result<NoteWriteOutcome, WikiError> {`
  - Purpose: Indexed function `write_note` in `crates/gwiki/src/research/model.rs`. [crates/gwiki/src/research/model.rs:217-224]

