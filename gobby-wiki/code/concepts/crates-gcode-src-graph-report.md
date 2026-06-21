---
title: Graph Analytics & Reporting
type: code_concept
provenance:
- file: crates/gcode/src/graph/report/generation.rs
- file: crates/gcode/src/graph/report/loading.rs
- file: crates/gcode/src/graph/report/queries.rs
- file: crates/gcode/src/graph/report/render.rs
- file: crates/gcode/src/graph/report/rows.rs
- file: crates/gcode/src/graph/report/summary.rs
- file: crates/gcode/src/graph/report/tests.rs
- file: crates/gcode/src/graph/report/time.rs
- file: crates/gcode/src/graph/report/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/generation.rs](crates/gcode/src/graph/report/generation.rs)
- [crates/gcode/src/graph/report/loading.rs](crates/gcode/src/graph/report/loading.rs)
- [crates/gcode/src/graph/report/queries.rs](crates/gcode/src/graph/report/queries.rs)
- [crates/gcode/src/graph/report/render.rs](crates/gcode/src/graph/report/render.rs)
- [crates/gcode/src/graph/report/rows.rs](crates/gcode/src/graph/report/rows.rs)
- [crates/gcode/src/graph/report/summary.rs](crates/gcode/src/graph/report/summary.rs)
- [crates/gcode/src/graph/report/tests.rs](crates/gcode/src/graph/report/tests.rs)
- [crates/gcode/src/graph/report/time.rs](crates/gcode/src/graph/report/time.rs)
- [crates/gcode/src/graph/report/types.rs](crates/gcode/src/graph/report/types.rs)

</details>

# Graph Analytics & Reporting

## Purpose

Graph Analytics & Reporting turns the project's code graph into human-readable insight. Once a codebase has been parsed into a graph of nodes (files, modules, symbols) and edges (dependencies, references), a raw graph is hard to reason about directly. This concept adds an analytics layer on top of that graph and a reporting layer that renders the findings as Markdown.

Concretely, it answers questions an engineer actually asks about a large codebase: *Which parts of the system are the most connected and therefore the riskiest to change? Which edges act as bridges between otherwise separate areas? Which dependencies appear most often?* The working analytics are degree-based hotspot rankings, bridge-edge hypotheses, and dependency frequencies, all surfaced through generated Markdown reports. The report generation lives in the `crates/gcode/src/graph/report` module [crates/gcode/src/graph/report/generation.rs:21-23].

## Covers / Does not cover

This page covers the analytics computed over an already-constructed project code graph and the generation of Markdown reports from those analytics:

- Degree-based hotspot rankings (ranking nodes by their connectivity).
- Bridge-edge hypotheses (identifying edges that may connect distinct regions of the graph).
- Dependency frequency tallies.
- Markdown report generation [crates/gcode/src/graph/report/generation.rs:21-23].

It does **not** cover how the code graph itself is built (parsing source, constructing nodes and edges), nor the storage or persistence of that graph. It also does not cover consumers of the report output beyond producing the Markdown. Because the supplied input exposes only the report generation module and no public symbols, this page does not enumerate the concrete function names, CLI flags, or configuration keys for invoking the analytics — those are not present in the provided evidence.

## Architecture

The concept is arranged as a thin, read-only layer that sits *above* the code graph. The graph is the source of truth; analytics never mutate it. They traverse it to derive metrics (degree counts, bridge candidates, dependency frequencies), and those derived metrics are then handed to a separate reporting stage that formats them.

This separation between *analysis* and *presentation* is deliberate. By keeping the analytics independent of how results are displayed, the same metrics can feed different outputs, and the report layer can be evolved (formatting, section ordering, Markdown structure) without touching the graph-traversal logic. The reporting concern is isolated in its own module, `crates/gcode/src/graph/report` [crates/gcode/src/graph/report/generation.rs:21-23], which keeps generation code together and distinct from the graph data structures it reads.

The grouping under `graph/` reflects the dependency direction: report depends on the graph, not the reverse. This makes the analytics a leaf-ish feature that can be added or removed without destabilizing graph construction.

## Data flow

The runtime flow moves from a built graph, through analysis, to a rendered report:

1. A project code graph is provided as input to the analytics layer (this graph is constructed upstream and is outside the scope of this page).
2. Degree-based hotspot ranking traverses the graph's nodes, counts their connections, and orders them to surface the most connected hotspots.
3. Bridge-edge analysis inspects edges to form hypotheses about which edges bridge otherwise separate regions of the graph.
4. Dependency frequency analysis tallies how often dependencies occur across the graph.
5. The collected metrics are passed to the report generation module, which renders them into a Markdown report [crates/gcode/src/graph/report/generation.rs:21-23].

If the upstream graph is unavailable or empty, the analytics in steps 2–4 have nothing to traverse and produce no metrics, leaving the report in step 5 with no findings to render. The supplied evidence does not show the specific fallback or error behavior for a missing graph, so the precise handling of that case should be confirmed against the module source rather than assumed.

## Key components

The only component exposed by the supplied input is the report generation module; the analytics functions themselves are not present as indexed symbols.

| Symbol / Module | Role |
| --- | --- |
| `crates/gcode/src/graph/report` | Generates the Markdown report from the computed graph analytics [crates/gcode/src/graph/report/generation.rs:21-23] |

## Where to start

Begin with the report generation module, `crates/gcode/src/graph/report`, at `generation.rs` [crates/gcode/src/graph/report/generation.rs:21-23]. It is the entry point that ties the analytics together into output, so reading it first shows what metrics are ultimately consumed (hotspot rankings, bridge-edge hypotheses, dependency frequencies) and how they are shaped into a Markdown report. From there, trace backward into the graph-traversal code that produces each metric to understand how the numbers are computed.

## Explore

- [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

