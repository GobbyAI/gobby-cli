---
title: crates/ghook/schemas/diagnose-output.v2.schema.json
type: code_file
provenance:
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
  ranges:
  - 2-79
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/schemas/diagnose-output.v2.schema.json

Module: [[code/modules/crates/ghook/schemas|crates/ghook/schemas]]

## Purpose

Defines the draft-07 JSON Schema for `ghook --diagnose` output version 2. The schema names the document, fixes `schema_version` to `2`, and requires the core diagnostic fields that describe the installed `ghook` binary, the selected CLI/hook type, daemon connection details, whether the command is critical, and whether the CLI was recognized. It also allows optional contextual fields like `source`, project identifiers, and terminal preview data, while forbidding unknown properties. Version 2 extends the v1 shape with `install_method` and `install_source_url` so diagnose output can report install provenance from the sidecar metadata.
[crates/ghook/schemas/diagnose-output.v2.schema.json:2]
[crates/ghook/schemas/diagnose-output.v2.schema.json:3]
[crates/ghook/schemas/diagnose-output.v2.schema.json:4]
[crates/ghook/schemas/diagnose-output.v2.schema.json:5]
[crates/ghook/schemas/diagnose-output.v2.schema.json:6]

## API Symbols

- `$schema` (property) component `$schema [property]` (`bacf0899-0f32-5e82-a162-ce6ec065c665`) lines 2-2 [crates/ghook/schemas/diagnose-output.v2.schema.json:2]
  - Signature: `"$schema": "http://json-schema.org/draft-07/schema#",`
  - Purpose: Indexed property `$schema` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:2]
- `$id` (property) component `$id [property]` (`2098d2a7-1567-5d38-b7ff-aa501e6f20f2`) lines 3-3 [crates/ghook/schemas/diagnose-output.v2.schema.json:3]
  - Signature: `"$id": "https://gobby.ai/schemas/ghook/diagnose-output.v2.schema.json",`
  - Purpose: Indexed property `$id` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:3]
- `title` (property) component `title [property]` (`f4184134-2496-5da6-a6d3-148b09001802`) lines 4-4 [crates/ghook/schemas/diagnose-output.v2.schema.json:4]
  - Signature: `"title": "Gobby ghook --diagnose output",`
  - Purpose: Indexed property `title` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:4]
- `description` (property) component `description [property]` (`8c90ed26-3cbd-53ca-9b4e-85bbdf3a873c`) lines 5-5 [crates/ghook/schemas/diagnose-output.v2.schema.json:5]
  - Signature: ``"description": "Output of `ghook --diagnose --cli=<c> --type=<t>`. Schema version 2 — adds install_method and install_source_url for install-provenance reporting. v1 fields are unchanged.",``
  - Purpose: Indexed property `description` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:5]
- `type` (property) component `type [property]` (`3cfe478d-baf7-53af-adc4-6bc7073dd4d0`) lines 6-6 [crates/ghook/schemas/diagnose-output.v2.schema.json:6]
  - Signature: `"type": "object",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:6]
- `required` (property) component `required [property]` (`255c1c10-fb50-5c4c-ab0a-6fab53823622`) lines 7-18 [crates/ghook/schemas/diagnose-output.v2.schema.json:7-18]
  - Signature: `"required": [`
  - Purpose: Indexed property `required` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:7-18]
- `additionalProperties` (property) component `additionalProperties [property]` (`d32937c3-8cbc-5f70-ad2e-bc4163ff124e`) lines 19-19 [crates/ghook/schemas/diagnose-output.v2.schema.json:19]
  - Signature: `"additionalProperties": false,`
  - Purpose: Indexed property `additionalProperties` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:19]
- `properties` (property) component `properties [property]` (`0c90c2b2-0f3f-566e-9aad-5557d8397b0d`) lines 20-79 [crates/ghook/schemas/diagnose-output.v2.schema.json:20-79]
  - Signature: `"properties": {`
  - Purpose: Indexed property `properties` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:20-79]
- `schema_version` (property) component `schema_version [property]` (`98a0fbc5-cad9-5724-b8a8-bfcfdb872584`) lines 21-24 [crates/ghook/schemas/diagnose-output.v2.schema.json:21-24]
  - Signature: `"schema_version": {`
  - Purpose: Indexed property `schema_version` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:21-24]
- `type` (property) component `type [property]` (`efdb5996-ebcd-589c-87ea-a123854987bd`) lines 22-22 [crates/ghook/schemas/diagnose-output.v2.schema.json:22]
  - Signature: `"type": "integer",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:22]
- `const` (property) component `const [property]` (`c67570be-71bc-5b6f-9299-251552edf051`) lines 23-23 [crates/ghook/schemas/diagnose-output.v2.schema.json:23]
  - Signature: `"const": 2`
  - Purpose: Indexed property `const` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:23]
- `ghook_version` (property) component `ghook_version [property]` (`8fafacd4-4027-5f64-9cef-d0bcad3139ef`) lines 25-28 [crates/ghook/schemas/diagnose-output.v2.schema.json:25-28]
  - Signature: `"ghook_version": {`
  - Purpose: Indexed property `ghook_version` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:25-28]
