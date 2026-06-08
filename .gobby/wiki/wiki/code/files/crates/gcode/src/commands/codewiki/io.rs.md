---
title: crates/gcode/src/commands/codewiki/io.rs
type: code_file
source_files:
- file: crates/gcode/src/commands/codewiki/io.rs
  ranges:
  - 3-9
  - 11-59
  - 61-69
  - 71-89
  - 91-111
  - 113-120
  - 122-125
  - 127-148
  - 150-183
  - 186-216
  - 219-226
  - 228-238
---

# crates/gcode/src/commands/codewiki/io.rs

Module: [[modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/io.rs` exposes 12 indexed API symbols. [crates/gcode/src/commands/codewiki/io.rs:3-9] [crates/gcode/src/commands/codewiki/io.rs:11-59] [crates/gcode/src/commands/codewiki/io.rs:61-69] [crates/gcode/src/commands/codewiki/io.rs:71-89] [crates/gcode/src/commands/codewiki/io.rs:91-111] [crates/gcode/src/commands/codewiki/io.rs:113-120] [crates/gcode/src/commands/codewiki/io.rs:122-125] [crates/gcode/src/commands/codewiki/io.rs:127-148] [crates/gcode/src/commands/codewiki/io.rs:150-183] [crates/gcode/src/commands/codewiki/io.rs:186-216] [crates/gcode/src/commands/codewiki/io.rs:219-226] [crates/gcode/src/commands/codewiki/io.rs:228-238]

## API Symbols

- `write_doc_set` (function) component `write_doc_set [function]` (`da03a0d9-08a1-5f2c-848f-855e55517a86`) lines 3-9 [crates/gcode/src/commands/codewiki/io.rs:3-9]
  - Signature: `pub fn write_doc_set(out_dir: &Path, docs: &[(String, String)]) -> anyhow::Result<()> {`
  - Purpose: Creates an output directory and writes each document from a collection of (relative_path, content) tuples to disk. [crates/gcode/src/commands/codewiki/io.rs:3-9]
- `write_incremental_doc_set` (function) component `write_incremental_doc_set [function]` (`fa8a9d60-b906-5015-bfaa-0440a7025e2d`) lines 11-59 [crates/gcode/src/commands/codewiki/io.rs:11-59]
  - Signature: `pub fn write_incremental_doc_set(`
  - Purpose: Increments a documentation set in an output directory by computing source hashes to detect changes, writing only modified or new documents, removing stale files, and returning the paths of newly generated documents. [crates/gcode/src/commands/codewiki/io.rs:11-59]
- `write_doc` (function) component `write_doc [function]` (`c9fb6d1b-76be-5ba6-819b-4d44cb30d0b7`) lines 61-69 [crates/gcode/src/commands/codewiki/io.rs:61-69]
  - Signature: `pub(crate) fn write_doc(out_dir: &Path, relative_path: &str, content: &str) -> anyhow::Result<()> {`
  - Purpose: Writes string content to a file at a relative path within an output directory, creating parent directories and validating the target path against symlink exploitation. [crates/gcode/src/commands/codewiki/io.rs:61-69]
- `reject_symlinked_doc_path` (function) component `reject_symlinked_doc_path [function]` (`7a8ce462-edf6-5553-b58b-85416b527c0d`) lines 71-89 [crates/gcode/src/commands/codewiki/io.rs:71-89]
  - Signature: `pub(crate) fn reject_symlinked_doc_path(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Validates that a target path contains no symlinks by traversing each path component from an output directory, returning an error if any symlink is encountered. [crates/gcode/src/commands/codewiki/io.rs:71-89]
- `prune_empty_doc_dirs` (function) component `prune_empty_doc_dirs [function]` (`f9818876-3c5a-5b74-b860-9a5fe4a8006f`) lines 91-111 [crates/gcode/src/commands/codewiki/io.rs:91-111]
  - Signature: `pub(crate) fn prune_empty_doc_dirs(out_dir: &Path, target: &Path) -> anyhow::Result<()> {`
  - Purpose: Recursively removes empty ancestor directories starting from the target's parent directory up to (but not including) the specified output directory, halting on the first non-empty directory, missing directory, or error. [crates/gcode/src/commands/codewiki/io.rs:91-111]
- `read_codewiki_meta` (function) component `read_codewiki_meta [function]` (`a511cb44-ab08-5517-8e51-3a514663d9fd`) lines 113-120 [crates/gcode/src/commands/codewiki/io.rs:113-120]
  - Signature: `pub(crate) fn read_codewiki_meta(out_dir: &Path) -> anyhow::Result<CodewikiMeta> {`
  - Purpose: Reads and deserializes a JSON metadata file from the output directory into a `CodewikiMeta` struct, returning a default instance if the file doesn't exist or propagating any other I/O or deserialization errors. [crates/gcode/src/commands/codewiki/io.rs:113-120]
- `write_codewiki_meta` (function) component `write_codewiki_meta [function]` (`ff7ae738-b4a1-52d6-9f54-524a0ab0f7f6`) lines 122-125 [crates/gcode/src/commands/codewiki/io.rs:122-125]
  - Signature: `pub(crate) fn write_codewiki_meta(out_dir: &Path, meta: &CodewikiMeta) -> anyhow::Result<()> {`
  - Purpose: Serializes a `CodewikiMeta` struct to pretty-printed JSON and writes it to the codewiki metadata file in the specified output directory with a trailing newline. [crates/gcode/src/commands/codewiki/io.rs:122-125]
- `source_hashes_for_doc` (function) component `source_hashes_for_doc [function]` (`2a3bf644-3ee9-5d26-9e49-f4800e1559bf`) lines 127-148 [crates/gcode/src/commands/codewiki/io.rs:127-148]
  - Signature: `pub(crate) fn source_hashes_for_doc(`
  - Purpose: Generates a sorted map of filename-to-content-hash pairs for source files referenced in document frontmatter, with canonicalized path validation to prevent directory traversal outside the project root. [crates/gcode/src/commands/codewiki/io.rs:127-148]
- `source_files_from_frontmatter` (function) component `source_files_from_frontmatter [function]` (`acf21bf1-dfc5-56c6-994e-e307b0454235`) lines 150-183 [crates/gcode/src/commands/codewiki/io.rs:150-183]
  - Signature: `pub(crate) fn source_files_from_frontmatter(content: &str) -> BTreeSet<String> {`
  - Purpose: Parses YAML frontmatter from markdown content and returns a sorted set of unique file names extracted from the "source_files" or "sources" sequence fields. [crates/gcode/src/commands/codewiki/io.rs:150-183]
- `unquote_yaml_string` (function) component `unquote_yaml_string [function]` (`7c4d5ad1-df7c-5562-b4fd-be30c923fd24`) lines 186-216 [crates/gcode/src/commands/codewiki/io.rs:186-216]
  - Signature: `pub(crate) fn unquote_yaml_string(value: &str) -> Option<String> {`
  - Purpose: Unquotes a double-quoted YAML string and expands all backslash escape sequences (control characters, quotes, slashes, and 2/4/8-digit hex/unicode escapes) into their corresponding characters, returning `None` on invalid syntax. [crates/gcode/src/commands/codewiki/io.rs:186-216]
- `decode_hex_escape` (function) component `decode_hex_escape [function]` (`eb616ae2-713c-5bac-a07b-2f0c8cd38de3`) lines 219-226 [crates/gcode/src/commands/codewiki/io.rs:219-226]
  - Signature: `fn decode_hex_escape(chars: &mut std::str::Chars<'_>, digits: usize) -> Option<char> {`
  - Purpose: Decodes the next N hexadecimal digits from a character iterator into a Unicode character, with overflow protection via checked arithmetic. [crates/gcode/src/commands/codewiki/io.rs:219-226]
- `safe_doc_path` (function) component `safe_doc_path [function]` (`06cc83eb-edda-5fa2-afe8-995a491dc2bb`) lines 228-238 [crates/gcode/src/commands/codewiki/io.rs:228-238]
  - Signature: `pub(crate) fn safe_doc_path(out_dir: &Path, relative_path: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: This function validates that a relative path contains no absolute components or parent directory references (preventing directory traversal), then safely joins it with an output directory. [crates/gcode/src/commands/codewiki/io.rs:228-238]

