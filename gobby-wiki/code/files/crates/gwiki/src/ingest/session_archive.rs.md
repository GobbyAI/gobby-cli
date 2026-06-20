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

`crates/gwiki/src/ingest/session_archive.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AcceptedSessionArchive` | class | The 'AcceptedSessionArchive' struct is a crate-visible data structure that associates the file system path of an accepted session archive with its corresponding ingestion result. [crates/gwiki/src/ingest/session_archive.rs:16-19] |
| `SkippedSessionArchive` | class | The 'SkippedSessionArchive' struct is a crate-private data structure that represents a session archive bypassed during processing, storing its file system path, the hash of its contents, and the technical reason why it was skipped. [crates/gwiki/src/ingest/session_archive.rs:22-26] |
| `SessionArchiveFailure` | class | 'SessionArchiveFailure' is a crate-visible struct that represents a session archiving failure by encapsulating the target archive's path, an error code, and a descriptive error message. [crates/gwiki/src/ingest/session_archive.rs:29-33] |
| `SessionArchiveBatchIngest` | class | The 'SessionArchiveBatchIngest' struct represents the results and state of a batch session archive ingestion process from a specified directory, tracking the total number of scanned items alongside lists of accepted, skipped, and failed archives. [crates/gwiki/src/ingest/session_archive.rs:36-42] |
| `SessionArchiveBatchIngest::status` | method | This method returns a static string slice representing the ingestion status—"empty", "skipped", "ingested", "failed", or "partial"—by pattern matching a tuple of booleans indicating whether the accepted, skipped, and failed collections are empty, alongside whether the scanned count is zero. [crates/gwiki/src/ingest/session_archive.rs:45-58] |
| `SessionArchiveBatchIngest::exit_code` | method | The 'exit_code' method returns '1' if the collection of failed items is not empty and the collection of accepted items is empty, and '0' otherwise, by converting the boolean result of this conjunction to a 'u8' value. [crates/gwiki/src/ingest/session_archive.rs:60-62] |
| `sync_session_transcript_archives` | function | The function decompresses and ingests new session transcript archives from a specified directory into a vault up to an optional limit, filtering out previously ingested archives by comparing their content hashes against a source manifest. [crates/gwiki/src/ingest/session_archive.rs:65-145] |
| `session_archive_paths` | function | This function retrieves and returns a sorted vector of file paths matching the '.jsonl.gz' format from the specified archive directory, returning an empty vector if the directory does not exist or propagating I/O failures as a 'WikiError'. [crates/gwiki/src/ingest/session_archive.rs:147-173] |
| `is_jsonl_gz` | function | The function 'is_jsonl_gz' takes a reference to a 'Path' and returns 'true' if the path has a valid UTF-8 filename ending with the '.jsonl.gz' suffix, and 'false' otherwise. [crates/gwiki/src/ingest/session_archive.rs:175-179] |
| `read_gzipped_archive` | function | The function opens a file at the specified path, decompresses its gzip-encoded contents into a byte vector, and returns the vector while mapping I/O and decompression errors to a custom 'SessionArchiveFailure' type. [crates/gwiki/src/ingest/session_archive.rs:181-195] |
| `archive_file_name` | function | The 'archive_file_name' function extracts and returns the file name of a given 'Path' as a 'String', falling back to '"session.jsonl.gz"' if the path lacks a valid UTF-8 file name. [crates/gwiki/src/ingest/session_archive.rs:197-202] |
| `SessionArchiveFailure::new` | method | The 'new' constructor instantiates and returns a new instance of the struct by converting the provided '&Path' reference into an owned 'PathBuf' and converting both the 'code' and 'message' arguments into owned 'String' values. [crates/gwiki/src/ingest/session_archive.rs:205-211] |
| `SessionArchiveFailure::from_wiki_error` | method | The 'from_wiki_error' method instantiates the implementing type by invoking its 'new' constructor with the provided file path reference, the error code from the given 'WikiError', and the error's string representation. [crates/gwiki/src/ingest/session_archive.rs:213-215] |
| `write_archive` | function | The 'write_archive' function creates a file at the specified path and writes the provided byte slice to it as a Gzip-compressed archive using default compression. [crates/gwiki/src/ingest/session_archive.rs:360-365] |
| `indexed_store_text` | function | This function concatenates the body of every document and the content of every chunk in a 'MemoryWikiStore' into a single, newline-separated string. [crates/gwiki/src/ingest/session_archive.rs:367-380] |

_Verified by 4 in-file unit tests._

