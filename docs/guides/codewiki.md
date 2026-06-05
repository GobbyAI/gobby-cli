# gcode Codewiki Guide

`gcode codewiki` generates vault-ready Markdown documentation from the code
index. It is the producer in the code-to-wiki workflow: gcode owns AST symbols,
source spans, and the FalkorDB graph; gwiki later indexes the generated Markdown
as normal vault documents.

## Run

Generate docs into the default `codewiki/` directory:

```bash
gcode codewiki
```

Write directly into a gwiki vault code-doc subtree:

```bash
gcode codewiki --out /path/to/vault/wiki/code
gwiki index --vault /path/to/vault
```

Limit generation to one or more indexed paths:

```bash
gcode codewiki --scope crates/gcode src
```

## Output Tree

The generated tree is hierarchical:

- `repo.md` is the repository overview.
- `modules/<module>.md` documents directory/module groups.
- `files/<path>.md` documents individual source files.
- `_meta/codewiki.json` records the docs written in the last run for
  incremental regeneration.

Documents use `[[wikilink]]` references between repo, module, and file pages.
Each page includes `source_files:` frontmatter with file paths and line ranges
derived from indexed symbol spans.

## Generation Pipeline

`gcode codewiki` resolves the project context, loads indexed files and symbols
from PostgreSQL, filters out non-core files such as tests and generated/vendor
paths, and asks FalkorDB for call/import edges when graph configuration is
available.

The generator then builds docs bottom-up:

1. File docs are created from AST symbols, signatures, component IDs, and exact
   source spans.
2. Files are clustered into modules. With graph edges, connected call/import
   components are grouped under their common module. Without graph edges,
   directory and AST grouping are used.
3. Module docs aggregate direct files and child modules.
4. `repo.md` summarizes the top-level modules and root files.

When `ai.text_generate` is configured, gcode calls the shared
`text_generate` route for symbol, file, module, and repo prose. Generated text
is citation-checked before write. Empty or unavailable generation falls back to
structural AST-only prose.

## Diagrams

When FalkorDB graph edges are available, module docs can include bounded Mermaid
diagrams:

- Dependency diagrams from import edges.
- Call sequence diagrams from call edges.

The diagrams are intentionally bounded around the documented module. They are
not full-graph dumps.

## Citations

Every generated claim is grounded against indexed source spans. Invalid
citations are stripped, and missing citations are repaired with a valid fallback
span when one exists. This keeps prose tied to source files and line ranges that
gcode has actually indexed.

## Incremental Regeneration

`gcode codewiki` hashes source files referenced by each generated document.
On later runs, unchanged file docs are preserved; changed files cause their file
doc, owning module doc, and `repo.md` to regenerate. `_meta/codewiki.json`
records the generated set for audit and repeat runs.

## Graph-Degraded Output

FalkorDB is required for graph-derived codewiki structure. In explicitly
degraded paths, or when a configured FalkorDB service is unreachable, codewiki
still produces valid docs:

- Clustering degrades to directory and AST-only grouping.
- Component IDs remain `file_path::name`.
- Non-core filtering still applies.
- Module, file, and repo prose is still emitted and citation-grounded.
- Graph-derived Mermaid diagrams are omitted or replaced with the
  `degraded: graph-unavailable` marker.

This degraded mode is the expected standalone behavior for projects that have
PostgreSQL code-index data but no graph service.

## gcode to gwiki Ingest

The intended handoff is a file workflow, not a crate dependency:

1. Run `gcode codewiki --out <vault>/wiki/code`.
2. Run `gwiki index --vault <vault>`.
3. gwiki's vault index walk discovers `wiki/code/**/*.md`, preserves
   `source_files:` frontmatter, extracts `[[wikilinks]]`, and indexes changed
   docs incrementally.

Because gcode writes vault-ready Markdown, gwiki only needs to classify and
index the generated subtree. Re-running codewiki rewrites only changed docs, and
the next gwiki index run picks up only those changed Markdown files.

_Last verified: 2026-06-01_
