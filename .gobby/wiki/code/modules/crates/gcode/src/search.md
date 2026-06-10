---
title: crates/gcode/src/search
type: code_module
provenance:
- file: crates/gcode/src/search/fts/common.rs
  ranges:
  - '16'
  - 19-22
  - 25-29
  - 32-36
  - 38-54
  - 39-53
  - 56-59
  - 63-69
  - 71-76
  - 78-86
  - 88-123
  - 126-135
  - 138-148
  - 150-152
  - 154-175
  - 177-184
  - 186-196
  - 198-200
  - 202-233
  - 235-250
  - 252-272
  - 274-291
  - 293-341
  - 348-354
  - 357-362
- file: crates/gcode/src/search/fts/content.rs
  ranges:
  - 13-21
  - 24-81
  - 83-138
  - 140-178
  - 180-196
  - 199-202
  - 204-210
  - 212-227
  - 229-244
  - 250-253
  - 256-261
  - 264-269
- file: crates/gcode/src/search/fts/counts.rs
  ranges:
  - 10-66
  - 69-113
  - 115-146
  - 148-164
  - 166-191
  - 193-243
  - 245-259
  - 261-273
  - 275-294
  - 296-307
  - 309-333
  - 335-359
  - 366-385
- file: crates/gcode/src/search/fts/graph.rs
  ranges:
  - 16-50
  - 52-55
  - 57-62
  - 64-69
  - 71-78
  - 80-96
  - 98-103
  - 108-147
- file: crates/gcode/src/search/fts/symbols.rs
  ranges:
  - 15-18
  - 21-26
  - 28-33
  - 36-73
  - 76-112
  - 114-190
  - 192-225
  - 227-260
  - 262-337
  - 339-371
  - 374-386
  - 388-401
- file: crates/gcode/src/search/fts/tests.rs
  ranges:
  - 17-26
  - 29-34
  - 37-43
  - 46-49
  - 52-57
  - 60-72
  - 75-81
  - 84-99
  - 102-133
  - 136-142
  - 145-151
  - 154-166
  - 173-207
  - 211-239
  - 242-257
  - 260-269
  - 272-281
  - 283-302
  - 304-308
  - 310-319
  - 311-318
  - 321-325
  - 327-336
  - 328-335
  - 338-342
  - 339-341
  - 344-347
  - 349-355
  - 350-354
  - 357-360
  - 362-364
  - 366-380
  - 382-470
  - 472-480
  - 482-499
  - 501-514
  - 516-533
  - 535-554
- file: crates/gcode/src/search/graph_boost.rs
  ranges:
  - 21-47
  - 55-86
  - 88-106
  - 113-127
  - 129-153
  - 156-160
  - 163-167
  - 170-174
  - 177-223
- file: crates/gcode/src/search/rrf.rs
  ranges:
  - '7'
  - 15-20
  - 27-34
  - 37-49
  - 52-64
  - 67-75
  - 78-81
  - 84-87
  - 90-113
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

