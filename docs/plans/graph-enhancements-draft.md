# Graph Enhancements Draft

## Summary

Use Graphify as product and UX inspiration for native gcode and Gobby graph
work. Keep gcode as the deterministic code index and retrieval engine. Let
Gobby own richer graph orchestration, memory/code joins, reports, UI, MCP
surfaces, and cross-repo workflows.

This plan does not add Graphify as a runtime dependency.

## Goals

- Make graph edges safer for agents by distinguishing deterministic facts from
  inferred relationships.
- Give agents and humans a quick orientation report before they dive into code
  search.
- Connect the existing code graph and memory knowledge graph without collapsing
  their ownership boundaries.
- Prepare for cross-repo graph views using Gobby projects and clones.

## Non-Goals

- Do not rebuild Graphify inside gcode.
- Do not add video/audio/PDF ingestion in this phase.
- Do not make gcode own Gobby database lifecycle or Gobby-owned schema.
- Do not run or automate `gcode invalidate`.

## gcode Side

### Graph Result Provenance

- Extend graph-facing result types so relationships can carry:
  - `provenance`: `EXTRACTED`, `INFERRED`, or `AMBIGUOUS`
  - `confidence`: optional float, with `1.0` for deterministic code edges
  - `source`: optional source detail such as file path, line, or upstream system
- Preserve compatibility for existing callers by making the new fields optional
  in JSON output.
- Treat code-derived `CALLS`, `IMPORTS`, and `DEFINES` as `EXTRACTED`.

### `gcode graph report`

- Add a `gcode graph report` command under the existing `graph` subcommand.
- Prefer the Gobby daemon report endpoint when available.
- Support `--format json` and `--format text`.
- Text output should be Markdown-oriented and suitable for dropping into a
  project plan or agent prompt.
- If the daemon or Neo4j is unavailable, return a clear degraded response rather
  than failing with a transport-heavy error.

### Report Contents

The report should include:

- High-degree files and symbols.
- Call graph hubs and blast-radius hotspots.
- Unresolved and external call targets worth inspecting.
- Top imported modules.
- Suggested investigation questions based on graph structure.
- Explicit provenance guidance reminding agents to trust `EXTRACTED` edges more
  than inferred links.

### Constraints

- Keep gcode non-destructive to Gobby-owned data.
- Do not write `.gobby/project.json`.
- Do not alter or drop Gobby-created tables.
- Do not modify `config_store`.
- Keep CI green with:
  - `cargo test --no-default-features`
  - `cargo clippy --no-default-features -- -D warnings`

## Gobby Side

### Code Graph Edge Metadata

- Update `CodeGraph` Neo4j writes so deterministic code edges include:
  - `provenance = "EXTRACTED"`
  - `confidence = 1.0`
  - `source_system = "gcode"`
  - file/line source properties where available
- Apply this to `DEFINES`, `IMPORTS`, and `CALLS`.
- Expose these properties through existing code graph HTTP routes and frontend
  graph data types.

### Memory Knowledge Graph Metadata

- Update `KnowledgeGraphService` so LLM-created entity relationships include:
  - `provenance = "INFERRED"`
  - `confidence` when extraction prompts return it
  - conservative default confidence when omitted
  - source memory identifiers for auditability
- Mark uncertain or malformed relationships as `AMBIGUOUS` when extraction can
  recover enough structure to keep them.
- Keep memory SQLite as source of truth; Neo4j remains a projection.

### Code/Memory Bridge Edges

- Extend `RELATES_TO_CODE` edges with:
  - `provenance = "INFERRED"`
  - Qdrant similarity as `confidence`
  - matching method, such as `entity_embedding_to_code_symbol`
  - update timestamp
- Agent-facing tools should label these links as hypotheses and prefer
  `EXTRACTED` call/import edges when planning edits.

### Project Graph Report Service

- Add a Gobby service that computes a project graph report from Neo4j.
- Include code graph facts, memory graph facts, and code/memory bridge edges.
- Return both:
  - Markdown for humans and agent orientation
  - JSON for UI, MCP, and CLI callers
