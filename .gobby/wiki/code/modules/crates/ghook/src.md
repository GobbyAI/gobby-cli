---
title: crates/ghook/src
type: code_module
provenance:
- file: crates/ghook/src/action.rs
  ranges:
  - 8-12
  - 14-20
  - 22-24
  - 26-34
  - 36-106
  - 108-127
  - 129-189
  - 191-213
  - 215-243
  - 252-273
  - 276-292
  - 295-311
  - 314-331
  - 334-352
  - 355-371
  - 374-390
  - 393-404
  - 407-413
  - 416-432
  - 435-449
  - 452-467
  - 470-483
  - 486-496
  - 499-512
  - 515-528
  - 531-540
- file: crates/ghook/src/args.rs
  ranges:
  - 9-33
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
  - 23-44
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
- file: crates/ghook/src/dispatch.rs
  ranges:
  - 16-179
  - 181-183
  - 185-213
  - 223-226
  - 229-241
  - 244-252
  - 255-295
  - 298-330
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
  - 40-63
  - 65-81
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
- file: crates/ghook/src/runtime.rs
  ranges:
  - 4-16
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

The `ghook` module is the CLI-side hook bridge for Gobby: it parses invocation mode, recognizes host CLIs, diagnoses what a hook would do, and dispatches owned hook calls into a durable daemon-facing envelope. `main` routes parsed arguments to version stamping, diagnostics, or owned execution, with validation failures returning usage-style exit code 2; `Args` supplies the mode, CLI name, hook type, diagnostics, runtime stamp, and optional detachment settings that drive those paths. [crates/ghook/src/main.rs:40-63] [crates/ghook/src/main.rs:65-81] [crates/ghook/src/args.rs:9-33] Host-specific behavior is centralized in `CliConfig`, which maps CLI names to canonical sources, critical hooks, and malformed-JSON exit codes, while `source` adds Claude-only source overrides and `detach` offers best-effort process/session detachment without affecting control flow. [crates/ghook/src/cli_config.rs:11-18] [crates/ghook/src/cli_config.rs:20-61] [crates/ghook/src/source.rs:3-14] [crates/ghook/src/detach.rs:23-44]

The normal dispatch flow is enqueue-first. `run_gobby_owned` validates the CLI and hook type, honors disabled-hooks and planned-shutdown gates, handles Claude statusline as a separate path, then gathers stdin and project context to build an `Envelope`. [crates/ghook/src/dispatch.rs:16-179] [crates/ghook/src/envelope.rs:24-32] `build_dispatch_envelope` enriches the envelope with headers and terminal/session context when available, using `terminal_context` only for session-start hooks and preserving existing terminal context in the input. [crates/ghook/src/dispatch.rs:185-213] [crates/ghook/src/terminal_context.rs:18-23] [crates/ghook/src/terminal_context.rs:25-32] [crates/ghook/src/terminal_context.rs:34-65] Transport then writes the envelope atomically to `~/.gobby/hooks/inbox`, posts it to `/api/hooks/execute`, deletes it only after a 2xx response, and otherwise leaves it for replay; malformed stdin can be quarantined with payload and metadata.  [crates/ghook/src/transport.rs:31-36] [crates/ghook/src/transport.rs:40-45] 

Result handling is split between live daemon responses and host-facing hook behavior. `action` converts successful daemon JSON and transport failures into `HookAction` values, using source-specific handling for Claude, Droid, blocked decisions, critical hooks, stderr, JSON stdout, and exit codes.  [crates/ghook/src/action.rs:36-100] Planned shutdown handling narrows suppression to `Stop` hooks during fresh shutdown markers when the daemon is unreachable, including post-enqueue suppression for connect and timeout races.   The diagnostic, runtime, statusline, JSON truthiness, and output helpers round out the module: diagnostics emit schema-shaped introspection without network I/O, runtime stamping records schema and ghook version, statusline best-effort posts session payloads while preserving downstream stdout and success exits, `json_value` mirrors dispatcher truthiness, and `output` provides fire-and-forget stdout/stderr writes. [crates/ghook/src/diagnose.rs:15-32] [crates/ghook/src/diagnose.rs:72-120] [crates/ghook/src/runtime.rs:4-16]   [crates/ghook/src/json_value.rs:3-20]

## Call Diagram

