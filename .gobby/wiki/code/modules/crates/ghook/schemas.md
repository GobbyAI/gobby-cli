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

# crates/ghook/schemas

Parent: [[code/modules/crates/ghook|crates/ghook]]

## Overview

The `crates/ghook/schemas` module owns the JSON Schema contracts for ghook’s externally consumed structured data. One schema validates `ghook --diagnose` output as a draft-07 object with fixed metadata, required diagnostic fields, and no extra top-level properties, with version 2 explicitly adding install provenance while preserving the v1 field set . The other schema defines the v1 inbox envelope written by ghook for later daemon replay, likewise as a fixed-version object with required fields and `additionalProperties: false` .

The diagnostic flow captures runtime and configuration state for a host CLI invocation: ghook version, CLI name, hook type, criticality, terminal-context status, daemon URL/host/port, and whether the CLI was recognized are mandatory, while source, project context, terminal preview, and install provenance are nullable optional properties [crates/ghook/schemas/diagnose-output.v2.schema.json:21-79]. The port is constrained to the valid TCP range, required strings have minimum lengths, and install provenance is read from a sidecar when present, allowing consumers to distinguish known installer sources from unknown or absent metadata [crates/ghook/schemas/diagnose-output.v2.schema.json:47-78].

The inbox envelope flow preserves hook input for deferred processing: ghook records when the envelope was enqueued, whether failure should be critical to the host CLI, the hook type, the original stdin payload, the source CLI identifier, and headers mirroring the daemon request [crates/ghook/schemas/inbox-envelope.v1.schema.json:20-48]. The schema also standardizes optional project and session header names while allowing other non-empty string header values, so the daemon drain worker can replay envelopes with the same metadata shape ghook would have sent directly [crates/ghook/schemas/inbox-envelope.v1.schema.json:49-63].

## Files

- [[code/files/crates/ghook/schemas/diagnose-output.v2.schema.json|crates/ghook/schemas/diagnose-output.v2.schema.json]] - Defines the JSON Schema v2 for `ghook --diagnose` output, describing the structured object emitted by the CLI and pinning the schema metadata and version. It requires the core diagnostic fields, forbids extra properties, and validates each property’s shape and constraints, with v2 adding optional install provenance fields (`install_method` and `install_source_url`) while keeping the v1 output fields unchanged.
[crates/ghook/schemas/diagnose-output.v2.schema.json:2]
[crates/ghook/schemas/diagnose-output.v2.schema.json:3]
[crates/ghook/schemas/diagnose-output.v2.schema.json:4]
[crates/ghook/schemas/diagnose-output.v2.schema.json:5]
[crates/ghook/schemas/diagnose-output.v2.schema.json:6]
- [[code/files/crates/ghook/schemas/inbox-envelope.v1.schema.json|crates/ghook/schemas/inbox-envelope.v1.schema.json]] - Defines the JSON Schema for a v1 “Gobby ghook inbox envelope” written by `ghook` into `~/.gobby/hooks/inbox/` and later replayed by the daemon drain worker. It requires a fixed-version object with `schema_version`, `enqueued_at`, `critical`, `hook_type`, `input_data`, `source`, and `headers`, forbids extra top-level fields, and describes how the envelope carries the original stdin payload plus metadata like the enqueue timestamp, failure-critical flag, CLI/source identifier, and mirrored HTTP headers, including optional `X-Gobby-Project-Id` and `X-Gobby-Session-Id` values.
[crates/ghook/schemas/inbox-envelope.v1.schema.json:2]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:3]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:4]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:5]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:6]

## Components

