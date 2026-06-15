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
  - 50-93
  - 99-109
  - 113-119
  - 121-143
  - 147-195
  - 197-208
  - 212-240
  - 243-247
  - 249-253
  - 255-263
  - 265-283
  - 285-305
  - 307-325
  - 327-330
  - 332-339
  - 341-344
  - 346-367
  - 369-404
  - 407-437
  - 440-447
  - 449-459
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/io.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file handles codewiki documentation I/O and pruning. It provides helpers to write whole doc sets or incremental updates, with `DocSink` coordinating metadata loading, doc persistence, and finalization. `DocPruneScope` normalizes scope selectors and decides which file, module, or doc paths are included for pruning. The lower-level helpers enforce safe output paths, reject symlinked targets, prune empty directories, read/write codewiki and ownership metadata, and parse frontmatter source provenance to compute source hashes for doc change tracking.
[crates/gcode/src/commands/codewiki/io.rs:3-9]
[crates/gcode/src/commands/codewiki/io.rs:11-28]
[crates/gcode/src/commands/codewiki/io.rs:30-43]
[crates/gcode/src/commands/codewiki/io.rs:46-48]
[crates/gcode/src/commands/codewiki/io.rs:50-93]

## API Symbols

- `write_doc_set` (function) component `write_doc_set [function]` (`da03a0d9-08a1-5f2c-848f-855e55517a86`) lines 3-9 [crates/gcode/src/commands/codewiki/io.rs:3-9]
  - Signature: `pub fn write_doc_set(out_dir: &Path, docs: &[(String, String)]) -> anyhow::Result<()> {`
  - Purpose: Creates `out_dir` if necessary, then writes each `(relative_path, content)` in `docs` to that directory via `write_doc`, propagating any I/O or write error as `anyhow::Result<()>`. [crates/gcode/src/commands/codewiki/io.rs:3-9]
- `write_incremental_doc_set` (function) component `write_incremental_doc_set [function]` (`fa8a9d60-b906-5015-bfaa-0440a7025e2d`) lines 11-28 [crates/gcode/src/commands/codewiki/io.rs:11-28]
  - Signature: `pub fn write_incremental_doc_set(`
  - Purpose: `write_incremental_doc_set` converts each `(path, content)` pair into a healthy `BuiltDoc` and delegates to `write_incremental_doc_set_with_snapshot` with no snapshot, pruning disabled (`"off"`), and an unscoped prune setting, returning the resulting `Vec<String>`. [crates/gcode/src/commands/codewiki/io.rs:11-28]
- `write_incremental_doc_set_with_snapshot` (function) component `write_incremental_doc_set_with_snapshot [function]` (`ee37fea1-7784-545c-95d5-aa8f3ba13aaf`) lines 30-43 [crates/gcode/src/commands/codewiki/io.rs:30-43]
  - Signature: `pub(crate) fn write_incremental_doc_set_with_snapshot(`
  - Purpose: Opens a `DocSink` for the given project/output paths with the specified AI mode and prune scope, persists each `BuiltDoc` into it, then finalizes the sink with an optional `CodewikiIndexSnapshot` and returns the resulting `Vec<String>` wrapped in `anyhow::Result`. [crates/gcode/src/commands/codewiki/io.rs:30-43]
- `DocPruneScope` (class) component `DocPruneScope [class]` (`5b8a74d4-7871-5772-8f41-fb83fe831ec4`) lines 46-48 [crates/gcode/src/commands/codewiki/io.rs:46-48]
  - Signature: `pub(crate) struct DocPruneScope {`
  - Purpose: `DocPruneScope` is a crate-private value type that stores a `Vec<String>` of scope identifiers used to represent the document-pruning scope set. [crates/gcode/src/commands/codewiki/io.rs:46-48]
- `DocPruneScope` (class) component `DocPruneScope [class]` (`1b2be36f-8693-5cdb-8f24-a8841e937158`) lines 50-93 [crates/gcode/src/commands/codewiki/io.rs:50-93]
  - Signature: `impl DocPruneScope {`
  - Purpose: 'DocPruneScope' is a scope filter that normalizes empty or invalid scope lists to an unscoped state and then determines whether files, modules, or document paths are included by matching them against the configured scopes. [crates/gcode/src/commands/codewiki/io.rs:50-93]
