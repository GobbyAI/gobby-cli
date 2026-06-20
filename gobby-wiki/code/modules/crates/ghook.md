---
title: crates/ghook
type: code_module
provenance:
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
- file: crates/ghook/src/action.rs
- file: crates/ghook/src/args.rs
- file: crates/ghook/src/cli_config.rs
- file: crates/ghook/src/detach.rs
- file: crates/ghook/src/diagnose.rs
- file: crates/ghook/src/dispatch.rs
- file: crates/ghook/src/envelope.rs
- file: crates/ghook/src/json_value.rs
- file: crates/ghook/src/main.rs
- file: crates/ghook/src/output.rs
- file: crates/ghook/src/planned_shutdown.rs
- file: crates/ghook/src/runtime.rs
- file: crates/ghook/src/source.rs
- file: crates/ghook/src/statusline.rs
- file: crates/ghook/src/terminal_context.rs
- file: crates/ghook/src/transport.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook

Parent: [[code/modules/crates|crates]]

## Overview

`crates/ghook` is Gobby’s hook-side integration layer. Its runtime child module receives host-agent hook invocations, builds a hook envelope, persists it locally, and then attempts daemon delivery; its schema child module defines the JSON contracts for both diagnostics and durable inbox envelopes (crates/ghook/src/transport.rs:1-18) (crates/ghook/schemas/diagnose-output.v2.schema.json:1) (crates/ghook/schemas/inbox-envelope.v1.schema.json:1).

The main delivery flow is durability-first: write the envelope atomically to `~/.gobby/hooks/inbox/<p>-<ts13>-<uuid>.json`, POST to the daemon, delete the inbox file only on 2xx, and rely on the daemon drain worker to replay envelopes after timeout, connection failure, or HTTP failure (crates/ghook/src/transport.rs:1-18). After daemon interaction, `action` translates success or failure responses into hook-visible stdout, stderr, and exit behavior through `HookAction`, with collaborators for CLI policy, Python-style truthiness, Stop-hook behavior, output, and transport (crates/ghook/src/action.rs:1-29).

The module collaborates outward with the Gobby daemon over HTTP and inward with durable local storage, while also maintaining stable JSON schema boundaries. The schema files publish draft-07 schemas under `https://gobby.ai/schemas/ghook/`, require explicit `schema_version` fields, and reject unknown top-level fields with `additionalProperties: false` (crates/ghook/schemas/diagnose-output.v2.schema.json:1) (crates/ghook/schemas/inbox-envelope.v1.schema.json:1).

| Contract | Purpose | Notable Rules |
| --- | --- | --- |
| `diagnose-output.v2` | Diagnostic output schema | draft-07, stable `$id`, explicit version, no unknown top-level fields |
| `inbox-envelope.v1` | Durable inbox envelope schema | draft-07, stable `$id`, explicit version, no unknown top-level fields |

| Runtime Area | Public Symbols |
| --- | --- |
| CLI/config | `Args`, `CliConfig`, `CliConfig::for_cli`, `CliConfig::for_dispatch`, `CliConfig::is_critical_hook` |
| Delivery | `Envelope`, `Envelope::new`, `DeliveryOutcome`, `DeliveryFailureKind`, `DeliveryReport`, `enqueue_to`, `post_and_cleanup` |
| Hook action | `HookAction`, `continue_action`, `emit_action`, `action_from_success_response`, `action_from_failure` |
| Diagnostics | `DiagnoseOutput`, `diagnose`, `run_diagnose` |
| Terminal context | `capture`, `enabled_for_hook`, `build_context`, `inject` |
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/terminal_context.rs:18-23]
[crates/ghook/src/action.rs:9-13]
[crates/ghook/src/args.rs:9-33]
[crates/ghook/src/diagnose.rs:15-32]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/ghook/schemas\|crates/ghook/schemas]] | `crates/ghook/schemas` defines JSON Schema contracts for ghook’s diagnostic output and durable inbox envelopes. Both schemas target JSON Schema draft-07, publish stable `$id` URLs under `https://gobby.ai/schemas/ghook/`, require explicit schema versions, and reject unknown top-level fields with `additionalProperties: false` (crates/ghook/schemas/diagnose-output.v2.schema.json:1) (crates/ghook/schemas/inbox-envelope.v1.schema.json:1). |
| [[code/modules/crates/ghook/src\|crates/ghook/src]] | `crates/ghook/src` implements the hook-side CLI/runtime for forwarding host-agent hook invocations into Gobby. Its normal path builds a hook envelope, writes it to the local inbox first, then attempts a daemon POST; `transport` documents the durability contract as atomic write to `~/.gobby/hooks/inbox/<p>-<ts13>-<uuid>.json`, deletion on 2xx, and replay by the daemon drain worker on timeout, connection failure, or HTTP failure (`crates/ghook/src/transport.rs:1-18`). `action` translates daemon responses into hook-visible stdout/stderr/exit behavior through `HookAction`, importing CLI policy,… |

