---
title: crates/gwiki/src/research
type: code_module
provenance:
- file: crates/gwiki/src/research/mod.rs
  ranges:
  - '41'
  - 44-50
  - 45-49
  - 53-59
  - 62-71
  - '74'
  - 77-83
  - 86-97
  - 100-122
  - 126-130
  - 134-142
  - 145-152
  - 156-160
  - 163-166
  - 168-287
  - 289-336
  - 338-353
  - 355-366
- file: crates/gwiki/src/research/model.rs
  ranges:
  - 21-24
  - 26-33
  - 27-32
  - 35-96
  - 36-95
  - 103-105
  - 107-129
  - 108-114
  - 116-128
  - 131-142
  - 144-146
  - 148-159
  - 149-158
  - 161-163
  - 165-181
  - 166-180
  - 183-204
  - 206-208
  - 210-218
  - 211-217
  - 220-222
  - 224-254
  - 225-233
  - 235-253
  - 256-259
  - 262-269
- file: crates/gwiki/src/research/notes.rs
  ranges:
  - 5-16
  - 18-20
  - 22-26
  - 28-99
  - 101-108
  - 110-113
  - 115-126
  - 128-157
  - 159-256
  - 258-300
  - 302-313
  - 315-318
  - 320-364
  - 366-402
  - 404-410
  - 415-423
  - 428-430
  - 432-441
  - 443-449
  - 451-459
- file: crates/gwiki/src/research/outcome.rs
  ranges:
  - 15-24
  - 26-41
  - 43-51
  - 53-89
  - 91-99
  - 101-127
  - 129-147
  - 149-152
  - 154-171
  - 173-188
  - 190-200
  - 202-216
  - 221-228
  - 230-252
  - 254-329
  - 331-334
  - 336-344
  - 346-353
  - 360-372
  - 375-385
  - 388-426
  - 429-444
  - 447-457
  - 460-470
  - 473-482
- file: crates/gwiki/src/research/storage.rs
  ranges:
  - 12-59
  - 61-91
  - 93-95
  - 97-135
  - 137-151
  - 153-155
  - 157-159
  - 168-177
- file: crates/gwiki/src/research/tests.rs
  ranges:
  - 8-21
  - 23-27
  - 29-37
  - 40-46
  - 49-60
  - 63-72
  - 75-107
  - 110-121
  - 124-168
  - 171-211
  - 214-254
  - 257-279
  - 282-322
  - 325-342
  - 345-378
  - 381-404
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

