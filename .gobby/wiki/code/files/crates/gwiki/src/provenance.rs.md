---
title: crates/gwiki/src/provenance.rs
type: code_file
provenance:
- file: crates/gwiki/src/provenance.rs
  ranges:
  - 14-22
  - 25-29
  - 32-36
  - 39-47
  - 49-168
  - 170-172
  - 174-205
  - 207-223
  - 230-278
  - 281-304
  - 307-313
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/provenance.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the provenance model for tracking how raw source chunks support synthesized wiki sections. It introduces `SourceChunkRef`, `WikiSectionRef`, and `ProvenanceLink` as serializable records, then wraps them in `ProvenanceGraph`, which stores links and maintains secondary indexes by section ID, page-plus-section, and source ID so lookups stay fast. The graph can add links, query them through each index, rebuild indexes after deserialization, and persist itself to or restore itself from `<vault_root>/meta/provenance.json` with durable file writes. Helper functions handle page/section key निर्माण and Unix directory syncing, and the tests verify linking, save/load roundtrips, and empty loads when the provenance file is missing.
[crates/gwiki/src/provenance.rs:14-22]
[crates/gwiki/src/provenance.rs:25-29]
[crates/gwiki/src/provenance.rs:32-36]
[crates/gwiki/src/provenance.rs:39-47]
[crates/gwiki/src/provenance.rs:49-168]

## API Symbols

- `SourceChunkRef` (class) component `SourceChunkRef [class]` (`1d92784d-2c74-5e0f-82c1-df8b8e2f23d7`) lines 14-22 [crates/gwiki/src/provenance.rs:14-22]
  - Signature: `pub struct SourceChunkRef {`
  - Purpose: 'SourceChunkRef' is a reference record that identifies a specific byte-range chunk within a source note by 'source_id', 'chunk_id', filesystem 'path', and inclusive/exclusive byte offsets 'byte_start' and 'byte_end'. [crates/gwiki/src/provenance.rs:14-22]
- `WikiSectionRef` (class) component `WikiSectionRef [class]` (`a9b9e35f-7dfe-537e-b98f-6d7675ea04af`) lines 25-29 [crates/gwiki/src/provenance.rs:25-29]
  - Signature: `pub struct WikiSectionRef {`
  - Purpose: 'WikiSectionRef' is a struct that identifies a wiki section by storing the page path ('PathBuf'), the section heading text, and a string section identifier. [crates/gwiki/src/provenance.rs:25-29]
- `ProvenanceLink` (class) component `ProvenanceLink [class]` (`71f6214a-0988-580d-ac48-35088e3313a6`) lines 32-36 [crates/gwiki/src/provenance.rs:32-36]
  - Signature: `pub struct ProvenanceLink {`
  - Purpose: 'ProvenanceLink' is a data-only struct that links a 'SourceChunkRef' to a 'WikiSectionRef' and optionally stores a claim string describing the provenance relationship. [crates/gwiki/src/provenance.rs:32-36]
- `ProvenanceGraph` (class) component `ProvenanceGraph [class]` (`498890e2-7252-5bc3-b2fa-624e1e9f486c`) lines 39-47 [crates/gwiki/src/provenance.rs:39-47]
  - Signature: `pub struct ProvenanceGraph {`
  - Purpose: 'ProvenanceGraph' is a serialized provenance index that stores a list of 'ProvenanceLink' entries and maintains skipped runtime lookup maps from section, page-section, and source identifiers to link indices for efficient provenance queries. [crates/gwiki/src/provenance.rs:39-47]
- `ProvenanceGraph` (class) component `ProvenanceGraph [class]` (`8a87dafd-6c72-5a5f-85e6-3f55202ad3ec`) lines 49-168 [crates/gwiki/src/provenance.rs:49-168]
  - Signature: `impl ProvenanceGraph {`
  - Purpose: 'ProvenanceGraph' is an in-memory collection of 'ProvenanceLink' records that maintains secondary indexes by section ID, page-path-plus-section, and source ID to support efficient lookups and persistence to a vault. [crates/gwiki/src/provenance.rs:49-168]
