---
title: crates/gwiki/src/graph
type: code_module
provenance:
- file: crates/gwiki/src/graph/analytics.rs
  ranges:
  - 14-22
  - 25-38
  - 44-51
  - 54-58
  - 61-65
  - 68-71
  - 74-78
  - 81-85
  - 87-91
  - 94-98
  - 100-161
  - 163-184
  - 187-220
  - 224-234
  - 238-244
  - 248-254
  - 258-263
  - 267-273
  - 288-319
  - 322-347
  - 350-365
- file: crates/gwiki/src/graph/context.rs
  ranges:
  - 8-11
  - 14-16
  - 18-23
  - 25-28
  - 32-39
  - 42-45
  - 48-53
  - 56-61
  - 64-73
  - 76-80
  - 83-88
  - 91-99
  - 102-105
  - 107-153
  - 155-172
  - 174-183
  - 185-201
  - 203-212
  - 214-227
  - 229-242
  - 244-272
  - 274-311
  - 313-320
  - 322-329
  - 331-340
  - 342-390
  - 392-394
  - 407-502
  - 505-557
  - 560-654
  - 656-662
  - 664-670
  - 672-684
  - 686-693
  - 695-714
- file: crates/gwiki/src/graph/export.rs
  ranges:
  - 12-111
  - 114-190
  - 204-317
  - 320-349
