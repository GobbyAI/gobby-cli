---
title: crates/gwiki/src/store/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/types.rs
  ranges:
  - 8-14
  - 17-23
  - 26-33
  - 36-42
  - 45-50
  - 53-59
  - 62-66
  - 69-71
  - 74-80
  - 82-88
  - 90-92
  - 94-96
  - 98-100
  - 102-104
  - 108-114
  - 117-126
  - 132-140
  - 143-152
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/store/types.rs:8-14](crates/gwiki/src/store/types.rs#L8-L14), [crates/gwiki/src/store/types.rs:17-23](crates/gwiki/src/store/types.rs#L17-L23), [crates/gwiki/src/store/types.rs:26-33](crates/gwiki/src/store/types.rs#L26-L33), [crates/gwiki/src/store/types.rs:36-42](crates/gwiki/src/store/types.rs#L36-L42), [crates/gwiki/src/store/types.rs:45-50](crates/gwiki/src/store/types.rs#L45-L50), [crates/gwiki/src/store/types.rs:53-59](crates/gwiki/src/store/types.rs#L53-L59), [crates/gwiki/src/store/types.rs:62-66](crates/gwiki/src/store/types.rs#L62-L66), [crates/gwiki/src/store/types.rs:69-71](crates/gwiki/src/store/types.rs#L69-L71), [crates/gwiki/src/store/types.rs:74-80](crates/gwiki/src/store/types.rs#L74-L80), [crates/gwiki/src/store/types.rs:82-88](crates/gwiki/src/store/types.rs#L82-L88), [crates/gwiki/src/store/types.rs:90-92](crates/gwiki/src/store/types.rs#L90-L92), [crates/gwiki/src/store/types.rs:94-96](crates/gwiki/src/store/types.rs#L94-L96), [crates/gwiki/src/store/types.rs:98-100](crates/gwiki/src/store/types.rs#L98-L100), [crates/gwiki/src/store/types.rs:102-104](crates/gwiki/src/store/types.rs#L102-L104), [crates/gwiki/src/store/types.rs:108-114](crates/gwiki/src/store/types.rs#L108-L114), [crates/gwiki/src/store/types.rs:117-126](crates/gwiki/src/store/types.rs#L117-L126), [crates/gwiki/src/store/types.rs:132-140](crates/gwiki/src/store/types.rs#L132-L140), [crates/gwiki/src/store/types.rs:143-152](crates/gwiki/src/store/types.rs#L143-L152)

</details>

# crates/gwiki/src/store/types.rs

Module: [[code/modules/crates/gwiki/src/store|crates/gwiki/src/store]]

## Purpose

This file defines the core store-side data types for wiki indexing and ingestion: document, chunk, link, source, and ingestion event records, plus enums that classify document kinds and ingestion outcomes. It also wraps `WikiScope` in `WikiStoreScope` to construct and inspect project/topic scopes, and defines `StoreError` and `WikiIndexStore` as the error and index-store abstractions that tie the storage layer together.
[crates/gwiki/src/store/types.rs:8-14]
[crates/gwiki/src/store/types.rs:17-23]
[crates/gwiki/src/store/types.rs:26-33]
[crates/gwiki/src/store/types.rs:36-42]
[crates/gwiki/src/store/types.rs:45-50]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WikiDocumentKind` | type | `pub enum WikiDocumentKind {` | `WikiDocumentKind [type]` | `a9a513a7-38be-532d-969c-7734cc2a7324` | 8-14 [crates/gwiki/src/store/types.rs:8-14] | Indexed type `WikiDocumentKind` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:8-14] |
| `WikiDocument` | class | `pub struct WikiDocument {` | `WikiDocument [class]` | `a4d1991b-d7d7-501b-bc91-920e1feb59a6` | 17-23 [crates/gwiki/src/store/types.rs:17-23] | Indexed class `WikiDocument` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:17-23] |
| `WikiChunk` | class | `pub struct WikiChunk {` | `WikiChunk [class]` | `274a3f7b-3f5a-5a5d-b7cb-d994d281f66e` | 26-33 [crates/gwiki/src/store/types.rs:26-33] | Indexed class `WikiChunk` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:26-33] |
| `WikiLink` | class | `pub struct WikiLink {` | `WikiLink [class]` | `ccc3f0fd-75d0-5e46-97b9-0a57087c15ae` | 36-42 [crates/gwiki/src/store/types.rs:36-42] | Indexed class `WikiLink` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:36-42] |
| `WikiSource` | class | `pub struct WikiSource {` | `WikiSource [class]` | `0993e308-6704-5b8b-8bea-647c2c415753` | 45-50 [crates/gwiki/src/store/types.rs:45-50] | Indexed class `WikiSource` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:45-50] |
| `WikiIngestionEvent` | type | `pub enum WikiIngestionEvent {` | `WikiIngestionEvent [type]` | `adf6b959-071e-5f08-8fae-f4e9117eefdb` | 53-59 [crates/gwiki/src/store/types.rs:53-59] | Indexed type `WikiIngestionEvent` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:53-59] |
| `WikiIngestion` | class | `pub struct WikiIngestion {` | `WikiIngestion [class]` | `0b0d8aa5-e3fa-5814-a9ab-3d11fee13862` | 62-66 [crates/gwiki/src/store/types.rs:62-66] | Indexed class `WikiIngestion` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:62-66] |
| `WikiStoreScope` | class | `pub struct WikiStoreScope {` | `WikiStoreScope [class]` | `d3e1fa5b-1625-5ea1-b25b-5638cd5ebae9` | 69-71 [crates/gwiki/src/store/types.rs:69-71] | Indexed class `WikiStoreScope` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:69-71] |
| `WikiStoreScope::project` | method | `pub fn project(project_id: impl Into<String>) -> Self {` | `WikiStoreScope::project [method]` | `1489fd1b-aebf-5c55-ae43-cfb71b333e9a` | 74-80 [crates/gwiki/src/store/types.rs:74-80] | Indexed method `WikiStoreScope::project` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:74-80] |
| `WikiStoreScope::topic` | method | `pub fn topic(topic_name: impl Into<String>) -> Self {` | `WikiStoreScope::topic [method]` | `2f96cf4e-37fb-5afa-8f78-f47c53194737` | 82-88 [crates/gwiki/src/store/types.rs:82-88] | Indexed method `WikiStoreScope::topic` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:82-88] |
| `WikiStoreScope::scope_kind` | method | `pub fn scope_kind(&self) -> &str {` | `WikiStoreScope::scope_kind [method]` | `752989fa-3377-5b80-8918-e63f084c4314` | 90-92 [crates/gwiki/src/store/types.rs:90-92] | Indexed method `WikiStoreScope::scope_kind` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:90-92] |
| `WikiStoreScope::scope_id` | method | `pub fn scope_id(&self) -> &str {` | `WikiStoreScope::scope_id [method]` | `9af54b62-a10e-532d-8a48-d4f5e421fa26` | 94-96 [crates/gwiki/src/store/types.rs:94-96] | Indexed method `WikiStoreScope::scope_id` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:94-96] |
| `WikiStoreScope::project_id` | method | `pub(super) fn project_id(&self) -> Option<String> {` | `WikiStoreScope::project_id [method]` | `6940abd7-4c1b-5b2b-84af-f59915ba03e8` | 98-100 [crates/gwiki/src/store/types.rs:98-100] | Indexed method `WikiStoreScope::project_id` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:98-100] |
| `WikiStoreScope::topic_name` | method | `pub(super) fn topic_name(&self) -> Option<String> {` | `WikiStoreScope::topic_name [method]` | `931bde35-e7af-5485-9f25-9bc6a5d2ca1f` | 102-104 [crates/gwiki/src/store/types.rs:102-104] | Indexed method `WikiStoreScope::topic_name` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:102-104] |
| `StoreError` | type | `pub enum StoreError {` | `StoreError [type]` | `fe011066-9b74-5b71-80c4-0b30af29fa4f` | 108-114 [crates/gwiki/src/store/types.rs:108-114] | Indexed type `StoreError` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:108-114] |
| `StoreError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `StoreError::fmt [method]` | `4df97852-9bdc-51a8-8227-d9e65ca165b7` | 117-126 [crates/gwiki/src/store/types.rs:117-126] | Indexed method `StoreError::fmt` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:117-126] |
| `StoreError::from` | method | `fn from(error: postgres::Error) -> Self {` | `StoreError::from [method]` | `104a272f-e79d-5469-baf6-7c986eda0c59` | 132-140 [crates/gwiki/src/store/types.rs:132-140] | Indexed method `StoreError::from` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:132-140] |
| `WikiIndexStore` | type | `pub trait WikiIndexStore {` | `WikiIndexStore [type]` | `a35a23c5-eace-5743-a594-87e0732a1e58` | 143-152 [crates/gwiki/src/store/types.rs:143-152] | Indexed type `WikiIndexStore` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:143-152] |
