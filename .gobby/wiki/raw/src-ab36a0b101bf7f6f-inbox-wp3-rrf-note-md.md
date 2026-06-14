---
source_kind: markdown
source_location: inbox/wp3-rrf-note.md
fetched_at: "unix-ms:1781420000295"
source_hash: ab36a0b101bf7f6fd29ba29ea02c78ab3f3a55a6e1d664071a372554a4fb518d
---

# wp3-rrf-note.md

# How gobby-cli merges hybrid search results

The gcode and gwiki search stacks both combine three independent retrieval
signals — pg_search BM25, Qdrant semantic vectors, and a FalkorDB graph
relevance boost — and merge their ranked lists with Reciprocal Rank Fusion
(RRF). RRF is rank-based, so it is robust to incomparable per-engine scores:
each engine contributes 1/(k + rank) per document, and the sums determine the
final order. Any engine can be absent (graph down, embeddings off) and the
fusion still returns a sensible ranking from the remaining signals.

Source: crates/gcode/src/search/rrf.rs; CLAUDE.md "search/ — Search Pipeline".
