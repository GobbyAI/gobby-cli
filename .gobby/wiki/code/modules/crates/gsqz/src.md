---
title: crates/gsqz/src
type: code_module
provenance:
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

# crates/gsqz/src

Parent: [[code/modules/crates/gsqz|crates/gsqz]]

## Overview

The `crates/gsqz/src` module implements the `gsqz` CLI for turning command or stdin output into shorter LLM-oriented text. `main.rs` owns argument parsing, config initialization/loading, stdin mode, and command-output mode, including ANSI stripping before compression and optional daemon integration [crates/gsqz/src/main.rs:25-48] [crates/gsqz/src/main.rs:67-139] [crates/gsqz/src/main.rs:141-184] [crates/gsqz/src/main.rs:186-276]. Configuration is defined in `config.rs`, where `Config`, `Settings`, `Pipeline`, and `Step` describe pipeline matching, fallback behavior, excluded commands, default sizing, daemon URL overrides, and custom single-key YAML step deserialization [crates/gsqz/src/config.rs:26-35] [crates/gsqz/src/config.rs:38-47] [crates/gsqz/src/config.rs:49-58] [crates/gsqz/src/config.rs:60-62].

The central compression flow lives in `compressor.rs`: it compiles configured regex pipelines, applies built-in and configured command exclusions, skips short output, selects a matching pipeline or fallback, executes steps, and records original/compressed sizes plus the strategy name [crates/gsqz/src/compressor.rs:7-12] [crates/gsqz/src/compressor.rs:14-34] [crates/gsqz/src/compressor.rs:36-40]. Compound command handling is delegated to `command_split.rs`, which splits only top-level `&&`, `||`, and `;` while preserving pipes, quoted operators, escapes inside double quotes, and parenthesized subexpressions, so exclusion and pipeline decisions can reason about individual command segments without corrupting shell syntax .

Compression steps are implemented by the `primitives` child module, which provides focused reducers for filtering, grouping, truncation, adjacent deduplication, regex replacement, output matching, and prose compression [crates/gsqz/src/primitives/mod.rs:1-8]. These primitives remove known noise, summarize repeated structures, and preserve useful boundary content through operations such as invalid-regex-tolerant filtering, sequential replacements, section-aware truncation, and adjacent duplicate collapse [crates/gsqz/src/primitives/filter.rs:4-15] [crates/gsqz/src/primitives/replace.rs:7-30] [crates/gsqz/src/primitives/truncate.rs:5-27] [crates/gsqz/src/primitives/dedup.rs:9-45]. `daemon.rs` adds best-effort, feature-gated Gobby integration for fetching compression settings, reporting savings, and resolving daemon URLs from config or shared bootstrap/env sources, while compiling to no-op behavior when the feature is disabled [crates/gsqz/src/daemon.rs:11-23] [crates/gsqz/src/daemon.rs:26-28] [crates/gsqz/src/daemon.rs:32-43] [crates/gsqz/src/daemon.rs:46-53] [crates/gsqz/src/daemon.rs:62-76].

## Call Diagram

