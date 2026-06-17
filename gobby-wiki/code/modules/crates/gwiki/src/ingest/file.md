---
title: crates/gwiki/src/ingest/file
type: code_module
provenance:
- file: crates/gwiki/src/ingest/file/degradation.rs
  ranges:
  - 4-11
  - 13-15
  - 18-22
  - 24-39
- file: crates/gwiki/src/ingest/file/dispatch.rs
  ranges:
  - 43-242
- file: crates/gwiki/src/ingest/file/generic.rs
  ranges:
  - 11-57
- file: crates/gwiki/src/ingest/file/render.rs
  ranges:
  - 6-51
- file: crates/gwiki/src/ingest/file/replay.rs
  ranges:
  - 8-32
- file: crates/gwiki/src/ingest/file/source.rs
  ranges:
  - 9-25
  - 27-41
  - 43-55
  - 57-63
- file: crates/gwiki/src/ingest/file/tests.rs
  ranges:
  - 13-22
  - 24-30
  - 33-49
  - 52-105
  - 108-130
  - 133-147
  - 150-190
  - 193-220
  - 223-246
  - 249-324
  - 327-365
  - 368-407
  - 410-451
  - 454-490
  - 493-531
  - 534-571
  - 574-612
  - 616-650
  - 654-680
  - 684-708
  - 712-736
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file/degradation.rs:4-11](crates/gwiki/src/ingest/file/degradation.rs#L4-L11), [crates/gwiki/src/ingest/file/degradation.rs:13-15](crates/gwiki/src/ingest/file/degradation.rs#L13-L15), [crates/gwiki/src/ingest/file/degradation.rs:18-22](crates/gwiki/src/ingest/file/degradation.rs#L18-L22), [crates/gwiki/src/ingest/file/degradation.rs:24-39](crates/gwiki/src/ingest/file/degradation.rs#L24-L39)
- [crates/gwiki/src/ingest/file/dispatch.rs:43-242](crates/gwiki/src/ingest/file/dispatch.rs#L43-L242)
- [crates/gwiki/src/ingest/file/generic.rs:11-57](crates/gwiki/src/ingest/file/generic.rs#L11-L57)
- [crates/gwiki/src/ingest/file/render.rs:6-51](crates/gwiki/src/ingest/file/render.rs#L6-L51)
- [crates/gwiki/src/ingest/file/replay.rs:8-32](crates/gwiki/src/ingest/file/replay.rs#L8-L32)
- [crates/gwiki/src/ingest/file/source.rs:9-25](crates/gwiki/src/ingest/file/source.rs#L9-L25), [crates/gwiki/src/ingest/file/source.rs:27-41](crates/gwiki/src/ingest/file/source.rs#L27-L41), [crates/gwiki/src/ingest/file/source.rs:43-55](crates/gwiki/src/ingest/file/source.rs#L43-L55), [crates/gwiki/src/ingest/file/source.rs:57-63](crates/gwiki/src/ingest/file/source.rs#L57-L63)
- [crates/gwiki/src/ingest/file/tests.rs:13-22](crates/gwiki/src/ingest/file/tests.rs#L13-L22), [crates/gwiki/src/ingest/file/tests.rs:24-30](crates/gwiki/src/ingest/file/tests.rs#L24-L30), [crates/gwiki/src/ingest/file/tests.rs:33-49](crates/gwiki/src/ingest/file/tests.rs#L33-L49), [crates/gwiki/src/ingest/file/tests.rs:52-105](crates/gwiki/src/ingest/file/tests.rs#L52-L105), [crates/gwiki/src/ingest/file/tests.rs:108-130](crates/gwiki/src/ingest/file/tests.rs#L108-L130), [crates/gwiki/src/ingest/file/tests.rs:133-147](crates/gwiki/src/ingest/file/tests.rs#L133-L147), [crates/gwiki/src/ingest/file/tests.rs:150-190](crates/gwiki/src/ingest/file/tests.rs#L150-L190), [crates/gwiki/src/ingest/file/tests.rs:193-220](crates/gwiki/src/ingest/file/tests.rs#L193-L220), [crates/gwiki/src/ingest/file/tests.rs:223-246](crates/gwiki/src/ingest/file/tests.rs#L223-L246), [crates/gwiki/src/ingest/file/tests.rs:249-324](crates/gwiki/src/ingest/file/tests.rs#L249-L324), [crates/gwiki/src/ingest/file/tests.rs:327-365](crates/gwiki/src/ingest/file/tests.rs#L327-L365), [crates/gwiki/src/ingest/file/tests.rs:368-407](crates/gwiki/src/ingest/file/tests.rs#L368-L407), [crates/gwiki/src/ingest/file/tests.rs:410-451](crates/gwiki/src/ingest/file/tests.rs#L410-L451), [crates/gwiki/src/ingest/file/tests.rs:454-490](crates/gwiki/src/ingest/file/tests.rs#L454-L490), [crates/gwiki/src/ingest/file/tests.rs:493-531](crates/gwiki/src/ingest/file/tests.rs#L493-L531), [crates/gwiki/src/ingest/file/tests.rs:534-571](crates/gwiki/src/ingest/file/tests.rs#L534-L571), [crates/gwiki/src/ingest/file/tests.rs:574-612](crates/gwiki/src/ingest/file/tests.rs#L574-L612), [crates/gwiki/src/ingest/file/tests.rs:616-650](crates/gwiki/src/ingest/file/tests.rs#L616-L650), [crates/gwiki/src/ingest/file/tests.rs:654-680](crates/gwiki/src/ingest/file/tests.rs#L654-L680), [crates/gwiki/src/ingest/file/tests.rs:684-708](crates/gwiki/src/ingest/file/tests.rs#L684-L708), [crates/gwiki/src/ingest/file/tests.rs:712-736](crates/gwiki/src/ingest/file/tests.rs#L712-L736)

</details>

# crates/gwiki/src/ingest/file

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

The `crates/gwiki/src/ingest/file` module coordinates the no-index ingestion pipeline of local files into the wiki store [crates/gwiki/src/ingest/file/dispatch.rs:43-242]. When a file path is ingested through `ingest_path_without_index`, the module uses `detect_source_kind` to map extensions to categorical `SourceKind` types [crates/gwiki/src/ingest/file/source.rs:9-25], calculates normalized source-relative locations with `source_location` [crates/gwiki/src/ingest/file/source.rs:27-41], and decides if the file should be kept inline or stored as an asset based on its type and size via `should_store_asset` [crates/gwiki/src/ingest/file/source.rs:43-55]. The dispatcher then routes the file to its format-specific specialized ingester (such as audio, image, video, session, document, or PDF) or falls back to generic file ingestion [crates/gwiki/src/ingest/file/dispatch.rs:43-242], which registers a source record and writes out a rendered Markdown representation [crates/gwiki/src/ingest/file/generic.rs:11-57, crates/gwiki/src/ingest/file/render.rs:6-51].

To finish ingestion, the dispatcher normalizes result metadata and tracks ingestion degradations (such as video, transcription, vision, or document extraction issues) by serializing them into standard type-prefixed strings . It collaborates with replay hookups via `attach_replay_metadata` to register a `SourceReplay` on the `SourceManifest` and sync the local result [crates/gwiki/src/ingest/file/replay.rs:8-32]. This comprehensive pipeline, including stdin support, canonicalization, and specialized media or document dispatch fallback strategies, is verified within the unit testing suite .

### Public API Symbols
| Symbol | Type | Description | Citation |
| --- | --- | --- | --- |
| `ingest_path_without_index` | Function | Dispatches and runs ingestion for local file paths | crates/gwiki/src/ingest/file/dispatch.rs:43-242 |
| `detect_source_kind` | Function | Maps file extensions to categorical source kinds | crates/gwiki/src/ingest/file/source.rs:9-25 |
| `source_location` | Function | Normalizes paths relative to the vault root | crates/gwiki/src/ingest/file/source.rs:27-41 |
| `should_store_asset` | Function | Determines if a file should be treated as an asset | crates/gwiki/src/ingest/file/source.rs:43-55 |
| `read_source_file` | Function | Reads filesystem bytes wrapped in a wiki error | crates/gwiki/src/ingest/file/source.rs:57-63 |
| `attach_replay_metadata` | Function | Hooks up and writes ingest-time replay metadata | crates/gwiki/src/ingest/file/replay.rs:8-32 |

### Configuration Options
| Key / Field | Type | Description | Citation |
| --- | --- | --- | --- |
| `no_ai` | Boolean | Disables AI features during file ingestion | crates/gwiki/src/ingest/file/tests.rs:16 |
| `video_frame_interval_seconds` | Option<u64> | Specifies the interval for video frame extraction | crates/gwiki/src/ingest/file/tests.rs:27 |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/file/degradation.rs\|crates/gwiki/src/ingest/file/degradation.rs]] | This file defines small formatting helpers that turn different ingest degradation records into standardized summary strings. `transcription_degradation_summary`, `vision_degradation_summary`, and the feature-gated `document_degradation_summary` each encode a single degradation as a type-prefixed `reason`/`fallback` string, while `video_degradation_summaries` collects all media degradations from a `VideoIngestResult` into `Vec<String>` and appends the transcription degradation summary when present. [crates/gwiki/src/ingest/file/degradation.rs:4-11] [crates/gwiki/src/ingest/file/degradation.rs:13-15] [crates/gwiki/src/ingest/file/degradation.rs:18-22] [crates/gwiki/src/ingest/file/degradation.rs:24-39] |
| [[code/files/crates/gwiki/src/ingest/file/dispatch.rs\|crates/gwiki/src/ingest/file/dispatch.rs]] | Provides the no-index ingest dispatcher for local files. `ingest_path_without_index` inspects a path to determine the `SourceKind`, derives a fallback file name and source location, then routes the file through the appropriate specialized ingestor: audio, image, video, session, and, when enabled, document or PDF handling. If no specialized path applies, it falls back to the generic file ingester. The resulting `LocalFileIngestResult` is then normalized with replay metadata and returned, so this file acts as the central entry point that coordinates source detection, format-specific ingestion, and shared result post-processing. [crates/gwiki/src/ingest/file/dispatch.rs:43-242] |
| [[code/files/crates/gwiki/src/ingest/file/generic.rs\|crates/gwiki/src/ingest/file/generic.rs]] | Provides the no-index ingestion path for a generic local file. It reads the file bytes, registers a borrowed source record with metadata like location, kind, fetched time, title, and manual ingestion status, then decides whether to persist the file as an asset based on size/kind. It finishes by rendering raw markdown from the file contents and record hash, writing that markdown out, and returning the ingest result with no degradations. [crates/gwiki/src/ingest/file/generic.rs:11-57] |
| [[code/files/crates/gwiki/src/ingest/file/render.rs\|crates/gwiki/src/ingest/file/render.rs]] | Builds a Markdown representation of an ingested file, attaching source metadata, a title heading, and either the decoded text content or a note about where the original artifact was stored. It assembles the front matter from source kind, location, fetch time, hash, and optional asset path, then switches behavior based on file type and whether a raw asset exists so text-like inputs embed their contents while other inputs only reference the recorded artifact. [crates/gwiki/src/ingest/file/render.rs:6-51] |
| [[code/files/crates/gwiki/src/ingest/file/replay.rs\|crates/gwiki/src/ingest/file/replay.rs]] | Provides the ingest-time replay metadata hookup for a file. `attach_replay_metadata` builds a `SourceReplay` for the local file path, then updates the `SourceManifest` entry matching the ingested record ID. If the manifest has no matching entry, it still records the replay on the in-memory ingest result and reports no manifest change; if the entry already has the same replay, it only syncs the result record; otherwise it writes the replay into both the manifest entry and the ingest result, returning whether the manifest was modified. [crates/gwiki/src/ingest/file/replay.rs:8-32] |
| [[code/files/crates/gwiki/src/ingest/file/source.rs\|crates/gwiki/src/ingest/file/source.rs]] | This module classifies input files, derives a stable source-relative location string, decides whether a file should be stored as an asset versus kept inline, and reads the file bytes with I/O errors wrapped as `WikiError`. `detect_source_kind` maps file extensions to `SourceKind` categories; `source_location` normalizes a path against the vault root and converts separators to `/`; `should_store_asset` uses the kind and size threshold to route large text files and all non-text media/doc types into asset storage; `read_source_file` performs the filesystem read for ingest. [crates/gwiki/src/ingest/file/source.rs:9-25] [crates/gwiki/src/ingest/file/source.rs:27-41] [crates/gwiki/src/ingest/file/source.rs:43-55] [crates/gwiki/src/ingest/file/source.rs:57-63] |
| [[code/files/crates/gwiki/src/ingest/file/tests.rs\|crates/gwiki/src/ingest/file/tests.rs]] | This test module exercises the file-ingest pipeline end to end, with small helpers for building an AI context and ingest options. The tests verify source-location canonicalization, hashing for file and stdin inputs, media detection and dispatch, structured-document handling, and routing of multiple JSONL session formats to the correct orchestrators. It also checks office HTML and PDF dispatch behavior, including fallback to asset storage when document extraction is disabled. [crates/gwiki/src/ingest/file/tests.rs:13-22] [crates/gwiki/src/ingest/file/tests.rs:24-30] [crates/gwiki/src/ingest/file/tests.rs:33-49] [crates/gwiki/src/ingest/file/tests.rs:52-105] [crates/gwiki/src/ingest/file/tests.rs:108-130] |

## Components

| Component ID |
| --- |
| `d864d1c9-a5d4-56d1-9044-ef2972a76b3e` |
| `387e4be4-1a32-5b50-b2d8-46c532d02e50` |
| `01d024dc-1ebe-518e-8db2-97d3d9195193` |
| `a1fd8178-96ce-546d-ad0b-f19e41840cf8` |
| `90056d6c-fb43-5530-a1b4-6117c5481458` |
| `aa6e9d33-cb14-5cc9-9e17-40e1c671966c` |
| `4564f049-6c18-59cd-9578-af3f8c0754c9` |
| `f26f2009-6ceb-59de-9a93-702056d13e39` |
| `4b8b28d2-e21b-5fbf-93fd-476a887f484a` |
| `a690661d-5f6b-5079-a56c-140134e3a46f` |
| `f08a065e-0f26-563e-9397-30d9aa1b0543` |
| `acb81f97-9232-5b06-aef6-4f136b8fa6af` |
| `10429e53-e6ce-58de-ba73-2cfec6172411` |
| `b1de1ef8-1fbf-53bf-a96f-76ce74c753c3` |
| `95b83175-91e9-5a59-91bd-e5d25eb4379f` |
| `8b75c159-11d6-575b-968c-ebef4cd270a0` |
| `a67767c7-903e-552e-af9e-d5e7def5b090` |
| `39d16249-97cd-51e4-8205-b8ab1a3ea149` |
| `e7a24b77-e416-5e28-84fe-3e808eb3c84b` |
| `c332a148-a868-5a5c-9ade-e273cf9edd60` |
| `1640a8b2-72ae-5998-b8fd-2de0bc496397` |
| `bab5386c-e7f2-5cae-bcce-36aca58a6b9c` |
| `f4db65c2-d2e1-54af-9082-5bbaa9ec4d42` |
| `ee487ac7-a634-5421-8f78-37e77ed541f5` |
| `aa838a9d-afe9-5ca6-9d8d-935c2d2eb067` |
| `200e0dee-1ac8-53f7-9131-75285db99e7e` |
| `5cf84d93-e8e2-5119-b8b5-d9e576e2e8a3` |
| `c026c53f-901f-56d8-a54e-8c783de48d95` |
| `5f02dc07-3cf9-50c1-9f29-0ed2dbd620b1` |
| `605baf1a-0732-5580-82bd-e1dc79a6956e` |
| `27f17fe5-b2c9-5987-bf3b-99184bad28b4` |
| `aca55119-6640-54ce-ab10-93f4ef71c5eb` |
| `8a972c3f-1c22-54b2-b9e5-04c6290e1d44` |
