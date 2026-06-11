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

# crates/gcode/src/index/parser/calls/shadowing.rs

Module: [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]

## Purpose

`crates/gcode/src/index/parser/calls/shadowing.rs` exposes 18 indexed API symbols.
[crates/gcode/src/index/parser/calls/shadowing.rs:6-23]
[crates/gcode/src/index/parser/calls/shadowing.rs:25-43]
[crates/gcode/src/index/parser/calls/shadowing.rs:45-84]
[crates/gcode/src/index/parser/calls/shadowing.rs:86-96]
[crates/gcode/src/index/parser/calls/shadowing.rs:98-113]

## API Symbols

- `external_call_is_shadowed` (function) component `external_call_is_shadowed [function]` (`f711cf40-36c2-52cf-a202-bec5a2006631`) lines 6-23 [crates/gcode/src/index/parser/calls/shadowing.rs:6-23]
  - Signature: `pub(super) fn external_call_is_shadowed(`
  - Purpose: Determines whether an external function call is shadowed by checking if a local-scoped identifier matching the call target exists in scope before the call site. [crates/gcode/src/index/parser/calls/shadowing.rs:6-23]
- `local_name_in_scope_before_call` (function) component `local_name_in_scope_before_call [function]` (`b0d1f2d1-32c5-5ede-87e1-ac1a74ee89e9`) lines 25-43 [crates/gcode/src/index/parser/calls/shadowing.rs:25-43]
  - Signature: `fn local_name_in_scope_before_call(`
  - Purpose: Determines whether a name is in scope as a parameter or local variable binding within a caller's function scope prior to a specified call site, excluding block-commented source regions. [crates/gcode/src/index/parser/calls/shadowing.rs:25-43]
- `remove_block_comments` (function) component `remove_block_comments [function]` (`91f1f774-696c-59ea-a440-ebfe9a240361`) lines 45-84 [crates/gcode/src/index/parser/calls/shadowing.rs:45-84]
  - Signature: `fn remove_block_comments(text: &str) -> String {`
  - Purpose: This function removes nested C-style block comments (`/* */`) from a string by tracking comment depth and excising matched comment pairs while preserving all non-comment content. [crates/gcode/src/index/parser/calls/shadowing.rs:45-84]
- `parameter_list_contains_name` (function) component `parameter_list_contains_name [function]` (`27126f44-582f-5846-bbb3-35f882af0451`) lines 86-96 [crates/gcode/src/index/parser/calls/shadowing.rs:86-96]
  - Signature: `fn parameter_list_contains_name(prefix: &str, name: &str) -> bool {`
  - Purpose: This function checks whether a parameter with the specified name exists in the comma-separated parameter list enclosed by parentheses within the prefix string. [crates/gcode/src/index/parser/calls/shadowing.rs:86-96]
- `matching_paren_in_str` (function) component `matching_paren_in_str [function]` (`9a912ba2-7c9e-56b2-8ec3-a010eabb16c0`) lines 98-113 [crates/gcode/src/index/parser/calls/shadowing.rs:98-113]
  - Signature: `fn matching_paren_in_str(text: &str, open: usize) -> Option<usize> {`
  - Purpose: Returns the index of the closing parenthesis that matches the opening parenthesis at position `open`, accounting for nested parentheses by tracking depth. [crates/gcode/src/index/parser/calls/shadowing.rs:98-113]
- `parameter_segment_name` (function) component `parameter_segment_name [function]` (`d2baba53-3b1c-5882-ac45-347bb590c86c`) lines 115-129 [crates/gcode/src/index/parser/calls/shadowing.rs:115-129]
  - Signature: `fn parameter_segment_name(segment: &str) -> Option<&str> {`
  - Purpose: This function extracts the first valid identifier token from a parameter segment string, removing content before `=` or `:` delimiters and returning the trimmed identifier if non-empty. [crates/gcode/src/index/parser/calls/shadowing.rs:115-129]
- `local_binding_line_defines` (function) component `local_binding_line_defines [function]` (`f415fafa-d665-539d-a4b7-afc5cc430827`) lines 131-153 [crates/gcode/src/index/parser/calls/shadowing.rs:131-153]
  - Signature: `fn local_binding_line_defines(line: &str, name: &str) -> bool {`
  - Purpose: Determines whether a code line defines a local binding with the specified name through `:=` or standard assignment operators, or through declaration without assignment, while excluding comments and import statements. [crates/gcode/src/index/parser/calls/shadowing.rs:131-153]
- `split_assignment` (function) component `split_assignment [function]` (`cf48944d-8b8e-5118-af00-bdfbe3bcfd31`) lines 155-218 [crates/gcode/src/index/parser/calls/shadowing.rs:155-218]
  - Signature: `fn split_assignment(line: &str) -> Option<(&str, &str)> {`
  - Purpose: Parses a code line to locate the first simple assignment operator (`=`) that is unquoted and not part of a compound operator, returning the left and right operand slices. [crates/gcode/src/index/parser/calls/shadowing.rs:155-218]
- `binding_left_side_contains` (function) component `binding_left_side_contains [function]` (`c4cf63f5-441f-58dc-bb8d-ce325f3b1102`) lines 220-224 [crates/gcode/src/index/parser/calls/shadowing.rs:220-224]
  - Signature: `fn binding_left_side_contains(left: &str, name: &str) -> bool {`
  - Purpose: Checks whether a comma-delimited string contains a binding name matching the specified name by extracting binding identifiers from each comma-separated part. [crates/gcode/src/index/parser/calls/shadowing.rs:220-224]
