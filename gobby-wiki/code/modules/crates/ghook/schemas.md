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

## crates/ghook/schemas

This module is the canonical contract layer for the `ghook` binary's two primary data shapes: the structured diagnostic report emitted by `ghook --diagnose` and the inbox envelope persisted to disk when the daemon is unreachable. Both files are JSON Schema Draft-07 documents published under the `https://gobby.ai/schemas/ghook/` namespace, making them usable by any consumer — Rust, TypeScript, CI linters, or documentation tooling — that can validate against a schema URL. The schemas enforce `additionalProperties: false` on every top-level object, which means any unrecognised field causes a validation failure and prevents silent forward-compatibility drift crates/ghook/schemas/diagnose-output.v2.schema.json:9, crates/ghook/schemas/inbox-envelope.v1.schema.json:9.

The diagnose schema (`diagnose-output.v2.schema.json`) captures a snapshot of the hook installation at runtime. It was bumped to `schema_version: 2` to add the `install_method` and `install_source_url` fields, which record how and from where the `ghook` binary was fetched; v1 fields are otherwise unchanged crates/ghook/schemas/diagnose-output.v2.schema.json:4-5. The inbox-envelope schema (`inbox-envelope.v1.schema.json`) defines the structure written by `ghook` to `~/.gobby/hooks/inbox/` and subsequently drained by the daemon's replay worker; it carries the original stdin payload, routing metadata, and the HTTP headers that were sent (or would have been sent) to the daemon crates/ghook/schemas/inbox-envelope.v1.schema.json:5-6.

### diagnose-output.v2 — Required Properties

| Field | Type | Constraints | Notes |
|---|---|---|---|
| `schema_version` | integer | `const: 2` | Bumped from 1; consumers must reject other values |
| `ghook_version` | string | `minLength: 1` | Semver string of the running binary |
| `cli` | string | `minLength: 1` | Host CLI identifier |
| `hook_type` | string | `minLength: 1` | Hook name passed via `--type` |
| `critical` | boolean | — | Whether hook failure exits 2 |
| `terminal_context_enabled` | boolean | — | tmux pane capture enabled |
| `daemon_url` | string | `minLength: 1` | Full daemon base URL |
| `daemon_host` | string | `minLength: 1` | Daemon hostname component |
| `daemon_port` | integer | `1–65535` | Daemon port component |
| `cli_recognized` | boolean | — | Whether the CLI was known at hook time |

### diagnose-output.v2 — Optional Properties

| Field | Type | Notes |
|---|---|---|
| `source` | string \| null | Source CLI identifier |
| `project_root` | string \| null | Detected repo root |
| `project_id` | string \| null | Resolved project identifier |
| `terminal_context_preview` | object \| null | Sampled tmux pane data |
| `install_method` | string \| null | Conventional values: `github-release`, `crates-binstall`, `cargo-install`, `manual`, `unknown`; null when no sidecar crates/ghook/schemas/diagnose-output.v2.schema.json:68-73 |
| `install_source_url` | string \| null | GitHub release asset URL or null crates/ghook/schemas/diagnose-output.v2.schema.json:74-78 |

### inbox-envelope.v1 — Properties

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | integer (`const: 1`) | ✓ | Consumers must reject unknown versions crates/ghook/schemas/inbox-envelope.v1.schema.json:19-22 |
| `enqueued_at` | string (`date-time`) | ✓ | ISO-8601 UTC timestamp of enqueue crates/ghook/schemas/inbox-envelope.v1.schema.json:23-27 |
| `critical` | boolean | ✓ | `true` → ghook exited 2 on daemon failure crates/ghook/schemas/inbox-envelope.v1.schema.json:28-31 |
| `hook_type` | string | ✓ | e.g. `session-start`, `PreToolUse` crates/ghook/schemas/inbox-envelope.v1.schema.json:32-36 |
| `input_data` | any | ✓ | Original stdin payload; may include enriched `terminal_context` crates/ghook/schemas/inbox-envelope.v1.schema.json:37-39 |
| `source` | string | ✓ | `claude`, `codex`, `gemini`, `qwen`, `droid`, `grok` crates/ghook/schemas/inbox-envelope.v1.schema.json:40-44 |
| `headers` | object | ✓ | Mirror of HTTP headers; absent keys = omitted headers crates/ghook/schemas/inbox-envelope.v1.schema.json:45-63 |
| `headers.X-Gobby-Project-Id` | string | — | Routing header for project scope |
| `headers.X-Gobby-Session-Id` | string | — | Routing header for session scope |

Both schemas sit at the boundary between the `ghook` binary and its downstream consumers (the daemon drain worker and any tooling that parses `--diagnose` output). The `ghook` binary is the sole writer; the daemon replay worker and diagnostic tooling are the readers. Versioning is made explicit through the `schema_version` constant in each document, allowing readers to fail fast on unknown versions rather than silently misinterpret data.

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/ghook/schemas/diagnose-output.v2.schema.json\|crates/ghook/schemas/diagnose-output.v2.schema.json]] | `crates/ghook/schemas/diagnose-output.v2.schema.json` exposes 50 indexed API symbols. |
| [[code/files/crates/ghook/schemas/inbox-envelope.v1.schema.json\|crates/ghook/schemas/inbox-envelope.v1.schema.json]] | `crates/ghook/schemas/inbox-envelope.v1.schema.json` exposes 42 indexed API symbols. |

