---
title: crates/gwiki/src/provenance.rs
type: code_file
provenance:
- file: crates/gwiki/src/provenance.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/provenance.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/provenance.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gwiki/src/provenance.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SourceChunkRef` | class | 'SourceChunkRef' is a reference record identifying a chunk within a source note by source ID, chunk ID, file path, and an inclusive start/exclusive end byte range. [crates/gwiki/src/provenance.rs:14-22] |
| `WikiSectionRef` | class | 'WikiSectionRef' is a struct that identifies a wiki section by storing the page path ('PathBuf'), the section heading ('String'), and the section ID ('String'). [crates/gwiki/src/provenance.rs:25-29] |
| `ProvenanceLink` | class | 'ProvenanceLink' is a data structure that links a 'SourceChunkRef' to a 'WikiSectionRef' with an optional textual 'claim' describing the supported statement. [crates/gwiki/src/provenance.rs:32-36] |
| `ProvenanceGraph` | class | 'ProvenanceGraph' is a serialized graph container that stores a list of 'ProvenanceLink' edges and maintains skipped, derived BTreeMap indices for fast lookup by section, page section, and source identifiers. [crates/gwiki/src/provenance.rs:39-47] |
| `ProvenanceGraph::add_link` | method | Appends a 'ProvenanceLink' to 'self.links' and records its new index in the section, page-section, and source lookup maps keyed by the link’s 'section_id', 'page_path' plus 'section_id', and 'source_id', respectively. [crates/gwiki/src/provenance.rs:50-68] |
| `ProvenanceGraph::links_for_section` | method | Returns a vector of references to 'ProvenanceLink' values for the given 'section_id' by looking up the section’s link indices in 'section_index', mapping each index to the corresponding entry in 'links', and collecting only the links that still exist. [crates/gwiki/src/provenance.rs:71-78] |
| `ProvenanceGraph::links_for_page_section` | method | Returns all 'ProvenanceLink' references associated with the given page path and section ID by looking up their indices in 'page_section_index', resolving each index through 'self.links', and collecting the existing matches into a 'Vec<&ProvenanceLink>'. [crates/gwiki/src/provenance.rs:80-91] |
| `ProvenanceGraph::links_for_source` | method | Returns all 'ProvenanceLink' references associated with 'source_id' by looking up its indexed link positions in 'source_index', discarding missing entries, resolving each index through 'self.links', and collecting the resulting references into a 'Vec<&ProvenanceLink>'. [crates/gwiki/src/provenance.rs:93-100] |
| `ProvenanceGraph::links` | method | Returns an immutable slice of the provenance links stored in 'self.links'. [crates/gwiki/src/provenance.rs:102-104] |
| `ProvenanceGraph::save_to_vault` | method | Creates 'vault_root/meta' if needed, pretty-serializes 'self' as 'meta/provenance.json', and durably writes that JSON file, mapping directory creation and serialization failures into 'WikiError'. [crates/gwiki/src/provenance.rs:106-120] |
| `ProvenanceGraph::load_from_vault` | method | 'load_from_vault' reads 'meta/provenance.json' under the given vault root, returns 'Self::default()' if the file is missing, otherwise deserializes the JSON into 'Self', rebuilds its indexes, and maps I/O or parse failures into 'WikiError::Io' or 'WikiError::Json' with the provenance file path. [crates/gwiki/src/provenance.rs:122-144] |
| `ProvenanceGraph::rebuild_indexes` | method | Clears the three lookup maps and rebuilds them by iterating over 'self.links', recording each link’s index under its 'section_id', computed page-section key, and 'source_id'. [crates/gwiki/src/provenance.rs:146-167] |
| `page_section_key` | function | Returns a string key formed by concatenating the page path’s lossily converted string representation, a '#' separator, and the provided 'section_id'. [crates/gwiki/src/provenance.rs:170-172] |
| `write_provenance_json_durably` | function | Creates a temporary file in 'meta_dir', writes 'contents' to it, 'sync_all's the temp file to disk, atomically persists it to 'path', and then fsyncs the provenance directory via 'sync_provenance_dir(meta_dir)', mapping any I/O failure into 'WikiError::Io'. [crates/gwiki/src/provenance.rs:174-205] |
| `sync_provenance_dir` | function | On Unix, opens 'meta_dir' and calls 'sync_all()' to flush the provenance metadata directory to stable storage, mapping any I/O error into 'WikiError::Io' with the directory path; on non-Unix platforms it is a no-op that returns 'Ok(())'. [crates/gwiki/src/provenance.rs:207-223] |

_Verified by 3 in-file unit tests._