- `type` (property) component `type [property]` (`e5d2730a-aa45-5bc2-9cd4-2f0c86147f53`) lines 26-26 [crates/ghook/schemas/diagnose-output.v2.schema.json:26]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:26]
- `minLength` (property) component `minLength [property]` (`cbfd1119-fdcd-5cb9-b25b-c0d75f68369c`) lines 27-27 [crates/ghook/schemas/diagnose-output.v2.schema.json:27]
  - Signature: `"minLength": 1`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:27]
- `cli` (property) component `cli [property]` (`edefea07-9c4f-5ee1-bce3-c7b7eeedf72b`) lines 29-32 [crates/ghook/schemas/diagnose-output.v2.schema.json:29-32]
  - Signature: `"cli": {`
  - Purpose: Indexed property `cli` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:29-32]
- `type` (property) component `type [property]` (`d1ff8a5a-bbe5-5f69-b911-5e7fef8a1931`) lines 30-30 [crates/ghook/schemas/diagnose-output.v2.schema.json:30]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:30]
- `minLength` (property) component `minLength [property]` (`37d3d038-bc2b-5c2e-a705-a374231a5cb7`) lines 31-31 [crates/ghook/schemas/diagnose-output.v2.schema.json:31]
  - Signature: `"minLength": 1`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:31]
