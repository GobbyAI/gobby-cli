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
| `Command` | type | Indexed type `Command` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:11-132] |
| `ReadTarget` | type | Indexed type `ReadTarget` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:135-138] |
| `SetupOptions` | class | SetupOptions is a configuration struct that encapsulates parameters for database connectivity, FalkorDB and Qdrant service integration, and embedding provider configuration. [crates/gwiki/src/api.rs:141-155] |
| `BenchmarkOptions` | class | 'BenchmarkOptions' is a public struct that encapsulates a single configuration parameter ('retrieval_candidates: usize') for specifying the number of retrieval candidates to use in benchmark operations. [crates/gwiki/src/api.rs:158-160] |
| `BenchmarkOptions::default` | method | Returns a new instance of 'Self' with the 'retrieval_candidates' field initialized to the constant value 'Self::DEFAULT_RETRIEVAL_CANDIDATES'. [crates/gwiki/src/api.rs:168-172] |
| `IngestFileOptions` | class | IngestFileOptions is a configuration struct that controls file ingestion parameters including AI processing toggles, translation settings, video frame sampling intervals, and optional AI model routing for transcription, vision, and text analysis. [crates/gwiki/src/api.rs:177-185] |
| `SyncSessionsOptions` | class | 'SyncSessionsOptions' is a configuration struct providing optional parameters for session synchronization: an archive directory path and a maximum session count limit. [crates/gwiki/src/api.rs:188-191] |
| `ReviewReportOptions` | class | ReviewReportOptions is a configuration struct that specifies a collection of files and symbols to analyze, an optional diff file path, and an output destination for generating a code review report. [crates/gwiki/src/api.rs:194-199] |
| `IngestFileOptions::apply_to_ai_context` | method | # Summary Conditionally applies transcription, vision, and text routing configurations along with translation target language settings to the AiContext bindings, or disables all AI bindings if the 'no_ai' flag is set. [crates/gwiki/src/api.rs:202-230] |
| `ScopeSelection` | type | Indexed type `ScopeSelection` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:235-239] |
| `ScopeSelection::detect` | method | The 'detect' method is a zero-parameter constructor function that returns the 'Detect' variant of the implementing enum type. [crates/gwiki/src/api.rs:242-244] |
| `ScopeSelection::project` | method | Constructs a 'ProjectRoot' enum variant by converting the provided path argument into a 'PathBuf'. [crates/gwiki/src/api.rs:246-248] |
| `ScopeSelection::topic` | method | This method is a generic constructor that accepts any type implementing 'Into<String>', converts it to a 'String', and returns a 'Self::Topic' enum variant. [crates/gwiki/src/api.rs:250-252] |
| `ScopeSelection::identity` | method | Maps the enum variant to its corresponding 'ScopeIdentity' type: global identity for 'Detect', project-scoped identity for 'ProjectRoot', and topic-scoped identity for 'Topic'. [crates/gwiki/src/api.rs:254-260] |
| `ScopeSelection::is_project` | method | This method returns 'true' if the instance matches the 'ProjectRoot' enum variant, otherwise 'false'. [crates/gwiki/src/api.rs:262-264] |
| `ScopeSelection::project_root` | method | Returns an optional reference to the inner path if 'self' is the 'ProjectRoot' variant, otherwise returns 'None' for 'Detect' and 'Topic' variants. [crates/gwiki/src/api.rs:266-271] |
| `ScopeSelection::topic_name` | method | Returns an optional string reference to the inner topic string if the enum variant is Topic, otherwise returns None for Detect and ProjectRoot variants. [crates/gwiki/src/api.rs:273-278] |
| `ScopeSelection::default` | method | The 'default()' method implements the 'Default' trait by delegating to the 'detect()' associated function to construct and return a new instance of the type. [crates/gwiki/src/api.rs:282-284] |
| `ScopeKind` | type | Indexed type `ScopeKind` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:289-293] |
| `ScopeKind::as_str` | method | Converts the enum value into a ''static' string reference corresponding to its variant through exhaustive pattern matching. [crates/gwiki/src/api.rs:296-302] |
| `ScopeIdentity` | class | ScopeIdentity is a public struct that pairs a ScopeKind discriminant with a unique String identifier to represent an entity within a specific scope context. [crates/gwiki/src/api.rs:306-309] |
| `ScopeIdentity::global` | method | Returns a new instance of Self with 'ScopeKind::Global' and an identifier of '"default"'. [crates/gwiki/src/api.rs:312-317] |
| `ScopeIdentity::project` | method | Constructs a new instance of the containing type with 'kind' set to 'ScopeKind::Project' and 'id' set to the provided value converted into a 'String'. [crates/gwiki/src/api.rs:319-324] |
| `ScopeIdentity::topic` | method | Creates a new instance of 'Self' with 'kind' set to 'ScopeKind::Topic' and 'id' converted from any type implementing 'Into<String>'. [crates/gwiki/src/api.rs:326-331] |

_3 more symbol(s) not shown — run `gcode outline crates/gwiki/src/api.rs` for the full list._

_Verified by 4 in-file unit tests._