- `DocPruneScope.unscoped` (method) component `DocPruneScope.unscoped [method]` (`cfe219c4-9b2a-5101-9d81-19b2e8e22632`) lines 51-53 [crates/gcode/src/commands/codewiki/io.rs:51-53]
  - Signature: `pub(crate) fn unscoped() -> Self {`
  - Purpose: Constructs and returns a `Self` value with `scopes` initialized to an empty `Vec`, producing an unscoped instance. [crates/gcode/src/commands/codewiki/io.rs:51-53]
- `DocPruneScope.from_scopes` (method) component `DocPruneScope.from_scopes [method]` (`45d7c8b7-e83d-5762-8282-21907063c7b0`) lines 55-63 [crates/gcode/src/commands/codewiki/io.rs:55-63]
  - Signature: `pub(crate) fn from_scopes(scopes: &[String]) -> Self {`
  - Purpose: `from_scopes` returns `Self::unscoped()` when the input slice is empty or contains any empty scope string, otherwise it constructs `Self` by cloning the provided scopes into its `scopes` field. [crates/gcode/src/commands/codewiki/io.rs:55-63]
- `DocPruneScope.is_unscoped` (method) component `DocPruneScope.is_unscoped [method]` (`b4206733-6718-59ee-8a5e-44d4fc837cb4`) lines 65-67 [crates/gcode/src/commands/codewiki/io.rs:65-67]
  - Signature: `pub(crate) fn is_unscoped(&self) -> bool {`
  - Purpose: Returns 'true' when 'self.scopes' is empty, indicating the object has no scopes configured. [crates/gcode/src/commands/codewiki/io.rs:65-67]
- `DocPruneScope.includes_file` (method) component `DocPruneScope.includes_file [method]` (`8ff7f113-5357-5090-b2a9-b170267efe66`) lines 69-71 [crates/gcode/src/commands/codewiki/io.rs:69-71]
  - Signature: `pub(crate) fn includes_file(&self, file: &str) -> bool {`
  - Purpose: Returns 'true' when the instance is unscoped or when 'file' matches one of the configured scopes via 'in_scope(file, &self.scopes)'. [crates/gcode/src/commands/codewiki/io.rs:69-71]
- `DocPruneScope.includes_module` (method) component `DocPruneScope.includes_module [method]` (`9383f616-c190-5bbc-9fd8-beae9762c860`) lines 73-75 [crates/gcode/src/commands/codewiki/io.rs:73-75]
  - Signature: `pub(crate) fn includes_module(&self, module: &str) -> bool {`
  - Purpose: Returns 'true' when the scope is unscoped or when the given 'module' is contained in 'self.scopes' according to 'in_scope'. [crates/gcode/src/commands/codewiki/io.rs:73-75]
- `DocPruneScope.includes_doc` (method) component `DocPruneScope.includes_doc [method]` (`f4793a2d-94b2-5e4e-bfc2-de4a94268936`) lines 77-88 [crates/gcode/src/commands/codewiki/io.rs:77-88]
  - Signature: `pub(crate) fn includes_doc(&self, doc_path: &str) -> bool {`
  - Purpose: Returns 'true' for any doc when unscoped, otherwise delegates to 'includes_file' for file-scoped docs, 'includes_module' for module-scoped docs, and returns 'false' for all other paths. [crates/gcode/src/commands/codewiki/io.rs:77-88]
- `DocPruneScope.should_prune` (method) component `DocPruneScope.should_prune [method]` (`6e3c3ef6-c5ca-5395-8be8-5e65f0b88d0e`) lines 90-92 [crates/gcode/src/commands/codewiki/io.rs:90-92]
  - Signature: `fn should_prune(&self, doc_path: &str) -> bool {`
  - Purpose: Returns the result of 'self.includes_doc(doc_path)', so a document path is pruned exactly when it is included by the current selector. [crates/gcode/src/commands/codewiki/io.rs:90-92]
