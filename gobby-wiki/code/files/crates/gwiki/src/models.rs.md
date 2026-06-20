---
title: crates/gwiki/src/models.rs
type: code_file
provenance:
- file: crates/gwiki/src/models.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/models.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/models.rs` exposes 21 indexed API symbols.

## How it fits

`crates/gwiki/src/models.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiScope` | type | Indexed type `WikiScope` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:12-15] |
| `WikiScope::kind` | method | Returns the static string '"project"' for 'Self::Project' and '"topic"' for 'Self::Topic', providing a variant discriminator. [crates/gwiki/src/models.rs:18-23] |
| `WikiScope::identity` | method | Returns a '&str' borrowed from the enum’s active variant, yielding 'project_id' for 'Self::Project' and 'name' for 'Self::Topic'. [crates/gwiki/src/models.rs:25-30] |
| `WikiScope::project_id` | method | Returns 'Some(&str)' containing the project ID when 'self' is 'Self::Project', and 'None' when 'self' is 'Self::Topic'. [crates/gwiki/src/models.rs:32-37] |
| `WikiScope::topic_name` | method | Returns 'None' for 'Project' variants and 'Some(&name)' for 'Topic' variants, exposing the topic name as an optional string slice. [crates/gwiki/src/models.rs:39-44] |
| `WikiScope::vector_collection_name` | method | Returns the appropriate vector collection name for 'self' by delegating to 'project_collection_name(project_id)' for 'Self::Project' and 'topic_collection_name(name)' for 'Self::Topic', propagating any 'WikiError' from those helpers. [crates/gwiki/src/models.rs:46-51] |
| `WikiSourceKind` | type | Indexed type `WikiSourceKind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:55-61] |
| `WikiSourceKind::as_str` | method | Returns a ''static' string slice naming the enum variant, mapping 'Raw', 'SourceNote', 'Concept', 'Topic', and 'Inbox' to '"raw"', '"source_note"', '"concept"', '"topic"', and '"inbox"' respectively. [crates/gwiki/src/models.rs:64-72] |
| `WikiProvenance` | class | 'WikiProvenance' is a provenance record that stores the original 'source_path', an optional 'captured_from' reference, and a 'content_hash' for identifying and verifying the captured wiki content. [crates/gwiki/src/models.rs:76-80] |
| `WikiDocumentRow` | class | 'WikiDocumentRow' is a denormalized persistence record for a wiki document, storing its canonical scope ('scope_kind', 'scope_id') plus query-friendly scope mirrors ('project_id', 'topic_name'), document identity/path, source kind, content hash, and structured 'frontmatter'/'provenance' metadata. [crates/gwiki/src/models.rs:83-97] |
| `WikiDocumentRow::new` | method | Constructs a new instance by converting 'id', 'path', and 'content_hash' into owned strings, extracting 'scope_kind', 'scope_id', optional 'project_id' and 'topic_name' from 'WikiScope', and storing the provided 'source_kind', 'frontmatter', and 'provenance' values. [crates/gwiki/src/models.rs:100-125] |
| `WikiDocumentRow::validate_scope_consistency` | method | Returns 'Ok(())' only when the denormalized scope columns are consistent with 'scope_kind' ('project' requires 'project_id == scope_id' and no 'topic_name'; 'topic' requires 'topic_name == scope_id' and no 'project_id'), otherwise returns 'WikiError::InvalidInput' for 'scope'. [crates/gwiki/src/models.rs:127-149] |
| `validate_project_id` | function | Returns the result of validating 'project_id' as a project ID by delegating to 'validate_scope_id("project id", project_id)', yielding either a normalized 'String' or a 'WikiError'. [crates/gwiki/src/models.rs:152-154] |
| `validate_topic_name` | function | Validates a topic name by delegating to 'validate_scope_id("topic name", topic_name)' and returning either the validated 'String' or a 'WikiError'. [crates/gwiki/src/models.rs:156-158] |
| `project_collection_name` | function | Validates the given project ID and returns the corresponding immutable GWiki project collection name as a 'String', panicking only if the infallible project-scoped collection-name construction fails. [crates/gwiki/src/models.rs:160-166] |
| `topic_collection_name` | function | Validates 'topic_name' and returns the corresponding infallible 'gwiki' topic-scoped collection name as a 'String', propagating any 'WikiError' from validation. [crates/gwiki/src/models.rs:168-174] |
| `validate_scope_id` | function | Trims the input and returns it as an owned 'String' only if it is nonempty, not '"."' or '".."', contains no ':', '/', '\', or ASCII control characters, otherwise returns 'WikiError::InvalidScope' with a formatted detail message. [crates/gwiki/src/models.rs:176-191] |

_Verified by 4 in-file unit tests._

