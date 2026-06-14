---
title: crates/gcode/src/vector
type: code_module
provenance:
- file: crates/gcode/src/vector/code_symbols.rs
  ranges:
  - 1-28
- file: crates/gcode/src/vector/code_symbols/embedding.rs
  ranges:
  - 21-23
  - 26-29
  - 31-35
  - 37-41
  - 44-47
  - 49-121
  - 123-126
  - 128-140
  - 142-145
  - 147-179
  - 181-203
  - 205-211
  - 213-216
  - 218-224
  - 226-247
  - 249-270
  - 272-287
  - 289-320
  - 331-333
  - 335-341
  - 343-354
  - 357-391
  - 394-416
  - 419-442
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
  ranges:
  - 29-37
  - 39-43
  - 45-56
  - 58-376
  - 378-389
  - 391-393
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
  ranges:
  - 18-24
  - 26-28
  - 30-37
  - 39-47
  - 49-76
  - 78-99
  - 101-111
  - 113-124
  - 126-141
  - 143-152
  - 154-164
  - 166-173
  - 175-194
  - 196-217
  - 219-227
  - 229-299
  - 301-311
  - 318-323
  - 326-336
- file: crates/gcode/src/vector/code_symbols/repository.rs
  ranges:
  - 6-18
  - 20-25
  - 27-35
  - 38-43
  - 45-56
  - 59-77
- file: crates/gcode/src/vector/code_symbols/search.rs
  ranges:
  - 8-14
  - 16-26
  - '28'
  - 30-58
  - 63-81
- file: crates/gcode/src/vector/code_symbols/tests.rs
  ranges:
  - 13-34
  - 36-44
  - 47-74
  - 77-86
  - 89-94
  - 97-102
  - 105-117
  - 120-137
  - 139-153
  - 156-167
  - 170-184
  - 187-236
  - 239-256
  - 259-321
  - 324-364
  - 367-390
  - 393-422
  - 425-463
  - 466-512
  - 515-580
  - 583-653
  - 656-703
  - 705-762
  - 764-783
  - 785-796
  - 798-803
  - 805-819
  - 821-838
  - 840-849
  - 851-859
  - 862-873
  - 876-884
  - 886-915
  - 917-937
  - 939-979
- file: crates/gcode/src/vector/code_symbols/types.rs
  ranges:
  - 7-12
  - 15-18
  - 20-24
  - '26'
  - 29-57
  - 59-96
  - 100-105
  - 108-112
  - 115-118
  - 121-124
  - 127-137
  - 140-162
  - 164-203
  - 205-209
  - '211'
- file: crates/gcode/src/vector/mod.rs
  ranges:
  - 1-2
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `crates/gcode/src/vector` module is a small entry point that exposes vector functionality through its `code_symbols` submodule, making semantic code-symbol indexing available to the rest of the crate via `pub mod code_symbols` [crates/gcode/src/vector/mod.rs:1-2]. The `code_symbols` facade gathers the public API from its internal embedding, lifecycle, Qdrant, repository, search, and type modules, so callers can use one namespace for embedding text and queries, probing dimensions, resolving embedding sources, fetching repository symbols, managing vector collections, deleting project or file vectors, and running semantic searches [crates/gcode/src/vector/code_symbols.rs:1-21].

Its key flow starts with repository symbol extraction, turns `Symbol` records into vector text and payloads, embeds that text, and stores or searches the resulting vectors in Qdrant-backed collections. The child module summaries show that shared types carry search requests and hits, payload provenance, source locations, symbol identity, lifecycle status/output/schema data, and lifecycle errors, with tests covering preserved metadata and optional summary enrichment [crates/gcode/src/vector/code_symbols/tests.rs:47-74]. Embedding support sits at the front of that flow by abstracting daemon-backed AI contexts and direct embedding configs, validating direct configuration, caching blocking clients, applying query prefixes, supporting single and batch embeddings, and providing a fixed probe text for dimension checks [crates/gcode/src/vector/code_symbols/embedding.rs:58-100].

The files collaborate through `code_symbols.rs` as a public facade rather than exposing each implementation module directly. Lifecycle APIs coordinate collection setup, schema compatibility, sync, rebuild, and status reporting; Qdrant APIs handle collection naming, deletion, vector search, and distance configuration; repository APIs fetch symbols at file or project scope; search APIs provide higher-level semantic lookup and error handling; and the type exports define the request, hit, payload, lifecycle, schema, and error structures shared across those operations [crates/gcode/src/vector/code_symbols.rs:7-21].

## Call Diagram