```mermaid
sequenceDiagram
    participant m_00c45c9b_0377_5f2c_b12f_360c8d9afc3b as marker_accepts_fresh_allowed_intents &#91;function&#93;
    participant m_00e9dfcb_4c8a_5ce3_9fb1_8c1101e1e67b as compile_v2_schema &#91;function&#93;
    participant m_01ba2b47_3993_5e79_a5c4_b1d9417b1295 as action_from_success_claude_stop_with_permission_deny_no_exit_two &#91;function&#93;
    participant m_032ab45d_17a0_5053_a16d_21bf4a58cdb3 as capture &#91;function&#93;
    participant m_03ff381b_511e_56de_96af_0cb6557a25d5 as unknown_cli_marked_not_recognized &#91;function&#93;
    participant m_0897e27e_b9c0_58f8_8cfd_fe2c0131f65a as parse_tmux_socket_path &#91;function&#93;
    participant m_0a673d02_fe70_5e9d_97c3_8401533286eb as SourceEnvGuard.new &#91;method&#93;
    participant m_0ebbc49b_d873_572f_b040_a9df9661de4d as action_from_failure_blocks_critical_hooks &#91;function&#93;
    participant m_1037de6b_5f5f_50b7_861d_9f1d9a9a8ffa as install_provenance_absent_when_no_sidecar &#91;function&#93;
    participant m_122bbc33_3e69_5b6e_8aef_f4faf1b67741 as posts_statusline_payload_to_daemon_endpoint &#91;function&#93;
    participant m_14ae6661_fb9d_5b9e_95dd_ffd3a5d7a474 as droid_session_start_is_recognized_noncritical_with_terminal_context_enabled &#91;function&#93;
    participant m_23646fad_b5d5_5ed2_aa07_56333505a4a7 as diagnose_output_for_unknown_cli_validates &#91;function&#93;
    participant m_271dfe9e_f471_5360_abc1_ec4df58efec4 as statusline_post_honors_gobby_daemon_url_override &#91;function&#93;
    participant m_2ab1c8cb_1a26_526b_97e2_c3ced80e7439 as codex_pre_tool_use_noncritical_without_terminal_context &#91;function&#93;
    participant m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e as build_context &#91;function&#93;
    participant m_2f2bbcab_d802_53cd_a5ff_3df416ab975e as dispatch_envelope_omits_terminal_context_for_tool_hooks &#91;function&#93;
    participant m_4e51d57c_e47d_5e20_9b1a_797318e05011 as handle &#91;function&#93;
    participant m_6162c40d_ddf8_5812_bd34_5902c76f6b62 as assert_validates &#91;function&#93;
    participant m_70194d1e_f9d9_5d3f_a7f0_91efdfaf18a8 as tty_name_or_null &#91;function&#93;
    participant m_7943af65_4575_5a6f_9788_0a7d2baa60b5 as action_from_success_response &#91;function&#93;
    participant m_8ad675ee_8102_5b17_9be0_596b651dfb2d as read_install_provenance &#91;function&#93;
    participant m_97af9d03_cbf7_57d6_9a35_24425c730f05 as clear_source_env &#91;function&#93;
    participant m_9a03c200_a64a_5b13_8149_3aad1b137c89 as parent_pid_or_null &#91;function&#93;
    participant m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7 as diagnose &#91;function&#93;
    participant m_b790b565_784f_5385_819b_858e1b4a29e2 as write_marker &#91;function&#93;
    participant m_ba1c1670_6c09_5a0f_9888_a0b28c8418bb as is_valid_tmux_pane &#91;function&#93;
    participant m_cedf4a3a_8ca0_5584_98f4_a65a36cf6613 as build_dispatch_envelope &#91;function&#93;
    participant m_e54362c6_30f4_5525_be69_4cd83ede2126 as handle_with &#91;function&#93;
    participant m_f3e134e5_9f40_5b9e_80cc_5c148e09d975 as action_from_failure &#91;function&#93;
    participant m_fb84c468_93b9_5ab0_8408_49a199163341 as env_or_null &#91;function&#93;
    m_00c45c9b_0377_5f2c_b12f_360c8d9afc3b->>m_b790b565_784f_5385_819b_858e1b4a29e2: calls
    m_01ba2b47_3993_5e79_a5c4_b1d9417b1295->>m_7943af65_4575_5a6f_9788_0a7d2baa60b5: calls
    m_032ab45d_17a0_5053_a16d_21bf4a58cdb3->>m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e: calls
    m_03ff381b_511e_56de_96af_0cb6557a25d5->>m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7: calls
    m_0a673d02_fe70_5e9d_97c3_8401533286eb->>m_97af9d03_cbf7_57d6_9a35_24425c730f05: calls
    m_0ebbc49b_d873_572f_b040_a9df9661de4d->>m_f3e134e5_9f40_5b9e_80cc_5c148e09d975: calls
    m_1037de6b_5f5f_50b7_861d_9f1d9a9a8ffa->>m_8ad675ee_8102_5b17_9be0_596b651dfb2d: calls
    m_122bbc33_3e69_5b6e_8aef_f4faf1b67741->>m_e54362c6_30f4_5525_be69_4cd83ede2126: calls
    m_14ae6661_fb9d_5b9e_95dd_ffd3a5d7a474->>m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7: calls
    m_23646fad_b5d5_5ed2_aa07_56333505a4a7->>m_00e9dfcb_4c8a_5ce3_9fb1_8c1101e1e67b: calls
    m_23646fad_b5d5_5ed2_aa07_56333505a4a7->>m_6162c40d_ddf8_5812_bd34_5902c76f6b62: calls
    m_23646fad_b5d5_5ed2_aa07_56333505a4a7->>m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7: calls
    m_271dfe9e_f471_5360_abc1_ec4df58efec4->>m_4e51d57c_e47d_5e20_9b1a_797318e05011: calls
    m_2ab1c8cb_1a26_526b_97e2_c3ced80e7439->>m_a992c00e_a5b1_52d1_95fe_4a2da82f0ca7: calls
    m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e->>m_0897e27e_b9c0_58f8_8cfd_fe2c0131f65a: calls
    m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e->>m_70194d1e_f9d9_5d3f_a7f0_91efdfaf18a8: calls
    m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e->>m_9a03c200_a64a_5b13_8149_3aad1b137c89: calls
    m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e->>m_ba1c1670_6c09_5a0f_9888_a0b28c8418bb: calls
    m_2e89661f_cc0d_5e6c_a0a0_8d2b5c0a111e->>m_fb84c468_93b9_5ab0_8408_49a199163341: calls
    m_2f2bbcab_d802_53cd_a5ff_3df416ab975e->>m_cedf4a3a_8ca0_5584_98f4_a65a36cf6613: calls
```