- `DocSink` (class) component `DocSink [class]` (`8ed05910-d8e1-5329-8cba-dab712996754`) lines 99-109 [crates/gcode/src/commands/codewiki/io.rs:99-109]
  - Signature: `pub(crate) struct DocSink<'a> {`
  - Purpose: 'DocSink' is a crate-private stateful accumulator that tracks project paths, AI mode, prior and next documentation indexes, seen/generated document keys, an optional index snapshot, and a prune scope while preparing doc output. [crates/gcode/src/commands/codewiki/io.rs:99-109]
- `open` (function) component `open [function]` (`9ea7e265-311f-5500-8dee-fbefe886afb9`) lines 113-119 [crates/gcode/src/commands/codewiki/io.rs:113-119]
  - Signature: `pub(crate) fn open(`
  - Purpose: Constructs an instance by calling 'Self::open_with_prune_scope' with the given 'project_root', 'out_dir', and 'ai_mode', using 'DocPruneScope::unscoped()', and returns the resulting 'anyhow::Result<Self>'. [crates/gcode/src/commands/codewiki/io.rs:113-119]
- `open_with_prune_scope` (function) component `open_with_prune_scope [function]` (`c0fdce2b-a2f4-5cf1-af5d-960e845dcedf`) lines 121-143 [crates/gcode/src/commands/codewiki/io.rs:121-143]
  - Signature: `pub(crate) fn open_with_prune_scope(`
  - Purpose: Creates the output directory, loads prior 'codewiki' metadata, and initializes a 'Self' state that preserves previous document entries for interrupted-run safety while preparing fresh 'seen'/'generated_docs' tracking and storing the requested prune scope. [crates/gcode/src/commands/codewiki/io.rs:121-143]
- `persist` (function) component `persist [function]` (`a6e5e039-1209-566e-9db1-30ed17f29647`) lines 147-195 [crates/gcode/src/commands/codewiki/io.rs:147-195]
  - Signature: `pub(crate) fn persist(&mut self, doc: &BuiltDoc) -> anyhow::Result<bool> {`
  - Purpose: 'persist' computes the document’s source hashes, checks whether an on-disk copy can be reused based on existing metadata, degradation state, AI mode, and summary availability, and either skips rewriting while preserving prior metadata or writes the new content and records updated doc metadata, returning whether the document was rewritten. [crates/gcode/src/commands/codewiki/io.rs:147-195]
- `flush` (function) component `flush [function]` (`a1672a72-b6ea-5188-8f81-ad0001155476`) lines 197-208 [crates/gcode/src/commands/codewiki/io.rs:197-208]
  - Signature: `fn flush(&self) -> anyhow::Result<()> {`
  - Purpose: Builds a 'CodewikiMeta' snapshot from the current docs, generated docs, preserved previous index snapshot, and AI mode, then persists it to 'self.out_dir' via 'write_codewiki_meta'. [crates/gcode/src/commands/codewiki/io.rs:197-208]
- `finish` (function) component `finish [function]` (`fa35b8cb-1059-5abb-b4e5-b85da80e55c1`) lines 212-240 [crates/gcode/src/commands/codewiki/io.rs:212-240]
  - Signature: `pub(crate) fn finish(`
  - Purpose: Removes stale prunable docs from 'out_dir', prunes empty parent directories, writes updated 'CodewikiMeta' with the current docs/generated-docs and resolved index snapshot, and returns the list of generated document paths. [crates/gcode/src/commands/codewiki/io.rs:212-240]
- `scoped_file_doc` (function) component `scoped_file_doc [function]` (`6b9f2905-adb1-585f-8be4-00a01f8de572`) lines 243-247 [crates/gcode/src/commands/codewiki/io.rs:243-247]
  - Signature: `fn scoped_file_doc(doc_path: &str) -> Option<&str> {`
  - Purpose: Returns the inner path as a string slice only when 'doc_path' starts with 'code/files/' and ends with '.md', otherwise returns 'None'. [crates/gcode/src/commands/codewiki/io.rs:243-247]
