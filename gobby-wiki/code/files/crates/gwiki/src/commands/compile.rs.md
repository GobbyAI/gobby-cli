---
title: crates/gwiki/src/commands/compile.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/compile.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/compile.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/compile.rs` exposes 23 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/compile.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Indexed function `execute` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:18-100] |
| `compile_topic_seed` | function | Indexed function `compile_topic_seed` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:102-110] |
| `load_compile_session` | function | Indexed function `load_compile_session` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:112-132] |
| `resolve_compile_topic` | function | Indexed function `resolve_compile_topic` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:134-142] |
| `apply_source_selection` | function | Indexed function `apply_source_selection` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:144-151] |
| `resolve_source_notes` | function | Indexed function `resolve_source_notes` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:153-167] |
| `resolve_source_selector` | function | Indexed function `resolve_source_selector` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:169-203] |
| `accepted_note_from_source` | function | Indexed function `accepted_note_from_source` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:205-237] |
| `ExplainerTransport` | type | Indexed type `ExplainerTransport` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:242-252] |
| `ExplainerTransport::is_active` | method | Indexed method `ExplainerTransport::is_active` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:255-257] |
| `ExplainerTransport::route_label` | method | Indexed method `ExplainerTransport::route_label` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:259-264] |
| `ExplainerTransport::generate` | method | Indexed method `ExplainerTransport::generate` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:266-287] |
| `resolve_explainer_transport` | function | Indexed function `resolve_explainer_transport` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:293-323] |
| `routing_label` | function | Indexed function `routing_label` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:325-332] |
| `source_record` | function | Indexed function `source_record` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:340-360] |
| `write_raw_source` | function | Indexed function `write_raw_source` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:362-366] |
| `source_selectors_resolve_id_raw_path_location_and_canonical_location` | function | Indexed function `source_selectors_resolve_id_raw_path_location_and_canonical_location` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:369-423] |
| `source_selection_dedupes_by_source_id_in_selector_order` | function | Indexed function `source_selection_dedupes_by_source_id_in_selector_order` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:426-458] |
| `missing_source_selector_reports_source_not_found` | function | Indexed function `missing_source_selector_reports_source_not_found` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:461-479] |
| `ambiguous_non_id_selector_reports_invalid_input` | function | Indexed function `ambiguous_non_id_selector_reports_invalid_input` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:482-501] |
| `missing_raw_file_for_selected_source_reports_raw_source_not_found` | function | Indexed function `missing_raw_file_for_selected_source_reports_raw_source_not_found` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:504-525] |
| `missing_checkpoint_with_topic_seed_creates_fresh_compile_session` | function | Indexed function `missing_checkpoint_with_topic_seed_creates_fresh_compile_session` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:528-538] |
| `missing_checkpoint_without_topic_seed_requires_topic` | function | Indexed function `missing_checkpoint_without_topic_seed_requires_topic` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:541-557] |

