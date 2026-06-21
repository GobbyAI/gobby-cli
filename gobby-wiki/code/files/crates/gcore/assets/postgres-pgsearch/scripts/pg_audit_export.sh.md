---
title: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
type: code_file
provenance:
- file: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh

Module: [[code/modules/crates/gcore/assets/postgres-pgsearch/scripts|crates/gcore/assets/postgres-pgsearch/scripts]]

## Overview

`crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh` exposes 7 indexed API symbols.

## How it fits

`crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `usage` | function | The 'usage()' function prints the help documentation for pg_audit_export.sh, which filters and emits pgAudit AUDIT log lines based on PostgreSQL log timestamps falling within a specified ISO8601 time window. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17] |
| `die_usage` | function | # Summary 'die_usage()' outputs an error message and usage information to standard error, then exits the script with exit code 2. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23] |
| `require_value` | function | This function validates that a command-line flag argument is non-empty and does not start with '--', exiting with status code 2 if validation fails, otherwise echoing the argument value to stdout. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36] |
| `parse_epoch` | function | Converts a timestamp string to Unix epoch using the 'timestamp_epoch' function, outputting the epoch value to stdout or exiting with status code 2 if parsing fails. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:38-49] |
| `timestamp_epoch` | function | Converts a timestamp string to Unix epoch seconds by attempting GNU date parsing first, then falling back to BSD date parsing with ISO 8601 format normalization (replacing 'T' and 'Z' indicators). [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:51-73] |
| `audit_line_epoch` | function | Extracts an ISO 8601 timestamp (YYYY-MM-DD HH:MM:SS with optional fractional seconds) and a timezone/identifier field from an audit log line, then converts them to epoch time via the 'timestamp_epoch' function. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:75-84] |
| `emit_windowed_audit_lines` | function | # Summary Outputs all lines containing the "AUDIT:" marker from multiple sorted log files whose extracted epoch timestamps fall within a specified time window [start_epoch, end_epoch]. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:86-103] |

