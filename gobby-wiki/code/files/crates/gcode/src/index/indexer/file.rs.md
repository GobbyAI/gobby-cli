---
title: crates/gcode/src/index/indexer/file.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/file.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/file.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/file.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/file.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `index_file` | function | Indexes a file by resolving its path relative to the project root, parsing it with optional semantic import resolution, computing language/hash/size metadata, and then writing the resulting facts into a PostgreSQL transaction, returning 'None' for skipped/unreadable files. [crates/gcode/src/index/indexer/file.rs:15-91] |
| `create_semantic_resolver_if_needed` | function | Returns 'None' when no candidate path appears to require C++ semantics, otherwise delegates to 'semantic::create_cpp_semantic_resolver(root_path, require_cpp_semantics)' and returns its 'Result<Option<Box<dyn SemanticCallResolver>>>'. [crates/gcode/src/index/indexer/file.rs:93-102] |
| `has_cpp_semantic_candidate` | function | Returns 'true' if any path in 'candidates' is detected by 'languages::detect_language' as either '"c"' or '"cpp"', and 'false' otherwise. [crates/gcode/src/index/indexer/file.rs:104-111] |
| `ExplicitFileRoute` | type | Indexed type `ExplicitFileRoute` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:114-118] |
| `explicit_file_route` | function | Classifies 'path' relative to 'root_path' using 'walker::classify_file' and maps the result to 'ExplicitFileRoute::Ast', 'ExplicitFileRoute::ContentOnly', or 'ExplicitFileRoute::Skip' when no classification is returned. [crates/gcode/src/index/indexer/file.rs:120-130] |
| `index_content_only` | function | Indexes a content-only file by filtering with content-indexability rules, resolving its path relative to the root, reading its bytes, deriving language and content hash, and writing file facts in a Postgres transaction, returning 'None' for skipped or unreadable files. [crates/gcode/src/index/indexer/file.rs:133-180] |
| `write_parsed_file_facts` | function | Persists parsed-file facts into the 'CodeFactSink' by upserting symbols, imports, calls, file metadata, and content chunks while deleting stale symbol/non-symbol records, then returns a 'FileIndexCounts' summary of the indexing work. [crates/gcode/src/index/indexer/file.rs:182-232] |
| `write_content_only_file_facts` | function | Deletes any existing facts for the file, upserts a content-only 'IndexedFile' record with zero symbols and the provided metadata, chunks the source bytes, conditionally persists those content chunks, and returns 'FileIndexCounts' reporting one indexed file and the number of chunks written. [crates/gcode/src/index/indexer/file.rs:234-267] |
| `c_header_candidates_enable_cpp_semantic_resolution` | function | Creates a temporary C header file containing a function declaration and asserts that it is recognized as a C++ semantic candidate by 'has_cpp_semantic_candidate'. [crates/gcode/src/index/indexer/file.rs:278-284] |
| `cpp_header_candidates_enable_cpp_semantic_resolution` | function | Creates a temporary C++ header containing 'namespace app { class Widget {}; }' and asserts that 'has_cpp_semantic_candidate' recognizes the header path as a semantic candidate. [crates/gcode/src/index/indexer/file.rs:287-293] |
| `objc_header_candidates_do_not_enable_cpp_semantic_resolution` | function | Creates a temporary Objective-C header file containing an '@interface' declaration and asserts that 'has_cpp_semantic_candidate' returns 'false' for it, verifying such headers do not enable C++ semantic resolution. [crates/gcode/src/index/indexer/file.rs:296-302] |