```mermaid
sequenceDiagram
    participant m_001e5557_abaf_5197_b5ac_897f6a6ad6bc as test_no_match_returns_none &#91;function&#93;
    participant m_00260bd3_7b94_5050_87e1_8f9d438367cd as test_on_empty_pipeline_overrides_global &#91;function&#93;
    participant m_00f6cfc1_fef1_593a_8493_dc9f7c660663 as test_dedup_mixed_groups &#91;function&#93;
    participant m_0109c774_ada4_5242_9e1c_a990394e462a as test_filter_removes_none &#91;function&#93;
    participant m_035c2b73_fa04_5199_8c00_6aa232714c78 as test_dedup_different &#91;function&#93;
    participant m_08488e18_4735_5d3a_82ee_5bf7d5f46d2e as test_test_failures_captures_fail_lines &#91;function&#93;
    participant m_08ca6a31_4880_55be_9fb6_fb381b93f51b as test_filter_empty_patterns &#91;function&#93;
    participant m_09f3939e_f6f8_5881_841b_e008c8f8a527 as test_multiple_matches_per_line &#91;function&#93;
    participant m_0ca60299_497e_512f_92c6_30cf0e95505d as test_filter_removes_all &#91;function&#93;
    participant m_0fd9af53_3342_5461_8496_8c5e90555988 as replace &#91;function&#93;
    participant m_10e4d22b_0b39_5ef2_a0a7_d255fa00f24e as test_good_compression_has_no_marker &#91;function&#93;
    participant m_10e633e0_a676_5e67_9492_70f800426bca as test_empty_lines &#91;function&#93;
    participant m_1d237b01_a52b_586f_8553_230e2304698f as test_errors_warnings_only_errors &#91;function&#93;
    participant m_1e9421bd_6c46_5041_ad56_06265939d31e as test_filter_invalid_regex_skipped &#91;function&#93;
    participant m_229484c2_5086_5772_b8fa_2bb9eee8dc2b as test_git_status_many_files_truncated &#91;function&#93;
    participant m_25be7ab4_68f7_58ee_b58b_f9777d5d464c as test_compound_falls_back_to_earlier_segment &#91;function&#93;
    participant m_266e5f64_482b_55c8_b7b5_9d67b90ef67a as test_fallback_used_when_no_pipeline_matches &#91;function&#93;
    participant m_27c68279_175d_5913_a390_a0b61a6c6fb4 as test_dedup_single_line &#91;function&#93;
    participant m_32efbce0_fa3f_56fe_bc0f_f835fc242381 as check &#91;function&#93;
    participant m_3870c8ea_daae_5054_97ec_c28cb949a695 as group_git_status &#91;function&#93;
    participant m_4690ffe8_c1e2_5c70_9a9d_d5cb2ff5919b as dedup &#91;function&#93;
    participant m_4d96cd0c_6125_510e_8a0c_be9ca181554f as test_config &#91;function&#93;
    participant m_51e5d958_0fc2_5f5a_99f8_d2dafac5d86a as rule &#91;function&#93;
    participant m_8918cfc8_ed39_5d2d_9338_b2c301df4d96 as group_errors_warnings &#91;function&#93;
    participant m_8faa2138_fa37_53b4_b21b_2dc80b2babf5 as filter_lines &#91;function&#93;
    participant m_def86bb9_e734_5291_a0c0_043c8d384f39 as lines &#91;function&#93;
    participant m_efd37613_da20_5fbf_9c5d_1ab33c9053a6 as group_test_failures &#91;function&#93;
    m_001e5557_abaf_5197_b5ac_897f6a6ad6bc->>m_32efbce0_fa3f_56fe_bc0f_f835fc242381: calls
    m_001e5557_abaf_5197_b5ac_897f6a6ad6bc->>m_def86bb9_e734_5291_a0c0_043c8d384f39: calls
    m_00260bd3_7b94_5050_87e1_8f9d438367cd->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_00f6cfc1_fef1_593a_8493_dc9f7c660663->>m_4690ffe8_c1e2_5c70_9a9d_d5cb2ff5919b: calls
    m_0109c774_ada4_5242_9e1c_a990394e462a->>m_8faa2138_fa37_53b4_b21b_2dc80b2babf5: calls
    m_035c2b73_fa04_5199_8c00_6aa232714c78->>m_4690ffe8_c1e2_5c70_9a9d_d5cb2ff5919b: calls
    m_08488e18_4735_5d3a_82ee_5bf7d5f46d2e->>m_efd37613_da20_5fbf_9c5d_1ab33c9053a6: calls
    m_08ca6a31_4880_55be_9fb6_fb381b93f51b->>m_8faa2138_fa37_53b4_b21b_2dc80b2babf5: calls
    m_09f3939e_f6f8_5881_841b_e008c8f8a527->>m_0fd9af53_3342_5461_8496_8c5e90555988: calls
    m_09f3939e_f6f8_5881_841b_e008c8f8a527->>m_51e5d958_0fc2_5f5a_99f8_d2dafac5d86a: calls
    m_0ca60299_497e_512f_92c6_30cf0e95505d->>m_8faa2138_fa37_53b4_b21b_2dc80b2babf5: calls
    m_10e4d22b_0b39_5ef2_a0a7_d255fa00f24e->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_10e633e0_a676_5e67_9492_70f800426bca->>m_0fd9af53_3342_5461_8496_8c5e90555988: calls
    m_10e633e0_a676_5e67_9492_70f800426bca->>m_51e5d958_0fc2_5f5a_99f8_d2dafac5d86a: calls
    m_1d237b01_a52b_586f_8553_230e2304698f->>m_8918cfc8_ed39_5d2d_9338_b2c301df4d96: calls
    m_1e9421bd_6c46_5041_ad56_06265939d31e->>m_8faa2138_fa37_53b4_b21b_2dc80b2babf5: calls
    m_229484c2_5086_5772_b8fa_2bb9eee8dc2b->>m_3870c8ea_daae_5054_97ec_c28cb949a695: calls
    m_25be7ab4_68f7_58ee_b58b_f9777d5d464c->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_266e5f64_482b_55c8_b7b5_9d67b90ef67a->>m_4d96cd0c_6125_510e_8a0c_be9ca181554f: calls
    m_27c68279_175d_5913_a390_a0b61a6c6fb4->>m_4690ffe8_c1e2_5c70_9a9d_d5cb2ff5919b: calls
```

