---
title: crates/gcode/src/commands/codewiki/run.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/run.rs
  ranges:
  - 22-186
  - 188-193
  - 198-200
  - 204-206
  - 208-215
  - 220-266
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/run.rs:22-186](crates/gcode/src/commands/codewiki/run.rs#L22-L186), [crates/gcode/src/commands/codewiki/run.rs:188-193](crates/gcode/src/commands/codewiki/run.rs#L188-L193), [crates/gcode/src/commands/codewiki/run.rs:198-200](crates/gcode/src/commands/codewiki/run.rs#L198-L200), [crates/gcode/src/commands/codewiki/run.rs:204-206](crates/gcode/src/commands/codewiki/run.rs#L204-L206), [crates/gcode/src/commands/codewiki/run.rs:208-215](crates/gcode/src/commands/codewiki/run.rs#L208-L215), [crates/gcode/src/commands/codewiki/run.rs:220-266](crates/gcode/src/commands/codewiki/run.rs#L220-L266)

</details>

# crates/gcode/src/commands/codewiki/run.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file implements the `codewiki` command pipeline. `run` validates the edge limit, sets up progress reporting and a readonly DB connection, normalizes and scopes the requested file paths, filters visible files to those that should be documented, loads the relevant symbols, leading content chunks, and graph edges, then packages everything into a `CodewikiInput` for downstream generation and output. The helper functions split that work into focused steps: `validate_edge_limit` enforces the configured graph size cap, `documents_file` and `should_document_file` decide which paths belong in the documentation set, `load_symbols_for_codewiki` fetches symbols for the selected files, and `load_leading_chunks` gathers the initial file content needed to build the docs.
[crates/gcode/src/commands/codewiki/run.rs:22-186]
[crates/gcode/src/commands/codewiki/run.rs:188-193]
[crates/gcode/src/commands/codewiki/run.rs:198-200]
[crates/gcode/src/commands/codewiki/run.rs:204-206]
[crates/gcode/src/commands/codewiki/run.rs:208-215]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `run` | function | `pub fn run(` | `run [function]` | `a1ca5475-303f-56f8-9f3e-b67a2a320a49` | 22-186 [crates/gcode/src/commands/codewiki/run.rs:22-186] | Indexed function `run` in `crates/gcode/src/commands/codewiki/run.rs`. [crates/gcode/src/commands/codewiki/run.rs:22-186] |
| `validate_edge_limit` | function | `pub(crate) fn validate_edge_limit(edge_limit: usize) -> anyhow::Result<()> {` | `validate_edge_limit [function]` | `44cd3029-0419-594d-b244-bfe317961952` | 188-193 [crates/gcode/src/commands/codewiki/run.rs:188-193] | Indexed function `validate_edge_limit` in `crates/gcode/src/commands/codewiki/run.rs`. [crates/gcode/src/commands/codewiki/run.rs:188-193] |
| `documents_file` | function | `fn documents_file(file_path: &str) -> bool {` | `documents_file [function]` | `d55d19d4-1102-5a6d-90df-433edf040936` | 198-200 [crates/gcode/src/commands/codewiki/run.rs:198-200] | Indexed function `documents_file` in `crates/gcode/src/commands/codewiki/run.rs`. [crates/gcode/src/commands/codewiki/run.rs:198-200] |
| `should_document_file` | function | `pub(crate) fn should_document_file(file_path: &str, include_docs: bool) -> bool {` | `should_document_file [function]` | `047568ab-a97a-5cc9-ad62-05261b3df3e7` | 204-206 [crates/gcode/src/commands/codewiki/run.rs:204-206] | Indexed function `should_document_file` in `crates/gcode/src/commands/codewiki/run.rs`. [crates/gcode/src/commands/codewiki/run.rs:204-206] |
| `load_symbols_for_codewiki` | function | `pub(crate) fn load_symbols_for_codewiki(` | `load_symbols_for_codewiki [function]` | `cca5bdb4-2c1a-52a5-b898-fd0e22d8a124` | 208-215 [crates/gcode/src/commands/codewiki/run.rs:208-215] | Indexed function `load_symbols_for_codewiki` in `crates/gcode/src/commands/codewiki/run.rs`. [crates/gcode/src/commands/codewiki/run.rs:208-215] |
| `load_leading_chunks` | function | `fn load_leading_chunks(` | `load_leading_chunks [function]` | `0bbf118d-cc4b-5561-a44c-d34f79006439` | 220-266 [crates/gcode/src/commands/codewiki/run.rs:220-266] | Indexed function `load_leading_chunks` in `crates/gcode/src/commands/codewiki/run.rs`. [crates/gcode/src/commands/codewiki/run.rs:220-266] |
