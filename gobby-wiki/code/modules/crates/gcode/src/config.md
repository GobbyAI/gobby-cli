---
title: crates/gcode/src/config
type: code_module
provenance:
- file: crates/gcode/src/config/context.rs
  ranges:
  - 26-31
  - '34'
  - '37'
  - 51-53
  - '55'
  - 58-63
  - 66-73
  - 75-82
  - 84-91
  - 93-100
  - 102-109
  - 111-118
  - 120-127
  - 131-133
  - 137-140
  - 143-151
  - 157-163
  - 168-191
  - 194-203
  - 206-209
  - 212-219
  - 222-229
  - 233-235
  - 237-302
  - 305-352
  - 355-408
  - 410-464
  - 466-474
  - 476-484
  - 486-494
  - 496-527
  - 529-536
  - 541-565
  - 567-569
  - 577-580
  - 582-618
  - 627-629
  - 631-639
- file: crates/gcode/src/config/services.rs
  ranges:
  - 20-22
  - 24-27
  - 29-39
  - 41-48
  - 51-57
  - 59-61
  - 64-67
  - 70-81
  - 83-85
  - 89-93
  - 95-99
  - 102-104
  - 108-125
  - 127-129
  - 132-135
  - 138-143
  - 150-162
  - 164-166
  - 169-178
  - 181-196
  - 199-221
  - 226-241
  - 244-247
  - 255-257
  - 259-261
  - 270-276
  - 278-280
  - 284-287
  - 295-301
  - 303-305
  - 309-322
  - 325-338
  - 341-354
  - 357-370
  - 373-384
  - 389-399
  - 401-416
  - 421-431
  - 433-442
  - 444-452
  - 454-469
  - 471-494
  - 501-511
  - 513-533
  - 535-545
  - 547-557
  - 559-568
  - 570-576
  - 578-587
  - 589-603
  - 605-611
  - 613-624
  - 626-635
