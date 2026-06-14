---
title: crates/gloc/config.yaml
type: code_file
provenance:
- file: crates/gloc/config.yaml
  ranges:
  - 11-57
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gloc/config.yaml

Module: [[code/modules/crates/gloc|crates/gloc]]

## Purpose

This file defines the built-in default `gloc` configuration: global settings, backend discovery, client launch templates, and model aliases. The `settings` block tunes probing and pull behavior, `backends` lists local LLM servers to probe in priority order, `clients` maps supported CLIs (`claude` and `codex`) to their binaries, environment variables, model flags, and defaults, and `aliases` provides shorthand model names that resolve before execution.
[crates/gloc/config.yaml:11-17]
[crates/gloc/config.yaml:12]
[crates/gloc/config.yaml:13]
[crates/gloc/config.yaml:14]
[crates/gloc/config.yaml:18-30]

## API Symbols

- `settings` (property) component `settings [property]` (`fca2a16f-84a6-52a6-a2da-6c1b375d372f`) lines 11-17 [crates/gloc/config.yaml:11-17]
  - Signature: `settings:`
  - Purpose: Indexed property `settings` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:11-17]
- `probe_timeout_ms` (property) component `probe_timeout_ms [property]` (`04b11aa3-1b5b-545f-a800-7ecbf30988bb`) lines 12-12 [crates/gloc/config.yaml:12]
  - Signature: `probe_timeout_ms: 500`
  - Purpose: Indexed property `probe_timeout_ms` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:12]
- `auto_load` (property) component `auto_load [property]` (`313132e9-8044-58d9-bb7e-81d4c6902638`) lines 13-13 [crates/gloc/config.yaml:13]
  - Signature: `auto_load: true # load model into backend before exec`
  - Purpose: Indexed property `auto_load` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:13]
- `auto_pull` (property) component `auto_pull [property]` (`475d66fe-76c2-557d-8431-f8e87ce9a610`) lines 14-14 [crates/gloc/config.yaml:14]
  - Signature: `auto_pull: false # (ollama) pull model if not downloaded`
  - Purpose: Indexed property `auto_pull` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:14]
- `backends` (property) component `backends [property]` (`7e6d23f7-5cf0-58a8-bfdf-bec89f7d7722`) lines 18-30 [crates/gloc/config.yaml:18-30]
  - Signature: `backends:`
  - Purpose: Indexed property `backends` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:18-30]
- `name` (property) component `name [property]` (`b914bfb4-16c7-5836-b2e2-051eebd5c8ab`) lines 19-19 [crates/gloc/config.yaml:19]
  - Signature: `name: lmstudio`
  - Purpose: Indexed property `name` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:19]
- `url` (property) component `url [property]` (`c2e39dba-680b-5a6a-af82-563b838f9286`) lines 20-20 [crates/gloc/config.yaml:20]
  - Signature: `url: "http://localhost:1234"`
  - Purpose: Indexed property `url` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:20]
- `probe` (property) component `probe [property]` (`ab98c7d7-260d-527a-80c2-22a8bd6118ee`) lines 21-21 [crates/gloc/config.yaml:21]
  - Signature: `probe: "/v1/models"`
  - Purpose: Indexed property `probe` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:21]
- `auth_token` (property) component `auth_token [property]` (`13915f2a-bc13-52d8-862a-c21d2f98d965`) lines 22-22 [crates/gloc/config.yaml:22]
  - Signature: `auth_token: "lmstudio"`
  - Purpose: Indexed property `auth_token` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:22]
- `name` (property) component `name [property]` (`413fb398-c19d-523e-84b9-041475d8ffeb`) lines 24-24 [crates/gloc/config.yaml:24]
  - Signature: `name: ollama`
  - Purpose: Indexed property `name` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:24]
- `url` (property) component `url [property]` (`5049e07f-6d87-5f55-9c8f-8896de2e72b3`) lines 25-25 [crates/gloc/config.yaml:25]
  - Signature: `url: "http://localhost:11434"`
  - Purpose: Indexed property `url` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:25]