- `hook_type` (property) component `hook_type [property]` (`d21d0c64-1768-5acc-b463-406be2d7b8c0`) lines 33-36 [crates/ghook/schemas/diagnose-output.v2.schema.json:33-36]
  - Signature: `"hook_type": {`
  - Purpose: Indexed property `hook_type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:33-36]
- `type` (property) component `type [property]` (`b828923e-0236-5616-a339-df5d5bff6830`) lines 34-34 [crates/ghook/schemas/diagnose-output.v2.schema.json:34]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:34]
- `minLength` (property) component `minLength [property]` (`2916f41a-c5bd-5505-9caa-4699aba07f02`) lines 35-35 [crates/ghook/schemas/diagnose-output.v2.schema.json:35]
  - Signature: `"minLength": 1`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:35]
- `source` (property) component `source [property]` (`b21f51e9-f548-56f9-9e5f-849c71b59944`) lines 37-39 [crates/ghook/schemas/diagnose-output.v2.schema.json:37-39]
  - Signature: `"source": {`
  - Purpose: Indexed property `source` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:37-39]
- `type` (property) component `type [property]` (`6eeef965-c316-5f6f-9013-c5977f691690`) lines 38-38 [crates/ghook/schemas/diagnose-output.v2.schema.json:38]
  - Signature: `"type": ["string", "null"]`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:38]
- `critical` (property) component `critical [property]` (`76db3b7a-3b7f-5c44-b510-8d1188beeb86`) lines 40-42 [crates/ghook/schemas/diagnose-output.v2.schema.json:40-42]
  - Signature: `"critical": {`
  - Purpose: Indexed property `critical` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:40-42]
- `type` (property) component `type [property]` (`cf36f950-0e73-5dab-8c96-914dbfcd31b1`) lines 41-41 [crates/ghook/schemas/diagnose-output.v2.schema.json:41]
  - Signature: `"type": "boolean"`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:41]
- `terminal_context_enabled` (property) component `terminal_context_enabled [property]` (`589bbd4a-9e7b-5a24-b1c0-7b9883f5c991`) lines 43-45 [crates/ghook/schemas/diagnose-output.v2.schema.json:43-45]
  - Signature: `"terminal_context_enabled": {`
  - Purpose: Indexed property `terminal_context_enabled` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:43-45]
- `type` (property) component `type [property]` (`d3d51a75-fcb5-5f99-be5d-0677d2587ec0`) lines 44-44 [crates/ghook/schemas/diagnose-output.v2.schema.json:44]
  - Signature: `"type": "boolean"`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:44]
- `daemon_url` (property) component `daemon_url [property]` (`25f7bffd-0360-59f1-bfe5-5a4224e27969`) lines 46-49 [crates/ghook/schemas/diagnose-output.v2.schema.json:46-49]
  - Signature: `"daemon_url": {`
  - Purpose: Indexed property `daemon_url` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:46-49]
- `type` (property) component `type [property]` (`239f3d50-c63a-5fa5-8ec9-b5e33b1d4cf6`) lines 47-47 [crates/ghook/schemas/diagnose-output.v2.schema.json:47]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:47]
- `minLength` (property) component `minLength [property]` (`61e5c980-5107-5b94-a255-dd30fff3256a`) lines 48-48 [crates/ghook/schemas/diagnose-output.v2.schema.json:48]
  - Signature: `"minLength": 1`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:48]
- `daemon_host` (property) component `daemon_host [property]` (`37e526c1-d0ad-56f2-8f84-459b34ac5abd`) lines 50-53 [crates/ghook/schemas/diagnose-output.v2.schema.json:50-53]
  - Signature: `"daemon_host": {`
  - Purpose: Indexed property `daemon_host` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:50-53]
- `type` (property) component `type [property]` (`4a698df5-5087-5ad1-ae48-a5fdde313a83`) lines 51-51 [crates/ghook/schemas/diagnose-output.v2.schema.json:51]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:51]
- `minLength` (property) component `minLength [property]` (`5a603945-bf8c-539f-8f27-535d8d4ff04e`) lines 52-52 [crates/ghook/schemas/diagnose-output.v2.schema.json:52]
  - Signature: `"minLength": 1`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:52]
- `daemon_port` (property) component `daemon_port [property]` (`d5d778e3-e1c0-57d3-b59d-5ceb5e9ac8a3`) lines 54-58 [crates/ghook/schemas/diagnose-output.v2.schema.json:54-58]
  - Signature: `"daemon_port": {`
  - Purpose: Indexed property `daemon_port` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:54-58]
- `type` (property) component `type [property]` (`f10afc11-7fd5-57b7-b234-eeef33756cfe`) lines 55-55 [crates/ghook/schemas/diagnose-output.v2.schema.json:55]
  - Signature: `"type": "integer",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:55]
- `minimum` (property) component `minimum [property]` (`3184bba7-db11-50eb-ace8-f4dd85fbb21d`) lines 56-56 [crates/ghook/schemas/diagnose-output.v2.schema.json:56]
  - Signature: `"minimum": 1,`
  - Purpose: Indexed property `minimum` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:56]
- `maximum` (property) component `maximum [property]` (`f3af8c8a-b418-5597-885b-db8fb9c1da05`) lines 57-57 [crates/ghook/schemas/diagnose-output.v2.schema.json:57]
  - Signature: `"maximum": 65535`
  - Purpose: Indexed property `maximum` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:57]
- `project_root` (property) component `project_root [property]` (`0f0d8050-a628-564e-9be3-33ac3c2f603e`) lines 59-61 [crates/ghook/schemas/diagnose-output.v2.schema.json:59-61]
  - Signature: `"project_root": {`
  - Purpose: Indexed property `project_root` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:59-61]
- `type` (property) component `type [property]` (`24560909-6e1a-5e14-8b72-4998c7ad0db0`) lines 60-60 [crates/ghook/schemas/diagnose-output.v2.schema.json:60]
  - Signature: `"type": ["string", "null"]`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:60]
- `project_id` (property) component `project_id [property]` (`e24a0919-9834-56da-a898-4d640d511e08`) lines 62-64 [crates/ghook/schemas/diagnose-output.v2.schema.json:62-64]
  - Signature: `"project_id": {`
  - Purpose: Indexed property `project_id` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:62-64]
