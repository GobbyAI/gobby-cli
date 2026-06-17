---
title: crates/gwiki/src/audit
type: code_module
provenance:
- file: crates/gwiki/src/audit/claims.rs
  ranges:
  - 15-44
  - 46-55
  - 57-62
  - 64-73
  - 75-80
  - 82-98
  - 100-106
  - 108-145
  - 148-153
  - 156-159
  - 166-243
  - 245-251
  - 253-262
  - 264-268
  - 270-272
  - 274-281
  - 283-295
  - 297-305
  - 307-320
  - 322-327
  - 329-334
  - 336-347
  - 349-371
- file: crates/gwiki/src/audit/render.rs
  ranges:
  - 3-32
- file: crates/gwiki/src/audit/tests.rs
  ranges:
  - 14-48
  - 51-117
  - 120-145
  - 148-174
  - 177-196
  - 199-219
  - 222-230
  - 233-246
  - 249-286
  - 289-296
  - 299-328
  - 331-384
  - 386-395
  - 398-417
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/audit/claims.rs:15-44](crates/gwiki/src/audit/claims.rs#L15-L44), [crates/gwiki/src/audit/claims.rs:46-55](crates/gwiki/src/audit/claims.rs#L46-L55), [crates/gwiki/src/audit/claims.rs:57-62](crates/gwiki/src/audit/claims.rs#L57-L62), [crates/gwiki/src/audit/claims.rs:64-73](crates/gwiki/src/audit/claims.rs#L64-L73), [crates/gwiki/src/audit/claims.rs:75-80](crates/gwiki/src/audit/claims.rs#L75-L80), [crates/gwiki/src/audit/claims.rs:82-98](crates/gwiki/src/audit/claims.rs#L82-L98), [crates/gwiki/src/audit/claims.rs:100-106](crates/gwiki/src/audit/claims.rs#L100-L106), [crates/gwiki/src/audit/claims.rs:108-145](crates/gwiki/src/audit/claims.rs#L108-L145), [crates/gwiki/src/audit/claims.rs:148-153](crates/gwiki/src/audit/claims.rs#L148-L153), [crates/gwiki/src/audit/claims.rs:156-159](crates/gwiki/src/audit/claims.rs#L156-L159), [crates/gwiki/src/audit/claims.rs:166-243](crates/gwiki/src/audit/claims.rs#L166-L243), [crates/gwiki/src/audit/claims.rs:245-251](crates/gwiki/src/audit/claims.rs#L245-L251), [crates/gwiki/src/audit/claims.rs:253-262](crates/gwiki/src/audit/claims.rs#L253-L262), [crates/gwiki/src/audit/claims.rs:264-268](crates/gwiki/src/audit/claims.rs#L264-L268), [crates/gwiki/src/audit/claims.rs:270-272](crates/gwiki/src/audit/claims.rs#L270-L272), [crates/gwiki/src/audit/claims.rs:274-281](crates/gwiki/src/audit/claims.rs#L274-L281), [crates/gwiki/src/audit/claims.rs:283-295](crates/gwiki/src/audit/claims.rs#L283-L295), [crates/gwiki/src/audit/claims.rs:297-305](crates/gwiki/src/audit/claims.rs#L297-L305), [crates/gwiki/src/audit/claims.rs:307-320](crates/gwiki/src/audit/claims.rs#L307-L320), [crates/gwiki/src/audit/claims.rs:322-327](crates/gwiki/src/audit/claims.rs#L322-L327), [crates/gwiki/src/audit/claims.rs:329-334](crates/gwiki/src/audit/claims.rs#L329-L334), [crates/gwiki/src/audit/claims.rs:336-347](crates/gwiki/src/audit/claims.rs#L336-L347), [crates/gwiki/src/audit/claims.rs:349-371](crates/gwiki/src/audit/claims.rs#L349-L371)
- [crates/gwiki/src/audit/render.rs:3-32](crates/gwiki/src/audit/render.rs#L3-L32)
- [crates/gwiki/src/audit/tests.rs:14-48](crates/gwiki/src/audit/tests.rs#L14-L48), [crates/gwiki/src/audit/tests.rs:51-117](crates/gwiki/src/audit/tests.rs#L51-L117), [crates/gwiki/src/audit/tests.rs:120-145](crates/gwiki/src/audit/tests.rs#L120-L145), [crates/gwiki/src/audit/tests.rs:148-174](crates/gwiki/src/audit/tests.rs#L148-L174), [crates/gwiki/src/audit/tests.rs:177-196](crates/gwiki/src/audit/tests.rs#L177-L196), [crates/gwiki/src/audit/tests.rs:199-219](crates/gwiki/src/audit/tests.rs#L199-L219), [crates/gwiki/src/audit/tests.rs:222-230](crates/gwiki/src/audit/tests.rs#L222-L230), [crates/gwiki/src/audit/tests.rs:233-246](crates/gwiki/src/audit/tests.rs#L233-L246), [crates/gwiki/src/audit/tests.rs:249-286](crates/gwiki/src/audit/tests.rs#L249-L286), [crates/gwiki/src/audit/tests.rs:289-296](crates/gwiki/src/audit/tests.rs#L289-L296), [crates/gwiki/src/audit/tests.rs:299-328](crates/gwiki/src/audit/tests.rs#L299-L328), [crates/gwiki/src/audit/tests.rs:331-384](crates/gwiki/src/audit/tests.rs#L331-L384), [crates/gwiki/src/audit/tests.rs:386-395](crates/gwiki/src/audit/tests.rs#L386-L395), [crates/gwiki/src/audit/tests.rs:398-417](crates/gwiki/src/audit/tests.rs#L398-L417)

</details>

# crates/gwiki/src/audit

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

The `crates/gwiki/src/audit` module is responsible for analyzing wiki pages to verify their claim provenance and rendering human-readable plain-text audit reports. The core flow is driven by evaluating wiki page claims against the `ProvenanceGraph`, frontmatter configuration, and inline citations to identify claim lines that lack acceptable provenance and report them as `UnsupportedClaim`s [crates/gwiki/src/audit/claims.rs:15-44]. The module collaborates directly with Markdown page representations (`WikiPage`) and provenance structures, applying special-case rules to generated codewiki pages to ensure they do not inherit raw source contexts .

Once the audit pipeline evaluates the pages, the module formats the resulting `AuditReport` using a plain-text renderer. The `render_text` function builds a clean, structured summary highlighting the audit's scope and listing each unsupported claim with its exact file path, line number, claim text, and optional source IDs [crates/gwiki/src/audit/render.rs:3-32].

### Public API and Module Symbols

| Symbol | Type | Description | Source Citation |
| --- | --- | --- | --- |
| `render_text` | Function | Renders an `AuditReport` into a plain-text human-readable string. | crates/gwiki/src/audit/render.rs:3-32 |
| `AuditReport` | Struct | Holds the completed audit results, including the target scope and a collection of unsupported claims. | crates/gwiki/src/audit/render.rs:3 |
| `UnsupportedClaim` | Struct | Represents a claim line lacking provenance, detailing its path, line, heading, text, and context. | crates/gwiki/src/audit/claims.rs:32-44 |
| `AuditOptions` | Struct | Configuration parameters controlling the claim-auditing behavior. | crates/gwiki/src/audit/claims.rs:15-20 |
| `AuditSourceContext` | Struct | Contains source citation and ID metadata used to verify claims. | crates/gwiki/src/audit/claims.rs:15-20 |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/audit/claims.rs\|crates/gwiki/src/audit/claims.rs]] | This file implements the audit logic for wiki-page claims, deciding which claim lines lack acceptable provenance and should be reported as `UnsupportedClaim`s. `unsupported_claims` ties the pieces together by collecting claim lines, checking whether each line is supported by page/frontmatter provenance or inline citations, and attaching source context, while the helper functions classify claim kinds, detect generated codewiki pages, inspect frontmatter/source spans, and filter out structural, ignored, or otherwise supported claims. [crates/gwiki/src/audit/claims.rs:15-44] [crates/gwiki/src/audit/claims.rs:46-55] [crates/gwiki/src/audit/claims.rs:57-62] [crates/gwiki/src/audit/claims.rs:64-73] [crates/gwiki/src/audit/claims.rs:75-80] |
| [[code/files/crates/gwiki/src/audit/render.rs\|crates/gwiki/src/audit/render.rs]] | This file provides a plain-text renderer for `AuditReport`. `render_text` builds a human-readable wiki audit report starting with the report scope, then appends an “Unsupported claims” section that either says `none` or lists each unsupported claim with its file path, line number, claim text, and optional source IDs from `source_context`. [crates/gwiki/src/audit/render.rs:3-32] |
| [[code/files/crates/gwiki/src/audit/tests.rs\|crates/gwiki/src/audit/tests.rs]] | This file is an audit test suite for wiki page claim extraction and source-context rules. It sets up temporary wiki roots, registers source manifests, and runs the audit pipeline to verify that unsupported claims are reported with the correct path, line, heading, and citation data; that generated codewiki numeric claims do not accidentally inherit raw source context; that reports preserve path and scope information; that topic audits only inspect topic pages; that frontmatter and HTML comment parsing behave correctly; and that inline or frontmatter source spans are accepted or rejected according to claim type, migration mode, and configured ignored sections. [crates/gwiki/src/audit/tests.rs:14-48] [crates/gwiki/src/audit/tests.rs:51-117] [crates/gwiki/src/audit/tests.rs:120-145] [crates/gwiki/src/audit/tests.rs:148-174] [crates/gwiki/src/audit/tests.rs:177-196] |

## Components

| Component ID |
| --- |
| `bb771ef7-b1fb-5c78-99cc-5384c6645ed0` |
| `79c6c10b-f4bc-5b8f-ae41-9af7c7b1c1dc` |
| `89d06819-27e5-56e7-b43c-7d8745a63a61` |
| `3cc8426f-c5dd-581d-b5df-309aea49d190` |
| `3dc8cb1f-352c-50b5-9f5f-6ae0508f12cb` |
| `9d6d71ea-06ed-5a7c-a3e4-441e51459081` |
| `646fd59a-8711-5d1d-82f6-38a417a482a6` |
| `213ddb02-a92c-55a7-b7e8-ce12fd455afb` |
| `2a2866b8-0e85-5583-8267-60b8fd16edd4` |
| `7e0e51e9-7522-59cd-a6ce-781274798d0b` |
| `2c337166-5272-5bc4-a295-8c06d43cd9f1` |
| `ffd89550-d951-59b7-a8a8-ed43f4c1081c` |
| `39c1e0c0-6e67-5f9b-a9d3-a15c15de8cbd` |
| `ef51c03b-1755-5967-8954-55a0b6a7bf76` |
| `ceb9984d-3f54-5cb8-9eeb-f869f6a6dff6` |
| `7f3ba8b5-835b-50f8-a279-9abab16398d6` |
| `5854c35e-e0b6-5738-af87-76f25cd61c18` |
| `b2f1979f-585b-5a43-baf4-dc3896505436` |
| `ce09f2d1-c92c-53ec-85f5-4fcfd51528bc` |
| `d4ce3bdb-6817-5c2e-8500-1bb69b8b1332` |
| `fd2f5b36-16ed-534a-baa7-0355ea2b77ad` |
| `44719776-0871-55f4-878c-ec897dd657df` |
| `871e5c2f-c3a6-5d37-b32d-2b5df199947c` |
| `d261ce57-7b10-5b29-8e5f-6f103999a468` |
| `97faef9e-0cc6-50c4-8781-fb1c8f0b9b67` |
| `9a36e866-3e86-5670-b8ea-74252b113b37` |
| `ed005516-2a0c-5c35-90ff-979240d44e6b` |
| `dedece25-7042-5177-9d93-9267ff9cfbd1` |
| `dd053e87-efa9-535d-ad6c-eb4326276c90` |
| `46447086-db83-5d79-b2b0-2346d7c5d45c` |
| `dd5581a2-0c40-59ea-a147-548057babc23` |
| `2d5a14a8-60f5-595f-a226-c0652d3b7a76` |
| `710a6796-6b9c-5899-9831-2968de980256` |
| `2d6ef56c-f898-558c-8e94-89557a7fb1a6` |
| `76af33b0-e5a2-50af-81f8-c3acd6070829` |
| `a9b91493-11bb-58a2-aafc-8dcf0aa19727` |
| `68c45157-0a33-5153-a3e6-73da88a3097c` |
| `1082329c-dee9-5555-9155-5104368d8d6b` |
