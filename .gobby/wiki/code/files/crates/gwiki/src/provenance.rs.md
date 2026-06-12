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

`crates/gwiki/src/provenance.rs` exposes 19 indexed API symbols.
[crates/gwiki/src/provenance.rs:14-22]
[crates/gwiki/src/provenance.rs:25-29]
[crates/gwiki/src/provenance.rs:32-36]
[crates/gwiki/src/provenance.rs:39-47]
[crates/gwiki/src/provenance.rs:49-168]

## API Symbols

- `SourceChunkRef` (class) component `SourceChunkRef [class]` (`1d92784d-2c74-5e0f-82c1-df8b8e2f23d7`) lines 14-22 [crates/gwiki/src/provenance.rs:14-22]
  - Signature: `pub struct SourceChunkRef {`
  - Purpose: Indexed class `SourceChunkRef` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:14-22]
- `WikiSectionRef` (class) component `WikiSectionRef [class]` (`a9b9e35f-7dfe-537e-b98f-6d7675ea04af`) lines 25-29 [crates/gwiki/src/provenance.rs:25-29]
  - Signature: `pub struct WikiSectionRef {`
  - Purpose: Indexed class `WikiSectionRef` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:25-29]
- `ProvenanceLink` (class) component `ProvenanceLink [class]` (`71f6214a-0988-580d-ac48-35088e3313a6`) lines 32-36 [crates/gwiki/src/provenance.rs:32-36]
  - Signature: `pub struct ProvenanceLink {`
  - Purpose: Indexed class `ProvenanceLink` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:32-36]
- `ProvenanceGraph` (class) component `ProvenanceGraph [class]` (`498890e2-7252-5bc3-b2fa-624e1e9f486c`) lines 39-47 [crates/gwiki/src/provenance.rs:39-47]
  - Signature: `pub struct ProvenanceGraph {`
  - Purpose: Indexed class `ProvenanceGraph` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:39-47]
- `ProvenanceGraph` (class) component `ProvenanceGraph [class]` (`8a87dafd-6c72-5a5f-85e6-3f55202ad3ec`) lines 49-168 [crates/gwiki/src/provenance.rs:49-168]
  - Signature: `impl ProvenanceGraph {`
  - Purpose: Indexed class `ProvenanceGraph` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:49-168]
- `ProvenanceGraph.add_link` (method) component `ProvenanceGraph.add_link [method]` (`fa37e1f2-1d85-5192-a172-579bce453d62`) lines 50-68 [crates/gwiki/src/provenance.rs:50-68]
  - Signature: `pub fn add_link(&mut self, link: ProvenanceLink) {`
  - Purpose: Indexed method `ProvenanceGraph.add_link` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:50-68]
- `ProvenanceGraph.links_for_section` (method) component `ProvenanceGraph.links_for_section [method]` (`9a3f8f39-55d3-59c6-a4d3-3c9083e5a709`) lines 71-78 [crates/gwiki/src/provenance.rs:71-78]
  - Signature: `pub fn links_for_section(&self, section_id: &str) -> Vec<&ProvenanceLink> {`
  - Purpose: Indexed method `ProvenanceGraph.links_for_section` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:71-78]
- `ProvenanceGraph.links_for_page_section` (method) component `ProvenanceGraph.links_for_page_section [method]` (`6fd439b3-7c9c-594e-b725-ea7d5b1a1b17`) lines 80-91 [crates/gwiki/src/provenance.rs:80-91]
  - Signature: `pub fn links_for_page_section(`
  - Purpose: Indexed method `ProvenanceGraph.links_for_page_section` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:80-91]
- `ProvenanceGraph.links_for_source` (method) component `ProvenanceGraph.links_for_source [method]` (`3d3af56f-3f39-588c-8408-a2016631831b`) lines 93-100 [crates/gwiki/src/provenance.rs:93-100]
  - Signature: `pub fn links_for_source(&self, source_id: &str) -> Vec<&ProvenanceLink> {`
  - Purpose: Indexed method `ProvenanceGraph.links_for_source` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:93-100]
