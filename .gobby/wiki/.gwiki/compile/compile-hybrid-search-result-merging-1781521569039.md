# Compile bundle: hybrid search result merging

## Topic outline

- None recorded.

## Accepted sources

- How gobby-cli merges hybrid search results (/Users/josh/Projects/gobby-cli/.gobby/wiki/raw/src-ab36a0b101bf7f6f-inbox-wp3-rrf-note-md.md)
  - # wp3-rrf-note.md
  - # How gobby-cli merges hybrid search results
  - The gcode and gwiki search stacks both combine three independent retrieval
  - signals — pg_search BM25, Qdrant semantic vectors, and a FalkorDB graph
  - relevance boost — and merge their ranked lists with Reciprocal Rank Fusion
  - (RRF). RRF is rank-based, so it is robust to incomparable per-engine scores:
  - each engine contributes 1/(k + rank) per document, and the sums determine the
  - final order. Any engine can be absent (graph down, embeddings off) and the
  - fusion still returns a sensible ranking from the remaining signals.
  - Source: crates/gcode/src/search/rrf.rs; CLAUDE.md "search/ — Search Pipeline".

## Citations

- None recorded.

## Conflicting claims

- None recorded.

## Missing evidence

- None recorded.

