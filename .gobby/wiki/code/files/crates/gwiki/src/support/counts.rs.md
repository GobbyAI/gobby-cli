---
title: crates/gwiki/src/support/counts.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/counts.rs
  ranges:
  - 4-10
  - 12-20
  - 22-33
  - 36-42
  - 44-54
  - 56-72
  - 79-85
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/counts.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

This file provides count aggregation for Gwiki index data, in both in-memory and PostgreSQL-backed forms. `IndexCounts` is the shared struct for document, chunk, link, source, and ingestion totals; `index_counts` derives those totals from `MemoryWikiStore`, while `postgres_index_counts` gathers the same counts from PostgreSQL by calling `postgres_count` for each table. `GwikiTable` and its `as_identifier` mapping keep the SQL table names fixed and centralized, and the test verifies those identifiers stay aligned with the expected `gwiki_*` tables.
[crates/gwiki/src/support/counts.rs:4-10]
[crates/gwiki/src/support/counts.rs:12-20]
[crates/gwiki/src/support/counts.rs:22-33]
[crates/gwiki/src/support/counts.rs:36-42]
[crates/gwiki/src/support/counts.rs:44-54]

## API Symbols

- `IndexCounts` (class) component `IndexCounts [class]` (`656f145d-38f1-5e5f-8d2f-3e5b9e20e1e1`) lines 4-10 [crates/gwiki/src/support/counts.rs:4-10]
  - Signature: `pub(crate) struct IndexCounts {`
  - Purpose: 'IndexCounts' is an internal Rust struct that aggregates five 'usize' counters for indexed 'documents', 'chunks', 'links', 'sources', and 'ingestions'. [crates/gwiki/src/support/counts.rs:4-10]
- `index_counts` (function) component `index_counts [function]` (`fc6bcd38-24d5-5898-abd8-f7cccb038630`) lines 12-20 [crates/gwiki/src/support/counts.rs:12-20]
  - Signature: `pub(crate) fn index_counts(store: &store::MemoryWikiStore) -> IndexCounts {`
  - Purpose: Returns an 'IndexCounts' aggregate populated from a 'MemoryWikiStore' by counting documents, total chunk entries across all chunk vectors, total link entries across all link vectors, sources, and ingestions. [crates/gwiki/src/support/counts.rs:12-20]
- `postgres_index_counts` (function) component `postgres_index_counts [function]` (`b479c64e-4fae-51b0-92fe-d60f7c9f9d94`) lines 22-33 [crates/gwiki/src/support/counts.rs:22-33]
  - Signature: `pub(crate) fn postgres_index_counts(`
  - Purpose: Queries the given PostgreSQL client for scoped row counts across the 'Documents', 'Chunks', 'Links', 'Sources', and 'Ingestions' tables and returns them assembled into an 'IndexCounts' struct. [crates/gwiki/src/support/counts.rs:22-33]
- `GwikiTable` (type) component `GwikiTable [type]` (`95bb5c54-adbf-5876-a1e5-d79aac9a09ba`) lines 36-42 [crates/gwiki/src/support/counts.rs:36-42]
  - Signature: `enum GwikiTable {`
  - Purpose: Indexed type `GwikiTable` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:36-42]
- `GwikiTable` (class) component `GwikiTable [class]` (`d9074934-27e8-51a1-87d0-41b9ed0a7b34`) lines 44-54 [crates/gwiki/src/support/counts.rs:44-54]
  - Signature: `impl GwikiTable {`
  - Purpose: 'GwikiTable' is an enum-like type whose 'as_identifier' method maps each variant ('Documents', 'Chunks', 'Links', 'Sources', 'Ingestions') to its corresponding static database table name string. [crates/gwiki/src/support/counts.rs:44-54]
- `GwikiTable.as_identifier` (method) component `GwikiTable.as_identifier [method]` (`dbfc88fd-48d8-53db-864a-51902f6844ea`) lines 45-53 [crates/gwiki/src/support/counts.rs:45-53]
  - Signature: `fn as_identifier(self) -> &'static str {`
  - Purpose: Returns the static string identifier corresponding to the enum variant, mapping 'Documents', 'Chunks', 'Links', 'Sources', and 'Ingestions' to their respective 'gwiki_*' table names. [crates/gwiki/src/support/counts.rs:45-53]
- `postgres_count` (function) component `postgres_count [function]` (`92643004-1821-5f95-a129-821545208e0d`) lines 56-72 [crates/gwiki/src/support/counts.rs:56-72]
  - Signature: `fn postgres_count(`
  - Purpose: Counts rows in the specified PostgreSQL 'GwikiTable' matching 'scope_kind' and 'scope_id', returning the result as 'usize' and mapping query or 'i64'-to-'usize' conversion failures to 'WikiError::Config'. [crates/gwiki/src/support/counts.rs:56-72]
- `gwiki_table_identifiers_are_fixed` (function) component `gwiki_table_identifiers_are_fixed [function]` (`c79499c8-39f6-5d27-85e5-9ec608e58c4a`) lines 79-85 [crates/gwiki/src/support/counts.rs:79-85]
  - Signature: `fn gwiki_table_identifiers_are_fixed() {`
  - Purpose: Verifies that each 'GwikiTable' enum variant returns its expected fixed string identifier: 'gwiki_documents', 'gwiki_chunks', 'gwiki_links', 'gwiki_sources', and 'gwiki_ingestions'. [crates/gwiki/src/support/counts.rs:79-85]

