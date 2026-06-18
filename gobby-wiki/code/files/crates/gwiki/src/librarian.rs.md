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

`crates/gwiki/src/librarian.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Options` | class | Indexed class `Options` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:15-20] |
| `Options::offline` | method | Indexed method `Options::offline` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:23-30] |
| `Options::default` | method | Indexed method `Options::default` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:34-39] |
| `ProposalsReport` | class | Indexed class `ProposalsReport` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:43-50] |
| `ProposalsReport::check` | method | Indexed method `ProposalsReport::check` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:54-59] |
| `CheckReport` | class | Indexed class `CheckReport` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:63-69] |
| `SuggestedTask` | class | Indexed class `SuggestedTask` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:72-76] |
| `SuggestedPatchDiff` | class | Indexed class `SuggestedPatchDiff` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:79-85] |
| `LibrarianArtifacts` | class | Indexed class `LibrarianArtifacts` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:88-93] |
| `DependencyClassification` | class | Indexed class `DependencyClassification` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:96-100] |
| `run` | function | Indexed function `run` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:102-198] |
| `render_text` | function | Indexed function `render_text` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:200-230] |
| `available_check` | function | Indexed function `available_check` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:232-239] |
| `optional_check` | function | Indexed function `optional_check` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:241-253] |
| `weak_provenance_pages` | function | Indexed function `weak_provenance_pages` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:255-264] |
| `provenance_mentions_page` | function | Indexed function `provenance_mentions_page` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:266-272] |
| `outdated_codewiki_pages` | function | Indexed function `outdated_codewiki_pages` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:274-283] |
| `page_is_codewiki` | function | Indexed function `page_is_codewiki` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:285-291] |
| `frontmatter_flag` | function | Indexed function `frontmatter_flag` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:293-303] |
| `suggested_tasks` | function | Indexed function `suggested_tasks` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:305-355] |
| `push_task` | function | Indexed function `push_task` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:357-371] |
| `suggested_patch_diffs` | function | Indexed function `suggested_patch_diffs` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:373-390] |
| `unique_paths` | function | Indexed function `unique_paths` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:392-394] |
| `artifacts` | function | Indexed function `artifacts` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:396-403] |
| `persist_report` | function | Indexed function `persist_report` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:405-434] |
| `write_json` | function | Indexed function `write_json` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:436-452] |
| `write_text` | function | Indexed function `write_text` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:454-461] |
| `librarian_detects_and_proposes_without_rewriting_pages` | function | Indexed function `librarian_detects_and_proposes_without_rewriting_pages` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:475-562] |
| `librarian_filters_codewiki_checks_to_selected_scope` | function | Indexed function `librarian_filters_codewiki_checks_to_selected_scope` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:565-591] |
| `librarian_degrades_each_optional_check_independently` | function | Indexed function `librarian_degrades_each_optional_check_independently` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:594-617] |
| `librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale` | function | Indexed function `librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:620-639] |
| `librarian_codewiki_path_checks_are_sorted` | function | Indexed function `librarian_codewiki_path_checks_are_sorted` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:642-656] |
| `librarian_requires_configured_postgres_index` | function | Indexed function `librarian_requires_configured_postgres_index` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:660-679] |
| `write_page` | function | Indexed function `write_page` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:681-685] |
| `codewiki_page` | function | Indexed function `codewiki_page` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:687-701] |

