---
title: crates/gcode/src/commands/graph
type: code_module
provenance:
- file: crates/gcode/src/commands/graph/lifecycle.rs
  ranges:
  - 12-14
  - 17-28
  - 30-41
  - 43-45
  - 47-49
  - 51-53
  - 57-64
  - 69-76
  - 78-84
  - '86'
  - 89-98
  - 101-115
  - 117-129
  - 131-138
  - 140-147
  - 149-161
  - 163-165
  - 167-211
  - 213-234
  - 236-320
  - 322-329
  - 331-338
  - 345-365
  - 367-375
  - 377-440
- file: crates/gcode/src/commands/graph/payload.rs
  ranges:
  - 6-37
  - 39-44
  - 46-48
  - 50-59
  - 61-64
  - 66-69
  - 71-79
  - 81-96
- file: crates/gcode/src/commands/graph/reads.rs
  ranges:
  - 19-25
  - 27-35
  - 37-43
  - 45-49
  - 51-59
  - 61-84
  - 86-101
  - 103-129
  - 131-136
  - 138-144
  - 146-152
  - 155-159
  - 162-172
  - 174-181
  - 183-214
  - 216-251
  - 253-266
  - 268-280
  - 282-291
  - 295-301
  - 303-332
  - 334-348
  - 350-383
  - 385-436
  - 438-502
  - 504-539
  - 541-562
  - 564-623
  - 640-643
  - 645-652
  - 654-661
  - 663-666
  - 669-674
  - 678-689
  - 692-695
  - 697-711
  - 713-722
  - 724-735
  - 737-756
  - 767-793
  - 801-825
  - 833-867