## Files

- [[code/files/crates/ghook/src/action.rs|crates/ghook/src/action.rs]] - Defines the hook-action layer for `ghook`: a small crate-visible `HookAction` record carries an exit code plus optional JSON stdout and stderr text, and helper functions build, emit, and translate hook outcomes into that form. Successful responses are trimmed, parsed as JSON, and mapped differently for `droid`, `claude`, and other sources, with special handling for blocked/denied payloads and extracted reasons; delivery failures are converted into fail-safe actions based on source, hook criticality, and failure kind. The rest of the file is a focused test suite that checks these mappings preserve the expected JSON fields, stderr messages, and exit codes.
[crates/ghook/src/action.rs:8-12]
[crates/ghook/src/action.rs:14-20]
[crates/ghook/src/action.rs:22-24]
[crates/ghook/src/action.rs:26-34]
[crates/ghook/src/action.rs:36-106]
- [[code/files/crates/ghook/src/args.rs|crates/ghook/src/args.rs]] - Defines the `ghook` CLI argument type used to configure hook dispatch behavior. `Args` is a `clap::Parser` struct for the crate-visible entrypoint, collecting flags for owned invocation mode, diagnostic output, version stamping, host CLI name, hook type, and optional process-group detachment. These fields work together to steer whether the hook runs normally, emits diagnostics, records a runtime version stamp, and how it identifies the calling CLI and hook kind before posting. [crates/ghook/src/args.rs:9-33]
- [[code/files/crates/ghook/src/cli_config.rs|crates/ghook/src/cli_config.rs]] - `cli_config.rs` defines a compile-time `CliConfig` registry for supported host CLIs, mapping each known CLI name to a source identifier, a set of fail-closed critical hooks, and the malformed-JSON exit code expected by the dispatcher. `CliConfig::for_cli` does the case-insensitive lookup and returns `None` for unknown CLIs, `for_dispatch` applies a Claude fallback when dispatch needs a guaranteed config, and `is_critical_hook` checks whether a hook should block on failure. The tests lock in the per-CLI mappings, case-insensitive matching, unknown-CLI behavior, and the Claude fallback path.
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/cli_config.rs:20-61]
[crates/ghook/src/cli_config.rs:21-52]
[crates/ghook/src/cli_config.rs:54-56]
[crates/ghook/src/cli_config.rs:58-60]
- [[code/files/crates/ghook/src/detach.rs|crates/ghook/src/detach.rs]] - Provides a small cross-platform helper for detaching the current process from its controlling terminal or console. On Unix, `detach()` calls `setsid()` to start a new session and leave the parent process group; on Windows, it calls `FreeConsole()` as a best-effort way to drop console attachment. The function is intentionally lightweight and non-fatal: failures are ignored so callers can request detachment without changing control flow. [crates/ghook/src/detach.rs:23-44]
- [[code/files/crates/ghook/src/diagnose.rs|crates/ghook/src/diagnose.rs]] - Implements `ghook --diagnose`, a pure introspection command that emits a JSON report describing what a Git hook invocation would do, without network I/O or envelope writes. `DiagnoseOutput` defines the schema-shaped payload, `read_install_provenance` and `install_provenance_for_running_binary` load optional installer sidecar metadata, and `diagnose` combines CLI config, daemon/project context, hook criticality, terminal context, and install provenance into the final result. The tests exercise CLI recognition, criticality, provenance fallback behavior, and validation against the v2 JSON schema.
[crates/ghook/src/diagnose.rs:15-32]
[crates/ghook/src/diagnose.rs:42-45]
[crates/ghook/src/diagnose.rs:51-60]
[crates/ghook/src/diagnose.rs:62-70]
[crates/ghook/src/diagnose.rs:72-120]
- [[code/files/crates/ghook/src/dispatch.rs|crates/ghook/src/dispatch.rs]] - This file implements the owned gobby hook dispatch path: `run_gobby_owned` validates the CLI and hook type, handles special cases first (`GOBBY_HOOKS_DISABLED`, planned shutdown, and statusline hooks), then gathers project context and stdin so the hook can be dispatched safely. `build_dispatch_envelope` assembles the JSON envelope for that dispatch, enriching it with terminal context and project/session headers when available, while `with_tmux_env` provides a controlled way for tests to simulate tmux state. The tests verify the environment gate and the envelope’s tmux/terminal-context behavior across valid, missing, and malformed inputs.
[crates/ghook/src/dispatch.rs:16-179]
[crates/ghook/src/dispatch.rs:181-183]
[crates/ghook/src/dispatch.rs:185-213]
[crates/ghook/src/dispatch.rs:223-226]
[crates/ghook/src/dispatch.rs:229-241]
- [[code/files/crates/ghook/src/envelope.rs|crates/ghook/src/envelope.rs]] - Defines the v1 inbox envelope format that ghook enqueues and the daemon replays, with a fixed schema version, enqueue timestamp, priority flag, hook type, raw JSON input, source, and ordered headers. `Envelope::new` builds instances with the current UTC RFC3339 timestamp and constant schema version, while the test module checks serialization and schema validation, including correct handling of optional headers as an omitted object rather than empty strings.
[crates/ghook/src/envelope.rs:24-32]
[crates/ghook/src/envelope.rs:34-52]
[crates/ghook/src/envelope.rs:35-51]
[crates/ghook/src/envelope.rs:59-70]
[crates/ghook/src/envelope.rs:73-84]
- [[code/files/crates/ghook/src/json_value.rs|crates/ghook/src/json_value.rs]] - Provides a small JSON utility for ghook that evaluates `serde_json::Value` using Python-style truthiness: `null`, `false`, zero numbers, empty strings, empty arrays, and empty objects are false, while booleans, nonzero numbers, nonempty strings, and nonempty collections are true. The test module confirms these dispatcher semantics with representative falsy and truthy cases.
[crates/ghook/src/json_value.rs:3-20]
[crates/ghook/src/json_value.rs:28-52]
- [[code/files/crates/ghook/src/main.rs|crates/ghook/src/main.rs]] - This file is the `ghook` CLI entrypoint and mode dispatcher. `main` parses command-line arguments, then routes to version handling, diagnostics, or gobby-owned hook execution; if no valid mode is selected, it prints a usage error and exits with code 2. `run_diagnose` implements the diagnostic path by requiring both `--cli` and `--type`, calling `diagnose::diagnose`, and printing the result as pretty JSON on stdout, or reporting an error and returning exit code 2 if validation or serialization fails.
[crates/ghook/src/main.rs:40-63]
[crates/ghook/src/main.rs:65-81]
- [[code/files/crates/ghook/src/output.rs|crates/ghook/src/output.rs]] - Provides tiny helper functions for writing formatted output to the process streams. `stdout` and `stderr` each lock the corresponding standard handle, call `write_fmt` with the supplied `Arguments`, and deliberately ignore any I/O error, giving the rest of the crate a simple, fire-and-forget way to print to standard output or error.
[crates/ghook/src/output.rs:3-5]
[crates/ghook/src/output.rs:7-9]
- [[code/files/crates/ghook/src/planned_shutdown.rs|crates/ghook/src/planned_shutdown.rs]] - This file implements planned shutdown handling for `Stop` hooks. It detects a fresh shutdown marker in the Gobby home directory, checks daemon reachability through a short health probe, and uses those two signals to decide when a `Stop` hook dispatch should be skipped because the daemon has intentionally gone away. It also handles failed post-enqueue cases by suppressing only `Stop` hook `Connect`/`Timeout` races during an active shutdown marker, deleting the queued item when suppression applies. The rest of the file is support code for reading and validating marker JSON, enforcing freshness and allowed intents/sources, parsing the freshness timeout from the environment, and providing small helpers and tests for those behaviors.
[crates/ghook/src/planned_shutdown.rs:21-27]
[crates/ghook/src/planned_shutdown.rs:29-37]
[crates/ghook/src/planned_shutdown.rs:39-50]
[crates/ghook/src/planned_shutdown.rs:52-54]
[crates/ghook/src/planned_shutdown.rs:56-62]
- [[code/files/crates/ghook/src/runtime.rs|crates/ghook/src/runtime.rs]] - Provides `write_runtime_stamp`, which initializes `~/.gobby/bin`, builds a `.ghook-runtime.json` stamp containing the current envelope schema version and `ghook` version, writes it atomically, and prints `ghook <version>` to stdout. The function ties together `gobby_core` path resolution, `envelope` metadata, `diagnose` version info, `transport` atomic persistence, and `output` reporting, returning any I/O or serialization error. [crates/ghook/src/runtime.rs:4-16]
- [[code/files/crates/ghook/src/source.rs|crates/ghook/src/source.rs]] - This file resolves the effective CLI source name, with a special override path only for `claude`: `detect_source` returns the configured source unchanged for non-`claude` CLIs, but can substitute `GOBBY_SOURCE` when that environment variable is set to a non-empty value. The test-only helpers `clear_source_env`, `set_source_env`, and `SourceEnvGuard` manage process-wide environment state safely across tests by clearing it on setup and drop. The unit test verifies the override behavior, including that `CLAUDE_CODE_ENTRYPOINT` is ignored, empty overrides are skipped, and non-`claude` sources are left alone.
[crates/ghook/src/source.rs:3-14]
[crates/ghook/src/source.rs:20-27]
[crates/ghook/src/source.rs:29-35]
[crates/ghook/src/source.rs:37]
[crates/ghook/src/source.rs:39-44]
- [[code/files/crates/ghook/src/statusline.rs|crates/ghook/src/statusline.rs]] - Implements the Claude Code statusline hook path for `ghook`: it accepts raw JSON from stdin, validates that the input is a JSON object, and then best-effort posts a derived session payload to the daemon while preserving the hook’s success exit behavior even on malformed input or transport failures. If `GOBBY_STATUSLINE_DOWNSTREAM` is set, it also forwards the original stdin bytes to a downstream shell command and relays that command’s stdout back unchanged, with timeout and process-group cleanup logic to avoid hanging or leaving survivors.

