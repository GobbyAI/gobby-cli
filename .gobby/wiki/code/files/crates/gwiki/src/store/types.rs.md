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
  - 73-105
  - 108-114
  - 116-127
  - '129'
  - 131-141
  - 143-152
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store/types.rs

Module: [[code/modules/crates/gwiki/src/store|crates/gwiki/src/store]]

## Purpose

This file defines the store-layer data model for wiki ingestion and indexing: document, chunk, link, source, and ingestion event records, plus a `WikiDocumentKind` enum that classifies document types. It also wraps `WikiScope` in `WikiStoreScope` to construct project/topic scopes and expose their kind, identity, and derived IDs, and it defines `StoreError` for formatting/conversion plus a `WikiIndexStore` type used by the store.
[crates/gwiki/src/store/types.rs:8-14]
[crates/gwiki/src/store/types.rs:17-23]
[crates/gwiki/src/store/types.rs:26-33]
[crates/gwiki/src/store/types.rs:36-42]
[crates/gwiki/src/store/types.rs:45-50]

## API Symbols

- `WikiDocumentKind` (type) component `WikiDocumentKind [type]` (`a9a513a7-38be-532d-969c-7734cc2a7324`) lines 8-14 [crates/gwiki/src/store/types.rs:8-14]
  - Signature: `pub enum WikiDocumentKind {`
  - Purpose: Indexed type `WikiDocumentKind` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:8-14]
- `WikiDocument` (class) component `WikiDocument [class]` (`a4d1991b-d7d7-501b-bc91-920e1feb59a6`) lines 17-23 [crates/gwiki/src/store/types.rs:17-23]
  - Signature: `pub struct WikiDocument {`
  - Purpose: Indexed class `WikiDocument` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:17-23]
- `WikiChunk` (class) component `WikiChunk [class]` (`274a3f7b-3f5a-5a5d-b7cb-d994d281f66e`) lines 26-33 [crates/gwiki/src/store/types.rs:26-33]
  - Signature: `pub struct WikiChunk {`
  - Purpose: Indexed class `WikiChunk` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:26-33]
- `WikiLink` (class) component `WikiLink [class]` (`ccc3f0fd-75d0-5e46-97b9-0a57087c15ae`) lines 36-42 [crates/gwiki/src/store/types.rs:36-42]
  - Signature: `pub struct WikiLink {`
  - Purpose: Indexed class `WikiLink` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:36-42]
- `WikiSource` (class) component `WikiSource [class]` (`0993e308-6704-5b8b-8bea-647c2c415753`) lines 45-50 [crates/gwiki/src/store/types.rs:45-50]
  - Signature: `pub struct WikiSource {`
  - Purpose: Indexed class `WikiSource` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:45-50]
- `WikiIngestionEvent` (type) component `WikiIngestionEvent [type]` (`adf6b959-071e-5f08-8fae-f4e9117eefdb`) lines 53-59 [crates/gwiki/src/store/types.rs:53-59]
  - Signature: `pub enum WikiIngestionEvent {`
  - Purpose: Indexed type `WikiIngestionEvent` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:53-59]
- `WikiIngestion` (class) component `WikiIngestion [class]` (`0b0d8aa5-e3fa-5814-a9ab-3d11fee13862`) lines 62-66 [crates/gwiki/src/store/types.rs:62-66]
  - Signature: `pub struct WikiIngestion {`
  - Purpose: Indexed class `WikiIngestion` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:62-66]
- `WikiStoreScope` (class) component `WikiStoreScope [class]` (`d3e1fa5b-1625-5ea1-b25b-5638cd5ebae9`) lines 69-71 [crates/gwiki/src/store/types.rs:69-71]
  - Signature: `pub struct WikiStoreScope {`
  - Purpose: Indexed class `WikiStoreScope` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:69-71]
- `WikiStoreScope` (class) component `WikiStoreScope [class]` (`ca3a95e7-421b-519b-9c3e-e1391cfbd3d9`) lines 73-105 [crates/gwiki/src/store/types.rs:73-105]
  - Signature: `impl WikiStoreScope {`
  - Purpose: Indexed class `WikiStoreScope` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:73-105]
- `WikiStoreScope.project` (method) component `WikiStoreScope.project [method]` (`1489fd1b-aebf-5c55-ae43-cfb71b333e9a`) lines 74-80 [crates/gwiki/src/store/types.rs:74-80]
  - Signature: `pub fn project(project_id: impl Into<String>) -> Self {`
  - Purpose: Indexed method `WikiStoreScope.project` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:74-80]
