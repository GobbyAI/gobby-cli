---
title: crates/ghook/src
type: code_module
provenance:
- file: crates/ghook/src/cli_config.rs
  ranges:
  - 11-18
  - 20-61
  - 68-74
  - 77-80
  - 83-88
  - 91-96
  - 99-101
  - 104-108
  - 111-116
- file: crates/ghook/src/detach.rs
  ranges:
  - 23-43
- file: crates/ghook/src/diagnose.rs
  ranges:
  - 15-32
  - 42-45
  - 51-60
  - 62-70
  - 72-120
  - 128-134
  - 137-143
  - 146-152
  - 155-161
  - 163-170
  - 172-177
  - 180-192
  - 195-207
  - 210-213
  - 216-221
  - 224-246
  - 249-256
  - 259-266
- file: crates/ghook/src/envelope.rs
  ranges:
  - 24-32
  - 34-52
  - 59-70
  - 73-84
  - 87-109
  - 112-123
  - 126-140
  - 143-162
- file: crates/ghook/src/json_value.rs
  ranges:
  - 3-20
  - 28-52
- file: crates/ghook/src/main.rs
  ranges:
  - 45-49
  - 57-81
  - 83-106
  - 108-124
  - 126-289
  - 291-297
  - 299-301
  - 303-305
  - 307-335
  - 337-345
  - 347-417
  - 419-438
  - 440-500
  - 502-524
  - 526-554
  - 556-568
  - 579-582
  - 585-597
  - 600-608
  - 611-651
  - 654-675
  - 678-694
  - 697-713
  - 716-733
  - 736-754
  - 757-773
  - 776-792
  - 795-806
  - 809-815
  - 818-834
  - 837-851
  - 854-869
  - 872-885
  - 888-898
  - 901-914
  - 917-930
  - 933-965
  - 968-977
- file: crates/ghook/src/output.rs
  ranges:
  - 3-5
  - 7-9
- file: crates/ghook/src/planned_shutdown.rs
  ranges:
  - 21-27
  - 29-37
  - 39-50
  - 52-54
  - 56-62
  - 64-75
  - 77-79
  - 81-84
  - 86-113
  - 115-119
  - 121-130
  - 132-134
  - 136-142
  - 144-152
  - 154-160
  - 162-169
  - 171-176
  - 178-184
  - 195-198
  - 201-206
  - 209-219
  - 222-237
  - 240-282
  - 285-291
  - 294-304
  - 307-323
  - 326-328
  - 331-353
  - 356-366
  - 369-399
  - 402-408
- file: crates/ghook/src/source.rs
  ranges:
  - 3-14
  - 20-27
  - 29-35
  - '37'
  - 39-44
  - 46-50
  - 53-82
- file: crates/ghook/src/statusline.rs
  ranges:
  - 25-27
  - 29-35
  - 37-67
  - 69-104
  - 106-119
  - 121-168
  - 170-174
  - 177-183
  - '186'
  - 189-194
  - 197-201
  - 217-222
  - 225-229
  - 232-236
  - 239-245
  - 248-253
  - 256-283
  - 286-310
  - 313-324
  - 327-344
  - 347-371
  - 374-397
- file: crates/ghook/src/terminal_context.rs
  ranges:
  - 18-23
  - 25-32
  - 34-65
  - 71-77
  - 79-84
  - 86-102
  - 104-126
  - 128-133
  - 138-145
  - 153-158
  - 161-164
  - 167-171
  - 174-187
  - 190-198
  - 201-209
  - 212-216
  - 219-237
- file: crates/ghook/src/transport.rs
  ranges:
  - 31-36
  - 40-45
  - 49-55
  - 58-60
  - 63-65
  - 68-74
  - 77-81
  - 87-114
  - 119-125
  - 127-129
  - 137-204
  - 206-221
  - 225-232
  - 242-273
  - 286-290
  - 293-296
  - 299-305
  - 308-314
  - 317-332
  - 335-348
  - 351-404
  - 407-458
  - 461-493
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src

Parent: [[code/modules/crates/ghook|crates/ghook]]

## Overview

The `crates/ghook/src` module is the Rust implementation of `ghook`, Gobby’s sandbox-tolerant hook dispatcher. Its entry point supports normal owned hook dispatch, diagnostics, and version stamping, with the normal path enqueueing an envelope before attempting a daemon POST while preserving each host CLI’s stdout, stderr, and exit-code protocol . CLI-specific behavior is centralized in `cli_config`, which recognizes supported hosts, chooses fallback dispatch settings, and marks which hooks fail closed; `source` resolves the dispatch source, `json_value` mirrors Python-style truthiness for dispatcher semantics, and `output` provides best-effort console writes [crates/ghook/src/cli_config.rs:20-61] [crates/ghook/src/source.rs] [crates/ghook/src/json_value.rs:3-20] .

