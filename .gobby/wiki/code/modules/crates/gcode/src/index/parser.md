---
title: crates/gcode/src/index/parser
type: code_module
provenance:
- file: crates/gcode/src/index/parser/calls.rs
  ranges:
  - 23-32
  - 35-42
  - 44-55
  - 57-132
- file: crates/gcode/src/index/parser/calls/ast.rs
  ranges:
  - 17-96
  - 109-140
  - 142-154
  - 157-166
  - 169-178
  - 181-196
  - 199-213
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
  ranges:
  - 8-55
  - 57-77
  - 79-168
  - 170-172
  - 174-189
  - 191-216
  - 218-223
  - 226-232
  - 234-244
  - 235-237
  - 239-243
  - 247-252
  - 255-259
  - 261-371
  - 262-362
  - 364-366
  - 368-370
  - 373-375
  - 377-379
  - 381-391
  - 393-417
  - 419-441
  - 443-492
- file: crates/gcode/src/index/parser/calls/resolution.rs
  ranges:
  - 6-10
  - 17-21
  - 23-46
  - 48-61
  - 63-65
  - 67-90
  - 92-105
  - 107-115
  - 117-155
  - 157-162
  - 164-175
  - 177-182
- file: crates/gcode/src/index/parser/calls/shadowing.rs
  ranges:
  - 6-23
  - 25-43
  - 45-84
  - 86-96
  - 98-113
  - 115-129
  - 131-153
  - 155-218
  - 220-224
  - 226-235
  - 237-260
  - 262-273
  - 283-299
  - 302-315
  - 318-327
  - 330-339
  - 342-351
  - 354-363
- file: crates/gcode/src/index/parser/calls/text.rs
  ranges:
  - 4-20
  - 22-30
  - 32-49
  - 51-53
  - 55-57
  - 59-61
  - 63-65
  - 67-151
  - 158-163
  - 166-172
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser

Parent: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

