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

`crates/gcode/src/commands/codewiki/io.rs` exposes 35 indexed API symbols.

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
| `DocSink` | class | DocSink is a crate-internal documentation generation manager that orchestrates AI-enhanced code documentation with git-diff-based incremental updates and automatic structural fallback on AI degradation. [crates/gcode/src/commands/codewiki/io.rs:99-120] |
| `open_with_prune_scope` | function | # Summary Initializes a codewiki instance with the specified project paths, AI mode, and pruning scope, restoring previous documentation state from the output directory to preserve unprocessed entries across interrupted runs. [crates/gcode/src/commands/codewiki/io.rs:132-156] |
| `with_since` | function | This crate-private builder method sets the 'since' field to an optional BTreeSet of strings and returns self for method chaining. [crates/gcode/src/commands/codewiki/io.rs:161-164] |
| `persist` | function | Persists a built document to disk, returning whether the document was actually written by comparing source hashes, invalidation keys, and cached metadata to determine if the content has changed. [crates/gcode/src/commands/codewiki/io.rs:168-254] |
| `degraded_docs` | function | Returns a crate-scoped reference to a slice of String elements containing degraded documentation data. [crates/gcode/src/commands/codewiki/io.rs:258-260] |
| `flush` | function | Writes the current CodewikiMeta state—comprising next_docs, generated_docs, previous_snapshot, and ai_mode—to the output directory via 'write_codewiki_meta'. [crates/gcode/src/commands/codewiki/io.rs:262-273] |
| `finish` | function | # Summary Finalizes a documentation generation run by identifying and removing stale pages not regenerated in the current pass from both tracked metadata and disk (within the designated prune scope), then returning the updated metadata. [crates/gcode/src/commands/codewiki/io.rs:277-321] |
| `collect_generated_doc_pages` | function | The function recursively collects all Markdown files from a "code" subdirectory and returns their paths relative to the output directory with normalized forward-slash separators. [crates/gcode/src/commands/codewiki/io.rs:331-360] |
| `scoped_file_doc` | function | # Summary 'scoped_file_doc' removes the "code/files/" prefix and ".md" suffix from a file path, returning the intermediate string slice if both operations succeed, or None otherwise. [crates/gcode/src/commands/codewiki/io.rs:362-366] |
| `scoped_module_doc` | function | Removes the "code/modules/" prefix and ".md" suffix from a documentation file path, returning the intermediate string slice or None if either component is absent. [crates/gcode/src/commands/codewiki/io.rs:368-372] |
| `write_doc` | function | Safely writes content to a file at a validated, non-symlinked path within a specified output directory, creating parent directories as needed. [crates/gcode/src/commands/codewiki/io.rs:374-382] |
| `reject_symlinked_doc_path` | function | This function validates that a target path contains no symbolic link components relative to a specified output directory, returning an error if any symlinks are detected in the path traversal. [crates/gcode/src/commands/codewiki/io.rs:384-402] |
| `prune_empty_doc_dirs` | function | Traverses and removes empty parent directories of 'target' up to 'out_dir', halting when encountering a non-empty directory, missing directory, or I/O error. [crates/gcode/src/commands/codewiki/io.rs:404-424] |

_8 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/codewiki/io.rs` for the full list._

_Verified by 3 in-file unit tests._

