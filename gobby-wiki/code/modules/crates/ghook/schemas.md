---
title: crates/ghook/schemas
type: code_module
provenance:
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
  ranges:
  - 2-79
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
  ranges:
  - 2-63
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/schemas/diagnose-output.v2.schema.json:2-79](crates/ghook/schemas/diagnose-output.v2.schema.json#L2-L79)
- [crates/ghook/schemas/inbox-envelope.v1.schema.json:2-63](crates/ghook/schemas/inbox-envelope.v1.schema.json#L2-L63)

</details>

# crates/ghook/schemas

Parent: [[code/modules/crates/ghook|crates/ghook]]

## Overview

The crates/ghook/schemas module defines structured JSON schemas that govern the diagnostics and queueing payloads of the ghook utility and Gobby background daemon [crates/ghook/schemas/diagnose-output.v2.schema.json:4, crates/ghook/schemas/inbox-envelope.v1.schema.json:4]. Key flows include the ghook --diagnose command, which relies on the diagnose-output schema to report binary health, install provenance, and daemon socket connectivity [crates/ghook/schemas/diagnose-output.v2.schema.json:4, 12-19], and standard ghook hook runs, which serializes and enqueues inbox-envelope payloads containing execution metadata and HTTP headers to ~/.gobby/hooks/inbox/ [crates/ghook/schemas/inbox-envelope.v1.schema.json:4]. These schemas act as the formal API contract between the ghook CLI and the daemon's asynchronous replay/drain worker [crates/ghook/schemas/inbox-envelope.v1.schema.json:4].

### Module Schemas
| Schema | Title | Target File Path | Version | Supporting Spans |
| --- | --- | --- | --- | --- |
| diagnose-output | Gobby ghook --diagnose output | crates/ghook/schemas/diagnose-output.v2.schema.json | 2 |  |
| inbox-envelope | Gobby ghook inbox envelope | crates/ghook/schemas/inbox-envelope.v1.schema.json | 1 |  |

### Command Line Flags
| Command / Flag | Description | Supporting Spans |
| --- | --- | --- |
| ghook --diagnose --cli=<c> --type=<t> | Formats diagnostic output mapping daemon state, binary versions, and install context | [crates/ghook/schemas/diagnose-output.v2.schema.json:4] |

### Envelope Header Fields
| Header | Description | Supporting Spans |
| --- | --- | --- |
| X-Gobby-Project-Id | Optional project identifier header sent to the daemon | [crates/ghook/schemas/inbox-envelope.v1.schema.json:52-56] |
| X-Gobby-Session-Id | Optional session identifier header sent to the daemon | [crates/ghook/schemas/inbox-envelope.v1.schema.json:57-61] |

### Install Provenance & Source Fields
| Field | Context / Enumerated Values | Supporting Spans |
| --- | --- | --- |
| install_method | Sourced from .ghook-install.json: github-release, crates-binstall, cargo-install, manual, unknown, null | [crates/ghook/schemas/diagnose-output.v2.schema.json:69-72] |
| install_source_url | Sourced from sidecar; typically a GitHub release asset URL, null | [crates/ghook/schemas/diagnose-output.v2.schema.json:73-76] |
| source (CLI source) | Sourced from host CLI: claude, codex, gemini, qwen, droid, grok | [crates/ghook/schemas/inbox-envelope.v1.schema.json:39-43] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/ghook/schemas/diagnose-output.v2.schema.json\|crates/ghook/schemas/diagnose-output.v2.schema.json]] | JSON Schema for `ghook --diagnose` output version 2. It defines a closed object shape with required runtime/status fields like `schema_version`, `ghook_version`, `cli`, `hook_type`, daemon details, and recognition flags, then constrains each property’s type and bounds; `schema_version` is fixed to `2`, `additionalProperties` is false, and v2 adds optional install provenance fields `install_method` and `install_source_url` while keeping the v1 fields unchanged. [crates/ghook/schemas/diagnose-output.v2.schema.json:2] [crates/ghook/schemas/diagnose-output.v2.schema.json:3] [crates/ghook/schemas/diagnose-output.v2.schema.json:4] [crates/ghook/schemas/diagnose-output.v2.schema.json:5] [crates/ghook/schemas/diagnose-output.v2.schema.json:6] |
| [[code/files/crates/ghook/schemas/inbox-envelope.v1.schema.json\|crates/ghook/schemas/inbox-envelope.v1.schema.json]] | Defines a JSON Schema v1 for a Gobby ghook inbox envelope: an object written by `ghook` into `~/.gobby/hooks/inbox/` and later replayed by the daemon drain worker. It requires `schema_version`, `enqueued_at`, `critical`, `hook_type`, `input_data`, `source`, and `headers`, forbids extra top-level fields, and constrains each field’s shape. The schema locks `schema_version` to `1`, requires an ISO-8601 UTC timestamp for `enqueued_at`, records whether the hook failure was critical, captures the hook name and original stdin payload, identifies the source CLI, and carries HTTP-style headers with optional `X-Gobby-Project-Id` and `X-Gobby-Session-Id` string values. [crates/ghook/schemas/inbox-envelope.v1.schema.json:2] [crates/ghook/schemas/inbox-envelope.v1.schema.json:3] [crates/ghook/schemas/inbox-envelope.v1.schema.json:4] [crates/ghook/schemas/inbox-envelope.v1.schema.json:5] [crates/ghook/schemas/inbox-envelope.v1.schema.json:6] |

