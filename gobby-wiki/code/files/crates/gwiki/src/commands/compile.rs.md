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

`crates/gwiki/src/commands/compile.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | 'execute' resolves the requested scope and compile session, optionally filters sources, determines the compile topic, probes daemon and explainer transport capabilities, invokes 'wiki_compile::compile_to_wiki_with_options' to generate a wiki article with the selected outline/target kind/write intent, and then packages the result into a 'CommandOutcome' or propagates 'WikiError'. [crates/gwiki/src/commands/compile.rs:18-100] |
| `compile_topic_seed` | function | Returns the provided 'topic' as an owned 'String', or if 'topic' is 'None' and 'research_scope' is 'ResearchScope::Topic', clones and returns that scope’s 'name'; otherwise it returns 'None'. [crates/gwiki/src/commands/compile.rs:102-110] |
| `load_compile_session` | function | Loads a 'ResearchSession' from the checkpoint at 'research_scope.root()', or if the checkpoint is missing creates a new session from 'topic_seed' and 'research_scope', otherwise returns the underlying error. [crates/gwiki/src/commands/compile.rs:112-132] |
| `resolve_compile_topic` | function | Returns 'topic_seed' when provided, otherwise falls back to 'session.compile_state.topic' if present, and finally to 'session.question.clone()' if no compile state exists. [crates/gwiki/src/commands/compile.rs:134-142] |
| `apply_source_selection` | function | Loads the source manifest from the session scope root, resolves the given selector strings into accepted notes, stores them on 'session.accepted_notes', and persists the updated session state by saving a checkpoint. [crates/gwiki/src/commands/compile.rs:144-151] |
| `resolve_source_notes` | function | Resolves each selector against the manifest, de-duplicates by source record ID, converts the unique records into 'session::AcceptedResearchNote' values using 'vault_root', and returns them as a 'Vec' or propagates any 'WikiError'. [crates/gwiki/src/commands/compile.rs:153-167] |
| `resolve_source_selector` | function | Resolves a trimmed source selector to a unique 'SourceRecord' by matching first on 'id', then on raw source path, then on 'location' or 'canonical_location', returning 'NotFound' if none match and 'InvalidInput' if multiple records match. [crates/gwiki/src/commands/compile.rs:169-203] |
| `accepted_note_from_source` | function | Validates that the raw source file for a 'SourceRecord' exists under 'vault_root' and, if so, constructs an 'AcceptedResearchNote' using the record’s title or location, the raw source path, and empty/default citation and degradation fields. [crates/gwiki/src/commands/compile.rs:205-237] |
| `ExplainerTransport` | type | Indexed type `ExplainerTransport` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:242-252] |
| `ExplainerTransport::is_active` | method | 'is_active' returns 'true' for every 'Self' variant except 'Self::Off', for which it returns 'false'. [crates/gwiki/src/commands/compile.rs:255-257] |
| `ExplainerTransport::route_label` | method | Returns the static route label '"off"' for 'Self::Off', and otherwise delegates to 'routing_label(*route)' for both 'Unresolved' and 'Resolved' variants. [crates/gwiki/src/commands/compile.rs:259-264] |
| `ExplainerTransport::generate` | method | 'generate' returns an error when synthesis is 'Off' or 'Unresolved', and otherwise dispatches to either daemon-based or text-based AI generation using the resolved route and context, converting any generation error to a string and packaging the resulting text, model, and routing label into an 'ExplainerResponse'. [crates/gwiki/src/commands/compile.rs:266-287] |
| `resolve_explainer_transport` | function | Returns 'ExplainerTransport::Off' for 'AiRouting::Off' or any non-daemon/direct effective route, otherwise resolves AI config and returns 'Resolved' with the computed 'AiContext' for 'Daemon' or 'Direct', and on config-source failure returns 'Unresolved' only for requested 'Daemon'/'Direct' routes. [crates/gwiki/src/commands/compile.rs:293-323] |
| `routing_label` | function | Returns a static string label for an 'AiRouting' variant, mapping 'Auto' to '"auto"', 'Daemon' to '"daemon"', 'Direct' to '"direct"', and 'Off' to '"off"'. [crates/gwiki/src/commands/compile.rs:325-332] |
| `source_record` | function | Creates a 'SourceRecord' for a Markdown source from the given identifiers and optional title, populating fixed metadata such as a synthetic fetched timestamp, hash, manual ingestion method, pending compile status, and leaving citation/license/replay unset. [crates/gwiki/src/commands/compile.rs:340-360] |
| `write_raw_source` | function | Creates the parent directories for the raw-source file under 'root' and writes a one-line file containing '# {record.id}\n' at the path derived from 'record.id'. [crates/gwiki/src/commands/compile.rs:362-366] |

_Verified by 7 in-file unit tests._