Provides comprehensive search functionality for the GCode crate, leveraging PostgreSQL for full-text search (FTS) with BM25 relevance scoring, snippet generation, and advanced path/glob filtering. The module orchestrates result ranking and merging through graph-aware boosting and Reciprocal Rank Fusion (RRF). It exposes utilities for query construction, visibility predicate management, graph symbol resolution, and path expansion, alongside extensive test fixtures for validating search behavior, scoring, and database interactions.
[crates/gcode/src/search/fts/common.rs:16]
[crates/gcode/src/search/fts/common.rs:19-22]
[crates/gcode/src/search/fts/common.rs:25-29]
[crates/gcode/src/search/fts/common.rs:32-36]
[crates/gcode/src/search/fts/common.rs:38-54]
[crates/gcode/src/search/fts/common.rs:39-53]
[crates/gcode/src/search/fts/common.rs:56-59]
[crates/gcode/src/search/fts/common.rs:63-69]
[crates/gcode/src/search/fts/common.rs:71-76]
[crates/gcode/src/search/fts/common.rs:78-86]
[crates/gcode/src/search/fts/common.rs:88-123]
[crates/gcode/src/search/fts/common.rs:126-135]
[crates/gcode/src/search/fts/common.rs:138-148]
[crates/gcode/src/search/fts/common.rs:150-152]
[crates/gcode/src/search/fts/common.rs:154-175]
[crates/gcode/src/search/fts/common.rs:177-184]
[crates/gcode/src/search/fts/common.rs:186-196]
[crates/gcode/src/search/fts/common.rs:198-200]
[crates/gcode/src/search/fts/common.rs:202-233]
[crates/gcode/src/search/fts/common.rs:235-250]
[crates/gcode/src/search/fts/common.rs:252-272]
[crates/gcode/src/search/fts/common.rs:274-291]
[crates/gcode/src/search/fts/common.rs:293-341]
[crates/gcode/src/search/fts/common.rs:348-354]
[crates/gcode/src/search/fts/common.rs:357-362]
[crates/gcode/src/search/fts/content.rs:13-21]
[crates/gcode/src/search/fts/content.rs:24-81]
[crates/gcode/src/search/fts/content.rs:83-138]
[crates/gcode/src/search/fts/content.rs:140-178]
[crates/gcode/src/search/fts/content.rs:180-196]
[crates/gcode/src/search/fts/content.rs:199-202]
[crates/gcode/src/search/fts/content.rs:204-210]
[crates/gcode/src/search/fts/content.rs:212-227]
[crates/gcode/src/search/fts/content.rs:229-244]
[crates/gcode/src/search/fts/content.rs:250-253]
[crates/gcode/src/search/fts/content.rs:256-261]
[crates/gcode/src/search/fts/content.rs:264-269]
[crates/gcode/src/search/fts/counts.rs:10-66]
[crates/gcode/src/search/fts/counts.rs:69-113]
[crates/gcode/src/search/fts/counts.rs:115-146]
[crates/gcode/src/search/fts/counts.rs:148-164]
[crates/gcode/src/search/fts/counts.rs:166-191]
[crates/gcode/src/search/fts/counts.rs:193-243]
[crates/gcode/src/search/fts/counts.rs:245-259]
[crates/gcode/src/search/fts/counts.rs:261-273]
[crates/gcode/src/search/fts/counts.rs:275-294]
[crates/gcode/src/search/fts/counts.rs:296-307]
[crates/gcode/src/search/fts/counts.rs:309-333]
[crates/gcode/src/search/fts/counts.rs:335-359]
[crates/gcode/src/search/fts/counts.rs:366-385]
[crates/gcode/src/search/fts/graph.rs:16-50]
[crates/gcode/src/search/fts/graph.rs:52-55]
[crates/gcode/src/search/fts/graph.rs:57-62]
[crates/gcode/src/search/fts/graph.rs:64-69]
[crates/gcode/src/search/fts/graph.rs:71-78]
[crates/gcode/src/search/fts/graph.rs:80-96]
[crates/gcode/src/search/fts/graph.rs:98-103]
[crates/gcode/src/search/fts/graph.rs:108-147]
[crates/gcode/src/search/fts/symbols.rs:15-18]
[crates/gcode/src/search/fts/symbols.rs:21-26]
[crates/gcode/src/search/fts/symbols.rs:28-33]
[crates/gcode/src/search/fts/symbols.rs:36-73]
[crates/gcode/src/search/fts/symbols.rs:76-112]
[crates/gcode/src/search/fts/symbols.rs:114-190]
[crates/gcode/src/search/fts/symbols.rs:192-225]
[crates/gcode/src/search/fts/symbols.rs:227-260]
[crates/gcode/src/search/fts/symbols.rs:262-337]
[crates/gcode/src/search/fts/symbols.rs:339-371]
[crates/gcode/src/search/fts/symbols.rs:374-386]
[crates/gcode/src/search/fts/symbols.rs:388-401]
[crates/gcode/src/search/fts/tests.rs:17-26]
[crates/gcode/src/search/fts/tests.rs:29-34]
[crates/gcode/src/search/fts/tests.rs:37-43]
[crates/gcode/src/search/fts/tests.rs:46-49]
[crates/gcode/src/search/fts/tests.rs:52-57]
[crates/gcode/src/search/fts/tests.rs:60-72]
[crates/gcode/src/search/fts/tests.rs:75-81]
[crates/gcode/src/search/fts/tests.rs:84-99]
[crates/gcode/src/search/fts/tests.rs:102-133]
[crates/gcode/src/search/fts/tests.rs:136-142]
[crates/gcode/src/search/fts/tests.rs:145-151]
[crates/gcode/src/search/fts/tests.rs:154-166]
[crates/gcode/src/search/fts/tests.rs:173-207]
[crates/gcode/src/search/fts/tests.rs:211-239]
[crates/gcode/src/search/fts/tests.rs:242-257]
[crates/gcode/src/search/fts/tests.rs:260-269]
[crates/gcode/src/search/fts/tests.rs:272-281]
[crates/gcode/src/search/fts/tests.rs:283-302]
[crates/gcode/src/search/fts/tests.rs:304-308]
[crates/gcode/src/search/fts/tests.rs:310-319]
[crates/gcode/src/search/fts/tests.rs:311-318]
[crates/gcode/src/search/fts/tests.rs:321-325]
[crates/gcode/src/search/fts/tests.rs:327-336]
[crates/gcode/src/search/fts/tests.rs:328-335]
[crates/gcode/src/search/fts/tests.rs:338-342]
[crates/gcode/src/search/fts/tests.rs:339-341]
[crates/gcode/src/search/fts/tests.rs:344-347]
[crates/gcode/src/search/fts/tests.rs:349-355]
[crates/gcode/src/search/fts/tests.rs:350-354]
[crates/gcode/src/search/fts/tests.rs:357-360]
[crates/gcode/src/search/fts/tests.rs:362-364]
[crates/gcode/src/search/fts/tests.rs:366-380]
[crates/gcode/src/search/fts/tests.rs:382-470]
[crates/gcode/src/search/fts/tests.rs:472-480]
[crates/gcode/src/search/fts/tests.rs:482-499]
[crates/gcode/src/search/fts/tests.rs:501-514]
[crates/gcode/src/search/fts/tests.rs:516-533]
[crates/gcode/src/search/fts/tests.rs:535-554]
[crates/gcode/src/search/graph_boost.rs:21-47]
[crates/gcode/src/search/graph_boost.rs:55-86]
[crates/gcode/src/search/graph_boost.rs:88-106]
[crates/gcode/src/search/graph_boost.rs:113-127]
[crates/gcode/src/search/graph_boost.rs:129-153]
[crates/gcode/src/search/graph_boost.rs:156-160]
[crates/gcode/src/search/graph_boost.rs:163-167]
[crates/gcode/src/search/graph_boost.rs:170-174]
[crates/gcode/src/search/graph_boost.rs:177-223]
[crates/gcode/src/search/rrf.rs:7]
[crates/gcode/src/search/rrf.rs:15-20]
[crates/gcode/src/search/rrf.rs:27-34]
[crates/gcode/src/search/rrf.rs:37-49]
[crates/gcode/src/search/rrf.rs:52-64]
[crates/gcode/src/search/rrf.rs:67-75]
[crates/gcode/src/search/rrf.rs:78-81]
[crates/gcode/src/search/rrf.rs:84-87]
[crates/gcode/src/search/rrf.rs:90-113]

