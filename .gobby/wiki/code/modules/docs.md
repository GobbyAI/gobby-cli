---
title: docs
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

# docs

Parent: [[code/repo|Repository Overview]]

## Overview

The docs module is currently a documentation namespace with no direct files of its own. Its responsibilities are expressed through child modules, especially docs/evidence, which acts as a container for proof artifacts rather than executable source or authored documentation.

The visible flow is evidence-driven: docs/evidence/wiki-parity-2026-06 records artifacts for a gwiki parity workflow that resolves a project scope, searches within that scope, selects relevant sources, and uses those sources to compile a grounded explainer. The stable component IDs show the shape of those artifacts, including search inputs and results, selected source paths, prompts, synthesis metadata, citation handling, page writes, and generated article/index paths.

Because the docs module has no direct files or source excerpts in the supplied input, collaboration is organized by containment rather than code calls: docs owns the top-level documentation area, docs/evidence groups evidence sets, and the wiki parity child set carries the concrete workflow records and metadata. No file:line spans were supplied for citation.
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:5]

## Child Modules

- [[code/modules/docs/evidence|docs/evidence]] - docs/evidence is an evidence container rather than a source module: it has no direct files of its own, and its documented behavior currently comes through child evidence sets. The visible child, docs/evidence/wiki-parity-2026-06, stores proof artifacts for a gwiki parity workflow that first searches a resolved project scope and then uses selected sources to compile a grounded explainer.

The key flow is search-to-synthesis evidence capture. The search artifact records the query, limit, command invocation, degradations, code citation targets, and ranked hybrid results for “reciprocal rank fusion hybrid search,” preserving both BM25 and semantic explanations along with fusion keys, snippets, source paths, titles, and wiki pages (docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:1-49).

The module’s collaboration pattern is therefore archival: docs/evidence groups dated evidence submodules, while the child artifact files hold the structured fields needed to audit how a wiki answer was grounded. Properties such as command, scope, source_paths, status, article_path, outline, page_writes, and citation-tracking fields indicate that search metadata, source selection, synthesis availability, and final write outputs are captured together so later reviewers can trace the workflow from inputs through generated documentation.
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:5]

