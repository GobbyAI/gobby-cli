---
title: crates/gcore/assets/postgres-pgsearch
type: code_module
provenance:
- file: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
- file: crates/gcore/assets/postgres-pgsearch/version.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/assets/postgres-pgsearch

Parent: [[code/modules/crates/gcore/assets|crates/gcore/assets]]

## Overview

## Module: crates/gcore/assets/postgres-pgsearch

This module is a versioned asset bundle that pins and distributes the `pg_search` PostgreSQL extension within the broader `gcore` infrastructure. Its primary artifact is `version.json`, which serves as the single source of truth for the extension release being consumed: it records the exact version string, a canonical SHA-256 digest, per-architecture digests, and the target PostgreSQL major version. Downstream tooling reads these values to fetch, verify, and install the correct extension binary without embedding version details in code.

| Property | Value (version.json:1-9) |
|---|---|
| `pg_search_version` | `0.23.4` |
| `pg_search_sha256` (canonical) | `6b042d61d156ca5fdcb1c417e291d90bffe3026848890be30bf6e578146b4676` |
| `pg_search_sha256_by_arch.amd64` | `6b042d61d156ca5fdcb1c417e291d90bffe3026848890be30bf6e578146b4676` |
| `pg_search_sha256_by_arch.arm64` | `5ad13a80b76c46590914e0c366bd8deaf807d5b352f5ad489876ec836d06d3d1` |
| `postgres_major` | `18` |

The child module `crates/gcore/assets/postgres-pgsearch/scripts` provides the operational shell logic that acts on these version values. Its exported components — `usage`, `die_usage`, and `require_value` — handle CLI argument validation and help output, while `parse_epoch`, `timestamp_epoch`, `audit_line_epoch`, and `emit_windowed_audit_lines` implement time-window utilities for parsing and emitting audit log lines during install or upgrade operations. This separation keeps static metadata (`version.json`) decoupled from procedural installation logic (`scripts/`), making version bumps a one-file change.

Collaboration in the wider system flows inward: external provisioning or CI scripts read `version.json` (version.json:2-8) to resolve the artifact URL and validate the downloaded tarball's integrity against the appropriate architecture digest before handing off to the shell scripts for actual installation steps. The dual-digest design (`pg_search_sha256` for the canonical path and `pg_search_sha256_by_arch` for `amd64`/`arm64`) allows multi-architecture build pipelines to select the correct checksum without conditional logic at the call site.
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17]
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:38-49]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/assets/postgres-pgsearch/scripts\|crates/gcore/assets/postgres-pgsearch/scripts]] | ## Module: crates/gcore/assets/postgres-pgsearch/scripts |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/assets/postgres-pgsearch/version.json\|crates/gcore/assets/postgres-pgsearch/version.json]] | `crates/gcore/assets/postgres-pgsearch/version.json` exposes 6 indexed API symbols. |