The core dispatch flow starts in `main`, parses `--gobby-owned`, `--diagnose`, `--version`, CLI name, hook type, and optional detachment flags, then routes to the appropriate execution path . Normal dispatch builds a versioned `Envelope` containing hook metadata, criticality, source, raw input JSON, ordered headers, and enqueue time, optionally enriches session-start input with terminal context, and sends it through the enqueue-first transport   . The transport writes lexicographically sortable inbox files atomically under `~/.gobby/hooks/inbox/`, posts to `/api/hooks/execute`, deletes successful deliveries, and leaves or quarantines failed/malformed envelopes so the daemon can replay them later  .

Several supporting paths keep hook behavior resilient around special cases. `diagnose` emits a schema-versioned, network-free JSON report about the current invocation, daemon context, CLI recognition, terminal-context eligibility, and install provenance sidecar metadata [crates/ghook/src/diagnose.rs:15-32] [crates/ghook/src/diagnose.rs:72-120]. `planned_shutdown` prevents intentional daemon stop or restart windows from blocking Stop hooks by detecting fresh shutdown markers, probing daemon health, and deleting queued stop envelopes only for connection or timeout races  . `statusline` is a separate Claude-only path because Claude consumes statusline stdout directly: it extracts and posts session status payloads best-effort, forwards optional downstream stdout byte-for-byte, and times out or terminates lingering downstream work without surfacing daemon transport failures as hook errors  .

## Call Diagram

