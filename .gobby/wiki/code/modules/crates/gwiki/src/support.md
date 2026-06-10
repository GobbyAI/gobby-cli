---
title: crates/gwiki/src/support
type: code_module
provenance:
- file: crates/gwiki/src/support/config.rs
  ranges:
  - 17-20
  - 22-29
  - 23-28
  - 31-35
  - 37-42
  - 45-51
  - 53-60
  - 62-67
  - 69-76
  - 78-85
  - 87-91
  - 93-100
  - 102-117
  - 131-134
  - 136-150
  - 137-149
  - 152-161
  - 153-160
  - 163-169
  - 172-174
  - 176-181
  - 177-180
  - 183-191
  - 184-186
  - 188-190
  - 194-206
  - 209-228
  - 232-250
  - 253-265
  - 269-281
  - 285-312
- file: crates/gwiki/src/support/counts.rs
  ranges:
  - 4-10
  - 12-20
  - 22-33
  - 36-42
  - 44-54
  - 45-53
  - 56-72
  - 79-85
- file: crates/gwiki/src/support/env.rs
  ranges:
  - 21-24
  - 27-30
  - 32-49
  - 51-55
  - 57-66
  - 68-75
  - 77-89
  - 91-98
  - 100-109
  - 111-142
  - 144-154
  - 156-180
  - 182-188
  - 190-200
  - 202-218
  - 220-224
  - 226-234
  - 236-238
  - 251-257
  - 261-285
  - 288-297
  - 299-322
- file: crates/gwiki/src/support/graph.rs
  ranges:
  - 8-55
  - 57-90
  - 92-103
  - 105-107
  - 109-122
  - 124-146
  - 148-154
  - 162-192
  - 195-208
  - 211-236
  - 239-272
- file: crates/gwiki/src/support/postgres.rs
  ranges:
  - 6-39
  - 41-51
- file: crates/gwiki/src/support/scope.rs
  ranges:
  - 12-36
  - 38-42
  - 44-55
  - 60-66
  - 68-76
  - 78-87
  - 89-96
  - 98-104
  - 106-111
  - 114-118
  - 120-131
- file: crates/gwiki/src/support/search.rs
  ranges:
  - 11-13
  - 15-22
  - 16-21
  - '24'
  - 26-39
  - 27-38
  - 41-43
  - 46-51
  - 53-57
  - 60-161
- file: crates/gwiki/src/support/text.rs
  ranges:
  - 7-13
  - 15-22
  - 24-35
  - 37-49
  - 51-59
  - 61-67
  - 69-71
  - 73-75
  - 77-102
  - 109-114
  - 117-127
- file: crates/gwiki/src/support/time.rs
  ranges:
  - 3-6
  - 8-17
  - 24-39
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

