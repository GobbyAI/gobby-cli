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

This module contains a single Bash utility for exporting pgAudit records from PostgreSQL logs. `pg_audit_export.sh` scans log files, keeps only lines containing `AUDIT:`, parses each line’s leading PostgreSQL timestamp, and emits records whose epoch falls inside an inclusive `--start`/`--end` validation window . Its default log root is `/var/log/pgaudit`, with an overridable `--log-dir` implied by the usage text .

The key flow is argument validation followed by timestamp normalization and filtering. `require_value` rejects missing flag values, `parse_epoch` turns CLI timestamps into UTC epoch seconds via `timestamp_epoch`, and `audit_line_epoch` extracts timestamps from log lines before the window check   [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:62]. `timestamp_epoch` supports GNU `date -d` first, then a BSD/macOS `date -j -f` fallback after normalizing ISO `T` and trailing `Z` forms [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:48].

`emit_windowed_audit_lines` is the module’s main collaboration point with the filesystem-facing portion of the script: it accepts computed start/end epochs plus a list of log files, sorts file paths deterministically with `LC_ALL=C sort -z`, streams each file line by line, and prints matching audit records [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:75]. No cross-file relationships or child modules are supplied, so this scripts module appears self-contained within the provided input.

| CLI surface | Description | Anchor |
| --- | --- | --- |
| `pg_audit_export.sh --start <iso8601> --end <iso8601> [--log-dir <path>]` | Emits pgAudit `AUDIT:` lines within the inclusive timestamp window. |  |
| `--start <iso8601>` | Required start timestamp parsed to UTC epoch. |  |
| `--end <iso8601>` | Required end timestamp parsed to UTC epoch. |  |
| `--log-dir <path>` | Optional log directory override; default is `/var/log/pgaudit`. |  |

| Public symbol | Responsibility | Anchor |
| --- | --- | --- |
| `usage` | Prints command usage and behavior summary. |  |
| `die_usage` | Prints an error, usage, and exits with code `2`. | [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:17] |
| `require_value` | Validates that a flag has a non-flag value. |  |
| `timestamp_epoch` | Converts supported timestamp formats to UTC epoch seconds. | [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:48] |
| `audit_line_epoch` | Extracts and parses the leading timestamp from a log line. | [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:62] |
| `emit_windowed_audit_lines` | Filters sorted log files to matching `AUDIT:` lines in the epoch window. | [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:75] |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh\|crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh]] | `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh` exposes 7 indexed API symbols. |