## Call Diagram

```mermaid
sequenceDiagram
    participant m_22a35146_0b3d_5a8b_a030_3da3a66883cd as test_merge_single_source &#91;function&#93;
    participant m_239158ff_3daf_584d_b001_791e25c54319 as merge_delegates_to_gobby_core_rrf &#91;function&#93;
    participant m_2cd40db1_4e53_5de4_be24_7b59e0b83a43 as graph_expand &#91;function&#93;
    participant m_58647f00_fd39_5646_bad7_155c0cbd79f2 as test_merge_sorts_sources_deterministically &#91;function&#93;
    participant m_752226a9_8b51_5e80_97ec_354312b73330 as graph_expand_grouped_expands_each_project_scope_and_dedupes &#91;function&#93;
    participant m_76109a10_3a96_55e7_bf6b_0ebfdd2fcb4a as test_merge_empty_sources &#91;function&#93;
    participant m_821967f5_60ed_567d_b11d_f9cfb2726a60 as graph_boost &#91;function&#93;
    participant m_84046dbc_3560_568e_a490_df5f55d17f96 as test_merge_two_sources_disjoint &#91;function&#93;
    participant m_873d4c1e_dd07_58fe_a832_e784dabd9689 as test_merge_two_sources_same_ids &#91;function&#93;
    participant m_8cb6830f_e7a6_5d3f_b87c_ad56c1e35dd1 as test_merge_empty_id_lists &#91;function&#93;
    participant m_8e07f24c_1345_5ff2_b99b_fa4256b92f7a as make_ctx_with_overlay &#91;function&#93;
    participant m_8e475747_c493_5cc6_a3e7_f86a684ba506 as test_graph_expand_no_falkordb &#91;function&#93;
    participant m_cdbdd7fb_61d4_5e31_b2bb_b1e42758c75a as graph_expand_grouped &#91;function&#93;
    participant m_d0070db0_0756_5591_97c0_c2b4fa4bd3f2 as test_graph_expand_empty_seeds &#91;function&#93;
    participant m_d2b29a0f_7fa5_5865_a104_83fe2cdd3eef as test_graph_boost_no_falkordb &#91;function&#93;
    participant m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5 as merge &#91;function&#93;
    participant m_fce20da6_a98f_553e_bfa7_bec5b8685476 as make_ctx_no_falkordb &#91;function&#93;
    m_22a35146_0b3d_5a8b_a030_3da3a66883cd->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_239158ff_3daf_584d_b001_791e25c54319->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_2cd40db1_4e53_5de4_be24_7b59e0b83a43->>m_cdbdd7fb_61d4_5e31_b2bb_b1e42758c75a: calls
    m_58647f00_fd39_5646_bad7_155c0cbd79f2->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_752226a9_8b51_5e80_97ec_354312b73330->>m_8e07f24c_1345_5ff2_b99b_fa4256b92f7a: calls
    m_752226a9_8b51_5e80_97ec_354312b73330->>m_cdbdd7fb_61d4_5e31_b2bb_b1e42758c75a: calls
    m_76109a10_3a96_55e7_bf6b_0ebfdd2fcb4a->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_84046dbc_3560_568e_a490_df5f55d17f96->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_873d4c1e_dd07_58fe_a832_e784dabd9689->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_8cb6830f_e7a6_5d3f_b87c_ad56c1e35dd1->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_8e475747_c493_5cc6_a3e7_f86a684ba506->>m_2cd40db1_4e53_5de4_be24_7b59e0b83a43: calls
    m_8e475747_c493_5cc6_a3e7_f86a684ba506->>m_fce20da6_a98f_553e_bfa7_bec5b8685476: calls
    m_d0070db0_0756_5591_97c0_c2b4fa4bd3f2->>m_2cd40db1_4e53_5de4_be24_7b59e0b83a43: calls
    m_d0070db0_0756_5591_97c0_c2b4fa4bd3f2->>m_fce20da6_a98f_553e_bfa7_bec5b8685476: calls
    m_d2b29a0f_7fa5_5865_a104_83fe2cdd3eef->>m_821967f5_60ed_567d_b11d_f9cfb2726a60: calls
    m_d2b29a0f_7fa5_5865_a104_83fe2cdd3eef->>m_fce20da6_a98f_553e_bfa7_bec5b8685476: calls
```

