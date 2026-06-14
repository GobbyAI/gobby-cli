---
title: crates/gloc/src
type: code_module
provenance:
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

# crates/gloc/src

Parent: [[code/modules/crates/gloc|crates/gloc]]

## Overview

The `crates/gloc/src` module implements the `gloc` launcher: it loads configuration, resolves a backend/client/model combination, prepares local model availability, then transfers control to the selected AI CLI tool. The CLI surface in `main.rs` accepts client, backend, model, URL override, config path, status/init/dump modes, and passthrough arguments, then sequences early exits, config loading/export, backend and client resolution, alias-aware model resolution, status printing, readiness checks, and execution handoff [crates/gloc/src/main.rs:16-52] [crates/gloc/src/main.rs:54-100]. Configuration is owned by `config.rs`, where `Config` groups settings, backend definitions, named clients, and aliases, with defaults for probe timeout, auto-load, and auto-pull behavior .

Backend readiness is isolated in `backend.rs`. `ensure_model_ready` deliberately no-ops for non-Ollama backends, while Ollama follows a check, optional pull, and optional warmup flow controlled by `Settings`; failures are represented as `ModelError` variants for missing models, pull failures, warmup failures, and network errors  . This keeps model lifecycle policy separate from CLI orchestration, so `main.rs` only has to call readiness after resolving the active backend and model [crates/gloc/src/main.rs:84-100].

Process launch concerns live in `exec.rs`. It builds the child environment by applying `default_env` first and allowing explicit client env values to override it, resolving templates against the selected backend and model . It then assembles arguments from the model flag, client default args, and passthrough CLI args , provides `PATH` lookup for binaries , and finally executes the configured client, replacing the current process on Unix or spawning and exiting with the child status elsewhere .

## Call Diagram

