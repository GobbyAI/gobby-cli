---
title: docs/evidence
type: code_module
provenance:
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json
  ranges:
  - 3-47
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json
  ranges:
  - 3-47
- file: docs/evidence/wiki-parity-2026-06/wp3-search-sources.json
  ranges:
  - 3-227
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs/evidence

Parent: [[code/modules/docs|docs]]

## Overview

docs/evidence is an evidence container rather than a source module: it has no direct files of its own, and its documented behavior currently comes through child evidence sets. The visible child, docs/evidence/wiki-parity-2026-06, stores proof artifacts for a gwiki parity workflow that first searches a resolved project scope and then uses selected sources to compile a grounded explainer.

The key flow is search-to-synthesis evidence capture. The search artifact records the query, limit, command invocation, degradations, code citation targets, and ranked hybrid results for “reciprocal rank fusion hybrid search,” preserving both BM25 and semantic explanations along with fusion keys, snippets, source paths, titles, and wiki pages (docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:1-49).

The module’s collaboration pattern is therefore archival: docs/evidence groups dated evidence submodules, while the child artifact files hold the structured fields needed to audit how a wiki answer was grounded. Properties such as command, scope, source_paths, status, article_path, outline, page_writes, and citation-tracking fields indicate that search metadata, source selection, synthesis availability, and final write outputs are captured together so later reviewers can trace the workflow from inputs through generated documentation.
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:5]

## Child Modules

- [[code/modules/docs/evidence/wiki-parity-2026-06|docs/evidence/wiki-parity-2026-06]] - This evidence module captures wiki-parity proof artifacts for a `gwiki` workflow: first searching a resolved project scope, then compiling a grounded explainer from the selected sources. The search artifact records the query, limit, command, degradations, code citation targets, and ranked hybrid results for “reciprocal rank fusion hybrid search,” including per-result BM25 and semantic explanations, fusion keys, snippets, source paths, titles, and wiki pages (docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:1-49).

The compile artifacts document two runs that generated the “gsqz compression shipping decision” explainer. Both runs show daemon-routed AI synthesis using the `haiku` model with successful generated status, no errors, no fallback sections, and no stripped citations, then tie the compile command to the article path, wiki index path, handoff id, outline, and created page writes for the topic article and supporting source page (docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:1-30) (docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:1-30).

Together, the files preserve the collaboration between `gwiki search` evidence and `gwiki compile` output: search results make source discovery traceable back to code documentation pages, while compile records the exact explainer prompt, daemon synthesis availability, estimated token budget, source truncation count, and requested sections used to produce the final wiki page (docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16) (docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:31-49) (docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:31-49).
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:5]

