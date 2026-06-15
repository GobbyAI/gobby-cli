---
title: "hybrid search result merging"
source_kind: "topic"
tags:
  - gwiki
  - compiled
compile_handoff: "compile-hybrid-search-result-merging-1781521569039"
synthesis_mode: "daemon"
---

# hybrid search result merging

Sources: [[knowledge/sources/how-gobby-cli-merges-hybrid-search-results-2|How gobby-cli merges hybrid search results]]

## Overview

The gcode and gwiki search stacks combine three independent retrieval signals: pg_search BM25, Qdrant semantic vectors, and a FalkorDB graph relevance boost. They merge the ranked lists with Reciprocal Rank Fusion, or RRF, which is rank-based rather than score-based and therefore works well when the per-engine scores are not directly comparable [[knowledge/sources/how-gobby-cli-merges-hybrid-search-results-2|How gobby-cli merges hybrid search results]].

With RRF, each engine contributes `1/(k + rank)` per document, and the combined sums determine the final order. The approach is resilient when an engine is missing, so if graph search is down or embeddings are off, the fusion still produces a sensible ranking from the remaining signals [[knowledge/sources/how-gobby-cli-merges-hybrid-search-results-2|How gobby-cli merges hybrid search results]].

## Source excerpts

- How gobby-cli merges hybrid search results: # wp3-rrf-note.md

## Citations

- None recorded.

## Conflicting claims

- None recorded.

## Missing evidence

- None recorded.

## Backlinks

- [[knowledge/sources/how-gobby-cli-merges-hybrid-search-results-2|How gobby-cli merges hybrid search results]]