- `binding_name_from_left_part` (function) component `binding_name_from_left_part [function]` (`5c036c95-a10b-5266-bb92-093fffd8426f`) lines 226-235 [crates/gcode/src/index/parser/calls/shadowing.rs:226-235]
  - Signature: `fn binding_name_from_left_part(part: &str) -> Option<&str> {`
  - Purpose: Extracts the binding identifier from the left part of a pattern by taking the last whitespace-delimited token (after stripping type annotations), returning `None` if the pattern contains field access or indexing operations. [crates/gcode/src/index/parser/calls/shadowing.rs:226-235]
- `declaration_without_assignment_contains` (function) component `declaration_without_assignment_contains [function]` (`1918300f-65c6-5a07-afb9-d4f94583c372`) lines 237-260 [crates/gcode/src/index/parser/calls/shadowing.rs:237-260]
  - Signature: `fn declaration_without_assignment_contains(line: &str, name: &str) -> bool {`
  - Purpose: Determines whether a specified name is a declared binding on a line prefixed with a variable declaration keyword (let, const, var, val, final, late, or auto). [crates/gcode/src/index/parser/calls/shadowing.rs:237-260]
- `binding_name_from_name_first_part` (function) component `binding_name_from_name_first_part [function]` (`e2847a7f-7c36-5a77-a2e2-4ba041ba4fd9`) lines 262-273 [crates/gcode/src/index/parser/calls/shadowing.rs:262-273]
  - Signature: `fn binding_name_from_name_first_part(part: &str) -> Option<&str> {`
  - Purpose: Extracts and validates a binding identifier by parsing the first whitespace token, rejecting tokens containing structural characters (`.`, `[`, `]`), and returning the portion before the first colon. [crates/gcode/src/index/parser/calls/shadowing.rs:262-273]
- `split_assignment_ignores_bitwise_compound_operators` (function) component `split_assignment_ignores_bitwise_compound_operators [function]` (`ec04f0a0-efd8-52c8-a5c3-599458fe9acf`) lines 283-299 [crates/gcode/src/index/parser/calls/shadowing.rs:283-299]
  - Signature: `fn split_assignment_ignores_bitwise_compound_operators() {`
  - Purpose: This test validates that `split_assignment` returns `None` for all compound assignment operators (bitwise, arithmetic, logical, and other variants) while only splitting on simple assignment operators. [crates/gcode/src/index/parser/calls/shadowing.rs:283-299]
- `name_first_declarations_use_declared_name` (function) component `name_first_declarations_use_declared_name [function]` (`b17f0d6c-1293-5411-b64d-0d647a9e93db`) lines 302-315 [crates/gcode/src/index/parser/calls/shadowing.rs:302-315]
  - Signature: `fn name_first_declarations_use_declared_name() {`
  - Purpose: This test verifies that `declaration_without_assignment_contains` performs case-sensitive matching of variable declarations against their declared identifiers. [crates/gcode/src/index/parser/calls/shadowing.rs:302-315]
- `typed_assignment_bindings_use_name_before_colon` (function) component `typed_assignment_bindings_use_name_before_colon [function]` (`a4ea9e5c-1e62-5126-8f32-c7c46b895e78`) lines 318-327 [crates/gcode/src/index/parser/calls/shadowing.rs:318-327]
  - Signature: `fn typed_assignment_bindings_use_name_before_colon() {`
  - Purpose: This function tests that `binding_left_side_contains()` correctly identifies the variable name (`owner`) but not the type annotation (`User`) on the left side of a typed binding assignment pattern (`let owner: User`). [crates/gcode/src/index/parser/calls/shadowing.rs:318-327]
- `block_comments_do_not_define_shadowing_bindings` (function) component `block_comments_do_not_define_shadowing_bindings [function]` (`06cdea89-74a0-5cb1-b281-6ff2abd3ab95`) lines 330-339 [crates/gcode/src/index/parser/calls/shadowing.rs:330-339]
  - Signature: `fn block_comments_do_not_define_shadowing_bindings() {`
  - Purpose: This function verifies that variable assignments declared within block comments are not actually bound in the local scope, confirming that `remove_block_comments` correctly eliminates them and `local_name_in_scope_before_call` returns false for identifiers only defined in comments. [crates/gcode/src/index/parser/calls/shadowing.rs:330-339]
- `nested_block_comments_do_not_leak_inner_tail` (function) component `nested_block_comments_do_not_leak_inner_tail [function]` (`5cb38be7-7a0b-55f3-a86e-19cfbc4a490b`) lines 342-351 [crates/gcode/src/index/parser/calls/shadowing.rs:342-351]
  - Signature: `fn nested_block_comments_do_not_leak_inner_tail() {`
  - Purpose: This test verifies that nested block comments are correctly parsed as a single unit (preventing the inner comment's closing `*/` from prematurely terminating the outer comment) and that variable declarations within commented code do not leak into scope. [crates/gcode/src/index/parser/calls/shadowing.rs:342-351]
- `unclosed_block_comments_are_treated_as_eof_terminated` (function) component `unclosed_block_comments_are_treated_as_eof_terminated [function]` (`80f0837f-99ac-5448-8675-89e6bf304849`) lines 354-363 [crates/gcode/src/index/parser/calls/shadowing.rs:354-363]
  - Signature: `fn unclosed_block_comments_are_treated_as_eof_terminated() {`
  - Purpose: Tests that unclosed block comments are implicitly terminated at EOF, preventing their removal and excluding contained identifiers from scope analysis. [crates/gcode/src/index/parser/calls/shadowing.rs:354-363]

