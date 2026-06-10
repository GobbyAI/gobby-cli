---
title: crates/gcode/src/commands/codewiki/io.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/io.rs
  ranges:
  - 3-9
  - 11-17
  - 19-79
  - 81-89
  - 91-109
  - 111-131
  - 133-140
  - 142-145
  - 147-154
  - 156-159
  - 161-182
  - 184-217
  - 220-250
  - 253-260
  - 262-272
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/io.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/io.rs` exposes 15 indexed API symbols.
[crates/gcode/src/commands/codewiki/io.rs:3-9]
[crates/gcode/src/commands/codewiki/io.rs:11-17]
[crates/gcode/src/commands/codewiki/io.rs:19-79]
[crates/gcode/src/commands/codewiki/io.rs:81-89]
[crates/gcode/src/commands/codewiki/io.rs:91-109]
[crates/gcode/src/commands/codewiki/io.rs:111-131]
[crates/gcode/src/commands/codewiki/io.rs:133-140]
[crates/gcode/src/commands/codewiki/io.rs:142-145]
[crates/gcode/src/commands/codewiki/io.rs:147-154]
[crates/gcode/src/commands/codewiki/io.rs:156-159]
[crates/gcode/src/commands/codewiki/io.rs:161-182]
[crates/gcode/src/commands/codewiki/io.rs:184-217]
[crates/gcode/src/commands/codewiki/io.rs:220-250]
[crates/gcode/src/commands/codewiki/io.rs:253-260]
[crates/gcode/src/commands/codewiki/io.rs:262-272]

## API Symbols

- `write_doc_set` (function) component `write_doc_set [function]` (`da03a0d9-08a1-5f2c-848f-855e55517a86`) lines 3-9 [crates/gcode/src/commands/codewiki/io.rs:3-9]
  - Signature: `pub fn write_doc_set(out_dir: &Path, docs: &[(String, String)]) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:3-9]
- `write_incremental_doc_set` (function) component `write_incremental_doc_set [function]` (`fa8a9d60-b906-5015-bfaa-0440a7025e2d`) lines 11-17 [crates/gcode/src/commands/codewiki/io.rs:11-17]
  - Signature: `pub fn write_incremental_doc_set(`
  - Purpose: Indexed function `write_incremental_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:11-17]
- `write_incremental_doc_set_with_snapshot` (function) component `write_incremental_doc_set_with_snapshot [function]` (`fe44c412-b3a7-5e9e-b709-8dfcb29c48f6`) lines 19-79 [crates/gcode/src/commands/codewiki/io.rs:19-79]
  - Signature: `pub(crate) fn write_incremental_doc_set_with_snapshot(`
  - Purpose: Indexed function `write_incremental_doc_set_with_snapshot` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:19-79]
- `write_doc` (function) component `write_doc [function]` (`6eafe506-975b-59f6-9ddd-c97fbcf0d2fc`) lines 81-89 [crates/gcode/src/commands/codewiki/io.rs:81-89]
  - Signature: `pub(crate) fn write_doc(out_dir: &Path, relative_path: &str, content: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:81-89]
- `reject_symlinked_doc_path` (function) component `reject_symlinked_doc_path [function]` (`e54d5c3b-7665-5e46-b4b0-e98b8c112c75`) lines 91-109 [crates/gcode/src/commands/codewiki/io.rs:91-109]
  - Signature: `pub(crate) fn reject_symlinked_doc_path(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed function `reject_symlinked_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:91-109]
- `prune_empty_doc_dirs` (function) component `prune_empty_doc_dirs [function]` (`7d3bc3a4-7d8f-5a42-8d3c-8f1b7e2ae50b`) lines 111-131 [crates/gcode/src/commands/codewiki/io.rs:111-131]
  - Signature: `pub(crate) fn prune_empty_doc_dirs(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed function `prune_empty_doc_dirs` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:111-131]
- `read_codewiki_meta` (function) component `read_codewiki_meta [function]` (`34544a04-7bbc-5ee0-8fe1-51567fc85fa8`) lines 133-140 [crates/gcode/src/commands/codewiki/io.rs:133-140]
  - Signature: `pub(crate) fn read_codewiki_meta(out_dir: &Path) -> anyhow::Result<CodewikiMeta> {`
  - Purpose: Indexed function `read_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:133-140]
- `write_codewiki_meta` (function) component `write_codewiki_meta [function]` (`86b5c6b0-de05-51d7-94b0-9adfb95d6fdb`) lines 142-145 [crates/gcode/src/commands/codewiki/io.rs:142-145]
  - Signature: `pub(crate) fn write_codewiki_meta(out_dir: &Path, meta: &CodewikiMeta) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:142-145]
- `read_ownership_meta` (function) component `read_ownership_meta [function]` (`bf3a9ef0-9d07-5149-874e-1bf404639f2b`) lines 147-154 [crates/gcode/src/commands/codewiki/io.rs:147-154]
  - Signature: `pub(crate) fn read_ownership_meta(out_dir: &Path) -> anyhow::Result<OwnershipMeta> {`
  - Purpose: Indexed function `read_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:147-154]
- `write_ownership_meta` (function) component `write_ownership_meta [function]` (`78590362-f00e-5aaf-b4d4-44a56ddb9efb`) lines 156-159 [crates/gcode/src/commands/codewiki/io.rs:156-159]
  - Signature: `pub(crate) fn write_ownership_meta(out_dir: &Path, meta: &OwnershipMeta) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:156-159]
- `source_hashes_for_doc` (function) component `source_hashes_for_doc [function]` (`698f72a6-b9a1-5e2c-8201-427dfc0e450b`) lines 161-182 [crates/gcode/src/commands/codewiki/io.rs:161-182]
  - Signature: `pub(crate) fn source_hashes_for_doc(`
  - Purpose: Indexed function `source_hashes_for_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:161-182]
- `source_files_from_frontmatter` (function) component `source_files_from_frontmatter [function]` (`f994b7ef-3758-50d0-8238-016b6308a484`) lines 184-217 [crates/gcode/src/commands/codewiki/io.rs:184-217]
  - Signature: `pub(crate) fn source_files_from_frontmatter(content: &str) -> BTreeSet<String> {`
  - Purpose: Indexed function `source_files_from_frontmatter` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:184-217]
- `unquote_yaml_string` (function) component `unquote_yaml_string [function]` (`fa2d4760-c5a2-5f3a-b30d-43e9f8838cf4`) lines 220-250 [crates/gcode/src/commands/codewiki/io.rs:220-250]
  - Signature: `pub(crate) fn unquote_yaml_string(value: &str) -> Option<String> {`
  - Purpose: Indexed function `unquote_yaml_string` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:220-250]
- `decode_hex_escape` (function) component `decode_hex_escape [function]` (`8805b874-8f5b-52e2-a744-12a8aafce3a3`) lines 253-260 [crates/gcode/src/commands/codewiki/io.rs:253-260]
  - Signature: `fn decode_hex_escape(chars: &mut std::str::Chars<'_>, digits: usize) -> Option<char> {`
  - Purpose: Indexed function `decode_hex_escape` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:253-260]
- `safe_doc_path` (function) component `safe_doc_path [function]` (`d9008d35-32b1-5373-af68-d115de7db276`) lines 262-272 [crates/gcode/src/commands/codewiki/io.rs:262-272]
  - Signature: `pub(crate) fn safe_doc_path(out_dir: &Path, relative_path: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: Indexed function `safe_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:262-272]

