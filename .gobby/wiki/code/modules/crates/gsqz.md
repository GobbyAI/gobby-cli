---
title: crates/gsqz
type: code_module
provenance:
- file: crates/gsqz/config.yaml
  ranges:
  - 12-15
  - 17-204
  - 206-214
- file: crates/gsqz/src/command_split.rs
  ranges:
  - 5-85
  - 92-94
  - 97-102
  - 105-107
  - 110-112
  - 115-120
  - 123-128
  - 131-136
  - 139-144
  - 147-152
  - 155-157
  - 160-162
  - 165-167
- file: crates/gsqz/src/compressor.rs
  ranges:
  - 7-12
  - 14-34
  - 36-40
  - 42-52
  - 54-60
  - 62-67
  - 69-76
  - 78-233
  - 235-266
  - 272-274
  - 277-282
  - 285-293
  - 296-304
  - 307-315
  - 318-327
  - 330-345
  - 348-358
  - 361-377
  - 380-402
  - 405-410
  - 413-424
  - 427-431
  - 434-455
  - 458-468
  - 471-481
  - 484-493
  - 496-507
  - 510-523
  - 526-548
  - 551-571
  - 574-583
  - 586-618
  - 621-646
  - 649-666
  - 669-678
  - 681-691
  - 694-702
  - 705-715
- file: crates/gsqz/src/config.rs
  ranges:
  - 26-35
  - 38-47
  - 49-58
  - 60-62
  - 64-66
  - 69-76
  - 79-87
  - 91-166
  - 169-172
  - 175-177
  - 180-189
  - 191-193
  - 195-197
  - '200'
  - 203-205
  - 208-211
  - 214-216
  - 219-224
  - 227-230
  - 232-234
  - 237-240
  - 242-248
  - 250-257
  - 259-326
  - 333-338
  - 341-345
  - 348-353
  - 356-359
  - 362-368
  - 371-374
  - 377-381
  - 384-388
  - 391-398
  - 401-408
  - 411-423
  - 426-436
  - 439-443
  - 446-457
  - 460-473
  - 476-480
  - 483-490
  - 493-503
  - 506-513
  - 516-526
- file: crates/gsqz/src/daemon.rs
  ranges:
  - 11-23
  - 26-28
  - 32-43
  - 46-53
  - 62-76
  - 79-83
  - 90-95
  - 98-105
  - 108-126
- file: crates/gsqz/src/main.rs
  ranges:
  - 25-48
  - 50-65
  - 67-139
  - 141-184
  - 186-276
- file: crates/gsqz/src/primitives/dedup.rs
  ranges:
  - 9-45
  - 52-58
  - 61-70
  - 73-77
  - 80-83
  - 86-89
  - 92-97
  - 100-118
  - 121-126
- file: crates/gsqz/src/primitives/filter.rs
  ranges:
  - 4-15
  - 22-32
  - 35-39
  - 42-45
  - 48-52
  - 55-59
  - 62-72
  - 75-80
- file: crates/gsqz/src/primitives/group.rs
  ranges:
  - 8-21
  - 28-79
  - 99-183
  - 187-243
  - 247-296
  - 304-344
  - 348-387
  - 391-428
  - 434-475
  - 482-525
  - 532-543
  - 546-556
  - 559-567
  - 570-574
  - 577-581
  - 584-587
  - 590-595
  - 598-606
  - 609-623
  - 626-634
  - 637-650
  - 653-665
  - 668-681
  - 684-709
  - 712-716
  - 719-734
  - 737-750
  - 753-770
  - 773-781
  - 784-793
  - 796-805
  - 808-812
  - 815-822
  - 825-834
  - 837-840
  - 843-849
  - 852-861
  - 864-868
  - 871-880
  - 883-887
  - 890-901
  - 904-908
  - 911-921
  - 924-929
  - 932-940