The `research` module orchestrates AI-assisted research workflows within the gwiki system, managing the complete lifecycle from initialization and scope resolution to enrichment execution and state tracking. It defines core domain models for research configuration, status, and audit findings, while providing utilities to process outcomes, extract and deduplicate code citations, sanitize paths, and estimate token usage. The module handles the creation, materialization, and acceptance of research notes, including frontmatter parsing, body rendering, and idempotent write strategies backed by atomic file operations and synchronization primitives. Comprehensive logic and test coverage validates enrichment behavior, note collision handling, path safety, and checkpoint-based state recovery.
[crates/gwiki/src/research/mod.rs:41]
[crates/gwiki/src/research/mod.rs:44-50]
[crates/gwiki/src/research/mod.rs:45-49]
[crates/gwiki/src/research/mod.rs:53-59]
[crates/gwiki/src/research/mod.rs:62-71]
[crates/gwiki/src/research/mod.rs:74]
[crates/gwiki/src/research/mod.rs:77-83]
[crates/gwiki/src/research/mod.rs:86-97]
[crates/gwiki/src/research/mod.rs:100-122]
[crates/gwiki/src/research/mod.rs:126-130]
[crates/gwiki/src/research/mod.rs:134-142]
[crates/gwiki/src/research/mod.rs:145-152]
[crates/gwiki/src/research/mod.rs:156-160]
[crates/gwiki/src/research/mod.rs:163-166]
[crates/gwiki/src/research/mod.rs:168-287]
[crates/gwiki/src/research/mod.rs:289-336]
[crates/gwiki/src/research/mod.rs:338-353]
[crates/gwiki/src/research/mod.rs:355-366]
[crates/gwiki/src/research/model.rs:21-24]
[crates/gwiki/src/research/model.rs:26-33]
[crates/gwiki/src/research/model.rs:27-32]
[crates/gwiki/src/research/model.rs:35-96]
[crates/gwiki/src/research/model.rs:36-95]
[crates/gwiki/src/research/model.rs:103-105]
[crates/gwiki/src/research/model.rs:107-129]
[crates/gwiki/src/research/model.rs:108-114]
[crates/gwiki/src/research/model.rs:116-128]
[crates/gwiki/src/research/model.rs:131-142]
[crates/gwiki/src/research/model.rs:144-146]
[crates/gwiki/src/research/model.rs:148-159]
[crates/gwiki/src/research/model.rs:149-158]
[crates/gwiki/src/research/model.rs:161-163]
[crates/gwiki/src/research/model.rs:165-181]
[crates/gwiki/src/research/model.rs:166-180]
[crates/gwiki/src/research/model.rs:183-204]
[crates/gwiki/src/research/model.rs:206-208]
[crates/gwiki/src/research/model.rs:210-218]
[crates/gwiki/src/research/model.rs:211-217]
[crates/gwiki/src/research/model.rs:220-222]
[crates/gwiki/src/research/model.rs:224-254]
[crates/gwiki/src/research/model.rs:225-233]
[crates/gwiki/src/research/model.rs:235-253]
[crates/gwiki/src/research/model.rs:256-259]
[crates/gwiki/src/research/model.rs:262-269]
[crates/gwiki/src/research/notes.rs:5-16]
[crates/gwiki/src/research/notes.rs:18-20]
[crates/gwiki/src/research/notes.rs:22-26]
[crates/gwiki/src/research/notes.rs:28-99]
[crates/gwiki/src/research/notes.rs:101-108]
[crates/gwiki/src/research/notes.rs:110-113]
[crates/gwiki/src/research/notes.rs:115-126]
[crates/gwiki/src/research/notes.rs:128-157]
[crates/gwiki/src/research/notes.rs:159-256]
[crates/gwiki/src/research/notes.rs:258-300]
[crates/gwiki/src/research/notes.rs:302-313]
[crates/gwiki/src/research/notes.rs:315-318]
[crates/gwiki/src/research/notes.rs:320-364]
[crates/gwiki/src/research/notes.rs:366-402]
[crates/gwiki/src/research/notes.rs:404-410]
[crates/gwiki/src/research/notes.rs:415-423]
[crates/gwiki/src/research/notes.rs:428-430]
[crates/gwiki/src/research/notes.rs:432-441]
[crates/gwiki/src/research/notes.rs:443-449]
[crates/gwiki/src/research/notes.rs:451-459]
[crates/gwiki/src/research/outcome.rs:15-24]
[crates/gwiki/src/research/outcome.rs:26-41]
[crates/gwiki/src/research/outcome.rs:43-51]
[crates/gwiki/src/research/outcome.rs:53-89]
[crates/gwiki/src/research/outcome.rs:91-99]
[crates/gwiki/src/research/outcome.rs:101-127]
[crates/gwiki/src/research/outcome.rs:129-147]
[crates/gwiki/src/research/outcome.rs:149-152]
[crates/gwiki/src/research/outcome.rs:154-171]
[crates/gwiki/src/research/outcome.rs:173-188]
[crates/gwiki/src/research/outcome.rs:190-200]
[crates/gwiki/src/research/outcome.rs:202-216]
[crates/gwiki/src/research/outcome.rs:221-228]
[crates/gwiki/src/research/outcome.rs:230-252]
[crates/gwiki/src/research/outcome.rs:254-329]
[crates/gwiki/src/research/outcome.rs:331-334]
[crates/gwiki/src/research/outcome.rs:336-344]
[crates/gwiki/src/research/outcome.rs:346-353]
[crates/gwiki/src/research/outcome.rs:360-372]
[crates/gwiki/src/research/outcome.rs:375-385]
[crates/gwiki/src/research/outcome.rs:388-426]
[crates/gwiki/src/research/outcome.rs:429-444]
[crates/gwiki/src/research/outcome.rs:447-457]
[crates/gwiki/src/research/outcome.rs:460-470]
[crates/gwiki/src/research/outcome.rs:473-482]
[crates/gwiki/src/research/storage.rs:12-59]
[crates/gwiki/src/research/storage.rs:61-91]
[crates/gwiki/src/research/storage.rs:93-95]
[crates/gwiki/src/research/storage.rs:97-135]
[crates/gwiki/src/research/storage.rs:137-151]
[crates/gwiki/src/research/storage.rs:153-155]
[crates/gwiki/src/research/storage.rs:157-159]
[crates/gwiki/src/research/storage.rs:168-177]
[crates/gwiki/src/research/tests.rs:8-21]
[crates/gwiki/src/research/tests.rs:23-27]
[crates/gwiki/src/research/tests.rs:29-37]
[crates/gwiki/src/research/tests.rs:40-46]
[crates/gwiki/src/research/tests.rs:49-60]
[crates/gwiki/src/research/tests.rs:63-72]
[crates/gwiki/src/research/tests.rs:75-107]
[crates/gwiki/src/research/tests.rs:110-121]
[crates/gwiki/src/research/tests.rs:124-168]
[crates/gwiki/src/research/tests.rs:171-211]
[crates/gwiki/src/research/tests.rs:214-254]
[crates/gwiki/src/research/tests.rs:257-279]
[crates/gwiki/src/research/tests.rs:282-322]
[crates/gwiki/src/research/tests.rs:325-342]
[crates/gwiki/src/research/tests.rs:345-378]
[crates/gwiki/src/research/tests.rs:381-404]

