---
title: crates/gcode/src/index/parser/calls/shadowing.rs
type: code_file
provenance:
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls/shadowing.rs:6-23](crates/gcode/src/index/parser/calls/shadowing.rs#L6-L23), [crates/gcode/src/index/parser/calls/shadowing.rs:25-43](crates/gcode/src/index/parser/calls/shadowing.rs#L25-L43), [crates/gcode/src/index/parser/calls/shadowing.rs:45-84](crates/gcode/src/index/parser/calls/shadowing.rs#L45-L84), [crates/gcode/src/index/parser/calls/shadowing.rs:86-96](crates/gcode/src/index/parser/calls/shadowing.rs#L86-L96), [crates/gcode/src/index/parser/calls/shadowing.rs:98-113](crates/gcode/src/index/parser/calls/shadowing.rs#L98-L113), [crates/gcode/src/index/parser/calls/shadowing.rs:115-129](crates/gcode/src/index/parser/calls/shadowing.rs#L115-L129), [crates/gcode/src/index/parser/calls/shadowing.rs:131-153](crates/gcode/src/index/parser/calls/shadowing.rs#L131-L153), [crates/gcode/src/index/parser/calls/shadowing.rs:155-218](crates/gcode/src/index/parser/calls/shadowing.rs#L155-L218), [crates/gcode/src/index/parser/calls/shadowing.rs:220-224](crates/gcode/src/index/parser/calls/shadowing.rs#L220-L224), [crates/gcode/src/index/parser/calls/shadowing.rs:226-235](crates/gcode/src/index/parser/calls/shadowing.rs#L226-L235), [crates/gcode/src/index/parser/calls/shadowing.rs:237-260](crates/gcode/src/index/parser/calls/shadowing.rs#L237-L260), [crates/gcode/src/index/parser/calls/shadowing.rs:262-273](crates/gcode/src/index/parser/calls/shadowing.rs#L262-L273), [crates/gcode/src/index/parser/calls/shadowing.rs:283-299](crates/gcode/src/index/parser/calls/shadowing.rs#L283-L299), [crates/gcode/src/index/parser/calls/shadowing.rs:302-315](crates/gcode/src/index/parser/calls/shadowing.rs#L302-L315), [crates/gcode/src/index/parser/calls/shadowing.rs:318-327](crates/gcode/src/index/parser/calls/shadowing.rs#L318-L327), [crates/gcode/src/index/parser/calls/shadowing.rs:330-339](crates/gcode/src/index/parser/calls/shadowing.rs#L330-L339), [crates/gcode/src/index/parser/calls/shadowing.rs:342-351](crates/gcode/src/index/parser/calls/shadowing.rs#L342-L351), [crates/gcode/src/index/parser/calls/shadowing.rs:354-363](crates/gcode/src/index/parser/calls/shadowing.rs#L354-L363)

</details>

# crates/gcode/src/index/parser/calls/shadowing.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file provides shadowing detection for call resolution. `external_call_is_shadowed` chooses the candidate name to test based on call syntax and then delegates to `local_name_in_scope_before_call`, which inspects the caller’s source span before the call site, strips block comments, and checks for either parameter names or local bindings that would shadow the external call. The rest of the helpers break that parsing into small pieces: they remove nested block comments, extract names from parameter and binding forms, split assignments and declarations, and avoid false positives from comments, typed bindings, and compound operators.
[crates/gcode/src/index/parser/calls/shadowing.rs:6-23]
[crates/gcode/src/index/parser/calls/shadowing.rs:25-43]
[crates/gcode/src/index/parser/calls/shadowing.rs:45-84]
[crates/gcode/src/index/parser/calls/shadowing.rs:86-96]
[crates/gcode/src/index/parser/calls/shadowing.rs:98-113]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `external_call_is_shadowed` | function | `pub(super) fn external_call_is_shadowed(` | `external_call_is_shadowed [function]` | `f711cf40-36c2-52cf-a202-bec5a2006631` | 6-23 [crates/gcode/src/index/parser/calls/shadowing.rs:6-23] | Indexed function `external_call_is_shadowed` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:6-23] |
| `local_name_in_scope_before_call` | function | `fn local_name_in_scope_before_call(` | `local_name_in_scope_before_call [function]` | `b0d1f2d1-32c5-5ede-87e1-ac1a74ee89e9` | 25-43 [crates/gcode/src/index/parser/calls/shadowing.rs:25-43] | Indexed function `local_name_in_scope_before_call` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:25-43] |
| `remove_block_comments` | function | `fn remove_block_comments(text: &str) -> String {` | `remove_block_comments [function]` | `91f1f774-696c-59ea-a440-ebfe9a240361` | 45-84 [crates/gcode/src/index/parser/calls/shadowing.rs:45-84] | Indexed function `remove_block_comments` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:45-84] |
| `parameter_list_contains_name` | function | `fn parameter_list_contains_name(prefix: &str, name: &str) -> bool {` | `parameter_list_contains_name [function]` | `27126f44-582f-5846-bbb3-35f882af0451` | 86-96 [crates/gcode/src/index/parser/calls/shadowing.rs:86-96] | Indexed function `parameter_list_contains_name` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:86-96] |
| `matching_paren_in_str` | function | `fn matching_paren_in_str(text: &str, open: usize) -> Option<usize> {` | `matching_paren_in_str [function]` | `9a912ba2-7c9e-56b2-8ec3-a010eabb16c0` | 98-113 [crates/gcode/src/index/parser/calls/shadowing.rs:98-113] | Indexed function `matching_paren_in_str` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:98-113] |
| `parameter_segment_name` | function | `fn parameter_segment_name(segment: &str) -> Option<&str> {` | `parameter_segment_name [function]` | `d2baba53-3b1c-5882-ac45-347bb590c86c` | 115-129 [crates/gcode/src/index/parser/calls/shadowing.rs:115-129] | Indexed function `parameter_segment_name` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:115-129] |
| `local_binding_line_defines` | function | `fn local_binding_line_defines(line: &str, name: &str) -> bool {` | `local_binding_line_defines [function]` | `f415fafa-d665-539d-a4b7-afc5cc430827` | 131-153 [crates/gcode/src/index/parser/calls/shadowing.rs:131-153] | Indexed function `local_binding_line_defines` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:131-153] |
| `split_assignment` | function | `fn split_assignment(line: &str) -> Option<(&str, &str)> {` | `split_assignment [function]` | `cf48944d-8b8e-5118-af00-bdfbe3bcfd31` | 155-218 [crates/gcode/src/index/parser/calls/shadowing.rs:155-218] | Indexed function `split_assignment` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:155-218] |
| `binding_left_side_contains` | function | `fn binding_left_side_contains(left: &str, name: &str) -> bool {` | `binding_left_side_contains [function]` | `c4cf63f5-441f-58dc-bb8d-ce325f3b1102` | 220-224 [crates/gcode/src/index/parser/calls/shadowing.rs:220-224] | Indexed function `binding_left_side_contains` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:220-224] |
| `binding_name_from_left_part` | function | `fn binding_name_from_left_part(part: &str) -> Option<&str> {` | `binding_name_from_left_part [function]` | `5c036c95-a10b-5266-bb92-093fffd8426f` | 226-235 [crates/gcode/src/index/parser/calls/shadowing.rs:226-235] | Indexed function `binding_name_from_left_part` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:226-235] |
| `declaration_without_assignment_contains` | function | `fn declaration_without_assignment_contains(line: &str, name: &str) -> bool {` | `declaration_without_assignment_contains [function]` | `1918300f-65c6-5a07-afb9-d4f94583c372` | 237-260 [crates/gcode/src/index/parser/calls/shadowing.rs:237-260] | Indexed function `declaration_without_assignment_contains` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:237-260] |
| `binding_name_from_name_first_part` | function | `fn binding_name_from_name_first_part(part: &str) -> Option<&str> {` | `binding_name_from_name_first_part [function]` | `e2847a7f-7c36-5a77-a2e2-4ba041ba4fd9` | 262-273 [crates/gcode/src/index/parser/calls/shadowing.rs:262-273] | Indexed function `binding_name_from_name_first_part` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:262-273] |
| `split_assignment_ignores_bitwise_compound_operators` | function | `fn split_assignment_ignores_bitwise_compound_operators() {` | `split_assignment_ignores_bitwise_compound_operators [function]` | `ec04f0a0-efd8-52c8-a5c3-599458fe9acf` | 283-299 [crates/gcode/src/index/parser/calls/shadowing.rs:283-299] | Indexed function `split_assignment_ignores_bitwise_compound_operators` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:283-299] |
| `name_first_declarations_use_declared_name` | function | `fn name_first_declarations_use_declared_name() {` | `name_first_declarations_use_declared_name [function]` | `b17f0d6c-1293-5411-b64d-0d647a9e93db` | 302-315 [crates/gcode/src/index/parser/calls/shadowing.rs:302-315] | Indexed function `name_first_declarations_use_declared_name` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:302-315] |
| `typed_assignment_bindings_use_name_before_colon` | function | `fn typed_assignment_bindings_use_name_before_colon() {` | `typed_assignment_bindings_use_name_before_colon [function]` | `a4ea9e5c-1e62-5126-8f32-c7c46b895e78` | 318-327 [crates/gcode/src/index/parser/calls/shadowing.rs:318-327] | Indexed function `typed_assignment_bindings_use_name_before_colon` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:318-327] |
| `block_comments_do_not_define_shadowing_bindings` | function | `fn block_comments_do_not_define_shadowing_bindings() {` | `block_comments_do_not_define_shadowing_bindings [function]` | `06cdea89-74a0-5cb1-b281-6ff2abd3ab95` | 330-339 [crates/gcode/src/index/parser/calls/shadowing.rs:330-339] | Indexed function `block_comments_do_not_define_shadowing_bindings` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:330-339] |
| `nested_block_comments_do_not_leak_inner_tail` | function | `fn nested_block_comments_do_not_leak_inner_tail() {` | `nested_block_comments_do_not_leak_inner_tail [function]` | `5cb38be7-7a0b-55f3-a86e-19cfbc4a490b` | 342-351 [crates/gcode/src/index/parser/calls/shadowing.rs:342-351] | Indexed function `nested_block_comments_do_not_leak_inner_tail` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:342-351] |
| `unclosed_block_comments_are_treated_as_eof_terminated` | function | `fn unclosed_block_comments_are_treated_as_eof_terminated() {` | `unclosed_block_comments_are_treated_as_eof_terminated [function]` | `80f0837f-99ac-5448-8675-89e6bf304849` | 354-363 [crates/gcode/src/index/parser/calls/shadowing.rs:354-363] | Indexed function `unclosed_block_comments_are_treated_as_eof_terminated` in `crates/gcode/src/index/parser/calls/shadowing.rs`. [crates/gcode/src/index/parser/calls/shadowing.rs:354-363] |