## Child Modules

- [[code/modules/crates/gsqz/src/primitives|crates/gsqz/src/primitives]] - The `primitives` module is the core text-reduction toolkit for `gsqz`, exported as a collection of focused operations for deduplication, filtering, grouping, output matching, prose compression, replacement, and truncation [crates/gsqz/src/primitives/mod.rs:1-8]. Its line-oriented primitives either remove noise, summarize repeated structure, or preserve the most useful boundary content: `dedup` collapses only adjacent duplicate or number-normalized runs [crates/gsqz/src/primitives/dedup.rs:9-45], `filter_lines` drops lines matching any valid configured regex while ignoring invalid patterns [crates/gsqz/src/primitives/filter.rs:4-15], `replace` applies compiled regex replacement rules sequentially across every line [crates/gsqz/src/primitives/replace.rs:7-30], and `truncate` keeps head and tail lines or delegates to section-aware truncation when a marker is configured [crates/gsqz/src/primitives/truncate.rs:5-27].

The module’s heavier summarization flow lives in `group.rs`, where `group_lines` dispatches by mode to specialized aggregators for git status, git diff, pytest failures, generic test failures, lint rules, extensions, directories, files, and error/warning logs [crates/gsqz/src/primitives/group.rs:8-21]. These helpers parse common CLI-output shapes into labeled counts and representative samples, with truncation when groups grow large [crates/gsqz/src/primitives/group.rs:28-79] [crates/gsqz/src/primitives/group.rs:99-183] [crates/gsqz/src/primitives/group.rs:187-243]. Separately, `match_output::check` treats the entire output as one blob, evaluates configured `MatchOutputRule`s in order, skips invalid regexes, honors optional `unless` blockers, and returns the first matching message [crates/gsqz/src/primitives/match_output.rs:8-33].

`prose.rs` handles document-style compression rather than line filtering: callers choose `Lite`, `Standard`, or `Aggressive` via `Level::from_str`, then `compress_prose` protects YAML frontmatter, code blocks, inline code, URLs, XML tags, and file paths before applying the selected compression strategy and restoring protected spans  [crates/gsqz/src/primitives/prose.rs:50-100]. Across the module, tests exercise empty inputs, invalid regex fallback, passthrough cases, truncation boundaries, preservation behavior, and mode-specific grouping, showing that these primitives are meant to compose safely in configurable output-squeezing pipelines  .

## Files

