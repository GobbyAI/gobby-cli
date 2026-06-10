---
title: crates/ghook/schemas/inbox-envelope.v1.schema.json
type: code_file
provenance:
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
  ranges:
  - '2'
  - '3'
  - '4'
  - '5'
  - '6'
  - 7-15
  - '16'
  - 17-63
  - 18-22
  - '19'
  - '20'
  - '21'
  - 23-27
  - '24'
  - '25'
  - '26'
  - 28-31
  - '29'
  - '30'
  - 32-36
  - '33'
  - '34'
  - '35'
  - 37-39
  - '38'
  - 40-44
  - '41'
  - '42'
  - '43'
  - 45-62
  - '46'
  - '47'
  - 48-51
  - '49'
  - '50'
  - 52-61
  - 53-56
  - '54'
  - '55'
  - 57-60
  - '58'
  - '59'
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/schemas/inbox-envelope.v1.schema.json

Module: [[code/modules/crates/ghook/schemas|crates/ghook/schemas]]

## Purpose

`crates/ghook/schemas/inbox-envelope.v1.schema.json` exposes 42 indexed API symbols.
[crates/ghook/schemas/inbox-envelope.v1.schema.json:2]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:3]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:4]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:5]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:6]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:7-15]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:16]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:17-63]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:18-22]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:19]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:20]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:21]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:23-27]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:24]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:25]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:26]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:28-31]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:29]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:30]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:32-36]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:33]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:34]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:35]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:37-39]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:38]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:40-44]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:41]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:42]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:43]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:45-62]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:46]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:47]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:48-51]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:49]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:50]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:52-61]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:53-56]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:54]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:55]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:57-60]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:58]
[crates/ghook/schemas/inbox-envelope.v1.schema.json:59]

## API Symbols

- `$schema` (property) component `$schema [property]` (`17f7907d-c460-52fe-bb16-0881d8534d8c`) lines 2-2 [crates/ghook/schemas/inbox-envelope.v1.schema.json:2]
  - Signature: `"$schema": "http://json-schema.org/draft-07/schema#",`
  - Purpose: Indexed property `$schema` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:2]
- `$id` (property) component `$id [property]` (`cd2dfa48-fffa-5667-984b-ed4eae020f3f`) lines 3-3 [crates/ghook/schemas/inbox-envelope.v1.schema.json:3]
  - Signature: `"$id": "https://gobby.ai/schemas/ghook/inbox-envelope.v1.schema.json",`
  - Purpose: Indexed property `$id` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:3]
- `title` (property) component `title [property]` (`0400aa16-fd74-5b9b-9cca-c6d79166d255`) lines 4-4 [crates/ghook/schemas/inbox-envelope.v1.schema.json:4]
  - Signature: `"title": "Gobby ghook inbox envelope",`
  - Purpose: Indexed property `title` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:4]
- `description` (property) component `description [property]` (`970506da-8e5c-5ff3-935e-5df113530489`) lines 5-5 [crates/ghook/schemas/inbox-envelope.v1.schema.json:5]
  - Signature: `"description": "Envelope written by ghook to ~/.gobby/hooks/inbox/ and replayed by the daemon drain worker. Schema version 1.",`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:5]
- `type` (property) component `type [property]` (`6d3a4c21-424c-587c-bc52-646246a3e7a3`) lines 6-6 [crates/ghook/schemas/inbox-envelope.v1.schema.json:6]
  - Signature: `"type": "object",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:6]
- `required` (property) component `required [property]` (`fd16482c-1ae6-5e18-a20a-d9a2ed6023d5`) lines 7-15 [crates/ghook/schemas/inbox-envelope.v1.schema.json:7-15]
  - Signature: `"required": [`
  - Purpose: Indexed property `required` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:7-15]
- `additionalProperties` (property) component `additionalProperties [property]` (`256f4bb0-7817-5dc9-91d8-e4eaf07a4848`) lines 16-16 [crates/ghook/schemas/inbox-envelope.v1.schema.json:16]
  - Signature: `"additionalProperties": false,`
  - Purpose: Indexed property `additionalProperties` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:16]
- `properties` (property) component `properties [property]` (`916907be-0c09-5cb6-8a64-dbb3fc3a2b55`) lines 17-63 [crates/ghook/schemas/inbox-envelope.v1.schema.json:17-63]
  - Signature: `"properties": {`
  - Purpose: Indexed property `properties` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:17-63]
- `schema_version` (property) component `schema_version [property]` (`08b9293c-dfb0-58e7-8ab9-4ace41a3aa48`) lines 18-22 [crates/ghook/schemas/inbox-envelope.v1.schema.json:18-22]
  - Signature: `"schema_version": {`
  - Purpose: Indexed property `schema_version` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:18-22]
- `type` (property) component `type [property]` (`9eca6f35-d514-504d-a338-ea47cfa63264`) lines 19-19 [crates/ghook/schemas/inbox-envelope.v1.schema.json:19]
  - Signature: `"type": "integer",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:19]
- `const` (property) component `const [property]` (`f9ead96a-ca1f-5f39-9b50-d07ec066e15a`) lines 20-20 [crates/ghook/schemas/inbox-envelope.v1.schema.json:20]
  - Signature: `"const": 1,`
  - Purpose: Indexed property `const` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:20]
- `description` (property) component `description [property]` (`ac91e290-83f5-544c-a35f-34ce3b332cf1`) lines 21-21 [crates/ghook/schemas/inbox-envelope.v1.schema.json:21]
  - Signature: `"description": "Envelope schema version; consumers must reject unknown versions."`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:21]
