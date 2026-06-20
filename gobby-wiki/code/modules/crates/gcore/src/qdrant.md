---
title: crates/gcore/src/qdrant
type: code_module
provenance:
- file: crates/gcore/src/qdrant/naming.rs
- file: crates/gcore/src/qdrant/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/qdrant

Parent: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

The `crates/gcore/src/qdrant` module owns Qdrant collection naming plus the client-facing behavior exercised by its tests. Its naming layer defines scoped collection names for project, topic, and caller-supplied custom collections, with namespace prefixes for project/topic scopes and verbatim names for custom scopes ((crates/gcore/src/qdrant/naming.rs:1)). It rejects empty names, reserved path-like names, whitespace-surrounded names, ASCII whitespace/control characters, and path/URL-like separators (`/`, `\`, `:`) before building collection names ((crates/gcore/src/qdrant/naming.rs:44)).

The test coverage documents the main flows around payload opacity, degradation, search, upsert, HTTP error typing, schema validation, and collection lifecycle. Payloads and filters are treated as opaque JSON maps/values rather than schema-bound structs, preserving caller-provided fields such as `symbol_id`, `wiki`, and filter clauses ((crates/gcore/src/qdrant/tests.rs:11)). The `with_qdrant` helper degrades to `ServiceState::NotConfigured` when config or URL is missing, returns `ServiceState::Available` when configured, and propagates closure errors unchanged ((crates/gcore/src/qdrant/tests.rs:32)).

Within the wider crate, this module collaborates with configuration, degradation-state reporting, JSON serialization, and HTTP test helpers. The tests import `QdrantConfig`, `ServiceState`, and HTTP harness utilities from sibling crate modules, showing that production Qdrant behavior is configured through `crate::config`, reported through `crate::degradation`, and verified through `crate::test_http` request/response helpers ((crates/gcore/src/qdrant/tests.rs:1)). Search is exercised through a CLI-style path that sends a `SearchRequest` to a configured collection with API-key support ((crates/gcore/src/qdrant/tests.rs:61)).

| Public Symbol | Kind | Responsibility |
| --- | --- | --- |
| `CollectionScope` | enum | Selects project, topic, or custom collection naming mode ((crates/gcore/src/qdrant/naming.rs:1)) |
| `CollectionNameError` | enum | Reports empty, reserved, invalid-character, or surrounding-whitespace collection names ((crates/gcore/src/qdrant/naming.rs:12)) |
| `collection_name` | function | Builds validated collection names from namespace plus scope ((crates/gcore/src/qdrant/naming.rs:24)) |
| `validate_collection_name_component` | function | Internal validator for collection-name components ((crates/gcore/src/qdrant/naming.rs:44)) |

| Configuration Field | Meaning |
| --- | --- |
| `QdrantConfig.url` | Enables Qdrant when present; missing URL degrades as not configured ([crates/gcore/src/qdrant/tests.rs:34-49](crates/gcore/src/qdrant/tests.rs:34)) |
| `QdrantConfig.api_key` | Optional API key used by configured search flow ([crates/gcore/src/qdrant/tests.rs:73-83](crates/gcore/src/qdrant/tests.rs:73)) |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/qdrant/naming.rs\|crates/gcore/src/qdrant/naming.rs]] | `crates/gcore/src/qdrant/naming.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcore/src/qdrant/tests.rs\|crates/gcore/src/qdrant/tests.rs]] | `crates/gcore/src/qdrant/tests.rs` exposes 15 indexed API symbols. |

