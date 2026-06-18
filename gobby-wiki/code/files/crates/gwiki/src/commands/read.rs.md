---
title: crates/gwiki/src/commands/read.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/read.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/read.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/read.rs` exposes 36 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/read.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Indexed function `execute` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:17-28] |
| `read_path` | function | Indexed function `read_path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:30-57] |
| `read_title` | function | Indexed function `read_title` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:59-85] |
| `read_existing_path` | function | Indexed function `read_existing_path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:87-114] |
| `configured_read_max_bytes` | function | Indexed function `configured_read_max_bytes` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:116-122] |
| `read_markdown_prefix` | function | Indexed function `read_markdown_prefix` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:124-152] |
| `normalize_requested_path` | function | Indexed function `normalize_requested_path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:154-181] |
| `readable_path_degradation` | function | Indexed function `readable_path_degradation` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:183-197] |
| `is_readable_wiki_path` | function | Indexed function `is_readable_wiki_path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:199-211] |
| `title_candidates` | function | Indexed function `title_candidates` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:213-219] |
| `title_candidates_with_scan_budget` | function | Indexed function `title_candidates_with_scan_budget` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:221-235] |
| `TitleCandidateSearch` | class | Indexed class `TitleCandidateSearch` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:237-241] |
| `collect_title_candidates` | function | Indexed function `collect_title_candidates` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:243-312] |
| `first_heading` | function | Indexed function `first_heading` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:314-320] |
| `normal_components` | function | Indexed function `normal_components` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:322-329] |
| `render` | function | Indexed function `render` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:331-340] |
| `render_text` | function | Indexed function `render_text` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:342-361] |
| `ReadOutput` | class | Indexed class `ReadOutput` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:364-378] |
| `ReadFoundContent` | class | Indexed class `ReadFoundContent` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:380-385] |
| `ReadOutput::found` | method | Indexed method `ReadOutput::found` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:388-410] |
| `ReadOutput::not_found` | method | Indexed method `ReadOutput::not_found` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:412-427] |
| `ReadOutput::invalid_request` | method | Indexed method `ReadOutput::invalid_request` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:429-442] |
| `ReadOutput::ambiguous` | method | Indexed method `ReadOutput::ambiguous` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:444-461] |
| `ReadOutput::empty` | method | Indexed method `ReadOutput::empty` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:463-486] |
| `ReadRequested` | class | Indexed class `ReadRequested` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:490-493] |
| `ReadRequested::path` | method | Indexed method `ReadRequested::path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:496-501] |
| `ReadRequested::title` | method | Indexed method `ReadRequested::title` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:503-508] |
| `ReadCandidate` | class | Indexed class `ReadCandidate` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:512-515] |
| `ReadDegradation` | class | Indexed class `ReadDegradation` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:518-522] |
| `ReadDegradation::display_label` | method | Indexed method `ReadDegradation::display_label` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:525-532] |
| `ReadDegradation::invalid_request` | method | Indexed method `ReadDegradation::invalid_request` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:534-540] |
| `ReadDegradation::not_found` | method | Indexed method `ReadDegradation::not_found` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:542-548] |
| `ReadDegradation::ambiguous` | method | Indexed method `ReadDegradation::ambiguous` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:550-556] |
| `read_path_caps_content_and_marks_truncated` | function | Indexed function `read_path_caps_content_and_marks_truncated` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:566-592] |
| `title_search_stops_at_max_depth` | function | Indexed function `title_search_stops_at_max_depth` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:595-608] |
| `title_search_stops_at_scan_budget` | function | Indexed function `title_search_stops_at_scan_budget` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:611-622] |