- [[code/files/crates/gsqz/src/command_split.rs|crates/gsqz/src/command_split.rs]] - Implements `split_compound`, a shell-command splitter that breaks a command string into trimmed segments at top-level `&&`, `||`, and `;` delimiters while preserving quoted text, escaped characters in double quotes, nested parentheses, and pipe chains. If no split points are found, it returns the original command as a single-element vector. The test module exercises the splitter across plain commands, each supported operator, mixed operators, quoted and parenthesized subexpressions, empty input, trailing operators, and whitespace trimming.
[crates/gsqz/src/command_split.rs:5-85]
[crates/gsqz/src/command_split.rs:92-94]
[crates/gsqz/src/command_split.rs:97-102]
[crates/gsqz/src/command_split.rs:105-107]
[crates/gsqz/src/command_split.rs:110-112]
- [[code/files/crates/gsqz/src/compressor.rs|crates/gsqz/src/compressor.rs]] - Implements the `gsqz` text compressor: it decides when command output should be passed through, excluded, or compressed, then applies a regex-selected pipeline or fallback steps to shorten verbose output while tracking the original and compressed sizes. The file also includes helpers for parsing command tokens and shell-style basenames, plus the step executor that performs filtering, grouping, truncation, deduplication, replacement, and prose compression, with tests covering pipeline selection, exclusions, savings calculations, and empty-output fallback behavior.
[crates/gsqz/src/compressor.rs:7-12]
[crates/gsqz/src/compressor.rs:14-34]
[crates/gsqz/src/compressor.rs:15-20]
[crates/gsqz/src/compressor.rs:29-33]
[crates/gsqz/src/compressor.rs:36-40]
- [[code/files/crates/gsqz/src/config.rs|crates/gsqz/src/config.rs]] - Defines the gsqz configuration schema and its serde behavior. The file ties together top-level `Config`, `Settings`, `Pipeline`, and `Step` types, supplies defaults for output sizing and fallback truncation, and implements custom step deserialization from single-key YAML maps into the appropriate operation-specific argument structs.
[crates/gsqz/src/config.rs:26-35]
[crates/gsqz/src/config.rs:38-47]
[crates/gsqz/src/config.rs:49-58]
[crates/gsqz/src/config.rs:50-57]
[crates/gsqz/src/config.rs:60-62]
- [[code/files/crates/gsqz/src/daemon.rs|crates/gsqz/src/daemon.rs]] - This module provides best-effort integration with the Gobby daemon behind the `gobby` feature flag: it fetches compression settings from the daemon’s config endpoint, reports compression savings to an admin endpoint, and resolves the daemon base URL from either a config override with `${GOBBY_PORT}` expansion or a shared fallback resolver. When the feature is disabled, the same APIs degrade to no-ops that return `None` or do nothing, and the tests verify passthrough behavior, environment-variable expansion, and bootstrap-based URL resolution.
[crates/gsqz/src/daemon.rs:11-23]
[crates/gsqz/src/daemon.rs:26-28]
[crates/gsqz/src/daemon.rs:32-43]
[crates/gsqz/src/daemon.rs:46-53]
[crates/gsqz/src/daemon.rs:62-76]
- [[code/files/crates/gsqz/src/main.rs|crates/gsqz/src/main.rs]] - `main.rs` is the CLI entry point for `gsqz`, a tool that runs a command or reads stdin and compresses the resulting text for LLM use. `Cli` defines the top-level flags for config handling, stats, and subcommand dispatch; `parse_input_level` extracts a `--level` setting for stdin compression, defaulting to `Standard` when absent or invalid. `main` loads configuration, auto-initializes a default config file on first run, and routes execution to `run_input_mode` or `run_output_mode`, which either compress stdin directly or run a shell command, strip ANSI escape codes, and compress the cleaned output with optional config and daemon integration.
[crates/gsqz/src/main.rs:25-48]
[crates/gsqz/src/main.rs:50-65]
[crates/gsqz/src/main.rs:67-139]
[crates/gsqz/src/main.rs:141-184]
[crates/gsqz/src/main.rs:186-276]

## Components

