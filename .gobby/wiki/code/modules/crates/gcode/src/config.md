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
  - 65-128
  - 130-134
  - 137-140
  - 142-152
  - '154'
  - 156-164
  - 168-191
  - 194-203
  - 206-209
  - 212-219
  - 222-229
  - 231-335
  - 337-390
  - 392-446
  - 448-456
  - 458-466
  - 468-476
  - 478-509
  - 511-518
  - 523-547
  - 549-551
  - 559-562
  - 564-600
  - 609-611
  - 613-621
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
  - 198-222
  - '224'
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
  - 518-525
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The config module is responsible for turning bootstrap, database, config-store, standalone file, environment, Git, filesystem, and `.gobby` metadata into the runtime configuration used by `gcode`. Its central `context.rs` types define the runtime-facing shapes for FalkorDB, Qdrant, embeddings, code-vector settings, indexing settings, and service-selection presets, including constants for graph names, collection prefixes, environment keys, and config-store keys . `Context` resolution then combines those service settings with project identity and project-root discovery, including helpers for isolated overlays, parent roots, normalized IDs, project-name lookup, and absolute-path fallbacks.

The service flow lives in `services.rs`, where a shared `ServiceConfigSource` interface lets the module read raw config values and resolve secret or variable references through different backing stores [crates/gcode/src/config/services.rs:20-22]. PostgreSQL-backed reads decode config-store values, treat a missing config table as an absent value, and resolve stored secrets through the database connection . Environment overrides are mapped for FalkorDB and Qdrant keys up front, while fallback source adapters layer PostgreSQL, optional `gcore.yaml` standalone config, tracing, closure sources, and error capture so concrete resolvers can consistently choose defaults, propagate failures, and report which source supplied a value .

The files collaborate with tests that exercise the same boundaries the runtime code depends on: service-value parsing, environment precedence, secret resolution, missing or invalid ports, embedding error propagation, daemon URL fallback, and project-identity edge cases. `tests.rs` builds realistic fixtures by writing `.gobby/project.json`, initializing Git repositories, creating linked worktrees, and scoping service environment variables so project ID and service config behavior can be verified across normal repos, copied metadata, isolated overlays, and generated identities [crates/gcode/src/config/tests.rs:14-22]  .

## Call Diagram

