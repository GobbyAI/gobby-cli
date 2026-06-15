---
title: crates/gsqz/src/primitives/dedup.rs
type: code_file
provenance:
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/primitives/dedup.rs

Module: [[code/modules/crates/gsqz/src/primitives|crates/gsqz/src/primitives]]

## Purpose

Provides a line deduplication primitive that collapses only consecutive duplicates, including near-identical lines that differ only by numbers. It normalizes digits with a shared regex, tracks each run’s first line and count, and when a run ends emits either the original line or the line plus a `"[repeated N times]"` annotation. The tests cover identical, numeric-variant, distinct, empty, single-line, mixed-group, and non-consecutive cases to confirm it only merges adjacent runs.
[crates/gsqz/src/primitives/dedup.rs:9-45]
[crates/gsqz/src/primitives/dedup.rs:52-58]
[crates/gsqz/src/primitives/dedup.rs:61-70]
[crates/gsqz/src/primitives/dedup.rs:73-77]
[crates/gsqz/src/primitives/dedup.rs:80-83]

## API Symbols

- `dedup` (function) component `dedup [function]` (`4690ffe8-c1e2-5c70-9a9d-d5cb2ff5919b`) lines 9-45 [crates/gsqz/src/primitives/dedup.rs:9-45]
  - Signature: `pub fn dedup(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Deduplicates consecutive lines by comparing number-normalized versions and replaces duplicate runs with the first instance plus a repetition count annotation. [crates/gsqz/src/primitives/dedup.rs:9-45]
- `test_dedup_identical` (function) component `test_dedup_identical [function]` (`6a862d29-6201-5383-9436-57ac995e1b8e`) lines 52-58 [crates/gsqz/src/primitives/dedup.rs:52-58]
  - Signature: `fn test_dedup_identical() {`
  - Purpose: This test verifies that `dedup()` collapses consecutive identical lines into the original line plus a summary line indicating the repetition count. [crates/gsqz/src/primitives/dedup.rs:52-58]
- `test_dedup_near_identical` (function) component `test_dedup_near_identical [function]` (`e83950d1-ed41-5d52-8fe0-872e65857061`) lines 61-70 [crates/gsqz/src/primitives/dedup.rs:61-70]
  - Signature: `fn test_dedup_near_identical() {`
  - Purpose: Tests that the `dedup` function consolidates three near-identical lines (differing only in position values) into two entries: the first line and a summary message indicating three repetitions. [crates/gsqz/src/primitives/dedup.rs:61-70]
- `test_dedup_different` (function) component `test_dedup_different [function]` (`035c2b73-fa04-5199-8c00-6aa232714c78`) lines 73-77 [crates/gsqz/src/primitives/dedup.rs:73-77]
  - Signature: `fn test_dedup_different() {`
  - Purpose: This test verifies that the `dedup` function returns the input vector unchanged when all lines are distinct. [crates/gsqz/src/primitives/dedup.rs:73-77]
- `test_dedup_empty` (function) component `test_dedup_empty [function]` (`525eed98-3a8a-5393-aa0f-c88e76d459d8`) lines 80-83 [crates/gsqz/src/primitives/dedup.rs:80-83]
  - Signature: `fn test_dedup_empty() {`
  - Purpose: Verifies that the `dedup` function returns an empty vector when applied to an empty input vector. [crates/gsqz/src/primitives/dedup.rs:80-83]
- `test_dedup_single_line` (function) component `test_dedup_single_line [function]` (`27c68279-175d-5913-a390-a0b61a6c6fb4`) lines 86-89 [crates/gsqz/src/primitives/dedup.rs:86-89]
  - Signature: `fn test_dedup_single_line() {`
  - Purpose: Tests that the `dedup` function preserves a single-element vector containing the string "only one\n" without modification. [crates/gsqz/src/primitives/dedup.rs:86-89]
- `test_dedup_two_identical` (function) component `test_dedup_two_identical [function]` (`dddc23f5-064d-50de-b318-d9902b3d0d27`) lines 92-97 [crates/gsqz/src/primitives/dedup.rs:92-97]
  - Signature: `fn test_dedup_two_identical() {`
  - Purpose: This test verifies that `dedup()` preserves duplicate consecutive strings while annotating them with a repetition count marker. [crates/gsqz/src/primitives/dedup.rs:92-97]
- `test_dedup_mixed_groups` (function) component `test_dedup_mixed_groups [function]` (`00f6cfc1-fef1-593a-8493-dc9f7c660663`) lines 100-118 [crates/gsqz/src/primitives/dedup.rs:100-118]
  - Signature: `fn test_dedup_mixed_groups() {`
  - Purpose: This test validates that the `dedup` function collapses consecutive identical lines into a representative line paired with a repetition count message, correctly handling multiple interleaved groups of duplicates. [crates/gsqz/src/primitives/dedup.rs:100-118]
- `test_dedup_non_consecutive_identical_not_collapsed` (function) component `test_dedup_non_consecutive_identical_not_collapsed [function]` (`ab9b57c6-1308-587a-94a6-b897e4ead449`) lines 121-126 [crates/gsqz/src/primitives/dedup.rs:121-126]
  - Signature: `fn test_dedup_non_consecutive_identical_not_collapsed() {`
  - Purpose: Verifies that the `dedup` function preserves non-consecutive duplicate lines instead of collapsing them across the entire sequence. [crates/gsqz/src/primitives/dedup.rs:121-126]

