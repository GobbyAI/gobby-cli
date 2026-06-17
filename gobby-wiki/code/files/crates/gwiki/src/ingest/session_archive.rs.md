---
title: crates/gwiki/src/ingest/session_archive.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session_archive.rs
  ranges:
  - 16-19
  - 22-26
  - 29-33
  - 36-42
  - 45-58
  - 60-62
  - 65-145
  - 147-173
  - 175-179
  - 181-195
  - 197-202
  - 205-211
  - 213-215
  - 229-269
  - 272-290
  - 293-330
  - 333-358
  - 360-365
  - 367-380
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session_archive.rs:16-19](crates/gwiki/src/ingest/session_archive.rs#L16-L19), [crates/gwiki/src/ingest/session_archive.rs:22-26](crates/gwiki/src/ingest/session_archive.rs#L22-L26), [crates/gwiki/src/ingest/session_archive.rs:29-33](crates/gwiki/src/ingest/session_archive.rs#L29-L33), [crates/gwiki/src/ingest/session_archive.rs:36-42](crates/gwiki/src/ingest/session_archive.rs#L36-L42), [crates/gwiki/src/ingest/session_archive.rs:45-58](crates/gwiki/src/ingest/session_archive.rs#L45-L58), [crates/gwiki/src/ingest/session_archive.rs:60-62](crates/gwiki/src/ingest/session_archive.rs#L60-L62), [crates/gwiki/src/ingest/session_archive.rs:65-145](crates/gwiki/src/ingest/session_archive.rs#L65-L145), [crates/gwiki/src/ingest/session_archive.rs:147-173](crates/gwiki/src/ingest/session_archive.rs#L147-L173), [crates/gwiki/src/ingest/session_archive.rs:175-179](crates/gwiki/src/ingest/session_archive.rs#L175-L179), [crates/gwiki/src/ingest/session_archive.rs:181-195](crates/gwiki/src/ingest/session_archive.rs#L181-L195), [crates/gwiki/src/ingest/session_archive.rs:197-202](crates/gwiki/src/ingest/session_archive.rs#L197-L202), [crates/gwiki/src/ingest/session_archive.rs:205-211](crates/gwiki/src/ingest/session_archive.rs#L205-L211), [crates/gwiki/src/ingest/session_archive.rs:213-215](crates/gwiki/src/ingest/session_archive.rs#L213-L215), [crates/gwiki/src/ingest/session_archive.rs:229-269](crates/gwiki/src/ingest/session_archive.rs#L229-L269), [crates/gwiki/src/ingest/session_archive.rs:272-290](crates/gwiki/src/ingest/session_archive.rs#L272-L290), [crates/gwiki/src/ingest/session_archive.rs:293-330](crates/gwiki/src/ingest/session_archive.rs#L293-L330), [crates/gwiki/src/ingest/session_archive.rs:333-358](crates/gwiki/src/ingest/session_archive.rs#L333-L358), [crates/gwiki/src/ingest/session_archive.rs:360-365](crates/gwiki/src/ingest/session_archive.rs#L360-L365), [crates/gwiki/src/ingest/session_archive.rs:367-380](crates/gwiki/src/ingest/session_archive.rs#L367-L380)

</details>

# crates/gwiki/src/ingest/session_archive.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file manages batch ingestion of session transcript archives from a directory into the wiki index. It defines result records for accepted, skipped, and failed archives, then wraps them in `SessionArchiveBatchIngest`, which summarizes the run with a coarse `status()` and `exit_code()`. The main entry point, `sync_session_transcript_archives`, gathers archive paths, validates input like `limit`, reads gzipped JSONL archives, ingests each session file without indexing, and then indexes successful ingests through the store. Helper functions support path discovery, gzip detection and reading, archive naming, and converting ingestion errors into structured failures.
[crates/gwiki/src/ingest/session_archive.rs:16-19]
[crates/gwiki/src/ingest/session_archive.rs:22-26]
[crates/gwiki/src/ingest/session_archive.rs:29-33]
[crates/gwiki/src/ingest/session_archive.rs:36-42]
[crates/gwiki/src/ingest/session_archive.rs:45-58]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `AcceptedSessionArchive` | class | `pub(crate) struct AcceptedSessionArchive {` | `AcceptedSessionArchive [class]` | `6aa53191-8a13-575b-b3de-654b76ac6fda` | 16-19 [crates/gwiki/src/ingest/session_archive.rs:16-19] | Indexed class `AcceptedSessionArchive` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:16-19] |
| `SkippedSessionArchive` | class | `pub(crate) struct SkippedSessionArchive {` | `SkippedSessionArchive [class]` | `dcf2398b-7682-5a44-b461-b8cc74f23636` | 22-26 [crates/gwiki/src/ingest/session_archive.rs:22-26] | Indexed class `SkippedSessionArchive` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:22-26] |
| `SessionArchiveFailure` | class | `pub(crate) struct SessionArchiveFailure {` | `SessionArchiveFailure [class]` | `a122e6fd-5e35-5f2c-9b13-f2b14dd9dba7` | 29-33 [crates/gwiki/src/ingest/session_archive.rs:29-33] | Indexed class `SessionArchiveFailure` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:29-33] |
| `SessionArchiveBatchIngest` | class | `pub(crate) struct SessionArchiveBatchIngest {` | `SessionArchiveBatchIngest [class]` | `496a7aaa-b6ad-5e3e-9976-1462bfd51c84` | 36-42 [crates/gwiki/src/ingest/session_archive.rs:36-42] | Indexed class `SessionArchiveBatchIngest` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:36-42] |
| `SessionArchiveBatchIngest::status` | method | `pub(crate) fn status(&self) -> &'static str {` | `SessionArchiveBatchIngest::status [method]` | `5808bed8-be63-5987-a780-c01191016b15` | 45-58 [crates/gwiki/src/ingest/session_archive.rs:45-58] | Indexed method `SessionArchiveBatchIngest::status` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:45-58] |
| `SessionArchiveBatchIngest::exit_code` | method | `pub(crate) fn exit_code(&self) -> u8 {` | `SessionArchiveBatchIngest::exit_code [method]` | `222f79ac-8144-554e-a550-d4b89046dbac` | 60-62 [crates/gwiki/src/ingest/session_archive.rs:60-62] | Indexed method `SessionArchiveBatchIngest::exit_code` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:60-62] |
| `sync_session_transcript_archives` | function | `pub(crate) fn sync_session_transcript_archives(` | `sync_session_transcript_archives [function]` | `9af90cb1-e8f0-574a-ba60-f5c417d6d662` | 65-145 [crates/gwiki/src/ingest/session_archive.rs:65-145] | Indexed function `sync_session_transcript_archives` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:65-145] |
| `session_archive_paths` | function | `fn session_archive_paths(archive_dir: &Path) -> Result<Vec<PathBuf>, WikiError> {` | `session_archive_paths [function]` | `5291c4be-a3e1-58db-9085-83a5a6d70273` | 147-173 [crates/gwiki/src/ingest/session_archive.rs:147-173] | Indexed function `session_archive_paths` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:147-173] |
| `is_jsonl_gz` | function | `fn is_jsonl_gz(path: &Path) -> bool {` | `is_jsonl_gz [function]` | `54dcec58-fd26-5623-ab22-164191f6eb6d` | 175-179 [crates/gwiki/src/ingest/session_archive.rs:175-179] | Indexed function `is_jsonl_gz` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:175-179] |
| `read_gzipped_archive` | function | `fn read_gzipped_archive(path: &Path) -> Result<Vec<u8>, SessionArchiveFailure> {` | `read_gzipped_archive [function]` | `7c8f94c1-dcc2-56cb-a9c9-05fde6da9a23` | 181-195 [crates/gwiki/src/ingest/session_archive.rs:181-195] | Indexed function `read_gzipped_archive` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:181-195] |
| `archive_file_name` | function | `fn archive_file_name(path: &Path) -> String {` | `archive_file_name [function]` | `23e1ac93-d0f7-5a1f-8267-5a2a505b0bb0` | 197-202 [crates/gwiki/src/ingest/session_archive.rs:197-202] | Indexed function `archive_file_name` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:197-202] |
| `SessionArchiveFailure::new` | method | `fn new(path: &Path, code: impl Into<String>, message: impl Into<String>) -> Self {` | `SessionArchiveFailure::new [method]` | `284436aa-3ad1-578b-8bd2-b7abcb0058ad` | 205-211 [crates/gwiki/src/ingest/session_archive.rs:205-211] | Indexed method `SessionArchiveFailure::new` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:205-211] |
| `SessionArchiveFailure::from_wiki_error` | method | `fn from_wiki_error(path: &Path, error: WikiError) -> Self {` | `SessionArchiveFailure::from_wiki_error [method]` | `05af5d1a-a291-5622-9e21-52a258b6648e` | 213-215 [crates/gwiki/src/ingest/session_archive.rs:213-215] | Indexed method `SessionArchiveFailure::from_wiki_error` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:213-215] |
| `sync_session_archives_ingests_gzip_and_indexes_once` | function | `fn sync_session_archives_ingests_gzip_and_indexes_once() {` | `sync_session_archives_ingests_gzip_and_indexes_once [function]` | `94cbf0ec-73db-5977-839d-0f47b7365c55` | 229-269 [crates/gwiki/src/ingest/session_archive.rs:229-269] | Indexed function `sync_session_archives_ingests_gzip_and_indexes_once` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:229-269] |
| `sync_session_archives_treats_missing_archive_dir_as_empty` | function | `fn sync_session_archives_treats_missing_archive_dir_as_empty() {` | `sync_session_archives_treats_missing_archive_dir_as_empty [function]` | `4438b0b3-b559-51d6-a135-a35427f50604` | 272-290 [crates/gwiki/src/ingest/session_archive.rs:272-290] | Indexed function `sync_session_archives_treats_missing_archive_dir_as_empty` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:272-290] |
| `sync_session_archives_skips_previously_ingested_hashes` | function | `fn sync_session_archives_skips_previously_ingested_hashes() {` | `sync_session_archives_skips_previously_ingested_hashes [function]` | `40d4a2dc-03c3-54d8-a4e6-eddf81dad5ce` | 293-330 [crates/gwiki/src/ingest/session_archive.rs:293-330] | Indexed function `sync_session_archives_skips_previously_ingested_hashes` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:293-330] |
| `sync_session_archives_reports_bad_gzip_without_blocking_good_archives` | function | `fn sync_session_archives_reports_bad_gzip_without_blocking_good_archives() {` | `sync_session_archives_reports_bad_gzip_without_blocking_good_archives [function]` | `fef8a5f8-94f7-5df0-8209-a518aa9afb2e` | 333-358 [crates/gwiki/src/ingest/session_archive.rs:333-358] | Indexed function `sync_session_archives_reports_bad_gzip_without_blocking_good_archives` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:333-358] |
| `write_archive` | function | `fn write_archive(path: &Path, bytes: &[u8]) {` | `write_archive [function]` | `14fdadfc-b5f4-514d-bfdb-ffeea2ad7825` | 360-365 [crates/gwiki/src/ingest/session_archive.rs:360-365] | Indexed function `write_archive` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:360-365] |
| `indexed_store_text` | function | `fn indexed_store_text(store: &MemoryWikiStore) -> String {` | `indexed_store_text [function]` | `c7317fe7-0151-578b-ae4a-bb7c5e6c6350` | 367-380 [crates/gwiki/src/ingest/session_archive.rs:367-380] | Indexed function `indexed_store_text` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:367-380] |