```mermaid
sequenceDiagram
    participant m_00c45c9b_0377_5f2c_b12f_360c8d9afc3b as marker_accepts_fresh_allowed_intents &#91;function&#93;
    participant m_00e9dfcb_4c8a_5ce3_9fb1_8c1101e1e67b as compile_v2_schema &#91;function&#93;
    participant m_032ab45d_17a0_5053_a16d_21bf4a58cdb3 as capture &#91;function&#93;
    participant m_03ff381b_511e_56de_96af_0cb6557a25d5 as unknown_cli_marked_not_recognized &#91;function&#93;
    participant m_094be0ed_401a_5f46_9e62_a10b029f7c39 as action_from_success_response &#91;function&#93;
    participant m_0a673d02_fe70_5e9d_97c3_8401533286eb as SourceEnvGuard.new &#91;method&#93;
    participant m_0be42067_4564_5016_b8ad_82238c6b08cb as dispatch_envelope_injects_valid_tmux_pane_for_session_start &#91;function&#93;
    participant m_0d89e513_ac43_50de_a5a4_d4fdd54101ea as with_tmux_env &#91;function&#93;
    participant m_0e95b086_3657_5dd3_82a6_4b6591f5b018 as action_from_failure_returns_stderr_for_droid_transport_errors &#91;function&#93;
    participant m_1037de6b_5f5f_50b7_861d_9f1d9a9a8ffa as install_provenance_absent_when_no_sidecar &#91;function&#93;
    participant m_11ef1c20_6ac4_5c90_82fd_b8ed5c6e2dd2 as action_from_success_treats_codex_pretool_deny_as_json_block &#91;function&#93;
    participant m_122bbc33_3e69_5b6e_8aef_f4faf1b67741 as posts_statusline_payload_to_daemon_endpoint &#91;function&#93;
    participant m_14ae6661_fb9d_5b9e_95dd_ffd3a5d7a474 as droid_session_start_is_recognized_noncritical_with_terminal_context_enabled &#91;function&#93;
    participant m_18168f09_19dd_51df_a93c_0d919181cb35 as main &#91;function&#93;
    participant m_23646fad_b5d5_5ed2_aa07_56333505a4a7 as diagnose_output_for_unknown_cli_validates &#91;function&#93;
    participant m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e as build_context &#91;function&#93;
    participant m_4fa09064_905f_5260_a275_4a70fd4ea731 as extract_reason &#91;function&#93;
    participant m_528d15bd_7d26_5e92_8a1d_9898be9c4048 as action_from_droid_success &#91;function&#93;
    participant m_568e6201_8996_51fe_80e1_fd4a9426321f as is_blocked &#91;function&#93;
    participant m_6162c40d_ddf8_5812_bd34_5902c76f6b62 as assert_validates &#91;function&#93;
    participant m_8574adfe_9f39_5b74_82f7_ad71301bd635 as write_runtime_stamp &#91;function&#93;
    participant m_8ad675ee_8102_5b17_9be0_596b651dfb2d as read_install_provenance &#91;function&#93;
    participant m_97af9d03_cbf7_57d6_9a35_24425c730f05 as clear_source_env &#91;function&#93;
    participant m_a7cdbeb5_469f_58f0_9dc7_5f4cc7a9b8ea as run_diagnose &#91;function&#93;
    participant m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7 as diagnose &#91;function&#93;
    participant m_b790b565_784f_5385_819b_858e1b4a29e2 as write_marker &#91;function&#93;
    participant m_bd3daea7_e3c6_5498_87b0_2b83a2eec2af as action_from_failure &#91;function&#93;
    participant m_beb7d475_755e_535a_943d_7f52fdafdee3 as run_gobby_owned &#91;function&#93;
    participant m_dfe102a7_844a_58d7_a61a_2ddfd8af78c5 as build_dispatch_envelope &#91;function&#93;
    participant m_e54362c6_30f4_5525_be69_4cd83ede2126 as handle_with &#91;function&#93;
    m_00c45c9b_0377_5f2c_b12f_360c8d9afc3b->>m_b790b565_784f_5385_819b_858e1b4a29e2: calls
    m_032ab45d_17a0_5053_a16d_21bf4a58cdb3->>m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e: calls
    m_03ff381b_511e_56de_96af_0cb6557a25d5->>m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7: calls
    m_094be0ed_401a_5f46_9e62_a10b029f7c39->>m_4fa09064_905f_5260_a275_4a70fd4ea731: calls
    m_094be0ed_401a_5f46_9e62_a10b029f7c39->>m_528d15bd_7d26_5e92_8a1d_9898be9c4048: calls
    m_094be0ed_401a_5f46_9e62_a10b029f7c39->>m_568e6201_8996_51fe_80e1_fd4a9426321f: calls
    m_0a673d02_fe70_5e9d_97c3_8401533286eb->>m_97af9d03_cbf7_57d6_9a35_24425c730f05: calls
    m_0be42067_4564_5016_b8ad_82238c6b08cb->>m_0d89e513_ac43_50de_a5a4_d4fdd54101ea: calls
    m_0be42067_4564_5016_b8ad_82238c6b08cb->>m_dfe102a7_844a_58d7_a61a_2ddfd8af78c5: calls
    m_0e95b086_3657_5dd3_82a6_4b6591f5b018->>m_bd3daea7_e3c6_5498_87b0_2b83a2eec2af: calls
    m_1037de6b_5f5f_50b7_861d_9f1d9a9a8ffa->>m_8ad675ee_8102_5b17_9be0_596b651dfb2d: calls
    m_11ef1c20_6ac4_5c90_82fd_b8ed5c6e2dd2->>m_094be0ed_401a_5f46_9e62_a10b029f7c39: calls
    m_122bbc33_3e69_5b6e_8aef_f4faf1b67741->>m_e54362c6_30f4_5525_be69_4cd83ede2126: calls
    m_14ae6661_fb9d_5b9e_95dd_ffd3a5d7a474->>m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7: calls
    m_18168f09_19dd_51df_a93c_0d919181cb35->>m_8574adfe_9f39_5b74_82f7_ad71301bd635: calls
    m_18168f09_19dd_51df_a93c_0d919181cb35->>m_a7cdbeb5_469f_58f0_9dc7_5f4cc7a9b8ea: calls
    m_18168f09_19dd_51df_a93c_0d919181cb35->>m_beb7d475_755e_535a_943d_7f52fdafdee3: calls
    m_23646fad_b5d5_5ed2_aa07_56333505a4a7->>m_00e9dfcb_4c8a_5ce3_9fb1_8c1101e1e67b: calls
    m_23646fad_b5d5_5ed2_aa07_56333505a4a7->>m_6162c40d_ddf8_5812_bd34_5902c76f6b62: calls
    m_23646fad_b5d5_5ed2_aa07_56333505a4a7->>m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7: calls
```

## Files

