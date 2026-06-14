---
title: crates/gcode/src/cli
type: code_module
provenance:
- file: crates/gcode/src/cli/tests.rs
  ranges:
  - 5-213
  - 216-234
  - 237-252
  - 255-270
  - 273-288
  - 291-298
  - 301-312
  - 315-348
  - 351-359
  - 362-372
  - 375-394
  - 397-415
  - 418-440
  - 443-461
  - 464-478
  - 481-488
  - 491-503
  - 506-511
  - 514-528
  - 531-559
  - 562-614
  - 617-636
  - 639-646
  - 649-658
  - 661-693
  - 696-726
  - 729-784
  - 787-796
  - 799-808
  - 811-821
  - 824-835
  - 838-850
  - 853-876
  - 879-887
  - 890-899
  - 902-913
  - 916-924
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `crates/gcode/src/cli` module is responsible for defining and preserving the command-line surface of `gcode`, with its behavior documented here through parser tests. Its coverage centers on mapping user invocations into structured `Cli` and `Command` variants, including graph and vector projection lifecycle commands such as `sync-file`, `clear`, `rebuild`, `report`, and `overview`, while also checking global format handling like `--format text` on projection commands (crates/gcode/src/cli/tests.rs:5-100). The tests assert both command shape and parsed field values, so this module acts as the contract between raw CLI arguments and the rest of the application’s typed command execution layer.

The key flows are argument parsing, validation, and default resolution. Search commands are tested across symbol, text, and content variants with filters, positional paths, graph selection, language constraints, and rejected legacy or unsupported flags; grep parsing is similarly exercised for pattern options, fixed JSON output, max counts, empty-pattern rejection, and unsupported flag failures (crates/gcode/src/cli/tests.rs:5-213, crates/gcode/src/cli/tests.rs:216-234, crates/gcode/src/cli/tests.rs:237-252). The module also keeps important commands at the top level, including callers, usages, imports, and blast-radius, and validates configuration/setup-oriented flows such as index, codewiki, and setup parsing.

Because there are no child modules, collaboration is mostly between the CLI definitions in the parent module and this test suite’s exhaustive checks. The tests use Clap’s `Cli::try_parse_from()` and command factory support to verify success cases, parser errors, help text content, and output-format defaults, including the special case that grep defaults to text while other commands retain JSON unless explicitly overridden (crates/gcode/src/cli/tests.rs:255-270, crates/gcode/src/cli/tests.rs:273-288).
[crates/gcode/src/cli/tests.rs:5-213]
[crates/gcode/src/cli/tests.rs:216-234]
[crates/gcode/src/cli/tests.rs:237-252]
[crates/gcode/src/cli/tests.rs:255-270]
[crates/gcode/src/cli/tests.rs:273-288]

## Files

- [[code/files/crates/gcode/src/cli/tests.rs|crates/gcode/src/cli/tests.rs]] - This file contains comprehensive unit tests for the gcode CLI parser, validating argument parsing across all command variants. The tests simulate CLI invocations using `Cli::try_parse_from()` with various argument combinations, then assert the parsed command structure, field values, and default values match expectations. Coverage spans multiple command families: projection lifecycle operations (graph/vector sync-file, clear, rebuild), search variants (search-symbol, search-text, search-content) with filter flags, grep with pattern matching options, top-level commands (callers, usages, imports, blast-radius), and configuration commands (index, codewiki, setup). The suite validates both successful parsing and error handling for unsupported flags, invalid argument positions, and constraint violations like empty patterns or oversized numeric values. Additional tests verify help text content accuracy and the effective_format function's logic for defaulting output formats based on command type.
[crates/gcode/src/cli/tests.rs:5-213]
[crates/gcode/src/cli/tests.rs:216-234]
[crates/gcode/src/cli/tests.rs:237-252]
[crates/gcode/src/cli/tests.rs:255-270]
[crates/gcode/src/cli/tests.rs:273-288]

## Components

- `9c741412-7933-5ef9-828a-c7cbed61eb6c`
- `d7c125ef-0fcc-56ab-bfce-52398aec3be3`
- `fc8a3ded-0516-5e00-9fe7-a613b72cc2bf`
- `1d0d67ea-99c9-5868-b106-04cdbb46b7fc`
- `f08b3ddb-160c-5181-abe3-ceb46260ceec`
- `b37dcc5d-3d2e-5eb1-826e-71b807a59f48`
- `3692d049-bcce-5629-9ab8-51d4ce433c50`
- `96d50dd6-56ec-5bca-9797-25ffb2a24856`
- `c51f13d4-9b81-550e-8457-3adf2d176229`
- `b0718bf1-d30c-5c3b-9da3-050d32f7d716`
- `00dbdfe0-4b8f-5f24-9a29-ce8966da102d`
- `57311634-100e-5bb4-81f5-39e6837bc818`
- `d11ba557-7d75-5d1f-872b-d5a2d849e310`
- `1bf6d286-1d88-537a-ab8e-27329f738e83`
- `b0438a53-61e7-589f-b46b-7fd24a965d2d`
- `b109dc9a-f0c3-5875-b206-237f2beacba6`
- `4d4500ab-b067-5900-96d6-b99eeb6dce2b`
- `3518e280-04a4-5b2c-999f-805a9c959939`
- `cc695152-b17b-5865-806e-8e13cf1ffd68`
- `17dc8c95-d813-5784-9d05-be8c905c7fcd`
- `fb6c5404-cd34-5039-a4bd-cdd8ab0c0244`
- `30e3a1a0-c154-5df2-bf00-e5affbcfd97a`
- `3d48f22c-5145-505c-9650-6d373361aaed`
- `b94a2778-9e2b-540d-8ab8-03b369075a15`
- `ccbd1042-b3a8-5eba-95b6-e01ce9f02e3f`
- `3f87276e-1133-5b86-af2b-2390ccda6c36`
- `eed18059-ffa2-5a90-801a-fae98c5c167a`
- `29c79d7c-9cd9-5220-b2d2-fb1b8bab7339`
- `5eab7ad4-9146-51d8-aa70-0729e1e2e4d0`
- `d221cdf1-781a-5038-8ebf-d04746c6f202`
- `99a75153-06d2-5af8-b960-20171a4bc9f8`
- `41bdaeb5-7f96-5b24-8cf0-bae525456b4f`
- `66252b91-b4fe-5a32-9402-5fa057f238ac`
- `0d69e5a4-0225-503b-a866-b975cb7f74ec`
- `c92485b7-171b-5bcc-b1fc-aeedec156d93`
- `0474b35f-05d2-59f9-9226-2fe181b44463`
- `cd9492ef-bfe0-5848-82f1-913b7776cfbb`

