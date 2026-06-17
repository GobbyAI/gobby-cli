---
title: crates/ghook/src/args.rs
type: code_file
provenance:
- file: crates/ghook/src/args.rs
  ranges:
  - 9-33
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/args.rs:9-33](crates/ghook/src/args.rs#L9-L33)

</details>

# crates/ghook/src/args.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Defines the `ghook` command-line argument parser using `clap::Parser`. The `Args` struct collects the hook dispatcher’s flags into one place: `gobby_owned` marks normal hook-invocation mode, `diagnose` and `version` enable diagnostic/version output, `cli` and `hook_type` identify the host CLI and hook variant, and `detach` controls whether the process leaves the parent session before POST handling. [crates/ghook/src/args.rs:9-33]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Args` | class | `pub(crate) struct Args {` | `Args [class]` | `154c6c0f-2312-50d9-a91b-7174eaa8d2a6` | 9-33 [crates/ghook/src/args.rs:9-33] | Indexed class `Args` in `crates/ghook/src/args.rs`. [crates/ghook/src/args.rs:9-33] |