- [[code/files/crates/ghook/src/cli_config.rs|crates/ghook/src/cli_config.rs]] - This file defines the compile-time `CliConfig` registry for Gobby’s hook dispatcher. It maps known CLI names to fixed per-host settings: a daemon source label, the set of hook types that must fail closed, and the malformed-JSON exit code. `for_cli` performs case-insensitive lookup for the supported CLIs, `for_dispatch` guarantees a usable config by falling back to `claude`, and `is_critical_hook` checks whether a hook should be treated as failure-critical. The tests lock in the expected CLI-specific critical-hook sets, exit codes, case-insensitive matching, and fallback behavior.
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/cli_config.rs:20-61]
[crates/ghook/src/cli_config.rs:21-52]
[crates/ghook/src/cli_config.rs:54-56]
[crates/ghook/src/cli_config.rs:58-60]
- [[code/files/crates/ghook/src/detach.rs|crates/ghook/src/detach.rs]] - Provides a small cross-platform process-detachment helper for the `ghook` crate. `detach()` uses `setsid()` on Unix to leave the controlling terminal and process group, and `FreeConsole()` on Windows to drop the current console, with both paths treated as best-effort so the caller can continue even if detachment does nothing. [crates/ghook/src/detach.rs:23-43]
- [[code/files/crates/ghook/src/diagnose.rs|crates/ghook/src/diagnose.rs]] - Builds the `ghook --diagnose` introspection output: it assembles a schema-versioned JSON report describing the current CLI/hook invocation, daemon connection details, project context, terminal-context state, CLI recognition, and install provenance for the running binary. The helper functions read optional `.ghook-install.json` sidecar metadata and locate it beside the executable, while the tests verify CLI-specific criticality/source behavior and that the output and provenance parsing conform to the v2 schema and failure-tolerant sidecar rules.
[crates/ghook/src/diagnose.rs:15-32]
[crates/ghook/src/diagnose.rs:42-45]
[crates/ghook/src/diagnose.rs:51-60]
[crates/ghook/src/diagnose.rs:62-70]
[crates/ghook/src/diagnose.rs:72-120]
- [[code/files/crates/ghook/src/envelope.rs|crates/ghook/src/envelope.rs]] - Defines the v1 inbox webhook envelope that `ghook` enqueues and the daemon later replays, with a frozen `SCHEMA_VERSION` and a serialized `Envelope` struct carrying enqueue time, critical flag, hook type, raw `input_data`, source, and ordered headers. `Envelope::new` fills in the schema version and current UTC RFC3339 timestamp, while the test helpers build sample envelopes and verify JSON serialization and Draft 7 schema conformance, including the behavior of present and absent headers.
[crates/ghook/src/envelope.rs:24-32]
[crates/ghook/src/envelope.rs:34-52]
[crates/ghook/src/envelope.rs:35-51]
[crates/ghook/src/envelope.rs:59-70]
[crates/ghook/src/envelope.rs:73-84]
- [[code/files/crates/ghook/src/json_value.rs|crates/ghook/src/json_value.rs]] - This file defines a small JSON utility for Python-style truthiness checks. `is_python_truthy` maps `serde_json::Value` to a boolean by treating `Null`, `false`, numeric zero, empty strings, empty arrays, and empty objects as false, while all other values are true. The test module verifies that behavior against the expected dispatcher semantics with representative falsy and truthy JSON values.
[crates/ghook/src/json_value.rs:3-20]
[crates/ghook/src/json_value.rs:28-52]
- [[code/files/crates/ghook/src/main.rs|crates/ghook/src/main.rs]] - `crates/ghook/src/main.rs` is the `ghook` CLI entry point for Gobby’s sandbox-tolerant hook dispatcher. It parses hook-runtime flags, routes into version, diagnose, or normal `gobby_owned` execution, writes the runtime stamp, builds dispatch envelopes with project/session and terminal context, and converts successful or failed daemon responses into `HookAction` exit codes plus stdout/stderr output, with helpers handling blocked decisions, disabled hooks, tmux environment, and related integration tests.
[crates/ghook/src/main.rs:45-49]
[crates/ghook/src/main.rs:57-81]
[crates/ghook/src/main.rs:83-106]
[crates/ghook/src/main.rs:108-124]
[crates/ghook/src/main.rs:126-289]
- [[code/files/crates/ghook/src/output.rs|crates/ghook/src/output.rs]] - Provides two tiny output helpers for the crate: `stdout` writes formatted `Arguments` to a locked standard output stream, and `stderr` does the same for standard error. Both ignore any I/O error from `write_fmt`, so the file centralizes best-effort console logging without propagating failures.
[crates/ghook/src/output.rs:3-5]
[crates/ghook/src/output.rs:7-9]
- [[code/files/crates/ghook/src/planned_shutdown.rs|crates/ghook/src/planned_shutdown.rs]] - This file implements planned shutdown handling for Gobby’s Stop hooks. It detects short-lived shutdown markers in the Gobby home directory, checks whether they are fresh and allowed, probes daemon reachability, and uses that combination to decide when a Stop hook should skip dispatch or suppress a failed post. The helper functions work together to parse and validate marker JSON, derive the freshness window from an environment override, read the current time, probe `/api/admin/health`, and delete enqueued items when suppression is warranted. The tests cover stop-hook matching, marker validation rules, daemon probing behavior, environment parsing, and the suppression/skip decision paths.
[crates/ghook/src/planned_shutdown.rs:21-27]
[crates/ghook/src/planned_shutdown.rs:29-37]
[crates/ghook/src/planned_shutdown.rs:39-50]
[crates/ghook/src/planned_shutdown.rs:52-54]
[crates/ghook/src/planned_shutdown.rs:56-62]
- [[code/files/crates/ghook/src/source.rs|crates/ghook/src/source.rs]] - This file resolves the active source name for ghook dispatch. `detect_source` returns the configured source by default, but for `claude` it can be overridden by a non-empty `GOBBY_SOURCE` environment variable; `CLAUDE_CODE_ENTRYPOINT` is intentionally ignored here.

