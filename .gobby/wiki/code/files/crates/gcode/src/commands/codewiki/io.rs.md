---
title: crates/gcode/src/commands/codewiki/io.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/io.rs
  ranges:
  - 3-9
  - 11-17
  - 19-69
  - 71-79
  - 81-99
  - 101-121
  - 123-130
  - 132-135
  - 137-144
  - 146-149
  - 151-172
  - 174-207
  - 210-240
  - 243-250
  - 252-262
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/io.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/io.rs` exposes 15 indexed API symbols.
[crates/gcode/src/commands/codewiki/io.rs:3-9] [crates/gcode/src/commands/codewiki/io.rs:11-17] [crates/gcode/src/commands/codewiki/io.rs:19-69] [crates/gcode/src/commands/codewiki/io.rs:71-79]
[crates/gcode/src/commands/codewiki/io.rs:81-99] [crates/gcode/src/commands/codewiki/io.rs:101-121] [crates/gcode/src/commands/codewiki/io.rs:123-130] [crates/gcode/src/commands/codewiki/io.rs:132-135]
[crates/gcode/src/commands/codewiki/io.rs:137-144] [crates/gcode/src/commands/codewiki/io.rs:146-149] [crates/gcode/src/commands/codewiki/io.rs:151-172] [crates/gcode/src/commands/codewiki/io.rs:174-207]
[crates/gcode/src/commands/codewiki/io.rs:210-240] [crates/gcode/src/commands/codewiki/io.rs:243-250] [crates/gcode/src/commands/codewiki/io.rs:252-262]

## API Symbols

- `write_doc_set` (function) component `write_doc_set [function]` (`da03a0d9-08a1-5f2c-848f-855e55517a86`) lines 3-9 [crates/gcode/src/commands/codewiki/io.rs:3-9]
  - Signature: `pub fn write_doc_set(out_dir: &Path, docs: &[(String, String)]) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:3-9]
- `write_incremental_doc_set` (function) component `write_incremental_doc_set [function]` (`fa8a9d60-b906-5015-bfaa-0440a7025e2d`) lines 11-17 [crates/gcode/src/commands/codewiki/io.rs:11-17]
  - Signature: `pub fn write_incremental_doc_set(`
  - Purpose: Indexed function `write_incremental_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:11-17]
- `write_incremental_doc_set_with_snapshot` (function) component `write_incremental_doc_set_with_snapshot [function]` (`e7519bc0-f758-5d62-885b-56ccf85cc427`) lines 19-69 [crates/gcode/src/commands/codewiki/io.rs:19-69]
  - Signature: `pub(crate) fn write_incremental_doc_set_with_snapshot(`
  - Purpose: Indexed function `write_incremental_doc_set_with_snapshot` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:19-69]
- `write_doc` (function) component `write_doc [function]` (`23797dbc-db9c-5de9-8b8a-49a776d92da2`) lines 71-79 [crates/gcode/src/commands/codewiki/io.rs:71-79]
  - Signature: `pub(crate) fn write_doc(out_dir: &Path, relative_path: &str, content: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:71-79]
- `reject_symlinked_doc_path` (function) component `reject_symlinked_doc_path [function]` (`159ac265-551e-5c95-8d36-b65b7fb85eb2`) lines 81-99 [crates/gcode/src/commands/codewiki/io.rs:81-99]
  - Signature: `pub(crate) fn reject_symlinked_doc_path(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed function `reject_symlinked_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:81-99]
- `prune_empty_doc_dirs` (function) component `prune_empty_doc_dirs [function]` (`459f2a74-d6fd-5df9-afa2-2d6e02257948`) lines 101-121 [crates/gcode/src/commands/codewiki/io.rs:101-121]
  - Signature: `pub(crate) fn prune_empty_doc_dirs(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed function `prune_empty_doc_dirs` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:101-121]
- `read_codewiki_meta` (function) component `read_codewiki_meta [function]` (`3db6cdd0-a12d-5c54-8d4b-c4bab07b1880`) lines 123-130 [crates/gcode/src/commands/codewiki/io.rs:123-130]
  - Signature: `pub(crate) fn read_codewiki_meta(out_dir: &Path) -> anyhow::Result<CodewikiMeta> {`
  - Purpose: Indexed function `read_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:123-130]
- `write_codewiki_meta` (function) component `write_codewiki_meta [function]` (`7c34bf5c-55e3-513d-aa43-326a859ca342`) lines 132-135 [crates/gcode/src/commands/codewiki/io.rs:132-135]
  - Signature: `pub(crate) fn write_codewiki_meta(out_dir: &Path, meta: &CodewikiMeta) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:132-135]
- `read_ownership_meta` (function) component `read_ownership_meta [function]` (`a26b893f-a0d9-5f5e-82e3-08b0f1e03e26`) lines 137-144 [crates/gcode/src/commands/codewiki/io.rs:137-144]
  - Signature: `pub(crate) fn read_ownership_meta(out_dir: &Path) -> anyhow::Result<OwnershipMeta> {`
  - Purpose: Indexed function `read_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:137-144]
- `write_ownership_meta` (function) component `write_ownership_meta [function]` (`d82ab49b-4aa8-59cc-838b-65151b4cc898`) lines 146-149 [crates/gcode/src/commands/codewiki/io.rs:146-149]
  - Signature: `pub(crate) fn write_ownership_meta(out_dir: &Path, meta: &OwnershipMeta) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:146-149]
- `source_hashes_for_doc` (function) component `source_hashes_for_doc [function]` (`9de18ac6-b61b-5c36-91f0-8982fd20c2b8`) lines 151-172 [crates/gcode/src/commands/codewiki/io.rs:151-172]
  - Signature: `pub(crate) fn source_hashes_for_doc(`
  - Purpose: Indexed function `source_hashes_for_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:151-172]
- `source_files_from_frontmatter` (function) component `source_files_from_frontmatter [function]` (`24f25131-b3d8-5439-8d1b-efbcd24cbcd2`) lines 174-207 [crates/gcode/src/commands/codewiki/io.rs:174-207]
  - Signature: `pub(crate) fn source_files_from_frontmatter(content: &str) -> BTreeSet<String> {`
  - Purpose: Indexed function `source_files_from_frontmatter` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:174-207]
- `unquote_yaml_string` (function) component `unquote_yaml_string [function]` (`958d12c2-64df-56e2-8b50-8fe1d86771c2`) lines 210-240 [crates/gcode/src/commands/codewiki/io.rs:210-240]
  - Signature: `pub(crate) fn unquote_yaml_string(value: &str) -> Option<String> {`
  - Purpose: Indexed function `unquote_yaml_string` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:210-240]
- `decode_hex_escape` (function) component `decode_hex_escape [function]` (`dd4bdb09-46b4-5a8c-b68e-b958a2e04b6c`) lines 243-250 [crates/gcode/src/commands/codewiki/io.rs:243-250]
  - Signature: `fn decode_hex_escape(chars: &mut std::str::Chars<'_>, digits: usize) -> Option<char> {`
  - Purpose: Indexed function `decode_hex_escape` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:243-250]
- `safe_doc_path` (function) component `safe_doc_path [function]` (`fcce327e-0b99-5e68-8045-6ead848668b0`) lines 252-262 [crates/gcode/src/commands/codewiki/io.rs:252-262]
  - Signature: `pub(crate) fn safe_doc_path(out_dir: &Path, relative_path: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: Indexed function `safe_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:252-262]