- `ProvenanceGraph.add_link` (method) component `ProvenanceGraph.add_link [method]` (`fa37e1f2-1d85-5192-a172-579bce453d62`) lines 50-68 [crates/gwiki/src/provenance.rs:50-68]
  - Signature: `pub fn add_link(&mut self, link: ProvenanceLink) {`
  - Purpose: Appends a 'ProvenanceLink' to 'self.links' and records its new index in the section, page-section, and source lookup indices keyed by the link’s section ID, page/section key, and source ID. [crates/gwiki/src/provenance.rs:50-68]
- `ProvenanceGraph.links_for_section` (method) component `ProvenanceGraph.links_for_section [method]` (`9a3f8f39-55d3-59c6-a4d3-3c9083e5a709`) lines 71-78 [crates/gwiki/src/provenance.rs:71-78]
  - Signature: `pub fn links_for_section(&self, section_id: &str) -> Vec<&ProvenanceLink> {`
  - Purpose: Returns a vector of references to 'ProvenanceLink' entries for the given 'section_id' by looking up that section’s indexed link positions in 'section_index', resolving each index through 'self.links', and discarding any missing entries. [crates/gwiki/src/provenance.rs:71-78]
- `ProvenanceGraph.links_for_page_section` (method) component `ProvenanceGraph.links_for_page_section [method]` (`6fd439b3-7c9c-594e-b725-ea7d5b1a1b17`) lines 80-91 [crates/gwiki/src/provenance.rs:80-91]
  - Signature: `pub fn links_for_page_section(`
  - Purpose: Returns all 'ProvenanceLink' references associated with the '(page_path, section_id)' key by looking up matching link indices in 'page_section_index', resolving each index through 'self.links', and collecting the existing references into a 'Vec<&ProvenanceLink>'. [crates/gwiki/src/provenance.rs:80-91]
- `ProvenanceGraph.links_for_source` (method) component `ProvenanceGraph.links_for_source [method]` (`3d3af56f-3f39-588c-8408-a2016631831b`) lines 93-100 [crates/gwiki/src/provenance.rs:93-100]
  - Signature: `pub fn links_for_source(&self, source_id: &str) -> Vec<&ProvenanceLink> {`
  - Purpose: Returns all 'ProvenanceLink' references associated with the given 'source_id' by looking up its indexed link positions in 'source_index', resolving each index through 'links', and collecting the existing entries into a 'Vec<&ProvenanceLink>'. [crates/gwiki/src/provenance.rs:93-100]
- `ProvenanceGraph.links` (method) component `ProvenanceGraph.links [method]` (`59be75eb-5df6-5465-bc3f-8b5afadba396`) lines 102-104 [crates/gwiki/src/provenance.rs:102-104]
  - Signature: `pub fn links(&self) -> &[ProvenanceLink] {`
  - Purpose: Returns an immutable slice view of the 'ProvenanceLink' values stored in 'self.links'. [crates/gwiki/src/provenance.rs:102-104]
- `ProvenanceGraph.save_to_vault` (method) component `ProvenanceGraph.save_to_vault [method]` (`b8f1fdd6-6484-5e25-829d-fc3b4ba74689`) lines 106-120 [crates/gwiki/src/provenance.rs:106-120]
  - Signature: `pub fn save_to_vault(&self, vault_root: &std::path::Path) -> Result<(), WikiError> {`
  - Purpose: Creates '<vault_root>/meta', serializes 'self' as pretty-printed JSON to '<vault_root>/meta/provenance.json', and durably writes the file, mapping directory-creation and serialization failures into 'WikiError::Io' and 'WikiError::Json' respectively. [crates/gwiki/src/provenance.rs:106-120]
- `ProvenanceGraph.load_from_vault` (method) component `ProvenanceGraph.load_from_vault [method]` (`446fabec-31a7-5ad0-9b56-2c8da2def08c`) lines 122-144 [crates/gwiki/src/provenance.rs:122-144]
  - Signature: `pub fn load_from_vault(vault_root: &std::path::Path) -> Result<Self, WikiError> {`
  - Purpose: Loads a provenance graph from '<vault_root>/meta/provenance.json', returns 'Self::default()' if the file is missing, maps read/parse failures to 'WikiError::Io' or 'WikiError::Json', rebuilds indexes on success, and returns the reconstructed graph. [crates/gwiki/src/provenance.rs:122-144]
