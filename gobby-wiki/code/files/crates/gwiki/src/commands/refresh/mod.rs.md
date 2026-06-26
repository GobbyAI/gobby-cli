---
title: crates/gwiki/src/commands/refresh/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/refresh/mod.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/refresh/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Wraps 'execute_with_fetcher', passing a fetcher that refreshes each record’s URL and ingests the fetched snapshot via 'ingest::url::fetch_url_snapshot', returning a 'CommandOutcome' or 'WikiError'. [crates/gwiki/src/commands/refresh/mod.rs:29-37] |
| `execute_with_fetcher` | function | Resolves the command scope from 'selection' and delegates to 'execute_resolved_with_fetcher', forwarding 'source_ids', 'dry_run', and the provided mutable fetcher closure that maps each 'SourceRecord' and fetch timestamp string to a 'UrlSnapshot' or 'UrlIngestFailure'. [crates/gwiki/src/commands/refresh/mod.rs:39-49] |
| `execute_resolved_with_fetcher` | function | Validates the scope root, loads the source manifest, selects requested sources, returns a dry-run refresh render if requested, otherwise timestamps the refresh and iterates planned entries to refresh URL and local-file candidates while accumulating refreshed, unchanged, failed, and degradation results into a 'CommandOutcome'. [crates/gwiki/src/commands/refresh/mod.rs:51-140] |