```mermaid
sequenceDiagram
    participant m_011a0baa_dc8d_5b8e_b0e9_cb9f4295edb3 as falkor_password_reads_password_key &#91;function&#93;
    participant m_025b4846_7970_5700_99f0_0ccabc7ebfc4 as resolve_embedding_config &#91;function&#93;
    participant m_037d8ca9_2112_5a2a_a6d8_fc5b94b97da4 as self_referential_parent_marker_keeps_project_json_id &#91;function&#93;
    participant m_0726e300_44c4_51cc_abca_bed13666836f as vector_dim_setting_reads_ai_config_no_env &#91;function&#93;
    participant m_080a3cf9_226c_583b_84d1_37d8144cf37d as Context.resolve_for_project_id &#91;method&#93;
    participant m_0ba6c756_8d10_575b_adba_be13dedfe9cf as is_self_referential_isolation_marker &#91;function&#93;
    participant m_1c0fa5fa_a8b0_5b8b_8d48_e43da3c43b16 as config_value &#91;function&#93;
    participant m_1f13e8b8_ed66_50e9_99cf_6e6a742d4c0c as resolve_falkordb_config_from_source &#91;function&#93;
    participant m_28c47d46_bd7b_5133_b7c7_372cfc12895e as resolve_embedding_config_from_source &#91;function&#93;
    participant m_2ac646f0_7ad2_54bd_969e_9f0be46734dc as main_repo_keeps_project_json_id &#91;function&#93;
    participant m_3279a046_bbbe_594e_83d8_f146c1faea61 as resolve_project_id &#91;function&#93;
    participant m_3308f5d4_fe0e_5ddd_86b0_1a239ad5cbc4 as config_value &#91;function&#93;
    participant m_3a3fcf9e_3bc0_592a_936a_6c4014fc535f as resolve_code_vector_settings &#91;function&#93;
    participant m_3ece38b5_268b_5b8a_9823_117d1d053be8 as phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name &#91;function&#93;
    participant m_43346b4a_a439_52fb_b995_db9d5f53bc03 as embedding_binding_uses_openai_http &#91;function&#93;
    participant m_481ab8e0_920d_5092_82f8_60e726ec5b68 as config_value &#91;function&#93;
    participant m_595fac55_0d4e_55e5_b2fd_69fe49196253 as write_project_json &#91;function&#93;
    participant m_73a8e787_c170_5e1d_82eb_c9430da704fd as embedding_binding_routes_direct &#91;function&#93;
    participant m_7cfbc9d2_c867_5ffb_87d4_54932a1df488 as resolve_project_identity &#91;function&#93;
    participant m_80b86ae0_52b6_557e_a3f7_fcd29acbffbd as with_service_env &#91;function&#93;
    participant m_8c73cf1c_116b_549f_a285_656fb12318b7 as service_env_value &#91;function&#93;
    participant m_9138da44_4687_593a_95c5_29b8cbd7391a as resolve_service_port &#91;function&#93;
    participant m_9685df1c_b537_5fd4_a2a4_296cabc2ea30 as resolve_parent_project_root &#91;function&#93;
    participant m_99326af5_69bd_5565_bee6_cb3375d238ae as config_value_for &#91;function&#93;
    participant m_a3104df3_262f_55d2_b96d_e90615651334 as resolve_code_vector_settings_from_source &#91;function&#93;
    participant m_a5a01ca9_8086_52b4_97c9_132d324c6f85 as resolve_service_setting &#91;function&#93;
    participant m_ac53669b_29ee_5344_acd8_336ad0104d53 as resolve_embedding_config_from_service_source &#91;function&#93;
    participant m_df11b4d5_8541_54fe_ab58_fe0a5ac0557b as normalize_project_id &#91;function&#93;
    m_011a0baa_dc8d_5b8e_b0e9_cb9f4295edb3->>m_80b86ae0_52b6_557e_a3f7_fcd29acbffbd: calls
    m_011a0baa_dc8d_5b8e_b0e9_cb9f4295edb3->>m_99326af5_69bd_5565_bee6_cb3375d238ae: calls
    m_025b4846_7970_5700_99f0_0ccabc7ebfc4->>m_ac53669b_29ee_5344_acd8_336ad0104d53: calls
    m_037d8ca9_2112_5a2a_a6d8_fc5b94b97da4->>m_595fac55_0d4e_55e5_b2fd_69fe49196253: calls
    m_0726e300_44c4_51cc_abca_bed13666836f->>m_80b86ae0_52b6_557e_a3f7_fcd29acbffbd: calls
    m_0726e300_44c4_51cc_abca_bed13666836f->>m_99326af5_69bd_5565_bee6_cb3375d238ae: calls
    m_080a3cf9_226c_583b_84d1_37d8144cf37d->>m_df11b4d5_8541_54fe_ab58_fe0a5ac0557b: calls
    m_0ba6c756_8d10_575b_adba_be13dedfe9cf->>m_9685df1c_b537_5fd4_a2a4_296cabc2ea30: calls
    m_1c0fa5fa_a8b0_5b8b_8d48_e43da3c43b16->>m_8c73cf1c_116b_549f_a285_656fb12318b7: calls
    m_1f13e8b8_ed66_50e9_99cf_6e6a742d4c0c->>m_9138da44_4687_593a_95c5_29b8cbd7391a: calls
    m_1f13e8b8_ed66_50e9_99cf_6e6a742d4c0c->>m_a5a01ca9_8086_52b4_97c9_132d324c6f85: calls
    m_28c47d46_bd7b_5133_b7c7_372cfc12895e->>m_43346b4a_a439_52fb_b995_db9d5f53bc03: calls
    m_28c47d46_bd7b_5133_b7c7_372cfc12895e->>m_73a8e787_c170_5e1d_82eb_c9430da704fd: calls
    m_2ac646f0_7ad2_54bd_969e_9f0be46734dc->>m_595fac55_0d4e_55e5_b2fd_69fe49196253: calls
    m_3279a046_bbbe_594e_83d8_f146c1faea61->>m_7cfbc9d2_c867_5ffb_87d4_54932a1df488: calls
    m_3308f5d4_fe0e_5ddd_86b0_1a239ad5cbc4->>m_8c73cf1c_116b_549f_a285_656fb12318b7: calls
    m_3a3fcf9e_3bc0_592a_936a_6c4014fc535f->>m_a3104df3_262f_55d2_b96d_e90615651334: calls
    m_3ece38b5_268b_5b8a_9823_117d1d053be8->>m_80b86ae0_52b6_557e_a3f7_fcd29acbffbd: calls
    m_3ece38b5_268b_5b8a_9823_117d1d053be8->>m_99326af5_69bd_5565_bee6_cb3375d238ae: calls
    m_481ab8e0_920d_5092_82f8_60e726ec5b68->>m_8c73cf1c_116b_549f_a285_656fb12318b7: calls
```

