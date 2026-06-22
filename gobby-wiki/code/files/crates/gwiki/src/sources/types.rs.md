---
title: crates/gwiki/src/sources/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/types.rs

Module: [[code/modules/crates/gwiki/src/sources|crates/gwiki/src/sources]]

## Overview

`crates/gwiki/src/sources/types.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gwiki/src/sources/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SourceKind` | type | Indexed type `SourceKind` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:12-30] |
| `SourceKind::fmt` | method | Formats the enum by matching each variant to its corresponding lowercase string literal and writing that string to the formatter. [crates/gwiki/src/sources/types.rs:33-52] |
| `IngestionMethod` | type | Indexed type `IngestionMethod` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:57-60] |
| `IngestionMethod::fmt` | method | Writes the string '"manual"' for 'Self::Manual' and '"research"' for 'Self::Research' into the provided formatter, returning the resulting 'fmt::Result'. [crates/gwiki/src/sources/types.rs:63-68] |
| `CompileStatus` | type | Indexed type `CompileStatus` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:73-76] |
| `CompileStatus::fmt` | method | Writes the string '"pending"' or '"compiled"' to the formatter according to the enum variant, implementing 'Display'-style formatting for 'self'. [crates/gwiki/src/sources/types.rs:79-84] |
| `SourceDraft` | class | 'SourceDraft' is a data-only Rust struct representing an ingested source artifact with its origin metadata, raw byte content, optional citation and licensing information, and current ingestion/compilation status. [crates/gwiki/src/sources/types.rs:88-98] |
| `SourceDraft::new` | method | Constructs a new 'Self' by converting and storing the provided 'location', 'kind', 'fetched_at', and 'content', while initializing 'title', 'citation', and 'license' to 'None', 'ingestion_method' to 'IngestionMethod::Manual', and 'compile_status' to 'CompileStatus::Pending'. [crates/gwiki/src/sources/types.rs:101-118] |
| `SourceDraft::url` | method | Constructs a new 'Self' source from a URL location by converting 'location', 'fetched_at', and 'content' into owned 'String'/'Vec<u8>' values and delegating to 'Self::new' with 'SourceKind::Url'. [crates/gwiki/src/sources/types.rs:120-126] |
| `SourceDraft::with_title` | method | Returns 'self' after setting 'self.title' to 'Some(title.into())', enabling builder-style assignment of the title field. [crates/gwiki/src/sources/types.rs:128-131] |
| `SourceDraft::with_citation` | method | Sets the builder’s 'citation' field to 'Some(citation.into())' and returns the updated 'self' for method chaining. [crates/gwiki/src/sources/types.rs:133-136] |
| `SourceDraft::with_license` | method | Sets 'self.license' to 'Some(license.into())' and returns the updated builder instance by value. [crates/gwiki/src/sources/types.rs:138-141] |
| `SourceDraft::with_ingestion_method` | method | Sets 'self.ingestion_method' to the provided 'IngestionMethod' and returns the updated value by value. [crates/gwiki/src/sources/types.rs:143-146] |
| `SourceDraft::with_compile_status` | method | Sets 'self.compile_status' to the provided 'CompileStatus' value and returns the updated instance for chaining. [crates/gwiki/src/sources/types.rs:148-151] |
| `SourceDraftRef` | class | 'SourceDraftRef<'a>' is a borrowed, crate-visible record of an ingested source draft that carries its location, kind, fetch timestamp, raw byte content, optional metadata (title, citation, license), and ingestion/compile status. [crates/gwiki/src/sources/types.rs:154-164] |
| `SourceRecord` | class | 'SourceRecord' is a serializable Rust struct that captures a source’s identity, locations, kind, fetch metadata, content hash, optional descriptive/licensing fields, ingestion and compile status, and an optional replay payload. [crates/gwiki/src/sources/types.rs:167-181] |
| `SourceReplay` | type | Indexed type `SourceReplay` in `crates/gwiki/src/sources/types.rs`. [crates/gwiki/src/sources/types.rs:185-191] |
| `SourceReplay::local_file` | method | Constructs and returns a 'Self::LocalFile' variant by storing the provided 'path' and converting 'options' into 'SourceReplayOptions' via 'SourceReplayOptions::from_ingest_file_options'. [crates/gwiki/src/sources/types.rs:194-199] |
| `SourceReplayOptions` | class | 'SourceReplayOptions' is a serde-serializable configuration struct for source replay that toggles AI usage and translation, optionally sets a target language, video frame sampling interval, and routing overrides for transcription, vision, and text processing. [crates/gwiki/src/sources/types.rs:203-218] |
| `SourceReplayOptions::from_ingest_file_options` | method | Constructs 'Self' by copying the 'no_ai', 'translate', 'target_lang', and 'video_frame_interval_seconds' fields from 'IngestFileOptions', and converting each optional routing field to a routed name via 'routing_name'. [crates/gwiki/src/sources/types.rs:221-231] |
| `SourceReplayOptions::to_ingest_file_options` | method | Builds and returns an 'IngestFileOptions' by copying the struct’s flags and values, cloning 'target_lang', and validating/parsing the transcription, vision, and text routing fields via 'parse_routing', propagating any 'WikiError'. [crates/gwiki/src/sources/types.rs:233-246] |
| `is_false` | function | Returns the logical negation of the referenced boolean, yielding 'true' when 'value' is 'false' and 'false' when 'value' is 'true'. [crates/gwiki/src/sources/types.rs:249-251] |
| `routing_name` | function | Returns the lowercase string name of an 'AiRouting' enum variant by matching 'Auto', 'Daemon', 'Direct', or 'Off' to '"auto"', '"daemon"', '"direct"', or '"off"' respectively and converting it to a 'String'. [crates/gwiki/src/sources/types.rs:253-261] |
| `parse_routing` | function | Parses an optional routing string into 'Option<AiRouting>', converting any parse failure into 'WikiError::InvalidInput' annotated with the given field name. [crates/gwiki/src/sources/types.rs:263-276] |

