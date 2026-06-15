---
title: docs/evidence/wiki-parity-2026-06/wp3-compile-source.json
type: code_file
provenance:
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-source.json
  ranges:
  - 2-3
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs/evidence/wiki-parity-2026-06/wp3-compile-source.json

Module: [[code/modules/docs/evidence/wiki-parity-2026-06|docs/evidence/wiki-parity-2026-06]]

## Purpose

This JSON file captures an I/O failure record for the wiki-parity compile source: `code` identifies the error as `io_error`, and `message` explains that reading the research checkpoint failed because `research-session.json` was missing. The two fields work together to provide a machine-readable error type and a human-readable diagnostic.
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:3]

## API Symbols

- `code` (property) component `code [property]` (`e7ca7d38-b30f-5f4d-9c7a-5466faf22b82`) lines 2-2 [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
  - Signature: `"code": "io_error",`
  - Purpose: Indexed property `code` in `docs/evidence/wiki-parity-2026-06/wp3-compile-source.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
- `message` (property) component `message [property]` (`f53d2bd7-cb19-5344-92aa-07a560fe7b7c`) lines 3-3 [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:3]
  - Signature: `"message": "read research checkpoint failed for /Users/josh/Projects/gobby-cli/.gobby/wiki/.gwiki/research-session.json: No such file or directory (os error 2) (io_error)"`
  - Purpose: Indexed property `message` in `docs/evidence/wiki-parity-2026-06/wp3-compile-source.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:3]

