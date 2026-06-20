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

This module packages pg_search asset metadata and supporting PostgreSQL audit-log export tooling. The version manifest pins pg_search `0.23.4`, records SHA-256 checksums, includes per-architecture hashes, and targets PostgreSQL major version `18` (`crates/gcore/assets/postgres-pgsearch/version.json:1-10`).

Its child `scripts` module provides `pg_audit_export.sh`, a Bash utility that filters PostgreSQL logs for `AUDIT:` lines, parses their leading timestamps, and emits records inside an inclusive `--start` / `--end` epoch window. The default log root is `/var/log/pgaudit`, with `--log-dir` available to override it.

Collaboration-wise, this module acts as a data-and-utility asset consumed by higher-level packaging or deployment code: callers can read `version.json` to choose the pg_search artifact and validate downloaded binaries by architecture, while operators or automation can call the audit export script to extract pgAudit records from PostgreSQL log files. No explicit cross-file caller/import relationships were supplied beyond the child script module and manifest fields.

| Key | Value |
| --- | --- |
| `pg_search_version` | `0.23.4` |
| `pg_search_sha256` | `6b042d61d156ca5fdcb1c417e291d90bffe3026848890be30bf6e578146b4676` |
| `pg_search_sha256_by_arch.amd64` | `6b042d61d156ca5fdcb1c417e291d90bffe3026848890be30bf6e578146b4676` |
| `pg_search_sha256_by_arch.arm64` | `5ad13a80b76c46590914e0c366bd8deaf807d5b352f5ad489876ec836d06d3d1` |
| `postgres_major` | `18` |

| Script Symbol | Kind |
| --- | --- |
| `usage` | function |
| `die_usage` | function |
| `require_value` | function |
| `parse_epoch` | function |
| `timestamp_epoch` | function |
| `audit_line_epoch` | function |
| `emit_windowed_audit_lines` | function |
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17]
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:38-49]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/assets/postgres-pgsearch/scripts\|crates/gcore/assets/postgres-pgsearch/scripts]] | This module contains a single Bash utility for exporting pgAudit records from PostgreSQL logs. `pg_audit_export.sh` scans log files, keeps only lines containing `AUDIT:`, parses each line’s leading PostgreSQL timestamp, and emits records whose epoch falls inside an inclusive `--start`/`--end` validation window . Its default log root is `/var/log/pgaudit`, with an overridable `--log-dir` implied by the usage text . |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/assets/postgres-pgsearch/version.json\|crates/gcore/assets/postgres-pgsearch/version.json]] | `crates/gcore/assets/postgres-pgsearch/version.json` exposes 6 indexed API symbols. |

