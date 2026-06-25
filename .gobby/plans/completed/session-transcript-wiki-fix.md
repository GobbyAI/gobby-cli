# Session knowledge-synthesis: daemon-side synth + gwiki vault ingest

## Context

gwiki's `sync-sessions` is live but produces a **verbose, redundant** artifact: it re-parses raw
`~/.gobby/session_transcripts/*.jsonl.gz` with 7 per-CLI adapters into a full `## Messages` dump
(every user/assistant turn + every `Tool use:`/`Tool result:` block), and **ignores** the daemon's
existing `sessions.digest_markdown` (per-turn distillation) and `sessions.summary_markdown` (handoff).

In the wiki bake-off, only **llm-wiki** (1 of 7 competitors) does session ingestion. Its value is a
**concise knowledge page** per session — `Summary` / `Key Claims` / `Key Quotes` / `Connections (([[wikilinks]]))` /
`Contradictions` — which neither the daemon nor gwiki produces today. The daemon's `summary_markdown`
is **handoff-purposed** (`Current State` / `Files Changed` / `Next Steps`, git-grounded, for resuming work);
folding llm-wiki's prompt into it would degrade that job. They are complementary artifacts.

**Decision (user-approved):** add a **new** knowledge-synthesis artifact daemon-side, fed by the already-distilled
`digest_markdown` (cheap, no raw re-read), using llm-wiki's prompt; have gwiki **ingest** that synthesized
markdown into the vault for search/graph/backlinks, and **demote** the raw `.jsonl.gz` re-parse to a fallback.

**Outcome:** concise + durable + cross-linked session knowledge in the vault; one synthesis owner (daemon);
no duplicate parsing; verbosity gone.

This is **one effort across both repos** (not split):
- **Daemon** (Python) — `/Users/josh/Projects/gobby` — synthesis generation + persistence + file mirror.
- **gwiki** (Rust) — `/Users/josh/Projects/gobby-cli` (this repo) — vault ingest of the synthesized markdown.

**Execution order:** Part A (daemon) first so the seam files exist; then Part B (gwiki) ingests them. gwiki
code can be written in parallel against a hand-authored `~/.gobby/session_wiki/*.md` fixture, but the
end-to-end verification requires Part A landed. Each repo gets its own branch + commit(s).

> Incorporates Codex review corrections: real trigger path, migration `296`, dedicated revisions table,
> `gobby_home()` path resolution, explicit redaction, path-based document kind, external_id fallback keying,
> and regeneration/update behavior.

---

## The seam (transport contract)

Daemon writes one file per session: **`~/.gobby/session_wiki/{external_id}.md`** (path resolved through
`gobby_home()`, **not** `Path(relative).expanduser()` — see A.3).

```markdown
---
title: "Session: f0a56143 — 2026-06-03"
type: source
tags: [prompt-caching, indexing-performance, rust]   # 3–5 from synthesis
date: 2026-06-03
model: claude-opus-4-8
project: gobby-cli
session_id: 169fe279-7e82-402e-ba6c-fe3f26ac8a57
source: claude-code        # session_source
---
## Summary
…
## Key Claims
- …
## Key Quotes
> "…" — context
## Connections
- [[EntityName]] — relation
## Contradictions
- Contradicts [[OtherPage]] on: … (only if applicable)
```

- The LLM emits **body only**; the daemon wraps frontmatter (as llm-wiki does).
- **Redaction is mandatory before the daemon writes the file** — `Key Quotes` can carry secrets lifted from the
  digest. gwiki re-redacts defensively on ingest (B.2).
- gwiki **parses and strips** this frontmatter, then writes its **own** gwiki-owned frontmatter + the daemon body
  (no nested frontmatter blocks — B.2).

---

## Part A — Daemon synthesis (`/Users/josh/Projects/gobby`)

