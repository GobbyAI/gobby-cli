---
title: crates/gloc
type: code_module
provenance:
- file: crates/gloc/config.yaml
  ranges:
  - 11-17
  - '12'
  - '13'
  - '14'
  - 18-30
  - '19'
  - '20'
  - '21'
  - '22'
  - '24'
  - '25'
  - '26'
  - '27'
  - 31-53
  - 32-41
  - '33'
  - 34-37
  - '35'
  - '36'
  - '37'
  - '38'
  - '39'
  - '40'
  - '41'
  - 43-53
  - '44'
  - 45-47
  - '46'
  - '47'
  - '48'
  - '49'
  - '50'
  - '51'
  - 54-57
  - '55'
  - '56'
- file: crates/gloc/src/backend.rs
  ranges:
  - 7-12
  - 14-23
  - 15-22
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
  - 35-41
  - 44-46
  - 48-50
  - 53-65
  - 67-166
  - 70-88
  - 90-100
  - 102-117
  - 120-125
  - 128-159
  - 163-165
  - 170-176
  - 183-188
  - 191-196
  - 199-210
  - 213-217
  - 220-235
  - 238-247
  - 250-254
  - 257-260
  - 263-266
  - 269-278
  - 281-290
  - 293-302
  - 305-316
  - 319-327
  - 330-335
  - 338-345
  - 348-355
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
  - 54-123
  - 125-136
  - 138-161
  - 163-205
  - 207-232
  - 234-237
  - 239-270
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gloc

Parent: [[code/modules/crates|crates]]

## Overview

The `gloc` crate is a CLI tool that launches AI client binaries (e.g. Claude, Codex) against configurable LLM backends, including local Ollama models. It loads layered configuration (built-in defaults plus YAML overrides in `config.yaml`) defining backends, clients, model aliases, and settings such as probe timeouts and auto-load/pull behavior. Core responsibilities include resolving the active backend, client, and model (with template and alias expansion), building environment variables and command arguments, locating the target binary, and execing the client process. It also probes backend reachability and ensures Ollama models are present and warmed up before launch. A `main` entry point and `Cli` parser drive subcommands like init, status reporting, and config export, backed by an extensive unit test suite.
[crates/gloc/config.yaml:11-17]
[crates/gloc/src/backend.rs:7-12]
[crates/gloc/src/config.rs:13-22]
[crates/gloc/src/exec.rs:9-21]
[crates/gloc/src/main.rs:16-52]

## Child Modules

- [[code/modules/crates/gloc/src|crates/gloc/src]] - The `gloc` crate is a CLI tool that launches AI client binaries (e.g. Claude, Codex) against configurable LLM backends, including local Ollama models.

- **config.rs**: Defines the configuration model (`Config`, `Settings`, `Client`) with TOML loading (`load`, `try_load`, `load_or_exit`, `load_builtin`), alias resolution, template variable substitution, and config dumping. Provides defaults for probe timeouts and auto-load behavior.
- **backend.rs**: Manages Ollama model readiness via `ensure_model_ready`, including model existence checks, pulling, warmup, and name matching. Defines `ModelError` for failure reporting.
- **exec.rs**: Builds the execution environment and arguments for client processes, locates binaries (`which_binary`), and runs them (`exec_client`).
- **main.rs**: Entry point wiring the CLI (`Cli`, `main`), handling init, backend/client/model resolution, status reporting, and automatic config export.

Each file carries extensive unit tests covering config parsing, template resolution, env/arg construction, model matching, and backend validation.
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
- `1ca7c657-fd0e-526a-857b-2eca445f719b`
- `11880536-a723-50de-accb-ec46b5e68789`
- `e8915c05-78b6-51bf-b6f4-9807ea9616f2`
- `14c1e7aa-fa81-5f57-8123-4aaddcaccdac`
- `2801df61-3b74-5451-94f2-92579d68917f`
- `cdeb6423-fbd5-59e1-ba4a-e97c91fe6fb1`
- `4b437605-9873-5a6e-b484-6cad6b6310aa`
- `cbca34e6-8444-57c8-9ba1-a32e0818b04e`
- `0d424988-0203-56c1-ba0c-9e706a5f4a30`
- `c08aca9d-a7b3-555a-9ec0-5e5c65703cfb`
- `c2e6a01d-d40a-53a0-a091-106e834bafab`
- `97cf4d3f-ecfc-57c1-9ede-199a7b1891b9`
- `7f874d50-c295-5597-aea3-b431859f3931`
- `06a4c4b3-e6a9-5401-a000-d8439866d03e`
- `b01c369a-ed84-5408-9712-5553f83b9ad2`
- `f927f447-87d2-5b5f-bcf6-273687eb7cfd`
- `977cecda-12b9-5c6d-98cf-513eddffe657`
- `8677cf28-7bcd-5ecb-b423-987ef0315d20`
- `2f9bfc66-80a9-5c4b-ba32-8d9432fc8190`
- `06d0529f-e596-549c-bbd1-f788368ec7ab`
- `3c04ef55-d208-53a5-9262-f642a9163304`
- `c2874e82-2998-5f9a-88e7-7b7f14d171df`
- `7a2ed3f7-835c-5239-97e7-cd391c748e7b`
- `8958b812-3eed-53a5-a1f7-d7bf21c21b0d`
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
- `07d67fd3-b948-5071-81ec-e1c996f1540d`
- `13de0d74-9fef-5129-8312-e710e06ad480`
- `b9dfbc8b-4498-5ea8-8575-cf55b25ba00f`
- `8d8063b5-eafe-56f3-8b5c-321f14aa7c38`
- `b1969e2c-20cf-556d-9a13-e29bca435201`
- `0be47608-7312-5573-95db-138e4149e0de`

