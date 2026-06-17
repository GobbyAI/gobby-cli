---
title: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
type: code_file
provenance:
- file: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
  ranges:
  - 10-17
  - 19-23
  - 25-36
  - 38-49
  - 51-73
  - 75-84
  - 86-103
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17](crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh#L10-L17), [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23](crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh#L19-L23), [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36](crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh#L25-L36), [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:38-49](crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh#L38-L49), [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:51-73](crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh#L51-L73), [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:75-84](crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh#L75-L84), [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:86-103](crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh#L86-L103)

</details>

# crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh

Module: [[code/modules/crates/gcore/assets/postgres-pgsearch/scripts|crates/gcore/assets/postgres-pgsearch/scripts]]

## Purpose

This Bash script exports PostgreSQL pgAudit `AUDIT:` log lines whose timestamps fall within an inclusive `--start`/`--end` window, with an optional `--log-dir` override. The helper functions validate CLI values, print usage errors, normalize ISO-8601 timestamps into epoch seconds with portable `date` handling, extract epochs from individual audit log lines, and then sort the discovered log files before streaming only matching lines from the requested time range.
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:38-49]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:51-73]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `usage` | function | `usage() {` | `usage [function]` | `4b31971a-4bab-564b-b9ea-cd5f03f8c5b8` | 10-17 [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17] | Indexed function `usage` in `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh`. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17] |
| `die_usage` | function | `die_usage() {` | `die_usage [function]` | `d19f1a5b-af59-5ff2-94cd-fc1675c70b58` | 19-23 [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23] | Indexed function `die_usage` in `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh`. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23] |
| `require_value` | function | `require_value() {` | `require_value [function]` | `697e4428-536b-5429-a66e-b114c7fd7f98` | 25-36 [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36] | Indexed function `require_value` in `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh`. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36] |
| `parse_epoch` | function | `parse_epoch() {` | `parse_epoch [function]` | `7a246ae0-e014-5c25-8748-e6007cf48164` | 38-49 [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:38-49] | Indexed function `parse_epoch` in `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh`. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:38-49] |
| `timestamp_epoch` | function | `timestamp_epoch() {` | `timestamp_epoch [function]` | `199d586c-e52d-5aa8-9c4e-c83adae92a4c` | 51-73 [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:51-73] | Indexed function `timestamp_epoch` in `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh`. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:51-73] |
| `audit_line_epoch` | function | `audit_line_epoch() {` | `audit_line_epoch [function]` | `27b64163-8ebd-52a7-8462-229ef16e07ce` | 75-84 [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:75-84] | Indexed function `audit_line_epoch` in `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh`. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:75-84] |
| `emit_windowed_audit_lines` | function | `emit_windowed_audit_lines() {` | `emit_windowed_audit_lines [function]` | `d531e2b3-4670-5fa5-8c6d-2f3396ed59dd` | 86-103 [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:86-103] | Indexed function `emit_windowed_audit_lines` in `crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh`. [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:86-103] |