1. **Prompt** — new `src/gobby/install/shared/prompts/wiki/source_page.md`. Port llm-wiki's prompt
   (`/Users/josh/Projects/wiki-bakeoff/llm-wiki/llmwiki/synth/prompts/source_page.md`: suggested-tags comment →
   `Summary`/`Key Claims`/`Key Quotes`/`Connections`/`Contradictions`, the 5 synthesis rules, "body only / caller
   adds frontmatter"). **Change the input** from "raw session transcript" to the **per-turn digest**: feed
   `{{ digest_markdown }}` (+ `{{ meta }}` = project/date/model/tools/tokens). Add YAML frontmatter listing
   required/optional vars; loaded via `src/gobby/prompts/loader.py` `PromptLoader.render("wiki/source_page", ctx)`.

2. **Schema** — new migration **`src/gobby/storage/migrations/296_add_wiki_to_sessions.postgres.sql`**
   (`BASELINE_VERSION` = 294 in `storage/migrations.py:31`, but `295_relabel_gemini_sessions.postgres.sql` already
   exists → next is **296**; re-confirm no later migration lands first).
   - `sessions` columns: `wiki_markdown TEXT`, `wiki_revision_id TEXT`, `wiki_generated_at TIMESTAMPTZ`,
     `wiki_path TEXT`, `wiki_source_context_hash TEXT`, `wiki_digest_turn_count INTEGER`, `wiki_generation_mode TEXT`
     (traceability parity with summary). Wire a **composite FK** `(wiki_revision_id, id)` →
     `session_wiki_revisions(id, session_id)` — not a bare `wiki_revision_id → id`, which would let a session point at
     another session's wiki revision — + index, matching the summary-revision wiring at
     `storage/postgres_baseline_schema.sql:272`.
   - **New dedicated table** `session_wiki_revisions` (do **not** overload `session_summary_revisions` — different
     artifact), mirroring the **summary-revision constraints**: `id` PK, `session_id` FK→sessions,
     `previous_revision_id` (self-FK, nullable), `wiki_markdown`, `source_context_hash`,
     `digest_turn_count INTEGER CHECK (digest_turn_count >= 0)`, `generation_mode` (+ a value CHECK if summary has
     one), `created_at`; **`UNIQUE (id, session_id)`** (backs the composite FK above); index on `session_id`.
   - Mirror fields onto the `Session` dataclass (`storage/session_models.py`) and `storage/postgres_baseline_schema.sql`.

3. **Feature config** — new `SessionWikiConfig(FeatureDefaultConfig)` in `src/gobby/config/sessions.py`
   (mirror `SessionSummaryConfig`): `enabled`, **`prompt_path="wiki/source_page"`** (a *loader path*, not literal
   prompt text — `SessionSummaryConfig.prompt` is a literal fallback string and `call_feature` does **not** read
   `feature_config.prompt`; see A.4), `wiki_file_path=".gobby/session_wiki"`, default `profile=FeatureProfile.LOW`
   (claude/haiku — parity with summary; bump to MEDIUM if eval shows thin claims).
   Register `session_wiki: SessionWikiConfig` on `DaemonConfig` (`src/gobby/config/app.py`).
   **Resolve `wiki_file_path` through `gobby_home()`** at write time (a relative `.gobby/session_wiki` stays
   relative under `Path.expanduser()` — must join onto gobby home).

4. **Generation + persist (single integration point)** — append wiki synthesis to the **tail of the existing
   `generate_session_summaries` flow** (gated by `session_wiki.enabled`) so **every** caller — lifecycle/background,
   dispatcher, and CLI/server/MCP refresh — produces both artifacts with no caller drift. (May expose a
   `generate_session_artifacts` alias, but the integration must be the shared summary flow, not one re-pointed caller.)
   - **Render the prompt explicitly**: `prompt = PromptLoader.render(config.prompt_path, ctx, strict=True)`
     (`strict=True` so a missing `digest_markdown`/`meta` fails loudly), then `llm_service.call_feature(session_wiki,
     prompt, …)` — `call_feature` takes an already-rendered prompt (`llm/service.py:88`).
   - **Input + concrete threshold**: input = `session.digest_markdown`; run synthesis only when
     `digest_turn_count >= 3` — the **same** threshold the summary uses (lifecycle treats `< 3` as skip-worthy) — so
     "wiki never runs where summary wouldn't" holds literally. Below it → **skip** (no transcript-like fallback: the
     artifact is digest-backed synthesis, and a fallback reintroduces drift + test ambiguity).
   - **Skip policy lives inside the shared wiki-generation function** (not only in lifecycle): gate on
     subagent / pipeline / cron / short-session **there**, so manual CLI/server/MCP refresh enforces the same skips as
     lifecycle. Wiki never runs where summary wouldn't.
   - **Redact the synthesis once, before any persistence.** `persist_wiki_state(...)` then stores the **redacted**
     `wiki_markdown` in the `sessions` columns **and** the `session_wiki_revisions` row (with `previous_revision_id`) —
     DB and file must not diverge on secrets — and the same redacted body is written to the `gobby_home()`-resolved
     `session_wiki/{external_id}.md`. (`persist_wiki_state` mirrors `persist_summary_state`,
     `storage/sessions/_summary_update.py`.)

5. **Trigger + gate (corrected)** — `_session_end.py` does **not** generate summaries (it cleans up + marks status);
   generation runs from the lifecycle/background + dispatcher path. Hanging wiki off the tail of
   `generate_session_summaries` (`src/gobby/sessions/summarize.py:194`) covers all callers, **but** the lifecycle gate
   `_generate_summaries_if_needed` returns early when `summary_markdown` is already valid — so a session with a summary
   but no wiki would never synthesize one. **Extend that gate** (rename to artifact-generation): proceed when summary
   is missing/invalid **OR** `wiki_markdown` is missing/stale, running only the missing artifact(s). Full generation at
   the refresh point is enough; no per-turn/delta mode for a knowledge page; nothing added to `_session_end.py`.

---

## Part B — gwiki vault ingest (`/Users/josh/Projects/gobby-cli`)

Source the daemon's synthesis files **first** (keyed by `external_id`), raw archives **second**.

1. **CLI/dir** — add `wiki_dir: Option<PathBuf>` (`--wiki-dir`) to `SyncSessionsArgs` (`crates/gwiki/src/main.rs`)
   and `SyncSessionsOptions` (`crates/gwiki/src/api.rs`). Add `wiki_dir_or_default()` →
   `gobby_home().join("session_wiki")` beside `archive_dir_or_default()` (`crates/gwiki/src/commands/session_sync.rs`).

2. **Synthesis ingest** — new `ingest_session_wiki_file_without_index()` in `crates/gwiki/src/ingest/session.rs`,
   parallel to `ingest_session_file_without_index()`:
   - Read the `.md` bytes; **parse and strip the daemon frontmatter**, keep the body.
   - Register a `SourceDraftRef { kind: SourceKind::Session, location = "session:{external_id}", … }` via
     `SourceManifest`. **Use `session:{external_id}` as the canonical location for BOTH this path and the raw fallback
     (B.3)** so a session is one logical source and replacement lookup (B.4) is stable across content changes and lets
     synthesis supersede raw. (The raw fallback currently keys location on the file path — change it to
     `session:{external_id}` too.)
   - Write **gwiki-owned** source frontmatter (`source_kind: session`, `source_location: session:{external_id}`,
     `source_hash`, `session_type` ← daemon `source`, `model`, carry `tags`, **plus a separate `source_archive` field
     preserving the original transcript / daemon mirror path** — since `source_location` is now the canonical
     `session:{external_id}`, the real provenance path needs its own field) + the daemon body to
     `knowledge/sources/{id}.md` (no `## Messages`). One frontmatter block only.
   - **Re-redact** the body defensively (`redact_session_markdown`) before write.
   - Note: `knowledge/sources/*.md` indexes as `WikiDocumentKind::SourceNote` (`indexer.rs:258`, path-based — the
     indexer does **not** read frontmatter for kind). Same kind sessions already use today; a distinct
     `WikiDocumentKind::Session` is **out of scope** (would touch `document_kind` + the enum).

3. **Sourcing loop + fallback (keyed by external_id, not content hash)** — in
   `crates/gwiki/src/ingest/session_archive.rs`: build `synthesized = { file stem of *.md in wiki_dir }`.
   Ingest each synthesis file via B.2. For `*.jsonl.gz` in `archive_dir` whose **stem ∉ synthesized**, fall back to
   the existing adapter parse (`ingest_session_file_without_index`); **suppress** raw parse when `{external_id}.md`
   exists. **Strip the full compound suffix explicitly** — `Path::file_stem` on `abc.jsonl.gz` returns `abc.jsonl`,
   not `abc`; reduce both `.jsonl.gz` and `.md` to the bare `external_id` before comparing. Do **not** use content-hash
   to decide synthesis-vs-raw — content-hash dedup at `session_archive.rs:65` still applies *within* each path for
   re-run skipping.
   Single `index_after_ingest(vault_root, store)?` at the end pushes BM25/Qdrant/FalkorDB.

4. **Regeneration / replacement (latest-wins)** — source IDs **embed the content-hash prefix**
   (`crates/gwiki/src/sources/render.rs:168`) and derived paths are built from that ID (`crates/gwiki/src/paths.rs:29`),
   so a content change **cannot** reuse the same `{id}.md` without redesigning source IDs (out of scope). Do
   **latest-wins replacement** instead: look up any existing manifest entry for the same canonical location
   (`session:{external_id}`); if found with a **different** content hash, **remove the old manifest entry + old derived
   page**, then register the new content (new hash-prefixed id) and reindex. This also lets a fresh synthesis supersede
   a previously raw-parsed page for the same session — exactly one page per session.
   **Back-compat:** existing vaults may already hold raw session pages keyed by the **old** location
   (`session_transcripts/{file_name}` / the archive file path). The replacement lookup must match **both** the old
   location form and the new `session:{external_id}` during transition, or stale verbose pages survive beside the new
   synthesis page.

5. **Links come free** — `indexer.rs` `parse_wiki_document` → `extract_links` (`links.rs`) pulls `[[wikilinks]]`
   into `gwiki_links` (`store.replace_links`), so `## Connections` become real backlinks; the page joins
   `gwiki search` / `ask` / `compile` / `backlinks` automatically.

---

## Reused, do not rebuild

- Daemon: `PromptLoader.render`, `FeatureDefaultConfig`/`call_feature`, `persist_summary_state` (template for
  `persist_wiki_state`), migration file-versioning, the `generate_session_summaries` lifecycle/dispatcher call site.
- gwiki: `SourceManifest` dedup, `SourceDraftRef`/`SourceRecord`, `write_session_derived_markdown`,
  `index_after_ingest` → `indexer::index_vault`, `links.rs` wikilink extraction, `session/metadata.rs` field builders,
  `redact_session_markdown`.

---

## Verification (end-to-end)

1. **Daemon unit**: feed a fixture `digest_markdown` to the wiki synthesis; assert body has the five sections +
   ≥1 `[[wikilink]]` + redaction applied (no `sk-…`, no real home path) **in both the DB column and the file**.
   Assert `persist_wiki_state` writes the row columns, a `session_wiki_revisions` row, and the `gobby_home()`-resolved
   `session_wiki/{external_id}.md` file with correct frontmatter.
   - **Migration test**: after applying `296`, assert the composite FK `(wiki_revision_id, id)` →
     `session_wiki_revisions(id, session_id)`, the `UNIQUE (id, session_id)`, and the `session_id` index all exist.
   - **Summary-noop test**: a session whose `summary_markdown` is valid but `wiki_markdown` is missing still triggers
     wiki synthesis through the extended artifact-generation gate (proves the Blocker-1 fix).
   Run the daemon suite for the touched modules.
2. **Real synthesis**: drive a session through the summary-refresh path with a populated `digest_markdown`; confirm
   `wiki_markdown` is set and the mirror file is concise (~1 screen), not a transcript.
3. **gwiki ingest**: `gwiki sync-sessions --wiki-dir <dir>`; confirm `knowledge/sources/{id}.md` is the synthesis
   page (single frontmatter block, no `## Messages`); re-run skips by content hash.
   `cargo nextest run -p gobby-wiki`, `cargo clippy --workspace -- -D warnings`, `cargo fmt --all --check`.
4. **gwiki content test**: synthesized session page contains `## Summary`, `## Key Claims`, `## Connections`,
   ≥1 `[[wikilink]]`, and **no** `## Messages`.
5. **gwiki fallback test**: with both `abc.md` and `abc.jsonl.gz` present, only the synthesized page is
   ingested/indexed (raw parse suppressed).
6. **gwiki replacement test**: re-running with changed `abc.md` content removes the old `knowledge/sources/{id}.md`
   and writes the new-hash page for the same `session:{external_id}` (no orphan; exactly one page per session).
7. **Vault wiring**: `gwiki search "<concept from a Key Claim>"` returns the session page;
   `gwiki backlinks "<EntityName>"` shows it via `## Connections`.
8. **A/B vs baseline**: run on the 8 bake-off transcripts (`~/Projects/wiki-bakeoff/inputs/track-b-sessions/`) and
   eyeball gwiki's synthesis pages against `~/Projects/wiki-bakeoff/outputs/llm-wiki/run/wiki/sources/gobby-cli/*.md`
   (do **not** modify the preserved bake-off baseline).

---

## Confirm at implementation time

- Migration number `296` still free at landing (no later migration merged first).
- `digest_markdown` coverage per session source; size of the raw-parse fallback set (Gemini in particular may lack
  daemon synthesis today — gwiki's Gemini adapter stays as fallback).
- `SessionWikiConfig` model profile after eyeballing claim/quote quality (LOW vs MEDIUM).
- Whether `generate_session_artifacts` should also fire on `/clear` and `/compact` (like summary) or session-end only.
- Whether to also vault `digest_markdown` as a collapsed "transcript" companion page (deferred; not in this plan).