```mermaid
sequenceDiagram
    participant m_068f6d68_9c77_52ed_b5a6_7f2c8768040e as payloads_carry_provenance_metadata &#91;function&#93;
    participant m_08abaa70_62f0_5531_b9e1_6d5eb0ab736b as char_literal_end &#91;function&#93;
    participant m_0bad8712_4896_5d24_b607_9c25e4d63188 as rust_code_without_comments_and_literals &#91;function&#93;
    participant m_0e7c1d57_7114_50e2_84a9_1682d3a28e18 as delete_qdrant_collection &#91;function&#93;
    participant m_11d61977_239b_50f6_bf35_94bb6e9f1977 as direct_source_uses_resolved_embedding_config &#91;function&#93;
    participant m_12b82731_a570_5519_941a_7ecf340f9c75 as skip_block_comment &#91;function&#93;
    participant m_1789414f_d055_5920_9aa3_af279ef7de96 as delete_file_vectors_skips_delete_when_count_is_zero &#91;function&#93;
    participant m_1e1583c9_745e_5c42_856e_5e1b261b64fd as EmbeddingBackend.new &#91;method&#93;
    participant m_207703c8_c51f_58dc_a2dd_7cecf74d1cfc as delete_file_vectors &#91;function&#93;
    participant m_2107d03f_8e95_51cc_a7a8_05371b1b45a2 as lifecycle_http_scoped_to_module &#91;function&#93;
    participant m_24dee124_d569_52ac_a227_d502192f3000 as fetch_symbols_for_project &#91;function&#93;
    participant m_2891b793_606c_5557_b81f_6fba2da95d75 as sync_rejects_embedding_vectors_with_wrong_dimension &#91;function&#93;
    participant m_55b43c4d_6aaf_578e_b5ef_eceb572052da as skip_quoted_string &#91;function&#93;
    participant m_6ab7845d_4731_546c_a29b_8405430b3241 as raw_hashes_match &#91;function&#93;
    participant m_701ba072_c2f3_5035_8c2f_eca788ac5617 as embedding_source_from_resolved_ai_context &#91;function&#93;
    participant m_753537a7_c2e6_552d_b8ef_08f7def1f99b as collection_name &#91;function&#93;
    participant m_79becebc_7348_56eb_b09e_07ea3974921b as spawn_http_responses &#91;function&#93;
    participant m_7f9161ad_3ab2_5577_8ac0_3562563d9937 as qdrant_request_for_config &#91;function&#93;
    participant m_823584ac_ee4f_5a77_9d40_ad2f95e4988f as test_symbol &#91;function&#93;
    participant m_86e32944_ff07_5f89_aac1_3be7ffc98412 as push_masked &#91;function&#93;
    participant m_9e348111_a612_5af1_97d4_c9447ffde82c as escaped_char_literal_payload_end &#91;function&#93;
    participant m_ae80a1c0_b3d5_5643_82c4_37a9507a9d52 as visit &#91;function&#93;
    participant m_bb5add13_83d0_5d5f_97a5_b318647215f4 as fetch_symbols_where &#91;function&#93;
    participant m_d1f6ab42_05ef_5849_b9c8_27615e3b516b as collection_path &#91;function&#93;
    participant m_d35c16dd_7eb0_5a67_b10f_6ae70cac681b as qdrant_http_error &#91;function&#93;
    participant m_ec0b0c90_cf56_5a49_bea0_b8c2fabb962a as delete_vectors_for_filter &#91;function&#93;
    participant m_f036e431_77ef_5476_a9a5_af731616f618 as embedding_client &#91;function&#93;
    participant m_f3d7949d_38d5_5480_9aed_dbc8c0d1f455 as raw_string_prefix &#91;function&#93;
    participant m_f9ba033c_f3c6_5bc3_8b1f_e7b40ad825f4 as qdrant_http_client &#91;function&#93;
    m_068f6d68_9c77_52ed_b5a6_7f2c8768040e->>m_823584ac_ee4f_5a77_9d40_ad2f95e4988f: calls
    m_08abaa70_62f0_5531_b9e1_6d5eb0ab736b->>m_9e348111_a612_5af1_97d4_c9447ffde82c: calls
    m_0bad8712_4896_5d24_b607_9c25e4d63188->>m_08abaa70_62f0_5531_b9e1_6d5eb0ab736b: calls
    m_0bad8712_4896_5d24_b607_9c25e4d63188->>m_12b82731_a570_5519_941a_7ecf340f9c75: calls
    m_0bad8712_4896_5d24_b607_9c25e4d63188->>m_55b43c4d_6aaf_578e_b5ef_eceb572052da: calls
    m_0bad8712_4896_5d24_b607_9c25e4d63188->>m_6ab7845d_4731_546c_a29b_8405430b3241: calls
    m_0bad8712_4896_5d24_b607_9c25e4d63188->>m_86e32944_ff07_5f89_aac1_3be7ffc98412: calls
    m_0bad8712_4896_5d24_b607_9c25e4d63188->>m_f3d7949d_38d5_5480_9aed_dbc8c0d1f455: calls
    m_0e7c1d57_7114_50e2_84a9_1682d3a28e18->>m_7f9161ad_3ab2_5577_8ac0_3562563d9937: calls
    m_0e7c1d57_7114_50e2_84a9_1682d3a28e18->>m_d1f6ab42_05ef_5849_b9c8_27615e3b516b: calls
    m_0e7c1d57_7114_50e2_84a9_1682d3a28e18->>m_d35c16dd_7eb0_5a67_b10f_6ae70cac681b: calls
    m_11d61977_239b_50f6_bf35_94bb6e9f1977->>m_701ba072_c2f3_5035_8c2f_eca788ac5617: calls
    m_1789414f_d055_5920_9aa3_af279ef7de96->>m_79becebc_7348_56eb_b09e_07ea3974921b: calls
    m_1e1583c9_745e_5c42_856e_5e1b261b64fd->>m_f036e431_77ef_5476_a9a5_af731616f618: calls
    m_207703c8_c51f_58dc_a2dd_7cecf74d1cfc->>m_753537a7_c2e6_552d_b8ef_08f7def1f99b: calls
    m_207703c8_c51f_58dc_a2dd_7cecf74d1cfc->>m_ec0b0c90_cf56_5a49_bea0_b8c2fabb962a: calls
    m_207703c8_c51f_58dc_a2dd_7cecf74d1cfc->>m_f9ba033c_f3c6_5bc3_8b1f_e7b40ad825f4: calls
    m_2107d03f_8e95_51cc_a7a8_05371b1b45a2->>m_ae80a1c0_b3d5_5643_82c4_37a9507a9d52: calls
    m_24dee124_d569_52ac_a227_d502192f3000->>m_bb5add13_83d0_5d5f_97a5_b318647215f4: calls
    m_2891b793_606c_5557_b81f_6fba2da95d75->>m_79becebc_7348_56eb_b09e_07ea3974921b: calls
```

