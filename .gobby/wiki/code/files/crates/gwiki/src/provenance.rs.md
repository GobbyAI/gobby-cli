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
  - 49-167
  - 50-68
  - 70-77
  - 79-90
  - 92-99
  - 101-103
  - 105-119
  - 121-143
  - 145-166
  - 169-171
  - 173-204
  - 206-222
  - 229-277
  - 280-303
  - 306-312
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
[crates/gwiki/src/provenance.rs:49-167]

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
- `ProvenanceGraph` (class) component `ProvenanceGraph [class]` (`8a87dafd-6c72-5a5f-85e6-3f55202ad3ec`) lines 49-167 [crates/gwiki/src/provenance.rs:49-167]
  - Signature: `impl ProvenanceGraph {`
  - Purpose: Indexed class `ProvenanceGraph` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:49-167]
- `ProvenanceGraph.add_link` (method) component `ProvenanceGraph.add_link [method]` (`fa37e1f2-1d85-5192-a172-579bce453d62`) lines 50-68 [crates/gwiki/src/provenance.rs:50-68]
  - Signature: `pub fn add_link(&mut self, link: ProvenanceLink) {`
  - Purpose: Indexed method `ProvenanceGraph.add_link` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:50-68]
- `ProvenanceGraph.links_for_section` (method) component `ProvenanceGraph.links_for_section [method]` (`2cc2cda8-f217-5930-a0c5-3489310cfa33`) lines 70-77 [crates/gwiki/src/provenance.rs:70-77]
  - Signature: `pub fn links_for_section(&self, section_id: &str) -> Vec<&ProvenanceLink> {`
  - Purpose: Indexed method `ProvenanceGraph.links_for_section` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:70-77]
- `ProvenanceGraph.links_for_page_section` (method) component `ProvenanceGraph.links_for_page_section [method]` (`d96873aa-996b-51a7-ba70-389549755070`) lines 79-90 [crates/gwiki/src/provenance.rs:79-90]
  - Signature: `pub fn links_for_page_section(`
  - Purpose: Indexed method `ProvenanceGraph.links_for_page_section` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:79-90]
- `ProvenanceGraph.links_for_source` (method) component `ProvenanceGraph.links_for_source [method]` (`233acaf0-d628-5814-8dc0-63b41914e18c`) lines 92-99 [crates/gwiki/src/provenance.rs:92-99]
  - Signature: `pub fn links_for_source(&self, source_id: &str) -> Vec<&ProvenanceLink> {`
  - Purpose: Indexed method `ProvenanceGraph.links_for_source` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:92-99]
- `ProvenanceGraph.links` (method) component `ProvenanceGraph.links [method]` (`ecb073bf-4d8f-5ad8-865d-7d073ef39674`) lines 101-103 [crates/gwiki/src/provenance.rs:101-103]
  - Signature: `pub fn links(&self) -> &[ProvenanceLink] {`
  - Purpose: Indexed method `ProvenanceGraph.links` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:101-103]
- `ProvenanceGraph.save_to_vault` (method) component `ProvenanceGraph.save_to_vault [method]` (`b4a472bc-fab1-59ae-8ab3-ae55432da0a9`) lines 105-119 [crates/gwiki/src/provenance.rs:105-119]
  - Signature: `pub fn save_to_vault(&self, vault_root: &std::path::Path) -> Result<(), WikiError> {`
  - Purpose: Indexed method `ProvenanceGraph.save_to_vault` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:105-119]
- `ProvenanceGraph.load_from_vault` (method) component `ProvenanceGraph.load_from_vault [method]` (`b4371763-4b0d-5d58-9c94-e94387df251e`) lines 121-143 [crates/gwiki/src/provenance.rs:121-143]
  - Signature: `pub fn load_from_vault(vault_root: &std::path::Path) -> Result<Self, WikiError> {`
  - Purpose: Indexed method `ProvenanceGraph.load_from_vault` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:121-143]
- `ProvenanceGraph.rebuild_indexes` (method) component `ProvenanceGraph.rebuild_indexes [method]` (`8109f603-70f6-539f-a727-fe2f7abdd5d9`) lines 145-166 [crates/gwiki/src/provenance.rs:145-166]
  - Signature: `fn rebuild_indexes(&mut self) {`
  - Purpose: Indexed method `ProvenanceGraph.rebuild_indexes` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:145-166]
- `page_section_key` (function) component `page_section_key [function]` (`ade31f15-b434-52eb-a7a5-b30b5a06feb4`) lines 169-171 [crates/gwiki/src/provenance.rs:169-171]
  - Signature: `fn page_section_key(page_path: &Path, section_id: &str) -> String {`
  - Purpose: Indexed function `page_section_key` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:169-171]
- `write_provenance_json_durably` (function) component `write_provenance_json_durably [function]` (`361e0bd1-eb77-5f69-9e7d-a77e563dc096`) lines 173-204 [crates/gwiki/src/provenance.rs:173-204]
  - Signature: `fn write_provenance_json_durably(`
  - Purpose: Indexed function `write_provenance_json_durably` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:173-204]
- `sync_provenance_dir` (function) component `sync_provenance_dir [function]` (`b0e24c0f-fcb0-5d1c-b253-e51b05be5c62`) lines 206-222 [crates/gwiki/src/provenance.rs:206-222]
  - Signature: `fn sync_provenance_dir(meta_dir: &std::path::Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `sync_provenance_dir` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:206-222]
- `links_sources_to_sections` (function) component `links_sources_to_sections [function]` (`fe70e52c-7d11-5c29-9cce-ed78f3c14897`) lines 229-277 [crates/gwiki/src/provenance.rs:229-277]
  - Signature: `fn links_sources_to_sections() {`
  - Purpose: Indexed function `links_sources_to_sections` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:229-277]
- `saves_and_loads_vault_roundtrip` (function) component `saves_and_loads_vault_roundtrip [function]` (`ea9c82a4-6bf2-592e-aa33-a45d4a39bc10`) lines 280-303 [crates/gwiki/src/provenance.rs:280-303]
  - Signature: `fn saves_and_loads_vault_roundtrip() {`
  - Purpose: Indexed function `saves_and_loads_vault_roundtrip` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:280-303]
- `missing_provenance_file_loads_empty_graph` (function) component `missing_provenance_file_loads_empty_graph [function]` (`4f6c2361-54ea-554d-b508-267bc0d27ab8`) lines 306-312 [crates/gwiki/src/provenance.rs:306-312]
  - Signature: `fn missing_provenance_file_loads_empty_graph() {`
  - Purpose: Indexed function `missing_provenance_file_loads_empty_graph` in `crates/gwiki/src/provenance.rs`. [crates/gwiki/src/provenance.rs:306-312]

