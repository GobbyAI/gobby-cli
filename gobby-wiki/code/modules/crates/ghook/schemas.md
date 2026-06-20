---
title: crates/ghook/schemas
type: code_module
provenance:
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/schemas

Parent: [[code/modules/crates/ghook|crates/ghook]]

## Overview

The `crates/ghook/schemas` module defines strict JSON Schema contracts for ghook’s observable data formats. `diagnose-output.v2` describes `ghook --diagnose --cli=<c> --type=<t>` output and preserves v1 fields while adding install provenance fields; `inbox-envelope.v1` describes the envelope ghook writes into `~/.gobby/hooks/inbox/` for later daemon replay (`crates/ghook/schemas/diagnose-output.v2.schema.json:1-5`, `crates/ghook/schemas/inbox-envelope.v1.schema.json:1-5`).

The key flow is producer-to-consumer validation. ghook emits diagnostic state about CLI recognition, hook type, terminal-context support, daemon connection details, and install provenance, with required fields and no undeclared properties (`crates/ghook/schemas/diagnose-output.v2.schema.json:6-20`, `crates/ghook/schemas/diagnose-output.v2.schema.json:21-80`). For queued hook delivery, ghook writes an inbox envelope containing enqueue time, criticality, hook payload, source CLI, and daemon-style headers; the daemon drain worker replays it, and consumers are expected to reject unknown schema versions (`crates/ghook/schemas/inbox-envelope.v1.schema.json:5-17`, `crates/ghook/schemas/inbox-envelope.v1.schema.json:19-64`).

Collaboration is explicit at the schema boundary: external ghook CLI code calls into these contracts by producing matching JSON, while daemon-side drain logic consumes the inbox envelope. Both schemas import JSON Schema draft-07 through `$schema` and publish stable `$id` URLs for validators and downstream tooling (`crates/ghook/schemas/diagnose-output.v2.schema.json:2-3`, `crates/ghook/schemas/inbox-envelope.v1.schema.json:2-3`).

| Schema | Version | Purpose | Strictness |
| --- | ---: | --- | --- |
| `diagnose-output.v2.schema.json` | `2` | Diagnose output for `ghook --diagnose --cli=<c> --type=<t>` | `additionalProperties: false` (`crates/ghook/schemas/diagnose-output.v2.schema.json:4-21`) |
| `inbox-envelope.v1.schema.json` | `1` | Inbox envelope written by ghook and replayed by daemon drain worker | `additionalProperties: false` (`crates/ghook/schemas/inbox-envelope.v1.schema.json:4-18`) |

| Public Field | Schema | Notes |
| --- | --- | --- |
| `daemon_host`, `daemon_port`, `daemon_url` | Diagnose v2 | Daemon connection target; port is `1..65535` (`crates/ghook/schemas/diagnose-output.v2.schema.json:44-54`) |
| `install_method`, `install_source_url` | Diagnose v2 | Install provenance from sidecar metadata (`crates/ghook/schemas/diagnose-output.v2.schema.json:69-78`) |
| `input_data` | Inbox v1 | Original stdin payload, optionally enriched with terminal context (`crates/ghook/schemas/inbox-envelope.v1.schema.json:37-39`) |
| `headers.X-Gobby-Project-Id`, `headers.X-Gobby-Session-Id` | Inbox v1 | Optional mirrored daemon HTTP headers (`crates/ghook/schemas/inbox-envelope.v1.schema.json:48-61`) |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/ghook/schemas/diagnose-output.v2.schema.json\|crates/ghook/schemas/diagnose-output.v2.schema.json]] | `crates/ghook/schemas/diagnose-output.v2.schema.json` exposes 50 indexed API symbols. |
| [[code/files/crates/ghook/schemas/inbox-envelope.v1.schema.json\|crates/ghook/schemas/inbox-envelope.v1.schema.json]] | `crates/ghook/schemas/inbox-envelope.v1.schema.json` exposes 42 indexed API symbols. |