## Call Diagram

```mermaid
sequenceDiagram
    participant m_056d29d3_15b2_524f_806f_4036adacd1ef as deterministic_audit_uses_checkpoint_inventory &#91;function&#93;
    participant m_0de40973_2b45_5ccb_94c4_a204d4782919 as outcome_degradations &#91;function&#93;
    participant m_13b5734b_5766_58af_81ec_d3c9db0e3828 as default_options &#91;function&#93;
    participant m_179e1b62_c5b0_51b3_8b10_d38374ed5943 as outcome_code_citations_skip_empty_provenance &#91;function&#93;
    participant m_1e6f5c3a_eb65_5d14_b4a5_64c0ec372c80 as wait_for_materializing_research_note &#91;function&#93;
    participant m_21ac680c_12b4_5efe_aafd_805eddbdc1de as write_accepted_note &#91;function&#93;
    participant m_267a61df_4660_57e7_8002_45bafb2a723c as outcome_code_citations &#91;function&#93;
    participant m_2a9413c4_421f_51e7_992e_6ae55479173c as resolve_scope &#91;function&#93;
    participant m_2cff8301_37b0_50ca_9c64_9d1cc6ca3bba as create_materializing_research_note &#91;function&#93;
    participant m_2e751191_f2fe_5fa7_bf0e_8177b8228116 as dedup_strings &#91;function&#93;
    participant m_30524709_0f53_567d_97f0_27432eb4f00f as outcome_changed_paths &#91;function&#93;
    participant m_3bcd02ad_92fc_5a8f_a498_c43f23c2f089 as sanitize_code_path &#91;function&#93;
    participant m_42a3c4d6_bc96_5b49_a7fa_393fd94823de as remove_accepted_note_after_failure &#91;function&#93;
    participant m_436eb0c1_1863_50d7_b6ef_66006e8d7c0d as append_raw_index &#91;function&#93;
    participant m_44de0153_3b36_5444_8d45_1c93c694114d as research_scope_from_resolved &#91;function&#93;
    participant m_4a1fc371_011e_5a69_93d7_de14237c1c58 as accepted_note_draft_id &#91;function&#93;
    participant m_81ffca0c_119d_5a66_ace4_8391f76fd9b4 as dedup_code_citations &#91;function&#93;
    participant m_9684dbeb_e9a5_5f74_a6fb_58d4afcb9dcd as render_accepted_note_body &#91;function&#93;
    participant m_b0ffd1cb_2a0a_56b8_9d66_36231fe1560a as collect_keyed_strings &#91;function&#93;
    participant m_b12680e4_8e3f_59ad_a57e_ee6f35c02c20 as write_test_source &#91;function&#93;
    participant m_e6ab371c_3250_54e2_8e61_4c5d7f0113da as research_note_file_state &#91;function&#93;
    participant m_f4aacda3_69dc_5e9b_8f91_7c7c652ce558 as find_completed_accepted_note &#91;function&#93;
    m_056d29d3_15b2_524f_806f_4036adacd1ef->>m_13b5734b_5766_58af_81ec_d3c9db0e3828: calls
    m_056d29d3_15b2_524f_806f_4036adacd1ef->>m_b12680e4_8e3f_59ad_a57e_ee6f35c02c20: calls
    m_0de40973_2b45_5ccb_94c4_a204d4782919->>m_2e751191_f2fe_5fa7_bf0e_8177b8228116: calls
    m_0de40973_2b45_5ccb_94c4_a204d4782919->>m_b0ffd1cb_2a0a_56b8_9d66_36231fe1560a: calls
    m_179e1b62_c5b0_51b3_8b10_d38374ed5943->>m_267a61df_4660_57e7_8002_45bafb2a723c: calls
    m_1e6f5c3a_eb65_5d14_b4a5_64c0ec372c80->>m_e6ab371c_3250_54e2_8e61_4c5d7f0113da: calls
    m_21ac680c_12b4_5efe_aafd_805eddbdc1de->>m_2cff8301_37b0_50ca_9c64_9d1cc6ca3bba: calls
    m_21ac680c_12b4_5efe_aafd_805eddbdc1de->>m_42a3c4d6_bc96_5b49_a7fa_393fd94823de: calls
    m_21ac680c_12b4_5efe_aafd_805eddbdc1de->>m_436eb0c1_1863_50d7_b6ef_66006e8d7c0d: calls
    m_21ac680c_12b4_5efe_aafd_805eddbdc1de->>m_4a1fc371_011e_5a69_93d7_de14237c1c58: calls
    m_21ac680c_12b4_5efe_aafd_805eddbdc1de->>m_9684dbeb_e9a5_5f74_a6fb_58d4afcb9dcd: calls
    m_21ac680c_12b4_5efe_aafd_805eddbdc1de->>m_f4aacda3_69dc_5e9b_8f91_7c7c652ce558: calls
    m_267a61df_4660_57e7_8002_45bafb2a723c->>m_3bcd02ad_92fc_5a8f_a498_c43f23c2f089: calls
    m_267a61df_4660_57e7_8002_45bafb2a723c->>m_81ffca0c_119d_5a66_ace4_8391f76fd9b4: calls
    m_2a9413c4_421f_51e7_992e_6ae55479173c->>m_44de0153_3b36_5444_8d45_1c93c694114d: calls
    m_2cff8301_37b0_50ca_9c64_9d1cc6ca3bba->>m_1e6f5c3a_eb65_5d14_b4a5_64c0ec372c80: calls
    m_2cff8301_37b0_50ca_9c64_9d1cc6ca3bba->>m_9684dbeb_e9a5_5f74_a6fb_58d4afcb9dcd: calls
    m_2cff8301_37b0_50ca_9c64_9d1cc6ca3bba->>m_e6ab371c_3250_54e2_8e61_4c5d7f0113da: calls
    m_30524709_0f53_567d_97f0_27432eb4f00f->>m_2e751191_f2fe_5fa7_bf0e_8177b8228116: calls
    m_30524709_0f53_567d_97f0_27432eb4f00f->>m_b0ffd1cb_2a0a_56b8_9d66_36231fe1560a: calls
```

