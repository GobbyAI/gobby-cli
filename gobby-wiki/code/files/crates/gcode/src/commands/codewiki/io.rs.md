---
title: crates/gcode/src/commands/codewiki/io.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/io.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/io.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/io.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/io.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `write_doc_set` | function | Creates the output directory if needed and then writes each '(relative_path, content)' document in 'docs' via 'write_doc', returning 'Ok(())' on success. [crates/gcode/src/commands/codewiki/io.rs:3-9] |
| `write_incremental_doc_set` | function | Creates a vector of healthy 'BuiltDoc' values from the provided '(path, content)' pairs and delegates to 'write_incremental_doc_set_with_snapshot' with no snapshot, pruning disabled ('"off"'), and an unscoped 'DocPruneScope', returning the resulting 'Vec<String>' of written document paths or identifiers. [crates/gcode/src/commands/codewiki/io.rs:11-28] |
| `write_incremental_doc_set_with_snapshot` | function | Creates a 'DocSink' configured with the given project root, output directory, AI mode, and prune scope, persists each 'BuiltDoc' into it, and finalizes the write by returning the result of 'finish(index_snapshot)' as a 'Vec<String>'. [crates/gcode/src/commands/codewiki/io.rs:30-43] |
| `DocPruneScope` | class | 'DocPruneScope' is a crate-private Rust struct that stores a 'Vec<String>' of scope identifiers used to define the pruning scope for documentation processing. [crates/gcode/src/commands/codewiki/io.rs:46-48] |
| `DocPruneScope::unscoped` | method | Constructs and returns a 'Self' instance with 'scopes' initialized to an empty 'Vec'. [crates/gcode/src/commands/codewiki/io.rs:51-53] |
| `DocPruneScope::from_scopes` | method | Constructs a scoped value from a slice of scope strings by returning 'Self::unscoped()' when the slice is empty or contains any empty string, otherwise cloning the input into 'Self { scopes }'. [crates/gcode/src/commands/codewiki/io.rs:55-63] |
| `DocPruneScope::is_unscoped` | method | Returns 'true' when 'self.scopes' contains no entries, indicating the value is unscoped. [crates/gcode/src/commands/codewiki/io.rs:65-67] |
| `DocPruneScope::includes_file` | method | Returns 'true' if the scope is unscoped or if 'file' is within 'self.scopes' according to 'in_scope', and 'false' otherwise. [crates/gcode/src/commands/codewiki/io.rs:69-71] |
| `DocPruneScope::includes_module` | method | Returns 'true' when the receiver is unscoped, or otherwise when 'module' is contained in 'self.scopes' according to 'in_scope(module, &self.scopes)'. [crates/gcode/src/commands/codewiki/io.rs:73-75] |
| `DocPruneScope::includes_doc` | method | Returns 'true' for all docs when the scope is unscoped, otherwise delegates to 'includes_file' for file docs, 'includes_module' for module docs, and returns 'false' for any path that matches neither. [crates/gcode/src/commands/codewiki/io.rs:77-88] |
| `DocPruneScope::should_prune` | method | Returns 'self.includes_doc(doc_path)', so it prunes exactly when the document path is included. [crates/gcode/src/commands/codewiki/io.rs:90-92] |
| `DocSink` | class | 'DocSink<'a>' is a stateful document-generation/pruning accumulator that tracks project and output paths, AI mode, prior and next documentation metadata, visited and generated document IDs, an optional index snapshot, and the active prune scope. [crates/gcode/src/commands/codewiki/io.rs:99-109] |
| `open` | function | Constructs and returns 'Self' by delegating to 'open_with_prune_scope' with the given 'project_root', 'out_dir', and 'ai_mode', using an unscoped 'DocPruneScope'. [crates/gcode/src/commands/codewiki/io.rs:113-119] |
| `open_with_prune_scope` | function | Creates the output directory, loads prior codewiki metadata, and initializes a new state object with the existing doc set as both 'previous_docs' and 'next_docs', empty 'seen'/'generated_docs', the previous index snapshot, and the supplied 'prune_scope' and 'ai_mode'. [crates/gcode/src/commands/codewiki/io.rs:121-143] |
| `persist` | function | Checks whether a built document is unchanged by comparing source hashes and prior metadata, skips rewriting healthy unchanged docs, and otherwise writes the file, records it as generated, and refreshes its persisted metadata. [crates/gcode/src/commands/codewiki/io.rs:147-197] |
| `flush` | function | Creates a 'CodewikiMeta' snapshot from the current docs, generated docs, previous complete index snapshot, and AI mode, then persists it to 'self.out_dir' via 'write_codewiki_meta', returning any I/O error as 'anyhow::Result<()>'. [crates/gcode/src/commands/codewiki/io.rs:199-210] |
| `finish` | function | Prunes stale docs under the configured prune scope by safely deleting their files and empty parent directories, then writes updated 'CodewikiMeta' (including an optional index snapshot) to 'out_dir' and returns the list of generated document paths. [crates/gcode/src/commands/codewiki/io.rs:214-242] |
| `scoped_file_doc` | function | Returns the inner path as 'Some(&str)' only when 'doc_path' starts with 'code/files/' and ends with '.md', stripping both the prefix and suffix; otherwise returns 'None'. [crates/gcode/src/commands/codewiki/io.rs:245-249] |
| `scoped_module_doc` | function | Returns the substring of 'doc_path' after the 'code/modules/' prefix and before a trailing '.md' suffix, or 'None' if either delimiter is absent. [crates/gcode/src/commands/codewiki/io.rs:251-255] |
| `write_doc` | function | Resolves a safe output path for 'relative_path' under 'out_dir', rejects symlinked targets, creates any missing parent directories, and writes 'content' to the resulting file. [crates/gcode/src/commands/codewiki/io.rs:257-265] |
| `reject_symlinked_doc_path` | function | Checks each path component from 'out_dir' to 'target' and returns an error if any existing component is a symlink, preventing traversal through symlinked doc paths. [crates/gcode/src/commands/codewiki/io.rs:267-285] |
| `prune_empty_doc_dirs` | function | Removes empty ancestor directories of 'target' up to but not including 'out_dir', stopping when it reaches 'out_dir' or encounters a missing/non-empty directory, and returns any other I/O error. [crates/gcode/src/commands/codewiki/io.rs:287-307] |
| `read_codewiki_meta` | function | Reads and deserializes 'CodewikiMeta' from 'CODEWIKI_META_PATH' under 'out_dir', returns 'CodewikiMeta::default()' if the file is missing, propagates other I/O/JSON errors, and backfills any docs with empty 'ai_mode' using the run-level 'ai_mode'. [crates/gcode/src/commands/codewiki/io.rs:309-327] |
| `write_codewiki_meta` | function | Serializes 'meta' to pretty-printed JSON, appends a trailing newline, and writes it to 'CODEWIKI_META_PATH' under 'out_dir' via 'write_doc'. [crates/gcode/src/commands/codewiki/io.rs:329-332] |
| `read_ownership_meta` | function | Resolves the ownership-metadata file path under 'out_dir', deserializes 'OwnershipMeta' from its JSON contents if present, returns 'OwnershipMeta::default()' when the file is missing, and propagates any other I/O or parse error. [crates/gcode/src/commands/codewiki/io.rs:334-341] |
| `write_ownership_meta` | function | Serializes 'meta' to pretty-printed JSON, appends a trailing newline, and writes the result to 'OWNERSHIP_META_PATH' under 'out_dir' via 'write_doc'. [crates/gcode/src/commands/codewiki/io.rs:343-346] |
| `source_hashes_for_doc` | function | Resolves the project root and each source file listed in the document frontmatter, verifies every canonicalized path stays within that root, computes each file’s content hash, and returns the results as a 'BTreeMap' keyed by the original file path string. [crates/gcode/src/commands/codewiki/io.rs:348-369] |
| `source_files_from_frontmatter` | function | Parses a leading YAML frontmatter block delimited by '---', extracts the 'provenance' sequence entries, collects each entry’s 'file' string field, and returns the unique file paths as a 'BTreeSet<String>', or an empty set if the frontmatter is absent or invalid. [crates/gcode/src/commands/codewiki/io.rs:371-406] |
| `unquote_yaml_string` | function | Trims the input, requires it to be wrapped in double quotes, and returns the unescaped YAML double-quoted string by decoding standard backslash escapes and '\x'/'\u'/'\U' hex escapes, or 'None' on malformed input. [crates/gcode/src/commands/codewiki/io.rs:409-439] |
| `decode_hex_escape` | function | Parses exactly 'digits' hexadecimal characters from 'chars', accumulating them into a 'u32' with checked arithmetic and returning the corresponding 'char' via 'char::from_u32', or 'None' if input is insufficient, contains a non-hex digit, overflows, or yields an invalid Unicode scalar value. [crates/gcode/src/commands/codewiki/io.rs:442-449] |
| `safe_doc_path` | function | Validates that 'relative_path' is non-absolute and contains no '..' parent-directory components, then returns 'out_dir.join(relative_path)' or bails with an error if the path is unsafe. [crates/gcode/src/commands/codewiki/io.rs:451-461] |

