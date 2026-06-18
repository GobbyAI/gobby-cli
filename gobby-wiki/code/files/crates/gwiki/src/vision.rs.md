---
title: crates/gwiki/src/vision.rs
type: code_file
provenance:
- file: crates/gwiki/src/vision.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/vision.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/vision.rs` exposes 32 indexed API symbols.

## How it fits

`crates/gwiki/src/vision.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VisionExtraction` | class | Indexed class `VisionExtraction` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:19-23] |
| `VisionDegradation` | class | Indexed class `VisionDegradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:26-29] |
| `VisionDegradation::for_routing` | method | Indexed method `VisionDegradation::for_routing` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:32-43] |
| `disabled_degradation` | function | Indexed function `disabled_degradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:47-52] |
| `vision_extraction_is_empty` | function | Indexed function `vision_extraction_is_empty` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:58-65] |
| `VisionClient` | type | Indexed type `VisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:67-69] |
| `VisionRequest` | class | Indexed class `VisionRequest` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:72-79] |
| `VisionEndpoint` | type | Indexed type `VisionEndpoint` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:81-85] |
| `VisionMarkdownResult` | class | Indexed class `VisionMarkdownResult` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:88-91] |
| `write_image_derived_markdown` | function | Indexed function `write_image_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:93-140] |
| `render_image_derived_markdown` | function | Indexed function `render_image_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:142-254] |
| `dedupe_vision_metadata` | function | Indexed function `dedupe_vision_metadata` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:256-264] |
| `bounded_vision_metadata_key` | function | Indexed function `bounded_vision_metadata_key` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:266-283] |
| `vision_metadata_key` | function | Indexed function `vision_metadata_key` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:285-303] |
| `write_vision_markdown_atomically` | function | Indexed function `write_vision_markdown_atomically` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:305-329] |
| `create_vision_temp_file` | function | Indexed function `create_vision_temp_file` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:331-358] |
| `sync_parent_dir` | function | Indexed function `sync_parent_dir` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:360-379] |
| `FakeVisionClient` | class | Indexed class `FakeVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:388-390] |
| `FailingVisionClient` | class | Indexed class `FailingVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:392] |
| `FakeVisionClient::extract` | method | Indexed method `FakeVisionClient::extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:395-402] |
| `FailingVisionClient::extract` | method | Indexed method `FailingVisionClient::extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:406-411] |
| `EmptyVisionClient` | class | Indexed class `EmptyVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:414] |
| `EmptyVisionClient::extract` | method | Indexed method `EmptyVisionClient::extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:417-425] |
| `record_for` | function | Indexed function `record_for` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:428-444] |
| `vision_writes_derived_markdown` | function | Indexed function `vision_writes_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:447-491] |
| `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` | function | Indexed function `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:494-522] |
| `vision_metadata_bounds_entries_and_hashes_long_keys` | function | Indexed function `vision_metadata_bounds_entries_and_hashes_long_keys` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:525-547] |
| `missing_vision_degrades` | function | Indexed function `missing_vision_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:550-592] |
| `vision_client_error_degrades` | function | Indexed function `vision_client_error_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:595-626] |
| `empty_vision_extraction_degrades` | function | Indexed function `empty_vision_extraction_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:629-659] |
| `vision_markdown_overwrites_atomically_without_temp_leftovers` | function | Indexed function `vision_markdown_overwrites_atomically_without_temp_leftovers` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:662-715] |
| `vision_temp_file_requires_parent_directory` | function | Indexed function `vision_temp_file_requires_parent_directory` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:718-729] |