- `ProvenanceGraph.rebuild_indexes` (method) component `ProvenanceGraph.rebuild_indexes [method]` (`86568a02-3afb-5678-880b-e7a68638fcf9`) lines 146-167 [crates/gwiki/src/provenance.rs:146-167]
  - Signature: `fn rebuild_indexes(&mut self) {`
  - Purpose: Rebuilds all three lookup indexes by clearing them and then scanning 'self.links' to repopulate 'section_index', 'page_section_index', and 'source_index' with each link’s current position. [crates/gwiki/src/provenance.rs:146-167]
- `page_section_key` (function) component `page_section_key [function]` (`655593cc-70db-5c52-814f-de7e0529773b`) lines 170-172 [crates/gwiki/src/provenance.rs:170-172]
  - Signature: `fn page_section_key(page_path: &Path, section_id: &str) -> String {`
  - Purpose: Returns a string key by concatenating the page path’s lossy string representation, a '#', and the given section ID. [crates/gwiki/src/provenance.rs:170-172]
- `write_provenance_json_durably` (function) component `write_provenance_json_durably [function]` (`41e8dcb9-66ba-5fcf-9bda-02ae3bfae947`) lines 174-205 [crates/gwiki/src/provenance.rs:174-205]
  - Signature: `fn write_provenance_json_durably(`
  - Purpose: Creates a temporary file in 'meta_dir', writes 'contents' to it, 'sync_all's the file for durability, atomically persists it to 'path', and then syncs the provenance directory, converting any I/O failure into a 'WikiError::Io' with the relevant action and path. [crates/gwiki/src/provenance.rs:174-205]
- `sync_provenance_dir` (function) component `sync_provenance_dir [function]` (`83e75adf-da8a-58d2-a938-e701d77c8ebb`) lines 207-223 [crates/gwiki/src/provenance.rs:207-223]
  - Signature: `fn sync_provenance_dir(meta_dir: &std::path::Path) -> Result<(), WikiError> {`
  - Purpose: On Unix, it opens 'meta_dir' as a directory and calls 'sync_all()' to flush provenance metadata to stable storage, mapping any I/O failure into 'WikiError::Io', while on non-Unix it is a no-op that returns 'Ok(())'. [crates/gwiki/src/provenance.rs:207-223]
- `links_sources_to_sections` (function) component `links_sources_to_sections [function]` (`f601353d-ce31-54c8-a3fd-95623cfd9a1d`) lines 230-278 [crates/gwiki/src/provenance.rs:230-278]
  - Signature: `fn links_sources_to_sections() {`
  - Purpose: Constructs a 'ProvenanceGraph', adds a 'ProvenanceLink' from a 'SourceChunkRef' to a 'WikiSectionRef' with an optional claim, and verifies the graph can retrieve that link by section, page/section, and source identifiers. [crates/gwiki/src/provenance.rs:230-278]
- `saves_and_loads_vault_roundtrip` (function) component `saves_and_loads_vault_roundtrip [function]` (`fe446f60-9481-5880-9011-b877698759a3`) lines 281-304 [crates/gwiki/src/provenance.rs:281-304]
  - Signature: `fn saves_and_loads_vault_roundtrip() {`
  - Purpose: Creates a 'ProvenanceGraph' with one 'ProvenanceLink', saves it to a temporary vault directory, reloads it from disk, and asserts the deserialized graph is exactly equal to the original. [crates/gwiki/src/provenance.rs:281-304]
- `missing_provenance_file_loads_empty_graph` (function) component `missing_provenance_file_loads_empty_graph [function]` (`9c8e12fe-c50c-5505-a071-fd1aadcc8f9e`) lines 307-313 [crates/gwiki/src/provenance.rs:307-313]
  - Signature: `fn missing_provenance_file_loads_empty_graph() {`
  - Purpose: Verifies that 'ProvenanceGraph::load_from_vault' returns an empty graph with no links when the provenance file is absent. [crates/gwiki/src/provenance.rs:307-313]

