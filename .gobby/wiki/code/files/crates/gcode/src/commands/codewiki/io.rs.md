---
title: crates/gcode/src/commands/codewiki/io.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/io.rs
  ranges:
  - 3-9
  - 11-28
  - 30-43
  - 46-48
  - 50-77
  - 83-93
  - 97-103
  - 105-127
  - 131-179
  - 181-192
  - 196-224
  - 227-231
  - 233-237
  - 239-247
  - 249-267
  - 269-289
  - 291-309
  - 311-314
  - 316-323
  - 325-328
  - 330-351
  - 353-388
  - 391-421
  - 424-431
  - 433-443
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/io.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/io.rs` exposes 28 indexed API symbols.
[crates/gcode/src/commands/codewiki/io.rs:3-9]
[crates/gcode/src/commands/codewiki/io.rs:11-28]
[crates/gcode/src/commands/codewiki/io.rs:30-43]
[crates/gcode/src/commands/codewiki/io.rs:46-48]
[crates/gcode/src/commands/codewiki/io.rs:50-77]

## API Symbols

- `write_doc_set` (function) component `write_doc_set [function]` (`da03a0d9-08a1-5f2c-848f-855e55517a86`) lines 3-9 [crates/gcode/src/commands/codewiki/io.rs:3-9]
  - Signature: `pub fn write_doc_set(out_dir: &Path, docs: &[(String, String)]) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:3-9]
- `write_incremental_doc_set` (function) component `write_incremental_doc_set [function]` (`fa8a9d60-b906-5015-bfaa-0440a7025e2d`) lines 11-28 [crates/gcode/src/commands/codewiki/io.rs:11-28]
  - Signature: `pub fn write_incremental_doc_set(`
  - Purpose: Indexed function `write_incremental_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:11-28]
- `write_incremental_doc_set_with_snapshot` (function) component `write_incremental_doc_set_with_snapshot [function]` (`ee37fea1-7784-545c-95d5-aa8f3ba13aaf`) lines 30-43 [crates/gcode/src/commands/codewiki/io.rs:30-43]
  - Signature: `pub(crate) fn write_incremental_doc_set_with_snapshot(`
  - Purpose: Indexed function `write_incremental_doc_set_with_snapshot` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:30-43]
- `DocPruneScope` (class) component `DocPruneScope [class]` (`5b8a74d4-7871-5772-8f41-fb83fe831ec4`) lines 46-48 [crates/gcode/src/commands/codewiki/io.rs:46-48]
  - Signature: `pub(crate) struct DocPruneScope {`
  - Purpose: Indexed class `DocPruneScope` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:46-48]
- `DocPruneScope` (class) component `DocPruneScope [class]` (`1b2be36f-8693-5cdb-8f24-a8841e937158`) lines 50-77 [crates/gcode/src/commands/codewiki/io.rs:50-77]
  - Signature: `impl DocPruneScope {`
  - Purpose: Indexed class `DocPruneScope` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:50-77]
- `DocPruneScope.unscoped` (method) component `DocPruneScope.unscoped [method]` (`cfe219c4-9b2a-5101-9d81-19b2e8e22632`) lines 51-53 [crates/gcode/src/commands/codewiki/io.rs:51-53]
  - Signature: `pub(crate) fn unscoped() -> Self {`
  - Purpose: Indexed method `DocPruneScope.unscoped` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:51-53]
- `DocPruneScope.from_scopes` (method) component `DocPruneScope.from_scopes [method]` (`45d7c8b7-e83d-5762-8282-21907063c7b0`) lines 55-63 [crates/gcode/src/commands/codewiki/io.rs:55-63]
  - Signature: `pub(crate) fn from_scopes(scopes: &[String]) -> Self {`
  - Purpose: Indexed method `DocPruneScope.from_scopes` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:55-63]
- `DocPruneScope.should_prune` (method) component `DocPruneScope.should_prune [method]` (`51376235-a190-51d3-9615-b963c43e39ea`) lines 65-76 [crates/gcode/src/commands/codewiki/io.rs:65-76]
  - Signature: `fn should_prune(&self, doc_path: &str) -> bool {`
  - Purpose: Indexed method `DocPruneScope.should_prune` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:65-76]
- `DocSink` (class) component `DocSink [class]` (`57b6130e-5922-50fc-9f65-f7f1c3818806`) lines 83-93 [crates/gcode/src/commands/codewiki/io.rs:83-93]
  - Signature: `pub(crate) struct DocSink<'a> {`
  - Purpose: Indexed class `DocSink` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:83-93]
- `open` (function) component `open [function]` (`8a395671-584c-50c8-aa77-7263cb099b46`) lines 97-103 [crates/gcode/src/commands/codewiki/io.rs:97-103]
  - Signature: `pub(crate) fn open(`
  - Purpose: Indexed function `open` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:97-103]
- `open_with_prune_scope` (function) component `open_with_prune_scope [function]` (`7fa4ab11-5317-55a5-bb8e-0bf08b6ae755`) lines 105-127 [crates/gcode/src/commands/codewiki/io.rs:105-127]
  - Signature: `pub(crate) fn open_with_prune_scope(`
  - Purpose: Indexed function `open_with_prune_scope` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:105-127]
- `persist` (function) component `persist [function]` (`26a8b910-9567-5637-ace3-105c515669d8`) lines 131-179 [crates/gcode/src/commands/codewiki/io.rs:131-179]
  - Signature: `pub(crate) fn persist(&mut self, doc: &BuiltDoc) -> anyhow::Result<bool> {`
  - Purpose: Indexed function `persist` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:131-179]
- `flush` (function) component `flush [function]` (`2639b096-0526-56aa-88cc-a5a59e71eac3`) lines 181-192 [crates/gcode/src/commands/codewiki/io.rs:181-192]
  - Signature: `fn flush(&self) -> anyhow::Result<()> {`
  - Purpose: Indexed function `flush` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:181-192]
- `finish` (function) component `finish [function]` (`c111480d-d8c1-596f-926f-e2aed2338a3e`) lines 196-224 [crates/gcode/src/commands/codewiki/io.rs:196-224]
  - Signature: `pub(crate) fn finish(`
  - Purpose: Indexed function `finish` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:196-224]
