---
title: scripts/verify.sh
type: code_file
provenance:
- file: scripts/verify.sh
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# scripts/verify.sh

Module: [[code/modules/scripts|scripts]]

## Overview

`scripts/verify.sh` exposes 2 indexed API symbols.

## How it fits

`scripts/verify.sh` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `usage` | function | Prints a usage message to stderr describing 'scripts/verify.sh' subcommands ('build', 'unit_tests', 'doc_tests', 'format', 'lint', etc.) and notes that running with no arguments executes all checks. [scripts/verify.sh:4-10] |
| `run_check` | function | Dispatches a named workspace check target to the corresponding Cargo command ('build', 'nextest' unit tests, doc tests, formatting, or Clippy with warnings denied), prints usage for help, and exits with status 2 on unknown checks. [scripts/verify.sh:12-39] |

