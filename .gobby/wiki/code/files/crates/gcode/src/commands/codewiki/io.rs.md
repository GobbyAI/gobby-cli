---
title: crates/gcode/src/commands/codewiki/io.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/io.rs
  ranges:
  - 3-9
  - 11-21
  - 23-35
  - 41-50
  - 53-73
  - 77-125
  - 127-138
  - 142-170
  - 173-181
  - 183-201
  - 203-223
  - 225-243
  - 245-248
  - 250-257
  - 259-262
  - 264-285
  - 287-320
  - 323-353
  - 356-363
  - 365-375
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/io.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/io.rs` exposes 20 indexed API symbols.
[crates/gcode/src/commands/codewiki/io.rs:3-9]
[crates/gcode/src/commands/codewiki/io.rs:11-21]
[crates/gcode/src/commands/codewiki/io.rs:23-35]
[crates/gcode/src/commands/codewiki/io.rs:41-50]
[crates/gcode/src/commands/codewiki/io.rs:53-73]

## API Symbols

- `write_doc_set` (function) component `write_doc_set [function]` (`da03a0d9-08a1-5f2c-848f-855e55517a86`) lines 3-9 [crates/gcode/src/commands/codewiki/io.rs:3-9]
  - Signature: `pub fn write_doc_set(out_dir: &Path, docs: &[(String, String)]) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:3-9]
- `write_incremental_doc_set` (function) component `write_incremental_doc_set [function]` (`fa8a9d60-b906-5015-bfaa-0440a7025e2d`) lines 11-21 [crates/gcode/src/commands/codewiki/io.rs:11-21]
  - Signature: `pub fn write_incremental_doc_set(`
  - Purpose: Indexed function `write_incremental_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:11-21]
- `write_incremental_doc_set_with_snapshot` (function) component `write_incremental_doc_set_with_snapshot [function]` (`bed39b74-bd57-5d7d-bbc2-d28fb37bac95`) lines 23-35 [crates/gcode/src/commands/codewiki/io.rs:23-35]
  - Signature: `pub(crate) fn write_incremental_doc_set_with_snapshot(`
  - Purpose: Indexed function `write_incremental_doc_set_with_snapshot` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:23-35]
- `DocSink` (class) component `DocSink [class]` (`8c07861c-4ab5-5726-b9c7-a2365e9481c7`) lines 41-50 [crates/gcode/src/commands/codewiki/io.rs:41-50]
  - Signature: `pub(crate) struct DocSink<'a> {`
  - Purpose: Indexed class `DocSink` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:41-50]
- `open` (function) component `open [function]` (`79197c19-bd3a-5117-a027-0195fb337b6a`) lines 53-73 [crates/gcode/src/commands/codewiki/io.rs:53-73]
  - Signature: `pub(crate) fn open(`
  - Purpose: Indexed function `open` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:53-73]
- `persist` (function) component `persist [function]` (`e711b819-26e6-539b-a569-15754698f4d7`) lines 77-125 [crates/gcode/src/commands/codewiki/io.rs:77-125]
  - Signature: `pub(crate) fn persist(&mut self, doc: &BuiltDoc) -> anyhow::Result<bool> {`
  - Purpose: Indexed function `persist` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:77-125]
- `flush` (function) component `flush [function]` (`471dbd1e-a1b9-5bc3-bdc4-efe74bb3d4c6`) lines 127-138 [crates/gcode/src/commands/codewiki/io.rs:127-138]
  - Signature: `fn flush(&self) -> anyhow::Result<()> {`
  - Purpose: Indexed function `flush` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:127-138]
- `finish` (function) component `finish [function]` (`084d7fa0-7759-5c5a-8d74-6850060bb0d2`) lines 142-170 [crates/gcode/src/commands/codewiki/io.rs:142-170]
  - Signature: `pub(crate) fn finish(`
  - Purpose: Indexed function `finish` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:142-170]
