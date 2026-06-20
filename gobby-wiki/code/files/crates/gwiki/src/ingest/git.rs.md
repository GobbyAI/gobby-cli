---
title: crates/gwiki/src/ingest/git.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/git.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/git.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/git.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/git.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GitFileSnapshot` | class | The 'GitFileSnapshot' struct represents a snapshot of a file, containing its file path as a 'String' and its raw content as a vector of bytes. [crates/gwiki/src/ingest/git.rs:15-18] |
| `GitRepositorySnapshot` | class | The 'GitRepositorySnapshot' struct represents a point-in-time snapshot of a Git repository, capturing its remote URL, commit SHA, retrieval timestamp, and a collection of individual file snapshots. [crates/gwiki/src/ingest/git.rs:22-27] |
| `ingest_repository` | function | The 'ingest_repository' function validates that a 'GitRepositorySnapshot' contains files, registers its metadata and raw content as a 'SourceManifest' within the vault, and then renders and indexes a markdown representation of the repository into the wiki store. [crates/gwiki/src/ingest/git.rs:30-55] |
| `snapshot_content_bytes` | function | This function serializes a 'GitRepositorySnapshot' into a byte vector by concatenating its remote URL, commit SHA, and individual file paths and contents separated by structured delimiters and newlines. [crates/gwiki/src/ingest/git.rs:58-74] |
| `render_git_markdown` | function | The 'render_git_markdown' function serializes a 'GitRepositorySnapshot' into a Markdown string containing structured repository metadata, a main heading, and formatted sections for each repository file displaying its path and lossily-decoded UTF-8 contents within code fences. [crates/gwiki/src/ingest/git.rs:77-109] |
| `git_markdown_metadata` | function | This function serializes a slice of key-value string pairs into a YAML-formatted Markdown frontmatter block with single-line values. [crates/gwiki/src/ingest/git.rs:112-127] |
| `code_fence_info` | function | The 'code_fence_info' function extracts and sanitizes the file extension of a given path, returning a string containing only its ASCII alphanumeric, underscore, and hyphen characters, or defaulting to '"text"' if the extension is missing or empty. [crates/gwiki/src/ingest/git.rs:130-142] |
| `markdown_code_fence` | function | This function determines and returns a safe Markdown code fence delimiter string of at least three characters by selecting either backticks or tildes—whichever has a shorter maximum consecutive run in the input text—and repeating it one more time than its maximum detected run. [crates/gwiki/src/ingest/git.rs:145-154] |
| `bounded_max_run` | function | The function calculates the maximum length of consecutive occurrences of a specified delimiter character in a string, capped at 'MAX_CODE_FENCE_LEN - 1'. [crates/gwiki/src/ingest/git.rs:157-172] |

_Verified by 3 in-file unit tests._

