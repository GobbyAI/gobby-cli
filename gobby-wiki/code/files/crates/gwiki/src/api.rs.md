---
title: crates/gwiki/src/api.rs
type: code_file
provenance:
- file: crates/gwiki/src/api.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/api.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/api.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gwiki/src/api.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Command` | type | Indexed type `Command` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:11-130] |
| `ReadTarget` | type | Indexed type `ReadTarget` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:133-136] |
| `SetupOptions` | class | 'SetupOptions' is a configuration struct for setup/runtime provisioning that toggles standalone and service-free modes and optionally supplies database, FalkorDB, Qdrant, and embedding provider connection and model parameters. [crates/gwiki/src/api.rs:139-153] |
| `BenchmarkOptions` | class | 'BenchmarkOptions' is a struct that configures benchmarking by storing a single 'usize' field, 'retrieval_candidates', representing the number of retrieval candidates to use. [crates/gwiki/src/api.rs:156-158] |
| `BenchmarkOptions::default` | method | Returns a new 'Self' initialized with 'retrieval_candidates' set to 'Self::DEFAULT_RETRIEVAL_CANDIDATES'. [crates/gwiki/src/api.rs:166-170] |
| `IngestFileOptions` | class | 'IngestFileOptions' configures file ingestion behavior, including whether AI is disabled, whether translation is performed and into which target language, the optional video frame sampling interval, and optional AI routing overrides for transcription, vision, and text processing. [crates/gwiki/src/api.rs:175-183] |
| `SyncSessionsOptions` | class | 'SyncSessionsOptions' configures session synchronization with an optional archive directory ('archive_dir') and an optional maximum number of sessions to process or retain ('limit'). [crates/gwiki/src/api.rs:186-189] |
| `ReviewReportOptions` | class | 'ReviewReportOptions' is a configuration struct that specifies the target files and symbols to review, an optional diff file path, and the output destination or format as a string. [crates/gwiki/src/api.rs:192-197] |
| `IngestFileOptions::apply_to_ai_context` | method | 'apply_to_ai_context' mutates an 'AiContext' by copying any configured routing overrides into the relevant audio/vision/text bindings (using 'audio_translate' when 'translate' is set, otherwise 'audio_transcribe', and also propagating 'target_lang' for translation), or, if 'no_ai' is enabled, disables all AI bindings by setting their routing to 'AiRouting::Off'. [crates/gwiki/src/api.rs:200-228] |
| `ScopeSelection` | type | Indexed type `ScopeSelection` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:233-237] |
| `ScopeSelection::detect` | method | Returns the 'Detect' enum variant by constructing 'Self::Detect'. [crates/gwiki/src/api.rs:240-242] |
| `ScopeSelection::project` | method | Constructs and returns a 'Self::ProjectRoot' variant by converting the provided 'root' into a 'PathBuf'. [crates/gwiki/src/api.rs:244-246] |
| `ScopeSelection::topic` | method | Constructs and returns a 'Self' value by converting the input 'topic' into a 'String' and wrapping it in the 'Self::Topic' variant. [crates/gwiki/src/api.rs:248-250] |
| `ScopeSelection::identity` | method | Returns a 'ScopeIdentity' by mapping 'Detect' to the global identity, 'ProjectRoot(root)' to a project identity built from 'root'’s display string, and 'Topic(topic)' to a topic identity cloned from 'topic'. [crates/gwiki/src/api.rs:252-258] |
| `ScopeSelection::is_project` | method | Returns 'true' when 'self' is the 'ProjectRoot' variant and 'false' otherwise. [crates/gwiki/src/api.rs:260-262] |
| `ScopeSelection::project_root` | method | Returns the underlying project-root 'Path' as 'Some(&Path)' when 'self' is 'Self::ProjectRoot', and 'None' for 'Self::Detect' or 'Self::Topic(_)'. [crates/gwiki/src/api.rs:264-269] |
| `ScopeSelection::topic_name` | method | Returns 'Some(&str)' containing the topic string when 'self' is 'Self::Topic', and 'None' for 'Self::Detect' or 'Self::ProjectRoot(_)'. [crates/gwiki/src/api.rs:271-276] |
| `ScopeSelection::default` | method | Returns 'Self::detect()', using automatic detection to construct the default instance. [crates/gwiki/src/api.rs:280-282] |
| `ScopeKind` | type | Indexed type `ScopeKind` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:287-291] |
| `ScopeKind::as_str` | method | Returns the ''static' string literal representation of the enum value, mapping 'Global' to '"global"', 'Project' to '"project"', and 'Topic' to '"topic"'. [crates/gwiki/src/api.rs:294-300] |
| `ScopeIdentity` | class | 'ScopeIdentity' is a struct that uniquely identifies a scope by storing its 'ScopeKind' and a string 'id'. [crates/gwiki/src/api.rs:304-307] |
| `ScopeIdentity::global` | method | Constructs and returns a 'Self' value representing the global scope, with 'kind' set to 'ScopeKind::Global' and 'id' initialized to '"default"'. [crates/gwiki/src/api.rs:310-315] |
| `ScopeIdentity::project` | method | Constructs and returns a 'Self' value representing a project-scoped scope by setting 'kind' to 'ScopeKind::Project' and initializing 'id' from the provided 'Into<String>' argument. [crates/gwiki/src/api.rs:317-322] |
| `ScopeIdentity::topic` | method | Constructs and returns a 'Self' value with 'kind' set to 'ScopeKind::Topic' and 'id' initialized from the provided 'id' converted into a 'String'. [crates/gwiki/src/api.rs:324-329] |

_3 more symbol(s) not shown — run `gcode outline crates/gwiki/src/api.rs` for the full list._

_Verified by 4 in-file unit tests._

