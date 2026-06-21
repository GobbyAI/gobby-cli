---
title: crates/gcore/assets/postgres-pgsearch/scripts
type: code_module
provenance:
- file: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/assets/postgres-pgsearch/scripts

Parent: [[code/modules/crates/gcore/assets/postgres-pgsearch|crates/gcore/assets/postgres-pgsearch]]

## Overview

## Module: crates/gcore/assets/postgres-pgsearch/scripts

This module contains a single Bash utility, `pg_audit_export.sh`, whose sole responsibility is extracting pgAudit `AUDIT:` log lines from PostgreSQL log files that fall within a caller-supplied inclusive time window. It is deployed as a static asset alongside the `postgres-pgsearch` crate and is intended to be invoked directly from the command line or from orchestration tooling that needs time-bounded audit trail exports. No child modules exist; all logic is self-contained in one script (pg_audit_export.sh:1–100).

The script's primary flow begins with argument parsing: `--start` and `--end` flags accept ISO 8601 timestamps, validated by `require_value` (pg_audit_export.sh:26–35) and converted to Unix epochs via `parse_epoch` (pg_audit_export.sh:37–44). Timestamp-to-epoch conversion is handled by `timestamp_epoch` (pg_audit_export.sh:46–70), which attempts GNU `date -d` first and falls back to BSD `date -j -f` for macOS compatibility, normalising `T`-separator and `Z`-suffix variants along the way. Once epochs are established, `emit_windowed_audit_lines` (pg_audit_export.sh:79–100) sorts the discovered log files lexicographically (using null-delimited `sort -z` for safety), streams each file line by line, skips lines that do not contain the literal string `AUDIT:`, and prints only those whose embedded timestamp — parsed by `audit_line_epoch` (pg_audit_export.sh:72–78) — falls within `[start_epoch, end_epoch]`.

Error handling is centralised through two helpers: `die_usage` (pg_audit_export.sh:22–25) writes a message to stderr and exits with code 2, and `require_value` (pg_audit_export.sh:26–35) enforces that flag arguments are non-empty and do not accidentally start with `--`. The script runs under `set -euo pipefail` (pg_audit_export.sh:2), so any unhandled subprocess failure causes an immediate non-zero exit. The default log directory is `/var/log/pgaudit` (pg_audit_export.sh:4) but can be overridden at runtime.

### CLI Interface

| Flag | Required | Default | Description |
|---|---|---|---|
| `--start <iso8601>` | Yes | — | Inclusive window start timestamp |
| `--end <iso8601>` | Yes | — | Inclusive window end timestamp |
| `--log-dir <path>` | No | `/var/log/pgaudit` | Directory containing pgAudit log files |

### Public API Symbols

| Function | Location | Responsibility |
|---|---|---|
| `usage` | pg_audit_export.sh:9 | Prints help text to stdout |
| `die_usage` | pg_audit_export.sh:22 | Prints error + usage to stderr, exits 2 |
| `require_value` | pg_audit_export.sh:26 | Validates a flag has a non-empty, non-flag value |
| `parse_epoch` | pg_audit_export.sh:37 | Converts a timestamp string to epoch, exits 2 on failure |
| `timestamp_epoch` | pg_audit_export.sh:46 | Cross-platform ISO 8601 → Unix epoch conversion |
| `audit_line_epoch` | pg_audit_export.sh:72 | Extracts and converts the leading timestamp of a log line |
| `emit_windowed_audit_lines` | pg_audit_export.sh:79 | Filters and emits `AUDIT:` lines within the epoch window |
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:38-49]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:51-73]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh\|crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh]] | `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh` exposes 7 indexed API symbols. |