- `type` (property) component `type [property]` (`85cd11d0-506d-549e-b640-bc1527518ee2`) lines 63-63 [crates/ghook/schemas/diagnose-output.v2.schema.json:63]
  - Signature: `"type": ["string", "null"]`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:63]
- `terminal_context_preview` (property) component `terminal_context_preview [property]` (`51fe7313-cece-5ccb-a29b-7e6cc6d2a9be`) lines 65-67 [crates/ghook/schemas/diagnose-output.v2.schema.json:65-67]
  - Signature: `"terminal_context_preview": {`
  - Purpose: Indexed property `terminal_context_preview` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:65-67]
- `type` (property) component `type [property]` (`43b83a6c-d9be-5131-96ab-eb1af64f1e5b`) lines 66-66 [crates/ghook/schemas/diagnose-output.v2.schema.json:66]
  - Signature: `"type": ["object", "null"]`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:66]
- `cli_recognized` (property) component `cli_recognized [property]` (`e0465c18-a77b-5c38-b139-77849c1f6929`) lines 68-70 [crates/ghook/schemas/diagnose-output.v2.schema.json:68-70]
  - Signature: `"cli_recognized": {`
  - Purpose: Indexed property `cli_recognized` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:68-70]
- `type` (property) component `type [property]` (`42985042-0643-5ae2-9fe0-c9d4bd1a6113`) lines 69-69 [crates/ghook/schemas/diagnose-output.v2.schema.json:69]
  - Signature: `"type": "boolean"`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:69]
- `install_method` (property) component `install_method [property]` (`dc946393-4886-50da-8a0a-351239f928ed`) lines 71-74 [crates/ghook/schemas/diagnose-output.v2.schema.json:71-74]
  - Signature: `"install_method": {`
  - Purpose: Indexed property `install_method` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:71-74]
- `type` (property) component `type [property]` (`322f6e90-7f84-5ff0-85c0-9e1d9eca8c9f`) lines 72-72 [crates/ghook/schemas/diagnose-output.v2.schema.json:72]
  - Signature: `"type": ["string", "null"],`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:72]
- `description` (property) component `description [property]` (`081c77c1-7c54-5af9-9e9e-a2a6f0045a44`) lines 73-73 [crates/ghook/schemas/diagnose-output.v2.schema.json:73]
  - Signature: `"description": "How ghook was installed, sourced from the install sidecar (.ghook-install.json) next to the binary. Conventional values: github-release, crates-binstall, cargo-install, manual, unknown...`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:73]
- `install_source_url` (property) component `install_source_url [property]` (`e935415a-1e52-589c-9ebb-ec2d584d1d71`) lines 75-78 [crates/ghook/schemas/diagnose-output.v2.schema.json:75-78]
  - Signature: `"install_source_url": {`
  - Purpose: Indexed property `install_source_url` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:75-78]
- `type` (property) component `type [property]` (`10ea730c-b509-535b-94d0-33d46f6e36d4`) lines 76-76 [crates/ghook/schemas/diagnose-output.v2.schema.json:76]
  - Signature: `"type": ["string", "null"],`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:76]
- `description` (property) component `description [property]` (`a7439602-0f19-534d-916b-65788e133a6a`) lines 77-77 [crates/ghook/schemas/diagnose-output.v2.schema.json:77]
  - Signature: `"description": "URL the binary was fetched from (typically a GitHub release asset URL), sourced from the install sidecar. null when unknown or not applicable."`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/diagnose-output.v2.schema.json`. [crates/ghook/schemas/diagnose-output.v2.schema.json:77]

