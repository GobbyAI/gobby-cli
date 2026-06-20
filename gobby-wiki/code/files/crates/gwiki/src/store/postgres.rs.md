---
title: crates/gwiki/src/store/postgres.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/postgres.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store/postgres.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/store/postgres.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gwiki/src/store/postgres.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DocumentMeta` | class | 'DocumentMeta' is a struct that stores a document identifier, a source-kind label, and a content hash as 'String' fields. [crates/gwiki/src/store/postgres.rs:18-22] |
| `PostgresWikiStore` | class | 'PostgresWikiStore<'a>' is a mutable PostgreSQL-backed wiki store that holds a borrowed 'postgres::Client', a 'WikiStoreScope', and a 'BTreeMap<PathBuf, DocumentMeta>' indexing document metadata by path. [crates/gwiki/src/store/postgres.rs:24-28] |
| `new` | function | Constructs a new instance by storing the provided mutable 'postgres::Client' reference and 'WikiStoreScope', and initializing 'documents' as an empty 'BTreeMap'. [crates/gwiki/src/store/postgres.rs:31-37] |
| `scope_params` | function | Returns a tuple containing the scope kind and scope ID as 'String's, followed by the optional project ID and topic name from 'self.scope'. [crates/gwiki/src/store/postgres.rs:39-46] |
| `document_meta` | function | Returns a cached 'DocumentMeta' for 'path' if present, otherwise looks up the document row in 'gwiki_documents' for the current scope, builds 'DocumentMeta' from 'id', 'source_kind', and 'content_hash', caches it by path, and errors with 'StoreError::InvalidData' if no indexed document exists. [crates/gwiki/src/store/postgres.rs:48-75] |
| `indexed_hashes` | function | Returns a 'BTreeMap' of document paths to content hashes for the current scope by querying 'gwiki_documents' for 'path' and 'content_hash' rows and converting each stored display path back into a 'PathBuf'. [crates/gwiki/src/store/postgres.rs:79-95] |
| `upsert_document` | function | 'upsert_document' computes a scoped document ID and JSONB provenance/frontmatter metadata, then inserts the 'WikiDocument' into 'gwiki_documents' or, on '(scope_kind, scope_id, path)' conflict, updates the existing row’s identifiers, metadata, body, and timestamps ('indexed_at'/'updated_at'). [crates/gwiki/src/store/postgres.rs:97-153] |
| `replace_chunks` | function | Replaces all stored wiki chunks for a given 'path' by validating the new chunks, deleting existing rows for that scoped path in a transaction, and then inserting the provided chunks with checked 'chunk_index' conversion, committing only if the replacement succeeds. [crates/gwiki/src/store/postgres.rs:155-251] |
| `replace_links` | function | Replaces all wiki-link records for the given 'path' within the current scope by validating the links, deleting existing rows in 'gwiki_links' for that path, and upserting each new link in a transaction, with rollback on any database error. [crates/gwiki/src/store/postgres.rs:253-322] |
| `upsert_source` | function | Upserts a 'WikiSource' into 'gwiki_sources' for the current scope by inserting or updating the row keyed on '(scope_kind, scope_id, document_path)', recomputing the scoped 'id' and metadata fields ('path', 'document_path', 'source_kind', 'content_hash', 'frontmatter', 'provenance'), and refreshing 'captured_at' to 'NOW()'. [crates/gwiki/src/store/postgres.rs:324-368] |
| `record_ingestion` | function | Records a wiki ingestion event by deriving a scoped ingestion ID and metadata from the current scope and document state, then upserting a corresponding row into 'gwiki_ingestions' with the event status, content hash, provenance, and timestamp. [crates/gwiki/src/store/postgres.rs:370-415] |
| `record_file_hash` | function | No-ops and returns 'Ok(())', ignoring the provided path and content hash because PostgreSQL persists file hashes via 'upsert_document' on 'gwiki_documents' instead. [crates/gwiki/src/store/postgres.rs:417-424] |
| `delete_derived_rows` | function | Deletes all derived database rows for the given document path within the current scope by running a transaction that removes matching records from 'gwiki_chunks', 'gwiki_links', 'gwiki_sources', and 'gwiki_documents', then updates the in-memory 'documents' cache and commits. [crates/gwiki/src/store/postgres.rs:426-451] |

