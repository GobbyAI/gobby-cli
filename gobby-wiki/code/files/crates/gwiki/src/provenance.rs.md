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
  - 50-68
  - 71-78
  - 80-91
  - 93-100
  - 102-104
  - 106-120
  - 122-144
  - 146-167
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/provenance.rs:14-22](crates/gwiki/src/provenance.rs#L14-L22), [crates/gwiki/src/provenance.rs:25-29](crates/gwiki/src/provenance.rs#L25-L29), [crates/gwiki/src/provenance.rs:32-36](crates/gwiki/src/provenance.rs#L32-L36), [crates/gwiki/src/provenance.rs:39-47](crates/gwiki/src/provenance.rs#L39-L47), [crates/gwiki/src/provenance.rs:50-68](crates/gwiki/src/provenance.rs#L50-L68), [crates/gwiki/src/provenance.rs:71-78](crates/gwiki/src/provenance.rs#L71-L78), [crates/gwiki/src/provenance.rs:80-91](crates/gwiki/src/provenance.rs#L80-L91), [crates/gwiki/src/provenance.rs:93-100](crates/gwiki/src/provenance.rs#L93-L100), [crates/gwiki/src/provenance.rs:102-104](crates/gwiki/src/provenance.rs#L102-L104), [crates/gwiki/src/provenance.rs:106-120](crates/gwiki/src/provenance.rs#L106-L120), [crates/gwiki/src/provenance.rs:122-144](crates/gwiki/src/provenance.rs#L122-L144), [crates/gwiki/src/provenance.rs:146-167](crates/gwiki/src/provenance.rs#L146-L167), [crates/gwiki/src/provenance.rs:170-172](crates/gwiki/src/provenance.rs#L170-L172), [crates/gwiki/src/provenance.rs:174-205](crates/gwiki/src/provenance.rs#L174-L205), [crates/gwiki/src/provenance.rs:207-223](crates/gwiki/src/provenance.rs#L207-L223), [crates/gwiki/src/provenance.rs:230-278](crates/gwiki/src/provenance.rs#L230-L278), [crates/gwiki/src/provenance.rs:281-304](crates/gwiki/src/provenance.rs#L281-L304), [crates/gwiki/src/provenance.rs:307-313](crates/gwiki/src/provenance.rs#L307-L313)

</details>

# crates/gwiki/src/provenance.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the provenance model for gwiki, tracking links from raw source chunks to synthesized wiki sections. `SourceChunkRef`, `WikiSectionRef`, and `ProvenanceLink` are serializable record types, and `ProvenanceGraph` stores the links plus in-memory indexes for fast lookup by section, page/section pair, or source. Its methods add links while maintaining those indexes, query links through the different keys, and persist or restore the graph from the vault using durable JSON writes and index rebuilding after load. The helper functions support stable page/section keys and safe file syncing, and the tests exercise source-to-section linking, round-trip save/load behavior, and loading when the provenance file is missing.
[crates/gwiki/src/provenance.rs:14-22]
[crates/gwiki/src/provenance.rs:25-29]
[crates/gwiki/src/provenance.rs:32-36]
[crates/gwiki/src/provenance.rs:39-47]
[crates/gwiki/src/provenance.rs:50-68]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SourceChunkRef` | class | `pub struct SourceChunkRef {` | `SourceChunkRef [class]` | `1d92784d-2c74-5e0f-82c1-df8b8e2f23d7` | 14-22 [crates/gwiki/src/provenance.rs:14-22] | Indexed class `SourceChunkRef` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:14-22] |
| `WikiSectionRef` | class | `pub struct WikiSectionRef {` | `WikiSectionRef [class]` | `a9b9e35f-7dfe-537e-b98f-6d7675ea04af` | 25-29 [crates/gwiki/src/provenance.rs:25-29] | Indexed class `WikiSectionRef` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:25-29] |
| `ProvenanceLink` | class | `pub struct ProvenanceLink {` | `ProvenanceLink [class]` | `71f6214a-0988-580d-ac48-35088e3313a6` | 32-36 [crates/gwiki/src/provenance.rs:32-36] | Indexed class `ProvenanceLink` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:32-36] |
| `ProvenanceGraph` | class | `pub struct ProvenanceGraph {` | `ProvenanceGraph [class]` | `498890e2-7252-5bc3-b2fa-624e1e9f486c` | 39-47 [crates/gwiki/src/provenance.rs:39-47] | Indexed class `ProvenanceGraph` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:39-47] |
| `ProvenanceGraph::add_link` | method | `pub fn add_link(&mut self, link: ProvenanceLink) {` | `ProvenanceGraph::add_link [method]` | `fa37e1f2-1d85-5192-a172-579bce453d62` | 50-68 [crates/gwiki/src/provenance.rs:50-68] | Indexed method `ProvenanceGraph::add_link` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:50-68] |
| `ProvenanceGraph::links_for_section` | method | `pub fn links_for_section(&self, section_id: &str) -> Vec<&ProvenanceLink> {` | `ProvenanceGraph::links_for_section [method]` | `9a3f8f39-55d3-59c6-a4d3-3c9083e5a709` | 71-78 [crates/gwiki/src/provenance.rs:71-78] | Indexed method `ProvenanceGraph::links_for_section` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:71-78] |
| `ProvenanceGraph::links_for_page_section` | method | `pub fn links_for_page_section(` | `ProvenanceGraph::links_for_page_section [method]` | `6fd439b3-7c9c-594e-b725-ea7d5b1a1b17` | 80-91 [crates/gwiki/src/provenance.rs:80-91] | Indexed method `ProvenanceGraph::links_for_page_section` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:80-91] |
| `ProvenanceGraph::links_for_source` | method | `pub fn links_for_source(&self, source_id: &str) -> Vec<&ProvenanceLink> {` | `ProvenanceGraph::links_for_source [method]` | `3d3af56f-3f39-588c-8408-a2016631831b` | 93-100 [crates/gwiki/src/provenance.rs:93-100] | Indexed method `ProvenanceGraph::links_for_source` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:93-100] |
| `ProvenanceGraph::links` | method | `pub fn links(&self) -> &[ProvenanceLink] {` | `ProvenanceGraph::links [method]` | `59be75eb-5df6-5465-bc3f-8b5afadba396` | 102-104 [crates/gwiki/src/provenance.rs:102-104] | Indexed method `ProvenanceGraph::links` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:102-104] |
| `ProvenanceGraph::save_to_vault` | method | `pub fn save_to_vault(&self, vault_root: &std::path::Path) -> Result<(), WikiError> {` | `ProvenanceGraph::save_to_vault [method]` | `b8f1fdd6-6484-5e25-829d-fc3b4ba74689` | 106-120 [crates/gwiki/src/provenance.rs:106-120] | Indexed method `ProvenanceGraph::save_to_vault` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:106-120] |
| `ProvenanceGraph::load_from_vault` | method | `pub fn load_from_vault(vault_root: &std::path::Path) -> Result<Self, WikiError> {` | `ProvenanceGraph::load_from_vault [method]` | `446fabec-31a7-5ad0-9b56-2c8da2def08c` | 122-144 [crates/gwiki/src/provenance.rs:122-144] | Indexed method `ProvenanceGraph::load_from_vault` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:122-144] |
| `ProvenanceGraph::rebuild_indexes` | method | `fn rebuild_indexes(&mut self) {` | `ProvenanceGraph::rebuild_indexes [method]` | `86568a02-3afb-5678-880b-e7a68638fcf9` | 146-167 [crates/gwiki/src/provenance.rs:146-167] | Indexed method `ProvenanceGraph::rebuild_indexes` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:146-167] |
| `page_section_key` | function | `fn page_section_key(page_path: &Path, section_id: &str) -> String {` | `page_section_key [function]` | `655593cc-70db-5c52-814f-de7e0529773b` | 170-172 [crates/gwiki/src/provenance.rs:170-172] | Indexed function `page_section_key` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:170-172] |
| `write_provenance_json_durably` | function | `fn write_provenance_json_durably(` | `write_provenance_json_durably [function]` | `41e8dcb9-66ba-5fcf-9bda-02ae3bfae947` | 174-205 [crates/gwiki/src/provenance.rs:174-205] | Indexed function `write_provenance_json_durably` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:174-205] |
| `sync_provenance_dir` | function | `fn sync_provenance_dir(meta_dir: &std::path::Path) -> Result<(), WikiError> {` | `sync_provenance_dir [function]` | `83e75adf-da8a-58d2-a938-e701d77c8ebb` | 207-223 [crates/gwiki/src/provenance.rs:207-223] | Indexed function `sync_provenance_dir` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:207-223] |
| `links_sources_to_sections` | function | `fn links_sources_to_sections() {` | `links_sources_to_sections [function]` | `f601353d-ce31-54c8-a3fd-95623cfd9a1d` | 230-278 [crates/gwiki/src/provenance.rs:230-278] | Indexed function `links_sources_to_sections` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:230-278] |
| `saves_and_loads_vault_roundtrip` | function | `fn saves_and_loads_vault_roundtrip() {` | `saves_and_loads_vault_roundtrip [function]` | `fe446f60-9481-5880-9011-b877698759a3` | 281-304 [crates/gwiki/src/provenance.rs:281-304] | Indexed function `saves_and_loads_vault_roundtrip` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:281-304] |
| `missing_provenance_file_loads_empty_graph` | function | `fn missing_provenance_file_loads_empty_graph() {` | `missing_provenance_file_loads_empty_graph [function]` | `9c8e12fe-c50c-5505-a071-fd1aadcc8f9e` | 307-313 [crates/gwiki/src/provenance.rs:307-313] | Indexed function `missing_provenance_file_loads_empty_graph` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:307-313] |
