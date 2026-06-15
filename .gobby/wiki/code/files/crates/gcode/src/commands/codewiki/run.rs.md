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

# crates/gcode/src/commands/codewiki/run.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Orchestrates the `codewiki` command: it validates the edge limit, opens the readonly database, filters visible files by document support and user scope, loads symbols and leading content chunks, fetches graph edges, then bundles everything into a `CodewikiInput` and configures the text generator and output destination for document generation. The helpers split that flow into small steps: `validate_edge_limit` enforces bounds, `documents_file` and `should_document_file` decide which files to include, `load_symbols_for_codewiki` wraps symbol collection with progress reporting, and `load_leading_chunks` gathers the first content chunk per file for inclusion in the generated wiki.
[crates/gcode/src/commands/codewiki/run.rs:22-186]
[crates/gcode/src/commands/codewiki/run.rs:188-193]
[crates/gcode/src/commands/codewiki/run.rs:198-200]
[crates/gcode/src/commands/codewiki/run.rs:204-206]
[crates/gcode/src/commands/codewiki/run.rs:208-215]

## API Symbols

- `run` (function) component `run [function]` (`a1ca5475-303f-56f8-9f3e-b67a2a320a49`) lines 22-186 [crates/gcode/src/commands/codewiki/run.rs:22-186]
  - Signature: `pub fn run(`
  - Purpose: Orchestrates codewiki generation by validating the edge limit, collecting scoped visible files, symbols, leading content, and graph edges from the readonly database, then assembling a 'CodewikiInput' and configuring the text generator/output destination for document emission. [crates/gcode/src/commands/codewiki/run.rs:22-186]
- `validate_edge_limit` (function) component `validate_edge_limit [function]` (`44cd3029-0419-594d-b244-bfe317961952`) lines 188-193 [crates/gcode/src/commands/codewiki/run.rs:188-193]
  - Signature: `pub(crate) fn validate_edge_limit(edge_limit: usize) -> anyhow::Result<()> {`
  - Purpose: Returns 'Ok(())' only when 'edge_limit' is within the inclusive range '1..=MAX_EDGE_LIMIT', otherwise bails with an 'anyhow' error stating the allowed bounds and the provided value. [crates/gcode/src/commands/codewiki/run.rs:188-193]
- `documents_file` (function) component `documents_file [function]` (`d55d19d4-1102-5a6d-90df-433edf040936`) lines 198-200 [crates/gcode/src/commands/codewiki/run.rs:198-200]
  - Signature: `fn documents_file(file_path: &str) -> bool {`
  - Purpose: Returns 'true' when 'crate::index::languages::detect_language(file_path)' recognizes the path as belonging to a supported document language, and 'false' otherwise. [crates/gcode/src/commands/codewiki/run.rs:198-200]
- `should_document_file` (function) component `should_document_file [function]` (`047568ab-a97a-5cc9-ad62-05261b3df3e7`) lines 204-206 [crates/gcode/src/commands/codewiki/run.rs:204-206]
  - Signature: `pub(crate) fn should_document_file(file_path: &str, include_docs: bool) -> bool {`
  - Purpose: Returns 'true' when 'include_docs' is enabled or when 'file_path' matches 'documents_file(file_path)', otherwise 'false'. [crates/gcode/src/commands/codewiki/run.rs:204-206]
- `load_symbols_for_codewiki` (function) component `load_symbols_for_codewiki [function]` (`cca5bdb4-2c1a-52a5-b898-fd0e22d8a124`) lines 208-215 [crates/gcode/src/commands/codewiki/run.rs:208-215]
  - Signature: `pub(crate) fn load_symbols_for_codewiki(`
  - Purpose: Emits a progress message reporting the number of input files, then invokes the provided 'load_symbols' callback with those file paths and returns its 'Vec<Symbol>' result. [crates/gcode/src/commands/codewiki/run.rs:208-215]
- `load_leading_chunks` (function) component `load_leading_chunks [function]` (`0bbf118d-cc4b-5561-a44c-d34f79006439`) lines 220-266 [crates/gcode/src/commands/codewiki/run.rs:220-266]
  - Signature: `fn load_leading_chunks(`
  - Purpose: 'load_leading_chunks' queries 'code_content_chunks' for the first chunk ('chunk_index = 0') of the requested files across the current project scope, preferring the first found entry per file and returning them as a 'BTreeMap<String, LeadingChunk>' keyed by file path. [crates/gcode/src/commands/codewiki/run.rs:220-266]

