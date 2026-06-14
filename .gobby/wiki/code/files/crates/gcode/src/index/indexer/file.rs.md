---
title: crates/gcode/src/index/indexer/file.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/file.rs
  ranges:
  - 15-91
  - 93-108
  - 111-115
  - 117-127
  - 130-177
  - 179-229
  - 231-264
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/file.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file implements the core file-level indexing logic for a code analysis system. The main `index_file` function orchestrates parsing, language detection, content hashing, and metadata collection for individual files, then persists the extracted facts to PostgreSQL through a transactional sink. Supporting functions handle semantic resolver setup (`create_semantic_resolver_if_needed`), explicit file routing configuration (`ExplicitFileRoute` and `explicit_file_route`), content-only indexing workflows (`index_content_only`), and database writes for both fully parsed results (`write_parsed_file_facts`) and content-only variants (`write_content_only_file_facts`).
[crates/gcode/src/index/indexer/file.rs:15-91]
[crates/gcode/src/index/indexer/file.rs:93-108]
[crates/gcode/src/index/indexer/file.rs:111-115]
[crates/gcode/src/index/indexer/file.rs:117-127]
[crates/gcode/src/index/indexer/file.rs:130-177]

## API Symbols

- `index_file` (function) component `index_file [function]` (`4b12832a-8119-5965-b9c6-d91d8cb4122e`) lines 15-91 [crates/gcode/src/index/indexer/file.rs:15-91]
  - Signature: `pub(super) fn index_file(`
  - Purpose: Indexed function `index_file` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:15-91]
- `create_semantic_resolver_if_needed` (function) component `create_semantic_resolver_if_needed [function]` (`c13ce350-3af8-5341-ba85-f91321f40cb2`) lines 93-108 [crates/gcode/src/index/indexer/file.rs:93-108]
  - Signature: `pub(super) fn create_semantic_resolver_if_needed(`
  - Purpose: Indexed function `create_semantic_resolver_if_needed` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:93-108]
- `ExplicitFileRoute` (type) component `ExplicitFileRoute [type]` (`e0425afb-6091-5f4b-8ed8-0077a7cbdbc8`) lines 111-115 [crates/gcode/src/index/indexer/file.rs:111-115]
  - Signature: `pub(super) enum ExplicitFileRoute {`
  - Purpose: Indexed type `ExplicitFileRoute` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:111-115]
- `explicit_file_route` (function) component `explicit_file_route [function]` (`a46733a5-8a30-596e-a98c-6214e9693bde`) lines 117-127 [crates/gcode/src/index/indexer/file.rs:117-127]
  - Signature: `pub(super) fn explicit_file_route(`
  - Purpose: Indexed function `explicit_file_route` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:117-127]
- `index_content_only` (function) component `index_content_only [function]` (`b07b2215-4ef6-53de-9d92-eef5f90e3aec`) lines 130-177 [crates/gcode/src/index/indexer/file.rs:130-177]
  - Signature: `pub(super) fn index_content_only(`
  - Purpose: Indexed function `index_content_only` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:130-177]
- `write_parsed_file_facts` (function) component `write_parsed_file_facts [function]` (`8db19430-dba8-52b8-b94c-ebd14b9c1b71`) lines 179-229 [crates/gcode/src/index/indexer/file.rs:179-229]
  - Signature: `pub(super) fn write_parsed_file_facts(`
  - Purpose: Indexed function `write_parsed_file_facts` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:179-229]
- `write_content_only_file_facts` (function) component `write_content_only_file_facts [function]` (`30dacd9b-2dd5-5b96-ae60-f434036b7dca`) lines 231-264 [crates/gcode/src/index/indexer/file.rs:231-264]
  - Signature: `pub(super) fn write_content_only_file_facts(`
  - Purpose: Indexed function `write_content_only_file_facts` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:231-264]

