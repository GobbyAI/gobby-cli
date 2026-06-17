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
  - 51-53
  - 55-63
  - 65-67
  - 69-71
  - 73-75
  - 77-88
  - 90-92
  - 99-109
  - 113-119
  - 121-143
  - 147-197
  - 199-210
  - 214-242
  - 245-249
  - 251-255
  - 257-265
  - 267-285
  - 287-307
  - 309-327
  - 329-332
  - 334-341
  - 343-346
  - 348-369
  - 371-406
  - 409-439
  - 442-449
  - 451-461
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/io.rs:3-9](crates/gcode/src/commands/codewiki/io.rs#L3-L9), [crates/gcode/src/commands/codewiki/io.rs:11-28](crates/gcode/src/commands/codewiki/io.rs#L11-L28), [crates/gcode/src/commands/codewiki/io.rs:30-43](crates/gcode/src/commands/codewiki/io.rs#L30-L43), [crates/gcode/src/commands/codewiki/io.rs:46-48](crates/gcode/src/commands/codewiki/io.rs#L46-L48), [crates/gcode/src/commands/codewiki/io.rs:51-53](crates/gcode/src/commands/codewiki/io.rs#L51-L53), [crates/gcode/src/commands/codewiki/io.rs:55-63](crates/gcode/src/commands/codewiki/io.rs#L55-L63), [crates/gcode/src/commands/codewiki/io.rs:65-67](crates/gcode/src/commands/codewiki/io.rs#L65-L67), [crates/gcode/src/commands/codewiki/io.rs:69-71](crates/gcode/src/commands/codewiki/io.rs#L69-L71), [crates/gcode/src/commands/codewiki/io.rs:73-75](crates/gcode/src/commands/codewiki/io.rs#L73-L75), [crates/gcode/src/commands/codewiki/io.rs:77-88](crates/gcode/src/commands/codewiki/io.rs#L77-L88), [crates/gcode/src/commands/codewiki/io.rs:90-92](crates/gcode/src/commands/codewiki/io.rs#L90-L92), [crates/gcode/src/commands/codewiki/io.rs:99-109](crates/gcode/src/commands/codewiki/io.rs#L99-L109), [crates/gcode/src/commands/codewiki/io.rs:113-119](crates/gcode/src/commands/codewiki/io.rs#L113-L119), [crates/gcode/src/commands/codewiki/io.rs:121-143](crates/gcode/src/commands/codewiki/io.rs#L121-L143), [crates/gcode/src/commands/codewiki/io.rs:147-197](crates/gcode/src/commands/codewiki/io.rs#L147-L197), [crates/gcode/src/commands/codewiki/io.rs:199-210](crates/gcode/src/commands/codewiki/io.rs#L199-L210), [crates/gcode/src/commands/codewiki/io.rs:214-242](crates/gcode/src/commands/codewiki/io.rs#L214-L242), [crates/gcode/src/commands/codewiki/io.rs:245-249](crates/gcode/src/commands/codewiki/io.rs#L245-L249), [crates/gcode/src/commands/codewiki/io.rs:251-255](crates/gcode/src/commands/codewiki/io.rs#L251-L255), [crates/gcode/src/commands/codewiki/io.rs:257-265](crates/gcode/src/commands/codewiki/io.rs#L257-L265), [crates/gcode/src/commands/codewiki/io.rs:267-285](crates/gcode/src/commands/codewiki/io.rs#L267-L285), [crates/gcode/src/commands/codewiki/io.rs:287-307](crates/gcode/src/commands/codewiki/io.rs#L287-L307), [crates/gcode/src/commands/codewiki/io.rs:309-327](crates/gcode/src/commands/codewiki/io.rs#L309-L327), [crates/gcode/src/commands/codewiki/io.rs:329-332](crates/gcode/src/commands/codewiki/io.rs#L329-L332), [crates/gcode/src/commands/codewiki/io.rs:334-341](crates/gcode/src/commands/codewiki/io.rs#L334-L341), [crates/gcode/src/commands/codewiki/io.rs:343-346](crates/gcode/src/commands/codewiki/io.rs#L343-L346), [crates/gcode/src/commands/codewiki/io.rs:348-369](crates/gcode/src/commands/codewiki/io.rs#L348-L369), [crates/gcode/src/commands/codewiki/io.rs:371-406](crates/gcode/src/commands/codewiki/io.rs#L371-L406), [crates/gcode/src/commands/codewiki/io.rs:409-439](crates/gcode/src/commands/codewiki/io.rs#L409-L439), [crates/gcode/src/commands/codewiki/io.rs:442-449](crates/gcode/src/commands/codewiki/io.rs#L442-L449), [crates/gcode/src/commands/codewiki/io.rs:451-461](crates/gcode/src/commands/codewiki/io.rs#L451-L461)

</details>

# crates/gcode/src/commands/codewiki/io.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file provides the I/O layer for codewiki documentation output: it writes full doc sets, persists incremental updates through a `DocSink`, and finishes by reconciling changes against an optional index snapshot. The `DocPruneScope` type encapsulates whether pruning is scoped and decides which files, modules, or docs are eligible, while helper functions open sinks, persist and flush docs, prune empty directories, and reject unsafe symlinked paths. It also reads and writes codewiki and ownership metadata, derives source hashes and source files from frontmatter, and includes YAML/string and path-safety helpers to keep doc paths and metadata handling valid.
[crates/gcode/src/commands/codewiki/io.rs:3-9]
[crates/gcode/src/commands/codewiki/io.rs:11-28]
[crates/gcode/src/commands/codewiki/io.rs:30-43]
[crates/gcode/src/commands/codewiki/io.rs:46-48]
[crates/gcode/src/commands/codewiki/io.rs:51-53]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `write_doc_set` | function | `pub fn write_doc_set(out_dir: &Path, docs: &[(String, String)]) -> anyhow::Result<()> {` | `write_doc_set [function]` | `da03a0d9-08a1-5f2c-848f-855e55517a86` | 3-9 [crates/gcode/src/commands/codewiki/io.rs:3-9] | Indexed function `write_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:3-9] |
| `write_incremental_doc_set` | function | `pub fn write_incremental_doc_set(` | `write_incremental_doc_set [function]` | `fa8a9d60-b906-5015-bfaa-0440a7025e2d` | 11-28 [crates/gcode/src/commands/codewiki/io.rs:11-28] | Indexed function `write_incremental_doc_set` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:11-28] |
| `write_incremental_doc_set_with_snapshot` | function | `pub(crate) fn write_incremental_doc_set_with_snapshot(` | `write_incremental_doc_set_with_snapshot [function]` | `ee37fea1-7784-545c-95d5-aa8f3ba13aaf` | 30-43 [crates/gcode/src/commands/codewiki/io.rs:30-43] | Indexed function `write_incremental_doc_set_with_snapshot` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:30-43] |
| `DocPruneScope` | class | `pub(crate) struct DocPruneScope {` | `DocPruneScope [class]` | `5b8a74d4-7871-5772-8f41-fb83fe831ec4` | 46-48 [crates/gcode/src/commands/codewiki/io.rs:46-48] | Indexed class `DocPruneScope` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:46-48] |
| `DocPruneScope::unscoped` | method | `pub(crate) fn unscoped() -> Self {` | `DocPruneScope::unscoped [method]` | `cfe219c4-9b2a-5101-9d81-19b2e8e22632` | 51-53 [crates/gcode/src/commands/codewiki/io.rs:51-53] | Indexed method `DocPruneScope::unscoped` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:51-53] |
| `DocPruneScope::from_scopes` | method | `pub(crate) fn from_scopes(scopes: &[String]) -> Self {` | `DocPruneScope::from_scopes [method]` | `45d7c8b7-e83d-5762-8282-21907063c7b0` | 55-63 [crates/gcode/src/commands/codewiki/io.rs:55-63] | Indexed method `DocPruneScope::from_scopes` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:55-63] |
| `DocPruneScope::is_unscoped` | method | `pub(crate) fn is_unscoped(&self) -> bool {` | `DocPruneScope::is_unscoped [method]` | `b4206733-6718-59ee-8a5e-44d4fc837cb4` | 65-67 [crates/gcode/src/commands/codewiki/io.rs:65-67] | Indexed method `DocPruneScope::is_unscoped` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:65-67] |
| `DocPruneScope::includes_file` | method | `pub(crate) fn includes_file(&self, file: &str) -> bool {` | `DocPruneScope::includes_file [method]` | `8ff7f113-5357-5090-b2a9-b170267efe66` | 69-71 [crates/gcode/src/commands/codewiki/io.rs:69-71] | Indexed method `DocPruneScope::includes_file` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:69-71] |
| `DocPruneScope::includes_module` | method | `pub(crate) fn includes_module(&self, module: &str) -> bool {` | `DocPruneScope::includes_module [method]` | `9383f616-c190-5bbc-9fd8-beae9762c860` | 73-75 [crates/gcode/src/commands/codewiki/io.rs:73-75] | Indexed method `DocPruneScope::includes_module` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:73-75] |
| `DocPruneScope::includes_doc` | method | `pub(crate) fn includes_doc(&self, doc_path: &str) -> bool {` | `DocPruneScope::includes_doc [method]` | `f4793a2d-94b2-5e4e-bfc2-de4a94268936` | 77-88 [crates/gcode/src/commands/codewiki/io.rs:77-88] | Indexed method `DocPruneScope::includes_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:77-88] |
| `DocPruneScope::should_prune` | method | `fn should_prune(&self, doc_path: &str) -> bool {` | `DocPruneScope::should_prune [method]` | `6e3c3ef6-c5ca-5395-8be8-5e65f0b88d0e` | 90-92 [crates/gcode/src/commands/codewiki/io.rs:90-92] | Indexed method `DocPruneScope::should_prune` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:90-92] |
| `DocSink` | class | `pub(crate) struct DocSink<'a> {` | `DocSink [class]` | `8ed05910-d8e1-5329-8cba-dab712996754` | 99-109 [crates/gcode/src/commands/codewiki/io.rs:99-109] | Indexed class `DocSink` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:99-109] |
| `open` | function | `pub(crate) fn open(` | `open [function]` | `9ea7e265-311f-5500-8dee-fbefe886afb9` | 113-119 [crates/gcode/src/commands/codewiki/io.rs:113-119] | Indexed function `open` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:113-119] |
| `open_with_prune_scope` | function | `pub(crate) fn open_with_prune_scope(` | `open_with_prune_scope [function]` | `c0fdce2b-a2f4-5cf1-af5d-960e845dcedf` | 121-143 [crates/gcode/src/commands/codewiki/io.rs:121-143] | Indexed function `open_with_prune_scope` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:121-143] |
| `persist` | function | `pub(crate) fn persist(&mut self, doc: &BuiltDoc) -> anyhow::Result<bool> {` | `persist [function]` | `a6e5e039-1209-566e-9db1-30ed17f29647` | 147-197 [crates/gcode/src/commands/codewiki/io.rs:147-197] | Indexed function `persist` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:147-197] |
| `flush` | function | `fn flush(&self) -> anyhow::Result<()> {` | `flush [function]` | `6d6fb7ad-a856-50cc-bf26-6ecf78e1adcc` | 199-210 [crates/gcode/src/commands/codewiki/io.rs:199-210] | Indexed function `flush` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:199-210] |
| `finish` | function | `pub(crate) fn finish(` | `finish [function]` | `9ea1654a-1522-5ed4-9195-769a3a2030de` | 214-242 [crates/gcode/src/commands/codewiki/io.rs:214-242] | Indexed function `finish` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:214-242] |
| `scoped_file_doc` | function | `fn scoped_file_doc(doc_path: &str) -> Option<&str> {` | `scoped_file_doc [function]` | `65526d37-836f-57e1-9bb7-e703129c83a7` | 245-249 [crates/gcode/src/commands/codewiki/io.rs:245-249] | Indexed function `scoped_file_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:245-249] |
| `scoped_module_doc` | function | `fn scoped_module_doc(doc_path: &str) -> Option<&str> {` | `scoped_module_doc [function]` | `a9caa318-bd1f-59cd-bed6-e5e161c8b6ce` | 251-255 [crates/gcode/src/commands/codewiki/io.rs:251-255] | Indexed function `scoped_module_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:251-255] |
| `write_doc` | function | `pub(crate) fn write_doc(out_dir: &Path, relative_path: &str, content: &str) -> anyhow::Result<()> {` | `write_doc [function]` | `6d73093e-4a75-5baf-a4b8-4b92b7aea9f4` | 257-265 [crates/gcode/src/commands/codewiki/io.rs:257-265] | Indexed function `write_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:257-265] |
| `reject_symlinked_doc_path` | function | `pub(crate) fn reject_symlinked_doc_path(out_dir: &Path, target: &Path) -> anyhow::Result<()> {` | `reject_symlinked_doc_path [function]` | `11f7db54-745d-5629-a099-7ae54adc9609` | 267-285 [crates/gcode/src/commands/codewiki/io.rs:267-285] | Indexed function `reject_symlinked_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:267-285] |
| `prune_empty_doc_dirs` | function | `pub(crate) fn prune_empty_doc_dirs(out_dir: &Path, target: &Path) -> anyhow::Result<()> {` | `prune_empty_doc_dirs [function]` | `acee27a4-5e8b-597b-9f13-81b7f53d07e1` | 287-307 [crates/gcode/src/commands/codewiki/io.rs:287-307] | Indexed function `prune_empty_doc_dirs` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:287-307] |
| `read_codewiki_meta` | function | `pub(crate) fn read_codewiki_meta(out_dir: &Path) -> anyhow::Result<CodewikiMeta> {` | `read_codewiki_meta [function]` | `40775d35-552c-5e89-8154-38247ca7a75f` | 309-327 [crates/gcode/src/commands/codewiki/io.rs:309-327] | Indexed function `read_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:309-327] |
| `write_codewiki_meta` | function | `pub(crate) fn write_codewiki_meta(out_dir: &Path, meta: &CodewikiMeta) -> anyhow::Result<()> {` | `write_codewiki_meta [function]` | `4351c1d9-043d-51be-8ab4-d008a824a559` | 329-332 [crates/gcode/src/commands/codewiki/io.rs:329-332] | Indexed function `write_codewiki_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:329-332] |
| `read_ownership_meta` | function | `pub(crate) fn read_ownership_meta(out_dir: &Path) -> anyhow::Result<OwnershipMeta> {` | `read_ownership_meta [function]` | `b73c975b-ed01-530c-9384-6ee6b566f5c5` | 334-341 [crates/gcode/src/commands/codewiki/io.rs:334-341] | Indexed function `read_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:334-341] |
| `write_ownership_meta` | function | `pub(crate) fn write_ownership_meta(out_dir: &Path, meta: &OwnershipMeta) -> anyhow::Result<()> {` | `write_ownership_meta [function]` | `a0faca9f-52c0-525b-87b6-b66ccf8cba14` | 343-346 [crates/gcode/src/commands/codewiki/io.rs:343-346] | Indexed function `write_ownership_meta` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:343-346] |
| `source_hashes_for_doc` | function | `pub(crate) fn source_hashes_for_doc(` | `source_hashes_for_doc [function]` | `52d802cb-9181-5e6b-b7aa-a53cc5295fe0` | 348-369 [crates/gcode/src/commands/codewiki/io.rs:348-369] | Indexed function `source_hashes_for_doc` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:348-369] |
| `source_files_from_frontmatter` | function | `pub(crate) fn source_files_from_frontmatter(content: &str) -> BTreeSet<String> {` | `source_files_from_frontmatter [function]` | `70d3ba46-9182-587c-b4af-df186ca034d1` | 371-406 [crates/gcode/src/commands/codewiki/io.rs:371-406] | Indexed function `source_files_from_frontmatter` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:371-406] |
| `unquote_yaml_string` | function | `pub(crate) fn unquote_yaml_string(value: &str) -> Option<String> {` | `unquote_yaml_string [function]` | `cfba8bfb-649d-5449-b365-6b0b6bf87f75` | 409-439 [crates/gcode/src/commands/codewiki/io.rs:409-439] | Indexed function `unquote_yaml_string` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:409-439] |
| `decode_hex_escape` | function | `fn decode_hex_escape(chars: &mut std::str::Chars<'_>, digits: usize) -> Option<char> {` | `decode_hex_escape [function]` | `2fbabf81-46e5-5f96-aa37-9ffc818b1120` | 442-449 [crates/gcode/src/commands/codewiki/io.rs:442-449] | Indexed function `decode_hex_escape` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:442-449] |
| `safe_doc_path` | function | `pub(crate) fn safe_doc_path(out_dir: &Path, relative_path: &str) -> anyhow::Result<PathBuf> {` | `safe_doc_path [function]` | `c16c61cf-5c95-565e-af76-ee3d36af888f` | 451-461 [crates/gcode/src/commands/codewiki/io.rs:451-461] | Indexed function `safe_doc_path` in `crates/gcode/src/commands/codewiki/io.rs`. [crates/gcode/src/commands/codewiki/io.rs:451-461] |