## Components

| Component ID |
| --- |
| `bacf0899-0f32-5e82-a162-ce6ec065c665` |
| `2098d2a7-1567-5d38-b7ff-aa501e6f20f2` |
| `f4184134-2496-5da6-a6d3-148b09001802` |
| `8c90ed26-3cbd-53ca-9b4e-85bbdf3a873c` |
| `3cfe478d-baf7-53af-adc4-6bc7073dd4d0` |
| `255c1c10-fb50-5c4c-ab0a-6fab53823622` |
| `d32937c3-8cbc-5f70-ad2e-bc4163ff124e` |
| `0c90c2b2-0f3f-566e-9aad-5557d8397b0d` |
| `98a0fbc5-cad9-5724-b8a8-bfcfdb872584` |
| `efdb5996-ebcd-589c-87ea-a123854987bd` |
| `c67570be-71bc-5b6f-9299-251552edf051` |
| `8fafacd4-4027-5f64-9cef-d0bcad3139ef` |
| `e5d2730a-aa45-5bc2-9cd4-2f0c86147f53` |
| `cbfd1119-fdcd-5cb9-b25b-c0d75f68369c` |
| `edefea07-9c4f-5ee1-bce3-c7b7eeedf72b` |
| `d1ff8a5a-bbe5-5f69-b911-5e7fef8a1931` |
| `37d3d038-bc2b-5c2e-a705-a374231a5cb7` |
| `d21d0c64-1768-5acc-b463-406be2d7b8c0` |
| `b828923e-0236-5616-a339-df5d5bff6830` |
| `2916f41a-c5bd-5505-9caa-4699aba07f02` |
| `b21f51e9-f548-56f9-9e5f-849c71b59944` |
| `6eeef965-c316-5f6f-9013-c5977f691690` |
| `76db3b7a-3b7f-5c44-b510-8d1188beeb86` |
| `cf36f950-0e73-5dab-8c96-914dbfcd31b1` |
| `589bbd4a-9e7b-5a24-b1c0-7b9883f5c991` |
| `d3d51a75-fcb5-5f99-be5d-0677d2587ec0` |
| `25f7bffd-0360-59f1-bfe5-5a4224e27969` |
| `239f3d50-c63a-5fa5-8ec9-b5e33b1d4cf6` |
| `61e5c980-5107-5b94-a255-dd30fff3256a` |
| `37e526c1-d0ad-56f2-8f84-459b34ac5abd` |
| `4a698df5-5087-5ad1-ae48-a5fdde313a83` |
| `5a603945-bf8c-539f-8f27-535d8d4ff04e` |
| `d5d778e3-e1c0-57d3-b59d-5ceb5e9ac8a3` |
| `f10afc11-7fd5-57b7-b234-eeef33756cfe` |
| `3184bba7-db11-50eb-ace8-f4dd85fbb21d` |
| `f3af8c8a-b418-5597-885b-db8fb9c1da05` |
| `0f0d8050-a628-564e-9be3-33ac3c2f603e` |
| `24560909-6e1a-5e14-8b72-4998c7ad0db0` |
| `e24a0919-9834-56da-a898-4d640d511e08` |
| `85cd11d0-506d-549e-b640-bc1527518ee2` |
| `51fe7313-cece-5ccb-a29b-7e6cc6d2a9be` |
| `43b83a6c-d9be-5131-96ab-eb1af64f1e5b` |
| `e0465c18-a77b-5c38-b139-77849c1f6929` |
| `42985042-0643-5ae2-9fe0-c9d4bd1a6113` |
| `dc946393-4886-50da-8a0a-351239f928ed` |
| `322f6e90-7f84-5ff0-85c0-9e1d9eca8c9f` |
| `081c77c1-7c54-5af9-9e9e-a2a6f0045a44` |
| `e935415a-1e52-589c-9ebb-ec2d584d1d71` |
| `10ea730c-b509-535b-94d0-33d46f6e36d4` |
| `a7439602-0f19-534d-916b-65788e133a6a` |
| `17f7907d-c460-52fe-bb16-0881d8534d8c` |
| `cd2dfa48-fffa-5667-984b-ed4eae020f3f` |
| `0400aa16-fd74-5b9b-9cca-c6d79166d255` |
| `970506da-8e5c-5ff3-935e-5df113530489` |
| `6d3a4c21-424c-587c-bc52-646246a3e7a3` |
| `fd16482c-1ae6-5e18-a20a-d9a2ed6023d5` |
| `256f4bb0-7817-5dc9-91d8-e4eaf07a4848` |
| `916907be-0c09-5cb6-8a64-dbb3fc3a2b55` |
| `08b9293c-dfb0-58e7-8ab9-4ace41a3aa48` |
| `9eca6f35-d514-504d-a338-ea47cfa63264` |
| `f9ead96a-ca1f-5f39-9b50-d07ec066e15a` |
| `ac91e290-83f5-544c-a35f-34ce3b332cf1` |
| `2a1fe475-78a9-5c5d-93a2-83e30d26df45` |
| `b9e238b5-812f-5777-806d-c6cee62da544` |
| `7f92b363-4acc-586d-8b52-c7315b40c75b` |
| `4cf38688-87f9-50c9-93e2-5f5c52cdb555` |
| `497fcc0c-55d3-59d0-b5fd-42e04987d38a` |
| `ab1d30ec-3a57-5a98-a71e-aa14de228a7f` |
| `c72222f5-99ef-5a80-87ae-c9d32f04882f` |
| `31abbb5a-8203-5c61-b443-a784c245431b` |
| `502ba512-43a0-5bc6-8791-78572816ce9b` |
| `9f9ca76c-562a-58c4-96b9-396610866190` |
| `16c7f78f-4495-5139-af00-1c68e8f04de8` |
| `1e19cd99-6a15-5ed5-830b-a541ab8e4dbe` |
| `a2cf8456-f864-551c-88c5-5dcac06e9561` |
| `60638bde-9f82-51ce-9cf7-3b713e417f67` |
| `e4052035-d08f-5495-bde0-895c3acf7c20` |
| `cf397469-b96c-5507-8101-526d2bf46f80` |
| `1bdcbe2a-2822-5254-a6cb-76f704f5d736` |
| `808d8c3b-4873-5c04-b13a-792d19d563ee` |
| `87127e44-b830-5956-9c52-4a904d2b483c` |
| `a2c36e12-cc69-52fd-9484-2e40abdd2e95` |
| `16f46968-68bb-5695-afa6-25e951ccef80` |
| `37ddcdf6-6dbc-51eb-9a32-ebd5fa88a125` |
| `c89715a7-ee6a-541d-8e6b-199e336c6dc6` |
| `55185456-ca5b-5b3d-85f2-ce53af730792` |
| `d71a8a2e-05c3-57af-9d8c-a304e4301d28` |
| `44d01634-ec3c-57f6-887c-844d84544233` |
| `2800c802-fee6-50ea-a2b3-f0962a30c2a3` |
| `1099d1a5-f4b5-5b5f-90f6-dd94e3de9a51` |
| `b4a7ce41-e765-5bd6-a537-4ad71a5051af` |
| `560fb369-0f20-53d3-b9ae-07e219ced95b` |