- file: crates/gsqz/src/primitives/match_output.rs
  ranges:
  - 8-33
  - 39-45
  - 47-49
  - 52-56
  - 59-63
  - 66-70
  - 73-77
  - 80-87
  - 90-94
  - 97-101
  - 104-107
  - 110-115
- file: crates/gsqz/src/primitives/mod.rs
  ranges:
  - 1-8
- file: crates/gsqz/src/primitives/prose.rs
  ranges:
  - 5-9
  - 11-20
  - 23-34
  - 50-100
  - 102-109
  - 116-124
  - 187-211
  - 218-278
  - 280-303
  - 310-314
  - 317-321
  - 324-328
  - 331-335
  - 338-343
  - 346-350
  - 353-363
  - 366-370
  - 373-378
  - 381-386
  - 389-393
  - 396-399
  - 402-407
  - 410-418
  - 421-425
  - 428-432
  - 435-439
  - 442-446
- file: crates/gsqz/src/primitives/replace.rs
  ranges:
  - 7-30
  - 36-41
  - 44-48
  - 51-55
  - 58-63
  - 66-70
  - 73-77
  - 80-84
  - 87-90
  - 93-97
- file: crates/gsqz/src/primitives/truncate.rs
  ranges:
  - 5-27
  - 29-67
  - 74-78
  - 81-88
  - 91-106
  - 109-112
  - 115-120
  - 123-128
  - 131-136
  - 139-145
  - 148-157
  - 160-165
  - 168-178
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz

Parent: [[code/modules/crates|crates]]

## Overview

crates/gsqz provides the default configuration and implementation surface for `gsqz`, a command-output compression utility that makes shell output easier for LLMs to consume. Its YAML defaults define global compression thresholds, a maximum compressed length, and the empty-output message, then establish that pipeline matching is ordered, first-match-wins, and sequential, with later config layers overriding built-in, global, project, and explicit config files . The Rust CLI layer loads this configuration, parses compression-level defaults, and routes either stdin or stripped-ANSI command output through the compressor, optionally reporting stats and daemon savings [crates/gsqz/src/main.rs:25-48] [crates/gsqz/src/main.rs:67-139] [crates/gsqz/src/main.rs:186-276].

The main flow is command classification followed by pipeline execution. Test commands such as pytest, cargo test, and generic runners first use `match_output` rules to collapse successful output to “All tests passed.” when failure markers are absent, then remove noisy pass/session lines and group remaining failures [crates/gsqz/config.yaml:17-67]. Linter pipelines deduplicate diagnostics, group them by rule, and truncate the result to keep the highest-value head and tail visible [crates/gsqz/config.yaml:69-100]. The broader default config extends the same pattern to build, package, container, download, listing, find, grep, and fallback cases with filters, grouping, replacement, deduplication, and truncation steps [crates/gsqz/config.yaml:17-204].

The module’s files collaborate by keeping policy in YAML and behavior in `src`: `config.yaml` names command patterns and ordered step chains, while the source module deserializes settings, pipelines, fallback steps, exclusions, and step arguments into typed configuration and executes them through the compressor. Supporting helpers handle command tokenization and exclusions before compression, while step implementations perform filtering, grouping, replacement, prose compression, deduplication, match-output short-circuiting, and truncation; the test surface covers those behaviors across command matching, fallback use, empty-output handling, exclusions, and per-step transforms.

## Call Diagram