## Files

- [[code/files/crates/gwiki/src/research/mod.rs|crates/gwiki/src/research/mod.rs]] - `crates/gwiki/src/research/mod.rs` exposes 18 indexed API symbols.
[crates/gwiki/src/research/mod.rs:41]
[crates/gwiki/src/research/mod.rs:44-50]
[crates/gwiki/src/research/mod.rs:45-49]
[crates/gwiki/src/research/mod.rs:53-59]
[crates/gwiki/src/research/mod.rs:62-71]
[crates/gwiki/src/research/mod.rs:74]
[crates/gwiki/src/research/mod.rs:77-83]
[crates/gwiki/src/research/mod.rs:86-97]
[crates/gwiki/src/research/mod.rs:100-122]
[crates/gwiki/src/research/mod.rs:126-130]
[crates/gwiki/src/research/mod.rs:134-142]
[crates/gwiki/src/research/mod.rs:145-152]
[crates/gwiki/src/research/mod.rs:156-160]
[crates/gwiki/src/research/mod.rs:163-166]
[crates/gwiki/src/research/mod.rs:168-287]
[crates/gwiki/src/research/mod.rs:289-336]
[crates/gwiki/src/research/mod.rs:338-353]
[crates/gwiki/src/research/mod.rs:355-366]
- [[code/files/crates/gwiki/src/research/model.rs|crates/gwiki/src/research/model.rs]] - `crates/gwiki/src/research/model.rs` exposes 26 indexed API symbols.
[crates/gwiki/src/research/model.rs:21-24]
[crates/gwiki/src/research/model.rs:26-33]
[crates/gwiki/src/research/model.rs:27-32]
[crates/gwiki/src/research/model.rs:35-96]
[crates/gwiki/src/research/model.rs:36-95]
[crates/gwiki/src/research/model.rs:103-105]
[crates/gwiki/src/research/model.rs:107-129]
[crates/gwiki/src/research/model.rs:108-114]
[crates/gwiki/src/research/model.rs:116-128]
[crates/gwiki/src/research/model.rs:131-142]
[crates/gwiki/src/research/model.rs:144-146]
[crates/gwiki/src/research/model.rs:148-159]
[crates/gwiki/src/research/model.rs:149-158]
[crates/gwiki/src/research/model.rs:161-163]
[crates/gwiki/src/research/model.rs:165-181]
[crates/gwiki/src/research/model.rs:166-180]
[crates/gwiki/src/research/model.rs:183-204]
[crates/gwiki/src/research/model.rs:206-208]
[crates/gwiki/src/research/model.rs:210-218]
[crates/gwiki/src/research/model.rs:211-217]
[crates/gwiki/src/research/model.rs:220-222]
[crates/gwiki/src/research/model.rs:224-254]
[crates/gwiki/src/research/model.rs:225-233]
[crates/gwiki/src/research/model.rs:235-253]
[crates/gwiki/src/research/model.rs:256-259]
[crates/gwiki/src/research/model.rs:262-269]
- [[code/files/crates/gwiki/src/research/notes.rs|crates/gwiki/src/research/notes.rs]] - `crates/gwiki/src/research/notes.rs` exposes 20 indexed API symbols.
[crates/gwiki/src/research/notes.rs:5-16]
[crates/gwiki/src/research/notes.rs:18-20]
[crates/gwiki/src/research/notes.rs:22-26]
[crates/gwiki/src/research/notes.rs:28-99]
[crates/gwiki/src/research/notes.rs:101-108]
[crates/gwiki/src/research/notes.rs:110-113]
[crates/gwiki/src/research/notes.rs:115-126]
[crates/gwiki/src/research/notes.rs:128-157]
[crates/gwiki/src/research/notes.rs:159-256]
[crates/gwiki/src/research/notes.rs:258-300]
[crates/gwiki/src/research/notes.rs:302-313]
[crates/gwiki/src/research/notes.rs:315-318]
[crates/gwiki/src/research/notes.rs:320-364]
[crates/gwiki/src/research/notes.rs:366-402]
[crates/gwiki/src/research/notes.rs:404-410]
[crates/gwiki/src/research/notes.rs:415-423]
[crates/gwiki/src/research/notes.rs:428-430]
[crates/gwiki/src/research/notes.rs:432-441]
[crates/gwiki/src/research/notes.rs:443-449]
[crates/gwiki/src/research/notes.rs:451-459]
- [[code/files/crates/gwiki/src/research/outcome.rs|crates/gwiki/src/research/outcome.rs]] - `crates/gwiki/src/research/outcome.rs` exposes 25 indexed API symbols.
[crates/gwiki/src/research/outcome.rs:15-24]
[crates/gwiki/src/research/outcome.rs:26-41]
[crates/gwiki/src/research/outcome.rs:43-51]
[crates/gwiki/src/research/outcome.rs:53-89]
[crates/gwiki/src/research/outcome.rs:91-99]
[crates/gwiki/src/research/outcome.rs:101-127]
[crates/gwiki/src/research/outcome.rs:129-147]
[crates/gwiki/src/research/outcome.rs:149-152]
[crates/gwiki/src/research/outcome.rs:154-171]
[crates/gwiki/src/research/outcome.rs:173-188]
[crates/gwiki/src/research/outcome.rs:190-200]
[crates/gwiki/src/research/outcome.rs:202-216]
[crates/gwiki/src/research/outcome.rs:221-228]
[crates/gwiki/src/research/outcome.rs:230-252]
[crates/gwiki/src/research/outcome.rs:254-329]
[crates/gwiki/src/research/outcome.rs:331-334]
[crates/gwiki/src/research/outcome.rs:336-344]
[crates/gwiki/src/research/outcome.rs:346-353]
[crates/gwiki/src/research/outcome.rs:360-372]
[crates/gwiki/src/research/outcome.rs:375-385]
[crates/gwiki/src/research/outcome.rs:388-426]
[crates/gwiki/src/research/outcome.rs:429-444]
[crates/gwiki/src/research/outcome.rs:447-457]
[crates/gwiki/src/research/outcome.rs:460-470]
[crates/gwiki/src/research/outcome.rs:473-482]
- [[code/files/crates/gwiki/src/research/storage.rs|crates/gwiki/src/research/storage.rs]] - `crates/gwiki/src/research/storage.rs` exposes 8 indexed API symbols.
[crates/gwiki/src/research/storage.rs:12-59]
[crates/gwiki/src/research/storage.rs:61-91]
[crates/gwiki/src/research/storage.rs:93-95]
[crates/gwiki/src/research/storage.rs:97-135]
[crates/gwiki/src/research/storage.rs:137-151]
[crates/gwiki/src/research/storage.rs:153-155]
[crates/gwiki/src/research/storage.rs:157-159]
[crates/gwiki/src/research/storage.rs:168-177]
- [[code/files/crates/gwiki/src/research/tests.rs|crates/gwiki/src/research/tests.rs]] - `crates/gwiki/src/research/tests.rs` exposes 16 indexed API symbols.
[crates/gwiki/src/research/tests.rs:8-21]
[crates/gwiki/src/research/tests.rs:23-27]
[crates/gwiki/src/research/tests.rs:29-37]
[crates/gwiki/src/research/tests.rs:40-46]
[crates/gwiki/src/research/tests.rs:49-60]
[crates/gwiki/src/research/tests.rs:63-72]
[crates/gwiki/src/research/tests.rs:75-107]
[crates/gwiki/src/research/tests.rs:110-121]
[crates/gwiki/src/research/tests.rs:124-168]
[crates/gwiki/src/research/tests.rs:171-211]
[crates/gwiki/src/research/tests.rs:214-254]
[crates/gwiki/src/research/tests.rs:257-279]
[crates/gwiki/src/research/tests.rs:282-322]
[crates/gwiki/src/research/tests.rs:325-342]
[crates/gwiki/src/research/tests.rs:345-378]
[crates/gwiki/src/research/tests.rs:381-404]

