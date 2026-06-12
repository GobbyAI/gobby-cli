---
title: crates/gcode/src/vector
type: code_module
provenance:
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The vector module provides comprehensive vector database integration and semantic search functionality for code symbols. It handles the generation of text embeddings through configurable embedding backends and manages the complete lifecycle of vector collections (primarily utilizing Qdrant), including indexing, syncing, updating, and deleting code symbol vectors. Additionally, it integrates with the symbol database repository to retrieve and index code symbols, enabling high-performance semantic search capabilities across project codebases.
[crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]
[crates/gcode/src/vector/code_symbols/qdrant.rs:18-24]
[crates/gcode/src/vector/code_symbols/repository.rs:6-18]
[crates/gcode/src/vector/code_symbols/search.rs:8-14]

## Child Modules

- [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]] - `crates/gcode/src/vector/code_symbols` contains 7 direct files and 0 child modules.
[crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]
[crates/gcode/src/vector/code_symbols/qdrant.rs:18-24]
[crates/gcode/src/vector/code_symbols/repository.rs:6-18]
[crates/gcode/src/vector/code_symbols/search.rs:8-14]

## Files

- [[code/files/crates/gcode/src/vector/code_symbols.rs|crates/gcode/src/vector/code_symbols.rs]] - `crates/gcode/src/vector/code_symbols.rs` has no indexed API symbols. 
- [[code/files/crates/gcode/src/vector/mod.rs|crates/gcode/src/vector/mod.rs]] - `crates/gcode/src/vector/mod.rs` has no indexed API symbols. 