- `ProvenanceGraph.links` (method) component `ProvenanceGraph.links [method]` (`59be75eb-5df6-5465-bc3f-8b5afadba396`) lines 102-104 [crates/gwiki/src/provenance.rs:102-104]
  - Signature: `pub fn links(&self) -> &[ProvenanceLink] {`
  - Purpose: Indexed method `ProvenanceGraph.links` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:102-104]
- `ProvenanceGraph.save_to_vault` (method) component `ProvenanceGraph.save_to_vault [method]` (`b8f1fdd6-6484-5e25-829d-fc3b4ba74689`) lines 106-120 [crates/gwiki/src/provenance.rs:106-120]
  - Signature: `pub fn save_to_vault(&self, vault_root: &std::path::Path) -> Result<(), WikiError> {`
  - Purpose: Indexed method `ProvenanceGraph.save_to_vault` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:106-120]
- `ProvenanceGraph.load_from_vault` (method) component `ProvenanceGraph.load_from_vault [method]` (`446fabec-31a7-5ad0-9b56-2c8da2def08c`) lines 122-144 [crates/gwiki/src/provenance.rs:122-144]
  - Signature: `pub fn load_from_vault(vault_root: &std::path::Path) -> Result<Self, WikiError> {`
  - Purpose: Indexed method `ProvenanceGraph.load_from_vault` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:122-144]
- `ProvenanceGraph.rebuild_indexes` (method) component `ProvenanceGraph.rebuild_indexes [method]` (`86568a02-3afb-5678-880b-e7a68638fcf9`) lines 146-167 [crates/gwiki/src/provenance.rs:146-167]
  - Signature: `fn rebuild_indexes(&mut self) {`
  - Purpose: Indexed method `ProvenanceGraph.rebuild_indexes` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:146-167]
- `page_section_key` (function) component `page_section_key [function]` (`655593cc-70db-5c52-814f-de7e0529773b`) lines 170-172 [crates/gwiki/src/provenance.rs:170-172]
  - Signature: `fn page_section_key(page_path: &Path, section_id: &str) -> String {`
  - Purpose: Indexed function `page_section_key` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:170-172]
- `write_provenance_json_durably` (function) component `write_provenance_json_durably [function]` (`41e8dcb9-66ba-5fcf-9bda-02ae3bfae947`) lines 174-205 [crates/gwiki/src/provenance.rs:174-205]
  - Signature: `fn write_provenance_json_durably(`
  - Purpose: Indexed function `write_provenance_json_durably` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:174-205]
- `sync_provenance_dir` (function) component `sync_provenance_dir [function]` (`83e75adf-da8a-58d2-a938-e701d77c8ebb`) lines 207-223 [crates/gwiki/src/provenance.rs:207-223]
  - Signature: `fn sync_provenance_dir(meta_dir: &std::path::Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `sync_provenance_dir` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:207-223]
- `links_sources_to_sections` (function) component `links_sources_to_sections [function]` (`f601353d-ce31-54c8-a3fd-95623cfd9a1d`) lines 230-278 [crates/gwiki/src/provenance.rs:230-278]
  - Signature: `fn links_sources_to_sections() {`
  - Purpose: Indexed function `links_sources_to_sections` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:230-278]
- `saves_and_loads_vault_roundtrip` (function) component `saves_and_loads_vault_roundtrip [function]` (`fe446f60-9481-5880-9011-b877698759a3`) lines 281-304 [crates/gwiki/src/provenance.rs:281-304]
  - Signature: `fn saves_and_loads_vault_roundtrip() {`
  - Purpose: Indexed function `saves_and_loads_vault_roundtrip` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:281-304]
- `missing_provenance_file_loads_empty_graph` (function) component `missing_provenance_file_loads_empty_graph [function]` (`9c8e12fe-c50c-5505-a071-fd1aadcc8f9e`) lines 307-313 [crates/gwiki/src/provenance.rs:307-313]
  - Signature: `fn missing_provenance_file_loads_empty_graph() {`
  - Purpose: Indexed function `missing_provenance_file_loads_empty_graph` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:307-313]

