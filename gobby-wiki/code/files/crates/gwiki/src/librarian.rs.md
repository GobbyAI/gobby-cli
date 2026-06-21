---
title: crates/gwiki/src/librarian.rs
type: code_file
provenance:
- file: crates/gwiki/src/librarian.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/librarian.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/librarian.rs` exposes 35 indexed API symbols.

## How it fits

`crates/gwiki/src/librarian.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Options` | class | 'Options' is a public struct containing four boolean fields that represent configuration flags for PostgreSQL indexing requirements and feature availability states (shared code graph, semantic analysis, and model support). [crates/gwiki/src/librarian.rs:15-20] |
| `Options::offline` | method | This method constructs and returns a 'Self' instance with all four capability flags ('require_postgres_index', 'shared_code_graph_available', 'semantic_available', and 'model_available') initialized to 'false', representing an offline configuration state. [crates/gwiki/src/librarian.rs:23-30] |
| `Options::default` | method | This method returns a default instance of 'Self' with 'require_postgres_index' set to 'true' and all other fields initialized from 'Self::offline()'. [crates/gwiki/src/librarian.rs:34-39] |
| `ProposalsReport` | class | ProposalsReport is a struct that aggregates proposal analysis results, containing scope identification, verification checks, suggested tasks and patches, librarian artifacts, and dependency classification data. [crates/gwiki/src/librarian.rs:43-50] |
| `CheckReport` | class | CheckReport is a Rust struct that encapsulates a named availability check result with an optional note and associated file path items, designed for serialization. [crates/gwiki/src/librarian.rs:63-69] |
| `SuggestedTask` | class | SuggestedTask is a public struct that aggregates a task suggestion containing a String title, String description, and a Vec<PathBuf> for associated filesystem paths. [crates/gwiki/src/librarian.rs:72-76] |
| `SuggestedPatchDiff` | class | A struct representing a proposed patch containing the target file path, summary description, diff content, and flags indicating canonical applicability and whether user acceptance is required. [crates/gwiki/src/librarian.rs:79-85] |
| `LibrarianArtifacts` | class | 'LibrarianArtifacts' is a struct that encapsulates file paths ('PathBuf') to proposal and audit artifact outputs in JSON and Markdown formats. [crates/gwiki/src/librarian.rs:88-93] |
| `DependencyClassification` | class | 'DependencyClassification' is a struct that categorizes dependencies into three static string reference fields: 'hard' and 'optional' vectors for required and optional dependencies, and a single 'multimodal' field for multimodal classification. [crates/gwiki/src/librarian.rs:96-100] |
| `run` | function | Aggregates results from health inspection, auditing, linting, and provenance graph analysis on a scoped wiki vault to generate a ProposalsReport. [crates/gwiki/src/librarian.rs:102-198] |
| `render_text` | function | Renders a 'ProposalsReport' into a formatted UTF-8 text string displaying the scope, availability-status checks with item paths, optional notes, and suggested tasks. [crates/gwiki/src/librarian.rs:200-230] |
| `available_check` | function | Constructs and returns a 'CheckReport' struct with the provided static name and 'PathBuf' items, with availability hardcoded to 'true' and note set to 'None'. [crates/gwiki/src/librarian.rs:232-239] |
| `optional_check` | function | Constructs a CheckReport with a conditionally populated note field (only if unavailable) and items list (only if available). [crates/gwiki/src/librarian.rs:241-253] |
| `weak_provenance_pages` | function | Filters CodeWiki pages that lack entries in the provided provenance graph and returns their sorted relative paths. [crates/gwiki/src/librarian.rs:255-264] |
| `provenance_mentions_page` | function | This function returns 'true' if the 'ProvenanceGraph' contains at least one link whose 'section.page_path' matches the provided 'Path' argument. [crates/gwiki/src/librarian.rs:266-272] |
| `outdated_codewiki_pages` | function | Extracts and returns the sorted relative paths of codewiki pages whose frontmatter contains the flag 'codewiki_status' set to 'stale'. [crates/gwiki/src/librarian.rs:274-283] |
| `page_is_codewiki` | function | Checks if a WikiPage's 'generated_by' frontmatter field contains the string "codewiki". [crates/gwiki/src/librarian.rs:285-291] |
| `frontmatter_flag` | function | This function returns 'true' if the frontmatter metadata value at the specified key matches the expected string (for String types) or is 'true' when the expected value is "true" (for Bool types), and returns 'false' otherwise. [crates/gwiki/src/librarian.rs:293-303] |
| `suggested_tasks` | function | Produces a vector of suggested maintenance tasks by conditionally creating task recommendations for each non-empty collection of wiki documentation quality issues (uncited sources, stale pages, broken links, weak provenance, and outdated codewiki pages). [crates/gwiki/src/librarian.rs:305-355] |
| `push_task` | function | Conditionally appends a SuggestedTask containing the provided title, description, and paths to a mutable vector when the include boolean flag is true. [crates/gwiki/src/librarian.rs:357-371] |
| `suggested_patch_diffs` | function | Generates deduplicated suggested patch diffs that inject HTML citation-refresh directives into file paths derived from combined stale and missing-citation collections. [crates/gwiki/src/librarian.rs:373-390] |
| `unique_paths` | function | This function deduplicates and lexicographically sorts an iterator of 'PathBuf' values into a vector by collecting through a 'BTreeSet'. [crates/gwiki/src/librarian.rs:392-394] |
| `artifacts` | function | Returns a 'LibrarianArtifacts' struct initialized with four 'PathBuf' instances referencing librarian metadata artifact files (proposals, audit annotations, and stale pages). [crates/gwiki/src/librarian.rs:396-403] |
| `persist_report` | function | Serializes a ProposalsReport to the vault's librarian metadata directory as JSON and markdown artifacts, including rendered proposals and audit/stale-page validation checks. [crates/gwiki/src/librarian.rs:405-434] |

_4 more symbol(s) not shown — run `gcode outline crates/gwiki/src/librarian.rs` for the full list._

_Verified by 7 in-file unit tests._