- `scoped_file_doc` (function) component `scoped_file_doc [function]` (`e2916b5b-0b4c-5770-b18d-b524aada19ec`) lines 227-231 [crates/gcode/src/commands/codewiki/io.rs:227-231]
  - Signature: `fn scoped_file_doc(doc_path: &str) -> Option<&str> {`
  - Purpose: Indexed function `scoped_file_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:227-231]
- `scoped_module_doc` (function) component `scoped_module_doc [function]` (`14a27cac-43be-5750-8cd3-ef5feab1d7e5`) lines 233-237 [crates/gcode/src/commands/codewiki/io.rs:233-237]
  - Signature: `fn scoped_module_doc(doc_path: &str) -> Option<&str> {`
  - Purpose: Indexed function `scoped_module_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:233-237]
- `write_doc` (function) component `write_doc [function]` (`85c6c1d3-01eb-594f-b86b-597e806cddd8`) lines 239-247 [crates/gcode/src/commands/codewiki/io.rs:239-247]
  - Signature: `pub(crate) fn write_doc(out_dir: &Path, relative_path: &str, content: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:239-247]
- `reject_symlinked_doc_path` (function) component `reject_symlinked_doc_path [function]` (`d23a3f9b-2f1d-5917-ac5a-b4ca219ec0bd`) lines 249-267 [crates/gcode/src/commands/codewiki/io.rs:249-267]
  - Signature: `pub(crate) fn reject_symlinked_doc_path(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed function `reject_symlinked_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:249-267]
- `prune_empty_doc_dirs` (function) component `prune_empty_doc_dirs [function]` (`eef73591-2c96-5cfa-adef-19637c997706`) lines 269-289 [crates/gcode/src/commands/codewiki/io.rs:269-289]
  - Signature: `pub(crate) fn prune_empty_doc_dirs(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed function `prune_empty_doc_dirs` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:269-289]
- `read_codewiki_meta` (function) component `read_codewiki_meta [function]` (`6ee34cee-aff3-5640-b231-3ce3716e6e10`) lines 291-309 [crates/gcode/src/commands/codewiki/io.rs:291-309]
  - Signature: `pub(crate) fn read_codewiki_meta(out_dir: &Path) -> anyhow::Result<CodewikiMeta> {`
  - Purpose: Indexed function `read_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:291-309]
- `write_codewiki_meta` (function) component `write_codewiki_meta [function]` (`c1a8f68c-9d9e-5e7d-bcf2-3c483350c382`) lines 311-314 [crates/gcode/src/commands/codewiki/io.rs:311-314]
  - Signature: `pub(crate) fn write_codewiki_meta(out_dir: &Path, meta: &CodewikiMeta) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:311-314]