This module provides foundational infrastructure and utility functions for the gwiki crate. It handles configuration and environment resolution, database connection setup, and Postgres table definitions. It includes helpers for graph target resolution, path normalization, and search scope management. Additionally, it implements search backend interfaces, indexing and document counting utilities, and text processing functions such as slugification and snippet generation, alongside timestamp handling utilities.
[crates/gwiki/src/support/config.rs:17-20]
[crates/gwiki/src/support/config.rs:22-29]
[crates/gwiki/src/support/config.rs:23-28]
[crates/gwiki/src/support/config.rs:31-35]
[crates/gwiki/src/support/config.rs:37-42]
[crates/gwiki/src/support/config.rs:45-51]
[crates/gwiki/src/support/config.rs:53-60]
[crates/gwiki/src/support/config.rs:62-67]
[crates/gwiki/src/support/config.rs:69-76]
[crates/gwiki/src/support/config.rs:78-85]
[crates/gwiki/src/support/config.rs:87-91]
[crates/gwiki/src/support/config.rs:93-100]
[crates/gwiki/src/support/config.rs:102-117]
[crates/gwiki/src/support/config.rs:131-134]
[crates/gwiki/src/support/config.rs:136-150]
[crates/gwiki/src/support/config.rs:137-149]
[crates/gwiki/src/support/config.rs:152-161]
[crates/gwiki/src/support/config.rs:153-160]
[crates/gwiki/src/support/config.rs:163-169]
[crates/gwiki/src/support/config.rs:172-174]
[crates/gwiki/src/support/config.rs:176-181]
[crates/gwiki/src/support/config.rs:177-180]
[crates/gwiki/src/support/config.rs:183-191]
[crates/gwiki/src/support/config.rs:184-186]
[crates/gwiki/src/support/config.rs:188-190]
[crates/gwiki/src/support/config.rs:194-206]
[crates/gwiki/src/support/config.rs:209-228]
[crates/gwiki/src/support/config.rs:232-250]
[crates/gwiki/src/support/config.rs:253-265]
[crates/gwiki/src/support/config.rs:269-281]
[crates/gwiki/src/support/config.rs:285-312]
[crates/gwiki/src/support/counts.rs:4-10]
[crates/gwiki/src/support/counts.rs:12-20]
[crates/gwiki/src/support/counts.rs:22-33]
[crates/gwiki/src/support/counts.rs:36-42]
[crates/gwiki/src/support/counts.rs:44-54]
[crates/gwiki/src/support/counts.rs:45-53]
[crates/gwiki/src/support/counts.rs:56-72]
[crates/gwiki/src/support/counts.rs:79-85]
[crates/gwiki/src/support/env.rs:21-24]
[crates/gwiki/src/support/env.rs:27-30]
[crates/gwiki/src/support/env.rs:32-49]
[crates/gwiki/src/support/env.rs:51-55]
[crates/gwiki/src/support/env.rs:57-66]
[crates/gwiki/src/support/env.rs:68-75]
[crates/gwiki/src/support/env.rs:77-89]
[crates/gwiki/src/support/env.rs:91-98]
[crates/gwiki/src/support/env.rs:100-109]
[crates/gwiki/src/support/env.rs:111-142]
[crates/gwiki/src/support/env.rs:144-154]
[crates/gwiki/src/support/env.rs:156-180]
[crates/gwiki/src/support/env.rs:182-188]
[crates/gwiki/src/support/env.rs:190-200]
[crates/gwiki/src/support/env.rs:202-218]
[crates/gwiki/src/support/env.rs:220-224]
[crates/gwiki/src/support/env.rs:226-234]
[crates/gwiki/src/support/env.rs:236-238]
[crates/gwiki/src/support/env.rs:251-257]
[crates/gwiki/src/support/env.rs:261-285]
[crates/gwiki/src/support/env.rs:288-297]
[crates/gwiki/src/support/env.rs:299-322]
[crates/gwiki/src/support/graph.rs:8-55]
[crates/gwiki/src/support/graph.rs:57-90]
[crates/gwiki/src/support/graph.rs:92-103]
[crates/gwiki/src/support/graph.rs:105-107]
[crates/gwiki/src/support/graph.rs:109-122]
[crates/gwiki/src/support/graph.rs:124-146]
[crates/gwiki/src/support/graph.rs:148-154]
[crates/gwiki/src/support/graph.rs:162-192]
[crates/gwiki/src/support/graph.rs:195-208]
[crates/gwiki/src/support/graph.rs:211-236]
[crates/gwiki/src/support/graph.rs:239-272]
[crates/gwiki/src/support/postgres.rs:6-39]
[crates/gwiki/src/support/postgres.rs:41-51]
[crates/gwiki/src/support/scope.rs:12-36]
[crates/gwiki/src/support/scope.rs:38-42]
[crates/gwiki/src/support/scope.rs:44-55]
[crates/gwiki/src/support/scope.rs:60-66]
[crates/gwiki/src/support/scope.rs:68-76]
[crates/gwiki/src/support/scope.rs:78-87]
[crates/gwiki/src/support/scope.rs:89-96]
[crates/gwiki/src/support/scope.rs:98-104]
[crates/gwiki/src/support/scope.rs:106-111]
[crates/gwiki/src/support/scope.rs:114-118]
[crates/gwiki/src/support/scope.rs:120-131]
[crates/gwiki/src/support/search.rs:11-13]
[crates/gwiki/src/support/search.rs:15-22]
[crates/gwiki/src/support/search.rs:16-21]
[crates/gwiki/src/support/search.rs:24]
[crates/gwiki/src/support/search.rs:26-39]
[crates/gwiki/src/support/search.rs:27-38]
[crates/gwiki/src/support/search.rs:41-43]
[crates/gwiki/src/support/search.rs:46-51]
[crates/gwiki/src/support/search.rs:53-57]
[crates/gwiki/src/support/search.rs:60-161]
[crates/gwiki/src/support/text.rs:7-13]
[crates/gwiki/src/support/text.rs:15-22]
[crates/gwiki/src/support/text.rs:24-35]
[crates/gwiki/src/support/text.rs:37-49]
[crates/gwiki/src/support/text.rs:51-59]
[crates/gwiki/src/support/text.rs:61-67]
[crates/gwiki/src/support/text.rs:69-71]
[crates/gwiki/src/support/text.rs:73-75]
[crates/gwiki/src/support/text.rs:77-102]
[crates/gwiki/src/support/text.rs:109-114]
[crates/gwiki/src/support/text.rs:117-127]
[crates/gwiki/src/support/time.rs:3-6]
[crates/gwiki/src/support/time.rs:8-17]
[crates/gwiki/src/support/time.rs:24-39]

