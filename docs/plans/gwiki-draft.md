# gwiki — Rust port of llm-wiki on gobby's data stack

## Context

[llm-wiki](https://github.com/nvk/llm-wiki) is a file-based, agent-driven knowledge system: `~/wiki/topics/<name>/` of Obsidian-compatible markdown with frontmatter, `[[wikilinks]]`, `_index.md` navigation, immutable `raw/` sources, and synthesized `wiki/` articles. The "engine" is shell scripts plus LLM skills (research / compile / query / audit) — no database.

We want **gwiki** as a fourth crate in this Cargo workspace alongside gcode/gsqz/gloc. The premise: keep llm-wiki's UX and on-disk artifacts, but back it with gobby's data stack so search, backlinks, and provenance get the same speed and rigor gcode gives code.

**Mapping is natural** — markdown files → tree-sitter-md (already a Tier-3 grammar in gcode), `[[wikilinks]]` → FalkorDB edges (like imports/calls), frontmatter tags → metadata, article bodies → PostgreSQL hub `pg_search` BM25 + Qdrant. The search pipeline (`fts` + `semantic` + `graph_boost` + `rrf`) is generic enough to reuse wholesale.

**User answers locked in:**
- Storage: option 3 — both global topics *and* per-project (my take below).
- Agent layer: full orchestrator, but research dispatch goes through gobby daemon endpoints, not internal subprocess management.
- Ingestion v1+: URLs, PDFs, local files, MediaWiki, Wayback, Git repos, plus multimodal (images / audio / video).
- LLM access: through gobby daemon (embeddings + completions + vision + transcription).

---

## My take on storage model (option 3)

**Why dual scope is right:**
- *Project-local* notes (`<project>/.gobby/wiki/`) get free cross-references with gcode symbols, sessions, memory, and tasks — all under the same `project_id`. Architectural decisions, runbooks, and design docs belong next to the code they describe.
- *Global topics* (`~/wiki/topics/<name>/`) preserve llm-wiki's topic-isolation discipline. Research about "Rust async" or "post-quantum crypto" doesn't belong in any single project; jamming it in pollutes project-scoped indexes.
- Same indexer, same schema, same CLI — the only difference is scope resolution.

**Why it's risky:**
- Two mental models. Users will ask "where does this note belong?" Mitigate with a *clear default*: inside a gobby project, default scope is project-local; everything else requires explicit `--topic <name>`. Add `gwiki promote <article> --to-topic <name>` to move misfiled notes.
- Global topics need a synthetic `project_id` so the daemon's project-scoped indexing accepts them — propose UUID5 of `gwiki:topic:<name>` with a `kind=topic` marker. **Risk**: daemon may validate project_ids against a registry; if so, we need a "topic" concept added daemon-side or we register topics as pseudo-projects. *Verify before coding v0.1.*
- Two collections in Qdrant, two namespaces in FalkorDB — keep them strictly separate from gcode's so the non-destructive constraint holds.

**Verdict:** ship option 3, but gate v0.1 on confirming the synthetic-project_id approach works with the daemon. If it doesn't, fall back to project-only for v0.1 and add topics in v0.2 once daemon support lands.

---

## Architecture

**Source of truth = markdown on disk.** Gobby stack = derived index. Same pattern gcode uses for code. Wipe the index any time, re-derive from disk; vault is portable, Obsidian works, git history survives.

### Crate layout

```text
crates/gwiki/
  Cargo.toml                 # name = "gobby-wiki", binary "gwiki", opt-level = 3
  src/
    main.rs                  # clap entry — pattern from crates/gcode/src/main.rs
    config.rs                # layered: built-in → ~/.gobby/gwiki.yaml → .gobby/gwiki.yaml → CLI
    scope.rs                 # NEW: resolve project-local vs --topic; synthesize topic project_id
    db.rs                    # thin wrapper; reuse gcore patterns
    schema.rs                # gwiki PostgreSQL hub schema (documents/chunks/links/ingestions/sessions)
    models.rs                # Document, Chunk, Link, Ingestion, Backlink
    index/
      walker.rs              # markdown discovery — pattern from crates/gcode/src/index/walker.rs
      frontmatter.rs         # NEW: YAML frontmatter parse (tags, aliases, confidence, sources)
      markdown.rs            # NEW: tree-sitter-md → headings, anchors, link spans
      links.rs               # NEW: [[wikilinks]] + std md links + alias resolution
      chunker.rs              # heading-section chunking — adapt crates/gcode/src/index/chunker.rs
      hasher.rs              # SHA-256 freshness — reuse pattern from gcode
      indexer.rs             # walk → parse → chunk → PostgreSQL hub/pg_search BM25 + FalkorDB edges + Qdrant points
    search/
      fts.rs                 # pg_search BM25 over chunks — pattern from crates/gcode/src/search/fts.rs
      semantic.rs            # Qdrant via daemon — pattern from crates/gcode/src/search/semantic.rs
      graph_boost.rs         # FalkorDB backlinks — adapt crates/gcode/src/search/graph_boost.rs
      rrf.rs                 # COPY (or extract to gcore::search) crates/gcode/src/search/rrf.rs
    ingest/
      mod.rs                 # dispatcher by source kind
      url.rs                 # HTML → markdown
      pdf.rs                 # PDF → markdown
      file.rs                # local file / stdin
      mediawiki.rs           # XML dump split to raw/  (v0.6)
      wayback.rs             # CDX collection → snapshots  (v0.6)
      gitrepo.rs             # clone + extract README/docs  (v0.6)
      multimodal/
        image.rs             # POST asset → daemon vision → markdown caption stub  (v0.7)
        audio.rs             # POST asset → daemon transcription → markdown stub  (v0.7)
        video.rs             # frame sampling + audio split via daemon  (v0.8)
    research/
      dispatch.rs            # POST /agents/dispatch — spawn N parallel research agents
      monitor.rs             # WS :60888 → stream into .session-events.jsonl
      checkpoint.rs          # .session-checkpoint.json read/write for --resume
    compile.rs               # mark raw/ sources for synthesis pass (LLM does the actual writing)
    audit.rs                 # link consistency, orphan detection, provenance trails
    output.rs                # text vs JSON — pattern from crates/gcode/src/output.rs
    skill.rs                 # vendor skills — pattern from crates/gcode/src/skill.rs
  skills/                    # markdown skill bundle shipped with the binary
    research.md
    compile.md
    query.md
    audit.md
  config.yaml                # built-in defaults (excludes, chunker tunables)
```

### CLI surface

```bash
gwiki init [--topic <name>]                       # set up project-local or topic wiki
gwiki ingest <path|url> [--topic <name>]          # add source to raw/
gwiki research "<thesis>" [--agents N] [--topic ...] # dispatch parallel research via daemon
gwiki compile [<article>]                          # trigger synthesis pass
gwiki search "<query>" [--depth quick|full|deep]
gwiki backlinks <article>
gwiki link suggest <article>                       # embeddings + graph boost
gwiki audit                                        # consistency + provenance
gwiki promote <article> --to-topic <name>          # move project-local → global topic
gwiki topic list|create|delete
gwiki status
```

### Data model

**PostgreSQL hub (gwiki-owned, namespaced tables plus pg_search BM25 indexes):**
- `gwiki_documents(id, scope, project_id, path, title, frontmatter_json, sha256, mtime, indexed_at)`
- `gwiki_chunks(id, document_id, heading_path, byte_start, byte_end, body)`
- `gwiki_chunks_search_bm25` — pg_search BM25 over `body` + `title`
- `gwiki_links(src_doc_id, dst_target, kind, byte_start)` — kind: wikilink | markdown | alias
- `gwiki_ingestions(id, scope, project_id, source_url, source_kind, raw_path, fetched_at, sha256, modality)`
- `gwiki_sessions(id, scope, started_at, status, last_event_at, checkpoint_path)`

**FalkorDB (gwiki-owned labels only — schema isolation, never touch gcode's Symbol/File):**
- Nodes: `(:WikiDoc {scope, project_id, path, title})`, `(:Source {url, modality})`
- Edges: `(:WikiDoc)-[:LINKS_TO]->(:WikiDoc)`, `(:WikiDoc)-[:CITES]->(:Source)`

**Qdrant:**
- Per-scope collections: `gwiki:project:<project_id>`, `gwiki:topic:<topic_name>`. Distinct from gcode's collections.

### Daemon endpoints (verify before coding)

| Endpoint | Status | Notes |
|---|---|---|
| Embeddings | exists (gcode uses) | reuse |
| FalkorDB proxy | exists (gcode uses) | reuse with gwiki labels |
| Qdrant proxy | exists (gcode uses) | new collections |
| `POST /agents/dispatch` | **verify** | spawn N agents with skill, return session IDs |
| `WS /sessions/<id>/events` | **verify** | stream events for monitor.rs |
| `POST /vision` | **verify** | image → caption |
| `POST /transcribe` | **verify** | audio → transcript |

If any of the verify-row endpoints don't exist, the matching gwiki phase is gated on adding them daemon-side — flag back to user before starting that phase.

### Reuse boundaries

Pull these into `gcore` as part of v0.1 (one PR, both gcode and gwiki then depend on it):
- `db.rs` — database bootstrap and connection helpers (adapt the gcode/gcore patterns).
- `search/rrf.rs` — pure RRF fusion, no code/wiki coupling.
- File walker pattern — parameterize the language/ext filter.
- SHA-256 hasher — pure utility.
- Daemon endpoint reader — already in `gcore::bootstrap`.

Keep these in gwiki only (they're domain-specific even though they look similar to gcode):
- Frontmatter parser, wikilink extractor, markdown chunker, doc-graph indexer.

---

## Phasing

| Phase | Scope | Gate |
|---|---|---|
| **v0.1** | Foundation: crate skeleton, config, scope, schema, walker, frontmatter, markdown+link parsing, pg_search BM25, CLI (init/ingest-file/search/status). Project + topic scopes both work locally. | Synthetic topic project_id verified with daemon. |
| **v0.2** | Daemon integration: embeddings + Qdrant semantic search, FalkorDB edges, RRF fusion, backlinks, link-suggest. | Daemon endpoints reachable. |
| **v0.3** | Research dispatch + WS monitor + checkpoint/resume. | `/agents/dispatch` + `/sessions/<id>/events` exist daemon-side. |
| **v0.4** | URL + PDF + file/paste ingestion. | — |
| **v0.5** | Compile + audit commands, vendored skills. | — |
| **v0.6** | MediaWiki + Wayback + Git-repo ingestion. | — |
| **v0.7** | Multimodal: image + audio. | `/vision`, `/transcribe` exist daemon-side. |
| **v0.8** | Multimodal: video (frame sampling + audio split). | — |

---

## Critical files to modify or read

**Modify (workspace root):**
- `Cargo.toml` — add `crates/gwiki` to workspace members; add `[profile.release.package.gobby-wiki]` with `opt-level = 3`.
- `crates/gcore/src/lib.rs` — accept extracted `db`, `search::rrf`, walker/hasher pattern modules.

**Read as patterns (do not modify in v0.1):**
- `crates/gcode/src/main.rs` — clap structure, global flags.
- `crates/gcode/src/config.rs` — layered config + `detect_project_root()`, `code_index_id_for_root()`.
- `crates/gcode/src/db.rs` — PostgreSQL bootstrap and hub connection helpers.
- `crates/gcode/src/falkor.rs` — FalkorDB client and Cypher query patterns.
- `crates/gcode/src/search/{fts,semantic,graph_boost,rrf}.rs` — search pipeline.
- `crates/gcode/src/index/{walker,chunker,hasher,indexer}.rs` — pipeline shape.
- `crates/gcode/src/skill.rs` — skill vendoring.
- `crates/gcode/src/output.rs` — text/JSON formatter pattern.
- `crates/gsqz/src/main.rs`, `crates/gloc/src/main.rs` — lighter clap layouts for reference on simpler subcommands.

---

## Top risks

1. **Multimodal video** is a v2-sized effort by itself (frame sampling, scene detection, audio split, transcript alignment). Don't let it gate v0.1 ship — phasing keeps it at v0.8.
2. **Research dispatch** assumes gobby daemon has agent-spawning endpoints. If they don't exist as we need, either we build them first (out of scope for gwiki) or fall back to local subprocesses (user said no). Verify in v0.3 entry gate.
3. **Topic project_id** — synthetic UUID5 must round-trip through daemon project validation. Spike this in week 1 of v0.1; if it fails, drop topics from v0.1 and add daemon support before v0.2.
4. **Schema isolation in FalkorDB** — gcode's non-destructive constraint is currently read-oriented. gwiki needs write access to its own labels. Confirm with daemon team that label-scoped writes are acceptable, or route writes through a daemon endpoint that enforces the namespace.
5. **gcode reuse vs. extraction** — pulling `db`, `rrf`, walker into `gcore` is the right move long-term but enlarges v0.1 PR. Acceptable trade — keeps gwiki and gcode from drifting.

---

## Verification

```bash
cargo build --workspace
cargo test -p gobby-wiki
cargo clippy --workspace -- -D warnings
cargo fmt --all --check
```

End-to-end smoke:
```bash
gwiki init --topic rust-async                       # creates ~/wiki/topics/rust-async/
gwiki ingest https://tokio.rs/tokio/tutorial --topic rust-async
gwiki search "select! cancellation" --topic rust-async --depth full
gwiki backlinks "concepts/cancellation.md" --topic rust-async
gwiki research "is structured concurrency a fit for tokio" --topic rust-async --agents 5
gwiki audit --topic rust-async
```

Daemon integration:
- Tail daemon logs during `gwiki ingest` — confirm Qdrant upsert + FalkorDB MERGE land.
- Open `~/wiki/topics/rust-async/` in Obsidian — links resolve, frontmatter parses, gwiki-only files (`.gwiki/`, `.session-events.jsonl`) don't break vault.
- Run `gcode search` on the same project after `gwiki init` (project scope) — confirm gwiki tables don't collide with gcode tables.

Compatibility with existing llm-wiki vaults:
- Point `gwiki init --topic <existing>` at an llm-wiki vault, run `gwiki index`, then `gwiki search` — should index without rewriting any user-facing markdown.
