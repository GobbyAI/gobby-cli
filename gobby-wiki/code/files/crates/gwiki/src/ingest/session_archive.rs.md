---
title: crates/gwiki/src/ingest/session_archive.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session_archive.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session_archive.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session_archive.rs` exposes 19 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session_archive.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AcceptedSessionArchive` | class | Indexed class `AcceptedSessionArchive` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:16-19] |
| `SkippedSessionArchive` | class | Indexed class `SkippedSessionArchive` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:22-26] |
| `SessionArchiveFailure` | class | Indexed class `SessionArchiveFailure` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:29-33] |
| `SessionArchiveBatchIngest` | class | Indexed class `SessionArchiveBatchIngest` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:36-42] |
| `SessionArchiveBatchIngest::status` | method | Indexed method `SessionArchiveBatchIngest::status` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:45-58] |
| `SessionArchiveBatchIngest::exit_code` | method | Indexed method `SessionArchiveBatchIngest::exit_code` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:60-62] |
| `sync_session_transcript_archives` | function | Indexed function `sync_session_transcript_archives` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:65-145] |
| `session_archive_paths` | function | Indexed function `session_archive_paths` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:147-173] |
| `is_jsonl_gz` | function | Indexed function `is_jsonl_gz` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:175-179] |
| `read_gzipped_archive` | function | Indexed function `read_gzipped_archive` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:181-195] |
| `archive_file_name` | function | Indexed function `archive_file_name` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:197-202] |
| `SessionArchiveFailure::new` | method | Indexed method `SessionArchiveFailure::new` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:205-211] |
| `SessionArchiveFailure::from_wiki_error` | method | Indexed method `SessionArchiveFailure::from_wiki_error` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:213-215] |
| `sync_session_archives_ingests_gzip_and_indexes_once` | function | Indexed function `sync_session_archives_ingests_gzip_and_indexes_once` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:229-269] |
| `sync_session_archives_treats_missing_archive_dir_as_empty` | function | Indexed function `sync_session_archives_treats_missing_archive_dir_as_empty` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:272-290] |
| `sync_session_archives_skips_previously_ingested_hashes` | function | Indexed function `sync_session_archives_skips_previously_ingested_hashes` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:293-330] |
| `sync_session_archives_reports_bad_gzip_without_blocking_good_archives` | function | Indexed function `sync_session_archives_reports_bad_gzip_without_blocking_good_archives` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:333-358] |
| `write_archive` | function | Indexed function `write_archive` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:360-365] |
| `indexed_store_text` | function | Indexed function `indexed_store_text` in `crates/gwiki/src/ingest/session_archive.rs`. [crates/gwiki/src/ingest/session_archive.rs:367-380] |