- `write_doc` (function) component `write_doc [function]` (`1dbe5302-ab02-5f60-92c5-9991824d1b05`) lines 173-181 [crates/gcode/src/commands/codewiki/io.rs:173-181]
  - Signature: `pub(crate) fn write_doc(out_dir: &Path, relative_path: &str, content: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:173-181]
- `reject_symlinked_doc_path` (function) component `reject_symlinked_doc_path [function]` (`c1699afd-0881-5b92-85b2-57cd73621c74`) lines 183-201 [crates/gcode/src/commands/codewiki/io.rs:183-201]
  - Signature: `pub(crate) fn reject_symlinked_doc_path(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed function `reject_symlinked_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:183-201]
- `prune_empty_doc_dirs` (function) component `prune_empty_doc_dirs [function]` (`1ac20481-259c-5583-9698-d6ba5ad11188`) lines 203-223 [crates/gcode/src/commands/codewiki/io.rs:203-223]
  - Signature: `pub(crate) fn prune_empty_doc_dirs(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed function `prune_empty_doc_dirs` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:203-223]
- `read_codewiki_meta` (function) component `read_codewiki_meta [function]` (`e5a5f96f-9842-55d7-807f-014488cb0cb1`) lines 225-243 [crates/gcode/src/commands/codewiki/io.rs:225-243]
  - Signature: `pub(crate) fn read_codewiki_meta(out_dir: &Path) -> anyhow::Result<CodewikiMeta> {`
  - Purpose: Indexed function `read_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:225-243]
- `write_codewiki_meta` (function) component `write_codewiki_meta [function]` (`1e48823c-c709-533e-93a7-10113f2cf147`) lines 245-248 [crates/gcode/src/commands/codewiki/io.rs:245-248]
  - Signature: `pub(crate) fn write_codewiki_meta(out_dir: &Path, meta: &CodewikiMeta) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:245-248]
- `read_ownership_meta` (function) component `read_ownership_meta [function]` (`5c08026a-d8df-5913-8eeb-895b79f55880`) lines 250-257 [crates/gcode/src/commands/codewiki/io.rs:250-257]
  - Signature: `pub(crate) fn read_ownership_meta(out_dir: &Path) -> anyhow::Result<OwnershipMeta> {`
  - Purpose: Indexed function `read_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:250-257]
- `write_ownership_meta` (function) component `write_ownership_meta [function]` (`c301e218-8c86-5be8-941a-bb23f1e0763a`) lines 259-262 [crates/gcode/src/commands/codewiki/io.rs:259-262]
  - Signature: `pub(crate) fn write_ownership_meta(out_dir: &Path, meta: &OwnershipMeta) -> anyhow::Result<()> {`
  - Purpose: Indexed function `write_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:259-262]
- `source_hashes_for_doc` (function) component `source_hashes_for_doc [function]` (`4096ae6f-2c0f-589d-83c6-79f3ccabf2d0`) lines 264-285 [crates/gcode/src/commands/codewiki/io.rs:264-285]
  - Signature: `pub(crate) fn source_hashes_for_doc(`
  - Purpose: Indexed function `source_hashes_for_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:264-285]
- `source_files_from_frontmatter` (function) component `source_files_from_frontmatter [function]` (`c67ea37f-694f-588c-9765-cd6662fa9eb9`) lines 287-320 [crates/gcode/src/commands/codewiki/io.rs:287-320]
  - Signature: `pub(crate) fn source_files_from_frontmatter(content: &str) -> BTreeSet<String> {`
  - Purpose: Indexed function `source_files_from_frontmatter` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:287-320]
- `unquote_yaml_string` (function) component `unquote_yaml_string [function]` (`3459ee96-51de-5dd3-99db-08f0613fd131`) lines 323-353 [crates/gcode/src/commands/codewiki/io.rs:323-353]
  - Signature: `pub(crate) fn unquote_yaml_string(value: &str) -> Option<String> {`
  - Purpose: Indexed function `unquote_yaml_string` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:323-353]
- `decode_hex_escape` (function) component `decode_hex_escape [function]` (`e4186686-d79b-5f16-a4d0-269424cc4b4a`) lines 356-363 [crates/gcode/src/commands/codewiki/io.rs:356-363]
  - Signature: `fn decode_hex_escape(chars: &mut std::str::Chars<'_>, digits: usize) -> Option<char> {`
  - Purpose: Indexed function `decode_hex_escape` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:356-363]
- `safe_doc_path` (function) component `safe_doc_path [function]` (`c8ac7390-7071-5975-8a05-60d3957ba6b0`) lines 365-375 [crates/gcode/src/commands/codewiki/io.rs:365-375]
  - Signature: `pub(crate) fn safe_doc_path(out_dir: &Path, relative_path: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: Indexed function `safe_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:365-375]