## Files

- [[code/files/crates/gcode/src/config/context.rs|crates/gcode/src/config/context.rs]] - Configuration resolution for `gcode`: it defines the service and indexing config types used to load FalkorDB, Qdrant, embedding, and code-vector settings from bootstrap/database/config-store sources, then combines them into a runtime `Context`. `ServiceConfigSelection` provides preset feature combinations for selectively enabling config groups, while `FalkorConfig`, `CodeVectorSettings`, and the related error type adapt and validate individual settings. The rest of the file resolves project identity and project roots from CLI, filesystem, Git, and `.gobby` metadata, validates overlay parents, and exposes helpers for name lookup, ID normalization, and absolute-path fallback so `Context` can be assembled consistently.
[crates/gcode/src/config/context.rs:26-31]
[crates/gcode/src/config/context.rs:34]
[crates/gcode/src/config/context.rs:37]
[crates/gcode/src/config/context.rs:51-53]
[crates/gcode/src/config/context.rs:55]
- [[code/files/crates/gcode/src/config/services.rs|crates/gcode/src/config/services.rs]] - This file provides the service-configuration plumbing for Gobby, layering environment variables, PostgreSQL-backed config, and optional standalone `gcore.yaml` settings to resolve service-specific values. It defines small config-source adapters (`PostgresConfigSource`, `FallbackConfigSource`, `TracingFallbackConfigSource`, `ErrorCapturingConfigSource`, and closure-based variants) that implement a common read/resolve interface, plus helpers for reading standalone config and reporting detailed read errors. On top of that, it builds the concrete resolvers for FalkorDB, Qdrant, embedding, code vector, and indexing settings, handling defaults, fallback order, tracing which source won, and preserving or surfacing configuration errors where needed.
[crates/gcode/src/config/services.rs:20-22]
[crates/gcode/src/config/services.rs:24-27]
[crates/gcode/src/config/services.rs:29-39]
[crates/gcode/src/config/services.rs:41-48]
[crates/gcode/src/config/services.rs:51-57]
- [[code/files/crates/gcode/src/config/tests.rs|crates/gcode/src/config/tests.rs]] - This file contains integration-style tests for `gcode` configuration resolution, especially how project identity, daemon URL selection, and service-specific settings are derived from on-disk config and environment variables. It also defines small test helpers for writing `.gobby/project.json`, running `git`, creating linked worktrees, and scoping service environment overrides so the tests can exercise precedence, secret resolution, error propagation, and project-identity edge cases consistently.
[crates/gcode/src/config/tests.rs:14-22]
[crates/gcode/src/config/tests.rs:24-38]
[crates/gcode/src/config/tests.rs:40-70]
[crates/gcode/src/config/tests.rs:80-90]
[crates/gcode/src/config/tests.rs:92-96]

## Components