```mermaid
sequenceDiagram
    participant m_001e5557_abaf_5197_b5ac_897f6a6ad6bc as test_no_match_returns_none &#91;function&#93;
    participant m_00260bd3_7b94_5050_87e1_8f9d438367cd as test_on_empty_pipeline_overrides_global &#91;function&#93;
    participant m_08488e18_4735_5d3a_82ee_5bf7d5f46d2e as test_test_failures_captures_fail_lines &#91;function&#93;
    participant m_10e4d22b_0b39_5ef2_a0a7_d255fa00f24e as test_good_compression_has_no_marker &#91;function&#93;
    participant m_1d237b01_a52b_586f_8553_230e2304698f as test_errors_warnings_only_errors &#91;function&#93;
    participant m_229484c2_5086_5772_b8fa_2bb9eee8dc2b as test_git_status_many_files_truncated &#91;function&#93;
    participant m_25be7ab4_68f7_58ee_b58b_f9777d5d464c as test_compound_falls_back_to_earlier_segment &#91;function&#93;
    participant m_266e5f64_482b_55c8_b7b5_9d67b90ef67a as test_fallback_used_when_no_pipeline_matches &#91;function&#93;
    participant m_28637dfe_e848_5dd1_92f9_9d8d4f738053 as test_first_rule_wins &#91;function&#93;
    participant m_32305f32_7ea1_5474_9381_c4024de06ea4 as test_low_savings_fallback_keeps_passthrough_marker &#91;function&#93;
    participant m_32b44318_1705_5255_851a_70fd9d140cb5 as test_errors_warnings_grouping &#91;function&#93;
    participant m_32efbce0_fa3f_56fe_bc0f_f835fc242381 as check &#91;function&#93;
    participant m_3870c8ea_daae_5054_97ec_c28cb949a695 as group_git_status &#91;function&#93;
    participant m_3d78adca_c8bc_599e_b8b2_3f9e690b7473 as test_git_status_is_excluded &#91;function&#93;
    participant m_3e5399e7_8362_507e_b212_3deb4fd101b3 as test_lint_by_rule_no_rules &#91;function&#93;
    participant m_4213e21c_d950_5fba_9fb1_4b502a646071 as test_git_diff_binary_collapsed &#91;function&#93;
    participant m_42e7086f_b4c2_5a60_93c6_30c01c7dd3df as test_low_savings_pipeline_gets_marker &#91;function&#93;
    participant m_4414b78e_2214_5ab9_a3d7_f34c460e7d82 as test_lint_by_rule_groups &#91;function&#93;
    participant m_46a62353_d5f2_5d00_9101_be5762be5a46 as group_git_diff &#91;function&#93;
    participant m_4d96cd0c_6125_510e_8a0c_be9ca181554f as test_config &#91;function&#93;
    participant m_4defbe90_0372_54ee_930d_e20f4b9bc88c as test_pytest_failures_no_failures_delegates &#91;function&#93;
    participant m_4e69c744_2191_55fe_9fbd_9a69144fd1fd as test_checks_full_blob_not_per_line &#91;function&#93;
    participant m_66cb62e2_31a9_51ab_9093_71614885da97 as group_pytest_failures &#91;function&#93;
    participant m_71101fc0_db55_51a8_91df_d07e93649273 as group_lint_by_rule &#91;function&#93;
    participant m_8918cfc8_ed39_5d2d_9338_b2c301df4d96 as group_errors_warnings &#91;function&#93;
    participant m_def86bb9_e734_5291_a0c0_043c8d384f39 as lines &#91;function&#93;
    participant m_efd37613_da20_5fbf_9c5d_1ab33c9053a6 as group_test_failures &#91;function&#93;
    m_001e5557_abaf_5197_b5ac_897f6a6ad6bc->>m_32efbce0_fa3f_56fe_bc0f_f835fc242381: calls
    m_001e5557_abaf_5197_b5ac_897f6a6ad6bc->>m_def86bb9_e734_5291_a0c0_043c8d384f39: calls
    m_00260bd3_7b94_5050_87e1_8f9d438367cd->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_08488e18_4735_5d3a_82ee_5bf7d5f46d2e->>m_efd37613_da20_5fbf_9c5d_1ab33c9053a6: calls
    m_10e4d22b_0b39_5ef2_a0a7_d255fa00f24e->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_1d237b01_a52b_586f_8553_230e2304698f->>m_8918cfc8_ed39_5d2d_9338_b2c301df4d96: calls
    m_229484c2_5086_5772_b8fa_2bb9eee8dc2b->>m_3870c8ea_daae_5054_97ec_c28cb949a695: calls
    m_25be7ab4_68f7_58ee_b58b_f9777d5d464c->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_266e5f64_482b_55c8_b7b5_9d67b90ef67a->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_28637dfe_e848_5dd1_92f9_9d8d4f738053->>m_32efbce0_fa3f_56fe_bc0f_f835fc242381: calls
    m_28637dfe_e848_5dd1_92f9_9d8d4f738053->>m_def86bb9_e734_5291_a0c0_043c8d384f39: calls
    m_32305f32_7ea1_5474_9381_c4024de06ea4->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_32b44318_1705_5255_851a_70fd9d140cb5->>m_8918cfc8_ed39_5d2d_9338_b2c301df4d96: calls
    m_3d78adca_c8bc_599e_b8b2_3f9e690b7473->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_3e5399e7_8362_507e_b212_3deb4fd101b3->>m_71101fc0_db55_51a8_91df_d07e93649273: calls
    m_4213e21c_d950_5fba_9fb1_4b502a646071->>m_46a62353_d5f2_5d00_9101_be5762be5a46: calls
    m_42e7086f_b4c2_5a60_93c6_30c01c7dd3df->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_4414b78e_2214_5ab9_a3d7_f34c460e7d82->>m_71101fc0_db55_51a8_91df_d07e93649273: calls
    m_4defbe90_0372_54ee_930d_e20f4b9bc88c->>m_66cb62e2_31a9_51ab_9093_71614885da97: calls
    m_4e69c744_2191_55fe_9fbd_9a69144fd1fd->>m_32efbce0_fa3f_56fe_bc0f_f835fc242381: calls
```

