---
title: "hybrid search result merging"
source_kind: "topic"
tags:
  - gwiki
  - compiled
compile_handoff: "compile-hybrid-search-result-merging-1781420467017"
synthesis_mode: "daemon"
---

# hybrid search result merging

Sources: [[knowledge/sources/how-gobby-cli-merges-hybrid-search-results|How gobby-cli merges hybrid search results]]

## Overview

Hybrid search result merging in gobby-cli combines three independent retrieval signals: pg_search BM25, Qdrant semantic vectors, and a FalkorDB graph relevance boost. The gcode and gwiki search stacks merge the ranked lists with Reciprocal Rank Fusion, which adds `1 / (k + rank)` for each document and uses the summed scores to produce the final order [[knowledge/sources/how-gobby-cli-merges-hybrid-search-results|How gobby-cli merges hybrid search results]].

Because RRF is rank-based, it is resilient to scores that are not directly comparable across engines. The fusion still produces a sensible ranking even if one signal is unavailable, such as when graph lookup is down or embeddings are disabled [[knowledge/sources/how-gobby-cli-merges-hybrid-search-results|How gobby-cli merges hybrid search results]].

## Source excerpts

- How gobby-cli merges hybrid search results: # wp3-rrf-note.md

## Citations

- None recorded.

## Conflicting claims

- None recorded.

## Missing evidence

- None recorded.

## Backlinks

- [[knowledge/sources/how-gobby-cli-merges-hybrid-search-results|How gobby-cli merges hybrid search results]]

