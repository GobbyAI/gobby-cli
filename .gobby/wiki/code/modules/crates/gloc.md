---
title: crates/gloc
type: code_module
provenance:
- file: crates/gloc/config.yaml
  ranges:
  - 11-57
- file: crates/gloc/src/backend.rs
  ranges:
  - 7-12
  - 14-23
  - 28-62
  - 67-108
  - 111-129
  - 132-149
  - 153-162
  - 168-175
  - 178-181
  - 184-189
  - 192-201
  - 204-207
  - 210-213
  - 216-219
  - 222-225
  - 228-231
  - 234-243
- file: crates/gloc/src/config.rs
  ranges:
  - 13-22
  - 25-32
  - 34-42
  - 44-46
  - 48-50
  - 53-65
  - 67-138
  - 142-148
  - 155-160
  - 163-168
  - 171-182
  - 185-189
  - 192-207
  - 210-219
  - 222-226
  - 229-232
  - 235-238
  - 241-250
  - 253-262
  - 265-274
  - 277-288
  - 291-299
  - 302-307
  - 310-317
  - 320-327
- file: crates/gloc/src/exec.rs
  ranges:
  - 9-21
  - 24-36
  - 39-45
  - 51-80
  - 87-94
  - 96-109
  - 111-123
  - 126-134
  - 137-144
  - 147-150
  - 153-156
  - 159-163
  - 166-171
  - 174-188
  - 191-194
  - 197-199
- file: crates/gloc/src/main.rs
  ranges:
  - 16-52
  - 54-118
  - 120-130
  - 132-155
  - 157-202
  - 204-213
  - 215-223
  - 225-250
  - 252-255
  - 257-288
  - 294-301
  - 304-318
  - 321-327
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gloc

Parent: [[code/modules/crates|crates]]

## Overview

The gloc module provides the core infrastructure for the gloc command-line utility, enabling the configuration, verification, resolution, and execution of local and remote AI models and clients. It integrates backend management (such as Ollama check, pull, and warmup procedures), client environments (including Claude and Codex), configuration loading, template and alias resolution, and terminal command execution.
[crates/gloc/config.yaml:11-17]
[crates/gloc/src/backend.rs:7-12]
[crates/gloc/src/config.rs:13-22]
[crates/gloc/src/exec.rs:9-21]
[crates/gloc/src/main.rs:16-52]

## Child Modules

- [[code/modules/crates/gloc/src|crates/gloc/src]] - This module forms the core of the `gloc` command-line utility, providing the infrastructure to configure, resolve, and execute local and remote AI models and clients.

- **backend.rs** handles backend status monitoring and model management, including detecting reachable endpoints, ensuring required models are pulled and ready (specifically for Ollama), and validating model names.
- **config.rs** manages loading, merging, and dumping application configurations, default settings, aliases, and template resolution for client parameters.
- **exec.rs** handles process execution logic, dynamically building environment variables and command arguments to run client binaries (like Claude or Codex) based on resolved backend configurations.
- **main.rs** provides the command-line interface entry point, managing CLI parsing, backend/client/model resolution, configuration initialization, and execution coordination.
[crates/gloc/src/backend.rs:7-12]
[crates/gloc/src/config.rs:13-22]
[crates/gloc/src/exec.rs:9-21]
[crates/gloc/src/main.rs:16-52]
[crates/gloc/src/backend.rs:14-23]

## Files

- [[code/files/crates/gloc/Cargo.toml|crates/gloc/Cargo.toml]] - `crates/gloc/Cargo.toml` has no indexed API symbols. 
- [[code/files/crates/gloc/config.yaml|crates/gloc/config.yaml]] - `crates/gloc/config.yaml` exposes 36 indexed API symbols.
[crates/gloc/config.yaml:11-17]
[crates/gloc/config.yaml:12]
[crates/gloc/config.yaml:13]
[crates/gloc/config.yaml:14]
[crates/gloc/config.yaml:18-30]

## Components

- `fca2a16f-84a6-52a6-a2da-6c1b375d372f`
- `04b11aa3-1b5b-545f-a800-7ecbf30988bb`
- `313132e9-8044-58d9-bb7e-81d4c6902638`
- `475d66fe-76c2-557d-8431-f8e87ce9a610`
- `7e6d23f7-5cf0-58a8-bfdf-bec89f7d7722`
- `b914bfb4-16c7-5836-b2e2-051eebd5c8ab`
- `c2e39dba-680b-5a6a-af82-563b838f9286`
- `ab98c7d7-260d-527a-80c2-22a8bd6118ee`
- `13915f2a-bc13-52d8-862a-c21d2f98d965`
- `413fb398-c19d-523e-84b9-041475d8ffeb`
- `5049e07f-6d87-5f55-9c8f-8896de2e72b3`
- `32c813bd-4073-5451-b7d5-d04adeda76f2`
- `04efb0e7-57ef-5e08-b8e8-7c14b8c43479`
- `9ae122eb-af10-58c6-b9a4-9144194d54d6`
- `efd7875e-42db-5f72-ad1a-3d76d7171af8`
- `28bf3f0c-0ce4-5b5d-9d3c-1d062c457948`
- `d781b89f-e056-5b21-9871-3f8a7a2d7090`
- `482a3db1-9298-5d02-8a9c-699162d4d8ad`
- `21644cb4-ca97-56e3-8251-e8f9ba6b59a0`
- `3c38a5c3-b1b5-5a84-8f75-88e3d0c09ae9`
- `eb44b6b2-b05f-58cc-bcb2-4bb400d58061`
- `7b1c893e-aefc-5e3c-b865-b62409ed0b83`
- `ac6ad77e-d061-57a5-ba7d-dc057d43b909`
- `f7d5cdc0-f29a-5efd-bf0e-b96324e7ebdf`
- `05731d3c-a5fb-51e0-9655-d89b0bc7c9bb`
- `8babf43f-0599-5b78-8748-190f778ea759`
- `15493f17-5f74-5d14-afca-1d6b769864f8`
- `eff2b949-cec7-599a-a509-92a8e12f5811`
- `3e365d89-2306-55a5-8806-6fb90ce67a48`
- `2ac4f039-c2ea-544d-8a90-22c06212e12d`
- `91549709-be6f-5b84-ac7f-4ec96cddbae5`
- `1fccc83d-723c-59ed-93c4-bfccb034c101`
- `6231898d-ade2-5b01-b710-831cc7ceb7bf`
- `61f6465c-bf9e-5ee6-a0ac-489b5f76057e`
- `737445ee-9824-5713-ad7c-3aba5967b9b9`
- `ce6d3345-56be-5343-afeb-200078408c2e`