- `scoped_module_doc` (function) component `scoped_module_doc [function]` (`e43ebb08-f57c-536a-8894-7164d3bce9e3`) lines 249-253 [crates/gcode/src/commands/codewiki/io.rs:249-253]
  - Signature: `fn scoped_module_doc(doc_path: &str) -> Option<&str> {`
  - Purpose: Returns the inner module path from a documentation path by removing the 'code/modules/' prefix and '.md' suffix, or 'None' if either is absent. [crates/gcode/src/commands/codewiki/io.rs:249-253]
- `write_doc` (function) component `write_doc [function]` (`0d0aa7f7-5f56-5f1c-9eb2-ec5d81bd56a5`) lines 255-263 [crates/gcode/src/commands/codewiki/io.rs:255-263]
  - Signature: `pub(crate) fn write_doc(out_dir: &Path, relative_path: &str, content: &str) -> anyhow::Result<()> {`
  - Purpose: Resolves a sanitized output path under 'out_dir', rejects symlinked targets, creates any missing parent directories, and writes 'content' to the file, returning any I/O or path-validation errors. [crates/gcode/src/commands/codewiki/io.rs:255-263]
- `reject_symlinked_doc_path` (function) component `reject_symlinked_doc_path [function]` (`8ca60bc0-a8a7-54db-90d5-5f32c19e02d9`) lines 265-283 [crates/gcode/src/commands/codewiki/io.rs:265-283]
  - Signature: `pub(crate) fn reject_symlinked_doc_path(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: It verifies that every existing path component from 'out_dir' to 'target' is non-symlinked, bailing with an error if any intermediate component is a symlink and otherwise returning 'Ok(())'. [crates/gcode/src/commands/codewiki/io.rs:265-283]
- `prune_empty_doc_dirs` (function) component `prune_empty_doc_dirs [function]` (`33adeb29-72c9-50ef-8fe5-3f975f56cc21`) lines 285-305 [crates/gcode/src/commands/codewiki/io.rs:285-305]
  - Signature: `pub(crate) fn prune_empty_doc_dirs(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: 'prune_empty_doc_dirs' walks upward from 'target'’s parent toward 'out_dir', deleting each empty directory it encounters and stopping at 'out_dir' or when it hits a missing/non-empty directory, while propagating any other I/O error. [crates/gcode/src/commands/codewiki/io.rs:285-305]
- `read_codewiki_meta` (function) component `read_codewiki_meta [function]` (`68cc2cbf-3185-5d8a-b95e-b8dc6abc62d8`) lines 307-325 [crates/gcode/src/commands/codewiki/io.rs:307-325]
  - Signature: `pub(crate) fn read_codewiki_meta(out_dir: &Path) -> anyhow::Result<CodewikiMeta> {`
  - Purpose: Reads and deserializes the codewiki metadata JSON from the safe meta path under 'out_dir', returns 'CodewikiMeta::default()' if the file is missing, propagates other I/O/parse errors, and backfills any empty per-doc 'ai_mode' fields with the run-level 'ai_mode'. [crates/gcode/src/commands/codewiki/io.rs:307-325]
- `write_codewiki_meta` (function) component `write_codewiki_meta [function]` (`58c23459-9651-5be4-a7ac-27e0acfe4f2c`) lines 327-330 [crates/gcode/src/commands/codewiki/io.rs:327-330]
  - Signature: `pub(crate) fn write_codewiki_meta(out_dir: &Path, meta: &CodewikiMeta) -> anyhow::Result<()> {`
  - Purpose: Serializes 'meta' to pretty-printed JSON, appends a trailing newline, and writes it to 'CODEWIKI_META_PATH' under 'out_dir' via 'write_doc'. [crates/gcode/src/commands/codewiki/io.rs:327-330]
- `read_ownership_meta` (function) component `read_ownership_meta [function]` (`176e3f2e-4ee1-5fe3-bb1b-f873d6319173`) lines 332-339 [crates/gcode/src/commands/codewiki/io.rs:332-339]
  - Signature: `pub(crate) fn read_ownership_meta(out_dir: &Path) -> anyhow::Result<OwnershipMeta> {`
  - Purpose: Reads the ownership metadata JSON from the sanitized 'OWNERSHIP_META_PATH' under 'out_dir', returns the parsed 'OwnershipMeta', falls back to 'OwnershipMeta::default()' if the file is missing, and propagates any other I/O or deserialization error. [crates/gcode/src/commands/codewiki/io.rs:332-339]
- `write_ownership_meta` (function) component `write_ownership_meta [function]` (`41d97a7b-78b0-50bb-9c86-26a35f015eae`) lines 341-344 [crates/gcode/src/commands/codewiki/io.rs:341-344]
  - Signature: `pub(crate) fn write_ownership_meta(out_dir: &Path, meta: &OwnershipMeta) -> anyhow::Result<()> {`
  - Purpose: Serializes 'meta' to pretty-printed JSON, appends a trailing newline, and writes it to 'OWNERSHIP_META_PATH' under 'out_dir' via 'write_doc'. [crates/gcode/src/commands/codewiki/io.rs:341-344]
- `source_hashes_for_doc` (function) component `source_hashes_for_doc [function]` (`2658dccc-c956-59b7-b9a7-b3915ad0691e`) lines 346-367 [crates/gcode/src/commands/codewiki/io.rs:346-367]
  - Signature: `pub(crate) fn source_hashes_for_doc(`
  - Purpose: Resolves and validates each source file listed in the document frontmatter against the canonical project root, hashes its contents, and returns a 'BTreeMap' from relative source path to content hash, erroring if resolution or hashing fails or if any file escapes the project root. [crates/gcode/src/commands/codewiki/io.rs:346-367]
- `source_files_from_frontmatter` (function) component `source_files_from_frontmatter [function]` (`9d97ca8d-3a9f-5a69-801f-7aac4eda1a73`) lines 369-404 [crates/gcode/src/commands/codewiki/io.rs:369-404]
  - Signature: `pub(crate) fn source_files_from_frontmatter(content: &str) -> BTreeSet<String> {`
  - Purpose: Parses a YAML frontmatter block at the start of 'content' and returns a deduplicated 'BTreeSet<String>' of all 'provenance.file' values found under the contract’s provenance key, or an empty set if the frontmatter is missing or malformed. [crates/gcode/src/commands/codewiki/io.rs:369-404]
- `unquote_yaml_string` (function) component `unquote_yaml_string [function]` (`8f64df88-ee28-5f7f-983a-541fed360f92`) lines 407-437 [crates/gcode/src/commands/codewiki/io.rs:407-437]
  - Signature: `pub(crate) fn unquote_yaml_string(value: &str) -> Option<String> {`
  - Purpose: Trims the input, requires it to be a double-quoted YAML scalar, and returns the unescaped inner string by interpreting standard YAML backslash escapes and hex Unicode escapes, or 'None' on malformed input. [crates/gcode/src/commands/codewiki/io.rs:407-437]
- `decode_hex_escape` (function) component `decode_hex_escape [function]` (`4fe425b7-6ca2-542c-a09b-97298b2f7bd8`) lines 440-447 [crates/gcode/src/commands/codewiki/io.rs:440-447]
  - Signature: `fn decode_hex_escape(chars: &mut std::str::Chars<'_>, digits: usize) -> Option<char> {`
  - Purpose: Parses exactly 'digits' hexadecimal digits from the provided character iterator, accumulates them into a 'u32' with checked base-16 arithmetic, and returns the corresponding Unicode 'char' via 'char::from_u32', or 'None' on missing/invalid digits or overflow. [crates/gcode/src/commands/codewiki/io.rs:440-447]
- `safe_doc_path` (function) component `safe_doc_path [function]` (`61e7c25e-451c-5bee-9570-406582a1b661`) lines 449-459 [crates/gcode/src/commands/codewiki/io.rs:449-459]
  - Signature: `pub(crate) fn safe_doc_path(out_dir: &Path, relative_path: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: Returns 'out_dir.join(relative_path)' only if 'relative_path' is not absolute and contains no '..' parent-directory components, otherwise it fails with an error refusing to write an unsafe path. [crates/gcode/src/commands/codewiki/io.rs:449-459]