## Child Modules

- [[code/modules/crates/gsqz/src|crates/gsqz/src]] - The `crates/gsqz/src` module implements `gsqz`, a command-output compression utility for making shell output more suitable for LLM consumption. Its CLI entry point defines flags and dispatch, parses compression level defaults, initializes and loads configuration, and routes either stdin or a command’s stripped-ANSI output through the compression path with optional stats and daemon reporting [crates/gsqz/src/main.rs:25-48] [crates/gsqz/src/main.rs:67-139] [crates/gsqz/src/main.rs:186-276]. Configuration is YAML-backed: `Config` combines global `Settings`, named pipelines, fallback steps, and excluded commands, while the built-in config and built-in exclusions provide first-run defaults and commands that should bypass compression  .

The central flow lives in `Compressor`: it compiles configured pipelines, tracks fallback steps and exclusion regexes, uses helper logic to identify the real command token after shell environment assignments, and reports savings or passthrough status through `CompressionResult`  . Compound command handling is delegated to `split_compound`, which scans command text while tracking quote state and parenthesis depth so top-level `&&`, `||`, and `;` split into segments while pipelines and quoted or grouped operators remain intact . The compressor then applies matched pipeline steps or fallback behavior, including low-savings and exclusion passthrough handling [crates/gsqz/src/compressor.rs:14-34].

The primitive submodule supplies the reusable transformations used by configured steps: filtering, replacement, deduplication, grouping, full-output matching, prose compression, and truncation are exported together for the compressor to compose [crates/gsqz/src/primitives/mod.rs:1-8] . These primitives generally operate over line vectors, such as regex-based filtering that skips invalid patterns, sequential replacement rules where earlier edits feed later ones, and adjacent-repeat deduplication with repetition markers [crates/gsqz/src/primitives/filter.rs:4-15] [crates/gsqz/src/primitives/replace.rs:7-30] [crates/gsqz/src/primitives/dedup.rs:9-45]. Daemon integration is isolated and feature-gated: when enabled it fetches compression settings, reports savings, and resolves daemon URLs with config and shared defaults; when disabled, the same APIs become no-ops or return `None`, keeping compression independent of daemon availability   [crates/gsqz/src/daemon.rs:62-76].