## Call Diagram

```mermaid
sequenceDiagram
    participant m_0e66cf59_0d78_55be_9627_7fe994e92989 as graph_resolves_relative_targets_from_source_document_directory &#91;function&#93;
    participant m_129019ee_da8b_544a_9574_38e8d372f45c as local_index_options_read_gcore_yaml &#91;function&#93;
    participant m_16b3f22a_23f0_5158_98f3_80f02cbac55f as index_options_from_conn &#91;function&#93;
    participant m_18b25317_47eb_57e2_a149_7bee167bfb4a as resolve_database_url_from_gcore_config &#91;function&#93;
    participant m_1eda6d02_1fa5_5d69_bb27_294bdeaf70aa as local_index_options &#91;function&#93;
    participant m_20f16aa6_97ae_5411_971b_177524a2cebd as shared_code_graph_limits_reject_invalid_or_negative_values &#91;function&#93;
    participant m_227d07d9_395c_5de5_b248_f26b36b2c4fb as max_inbox_item_bytes_from_env &#91;function&#93;
    participant m_25edf047_b574_5d44_ba5d_42891d7cc8f1 as search_scope_for_resolved &#91;function&#93;
    participant m_26d2526d_de98_529b_ae5f_cc41756e4559 as resolve_shared_code_graph_limits &#91;function&#93;
    participant m_289e2b52_0509_5e66_b63a_ba50562a6513 as graph_uses_distinct_source_document_paths &#91;function&#93;
    participant m_2e6f0d32_a201_59b5_81e4_20be67a8adcf as slugify &#91;function&#93;
    participant m_30377db8_c862_5fb7_a883_ddd62e0e4acb as resolve_database_url_from_bootstrap_file &#91;function&#93;
    participant m_3dc3cb65_c67f_558c_9095_1f919ab863c2 as snippets_reserve_space_for_ellipsis &#91;function&#93;
    participant m_3e2f928b_097a_5b21_9bce_c31e8a06b096 as collect_timestamp &#91;function&#93;
    participant m_40e90727_f9fd_5938_8725_0f6d40857f33 as shared_code_graph_limits_from_conn &#91;function&#93;
    participant m_42d8a2cb_4641_518e_84b0_13e45e109d00 as local_shared_code_graph_limits &#91;function&#93;
    participant m_565c6461_166f_5d18_91c6_23b28a664e08 as snippet_from_text &#91;function&#93;
    participant m_846416e3_5b33_5a34_aaa2_933004d7b604 as unix_timestamp_ms &#91;function&#93;
    participant m_8aff6269_e2ef_544a_affd_1f6e579c81b1 as topic_project_precedence &#91;function&#93;
    participant m_a6f8ad7e_af2f_59a1_bae5_47c7094b7d91 as slug_target_map &#91;function&#93;
    participant m_a8d3e8cc_b064_53c2_a44a_64e7c4b1ab9a as resolve_index_options &#91;function&#93;
    participant m_aafef5e8_bf8a_5a7f_a7d7_e7a44e2a4855 as parse_positive_u64 &#91;function&#93;
    participant m_b80d26fc_3355_527f_aa2c_8df0bf8e79d6 as slugify_with_options &#91;function&#93;
    participant m_ba7c38b2_b16d_50f8_8bf4_b0d23da13040 as read_standalone_config &#91;function&#93;
    participant m_bb07c06f_6a16_5a03_b359_d42af8261ce6 as non_empty_trimmed &#91;function&#93;
    participant m_bdc6ce54_eaaf_5226_9a52_7533273b5c01 as resolve_limit &#91;function&#93;
    participant m_c58bfe53_d5ea_5e3b_8307_5db7d7679aeb as memory_graph_from_store &#91;function&#93;
    participant m_d38c4257_cc17_581c_9bb9_29c06576b003 as write_file &#91;function&#93;
    m_0e66cf59_0d78_55be_9627_7fe994e92989->>m_a6f8ad7e_af2f_59a1_bae5_47c7094b7d91: calls
    m_129019ee_da8b_544a_9574_38e8d372f45c->>m_1eda6d02_1fa5_5d69_bb27_294bdeaf70aa: calls
    m_129019ee_da8b_544a_9574_38e8d372f45c->>m_d38c4257_cc17_581c_9bb9_29c06576b003: calls
    m_16b3f22a_23f0_5158_98f3_80f02cbac55f->>m_a8d3e8cc_b064_53c2_a44a_64e7c4b1ab9a: calls
    m_16b3f22a_23f0_5158_98f3_80f02cbac55f->>m_ba7c38b2_b16d_50f8_8bf4_b0d23da13040: calls
    m_18b25317_47eb_57e2_a149_7bee167bfb4a->>m_bb07c06f_6a16_5a03_b359_d42af8261ce6: calls
    m_1eda6d02_1fa5_5d69_bb27_294bdeaf70aa->>m_a8d3e8cc_b064_53c2_a44a_64e7c4b1ab9a: calls
    m_1eda6d02_1fa5_5d69_bb27_294bdeaf70aa->>m_ba7c38b2_b16d_50f8_8bf4_b0d23da13040: calls
    m_20f16aa6_97ae_5411_971b_177524a2cebd->>m_26d2526d_de98_529b_ae5f_cc41756e4559: calls
    m_227d07d9_395c_5de5_b248_f26b36b2c4fb->>m_aafef5e8_bf8a_5a7f_a7d7_e7a44e2a4855: calls
    m_25edf047_b574_5d44_ba5d_42891d7cc8f1->>m_8aff6269_e2ef_544a_affd_1f6e579c81b1: calls
    m_26d2526d_de98_529b_ae5f_cc41756e4559->>m_bdc6ce54_eaaf_5226_9a52_7533273b5c01: calls
    m_289e2b52_0509_5e66_b63a_ba50562a6513->>m_c58bfe53_d5ea_5e3b_8307_5db7d7679aeb: calls
    m_2e6f0d32_a201_59b5_81e4_20be67a8adcf->>m_b80d26fc_3355_527f_aa2c_8df0bf8e79d6: calls
    m_30377db8_c862_5fb7_a883_ddd62e0e4acb->>m_bb07c06f_6a16_5a03_b359_d42af8261ce6: calls
    m_3dc3cb65_c67f_558c_9095_1f919ab863c2->>m_565c6461_166f_5d18_91c6_23b28a664e08: calls
    m_3e2f928b_097a_5b21_9bce_c31e8a06b096->>m_846416e3_5b33_5a34_aaa2_933004d7b604: calls
    m_40e90727_f9fd_5938_8725_0f6d40857f33->>m_26d2526d_de98_529b_ae5f_cc41756e4559: calls
    m_40e90727_f9fd_5938_8725_0f6d40857f33->>m_ba7c38b2_b16d_50f8_8bf4_b0d23da13040: calls
    m_42d8a2cb_4641_518e_84b0_13e45e109d00->>m_26d2526d_de98_529b_ae5f_cc41756e4559: calls
```