- Expose the report through:
  - HTTP route under code-index or project graph namespace
  - MCP tool for agent use
  - `gcode graph report` via daemon call

### Report Metrics

The first version should use simple explainable metrics:

- Degree counts for files, symbols, entities, and modules.
- Incoming call counts for blast-radius risk.
- Unresolved/external call target frequency.
- Count and confidence range for `RELATES_TO_CODE` links.
- Cross-domain links between memory entities and code symbols.

Skip advanced community detection in v1. Add Leiden-style clustering later if
the basic report proves useful.

### Cross-Repo Graph Views

- Use existing Gobby projects and clones as graph scopes.
- Build read-only merged graph views tagged with source project, repo path, and
  clone ID when applicable.
- Do not merge project-owned graph projections destructively in v1.
- Target use cases:
  - Explain how service A depends on library B.
  - Find shared concepts across repos.
  - Identify cross-repo blast-radius hints before coordinated edits.

### UI

- Add provenance and confidence display to code graph and memory graph detail
  panels.
- Add a project graph report surface in the existing graph/code/memory area.
- Keep the report readable as a dense operational view, not a marketing-style
  graph dashboard.

## Interfaces

### Edge Metadata Shape

```json
{
  "type": "CALLS",
  "source": "symbol-a",
  "target": "symbol-b",
  "provenance": "EXTRACTED",
  "confidence": 1.0,
  "source_system": "gcode",
  "file_path": "src/example.rs",
  "line": 42
}
```

### Report JSON Shape

```json
{
  "project_id": "project-id",
  "generated_at": "2026-05-03T00:00:00Z",
  "summary": {
    "nodes": 0,
    "edges": 0,
    "code_edges": 0,
    "memory_edges": 0,
    "bridge_edges": 0
  },
  "high_degree_nodes": [],
  "blast_radius_hotspots": [],
  "unresolved_targets": [],
  "code_memory_bridges": [],
  "suggested_questions": [],
  "markdown": "# Project Graph Report\n"
}
```

## Suggested Implementation Order

1. Add edge provenance and confidence to Gobby Neo4j writes and reads.
2. Extend memory knowledge graph and `RELATES_TO_CODE` edges with provenance.
3. Add the Gobby project graph report service and HTTP route.
4. Add the MCP tool for retrieving the report.
5. Add `gcode graph report` as a thin daemon-backed CLI.
6. Add frontend rendering for provenance/confidence and the report surface.
7. Prototype read-only cross-repo merged graph views.

## Test Plan

### gcode

- Unit tests for `gcode graph report` CLI parsing.
- Unit tests for daemon URL construction and degraded daemon/Neo4j responses.
- JSON compatibility tests proving existing graph commands still parse without
  the new metadata fields.
- Run:
  - `cargo test --no-default-features`
  - `cargo clippy --no-default-features -- -D warnings`

### Gobby

- Unit tests for `CodeGraph.sync_file` proving deterministic edges get
  `EXTRACTED` and `confidence = 1.0`.
- Unit tests for knowledge graph relationship writes proving inferred edges get
  provenance, confidence, and source memory references.
- Unit tests for `RELATES_TO_CODE` edge metadata.
- Route tests for graph report success, empty graph, unavailable Neo4j, and
  project scoping.
- MCP tests for graph report tool shape and degraded responses.
- Frontend tests for displaying provenance/confidence in graph detail panels.

## Acceptance Criteria

- Existing gcode graph commands keep working for current JSON consumers.
- New graph metadata is visible in Gobby HTTP responses and UI detail panels.
- `gcode graph report` returns a useful report when Gobby and Neo4j are
  available.
- `gcode graph report` degrades cleanly when graph services are unavailable.
- Agents can distinguish extracted code facts from inferred semantic links.
- No Gobby-owned database or project metadata is modified by gcode.

## Assumptions

- Neo4j remains the shared graph projection layer for code and memory.
- SQLite remains source of truth for gcode symbols/files and Gobby memories.
- Qdrant similarity is acceptable as confidence for code/memory bridge edges.
- Graph reports are derived artifacts and can be regenerated at any time.
- Cross-repo graph work starts as read-only views before any persistent merged
  projection is considered.