```mermaid
sequenceDiagram
    participant m_0de5951d_2ed3_58aa_905b_800fd4e0804b as Settings.default &#91;method&#93;
    participant m_123761e3_1ee3_58ad_9298_11ac7b82103f as default_probe_timeout_ms &#91;function&#93;
    participant m_1550bb68_f95d_5cf7_9a78_634164f14e23 as ensure_model_ready &#91;function&#93;
    participant m_1a718268_cb56_5f8f_9339_ce52e89cb9c9 as test_build_args_with_model &#91;function&#93;
    participant m_1e60195b_5788_5f91_b6e2_6d960a13ecfb as test_build_args_codex_with_defaults &#91;function&#93;
    participant m_2679f7d7_f4bb_5c79_a06e_537fc750cf7c as main &#91;function&#93;
    participant m_2e3be105_cdbe_547f_90a6_bbe2885de96b as ollama_pull_model &#91;function&#93;
    participant m_35e60a15_0461_5842_8f99_d112b9e7f80e as handle_init &#91;function&#93;
    participant m_3be65073_d21a_506e_b864_3d6c82092932 as test_build_env_claude &#91;function&#93;
    participant m_3ef29eda_b6d2_5dbe_b208_162ea81f5f20 as build_args &#91;function&#93;
    participant m_40a6142a_2255_5000_b2bc_ed6d91bd0a5f as test_resolve_template_model &#91;function&#93;
    participant m_44053d16_a034_5247_9e93_82f38395b494 as exec_client &#91;function&#93;
    participant m_44b0a98a_f234_5970_930e_8d6b63632257 as resolve_template &#91;function&#93;
    participant m_54307264_6cff_5244_af17_1dbc2b3602dd as auto_export_config &#91;function&#93;
    participant m_5f667291_dbf4_517d_a474_fdd7b7d4dfce as build_env &#91;function&#93;
    participant m_65a042fe_e2ee_5878_9e01_26b1c2f0a546 as resolve_client &#91;function&#93;
    participant m_89009b7e_536e_522d_a4a2_2cefee9baad0 as default_auto_load &#91;function&#93;
    participant m_890d349c_d19a_5229_83bd_f48033ddab58 as test_codex_client &#91;function&#93;
    participant m_a3d5db2c_8890_5b16_90da_6767d68c5e42 as resolve_model &#91;function&#93;
    participant m_b32f228a_fea3_57c7_bbaf_095136afd61e as test_claude_client &#91;function&#93;
    participant m_c0d554a5_0ee5_5ddb_bae2_cc4021fb3ed0 as test_backend &#91;function&#93;
    participant m_c3153167_82c9_5ef3_a9f2_0b33df034b8c as ollama_check_model &#91;function&#93;
    participant m_c6062f0e_c3d4_5982_80a3_b19a5c29b2f9 as print_status &#91;function&#93;
    participant m_cd57587b_8493_53ba_bd7d_73e123d81762 as ollama_warmup_model &#91;function&#93;
    participant m_dfb631c4_7c31_59e2_b1f4_fc716efe1cbd as resolve_backend &#91;function&#93;
    m_0de5951d_2ed3_58aa_905b_800fd4e0804b->>m_123761e3_1ee3_58ad_9298_11ac7b82103f: calls
    m_0de5951d_2ed3_58aa_905b_800fd4e0804b->>m_89009b7e_536e_522d_a4a2_2cefee9baad0: calls
    m_1550bb68_f95d_5cf7_9a78_634164f14e23->>m_2e3be105_cdbe_547f_90a6_bbe2885de96b: calls
    m_1550bb68_f95d_5cf7_9a78_634164f14e23->>m_c3153167_82c9_5ef3_a9f2_0b33df034b8c: calls
    m_1550bb68_f95d_5cf7_9a78_634164f14e23->>m_cd57587b_8493_53ba_bd7d_73e123d81762: calls
    m_1a718268_cb56_5f8f_9339_ce52e89cb9c9->>m_3ef29eda_b6d2_5dbe_b208_162ea81f5f20: calls
    m_1a718268_cb56_5f8f_9339_ce52e89cb9c9->>m_b32f228a_fea3_57c7_bbaf_095136afd61e: calls
    m_1e60195b_5788_5f91_b6e2_6d960a13ecfb->>m_3ef29eda_b6d2_5dbe_b208_162ea81f5f20: calls
    m_1e60195b_5788_5f91_b6e2_6d960a13ecfb->>m_890d349c_d19a_5229_83bd_f48033ddab58: calls
    m_2679f7d7_f4bb_5c79_a06e_537fc750cf7c->>m_35e60a15_0461_5842_8f99_d112b9e7f80e: calls
    m_2679f7d7_f4bb_5c79_a06e_537fc750cf7c->>m_54307264_6cff_5244_af17_1dbc2b3602dd: calls
    m_2679f7d7_f4bb_5c79_a06e_537fc750cf7c->>m_65a042fe_e2ee_5878_9e01_26b1c2f0a546: calls
    m_2679f7d7_f4bb_5c79_a06e_537fc750cf7c->>m_a3d5db2c_8890_5b16_90da_6767d68c5e42: calls
    m_2679f7d7_f4bb_5c79_a06e_537fc750cf7c->>m_c6062f0e_c3d4_5982_80a3_b19a5c29b2f9: calls
    m_2679f7d7_f4bb_5c79_a06e_537fc750cf7c->>m_dfb631c4_7c31_59e2_b1f4_fc716efe1cbd: calls
    m_3be65073_d21a_506e_b864_3d6c82092932->>m_5f667291_dbf4_517d_a474_fdd7b7d4dfce: calls
    m_3be65073_d21a_506e_b864_3d6c82092932->>m_b32f228a_fea3_57c7_bbaf_095136afd61e: calls
    m_3be65073_d21a_506e_b864_3d6c82092932->>m_c0d554a5_0ee5_5ddb_bae2_cc4021fb3ed0: calls
    m_40a6142a_2255_5000_b2bc_ed6d91bd0a5f->>m_44b0a98a_f234_5970_930e_8d6b63632257: calls
    m_44053d16_a034_5247_9e93_82f38395b494->>m_3ef29eda_b6d2_5dbe_b208_162ea81f5f20: calls
```

## Files

- [[code/files/crates/gloc/src/backend.rs|crates/gloc/src/backend.rs]] - This file centralizes backend-specific model readiness for local inference, with a `ModelError` type for not-found, pull, warmup, and network failures. `ensure_model_ready` is the main entry point: it no-ops for non-Ollama backends, but for Ollama it checks whether a model is downloaded or loaded, optionally pulls missing models and warms them up based on settings, and propagates errors otherwise.

