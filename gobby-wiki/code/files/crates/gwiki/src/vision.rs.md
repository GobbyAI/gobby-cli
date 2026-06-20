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

`crates/gwiki/src/vision.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VisionExtraction` | class | The 'VisionExtraction' struct represents data extracted from visual analysis, comprising a mandatory description string, an optional OCR-extracted text string, and a collection of key-value metadata pairs represented as a vector of string tuples. [crates/gwiki/src/vision.rs:19-23] |
| `VisionDegradation` | class | The 'VisionDegradation' struct represents a vision modality degradation, capturing the specific reason for the degradation via a 'ModalityDegradationReason' and providing a fallback string representation. [crates/gwiki/src/vision.rs:26-29] |
| `VisionDegradation::for_routing` | method | This crate-private constructor instantiates 'Self' by mapping an 'AiRouting' variant to its corresponding 'ModalityDegradationReason' and storing it alongside a string representation of the provided fallback parameter. [crates/gwiki/src/vision.rs:32-43] |
| `disabled_degradation` | function | The 'disabled_degradation' function returns a 'VisionDegradation' struct configured with a disabled modality degradation reason and a fallback string instructing to retain only the PDF text layer. [crates/gwiki/src/vision.rs:47-52] |
| `vision_extraction_is_empty` | function | Returns 'true' if the 'VisionExtraction''s trimmed 'description' is empty and its optional 'ocr_text' is either 'None' or contains only whitespace when trimmed. [crates/gwiki/src/vision.rs:58-65] |
| `VisionClient` | type | Indexed type `VisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:67-69] |
| `VisionRequest` | class | 'VisionRequest' is a lifetime-bound Rust structure that encapsulates a visual asset's raw binary data along with its metadata, including its file name, path, optional MIME type, and optional pixel dimensions, for processing. [crates/gwiki/src/vision.rs:72-79] |
| `VisionEndpoint` | type | Indexed type `VisionEndpoint` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:81-85] |
| `VisionMarkdownResult` | class | The 'VisionMarkdownResult' struct represents the output of a vision-to-markdown operation, containing the target file path and an optional 'VisionDegradation' detailing any layout or quality degradation. [crates/gwiki/src/vision.rs:88-91] |
| `write_image_derived_markdown` | function | This function processes a vision request through a given endpoint to either extract image content or handle degradation fallbacks, renders a derived markdown document with these details, and atomically writes it to a resolved file path within the vault directory. [crates/gwiki/src/vision.rs:93-140] |
| `render_image_derived_markdown` | function | This function compiles metadata from an image's source record, scope, vision request, and optional extraction or degradation details to generate a formatted Markdown string. [crates/gwiki/src/vision.rs:142-254] |
| `dedupe_vision_metadata` | function | This function deduplicates up to 'MAX_VISION_METADATA_ENTRIES' key-value pairs by inserting them into a 'BTreeMap' using transformed keys, retaining the first encountered value for each unique processed key, and returning the sorted result as a vector of tuples. [crates/gwiki/src/vision.rs:256-264] |
| `bounded_vision_metadata_key` | function | The function 'bounded_vision_metadata_key' returns the input key unmodified if it is within a maximum character limit; otherwise, it truncates the key to that limit and appends a hyphen followed by a truncated content hash of the original key. [crates/gwiki/src/vision.rs:266-283] |
| `vision_metadata_key` | function | The 'vision_metadata_key' function sanitizes an input key string by converting it to a single line, replacing all non-alphanumeric and non-separator (underscore and hyphen) characters with underscores, transforming it to lowercase, and prepending "vision_" to the trimmed result, returning "vision_metadata" if the sanitized key is empty. [crates/gwiki/src/vision.rs:285-303] |
| `write_vision_markdown_atomically` | function | This function atomically writes a byte slice of markdown contents to a target path by writing to and syncing a temporary file, persisting it over the destination file, and flushing the parent directory, mapping any I/O errors to a 'WikiError'. [crates/gwiki/src/vision.rs:305-329] |
| `create_vision_temp_file` | function | This function creates a named temporary file in the parent directory of the provided path with a filename prefix derived from that path and a '.tmp' suffix, returning a 'Result' containing the 'NamedTempFile' or a 'WikiError' if the directory resolution or file creation fails. [crates/gwiki/src/vision.rs:331-358] |
| `sync_parent_dir` | function | On Unix platforms, this function opens the parent directory of the specified path and synchronizes its metadata to disk using 'sync_all' to persist directory entry changes, returning a 'WikiError' on failure, while performing a no-op on non-Unix systems. [crates/gwiki/src/vision.rs:360-379] |
| `FakeVisionClient` | class | The 'FakeVisionClient' struct is a mock client implementation that tracks its call count using an interior-mutable 'Cell<usize>' field. [crates/gwiki/src/vision.rs:388-390] |
| `FailingVisionClient` | class | The 'FailingVisionClient' is a unit struct representing a mock vision client designed to simulate failed operations during testing. [crates/gwiki/src/vision.rs:392] |
| `FakeVisionClient::extract` | method | The 'extract' method increments an internal call counter and returns a successful 'VisionExtraction' result containing predefined mock data for a circuit diagram's description, OCR text, and metadata. [crates/gwiki/src/vision.rs:395-402] |
| `FailingVisionClient::extract` | method | The 'extract' method accepts a 'VisionRequest' and unconditionally returns a 'WikiError::Daemon' error indicating that the '/api/chat/attachments' endpoint is temporarily unavailable. [crates/gwiki/src/vision.rs:406-411] |
| `EmptyVisionClient` | class | 'EmptyVisionClient' is a unit structure that serves as a placeholder or no-op implementation of a vision client interface. [crates/gwiki/src/vision.rs:414] |
| `EmptyVisionClient::extract` | method | The 'extract' method returns a successful 'Result' containing a 'VisionExtraction' with a whitespace-only description, no OCR text, and a single metadata entry identifying the model as 'haiku' to handle or simulate a blank-content vision daemon bug. [crates/gwiki/src/vision.rs:417-425] |
| `record_for` | function | The 'record_for' function registers a manually ingested, pending image 'SourceDraft' representing '/tmp/circuit.png' at the specified temporary directory path, returning the resulting 'SourceRecord' or panicking upon failure. [crates/gwiki/src/vision.rs:428-444] |

_Verified by 8 in-file unit tests._