- file: crates/gcode/src/commands/graph/tests.rs
  ranges:
  - 22-36
  - 39-45
  - 48-56
  - 59-98
  - 101-125
  - 128-178
  - 181-205
  - 208-215
  - 218-232
  - 235-237
  - 240-257
  - 261-284
  - 287-296
  - 299-315
  - 318-336
  - 339-347
  - 350-362
  - 365-377
  - 380-393
  - 396-411
  - 414-430
  - 433-450
  - 453-470
  - 473-535
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/graph/lifecycle.rs:12-14](crates/gcode/src/commands/graph/lifecycle.rs#L12-L14), [crates/gcode/src/commands/graph/lifecycle.rs:17-28](crates/gcode/src/commands/graph/lifecycle.rs#L17-L28), [crates/gcode/src/commands/graph/lifecycle.rs:30-41](crates/gcode/src/commands/graph/lifecycle.rs#L30-L41), [crates/gcode/src/commands/graph/lifecycle.rs:43-45](crates/gcode/src/commands/graph/lifecycle.rs#L43-L45), [crates/gcode/src/commands/graph/lifecycle.rs:47-49](crates/gcode/src/commands/graph/lifecycle.rs#L47-L49), [crates/gcode/src/commands/graph/lifecycle.rs:51-53](crates/gcode/src/commands/graph/lifecycle.rs#L51-L53), [crates/gcode/src/commands/graph/lifecycle.rs:57-64](crates/gcode/src/commands/graph/lifecycle.rs#L57-L64), [crates/gcode/src/commands/graph/lifecycle.rs:69-76](crates/gcode/src/commands/graph/lifecycle.rs#L69-L76), [crates/gcode/src/commands/graph/lifecycle.rs:78-84](crates/gcode/src/commands/graph/lifecycle.rs#L78-L84), [crates/gcode/src/commands/graph/lifecycle.rs:86](crates/gcode/src/commands/graph/lifecycle.rs#L86), [crates/gcode/src/commands/graph/lifecycle.rs:89-98](crates/gcode/src/commands/graph/lifecycle.rs#L89-L98), [crates/gcode/src/commands/graph/lifecycle.rs:101-115](crates/gcode/src/commands/graph/lifecycle.rs#L101-L115), [crates/gcode/src/commands/graph/lifecycle.rs:117-129](crates/gcode/src/commands/graph/lifecycle.rs#L117-L129), [crates/gcode/src/commands/graph/lifecycle.rs:131-138](crates/gcode/src/commands/graph/lifecycle.rs#L131-L138), [crates/gcode/src/commands/graph/lifecycle.rs:140-147](crates/gcode/src/commands/graph/lifecycle.rs#L140-L147), [crates/gcode/src/commands/graph/lifecycle.rs:149-161](crates/gcode/src/commands/graph/lifecycle.rs#L149-L161), [crates/gcode/src/commands/graph/lifecycle.rs:163-165](crates/gcode/src/commands/graph/lifecycle.rs#L163-L165), [crates/gcode/src/commands/graph/lifecycle.rs:167-211](crates/gcode/src/commands/graph/lifecycle.rs#L167-L211), [crates/gcode/src/commands/graph/lifecycle.rs:213-234](crates/gcode/src/commands/graph/lifecycle.rs#L213-L234), [crates/gcode/src/commands/graph/lifecycle.rs:236-320](crates/gcode/src/commands/graph/lifecycle.rs#L236-L320), [crates/gcode/src/commands/graph/lifecycle.rs:322-329](crates/gcode/src/commands/graph/lifecycle.rs#L322-L329), [crates/gcode/src/commands/graph/lifecycle.rs:331-338](crates/gcode/src/commands/graph/lifecycle.rs#L331-L338), [crates/gcode/src/commands/graph/lifecycle.rs:345-365](crates/gcode/src/commands/graph/lifecycle.rs#L345-L365), [crates/gcode/src/commands/graph/lifecycle.rs:367-375](crates/gcode/src/commands/graph/lifecycle.rs#L367-L375), [crates/gcode/src/commands/graph/lifecycle.rs:377-440](crates/gcode/src/commands/graph/lifecycle.rs#L377-L440)
- [crates/gcode/src/commands/graph/payload.rs:6-37](crates/gcode/src/commands/graph/payload.rs#L6-L37), [crates/gcode/src/commands/graph/payload.rs:39-44](crates/gcode/src/commands/graph/payload.rs#L39-L44), [crates/gcode/src/commands/graph/payload.rs:46-48](crates/gcode/src/commands/graph/payload.rs#L46-L48), [crates/gcode/src/commands/graph/payload.rs:50-59](crates/gcode/src/commands/graph/payload.rs#L50-L59), [crates/gcode/src/commands/graph/payload.rs:61-64](crates/gcode/src/commands/graph/payload.rs#L61-L64), [crates/gcode/src/commands/graph/payload.rs:66-69](crates/gcode/src/commands/graph/payload.rs#L66-L69), [crates/gcode/src/commands/graph/payload.rs:71-79](crates/gcode/src/commands/graph/payload.rs#L71-L79), [crates/gcode/src/commands/graph/payload.rs:81-96](crates/gcode/src/commands/graph/payload.rs#L81-L96)
- [crates/gcode/src/commands/graph/reads.rs:19-25](crates/gcode/src/commands/graph/reads.rs#L19-L25), [crates/gcode/src/commands/graph/reads.rs:27-35](crates/gcode/src/commands/graph/reads.rs#L27-L35), [crates/gcode/src/commands/graph/reads.rs:37-43](crates/gcode/src/commands/graph/reads.rs#L37-L43), [crates/gcode/src/commands/graph/reads.rs:45-49](crates/gcode/src/commands/graph/reads.rs#L45-L49), [crates/gcode/src/commands/graph/reads.rs:51-59](crates/gcode/src/commands/graph/reads.rs#L51-L59), [crates/gcode/src/commands/graph/reads.rs:61-84](crates/gcode/src/commands/graph/reads.rs#L61-L84), [crates/gcode/src/commands/graph/reads.rs:86-101](crates/gcode/src/commands/graph/reads.rs#L86-L101), [crates/gcode/src/commands/graph/reads.rs:103-129](crates/gcode/src/commands/graph/reads.rs#L103-L129), [crates/gcode/src/commands/graph/reads.rs:131-136](crates/gcode/src/commands/graph/reads.rs#L131-L136), [crates/gcode/src/commands/graph/reads.rs:138-144](crates/gcode/src/commands/graph/reads.rs#L138-L144), [crates/gcode/src/commands/graph/reads.rs:146-152](crates/gcode/src/commands/graph/reads.rs#L146-L152), [crates/gcode/src/commands/graph/reads.rs:155-159](crates/gcode/src/commands/graph/reads.rs#L155-L159), [crates/gcode/src/commands/graph/reads.rs:162-172](crates/gcode/src/commands/graph/reads.rs#L162-L172), [crates/gcode/src/commands/graph/reads.rs:174-181](crates/gcode/src/commands/graph/reads.rs#L174-L181), [crates/gcode/src/commands/graph/reads.rs:183-214](crates/gcode/src/commands/graph/reads.rs#L183-L214), [crates/gcode/src/commands/graph/reads.rs:216-251](crates/gcode/src/commands/graph/reads.rs#L216-L251), [crates/gcode/src/commands/graph/reads.rs:253-266](crates/gcode/src/commands/graph/reads.rs#L253-L266), [crates/gcode/src/commands/graph/reads.rs:268-280](crates/gcode/src/commands/graph/reads.rs#L268-L280), [crates/gcode/src/commands/graph/reads.rs:282-291](crates/gcode/src/commands/graph/reads.rs#L282-L291), [crates/gcode/src/commands/graph/reads.rs:295-301](crates/gcode/src/commands/graph/reads.rs#L295-L301), [crates/gcode/src/commands/graph/reads.rs:303-332](crates/gcode/src/commands/graph/reads.rs#L303-L332), [crates/gcode/src/commands/graph/reads.rs:334-348](crates/gcode/src/commands/graph/reads.rs#L334-L348), [crates/gcode/src/commands/graph/reads.rs:350-383](crates/gcode/src/commands/graph/reads.rs#L350-L383), [crates/gcode/src/commands/graph/reads.rs:385-436](crates/gcode/src/commands/graph/reads.rs#L385-L436), [crates/gcode/src/commands/graph/reads.rs:438-502](crates/gcode/src/commands/graph/reads.rs#L438-L502), [crates/gcode/src/commands/graph/reads.rs:504-539](crates/gcode/src/commands/graph/reads.rs#L504-L539), [crates/gcode/src/commands/graph/reads.rs:541-562](crates/gcode/src/commands/graph/reads.rs#L541-L562), [crates/gcode/src/commands/graph/reads.rs:564-623](crates/gcode/src/commands/graph/reads.rs#L564-L623), [crates/gcode/src/commands/graph/reads.rs:640-643](crates/gcode/src/commands/graph/reads.rs#L640-L643), [crates/gcode/src/commands/graph/reads.rs:645-652](crates/gcode/src/commands/graph/reads.rs#L645-L652), [crates/gcode/src/commands/graph/reads.rs:654-661](crates/gcode/src/commands/graph/reads.rs#L654-L661), [crates/gcode/src/commands/graph/reads.rs:663-666](crates/gcode/src/commands/graph/reads.rs#L663-L666), [crates/gcode/src/commands/graph/reads.rs:669-674](crates/gcode/src/commands/graph/reads.rs#L669-L674), [crates/gcode/src/commands/graph/reads.rs:678-689](crates/gcode/src/commands/graph/reads.rs#L678-L689), [crates/gcode/src/commands/graph/reads.rs:692-695](crates/gcode/src/commands/graph/reads.rs#L692-L695), [crates/gcode/src/commands/graph/reads.rs:697-711](crates/gcode/src/commands/graph/reads.rs#L697-L711), [crates/gcode/src/commands/graph/reads.rs:713-722](crates/gcode/src/commands/graph/reads.rs#L713-L722), [crates/gcode/src/commands/graph/reads.rs:724-735](crates/gcode/src/commands/graph/reads.rs#L724-L735), [crates/gcode/src/commands/graph/reads.rs:737-756](crates/gcode/src/commands/graph/reads.rs#L737-L756), [crates/gcode/src/commands/graph/reads.rs:767-793](crates/gcode/src/commands/graph/reads.rs#L767-L793), [crates/gcode/src/commands/graph/reads.rs:801-825](crates/gcode/src/commands/graph/reads.rs#L801-L825), [crates/gcode/src/commands/graph/reads.rs:833-867](crates/gcode/src/commands/graph/reads.rs#L833-L867)
- [crates/gcode/src/commands/graph/tests.rs:22-36](crates/gcode/src/commands/graph/tests.rs#L22-L36), [crates/gcode/src/commands/graph/tests.rs:39-45](crates/gcode/src/commands/graph/tests.rs#L39-L45), [crates/gcode/src/commands/graph/tests.rs:48-56](crates/gcode/src/commands/graph/tests.rs#L48-L56), [crates/gcode/src/commands/graph/tests.rs:59-98](crates/gcode/src/commands/graph/tests.rs#L59-L98), [crates/gcode/src/commands/graph/tests.rs:101-125](crates/gcode/src/commands/graph/tests.rs#L101-L125), [crates/gcode/src/commands/graph/tests.rs:128-178](crates/gcode/src/commands/graph/tests.rs#L128-L178), [crates/gcode/src/commands/graph/tests.rs:181-205](crates/gcode/src/commands/graph/tests.rs#L181-L205), [crates/gcode/src/commands/graph/tests.rs:208-215](crates/gcode/src/commands/graph/tests.rs#L208-L215), [crates/gcode/src/commands/graph/tests.rs:218-232](crates/gcode/src/commands/graph/tests.rs#L218-L232), [crates/gcode/src/commands/graph/tests.rs:235-237](crates/gcode/src/commands/graph/tests.rs#L235-L237), [crates/gcode/src/commands/graph/tests.rs:240-257](crates/gcode/src/commands/graph/tests.rs#L240-L257), [crates/gcode/src/commands/graph/tests.rs:261-284](crates/gcode/src/commands/graph/tests.rs#L261-L284), [crates/gcode/src/commands/graph/tests.rs:287-296](crates/gcode/src/commands/graph/tests.rs#L287-L296), [crates/gcode/src/commands/graph/tests.rs:299-315](crates/gcode/src/commands/graph/tests.rs#L299-L315), [crates/gcode/src/commands/graph/tests.rs:318-336](crates/gcode/src/commands/graph/tests.rs#L318-L336), [crates/gcode/src/commands/graph/tests.rs:339-347](crates/gcode/src/commands/graph/tests.rs#L339-L347), [crates/gcode/src/commands/graph/tests.rs:350-362](crates/gcode/src/commands/graph/tests.rs#L350-L362), [crates/gcode/src/commands/graph/tests.rs:365-377](crates/gcode/src/commands/graph/tests.rs#L365-L377), [crates/gcode/src/commands/graph/tests.rs:380-393](crates/gcode/src/commands/graph/tests.rs#L380-L393), [crates/gcode/src/commands/graph/tests.rs:396-411](crates/gcode/src/commands/graph/tests.rs#L396-L411), [crates/gcode/src/commands/graph/tests.rs:414-430](crates/gcode/src/commands/graph/tests.rs#L414-L430), [crates/gcode/src/commands/graph/tests.rs:433-450](crates/gcode/src/commands/graph/tests.rs#L433-L450), [crates/gcode/src/commands/graph/tests.rs:453-470](crates/gcode/src/commands/graph/tests.rs#L453-L470), [crates/gcode/src/commands/graph/tests.rs:473-535](crates/gcode/src/commands/graph/tests.rs#L473-L535)

</details>

# crates/gcode/src/commands/graph

Parent: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

The crates/gcode/src/commands/graph module implements the commands and controllers for Gobby's graph database integrations. Its core responsibilities are split between a write-side lifecycle layer, an output payload formatter, and a read-side query layer. The lifecycle subsystem manages state-altering actions, including file-level synchronization, project-wide database clearing or rebuilding, and automated cleanup of orphaned nodes or deleted projects [crates/gcode/src/commands/graph/lifecycle.rs:30-41]. It handles these operations via an abstract backend execution model and generates standardized JSON/text responses and typed contract errors if project index mappings or files are missing [crates/gcode/src/commands/graph/lifecycle.rs:12-14, 17-28, 47-49].

The query and payload subsystems format and dispatch read operations to analyze relationships between codebase symbols. Users can inspect imports, find callers, track usages, compute paths between symbols, or calculate a symbol's blast radius [crates/gcode/src/commands/graph/reads.rs:19-25]. The read layer handles target symbol resolution, performs paging, and degrades gracefully by providing context-aware setup hints if the underlying FalkorDB backend is unconfigured or offline [crates/gcode/src/commands/graph/reads.rs:27-35, 45-49, 51-59]. Finally, the payload module coordinates output serialization, marshaling complex graphs and markdown reports into JSON or plain text for display [crates/gcode/src/commands/graph/payload.rs:6-37, 50-59].

| Public API Symbol | Type | Description | Supporting Reference |
| --- | --- | --- | --- |
| GraphSyncContractError | Struct | Defines structured contract errors for graph sync failures. | [crates/gcode/src/commands/graph/lifecycle.rs:12-14] |
| CodeGraphLifecycleBackend | Class | High-level entry point for executing lifecycle actions. | [crates/gcode/src/commands/graph/lifecycle.rs:47-49] |
| sync_file | Function | Synchronizes code graph changes for a specific file. | [crates/gcode/src/commands/graph/lifecycle.rs:30-41] |
| clear | Function | Clears the active project's graph from the database. | [crates/gcode/src/commands/graph/lifecycle.rs:30-41] |
| rebuild | Function | Rebuilds the project graph from search indexes. | [crates/gcode/src/commands/graph/lifecycle.rs:30-41] |
| cleanup_orphans | Function | Deletes orphaned nodes across projects. | [crates/gcode/src/commands/graph/lifecycle.rs:30-41] |
| cleanup_deleted_project_graph | Function | Cleans up remnants of a deleted project's graph. | [crates/gcode/src/commands/graph/lifecycle.rs:30-41] |
| report | Function | Generates and prints a top-level project graph markdown report. | [crates/gcode/src/commands/graph/payload.rs:50-59] |
| overview | Function | Renders a high-level summary of the active project graph. | [crates/gcode/src/commands/graph/payload.rs:50-59] |
| file | Function | Retrieves and outputs node and link data for a specific file. | [crates/gcode/src/commands/graph/payload.rs:50-59] |
| neighbors | Function | Inspects immediate neighbors of a focal symbol in the graph. | [crates/gcode/src/commands/graph/payload.rs:50-59] |
| graph_blast_radius | Function | Prepares visualization payload mapping blast radius nodes. | [crates/gcode/src/commands/graph/payload.rs:50-59] |
| callers | Function | Finds and prints graph nodes calling the targeted symbol. | [crates/gcode/src/commands/graph/reads.rs:19-25] |
| usages | Function | Locates and prints occurrences of symbol usages. | [crates/gcode/src/commands/graph/reads.rs:19-25] |
| imports | Function | Returns files and symbols imported by the given file path. | [crates/gcode/src/commands/graph/reads.rs:19-25] |
| path | Function | Finds the dependency chain linking two symbol endpoints. | [crates/gcode/src/commands/graph/reads.rs:19-25] |
| blast_radius | Function | Performs an impact analysis showing descendants of a symbol. | [crates/gcode/src/commands/graph/reads.rs:19-25] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/graph/lifecycle.rs\|crates/gcode/src/commands/graph/lifecycle.rs]] | Implements the graph lifecycle command flow for the code graph: it defines a contract error type for sync failures, formats success/error output, and exposes a backend abstraction plus the high-level entry points for running lifecycle actions. The helper functions coordinate file-level sync, project graph clearing/rebuilding, orphan and deleted-project cleanup, and the sync/rebuild wrappers so the command layer can return structured JSON or human-readable status consistently. [crates/gcode/src/commands/graph/lifecycle.rs:12-14] [crates/gcode/src/commands/graph/lifecycle.rs:17-28] [crates/gcode/src/commands/graph/lifecycle.rs:30-41] [crates/gcode/src/commands/graph/lifecycle.rs:43-45] [crates/gcode/src/commands/graph/lifecycle.rs:47-49] |
| [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] | Provides the `graph` command’s payload/output layer: it turns `GraphPayload` and project graph reports into either JSON or plain text, then exposes command entry points that build specific graph views and print them. `format_graph_payload_text` renders node/link summaries, `print_graph_payload` dispatches between JSON and text, and `report`, `overview`, `file`, `neighbors`, and `graph_blast_radius` assemble the appropriate graph data from `Context` before handing it to the shared printers. [crates/gcode/src/commands/graph/payload.rs:6-37] [crates/gcode/src/commands/graph/payload.rs:39-44] [crates/gcode/src/commands/graph/payload.rs:46-48] [crates/gcode/src/commands/graph/payload.rs:50-59] [crates/gcode/src/commands/graph/payload.rs:61-64] |
| [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] | Provides the read-side graph commands for Gobby, including caller, usage, import, path, and blast-radius lookups plus the helpers needed to resolve symbols, page results, format output, and report backend availability or refinement hints. The top-level command functions delegate to shared resolution and formatting helpers, which either print JSON or text responses, surface FalkorDB-related errors as user hints, and fall back to empty paged responses when graph reads are unavailable. The lower section includes test setup and cleanup utilities for seeding projects, files, and symbols, along with regression tests covering UUID resolution, unknown UUID handling, and ambiguous name behavior. [crates/gcode/src/commands/graph/reads.rs:19-25] [crates/gcode/src/commands/graph/reads.rs:27-35] [crates/gcode/src/commands/graph/reads.rs:37-43] [crates/gcode/src/commands/graph/reads.rs:45-49] [crates/gcode/src/commands/graph/reads.rs:51-59] |
| [[code/files/crates/gcode/src/commands/graph/tests.rs\|crates/gcode/src/commands/graph/tests.rs]] | This test module validates the graph command layer end to end: it builds a minimal `Context`, exercises read/report/lifecycle helpers, and checks that graph output degrades cleanly when backends are missing. The tests cover text and markdown formatting, grouping and ordering of graph results, confidence labels, token-budget rendering, path formatting, lifecycle dispatch and URL construction, typed error/skip payloads, JSON parsing, and top-level read command response shapes. [crates/gcode/src/commands/graph/tests.rs:22-36] [crates/gcode/src/commands/graph/tests.rs:39-45] [crates/gcode/src/commands/graph/tests.rs:48-56] [crates/gcode/src/commands/graph/tests.rs:59-98] [crates/gcode/src/commands/graph/tests.rs:101-125] |

## Components

| Component ID |
| --- |
| `95cb25f4-e1f7-5eea-af0c-64c37790e5b9` |
| `3aa2684d-396b-57d6-81db-823ce9abf938` |
| `f8d135df-c390-5217-a73d-cd34d187be0f` |
| `eae964ca-8fdf-5d8a-913a-0cf46102e75f` |
| `71bea680-d940-53c1-9aa5-03725ed26611` |
| `0109de40-7324-5f91-99e9-6fd1ba08e599` |
| `71ed0210-42e4-56e8-a5ba-944001bfa546` |
| `14a613ca-e60f-5141-b5e0-cb157a7ca83d` |
| `2d492478-1988-5e01-9da7-4dbc99adc638` |
| `4d7bf3ce-41fb-5d3a-95a5-c71856a19da3` |
| `695f7fd4-361e-5210-a0b2-5129e506f4d3` |
| `d1f7ee77-88a6-5ae8-a267-120a6efe9b93` |
| `d5e3a602-cee7-596d-8bad-4eec33f4b381` |
| `5a6558a1-f41d-5c2f-801e-781a9cedc834` |
| `52ece424-9c84-5199-ac7d-5d3ff5d3322d` |
| `f6fb9a38-c7e7-538f-910b-c9aaf7cc197a` |
| `a43cb306-e69a-52a2-8edd-1be74a962e82` |
| `a23f30e5-ed7a-5f1a-b189-db940072bad9` |
| `4825b611-0875-5fa0-af2e-f2af16d203d5` |
| `0daae913-bbc7-51cf-aa40-e6223b20d7fa` |
| `2f46e8c3-ac41-5f5d-b926-c23f48d0e8f5` |
| `b869c442-314a-53c6-9871-1ac8e9db210d` |
| `3bfcfd68-522a-527e-89c3-76e697ae0cd0` |
| `2c406a81-3008-5ad8-b1c6-f175350676ab` |
| `7d04aa32-043b-56fc-a044-3359ec5b303d` |
| `3d28836a-3131-57ef-9d9d-7b47405155cc` |
| `eae59979-bc5d-5c0f-a67b-fadf5ff52825` |
| `b1011ef1-d6a0-5841-bf9e-aea33a9feaf8` |
| `bd2049dd-9c75-5e96-a74b-400a199fc004` |
| `a11de9f9-24a2-5c45-914e-05c652a70def` |
| `088ce1b3-b2ca-506f-b95e-31536517658b` |
| `52816628-b5e3-5102-9b08-0a024a0e7fb1` |
| `a4088741-10dc-5f7b-9197-c6357c877462` |
| `f81f7279-8978-5e45-9f05-e8cc357474ad` |
| `e47250b0-9454-5e37-a69f-cb4873f792f9` |
| `14ce3e29-d446-530a-b807-422a02c99c38` |
| `82be435d-61ce-5807-b440-876950f50447` |
| `972118ff-f49d-53fd-bdce-4bf98f62be78` |
| `d94b4f46-b23c-52a0-990b-8944ca12144b` |
| `13f9a0a6-7524-54c3-94de-3d76835a4f0d` |
| `0fb3d396-03c9-541a-9c73-d07f85490021` |
| `f745fee1-f580-517d-b725-914a4138f7dc` |
| `eb09a7bc-5e13-556f-b0e3-af278485cd73` |
| `169e35c6-12c3-5878-9de5-25e6328c8593` |
| `015162b9-3c95-5088-b757-3ae14791d783` |
| `2ac82dd1-1540-5aaf-ba3b-9304b08b5af9` |
| `63e8f0d9-fe96-57ee-874f-569512fd7b29` |
| `77173330-fed6-575c-b03d-0b9557eaeaa6` |
| `e62c3497-5a8e-5864-a03c-b46ce9f3552d` |
| `443cc001-2d98-5d61-8b65-e2f533220395` |
| `d3fae140-6b96-5b43-bc30-33764f38b7f4` |
| `6bfe6d6d-e482-536c-b18a-62ffd5a30089` |
| `25486561-4cf6-553a-b2fa-99598f9b8282` |
| `b3b5e81e-12d7-5acb-9fc4-01d9f63bf0f4` |
| `048e587f-6251-5283-8cbf-c5ec0110d70f` |
| `f2aecd7f-9a0e-5fc9-bd5b-9bc53ea93837` |
| `cb97cbc9-f10b-50cc-bfde-27552e9e63bb` |
| `6228a8be-fbee-5193-b24c-14d28ed56367` |
| `c1ccc4a9-4661-59e9-b7ca-4206c4687fec` |
| `d9c34928-fab1-5011-8c73-79807399e840` |
| `2115d586-cc0b-5558-b5e7-7945827071bf` |
| `1064255e-a372-5c5d-99fa-bba0b1882f0a` |
| `1d6569ae-b841-5a48-bad6-f7a113a18530` |
| `ee8266e4-16e2-5748-bec3-9bb4cab6e9e6` |
| `f910138d-d753-5e66-9fcc-9dd3d89fa3a9` |
| `a914c2f3-b897-54ad-b505-1626fd7d8fc8` |
| `604ce29b-1924-53a0-b174-858e57b580e9` |
| `f93e513c-4e8c-5637-bd13-c39f821a8f2b` |
| `c2ccf457-53f5-52cd-921f-a6ca894cc79d` |
| `087d30ea-8b7f-59be-91d6-6dcdbe545dd1` |
| `998fa8af-9973-57e2-931b-d02906885e25` |
| `591b33ec-562f-59cb-864d-060a2a81e9e5` |
| `faecd264-a32f-562b-8639-e50d029ccb85` |
| `2048167d-b65b-5844-9116-ae6539902a39` |
| `44efcb85-6330-501b-9f14-7aca6d56b4a4` |
| `9a1a06db-26b1-5a5b-bdb3-74ea81940ddc` |
| `24280c5c-c157-5ee5-b1d4-a2c905c04f91` |
| `134e04fb-264a-5824-80ae-cd391b14e434` |
| `5e5f77dd-893e-520a-b1ee-c26faf3420f6` |
| `f67306b6-88ee-537f-8ac1-5fe4e3ce7ed4` |
| `1652b2a0-c85a-58d0-a87f-0362e2fcdf36` |
| `11a8ae68-ac10-5d7e-81b5-9d4d746cf9bf` |
| `19d55c70-9814-5de6-a16d-37fe896c0aad` |
| `ecbe5cc2-9faf-5391-af84-76d4d4786519` |
| `5b0b0e22-9a9b-5f0b-93c9-82de8c0d51fb` |
| `9f5c1a14-5ee6-5672-8c24-f7b5e881bcca` |
| `479e3fb4-951b-5978-bde8-ed6aecb0b54a` |
| `4d8b9d52-f782-5b02-9b16-ccf6a1c5c124` |
| `453b8c16-c790-5ef5-8e1e-6700b16c8002` |
| `33e42b59-9899-5ddb-9777-fce1998c3944` |
| `bf19ece1-84a6-5add-a80a-d296919b6c39` |
| `751498bf-2a10-5aec-8e23-ed672f040475` |
| `745636dc-b284-5c9a-a01d-556ed7735f05` |
| `d7991012-488b-5c18-987a-e2077dca1ee2` |
| `db5902aa-41cc-5700-a4f4-2a57a0d38934` |
| `eded9078-a7c9-58dc-89c8-2d529b4ccc7f` |
| `93c21955-8e13-51f0-a7ab-ea5ba67d0704` |
| `671690ce-f214-50c6-a535-9b4545acf8ba` |
| `9a819916-ce95-54fc-a184-e65769d03be3` |
