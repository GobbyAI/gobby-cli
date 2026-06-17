---
title: crates/gcore/src/ai/daemon/operations.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/operations.rs
  ranges:
  - 20-72
  - 74-112
  - 114-120
  - 125-163
  - 165-199
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/daemon/operations.rs:20-72](crates/gcore/src/ai/daemon/operations.rs#L20-L72), [crates/gcore/src/ai/daemon/operations.rs:74-112](crates/gcore/src/ai/daemon/operations.rs#L74-L112), [crates/gcore/src/ai/daemon/operations.rs:114-120](crates/gcore/src/ai/daemon/operations.rs#L114-L120), [crates/gcore/src/ai/daemon/operations.rs:125-163](crates/gcore/src/ai/daemon/operations.rs#L125-L163), [crates/gcore/src/ai/daemon/operations.rs:165-199](crates/gcore/src/ai/daemon/operations.rs#L165-L199)

</details>

# crates/gcore/src/ai/daemon/operations.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Implements the daemon-backed AI operation layer for this crate. It wraps the local daemon’s transcription, vision, text generation, and embedding endpoints, assembling request bodies/forms from `AiContext` and operation options, applying the shared limiter and retry/backoff behavior, and delegating parsing to response helpers so each public function returns the corresponding typed result.
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/operations.rs:74-112]
[crates/gcore/src/ai/daemon/operations.rs:114-120]
[crates/gcore/src/ai/daemon/operations.rs:125-163]
[crates/gcore/src/ai/daemon/operations.rs:165-199]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `transcribe_via_daemon` | function | `pub fn transcribe_via_daemon(` | `transcribe_via_daemon [function]` | `d0c884c3-2413-5359-8687-746b3c4ea4f0` | 20-72 [crates/gcore/src/ai/daemon/operations.rs:20-72] | Indexed function `transcribe_via_daemon` in `crates/gcore/src/ai/daemon/operations.rs`. [crates/gcore/src/ai/daemon/operations.rs:20-72] |
| `describe_image_via_daemon` | function | `pub fn describe_image_via_daemon(` | `describe_image_via_daemon [function]` | `319b3f75-14cc-571b-9975-5a387539338f` | 74-112 [crates/gcore/src/ai/daemon/operations.rs:74-112] | Indexed function `describe_image_via_daemon` in `crates/gcore/src/ai/daemon/operations.rs`. [crates/gcore/src/ai/daemon/operations.rs:74-112] |
| `generate_via_daemon` | function | `pub fn generate_via_daemon(` | `generate_via_daemon [function]` | `b31d70ad-af61-55f9-8d05-95f978bbac2a` | 114-120 [crates/gcore/src/ai/daemon/operations.rs:114-120] | Indexed function `generate_via_daemon` in `crates/gcore/src/ai/daemon/operations.rs`. [crates/gcore/src/ai/daemon/operations.rs:114-120] |
| `generate_via_daemon_with_max_tokens` | function | `pub fn generate_via_daemon_with_max_tokens(` | `generate_via_daemon_with_max_tokens [function]` | `d0f0c56e-87d9-5ed4-bb4a-75194e163426` | 125-163 [crates/gcore/src/ai/daemon/operations.rs:125-163] | Indexed function `generate_via_daemon_with_max_tokens` in `crates/gcore/src/ai/daemon/operations.rs`. [crates/gcore/src/ai/daemon/operations.rs:125-163] |
| `embed_via_daemon` | function | `pub fn embed_via_daemon(` | `embed_via_daemon [function]` | `9d5431ab-69e6-5fa2-8a27-24da33201ad1` | 165-199 [crates/gcore/src/ai/daemon/operations.rs:165-199] | Indexed function `embed_via_daemon` in `crates/gcore/src/ai/daemon/operations.rs`. [crates/gcore/src/ai/daemon/operations.rs:165-199] |
