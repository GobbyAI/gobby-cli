---
title: crates/gwiki/src/commands/refresh/candidate.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/candidate.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/candidate.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Overview

`crates/gwiki/src/commands/refresh/candidate.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/refresh/candidate.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `refresh_url_candidate` | function | 'refresh_url_candidate' fetches a URL snapshot for a 'SourceRecord', compares the snapshot body hash to the record’s stored content hash, and then records the outcome as either unchanged, successfully refreshed via 'refresh_changed_url_source' with updated path/URL metadata, or failed, while propagating only the outer 'Result<(), WikiError>' for path/fetch setup errors. [crates/gwiki/src/commands/refresh/candidate.rs:15-74] |
| `refresh_local_candidate` | function | refresh_local_candidate validates local-file replay metadata for a source record, computes the current file hash, short-circuits as unchanged when it matches the stored content hash, and otherwise converts replay options and resolves ingest AI context while recording any selection or refresh failures into 'sinks'. [crates/gwiki/src/commands/refresh/candidate.rs:76-173] |
| `local_file_hash` | function | Validates that 'path' exists as a regular file and then returns its content hash via 'gobby_core::indexing::file_content_hash', otherwise mapping missing, non-file, stat, or hash I/O errors into 'RefreshFailure' variants tied to 'record'. [crates/gwiki/src/commands/refresh/candidate.rs:175-214] |
| `local_file_failure` | function | Constructs a 'RefreshFailure' by cloning the source record’s 'id', 'location', and 'kind' into the corresponding fields, converting 'code' to an owned 'String', and storing the provided 'message'. [crates/gwiki/src/commands/refresh/candidate.rs:216-224] |
| `refresh_changed_url_source` | function | Reingests a URL snapshot without indexing, gathers the prior source’s raw and asset paths from the vault, and finalizes a changed-refresh update against the previous 'SourceRecord'. [crates/gwiki/src/commands/refresh/candidate.rs:226-245] |
| `refresh_changed_local_source` | function | Reingests a local file path without indexing, collects the previous source’s raw and asset paths, and then finalizes a changed refresh by reconciling the new ingest result with the prior 'SourceRecord' and any degradations. [crates/gwiki/src/commands/refresh/candidate.rs:247-273] |
| `finalize_changed_refresh` | function | Deletes any obsolete previous source files except the current raw/asset paths, removes the prior record from the source manifest, and returns a 'ChangedRefresh' containing the ingest result, previous raw path, removed paths, and degradations. [crates/gwiki/src/commands/refresh/candidate.rs:275-310] |