The helper functions split that workflow into smaller steps: `ollama_check_model` probes Ollama for model presence/load state, `ollama_pull_model` downloads missing models, `ollama_warmup_model` triggers loading, `model_name_matches` compares requested model names against Ollama metadata, and `unreachable_backend` represents a backend that cannot be contacted. The tests exercise the readiness path, backend failure handling, model-name matching rules, and `ModelError` formatting.
[crates/gloc/src/backend.rs:7-12]
[crates/gloc/src/backend.rs:14-23]
[crates/gloc/src/backend.rs:15-22]
[crates/gloc/src/backend.rs:28-62]
[crates/gloc/src/backend.rs:67-108]
- [[code/files/crates/gloc/src/config.rs|crates/gloc/src/config.rs]] - This file defines the gloc configuration schema and loading logic. `Config` groups settings, backend definitions, named client configs, and model aliases, while `Settings` and `Client` describe the per-section values and defaults used during serde deserialization.

The implementation ties those pieces together by loading a single YAML config through layered first-found-wins resolution, falling back to the compiled-in `DEFAULT_CONFIG` when needed. It also supports alias lookup, pretty dumping of the resolved config, template interpolation for backend/model placeholders, and tests that pin the built-in defaults and substitution behavior.
[crates/gloc/src/config.rs:13-22]
[crates/gloc/src/config.rs:25-32]
[crates/gloc/src/config.rs:34-42]
[crates/gloc/src/config.rs:35-41]
[crates/gloc/src/config.rs:44-46]
- [[code/files/crates/gloc/src/exec.rs|crates/gloc/src/exec.rs]] - This file provides the process-launching helpers for `gloc`: it resolves a client’s execution environment from backend/model templates, assembles command-line arguments from the model flag, defaults, and passthrough args, and locates binaries on `PATH`. `exec_client` ties those pieces together to run the configured client binary, using `exec()` on Unix and spawning a child process on non-Unix platforms, while the tests verify backend/client-specific env resolution, argument construction, env precedence, and binary lookup behavior.
[crates/gloc/src/exec.rs:9-21]
[crates/gloc/src/exec.rs:24-36]
[crates/gloc/src/exec.rs:39-45]
[crates/gloc/src/exec.rs:51-80]
[crates/gloc/src/exec.rs:87-94]
- [[code/files/crates/gloc/src/main.rs|crates/gloc/src/main.rs]] - `crates/gloc/src/main.rs` is the CLI entrypoint for `gloc`, a launcher that auto-detects local LLM backends and starts AI client tools. `Cli` defines flags for choosing a client, backend, model, backend URL override, config path, and control modes like `--init`, `--status`, and `--dump_config`, plus passthrough args for the target binary. `main` wires the flow together by handling early exits, loading config, optionally exporting a default config, resolving the active backend/client/model, printing status when requested, checking model readiness, and then continuing into execution. The helper functions keep that orchestration focused: `auto_export_config` writes a default home config on first run, `handle_init` initializes a project-local `.gobby/gloc.yaml`, `resolve_backend` and `resolve_client` select the runtime targets with validation and fallback behavior, `resolve_model` canonicalizes aliases, `print_status` reports the resolved setup, and the URL override helpers and backend constructor support backend selection and tests.
[crates/gloc/src/main.rs:16-52]
[crates/gloc/src/main.rs:54-118]
[crates/gloc/src/main.rs:120-130]
[crates/gloc/src/main.rs:132-155]
[crates/gloc/src/main.rs:157-202]

## Components

