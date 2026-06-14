---
title: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json
type: code_file
provenance:
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json
  ranges:
  - 3-47
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json

Module: [[code/modules/docs/evidence/wiki-parity-2026-06|docs/evidence/wiki-parity-2026-06]]

## Purpose

Records the result of a `gwiki compile` run for the wiki-parity task, tying a resolved project scope to the generated article and its supporting index/source writes. The `ai` block captures the daemon-synthesized compilation metadata, while `command`, `handoff_id`, `outline`, `page_writes`, `article_path`, and `index_path` show what was compiled and where the output landed. The nested `prompt` and `scope` fields document the requested explainer format, token estimate, source coverage, and source path set used to generate the final wiki page.
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:5]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:6]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:7]

## API Symbols

- `ai` (property) component `ai [property]` (`39461b11-e8ef-5781-b6cf-cf5d8926739d`) lines 3-12 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
  - Signature: `"ai": {`
  - Purpose: Indexed property `ai` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
- `citations_kept` (property) component `citations_kept [property]` (`e0eb2ba5-aea5-591a-9412-8390d4f264f5`) lines 4-4 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:4]
  - Signature: `"citations_kept": 6,`
  - Purpose: Indexed property `citations_kept` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:4]
- `citations_stripped` (property) component `citations_stripped [property]` (`1cddca69-c198-5a13-8f62-9d15dfb454c9`) lines 5-5 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:5]
  - Signature: `"citations_stripped": 0,`
  - Purpose: Indexed property `citations_stripped` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:5]
- `error` (property) component `error [property]` (`d7d0b8ba-1749-5e3f-bb7a-d48a817dfda0`) lines 6-6 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:6]
  - Signature: `"error": null,`
  - Purpose: Indexed property `error` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:6]
- `fallback_sections` (property) component `fallback_sections [property]` (`e37f0651-8cd9-571d-a2c8-0a8b897a87b0`) lines 7-7 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:7]
  - Signature: `"fallback_sections": 0,`
  - Purpose: Indexed property `fallback_sections` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:7]
- `model` (property) component `model [property]` (`d87b3229-4d10-54a9-9d56-a50f0b84506e`) lines 8-8 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:8]
  - Signature: `"model": "haiku",`
  - Purpose: Indexed property `model` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:8]
- `requested_mode` (property) component `requested_mode [property]` (`7daed047-73de-5a94-8781-498e91004172`) lines 9-9 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:9]
  - Signature: `"requested_mode": "daemon",`
  - Purpose: Indexed property `requested_mode` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:9]
- `route` (property) component `route [property]` (`6313a0f7-198b-5efa-b2e2-b2e1046c386c`) lines 10-10 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:10]
  - Signature: `"route": "daemon",`
  - Purpose: Indexed property `route` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:10]
- `status` (property) component `status [property]` (`43041662-59a9-5c67-814d-02ec81b2957b`) lines 11-11 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:11]
  - Signature: `"status": "generated"`
  - Purpose: Indexed property `status` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:11]
- `article_path` (property) component `article_path [property]` (`7f88a36d-fee9-5180-8980-633e032b9d6d`) lines 13-13 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:13]
  - Signature: `"article_path": "/Users/josh/Projects/gobby-cli/.gobby/wiki/knowledge/topics/gsqz-compression-shipping-decision.md",`
  - Purpose: Indexed property `article_path` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:13]
- `command` (property) component `command [property]` (`7601c43d-fd24-521a-94a5-cb92cba92af7`) lines 14-14 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:14]
  - Signature: `"command": "compile",`
  - Purpose: Indexed property `command` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:14]
- `daemon_synthesis_available` (property) component `daemon_synthesis_available [property]` (`24f8f6dd-1d92-5d8a-9576-898f9ca1ed59`) lines 15-15 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:15]
  - Signature: `"daemon_synthesis_available": true,`
  - Purpose: Indexed property `daemon_synthesis_available` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:15]
- `handoff_id` (property) component `handoff_id [property]` (`b70134f2-4ef0-5827-8238-53768bbb6d59`) lines 16-16 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:16]
  - Signature: `"handoff_id": "compile-gsqz-compression-shipping-decision-1781313357326",`
  - Purpose: Indexed property `handoff_id` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:16]
- `index_path` (property) component `index_path [property]` (`c08d03cb-8da7-5cdc-9dd0-4fd2808704d3`) lines 17-17 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:17]
  - Signature: `"index_path": "/Users/josh/Projects/gobby-cli/.gobby/wiki/_index.md",`
  - Purpose: Indexed property `index_path` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:17]
- `outline` (property) component `outline [property]` (`4c1f1f13-0893-5f50-b3ff-79654033ed57`) lines 18-21 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:18-21]
  - Signature: `"outline": [`
  - Purpose: Indexed property `outline` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:18-21]