## Files

- [[code/files/crates/gsqz/config.yaml|crates/gsqz/config.yaml]] - This file defines the built-in default `gsqz` compression pipeline configuration. It sets global output thresholds and empty-output messaging, then maps command patterns to ordered pipelines whose steps filter, group, deduplicate, or truncate output for specific tools like test runners, linters, build, package, container, and download commands. The pipelines are applied in order, with first match winning and each step feeding the next, and later config layers can override these defaults.
[crates/gsqz/config.yaml:12-15]
[crates/gsqz/config.yaml:13]
[crates/gsqz/config.yaml:14]
[crates/gsqz/config.yaml:15]
[crates/gsqz/config.yaml:17-204]

## Components

- `713476f5-da29-5cf3-8f5f-e73fcc243386`
- `33fc0669-2397-5a12-9d25-bce2aec5d95d`
- `5d12914d-9cc6-5b71-b87a-8aa06981586e`
- `95590f17-31e0-5939-9994-86b6c9707dd5`
- `0ec0b6ab-9ec1-5ddb-8b13-7823a17412e5`
- `b36d304f-cdf3-59d3-a2b5-24c5b1c04a0e`
- `b79b771e-8eb0-5e6a-8434-f402b4e55c8e`
- `79708512-0b9e-5073-92d0-281e1fb7ce2c`
- `af4b6a83-b974-5282-8fb9-749135f01e0f`
- `26dd0bcb-b2dc-567f-a0a7-19cf74cc1f74`
- `848bf657-5d0a-56ba-95e6-b0b1f1cfcd13`
- `32f8057e-c668-50a1-8302-4f6ba6d1670b`
- `48c35eab-92a1-5dbd-a43e-8ca0bdb69304`
- `7b100d83-05b0-5ccc-b372-834f2fb3d3c4`
- `823a0b93-5cc0-5456-bdd4-01ac4e2c7246`
- `b384d393-fb8a-5dac-87a9-b2788d8210da`
- `8abac81f-5e5d-5454-87db-13f0b1e49e37`
- `432808e0-08ab-5833-acc8-5a32fc8796a4`
- `35aba420-cac5-5ff4-9404-9bb0292b71ba`
- `c327e359-6ee6-52e6-ba58-a2d03b7f5b46`
- `55ec5c27-b836-57d6-9b18-43c49985a48b`
- `3d167ffe-d1dd-552f-8922-4c46d7aca1c3`
- `4b12dda4-885b-5f94-b62f-e19697cf5913`
- `5ebf64c0-5833-5a5a-92f0-85f8f267f69a`
- `2c7edb9a-c83c-5b6e-9658-2d4d94aa8f81`
- `73b078e1-21b6-5c54-9c3b-e790e31b5463`
- `c269fa14-e158-518e-a97c-0e8bf4cad501`
- `8cf48d4e-6dd7-5ce9-84e4-9cade01ab4b5`
- `15116bed-66e4-53a7-8b26-98625f408ba6`
- `23597bc6-0f4c-5433-857d-2b5194eba698`
- `d5be92dd-72c5-50e1-95b6-f636d06a8516`
- `b1407540-bcaa-5862-8961-e85dd015e951`
- `282e2b79-ae7c-522b-8c17-ddecd0a3801b`
- `5a3a3f7f-8e7d-5cb3-b038-c47bffde0135`
- `138b6249-4a30-5822-9b2c-8648239e9b3f`
- `d8fb3c61-3ec1-5c28-b9a8-56405630a80c`
- `7bc5c3d0-eaf3-582a-b91f-26aa744bde90`
- `39e90a21-0086-57ae-9b0d-a5c7fb55086b`
- `17b074d6-5eba-51fc-82fe-1fb5cf6061d8`
- `a90d71b8-7cd8-5ff4-84ad-b75b841efbe7`
- `f473e36b-0a10-518c-8867-916b8b7b562d`
- `5921e8c8-7f97-5007-bb81-be1ee8f6b0f9`
- `b68c12b8-34fe-5646-9267-09fb5bcc2a3b`
- `42a1970b-7a09-51c7-afe1-f6e866474df1`
- `adf7e213-d7ac-55bf-8541-76fdf1c43b86`
- `f119b7ba-5024-5295-bad4-47e91888fc39`
- `2e34c11b-7336-59d9-8c06-3282b03b31e5`
- `e213d0ac-279d-5c6b-81ad-70e11312d609`
- `32bcc911-f5df-51e4-959d-e2f2d32b438f`
- `d5d145db-e06f-57fc-8d1a-0097657c9e60`
- `9b3b3507-c5d4-558c-9ca3-2036092d0c9c`
- `440f4254-faa7-5b2e-bda8-131e72085b57`
- `13153b38-084f-5bb7-927f-cafaa6da9078`
- `a2f36f1b-381c-551a-a2d0-e01136693988`
- `32f39506-f4e1-5927-a42a-b1b0b16cac55`
- `f3395051-05bb-5bbe-990b-4fdfa9d3fdf7`
- `3f48750d-9b8d-5660-9aec-238ebf879313`
- `225424f2-90fc-5132-8bdb-ec4af947f1c4`
- `ab35ed6e-d8d1-5997-9bd3-ce6e599f8b6d`
- `6485c710-40e1-5334-a475-d88265a14aa5`
- `3b548fdd-1c6b-51f6-9c29-01a01c20302a`
- `712da4f8-6633-5004-be70-0411f2b7523d`
- `8df3dfb4-588d-5c4b-b16b-c91d008a3602`
- `bb1432f5-ecc0-50b5-bbc6-b994be0817c9`
- `e3d356b3-34ee-5ea7-930e-73ae1203d0a7`
- `5f095f7b-760d-5ebf-83b8-252cd8520588`
- `2a33eeff-489b-5216-a32b-73c9b3316f63`
- `7c8877eb-5d85-518b-bff1-907c04fb7df7`
- `93a4d6df-f900-5c6d-bcdd-ced7e60a6d39`
- `6848869b-4df1-546b-927e-5fbe55caf02f`
- `9bf0c218-645f-5419-b2c5-f367ecb2681e`
- `df3b265a-805d-5b4f-b2b1-ca576c981e81`
- `65c21475-f7d6-573b-86fa-7423c91d1492`
- `df0feb1d-a6c7-5a9f-a822-cf55250590a3`
- `c81aaeaf-ce2a-55f3-9076-9dbc8f14f6fd`
- `6c805771-c56e-5a30-aef9-7ec17e72ea2e`
- `f56a512e-763f-5bee-83ef-3de3a30e1cde`
- `aa827c24-9bc5-5d56-8ad3-44fe52126150`
- `b8d3d9b1-55a2-5cad-8ac0-d2c704c8a0f4`
- `e5068cc3-f193-51ad-993c-eec87f0a9d98`
- `fa8d3ce9-8744-5b9d-8414-deba69fabd04`
- `7efabbd0-371d-5b8f-9ce3-9cbbbf72d665`
- `3aee3876-8c6d-5693-b7c7-8db0c96ce154`
- `624dd569-8e04-5fc6-89d1-6c55ae61a049`
- `7ecec7d6-42bd-53f5-a8ad-a1d59f28c96b`
- `00a70225-8a77-5a8f-b512-24822e867ee6`
- `b3fe3b8b-b866-5d06-92b7-62ac1126bc88`
- `713e29c3-f384-535e-ad65-d1bf3b83768d`
- `aa2901b7-940c-5e30-93d5-f47825fe2b99`
- `89a0efa3-1591-5dcb-bf5e-73db8ef5e97c`
- `10383766-8eb8-5e93-8797-2b4eccca999c`
- `e913a12d-0697-59a8-a154-168c6a08cf57`
- `9ed17d4d-3145-518b-a183-9efcdb679726`
- `e5fdb111-a260-5f0f-b0db-5db689366c73`
- `e09d6d66-41bb-5cd4-8e1e-2206d99c5284`
- `9ea45bc9-e233-5e51-9d4c-86c3bb29854c`
- `b01703e9-2093-5d7f-95af-4f6b2aabb369`
- `1e4ade45-ded3-5d09-8f15-9fe6c2e2dbe4`
- `20a96029-261f-51c5-b8bf-01fcf789b783`
- `fca78b0b-5fb7-5f71-9c72-c449339a5eb6`
- `46df94f8-0356-58e2-8736-bb1a3181e6fd`
- `4e7d9cef-3085-58f5-9852-d1ee6cc147d6`
- `988fa3eb-ddd6-5a21-b96c-f8af38a9c598`
- `a2214e06-6d26-59e4-b32c-03b58b048358`
- `a921181d-748b-55e5-8127-40f3e09ad85a`
- `456fde71-5016-53bf-a728-7f69fc706f8b`
- `641ed4be-35f0-5cd2-a730-e7718e8b9d16`
- `50aedbc1-fcff-525f-8489-1a42aa185ae9`
- `2021f00f-d7e4-5adf-a887-47a41bde73a9`
- `4f84ca6a-73a3-5fa7-a336-279368ecafcb`
- `ad641c73-8272-5fc1-9ca7-d35bb7b944d0`
- `1d03481a-b4c4-556d-aa1f-8a0b9122f2dc`
- `34bde704-be04-5d67-bccb-7e5c931f297d`
- `79ff21a2-6128-5ae6-adf7-96f4b4be5343`
- `26fa0ac8-6ae6-51cb-b20b-98ac46c65ab8`
- `77468b93-6563-5e54-9c2b-d835b4014bba`
- `2b4d4021-c135-5f64-8a53-a292b6219685`
- `386f97e8-78b6-5d39-8faa-9e0e6e65994d`
- `a8ba2c23-1ac8-56b0-bcec-0a18a1868050`
- `83f334d1-e2c9-5f5d-b05e-25663c1adc9a`
- `1c4838d2-faf2-52b3-82a0-77a73a497587`
- `95195ef4-0cda-5075-bf41-ed5c0fde1d76`
- `ad315e7d-37ea-5b84-8385-8307bf89f639`
- `3b304cd0-d33c-5a81-b6a2-3d9a75c1e989`
- `0d1e1adf-ab66-55dc-99c5-5e396ce5eb46`
- `cd8848ef-c579-53da-9088-6f37d447eb70`
- `d3fa5527-d7e3-5140-983f-477c3475e3d2`
- `3d71b4fb-b2bc-54b7-8e9a-dd15d7969fc6`
- `4c04e5a6-e14b-5a34-aa92-3f4224f5559f`
- `9da98587-f0da-5232-8be5-4111674e9ab9`
- `966f4306-1a9a-5dee-8f39-d14b9039e569`
- `2afc0f63-4f3c-5191-bfae-8ce9d75e5ed1`
- `8ce93fb3-cadd-52e1-bfbf-09ea1f30e84f`
- `cfdb5e8c-ea20-50ec-9570-0d6207e93155`
- `c405bb07-ca6f-5b29-9d73-45d5698976c8`
- `57ded2e2-454c-55a1-9d0a-b485041d9bb7`
- `0beabbb1-145d-5f19-87cf-df16f00e5734`
- `247542a1-27f6-5977-9955-e6efa43c0ed8`
- `c97de81c-d6a3-57ff-91ec-f38bab5503e2`
- `e5ddd6ec-fd15-5fe0-add2-7e837bbb3c0e`
- `888ee2e6-03bb-5e75-a7df-dee42220d4fc`