- `WikiStoreScope.topic` (method) component `WikiStoreScope.topic [method]` (`2f96cf4e-37fb-5afa-8f78-f47c53194737`) lines 82-88 [crates/gwiki/src/store/types.rs:82-88]
  - Signature: `pub fn topic(topic_name: impl Into<String>) -> Self {`
  - Purpose: Indexed method `WikiStoreScope.topic` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:82-88]
- `WikiStoreScope.scope_kind` (method) component `WikiStoreScope.scope_kind [method]` (`752989fa-3377-5b80-8918-e63f084c4314`) lines 90-92 [crates/gwiki/src/store/types.rs:90-92]
  - Signature: `pub fn scope_kind(&self) -> &str {`
  - Purpose: Indexed method `WikiStoreScope.scope_kind` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:90-92]
- `WikiStoreScope.scope_id` (method) component `WikiStoreScope.scope_id [method]` (`9af54b62-a10e-532d-8a48-d4f5e421fa26`) lines 94-96 [crates/gwiki/src/store/types.rs:94-96]
  - Signature: `pub fn scope_id(&self) -> &str {`
  - Purpose: Indexed method `WikiStoreScope.scope_id` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:94-96]
- `WikiStoreScope.project_id` (method) component `WikiStoreScope.project_id [method]` (`6940abd7-4c1b-5b2b-84af-f59915ba03e8`) lines 98-100 [crates/gwiki/src/store/types.rs:98-100]
  - Signature: `pub(super) fn project_id(&self) -> Option<String> {`
  - Purpose: Indexed method `WikiStoreScope.project_id` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:98-100]
- `WikiStoreScope.topic_name` (method) component `WikiStoreScope.topic_name [method]` (`931bde35-e7af-5485-9f25-9bc6a5d2ca1f`) lines 102-104 [crates/gwiki/src/store/types.rs:102-104]
  - Signature: `pub(super) fn topic_name(&self) -> Option<String> {`
  - Purpose: Indexed method `WikiStoreScope.topic_name` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:102-104]
- `StoreError` (type) component `StoreError [type]` (`fe011066-9b74-5b71-80c4-0b30af29fa4f`) lines 108-114 [crates/gwiki/src/store/types.rs:108-114]
  - Signature: `pub enum StoreError {`
  - Purpose: Indexed type `StoreError` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:108-114]
- `StoreError` (class) component `StoreError [class]` (`91a61636-dd30-5a42-89a1-476fa68cb1a6`) lines 116-127 [crates/gwiki/src/store/types.rs:116-127]
  - Signature: `impl fmt::Display for StoreError {`
  - Purpose: Indexed class `StoreError` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:116-127]
- `StoreError.fmt` (method) component `StoreError.fmt [method]` (`4df97852-9bdc-51a8-8227-d9e65ca165b7`) lines 117-126 [crates/gwiki/src/store/types.rs:117-126]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Indexed method `StoreError.fmt` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:117-126]
- `StoreError` (class) component `StoreError [class]` (`afae1730-dc70-52f8-8ec1-f236f8460068`) lines 129-129 [crates/gwiki/src/store/types.rs:129]
  - Signature: `impl std::error::Error for StoreError {}`
  - Purpose: Indexed class `StoreError` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:129]
- `StoreError` (class) component `StoreError [class]` (`e4c789e1-8fca-546c-8c87-6272fe3941db`) lines 131-141 [crates/gwiki/src/store/types.rs:131-141]
  - Signature: `impl From<postgres::Error> for StoreError {`
  - Purpose: Indexed class `StoreError` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:131-141]
- `StoreError.from` (method) component `StoreError.from [method]` (`104a272f-e79d-5469-baf6-7c986eda0c59`) lines 132-140 [crates/gwiki/src/store/types.rs:132-140]
  - Signature: `fn from(error: postgres::Error) -> Self {`
  - Purpose: Indexed method `StoreError.from` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:132-140]
- `WikiIndexStore` (type) component `WikiIndexStore [type]` (`a35a23c5-eace-5743-a594-87e0732a1e58`) lines 143-152 [crates/gwiki/src/store/types.rs:143-152]
  - Signature: `pub trait WikiIndexStore {`
  - Purpose: Indexed type `WikiIndexStore` in `crates/gwiki/src/store/types.rs`. [crates/gwiki/src/store/types.rs:143-152]

