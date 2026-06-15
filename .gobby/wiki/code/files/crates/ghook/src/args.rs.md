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

# crates/ghook/src/args.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Defines the `ghook` CLI argument type used to configure hook dispatch behavior. `Args` is a `clap::Parser` struct for the crate-visible entrypoint, collecting flags for owned invocation mode, diagnostic output, version stamping, host CLI name, hook type, and optional process-group detachment. These fields work together to steer whether the hook runs normally, emits diagnostics, records a runtime version stamp, and how it identifies the calling CLI and hook kind before posting. [crates/ghook/src/args.rs:9-33]

## API Symbols

- `Args` (class) component `Args [class]` (`154c6c0f-2312-50d9-a91b-7174eaa8d2a6`) lines 9-33 [crates/ghook/src/args.rs:9-33]
  - Signature: `pub(crate) struct Args {`
  - Purpose: 'Args' is a crate-visible CLI argument struct that configures gobby hook execution via flags for owned invocation mode, diagnostics, version stamping, host CLI name, hook type, and optional detachment from the parent process group. [crates/ghook/src/args.rs:9-33]