- `probe` (property) component `probe [property]` (`32c813bd-4073-5451-b7d5-d04adeda76f2`) lines 26-26 [crates/gloc/config.yaml:26]
  - Signature: `probe: "/api/tags"`
  - Purpose: Indexed property `probe` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:26]
- `auth_token` (property) component `auth_token [property]` (`04efb0e7-57ef-5e08-b8e8-7c14b8c43479`) lines 27-27 [crates/gloc/config.yaml:27]
  - Signature: `auth_token: "ollama"`
  - Purpose: Indexed property `auth_token` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:27]
- `clients` (property) component `clients [property]` (`9ae122eb-af10-58c6-b9a4-9144194d54d6`) lines 31-53 [crates/gloc/config.yaml:31-53]
  - Signature: `clients:`
  - Purpose: Indexed property `clients` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:31-53]
- `claude` (property) component `claude [property]` (`efd7875e-42db-5f72-ad1a-3d76d7171af8`) lines 32-41 [crates/gloc/config.yaml:32-41]
  - Signature: `claude:`
  - Purpose: Indexed property `claude` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:32-41]
- `binary` (property) component `binary [property]` (`28bf3f0c-0ce4-5b5d-9d3c-1d062c457948`) lines 33-33 [crates/gloc/config.yaml:33]
  - Signature: `binary: "claude"`
  - Purpose: Indexed property `binary` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:33]
- `env` (property) component `env [property]` (`d781b89f-e056-5b21-9871-3f8a7a2d7090`) lines 34-37 [crates/gloc/config.yaml:34-37]
  - Signature: `env:`
  - Purpose: Indexed property `env` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:34-37]
- `ANTHROPIC_BASE_URL` (property) component `ANTHROPIC_BASE_URL [property]` (`482a3db1-9298-5d02-8a9c-699162d4d8ad`) lines 35-35 [crates/gloc/config.yaml:35]
  - Signature: `ANTHROPIC_BASE_URL: "{backend.url}"`
  - Purpose: Indexed property `ANTHROPIC_BASE_URL` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:35]
- `ANTHROPIC_AUTH_TOKEN` (property) component `ANTHROPIC_AUTH_TOKEN [property]` (`21644cb4-ca97-56e3-8251-e8f9ba6b59a0`) lines 36-36 [crates/gloc/config.yaml:36]
  - Signature: `ANTHROPIC_AUTH_TOKEN: "{backend.auth_token}"`
  - Purpose: Indexed property `ANTHROPIC_AUTH_TOKEN` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:36]
- `ANTHROPIC_API_KEY` (property) component `ANTHROPIC_API_KEY [property]` (`3c38a5c3-b1b5-5a84-8f75-88e3d0c09ae9`) lines 37-37 [crates/gloc/config.yaml:37]
  - Signature: `ANTHROPIC_API_KEY: ""`
  - Purpose: Indexed property `ANTHROPIC_API_KEY` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:37]
- `model_flag` (property) component `model_flag [property]` (`eb44b6b2-b05f-58cc-bcb2-4bb400d58061`) lines 38-38 [crates/gloc/config.yaml:38]
  - Signature: `model_flag: "--model"`
  - Purpose: Indexed property `model_flag` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:38]
- `default_model` (property) component `default_model [property]` (`7b1c893e-aefc-5e3c-b865-b62409ed0b83`) lines 39-39 [crates/gloc/config.yaml:39]
  - Signature: `default_model: "qwen3-coder"`
  - Purpose: Indexed property `default_model` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:39]
- `default_args` (property) component `default_args [property]` (`ac6ad77e-d061-57a5-ba7d-dc057d43b909`) lines 40-40 [crates/gloc/config.yaml:40]
  - Signature: `default_args: []`
  - Purpose: Indexed property `default_args` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:40]