The rest of the file is test support for that behavior. `clear_source_env` and `set_source_env` manage the process-wide variables safely within tests, and `SourceEnvGuard` resets them on creation and drop so `detect_source_respects_override_only_for_claude` can verify override handling and the rule that only `GOBBY_SOURCE` changes the detected source.
[crates/ghook/src/source.rs:3-14]
[crates/ghook/src/source.rs:20-27]
[crates/ghook/src/source.rs:29-35]
[crates/ghook/src/source.rs:37]
[crates/ghook/src/source.rs:39-44]
- [[code/files/crates/ghook/src/statusline.rs|crates/ghook/src/statusline.rs]] - Claude Code statusline hook handler that reads JSON from stdin, extracts a statusline payload when the input looks like a valid session event, and best-effort posts it to the daemon’s `/api/sessions/statusline` endpoint without surfacing transport failures as hook errors. It also optionally runs a downstream command and mirrors its stdout back to Claude exactly, with timeout and process-group termination helpers to keep the pipeline responsive and to clean up surviving child processes; the tests cover hook recognition, payload extraction, daemon posting, stdout passthrough, and timeout/kill behavior.
[crates/ghook/src/statusline.rs:25-27]
[crates/ghook/src/statusline.rs:29-35]
[crates/ghook/src/statusline.rs:37-67]
[crates/ghook/src/statusline.rs:69-104]
[crates/ghook/src/statusline.rs:106-119]
- [[code/files/crates/ghook/src/terminal_context.rs|crates/ghook/src/terminal_context.rs]] - Builds and injects a terminal/process context payload for session-start hooks so the daemon can reconcile spawned terminal agents with their environment. `capture()` gathers `TMUX` and `TMUX_PANE` from the process environment and delegates to `build_context()`, while `enabled_for_hook()` gates the logic to `sessionstart` hook names after normalizing case and separators. `build_context()` assembles a JSON object with safe process, terminal, tmux, and `GOBBY_*` metadata, only filling tmux fields when `TMUX` is present and the pane matches the daemon’s `%<digits>` contract. The helper functions handle environment lookup, parent PID and TTY discovery, tmux pane validation, and tmux socket-path parsing, and `inject()` adds the resulting `terminal_context` to a JSON object only when it is missing.
[crates/ghook/src/terminal_context.rs:18-23]
[crates/ghook/src/terminal_context.rs:25-32]
[crates/ghook/src/terminal_context.rs:34-65]
[crates/ghook/src/terminal_context.rs:71-77]
[crates/ghook/src/terminal_context.rs:79-84]
- [[code/files/crates/ghook/src/transport.rs|crates/ghook/src/transport.rs]] - Implements the enqueue-first transport for `ghook --gobby-owned`: it names inbox envelopes with lexicographically sortable `prefix-ts13-uuid.json` filenames, writes them atomically into `~/.gobby/hooks/inbox/`, posts them to the daemon, and either deletes the inbox file on a 2xx response or leaves/quarantines it for later drain replay on failure. `DeliveryOutcome`, `DeliveryFailureKind`, and `DeliveryReport` model the result of the live POST so callers can distinguish successful delivery from queued replay and classify HTTP, connection, timeout, or other transport failures. The helper functions derive inbox/quarantine paths, generate timestamps and filenames, perform atomic writes, enqueue envelopes, extract envelope IDs from paths, classify transport errors, and move malformed envelopes into quarantine; the tests verify filename format, atomic write behavior, enqueue/quarantine writes, and that `post_and_cleanup` captures success bodies, error bodies, and special endpoint behavior.
[crates/ghook/src/transport.rs:31-36]
[crates/ghook/src/transport.rs:40-45]
[crates/ghook/src/transport.rs:49-55]
[crates/ghook/src/transport.rs:58-60]
[crates/ghook/src/transport.rs:63-65]

## Components