- `enqueued_at` (property) component `enqueued_at [property]` (`2a1fe475-78a9-5c5d-93a2-83e30d26df45`) lines 23-27 [crates/ghook/schemas/inbox-envelope.v1.schema.json:23-27]
  - Signature: `"enqueued_at": {`
  - Purpose: Indexed property `enqueued_at` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:23-27]
- `type` (property) component `type [property]` (`b9e238b5-812f-5777-806d-c6cee62da544`) lines 24-24 [crates/ghook/schemas/inbox-envelope.v1.schema.json:24]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:24]
- `format` (property) component `format [property]` (`7f92b363-4acc-586d-8b52-c7315b40c75b`) lines 25-25 [crates/ghook/schemas/inbox-envelope.v1.schema.json:25]
  - Signature: `"format": "date-time",`
  - Purpose: Indexed property `format` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:25]
- `description` (property) component `description [property]` (`4cf38688-87f9-50c9-93e2-5f5c52cdb555`) lines 26-26 [crates/ghook/schemas/inbox-envelope.v1.schema.json:26]
  - Signature: `"description": "ISO-8601 UTC timestamp when ghook enqueued this envelope."`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:26]
- `critical` (property) component `critical [property]` (`497fcc0c-55d3-59d0-b5fd-42e04987d38a`) lines 28-31 [crates/ghook/schemas/inbox-envelope.v1.schema.json:28-31]
  - Signature: `"critical": {`
  - Purpose: Indexed property `critical` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:28-31]
- `type` (property) component `type [property]` (`ab1d30ec-3a57-5a98-a71e-aa14de228a7f`) lines 29-29 [crates/ghook/schemas/inbox-envelope.v1.schema.json:29]
  - Signature: `"type": "boolean",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:29]
- `description` (property) component `description [property]` (`c72222f5-99ef-5a80-87ae-c9d32f04882f`) lines 30-30 [crates/ghook/schemas/inbox-envelope.v1.schema.json:30]
  - Signature: `"description": "When true, ghook exited 2 on failure to signal the host CLI."`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:30]
- `hook_type` (property) component `hook_type [property]` (`31abbb5a-8203-5c61-b443-a784c245431b`) lines 32-36 [crates/ghook/schemas/inbox-envelope.v1.schema.json:32-36]
  - Signature: `"hook_type": {`
  - Purpose: Indexed property `hook_type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:32-36]
- `type` (property) component `type [property]` (`502ba512-43a0-5bc6-8791-78572816ce9b`) lines 33-33 [crates/ghook/schemas/inbox-envelope.v1.schema.json:33]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:33]
- `minLength` (property) component `minLength [property]` (`9f9ca76c-562a-58c4-96b9-396610866190`) lines 34-34 [crates/ghook/schemas/inbox-envelope.v1.schema.json:34]
  - Signature: `"minLength": 1,`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:34]
- `description` (property) component `description [property]` (`16c7f78f-4495-5139-af00-1c68e8f04de8`) lines 35-35 [crates/ghook/schemas/inbox-envelope.v1.schema.json:35]
  - Signature: `"description": "Host-CLI-specific hook name (e.g. session-start, SessionStart, PreToolUse)."`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:35]
- `input_data` (property) component `input_data [property]` (`1e19cd99-6a15-5ed5-830b-a541ab8e4dbe`) lines 37-39 [crates/ghook/schemas/inbox-envelope.v1.schema.json:37-39]
  - Signature: `"input_data": {`
  - Purpose: Indexed property `input_data` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:37-39]
- `description` (property) component `description [property]` (`a2cf8456-f864-551c-88c5-5dcac06e9561`) lines 38-38 [crates/ghook/schemas/inbox-envelope.v1.schema.json:38]
  - Signature: `"description": "Original stdin payload from the host CLI, optionally enriched with a terminal_context object when valid tmux pane context is available."`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:38]
- `source` (property) component `source [property]` (`60638bde-9f82-51ce-9cf7-3b713e417f67`) lines 40-44 [crates/ghook/schemas/inbox-envelope.v1.schema.json:40-44]
  - Signature: `"source": {`
  - Purpose: Indexed property `source` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:40-44]
