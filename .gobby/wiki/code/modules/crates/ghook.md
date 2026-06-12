---
title: crates/ghook
type: code_module
provenance:
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
  ranges:
  - 2-79
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
  ranges:
  - 2-63
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
  - 303-331
  - 333-341
  - 343-413
  - 415-434
  - 436-496
  - 498-520
  - 522-550
  - 552-564
  - 575-578
  - 581-593
  - 596-604
  - 607-647
  - 650-671
  - 674-690
  - 693-709
  - 712-729
  - 732-750
  - 753-769
  - 772-788
  - 791-802
  - 805-811
  - 814-830
  - 833-847
  - 850-865
  - 868-881
  - 884-894
  - 897-910
  - 913-926
  - 929-961
  - 964-973
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

# crates/ghook

Parent: [[code/modules/crates|crates]]

## Overview

The crates/ghook module provides a resilient, Rust-based sidecar utility and its associated JSON Schema contracts to intercept, validate, and dispatch CLI tool-use and session-lifecycle hook events to the central Gobby daemon.
[crates/ghook/schemas/diagnose-output.v2.schema.json:2]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:2]
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/detach.rs:23-43]
[crates/ghook/src/diagnose.rs:15-32]

## Child Modules

- [[code/modules/crates/ghook/schemas|crates/ghook/schemas]] - The `crates/ghook/schemas` module defines JSON Schema contracts for ghook's data interchange. It contains two versioned schemas: `diagnose-output.v2.schema.json`, which specifies the diagnostic report format (CLI detection, daemon connection details, terminal context, and installation metadata), and `inbox-envelope.v1.schema.json`, which describes queued hook event envelopes (schema version, enqueue timestamp, hook type, input data, source, and Gobby project/session headers). These schemas serve as the validation and documentation source of truth for ghook's structured outputs and message payloads.
[crates/ghook/schemas/diagnose-output.v2.schema.json:2]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:2]
[crates/ghook/schemas/diagnose-output.v2.schema.json:3]
[crates/ghook/schemas/diagnose-output.v2.schema.json:4]
[crates/ghook/schemas/diagnose-output.v2.schema.json:5]
- [[code/modules/crates/ghook/src|crates/ghook/src]] - The crates/ghook/src module implements a resilient Rust-based sidecar utility that intercepts, validates, and dispatches CLI tool-use and session-lifecycle hooks to the central Gobby daemon.

Key Capabilities:
- CLI Configuration & Detection (cli_config, source): Maps critical/non-critical hooks and detects environment-derived client sources (such as Claude, Droid, and Codex).
- Context & Envelope Management (envelope, terminal_context, json_value): Encapsulates hook payloads in validated envelopes while injecting TMUX pane and terminal context.
- High-Reliability Transport & Queueing (transport, planned_shutdown, detach): Guarantees reliable delivery via atomic file-based queuing (inbox/quarantine) and suppresses dispatches during planned daemon shutdowns.
- Execution Control & Diagnostics (main, diagnose, statusline, output): Routes hook actions (allow, block, or specific exit-codes), validates installation provenance, and processes real-time status-line feeds.
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/detach.rs:23-43]
[crates/ghook/src/diagnose.rs:15-32]
[crates/ghook/src/envelope.rs:24-32]
[crates/ghook/src/json_value.rs:3-20]

## Files

- [[code/files/crates/ghook/Cargo.toml|crates/ghook/Cargo.toml]] - `crates/ghook/Cargo.toml` has no indexed API symbols. 
- [[code/files/crates/ghook/README.md|crates/ghook/README.md]] - `crates/ghook/README.md` has no indexed API symbols. 