- `page_writes` (property) component `page_writes [property]` (`25edd7d6-d82c-5da7-8662-dbcbf154c88d`) lines 22-31 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:22-31]
  - Signature: `"page_writes": [`
  - Purpose: Indexed property `page_writes` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:22-31]
- `kind` (property) component `kind [property]` (`1f73b2e8-0d88-5fc5-ab55-31790458e445`) lines 24-24 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:24]
  - Signature: `"kind": "created",`
  - Purpose: Indexed property `kind` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:24]
- `path` (property) component `path [property]` (`80db9cde-e37c-5097-8bb4-dcd5ade0b7c3`) lines 25-25 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:25]
  - Signature: `"path": "/Users/josh/Projects/gobby-cli/.gobby/wiki/knowledge/topics/gsqz-compression-shipping-decision.md"`
  - Purpose: Indexed property `path` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:25]
- `kind` (property) component `kind [property]` (`b1a24ee9-7df2-5c02-ad92-53477234ed0f`) lines 28-28 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:28]
  - Signature: `"kind": "created",`
  - Purpose: Indexed property `kind` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:28]
- `path` (property) component `path [property]` (`63777d74-62e7-54e4-b490-fbfbf8106380`) lines 29-29 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:29]
  - Signature: `"path": "/Users/josh/Projects/gobby-cli/.gobby/wiki/knowledge/sources/how-gsqz-decides-whether-compressed-output-ships.md"`
  - Purpose: Indexed property `path` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:29]
- `prompt` (property) component `prompt [property]` (`b5ddd8c5-3c0a-5581-9866-09bd3439967d`) lines 32-38 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:32-38]
  - Signature: `"prompt": {`
  - Purpose: Indexed property `prompt` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:32-38]
- `daemon_synthesis_available` (property) component `daemon_synthesis_available [property]` (`da06ba6f-35f1-5068-b8c3-462c8d5a2f34`) lines 33-33 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:33]
  - Signature: `"daemon_synthesis_available": true,`
  - Purpose: Indexed property `daemon_synthesis_available` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:33]
- `system` (property) component `system [property]` (`4aa87082-b97f-5063-8daf-c461e9c88cac`) lines 34-34 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:34]
  - Signature: `"system": "You write a grounded wiki explainer from supplied source excerpts. Use only facts stated in the excerpts. Write each requested section as a markdown '## <section>' heading followed by one o...`
  - Purpose: Indexed property `system` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:34]
- `tokens_estimated` (property) component `tokens_estimated [property]` (`c852e05d-e930-572c-92d2-03174a1ef0b4`) lines 35-35 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:35]
  - Signature: `"tokens_estimated": 550,`
  - Purpose: Indexed property `tokens_estimated` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:35]
- `truncated_sources` (property) component `truncated_sources [property]` (`d3b8af24-bb88-56af-bc07-08b0894b0ea4`) lines 36-36 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:36]
  - Signature: `"truncated_sources": 0,`
  - Purpose: Indexed property `truncated_sources` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:36]
- `user` (property) component `user [property]` (`9d61ccae-28d7-5720-a28d-db55d161e658`) lines 37-37 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:37]
  - Signature: `"user": "Topic: gsqz compression shipping decision\nWrite the explainer with exactly these sections:\n- Overview\n- Shipping thresholds\n\nSource excerpts:\n1. How gsqz decides whether compressed outp...`
  - Purpose: Indexed property `user` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:37]
- `scope` (property) component `scope [property]` (`ace3d794-89ad-533a-a7a3-951c80702798`) lines 39-42 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:39-42]
  - Signature: `"scope": {`
  - Purpose: Indexed property `scope` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:39-42]
- `id` (property) component `id [property]` (`3b2d1f35-998f-55b8-9ae3-160c56a02045`) lines 40-40 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:40]
  - Signature: `"id": "3bf57fe7-2a0c-4074-8912-a83d9cd4df01",`
  - Purpose: Indexed property `id` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:40]
- `kind` (property) component `kind [property]` (`7ba31266-a20a-5a10-bae0-a5786c5e9e7b`) lines 41-41 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:41]
  - Signature: `"kind": "project"`
  - Purpose: Indexed property `kind` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:41]
- `source_paths` (property) component `source_paths [property]` (`bf026c56-8963-5293-8d8d-c25317c4132b`) lines 43-45 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:43-45]
  - Signature: `"source_paths": [`
  - Purpose: Indexed property `source_paths` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:43-45]
- `status` (property) component `status [property]` (`3a8d6e39-d6c4-59d9-93b8-e66d3e62f261`) lines 46-46 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:46]
  - Signature: `"status": "compiled",`
  - Purpose: Indexed property `status` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:46]
- `target_kind` (property) component `target_kind [property]` (`f8c0b405-61c0-5912-bde8-3ee43732cf2b`) lines 47-47 [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:47]
  - Signature: `"target_kind": "topic"`
  - Purpose: Indexed property `target_kind` in `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json`. [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:47]