The supporting pieces split this into small responsibilities: `is_statusline_hook` gates the handler to Claude’s `statusline` hook, `extract_payload` pulls out the session/model/token metadata only when `session_id` is truthy, and the downstream helpers spawn, wait on, and terminate the child process tree safely on non-Windows platforms.
[crates/ghook/src/statusline.rs:25-27]
[crates/ghook/src/statusline.rs:29-35]
[crates/ghook/src/statusline.rs:37-67]
[crates/ghook/src/statusline.rs:69-104]
[crates/ghook/src/statusline.rs:106-119]
- [[code/files/crates/ghook/src/terminal_context.rs|crates/ghook/src/terminal_context.rs]] - Builds and injects a `terminal_context` JSON object for session-start hooks so the daemon can reconcile spawned-terminal agents. `capture` gathers `TMUX` and `TMUX_PANE` from the environment and delegates to `build_context`, while `enabled_for_hook` gates the logic to `sessionstart` hook types. `build_context` always records process and terminal data such as parent PID, TTY, `TERM_PROGRAM`, and `GOBBY_*` identifiers, but only includes tmux pane and socket path when `TMUX` is present and `TMUX_PANE` matches the expected `%<digits>` format. The helper functions handle environment lookup, Unix parent PID and TTY capture, tmux pane validation, and tmux socket-path parsing, and `inject` adds the computed context to an input JSON object only when `terminal_context` is missing.
[crates/ghook/src/terminal_context.rs:18-23]
[crates/ghook/src/terminal_context.rs:25-32]
[crates/ghook/src/terminal_context.rs:34-65]
[crates/ghook/src/terminal_context.rs:71-77]
[crates/ghook/src/terminal_context.rs:79-84]
- [[code/files/crates/ghook/src/transport.rs|crates/ghook/src/transport.rs]] - This file implements the enqueue-first transport path for `ghook`: it computes the inbox and quarantine locations under `~/.gobby/hooks/inbox`, generates lexicographically sortable envelope filenames with a critical/noncritical prefix, timestamp, and UUID, and persists envelopes atomically via temp-write, fsync, and rename before attempting delivery. It then posts the queued envelope to the daemon’s `/api/hooks/execute` endpoint, classifies failures as HTTP/connect/timeout/other, and deletes the inbox file only on a 2xx response; otherwise it leaves the file for replay and returns a `DeliveryReport` with diagnostics. It also provides quarantine helpers for malformed stdin, storing both the payload and metadata, plus tests that verify filename format, atomic writes, enqueueing, quarantine output, and post/cleanup behavior.
[crates/ghook/src/transport.rs:31-36]
[crates/ghook/src/transport.rs:40-45]
[crates/ghook/src/transport.rs:49-55]
[crates/ghook/src/transport.rs:58-60]
[crates/ghook/src/transport.rs:63-65]