This module exposes the parsing infrastructure for extracting and resolving function call sites within code indices. It unifies AST-based extraction and lightweight textual scanning, featuring language-specific state machines such as comment-aware scanning for Dart. The module handles call resolution by tracking qualified names, member qualifier paths, and same-file symbol lookups, while accurately managing variable shadowing through assignment and declaration analysis. Supporting utilities provide identifier validation, keyword filtering, parameter extraction, and text encoding to ensure robust, cross-language call analysis for downstream indexing and navigation.
[crates/gcode/src/index/parser/calls.rs:23-32]
[crates/gcode/src/index/parser/calls.rs:35-42]
[crates/gcode/src/index/parser/calls.rs:44-55]
[crates/gcode/src/index/parser/calls.rs:57-132]
[crates/gcode/src/index/parser/calls/ast.rs:17-96]
[crates/gcode/src/index/parser/calls/ast.rs:109-140]
[crates/gcode/src/index/parser/calls/ast.rs:142-154]
[crates/gcode/src/index/parser/calls/ast.rs:157-166]
[crates/gcode/src/index/parser/calls/ast.rs:169-178]
[crates/gcode/src/index/parser/calls/ast.rs:181-196]
[crates/gcode/src/index/parser/calls/ast.rs:199-213]
[crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
[crates/gcode/src/index/parser/calls/dart_textual.rs:57-77]
[crates/gcode/src/index/parser/calls/dart_textual.rs:79-168]
[crates/gcode/src/index/parser/calls/dart_textual.rs:170-172]
[crates/gcode/src/index/parser/calls/dart_textual.rs:174-189]
[crates/gcode/src/index/parser/calls/dart_textual.rs:191-216]
[crates/gcode/src/index/parser/calls/dart_textual.rs:218-223]
[crates/gcode/src/index/parser/calls/dart_textual.rs:226-232]
[crates/gcode/src/index/parser/calls/dart_textual.rs:234-244]
[crates/gcode/src/index/parser/calls/dart_textual.rs:235-237]
[crates/gcode/src/index/parser/calls/dart_textual.rs:239-243]
[crates/gcode/src/index/parser/calls/dart_textual.rs:247-252]
[crates/gcode/src/index/parser/calls/dart_textual.rs:255-259]
[crates/gcode/src/index/parser/calls/dart_textual.rs:261-371]
[crates/gcode/src/index/parser/calls/dart_textual.rs:262-362]
[crates/gcode/src/index/parser/calls/dart_textual.rs:364-366]
[crates/gcode/src/index/parser/calls/dart_textual.rs:368-370]
[crates/gcode/src/index/parser/calls/dart_textual.rs:373-375]
[crates/gcode/src/index/parser/calls/dart_textual.rs:377-379]
[crates/gcode/src/index/parser/calls/dart_textual.rs:381-391]
[crates/gcode/src/index/parser/calls/dart_textual.rs:393-417]
[crates/gcode/src/index/parser/calls/dart_textual.rs:419-441]
[crates/gcode/src/index/parser/calls/dart_textual.rs:443-492]
[crates/gcode/src/index/parser/calls/resolution.rs:6-10]
[crates/gcode/src/index/parser/calls/resolution.rs:17-21]
[crates/gcode/src/index/parser/calls/resolution.rs:23-46]
[crates/gcode/src/index/parser/calls/resolution.rs:48-61]
[crates/gcode/src/index/parser/calls/resolution.rs:63-65]
[crates/gcode/src/index/parser/calls/resolution.rs:67-90]
[crates/gcode/src/index/parser/calls/resolution.rs:92-105]
[crates/gcode/src/index/parser/calls/resolution.rs:107-115]
[crates/gcode/src/index/parser/calls/resolution.rs:117-155]
[crates/gcode/src/index/parser/calls/resolution.rs:157-162]
[crates/gcode/src/index/parser/calls/resolution.rs:164-175]
[crates/gcode/src/index/parser/calls/resolution.rs:177-182]
[crates/gcode/src/index/parser/calls/shadowing.rs:6-23]
[crates/gcode/src/index/parser/calls/shadowing.rs:25-43]
[crates/gcode/src/index/parser/calls/shadowing.rs:45-84]
[crates/gcode/src/index/parser/calls/shadowing.rs:86-96]
[crates/gcode/src/index/parser/calls/shadowing.rs:98-113]
[crates/gcode/src/index/parser/calls/shadowing.rs:115-129]
[crates/gcode/src/index/parser/calls/shadowing.rs:131-153]
[crates/gcode/src/index/parser/calls/shadowing.rs:155-218]
[crates/gcode/src/index/parser/calls/shadowing.rs:220-224]
[crates/gcode/src/index/parser/calls/shadowing.rs:226-235]
[crates/gcode/src/index/parser/calls/shadowing.rs:237-260]
[crates/gcode/src/index/parser/calls/shadowing.rs:262-273]
[crates/gcode/src/index/parser/calls/shadowing.rs:283-299]
[crates/gcode/src/index/parser/calls/shadowing.rs:302-315]
[crates/gcode/src/index/parser/calls/shadowing.rs:318-327]
[crates/gcode/src/index/parser/calls/shadowing.rs:330-339]
[crates/gcode/src/index/parser/calls/shadowing.rs:342-351]
[crates/gcode/src/index/parser/calls/shadowing.rs:354-363]
[crates/gcode/src/index/parser/calls/text.rs:4-20]
[crates/gcode/src/index/parser/calls/text.rs:22-30]
[crates/gcode/src/index/parser/calls/text.rs:32-49]
[crates/gcode/src/index/parser/calls/text.rs:51-53]
[crates/gcode/src/index/parser/calls/text.rs:55-57]
[crates/gcode/src/index/parser/calls/text.rs:59-61]
[crates/gcode/src/index/parser/calls/text.rs:63-65]
[crates/gcode/src/index/parser/calls/text.rs:67-151]
[crates/gcode/src/index/parser/calls/text.rs:158-163]
[crates/gcode/src/index/parser/calls/text.rs:166-172]

## Child Modules

- [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]] - This module provides infrastructure for parsing, extracting, and resolving function calls within code indices. It supports both AST-based extraction and lightweight textual scanning, featuring specialized state machines and comment-aware scanning for Dart. Call resolution logic handles qualified names, member qualifier paths, and same-file symbol lookup, while accurately tracking variable shadowing through assignment and declaration parsing. Supporting utilities cover identifier validation, keyword filtering, parameter extraction, and text encoding helpers to ensure robust cross-language call analysis.
[crates/gcode/src/index/parser/calls/ast.rs:17-96]
[crates/gcode/src/index/parser/calls/ast.rs:109-140]
[crates/gcode/src/index/parser/calls/ast.rs:142-154]
[crates/gcode/src/index/parser/calls/ast.rs:157-166]
[crates/gcode/src/index/parser/calls/ast.rs:169-178]
[crates/gcode/src/index/parser/calls/ast.rs:181-196]
[crates/gcode/src/index/parser/calls/ast.rs:199-213]
[crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
[crates/gcode/src/index/parser/calls/dart_textual.rs:57-77]
[crates/gcode/src/index/parser/calls/dart_textual.rs:79-168]
[crates/gcode/src/index/parser/calls/dart_textual.rs:170-172]
[crates/gcode/src/index/parser/calls/dart_textual.rs:174-189]
[crates/gcode/src/index/parser/calls/dart_textual.rs:191-216]
[crates/gcode/src/index/parser/calls/dart_textual.rs:218-223]
[crates/gcode/src/index/parser/calls/dart_textual.rs:226-232]
[crates/gcode/src/index/parser/calls/dart_textual.rs:234-244]
[crates/gcode/src/index/parser/calls/dart_textual.rs:235-237]
[crates/gcode/src/index/parser/calls/dart_textual.rs:239-243]
[crates/gcode/src/index/parser/calls/dart_textual.rs:247-252]
[crates/gcode/src/index/parser/calls/dart_textual.rs:255-259]
[crates/gcode/src/index/parser/calls/dart_textual.rs:261-371]
[crates/gcode/src/index/parser/calls/dart_textual.rs:262-362]
[crates/gcode/src/index/parser/calls/dart_textual.rs:364-366]
[crates/gcode/src/index/parser/calls/dart_textual.rs:368-370]
[crates/gcode/src/index/parser/calls/dart_textual.rs:373-375]
[crates/gcode/src/index/parser/calls/dart_textual.rs:377-379]
[crates/gcode/src/index/parser/calls/dart_textual.rs:381-391]
[crates/gcode/src/index/parser/calls/dart_textual.rs:393-417]
[crates/gcode/src/index/parser/calls/dart_textual.rs:419-441]
[crates/gcode/src/index/parser/calls/dart_textual.rs:443-492]
[crates/gcode/src/index/parser/calls/resolution.rs:6-10]
[crates/gcode/src/index/parser/calls/resolution.rs:17-21]
[crates/gcode/src/index/parser/calls/resolution.rs:23-46]
[crates/gcode/src/index/parser/calls/resolution.rs:48-61]
[crates/gcode/src/index/parser/calls/resolution.rs:63-65]
[crates/gcode/src/index/parser/calls/resolution.rs:67-90]
[crates/gcode/src/index/parser/calls/resolution.rs:92-105]
[crates/gcode/src/index/parser/calls/resolution.rs:107-115]
[crates/gcode/src/index/parser/calls/resolution.rs:117-155]
[crates/gcode/src/index/parser/calls/resolution.rs:157-162]
[crates/gcode/src/index/parser/calls/resolution.rs:164-175]
[crates/gcode/src/index/parser/calls/resolution.rs:177-182]
[crates/gcode/src/index/parser/calls/shadowing.rs:6-23]
[crates/gcode/src/index/parser/calls/shadowing.rs:25-43]
[crates/gcode/src/index/parser/calls/shadowing.rs:45-84]
[crates/gcode/src/index/parser/calls/shadowing.rs:86-96]
[crates/gcode/src/index/parser/calls/shadowing.rs:98-113]
[crates/gcode/src/index/parser/calls/shadowing.rs:115-129]
[crates/gcode/src/index/parser/calls/shadowing.rs:131-153]
[crates/gcode/src/index/parser/calls/shadowing.rs:155-218]
[crates/gcode/src/index/parser/calls/shadowing.rs:220-224]
[crates/gcode/src/index/parser/calls/shadowing.rs:226-235]
[crates/gcode/src/index/parser/calls/shadowing.rs:237-260]
[crates/gcode/src/index/parser/calls/shadowing.rs:262-273]
[crates/gcode/src/index/parser/calls/shadowing.rs:283-299]
[crates/gcode/src/index/parser/calls/shadowing.rs:302-315]
[crates/gcode/src/index/parser/calls/shadowing.rs:318-327]
[crates/gcode/src/index/parser/calls/shadowing.rs:330-339]
[crates/gcode/src/index/parser/calls/shadowing.rs:342-351]
[crates/gcode/src/index/parser/calls/shadowing.rs:354-363]
[crates/gcode/src/index/parser/calls/text.rs:4-20]
[crates/gcode/src/index/parser/calls/text.rs:22-30]
[crates/gcode/src/index/parser/calls/text.rs:32-49]
[crates/gcode/src/index/parser/calls/text.rs:51-53]
[crates/gcode/src/index/parser/calls/text.rs:55-57]
[crates/gcode/src/index/parser/calls/text.rs:59-61]
[crates/gcode/src/index/parser/calls/text.rs:63-65]
[crates/gcode/src/index/parser/calls/text.rs:67-151]
[crates/gcode/src/index/parser/calls/text.rs:158-163]
[crates/gcode/src/index/parser/calls/text.rs:166-172]

## Files

- [[code/files/crates/gcode/src/index/parser/calls.rs|crates/gcode/src/index/parser/calls.rs]] - `crates/gcode/src/index/parser/calls.rs` exposes 4 indexed API symbols.
[crates/gcode/src/index/parser/calls.rs:23-32]
[crates/gcode/src/index/parser/calls.rs:35-42]
[crates/gcode/src/index/parser/calls.rs:44-55]
[crates/gcode/src/index/parser/calls.rs:57-132]
- [[code/files/crates/gcode/src/index/parser/tests.rs|crates/gcode/src/index/parser/tests.rs]] - `crates/gcode/src/index/parser/tests.rs` has no indexed API symbols.

## Components

- `3948f226-4674-5fc9-ab77-faa8cbcded2e`
- `52986442-3c6c-5b74-8b49-4b78638db497`
- `e903b8d9-6b22-5ad3-a5aa-330b94923a9e`
- `0d374fc6-9cf4-539f-9c71-7ad4d398aa09`
- `01939a5b-e090-5540-8d47-89bb67ced83d`
- `b3483c06-ebea-51c2-af6f-d117e03e0e14`
- `e07e10e4-1d48-574d-8dc2-afdc044556eb`
- `4285af00-ea06-5e6e-9bb4-a124b63b67fa`
- `70058089-d832-5fb3-821e-00c47d79f8d2`
- `4369cc1b-3d2f-5e06-b490-edb9cdd35100`
- `a85b31c9-4048-5e10-85e0-98f46229b40d`
- `e61b2a21-72d5-5d34-8e75-b367e3ad76ba`
- `2738a422-f288-534e-a366-5e9e46974efe`
- `3159fb65-0a43-5df8-b392-1bc39ff422a6`
- `044945e8-53b2-5a84-abe4-a18304877a11`
- `75250a72-74e8-5862-ad9b-51b8a6da1a65`
- `647ac655-f5a8-5f0d-a60f-33c8ea2c9ce2`
- `18b2b0c1-9d75-540c-945d-d4927534fe86`
- `a0546f1a-f17f-57c6-b2ff-422ba208d0c1`
- `6baf9d3f-da3f-5253-b8b2-51b1f14b40bf`
- `1f8978c2-802f-5f74-bade-eb9b8c282f14`
- `c1a66187-3bcc-5091-b205-1883d9e3935b`
- `c94c5b27-366d-50be-b9e8-f8f2e7af1dc8`
- `826e8df3-be70-5ac4-ada1-55a31359f6ff`
- `b7006ee4-fd09-55a8-b408-ca7ca1e92081`
- `f3fb79da-43d4-545c-b031-131b84dca8a2`
- `ddf1d64c-873e-530c-8e50-7993d3724101`
- `8a1a9ca2-9049-55c1-b8f6-bc61d1c51cab`
- `c3e16433-934e-5dfc-a56a-f42893a6a5b1`
- `dcc92820-a198-56bc-bbad-0abad5c21c36`
- `3efdcaae-3db8-5670-b839-7d379eb7a396`
- `c99e04de-c6b8-5a5a-90af-0d60d1bc23f3`
- `0467e7e4-5fdd-570e-9d33-c53d9783c68f`
- `9ed7304a-528a-586b-adb5-856d6b59e102`
- `05532d20-0797-5f98-b19e-15a7f431a888`
- `9c30b856-c855-5c26-aa73-bdd164c437a1`
- `53222c78-5e39-5e45-a035-c9b48740a4d6`
- `6eca919c-11ec-5425-a720-90a47399bf04`
- `28c9ff78-6b41-50f6-a96d-e43acc99fb8f`
- `5124f9d4-2259-5d16-a479-3131f6cb9b16`
- `719a45ba-540c-509e-974f-23109a634cfb`
- `9d0c7948-4a09-5532-a9a1-d9c3c4bcb0dd`
- `720986cd-dadd-56a2-ad70-5fdc2a966923`
- `88a242ea-d394-5089-b65f-fcb57556954f`
- `1ad174c0-0cae-569e-a964-41e540ed90c0`
- `de130dfa-ced4-5096-aa07-d865ac254172`
- `f711cf40-36c2-52cf-a202-bec5a2006631`
- `b0d1f2d1-32c5-5ede-87e1-ac1a74ee89e9`
- `91f1f774-696c-59ea-a440-ebfe9a240361`
- `27126f44-582f-5846-bbb3-35f882af0451`
- `9a912ba2-7c9e-56b2-8ec3-a010eabb16c0`
- `d2baba53-3b1c-5882-ac45-347bb590c86c`
- `f415fafa-d665-539d-a4b7-afc5cc430827`
- `cf48944d-8b8e-5118-af00-bdfbe3bcfd31`
- `c4cf63f5-441f-58dc-bb8d-ce325f3b1102`
- `5c036c95-a10b-5266-bb92-093fffd8426f`
- `1918300f-65c6-5a07-afb9-d4f94583c372`
- `e2847a7f-7c36-5a77-a2e2-4ba041ba4fd9`
- `ec04f0a0-efd8-52c8-a5c3-599458fe9acf`
- `b17f0d6c-1293-5411-b64d-0d647a9e93db`
- `a4ea9e5c-1e62-5126-8f32-c7c46b895e78`
- `06cdea89-74a0-5cb1-b281-6ff2abd3ab95`
- `5cb38be7-7a0b-55f3-a86e-19cfbc4a490b`
- `80f0837f-99ac-5448-8675-89e6bf304849`
- `fdf5bec9-0f92-580b-ad2e-d55c1b4ab60c`
- `3b863457-e36d-5dad-a9b0-be2a70dadf05`
- `e8df33ef-7361-5e81-9601-63ebdf33a38f`
- `c03b08bd-256c-5124-9ad7-47206d4ca21c`
- `761af537-d29e-5635-af22-70470219838a`
- `d84b1f89-9474-5ae0-b6eb-11f06485d78b`
- `73d66dcf-5b03-5775-be09-6972894fa9a9`
- `7c1d719b-94ea-51f9-a0d0-a3e8634e8930`
- `c93f116e-886b-57d7-9591-c47dab4c5380`
- `652e44d5-64b2-5fd4-bd27-4d0381e2b588`