- `b05a5755-3822-5184-a05f-511f79a33790`
- `45ba74bd-50f6-57a2-a576-1b3170eb97c3`
- `656178ad-02d7-5b7c-b1f0-8f943bf97c38`
- `d1136450-588e-5d0f-b375-4e045bb4afe1`
- `c53d27cd-c4a3-56bc-9469-f247439d596b`
- `6d44fdde-e21b-5d31-80a6-305aae293a20`
- `fe8a10ef-6fc3-5e42-a152-493c66bbac0e`
- `3ed46273-d30f-5730-a29c-b963fc40f853`
- `1fe14273-a3f1-5af3-98a7-3be5d6777bf5`
- `6789a3b7-180d-5c2e-b576-777993cb1662`
- `d485a5b9-8ddf-557c-8e41-1099affcb842`
- `7dca957d-80d4-543a-9b89-8ceaf07fa5a1`
- `7d2016c1-ff23-50fd-905a-9cd16d8f98c5`
- `72df8651-a364-5c4e-acc5-8c9cd21e9524`
- `9854a28c-9b93-5d2b-9480-de05469fd68f`
- `c33f4294-b3d8-5ddf-b3f1-1afff71934fe`
- `3ac3f184-4da9-5e04-819c-f645ee0cfcad`
- `d236570a-4711-5192-a192-5741d959fa0f`
- `78816fa0-49b2-543c-845a-38a3286dd358`
- `0cb8da5a-eea9-5dd4-921c-19f79ee3dd87`
- `436c60a6-c1e8-5f2e-b449-55a94e08f6e4`
- `880dadac-40a2-5d27-88d4-05b3cf9df5ed`
- `aff9cb40-2d59-5dc4-b5fd-fdc80889ab74`
- `a2c1c64c-462d-5f42-9dc8-5b35344a04b5`
- `8efa0e8a-6b21-511c-a07f-6423de18fddc`
- `788d8c50-5ed2-5301-a6df-1d0d5958e804`
- `b9f4a498-1b46-5866-8057-03d7fd3db7a2`
- `4d96cd0c-6125-510e-8a0c-be9ca181554f`
- `82da9c95-f727-591e-9942-21c643550913`
- `5d783255-271c-5a75-8deb-3ec862819af3`
- `cfbb0621-7d91-5119-b162-b30dc3cd3e56`
- `b8c1c8fa-0070-5933-9d6e-245777fa2bc3`
- `266e5f64-482b-55c8-b7b5-9d67b90ef67a`
- `f53ea6fe-88b5-545b-a75d-043b12fb3f0a`
- `32305f32-7ea1-5474-9381-c4024de06ea4`
- `3d78adca-c8bc-599e-b8b2-3f9e690b7473`
- `c33da4f0-c953-5367-bae6-c676a18cee85`
- `8d608421-dcf6-54b8-a137-75be748af06e`
- `cf4732b9-64d1-5821-a2a4-3705327673a7`
- `5731515f-0018-5229-abf5-d0843ad24b68`
- `ee1f11f1-1d57-5a22-9afb-43f1ae8f1962`
- `59d025ad-0262-587a-9492-2dd770574b58`
- `cb63f364-22c4-592c-9f81-e08b5588698d`
- `7c0e68a6-4150-5ff2-8eb2-77621155aeaf`
- `eef9e1ad-e0fa-5e69-9a86-87d8e9d0bb86`
- `80fb0fdb-a33d-5192-ae12-c2017805790b`
- `d748924c-2414-5716-9e6e-7a635ba939dd`
- `00260bd3-7b94-5050-87e1-8f9d438367cd`
- `b197eca9-c3e2-5f6a-871d-972b88480059`
- `42e7086f-b4c2-5a60-93c6-30c01c7dd3df`
- `52ce9ccd-bfb7-54df-ad64-53574fb8f51d`
- `244f4e2e-f09d-5630-be63-93e3c2b43aca`
- `10e4d22b-0b39-5ef2-a0a7-d255fa00f24e`
- `575ed30f-5095-58fa-812e-162379f98752`
- `72a1f9c8-eee3-5eef-bc85-65940de1b80c`
- `25be7ab4-68f7-58ee-b58b-f9777d5d464c`
- `97e782d0-91b2-5fc2-b9e5-b17b655dd84d`
- `c99f5df8-5e38-5b4f-909b-63b22890e986`
- `f40bc0b3-9141-515d-99a6-24b2a8e5f706`
- `61e2caff-30a4-5d81-a921-9ffb808d6a6d`
- `d49a5c68-e3dc-538a-a368-f5567051b11a`
- `8a691623-f9d1-5a58-bb36-73790de7f69c`
- `1efb3c74-edf7-5ebc-a0b5-88669eac2e96`
- `8bbf9a80-b14b-52bb-b973-f157dadfbc28`
- `21c00c1b-e191-54b0-87c0-043b12afe344`
- `56149edc-ee35-5f1b-8ace-271999a70383`
- `3615d100-7c7a-545a-a5ff-e3338c872984`
- `7499f4da-79c2-5ca6-a3e6-0a46b6bcde5e`
- `a66c7e8b-a774-5f5a-8864-bab0e1b98432`
- `a4fd98f4-1986-5a02-b40c-6fa089eb797b`
- `fd3332ad-f1cf-55a7-8c3f-129c25d667ea`
- `262c8a3c-1bc2-59f1-88cd-0025b942738d`
- `70ff970c-0832-5f0b-a491-8780f58cd92b`
- `4497fb46-154d-5e52-8fb2-13dedea16bf5`
- `03348671-9439-5797-9091-294049237f7a`
- `444f8690-64bf-57e2-ac6b-1fd0c0e92204`
- `fa007958-7166-57a5-88ac-ba9d5880289b`
- `0d26e39a-9792-5ae2-82ac-76b2e3d971d3`
- `9a4e43d3-8796-56f0-945a-3d642416b95c`
- `f82d75c2-99d3-5e8d-85e2-1cb8bc5e0ef9`
- `6b0c3e07-cb4f-536a-98be-edf0805b978c`
- `d03e6ca4-e5b8-5c55-87a2-40828e2078c8`
- `0e60e410-df3d-5449-a753-ebb02a9ee4c9`
- `4585eab8-fb22-5aeb-82e6-cac370b74d93`
- `4265aaa4-a9f1-5b88-8a17-0d925919e3a5`
- `814ddd9d-5afe-597d-87d8-99d41110c04b`
- `fd118047-5041-5ca5-b03b-7431dc1ff002`
- `8e92b8ec-67bd-5ae4-9ce9-3c993f1d5dfc`
- `cf1061f8-a6c2-5d2f-9d5c-a8d6735f413e`
- `ab027411-5918-534c-be77-b27a5e5fe441`
- `42cf8946-29e2-573e-ac38-cb688653f8fc`
- `29e16829-6ac5-59aa-bd0c-e78f4f32e243`
- `14dee87e-39f8-575e-9d2f-b627c24ec474`
- `39f1fd34-f615-5c57-af0e-da171c85c69e`
- `3cf867f3-5f25-56af-a385-bdad6b74e27b`
- `0e7e96ad-ab75-56a4-a08c-93e1be23f511`
- `a4163ae2-500f-5871-b147-b76d074c9d7b`
- `de7c6b37-1d7f-5307-85e9-917b55d96198`
- `082b4df6-63d5-5909-ab55-b3915a57e462`
- `cd11cbdd-dd3c-56ca-b449-180a36c09340`
- `e699ad43-e45a-5b97-8a03-720780448a89`
- `1e44760b-ebd1-5eaf-8746-16bc00d75663`
- `188d95f6-a806-51e2-bbb9-4f7e2d2b8791`
- `f7652769-b395-55f2-b4aa-c7a304d5d88e`
- `10c262d5-0c66-529d-aa6e-8f60fe2a5a59`
- `dc0b4691-58f7-5570-9fe4-ef1c636f142f`
- `a5218f73-542e-5e6d-bd46-c15b18026dcc`
- `3ae8fdd6-6bf5-5248-af3c-fdf72f39ac44`
- `0b5a4f49-60fd-5014-ad66-9344aabf2781`
- `ab89657d-5853-5195-8839-91f7ab714268`
- `7fe7bc16-fde3-5e8c-9a12-226f03161819`
- `0b8e338f-d1bc-5d06-b96c-33edf5fa41b8`
- `4e16af20-55b1-5d02-82e2-d3287ca9a822`
- `fd4f33a8-f75a-5dc4-b46a-0db4058614d4`
- `da6d2d31-de6d-5a53-a862-624222237f42`
- `1f4837e5-07a9-54ab-ae65-808fef0937c5`
- `5257d186-f60a-596a-a9a9-5b71f341d9ed`
- `850e7143-4c06-5d9d-97e5-7115ab51a19b`
- `53136695-8e03-52ae-897c-e81b6fcf860b`
- `93008e10-d1c6-51cb-8a49-f51dbb842f13`
- `c7adc044-6efa-5afc-8862-690c339ee32c`
- `7cfcfe2a-4b46-532c-ac5f-3feba564bde7`
- `9eb0d9c5-2df1-5539-b212-9319fd97f9bb`
- `d93d6c6c-b216-5905-8e4d-4f9a3637730c`
- `88896e39-f136-5069-b7d1-73b094ae2ee7`