- `53926106-6dfb-54e8-98e8-fba4322e5dec`
- `64da5dd7-9a46-54c3-856e-22934520004d`
- `fa989081-e16b-5255-84da-f2e8958ca42c`
- `3c239d5c-acad-5519-8278-7872a54e5164`
- `375d916b-30e4-55bb-9471-2f963f005197`
- `8627d53f-73ba-53a7-8e99-16b027b0b43a`
- `029d25d6-a9f9-55ef-9799-f9ebd8327d6d`
- `c9a1cb62-7c8b-5590-91d0-babf0631b4b8`
- `b42e3e41-716a-5888-9afa-b816f1a85ee2`
- `41215555-256a-53a5-8d44-c0787823aade`
- `d44cbbc0-04e9-56bf-91ba-8ba562319e21`
- `3349fe55-9b04-504a-a9e7-3bdfb5e169b9`
- `03212a41-cc6c-5713-b627-83a209fc66e2`
- `d131f6ff-2354-5288-bd28-36e855c70efe`
- `b5535775-36d5-51ed-bb74-2a52131f014d`
- `308f7c78-476f-5d36-850a-328dc71dc624`
- `3d9e9087-b154-567a-8eb9-dad0ec7045f5`
- `302c98c3-e822-5869-af5b-11a58358b9e8`
- `c28ef263-af5a-5965-8ea5-195137ce9fb8`
- `22983480-0fe3-5146-94ff-d38f0fd5232b`
- `7421db62-9042-544c-8a54-78e90e700f95`
- `e024baa0-26a9-57fd-8f01-3454080ca15f`
- `f57e9fb3-ef45-5bc0-8ec7-a20ecf40b698`
- `7a5353d3-da7f-5160-9017-b32e9548aab8`
- `d0fce310-84e4-5d23-bbaa-1e8dc55ac538`
- `bff5f934-378e-5722-a8c7-aa3e45ab5c5f`
- `4328c2c8-aef6-57af-8d4d-acda4afbab80`
- `43ccda88-4c91-59a6-83b2-13e434748844`
- `79949d65-3a16-5c20-bbf0-6e5df87b1e62`
- `e95640c9-aa2f-5ba7-bba7-48ae9a58781d`
- `080a3cf9-226c-583b-84d1-37d8144cf37d`
- `7cfbc9d2-c867-5ffb-87d4-54932a1df488`
- `18d3460c-76db-5074-b3af-d86fcd0683f7`
- `0ba6c756-8d10-575b-adba-be13dedfe9cf`
- `9685df1c-b537-5fd4-a2a4-296cabc2ea30`
- `df11b4d5-8541-54fe-ab58-fe0a5ac0557b`
- `41088d8a-c2ff-5f50-9475-d89b67da6e6c`
- `0910fc74-98a8-5ac5-923e-ae7c433cae75`
- `56db3f05-eb61-57d2-bfa1-b4122a9fe790`
- `fb177664-5c95-501e-835e-de9ee8b4ac6a`
- `63d19fa3-f4c6-587c-b5d2-842b7825f487`
- `50faa516-22bd-5620-8886-6625ef4f17ad`
- `3279a046-bbbe-594e-83d8-f146c1faea61`
- `ded563af-79a7-5b37-a1c0-90957a3d93d1`
- `2b5627ba-b022-5c99-835a-10b3270e595a`
- `376426c5-af74-5515-b43e-71c79b27ab8e`
- `8c73cf1c-116b-549f-a285-656fb12318b7`
- `a1772b25-eb88-5555-acb1-3c9813b557a8`
- `80bdc425-dbd1-58ce-b569-e6e623d260d5`
- `802f41f9-6958-57bc-9239-5b29484e96c1`
- `2b6de914-554a-5521-85c1-34566ed0e76f`
- `3308f5d4-fe0e-5ddd-86b0-1a239ad5cbc4`
- `195d3c75-4fd1-5d55-a58d-080bc7eadcdc`
- `bb3b2b04-75d3-55ea-8326-7ed800d721f2`
- `f7c3b020-528e-516b-9c1d-e31527b7bc42`
- `2fb164b7-eb7d-54c7-bd56-0099afebd78b`
- `481ab8e0-920d-5092-82f8-60e726ec5b68`
- `f022087b-8ec1-5b21-933f-28275f1a9573`
- `59d8cbb2-3be8-53e7-abbb-6ec9ef356504`
- `000f4592-81ca-57d8-9950-f933ff4a3b5b`
- `d72d83bd-5aba-5c26-9d16-8cf00cb01d4c`
- `8dad6043-0fc8-5236-8061-0fc3a429e032`
- `8331635c-e2f7-5a97-9965-1d6d996826fe`
- `254de7ef-9797-5f6a-9ca7-c0aa8622aaaa`
- `2d5d88cb-2717-5134-b681-3ea8d3a2ea39`
- `da9d2337-c68c-5956-836f-8bf397465272`
- `05c5c555-7356-5546-999e-a80d22f5e6d0`
- `8eb27418-fb2b-5858-97d5-ecd8a1d2c31d`
- `5e91dc97-455d-5172-9d43-060d723ef1b0`
- `4b90bf43-1cac-5d65-8f5e-0f85ba3713e2`
- `e9344c04-d2a9-5560-b9ea-55e565b88e79`
- `1c0fa5fa-a8b0-5b8b-8d48-e43da3c43b16`
- `d727e622-20ad-5169-8567-28f4c0624627`
- `dbbe6486-153b-5779-9a08-bd7aa071b2bd`
- `d2fc1ff4-a198-505e-af3e-b2a9ef8899d1`
- `0e207cc9-a653-5aea-ba44-60ecfbfed306`
- `cc9828a3-8814-52a1-b87c-59e38dc98650`
- `9aba8a5f-536d-5453-b5ce-7771f6fb29e8`
- `9330a412-575b-5152-a1cf-135a7f308e3a`
- `e103c19a-2c6c-527b-9159-a254b6795001`
- `c13ee5b5-4dea-5d41-a3c4-6e3f6ec63209`
- `c5730274-e339-57fc-bc15-d5abfecf7c0f`
- `1f13e8b8-ed66-50e9-99cf-6e6a742d4c0c`
- `a4e3d0c0-846c-53fa-adc2-c86422c8ebb6`
- `bdf63c4f-b439-55e6-b850-a837b76becdb`
- `a5a01ca9-8086-52b4-97c9-132d324c6f85`
- `c90f25cf-fbe0-5ed0-b097-77ef348556d1`
- `9138da44-4687-593a-95c5-29b8cbd7391a`
- `025b4846-7970-5700-99f0-0ccabc7ebfc4`
- `b0c9bb0b-c7a0-5542-bd3c-95f25dd812df`
- `ac53669b-29ee-5344-acd8-336ad0104d53`
- `28c47d46-bd7b-5133-b7c7-372cfc12895e`
- `73a8e787-c170-5e1d-82eb-c9430da704fd`
- `43346b4a-a439-52fb-b995-db9d5f53bc03`
- `3a3fcf9e-3bc0-592a-936a-6c4014fc535f`
- `89da399d-3b25-55ce-a12e-30c060540b8c`
- `a3104df3-262f-55d2-b96d-e90615651334`
- `6b815bbb-2a31-5fae-9311-56606fe1ad6b`
- `688cb87e-bc31-5fda-a82d-3fd925232ac4`
- `595fac55-0d4e-55e5-b2fd-69fe49196253`
- `f7f4f1d9-0ff8-51db-b7e9-3b84c3dc6657`
- `e65d015b-ff27-55ad-991f-4d67c5588b34`
- `80b86ae0-52b6-557e-a3f7-fcd29acbffbd`
- `99326af5-69bd-5565-bee6-cb3375d238ae`
- `9681c9c5-f04e-5c15-8d67-f0a4b2222fcf`
- `76c2c53a-d210-5ce2-bcda-aef0b42e95eb`
- `4b1d863f-178d-5c97-bd65-0beb804d2ac0`
- `de39c51f-2749-5cc4-97e4-f187d47b7e0f`
- `e96521b6-6626-5d1d-ab17-986f939c4f9e`
- `61f1f75a-f159-5d07-8627-5cbc4cd12085`
- `d1cfe3e5-dc7e-5baa-a4fe-e01a042e81c5`
- `0726e300-44c4-51cc-abca-bed13666836f`
- `3ece38b5-268b-5b8a-9823-117d1d053be8`
- `011a0baa-dc8d-5b8e-b0e9-cb9f4295edb3`
- `4df88ecd-d98f-5d27-9a58-10523f89bb89`
- `1e617892-a520-5f9d-9b5b-6e2cc90d5955`
- `2ac646f0-7ad2-54bd-969e-9f0be46734dc`
- `037d8ca9-2112-5a2a-a6d8-fc5b94b97da4`
- `7510b96a-1e28-5409-89e9-379edd8b0db1`
- `af143919-a523-5668-8fd1-a757b2fa9dab`
- `7077a1e9-c8c5-5aa6-b33f-5fdf2f8ffb01`
- `dc387555-af78-5649-a814-00dbc63decf2`
- `e216bc71-c4fa-5991-b8b5-7b706c63c732`
- `cb578de5-07c5-5f19-817c-1030bfdbb004`