## Files

- [[code/files/crates/gwiki/src/support/config.rs|crates/gwiki/src/support/config.rs]] - `crates/gwiki/src/support/config.rs` exposes 31 indexed API symbols.
[crates/gwiki/src/support/config.rs:17-20]
[crates/gwiki/src/support/config.rs:22-29]
[crates/gwiki/src/support/config.rs:23-28]
[crates/gwiki/src/support/config.rs:31-35]
[crates/gwiki/src/support/config.rs:37-42]
[crates/gwiki/src/support/config.rs:45-51]
[crates/gwiki/src/support/config.rs:53-60]
[crates/gwiki/src/support/config.rs:62-67]
[crates/gwiki/src/support/config.rs:69-76]
[crates/gwiki/src/support/config.rs:78-85]
[crates/gwiki/src/support/config.rs:87-91]
[crates/gwiki/src/support/config.rs:93-100]
[crates/gwiki/src/support/config.rs:102-117]
[crates/gwiki/src/support/config.rs:131-134]
[crates/gwiki/src/support/config.rs:136-150]
[crates/gwiki/src/support/config.rs:137-149]
[crates/gwiki/src/support/config.rs:152-161]
[crates/gwiki/src/support/config.rs:153-160]
[crates/gwiki/src/support/config.rs:163-169]
[crates/gwiki/src/support/config.rs:172-174]
[crates/gwiki/src/support/config.rs:176-181]
[crates/gwiki/src/support/config.rs:177-180]
[crates/gwiki/src/support/config.rs:183-191]
[crates/gwiki/src/support/config.rs:184-186]
[crates/gwiki/src/support/config.rs:188-190]
[crates/gwiki/src/support/config.rs:194-206]
[crates/gwiki/src/support/config.rs:209-228]
[crates/gwiki/src/support/config.rs:232-250]
[crates/gwiki/src/support/config.rs:253-265]
[crates/gwiki/src/support/config.rs:269-281]
[crates/gwiki/src/support/config.rs:285-312]
- [[code/files/crates/gwiki/src/support/counts.rs|crates/gwiki/src/support/counts.rs]] - `crates/gwiki/src/support/counts.rs` exposes 8 indexed API symbols.
[crates/gwiki/src/support/counts.rs:4-10]
[crates/gwiki/src/support/counts.rs:12-20]
[crates/gwiki/src/support/counts.rs:22-33]
[crates/gwiki/src/support/counts.rs:36-42]
[crates/gwiki/src/support/counts.rs:44-54]
[crates/gwiki/src/support/counts.rs:45-53]
[crates/gwiki/src/support/counts.rs:56-72]
[crates/gwiki/src/support/counts.rs:79-85]
- [[code/files/crates/gwiki/src/support/env.rs|crates/gwiki/src/support/env.rs]] - `crates/gwiki/src/support/env.rs` exposes 22 indexed API symbols.
[crates/gwiki/src/support/env.rs:21-24]
[crates/gwiki/src/support/env.rs:27-30]
[crates/gwiki/src/support/env.rs:32-49]
[crates/gwiki/src/support/env.rs:51-55]
[crates/gwiki/src/support/env.rs:57-66]
[crates/gwiki/src/support/env.rs:68-75]
[crates/gwiki/src/support/env.rs:77-89]
[crates/gwiki/src/support/env.rs:91-98]
[crates/gwiki/src/support/env.rs:100-109]
[crates/gwiki/src/support/env.rs:111-142]
[crates/gwiki/src/support/env.rs:144-154]
[crates/gwiki/src/support/env.rs:156-180]
[crates/gwiki/src/support/env.rs:182-188]
[crates/gwiki/src/support/env.rs:190-200]
[crates/gwiki/src/support/env.rs:202-218]
[crates/gwiki/src/support/env.rs:220-224]
[crates/gwiki/src/support/env.rs:226-234]
[crates/gwiki/src/support/env.rs:236-238]
[crates/gwiki/src/support/env.rs:251-257]
[crates/gwiki/src/support/env.rs:261-285]
[crates/gwiki/src/support/env.rs:288-297]
[crates/gwiki/src/support/env.rs:299-322]
- [[code/files/crates/gwiki/src/support/graph.rs|crates/gwiki/src/support/graph.rs]] - `crates/gwiki/src/support/graph.rs` exposes 11 indexed API symbols.
[crates/gwiki/src/support/graph.rs:8-55]
[crates/gwiki/src/support/graph.rs:57-90]
[crates/gwiki/src/support/graph.rs:92-103]
[crates/gwiki/src/support/graph.rs:105-107]
[crates/gwiki/src/support/graph.rs:109-122]
[crates/gwiki/src/support/graph.rs:124-146]
[crates/gwiki/src/support/graph.rs:148-154]
[crates/gwiki/src/support/graph.rs:162-192]
[crates/gwiki/src/support/graph.rs:195-208]
[crates/gwiki/src/support/graph.rs:211-236]
[crates/gwiki/src/support/graph.rs:239-272]
- [[code/files/crates/gwiki/src/support/mod.rs|crates/gwiki/src/support/mod.rs]] - `crates/gwiki/src/support/mod.rs` has no indexed API symbols.
- [[code/files/crates/gwiki/src/support/postgres.rs|crates/gwiki/src/support/postgres.rs]] - `crates/gwiki/src/support/postgres.rs` exposes 2 indexed API symbols.
[crates/gwiki/src/support/postgres.rs:6-39]
[crates/gwiki/src/support/postgres.rs:41-51]
- [[code/files/crates/gwiki/src/support/scope.rs|crates/gwiki/src/support/scope.rs]] - `crates/gwiki/src/support/scope.rs` exposes 11 indexed API symbols.
[crates/gwiki/src/support/scope.rs:12-36]
[crates/gwiki/src/support/scope.rs:38-42]
[crates/gwiki/src/support/scope.rs:44-55]
[crates/gwiki/src/support/scope.rs:60-66]
[crates/gwiki/src/support/scope.rs:68-76]
[crates/gwiki/src/support/scope.rs:78-87]
[crates/gwiki/src/support/scope.rs:89-96]
[crates/gwiki/src/support/scope.rs:98-104]
[crates/gwiki/src/support/scope.rs:106-111]
[crates/gwiki/src/support/scope.rs:114-118]
[crates/gwiki/src/support/scope.rs:120-131]
- [[code/files/crates/gwiki/src/support/search.rs|crates/gwiki/src/support/search.rs]] - `crates/gwiki/src/support/search.rs` exposes 10 indexed API symbols.
[crates/gwiki/src/support/search.rs:11-13]
[crates/gwiki/src/support/search.rs:15-22]
[crates/gwiki/src/support/search.rs:16-21]
[crates/gwiki/src/support/search.rs:24]
[crates/gwiki/src/support/search.rs:26-39]
[crates/gwiki/src/support/search.rs:27-38]
[crates/gwiki/src/support/search.rs:41-43]
[crates/gwiki/src/support/search.rs:46-51]
[crates/gwiki/src/support/search.rs:53-57]
[crates/gwiki/src/support/search.rs:60-161]
- [[code/files/crates/gwiki/src/support/text.rs|crates/gwiki/src/support/text.rs]] - `crates/gwiki/src/support/text.rs` exposes 11 indexed API symbols.
[crates/gwiki/src/support/text.rs:7-13]
[crates/gwiki/src/support/text.rs:15-22]
[crates/gwiki/src/support/text.rs:24-35]
[crates/gwiki/src/support/text.rs:37-49]
[crates/gwiki/src/support/text.rs:51-59]
[crates/gwiki/src/support/text.rs:61-67]
[crates/gwiki/src/support/text.rs:69-71]
[crates/gwiki/src/support/text.rs:73-75]
[crates/gwiki/src/support/text.rs:77-102]
[crates/gwiki/src/support/text.rs:109-114]
[crates/gwiki/src/support/text.rs:117-127]
- [[code/files/crates/gwiki/src/support/time.rs|crates/gwiki/src/support/time.rs]] - `crates/gwiki/src/support/time.rs` exposes 3 indexed API symbols.
[crates/gwiki/src/support/time.rs:3-6]
[crates/gwiki/src/support/time.rs:8-17]
[crates/gwiki/src/support/time.rs:24-39]

