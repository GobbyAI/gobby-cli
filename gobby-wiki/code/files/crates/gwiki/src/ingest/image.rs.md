---
title: crates/gwiki/src/ingest/image.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/image.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/image.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/image.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/image.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ImageSnapshot` | class | 'ImageSnapshot' is a data container for a fetched image, storing its source location, filename, fetch timestamp, raw bytes, optional MIME type, and optional dimensions. [crates/gwiki/src/ingest/image.rs:23-31] |
| `ImageIngestResult` | class | 'ImageIngestResult' is a result container for image ingestion that bundles the source record and the raw, asset, and derived file paths, plus an optional 'VisionDegradation' descriptor. [crates/gwiki/src/ingest/image.rs:34-40] |
| `ingest_image` | function | 'ingest_image' delegates image ingestion to 'ingest_image_with_vision' using an unavailable vision endpoint configured with 'default_vision_degradation()', returning the resulting 'ImageIngestResult' or 'WikiError'. [crates/gwiki/src/ingest/image.rs:43-56] |
| `ingest_image_with_production_vision` | function | 'ingest_image_with_production_vision' ingests an image via 'ingest_image_with_production_vision_without_index', then rebuilds the wiki index with 'index_after_ingest', and returns the resulting 'ImageIngestResult' or a 'WikiError'. [crates/gwiki/src/ingest/image.rs:59-70] |
| `ingest_image_with_production_vision_without_index` | function | Builds a 'VisionEndpoint' from the current AI routing and, when the 'ai' feature allows 'Daemon' or 'Direct' routing, uses 'ProductionVisionClient' to ingest the image via 'ingest_image_with_vision_without_index'; otherwise it degrades to unavailable vision handling that preserves the raw image asset and metadata only. [crates/gwiki/src/ingest/image.rs:72-103] |
| `ingest_image_with_vision` | function | Ingests an image using the vision endpoint via 'ingest_image_with_vision_without_index', then rebuilds the wiki index with 'index_after_ingest' and returns the resulting 'ImageIngestResult'. [crates/gwiki/src/ingest/image.rs:106-116] |
| `ingest_image_with_vision_without_index` | function | Registers an image snapshot in the source manifest, writes the asset and raw markdown to disk, invokes a vision endpoint to generate derived markdown, and returns the resulting ingest record with paths and vision degradation metadata. [crates/gwiki/src/ingest/image.rs:118-167] |
| `IngestResult::from` | method | Constructs 'Self' by moving 'record' and 'raw_path' from 'ImageIngestResult' and wrapping 'result.asset_path' in 'Some' for the 'asset_path' field. [crates/gwiki/src/ingest/image.rs:170-176] |
| `render_raw_image_markdown` | function | Builds a markdown string for a raw image snapshot by serializing metadata fields such as source location, fetch time, hash, asset path, and optional MIME type/dimensions, then appending a title header and a note pointing to the stored original image path. [crates/gwiki/src/ingest/image.rs:179-210] |
| `default_vision_degradation` | function | Returns a 'VisionDegradation' configured for automatic AI routing that preserves raw image assets while exposing only filename/metadata and disabling visual extraction. [crates/gwiki/src/ingest/image.rs:213-218] |
| `sample_snapshot` | function | Returns a hard-coded 'ImageSnapshot' for '/tmp/diagram.png' containing PNG byte data, MIME type 'image/png', and dimensions '640x480' with a fixed 'fetched_at' timestamp. [crates/gwiki/src/ingest/image.rs:228-238] |
| `test_ai_context` | function | The 'test_ai_context' function constructs and returns an 'AiContext' configured for testing, mapping all AI capability bindings to a direct routing configuration targeting the specified API base URL using the 'gpt-4.1-mini' model with a concurrency limit of one. [crates/gwiki/src/ingest/image.rs:338-375] |
| `spawn_vision_server` | function | The 'spawn_vision_server' function spawns a test HTTP server configured to return a specified static JSON response, returning a tuple containing the server's address and a handle for managing the test requests. [crates/gwiki/src/ingest/image.rs:378-380] |

_Verified by 3 in-file unit tests._