## Child Modules

- [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]] - The `code_symbols` vector module owns semantic indexing and lookup for extracted code symbols. Its shared types define search requests and hits, vector payloads built from `Symbol` records, lifecycle status/output/schema structs, and common lifecycle errors, while tests show payloads preserving provenance, source location, symbol identity, and optional enrichment like summaries  [crates/gcode/src/vector/code_symbols/tests.rs:47-74]. Embedding support abstracts over daemon-backed AI contexts and direct embedding configs, validates direct configuration, caches blocking clients, applies query prefixes, and exposes both single-text and batch embedding paths plus the fixed probe text used for dimensionality checks   [crates/gcode/src/vector/code_symbols/embedding.rs:58-100].

The lifecycle flow centers on `CodeSymbolVectorLifecycle`, which combines a project id, derived Qdrant collection name, Qdrant config, embedding backend, vector settings, probed vector size, and blocking HTTP client . Creation validates the Qdrant boundary config, derives a stable code-symbol collection from the configured prefix and project id, constructs the embedding backend, and prepares a timeout-scoped client . Repository helpers feed that lifecycle by selecting symbols for a project or file through a shared predicate path, binding the appropriate SQL parameters, materializing `Symbol` rows, and ordering them by file path, byte offset, and id .

Qdrant integration provides the storage boundary used by lifecycle and search: it normalizes collection names through `gobby_core::qdrant`, builds encoded collection paths, caches HTTP clients, deletes whole project collections or per-file vectors, deletes all prefixed code-symbol collections, parses Qdrant responses, and reports degraded search behavior when Qdrant is missing or unreachable  . The search layer wraps this with user-facing errors for missing configuration, embedding failures, invalid collection naming, and transport failures, while the test suite exercises naming, deletion scoping, batch embedding order, sync validation, dimension probing, and HTTP lifecycle scoping across the collaborating files  .

## Files

- [[code/files/crates/gcode/src/vector/code_symbols.rs|crates/gcode/src/vector/code_symbols.rs]] - Re-exports the public API for code-symbol vector indexing and semantic search, wiring together embedding, lifecycle, Qdrant storage, repository symbol extraction, search, and shared vector types for the `gcode` vector module. [crates/gcode/src/vector/code_symbols.rs:1-28]
- [[code/files/crates/gcode/src/vector/mod.rs|crates/gcode/src/vector/mod.rs]] - Module entry point for the `vector` package, declaring the `code_symbols` submodule so vector-related code symbols are available to the crate. [crates/gcode/src/vector/mod.rs:1-2]