## Components

- `a9592906-9822-528d-94ce-5acfb346e7e1`
- `5e5df1bc-fdba-5d61-b38b-287cc3a6b2e3`
- `cacab5fa-3084-5651-9fd9-6afc784e1efa`
- `512e9d62-ae27-5b7f-9bd0-b69a85c7d1ea`
- `9e7045cd-5bbd-5a02-a73c-2ddd1fbb6287`
- `18abcfeb-fbac-523b-8e77-d5750e8a0d3b`
- `3b3d5fe0-29b9-5bef-af24-2b602b83c514`
- `ae173efe-b988-5067-9025-2645e1497011`
- `5cd0abd0-fd57-5f51-ad30-ad6757867e4a`
- `d2f13344-e047-520a-b422-52457f67c44d`
- `d39c02f2-a870-5eb6-9cef-1f6b7327cb36`
- `23b64e0b-e6a8-59fe-b587-84aa32808467`
- `4cbd9ba8-475e-54a9-93b9-7618ae6536c4`
- `a2a0ab58-6b5e-51c8-be8c-6f27b67cbbf7`
- `63e69e37-0cdd-5019-8a50-4f82f6301d6e`
- `a1097965-374c-5feb-a5fc-344fcbeff697`
- `3dfd2008-9791-50f8-aa2d-49429cba735d`
- `1df0202d-d5e8-5355-91dc-9019a02c104b`
- `b1dfc6dd-5168-54a2-afa3-49c24d5147c8`
- `3ee55bc7-7354-547e-ba42-a0cc7cf5f563`
- `3e30be16-a998-5e22-ba40-a8bc4e7daeb9`
- `cfca1604-d73b-54b7-b92d-82ed622e3acf`
- `b732a8bd-725c-5999-a9c3-d4f4b5d6c512`
- `64ba9cc6-80e9-5a27-9a57-330fb449554a`
- `75e47f3c-8b22-57e6-8940-19f53300c15a`
- `d88e1e01-7d30-5d3b-b183-885529b5e9c1`
- `bbb0f800-11ca-5198-b641-da93f5ab2e64`
- `87ca6721-3c00-52c5-82a7-2e59d7d17529`
- `ffd5be04-2b79-5830-b991-a7777464b837`
- `50174e5a-60d9-5ba2-b6a4-e17d2d94c959`
- `410da895-6404-58a3-b146-11bb37b8b5ef`
- `c1ff3510-efe1-5dc6-bbf3-5bfb1891a02d`
- `234865bd-d25d-5fb5-bc01-b37a5ec218d4`
- `9170e976-9638-53ea-aa9c-988a1e590b4e`
- `bfb54443-4e66-57d4-8134-96488a726413`
- `ad2c4899-e097-58b1-99f9-909c76105ede`
- `f1affbbb-7143-519e-af0b-daf6e5edeed7`
- `6ece662b-3dd0-58e5-9577-70edc92245b1`
- `822e30b8-608e-58f1-bb26-7ce8289b5520`
- `f9476f6f-462f-580f-9d87-e67a4aba1c05`
- `a7e137f4-8613-542f-a902-d5cd8d1df29d`
- `a37a0133-d303-5e31-b6b6-091941ee99a9`
- `80cb32ae-b2e5-5539-bbad-de692b503db3`
- `47d24729-4808-5a0e-b215-87e2f82ead30`
- `39fa6fba-c484-583a-af7a-cf12213274fd`
- `f2a4ecb5-d3c3-5e2a-8a80-fd9e113b9871`
- `d88dad28-77b4-551b-83c4-95f8f83c8e7a`
- `21ac680c-12b4-5efe-aafd-805eddbdc1de`
- `42a3c4d6-bc96-5b49-a7fa-393fd94823de`
- `0026686d-e325-540d-89a9-095cd0d9a045`
- `6702468d-220a-5ef7-8898-14705915edb0`
- `9684dbeb-e9a5-5f74-a6fb-58d4afcb9dcd`
- `2cff8301-37b0-50ca-9c64-9d1cc6ca3bba`
- `1e6f5c3a-eb65-5d14-b4a5-64c0ec372c80`
- `4a1fc371-011e-5a69-93d7-de14237c1c58`
- `9a8c65d0-3312-5c81-b395-8edd9e6f69ab`
- `f4aacda3-69dc-5e9b-8f91-7c7c652ce558`
- `e6ab371c-3250-54e2-8e61-4c5d7f0113da`
- `5e40ccee-6ae7-5585-99d1-79a1aa84e306`
- `57b1b64a-6c33-50ad-9ae3-16b972902abe`
- `a5f7cfa2-0174-5c10-9fa2-5f08d0d84731`
- `7b61d0e7-f6c7-54ab-8a58-09df1eb64871`
- `58efe48a-bb61-5c4c-8095-46e0995df6e8`
- `436eb0c1-1863-50d7-b6ef-66006e8d7c0d`
- `3f73fdeb-40b8-55c5-a707-2ef2588523b9`
- `7feb8773-b9dc-546f-92a2-326263a2697c`
- `30524709-0f53-567d-97f0-27432eb4f00f`
- `267a61df-4660-57e7-8002-45bafb2a723c`
- `0de40973-2b45-5ccb-94c4-a204d4782919`
- `81ffca0c-119d-5a66-ace4-8391f76fd9b4`
- `3bcd02ad-92fc-5a8f-a498-c43f23c2f089`
- `943d2eac-a830-5792-acf5-2e7b28cfd20e`
- `b0ffd1cb-2a0a-56b8-9d66-36231fe1560a`
- `6c6d19ef-3312-5994-abb8-995d91517426`
- `2e751191-f2fe-5fa7-bf0e-8177b8228116`
- `d15b1643-f85e-5196-98de-6525165bfb2c`
- `83785a6f-5462-5830-9a43-cc2684b4c0c1`
- `c286c89d-836d-571a-bfd0-36f12439799e`
- `5c4741f3-51f8-5941-b093-806815b6a0dc`
- `0032b8e7-e67d-5a56-b577-9a5672bf23ed`
- `2a9413c4-421f-51e7-992e-6ae55479173c`
- `44de0153-3b36-5444-8d45-1c93c694114d`
- `803e1430-93c2-59f0-9ff6-1b8a38f41c97`
- `5f2ea15f-b7df-54aa-9cc6-fd25a47ebca9`
- `bd215855-2bfb-51af-b331-6059420ed755`
- `5927f5ca-cf9a-554d-8634-34adf496068f`
- `b2272a0d-a49f-56f9-a1cc-7fe96a8fa0b4`
- `179e1b62-c5b0-51b3-8b10-d38374ed5943`
- `c302f376-befe-5b5f-b907-1d1a6c6b02c9`
- `8350b255-90ba-5990-a64e-0be468f89b09`
- `f102ddcd-2977-5479-b47b-5ab922ea849b`
- `e4a7d4e9-4b8a-5ac0-bd98-6bb67cad59ee`
- `adbe7184-ed5f-5dd8-81b5-c18605d3255e`
- `ad72a37c-2940-58a4-a9da-1ab2cc134772`
- `3524a1ec-5f88-5205-8039-b2fb2444c9bb`
- `593726c8-23ee-50b6-8cd1-183cce9ff468`
- `4e521ef2-ee96-56ee-92de-b3af8f2a5ffa`
- `13b5734b-5766-58af-81ec-d3c9db0e3828`
- `b12680e4-8e3f-59ad-a57e-ee6f35c02c20`
- `0f10de80-17f0-5662-8e92-b3ad1f74b9a0`
- `11374150-465b-5b1b-a9c9-e5761f2e5757`
- `7d97c472-54ca-5f2e-ba9b-107806d8cd1c`
- `b21f4c12-f9cd-5388-946f-ddc70ab64506`
- `9dde5b11-f509-5812-87a4-d4420c1bcb1c`
- `3a4a270e-8dab-5f9a-b9eb-ae77b7ec380c`
- `ac78227a-61dc-546f-9cca-af5959828709`
- `9f6b4c1c-a3aa-5ad1-bf7c-cfc633cac90d`
- `10392a73-4fb7-5493-a33e-02de7abdca95`
- `f4481eab-b66e-5c65-a9ba-b1cce99e4ab4`
- `41e5c4e1-dc14-5784-bd05-52e948963b96`
- `9185e3dd-392b-5e25-b471-f6a8a0a02ce5`
- `72642458-367b-58eb-94d3-9c56dae32ad5`
- `056d29d3-15b2-524f-806f-4036adacd1ef`

