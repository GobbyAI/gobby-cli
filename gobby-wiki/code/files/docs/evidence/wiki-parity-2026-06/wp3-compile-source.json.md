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

<details>
<summary>Relevant source files</summary>

- [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2-3](docs/evidence/wiki-parity-2026-06/wp3-compile-source.json#L2-L3)

</details>

# docs/evidence/wiki-parity-2026-06/wp3-compile-source.json

Module: [[code/modules/docs/evidence/wiki-parity-2026-06|docs/evidence/wiki-parity-2026-06]]

## Purpose

This JSON file records an I/O failure from the wiki-parity evidence pipeline. It pairs an error `code` with a human-readable `message` explaining that reading the research checkpoint failed because `research-session.json` was missing.
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:3]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | property | `"code": "io_error",` | `code [property]` | `e7ca7d38-b30f-5f4d-9c7a-5466faf22b82` | 2-2 [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2] | Indexed property `code` in `docs/evidence/wiki-parity-2026-06/wp3-compile-source.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2] |
| `message` | property | `"message": "read research checkpoint failed for /Users/josh/Projects/gobby-cli/.gobby/wiki/.gwiki/research-session.json: No such file or directory (os error 2) (io_error)"` | `message [property]` | `f53d2bd7-cb19-5344-92aa-07a560fe7b7c` | 3-3 [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:3] | Indexed property `message` in `docs/evidence/wiki-parity-2026-06/wp3-compile-source.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:3] |
