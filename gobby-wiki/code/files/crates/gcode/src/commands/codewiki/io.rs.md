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

`crates/gcode/src/commands/codewiki/io.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/io.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

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
| `DocSink` | class | 'DocSink' is a crate-private struct that orchestrates the generation, snapshot comparison, and pruning of documentation files, tracking current and historical metadata while supporting differential updates scoped to files changed since a specific git reference. [crates/gcode/src/commands/codewiki/io.rs:99-115] |
| `open_with_prune_scope` | function | This function initializes an instance of the struct by ensuring the output directory exists, loading previous metadata to populate the document states and index snapshot, and configuring the specified pruning scope. [crates/gcode/src/commands/codewiki/io.rs:127-150] |
| `with_since` | function | This builder-pattern method updates the 'since' field of the receiver with the provided 'Option<BTreeSet<String>>' and returns the modified 'self' by value. [crates/gcode/src/commands/codewiki/io.rs:155-158] |
| `persist` | function | The 'persist' function evaluates whether a document's compiled target is already up-to-date and can bypass being rewritten by validating the target file's existence and previous build metadata—such as degradation status, rendering configuration, invalidation keys, or source and neighbor hashes—against the current build state, returning a boolean indicating if the document remains unchanged. [crates/gcode/src/commands/codewiki/io.rs:162-245] |
| `flush` | function | The 'flush' method serializes and writes a 'CodewikiMeta' metadata snapshot—comprising cloned fields for next documents, generated documents, the previous index snapshot, and the AI mode—to the configured output directory. [crates/gcode/src/commands/codewiki/io.rs:247-258] |
| `finish` | function | The 'finish' function prunes stale document files within the prune scope from the disk, persists the updated codewiki metadata containing the current document index and optional snapshot, and returns the paths of all generated documents. [crates/gcode/src/commands/codewiki/io.rs:262-290] |
| `scoped_file_doc` | function | This function extracts the inner path substring from a document path by stripping the '"code/files/"' prefix and the '".md"' suffix, returning the resulting slice as 'Some(&str)' if both patterns match, or 'None' otherwise. [crates/gcode/src/commands/codewiki/io.rs:293-297] |
| `scoped_module_doc` | function | The 'scoped_module_doc' function strips the prefix '"code/modules/"' and the suffix '".md"' from the input 'doc_path' string slice, returning the inner substring slice as 'Some(&str)' if both exist, or 'None' otherwise. [crates/gcode/src/commands/codewiki/io.rs:299-303] |
| `write_doc` | function | The 'write_doc' function resolves a secure target path within a base directory, validates it against symlink-based directory traversal, creates any missing parent directories, and writes the specified string content to the file. [crates/gcode/src/commands/codewiki/io.rs:305-313] |
| `reject_symlinked_doc_path` | function | This function checks each component of the relative path from 'out_dir' to 'target' to ensure none of them are symbolic links, returning an error if any symlink is detected. [crates/gcode/src/commands/codewiki/io.rs:315-333] |
| `prune_empty_doc_dirs` | function | The function recursively traverses upward from the parent directory of 'target' toward 'out_dir', attempting to delete each directory and stopping when it encounters 'out_dir', a non-empty directory, or a missing directory, while propagating any other filesystem errors. [crates/gcode/src/commands/codewiki/io.rs:335-355] |
| `read_codewiki_meta` | function | The 'read_codewiki_meta' function deserializes 'CodewikiMeta' from a JSON file in the specified output directory, returning a default instance if the file is not found, and backfills any empty per-document AI modes with the run-level AI mode. [crates/gcode/src/commands/codewiki/io.rs:357-375] |
| `write_codewiki_meta` | function | This function serializes a 'CodewikiMeta' struct into a pretty-printed JSON string and writes it, appended with a trailing newline, to the path specified by 'CODEWIKI_META_PATH' within the designated output directory. [crates/gcode/src/commands/codewiki/io.rs:377-380] |

_6 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/codewiki/io.rs` for the full list._

_Verified by 3 in-file unit tests._