## Child Modules

- [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]] - This module implements full-text search (FTS) functionality for the GCode crate, primarily leveraging PostgreSQL's FTS engine. It provides core search operations for symbols, file contents, and raw text, featuring BM25 relevance scoring, snippet generation, and advanced path/glob filtering. The module handles query construction, visibility predicates, and graph symbol resolution, while tests.rs contains comprehensive validation and fixture management for search behavior, scoring, and database interactions.
[crates/gcode/src/search/fts/common.rs:16]
[crates/gcode/src/search/fts/common.rs:19-22]
[crates/gcode/src/search/fts/common.rs:25-29]
[crates/gcode/src/search/fts/common.rs:32-36]
[crates/gcode/src/search/fts/common.rs:38-54]
[crates/gcode/src/search/fts/common.rs:39-53]
[crates/gcode/src/search/fts/common.rs:56-59]
[crates/gcode/src/search/fts/common.rs:63-69]
[crates/gcode/src/search/fts/common.rs:71-76]
[crates/gcode/src/search/fts/common.rs:78-86]
[crates/gcode/src/search/fts/common.rs:88-123]
[crates/gcode/src/search/fts/common.rs:126-135]
[crates/gcode/src/search/fts/common.rs:138-148]
[crates/gcode/src/search/fts/common.rs:150-152]
[crates/gcode/src/search/fts/common.rs:154-175]
[crates/gcode/src/search/fts/common.rs:177-184]
[crates/gcode/src/search/fts/common.rs:186-196]
[crates/gcode/src/search/fts/common.rs:198-200]
[crates/gcode/src/search/fts/common.rs:202-233]
[crates/gcode/src/search/fts/common.rs:235-250]
[crates/gcode/src/search/fts/common.rs:252-272]
[crates/gcode/src/search/fts/common.rs:274-291]
[crates/gcode/src/search/fts/common.rs:293-341]
[crates/gcode/src/search/fts/common.rs:348-354]
[crates/gcode/src/search/fts/common.rs:357-362]
[crates/gcode/src/search/fts/content.rs:13-21]
[crates/gcode/src/search/fts/content.rs:24-81]
[crates/gcode/src/search/fts/content.rs:83-138]
[crates/gcode/src/search/fts/content.rs:140-178]
[crates/gcode/src/search/fts/content.rs:180-196]
[crates/gcode/src/search/fts/content.rs:199-202]
[crates/gcode/src/search/fts/content.rs:204-210]
[crates/gcode/src/search/fts/content.rs:212-227]
[crates/gcode/src/search/fts/content.rs:229-244]
[crates/gcode/src/search/fts/content.rs:250-253]
[crates/gcode/src/search/fts/content.rs:256-261]
[crates/gcode/src/search/fts/content.rs:264-269]
[crates/gcode/src/search/fts/counts.rs:10-66]
[crates/gcode/src/search/fts/counts.rs:69-113]
[crates/gcode/src/search/fts/counts.rs:115-146]
[crates/gcode/src/search/fts/counts.rs:148-164]
[crates/gcode/src/search/fts/counts.rs:166-191]
[crates/gcode/src/search/fts/counts.rs:193-243]
[crates/gcode/src/search/fts/counts.rs:245-259]
[crates/gcode/src/search/fts/counts.rs:261-273]
[crates/gcode/src/search/fts/counts.rs:275-294]
[crates/gcode/src/search/fts/counts.rs:296-307]
[crates/gcode/src/search/fts/counts.rs:309-333]
[crates/gcode/src/search/fts/counts.rs:335-359]
[crates/gcode/src/search/fts/counts.rs:366-385]
[crates/gcode/src/search/fts/graph.rs:16-50]
[crates/gcode/src/search/fts/graph.rs:52-55]
[crates/gcode/src/search/fts/graph.rs:57-62]
[crates/gcode/src/search/fts/graph.rs:64-69]
[crates/gcode/src/search/fts/graph.rs:71-78]
[crates/gcode/src/search/fts/graph.rs:80-96]
[crates/gcode/src/search/fts/graph.rs:98-103]
[crates/gcode/src/search/fts/graph.rs:108-147]
[crates/gcode/src/search/fts/symbols.rs:15-18]
[crates/gcode/src/search/fts/symbols.rs:21-26]
[crates/gcode/src/search/fts/symbols.rs:28-33]
[crates/gcode/src/search/fts/symbols.rs:36-73]
[crates/gcode/src/search/fts/symbols.rs:76-112]
[crates/gcode/src/search/fts/symbols.rs:114-190]
[crates/gcode/src/search/fts/symbols.rs:192-225]
[crates/gcode/src/search/fts/symbols.rs:227-260]
[crates/gcode/src/search/fts/symbols.rs:262-337]
[crates/gcode/src/search/fts/symbols.rs:339-371]
[crates/gcode/src/search/fts/symbols.rs:374-386]
[crates/gcode/src/search/fts/symbols.rs:388-401]
[crates/gcode/src/search/fts/tests.rs:17-26]
[crates/gcode/src/search/fts/tests.rs:29-34]
[crates/gcode/src/search/fts/tests.rs:37-43]
[crates/gcode/src/search/fts/tests.rs:46-49]
[crates/gcode/src/search/fts/tests.rs:52-57]
[crates/gcode/src/search/fts/tests.rs:60-72]
[crates/gcode/src/search/fts/tests.rs:75-81]
[crates/gcode/src/search/fts/tests.rs:84-99]
[crates/gcode/src/search/fts/tests.rs:102-133]
[crates/gcode/src/search/fts/tests.rs:136-142]
[crates/gcode/src/search/fts/tests.rs:145-151]
[crates/gcode/src/search/fts/tests.rs:154-166]
[crates/gcode/src/search/fts/tests.rs:173-207]
[crates/gcode/src/search/fts/tests.rs:211-239]
[crates/gcode/src/search/fts/tests.rs:242-257]
[crates/gcode/src/search/fts/tests.rs:260-269]
[crates/gcode/src/search/fts/tests.rs:272-281]
[crates/gcode/src/search/fts/tests.rs:283-302]
[crates/gcode/src/search/fts/tests.rs:304-308]
[crates/gcode/src/search/fts/tests.rs:310-319]
[crates/gcode/src/search/fts/tests.rs:311-318]
[crates/gcode/src/search/fts/tests.rs:321-325]
[crates/gcode/src/search/fts/tests.rs:327-336]
[crates/gcode/src/search/fts/tests.rs:328-335]
[crates/gcode/src/search/fts/tests.rs:338-342]
[crates/gcode/src/search/fts/tests.rs:339-341]
[crates/gcode/src/search/fts/tests.rs:344-347]
[crates/gcode/src/search/fts/tests.rs:349-355]
[crates/gcode/src/search/fts/tests.rs:350-354]
[crates/gcode/src/search/fts/tests.rs:357-360]
[crates/gcode/src/search/fts/tests.rs:362-364]
[crates/gcode/src/search/fts/tests.rs:366-380]
[crates/gcode/src/search/fts/tests.rs:382-470]
[crates/gcode/src/search/fts/tests.rs:472-480]
[crates/gcode/src/search/fts/tests.rs:482-499]
[crates/gcode/src/search/fts/tests.rs:501-514]
[crates/gcode/src/search/fts/tests.rs:516-533]
[crates/gcode/src/search/fts/tests.rs:535-554]