- `type` (property) component `type [property]` (`e4052035-d08f-5495-bde0-895c3acf7c20`) lines 41-41 [crates/ghook/schemas/inbox-envelope.v1.schema.json:41]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:41]
- `minLength` (property) component `minLength [property]` (`cf397469-b96c-5507-8101-526d2bf46f80`) lines 42-42 [crates/ghook/schemas/inbox-envelope.v1.schema.json:42]
  - Signature: `"minLength": 1,`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:42]
- `description` (property) component `description [property]` (`1bdcbe2a-2822-5254-a6cb-76f704f5d736`) lines 43-43 [crates/ghook/schemas/inbox-envelope.v1.schema.json:43]
  - Signature: `"description": "Source CLI identifier passed to the daemon (claude, codex, gemini, qwen, droid)."`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:43]
- `headers` (property) component `headers [property]` (`23078121-1b55-5e92-ad70-5576f50543ab`) lines 45-62 [crates/ghook/schemas/inbox-envelope.v1.schema.json:45-62]
  - Signature: `"headers": {`
  - Purpose: Indexed property `headers` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:45-62]
- `type` (property) component `type [property]` (`9e25e883-fa17-5f32-98ea-54ad18ddc947`) lines 46-46 [crates/ghook/schemas/inbox-envelope.v1.schema.json:46]
  - Signature: `"type": "object",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:46]
- `description` (property) component `description [property]` (`7aa8a2d4-fa60-56f2-a078-11408f4d3ab0`) lines 47-47 [crates/ghook/schemas/inbox-envelope.v1.schema.json:47]
  - Signature: `"description": "HTTP headers mirroring what ghook sent (or would have sent) to the daemon. Omitted headers are absent keys; empty-string values are never emitted.",`
  - Purpose: Indexed property `description` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:47]
- `additionalProperties` (property) component `additionalProperties [property]` (`b1f865fc-a6cc-5b32-b765-35814437fcd0`) lines 48-51 [crates/ghook/schemas/inbox-envelope.v1.schema.json:48-51]
  - Signature: `"additionalProperties": {`
  - Purpose: Indexed property `additionalProperties` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:48-51]
- `type` (property) component `type [property]` (`865a7d10-c395-5153-a43f-e081c88023c3`) lines 49-49 [crates/ghook/schemas/inbox-envelope.v1.schema.json:49]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:49]
- `minLength` (property) component `minLength [property]` (`1ac981d0-873b-51f4-a300-46137860a863`) lines 50-50 [crates/ghook/schemas/inbox-envelope.v1.schema.json:50]
  - Signature: `"minLength": 1`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:50]
- `properties` (property) component `properties [property]` (`41fbbe9f-07e6-52f8-aa6a-e4bc26dbc49d`) lines 52-61 [crates/ghook/schemas/inbox-envelope.v1.schema.json:52-61]
  - Signature: `"properties": {`
  - Purpose: Indexed property `properties` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:52-61]
- `X-Gobby-Project-Id` (property) component `X-Gobby-Project-Id [property]` (`e098f112-7d6b-5651-9021-59e0c880cee0`) lines 53-56 [crates/ghook/schemas/inbox-envelope.v1.schema.json:53-56]
  - Signature: `"X-Gobby-Project-Id": {`
  - Purpose: Indexed property `X-Gobby-Project-Id` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:53-56]
- `type` (property) component `type [property]` (`4333f09b-b80b-5fc3-8816-2115dd25a635`) lines 54-54 [crates/ghook/schemas/inbox-envelope.v1.schema.json:54]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:54]
- `minLength` (property) component `minLength [property]` (`4bcbc537-a256-5f80-9666-5dd823856785`) lines 55-55 [crates/ghook/schemas/inbox-envelope.v1.schema.json:55]
  - Signature: `"minLength": 1`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:55]
- `X-Gobby-Session-Id` (property) component `X-Gobby-Session-Id [property]` (`4c84adbb-080d-5e84-b68f-7fc8cdb1c46f`) lines 57-60 [crates/ghook/schemas/inbox-envelope.v1.schema.json:57-60]
  - Signature: `"X-Gobby-Session-Id": {`
  - Purpose: Indexed property `X-Gobby-Session-Id` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:57-60]
- `type` (property) component `type [property]` (`4ee87c87-7c05-5386-a19c-f679ebe1748f`) lines 58-58 [crates/ghook/schemas/inbox-envelope.v1.schema.json:58]
  - Signature: `"type": "string",`
  - Purpose: Indexed property `type` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:58]
- `minLength` (property) component `minLength [property]` (`b8a4d24c-2451-5980-ba93-8f4e6656b07d`) lines 59-59 [crates/ghook/schemas/inbox-envelope.v1.schema.json:59]
  - Signature: `"minLength": 1`
  - Purpose: Indexed property `minLength` in `crates/ghook/schemas/inbox-envelope.v1.schema.json`. [crates/ghook/schemas/inbox-envelope.v1.schema.json:59]