- file: crates/gwiki/src/graph/mod.rs
  ranges:
  - 22-26
  - 29-33
  - 36-39
  - 42-47
  - 50-59
  - 62-67
  - 70-72
  - 75-77
  - 79-81
  - 85-92
  - 95-103
  - 106-113
  - 116-122
  - 125-127
  - 130-135
  - 138-143
  - 146-148
  - 151-155
  - 158-239
  - 242-244
  - 247-249
  - 252-254
  - 256-290
  - 292-334
  - 336-343
  - 345-405
  - 407-413
  - 416-418
  - 420-422
  - 424-426
  - 428-430
  - 432-440
  - 442-449
  - 451-453
  - 455-464
  - 466-475
  - 477-486
  - 488-497
  - 499-501
  - 503-505
  - 507-513
  - 515-517
  - 519-521
  - 523-532
  - 534-554
  - 556-565
  - 567-593
  - 595-599
  - 601-606
  - 613-679
  - 682-715
  - 718-725
  - 728-771
  - 774-817
  - 820-862
  - 864-870
  - 872-884
  - 886-893
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/graph/analytics.rs:14-22](crates/gwiki/src/graph/analytics.rs#L14-L22), [crates/gwiki/src/graph/analytics.rs:25-38](crates/gwiki/src/graph/analytics.rs#L25-L38), [crates/gwiki/src/graph/analytics.rs:44-51](crates/gwiki/src/graph/analytics.rs#L44-L51), [crates/gwiki/src/graph/analytics.rs:54-58](crates/gwiki/src/graph/analytics.rs#L54-L58), [crates/gwiki/src/graph/analytics.rs:61-65](crates/gwiki/src/graph/analytics.rs#L61-L65), [crates/gwiki/src/graph/analytics.rs:68-71](crates/gwiki/src/graph/analytics.rs#L68-L71), [crates/gwiki/src/graph/analytics.rs:74-78](crates/gwiki/src/graph/analytics.rs#L74-L78), [crates/gwiki/src/graph/analytics.rs:81-85](crates/gwiki/src/graph/analytics.rs#L81-L85), [crates/gwiki/src/graph/analytics.rs:87-91](crates/gwiki/src/graph/analytics.rs#L87-L91), [crates/gwiki/src/graph/analytics.rs:94-98](crates/gwiki/src/graph/analytics.rs#L94-L98), [crates/gwiki/src/graph/analytics.rs:100-161](crates/gwiki/src/graph/analytics.rs#L100-L161), [crates/gwiki/src/graph/analytics.rs:163-184](crates/gwiki/src/graph/analytics.rs#L163-L184), [crates/gwiki/src/graph/analytics.rs:187-220](crates/gwiki/src/graph/analytics.rs#L187-L220), [crates/gwiki/src/graph/analytics.rs:224-234](crates/gwiki/src/graph/analytics.rs#L224-L234), [crates/gwiki/src/graph/analytics.rs:238-244](crates/gwiki/src/graph/analytics.rs#L238-L244), [crates/gwiki/src/graph/analytics.rs:248-254](crates/gwiki/src/graph/analytics.rs#L248-L254), [crates/gwiki/src/graph/analytics.rs:258-263](crates/gwiki/src/graph/analytics.rs#L258-L263), [crates/gwiki/src/graph/analytics.rs:267-273](crates/gwiki/src/graph/analytics.rs#L267-L273), [crates/gwiki/src/graph/analytics.rs:288-319](crates/gwiki/src/graph/analytics.rs#L288-L319), [crates/gwiki/src/graph/analytics.rs:322-347](crates/gwiki/src/graph/analytics.rs#L322-L347), [crates/gwiki/src/graph/analytics.rs:350-365](crates/gwiki/src/graph/analytics.rs#L350-L365)
- [crates/gwiki/src/graph/context.rs:8-11](crates/gwiki/src/graph/context.rs#L8-L11), [crates/gwiki/src/graph/context.rs:14-16](crates/gwiki/src/graph/context.rs#L14-L16), [crates/gwiki/src/graph/context.rs:18-23](crates/gwiki/src/graph/context.rs#L18-L23), [crates/gwiki/src/graph/context.rs:25-28](crates/gwiki/src/graph/context.rs#L25-L28), [crates/gwiki/src/graph/context.rs:32-39](crates/gwiki/src/graph/context.rs#L32-L39), [crates/gwiki/src/graph/context.rs:42-45](crates/gwiki/src/graph/context.rs#L42-L45), [crates/gwiki/src/graph/context.rs:48-53](crates/gwiki/src/graph/context.rs#L48-L53), [crates/gwiki/src/graph/context.rs:56-61](crates/gwiki/src/graph/context.rs#L56-L61), [crates/gwiki/src/graph/context.rs:64-73](crates/gwiki/src/graph/context.rs#L64-L73), [crates/gwiki/src/graph/context.rs:76-80](crates/gwiki/src/graph/context.rs#L76-L80), [crates/gwiki/src/graph/context.rs:83-88](crates/gwiki/src/graph/context.rs#L83-L88), [crates/gwiki/src/graph/context.rs:91-99](crates/gwiki/src/graph/context.rs#L91-L99), [crates/gwiki/src/graph/context.rs:102-105](crates/gwiki/src/graph/context.rs#L102-L105), [crates/gwiki/src/graph/context.rs:107-153](crates/gwiki/src/graph/context.rs#L107-L153), [crates/gwiki/src/graph/context.rs:155-172](crates/gwiki/src/graph/context.rs#L155-L172), [crates/gwiki/src/graph/context.rs:174-183](crates/gwiki/src/graph/context.rs#L174-L183), [crates/gwiki/src/graph/context.rs:185-201](crates/gwiki/src/graph/context.rs#L185-L201), [crates/gwiki/src/graph/context.rs:203-212](crates/gwiki/src/graph/context.rs#L203-L212), [crates/gwiki/src/graph/context.rs:214-227](crates/gwiki/src/graph/context.rs#L214-L227), [crates/gwiki/src/graph/context.rs:229-242](crates/gwiki/src/graph/context.rs#L229-L242), [crates/gwiki/src/graph/context.rs:244-272](crates/gwiki/src/graph/context.rs#L244-L272), [crates/gwiki/src/graph/context.rs:274-311](crates/gwiki/src/graph/context.rs#L274-L311), [crates/gwiki/src/graph/context.rs:313-320](crates/gwiki/src/graph/context.rs#L313-L320), [crates/gwiki/src/graph/context.rs:322-329](crates/gwiki/src/graph/context.rs#L322-L329), [crates/gwiki/src/graph/context.rs:331-340](crates/gwiki/src/graph/context.rs#L331-L340), [crates/gwiki/src/graph/context.rs:342-390](crates/gwiki/src/graph/context.rs#L342-L390), [crates/gwiki/src/graph/context.rs:392-394](crates/gwiki/src/graph/context.rs#L392-L394), [crates/gwiki/src/graph/context.rs:407-502](crates/gwiki/src/graph/context.rs#L407-L502), [crates/gwiki/src/graph/context.rs:505-557](crates/gwiki/src/graph/context.rs#L505-L557), [crates/gwiki/src/graph/context.rs:560-654](crates/gwiki/src/graph/context.rs#L560-L654), [crates/gwiki/src/graph/context.rs:656-662](crates/gwiki/src/graph/context.rs#L656-L662), [crates/gwiki/src/graph/context.rs:664-670](crates/gwiki/src/graph/context.rs#L664-L670), [crates/gwiki/src/graph/context.rs:672-684](crates/gwiki/src/graph/context.rs#L672-L684), [crates/gwiki/src/graph/context.rs:686-693](crates/gwiki/src/graph/context.rs#L686-L693), [crates/gwiki/src/graph/context.rs:695-714](crates/gwiki/src/graph/context.rs#L695-L714)
- [crates/gwiki/src/graph/export.rs:12-111](crates/gwiki/src/graph/export.rs#L12-L111), [crates/gwiki/src/graph/export.rs:114-190](crates/gwiki/src/graph/export.rs#L114-L190), [crates/gwiki/src/graph/export.rs:204-317](crates/gwiki/src/graph/export.rs#L204-L317), [crates/gwiki/src/graph/export.rs:320-349](crates/gwiki/src/graph/export.rs#L320-L349)
- [crates/gwiki/src/graph/mod.rs:22-26](crates/gwiki/src/graph/mod.rs#L22-L26), [crates/gwiki/src/graph/mod.rs:29-33](crates/gwiki/src/graph/mod.rs#L29-L33), [crates/gwiki/src/graph/mod.rs:36-39](crates/gwiki/src/graph/mod.rs#L36-L39), [crates/gwiki/src/graph/mod.rs:42-47](crates/gwiki/src/graph/mod.rs#L42-L47), [crates/gwiki/src/graph/mod.rs:50-59](crates/gwiki/src/graph/mod.rs#L50-L59), [crates/gwiki/src/graph/mod.rs:62-67](crates/gwiki/src/graph/mod.rs#L62-L67), [crates/gwiki/src/graph/mod.rs:70-72](crates/gwiki/src/graph/mod.rs#L70-L72), [crates/gwiki/src/graph/mod.rs:75-77](crates/gwiki/src/graph/mod.rs#L75-L77), [crates/gwiki/src/graph/mod.rs:79-81](crates/gwiki/src/graph/mod.rs#L79-L81), [crates/gwiki/src/graph/mod.rs:85-92](crates/gwiki/src/graph/mod.rs#L85-L92), [crates/gwiki/src/graph/mod.rs:95-103](crates/gwiki/src/graph/mod.rs#L95-L103), [crates/gwiki/src/graph/mod.rs:106-113](crates/gwiki/src/graph/mod.rs#L106-L113), [crates/gwiki/src/graph/mod.rs:116-122](crates/gwiki/src/graph/mod.rs#L116-L122), [crates/gwiki/src/graph/mod.rs:125-127](crates/gwiki/src/graph/mod.rs#L125-L127), [crates/gwiki/src/graph/mod.rs:130-135](crates/gwiki/src/graph/mod.rs#L130-L135), [crates/gwiki/src/graph/mod.rs:138-143](crates/gwiki/src/graph/mod.rs#L138-L143), [crates/gwiki/src/graph/mod.rs:146-148](crates/gwiki/src/graph/mod.rs#L146-L148), [crates/gwiki/src/graph/mod.rs:151-155](crates/gwiki/src/graph/mod.rs#L151-L155), [crates/gwiki/src/graph/mod.rs:158-239](crates/gwiki/src/graph/mod.rs#L158-L239), [crates/gwiki/src/graph/mod.rs:242-244](crates/gwiki/src/graph/mod.rs#L242-L244), [crates/gwiki/src/graph/mod.rs:247-249](crates/gwiki/src/graph/mod.rs#L247-L249), [crates/gwiki/src/graph/mod.rs:252-254](crates/gwiki/src/graph/mod.rs#L252-L254), [crates/gwiki/src/graph/mod.rs:256-290](crates/gwiki/src/graph/mod.rs#L256-L290), [crates/gwiki/src/graph/mod.rs:292-334](crates/gwiki/src/graph/mod.rs#L292-L334), [crates/gwiki/src/graph/mod.rs:336-343](crates/gwiki/src/graph/mod.rs#L336-L343), [crates/gwiki/src/graph/mod.rs:345-405](crates/gwiki/src/graph/mod.rs#L345-L405), [crates/gwiki/src/graph/mod.rs:407-413](crates/gwiki/src/graph/mod.rs#L407-L413), [crates/gwiki/src/graph/mod.rs:416-418](crates/gwiki/src/graph/mod.rs#L416-L418), [crates/gwiki/src/graph/mod.rs:420-422](crates/gwiki/src/graph/mod.rs#L420-L422), [crates/gwiki/src/graph/mod.rs:424-426](crates/gwiki/src/graph/mod.rs#L424-L426), [crates/gwiki/src/graph/mod.rs:428-430](crates/gwiki/src/graph/mod.rs#L428-L430), [crates/gwiki/src/graph/mod.rs:432-440](crates/gwiki/src/graph/mod.rs#L432-L440), [crates/gwiki/src/graph/mod.rs:442-449](crates/gwiki/src/graph/mod.rs#L442-L449), [crates/gwiki/src/graph/mod.rs:451-453](crates/gwiki/src/graph/mod.rs#L451-L453), [crates/gwiki/src/graph/mod.rs:455-464](crates/gwiki/src/graph/mod.rs#L455-L464), [crates/gwiki/src/graph/mod.rs:466-475](crates/gwiki/src/graph/mod.rs#L466-L475), [crates/gwiki/src/graph/mod.rs:477-486](crates/gwiki/src/graph/mod.rs#L477-L486), [crates/gwiki/src/graph/mod.rs:488-497](crates/gwiki/src/graph/mod.rs#L488-L497), [crates/gwiki/src/graph/mod.rs:499-501](crates/gwiki/src/graph/mod.rs#L499-L501), [crates/gwiki/src/graph/mod.rs:503-505](crates/gwiki/src/graph/mod.rs#L503-L505), [crates/gwiki/src/graph/mod.rs:507-513](crates/gwiki/src/graph/mod.rs#L507-L513), [crates/gwiki/src/graph/mod.rs:515-517](crates/gwiki/src/graph/mod.rs#L515-L517), [crates/gwiki/src/graph/mod.rs:519-521](crates/gwiki/src/graph/mod.rs#L519-L521), [crates/gwiki/src/graph/mod.rs:523-532](crates/gwiki/src/graph/mod.rs#L523-L532), [crates/gwiki/src/graph/mod.rs:534-554](crates/gwiki/src/graph/mod.rs#L534-L554), [crates/gwiki/src/graph/mod.rs:556-565](crates/gwiki/src/graph/mod.rs#L556-L565), [crates/gwiki/src/graph/mod.rs:567-593](crates/gwiki/src/graph/mod.rs#L567-L593), [crates/gwiki/src/graph/mod.rs:595-599](crates/gwiki/src/graph/mod.rs#L595-L599), [crates/gwiki/src/graph/mod.rs:601-606](crates/gwiki/src/graph/mod.rs#L601-L606), [crates/gwiki/src/graph/mod.rs:613-679](crates/gwiki/src/graph/mod.rs#L613-L679), [crates/gwiki/src/graph/mod.rs:682-715](crates/gwiki/src/graph/mod.rs#L682-L715), [crates/gwiki/src/graph/mod.rs:718-725](crates/gwiki/src/graph/mod.rs#L718-L725), [crates/gwiki/src/graph/mod.rs:728-771](crates/gwiki/src/graph/mod.rs#L728-L771), [crates/gwiki/src/graph/mod.rs:774-817](crates/gwiki/src/graph/mod.rs#L774-L817), [crates/gwiki/src/graph/mod.rs:820-862](crates/gwiki/src/graph/mod.rs#L820-L862), [crates/gwiki/src/graph/mod.rs:864-870](crates/gwiki/src/graph/mod.rs#L864-L870), [crates/gwiki/src/graph/mod.rs:872-884](crates/gwiki/src/graph/mod.rs#L872-L884), [crates/gwiki/src/graph/mod.rs:886-893](crates/gwiki/src/graph/mod.rs#L886-L893)

</details>

# crates/gwiki/src/graph

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

The crates/gwiki/src/graph module defines the core domain model and in-memory operations for representing, querying, exporting, and analyzing wiki graph structures [crates/gwiki/src/graph/mod.rs:22-26]. The module aggregates documents, source files, citations, and source code links into structured wiki facts via WikiGraphFacts [crates/gwiki/src/graph/mod.rs:42-47]. Through these structures, it resolves local targets, computes backlinks, and produces serialized representations used across the gwiki application [crates/gwiki/src/graph/mod.rs:50-59, crates/gwiki/src/graph/export.rs:12-111].

Key structural flows include exporting complete wiki graphs via WikiGraphFacts::export_graph [crates/gwiki/src/graph/export.rs:12-111] and conducting topological assessments in analytics.rs [crates/gwiki/src/graph/analytics.rs:14-22]. The analytics engine maps internal facts into a specialized analytical graph to calculate community clusters, bridge nodes, hotspots, and degree centrality [crates/gwiki/src/graph/analytics.rs:25-38, crates/gwiki/src/graph/analytics.rs:61-65]. Simultaneously, the context submodule packages query-specific neighborhoods and recommendations into a GraphContextPack [crates/gwiki/src/graph/context.rs:18-23], allowing downstream consumers to view localized document networks, citations, and related warnings [crates/gwiki/src/graph/context.rs:32-39].

### Public Constants

| Constant | Value | Description | Citation |
| --- | --- | --- | --- |
| WIKI_DOC_LABEL | "WikiDoc" | Node label representing a wiki document | crates/gwiki/src/graph/mod.rs:11 |
| WIKI_SOURCE_LABEL | "WikiSource" | Node label representing a source document | crates/gwiki/src/graph/mod.rs:12 |
| WIKI_TARGET_LABEL | "WikiTarget" | Node label representing a target link destination | crates/gwiki/src/graph/mod.rs:13 |
| WIKI_LINKS_TO_REL | "WIKI_LINKS_TO" | Relationship denoting that a wiki document links to a target | crates/gwiki/src/graph/mod.rs:14 |
| MENTIONS_TARGET_REL | "MENTIONS_TARGET" | Relationship for mentioning targets | crates/gwiki/src/graph/mod.rs:15 |
| SUPPORTS_REL | "SUPPORTS" | Relationship indicating that a source supports a document | crates/gwiki/src/graph/mod.rs:16 |
| BACKWARD_LINK_WEIGHT | 0.8 | Default scoring weight used for calculating backward links | crates/gwiki/src/graph/mod.rs:17 |

### Key Public Types and Functions

| Symbol | Type | Description | Citation |
| --- | --- | --- | --- |
| WikiGraphDocument | Struct | Stores search scope, file path, and optional title for a document | crates/gwiki/src/graph/mod.rs:20-25 |
| WikiGraphSource | Struct | Associates a source path with its supporting document path | crates/gwiki/src/graph/mod.rs:27-32 |
| WikiGraphLinkTarget | Enum | Distinguishes between resolved paths and unresolved raw targets | crates/gwiki/src/graph/mod.rs:34-38 |
| WikiGraphLink | Struct | Contains a reference's scope, source path, raw target, and resolved state | crates/gwiki/src/graph/mod.rs:40-46 |
| WikiGraphCodeEdge | Struct | Captures direction, kind, file position, and provenance of source code linkages | crates/gwiki/src/graph/mod.rs:48-58 |
| WikiGraphFacts | Struct | Top-level container for all documents, links, sources, and code edges | crates/gwiki/src/graph/mod.rs:60-66 |
| GraphExportOptions | Struct | Configures graph export behavior and degraded source paths | crates/gwiki/src/graph/mod.rs:68-71 |
| GraphExport | Struct | Holds nodes, edges, and analytic outcomes for serialized output | crates/gwiki/src/graph/mod.rs:83-91 |
| render_graph_report | Function | Renders the exported graph format into a user-friendly report | crates/gwiki/src/graph/mod.rs:9 |
| GraphContextOptions | Struct | Configuration for serializing degraded or truncated context | crates/gwiki/src/graph/context.rs:7-11 |
| GraphContextPack | Struct | Bundles neighborhood scope, degradation state, warnings, and suggestions | crates/gwiki/src/graph/context.rs:31-39 |
| GraphAnalyticsError | Enum | Error indicating duplicate node metadata conflicts during analysis | crates/gwiki/src/graph/analytics.rs:13-22 |
| GraphExportAnalytics | Struct | Serializes community, bridge, hotspot, and centrality results | crates/gwiki/src/graph/analytics.rs:43-51 |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/graph/analytics.rs\|crates/gwiki/src/graph/analytics.rs]] | Builds and exports graph analytics for wiki data. It defines a `GraphAnalyticsError` for duplicate node metadata conflicts, a set of serializable export types for communities, centrality, bridges, hotspots, and node/edge references, and conversion helpers that turn `MemoryWikiGraph` or `WikiGraphFacts` into a core `AnalyticsGraph`, insert nodes safely, run analysis, and map the core results back into the export structs. The tests verify the end-to-end conversion path, handling of missing resolved targets with placeholders, and rejection of duplicate node metadata. [crates/gwiki/src/graph/analytics.rs:14-22] [crates/gwiki/src/graph/analytics.rs:25-38] [crates/gwiki/src/graph/analytics.rs:44-51] [crates/gwiki/src/graph/analytics.rs:54-58] [crates/gwiki/src/graph/analytics.rs:61-65] |
| [[code/files/crates/gwiki/src/graph/context.rs\|crates/gwiki/src/graph/context.rs]] | Defines the data model and assembly helpers for a serialized graph-context response used by `gwiki`. `GraphContextOptions` captures whether the context is fully available or degraded/truncated, and `GraphContextPack` bundles the final output: scope, degradation state, warnings, neighborhood details, and recommendations. The helper functions build each part from graph facts and filesystem paths by collecting neighbors, document links, citations, code calls/imports, and per-path warnings, then combine wiki and code edges into unified recommendations and JSON-ready neighborhood records. [crates/gwiki/src/graph/context.rs:8-11] [crates/gwiki/src/graph/context.rs:14-16] [crates/gwiki/src/graph/context.rs:18-23] [crates/gwiki/src/graph/context.rs:25-28] [crates/gwiki/src/graph/context.rs:32-39] |
| [[code/files/crates/gwiki/src/graph/export.rs\|crates/gwiki/src/graph/export.rs]] | This file defines wiki graph export logic. `WikiGraphFacts::export_graph` walks the collected documents, sources, and links to build a `GraphExport`, deduplicating nodes with a `BTreeSet` and emitting the appropriate trust and audit edges between document, source, citation, resolved-target, and unresolved-target nodes. `render_graph_report` turns that exported graph into a report-friendly representation. The tests confirm link targets are scoped correctly, unresolved targets are emitted as nodes, and missing resolved targets get placeholder nodes. [crates/gwiki/src/graph/export.rs:12-111] [crates/gwiki/src/graph/export.rs:114-190] [crates/gwiki/src/graph/export.rs:204-317] [crates/gwiki/src/graph/export.rs:320-349] |
| [[code/files/crates/gwiki/src/graph/mod.rs\|crates/gwiki/src/graph/mod.rs]] | Defines the wiki graph domain model and in-memory graph operations for `gwiki`. It introduces the core data types for documents, sources, links, code edges, and aggregate facts, plus `GraphExport`/node/edge wrappers and `GraphExportOptions` for producing exportable graph output. `MemoryWikiGraph` stores and queries those facts to generate backlinks, link suggestions, and related paths, while the helper functions build labels, scoped IDs, node IDs, and Mermaid-friendly names consistently across the export and query logic. The file also re-exports `render_graph_report` from the export module and includes tests that lock down label ownership, missing-document filtering, scoped hashing, and scoring/filtering behavior. [crates/gwiki/src/graph/mod.rs:22-26] [crates/gwiki/src/graph/mod.rs:29-33] [crates/gwiki/src/graph/mod.rs:36-39] [crates/gwiki/src/graph/mod.rs:42-47] [crates/gwiki/src/graph/mod.rs:50-59] |

## Components

| Component ID |
| --- |
| `a728344c-24af-5a8a-bcb1-e70ff6b39cea` |
| `0410a958-c158-5f73-a010-4d238fbde733` |
| `bd8038f9-aef7-589f-b93a-6f9620d5c9a6` |
| `991274d0-969a-592f-b866-36c2e3136f33` |
| `65447477-7b2a-5a7d-88b9-8907c05a5a31` |
| `6095a595-4dc2-51c8-bc6d-1b1428493295` |
| `13ad723c-d4a5-59f8-9688-9c6fef0e3ff1` |
| `57cf85b0-e509-5b48-af83-f19998bc1709` |
| `79cd25b2-34a4-56fa-ad19-122096231d80` |
| `6d03da4d-80fa-51c9-8fd5-174c617260c4` |
| `88ba2ef7-d638-54aa-9256-b846ade995ca` |
| `11666de7-90ca-5e58-84ce-cde8b3d982d0` |
| `54e18678-d866-5f33-85a9-d819dc9fdb81` |
| `78267316-5e7f-5fb7-b0c2-8a8e4eec2910` |
| `5e0b58ed-d457-58a5-bdd8-92349055d719` |
| `106df146-0da5-52fa-b6e3-851848e4b6ac` |
| `c0440e5b-0a07-5671-abcd-1db61053bda8` |
| `3a73bcf9-9765-58e0-9090-09c68a9fdfb1` |
| `3ad916c3-f82b-5773-9170-04d1263017f6` |
| `f3e40b0f-2820-518f-a6cc-6650349c24a4` |
| `810cf12d-73c7-590a-9d9f-c0a878e7a6e4` |
| `ae429cf1-c77b-58be-bee2-630e1150849f` |
| `ab54c7a8-455e-527e-82db-17c7e366cbd2` |
| `efaf4f24-0dbc-5da1-9760-f4ec1ae31fc2` |
| `00aa606b-8887-508d-bd4a-76d562bfdfef` |
| `085f1593-8267-50e2-9788-b8672653e4cf` |
| `81940199-14f2-52f7-b553-a043a46cb99e` |
| `8d3dc1e2-3854-5ea4-9faf-d87cc94769c6` |
| `dae1bbc5-3b4c-5c33-8cd1-671ee6f706c3` |
| `94a7851c-1c7a-5287-bae1-9b4239062561` |
| `839ccabb-30c6-5660-8b60-12001f3fcaed` |
| `bb150b11-0bd9-5a7b-90d1-d37a443367cb` |
| `23901316-3853-5209-9121-4dcf36bc096a` |
| `3c9d1ab6-770b-5794-9f13-4e51a0170bd2` |
| `390af12e-a48d-51ee-a2c3-b48f854f1065` |
| `031478d6-2bba-5920-ac6a-ee17c2d497eb` |
| `2289f8d2-db5f-589b-9812-e444b861ebb4` |
| `3188ca19-45e3-5d82-a48b-a862e1b9c7ec` |
| `daab9c99-4bfe-5408-a14d-a19d4058753a` |
| `927e84de-831c-546f-b888-34afec7daa35` |
| `3c908a9e-7ec0-5316-ab44-9748bf8d4cf2` |
| `116bd1b0-a85d-5eb3-b701-758669e4d90a` |
| `f9eca0d4-d6cd-593e-a78a-0def53a2921c` |
| `c5de296b-0fa5-5040-9908-f12f668eeb58` |
| `7cc6251b-6f6e-5110-8e0f-76e13187f226` |
| `c56def57-c58a-5054-9681-a828f60fb30b` |
| `c6d13b57-41a9-5bc9-80b8-7c9136cba20d` |
| `44fb0018-7548-564f-8e8b-15854ccf489e` |
| `2a674ccf-433f-591a-b751-8bba0c39eddc` |
| `4c042788-2347-572d-84c9-86c85fbc31fb` |
| `e9bbaf7b-c48c-5cc3-8300-7804712fd68a` |
| `1fe41e41-9221-5863-8ebe-e33434d242ab` |
| `a344636d-27a7-584c-a4f8-657e8830da01` |
| `86eae7bb-ed54-5a36-9f34-dfe81a217197` |
| `c40a8ac3-c381-53ee-9768-4a1a61f3b35a` |
| `cc789d4c-c904-5cba-8d63-b5b3aae6fe21` |
| `7f77bc8c-8763-526d-85f9-942bb2382fa4` |
| `24fee7a5-bd0c-5d1b-84b2-2aed37596006` |
| `c2d2d1d6-edda-526e-933c-db52b1b81fcb` |
| `f8bfc816-60d3-59f3-9a64-6deb429e5dc5` |
| `ae3abb0d-9d89-53d0-9f77-bd19629bbd71` |
| `23ac1c98-2c08-572e-b5b7-a14206627c82` |
| `fe3f6a2f-b7a2-56c0-b7c9-fe9775f112f0` |
| `6b8d5203-ecb9-5370-9a9c-05284911f23c` |
| `98827567-d658-5c0c-b1c9-264af462d85e` |
| `a5370d6c-9459-5382-bdd5-152a94de302e` |
| `e44cdaf1-94de-54c4-9d08-5b270d746a8b` |
| `2cc9cd06-73db-572c-a36e-eb8ba2c81965` |
| `ccd5801a-c85d-5474-801c-b3f54d6bd654` |
| `f0f5a353-0a96-566e-bff2-f5c41eaf0684` |
| `22e6ba9d-3a8d-5fb5-b566-4b9d3046aefa` |
| `08ac016d-d912-5509-a0a9-a85565487bc7` |
| `a5ef95bb-bac2-5680-974c-7f7587e82138` |
| `b81e41d4-1540-5197-a578-04aff61df132` |
| `3c471dab-f9fe-5d01-95d3-e849ada407f6` |
| `9d7ae669-dfd8-5790-b926-27175f6077a6` |
| `5ef1a36d-9f7f-59e0-87bd-1571c4abd7cb` |
| `b103dac5-1f0d-5835-82c6-78550850f358` |
| `e7fb4b80-5bd1-536c-9ed8-18ad5c3b536c` |
| `0ed3333f-6cb2-5f58-9fc4-1ce345e396c3` |
| `b30def02-4991-528d-b788-f1cef3b98edf` |
| `d83faf5b-dce0-5a3e-a62a-4a8bf97da070` |
| `3d858d66-f687-552c-bcaf-7c0de1ed61ed` |
| `fb9fbf25-409d-52c4-a646-ca4240fe89fc` |
| `34bbc1c2-a884-5aa9-9c57-4fc5db3608a8` |
| `87577f54-820d-5073-9fa8-74921f0ec1a2` |
| `21bb4330-85ee-5c20-b5e2-f5f52c922695` |
| `f2ecf981-f9fe-5b89-ae3c-624c772c387e` |
| `8ebce724-afcb-555d-ab2c-b44b37028d6d` |
| `0c9536ff-594d-5897-b36f-d5a8370c0a07` |
| `384294d3-bfb3-5c56-8294-61a1e0f335e8` |
| `6ea5885d-0c8f-5bb0-bbb3-a2b573ee67c8` |
| `2a80359d-8836-5099-b790-24b620889645` |
| `12d8cd19-262d-587e-8cd3-17b2818f3a07` |
| `1ae31f01-1c99-55c7-af0c-0e0807245c97` |
| `f47d6394-06c6-5a86-8292-ed612ea5a5f0` |
| `b07698c6-990b-55a1-a75a-7739b8dd3f33` |
| `631a8fb3-e4b5-5c5d-9788-941aac064976` |
| `24dce42f-d268-57bf-a2fd-b868e9457c5f` |
| `3c0afb87-6378-5d56-9459-8fa2b6d22aff` |
| `8505e829-a76a-53ee-bc0b-508940f9bc39` |
| `6bee331e-0220-53b2-9bdc-fee7ff6a4983` |
| `3045da76-83ae-5e87-be99-9a644230d5de` |
| `974a41df-d9c8-578d-8254-b86b9b623780` |
| `550ceffc-d141-565f-9c7f-538e7664f092` |
| `b0dd8401-9883-5733-9e2d-875c444ff232` |
| `3b8f3ab9-33d9-56c4-9b70-e8d86d5b83f1` |
| `3fdfe00d-0f4e-537e-8995-3598676a192e` |
| `c51b8f74-b8a7-536c-b3c6-fc074dbc9bad` |
| `e5b9d33c-9cd5-5bfd-8cc9-830d118d25d4` |
| `ea8b41f6-61d3-5f14-a251-f0fe3fe8ae30` |
| `ce0fbd0b-2b64-573f-b428-92d87c66590c` |
| `3bb5f40e-4065-5517-a19b-e2221a3834cd` |
| `c3a548e7-f1ea-521c-903c-698bddf9ed2e` |
| `09b5d54f-729b-5869-a4b0-09277b078d16` |
| `b10d9cc3-44ac-55cd-b08f-9ace8ccba07b` |
| `37f4fe95-ae89-55cc-b264-f944c92007cc` |
| `8321713e-3c32-5398-9ae2-bf5895be5554` |
| `ac5e6d40-2304-507a-ade6-473ed49dede5` |