- file: crates/gcode/src/config/tests.rs
  ranges:
  - 14-22
  - 24-38
  - 40-70
  - 80-90
  - 92-96
  - 100-140
  - 143-148
  - 152-166
  - 170-191
  - 195-229
  - 232-242
  - 246-268
  - 272-295
  - 299-313
  - 317-333
  - 336-348
  - 351-367
  - 370-389
  - 392-426
  - 429-449
  - 452-466
  - 469-500
  - 503-515
  - 518-529
  - 532-539
  - 542-553
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/config/context.rs:26-31](crates/gcode/src/config/context.rs#L26-L31), [crates/gcode/src/config/context.rs:34](crates/gcode/src/config/context.rs#L34), [crates/gcode/src/config/context.rs:37](crates/gcode/src/config/context.rs#L37), [crates/gcode/src/config/context.rs:51-53](crates/gcode/src/config/context.rs#L51-L53), [crates/gcode/src/config/context.rs:55](crates/gcode/src/config/context.rs#L55), [crates/gcode/src/config/context.rs:58-63](crates/gcode/src/config/context.rs#L58-L63), [crates/gcode/src/config/context.rs:66-73](crates/gcode/src/config/context.rs#L66-L73), [crates/gcode/src/config/context.rs:75-82](crates/gcode/src/config/context.rs#L75-L82), [crates/gcode/src/config/context.rs:84-91](crates/gcode/src/config/context.rs#L84-L91), [crates/gcode/src/config/context.rs:93-100](crates/gcode/src/config/context.rs#L93-L100), [crates/gcode/src/config/context.rs:102-109](crates/gcode/src/config/context.rs#L102-L109), [crates/gcode/src/config/context.rs:111-118](crates/gcode/src/config/context.rs#L111-L118), [crates/gcode/src/config/context.rs:120-127](crates/gcode/src/config/context.rs#L120-L127), [crates/gcode/src/config/context.rs:131-133](crates/gcode/src/config/context.rs#L131-L133), [crates/gcode/src/config/context.rs:137-140](crates/gcode/src/config/context.rs#L137-L140), [crates/gcode/src/config/context.rs:143-151](crates/gcode/src/config/context.rs#L143-L151), [crates/gcode/src/config/context.rs:157-163](crates/gcode/src/config/context.rs#L157-L163), [crates/gcode/src/config/context.rs:168-191](crates/gcode/src/config/context.rs#L168-L191), [crates/gcode/src/config/context.rs:194-203](crates/gcode/src/config/context.rs#L194-L203), [crates/gcode/src/config/context.rs:206-209](crates/gcode/src/config/context.rs#L206-L209), [crates/gcode/src/config/context.rs:212-219](crates/gcode/src/config/context.rs#L212-L219), [crates/gcode/src/config/context.rs:222-229](crates/gcode/src/config/context.rs#L222-L229), [crates/gcode/src/config/context.rs:233-235](crates/gcode/src/config/context.rs#L233-L235), [crates/gcode/src/config/context.rs:237-302](crates/gcode/src/config/context.rs#L237-L302), [crates/gcode/src/config/context.rs:305-352](crates/gcode/src/config/context.rs#L305-L352), [crates/gcode/src/config/context.rs:355-408](crates/gcode/src/config/context.rs#L355-L408), [crates/gcode/src/config/context.rs:410-464](crates/gcode/src/config/context.rs#L410-L464), [crates/gcode/src/config/context.rs:466-474](crates/gcode/src/config/context.rs#L466-L474), [crates/gcode/src/config/context.rs:476-484](crates/gcode/src/config/context.rs#L476-L484), [crates/gcode/src/config/context.rs:486-494](crates/gcode/src/config/context.rs#L486-L494), [crates/gcode/src/config/context.rs:496-527](crates/gcode/src/config/context.rs#L496-L527), [crates/gcode/src/config/context.rs:529-536](crates/gcode/src/config/context.rs#L529-L536), [crates/gcode/src/config/context.rs:541-565](crates/gcode/src/config/context.rs#L541-L565), [crates/gcode/src/config/context.rs:567-569](crates/gcode/src/config/context.rs#L567-L569), [crates/gcode/src/config/context.rs:577-580](crates/gcode/src/config/context.rs#L577-L580), [crates/gcode/src/config/context.rs:582-618](crates/gcode/src/config/context.rs#L582-L618), [crates/gcode/src/config/context.rs:627-629](crates/gcode/src/config/context.rs#L627-L629), [crates/gcode/src/config/context.rs:631-639](crates/gcode/src/config/context.rs#L631-L639)
- [crates/gcode/src/config/services.rs:20-22](crates/gcode/src/config/services.rs#L20-L22), [crates/gcode/src/config/services.rs:24-27](crates/gcode/src/config/services.rs#L24-L27), [crates/gcode/src/config/services.rs:29-39](crates/gcode/src/config/services.rs#L29-L39), [crates/gcode/src/config/services.rs:41-48](crates/gcode/src/config/services.rs#L41-L48), [crates/gcode/src/config/services.rs:51-57](crates/gcode/src/config/services.rs#L51-L57), [crates/gcode/src/config/services.rs:59-61](crates/gcode/src/config/services.rs#L59-L61), [crates/gcode/src/config/services.rs:64-67](crates/gcode/src/config/services.rs#L64-L67), [crates/gcode/src/config/services.rs:70-81](crates/gcode/src/config/services.rs#L70-L81), [crates/gcode/src/config/services.rs:83-85](crates/gcode/src/config/services.rs#L83-L85), [crates/gcode/src/config/services.rs:89-93](crates/gcode/src/config/services.rs#L89-L93), [crates/gcode/src/config/services.rs:95-99](crates/gcode/src/config/services.rs#L95-L99), [crates/gcode/src/config/services.rs:102-104](crates/gcode/src/config/services.rs#L102-L104), [crates/gcode/src/config/services.rs:108-125](crates/gcode/src/config/services.rs#L108-L125), [crates/gcode/src/config/services.rs:127-129](crates/gcode/src/config/services.rs#L127-L129), [crates/gcode/src/config/services.rs:132-135](crates/gcode/src/config/services.rs#L132-L135), [crates/gcode/src/config/services.rs:138-143](crates/gcode/src/config/services.rs#L138-L143), [crates/gcode/src/config/services.rs:150-162](crates/gcode/src/config/services.rs#L150-L162), [crates/gcode/src/config/services.rs:164-166](crates/gcode/src/config/services.rs#L164-L166), [crates/gcode/src/config/services.rs:169-178](crates/gcode/src/config/services.rs#L169-L178), [crates/gcode/src/config/services.rs:181-196](crates/gcode/src/config/services.rs#L181-L196), [crates/gcode/src/config/services.rs:199-221](crates/gcode/src/config/services.rs#L199-L221), [crates/gcode/src/config/services.rs:226-241](crates/gcode/src/config/services.rs#L226-L241), [crates/gcode/src/config/services.rs:244-247](crates/gcode/src/config/services.rs#L244-L247), [crates/gcode/src/config/services.rs:255-257](crates/gcode/src/config/services.rs#L255-L257), [crates/gcode/src/config/services.rs:259-261](crates/gcode/src/config/services.rs#L259-L261), [crates/gcode/src/config/services.rs:270-276](crates/gcode/src/config/services.rs#L270-L276), [crates/gcode/src/config/services.rs:278-280](crates/gcode/src/config/services.rs#L278-L280), [crates/gcode/src/config/services.rs:284-287](crates/gcode/src/config/services.rs#L284-L287), [crates/gcode/src/config/services.rs:295-301](crates/gcode/src/config/services.rs#L295-L301), [crates/gcode/src/config/services.rs:303-305](crates/gcode/src/config/services.rs#L303-L305), [crates/gcode/src/config/services.rs:309-322](crates/gcode/src/config/services.rs#L309-L322), [crates/gcode/src/config/services.rs:325-338](crates/gcode/src/config/services.rs#L325-L338), [crates/gcode/src/config/services.rs:341-354](crates/gcode/src/config/services.rs#L341-L354), [crates/gcode/src/config/services.rs:357-370](crates/gcode/src/config/services.rs#L357-L370), [crates/gcode/src/config/services.rs:373-384](crates/gcode/src/config/services.rs#L373-L384), [crates/gcode/src/config/services.rs:389-399](crates/gcode/src/config/services.rs#L389-L399), [crates/gcode/src/config/services.rs:401-416](crates/gcode/src/config/services.rs#L401-L416), [crates/gcode/src/config/services.rs:421-431](crates/gcode/src/config/services.rs#L421-L431), [crates/gcode/src/config/services.rs:433-442](crates/gcode/src/config/services.rs#L433-L442), [crates/gcode/src/config/services.rs:444-452](crates/gcode/src/config/services.rs#L444-L452), [crates/gcode/src/config/services.rs:454-469](crates/gcode/src/config/services.rs#L454-L469), [crates/gcode/src/config/services.rs:471-494](crates/gcode/src/config/services.rs#L471-L494), [crates/gcode/src/config/services.rs:501-511](crates/gcode/src/config/services.rs#L501-L511), [crates/gcode/src/config/services.rs:513-533](crates/gcode/src/config/services.rs#L513-L533), [crates/gcode/src/config/services.rs:535-545](crates/gcode/src/config/services.rs#L535-L545), [crates/gcode/src/config/services.rs:547-557](crates/gcode/src/config/services.rs#L547-L557), [crates/gcode/src/config/services.rs:559-568](crates/gcode/src/config/services.rs#L559-L568), [crates/gcode/src/config/services.rs:570-576](crates/gcode/src/config/services.rs#L570-L576), [crates/gcode/src/config/services.rs:578-587](crates/gcode/src/config/services.rs#L578-L587), [crates/gcode/src/config/services.rs:589-603](crates/gcode/src/config/services.rs#L589-L603), [crates/gcode/src/config/services.rs:605-611](crates/gcode/src/config/services.rs#L605-L611), [crates/gcode/src/config/services.rs:613-624](crates/gcode/src/config/services.rs#L613-L624), [crates/gcode/src/config/services.rs:626-635](crates/gcode/src/config/services.rs#L626-L635)
- [crates/gcode/src/config/tests.rs:14-22](crates/gcode/src/config/tests.rs#L14-L22), [crates/gcode/src/config/tests.rs:24-38](crates/gcode/src/config/tests.rs#L24-L38), [crates/gcode/src/config/tests.rs:40-70](crates/gcode/src/config/tests.rs#L40-L70), [crates/gcode/src/config/tests.rs:80-90](crates/gcode/src/config/tests.rs#L80-L90), [crates/gcode/src/config/tests.rs:92-96](crates/gcode/src/config/tests.rs#L92-L96), [crates/gcode/src/config/tests.rs:100-140](crates/gcode/src/config/tests.rs#L100-L140), [crates/gcode/src/config/tests.rs:143-148](crates/gcode/src/config/tests.rs#L143-L148), [crates/gcode/src/config/tests.rs:152-166](crates/gcode/src/config/tests.rs#L152-L166), [crates/gcode/src/config/tests.rs:170-191](crates/gcode/src/config/tests.rs#L170-L191), [crates/gcode/src/config/tests.rs:195-229](crates/gcode/src/config/tests.rs#L195-L229), [crates/gcode/src/config/tests.rs:232-242](crates/gcode/src/config/tests.rs#L232-L242), [crates/gcode/src/config/tests.rs:246-268](crates/gcode/src/config/tests.rs#L246-L268), [crates/gcode/src/config/tests.rs:272-295](crates/gcode/src/config/tests.rs#L272-L295), [crates/gcode/src/config/tests.rs:299-313](crates/gcode/src/config/tests.rs#L299-L313), [crates/gcode/src/config/tests.rs:317-333](crates/gcode/src/config/tests.rs#L317-L333), [crates/gcode/src/config/tests.rs:336-348](crates/gcode/src/config/tests.rs#L336-L348), [crates/gcode/src/config/tests.rs:351-367](crates/gcode/src/config/tests.rs#L351-L367), [crates/gcode/src/config/tests.rs:370-389](crates/gcode/src/config/tests.rs#L370-L389), [crates/gcode/src/config/tests.rs:392-426](crates/gcode/src/config/tests.rs#L392-L426), [crates/gcode/src/config/tests.rs:429-449](crates/gcode/src/config/tests.rs#L429-L449), [crates/gcode/src/config/tests.rs:452-466](crates/gcode/src/config/tests.rs#L452-L466), [crates/gcode/src/config/tests.rs:469-500](crates/gcode/src/config/tests.rs#L469-L500), [crates/gcode/src/config/tests.rs:503-515](crates/gcode/src/config/tests.rs#L503-L515), [crates/gcode/src/config/tests.rs:518-529](crates/gcode/src/config/tests.rs#L518-L529), [crates/gcode/src/config/tests.rs:532-539](crates/gcode/src/config/tests.rs#L532-L539), [crates/gcode/src/config/tests.rs:542-553](crates/gcode/src/config/tests.rs#L542-L553)

</details>

# crates/gcode/src/config

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The crates/gcode/src/config module centralizes configuration resolution, project identity detection, and service-layer provisioning for gcode. It handles workspace root detection, project-name lookups, parent-index validation, ID normalization, and fallbacks for workspace settings and git worktrees crates/gcode/src/config/context.rs:51-53, crates/gcode/src/config/context.rs:55. The configuration pipeline resolves settings sequentially by reading bootstrap settings, standalone configuration files, environment variables, and live Postgres-backed configs, while also expanding dynamic secret or variable patterns crates/gcode/src/config/context.rs:1-5, crates/gcode/src/config/services.rs:20-22.

The module collaborates heavily with Postgres database clients to query config values and resolve secrets crates/gcode/src/config/services.rs:51-57. It integrates with gobby_core to reuse shared configuration structures (such as Qdrant, embeddings, and indexing settings) and provisioning helpers crates/gcode/src/config/services.rs:1-4, crates/gcode/src/config/context.rs:34-37. It also works in tandem with local git repositories to parse worktrees during project-identity resolution crates/gcode/src/config/tests.rs:40-70.

### Environment Variables
| Environment Variable | Description |
| --- | --- |
| GOBBY_FALKORDB_HOST | Host address for FalkorDB crates/gcode/src/config/context.rs:14, crates/gcode/src/config/context.rs:37 |
| GOBBY_FALKORDB_PORT | Port for FalkorDB crates/gcode/src/config/context.rs:14, crates/gcode/src/config/context.rs:37 |
| GOBBY_FALKORDB_PASSWORD | Password for FalkorDB crates/gcode/src/config/context.rs:14, crates/gcode/src/config/context.rs:37 |
| GOBBY_QDRANT_URL | URL endpoint for Qdrant database crates/gcode/src/config/services.rs:34 |
| GOBBY_QDRANT_API_KEY | API key for Qdrant database crates/gcode/src/config/services.rs:35 |

### Configuration Keys
| Configuration Key | Description |
| --- | --- |
| databases.falkordb.host | Database host configuration key for FalkorDB crates/gcode/src/config/context.rs:14, crates/gcode/src/config/context.rs:40 |
| databases.falkordb.port | Database port configuration key for FalkorDB crates/gcode/src/config/context.rs:14, crates/gcode/src/config/context.rs:41 |
| databases.falkordb.password | Database password configuration key for FalkorDB crates/gcode/src/config/context.rs:14, crates/gcode/src/config/context.rs:42 |
| databases.qdrant.url | Configuration key for Qdrant URL crates/gcode/src/config/services.rs:34 |
| databases.qdrant.api_key | Configuration key for Qdrant API key crates/gcode/src/config/services.rs:35 |

### Public API Symbols
| Symbol | Type | Description |
| --- | --- | --- |
| FalkorConfig | Struct | Represents FalkorDB connection configuration crates/gcode/src/config/context.rs:26-31 |
| QdrantConfig | Type Alias | Connection configuration for Qdrant crates/gcode/src/config/context.rs:34 |
| EmbeddingConfig | Type Alias | Embedding API configuration (OpenAI-compatible) crates/gcode/src/config/context.rs:37 |
| IndexingSettings | Type Alias | Type alias for gobby_core indexing configuration crates/gcode/src/config/context.rs:48 |
| CodeVectorSettings | Struct | Configuration for vector dimension settings crates/gcode/src/config/context.rs:44-47 |
| ServiceConfigSelection | Struct | Grouped toggles to selectively filter database, vector, or embedding services crates/gcode/src/config/context.rs:51-53 |
| FALKORDB_GRAPH_NAME | Constant | Name of the FalkorDB code graph crates/gcode/src/config/context.rs:11, crates/gcode/src/config/context.rs:38 |
| CODE_SYMBOL_COLLECTION_PREFIX | Constant | Prefix string used for symbol collections crates/gcode/src/config/context.rs:39 |
[crates/gcode/src/config/context.rs:26-31]
[crates/gcode/src/config/services.rs:20-22]
[crates/gcode/src/config/tests.rs:14-22]
[crates/gcode/src/config/context.rs:34]
[crates/gcode/src/config/context.rs:37]

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/config/context.rs\|crates/gcode/src/config/context.rs]] | This file centralizes gcode’s configuration resolution. It defines the local FalkorDB connection struct plus type aliases for Qdrant, embedding, and indexing configs, then groups service toggles in `ServiceConfigSelection` so callers can request all services or just subsets like database, vectors, or hybrid search. The `Context` and project-identity types drive resolution of a project’s config from bootstrap and workspace state, while the helper functions handle root detection, project-name lookup, parent-index validation, ID normalization, and fallback behavior when the project cannot be resolved cleanly. [crates/gcode/src/config/context.rs:26-31] [crates/gcode/src/config/context.rs:34] [crates/gcode/src/config/context.rs:37] [crates/gcode/src/config/context.rs:51-53] [crates/gcode/src/config/context.rs:55] |
| [[code/files/crates/gcode/src/config/services.rs\|crates/gcode/src/config/services.rs]] | Provides the service-configuration layer for Gobby, resolving runtime settings from Postgres-backed config, environment variables, standalone config files, and fallbacks. The file defines a small `ServiceConfigSource` abstraction plus concrete sources and helpers that read raw values, detect missing config stores, resolve secret references, and then assemble validated service configs for FalkorDB, Qdrant, embeddings, code-vector settings, and indexing, including parsing and normalization such as ports and vector dimensions. [crates/gcode/src/config/services.rs:20-22] [crates/gcode/src/config/services.rs:24-27] [crates/gcode/src/config/services.rs:29-39] [crates/gcode/src/config/services.rs:41-48] [crates/gcode/src/config/services.rs:51-57] |
| [[code/files/crates/gcode/src/config/tests.rs\|crates/gcode/src/config/tests.rs]] | Test module for `gcode` config resolution. It defines small fixtures for writing `.gobby/project.json`, running git, creating linked worktrees, and temporarily overriding service env vars, then uses them to verify config behavior across adapter/env precedence, project-name and project-id resolution, daemon URL derivation, secret and embedding config handling, service-specific settings for FalkorDB and Qdrant, invalid port fallback, and a range of project identity cases for main repos, isolated markers, linked worktrees, and empty IDs. [crates/gcode/src/config/tests.rs:14-22] [crates/gcode/src/config/tests.rs:24-38] [crates/gcode/src/config/tests.rs:40-70] [crates/gcode/src/config/tests.rs:80-90] [crates/gcode/src/config/tests.rs:92-96] |

## Components

| Component ID |
| --- |
| `53926106-6dfb-54e8-98e8-fba4322e5dec` |
| `64da5dd7-9a46-54c3-856e-22934520004d` |
| `fa989081-e16b-5255-84da-f2e8958ca42c` |
| `3c239d5c-acad-5519-8278-7872a54e5164` |
| `375d916b-30e4-55bb-9471-2f963f005197` |
| `8627d53f-73ba-53a7-8e99-16b027b0b43a` |
| `c9a1cb62-7c8b-5590-91d0-babf0631b4b8` |
| `b42e3e41-716a-5888-9afa-b816f1a85ee2` |
| `41215555-256a-53a5-8d44-c0787823aade` |
| `d44cbbc0-04e9-56bf-91ba-8ba562319e21` |
| `3349fe55-9b04-504a-a9e7-3bdfb5e169b9` |
| `03212a41-cc6c-5713-b627-83a209fc66e2` |
| `d131f6ff-2354-5288-bd28-36e855c70efe` |
| `308f7c78-476f-5d36-850a-328dc71dc624` |
| `3d9e9087-b154-567a-8eb9-dad0ec7045f5` |
| `c28ef263-af5a-5965-8ea5-195137ce9fb8` |
| `e024baa0-26a9-57fd-8f01-3454080ca15f` |
| `f57e9fb3-ef45-5bc0-8ec7-a20ecf40b698` |
| `7a5353d3-da7f-5160-9017-b32e9548aab8` |
| `d0fce310-84e4-5d23-bbaa-1e8dc55ac538` |
| `bff5f934-378e-5722-a8c7-aa3e45ab5c5f` |
| `4328c2c8-aef6-57af-8d4d-acda4afbab80` |
| `79949d65-3a16-5c20-bbf0-6e5df87b1e62` |
| `e95640c9-aa2f-5ba7-bba7-48ae9a58781d` |
| `e28cf06f-8d8a-5d73-9aa4-448c153e5282` |
| `c16a506e-0836-521f-a333-18c58479e2e7` |
| `be53020f-4090-5a99-b3eb-175cf5b8f008` |
| `339b011b-98d8-5d8f-b836-5a3b8cfe16ef` |
| `2a22b831-610e-5442-851e-1104373160e0` |
| `dfaf96cb-f000-58e3-8505-e26501faf934` |
| `5bd35579-5aa2-5c54-9998-165847b805f4` |
| `e921ff52-bfd9-5e31-91e8-098ebc78d498` |
| `c101f802-bb35-546d-993d-93a6bdfd6d98` |
| `f1dfe0c1-ecba-554b-9da6-94fcd8493113` |
| `edb5edf1-6aa4-5169-87ea-afc33b1a6031` |
| `bd38792f-4fe7-5434-877a-a315c412dedd` |
| `7e538a11-cd71-5054-a07b-62f379c3fcd2` |
| `610ff3cd-6440-5be0-ab50-d864c640c089` |
| `2b5627ba-b022-5c99-835a-10b3270e595a` |
| `376426c5-af74-5515-b43e-71c79b27ab8e` |
| `8c73cf1c-116b-549f-a285-656fb12318b7` |
| `a1772b25-eb88-5555-acb1-3c9813b557a8` |
| `80bdc425-dbd1-58ce-b569-e6e623d260d5` |
| `802f41f9-6958-57bc-9239-5b29484e96c1` |
| `2b6de914-554a-5521-85c1-34566ed0e76f` |
| `3308f5d4-fe0e-5ddd-86b0-1a239ad5cbc4` |
| `195d3c75-4fd1-5d55-a58d-080bc7eadcdc` |
| `bb3b2b04-75d3-55ea-8326-7ed800d721f2` |
| `f7c3b020-528e-516b-9c1d-e31527b7bc42` |
| `2fb164b7-eb7d-54c7-bd56-0099afebd78b` |
| `481ab8e0-920d-5092-82f8-60e726ec5b68` |
| `f022087b-8ec1-5b21-933f-28275f1a9573` |
| `59d8cbb2-3be8-53e7-abbb-6ec9ef356504` |
| `000f4592-81ca-57d8-9950-f933ff4a3b5b` |
| `d72d83bd-5aba-5c26-9d16-8cf00cb01d4c` |
| `8dad6043-0fc8-5236-8061-0fc3a429e032` |
| `8331635c-e2f7-5a97-9965-1d6d996826fe` |
| `254de7ef-9797-5f6a-9ca7-c0aa8622aaaa` |
| `da9d2337-c68c-5956-836f-8bf397465272` |
| `8eb27418-fb2b-5858-97d5-ecd8a1d2c31d` |
| `5e91dc97-455d-5172-9d43-060d723ef1b0` |
| `4b90bf43-1cac-5d65-8f5e-0f85ba3713e2` |
| `e9344c04-d2a9-5560-b9ea-55e565b88e79` |
| `1c0fa5fa-a8b0-5b8b-8d48-e43da3c43b16` |
| `d727e622-20ad-5169-8567-28f4c0624627` |
| `dbbe6486-153b-5779-9a08-bd7aa071b2bd` |
| `d2fc1ff4-a198-505e-af3e-b2a9ef8899d1` |
| `0e207cc9-a653-5aea-ba44-60ecfbfed306` |
| `cc9828a3-8814-52a1-b87c-59e38dc98650` |
| `9aba8a5f-536d-5453-b5ce-7771f6fb29e8` |
| `9330a412-575b-5152-a1cf-135a7f308e3a` |
| `e103c19a-2c6c-527b-9159-a254b6795001` |
| `c13ee5b5-4dea-5d41-a3c4-6e3f6ec63209` |
| `c5730274-e339-57fc-bc15-d5abfecf7c0f` |
| `1f13e8b8-ed66-50e9-99cf-6e6a742d4c0c` |
| `a4e3d0c0-846c-53fa-adc2-c86422c8ebb6` |
| `bdf63c4f-b439-55e6-b850-a837b76becdb` |
| `a5a01ca9-8086-52b4-97c9-132d324c6f85` |
| `c90f25cf-fbe0-5ed0-b097-77ef348556d1` |
| `9138da44-4687-593a-95c5-29b8cbd7391a` |
| `025b4846-7970-5700-99f0-0ccabc7ebfc4` |
| `b0c9bb0b-c7a0-5542-bd3c-95f25dd812df` |
| `ac53669b-29ee-5344-acd8-336ad0104d53` |
| `28c47d46-bd7b-5133-b7c7-372cfc12895e` |
| `73a8e787-c170-5e1d-82eb-c9430da704fd` |
| `43346b4a-a439-52fb-b995-db9d5f53bc03` |
| `3a3fcf9e-3bc0-592a-936a-6c4014fc535f` |
| `89da399d-3b25-55ce-a12e-30c060540b8c` |
| `a3104df3-262f-55d2-b96d-e90615651334` |
| `6b815bbb-2a31-5fae-9311-56606fe1ad6b` |
| `688cb87e-bc31-5fda-a82d-3fd925232ac4` |
| `595fac55-0d4e-55e5-b2fd-69fe49196253` |
| `f7f4f1d9-0ff8-51db-b7e9-3b84c3dc6657` |
| `e65d015b-ff27-55ad-991f-4d67c5588b34` |
| `80b86ae0-52b6-557e-a3f7-fcd29acbffbd` |
| `99326af5-69bd-5565-bee6-cb3375d238ae` |
| `9681c9c5-f04e-5c15-8d67-f0a4b2222fcf` |
| `76c2c53a-d210-5ce2-bcda-aef0b42e95eb` |
| `4b1d863f-178d-5c97-bd65-0beb804d2ac0` |
| `de39c51f-2749-5cc4-97e4-f187d47b7e0f` |
| `e96521b6-6626-5d1d-ab17-986f939c4f9e` |
| `61f1f75a-f159-5d07-8627-5cbc4cd12085` |
| `d1cfe3e5-dc7e-5baa-a4fe-e01a042e81c5` |
| `0726e300-44c4-51cc-abca-bed13666836f` |
| `3ece38b5-268b-5b8a-9823-117d1d053be8` |
| `011a0baa-dc8d-5b8e-b0e9-cb9f4295edb3` |
| `4df88ecd-d98f-5d27-9a58-10523f89bb89` |
| `1e617892-a520-5f9d-9b5b-6e2cc90d5955` |
| `2ac646f0-7ad2-54bd-969e-9f0be46734dc` |
| `037d8ca9-2112-5a2a-a6d8-fc5b94b97da4` |
| `7510b96a-1e28-5409-89e9-379edd8b0db1` |
| `af143919-a523-5668-8fd1-a757b2fa9dab` |
| `7077a1e9-c8c5-5aa6-b33f-5fdf2f8ffb01` |
| `dc387555-af78-5649-a814-00dbc63decf2` |
| `e216bc71-c4fa-5991-b8b5-7b706c63c732` |
| `cb578de5-07c5-5f19-817c-1030bfdbb004` |
| `8232a947-be72-558b-90b5-50239e68e7cd` |
| `ca3dbc67-f876-5738-a3c6-e21d730d6c3d` |