- `read_ownership_meta` (function) component `read_ownership_meta [function]` (`26964249-ab6f-59e8-8b1f-bb2ce57a0e16`) lines 316-323 [crates/gcode/src/commands/codewiki/io.rs:316-323]
  - Signature: `pub(crate) fn read_ownership_meta(out_dir: &Path) -> anyhow::Result<OwnershipMeta> {`
  - Purpose: Indexed function `read_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:316-323]
- `write_ownership_meta` (function) component `write_ownership_meta [function]` (`3a051d9f-1b2e-5ff8-b951-3e9a8affeead`) lines 325-328 [crates/gcode/src/commands/codewiki/io.rs:325-328]
  - Signature: `pub(crate) fn write_ownership_meta(out_dir: &Path, meta: &OwnershipMeta) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:325-328]
- `source_hashes_for_doc` (function) component `source_hashes_for_doc [function]` (`5fdfee46-2038-5e4a-b331-1331fde3c8c5`) lines 330-351 [crates/gcode/src/commands/codewiki/io.rs:330-351]
  - Signature: `pub(crate) fn source_hashes_for_doc(`
  - Purpose: Indexed function `source_hashes_for_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:330-351]
- `source_files_from_frontmatter` (function) component `source_files_from_frontmatter [function]` (`dc22d336-14a8-56ff-90e5-2aaad0185c87`) lines 353-388 [crates/gcode/src/commands/codewiki/io.rs:353-388]
  - Signature: `pub(crate) fn source_files_from_frontmatter(content: &str) -> BTreeSet<String> {`
  - Purpose: Indexed function `source_files_from_frontmatter` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:353-388]
- `unquote_yaml_string` (function) component `unquote_yaml_string [function]` (`5468036a-fe54-534b-ba60-7d590c5a4508`) lines 391-421 [crates/gcode/src/commands/codewiki/io.rs:391-421]
  - Signature: `pub(crate) fn unquote_yaml_string(value: &str) -> Option<String> {`
  - Purpose: Indexed function `unquote_yaml_string` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:391-421]
- `decode_hex_escape` (function) component `decode_hex_escape [function]` (`092efb89-a58e-5d6d-aeeb-1c03a72c1578`) lines 424-431 [crates/gcode/src/commands/codewiki/io.rs:424-431]
  - Signature: `fn decode_hex_escape(chars: &mut std::str::Chars<'_>, digits: usize) -> Option<char> {`
  - Purpose: Indexed function `decode_hex_escape` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:424-431]
- `safe_doc_path` (function) component `safe_doc_path [function]` (`ab3a0e4c-103f-53c2-b599-b1c175dd8001`) lines 433-443 [crates/gcode/src/commands/codewiki/io.rs:433-443]
  - Signature: `pub(crate) fn safe_doc_path(out_dir: &Path, relative_path: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: Indexed function `safe_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:433-443]

