---
title: CLI Interface & Routing
type: code_concept
provenance:
- file: crates/gcode/contract/gcode.contract.json
  ranges:
  - 2-1729
- file: crates/gcode/src/cli.rs
  ranges:
  - 23-46
  - 49-54
  - 57-64
  - 68-73
  - 76-82
  - 86-408
  - 411-475
  - 478-491
  - 494-497
  - 499-505
  - 507-509
  - 511-513
  - 515-526
  - 528-536
- file: crates/gcode/src/cli/tests.rs
  ranges:
  - 12-30
  - 32-36
  - 38-55
- file: crates/gcode/src/dispatch.rs
  ranges:
  - '8'
  - 11-13
  - 15-19
  - '21'
  - 24-28
  - 30-37
  - 39-47
  - 49-61
  - 63-65
  - 67-72
  - 74-78
  - 80-122
  - 124-209
  - 211-237
  - 239-586
- file: crates/gcode/src/dispatch/tests.rs
  ranges:
  - 5-9
  - 12-14
  - 17-22
  - 25-27
  - 30-70
  - 73-87
  - 90-115
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/contract/gcode.contract.json:2-1729](crates/gcode/contract/gcode.contract.json#L2-L1729)
- [crates/gcode/src/cli.rs:23-46](crates/gcode/src/cli.rs#L23-L46), [crates/gcode/src/cli.rs:49-54](crates/gcode/src/cli.rs#L49-L54), [crates/gcode/src/cli.rs:57-64](crates/gcode/src/cli.rs#L57-L64), [crates/gcode/src/cli.rs:68-73](crates/gcode/src/cli.rs#L68-L73), [crates/gcode/src/cli.rs:76-82](crates/gcode/src/cli.rs#L76-L82), [crates/gcode/src/cli.rs:86-408](crates/gcode/src/cli.rs#L86-L408), [crates/gcode/src/cli.rs:411-475](crates/gcode/src/cli.rs#L411-L475), [crates/gcode/src/cli.rs:478-491](crates/gcode/src/cli.rs#L478-L491), [crates/gcode/src/cli.rs:494-497](crates/gcode/src/cli.rs#L494-L497), [crates/gcode/src/cli.rs:499-505](crates/gcode/src/cli.rs#L499-L505), [crates/gcode/src/cli.rs:507-509](crates/gcode/src/cli.rs#L507-L509), [crates/gcode/src/cli.rs:511-513](crates/gcode/src/cli.rs#L511-L513), [crates/gcode/src/cli.rs:515-526](crates/gcode/src/cli.rs#L515-L526), [crates/gcode/src/cli.rs:528-536](crates/gcode/src/cli.rs#L528-L536)
- [crates/gcode/src/cli/tests.rs:12-30](crates/gcode/src/cli/tests.rs#L12-L30), [crates/gcode/src/cli/tests.rs:32-36](crates/gcode/src/cli/tests.rs#L32-L36), [crates/gcode/src/cli/tests.rs:38-55](crates/gcode/src/cli/tests.rs#L38-L55)
- [crates/gcode/src/dispatch.rs:8](crates/gcode/src/dispatch.rs#L8), [crates/gcode/src/dispatch.rs:11-13](crates/gcode/src/dispatch.rs#L11-L13), [crates/gcode/src/dispatch.rs:15-19](crates/gcode/src/dispatch.rs#L15-L19), [crates/gcode/src/dispatch.rs:21](crates/gcode/src/dispatch.rs#L21), [crates/gcode/src/dispatch.rs:24-28](crates/gcode/src/dispatch.rs#L24-L28), [crates/gcode/src/dispatch.rs:30-37](crates/gcode/src/dispatch.rs#L30-L37), [crates/gcode/src/dispatch.rs:39-47](crates/gcode/src/dispatch.rs#L39-L47), [crates/gcode/src/dispatch.rs:49-61](crates/gcode/src/dispatch.rs#L49-L61), [crates/gcode/src/dispatch.rs:63-65](crates/gcode/src/dispatch.rs#L63-L65), [crates/gcode/src/dispatch.rs:67-72](crates/gcode/src/dispatch.rs#L67-L72), [crates/gcode/src/dispatch.rs:74-78](crates/gcode/src/dispatch.rs#L74-L78), [crates/gcode/src/dispatch.rs:80-122](crates/gcode/src/dispatch.rs#L80-L122), [crates/gcode/src/dispatch.rs:124-209](crates/gcode/src/dispatch.rs#L124-L209), [crates/gcode/src/dispatch.rs:211-237](crates/gcode/src/dispatch.rs#L211-L237), [crates/gcode/src/dispatch.rs:239-586](crates/gcode/src/dispatch.rs#L239-L586)
- [crates/gcode/src/dispatch/tests.rs:5-9](crates/gcode/src/dispatch/tests.rs#L5-L9), [crates/gcode/src/dispatch/tests.rs:12-14](crates/gcode/src/dispatch/tests.rs#L12-L14), [crates/gcode/src/dispatch/tests.rs:17-22](crates/gcode/src/dispatch/tests.rs#L17-L22), [crates/gcode/src/dispatch/tests.rs:25-27](crates/gcode/src/dispatch/tests.rs#L25-L27), [crates/gcode/src/dispatch/tests.rs:30-70](crates/gcode/src/dispatch/tests.rs#L30-L70), [crates/gcode/src/dispatch/tests.rs:73-87](crates/gcode/src/dispatch/tests.rs#L73-L87), [crates/gcode/src/dispatch/tests.rs:90-115](crates/gcode/src/dispatch/tests.rs#L90-L115)

</details>

# CLI Interface & Routing

## Overview

Defines the command-line flags, options parsing, routing mechanisms, and CLI contract declarations for the gcode utility.

## Reference Modules

- [[code/modules/crates/gcode/contract|crates/gcode/contract]]
- [[code/modules/crates/gcode/src/cli|crates/gcode/src/cli]]
- [[code/modules/crates/gcode/src/dispatch|crates/gcode/src/dispatch]]

## Source Files

- [[code/files/crates/gcode/contract/gcode.contract.json|crates/gcode/contract/gcode.contract.json]]
- [[code/files/crates/gcode/src/cli.rs|crates/gcode/src/cli.rs]]
- [[code/files/crates/gcode/src/cli/tests.rs|crates/gcode/src/cli/tests.rs]]
- [[code/files/crates/gcode/src/dispatch.rs|crates/gcode/src/dispatch.rs]]
- [[code/files/crates/gcode/src/dispatch/tests.rs|crates/gcode/src/dispatch/tests.rs]]