- `default_env` (property) component `default_env [property]` (`f7d5cdc0-f29a-5efd-bf0e-b96324e7ebdf`) lines 41-41 [crates/gloc/config.yaml:41]
  - Signature: `default_env: {}`
  - Purpose: Indexed property `default_env` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:41]
- `codex` (property) component `codex [property]` (`05731d3c-a5fb-51e0-9655-d89b0bc7c9bb`) lines 43-53 [crates/gloc/config.yaml:43-53]
  - Signature: `codex:`
  - Purpose: Indexed property `codex` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:43-53]
- `binary` (property) component `binary [property]` (`8babf43f-0599-5b78-8748-190f778ea759`) lines 44-44 [crates/gloc/config.yaml:44]
  - Signature: `binary: "codex"`
  - Purpose: Indexed property `binary` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:44]
- `env` (property) component `env [property]` (`15493f17-5f74-5d14-afca-1d6b769864f8`) lines 45-47 [crates/gloc/config.yaml:45-47]
  - Signature: `env:`
  - Purpose: Indexed property `env` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:45-47]
- `OPENAI_BASE_URL` (property) component `OPENAI_BASE_URL [property]` (`eff2b949-cec7-599a-a509-92a8e12f5811`) lines 46-46 [crates/gloc/config.yaml:46]
  - Signature: `OPENAI_BASE_URL: "{backend.url}/v1"`
  - Purpose: Indexed property `OPENAI_BASE_URL` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:46]
- `OPENAI_API_KEY` (property) component `OPENAI_API_KEY [property]` (`3e365d89-2306-55a5-8806-6fb90ce67a48`) lines 47-47 [crates/gloc/config.yaml:47]
  - Signature: `OPENAI_API_KEY: "{backend.auth_token}"`
  - Purpose: Indexed property `OPENAI_API_KEY` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:47]
- `model_flag` (property) component `model_flag [property]` (`2ac4f039-c2ea-544d-8a90-22c06212e12d`) lines 48-48 [crates/gloc/config.yaml:48]
  - Signature: `model_flag: "--model"`
  - Purpose: Indexed property `model_flag` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:48]
- `default_model` (property) component `default_model [property]` (`91549709-be6f-5b84-ac7f-4ec96cddbae5`) lines 49-49 [crates/gloc/config.yaml:49]
  - Signature: `default_model: "qwen3-coder"`
  - Purpose: Indexed property `default_model` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:49]
- `default_args` (property) component `default_args [property]` (`1fccc83d-723c-59ed-93c4-bfccb034c101`) lines 50-50 [crates/gloc/config.yaml:50]
  - Signature: `default_args: ["--provider", "openai"]`
  - Purpose: Indexed property `default_args` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:50]
- `default_env` (property) component `default_env [property]` (`6231898d-ade2-5b01-b710-831cc7ceb7bf`) lines 51-51 [crates/gloc/config.yaml:51]
  - Signature: `default_env: {}`
  - Purpose: Indexed property `default_env` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:51]
- `aliases` (property) component `aliases [property]` (`61f6465c-bf9e-5ee6-a0ac-489b5f76057e`) lines 54-57 [crates/gloc/config.yaml:54-57]
  - Signature: `aliases:`
  - Purpose: Indexed property `aliases` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:54-57]
- `qwen` (property) component `qwen [property]` (`737445ee-9824-5713-ad7c-3aba5967b9b9`) lines 55-55 [crates/gloc/config.yaml:55]
  - Signature: `qwen: "qwen3-coder"`
  - Purpose: Indexed property `qwen` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:55]
- `glm` (property) component `glm [property]` (`ce6d3345-56be-5343-afeb-200078408c2e`) lines 56-56 [crates/gloc/config.yaml:56]
  - Signature: `glm: "glm-4.7:cloud"`
  - Purpose: Indexed property `glm` in `crates/gloc/config.yaml`. [crates/gloc/config.yaml:56]