## Files

- [[code/files/crates/gcode/src/search/fts.rs|crates/gcode/src/search/fts.rs]] - `crates/gcode/src/search/fts.rs` has no indexed API symbols.
- [[code/files/crates/gcode/src/search/graph_boost.rs|crates/gcode/src/search/graph_boost.rs]] - `crates/gcode/src/search/graph_boost.rs` exposes 9 indexed API symbols.
[crates/gcode/src/search/graph_boost.rs:21-47]
[crates/gcode/src/search/graph_boost.rs:55-86]
[crates/gcode/src/search/graph_boost.rs:88-106]
[crates/gcode/src/search/graph_boost.rs:113-127]
[crates/gcode/src/search/graph_boost.rs:129-153]
[crates/gcode/src/search/graph_boost.rs:156-160]
[crates/gcode/src/search/graph_boost.rs:163-167]
[crates/gcode/src/search/graph_boost.rs:170-174]
[crates/gcode/src/search/graph_boost.rs:177-223]
- [[code/files/crates/gcode/src/search/mod.rs|crates/gcode/src/search/mod.rs]] - `crates/gcode/src/search/mod.rs` has no indexed API symbols.
- [[code/files/crates/gcode/src/search/rrf.rs|crates/gcode/src/search/rrf.rs]] - `crates/gcode/src/search/rrf.rs` exposes 9 indexed API symbols.
[crates/gcode/src/search/rrf.rs:7]
[crates/gcode/src/search/rrf.rs:15-20]
[crates/gcode/src/search/rrf.rs:27-34]
[crates/gcode/src/search/rrf.rs:37-49]
[crates/gcode/src/search/rrf.rs:52-64]
[crates/gcode/src/search/rrf.rs:67-75]
[crates/gcode/src/search/rrf.rs:78-81]
[crates/gcode/src/search/rrf.rs:84-87]
[crates/gcode/src/search/rrf.rs:90-113]

