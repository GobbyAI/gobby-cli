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
gcode codewiki --out /path/to/vault
gwiki --project /path/to/project index
```

Limit generation to one or more indexed paths:

```bash
gcode codewiki --scope crates/gcode src
```

## Output Tree

The generated tree is hierarchical:

- `code/repo.md` is the repository overview.
- `code/modules/<module>.md` documents directory/module groups.
- `code/files/<path>.md` documents individual source files.
- `code/_architecture.md` is the architecture overview page.
- `code/_onboarding.md` is the "Start Here" onboarding page.
- `code/_hotspots.md` reports change hotspots.
- `code/_changes.md` reports index changes since the previous run.
- `code/_ownership.md` reports code ownership (git blame derived).
- `_meta/codewiki.json` records the docs written in the last run for
  incremental regeneration.
- `_meta/ownership.json` records ownership data for repeat runs.

Documents use `[[wikilink]]` references between repo, module, and file pages.
Each page includes `provenance:` frontmatter with file paths and line ranges
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
`text_generate` route for generated prose. Generated text is citation-checked
before write. Empty or unavailable generation falls back to structural AST-only
prose.

`--ai-depth` controls how deep AI prose generation reaches; gated tiers use
structural fallbacks:

- `sections` — architecture, module, and repo prose only (cheapest; a handful
  of LLM calls).
- `files` (default) — sections plus per-file summaries (one call per file).
- `symbols` — files plus per-symbol purposes. This issues one LLM call per
  indexed symbol and can take hours-to-days on large repos with local models;
  reserve it for small repos or scoped runs.

On the daemon route, aggregate docs (architecture, module, and repo prose)
request the heavier `feature_mid` daemon profile because they synthesize many
child summaries into one long grounded answer; file and symbol docs stay on
the daemon default profile. Override the aggregate tier with
`--ai-aggregate-profile <PROFILE>`.

## Diagrams

When FalkorDB graph edges are available, module docs can include bounded Mermaid
diagrams:

- Dependency diagrams from import edges.
- Call sequence diagrams from call edges.

The diagrams are intentionally bounded around the documented module. They are
not full-graph dumps.

## Citations

Every generated claim is grounded against indexed source spans. Invalid
citations are stripped, and prose with no valid citation gets a bounded set of
representative fallback citations (at most a handful, spread across distinct
source files) rather than the full span list. `repo.md` resolves citations
through numbered `[N]` markers, and its References section lists only the
markers that actually appear in the page. This keeps prose tied to source
files and line ranges that gcode has actually indexed without letting broad
pages accumulate citation walls.

## Incremental Regeneration

`gcode codewiki` hashes source files referenced by each generated document.
On later runs, unchanged file docs are preserved; changed files cause their file
doc, owning module doc, and `repo.md` to regenerate. `_meta/codewiki.json`
records the generated set for audit and repeat runs, along with the AI mode of
the last run (`off`, `sections`, `files`, or `symbols`); changing the AI route
or `--ai-depth` invalidates every doc, since prose content depends on the
generation mode rather than source hashes alone.

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

1. Run `gcode codewiki --out <vault>`.
2. Run `gwiki --project <project-root> index`.
3. gwiki's vault index walk discovers `code/**/*.md`, preserves
`provenance:` frontmatter, extracts `[[wikilinks]]`, and indexes changed
   docs incrementally.

Because gcode writes vault-ready Markdown, gwiki only needs to classify and
index the generated subtree. Re-running codewiki rewrites only changed docs, and
the next gwiki index run picks up only those changed Markdown files.

_Last verified: 2026-06-01_
