---
title: crates/gwiki/src/ingest/url.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/url.rs
  ranges:
  - 25-31
  - 34-38
  - 41-45
  - 48-51
  - 54-60
  - 62-64
  - 68-77
  - 79-113
  - 115-148
  - 150-163
  - 165-170
  - 172-211
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/url.rs:25-31](crates/gwiki/src/ingest/url.rs#L25-L31), [crates/gwiki/src/ingest/url.rs:34-38](crates/gwiki/src/ingest/url.rs#L34-L38), [crates/gwiki/src/ingest/url.rs:41-45](crates/gwiki/src/ingest/url.rs#L41-L45), [crates/gwiki/src/ingest/url.rs:48-51](crates/gwiki/src/ingest/url.rs#L48-L51), [crates/gwiki/src/ingest/url.rs:54-60](crates/gwiki/src/ingest/url.rs#L54-L60), [crates/gwiki/src/ingest/url.rs:62-64](crates/gwiki/src/ingest/url.rs#L62-L64), [crates/gwiki/src/ingest/url.rs:68-77](crates/gwiki/src/ingest/url.rs#L68-L77), [crates/gwiki/src/ingest/url.rs:79-113](crates/gwiki/src/ingest/url.rs#L79-L113), [crates/gwiki/src/ingest/url.rs:115-148](crates/gwiki/src/ingest/url.rs#L115-L148), [crates/gwiki/src/ingest/url.rs:150-163](crates/gwiki/src/ingest/url.rs#L150-L163), [crates/gwiki/src/ingest/url.rs:165-170](crates/gwiki/src/ingest/url.rs#L165-L170), [crates/gwiki/src/ingest/url.rs:172-211](crates/gwiki/src/ingest/url.rs#L172-L211)

</details>

# crates/gwiki/src/ingest/url.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides URL-ingest plumbing for gwiki: it models a fetched `UrlSnapshot`, records accepted and failed ingest outcomes in `UrlBatchIngest`, and exposes status/exit-code helpers for batch reporting. The ingest functions then take a snapshot or set of URLs, detect whether the response is HTML or not, render the appropriate markdown, write raw content and assets into the vault, and optionally run index updates after ingest; the fetcher-based path wraps URL retrieval before handing snapshots into the same ingest flow.
[crates/gwiki/src/ingest/url.rs:25-31]
[crates/gwiki/src/ingest/url.rs:34-38]
[crates/gwiki/src/ingest/url.rs:41-45]
[crates/gwiki/src/ingest/url.rs:48-51]
[crates/gwiki/src/ingest/url.rs:54-60]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `UrlSnapshot` | class | `pub struct UrlSnapshot {` | `UrlSnapshot [class]` | `c14b8f0a-a77a-503a-9bb9-4353724c9db4` | 25-31 [crates/gwiki/src/ingest/url.rs:25-31] | Indexed class `UrlSnapshot` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:25-31] |
| `AcceptedUrlIngest` | class | `pub struct AcceptedUrlIngest {` | `AcceptedUrlIngest [class]` | `10b5ab90-399b-564d-a071-16987e705a84` | 34-38 [crates/gwiki/src/ingest/url.rs:34-38] | Indexed class `AcceptedUrlIngest` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:34-38] |
| `UrlIngestFailure` | class | `pub struct UrlIngestFailure {` | `UrlIngestFailure [class]` | `e1a888d5-5ecc-50f0-8c6b-a2edc46ac72f` | 41-45 [crates/gwiki/src/ingest/url.rs:41-45] | Indexed class `UrlIngestFailure` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:41-45] |
| `UrlBatchIngest` | class | `pub struct UrlBatchIngest {` | `UrlBatchIngest [class]` | `c301d5b8-188c-50a5-acbc-40f22d82cba4` | 48-51 [crates/gwiki/src/ingest/url.rs:48-51] | Indexed class `UrlBatchIngest` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:48-51] |
| `UrlBatchIngest::status` | method | `pub fn status(&self) -> &'static str {` | `UrlBatchIngest::status [method]` | `0cc24868-fd0f-555a-b5cf-895a77c56d02` | 54-60 [crates/gwiki/src/ingest/url.rs:54-60] | Indexed method `UrlBatchIngest::status` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:54-60] |
| `UrlBatchIngest::exit_code` | method | `pub fn exit_code(&self) -> u8 {` | `UrlBatchIngest::exit_code [method]` | `2e635155-f4db-5502-9348-7e6cdca94939` | 62-64 [crates/gwiki/src/ingest/url.rs:62-64] | Indexed method `UrlBatchIngest::exit_code` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:62-64] |
| `ingest_snapshot` | function | `pub fn ingest_snapshot(` | `ingest_snapshot [function]` | `c056c1c8-97f3-5779-9a83-3d2e3dda80a0` | 68-77 [crates/gwiki/src/ingest/url.rs:68-77] | Indexed function `ingest_snapshot` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:68-77] |
| `ingest_snapshot_without_index` | function | `pub(crate) fn ingest_snapshot_without_index(` | `ingest_snapshot_without_index [function]` | `a4f1949d-4667-5f9f-9af6-cf853e1476ca` | 79-113 [crates/gwiki/src/ingest/url.rs:79-113] | Indexed function `ingest_snapshot_without_index` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:79-113] |
| `ingest_non_html_snapshot_without_index` | function | `fn ingest_non_html_snapshot_without_index(` | `ingest_non_html_snapshot_without_index [function]` | `c4a98887-d879-58d7-81a6-9d70911c19b3` | 115-148 [crates/gwiki/src/ingest/url.rs:115-148] | Indexed function `ingest_non_html_snapshot_without_index` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:115-148] |
| `ingest_urls` | function | `pub(crate) fn ingest_urls(` | `ingest_urls [function]` | `62953a1c-8373-5ac7-a984-4be6c048f349` | 150-163 [crates/gwiki/src/ingest/url.rs:150-163] | Indexed function `ingest_urls` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:150-163] |
| `fetch_url_snapshot` | function | `pub(crate) fn fetch_url_snapshot(` | `fetch_url_snapshot [function]` | `4c565554-84f8-5b2e-90f6-3ee1cce5914f` | 165-170 [crates/gwiki/src/ingest/url.rs:165-170] | Indexed function `fetch_url_snapshot` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:165-170] |
| `ingest_urls_with_fetcher` | function | `pub(crate) fn ingest_urls_with_fetcher(` | `ingest_urls_with_fetcher [function]` | `ab220337-f2ba-54b8-9c30-7018ddfa681b` | 172-211 [crates/gwiki/src/ingest/url.rs:172-211] | Indexed function `ingest_urls_with_fetcher` in `crates/gwiki/src/ingest/url.rs`. [crates/gwiki/src/ingest/url.rs:172-211] |
