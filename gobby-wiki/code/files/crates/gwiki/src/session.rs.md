---
title: crates/gwiki/src/session.rs
type: code_file
provenance:
- file: crates/gwiki/src/session.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/session.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/session.rs` exposes 39 indexed API symbols.

## How it fits

`crates/gwiki/src/session.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ResearchScope` | type | Indexed type `ResearchScope` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:15-18] |
| `ResearchScope::project_for_id` | method | Constructs and returns a 'Self::Project' variant by converting 'project_id' into a 'String' and 'root' into a 'PathBuf' and storing them in the corresponding fields. [crates/gwiki/src/session.rs:21-26] |
| `ResearchScope::topic` | method | Constructs and returns a 'Self::Topic' variant by converting 'name' into a 'String' and 'root' into a 'PathBuf' and storing them in the variant fields. [crates/gwiki/src/session.rs:28-33] |
| `ResearchScope::root` | method | Returns a shared reference to the 'Path' stored in the 'root' field for either 'Project' or 'Topic' variants of 'Self'. [crates/gwiki/src/session.rs:35-39] |
| `ResearchScope::set_root` | method | Updates the 'root' field in either 'Project' or 'Topic' by matching on 'self' and assigning 'new_root' to the mutable 'root' reference in place. [crates/gwiki/src/session.rs:41-45] |
| `ResearchScope::from` | method | Converts a 'ResolvedScope' into 'Self' by pattern-matching on 'scope.kind()', constructing a topic variant from the cloned topic name and 'scope.root().to_path_buf()', or a project variant from the cloned 'project_id' and the same root path. [crates/gwiki/src/session.rs:49-56] |
| `DaemonDispatch` | class | 'DaemonDispatch' is a data struct that identifies a daemon dispatch by 'dispatch_id', records the daemon endpoint in 'daemon_base_url', and tracks associated agent run IDs in 'agent_run_ids'. [crates/gwiki/src/session.rs:60-64] |
| `ResearchCodeCitation` | class | 'ResearchCodeCitation' is a serializable Rust struct that records a source file path with optional line number and symbol metadata plus a provenance list of strings, omitting absent fields during serialization. [crates/gwiki/src/session.rs:68-76] |
| `ResearchCodeCitationUnchecked` | class | 'ResearchCodeCitationUnchecked' is an unchecked citation record containing a source file path, optional line number and symbol name, and a provenance string list, with 'line' and 'symbol' deserialized as optional fields by default. [crates/gwiki/src/session.rs:79-87] |
| `ResearchCodeCitation::Error` | type | Indexed type `ResearchCodeCitation::Error` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:90] |
| `ResearchCodeCitation::try_from` | method | Converts a 'ResearchCodeCitationUnchecked' into 'Self' by delegating to 'Self::from_parts(value.file, value.line, value.symbol, value.provenance)' and returning its 'Result'. [crates/gwiki/src/session.rs:92-94] |
| `ResearchCodeCitation::new` | method | Constructs a 'Self' from 'file', 'line', 'symbol', and 'provenance' by delegating to 'Self::from_parts(file.into(), line, symbol, provenance)' and mapping any resulting validation error into 'WikiError::InvalidInput { field: "code_citations", message }'. [crates/gwiki/src/session.rs:98-110] |
| `ResearchCodeCitation::from_parts` | method | 'from_parts' validates that 'file' is non-empty and contains no '..' path components, that 'provenance' is non-empty with no blank entries, and then constructs 'Self' from the supplied 'file', 'line', 'symbol', and 'provenance', otherwise returning a 'String' error. [crates/gwiki/src/session.rs:112-139] |
| `ResearchCodeCitation::file` | method | Returns a shared string slice reference to the 'file' field stored in 'self'. [crates/gwiki/src/session.rs:141-143] |
| `ResearchCodeCitation::line` | method | Returns the stored line number as 'Option<usize>', exposing 'self.line' unchanged. [crates/gwiki/src/session.rs:145-147] |
| `ResearchCodeCitation::symbol` | method | Returns the optional symbol as an 'Option<&str>' by converting the stored string-like field to a borrowed string slice with 'as_deref()'. [crates/gwiki/src/session.rs:149-151] |
| `ResearchCodeCitation::provenance` | method | Returns an immutable slice of the struct’s internal 'provenance' 'String' vector, exposing its provenance entries by reference without cloning. [crates/gwiki/src/session.rs:153-155] |
| `AcceptedResearchNote` | class | 'AcceptedResearchNote' is a serializable Rust data container for an accepted research note, storing its 'title', filesystem 'path', optional 'code_citations' list, and optional 'degradation' metadata string. [crates/gwiki/src/session.rs:159-166] |
| `CompileState` | class | 'CompileState' is a compilation snapshot struct that tracks the current handoff metadata, target topic, bundle path, selected note/source identifiers, accumulated citations, detected conflicting claims and missing evidence, and a boolean write-intent flag. [crates/gwiki/src/session.rs:169-179] |
| `ResearchSession` | class | 'ResearchSession' is a serializable session record that captures a research request, its scope and source constraints, dispatch/agent coordination metadata, accepted notes, and optional compilation state. [crates/gwiki/src/session.rs:182-194] |
| `ResearchSession::new` | method | Constructs a new research session by rejecting 'agent_count == 0', converting 'question' into a 'String', generating a fresh 'session_id' and research prompt from the question, source constraints, and agent count, and initializing the remaining fields with the provided scope/task ID and empty state. [crates/gwiki/src/session.rs:197-224] |
| `ResearchSession::checkpoint_path` | method | Returns the path to 'research-session.json' under 'vault_root' joined with 'crate::vault::STATE_ROOT'. [crates/gwiki/src/session.rs:226-230] |
| `ResearchSession::save_checkpoint` | method | Persists 'self' as pretty-printed JSON to the checkpoint path by creating parent directories, writing through a uniquely named temporary file with 'sync_all', then atomically renaming it into place and converting I/O/serialization failures into 'WikiError'. [crates/gwiki/src/session.rs:232-291] |
| `ResearchSession::load_checkpoint` | method | Loads a checkpoint JSON from 'Self::checkpoint_path(vault_root)', maps I/O and deserialization failures into 'WikiError', validates and normalizes the checkpoint’s scope root against 'vault_root', updates 'session.scope' with the normalized root, and returns the reconstructed session. [crates/gwiki/src/session.rs:293-309] |

_7 more symbol(s) not shown — run `gcode outline crates/gwiki/src/session.rs` for the full list._

_Verified by 8 in-file unit tests._

