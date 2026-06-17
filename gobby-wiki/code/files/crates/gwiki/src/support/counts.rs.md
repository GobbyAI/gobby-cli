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
  - 45-53
  - 56-72
  - 79-85
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/counts.rs:4-10](crates/gwiki/src/support/counts.rs#L4-L10), [crates/gwiki/src/support/counts.rs:12-20](crates/gwiki/src/support/counts.rs#L12-L20), [crates/gwiki/src/support/counts.rs:22-33](crates/gwiki/src/support/counts.rs#L22-L33), [crates/gwiki/src/support/counts.rs:36-42](crates/gwiki/src/support/counts.rs#L36-L42), [crates/gwiki/src/support/counts.rs:45-53](crates/gwiki/src/support/counts.rs#L45-L53), [crates/gwiki/src/support/counts.rs:56-72](crates/gwiki/src/support/counts.rs#L56-L72), [crates/gwiki/src/support/counts.rs:79-85](crates/gwiki/src/support/counts.rs#L79-L85)

</details>

# crates/gwiki/src/support/counts.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines a small count-reporting helper for gwiki indexes. `IndexCounts` groups row totals for documents, chunks, links, sources, and ingestions, and `index_counts` computes those totals directly from the in-memory store. `postgres_index_counts` computes the same structure from PostgreSQL for a given search scope by calling `postgres_count` on each logical table. `GwikiTable` provides the fixed table-name mapping used by the SQL helper, and the test locks those identifiers down so the count queries stay pointed at the expected tables.
[crates/gwiki/src/support/counts.rs:4-10]
[crates/gwiki/src/support/counts.rs:12-20]
[crates/gwiki/src/support/counts.rs:22-33]
[crates/gwiki/src/support/counts.rs:36-42]
[crates/gwiki/src/support/counts.rs:45-53]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IndexCounts` | class | `pub(crate) struct IndexCounts {` | `IndexCounts [class]` | `656f145d-38f1-5e5f-8d2f-3e5b9e20e1e1` | 4-10 [crates/gwiki/src/support/counts.rs:4-10] | Indexed class `IndexCounts` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:4-10] |
| `index_counts` | function | `pub(crate) fn index_counts(store: &store::MemoryWikiStore) -> IndexCounts {` | `index_counts [function]` | `fc6bcd38-24d5-5898-abd8-f7cccb038630` | 12-20 [crates/gwiki/src/support/counts.rs:12-20] | Indexed function `index_counts` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:12-20] |
| `postgres_index_counts` | function | `pub(crate) fn postgres_index_counts(` | `postgres_index_counts [function]` | `b479c64e-4fae-51b0-92fe-d60f7c9f9d94` | 22-33 [crates/gwiki/src/support/counts.rs:22-33] | Indexed function `postgres_index_counts` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:22-33] |
| `GwikiTable` | type | `enum GwikiTable {` | `GwikiTable [type]` | `95bb5c54-adbf-5876-a1e5-d79aac9a09ba` | 36-42 [crates/gwiki/src/support/counts.rs:36-42] | Indexed type `GwikiTable` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:36-42] |
| `GwikiTable::as_identifier` | method | `fn as_identifier(self) -> &'static str {` | `GwikiTable::as_identifier [method]` | `dbfc88fd-48d8-53db-864a-51902f6844ea` | 45-53 [crates/gwiki/src/support/counts.rs:45-53] | Indexed method `GwikiTable::as_identifier` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:45-53] |
| `postgres_count` | function | `fn postgres_count(` | `postgres_count [function]` | `92643004-1821-5f95-a129-821545208e0d` | 56-72 [crates/gwiki/src/support/counts.rs:56-72] | Indexed function `postgres_count` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:56-72] |
| `gwiki_table_identifiers_are_fixed` | function | `fn gwiki_table_identifiers_are_fixed() {` | `gwiki_table_identifiers_are_fixed [function]` | `c79499c8-39f6-5d27-85e5-9ec608e58c4a` | 79-85 [crates/gwiki/src/support/counts.rs:79-85] | Indexed function `gwiki_table_identifiers_are_fixed` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:79-85] |