## Components

- `ffa5899d-d273-54b0-ab38-79ab6532b2bb`
- `0bd6c9e6-097c-568f-9caf-6f5f4a2d0def`
- `b04c09ab-89c5-594d-8c4b-672c97a634ce`
- `1eda6d02-1fa5-5d69-bb27-294bdeaf70aa`
- `16b3f22a-23f0-5158-98f3-80f02cbac55f`
- `42d8a2cb-4641-518e-84b0-13e45e109d00`
- `40e90727-f9fd-5938-8725-0f6d40857f33`
- `307d488c-ba74-5142-82de-5eb320757836`
- `ba7c38b2-b16d-50f8-8bf4-b0d23da13040`
- `a8d3e8cc-b064-53c2-a44a-64e7c4b1ab9a`
- `3d512a94-9084-5a93-b054-bbc87aed52fe`
- `26d2526d-de98-529b-ae5f-cc41756e4559`
- `bdc6ce54-eaaf-5226-9a52-7533273b5c01`
- `96ae673e-6ab4-5b9f-8c52-17ecc16afb54`
- `b676767d-cd66-5192-b811-b4395817b540`
- `52957757-34e4-56a1-bafc-229d38e5c270`
- `bc79dfe7-405e-547d-9eb5-20121a8530c3`
- `27b360ae-de7c-5ec0-9eb7-4067b6f812c5`
- `d38c4257-cc17-581c-9bb9-29c06576b003`
- `7fe5bc6b-cb98-5a58-9154-bfe1cf811c79`
- `3d2d321f-1dc1-537e-a37a-38200b0453b7`
- `53c3b772-1a31-5f18-b743-dc9e98f7e983`
- `0e534a0e-443c-5651-8918-0389d26e259f`
- `6bc1c131-6a60-5ef3-9128-3215cac5d99f`
- `11e8d499-3944-5b44-928f-63f38d739bb4`
- `57b47df4-03f5-5a87-9df3-301bd01d1dc7`
- `e99c6416-d8ea-5df3-b5cf-35b987c417b1`
- `afd70b74-3ab9-55bb-af01-3b64da8800f0`
- `20f16aa6-97ae-5411-971b-177524a2cebd`
- `129019ee-da8b-544a-9574-38e8d372f45c`
- `a49ec97f-8978-5704-a4a5-a2613b3f1052`
- `656f145d-38f1-5e5f-8d2f-3e5b9e20e1e1`
- `fc6bcd38-24d5-5898-abd8-f7cccb038630`
- `b479c64e-4fae-51b0-92fe-d60f7c9f9d94`
- `95bb5c54-adbf-5876-a1e5-d79aac9a09ba`
- `d9074934-27e8-51a1-87d0-41b9ed0a7b34`
- `dbfc88fd-48d8-53db-864a-51902f6844ea`
- `92643004-1821-5f95-a129-821545208e0d`
- `c79499c8-39f6-5d27-85e5-9ec608e58c4a`
- `6eef951c-c8de-5b3b-9eeb-431794396c90`
- `8786c9c3-4b38-5f85-8f9a-a2fa7b4b178a`
- `7acfa5f4-1a8d-55c2-8c66-45705c0b2ae9`
- `58500376-9458-5dd0-aacc-f3d53c8080f0`
- `1fad4bf4-a690-52bc-8d03-af8b394ae02c`
- `18b25317-47eb-57e2-a149-7bee167bfb4a`
- `30377db8-c862-5fb7-a883-ddd62e0e4acb`
- `96399e18-c124-5761-8a66-ebd00f10e793`
- `61248448-64b6-5ffa-b408-02fe22e9008a`
- `ce1e7c82-54fe-51d6-8571-84cfc5fe744e`
- `3e2c75af-1071-5ca2-a35a-c7576e8bb014`
- `920f35da-5b07-5065-b5fa-c5ab57f1ad2c`
- `65d37a63-038e-5844-85cd-a977b9824c6e`
- `51ab5688-3f0e-5b2e-8541-8fe116e619a9`
- `d20510a2-2f42-591d-b7be-4edd7db4fba3`
- `bb07c06f-6a16-5a03-b359-d42af8261ce6`
- `227d07d9-395c-5de5-b248-f26b36b2c4fb`
- `aafef5e8-bf8a-5a7f-a7d7-e7a44e2a4855`
- `4dadd1a6-e5a9-5733-8ff9-727835cf4023`
- `d5b21cc5-c6c1-530d-8aac-f21ed1660bd6`
- `6091d7ec-1fde-5e22-b8d8-76e452eb8ad4`
- `df1722b7-7ee6-534e-ae75-bd9bd50080e3`
- `c58bfe53-d5ea-5e3b-8307-5db7d7679aeb`
- `fbf0a734-28e0-54f1-a47d-63120beb0197`
- `cd20f1ee-83ea-57bb-96a3-d927c3608429`
- `c5197c2f-64c9-5a8b-abd7-ffce06d1e758`
- `5b38ce11-b074-5501-ad0f-a67c932f35f7`
- `a6f8ad7e-af2f-59a1-bae5-47c7094b7d91`
- `f10918ae-5486-56ec-bb51-c573bd941deb`
- `289e2b52-0509-5e66-b63a-ba50562a6513`
- `d111c3fe-cfab-50a5-8389-52b9fb7880ec`
- `7437ceb8-e970-50fa-bca9-257417e413de`
- `0e66cf59-0d78-55be-9627-7fe994e92989`
- `e5e4bf14-b0e4-5ecf-a2e7-b9ca1e8a01db`
- `5f965f9d-b719-59de-84bd-72e703a7bc08`
- `df141688-ee38-5b52-bd23-fc11a48ce4d9`
- `1d240702-63f1-5372-b4ca-5c3c97aa6710`
- `ab45668c-9fc1-537d-a96d-8f07bce81dff`
- `25edf047-b574-5d44-ba5d-42891d7cc8f1`
- `c5a00368-428f-5a21-a914-ad69e9e221b6`
- `118423b2-f7d5-5894-9213-cc544048ccdd`
- `9b22dbcb-071f-5cd1-a54b-31ba0a2d822d`
- `cdee2a59-85c5-5e73-aa95-10ee01910ed1`
- `b8f5ad0f-186e-5868-9916-49a43410ac45`
- `c3447c4f-1834-5fe7-9778-2f7f050e52ad`
- `8aff6269-e2ef-544a-affd-1f6e579c81b1`
- `57275bba-d082-54ff-b944-52fdd9f97c05`
- `8eb2ef98-3345-5b48-b9ce-625bdc330f44`
- `1f0c3d0f-f271-5426-a656-c12b82843f34`
- `0ab4dcb5-bbbc-51a8-b5ef-972b072e1658`
- `4f1ae42c-5d04-5187-8aec-95d9b9af2b9d`
- `15803901-4cc1-572d-a4ba-7110dfe6fe1a`
- `7c1fea1d-963a-5541-9f57-2744e8bb5f8d`
- `2325a736-cca6-5936-9f50-8c4900f9f802`
- `70142db5-bd7d-559f-b313-2ac7ee7cb55b`
- `23d15dc3-e88a-5fc5-8acf-a92884afbccf`
- `9d7a2ce6-8feb-5fb6-aa36-19986c3ef7b7`
- `91790d1a-0fe3-5fc3-ab61-2655714dc637`
- `565c6461-166f-5d18-91c6-23b28a664e08`
- `dd4c773e-02ab-5f4e-8e61-b20704393db1`
- `cd9bfc9c-9322-5e23-91f2-e44d1ea31620`
- `fb1bdf5a-98ea-5331-88a5-099bb1fb3caa`
- `865de779-6685-5a45-9b5b-52923941e2ee`
- `2e6f0d32-a201-59b5-81e4-20be67a8adcf`
- `b80d26fc-3355-527f-aa2c-8df0bf8e79d6`
- `3dc3cb65-c67f-558c-9095-1f919ab863c2`
- `22092578-41f7-5706-83d1-92d63e86a0f5`
- `3e2f928b-097a-5b21-9bce-c31e8a06b096`
- `846416e3-5b33-5a34-aaa2-933004d7b604`
- `53594747-a121-50f2-a698-e8d276c76a69`

