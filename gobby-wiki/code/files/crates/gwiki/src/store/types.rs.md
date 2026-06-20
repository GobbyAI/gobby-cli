---
title: crates/gwiki/src/store/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store/types.rs

Module: [[code/modules/crates/gwiki/src/store|crates/gwiki/src/store]]

## Overview

`crates/gwiki/src/store/types.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gwiki/src/store/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiDocumentKind` | type | Indexed type `WikiDocumentKind` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:8-14] |
| `WikiDocument` | class | 'WikiDocument' is a data structure representing a wiki page or document, storing its filesystem path, document kind, optional title, content hash, and raw body text. [crates/gwiki/src/store/types.rs:17-23] |
| `WikiChunk` | class | 'WikiChunk' is a data structure representing a contiguous wiki text segment identified by source 'path', 'chunk_index', and byte range ('byte_start' to 'byte_end'), with optional 'heading' metadata and the chunk’s 'content' payload. [crates/gwiki/src/store/types.rs:26-33] |
| `WikiLink` | class | 'WikiLink' is a parsed wiki-style link record containing the destination 'PathBuf', the resolved target string, an optional display alias, and the byte-range span ('byte_start' to 'byte_end') of the link in the source text. [crates/gwiki/src/store/types.rs:36-42] |
| `WikiSource` | class | 'WikiSource' is a data holder for a wiki document source, storing the source file path, the resolved document path, the document kind, and a content hash for change detection or identity. [crates/gwiki/src/store/types.rs:45-50] |
| `WikiIngestionEvent` | type | Indexed type `WikiIngestionEvent` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:53-59] |
| `WikiIngestion` | class | 'WikiIngestion' is a data container for a wiki ingestion item, holding the source 'path', the associated 'WikiIngestionEvent', and an optional 'content_hash' for deduplication or change detection. [crates/gwiki/src/store/types.rs:62-66] |
| `WikiStoreScope` | class | 'WikiStoreScope' is a thin wrapper struct that encapsulates a single 'WikiScope' value in its 'scope' field. [crates/gwiki/src/store/types.rs:69-71] |
| `WikiStoreScope::project` | method | Constructs and returns a 'Self' value whose 'scope' is set to 'WikiScope::Project' with 'project_id' converted from the provided 'Into<String>' argument. [crates/gwiki/src/store/types.rs:74-80] |
| `WikiStoreScope::topic` | method | Constructs and returns a 'Self' value whose 'scope' is set to 'WikiScope::Topic' with 'name' initialized from 'topic_name.into()'. [crates/gwiki/src/store/types.rs:82-88] |
| `WikiStoreScope::scope_kind` | method | Returns the string slice produced by 'self.scope.kind()', exposing the underlying scope’s kind. [crates/gwiki/src/store/types.rs:90-92] |
| `WikiStoreScope::scope_id` | method | Returns the current scope’s identity string as a '&str' by delegating to 'self.scope.identity()'. [crates/gwiki/src/store/types.rs:94-96] |
| `WikiStoreScope::project_id` | method | Returns the current scope’s project ID as an owned 'String', or 'None' if the scope has no project ID. [crates/gwiki/src/store/types.rs:98-100] |
| `WikiStoreScope::topic_name` | method | Returns an owned 'Option<String>' by delegating to 'self.scope.topic_name()' and converting any borrowed topic name into an owned 'String' with 'ToOwned::to_owned'. [crates/gwiki/src/store/types.rs:102-104] |
| `StoreError` | type | Indexed type `StoreError` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:108-114] |
| `StoreError::fmt` | method | Formats 'StoreError' as a human-readable message, emitting 'invalid {field}: {message}' for 'InvalidData' variants and 'PostgreSQL wiki index write failed: {message}' for 'Postgres' variants. [crates/gwiki/src/store/types.rs:117-126] |
| `StoreError::from` | method | Converts a 'postgres::Error' into 'StoreError::Postgres' by extracting the underlying 'DbError' string when available, otherwise falling back to 'error.to_string()'. [crates/gwiki/src/store/types.rs:132-140] |
| `WikiIndexStore` | type | Indexed type `WikiIndexStore` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:143-152] |