- `17e77151-ca44-58bc-9469-7f26e21f4719`
- `959f4302-6ec9-5693-892c-448fab92ce23`
- `7e263d52-5ed8-5422-a547-87a81d3649ac`
- `1550bb68-f95d-5cf7-9a78-634164f14e23`
- `c3153167-82c9-5ef3-a9f2-0b33df034b8c`
- `2e3be105-cdbe-547f-90a6-bbe2885de96b`
- `cd57587b-8493-53ba-bd7d-73e123d81762`
- `636cea91-7278-5e0b-a985-9e719e252bd3`
- `26bded03-836f-58c7-8409-c46953e9b282`
- `bc20d012-5207-57d8-87bf-b209fabb7988`
- `a381ca63-91a0-50da-b4d4-f9274138f5dd`
- `fb12b714-be3f-5221-a8ad-21e12c2d1c5d`
- `fb28a04e-5a8f-559a-afb2-f6d530ca292d`
- `8eb03b46-e5a9-5a2c-ad9b-f452fbfd72d1`
- `001d13de-e5d1-5ff5-8031-35b5d08aee92`
- `28f1c2a8-fc17-51ae-b0aa-c942e21f9368`
- `5e9f0915-50ce-5cfd-8e21-a853a3059467`
- `0b24632d-b0de-563d-bfad-d9c7a9df0df0`
- `e4aeb1b6-b112-5577-b443-865dcc440b2c`
- `40246c2c-bc9a-53d2-a5da-24858cd67e6d`
- `3b989843-c2da-541d-908d-cf57f4f3759e`
- `0de5951d-2ed3-58aa-905b-800fd4e0804b`
- `123761e3-1ee3-58ad-9298-11ac7b82103f`
- `89009b7e-536e-522d-a4a2-2cefee9baad0`
- `ec61d699-24de-5049-8e7c-7d3fc8ae4d8d`
- `c5648d9d-918e-5b51-bb23-0cca54761e20`
- `091f53fb-cba2-5931-97be-23ed133fd4f6`
- `46ea3e45-a48b-5c2e-8ee8-3ad64ca4ec71`
- `937f8cc4-e5c9-50b0-b78e-43ef155208aa`
- `883628f7-9a2a-501d-b753-d2f012eb13f4`
- `44b0a98a-f234-5970-930e-8d6b63632257`
- `e9157a4a-4997-5589-a5e0-83dcfbe964c4`
- `9f7d4a5d-dcf3-563e-8e93-c55f3e583936`
- `7c5ad7be-7a23-51c0-8b53-311a26d28f6c`
- `ac27f4f8-607c-55ab-99b8-671820619aef`
- `711eb0ad-3c1d-5bc1-8d21-6d5cd20cedfd`
- `ec49ad5a-88a9-5244-9fc7-cc709bd45c13`
- `1cb22630-78d7-5072-b82e-3c360e808f34`
- `c7ea4c03-f6f0-508d-beef-93a0dafc0afd`
- `2f955a74-2e66-5c22-ab0e-2bda34c868d8`
- `57e0bedf-06fb-5481-8bc0-306975e46e39`
- `71393741-4aa0-525f-b77a-083b99d45201`
- `40a6142a-2255-5000-b2bc-ed6d91bd0a5f`
- `2b08bf02-1815-51a3-b499-4039d8aa4d6d`
- `0055e704-44e7-59e6-b6b4-d15e258d8dd5`
- `5fd23c31-1ec9-5670-a964-8bc2b2f6ae6b`
- `ad501f95-e599-580e-a835-459e13800a47`
- `f1af90af-966b-593c-92fa-88ec6df56024`
- `5f667291-dbf4-517d-a474-fdd7b7d4dfce`
- `3ef29eda-b6d2-5dbe-b208-162ea81f5f20`
- `b5293d60-b85e-5a3f-a15c-3de280834d85`
- `44053d16-a034-5247-9e93-82f38395b494`
- `c0d554a5-0ee5-5ddb-bae2-cc4021fb3ed0`
- `b32f228a-fea3-57c7-bbaf-095136afd61e`
- `890d349c-d19a-5229-83bd-f48033ddab58`
- `3be65073-d21a-506e-b864-3d6c82092932`
- `67ae0308-2886-5c79-add5-274fc79c51f1`
- `1a718268-cb56-5f8f-9339-ce52e89cb9c9`
- `1e60195b-5788-5f91-b6e2-6d960a13ecfb`
- `cc9630db-6d87-5715-a8bb-40bcba35e833`
- `f5e0fd53-b4db-5238-86ec-8e1ec7a8a469`
- `95c344df-65d7-58ed-b08b-55450937a506`
- `5f69128c-734d-54b7-9151-c41113ec6264`
- `f7ac3ece-6fe9-57c8-a00d-dfb224d9db5d`
- `4f9b85cf-7812-598e-a21b-5c1368511d2f`
- `2679f7d7-f4bb-5c79-a06e-537fc750cf7c`
- `54307264-6cff-5244-af17-1dbc2b3602dd`
- `35e60a15-0461-5842-8f99-d112b9e7f80e`
- `dfb631c4-7c31-59e2-b1f4-fc716efe1cbd`
- `80170efa-b391-5bfd-bcc2-c818c6b3ec61`
- `67b18f9c-15b3-57c4-bd48-1761a0e4b1b9`
- `65a042fe-e2ee-5878-9e01-26b1c2f0a546`
- `a3d5db2c-8890-5b16-90da-6767d68c5e42`
- `c6062f0e-c3d4-5982-80a3-b19a5c29b2f9`
- `e9d0901f-58ab-5fda-bd04-0ef6e6da1942`
- `dae1b910-0dee-53fc-a051-bac36191b44b`
- `6f5b1fba-b61a-5d91-868f-c5bda190e3f3`

