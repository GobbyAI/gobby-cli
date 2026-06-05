# gwiki User Guide

A complete guide to using `gwiki` to capture, search, upkeep, and synthesize a
local-first knowledge vault: install → vault → ingest → search → research →
maintenance.

`gwiki` ingests multimodal sources (documents, PDFs, URLs, MediaWiki, git,
audio/image/video) into a Markdown vault, indexes them for hybrid search, and
turns accepted research notes into cited articles. It shares gcode's hybrid
BM25 + semantic + graph search stack and the shared Gobby AI routing layer.

## Getting Started

### Install

Download from [GitHub Releases](https://github.com/GobbyAI/gobby-cli/releases/latest)
or build from source:

```bash
cargo install gobby-wiki
```

If you use [Gobby](https://github.com/GobbyAI/gobby), gwiki is already installed.

`gwiki` is daemon-independent but not database-independent. PostgreSQL-backed
search uses ParadeDB's **`pg_search`** BM25 indexes on the `gwiki_documents` and
`gwiki_chunks` tables. The hub DSN is resolved from `~/.gobby/bootstrap.yaml`.
Run `gwiki setup --standalone` only against a PostgreSQL hub where the
`pg_search` extension is installed — setup preflights the extension before it
creates any BM25 indexes.

PostgreSQL, FalkorDB, Qdrant, and the embedding endpoint are the required
runtime stack. Use `gwiki setup --standalone` to provision or validate the same
Docker-backed services that attached Gobby mode uses.

### Scopes: `--project` vs `--topic`

Every `gwiki` command runs against one vault scope. There are two:

- `--project [ROOT]` — a Gobby project's wiki scope. Bare `--project` (no value)
  uses the current directory; `--project /path/to/repo` targets another project
  root.
- `--topic <NAME>` — a named topic vault that is independent of any project.

`--topic` wins over `--project` when both are given. With **no** scope flag,
`gwiki` detects the project from the current working directory. Scoped JSON
results carry a resolved `scope` identity with `kind` and `id`.

```bash
gwiki --project status          # current directory's project vault
gwiki --project /repo status    # another project root
gwiki --topic rust-async status # a standalone topic vault
```

The rest of this guide uses `gwiki --topic NAME <cmd>` and `gwiki --project <cmd>`
forms so the scope is always explicit.

### Initialize a Vault

```bash
gwiki --topic rust-async init
```

`gwiki init` scaffolds the vault structure and registers the scope. It creates:

| Path | Purpose |
|------|---------|
| `raw/` (+ `raw/assets/`) | Captured source bytes and the raw manifest |
| `wiki/` (+ `wiki/sources/`, `wiki/concepts/`, `wiki/topics/`) | Compiled article pages |
| `inbox/` | Drop zone for files awaiting `collect` |
| `outputs/` | Exported bundles and reports |
| `meta/` (+ `meta/health/`) | Health snapshots and vault metadata |
| `_index.md` | Wiki index landing page |
| `raw/INDEX.md` | Manifest of raw sources (drives `refresh`) |
| `log.md` | Vault activity log |

The `wiki/sources`, `wiki/concepts`, and `wiki/topics` subdirectories line up
with the three `compile --kind` values.

### Set Up Storage

```bash
gwiki --topic rust-async setup --standalone
```

`gwiki setup` creates gwiki-owned derived storage. `--standalone` resolves or
provisions the shared Gobby hub before creating gwiki storage, and provisions
Docker services when no reachable hub is configured. Setup preflights
`pg_search` before creating BM25 indexes.

**Options:**
- `--standalone` — Resolve or provision the shared Gobby hub before creating gwiki storage.
- `--database-url <DSN>` — PostgreSQL URL to use for setup without persisting the value in output.
- `--no-services` — Do not provision Docker services when no reachable hub is configured.
- `--falkordb-host <HOST>`, `--falkordb-port <PORT>`, `--falkordb-password <PASSWORD>` — FalkorDB graph store.
- `--qdrant-url <URL>` — Qdrant vector store.
- `--embedding-provider`, `--embedding-api-base <URL>`, `--embedding-model`, `--embedding-query-prefix`, `--embedding-vector-dim <DIM>`, `--embedding-api-key <KEY>` — Embedding endpoint for semantic search.

See [AI Configuration](./ai-configuration.md) for the canonical embedding and
routing matrix.

### Check Readiness

```bash
gwiki --topic rust-async status
```

Reports shell readiness, the resolved root, and the vault path. Run it after
`init`/`setup` to confirm the scope resolves before you start ingesting.

## Capture Sources

Ingestion lands raw source bytes under `raw/` and records a manifest entry in
`raw/INDEX.md`. Derived Markdown is written with frontmatter and provenance so
every downstream claim can cite its source.

### Capture a Local File (`ingest-file`)

```bash
gwiki --topic rust-async ingest-file notes/spec.pdf
gwiki --topic rust-async ingest-file media/talk.mp4 --translate --target-lang en
gwiki --topic rust-async ingest-file media/private.mp3 --no-ai
```

`ingest-file` routes a local source by type. Text-bearing sources (documents,
PDFs, HTML, Markdown, text) are derived directly; audio, image, and video are
sent through the multimodal orchestrators (transcription/translation, vision,
frame extraction) when AI routing is enabled.

**When to use:** You have a local file — document, PDF, image, audio, or video —
to bring into the vault.

**Options:**
- `--no-ai` — Disable AI-backed media extraction for this ingest (the privacy path). The source is still stored as a raw asset, with degraded derived output where applicable.
- `--translate` — Prefer audio translation over transcription where a backend is available.
- `--target-lang <LANG>` — Target language for audio translation.
- `--video-frame-interval <SECONDS>` — Seconds between sampled video frames; `0` disables frames.
- `--transcription-routing <auto|daemon|direct|off>` — Routing override for audio transcription and translation.
- `--vision-routing <auto|daemon|direct|off>` — Routing override for vision extraction.
- `--text-routing <auto|daemon|direct|off>` — Routing override for text generation.

The three `--*-routing` flags and `--no-ai` override the configured AI routing
for a single ingest. See [AI Routing & Configuration](#ai-routing--configuration).

### Fetch URLs (`ingest-url`)

```bash
gwiki --topic rust-async ingest-url https://example.com/post
gwiki --topic rust-async ingest-url https://a.com/x https://b.com/y
```

Fetches one or more URL sources into the vault. The positional `URL` argument is
repeatable. URL ingest handles web pages, Wayback captures, MediaWiki pages, and
git repositories by source type.

### Collect Inbox Drops (`collect`)

```bash
gwiki --topic rust-async collect
gwiki --topic rust-async collect "design docs"
```

Promotes recognized files dropped into `inbox/` into raw storage. The optional
`QUERY` positional narrows which drops to collect. Use this when you stage files
into `inbox/` out of band and want them brought into the vault in one pass.

### Refresh URL-Backed Sources (`refresh`)

```bash
gwiki --topic rust-async refresh
gwiki --topic rust-async refresh --id src-abc123 --id src-def456
gwiki --topic rust-async refresh --dry-run
```

`gwiki index` rebuilds derived state from files already on disk; `gwiki refresh`
re-fetches the upstream sources first, then indexes once when a batch changed.
Refresh is **manifest-driven** from `raw/INDEX.md` — it never scans directories
or follows globs.

It refreshes URL records and local files originally captured by `ingest-file`
(audio, image, video, PDF, Office, HTML, Markdown, text, and generic file
sources). Unchanged local file bytes are reported without rerunning AI/media
extraction. Connector records without replay contracts — stdin, research notes,
MediaWiki, Wayback, and git repositories — are skipped unless explicitly
selected with `--id`. Local file/media records that lack replay metadata are
reported in `failed`.

**Options:**
- `--id <SOURCE_ID>` — Source ID to refresh. Repeat to refresh multiple explicit sources.
- `--dry-run` — Preview refresh candidates without fetching, reading source bytes, writing, deleting, or indexing.

Changed content gets a new content-hash source ID and reports `old_id`,
`new_id`, `raw_path`, and `previous_raw_path`; unchanged content is left
untouched. See [`crates/gwiki/README.md`](../../crates/gwiki/README.md) for the
full refresh contract.

### List Sources (`sources`)

```bash
gwiki --topic rust-async sources
```

Lists the raw source manifest entries in the selected scope — each with its
`id`, `url`, `path`, `raw_path`, and `source_path`. Use it to find the
`SOURCE_ID` values that `refresh` and `remove-source` consume.

### Remove a Source (`remove-source`)

```bash
gwiki --topic rust-async remove-source --id src-abc123 --dry-run
gwiki --topic rust-async remove-source --id src-abc123 --yes
gwiki --topic rust-async remove-source --id src-abc123 --yes --keep-asset
```

Removes a raw source, its manifest entry, and its raw asset. `--id` is required.

**Options:**
- `--id <SOURCE_ID>` — Source ID to remove (required).
- `--dry-run` — Preview file and manifest changes without mutating the vault.
- `--yes` — Confirm destructive removal.
- `--keep-asset` — Preserve the raw source asset referenced by `source_asset` frontmatter.

## Search & Ask

### Index (`index`)

```bash
gwiki --topic rust-async index
```

Rebuilds BM25/derived search state for the Markdown and source notes in the
selected scope. Run it after capturing or editing sources so search can see
them. In PostgreSQL-backed mode, indexing also syncs the wiki graph to FalkorDB;
semantic search uses the required Qdrant and embedding configuration.

### Search (`search`)

```bash
gwiki --topic rust-async search "lifetime elision"
gwiki --topic rust-async search "lifetime elision" --limit 5
gwiki --topic rust-async search "lifetime elision" --no-semantic
```

Hybrid search across wiki documents: pg_search BM25 text matching merged with
semantic vector search and FalkorDB graph boost via Reciprocal Rank Fusion.

**When to use:** General-purpose queries over vault content. Best for natural
language and conceptual searches.

**Options:**
- `--limit <N>` — Max results (default: `10`).
- `--no-semantic` — Disable semantic vector ranking for this query (BM25 + graph only). This is a query-time ranking control; Qdrant and embeddings are still required runtime infrastructure.

### Ask (`ask`)

```bash
gwiki --topic rust-async ask "How does the borrow checker handle reborrows?"
gwiki --topic rust-async ask "..." --llm
gwiki --topic rust-async ask "..." --llm --ai direct --require-ai
```

`ask` runs the retrieval path and returns ranked hits, related pages, sources,
gaps, stale candidates, and suggested follow-up questions. Add `--llm` to
synthesize a written answer from the retrieved hits.

**When to use:** You want an answer assembled from the vault, not just a ranked
list of pages.

**Options:**
- `--llm` — Synthesize an answer from retrieved wiki hits.
- `--ai <auto|daemon|direct|off>` — AI routing override for synthesis (default: `auto`). Inert unless `--llm` is set.
- `--require-ai` — Fail if synthesis is requested but no AI route succeeds.

Without `--llm`, `ask` is a pure retrieval command and runs without any AI route.

## Navigate the Vault

### Read (`read`)

```bash
gwiki --topic rust-async read --path wiki/topics/borrow-checker.md
gwiki --topic rust-async read --title "Borrow Checker"
```

Reads a wiki page or document in the selected scope. Exactly one of `--path` or
`--title` is required.

**Options:**
- `--path <PATH>` — Vault-relative wiki path to read.
- `--title <TITLE>` — First-heading title to resolve inside the selected scope.

Read targets are restricted to canonical wiki documents: `raw/INDEX.md`,
`_index.md`, `log.md`, or paths under `wiki/`.

### Backlinks (`backlinks`)

```bash
gwiki --topic rust-async backlinks "Borrow Checker"
```

Shows the pages that link to the given page. Useful for understanding how a
concept is referenced across the vault.

### Suggest Links (`link-suggest`)

```bash
gwiki --topic rust-async link-suggest
gwiki --topic rust-async link-suggest --limit 25
```

Suggests unresolved wiki links in the selected scope — references that point at
pages that don't exist yet, so you can fill gaps or fix typos.

**Options:**
- `--limit <N>` — Max suggestions (default: `10`).

## Research & Compile

### Research (`research`)

```bash
gwiki --topic rust-async research "What changed in async fn in traits?"
gwiki --topic rust-async research "..." --max-sources 4 --source-constraint "docs.rs"
gwiki --topic rust-async research --audit
gwiki --topic rust-async research --audit --ai off
```

`research` is a mutating command with its own reason-act loop that runs inside
`gwiki` (no Gobby daemon required). Each step asks the model for the next action,
executes one allowed action — `ask`, `search`, `read`, `ingest_url`,
`ingest_file`, `accept_note`, `record_gap`, or `finish` — validates the output,
checkpoints, and stops on the first termination rule. Research produces accepted
notes under `raw/research/` and audit findings; it never writes final article
pages directly (that is `compile`'s job).

**When to use:** You want gwiki to enrich the vault on a question, gathering and
citing new sources, or to audit existing content for hygiene problems.

**Options:**
- `--audit` — Run deterministic audit checks instead of enrichment. `QUESTION` is optional in this mode; if omitted, the audit prompt is derived from vault health, stale pages, uncited claims, broken source references, and any source constraints.
- `--source-constraint <TEXT>` — Constrain acceptable sources. Repeatable.
- `--max-steps <N>` — Step budget (default: `12`).
- `--max-tokens <N>` — Combined model-output and tool-observation budget (default: `24000`).
- `--max-sources <N>` — Newly ingested external sources (default: `8`).
- `--ai <auto|daemon|direct|off>` — AI routing override (default: `auto`).
- `--require-ai` — Fail before mutation if AI is unavailable.

Enrichment mode needs a model, so `--ai off` is invalid there. `--ai off --audit`
is valid for the deterministic audit checks only and returns `ai_unavailable`
for any finding that needs model judgment. Internal budgets also include
`max_wall_time_seconds` (900) and `max_note_bytes` (24000 per note).

Every run reports a `stop_reason`: `finish`, `budget_exhausted`, `no_progress`,
`duplicate_frontier`, `source_blocked`, `write_conflict`, or `ai_unavailable`,
alongside `steps_used`, `tokens_used`, `sources_added`, and `changed_paths`.
Research tolerates another process ingesting or indexing the same vault; if a
target note changed between draft validation and commit it records
`write_conflict` and writes no partial note.

The full reason-act loop, provenance rules, audit checks, and the
gwiki-owned / Gobby-enhancer boundary are specified in
[gwiki Research Contract](../contracts/gwiki-research.md).

### Compile (`compile`)

```bash
gwiki --topic rust-async compile "Borrow Checker"
gwiki --topic rust-async compile "Borrow Checker" --kind concept
gwiki --topic rust-async compile "Borrow Checker" \
  --outline "Overview" --outline "Reborrows" --outline "Common errors"
gwiki --topic rust-async compile "Borrow Checker" --target wiki/topics/borrow.md --write-intent
```

Compiles accepted research notes into a wiki article. With no positional, it
compiles from the current accepted-note set; pass `[TOPIC]` to scope the article.

**Options:**
- `[TOPIC]` — Optional positional naming the article topic.
- `--outline <HEADING>` — Seed an article heading. Repeatable to set the section order.
- `--kind <source|concept|topic>` — Article kind (default: `topic`). Determines which `wiki/` subdirectory the page lands in (`wiki/sources`, `wiki/concepts`, or `wiki/topics`).
- `--target <PAGE>` — Explicit vault-relative target page path.
- `--write-intent` — Authorize overwriting an existing target page. By default `compile` **refuses** to overwrite an existing page and returns an `invalid_input` error asking for merge/diff handling; `--write-intent` opts into overwrite-after-merge.

`compile` is the only article-generation step. Research and audit produce
accepted notes and findings; `compile` turns those notes into cited pages and
updates the wiki index and provenance.

## Maintenance & Export

### Audit (`audit`)

```bash
gwiki --topic rust-async audit
```

Reports claims that lack source support — the uncited-claims check over the
vault. Findings include the offending page and evidence. (`gwiki research --audit`
runs a broader, optionally model-assisted audit; `gwiki audit` is the focused
deterministic claim check.)

### Lint (`lint`)

```bash
gwiki --topic rust-async lint
```

Detects broken links and vault hygiene issues — dangling wiki links, malformed
references, and similar structural problems.

### Health (`health`)

```bash
gwiki --topic rust-async health
```

Writes wiki health snapshots under `meta/health/` and reports the `text_path`
and `json_path` it wrote. Use it to capture a point-in-time readiness snapshot
for review or CI.

### Export (`export`)

```bash
gwiki --topic rust-async export workflow-assets
gwiki --topic rust-async export workflow-assets --output my-assets.md
gwiki --topic rust-async export report --from outputs/report.md --output shared/report.md
```

Exports generated bundles and reports under `outputs/`.

- `export workflow-assets` — Export bundled workflow prompts and skill assets.
  - `--output <FILE>` — Destination file (default: `workflow-assets.md`).
- `export report` — Export an existing generated report file.
  - `--output <FILE>` — Destination file (required).
  - `--from <PATH>` — Source report path (required).

## The Vault Model

A `gwiki` vault is a Markdown-first knowledge store with clear separation
between captured material and synthesized articles:

- `raw/` — Captured source bytes (`raw/assets/`) and the source manifest
  (`raw/INDEX.md`). Everything ingested lands here first.
- `inbox/` — Staging area for files dropped out of band, promoted by `collect`.
- `wiki/` — Compiled article pages, split into `wiki/sources/`,
  `wiki/concepts/`, and `wiki/topics/` to mirror the `compile --kind` values.
- `outputs/` — Exported bundles and reports.
- `meta/` — Vault metadata and `meta/health/` snapshots.

Derived Markdown carries **frontmatter** and **provenance**, and every accepted
claim **cites** a source. Research validation rejects an accepted note when a
factual claim has no source id, a source id is missing from frontmatter, a
source path is outside the resolved scope, a URL was not ingested or recorded as
intentionally external, or a quoted passage lacks available location metadata.
Unsupported claims become recorded gaps, not accepted notes. The vault model is
implemented in `crates/gwiki/src/vault.rs`, `frontmatter.rs`, `provenance.rs`,
and `citations.rs`; see the
[gwiki Development Guide](./gwiki-development-guide.md) for internals.

## AI Routing & Configuration

`gwiki` routes AI per capability. Each capability can use the daemon, a direct
OpenAI-compatible HTTP endpoint, or stay off:

| Capability | Used for |
|------------|----------|
| Audio transcription (`ai.audio_transcribe`) | Speech-to-text for audio/video |
| Audio translation (`ai.audio_translate`) | Translating audio segments |
| Vision extraction (`ai.vision_extract`) | Image/frame understanding |
| Text generation (`ai.text_generate`) | `ask --llm` synthesis, research, derived text |
| Embeddings (`ai.embeddings`) | Semantic vectors for hybrid search |

Routing values are `auto`, `daemon`, `direct`, and `off`. `direct` means any
OpenAI-compatible endpoint, local or remote — there is no `local` route. AI
settings resolve from `config_store` when the daemon database is available, then
`~/.gobby/gcore.yaml`, then defaults; `GOBBY_*` environment variables are not an
AI configuration layer.

Override routing for a single ingest with `--transcription-routing`,
`--vision-routing`, and `--text-routing`, or take the privacy path with
`--no-ai`, which forces every capability to `off` for that command while still
storing the raw asset and recording degraded derived output.

For the full capability/backend matrix, mixed-routing examples, local model
budget, and `$secret:` handling, see the canonical
[AI Configuration](./ai-configuration.md) guide.

## Graceful Degradation

The datastore stack is required: PostgreSQL stores the wiki hub/search rows,
FalkorDB stores the wiki graph, and Qdrant stores vectors. Missing datastore
configuration is a setup error, not a normal degraded search mode.

- **BM25 search** requires the PostgreSQL hub and the selected scope to be
  indexed.
- **Semantic search** requires Qdrant and a configured embedding endpoint.
- **Graph boost** requires FalkorDB and a synced wiki graph projection.
- **Multimodal ingest** falls back to storing the raw asset with explicit
  degradation markers when transcription/vision/text routing is off or
  unavailable.

JSON output still surfaces a `degradations` array for configured query-time
datastore outages, AI/media capability fallbacks, and explicit query-time
controls.

## Output Formats

All commands honor the global `--format` flag:

```bash
gwiki --topic rust-async search "query" --format json   # Default — structured JSON
gwiki --topic rust-async search "query" --format text   # Human-readable text
```

JSON is the default and the format daemon-facing code consumes; scoped results
include the resolved `scope` identity (`kind`, `id`). Suppress status messages
with `--quiet`:

```bash
gwiki --topic rust-async index --quiet
```

`gwiki contract --format json` emits the machine-readable CLI contract for
daemon conformance tests; it mirrors `crates/gwiki/contract/gwiki.contract.json`.
See [gwiki CLI Contract](../contracts/gwiki-cli.md) for the daemon-consumed
surface.

## Troubleshooting

### "No wiki scope found"

No scope resolved from the current directory. Initialize a vault or pass a scope
explicitly:

```bash
gwiki --topic NAME init
gwiki --project /path/to/repo status
```

### Empty search results

- Run `gwiki index` to pick up newly captured or edited sources.
- Confirm the scope is the one you ingested into (`gwiki status`).
- Use `gwiki status` to confirm PostgreSQL, FalkorDB, Qdrant, and embeddings
  are configured.

### `pg_search` missing

`setup` preflights ParadeDB's `pg_search` extension and fails if it is absent.
Install the `pg_search` extension on the PostgreSQL hub before running
`gwiki setup --standalone`.

### Semantic Search Configuration Error

Qdrant and the embedding endpoint are required for PostgreSQL-backed search.
Run `gwiki setup --standalone` or attach to Gobby's full datastore stack, then
re-run `gwiki index`.

### Media ingest produced skeleton output

The relevant AI capability was routed `off` or was unavailable, so ingest stored
the raw asset with degradation markers instead of derived text. Check the
`degradations` array, then re-run with an explicit routing override (for example
`--transcription-routing direct`) once the backend is reachable. `--no-ai`
always produces degraded output by design.

### `compile` refuses to overwrite a page

By default `compile` will not overwrite an existing target page. Pass
`--write-intent` to authorize overwrite-after-merge once you've confirmed the
merge is intended.

---

See also: [gwiki Development Guide](./gwiki-development-guide.md) (internals),
[gwiki README](../../crates/gwiki/README.md) (source refresh contract),
[gwiki Research Contract](../contracts/gwiki-research.md), and
[gwiki CLI Contract](../contracts/gwiki-cli.md).