## Components

- `875a5446-fa88-50ae-8ce9-ad57a6deeec3`
- `5b940a4c-43f0-5ceb-9f69-bb58acf44bb5`
- `37a9e542-63a5-5f2a-88b9-a8daa24f4685`
- `e6bb7f19-4789-53b7-b4a5-7a3d95651935`
- `875c9f83-ee42-5335-a79a-f943fe8d6f9a`
- `80bd4151-9a3a-5dae-89d9-58ac38cdf4fb`
- `3167635d-631c-5707-8b2d-6aa46bf46019`
- `33186fc9-8d87-555c-89d0-58c4b6c54b97`
- `95df4599-dd9f-564b-83ca-459b096613b2`
- `06820a48-7d6c-549b-a9e6-b1b1c68426de`
- `a0cab5a7-d2d4-5809-9959-3c3e8c5a211f`
- `8ff760fe-39ec-53a5-b358-e26a76e1864a`
- `03a59319-cb90-5da0-b6da-513367ba0b40`
- `434dcd5b-7d2e-58e3-a9ca-16cfcc62b746`
- `b759e95a-8cff-5199-ac82-4dc2ff56645b`
- `bbf9795e-e4aa-5b94-b61c-4c2f44ba6e94`
- `930b5993-fb3e-5fb7-8d6c-f60518226697`
- `6a5ed17f-f567-5446-8471-355288c34719`
- `24e75ff8-ffee-5114-97b1-60fbc8300eea`
- `615c1ea3-a547-58c7-b5f1-bf520f214fec`
- `c748a762-7ce0-5443-819e-c67875245c7d`
- `021bf360-d2b3-5062-a29f-aaba0c00a4fc`
- `f7d875d0-1c61-5191-8ace-0132624e23a2`
- `0c94647d-0190-534c-ab66-e0696b6a8385`
- `627e2f5a-6d72-59b1-b259-70253558829d`
- `3468182c-fb0e-5b7c-b068-8f2eb57ea954`
- `179dd1c5-b87f-53fc-a90c-763bdd51a20b`
- `7446ca66-ab33-5eff-a2b1-e4b2938026a7`
- `4b716707-ac59-56cf-90a8-cd24217c2bf3`
- `72fa13bb-eabb-5eb1-b8fe-d7db332ec1b3`
- `648255b9-169c-51d5-a62f-939415961c7f`
- `579fd432-ba03-56e4-a645-d3e3cc2b7706`
- `cd1e698f-50a5-5e42-a7b8-ead4ee7ccce2`
- `632f29a2-e318-5128-9034-41b5bbff48db`
- `a1573ddd-d8c0-52ea-a258-0425f294c453`
- `68e1dadb-848a-5b23-8adb-ba7424a83bff`
- `758bf97b-7f2d-5b82-953f-9d352043a0d8`
- `96b90155-4bc1-5422-9216-4edffe1168c7`
- `2db20335-3547-5506-bdc9-a382173a22f6`
- `0d0fec52-b764-59a1-8b21-62c58911c683`
- `8e85ae6a-f520-5f17-afd9-754b8de3432f`
- `bd9b91b7-a8f6-5c63-a256-05af4bf9efca`
- `baedf168-7509-5fc4-b62e-47be6ec62ace`
- `d3ee1ca5-ab0b-56bc-931e-148ce45b4a3e`
- `23214880-b18a-5115-928e-c8df175c75cc`
- `bc13a11f-4797-55ab-96a8-f7c8e4eb57e2`
- `36b6335a-ba3c-5adf-bbdd-5cce7c9bf895`
- `23475bad-2efa-5961-a13d-5721256c2451`
- `4caa4356-8cdc-53b0-9188-cb53dd79e859`
- `12d3a313-a917-5b4b-a086-596f05d19f5e`
- `842c67f7-b4e2-5d99-8a88-32cad789aa2c`
- `b4cc47ee-1f6a-5e5a-8441-d13a2e35cd07`
- `0ff8ece5-1205-58ae-905a-49ce8f454e17`
- `d1f8a2d2-61fd-58e2-b068-7689eccb3887`
- `3d1bee9a-3709-57f9-a28d-e88b9c8785a7`
- `a28d9b77-15e0-501a-8023-399c91273ecf`
- `f5aa9fa1-b1c7-562f-9575-b6658bdfd99c`
- `c405005b-f37b-5014-9917-2ce4df0bf22c`
- `f1ba3605-a9dc-5827-b185-e9d8ece938e9`
- `eb9daf75-1417-5e1f-8ef8-a06b2416d482`
- `9bde1975-6a34-5b77-bf7c-19bb8fa029b2`
- `ded7d11d-b336-5edf-b8f3-1fbf422eb146`
- `7f8858f7-6495-512a-a587-95d455f4fbbe`
- `0b688623-4f21-5b00-a280-a1d2cbb2d5fb`
- `f4b35aca-bf2c-543e-bf95-11d4a269183c`
- `7c7b30bd-72c2-5b36-a1d9-f1afbc529baa`
- `ff6f1083-33c6-59d1-9904-3b13f37ac480`
- `ac175e0a-4769-5ecc-a380-df2871381992`
- `3d569783-3c97-5d1a-add6-1b31103e4190`
- `54024085-f7fd-576a-b6ed-d61818739cd7`
- `1622d5fc-3a81-565d-8cfe-6ffabcb12f1f`
- `fd54f990-1b37-5f68-8408-2d3c7269ce30`
- `1f26ce71-11ec-50de-8b43-7b98692770bc`
- `fc44b822-a009-582b-b905-d5529393a1a2`
- `8689ca2e-c1bf-5808-8150-4bf0a6d9dd98`
- `5f195c43-9371-5d02-ba23-e1376bfb3de3`
- `d78afdfa-69fe-5921-a2ef-928494c47574`
- `49cc3e66-1b6d-5f9e-9964-c2c54ab58b80`
- `e294fe66-8239-5cc5-9153-12f7e13f587d`
- `576ff3eb-7797-5edc-ba13-7bdf39b37b5f`
- `78da6b7c-d5ab-5449-a982-91b42784285e`
- `1f5dc90a-1d58-5be8-8c77-426b53c26226`
- `e7a89329-186a-50f7-9f45-834cf3f5d189`
- `70ea9540-7e9c-556b-9125-c0d00efa1945`
- `ac13df70-4a1b-5715-a138-bdff7efaae89`
- `6ce78df0-8b75-58cb-bff6-3a7a8d5c00c2`
- `adece121-7c6d-5c41-b9b1-559f2a896ed3`
- `0e326739-88d8-5971-8ddf-6a59511de529`
- `c2edb10a-2bc8-5649-8aa9-099f0aa14504`
- `b0b511f1-9935-55ea-b891-a5baf8be77f4`
- `f64b55f9-c0e7-5456-ac7e-0ae5d3bc289e`
- `2c07fc55-be3f-569c-91a0-83656dbb6696`
- `673b9448-55d0-5859-a47c-78489448e643`
- `26e8ab31-86ed-5ca5-b570-56b44149663c`
- `7d3cefe4-8506-50e3-8415-87819a836943`
- `069c92e4-0653-554c-96ec-e138369841ac`
- `f8f6acf9-c230-59e0-a228-5dfbc798e605`
- `d4232e2f-aebe-52fb-ac05-20a32531a353`
- `ff80a57a-18f8-59af-b135-0efb3fe1dd44`
- `21f764c8-ccab-5311-975a-c3499cd9be81`
- `4254b793-3d52-581a-8a61-5f0134ac7d20`
- `8d662aa4-aad8-52aa-b186-0cd53d1ddc13`
- `e7450bd9-79a8-5dc2-b73f-4e01dc4cbf3a`
- `9a5ed7b9-87d8-55c9-952f-9be23dd54838`
- `c8eadff2-15a4-5099-b73d-9941c7866c77`
- `0bf71dd4-c8a5-53ab-a576-33893c11c841`
- `1983b58d-145c-5e2a-9bbf-85bdc4b3ddef`
- `ace6cf3e-47ec-5e0f-ba94-e00bc5fabbbb`
- `821967f5-60ed-567d-b11d-f9cfb2726a60`
- `2cd40db1-4e53-5de4-be24-7b59e0b83a43`
- `cdbdd7fb-61d4-5e31-b2bb-b1e42758c75a`
- `fce20da6-a98f-553e-bfa7-bec5b8685476`
- `8e07f24c-1345-5ff2-b99b-fa4256b92f7a`
- `d2b29a0f-7fa5-5865-a104-83fe2cdd3eef`
- `8e475747-c493-5cc6-a3e7-f86a684ba506`
- `d0070db0-0756-5591-97c0-c2b4fa4bd3f2`
- `752226a9-8b51-5e80-97ec-354312b73330`
- `4f252f0f-f18a-5b74-97a4-740bcaaa731d`
- `ee7eabc0-8008-50d8-9fde-f2a283bc7fe5`
- `22a35146-0b3d-5a8b-a030-3da3a66883cd`
- `873d4c1e-dd07-58fe-a832-e784dabd9689`
- `58647f00-fd39-5646-bad7-155c0cbd79f2`
- `84046dbc-3560-568e-a490-df5f55d17f96`
- `76109a10-3a96-55e7-bf6b-0ebfdd2fcb4a`
- `8cb6830f-e7a6-5d3f-b87c-ad56c1e35dd1`
- `239158ff-3daf-584d-b001-791e25c54319`

