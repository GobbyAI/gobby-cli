---
title: crates/gwiki/src/store/memory.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/memory.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store/memory.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/store/memory.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/store/memory.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `MemoryWikiStore` | class | 'MemoryWikiStore' is an in-memory wiki persistence state container that indexes documents, chunks, links, sources, file hashes, and ingestion/deletion records by 'PathBuf' while tracking upsert and replacement counters. [crates/gwiki/src/store/memory.rs:16-28] |
| `MemoryWikiStore::indexed_hashes` | method | Returns a clone of 'self.file_hashes' as a 'BTreeMap<PathBuf, String>' wrapped in 'Ok', without performing any additional computation or mutation. [crates/gwiki/src/store/memory.rs:31-33] |
| `MemoryWikiStore::upsert_document` | method | Increments the document-upsert counter, inserts the 'WikiDocument' into 'self.documents' keyed by its cloned 'path', and returns 'Ok(())' without performing any validation or deduplication beyond map insertion semantics. [crates/gwiki/src/store/memory.rs:35-39] |
| `MemoryWikiStore::replace_chunks` | method | Validates that all 'chunks' belong to 'path', increments the replacement counter, and atomically replaces the stored chunk vector for that path in 'self.chunks', returning 'Ok(())' on success. [crates/gwiki/src/store/memory.rs:41-46] |
| `MemoryWikiStore::replace_links` | method | Validates that all provided wiki link targets are consistent with 'path', increments the link-replacement counter, and atomically replaces the stored links for 'path' with the supplied 'Vec<WikiLink>'. [crates/gwiki/src/store/memory.rs:48-53] |
| `MemoryWikiStore::upsert_source` | method | Increments the 'source_upserts' counter, inserts the given 'WikiSource' into 'self.sources' keyed by its cloned 'document_path', and returns 'Ok(())'. [crates/gwiki/src/store/memory.rs:55-59] |
| `MemoryWikiStore::record_ingestion` | method | Appends the provided 'WikiIngestion' to 'self.ingestions' and returns 'Ok(())' without performing any validation or additional processing. [crates/gwiki/src/store/memory.rs:61-64] |
| `MemoryWikiStore::record_file_hash` | method | Inserts the given 'path' → 'content_hash' pair into 'self.file_hashes' and returns 'Ok(())' without performing any validation or additional logic. [crates/gwiki/src/store/memory.rs:66-69] |
| `MemoryWikiStore::delete_derived_rows` | method | Removes all derived data associated with 'path' from the 'documents', 'chunks', 'links', 'sources', and 'file_hashes' maps, records the path in 'deleted_paths', and returns 'Ok(())'. [crates/gwiki/src/store/memory.rs:71-80] |