- `dfe7d451-73f4-539e-9b59-32c8c9291990`
- `8ee0a776-cf79-5255-b0fd-2f7f365b159d`
- `c38c936b-fd31-5b98-9447-8cbc0e7c09af`
- `3c9c2a2b-aa89-5b2d-ab2e-bca9790720db`
- `f811c999-8711-59d2-8518-96c9feb5c664`
- `f40c9f23-98da-522f-8c45-ca809b03e638`
- `943c844b-abc9-5669-93e6-7a2ccd3c947a`
- `1c881534-3659-5877-b67f-17bb4ac95d39`
- `4f9d118c-758a-5611-9b5e-6736994333ce`
- `c23e955a-627c-536c-a068-42631db416c2`
- `f8ca49f8-6f88-5ec9-8719-55a412bf2ebc`
- `bc5df029-37ae-5c56-a2c3-f5e9984de2d9`
- `ad9a59f4-3cd2-52d5-8dc9-1447563bcc66`
- `ea8d006f-58de-5e56-9585-3e3626837766`
- `066e347c-e0f8-580e-859e-f0d06f843f57`
- `8ad675ee-8102-5b17-9be0-596b651dfb2d`
- `fc376df5-19c5-581d-b3d2-f09e12350b71`
- `a992c00e-a5b1-52d1-95fe-4a2da82f0ca7`
- `03ff381b-511e-56de-96af-0cb6557a25d5`
- `eccb2c13-3f5c-5c7c-a63e-4c670079d299`
- `2ab1c8cb-1a26-526b-97e2-c3ced80e7439`
- `14ae6661-fb9d-5b9e-95dd-ffd3a5d7a474`
- `00e9dfcb-4c8a-5ce3-9fb1-8c1101e1e67b`
- `6162c40d-ddf8-5812-bd34-5902c76f6b62`
- `a10ccd0d-dda9-53a5-b2a8-1c6acc8d7481`
- `23646fad-b5d5-5ed2-aa07-56333505a4a7`
- `b48a5f81-4b1e-50c4-a3c6-bd5a56e6adaf`
- `1037de6b-5f5f-50b7-861d-9f1d9a9a8ffa`
- `e7a32469-b625-5e77-a884-390c699de709`
- `68f07533-2835-53d4-ae83-6b840dffd509`
- `99ed98ac-6741-5da6-b9d6-23c91e3b0c19`
- `134b0274-548a-57f1-a2ae-2e1ade34d42b`
- `a20c2033-1b4a-5cbf-a028-ad84070bc7c9`
- `e9dd6b5a-9f95-533d-9247-b9d353b78915`
- `fba1baf1-58c9-5e8e-bea3-2f6922eb5a59`
- `69839c0d-7b5b-53c8-b485-7e62790725d5`
- `e08d73f1-796c-53fe-8bf3-1d8ace9895f5`
- `b5f5f2dd-0b5a-5f09-8e6f-39d40a4f98fc`
- `829b6804-81c4-5be6-b434-5246a5915eac`
- `2361477e-62f9-5d3e-bb73-98b600aea6fa`
- `5d14c0ef-39c5-5653-9867-265c50d0ac2b`
- `ff170581-95ff-5889-acf6-7e3482709df8`
- `b7deea92-b69e-59db-b0f9-aa74c3168cf2`
- `6aae9f18-b7ef-5eef-b421-a457b7ea5592`
- `18168f09-19dd-51df-a93c-0d919181cb35`
- `a7cdbeb5-469f-58f0-9dc7-5f4cc7a9b8ea`
- `beb7d475-755e-535a-943d-7f52fdafdee3`
- `2d8783f2-188c-535b-baf8-4e63d7a73614`
- `b5520f3a-fb3a-5d17-9567-35b8f83eec78`
- `40e9878e-caeb-5d05-a21a-48bc8e156a0c`
- `dfe102a7-844a-58d7-a61a-2ddfd8af78c5`
- `d8b40289-d659-593d-bd9c-72f619ffc3bb`
- `094be0ed-401a-5f46-9e62-a10b029f7c39`
- `528d15bd-7d26-5e92-8a1d-9898be9c4048`
- `bd3daea7-e3c6-5498-87b0-2b83a2eec2af`
- `568e6201-8996-51fe-80e1-fd4a9426321f`
- `4fa09064-905f-5260-a275-4a70fd4ea731`
- `8574adfe-9f39-5b74-82f7-ad71301bd635`
- `0d89e513-ac43-50de-a5a4-d4fdd54101ea`
- `0be42067-4564-5016-b8ad-82238c6b08cb`
- `23d1368a-e0f1-511f-8973-6a04cbe0fc05`
- `c1b47df2-70e8-5f71-ad8e-80786ead4fc9`
- `ac6569ae-6f86-5e82-8370-849fe970183a`
- `11ef1c20-6ac4-5c90-82fd-b8ed5c6e2dd2`
- `e18a39e3-96c8-54b4-a254-e8f9746a3826`
- `c1f2a53d-2ed2-519d-8ee3-ed1b31b2e341`
- `cca571b4-04b3-5e30-8816-4128d1e7af44`
- `61ca3292-9088-5897-966a-8615c61d1415`
- `5edf6eae-00a3-51fb-a7b9-5a3c805ba829`
- `30a4cf12-d637-5607-8d0a-9d8520bc3b95`
- `cc9082e3-997d-5d3a-b1f6-7edcc3da3471`
- `39462197-82e3-502a-802a-f1a5f1a173b5`
- `e783c0c2-0253-555f-a8b2-a868f36fd9a7`
- `a31fb368-b0a5-5c99-9e21-f286d81af118`
- `804d5e24-a7e0-52b8-b29c-8c4618af6521`
- `b51d61f6-7bcb-5340-ab70-87c7ea88bc96`
- `9a5f8dc2-b6f0-57bd-ab50-2d67d3fa5a14`
- `0e95b086-3657-5dd3-82a6-4b6591f5b018`
- `bf61da7f-1260-5c67-9825-5f6ac4fa364f`
- `cbd0ca63-2a53-549c-8040-49c22eb9e129`
- `677ea6dd-6742-544e-9bff-64bd94b6a6b1`
- `0a198369-26e3-55ef-a139-d04ae0c5fa76`
- `e42c0c01-e1ab-56b4-87ca-42cd184ae834`
- `480a97fa-f382-56de-81d6-231456e02757`
- `915605ab-403f-5ea7-919f-0d8b79d6bfdc`
- `8ede0f52-e4f0-5d0b-b223-36bd5ea11bb2`
- `f74d3a29-061a-5f08-a9ba-0d9e26b44077`
- `85b48489-0263-565e-bf19-5a18845e3c2d`
- `fd6c5466-4319-59b8-b435-fd161c8b2405`
- `ccb6214b-2a4e-5530-8a2b-9302a356ea6f`
- `b3c3b5d5-6d52-5c9e-91f7-aa4dfaa3b406`
- `05688997-63c0-5bf0-9083-978328be448d`
- `7a9b0033-3751-5d7e-9d9e-5665b2b2f174`
- `fea7a275-648e-59e3-a686-39b888fc347c`
- `933ab78d-939e-52d0-983c-8e96010de45e`
- `fbf08e40-b0bd-5487-8b9d-5305c01947b5`
- `76bb012b-1464-5bec-b7e2-edf391fe3245`
- `aa1adcdc-a165-5be2-9dbb-a77535328a6a`
- `4c480cc4-6019-53b3-94ee-887000152de5`
- `34768c55-e686-5b08-adf7-aff1710edf15`
- `b790b565-784f-5385-819b-858e1b4a29e2`
- `d476cae5-ff6f-533a-89f8-0243ac580704`
- `00c45c9b-0377-5f2c-b12f-360c8d9afc3b`
- `d1dd9125-6864-56f1-8c1e-591cbfa00739`
- `802d8af0-fd5f-5b8d-bf55-0390ca79e58a`
- `ed9a3e23-bd1a-5304-a8c2-6f0f950b52b2`
- `b577a8e8-f1b6-529d-8a11-72c75c04442b`
- `2ae06111-955d-5553-ae00-03de7532c146`
- `3e883e54-ca3d-5068-a0b0-6f68e377453f`
- `f43f8514-eb6e-5720-bc7d-240d40a86ae2`
- `a6e7ff0c-3d6c-5139-9be1-d9e3b7673cdc`
- `c17e17be-8228-5d89-99cf-f00b69e83031`
- `3f702f5f-5ce6-5a7b-b47b-8ed9c339a049`
- `32182b88-ac1b-5a85-8084-efc7eee1e0c3`
- `97af9d03-cbf7-57d6-9a35-24425c730f05`
- `7dd4ad00-7abe-5ed9-b923-e7646a56aca6`
- `8cc10a88-b936-5ef0-a760-b71a29f4875b`
- `e8eeea64-a990-57d2-85f5-0f49fd22ed66`
- `0a673d02-fe70-5e9d-97c3-8401533286eb`
- `9fe91193-cc60-5991-8139-693d88119cc8`
- `a19d35be-177c-59aa-aebe-fb5e0bccc023`
- `9e829fba-d764-5165-bdfa-83cff325db90`
- `98676496-c1ef-5e62-abc3-2f6fc510fe89`
- `4e51d57c-e47d-5e20-9b1a-797318e05011`
- `e54362c6-30f4-5525-be69-4cd83ede2126`
- `1882ec9f-4e36-53f4-8a85-0c963aecb5d2`
- `64d25050-ccb7-542a-b7ed-11466794a09d`
- `e9041adc-57e0-5c61-abfa-09da545cfb15`
- `a7f90096-675f-571f-aa5d-17a83ae432b4`
- `c351cb94-5e68-5bd1-a037-d29a05326bb1`
- `e15fa213-5637-5db1-ac26-36f0a4297e0e`
- `6d0eb7ae-9c75-53bc-a774-7f796ccc373d`
- `87a58021-b993-5d39-a0e8-807db949e60c`
- `d16adccf-b71e-51da-97ab-a58600962b23`
- `9dba13dd-a22d-57dd-b8a5-3170edbc2eba`
- `db5c0de8-9839-514c-a360-ff8080d86db9`
- `56fd7a3f-2596-5a55-8c97-fe480a524e27`
- `f97e1ca5-361f-52f8-ae46-40bd7f64464d`
- `122bbc33-3e69-5b6e-8aef-f4faf1b67741`
- `271dfe9e-f471-5360-abc1-ec4df58efec4`
- `35e38e77-8f95-5c4a-8954-a88f78b669b9`
- `d26f134a-9fb4-5e18-b6c6-c8879a1dd32e`
- `895005c4-92ea-51d5-bf58-1e4ed0df9f23`
- `c510a3d0-3fd9-5ee1-8a95-e2b3c4523b86`
- `032ab45d-17a0-5053-a16d-21bf4a58cdb3`
- `4be0ac35-4a63-5eaf-9eb8-f26f60ede61d`
- `2e89661f-cc0d-5e6c-a0a0-8d2b5c0a111e`
- `d242772e-aa15-5f25-88e4-a6d95061eebd`
- `fb84c468-93b9-5ab0-8408-49a199163341`
- `9a03c200-a64a-5b13-8149-3aad1b137c89`
- `70194d1e-f9d9-5d3f-a7f0-91efdfaf18a8`
- `ba1c1670-6c09-5a0f-9888-a0b28c8418bb`
- `0897e27e-b9c0-58f8-8cfd-fe2c0131f65a`
- `d065c630-b5fd-56ab-81b2-6976a000ef19`
- `50b499f0-980b-5ef0-b787-91b728960634`
- `33abafd6-98c6-5317-a520-c2a754c02cb9`
- `7c984ae4-de71-5f3b-89a9-07defc4ae74a`
- `4447068e-b3cc-512a-88ff-2405163f28d6`
- `f629e177-1cde-5057-b69c-4f3032b9864a`
- `8d707487-2178-5ece-8d22-7bd6cd8e886f`
- `c8c3ae50-4e71-5ac5-b79c-8f3f4caa9b4b`
- `e7612d20-b3e0-50e1-a2b4-6e0c0d469eeb`
- `635a2244-471a-578e-9431-93796af5a5e6`
- `fa9467a0-9921-538e-9ec3-9369b2376355`
- `337d52ed-6f16-5d5e-94ad-35a16cc183d4`
- `93cab374-71c7-5c68-b724-03dd57695d10`
- `14549333-a1e5-5a38-976d-6535683526f7`
- `f8be23e4-18cd-503a-8b93-098037bc2130`
- `eaac2601-001e-5287-8c77-829087ecf84b`
- `6b11eb8c-bf8a-56d0-9e90-68449253a47a`
- `4d3ecd62-3b6c-5674-ae84-3d766ad79d69`
- `e58a7860-6a72-5954-a5c8-645a64bc7581`
- `36a2f566-753b-51b7-bb72-507b303b984a`
- `8ccef319-bc5e-5ef7-bd04-a2d1e5b39563`
- `3f58ad50-ce04-5837-8138-d0c2fadd711a`
- `3bbefc82-9169-5a99-878b-abfaec512d8a`
- `6e376850-c377-5833-bbc5-e3762b9e6922`
- `95ba8874-a2df-5675-8004-9ade63a041ff`
- `f513006f-b922-5b80-a39e-51e07d4a26b8`
- `450dc9d4-6e70-57cd-b566-b7e4d5ac9030`
- `4adfa98a-3583-511e-90ce-99668ccedfc8`
- `ff6541be-441d-5821-a3bf-1ebf8f60f50d`
- `50a4ebc4-a089-5f1d-9955-f2da9deda388`
- `a1fa1f5d-8e49-5552-b64d-3aa8a5efb504`