## Components

- `f5dd5560-82fb-5444-90ec-c52f14453103`
- `f7f34afc-91e9-5d08-9c85-a1d2c956cfd8`
- `a0e2dc98-470a-5a92-b323-c3897cdac1bd`
- `53a2cebe-fa56-5b23-b6e2-aff808c32b5b`
- `7943af65-4575-5a6f-9788-0a7d2baa60b5`
- `878d10af-1a06-51a8-8f6d-d3bba3752a2a`
- `f3e134e5-9f40-5b9e-80cc-5c148e09d975`
- `7f389900-230b-5d25-9703-a26670c58474`
- `508c1c2e-6c93-5d01-9766-ce34b69ade39`
- `b0f88c8a-e48b-5c3e-9a97-e372b2692a29`
- `7f885d7d-c804-5a80-8084-03cd78960082`
- `f62c6e5c-cd61-5335-b502-c6d8ec2b044f`
- `4d4e6520-a366-57ba-816c-e2850ac098ed`
- `386ef81c-1c92-53f0-9b74-7a8e9de97905`
- `6c09b433-2e48-5a35-8569-597437823e71`
- `d26f5a56-d6d1-5b4b-a9d4-bba1710f7a37`
- `01ba2b47-3993-5e79-a5c4-b1d9417b1295`
- `81126c57-cc7f-59bc-a418-b5e6d245b775`
- `b9db8a12-d623-524a-9dab-0ece537db020`
- `ac7a2683-4f39-53e9-8fed-8bf949abe7b8`
- `0ebbc49b-d873-572f-b040-a9df9661de4d`
- `8c567c91-48d2-57b8-bf80-8b01cbf75b4e`
- `b560222e-c106-56c2-b2d5-5767deb0befb`
- `46b23092-7854-5a75-a3c3-64a9bb32ab49`
- `8ecf33c0-a92d-5b09-9597-2c43d1f64282`
- `8c4d5e40-b536-5aa5-85cf-cd46e8578cf5`
- `154c6c0f-2312-50d9-a91b-7174eaa8d2a6`
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
- `862baaa6-b74c-51be-a87d-4dcbb6f21965`
- `f2c73a2d-1c53-506d-a354-4e94eb6967f8`
- `cedf4a3a-8ca0-5584-98f4-a65a36cf6613`
- `f06761bf-55c8-50f1-a59b-de439e47366e`
- `7a9c79a8-0887-5c95-bee8-9edbf5ad760c`
- `2f2bbcab-d802-53cd-a5ff-3df416ab975e`
- `93e5c8ff-70cd-5df6-9754-ff0e410415de`
- `abf502a8-9127-50c3-aa41-b3bcec08825b`
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
- `dee4d56b-3252-5af3-b9d2-b1548601bf33`
- `80fd2295-eda8-5a6e-88af-12217cc3aa17`
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
- `56de4550-bc82-5099-9930-43415fd43d07`
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