- `bacf0899-0f32-5e82-a162-ce6ec065c665`
- `2098d2a7-1567-5d38-b7ff-aa501e6f20f2`
- `f4184134-2496-5da6-a6d3-148b09001802`
- `8c90ed26-3cbd-53ca-9b4e-85bbdf3a873c`
- `3cfe478d-baf7-53af-adc4-6bc7073dd4d0`
- `255c1c10-fb50-5c4c-ab0a-6fab53823622`
- `d32937c3-8cbc-5f70-ad2e-bc4163ff124e`
- `0c90c2b2-0f3f-566e-9aad-5557d8397b0d`
- `98a0fbc5-cad9-5724-b8a8-bfcfdb872584`
- `efdb5996-ebcd-589c-87ea-a123854987bd`
- `c67570be-71bc-5b6f-9299-251552edf051`
- `8fafacd4-4027-5f64-9cef-d0bcad3139ef`
- `e5d2730a-aa45-5bc2-9cd4-2f0c86147f53`
- `cbfd1119-fdcd-5cb9-b25b-c0d75f68369c`
- `edefea07-9c4f-5ee1-bce3-c7b7eeedf72b`
- `d1ff8a5a-bbe5-5f69-b911-5e7fef8a1931`
- `37d3d038-bc2b-5c2e-a705-a374231a5cb7`
- `d21d0c64-1768-5acc-b463-406be2d7b8c0`
- `b828923e-0236-5616-a339-df5d5bff6830`
- `2916f41a-c5bd-5505-9caa-4699aba07f02`
- `b21f51e9-f548-56f9-9e5f-849c71b59944`
- `6eeef965-c316-5f6f-9013-c5977f691690`
- `76db3b7a-3b7f-5c44-b510-8d1188beeb86`
- `cf36f950-0e73-5dab-8c96-914dbfcd31b1`
- `589bbd4a-9e7b-5a24-b1c0-7b9883f5c991`
- `d3d51a75-fcb5-5f99-be5d-0677d2587ec0`
- `25f7bffd-0360-59f1-bfe5-5a4224e27969`
- `239f3d50-c63a-5fa5-8ec9-b5e33b1d4cf6`
- `61e5c980-5107-5b94-a255-dd30fff3256a`
- `37e526c1-d0ad-56f2-8f84-459b34ac5abd`
- `4a698df5-5087-5ad1-ae48-a5fdde313a83`
- `5a603945-bf8c-539f-8f27-535d8d4ff04e`
- `d5d778e3-e1c0-57d3-b59d-5ceb5e9ac8a3`
- `f10afc11-7fd5-57b7-b234-eeef33756cfe`
- `3184bba7-db11-50eb-ace8-f4dd85fbb21d`
- `f3af8c8a-b418-5597-885b-db8fb9c1da05`
- `0f0d8050-a628-564e-9be3-33ac3c2f603e`
- `24560909-6e1a-5e14-8b72-4998c7ad0db0`
- `e24a0919-9834-56da-a898-4d640d511e08`
- `85cd11d0-506d-549e-b640-bc1527518ee2`
- `51fe7313-cece-5ccb-a29b-7e6cc6d2a9be`
- `43b83a6c-d9be-5131-96ab-eb1af64f1e5b`
- `e0465c18-a77b-5c38-b139-77849c1f6929`
- `42985042-0643-5ae2-9fe0-c9d4bd1a6113`
- `dc946393-4886-50da-8a0a-351239f928ed`
- `322f6e90-7f84-5ff0-85c0-9e1d9eca8c9f`
- `081c77c1-7c54-5af9-9e9e-a2a6f0045a44`
- `e935415a-1e52-589c-9ebb-ec2d584d1d71`
- `10ea730c-b509-535b-94d0-33d46f6e36d4`
- `a7439602-0f19-534d-916b-65788e133a6a`
- `17f7907d-c460-52fe-bb16-0881d8534d8c`
- `cd2dfa48-fffa-5667-984b-ed4eae020f3f`
- `0400aa16-fd74-5b9b-9cca-c6d79166d255`
- `970506da-8e5c-5ff3-935e-5df113530489`
- `6d3a4c21-424c-587c-bc52-646246a3e7a3`
- `fd16482c-1ae6-5e18-a20a-d9a2ed6023d5`
- `256f4bb0-7817-5dc9-91d8-e4eaf07a4848`
- `916907be-0c09-5cb6-8a64-dbb3fc3a2b55`
- `08b9293c-dfb0-58e7-8ab9-4ace41a3aa48`
- `9eca6f35-d514-504d-a338-ea47cfa63264`
- `f9ead96a-ca1f-5f39-9b50-d07ec066e15a`
- `ac91e290-83f5-544c-a35f-34ce3b332cf1`
- `2a1fe475-78a9-5c5d-93a2-83e30d26df45`
- `b9e238b5-812f-5777-806d-c6cee62da544`
- `7f92b363-4acc-586d-8b52-c7315b40c75b`
- `4cf38688-87f9-50c9-93e2-5f5c52cdb555`
- `497fcc0c-55d3-59d0-b5fd-42e04987d38a`
- `ab1d30ec-3a57-5a98-a71e-aa14de228a7f`
- `c72222f5-99ef-5a80-87ae-c9d32f04882f`
- `31abbb5a-8203-5c61-b443-a784c245431b`
- `502ba512-43a0-5bc6-8791-78572816ce9b`
- `9f9ca76c-562a-58c4-96b9-396610866190`
- `16c7f78f-4495-5139-af00-1c68e8f04de8`
- `1e19cd99-6a15-5ed5-830b-a541ab8e4dbe`
- `a2cf8456-f864-551c-88c5-5dcac06e9561`
- `60638bde-9f82-51ce-9cf7-3b713e417f67`
- `e4052035-d08f-5495-bde0-895c3acf7c20`
- `cf397469-b96c-5507-8101-526d2bf46f80`
- `1bdcbe2a-2822-5254-a6cb-76f704f5d736`
- `23078121-1b55-5e92-ad70-5576f50543ab`
- `9e25e883-fa17-5f32-98ea-54ad18ddc947`
- `7aa8a2d4-fa60-56f2-a078-11408f4d3ab0`
- `b1f865fc-a6cc-5b32-b765-35814437fcd0`
- `865a7d10-c395-5153-a43f-e081c88023c3`
- `1ac981d0-873b-51f4-a300-46137860a863`
- `41fbbe9f-07e6-52f8-aa6a-e4bc26dbc49d`
- `e098f112-7d6b-5651-9021-59e0c880cee0`
- `4333f09b-b80b-5fc3-8816-2115dd25a635`
- `4bcbc537-a256-5f80-9666-5dd823856785`
- `4c84adbb-080d-5e84-b68f-7fc8cdb1c46f`
- `4ee87c87-7c05-5386-a19c-f679ebe1748f`
- `b8a4d24c-2451-5980-ba93-8f4e6656b07d`

