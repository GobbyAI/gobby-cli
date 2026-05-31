# gwiki Multimodal AI — productionize multimodal ingest and unify Gobby CLI AI services

<!-- markdownlint-disable MD013 MD036 -->

**Plan ID:** gwiki-multimodal-ai

## O1: Overview

`kind: framing`

The shipped `gwiki.md` epic built `## P6: Multimodal Ingestion` (image/audio/video) as a **skeleton with
LLM-shaped placeholders**: `crates/gwiki/src/transcribe.rs`, `vision.rs`, `video.rs`, and `ingest/{audio,image,video}.rs`
define `TranscriptionClient`/`VisionClient` traits, Available/Unavailable endpoints, degradation vocabulary, and
derived-Markdown writers — but only **fake test clients** exist, there is no HTTP transport, no ffmpeg, and
`crates/gwiki/src/ingest/file.rs:18` never routes audio/image/video into those orchestrators. This epic makes multimodal
ingest **actually work** (real transcription/translation, vision, chunking, ffmpeg) and, in the same pass, **cleans up
the AI interconnectivity and crate demarcation** across `gcore`, `gwiki`, `gcode`, `gloc`, and the Gobby daemon: one
shared transport-only `gobby_core::ai`, per-modality routing (daemon / direct / off), a fixed local-model budget, and
gcode's embeddings + optional LLM outlines routed through the same layer.

The throughline is audio-centric (transcription/translation is the production centerpiece) with frames co-equal, all
endpoints HTTP (no new Docker), and graceful degradation everywhere so gwiki/gcode work standalone, via a local LLM, via
a separate OpenAI-compatible endpoint, or via the daemon.

## C1: Constraints

`kind: framing`

- **Ownership split (coherent across gwiki *and* gcode)**: AI *config types*, *`AiContext` resolution*, the
  per-capability **routing decision**, and an always-compiled **concurrency limiter** live in `gobby_core` (`config` + a
  new `ai_context`, always-compiled, no `reqwest`); the **pure result/error data types** live in a separate
  always-compiled `gobby_core::ai_types` (Round 9 #2 — `ai_context` keeps routing/context/limiter, `ai_types` keeps data,
  cleaner than co-locating); the *HTTP transport mechanics*, the *probe-backed effective router*, and the *daemon
  capability probe* live in a feature-gated `gobby_core::ai`. The result types being always-compiled (not behind `ai`) is
  deliberate — it keeps consumer signatures stable in lean builds and removes the prior contradiction with A1 (Round 8
  #1). **gwiki and gcode are both thin consumers** of the same
  gcore context/router/results — gwiki adds orchestration/ffmpeg/media/trait-adapters/Markdown; gcode adds its
  `embed`/`text_generate` call sites. No AI routing, context, or result type is defined in gwiki or gcode (this is what
  prevents three divergent AI stacks — Round 5 #5). `gcore` never depends on `gwiki`/`gcode`/`gloc`.
- **No gwiki→gcode dependency**: preserved (existing `crate_has_no_gcode_dependency` test). gcode does **not** depend on
  the `gloc` binary; shared local-backend logic moves *down* into `gcore`. **Code→wiki honors this (Round 15)**: the
  codebase-documentation generator lives in **gcode** (it owns AST + the FalkorDB graph + `text_generate`) and emits
  Markdown; **gwiki ingests** that Markdown via its existing path — a file/CLI producer→consumer seam, no crate link
  (P9, §9.6).
- **Document ingestion (gwiki-only, behind a default-on `documents` feature; Round 15)**: PDF/Office/HTML/structured-text
  become derived Markdown. **PDF combines** the text layer (`pdf-extract`) with vision (`pdfium-render` page raster →
  `vision_extract` OCR + figure/chart descriptions) — not a fallback; Office via `calamine` + `zip`/`quick-xml`; HTML via
  the existing `scraper`; structured text (`csv/json/jsonl/xml/yaml/toml/log`) inlined as `Text`, size-capped. Lean
  `--no-default-features` degrades PDF/Office to store-as-asset; `gcore` is unaffected (P1 §1.3, P5 §5.4–5.6).
- **Feature isolation (honest)**: the goal is **no AI multipart/STT transport code or `reqwest/multipart` in lean
  builds**, not "no reqwest anywhere" — `gwiki` already links `reqwest` via its default-on `rustls` feature (semantic search,
  `crates/gwiki/Cargo.toml:14-15,19`) and `gcore` pulls `reqwest` under `qdrant`. gcore gains two features: **`local_backend = ["dep:ureq"]`**
  (the `Backend` data type is always-compiled, but the `ureq` GET probes — `detect_backend`/`validate_backend` — sit
  behind it, §8.1) and **`ai = ["dep:reqwest", "reqwest/multipart", "local_backend"]`** (HTTP transport + the
  probe-backed effective router; `ai` pulls `local_backend` for endpoint auto-discovery). **gloc enables only
  `gobby-core/local_backend`** so the tiny gloc binary gets discovery + `ureq` **without** dragging in `reqwest`/multipart
  (Round 10 #2). gwiki gains `ai = ["gobby-core/ai"]` with **`default = ["rustls", "ai", "documents"]`** (today `default = ["rustls"]` — the existing default-on `rustls` is preserved, not dropped — `crates/gwiki/Cargo.toml:14`)
  so normal and release builds carry AI while `--no-default-features` exercises the lean/degraded path. Adding the gcore
  `ai`/`local_backend` features is a deliberate public-boundary change — `crates/gcore/tests/public_boundary.rs` pins the
  exact manifest and must be updated in lockstep (P2.1); the bare baseline links **neither `reqwest` nor `ureq`**.
- **AI services need no Docker; the data hub is shared and gwiki-provisionable**: the *AI* layer is HTTP only (daemon /
  local server / cloud) and adds no containers or schema. Separately, the Postgres/FalkorDB/Qdrant *hub* can be
  provisioned by **either** `gcode setup --standalone` **or** a new `gwiki setup --standalone`, both through the shared
  `gobby_core::provisioning`. Whoever installs first stands up the shared hub (same `~/.gobby/services/docker-compose.yml`
  and merged `~/.gobby/gcore.yaml`); the other **detects and reuses** it (resolve-existing-DSN → else provision). Tables
  are namespaced (`gwiki_*` vs `code_*`) so an independent gcode install and an independent gwiki install coexist in one
  hub without collision (§8.4).
- **Subset/superset schema ownership + single-hub-with-adoption**: gcode (`code_*`) and gwiki (`gwiki_*`) each own a
  **disjoint subset** of the full Gobby schema; the daemon owns the **superset** (`config_store`, `projects`, memories,
  sessions, voice, …). A standalone hub is therefore a **partial** Gobby database — e.g. it has no `config_store` (the
  gcode standalone setup test asserts its absence). Invariant: **one shared hub**. Whichever order things install, later
  installs **adopt the existing hub in place** rather than provisioning a competing one — and a later `gobby install`
  **additively upgrades** the partial hub to the full schema, preserving existing `code_*`/`gwiki_*` data. CLIs never
  create or alter daemon-owned tables; the daemon's upgrade never drops CLI subset data (§8.5, §6.1).
- **Scope vs project_id**: gwiki ingest still requires a **resolved wiki scope** (`crates/gwiki/src/scope.rs:95`):
  global/default auto-resolves a project when `.gobby/project.json` is present, else errors unless `--topic` is given;
  project scope requires `.gobby/project.json`. Separately, AI calls **include project_id only when resolvable and never
  require it**, so transcription/vision/outline work in topic/global scopes.
- **Local-model budget**: at most **three** models ever — one embeddings, one STT (whisper), and **one multimodal model
  serving vision + text + translation + gcode outlines** (see B1). Vision/text/translation/outline default to the **same
  multimodal endpoint**.
- **No in-process inference / no auto model pulls**: every modality is a thin HTTP call to a model *server*; the CLI
  never loads or force-downloads a model (lifecycle is gloc's job, §P8).

## A1: Architecture & ownership boundary

`kind: framing`

- `gobby_core::config` + `gobby_core::ai_context` (always-compiled, no `reqwest`): `AiRouting { Auto, Daemon, Direct,
  Off }` plus a per-**capability** binding `CapabilityBinding { routing, transport, api_base, api_key, model, provider }`
  for `embed|audio_transcribe|audio_translate|vision_extract|text_generate` (A2; `audio_transcribe` carries
  `task`/`language`, `audio_translate` carries `target_lang`). **There is no `video` capability** — frame-sampling cadence
  is a gwiki ingest/media policy, not a gcore AI binding (Round 6 #8). Resolved via the existing private
  `resolve_setting`/`ConfigSource` (`config.rs:177`); an always-compiled **`AiContext`** (bindings + tuning + a **shared
  concurrency limiter** + optional `project_id`) and the per-capability, **config-only routing decision**
  `route(&AiContext, capability) -> AiRouting` (returns the *desired* routing; `Auto` stays `Auto` here — the
  probe-backed collapse to daemon/direct/off is the feature-gated effective router, Round 6 #1). The limiter type is
  always-compiled (so the no-`ai` build links) and lent to feature-gated clients as permits. `provider`/`project_id` are
  forwarded to the daemon registry (S1/P6).
- `gobby_core::ai_types` (always-compiled, no `reqwest` — Round 8 #1 / Round 9 #2): the **pure result/error data types**
  — `TranscriptionResult { segments:[{start_ms, end_ms, text}]` — **integer milliseconds, preserving `Eq`/`Hash`; wire
  JSON carries faster-whisper float seconds, converted on parse** (Round 6 #2) — `, source_language, language, model,
  task, target_language, translated }`, `VisionResult { description, ocr_text: Option<String>, model, metadata }` —
  **OCR stays a distinct field** (Round 6 #7) — a text result, and `AiError`. Plain structs, so consumer signatures and
  the C1 "result types live in gcore" guarantee hold without the `ai` feature; the feature-gated `ai` clients parse wire
  JSON *into* these types but never *define* them.
- `gobby_core::ai` (feature `ai`): blocking `reqwest` clients (direct + daemon), the **daemon capability probe**, the
  **probe-backed effective router** `effective_route(&AiContext, capability) -> AiRouting` that collapses `Auto` →
  daemon/direct/off (Round 6 #1), and the **transport mechanics** (multipart/JSON request building, wire-JSON parsing
  into the `ai_types` result types, retry/backoff); borrows the limiter. **No result/error *type definitions* (those live
  in always-compiled `ai_types`), no config logic beyond the probe-backed effective routing, no gwiki dependency.**
- `gwiki`: file classification/dispatch, `gwiki::media` (ffmpeg/ffprobe), chunk orchestration, thin trait adapters
  mapping gcore results into gwiki's traits, and all Markdown — **consuming** gcore's `AiContext`/router/clients (no
  routing logic of its own).
- `gcode`: the `embed` capability (existing OpenAI-compatible embeddings, vocabulary-aligned) and optional `text_generate`
  outlines, both via the **same** `gobby_core` `AiContext`/router/clients gwiki uses — no separate gcode AI stack
  (§8.2/§8.3).
- `gloc`: owns local-backend discovery (`detect_backend`) and local-model lifecycle/residency; its discovery primitives
  move into `gobby_core::local_backend` so gcore::ai can auto-discover a local endpoint — with the `Backend` data type
  always-compiled but the `ureq` probing gated behind a dedicated **`local_backend`** feature (`= ["dep:ureq"]`; `ai`
  pulls it, gloc enables it alone without `reqwest`), keeping the lean core HTTP-free (Round 8 #2 / Round 10 #2, §8.1).

## A2: Capability registry & repo boundary

`kind: framing`

The AI surface is modeled as **capabilities** (what is requested) over **transports** (how a provider connects), shared by
vocabulary across both repos:

- **Capabilities**: `embed`, `audio_transcribe`, `audio_translate`, `vision_extract`, `text_generate` (the daemon/runtime
  additionally owns `agent_spawn`, `web_chat`). Per-capability config keys: `ai.embeddings`, `ai.audio_transcribe`,
  `ai.audio_translate`, `ai.vision_extract`, `ai.text_generate`.
- **Transports**: `cli_adapter` (claude/codex as LLMProvider adapters, gemini/grok/qwen/droid as ACP adapters, **agy**
  pending — daemon-internal adapter styles), `openai_compatible_http` (local *or* cloud, distinguished only by
  `api_base`/`api_key`, **bound per capability** — the same schema gcode embeddings already use), `daemon_native`
  (WhisperSTT/faster-whisper).
- A provider advertises which capabilities it satisfies. Per-(capability, request) resolution: **explicit `provider`/`model`
  override → daemon feature default → configured local/openai-compatible fallback → off**. A provider that exists but
  cannot satisfy a capability returns a typed **capability error**, distinct from "provider not configured". **Exception
  (Round 6 #6)**: `embed`'s `Auto` never selects the daemon (its embeddings route is reindex-only, not arbitrary
  generation) — it resolves direct → local discovery → off until the daemon owns a real embedding-generation route.

**Repo boundary (explicit):**

- **gobby-cli (this epic)** owns: the capability *vocabulary* + the `openai_compatible_http` per-capability binding schema
  in `gobby_core::config`; `gobby_core::ai` direct/daemon transport; gwiki orchestration/routing/media; the gcode `embed`
  and `text_generate` consumers; gloc local discovery. It **consumes** daemon routes when routing=`daemon` and degrades
  otherwise. It does **not** define the daemon capability registry and does not own `cli_adapter`/runtime providers
  (gemini/grok/qwen/droid/**agy**).
- **gobby daemon (`gwiki-daemon-web.md`, separate repo)** owns: the **capability registry** (provider identity ↔
  capabilities), the D1–D3 routes + GET status probes, the `LLMService` refactor (selection out of the hardcoded
  factory; Claude/Codex become generation adapters, Gemini/Grok/Qwen/Droid gain one-shot `text_generate` via **ACP
  adapters**, **agy = Antigravity CLI** stays *unavailable until documented transport parity*), the
  `code_index/summarizer` migration onto `text_generate`, and D5 hub adoption. It establishes the registry **contract**;
  embeddings stay implemented in gcode, vocabulary-aligned only.
- **Shared contract** both sides honor: the capability names, the `openai_compatible_http` binding fields
  (`api_base`/`model`/`api_key`), the per-capability config keys, the route shapes (P6/D1–D4), the resolution order, and
  the capability-error semantics.

## B1: Memory & model-load discipline

`kind: framing`

Target footprint is **≤ 3 resident models** (one embeddings, one STT, one multimodal). Enforcement levers, implemented
inside the deliverables that follow: no in-process models; a **single shared concurrency limiter** owned by `AiContext`
(`ai.max_concurrency`, default 1–2) threaded into **every** call site — transcription, chunking, vision, text, and video
sequencing — so the cap is global, not per-call (chunks run sequentially/bounded, never fanned out); **sequence
modalities** in video ingest (transcription → frame vision → text) so one model class is hot at a time; **short
keep-alive** (`ai.keep_alive`, sent only to providers that accept it — never push Ollama-style fields to cloud OpenAI
endpoints unless config says so) so servers evict between runs; **prefer one shared endpoint** on constrained machines.
gcore::ai never pulls/force-loads; that is gloc's job.

## S1: Install & runtime scenarios

`kind: framing`

AI routing resolves per modality from `config_store` (DB present) → standalone `~/.gobby/gcore.yaml` → defaults (no
env-var layer — Round 11),
with no new provisioning *for AI*: **(a) daemon present** → `auto` probes and routes to the daemon (project_id from
daemon-written `.gobby/project.json`); **(b) standalone** → `auto` falls to the direct configured endpoint (local LLM or
cloud — both `direct`, distinguished only by `*_api_base`), else off/degraded; **(c) one CLI, no daemon** → identical to
(b), with shared `~/.gobby/gcore.yaml` letting one tool's AI config serve the other. The three user-facing options map to
the routing enum: **daemon** = `daemon`; **separate OpenAI-compatible endpoint** and **local LLM** = `direct`; **off**.
When `daemon` is chosen the CLI forwards the selected `model`/`provider` so the daemon honors the choice. In daemonless
standalone mode, authenticated direct endpoints store the optional API token directly in local user config as
`ai.<capability>.api_key`; `~/.gobby/gcore.yaml` is user-local and must not be committed. Daemon-attached config_store
rows may use `$secret:` references resolved by the daemon-backed source.

## R1: DAG / phase order

`kind: framing`

Hard prerequisite first, then transport, then the gwiki extraction modalities, then docs/CI, then the cross-crate
cleanup, then code→wiki. Edges: **P1 (dispatch + baseline, no-AI)** → **P2 (gcore::ai transport)** and **P3 (gwiki
routing + media)** → **P4 (audio STT/translation/chunking)** + **P5 (image/video/document extraction)** → **P6 (daemon
contract, optional)**, **P7 (docs/CI/release)**, **P8 (gcode + gloc demarcation, downstream)** → **P9 (codebase→wiki,
downstream)**. P1 is the blocker: until `ingest/file.rs` routes into the orchestrators, every other extraction
deliverable is decorative. **P8 and P9 are gated behind the P1–P7 MVP** — their deliverables `depends:` on P2+/§8.3 and
none gates the MVP, so the epic→subtask expansion schedules them *after* the multimodal MVP rather than in one train
(Round 8 #7); they stay in-epic (not file-split like the cross-repo P0E).

## P1: Ingest dispatch & no-AI baseline

`kind: framing`

**Goal**: route `ingest-file` into the audio/image/video orchestrators and establish always-compiled AI config/context
types, so the no-`ai` build works end-to-end with off/degraded modalities.

**Scope boundary (Round 6 #9)**: `ingest-file` is the multimodal entry point. The **inbox `collect` sweep**
(`collect.rs:133` `classify_inbox_item`) is **explicitly out of scope** for this epic — dropped audio/image files keep
being stored as raw, preserved, indexable assets without AI derivation (no transcription/vision). Routing collected media
through the orchestrators is a tracked follow-up, not part of this plan.

### 1.1 Add gcore AI capability config types and per-capability routing [category: code]

`kind: deliverable`

Target: `crates/gcore/src/config.rs`

Add always-compiled, `reqwest`-free config to `gobby_core::config`, modeled on `EmbeddingConfig`/`resolve_embedding_config`
(`config.rs:164`) but **resolving from the `ConfigSource` only, with no env-var layer (Round 11)**: AI config is read from
`config_store` (DB present) → standalone `~/.gobby/gcore.yaml` → defaults, **never** from `GOBBY_*` env vars (the legacy
`resolve_setting` env-first path is not used for AI config):

- `enum AiRouting { Auto, Daemon, Direct, Off }` with `FromStr` over `auto|daemon|direct|off` (the CLI-side view of
  transport selection; `direct` = `openai_compatible_http`, `daemon` = forward to the registry — A2).
- `struct CapabilityBinding { routing, transport, api_base, api_key, model, provider }` resolved **per capability**
  (`embed|audio_transcribe|audio_translate|vision_extract|text_generate`); `audio_transcribe` carries `task`/`language`,
  `audio_translate` carries `target_lang`; **no `video` field — frame interval is gwiki-owned (Round 6 #8, §1.3)**;
  `provider` is forwarded to the daemon (S1/P6); `struct AiTuning { max_concurrency: u8, keep_alive: Option<String> }`.
- `resolve_capability_routing(source, capability) -> AiRouting`: per-capability key → global `ai.routing` → `Auto`. **STT
  inheritance (Round 8 #4, fields enumerated Round 9 #3)**: when `audio_translate`'s own keys are unset, its
  `CapabilityBinding` inherits exactly these fields from `audio_transcribe` — **`routing`, `api_base`, `api_key`, `model`,
  `provider`, `transport`** (they share one whisper/STT server per B1) — while **`target_lang` stays local to
  `audio_translate`** (and `audio_transcribe`'s `task`/`language` stay local to it). So `--transcription-routing` / a
  single `ai.audio_transcribe.*` block configures both endpoints; any explicit `ai.audio_translate.<field>` overrides just
  that field.
- Config keys use the shared registry vocabulary (A2), resolved **only from `config_store`/`gcore.yaml` — no env vars
  (Round 11)**: `ai.routing` (global), `ai.<capability>.routing`, `ai.<capability>.{api_base,api_key,model,provider}`
  (e.g. `ai.audio_transcribe.*`, `ai.text_generate.*`, `ai.embeddings.*`), `ai.audio_transcribe.{task,language}`,
  `ai.audio_translate.target_lang`, `ai.max_concurrency`, `ai.keep_alive`. (Frame interval is **not** an `ai.*` key —
  it's the gwiki-owned `gwiki.ingest.video_frame_interval_seconds`, §1.3.) For standalone `gcore.yaml`,
  `ai.<capability>.api_key` is an optional plaintext local token; for attached `config_store`, the value may be a
  daemon-resolved `$secret:` reference.

**Acceptance:**

- 1.1.1 - `AiRouting` + per-capability `CapabilityBinding` and `resolve_capability_routing` exist and compile without any
  feature. file: `crates/gcore/src/config.rs`.
- 1.1.2 - Per-capability routing precedence (capability key → `ai.routing` → `Auto`) holds. test:
  `crates/gcore/src/config.rs::tests::ai_routing_per_capability_precedence`.
- 1.1.3 - AI keys resolve `config_store` (preferred) → `gcore.yaml` → defaults with **no env-var layer** (a `GOBBY_*`
  env var set for an AI key has no effect — Round 11); standalone `gcore.yaml` plaintext `api_key` values are honored,
  and attached-mode `$secret:` values resolve through the caller's `ConfigSource` when supported. test:
  `crates/gcore/src/config.rs::tests::ai_config_resolves_store_then_yaml_no_env`.
- 1.1.4 - `provider` and `audio_translate.target_lang` resolve with documented precedence; **no `ai.video.*` key exists**.
  test: `crates/gcore/src/config.rs::tests::provider_and_translation_fields_resolve`.
- 1.1.5 - `audio_translate` inherits `routing`/`api_base`/`api_key`/`model`/`provider`/`transport` from `audio_transcribe`
  when unset, keeps `target_lang` local, and an explicit `ai.audio_translate.<field>` overrides just that field (Round 8
  #4 / Round 9 #3). test: `crates/gcore/src/config.rs::tests::audio_translate_inherits_transcribe_binding`.

### 1.2 Add shared `gobby_core::ai_context` (AiContext, config source, router) [category: code] (depends: 1.1)

`kind: deliverable`

Target: `crates/gcore/src/ai_context.rs`, `crates/gcore/src/config.rs`

Centralize AI context **in gcore** so gwiki and gcode share one stack (Round 5 #5/#1). Add an always-compiled
`gobby_core::ai_context` with a **shared AI `ConfigSource`** resolving in both modes **with no env-var layer (Round 11)**:
`config_store` (when a DB DSN resolves) → standalone `~/.gobby/gcore.yaml` / global config → defaults. **Value resolution
stays caller-owned (Round 6 #5)**: `AiContext::resolve` consumes a caller-provided `ConfigSource`; plain values are valid,
and `$secret:` Fernet expansion is supported only when the caller/source can resolve it (**no `${VAR}` env expansion for
AI config** — Round 11). gcode supplies `secrets::resolve_config_value` (`config/services.rs:25`, Fernet) for
daemon-backed sources; daemonless standalone `gcore.yaml` uses the literal local value. The Fernet logic does **not** move
into gcore. **A reachable Postgres whose `config_store` table is absent (a partial standalone hub, C1) is not an error** —
the store layer is skipped and resolution falls through to `gcore.yaml`/defaults (the DB `ConfigSource` is
`#[cfg(feature = "postgres")]`; the `gcore.yaml`/defaults resolution is always-compiled). Resolve an
always-compiled `AiContext { bindings: per-capability CapabilityBinding, tuning, limiter: shared always-compiled
concurrency limiter (B1), project_id: Option<String> }`, plus the per-capability **config-only**
`route(&AiContext, capability) -> AiRouting` decision (returns the *desired* routing; `Auto` is left as `Auto` — the
probe-backed collapse lives in the feature-gated `gobby_core::ai::effective_route`, Round 6 #1). **`project_id` is
caller-supplied, not cwd-derived (Round 8 #6)**: `AiContext::resolve` takes `project_id: Option<String>` from the caller
so each tool sources it from the correct authority — **gwiki passes the *resolved `ScopeIdentity`*'s project_id**
(project scope → that id; topic/global → `None`), **never** a cwd walk, since topic/global ingest legitimately runs
outside `.gobby/project.json` and must not forward a stray cwd project; **gcode** passes its own cwd-rooted
`gobby_core::project` resolution. The always-`None`-when-unresolvable rule (C1) is preserved; only the *authority* is the
caller's. gwiki and gcode each construct one `AiContext`; neither defines its own context or router. (gwiki's existing DB-DSN discovery `support/env.rs:1` — used only to *locate the hub*, not to source AI config — and its search-only Postgres `ConfigSource`
`commands/search.rs:58` fold into this shared source.)

**Acceptance:**

- 1.2.1 - `AiContext`, the shared config source, and `route()` compile with no `ai` feature and resolve in DB and no-DB
  modes. file: `crates/gcore/src/ai_context.rs`.
- 1.2.2 - No-DB resolution reads standalone `gcore.yaml` (no env layer for AI config — Round 11); DB mode also reads
  `config_store`. test: `crates/gcore/src/ai_context.rs::tests::resolves_in_db_and_no_db_modes`.
- 1.2.3 - `project_id` is caller-supplied (`AiContext::resolve(project_id, …)`): a topic/global wiki scope yields `None`
  even when cwd sits inside a `.gobby/project.json`, and a project scope yields its id — never a cwd-derived value (Round
  8 #6). test: `crates/gcore/src/ai_context.rs::tests::project_id_is_caller_supplied`.
- 1.2.4 - A reachable Postgres lacking the `config_store` table resolves via `gcore.yaml`/defaults without erroring.
  test: `crates/gcore/src/ai_context.rs::tests::db_without_config_store_falls_through`.
- 1.2.5 - `route(capability)` returns the config-only desired routing (forced `daemon`/`direct`/`off` honored, else
  `Auto`); forced modes and `--no-ai` override all per-capability config. test:
  `crates/gcore/src/ai_context.rs::tests::forced_routing_and_no_ai_override`.

### 1.3 Dispatch ingest-file to orchestrators and add CLI flags [category: code] (depends: 1.2)

`kind: deliverable`

Target: `crates/gwiki/src/ingest/file.rs`, `crates/gwiki/src/main.rs`, `crates/gwiki/src/lib.rs`, `crates/gwiki/src/sources.rs`

Extend `detect_source_kind` (`file.rs:108`) to map audio (`mp3,wav,m4a,flac,ogg,aac,opus`) → `SourceKind::Audio` and
image (`png,jpg,jpeg,gif,webp,bmp,tiff`) → `SourceKind::Image` (both variants already exist in `sources.rs:15`; video
already maps). **Also map documents (Round 15)**: `docx,xlsx,xls,ods,pptx` → new `SourceKind::Office`; `html,htm` → new
`SourceKind::Html`; structured text `csv,json,jsonl,xml,yaml,yml,toml,log` → `SourceKind::Text` (inlined, size-capped —
> ~256 KB stores as asset); `pdf` already → `SourceKind::Pdf`. `Pdf`/`Office`/`Html` dispatch to the document
orchestrator (P5 §5.4–5.6) — HTML via the always-linked `scraper`; without the `documents` feature `Pdf`/`Office`
degrade to store-as-asset. In `ingest_path` (`file.rs:18`), add `scope: &ScopeIdentity` and an `AiContext` and **branch by kind at
the top of the function, before building the generic `SourceDraft`/calling `SourceManifest::register` (`file.rs:47`)**:
audio/image/video delegate **entirely** to `ingest_audio_with_transcription` / `ingest_image` / `ingest_video`, each of
which already does its **own** `SourceManifest::register` and writes its own raw doc — so
the generic register/asset/markdown path runs **only** for the non-media fallthrough (`Pdf`/`Markdown`/`Text`/`File`).
This avoids double-registration and the wrong-raw-doc bug a register-then-branch ordering would create (Round 8 #3).
Media orchestrators return via the existing `From<…> for IngestResult` impls (in the audio/video ingest modules) with
`.into()`. With routing `Off`/unconfigured every modality resolves to its `Unavailable` endpoint (current behavior) —
assets preserved, no-AI build works. Add flags to **both** `CliCommand::IngestFile` and the library `Command::IngestFile`
variant (mapped at `main.rs:208`), resolved in the `run_ingest_file` handler: `--no-ai`, `--translate`,
`--target-lang <lang>`, `--video-frame-interval <seconds>` (`0` disables frames),
`--transcription-routing`/`--vision-routing`/`--text-routing`. **`--transcription-routing` governs *both* STT
capabilities — `audio_transcribe` and `audio_translate` (Round 8 #4)** — since they hit the same whisper/STT server (B1's
one-STT budget); there is no separate `--translation-routing` flag. At config granularity the two bindings remain
distinct (`ai.audio_transcribe.*` / `ai.audio_translate.*`), and **`audio_translate`'s binding inherits
`audio_transcribe`'s endpoint/routing when its own keys are unset**, so the common single-STT case needs no duplicate
config.
**Frame interval is a gwiki-owned media policy (Round 6 #8)**, resolved by gwiki — not gcore's AI registry — with
precedence **CLI `--video-frame-interval` > `config_store` > `gcore.yaml` > default** (no env layer — Round 11) under the
key `gwiki.ingest.video_frame_interval_seconds` (default 5).

**Acceptance:**

- 1.3.1 - `detect_source_kind` maps audio/image extensions to `SourceKind::Audio`/`Image`. test:
  `crates/gwiki/src/ingest/file.rs::tests::detects_audio_and_image_extensions`.
- 1.3.2 - `ingest_path` dispatches `.mp3`/`.png`/`.mp4` to the audio/image/video orchestrators and returns `IngestResult`.
  test: `crates/gwiki/src/ingest/file.rs::tests::dispatches_media_to_orchestrators`.
- 1.3.3 - With `--no-ai`/unconfigured routing, dispatch preserves the raw asset and writes degraded derived Markdown.
  test: `crates/gwiki/src/ingest/file.rs::tests::no_ai_dispatch_degrades`.
- 1.3.4 - Media dispatch registers each source **exactly once** — a `.mp3` ingest produces a single `SourceManifest`
  entry (the orchestrator's), never a generic-plus-media double entry (Round 8 #3). test:
  `crates/gwiki/src/ingest/file.rs::tests::media_dispatch_registers_once`.
- 1.3.5 - AI/translation/routing flags exist on `CliCommand::IngestFile` and the library `Command::IngestFile`, and
  `--transcription-routing` sets both `audio_transcribe` and `audio_translate` routing (Round 8 #4). file:
  `crates/gwiki/src/main.rs`.
- 1.3.6 - `detect_source_kind` maps document/structured-text/html extensions and `ingest_path` dispatches `.pdf`/`.docx`/
  `.html` to the document orchestrator while `.csv`/`.json` inline as size-capped `Text` (Round 15). test:
  `crates/gwiki/src/ingest/file.rs::tests::detects_and_dispatches_documents`.
- 1.3.7 - `SourceKind::Office` and `SourceKind::Html` variants exist with `Display`. file: `crates/gwiki/src/sources.rs`.

## P2: gcore::ai transport (feature-gated)

`kind: framing`

**Goal**: blocking OpenAI-compatible + daemon clients with numeric-timed results, retry/backoff, and a concurrency cap —
transport only, no routing.

### 2.1 Add gcore `ai` feature and transport skeleton [category: code] (depends: P1)

`kind: deliverable`

Target: `crates/gcore/Cargo.toml`, `crates/gcore/src/lib.rs`, `crates/gcore/src/ai_types.rs`, `crates/gcore/src/ai/mod.rs`

Add features `local_backend = ["dep:ureq"]` and `ai = ["dep:reqwest", "reqwest/multipart", "local_backend"]` (base
`reqwest` and `ureq` are both optional; base `reqwest` also lacks `multipart`), plus `#[cfg(feature = "ai")] pub mod ai;`
(and the `local_backend`-gated probing of §8.1). `ai` pulls `local_backend` so endpoint auto-discovery is available
whenever transport is. **Adding the features changes the locked public boundary** — update
`crates/gcore/tests/public_boundary.rs` (which pins the exact manifest incl. the `full`/feature lines) in the same
change. **The result/error *types* are defined in the always-compiled `gobby_core::ai_types` (Round 8 #1 / Round 9 #2),
not here** — `TranscriptionResult` with **integer-millisecond** `{start_ms, end_ms, text}` segments (preserves
`Eq`/`Hash`; the wire JSON carries faster-whisper float seconds and is converted to ms on parse — Round 6 #2),
`source_language`/`language`/`model`/`task`/`target_language`/`translated`; `VisionResult { description, ocr_text:
Option<String>, model, metadata }` — **OCR stays a distinct field** (verbatim in-image text is a high-value, separately
searchable retrieval signal; reverses Round 5 #4 — Round 6 #7); a text result; and `AiError`. This module (`ai/mod.rs`)
adds only the **transport mechanics over those types**: request building (multipart/JSON), wire-JSON parsing into the
`ai_types` result types, and a **retry + rate-limit backoff** wrapper. The clients **borrow the always-compiled limiter** from `AiContext` (the limiter type lives
in `gobby_core::ai_context`, not here, so the no-`ai` build links — Round 5 #1).
**Concrete defaults** (no implementation leaks): `max_concurrency = 1`; per-request timeout 60 s (text/vision) / 120 s
(STT chunk). **Backoff is exponential with jitter** on connect/timeout/5xx **and HTTP 429** — **honor the `Retry-After`
header when present**, else 250 ms → 500 ms, **at most 2 retries (3 attempts total)** with a hard ceiling (no infinite
waits — Round 6 #10, matching acceptance 2.1.2). Rate-limit (429) backoff is the path that matters for **non-local
OpenAI-compatible (cloud) APIs**; local servers rarely throttle but the wrapper is uniform. The `max_concurrency` limiter
is the first line of defense against tripping cloud rate limits.

**Acceptance:**

- 2.1.1 - `ai`/`local_backend` features compile, and the **bare baseline links neither `reqwest` nor `ureq`**:
  `cargo tree -p gobby-core -i reqwest` shows `reqwest` only under `ai`/`qdrant`, and `cargo tree -p gobby-core -i ureq`
  shows `ureq` only under `local_backend`/`ai` (Round 10 #2). file: `crates/gcore/Cargo.toml`.
- 2.1.1a - The `gobby_core::ai_types` result/error types compile with **no** feature (no `reqwest`/`ureq`), and the
  feature-gated `ai` clients parse wire JSON into them without redefining them (Round 9 #2). file:
  `crates/gcore/src/ai_types.rs`.
- 2.1.1b - `ai_types::AiError` is **transport-neutral**: it contains no `reqwest::Error`/`ureq::Error` (or any
  feature-gated transport type) in its public fields, carrying instead structured transport-neutral data — e.g.
  `status: Option<u16>`, `body`/`source` as `String`, and typed variants (capability error, not-configured, transport
  failure, parse failure). So no feature leaks through the always-compiled error type (Round 10 #3). test:
  `crates/gcore/src/ai_types.rs::tests::ai_error_is_transport_neutral`.
- 2.1.2 - Retry wrapper retries transient failures at most twice then surfaces a typed `AiError`. test:
  `crates/gcore/src/ai/mod.rs::tests::retry_caps_at_two`.
- 2.1.3 - The shared limiter (in `ai_context`, borrowed by clients) caps in-flight calls at `max_concurrency`. test:
  `crates/gcore/src/ai_context.rs::tests::concurrency_cap_enforced`.
- 2.1.4 - `crates/gcore/tests/public_boundary.rs` is updated for the new `ai` feature and passes. test:
  `crates/gcore/tests/public_boundary.rs::cargo_features_define_public_boundary`.

### 2.2 Direct transcription/translation client [category: code] (depends: 2.1)

`kind: deliverable`

Target: `crates/gcore/src/ai/transcription.rs`

`transcribe(cfg, bytes, file_name, mime, task, language)`: multipart POST to `/v1/audio/transcriptions` (verbatim) or
`/v1/audio/translations` (whisper→English), `response_format=verbose_json`, an optional `language` form field when the
hint is set (Round 5), **multipart `file` part carries the real filename+extension** (many STT servers key the decoder
off it). Parse `segments[]` (float-second `start`/`end`) → **integer-ms** `{start_ms, end_ms, text}` (Round 6 #2),
detected `language`. Bearer auth like `search/semantic.rs:190`.

**Acceptance:**

- 2.2.1 - Builds a multipart request with filename + `task`-selected endpoint and parses verbose_json segments. test:
  `crates/gcore/src/ai/transcription.rs::tests::builds_multipart_and_parses_segments`.
- 2.2.2 - A loopback server (`std::net::TcpListener` on `127.0.0.1:0`) receives the multipart `file` part with the
  declared filename and bearer header. test: `crates/gcore/src/ai/transcription.rs::tests::wire_multipart_filename_and_auth`.

### 2.3 Direct vision and text clients [category: code] (depends: 2.1)

`kind: deliverable`

Target: `crates/gcore/src/ai/vision.rs`, `crates/gcore/src/ai/text.rs`

`describe_image(cfg, bytes, mime)` → `/v1/chat/completions` with an `image_url` data-URI message, prompting for a small
**structured `{description, ocr_text}`** (JSON or two delimited sections); parse both, and on parse failure or a
describe-only model treat the whole response as `description` with `ocr_text = None` (Round 6 #7). `generate_text(cfg,
prompt, system?)` → `/v1/chat/completions`. Both bearer-auth, retry-wrapped.

**Acceptance:**

- 2.3.1 - Vision client sends an `image_url` data-URI chat request and parses `{description, ocr_text}`, falling back to
  description-only (`ocr_text = None`) when the model returns prose. test:
  `crates/gcore/src/ai/vision.rs::tests::sends_image_url_and_parses`.
- 2.3.2 - Text client sends a chat completion and returns content. test:
  `crates/gcore/src/ai/text.rs::tests::generates_text`.

### 2.4 Daemon clients with back-compat mapping [category: code] (depends: 2.2, 2.3)

`kind: deliverable`

Target: `crates/gcore/src/ai/daemon.rs`

`transcribe_via_daemon`/`describe_image_via_daemon`/`generate_via_daemon` POST to the daemon routes (P6), taking the
daemon URL from `gobby_core::daemon_url` and **authenticating with `X-Gobby-Local-Token` read from
`~/.gobby/local_cli_token`** (the same broker policy gcode uses, `db.rs:15,233`). Audio/image use `multipart/form-data`
with a `file` part (real filename); text uses a JSON body. **`/api/voice/transcribe` carries the daemon's current
multipart fields (Round 9 #1, wire values corrected Round 10)**: `capability`, `provider`, `model`, `language`, and
`prompt` (optional bias) alongside `file` — these select the daemon-side `voice.openai_compatible_audio` binding. **The
`capability` field carries the `AICapability` enum *value* — `audio_transcribe` or `audio_translate` (defaulting to
`audio_transcribe`), not `transcribe`/`translate`** — which is distinct from the faster-whisper `task` (`transcribe`/
`translate`) the daemon returns; gcore maps its requested capability to this field directly. All forward `provider`/`model`
and include `project_id` **only when resolvable** (C1;
omitted otherwise). **Back-compat**: if `/api/voice/transcribe` returns legacy `{text}`-only, synthesize one segment at
`start_ms = 0`, leaving `source_language`/`model`/`task` defaulted.

**Acceptance:**

- 2.4.1 - Daemon transcribe maps a legacy `{text}` body to a single zero-offset (`start_ms = 0`) segment. test:
  `crates/gcore/src/ai/daemon.rs::tests::legacy_text_maps_to_single_segment`.
- 2.4.2 - Daemon clients forward `provider`/`model` and include `project_id` only when resolvable. test:
  `crates/gcore/src/ai/daemon.rs::tests::forwards_provider_model_and_optional_project_id`.
- 2.4.3 - Daemon requests send `X-Gobby-Local-Token` from `~/.gobby/local_cli_token` and use a multipart `file` part for
  audio/image. test: `crates/gcore/src/ai/daemon.rs::tests::sends_local_token_and_multipart`.
- 2.4.4 - The voice multipart request includes the daemon's `capability`/`provider`/`model`/`language`/`prompt` fields,
  with `capability` set to the `AICapability` value `audio_transcribe`|`audio_translate` (default `audio_transcribe`),
  **not** `transcribe`/`translate` (Round 9 #1 / Round 10). test:
  `crates/gcore/src/ai/daemon.rs::tests::voice_multipart_carries_capability_fields`.

## P3: gwiki routing decision, adapters & media helpers

`kind: framing`

**Goal**: turn resolved routing into production trait clients, fix the daemon vision probe, and add real ffmpeg/ffprobe
media helpers.

### 3.1 Add gwiki thin trait adapters over the shared gcore router [category: code] (depends: P2)

`kind: deliverable`

Target: `crates/gwiki/src/ai/clients.rs`, `crates/gwiki/src/transcribe.rs`

`ProductionTranscriptionClient`/`ProductionVisionClient` implement gwiki's `TranscriptionClient`/`VisionClient` by
delegating to the `gobby_core::ai` clients selected by the **shared gcore effective router**
(`gobby_core::ai::effective_route`, which collapses the config-only `ai_context::route` `Auto` via the probe — §1.2,
Round 6 #1) — gwiki holds **no routing logic of its own**. `Auto` resolves daemon (capability probe present, 750 ms) →
direct (endpoint configured) → off; `daemon`/`direct`/`off` force it; `direct` covers cloud or local (api_base only);
`daemon` forwards `provider`/`model`/`project_id`. **Numeric timestamps (Round 5 #2 / Round 6 #2)**: change gwiki's
`TranscriptSegment` (`transcribe.rs:8`) to **integer-millisecond** `start_ms`/`end_ms` (`u64`, + `text`) — preserving the
existing `#[derive(Eq)]` chain (`TranscriptSegment`/`TranscriptionOutput`/`VideoSnapshot`/`AlignedVideoSegment`) that an
`f64` would break — so chunking can offset/dedup; format to the `[hh:mm:ss]` string **only in Markdown rendering**, never
in the model. `align_transcript_and_frames` (`video.rs:81`) currently parses `segment.timestamp` strings
(`video.rs:102,118`) — it now reads `start_ms` numerically and buckets on integer seconds, with no string parsing.

**Acceptance:**

- 3.1.1 - Production clients implement the gwiki traits over the gcore effective router; `TranscriptSegment` holds
  integer-ms `start_ms`/`end_ms` (`Eq` preserved), formatted to strings only in Markdown. file:
  `crates/gwiki/src/ai/clients.rs`.
- 3.1.2 - The shared gcore effective router (`gobby_core::ai::effective_route`) resolves `Auto` daemon→direct→off per
  capability against the probe — one router, used by both gwiki and gcode. test:
  `crates/gcore/src/ai/mod.rs::tests::effective_route_auto_falls_through_per_capability`.
- 3.1.3 - `align_transcript_and_frames` aligns on numeric `start_ms` (no string-timestamp parsing) and still produces the
  transcript-only and frame-aligned groupings. test: `crates/gwiki/src/video.rs::tests::aligns_on_numeric_start_ms`.

### 3.2 Add gwiki::media ffmpeg/ffprobe helpers [category: code] (depends: P1)

`kind: deliverable`

Target: `crates/gwiki/src/media.rs`

Path-based, temp-file helpers (probe PATH for `ffmpeg`/`ffprobe`; missing → `None`/error so callers degrade and preserve
assets): `probe_duration(path) -> Option<u32>`; `extract_audio_file(video) -> NamedTempFile`;
`sample_frame_images(video, interval) -> Vec<(start_ms: u64, NamedTempFile)>`;
`split_audio_file(audio, window) -> Vec<Chunk { start_ms: u64, path: NamedTempFile }>` (integer-ms offsets, Round 6 #2).
**Temp lifecycle**: all temp outputs are RAII (`NamedTempFile`/`TempPath`) and removed on drop/error/panic; the raw asset
is written to `raw/assets/` first and never tied to a temp lifetime.

**Acceptance:**

- 3.2.1 - Helpers are path-based, return RAII temp files, and report unavailability when ffmpeg/ffprobe are absent. file:
  `crates/gwiki/src/media.rs`.
- 3.2.2 - Temp outputs are cleaned up on a mid-run error while the raw asset survives. test:
  `crates/gwiki/src/media.rs::tests::temp_files_cleaned_asset_survives`.

### 3.3 Repoint the daemon vision capability probe to a GET status route [category: code] (depends: 3.1)

`kind: deliverable`

Target: `crates/gcore/src/ai/probe.rs`, `crates/gwiki/src/daemon.rs`

The capability probe **moves into `gobby_core::ai` (shared by gwiki and gcode, Round 5 #5)**; gwiki's existing GET-only
probe (`daemon.rs:86`) and the stale `VISION` contract (`daemon.rs:125`, which probes upload-only
`POST /api/chat/attachments`) fold into it. Probe targets: `vision_extract` → new **GET `/api/llm/vision/status`**
(extraction is `POST /api/llm/vision/extract`, P6); `audio_transcribe`/`audio_translate` → `GET /api/voice/status`;
`text_generate` → `GET /api/llm/status`. **The probe asserts capability-level truth, not bare HTTP 200 (Round 8 #5)**:
because `audio_transcribe` and `audio_translate` share `GET /api/voice/status`, a 200 there does **not** prove translate
support — a daemon may transcribe but not translate. So the probe **parses the status body's advertised capability flags**
and routes a capability to the daemon **only when that capability is advertised present**; an advertised-absent or
unparseable capability degrades to direct/off **even if the endpoint is reachable**. **For audio, the truth source is the
daemon's `voice.openai_compatible_audio` binding flags surfaced on `/api/voice/status` (Round 9 #1)** —
`transcription_enabled` gates `audio_transcribe` and `translation_enabled` gates `audio_translate` (the binding also
carries `provider`/`url`/`model`/optional `api_key`/`timeout_seconds`). **Truth-source precedence (Round 9 #4)**: the
per-capability **GET status route is checked first** (cheap availability — including these audio flags); `GET
/api/providers/models` is consulted **only for provider/model discovery**, not for availability. Until a status route
exists that capability degrades; `/api/chat/attachments` is never a description/OCR fallback.

**Acceptance:**

- 3.3.1 - The shared gcore probe maps `vision_extract`→`/api/llm/vision/status`, audio→`/api/voice/status`,
  `text_generate`→`/api/llm/status`; absence → degraded, not routed. test:
  `crates/gcore/src/ai/probe.rs::tests::capability_status_routes`.
- 3.3.2 - `/api/chat/attachments` is no longer treated as a vision-extraction capability. test:
  `crates/gcore/src/ai/probe.rs::tests::attachments_not_vision_extraction`.
- 3.3.3 - The probe reads capability-level advertisement: a `/api/voice/status` body with `transcription_enabled=true`,
  `translation_enabled=false` routes `audio_transcribe` to the daemon while degrading `audio_translate`, despite the
  shared 200 (Round 8 #5 / Round 9 #1). test: `crates/gcore/src/ai/probe.rs::tests::status_body_capability_truth`.
- 3.3.4 - Availability is decided by the GET status route, not `/api/providers/models` — the latter is read only for
  provider/model discovery (Round 9 #4). test: `crates/gcore/src/ai/probe.rs::tests::status_route_is_availability_truth`.

## P4: Audio transcription, translation & chunking

`kind: framing`

**Goal**: make audio the production centerpiece — real transcription, language auto-detect, configurable translation, and
deterministic long-media chunking.

### 4.1 Wire audio ingest to production transcription and extend output [category: code] (depends: 3.1, 3.2)

`kind: deliverable`

Target: `crates/gwiki/src/ingest/audio.rs`, `crates/gwiki/src/transcribe.rs`

Build the production `TranscriptionEndpoint` from resolved routing instead of the hardcoded `Unavailable` (`audio.rs:45`),
keeping the `_with_transcription` seam for fake-client tests. Extend `TranscriptionOutput` (`transcribe.rs:13`) with
`source_language`, `task`, `target_language`, `translated`, and surface them in `render_audio_transcript_markdown`
frontmatter (`transcription_task`, `transcription_source_language`, `transcription_target_language`, `translated`).

**Acceptance:**

- 4.1.1 - Audio ingest uses the production endpoint when routing is configured and writes the new frontmatter fields.
  test: `crates/gwiki/src/ingest/audio.rs::tests::production_transcription_writes_fields`.
- 4.1.2 - Unconfigured/`off` routing preserves the asset and writes degraded transcript Markdown. test:
  `crates/gwiki/src/ingest/audio.rs::tests::off_routing_degrades`.

### 4.2 Add language auto-detect and translation precedence [category: code] (depends: 4.1)

`kind: deliverable`

Target: `crates/gwiki/src/ai/translate.rs`

Auto-detect is default (omit `language` → whisper detects → record `source_language`); `ai.audio_transcribe.language` is
an optional hint. **Exact algorithm** (resolves the auto-detect ordering problem — the source is unknown until after a
pass):

1. **No translation requested** → transcribe (auto-detect), record `source_language`, `translated=false`.
2. **Translate-to-English** (`audio_translate.target_lang` unset/`en`) → call `/v1/audio/translations` in one pass;
   whisper self-detects the source and always emits English, so **no pre-pass source check is needed** (English source →
   output unchanged). Record detected `source_language`, `translated=true`.
3. **Translate to a non-English target** → transcribe first (auto-detect `source_language`); then if
   `source_language == target_lang` → skip (`translated=false`); else **segment-wise bounded-chunk LLM translation
   preserving each timestamp** (never one `generate_text(full_transcript)`). The per-chunk LLM call requests **indexed
   JSON** (`[{i, text}]`) so segment alignment is exact, with a validation fallback (re-request, else per-segment calls)
   on index/length mismatch (Round 5).
4. **Hint shortcut** — a supplied `language` hint is passed through as the known source, avoiding a detection pass.

If `/v1/audio/translations` is unsupported and a text LLM is configured, step 2 falls back to transcribe + segment-wise
LLM translation to English.

**Acceptance:**

- 4.2.1 - Source==target skips translation; non-English target translates per segment preserving timestamps. test:
  `crates/gwiki/src/ai/translate.rs::tests::precedence_and_segment_wise`.
- 4.2.2 - Unsupported `/v1/audio/translations` falls back to LLM translation when a text LLM is configured. test:
  `crates/gwiki/src/ai/translate.rs::tests::translations_unsupported_fallback`.
- 4.2.3 - Translate-to-English uses `/v1/audio/translations` in one pass with no pre-transcription source check; a
  non-English target transcribes first then applies the `source==target` skip. test:
  `crates/gwiki/src/ai/translate.rs::tests::english_one_pass_vs_target_first`.

### 4.3 Add deterministic long-media chunking [category: code] (depends: 4.1, 3.2)

`kind: deliverable`

Target: `crates/gwiki/src/ai/chunk.rs`

`gwiki::media::split_audio_file` decodes to a **fixed transcription codec — 16 kHz mono 16-bit PCM WAV** (ffmpeg
`-ar 16000 -ac 1 -c:a pcm_s16le`), giving ~32 KB/s so chunk-bytes math is deterministic; window = min(duration to reach
~24 MB ≈ ~12.5 min at 16 kHz mono, default 10 min), with a **~2–5 s overlap** dedup'd on stitch. Transcribe chunks
**sequentially/bounded by the shared limiter (`ai.max_concurrency`, B1)**, offset each chunk's segment `start_ms`/`end_ms`
by the chunk start (ms), concatenate ordered. **ffmpeg/ffprobe are required only for chunking and video extraction** — **short
audio already under the byte cap is sent verbatim, bypassing ffmpeg/ffprobe entirely** (so no-ffmpeg + short audio still
transcribes; unknown duration also single-shots when under the cap). Chunking returns a partial-aware aggregate
`ChunkedTranscription { segments, completed_ranges, missing_ranges, partial }` — the per-chunk `TranscriptionClient`
stays all-or-error (`transcribe.rs:26`); the aggregate records mid-run provider failures for P5.3.
Window/overlap/max-bytes are named constants.

**Acceptance:**

- 4.3.1 - Splitting normalizes to 16 kHz mono PCM WAV and keeps each chunk under the byte limit. test:
  `crates/gwiki/src/ai/chunk.rs::tests::chunks_under_limit_fixed_codec`.
- 4.3.2 - Concatenated segment timestamps are offset, ordered, and overlap-dedup'd. test:
  `crates/gwiki/src/ai/chunk.rs::tests::offsets_and_dedups`.
- 4.3.3 - Short audio under the cap (and unknown-duration audio) transcribes single-shot **without invoking
  ffmpeg/ffprobe**. test: `crates/gwiki/src/ai/chunk.rs::tests::short_audio_bypasses_ffmpeg`.
- 4.3.4 - A mid-run chunk failure yields `ChunkedTranscription { partial: true }` with completed chunks kept and missing
  ranges recorded. test: `crates/gwiki/src/ai/chunk.rs::tests::partial_chunk_outcome`.

## P5: Image, video, and document extraction

`kind: framing`

**Goal**: production vision for images, audio-centric video with co-equal real frames, and document extraction (PDF
combining text layer + vision, Office, HTML, structured text) — all to derived Markdown with graceful degradation.

### 5.1 Wire image ingest to production vision [category: code] (depends: 3.1)

`kind: deliverable`

Target: `crates/gwiki/src/ingest/image.rs`

Build the production `VisionEndpoint` from the shared router (§1.2/§3.1); on success write the `description`, the
**distinct `ocr_text`** (mapped from the always-compiled `gobby_core::ai_types::VisionResult.ocr_text` — Round 9 #2 —
into gwiki's existing `VisionExtraction.ocr_text`, `vision.rs:10`, rendered as the existing `## OCR Text` section), and `model`/`metadata`
frontmatter; else preserve the asset and emit vision degradation (existing `vision.rs` writer). gwiki's
`VisionExtraction`/`## OCR Text` renderer stay as-is — the thin adapter just fills `ocr_text` (Round 6 #7).

**Acceptance:**

- 5.1.1 - Image ingest calls the production vision client and writes the `description`, the `## OCR Text` section when
  `ocr_text` is present, and the model frontmatter. test:
  `crates/gwiki/src/ingest/image.rs::tests::production_vision_writes_description_and_ocr`.

### 5.2 Wire video to audio-first transcript plus real frames [category: code] (depends: 4.1, 4.3, 3.2, 5.1)

`kind: deliverable`

Target: `crates/gwiki/src/ingest/video.rs`, `crates/gwiki/src/video.rs`

Add real frame-image temp paths to `VideoSnapshot` (currently only `frame_descriptions`/`transcript_segments`,
`video.rs:9`). In `ingest_video` (`video.rs:41`): `extract_audio_file` → chunked transcribe/translate (P4) → real
`transcript_segments`; `sample_frame_images` at the **gwiki-owned frame interval** (resolved CLI > `config_store` >
`gcore.yaml` > default, `gwiki.ingest.video_frame_interval_seconds`; Round 6 #8 / no env, Round 11) → `describe_image` per frame → real
`frame_descriptions`; then reuse `align_transcript_and_frames` (now numeric `start_ms`, Round 6 #2) +
`write_video_derived_markdown`. **Run modalities sequentially** (transcription → frame vision) per B1. `sample_frames` coerces interval `0`→`1`, so **branch explicitly**:
`--video-frame-interval 0` skips frame sampling entirely (audio-only video).

**Acceptance:**

- 5.2.1 - `VideoSnapshot` carries real frame-image temp paths and video ingest produces transcript + frame descriptions
  from ffmpeg output. test: `crates/gwiki/src/ingest/video.rs::tests::video_produces_transcript_and_frames`.
- 5.2.2 - `--video-frame-interval 0` yields an audio-only transcript video doc (no frames). test:
  `crates/gwiki/src/ingest/video.rs::tests::frame_interval_zero_disables_frames`.

### 5.3 Add partial-video degradation matrix and media metadata [category: code] (depends: 5.2)

`kind: deliverable`

Target: `crates/gwiki/src/video.rs`

Each failure mode preserves the raw asset and writes a valid derived doc: no ffmpeg → raw + `media_degradation`; audio OK
/ frames fail → transcript-only (existing transcript-only fallback in `align_transcript_and_frames`); frames OK / STT
fail → frame-timeline-only + transcription degradation; provider fails mid-chunk → consume the `ChunkedTranscription`
partial aggregate (§4.3): keep completed chunks, mark `partial`, record the missing window range(s). Media degradation
metadata always records `file_size_bytes` and (when ffprobe succeeds) `duration_seconds`.

**Acceptance:**

- 5.3.1 - Each partial-failure mode writes the specified doc and preserves the asset. test:
  `crates/gwiki/src/video.rs::tests::partial_failure_matrix`.
- 5.3.2 - Degradation metadata includes `file_size_bytes` and `duration_seconds`. test:
  `crates/gwiki/src/video.rs::tests::degradation_metadata_has_size_and_duration`.

### 5.4 Office, HTML, and structured-text document extraction [category: code] (depends: P1)

`kind: deliverable`

Target: `crates/gwiki/src/ingest/document.rs`

Add a document orchestrator mirroring the audio/image pattern (`ingest_document` + a `DocumentEndpoint`
Available/Unavailable + `From<DocumentIngestResult> for IngestResult`), behind the default-on `documents` feature
(Round 15). Office text: `calamine` (xlsx/xls/ods → bounded Markdown tables), `zip`+`quick-xml` over `word/document.xml`
(docx paragraph/run text) and `ppt/slides/slideN.xml` (pptx per-slide text); HTML → readable Markdown via the existing
`scraper`; structured text is inlined as `Text` by §1.3. Parse failure preserves the raw asset and writes a
`media_degradation` doc. Embedded office images are a tracked follow-up (text-only here).

**Acceptance:**

- 5.4.1 - `.xlsx` renders a Markdown table, `.docx`/`.pptx` extract text, `.html` renders readable Markdown, and a parse
  failure degrades while preserving the asset. test:
  `crates/gwiki/src/ingest/document.rs::tests::extracts_office_html_and_degrades`.

### 5.5 PDF — text layer combined with vision [category: code] (depends: 5.4, 3.1, 3.2)

`kind: deliverable`

Target: `crates/gwiki/src/ingest/pdf.rs`

Per page, **combine** (not fall back): extract the text layer with `pdf-extract`; rasterize the page with `pdfium-render`
(statically bundled pdfium — no external runtime binary) at a configured DPI; run the page image through `vision_extract`
(§3.1) for OCR + figure/chart descriptions; merge with the text layer authoritative for digital text and vision adding
OCR of image-only regions + visual descriptions, dedup'ing overlap; an optional `text_generate` reconciliation pass when
text routing is configured. Scanned PDFs (empty text layer) collapse to vision-only. Pages run **sequentially, bounded by
the shared limiter** (B1). Frontmatter records `page_count`, `has_text_layer`, `vision_used`, `model`. Degradation: no
`ai` → text-layer-only; empty text layer + no vision → store-as-asset + degradation; `documents` off → store-as-asset.

**Acceptance:**

- 5.5.1 - A digital PDF yields per-page Markdown combining text layer + vision (overlap dedup'd); a scanned PDF (no text
  layer) yields vision-OCR Markdown; degraded paths preserve the asset. test:
  `crates/gwiki/src/ingest/pdf.rs::tests::combines_text_layer_and_vision`.

### 5.6 Document degradation matrix and metadata [category: code] (depends: 5.4, 5.5)

`kind: deliverable`

Target: `crates/gwiki/src/document.rs`

A uniform degradation vocabulary and metadata across pdf/office/html mirroring the video matrix (§5.3): each failure mode
preserves the raw asset and writes a valid derived doc, and metadata always records `file_size_bytes` plus the relevant
count (`page_count`/`sheet_count`/`slide_count`).

**Acceptance:**

- 5.6.1 - Each document failure mode writes a valid degraded doc preserving the asset, with `file_size_bytes` and the unit
  count recorded. test: `crates/gwiki/src/document.rs::tests::document_degradation_matrix`.

## P6: Daemon capability-registry contract (sibling repo)

`kind: framing`

**Goal**: pin the contract the CLI routes to when routing=`daemon`. The daemon-side implementation is the gobby agent's
**Unified AI Capability Registry** plan, folded as new phases into `/Users/josh/Projects/gobby/.gobby/plans/gwiki-daemon-web.md`
(separate repo/epic — it also owns the `LLMService` refactor, the `code_index/summarizer`→`text_generate` migration, and
the runtime providers incl. **agy/Antigravity**). This phase produces only the **gobby-cli-side contract doc**; gwiki/gcode
degrade until the daemon ships. Boundary in A2.

### 6.1 Author the daemon capability contract (CLI side) [category: docs] (depends: 3.3)

`kind: deliverable`

Target: `docs/guides/ai-daemon-contract.md`, `docs/guides/hub-install-contract.md`

Document the routes the CLI consumes, the capability/transport model (A2), the per-request resolution order and
capability-error semantics, and the hub adoption contract. The daemon implements these in `gwiki-daemon-web.md`:

- **D1 extend `POST /api/voice/transcribe`** (`servers/routes/voice.py:95`; `WhisperSTT.transcribe` currently joins and
  **discards** the faster-whisper `segments`/`info` at `voice/stt.py:164`): surface segments + detected language. The
  route **accepts multipart fields `capability` (`audio_transcribe`|`audio_translate`, the `AICapability` value,
  defaulting to `audio_transcribe` — *not* `transcribe`/`translate`), `provider`, `model`, `language`, `prompt`** (the
  daemon's current shape — Round 9 #1 / Round 10) alongside `file`, and returns `{ text, segments:[{start,end,text}],
  language, model, task }` where the returned `task` is the faster-whisper task (`transcribe`/`translate`), keeping
  `text` for back-compat. Capabilities `audio_transcribe`/`audio_translate` are configured by the
  daemon's **`voice.openai_compatible_audio` binding** — `provider`, `url`, `model`, optional `api_key`, `timeout_seconds`,
  and the **`transcription_enabled`/`translation_enabled` flags** (transport `openai_compatible_http` proxied
  daemon-side, with `daemon_native` WhisperSTT as the legacy path). `GET /api/voice/status` already exists (`voice.py:28`)
  — the probe target; **it must surface those binding flags** so the §3.3 probe routes the two STT capabilities
  independently (`transcription_enabled`→`audio_transcribe`, `translation_enabled`→`audio_translate`) rather than
  inferring both from one 200 (Round 8 #5 / Round 9 #1).
- **D2 new `POST /api/llm/vision/extract`** + **`GET /api/llm/vision/status`**: capability `vision_extract`; wraps
  `LLMProvider.describe_image` (`llm/base.py:125`, **path-based and currently internal-only** — `chat_attachments` is
  upload-only, never a description fallback); returns `{ description, ocr_text?, model, provider }` — **`ocr_text` is an
  optional verbatim-text field (Round 6 #7)**; the daemon surfaces it when `describe_image` can, and until then the CLI
  reads it as absent → `None` and renders description-only.
- **D3 new `POST /api/llm/generate`** + **`GET /api/llm/status`**: capability `text_generate`; wraps `generate_text`
  (`llm/base.py:68`); `{ prompt, system_prompt?, provider?, model?, max_tokens?, caller? }` → `{ text, model, provider }`.
- **D4 `GET /api/providers/models`** (`routes/providers.py:291`): unchanged; **provider/model discovery only**. **Truth-
  source precedence (Round 9 #4)**: the per-capability **GET status routes (D1–D3) are the availability source of truth**
  the §3.3 probe checks first — a reachable status route whose body does not advertise a capability (for audio, whose
  `transcription_enabled`/`translation_enabled` flag is false) means *degrade that capability*, not *route it* (Round 8
  #5). `/api/providers/models` is consulted **only** to enumerate provider/model choices, **never** for availability.
- **Resolution & errors**: per (capability, request) — explicit `provider`/`model` override → daemon feature default →
  configured local/openai-compatible fallback → off; a provider that exists but lacks the capability returns a typed
  **capability error** (not "unknown provider"). The CLI forwards `(capability, provider, model)` when routing=`daemon`.
- **D5 hub adoption / in-place upgrade (install ordering)**: when `gobby install` finds an existing reachable standalone
  hub recorded in `~/.gobby/gcore.yaml` (`databases.postgres.dsn`) with its `~/.gobby/services/` compose, it must
  **adopt that Postgres and apply the full Gobby schema additively in place**, **preserving existing `code_*`/`gwiki_*`
  subset data**, and write the adopted DSN into `bootstrap.yaml`. The daemon baseline state classifier today recognizes
  `code_*` but **not `gwiki_*`** (`storage/hub/postgres.py:395-449`) — a standalone gwiki hub currently classifies
  `corrupt_partial` and fails, so adoption must extend the classifier/skip-list and preserve project identity
  (`projects.py:170` `ON CONFLICT DO NOTHING`). Cross-repo (daemon side); the CLI side is §8.5.
- **D6 embedding-config namespace migration (0.5.0 breaking; sequenced by P0E expand/migrate/contract — Round 6 #4 / Round 7 cross-repo)**: the daemon's embedding
  config moves from the `embeddings.*` `config_store` namespace to `ai.embeddings.*` **in lockstep with gobby-cli 0.5.0**
  (§8.2). **Writer**: `cli/installers/embedding.py::_persist_embedding_config` (today writes `embeddings.model/api_base/
  dim`). **Readers**: `EmbeddingsConfig` (`config/persistence.py`) → `servers/http.py` (tool semantic search),
  `code_index/sync_worker.py` (reindex), `ai/registry.py` (the **embed capability entry** of the registry this epic's
  contract aligns with), `memory/vectorstore.py` / `memory/.../knowledge_graph/code_linker.py` / `cli/memory/indices.py`,
  `utils/deps.py` (`embeddings.api_base`/`.dim`), `runner_init/storage.py`, `search/models.py`,
  `mcp_proxy/semantic_search.py`, and the settings-UI config-write route (`configuration_values.py`)
  (`configuration_ui_settings.py` persists only `ui_settings.*`, never embedding config, so it is **not** in the writer
  scope). **Dimension key unifies on `ai.embeddings.dim`** (the daemon's existing field name) —
  gcode adopts the same key, *resolving the split* that the daemon's mcp-proxy semantic-search dimension guard protects
  against today; **old dim keys are repo-specific** (gcode `embeddings.vector_dim` vs daemon `embeddings.dim`), and each
  repo's P1 dual-read maps its own old key into canonical `ai.embeddings.dim`; model/api_base already share keys. **One-time `config_store`
  migration** in the hub install/upgrade path (the D5 adoption flow): rename existing `embeddings.* → ai.embeddings.*`
  rows, preserving values and the `is_secret` flag; without it, existing installs lose embedding config and semantic
  search / code index / memory KG silently disable. Because `config_store` is daemon-owned, **only the daemon** runs this
  migration; the CLIs never rewrite it. **No co-release constraint (via P0E)**: P0E's E1 dual-write + dual-read and E2
  migration populate and *prefer* `ai.embeddings.*` ahead of time, so this D6 cut is P0E's **daemon contract (E3) step** —
  it and gcode's §8.2 cut are **independent, non-breaking** releases with no same-window coupling and no permanent shim.
  Cross-repo (daemon side, `gwiki-daemon-web.md`); the gcode side is §8.2; the expand/migrate scaffolding is P0E E1/E2.
- **Daemon memory note**: serialize model loads / honor keep-alive so it does not hold whisper + multimodal + embeddings
  resident at once (B1).

**Acceptance:**

- 6.1.1 - The CLI contract documents D1–D4 with route shapes, the GET status/probe routes, the capability/transport model,
  the resolution order, and capability-error semantics — including the voice `capability`/`provider`/`model`/`language`/
  `prompt` multipart fields and the `voice.openai_compatible_audio` binding flags (Round 9 #1). file:
  `docs/guides/ai-daemon-contract.md`.
- 6.1.2 - The documented GET status routes match the capability probe targets in `crates/gcore/src/ai/probe.rs`; the
  contract specifies each status body advertises **capability-level** support (the `/api/voice/status`
  `transcription_enabled`/`translation_enabled` flags distinguish `audio_transcribe` from `audio_translate`), and that the
  **status route — not `/api/providers/models` — is the availability truth source** (Round 8 #5 / Round 9 #1/#4). behavior:
  "probe routes match the contract" in `docs/guides/ai-daemon-contract.md`.
- 6.1.3 - The hub-install contract specifies D5 adoption + additive in-place upgrade preserving `code_*`/`gwiki_*` data
  and project identity, and names the daemon-side classifier gap (`gwiki_*` not yet recognized). file:
  `docs/guides/hub-install-contract.md`.
- 6.1.4 - The contract documents D6: the `embeddings.* → ai.embeddings.*` migration (writer + reader inventory, the
  `ai.embeddings.dim` unification resolving the mcp-proxy semantic-search dimension split, the one-time daemon-owned
  `config_store` migration in the D5 flow, and the P0E dual-write sequencing that removes the same-window co-release
  constraint). file:
  `docs/guides/ai-daemon-contract.md`.

## P7: Docs, CI, and release

`kind: framing`

**Goal**: ship gwiki v0.1.0 to CI/release parity with the other crates and document configuration.

### 7.1 Add gwiki and the gcore ai feature to CI [category: config] (depends: P5)

`kind: deliverable`

Target: `.github/workflows/ci.yml`

Add, alongside the existing gloc/gsqz block (`ci.yml:44-63`): `cargo clippy -p gobby-wiki --all-targets -- -D warnings`,
`cargo test -p gobby-wiki`, plus lean `cargo clippy -p gobby-wiki --no-default-features -- -D warnings` and
`cargo test -p gobby-wiki --no-default-features` (proves the off/degraded path; gcode precedent `ci.yml:65-70`), and
`cargo clippy -p gobby-core --features ai --all-targets -- -D warnings` **and `cargo test -p gobby-core --features ai`**
(so the P2 transport tests actually execute, not just compile — Round 5 #6). ffmpeg is **not** installed in CI — ffmpeg-
touching tests are `#[ignore]`/env-gated; transport tests use loopback servers and trait fakes. **Documents (Round 15)**:
the default `cargo test -p gobby-wiki` exercises the default-on `documents` feature; CI fetches the `pdfium` library so
`pdfium-render` builds, and PDF-rasterization tests are `#[ignore]`/env-gated like ffmpeg; the `--no-default-features` run
proves the store-as-asset degraded path.

**Acceptance:**

- 7.1.1 - CI runs gwiki clippy+test (default — incl. the `documents` feature, with `pdfium` fetched — and
  `--no-default-features`) and gcore `--features ai` **clippy and test**. file: `.github/workflows/ci.yml`.

### 7.2 Add the gwiki release workflow [category: config] (depends: 7.1)

`kind: deliverable`

Target: `.github/workflows/release-gwiki.yml`

Model on `release-gsqz.yml`: trigger on `gwiki-v*`, tag↔`Cargo.toml` version guard (`release-gsqz.yml:23-40`, package
`gobby-wiki`), cross-platform build matrix (binary `gwiki`), `cargo publish -p gobby-wiki`, GitHub release. **Release
ordering (Round 5 #7, corrected Round 8 #8)**: `gobby-wiki` pins `gobby-core` via the workspace (currently `0.3.0`, `crates/gwiki/Cargo.toml:27`), but the published `gobby-core` must carry the new
`ai` feature (added by P2.1, which requires a gcore version bump) — so the required gcore version (≥ 0.3.0 with `ai`) must already be on crates.io and
`crates/gwiki/Cargo.toml:27` pinned to it before `cargo publish -p gobby-wiki` can succeed. **Publishing gcore is *not* this
workflow's job** — it belongs to gcore's own release path; `release-gwiki.yml` only adds a **precondition guard** that
*verifies* the pinned `gobby-core` version is published with the `ai` feature (e.g. resolve it from the index / a dry-run
`cargo publish`) and fails fast otherwise, never running `cargo publish -p gobby-core` itself. Release builds use default
features (`ai` on); gwiki version stays `0.1.0` (`gwiki/Cargo.toml:3`); first tag `gwiki-v0.1.0`.

**Acceptance:**

- 7.2.1 - `release-gwiki.yml` triggers on `gwiki-v*`, guards the version, builds the matrix, publishes, and releases.
  file: `.github/workflows/release-gwiki.yml`.
- 7.2.2 - `release-gwiki.yml` **verifies** (does not publish) that the pinned `gobby-core` version is on crates.io with
  the `ai` feature and fails fast otherwise; gcore publication lives in gcore's own release path (Round 8 #8). file:
  `.github/workflows/release-gwiki.yml`.

### 7.3 Document the AI configuration matrix [category: docs] (depends: P5)

`kind: deliverable`

Target: `crates/gwiki/README.md`, `docs/guides/ai-configuration.md`

A per-modality × backend matrix (OpenAI API / daemon / faster-whisper server / local VLM via LM Studio/Ollama), a worked
mixed-routing example (`transcription.routing=direct` faster-whisper + `vision.routing=direct` LM Studio + `--translate`),
the `--no-ai` privacy path, the 3-model budget guidance (B1), and the explicit note that **STT needs a server
implementing `/v1/audio/transcriptions`** — LM Studio/Ollama serve text/vision/embeddings but not STT.

**Acceptance:**

- 7.3.1 - The matrix, mixed-routing example, STT-server note, and 3-model budget guidance are documented. file:
  `docs/guides/ai-configuration.md`.

## P8: Crate demarcation — shared provisioning, gcode AI, gloc discovery (downstream)

`kind: framing`

**Goal**: clean up cross-crate responsibilities — give gwiki shared hub-provisioning parity and a single-hub
invariant across standalone/daemon installs, route gcode embeddings + optional LLM outlines through the shared layer,
and share gloc's local-backend discovery. Valid epic scope, downstream of the gwiki ingest MVP (none of it unblocks
multimodal ingest). The provisioning deliverables (8.4–8.5) are independent of the AI work and may run in parallel.

**Expansion gate (Round 8 #7; enforced as a validation condition, Round 9 #5)**: P8 stays **in this epic** but is
explicitly **gated behind the P1–P7 MVP** — every P8 deliverable carries a transitive `depends:` on the MVP and none is a
prerequisite of P1–P7. This is not just prose: VS1 states it as a **checkable expansion-validation invariant** (a manifest
that schedules any P8 task before the MVP gate is rejected). The adversarial review's "P8 buries the MVP in one
implementation train" concern assumes a single-shot build; it does not apply here, because the epic→subtask expansion
turns these `depends:` edges into **gated subtasks** that schedule after the MVP gate, not alongside it. Splitting P8 to a
*separate plan file* (the P0E treatment) is therefore unnecessary — the DAG, honored and validated at expansion time,
provides the same isolation while keeping the cross-crate demarcation legible in one epic. (P0E is extracted to its own
file only because it is **cross-repo**, spanning the daemon — an orthogonal reason from MVP sequencing.)

### 8.1 Extract local-backend discovery into gcore and adopt in gloc [category: refactor] (depends: P2, P5, P6, P7)

`kind: deliverable`

Target: `crates/gcore/src/local_backend.rs`, `crates/gloc/src/backend.rs`, `crates/gloc/src/config.rs`,
`crates/gloc/Cargo.toml`

Move `Backend { name, url, probe, auth_token }`, `detect_backend`, and `validate_backend` (currently in
`crates/gloc/src/backend.rs`) into `gobby_core::local_backend` with the LM Studio/Ollama defaults. **Split data from probing to keep the lean-core
boundary honest (Round 8 #2), behind a dedicated feature (Round 10 #2)**: the `Backend` struct + the static LM
Studio/Ollama default table are **always-compiled** (plain data, no HTTP), while `detect_backend`/`validate_backend` —
which do `ureq` GET probes — are **gated behind the `local_backend` feature** (`local_backend = ["dep:ureq"]`,
`#[cfg(feature = "local_backend")]`), so a bare `gobby-core` build pulls neither `ureq` nor any HTTP-probe code. Both
consumers enable the gate **at the right granularity**: `gloc` adopts the shared module with **`gobby-core/local_backend`
only** — gaining discovery + `ureq` **without** dragging in `reqwest`/multipart (keeping the tiny `opt-level="z"` binary
lean) and keeping its own `ensure_model_ready` lifecycle; `gcore::ai` gets `local_backend` transitively (the `ai` feature
pulls it) so `direct`/`auto` can auto-discover a local endpoint (`{backend.url}/v1`) when `*_api_base` is unset. **Discovery is capability-aware (Round 5 #10)**: LM Studio/Ollama
auto-discovery serves only `text_generate`/`vision_extract`/`embed` (they expose `/v1/chat/completions` + `/v1/embeddings`,
**not** `/v1/audio/transcriptions`); `audio_transcribe`/`audio_translate` are **never** auto-discovered to a
chat/embeddings backend — they require an explicitly configured STT endpoint (faster-whisper / OpenAI-compatible STT) or a
distinct STT probe, else degrade to off. gloc retains lifecycle (`ensure_model_ready`).

**Acceptance:**

- 8.1.1 - `gobby_core::local_backend::detect_backend` exists and gloc uses it with no behavior change. test:
  `crates/gcore/src/local_backend.rs::tests::detects_first_reachable`.
- 8.1.1a - The `Backend` data type compiles with no features while `detect_backend`/`validate_backend` are gated behind
  **`local_backend`** (`= ["dep:ureq"]`), so a bare `gobby-core` build links no `ureq`/probe code; `gloc` enables
  `gobby-core/local_backend` **without** pulling `reqwest`/multipart (Round 8 #2 / Round 10 #2); the public-boundary test
  reflects both features. test: `crates/gcore/tests/public_boundary.rs::cargo_features_define_public_boundary`.
- 8.1.2 - gcore::ai resolves `direct` api_base from discovery when unset. test:
  `crates/gcore/src/ai/mod.rs::tests::direct_autodiscovers_local_endpoint`.
- 8.1.3 - STT capabilities are not auto-discovered to an LM Studio/Ollama backend; they require explicit STT config. test:
  `crates/gcore/src/ai_context.rs::tests::stt_not_autodiscovered_to_chat_backend`.

### 8.2 Fold gcode embeddings under shared routing [category: refactor] (depends: 8.1)

`kind: deliverable`

Target: `crates/gcode/src/vector/code_symbols/embedding.rs`, `crates/gcode/src/config.rs`

Keep the existing OpenAI-compatible `/embeddings` client (`resolve_embedding_config`) but resolve its endpoint/routing
through the shared **`embed` capability binding** (`ai.embeddings.*`, transport `openai_compatible_http`; A2) +
`local_backend` discovery — the same vocabulary the daemon registry uses, so embeddings stops being a special case.
**The `embeddings.* → ai.embeddings.*` rename is owned by the separate `embeddings-namespace-migration` epic, NOT §8.2
(Round 11)**: §8.2 has a **hard cross-epic dependency on that epic's Contract phase** and does **not** re-own the no-alias
cut. That epic owns the complete inventory and the dangerous parts — the full gcode/standalone key set
(`api_base/model/api_key/query_prefix/provider`, `vector_dim`→**`ai.embeddings.dim`**) under `ai.embeddings.*` in
`gcore.yaml`/`config_store` with **no env vars (Round 11)** — the legacy `embeddings.api_key_env` env-indirection is
**retired**, not migrated — the gcore.yaml/setup writers, the daemon-side `config_store` migration, and the api-key storage
policy (`config_store` may use `$secret:embeddings_api_key` / `is_secret`; daemonless `gcore.yaml` may use a plaintext local
`ai.embeddings.api_key`; embeddings-namespaced, and for legacy installs that shared `openai_api_key`, copy-not-move).
**§8.2's
own work** is the embed-capability routing refactor: route gcode's existing OpenAI-compatible `/embeddings` client
(`resolve_embedding_config`) through the shared **`embed` capability binding** + `local_backend` discovery, **consuming**
the already-migrated `ai.embeddings.*` keys so embeddings stops being a special case and shares the same `AiContext` gwiki
uses. **`embed` never auto-routes to the daemon (Round 6 #6)**: its `Auto` resolves **direct → `local_backend` discovery →
off only** (no daemon leg) until the daemon owns a real embedding-generation route. Because the migration epic's
Expand/Migrate phases already populated and *preferred* `ai.embeddings.*` before its Contract cut, §8.2 (gated on that
Contract) is independent and non-breaking, with no permanent shim. Implementation stays in gcode (not migrated into gloc;
gcode does not depend on gloc).

**Acceptance:**

- 8.2.1 - Embeddings endpoint resolves via the `ai.embeddings.*` binding + discovery (`embed` `Auto` = direct→discovery→off,
  never daemon — Round 6 #6) and still degrades to empty results when unavailable. test:
  `crates/gcode/src/vector/code_symbols/embedding.rs::tests::resolves_via_shared_routing`.
- 8.2.2 - gcode's embeddings client resolves endpoint/model/key/dim/query_prefix from the shared `ai.embeddings.*` binding
  (no private `resolve_embedding_config` key reads); the `embeddings.*`→`ai.embeddings.*` rename and legacy-key rejection
  are owned and tested by the `embeddings-namespace-migration` epic's Contract phase, on which §8.2 depends (Round 11).
  test: `crates/gcode/src/vector/code_symbols/embedding.rs::tests::reads_endpoint_from_shared_binding`.

### 8.3 Add optional LLM-backed gcode outlines [category: code] (depends: 8.1)

`kind: deliverable`

Target: `crates/gcode/src/commands/symbols.rs`, `crates/gcode/src/cli.rs`

Default outline stays deterministic AST. Extend the existing `Command::Outline { file }` (`cli.rs:267`) with a
`--summarize` flag, handled in the flat `commands/symbols.rs` (no module split), that sends code
to `gobby_core::ai::generate_text` via the **`text_generate` capability binding** (`ai.text_generate.*`; auto → daemon
`/api/llm/generate` → openai-compatible direct → off; A2), returning a natural-language outline; degrade to AST when
unavailable. This mirrors the daemon's own `code_index/summarizer` path, which `gwiki-daemon-web.md` migrates onto
`text_generate`. No change to deterministic output or UUID5 symbol-ID parity.

**Acceptance:**

- 8.3.1 - `gcode outline --summarize` returns an LLM outline when text routing is configured. test:
  `crates/gcode/src/commands/symbols.rs::tests::summarizes_when_configured`.
- 8.3.2 - `--summarize` degrades to deterministic AST when text routing is off/unconfigured. test:
  `crates/gcode/src/commands/symbols.rs::tests::degrades_to_ast`.

### 8.4 Give gwiki shared hub-provisioning parity via `ensure_hub` [category: code] (depends: P5, P6, P7)

`kind: deliverable`

Target: `crates/gcore/src/provisioning.rs`, `crates/gwiki/src/commands/setup.rs`, `crates/gwiki/src/main.rs`, `crates/gcode/src/commands/setup.rs`, `crates/gcore/tests/public_boundary.rs`

Today the resolve-or-provision + `gcore.yaml`-merge orchestration lives only in gcode (`commands/setup.rs:162`
`resolve_or_provision_database` + `write_gcore_config`); `gwiki setup` (`commands/setup.rs`) only runs DDL when
`database_url_from_env()` is `Some`. Factor a shared `gobby_core::provisioning::ensure_hub(options) -> (database_url,
Option<DockerProvisioningReport>)`: resolve an existing reachable DSN (env `GOBBY_POSTGRES_DSN` → `~/.gobby/gcore.yaml`
`databases.postgres.dsn` → `~/.gobby/bootstrap.yaml` `database_url`) and **only on failure** call
`provision_docker_services` + `default_database_url`. Add `gwiki setup --standalone` (+ service/embedding flags) that
calls `ensure_hub`, runs the existing `gwiki_*` DDL (`crates/gwiki/src/setup.rs`), and **merges** its keys into
`gcore.yaml` via `StandaloneConfig` (preserving gcode/embedding keys). Refactor gcode's `resolve_or_provision_database`
to call `ensure_hub`, keeping gcode-specific DSN sources (`GCODE_DATABASE_URL`, daemon broker) as higher-priority
overrides. gwiki and gcode write only their **own** namespaced subset tables; neither touches the other's or daemon-owned
objects. **Boundary**: `provisioning` is always-compiled (`lib.rs:12`) but Postgres reachability needs the `postgres`
feature, so `ensure_hub`'s reachability/identity probe is `#[cfg(feature = "postgres")]`-gated (callers without it get the
resolve-from-config path only); update `crates/gcore/tests/public_boundary.rs` if the module surface changes.

**Acceptance:**

- 8.4.0 - `ensure_hub` compiles without the `postgres` feature (reachability probe gated) and the public-boundary test
  passes. test: `crates/gcore/tests/public_boundary.rs::cargo_features_define_public_boundary`.
- 8.4.1 - `ensure_hub` resolves an existing reachable DSN before provisioning and both crates call it. test:
  `crates/gcore/src/provisioning.rs::tests::ensure_hub_reuses_then_provisions`.
- 8.4.2 - `gwiki setup --standalone` provisions a hub when none exists and creates `gwiki_*` objects + merges `gcore.yaml`
  without clobbering gcode keys. test:
  `crates/gwiki/src/commands/setup.rs::tests::standalone_provisions_and_merges_config`.
- 8.4.3 - With a gcode-provisioned hub present, `gwiki setup` reuses the DSN (no new provisioning) and the two subsets
  coexist. test: `crates/gwiki/src/commands/setup.rs::tests::reuses_existing_gcode_hub`.

### 8.5 Enforce the single-hub invariant across install orders [category: code] (depends: 8.4)

`kind: deliverable`

Target: `crates/gcore/src/provisioning.rs`, `crates/gwiki/src/support/env.rs`, `crates/gcode/src/db.rs`

Make hub resolution coherent across all three install orders so previously-indexed subset data is never orphaned:

- **daemon-first → CLI**: CLIs resolve the daemon hub (broker/`bootstrap.yaml`) and add only their subset DDL (existing
  behavior; validate it stays non-destructive).
- **CLI-first → CLI**: §8.4 coexistence (disjoint subsets, shared `gcore.yaml`/compose).
- **CLI-first → daemon-later**: the daemon adopts and **upgrades the existing partial hub in place** (§6.1). On the CLI
  side, once `bootstrap.yaml`/broker appears, resolution prefers it — but `ensure_hub` first **verifies the
  daemon-reported DSN reaches the same physical hub that holds the existing `gcore.yaml` data**. *Same hub* is decided by
  a **read-only cluster-identity probe**: compare `SELECT system_identifier FROM pg_control_system()` **plus** the target
  database name across both DSNs (proves same physical cluster + database, no marker table, ownership-neutral). If the
  identities differ (genuine divergence), surface a typed conflict (`CoreError`/degradation naming both DSNs) instead of
  silently switching and losing data. Never provision a third hub when any recorded hub is reachable.

**Acceptance:**

- 8.5.1 - `ensure_hub` never provisions a second hub when a recorded DSN (gcore.yaml or bootstrap.yaml) is reachable.
  test: `crates/gcore/src/provisioning.rs::tests::no_double_provision_when_reachable`.
- 8.5.2 - When the two DSNs resolve to a different `system_identifier`+database (different physical hubs), resolution
  surfaces a conflict rather than silently switching. test:
  `crates/gcore/src/provisioning.rs::tests::divergent_hubs_surface_conflict`.
- 8.5.3 - After a daemon adopts the standalone hub (same DSN in both files), CLIs resolve it with no conflict and the
  subset data remains addressable. test: `crates/gcode/src/db.rs::tests::adopted_hub_resolves_without_conflict`.

## P9: Codebase → wiki documentation (gcode-generated, gwiki-ingested)

`kind: framing`

**Goal**: gcode produces robust, hierarchical, citation-grounded Markdown documentation of a codebase — per-file API docs
→ clustered module docs + Mermaid diagrams → a repo architecture overview — reusing its tree-sitter AST symbols, the
FalkorDB call/import graph, BM25/embeddings, and this epic's `text_generate`; **gwiki ingests** the generated Markdown
into the vault. This honors `crate_has_no_gcode_dependency` (gcode emits `.md`; gwiki ingests it; no crate link, C1). The
generator is modeled on the open-source CodeWiki/autodoc/gitsummarize/llama_index pipelines (prompts aren't licensed —
adapted freely, no attribution requirement). **Downstream of the MVP**: every P9 deliverable transitively `depends:` on
§8.3 (itself MVP-gated via §8.1), so the expansion schedules P9 after the P1–P7 MVP (VS1).

### 9.1 gcode hierarchical code-doc generator (file → module → repo) [category: code] (depends: 8.3)

`kind: deliverable`

Target: `crates/gcode/src/commands/codewiki.rs`, `crates/gcode/src/cli.rs`

Add a `gcode codewiki [--out DIR] [--scope …]` subcommand that generates a Markdown doc set bottom-up — symbol → file →
module → repo — via `text_generate` (the §8.3 capability), each level summarized **once** (token-efficient tree-summarize,
reusing lower-level summaries upward). Per-file docs are built from AST symbol spans (signatures + an LLM-written purpose).
Prompts live in a constants module adapted from autodoc's per-file/folder summaries, CodeWiki's module/repo overviews, and
the llama_index tree-summarize template. When text routing is off, degrade to AST-only structural docs (no LLM prose).

**Acceptance:**

- 9.1.1 - `gcode codewiki` emits per-file API docs, per-module overviews, and a repo overview as Markdown, and degrades to
  AST-only structural docs when text routing is off. test:
  `crates/gcode/src/commands/codewiki.rs::tests::generates_hierarchical_docs`.
- 9.1.2 - The `codewiki` subcommand is registered on the gcode CLI. file: `crates/gcode/src/cli.rs`.

### 9.2 Module clustering from the dependency graph [category: code] (depends: 9.1)

`kind: deliverable`

Target: `crates/gcode/src/commands/codewiki.rs`

Group symbols/files into modules using directory structure plus FalkorDB import/call edges (graph communities), adapting
CodeWiki's cluster/filter prompts to drop non-core files (tests/vendored/generated) and keep stable `file_path::name`
component IDs.

**Acceptance:**

- 9.2.1 - Components cluster into modules informed by directory + import/call edges; non-core files are filtered and
  component IDs keep the `file_path::name` form. test:
  `crates/gcode/src/commands/codewiki.rs::tests::clusters_modules_from_graph`.

### 9.3 Mermaid diagrams from the graph [category: code] (depends: 9.2)

`kind: deliverable`

Target: `crates/gcode/src/commands/codewiki.rs`

Emit Mermaid from gcode's FalkorDB graph: a module dependency graph from import edges, call/sequence diagrams from
callers/callees bounded to 1–2 hops, and an optional class diagram from AST class/inheritance — feeding the bounded
adjacency (never a full-graph dump) to the renderer.

**Acceptance:**

- 9.3.1 - Module docs include a Mermaid dependency diagram derived from import edges, bounded to N hops (no full-graph
  dump). test: `crates/gcode/src/commands/codewiki.rs::tests::emits_bounded_mermaid`.

### 9.4 Citation grounding and provenance frontmatter [category: code] (depends: 9.1)

`kind: deliverable`

Target: `crates/gcode/src/commands/codewiki.rs`

Ground every claim with a `file:line` citation resolved from gcode's exact symbol spans, mechanically verifying that each
cited range exists (dropping or repairing invalid citations before write). Each doc carries a `source_files:` YAML
frontmatter list (file + line ranges) for staleness detection and reverse lookup.

**Acceptance:**

- 9.4.1 - Generated docs carry `file:line` citations validated against real symbol spans, with a `source_files`
  frontmatter list, and invalid citations are rejected. test:
  `crates/gcode/src/commands/codewiki.rs::tests::citations_validated_against_spans`.

### 9.5 Incremental regeneration [category: code] (depends: 9.1, 9.4)

`kind: deliverable`

Target: `crates/gcode/src/commands/codewiki.rs`

Reuse gcode's existing SHA-256 incremental hashing plus the `source_files` frontmatter to regenerate only the docs whose
source files changed (file → owning module → repo overview), recording a `_meta` log of generated docs.

**Acceptance:**

- 9.5.1 - After a single-file change, only the affected file/module/overview docs regenerate; unchanged docs are left
  untouched. test: `crates/gcode/src/commands/codewiki.rs::tests::incremental_regenerates_only_changed`.

### 9.6 gwiki ingest of generated code-docs [category: code] (depends: 9.1, P1)

`kind: deliverable`

Target: `crates/gwiki/src/ingest/code_docs.rs`, `crates/gwiki/src/ingest/file.rs`, `crates/gwiki/src/sources.rs`

Add a `SourceKind::CodeDoc` variant and ingest the gcode-generated Markdown tree into the wiki vault via gwiki's existing
Markdown path, preserving the `source_files` provenance and converting code-doc cross-references to `[[wikilinks]]`. **No
gwiki→gcode crate dependency** — gwiki consumes the pre-generated `.md` only; the generate→ingest orchestration is a
documented CLI/daemon step (`gcode codewiki --out <vault>/code`, then gwiki indexes).

**Acceptance:**

- 9.6.1 - A gcode-generated doc tree ingests as `CodeDoc` wiki documents preserving `source_files` provenance and
  `[[wikilinks]]`. test: `crates/gwiki/src/ingest/code_docs.rs::tests::ingests_codedocs_with_provenance`.
- 9.6.2 - `ingest_path` recognizes and ingests the generated code-doc tree. test:
  `crates/gwiki/src/ingest/file.rs::tests::dispatches_generated_code_docs`.
- 9.6.3 - `SourceKind::CodeDoc` exists and `crate_has_no_gcode_dependency` still passes (no crate link). file:
  `crates/gwiki/src/sources.rs`.

### 9.7 codewiki CI and documentation [category: config] (depends: 9.1, 9.6)

`kind: deliverable`

Target: `.github/workflows/ci.yml`, `docs/guides/codewiki.md`

Add CI coverage that runs the `gcode codewiki` tests (driving `text_generate` through a loopback fake), and write
`docs/guides/codewiki.md` describing the generation pipeline (hierarchy, clustering, diagrams, citations, incremental regen) and
the gcode→gwiki ingest workflow.

**Acceptance:**

- 9.7.1 - CI runs the `gcode codewiki` tests. file: `.github/workflows/ci.yml`.
- 9.7.2 - `docs/guides/codewiki.md` documents the generation pipeline and the gcode→gwiki ingest workflow. file:
  `docs/guides/codewiki.md`.

## P0E: Embeddings-namespace migration — SEPARATE cross-repo P0 epic (captured for extraction)

`kind: framing`

**Status**: a *separate* P0 epic spanning **gobby-cli** and the **gobby daemon** (`gwiki-daemon-web.md`), captured here for
handoff — **not part of this epic's task manifest** (framing only, no `kind: deliverable` blocks). On approval it is
extracted to `.gobby/plans/embeddings-namespace-migration.md` and adversarially expanded on its own (its phases are
canonical `## P1` Expand / `## P2` Migrate / `## P3` Contract — Round 11). **This epic does not re-own the cut (Round 11)**:
the no-alias rename lives entirely in the migration epic's **Contract (P3)** phase; this epic's **§8.2 (gcode embed-routing)
is a downstream *consumer* that depends on that Contract** (not the cut itself), and **§6.1 D6 is a CLI-side contract *doc*
item**, not a daemon deliverable. Both are gated on the migration epic's Expand/Migrate shipping first.

**Why**: the `embeddings.* → ai.embeddings.*` rename is shared config living in daemon-owned `config_store`; a no-alias
*atomic* flip would force a same-window co-release and risk silently disabling embeddings (semantic tool search,
code-index reindex, memory KG) on any version skew. **Expand/migrate/contract with dual-write/dual-read** removes the
co-release constraint — both repos ship independently and the **end state still has no shims** (transitional dual paths
are deleted at E3/0.5.0 GA). It also *fixes a pre-existing bug*: gcode reads `embeddings.vector_dim` while the daemon
writes/reads `embeddings.dim` (the `semantic_search.py:184` "writers use one daemon embedding config" guard), unified
here on **`ai.embeddings.dim`**.

**E1 — Expand (both repos; non-breaking; ship anytime, concurrently):**

- **Key constants + CI guard**: centralize embedding key names behind constants and add a CI test rejecting any stray
  literal `embeddings.` key. gcode: `config.rs:165-168`, `context.rs:40`. daemon: `cli/installers/embedding.py`,
  `utils/deps.py`, `ai/registry.py`, `EmbeddingsConfig`/`config/persistence.py`.
- **Dim becomes advisory via a probe**: gcode auto-detects the embedding dimension from the endpoint (mirroring the
  daemon's `_probe_embedding_dim`, `embedding.py:377`), config key as override only, backed by the `semantic_search.py:184`
  mismatch guard — *immediately* resolving the `vector_dim`/`dim` split independent of the prefix.
- **Dual-read** everywhere (`ai.embeddings.*` preferred → `embeddings.*` fallback; `ai.embeddings.dim` → `embeddings.dim`
  /`embeddings.vector_dim`). Non-breaking — nothing writes the new namespace yet, so resolution still lands on the old.
- **Dual-write** (daemon): `_persist_embedding_config` + UI config-write paths write **both** namespaces during the window.
- **Pre-build + unit-test the one-time `config_store` migration** (`embeddings.* → ai.embeddings.*`, preserving
  `is_secret`), idempotent, wired into the D5 hub upgrade/adoption path.
- **Non-code**: finalize the D6 writer/reader inventory contract doc + an embedding-config **doctor** (read-only
  consistency check, both repos).

**E2 — Migrate:**

- Daemon runs the `config_store` migration on upgrade so every existing install has the `ai.embeddings.*` rows; the
  doctor confirms gcode + daemon agree.
- Both repos flip the *canonical* read to prefer `ai.embeddings.*` (old still fallback); verify real installs resolve from
  the new namespace.

**E3 / Contract (`## P3` on extraction) — the no-alias cut, OWNED by this migration epic (Round 11); the gwiki epic's
§8.2 *consumes* it and §6.1 D6 only *documents* it CLI-side:**

- gcode side: drop the old-key fallback in the resolver (`config.rs`/`context.rs`) + the gcore.yaml/setup writers;
  `ai.embeddings.*` only; tests assert old keys rejected. (The gwiki epic's §8.2 embed-routing refactor then depends on
  this and consumes the migrated keys.)
- daemon side: drop dual-write; read/write only `ai.embeddings.*`; retire the migration past baseline.
- Because E1–E2 already populated and *preferred* the new namespace, each repo's Contract cut is **independent and
  non-breaking** — the co-release constraint is gone, and the end state has no shims.

## VS1: Verification

`kind: verification`

End-to-end the epic succeeds when: `gwiki ingest-file` dispatches `.mp3`/`.png`/`.mp4` to the orchestrators (P1); audio
produces timestamped transcripts with language + task, translation honors precedence, and long media chunks
deterministically (P4); images and audio-first video with real co-equal frames render with the partial-failure matrix
(P5); each modality routes daemon/direct/off per scenario with project_id optional (P3/S1); the no-`ai` build compiles
and degrades cleanly and `cargo tree` shows reqwest only under `ai`/`qdrant` (P2/C1); gwiki is in CI and has a release
workflow at v0.1.0 (P7); the daemon contract documents D1–D4 with GET probe routes and provider/model policy (P6); and
gcode embeddings + optional outlines and shared gloc discovery work without a gcode→gloc dependency (P8); gwiki can
independently provision the shared hub and coexist with an independent gcode install, and all three install orders
(daemon-first, CLI-first, CLI-then-daemon) converge on **one** hub with `code_*`/`gwiki_*` subset data preserved (the
daemon additively upgrades a partial hub) and genuine divergence surfaced as a conflict (P8/§6.1); documents (PDF
combining text-layer + vision, Office, HTML, structured text) ingest to derived Markdown with graceful degradation
(P5 §5.4–5.6); and gcode generates hierarchical, citation-grounded, Mermaid-bearing codebase docs that gwiki ingests
with `crate_has_no_gcode_dependency` green (P9). The local-model footprint never exceeds the 3-model budget (B1).

**Expansion validation condition (Round 9 #5; extended to P9 in Round 15)** — enforced by the task-manifest
expansion/`gobby plans validate`, not just prose: **every P8 and P9 deliverable must carry a transitive `depends:` on the
P1–P7 MVP completion** (P9 inherits it via §8.3), and **no P1–P7 deliverable may `depends:` on any P8 or P9 deliverable**.
A generated manifest that schedules any P8/P9 task before the MVP gate is **invalid** and must be rejected/regenerated.
This makes "P1–P7 MVP gate before P8/P9" a checkable invariant (the in-epic equivalent of splitting them to a downstream
epic) rather than a hope.

## V1 Plan Changelog

`kind: verification`

**Round 0 (pre-draft, interactive)**

- reviewer: external (codex) + interactive design review
- verdict: incorporated
- findings resolved into the draft:
  - dispatch gap at `ingest/file.rs:18` made the hard-prerequisite P1;
  - daemon GET-only probe → added `GET /api/llm/vision/status`/`/api/llm/status` (3.3, 6.1);
  - real video frame-image data flow + explicit `interval 0` disable (5.2);
  - first-class gwiki AI config source for DB/no-DB (1.2);
  - honest feature-isolation goal (no AI/multipart transport in lean builds, not "no reqwest") (C1, 7.1);
  - concrete chunk codec/bitrate math and ffprobe-failure tolerance (4.3);
  - accurate scope-vs-project_id wording (C1);
  - daemon provider/model policy for the new LLM routes (6.1);
  - per-modality routing, 3-model budget, and gloc discovery/governor split (A1, B1, 3.1, 8.1).
- note: `## M1 Task Manifest` intentionally omitted from this draft; it is emitted by `plan-adversary-taskless` or the
  interactive coordinator on approval, then validated with `gobby plans validate --mode expansion`.

**Round 1 (interactive — provisioning & install ordering)**

- verdict: incorporated
- findings resolved:
  - corrected the "no Docker" constraint: AI is HTTP-only, but the **data hub is gwiki-provisionable** with parity to
    gcode via shared `gobby_core::provisioning::ensure_hub` (§8.4);
  - clarified **subset/superset** ownership: gcode (`code_*`) and gwiki (`gwiki_*`) own disjoint subsets; a standalone
    hub is a *partial* Gobby DB (no `config_store`); the daemon owns the superset (C1);
  - added the **single-hub invariant across all install orders**, including **CLI-first-then-daemon adoption with
    additive in-place upgrade** preserving subset data + project identity, and conflict-surfacing on divergence
    (§8.5 CLI side, §6.1 D5 daemon side).

**Round 2 (interactive — capability registry, provider demarcation, daemon-epic split)**

- verdict: incorporated
- findings resolved:
  - **daemon side has its own epic**: the daemon AI routes are folded into `gwiki-daemon-web.md` (the gobby agent's
    "Unified AI Capability Registry" plan), not free-floating; P6 is now the **CLI-side contract** that epic implements,
    with an explicit repo boundary (A2);
  - **capability-over-family model**: replaced the flat `{claude,codex,local}` / per-modality framing with **capabilities**
    (`embed`, `audio_transcribe`, `audio_translate`, `vision_extract`, `text_generate`) over **transports**
    (`cli_adapter`, per-capability `openai_compatible_http`, `daemon_native`); resolution = override → feature default →
    local fallback → off, with typed **capability errors** (A2, P1.1, P6);
  - **embeddings unified**: gcode embeddings reframed as the `embed` capability over `openai_compatible_http` — same
    binding schema (`api_base/model/api_key`) the daemon registry uses; implementation stays in gcode (§8.2);
  - **`local` is per-capability**, not one endpoint (STT→faster-whisper vs text/vision→LM Studio), honoring the 3-model
    budget (A2, P1.1);
  - **verified daemon internals** (gobby repo): `voice/transcribe` is text-only and `WhisperSTT` discards faster-whisper
    segments (`stt.py:164`); `describe_image` is path-based + internal-only and `chat_attachments` is upload-only;
    `GET /api/voice/status` already exists; `get_provider` builds only claude/codex/local while config advertises
    deprecated gemini/grok/qwen (`llm_providers.py:88`) — the daemon cleanup (namespace split, summarizer→`call_feature`,
    factory/resolver error fix) is tracked in `gwiki-daemon-web.md`, not gobby-cli;
  - **AGY = Antigravity CLI** (Google) — a runtime `cli_adapter`, registered unavailable/partial until transport parity;
    daemon-owned, out of gobby-cli scope;
  - **D5 classifier gap**: the daemon baseline state classifier recognizes `code_*` but not `gwiki_*`
    (`storage/hub/postgres.py:395-449`) — surfaced in the hub-install contract (§6.1.3).

**Round 3 (adversarial — expansion-readiness blockers)**

- reviewer: external (codex / gobby agent)
- verdict: incorporated
- blockers fixed:
  - **feature graph**: gwiki gains `ai = ["gobby-core/ai"]` with **`default = ["rustls", "ai", "documents"]`**; the gcore `ai` feature is flagged
    as a public-boundary change requiring `crates/gcore/tests/public_boundary.rs` updates (C1, P2.1);
  - **config surface**: added `provider` (daemon forwarding), `audio_translate.target_lang`, and video
    `frame_interval_seconds` to `CapabilityBinding`/`AiContext` with env keys + a precedence test (A1, P1.1, P1.2);
  - **partial standalone hub**: a reachable Postgres without `config_store` falls through to `gcore.yaml`/defaults rather
    than erroring, with a test (P1.2);
  - **translation algorithm**: defined the exact ordering — `/v1/audio/translations` is a one-pass self-detecting
    English path needing no pre-pass source check; the `source==target` skip applies only to post-transcription
    arbitrary-target LLM translation; a `language` hint short-circuits detection (P4.2);
  - **partial-result type**: chunking returns `ChunkedTranscription { segments, completed_ranges, missing_ranges,
    partial }`, keeping the per-chunk client all-or-error; P5.3 consumes it (P4.3, P5.3);
  - **same-hub policy**: §8.5 decides identity by a read-only `pg_control_system().system_identifier` + database-name
    probe (no marker table, ownership-neutral) (§8.5);
  - **gcore boundary**: `ensure_hub`'s reachability/identity probe is `#[cfg(feature = "postgres")]`-gated; `provisioning`
    stays always-compiled; public-boundary test updated (§8.4);
  - **gcode paths**: §8.3 retargeted to the real flat `commands/symbols.rs` + `Command::Outline { file }` (`cli.rs:267`),
    no invented `symbols/` module;
  - **ffmpeg boundary**: short audio under the byte cap (and unknown-duration audio) transcribes verbatim, bypassing
    ffmpeg/ffprobe; ffmpeg required only for chunking + video (P4.3);
  - **concurrency owner**: a single shared limiter is owned by `AiContext` and threaded through transcription, chunking,
    vision, text, and video sequencing (B1, P1.2, P2.1).

**Round 4 (interactive — daemon-plan alignment, 0.5.0 capability registry)**

- reviewer: gobby daemon agent ("0.5.0 AI Capability Registry Boundary") + interactive alignment check
- verdict: aligned; CLI plan reconciled
- reconciliations:
  - confirmed the 1:1 capability set, the five daemon routes, the ownership split, and "share the contract, not code";
  - **provider availability**: Gemini/Grok/Qwen/Droid become real `text_generate` providers via daemon **ACP adapters**
    (only **agy/Antigravity** stays unavailable until transport parity) — A2 wording corrected (it had lumped them as
    unavailable);
  - **gcode embeddings is a breaking 0.5.0 rename to `ai.embeddings.*` with no aliases/shims**, mirroring the daemon's
    removal of `llm_providers.*` generation config; old keys are not honored; migration is docs/changelog only (§8.2).

**Round 5 (adversarial — cross-crate AI coherence + rate limiting)**

- reviewer: external (codex / gobby agent) + user (rate-limit requirement)
- verdict: incorporated
- blockers fixed:
  - **#5 routing owner (the structural repair)**: `AiContext`, the per-capability router, result types, and the capability
    probe all move to `gobby_core` (`ai_context` + `ai`), consumed identically by gwiki **and** gcode — one AI stack, not
    three (C1, A1, §1.2, §3.1, §3.3);
  - **#1 limiter location**: the concurrency limiter is always-compiled in `gobby_core::ai_context` (not feature-gated
    `ai`), borrowed by clients, so the no-`ai` build links (B1, P1.2, P2.1);
  - **#2 numeric timestamps**: gwiki `TranscriptSegment` holds numeric `start_seconds`/`end_seconds`; string format only
    in Markdown (P3.1);
  - **#3 daemon contract**: daemon clients auth with `X-Gobby-Local-Token` (`~/.gobby/local_cli_token`), multipart `file`
    for audio/image, JSON for text, `project_id` only when resolvable (P2.4);
  - **#4 vision OCR**: `VisionResult { description, model, metadata }` — OCR folds into `description`, no separate field
    (P2.1, P5.1);
  - **#6 CI**: adds `cargo test -p gobby-core --features ai` so transport tests run (P7.1);
  - **#7 release ordering**: gcore is bumped + published with `ai` first and gwiki's dep updated, before gwiki publishes
    (P7.2);
  - **#8 config naming**: exact env stems `GOBBY_AI_EMBEDDINGS_*` (old `GOBBY_EMBEDDING_*` ignored), store
    `ai.embeddings.*` (P1.1, §8.2);
  - **#9 provisioning writers**: `provisioning.rs:513-518`/`:123` + `setup.rs:264` + `resolve_embedding_config` move to
    `ai.embeddings.*` with their tests (§8.2);
  - **#10 capability-aware discovery**: LM Studio/Ollama auto-discovery serves only text/vision/embed; STT requires an
    explicit endpoint and is never auto-routed to a chat backend (§8.1);
  - **other fixes**: concrete defaults (`max_concurrency=1`, 60/120 s timeouts, window/overlap); forced-routing + `--no-ai`
    override tests (1.2.5); `language` in the STT signature (P2.2); structured **indexed-JSON** segment-wise translation
    with validation fallback (P4.2); `keep_alive` sent only to providers that accept it (B1);
  - **rate limiting (user)**: transport backoff is **exponential with jitter on HTTP 429**, honoring `Retry-After`, for
    non-local OpenAI-compatible (cloud) APIs; the `max_concurrency` limiter is the first line of defense (P2.1).

**Round 6 (adversarial — spec contradictions & ownership leaks + user OCR challenge)**

- reviewer: external (codex / gobby agent) + user (OCR + frame-interval questions)
- verdict: incorporated
- blockers fixed:
  - **#1 router/probe feature boundary**: split the routing decision — always-compiled `ai_context::route` returns the
    *config-only desired* routing (`Auto` stays `Auto`); the feature-gated `gobby_core::ai::effective_route` does the
    probe-backed collapse to daemon/direct/off, so no-`ai` code never calls the probe (A1, §1.2, §3.1);
  - **#2 numeric timestamps vs video alignment**: timestamps are **integer milliseconds** (`start_ms`/`end_ms: u64`), not
    `f64` — preserves the existing `#[derive(Eq)]` chain and lets `align_transcript_and_frames` (`video.rs:81,102,118`)
    read `start_ms` directly instead of parsing strings; wire float-seconds convert on parse (A1, P2.1/P2.2, P3.1/3.1.3,
    P3.2, P4.3, P5.2);
  - **#3 embedding config naming**: canonical `_API_BASE` stem — `GOBBY_AI_EMBEDDINGS_API_BASE/_MODEL/_API_KEY`,
    `ai.embeddings.api_base/model/api_key` — matching §1.1's `GOBBY_AI_<CAP>_API_BASE` vocabulary (§8.2/8.2.2);
  - **#4 vector-dim migration (+ cross-repo unification)**: `GOBBY_EMBEDDING_VECTOR_DIM`/`embeddings.vector_dim`
    (`context.rs:39-40`) move to `GOBBY_AI_EMBEDDINGS_DIM`/**`ai.embeddings.dim`** — adopting the daemon's existing `dim`
    key so the rename *unifies* the dimension config split today (gcode `vector_dim` vs daemon `embeddings.dim`) and
    resolves the `semantic_search.py:184` guard; the daemon-side writer/readers + one-time `config_store` migration +
    co-release constraint are pinned as **P6 D6** (§8.2/8.2.2, §6.1/6.1.4);
  - **#5 secret-resolution ownership**: `AiContext` consumes a **caller-provided `ConfigSource`** whose `resolve_value`
    does `$secret:`/`${VAR}` expansion — gcode keeps `secrets::resolve_config_value` (Fernet, `config/services.rs:25`),
    gwiki keeps its own; Fernet does not move into gcore (§1.2);
  - **#6 embed avoids daemon auto-routing**: the daemon's embeddings route is reindex-only, so `embed`'s `Auto` resolves
    direct → local discovery → off, never daemon, until the daemon owns real embedding generation (A2, §8.2/8.2.1);
  - **#7 vision OCR (reverses Round 5 #4, per user)**: OCR stays a **distinct field** —
    `VisionResult { description, ocr_text: Option<String>, model, metadata }` — because verbatim in-image text is a
    high-value, separately searchable retrieval signal for a wiki; gcore *gains* `ocr_text` (vision client prompts for
    structured `{description, ocr_text}` with a prose-only fallback), gwiki's existing `VisionExtraction.ocr_text` +
    `## OCR Text` renderer stay as-is, and the daemon D2 contract carries `ocr_text?` optionally (A1, P2.1, P2.3/2.3.1,
    P5.1/5.1.1, §6.1 D2);
  - **#8 frame interval leak**: there is no `video` AI capability — frame-sampling cadence is a **gwiki ingest/media
    policy** under `gwiki.ingest.video_frame_interval_seconds`, resolved CLI > env > config_store > gcore.yaml > default;
    removed from gcore's `CapabilityBinding`/env vocabulary (A1, P1.1/1.1.4, §1.3, §5.2);
  - **#9 inbox collect**: declared **explicitly out of scope** — `ingest-file` is the multimodal entry; `collect`
    (`collect.rs:133`) keeps storing dropped media as raw preserved assets without AI derivation; routing it through the
    orchestrators is a tracked follow-up (P1 scope boundary);
  - **#10 retry count**: locked to **at most 2 retries (3 attempts total)**, backoff 250 ms → 500 ms honoring
    `Retry-After`, consistent with acceptance 2.1.2 (P2.1).

**Round 7 (interactive — embeddings-migration de-risking, cross-repo)**

- reviewer: user (cross-repo coordination question) + gobby-repo investigation
- verdict: incorporated
- findings resolved:
  - **verified the daemon's embedding-config surface** (gobby repo): writer
    `cli/installers/embedding.py::_persist_embedding_config` emits `embeddings.model/api_base/dim` to `config_store`;
    readers are `EmbeddingsConfig` (`config/persistence.py`) → `servers/http.py`, `code_index/sync_worker.py`,
    `ai/registry.py` (the embed capability), `memory/vectorstore.py`/`knowledge_graph/code_linker.py`/`cli/memory/
    indices.py`, `utils/deps.py`, `runner_init/storage.py`, `search/models.py`, `mcp_proxy/semantic_search.py`, and the
    settings-UI config routes;
  - **dimension key was split pre-existing** — gcode `embeddings.vector_dim` vs daemon `embeddings.dim` (the
    `semantic_search.py:184` guard) — so Round 6 #4 is corrected to unify on **`ai.embeddings.dim`** (daemon's name), which
    *fixes* the split rather than carrying it forward (§8.2/8.2.2, §6.1 D6);
  - **migration strategy = expand/migrate/contract with dual-write/dual-read** (user choice), captured as a **separate
    cross-repo P0 epic P0E** (E1 expand: key constants + CI guard, probe-based advisory dim, dual-read, daemon dual-write,
    pre-built `config_store` migration, contract doc + doctor; E2 migrate; E3 contract = this epic's §8.2 + D6). This
    **removes the same-window co-release constraint** — gobby-cli 0.5.0 and the daemon ship independently — while keeping a
    **shim-free end state** (P0E, §8.2, §6.1 D6/6.1.4);
  - P0E is framing-only here (not in this epic's manifest) and is extracted to
    `.gobby/plans/embeddings-namespace-migration.md` for its own adversarial expansion.

**Round 8 (adversarial — internal contradictions + ownership leaks; user P8-split context)**

- reviewer: external (codex / gobby agent) + user (P8 expansion-model context)
- verdict: incorporated (P8 split reinterpreted per the expansion model, not file-split)
- blockers fixed:
  - **#1 result-type ownership contradiction (the real blocker)**: C1 said result types are always-compiled in gcore while
    A1/P2.1 placed them inside the feature-gated `gobby_core::ai`. Resolved by **defining the pure result/error data types
    (`TranscriptionResult`/`VisionResult`/text/`AiError`) in always-compiled `ai_context`** and leaving only the
    *transport mechanics* (request building, wire-JSON parsing into those types, retry/backoff) and the probe/effective
    router behind `ai` — so consumer signatures and the C1 guarantee hold in lean builds (C1, A1, P2.1);
  - **#2 local_backend lean-core leak**: an always-compiled `gobby_core::local_backend` doing `ureq` HTTP probes violated
    the HTTP-free lean-core boundary — split so the **`Backend` data type + defaults are always-compiled** while
    **`detect_backend`/`validate_backend` (ureq probes) are gated behind `ai`**; gloc and gcore::ai both enable the gate
    (A1, §8.1/8.1.1a);
  - **#3 dispatch double-registration**: `ingest_path` must **branch by kind before the generic `SourceManifest::register`
    (`file.rs:47`)** and delegate media entirely to the orchestrators (which self-register at `audio.rs:73`/`video.rs:60`),
    so a `.mp3` registers exactly once instead of generic-plus-media (§1.3/1.3.4);
  - **#4 translation routing under-specified**: `audio_translate` is a distinct capability but had no flag — resolved by
    making **`--transcription-routing` govern both STT capabilities** and **`audio_translate`'s binding inherit
    `audio_transcribe`'s** when unset (one whisper server, B1), with `ai.audio_translate.*` still overriding (§1.1/1.1.5,
    §1.3/1.3.5);
  - **#5 probe needs capability-level truth, not HTTP 200**: because `audio_transcribe`/`audio_translate` share
    `GET /api/voice/status`, the probe now **parses the status body's advertised capability list** and routes a capability
    to the daemon only when advertised present — degrading an advertised-absent capability even on a reachable endpoint;
    the daemon D1/D4 contract makes the status routes advertise capability-level support (§3.3/3.3.3, §6.1 D1/D4/6.1.2);
  - **#6 project_id from cwd was wrong**: `project_id` is now **caller-supplied** — **gwiki sources it from the resolved
    `ScopeIdentity`** (topic/global → `None` even inside a `.gobby/project.json` cwd; project scope → its id), gcode keeps
    its cwd-rooted resolution — so topic/global ingest never forwards a stray cwd project (§1.2/1.2.3);
  - **#8 release publishes gcore from the wrong workflow**: `release-gwiki.yml` now only **verifies** the pinned
    `gobby-core` (≥ 0.3.0 with `ai`) is on crates.io and fails fast otherwise; **publishing gcore stays in gcore's own
    release path** (§7.2/7.2.2);
- reinterpreted (not a code change):
  - **#7 "split P8 into a downstream epic"**: the reviewer assumed a single-shot implementation train. Per the user, the
    gobby **epic→subtask expansion** turns P8's `depends: P2+` edges into **gated subtasks scheduled after the P1–P7 MVP**,
    so P8 does not compete with the MVP and needs **no separate plan file**. Made the gate explicit in **R1 and the P8
    framing**; P0E remains file-split only because it is *cross-repo*, an orthogonal reason (R1, P8 framing);
- good calls confirmed (no change): integer-ms `start_ms`/`end_ms` (Round 6 #2), distinct `ocr_text` (Round 6 #7), vision
  probe moved off `/api/chat/attachments` (§3.3), and partial-hub/`config_store`-absent fall-through (§1.2.4).

**Round 9 (adversarial — daemon audio contract refresh + result-module naming)**

- reviewer: external (codex / gobby agent), against the *current* daemon audio config
- verdict: incorporated; reviewer flagged expansion-ready after these edits
- must-fix:
  - **#1 daemon audio contract refresh**: the daemon now exposes a **`voice.openai_compatible_audio` binding** (`provider`,
    `url`, `model`, optional `api_key`, `transcription_enabled`, `translation_enabled`, `timeout_seconds`) and
    `/api/voice/transcribe` accepts multipart **`capability`/`provider`/`model`/`language`/`prompt`**. Updated: the §2.4
    daemon voice client sends those fields (`capability` from `task`); the §3.3 probe reads `transcription_enabled`/
    `translation_enabled` off `/api/voice/status` as the per-capability truth; D1 documents the binding + multipart fields
    (§2.4/2.4.4, §3.3/3.3.3, §6.1 D1/6.1.1/6.1.2);
  - **#2 result-module rename**: moved the pure result/error types out of `ai_context` into a dedicated always-compiled
    **`gobby_core::ai_types`** (`TranscriptionResult`/`VisionResult`/text/`AiError`); `ai_context` keeps
    routing/context/limiter, `ai_types` keeps data, `ai` keeps transport — same boundary, cleaner API (C1, A1, P2.1/2.1.1a,
    §5.1);
- should-fix:
  - **#3 inheritance fields enumerated**: `audio_translate` inherits exactly `routing`/`api_base`/`api_key`/`model`/
    `provider`/`transport` from `audio_transcribe`; `target_lang` stays local (and `task`/`language` stay local to
    transcribe) (§1.1/1.1.5);
  - **#4 truth-source precedence**: the **GET status route is checked first** for cheap per-capability availability;
    `/api/providers/models` is consulted **only** for provider/model discovery, never availability (§3.3/3.3.4, §6.1 D4/
    6.1.2);
  - **#5 P8 gate as a validation condition**: "P1–P7 MVP gate before P8" is now a **checkable expansion-validation
    invariant** in VS1 (every P8 deliverable transitively `depends:` on the MVP; no P1–P7 deliverable depends on P8; a
    manifest violating this is rejected), not just prose (VS1, P8 framing);
- good now (reviewer-confirmed, no change): double-registration fix (§1.3), caller-supplied `project_id` (§1.2), P0E
  dual-write/read removing the cross-repo release trap, `ai.embeddings.dim` unification (§8.2), release-workflow
  correction (§7.2).

**Round 10 (adversarial — wire-value + feature-graph correctness)**

- reviewer: external (codex / gobby agent), against current daemon code
- verdict: incorporated; reviewer flagged expansion-ready after these edits
- must-fix:
  - **#1 voice `capability` wire values**: the daemon defaults the `capability` multipart field to
    `AICapability.AUDIO_TRANSCRIBE.value`, so the wire values are **`audio_transcribe`|`audio_translate`** (default
    `audio_transcribe`), **not** `transcribe`/`translate` — the latter is only the faster-whisper `task` the daemon
    *returns*. Corrected the `capability` field everywhere it appears (§2.4/2.4.4, §6.1 D1), keeping the distinct returned
    `task` semantics;
  - **#2 `ureq` feature graph**: §8.1's `ureq` local-backend probes had no dependency declared under `ai`
    (`= ["dep:reqwest", "reqwest/multipart"]`). Added a dedicated **`local_backend = ["dep:ureq"]`** feature gating the
    probes, with **`ai = [..., "local_backend"]`** pulling it for discovery and **gloc enabling `local_backend` alone**
    (no `reqwest`, keeping the tiny binary lean). Expanded the bare-baseline check to assert **neither `reqwest` nor
    `ureq`** links in the baseline (C1, P2.1/2.1.1, §8.1/8.1.1a, A1 gloc bullet);
  - **#3 `AiError` transport-neutrality**: added explicit acceptance that `ai_types::AiError` carries **no
    `reqwest::Error`/`ureq::Error` or any gated transport type** — only transport-neutral data (`status: Option<u16>`,
    `body`/`source` strings, typed variants: capability error / not-configured / transport failure / parse failure) — so
    the always-compiled error type leaks no feature (P2.1/2.1.1b);
- looks good (reviewer-confirmed, no change): the `ai_types` split, the `voice.openai_compatible_audio` binding reflected
  in probe/docs, status-route-as-availability vs providers/models-as-discovery, the checkable P8 gate, and P0E isolation.

**Round 11 (interactive — migration ownership + no-env config; user directives)**

- reviewer: external (codex / gobby agent, against the live daemon repo) + user (key-naming + no-env directives)
- verdict: incorporated
- findings resolved:
  - **§8.2 must depend on the migration epic, not re-own the cut**: §8.2 is reframed as a **downstream consumer with a
    hard cross-epic dependency on `embeddings-namespace-migration`'s Contract phase**; the no-alias rename, the full key
    inventory, the gcore.yaml/`config_store` writers, and the api-key secret all move out of §8.2 into that epic. Dropped
    `provisioning.rs`/`setup.rs` from §8.2 targets and acceptance 8.2.3; reframed 8.2.2; P0E framing updated so the
    Contract (`## P3`) is owned by the migration epic, with §8.2 consuming it and §6.1 D6 only *documenting* it CLI-side;
  - **key naming = embeddings-namespaced, not `openai` (user)**: the api-key secret is `ai.embeddings.api_key` →
    `$secret:embeddings_api_key`, **copied** (not moved) from the daemon's existing `openai_api_key` so the shared LLM key
    is not orphaned;
  - **no env vars as an AI-config source (user)**: removed the entire `GOBBY_AI_*` / `GOBBY_EMBEDDING_*` env vocabulary —
    AI config (incl. routing, per-capability bindings, tuning, frame interval) resolves **only** `config_store` (DB) →
    `gcore.yaml` (standalone) → defaults, plus **CLI flags** for per-invocation overrides (flags are not env vars). The
    `${VAR}` env expansion is dropped for AI config (secrets resolve via `$secret:` Fernet only); the standalone
    `embeddings.api_key_env` env-indirection is **retired**, with the standalone key living in `gcore.yaml` as
    `ai.embeddings.api_key` (a `$secret:` ref). DB-DSN discovery (hub location) is unaffected — it is infra, not AI config
    (C1/S1, §1.1/1.1.3, §1.2/1.2.2, §1.3, §5.2, §8.2);
  - **migration prompts (kept in chat) revised** to canonical `## P1/P2/P3` phases, the full gcode key inventory
    (`query_prefix`/`provider`, retired `api_key_env`), the daemon runtime config-model decision (normalize `ai.embeddings.*`
    onto the existing `config.embeddings` at load), the api-key custom write path (is_secret-preserving, copy-not-move),
    a fully-specified cross-repo `embeddings doctor`, an allowlisted CI key-literal guard, the no-env contract, and
    dropping the nonexistent `gwiki-daemon-web.md` "D6" as a daemon gate.

**Round 12 (interactive — live config-store reality check; user)**

- reviewer: user + live `config_store` inspection (this daemon-managed install)
- verdict: incorporated
- findings resolved:
  - **confirmed the current state**: `config_store` already holds `embeddings.{api_base,model,dim,api_key}` (LM Studio:
    `http://localhost:1234/v1`, `text-embedding-nomic-embed-text-v1.5@f16`, dim `768`), and `ai.embeddings.*` does not
    exist yet — so the migration target is real and unstarted. The dim is under the daemon's `embeddings.dim` (gcode's
    `embeddings.vector_dim` is absent), confirming the split this epic unifies on `ai.embeddings.dim`;
  - **api_key storage is mode-specific**: attached daemon `config_store` should preserve secret metadata and may resolve
    `ai.embeddings.api_key` via `$secret:embeddings_api_key` (`is_secret=true`); daemonless standalone has no secret store,
    so `~/.gobby/gcore.yaml` may hold the optional `ai.embeddings.api_key` as a plaintext local user token. The migration's
    daemon api-key step preserves `is_secret` and the secret reference via a custom write path (not `set_many`/`set_secret`),
    keeping the embeddings-namespaced secret name (§8.2; migration prompts decision #2 reframed).

**Round 13 (interactive — migration-plan accuracy mirror; reviewer)**

- reviewer: external (codex / gobby agent) against the live daemon repo
- verdict: incorporated (edits applied to the `embeddings-namespace-migration.md` plans in both repos; mirrored here in
  §6.1 D6 for consistency)
- findings resolved:
  - **`configuration_ui_settings.py` is not an embedding writer**: it persists only `ui_settings.*`, so it was dropped
    from the D6 reader/writer inventory (and from the daemon migration plan's writer scope) — only `configuration_values.py`
    writes embedding config (a future settings form would matter solely if it writes through `/config/values`);
  - **repo-specific old dim key made explicit**: canonical is `ai.embeddings.dim`; the old key differs by repo (daemon
    `embeddings.dim`, gcode `embeddings.vector_dim`), and each repo's P1 dual-read maps **its own** old key into the
    canonical (D6, migration plans' C1/P1);
  - **doctor JSON gains `api_key_fingerprint`** (migration plans only — the gwiki plan names the doctor but carries no
    field list): the shared-contract shape is now `{endpoint, model, dim, api_key_present, api_key_fingerprint,
    namespace_resolved, source, agrees, drift}`, with `api_key_fingerprint` the `sha256[:8]` redaction (`string | null`).

**Round 14 (adversarial — migration breaking-change honesty, P8 gate integrity, doctor contract)**

- reviewer: external (codex / gobby agent) against the live gobby-cli code + user (breaking-change directive)
- verdict: incorporated
- findings resolved:
  - **#1 P1 env-removal is breaking, not "non-breaking" (migration plan)**: the env layer is removed at P1 while the live
    resolver still reads `GOBBY_EMBEDDING_*` (`crates/gcore/src/config.rs:168`) and `GOBBY_EMBEDDING_VECTOR_DIM`
    (`crates/gcode/src/config/services.rs:203`). Per user — **keep it breaking at P1** (do not defer to P3); the fix is
    honesty: the migration plan's R1/P1/§1.3 now state the *namespace* dual-read is non-breaking but P1 deliberately drops
    the `GOBBY_EMBEDDING_*` env layer as an accepted breaking change (no-env decision). Also closed a coverage gap —
    `crates/gcode/src/config/services.rs` (the dim env read) is now in §1.2's Target;
  - **#2 P8 MVP-gate invariant was violated by the actual DAG**: VS1 requires every P8 deliverable to transitively
    `depends:` on the P1–P7 MVP, but §8.1 only declared `depends: P2`, §8.4 declared none, and §8.5 chained to §8.4 — so
    the closure never reached the MVP. Added `P5, P6, P7` to the two P8 roots (§8.1, §8.4); §8.2/§8.3 (via §8.1) and §8.5
    (via §8.4) now inherit the gate, making the invariant true in the headings, not just the prose;
  - **#3 doctor exit codes + drift schema were undefined (migration plans)**: both doctors now spell out the shared
    exit-code contract — `0` healthy / `10` config-unresolved / `11` drift / `20` probe-failure — and the `drift` JSON
    shape (`null` when agrees∈{true,null}, else `[{field, self, peer}]` over endpoint/model/dim), so gcode and the daemon
    cannot diverge on meanings.

**Round 15 (interactive — document ingestion + robust code→wiki; user)**

- reviewer: user direction + landscape research (deepwiki-open, CodeWiki, autodoc, gitsummarize, Unstructured.io,
  markitdown)
- verdict: incorporated
- findings resolved:
  - **document ingestion folded into the epic**: PDF/Office/HTML/structured-text become derived Markdown behind a
    default-on `documents` feature (P1 §1.3 dispatch + new `SourceKind::Office`/`Html`; P5 §5.4–5.6). **PDF combines** the
    text layer (`pdf-extract`) with vision (`pdfium-render` page raster → `vision_extract` OCR + figure/chart
    descriptions) — *not* a fallback (user); Office via `calamine` + `zip`/`quick-xml`; HTML via the existing `scraper`;
    structured text (`csv/json/jsonl/xml/yaml/toml/log`) inlined as size-capped `Text`. Lean `--no-default-features`
    degrades PDF/Office to store-as-asset; gcore unaffected;
  - **pdfium-render with statically bundled pdfium** chosen (user) for full-page rasterization quality with no external
    runtime binary; CI fetches pdfium, rasterization tests env-gated like ffmpeg; gwiki gains an `opt-level="z"` override
    to bound the size hit;
  - **robust code→wiki added as new phase P9** (user: "rich, in this epic"): a `gcode codewiki` generator producing
    hierarchical file→module→repo docs, graph-derived Mermaid, `file:line` citation grounding, and incremental regen,
    reusing gcode's AST + FalkorDB graph + this epic's `text_generate`; **gwiki ingests** the generated Markdown as a new
    `SourceKind::CodeDoc`. **`crate_has_no_gcode_dependency` kept** (user) — generator in gcode, output ingested by gwiki,
    file/CLI seam, no crate link (rationale: gcode is the heavy crate; share-via-gcore layering; independent release).
    Prompts adapted from CodeWiki/autodoc/gitsummarize/llama_index — prompts aren't licensed, so no attribution required;
  - **VS1 expansion invariant extended to P9** (every P8/P9 deliverable transitively `depends:` on the P1–P7 MVP — P9 via
    §8.3; no P1–P7 depends on P9); R1 DAG updated (P5 now covers documents; P9 downstream after P8);
  - **doc paths corrected to `docs/guides/`** (repo convention) for the epic-created docs (codewiki, ai-daemon-contract,
    hub-install-contract, ai-configuration).

**Round 16 (stage-native planner — task-manifest authoring)**

- reviewer: stage-native planning pipeline (planner.yaml); pre-adversary draft gate
- verdict: incorporated
- changes:
  - **`## M1 Task Manifest` authored** by the stage-native planner per the planner.yaml TASK MANIFEST contract — one
    entry per `kind: deliverable` section (35 entries; all 91 acceptance items carried as
    `covers:gwiki-multimodal-ai:<section>:<item>` labels, one per item). **Supersedes the Round 0 deferral note**: in the
    stage-native flow the planner emits the manifest once the plan is expansion-ready (reviewer-confirmed Rounds 9–10),
    and the approving adversary preserves planner-supplied category/domain decisions per the Manifest-on-Approval
    contract (`docs/contracts/plan-coverage.md`);
  - **phase-level `(depends: P<N>)` headings translated to leaf `depends_on`** using each phase's terminal leaves
    (P1→1.3, P2→2.4, P5→[5.3, 5.6], P6→6.1, P7→[7.2, 7.3]) — phase IDs are invalid in `depends_on`;
  - **VS1 MVP-gate invariant preserved in the manifest DAG**: every P8/P9 entry transitively `depends_on` the P1–P7 MVP
    and no P1–P7 entry depends on P8/P9 (verified by transitive-closure check); leaf DAG is acyclic;
  - category→TDD per contract: `code`→`tdd: true`; `config`/`docs`/`refactor`→`tdd: false`; every entry carries
    `implementation_domain: backend`;
  - fixed a `target-coverage` semantic-lint finding in §8.2: reworded "the api-key storage **split**" to "…**policy**" so
    the migration-epic-owned `gcore.yaml` reference (explicitly **not** an §8.2 change target — Round 11) no longer reads
    as a change-intent path; §8.2's `Target:` inventory (the two `crates/gcode/...rs` files) is unchanged;
  - self-checked against the Plan-Coverage Contract (1:1 manifest↔deliverable, every `covers:` label resolves to a real
    acceptance item, every `depends_on` resolves to another entry, acyclic leaf DAG, P8/P9→MVP gate closure) — `gobby
    plans validate` (draft) passes, `parse_mode="expansion"` parses 35 entries 1:1 with deliverables, semantic lint clean.

**Round 17 (stage-native planner — adversary Round 16 blocking fixes)**

- reviewer: stage-native planning adversary (Round 16 findings F1, F2)
- verdict: incorporated (surgical)
- blockers fixed:
  - **F1 bad-sequencing (§7.1 CI vs feature-producing phases)**: §7.1 (the CI task that builds `gobby-core --features ai`
    and runs the default-on `documents` tests) was gated only on `(depends: P1)` → manifest `depends_on: ["1.3"]`, so
    expansion could schedule it before the `ai` transport (P2) and document-extraction (P5) surfaces exist. Re-gated §7.1
    to **`(depends: P5)`** and its manifest entry to **`depends_on: ["5.3", "5.6"]`** (P5's terminal leaves), which
    transitively orders it after P2 (5.x → … → 3.1 → P2) and the `documents` feature (5.6). §7.2 already sits behind §7.1
    (`(depends: 7.1)` / `depends_on: ["7.1"]`), so the release workflow inherits the gate;
  - **F2 stale Cargo/release facts (C1, §7.2, VS1)**: corrected the plan against the live repo — `gwiki` links `reqwest`
    via its default-on `rustls` feature (not "unconditionally"; `crates/gwiki/Cargo.toml:14-15,19`), and gwiki's default
    becomes **`default = ["rustls", "ai", "documents"]`** (preserving the existing default-on `rustls`; today
    `default = ["rustls"]`, `crates/gwiki/Cargo.toml:14`), fixed in both C1 and the VS1 feature-graph note. Reframed
    §7.2's release-ordering guard: `gobby-wiki` pins `gobby-core` `0.3.0` via the workspace (`crates/gwiki/Cargo.toml:27`,
    not the stale `0.2.2` / `gwiki/Cargo.toml:26`); the published `gobby-core` carrying the P2.1-added `ai` feature (which
    requires a gcore version bump) must be on crates.io before `gobby-wiki` publishes. P2.1 already correctly describes
    adding the `ai`/`local_backend` features to the current featureless gcore `0.3.0`, so it needed no change;
- whole-plan sweep: the F2 stale-fact class is fully cleared (`0.2.2`, `default = []`, `default = ["ai"]`,
  "reqwest unconditionally", `gwiki/Cargo.toml:26` all now absent) and the F1 sequencing class has no other under-gated
  CI/release task (§7.3 docs → P5; §7.2 → 7.1; §8.1/§8.4 → P5, P6, P7 already gate after the feature phases);
- validation: `uv run gobby plans validate` passes (9 phases, 35 deliverables, consumer sweep passed); manifest stays
  1:1 with deliverables and the leaf DAG remains acyclic with the P8/P9→MVP gate intact.

## M1 Task Manifest

`kind: manifest`

```yaml
- title: "Add gcore AI capability config types and per-capability routing"
  category: code
  task_type: feature
  depends_on: []
  validation_criteria: "cargo test -p gobby-core ai_routing_per_capability_precedence"
  labels:
    - covers:gwiki-multimodal-ai:1.1:1.1.1
    - covers:gwiki-multimodal-ai:1.1:1.1.2
    - covers:gwiki-multimodal-ai:1.1:1.1.3
    - covers:gwiki-multimodal-ai:1.1:1.1.4
    - covers:gwiki-multimodal-ai:1.1:1.1.5
  implementation_domain: backend
  tdd: true
  source_section: "1.1"
- title: "Add shared `gobby_core::ai_context` (AiContext, config source, router)"
  category: code
  task_type: feature
  depends_on:
    - "1.1"
  validation_criteria: "cargo test -p gobby-core resolves_in_db_and_no_db_modes"
  labels:
    - covers:gwiki-multimodal-ai:1.2:1.2.1
    - covers:gwiki-multimodal-ai:1.2:1.2.2
    - covers:gwiki-multimodal-ai:1.2:1.2.3
    - covers:gwiki-multimodal-ai:1.2:1.2.4
    - covers:gwiki-multimodal-ai:1.2:1.2.5
  implementation_domain: backend
  tdd: true
  source_section: "1.2"
- title: "Dispatch ingest-file to orchestrators and add CLI flags"
  category: code
  task_type: feature
  depends_on:
    - "1.2"
  validation_criteria: "cargo test -p gobby-wiki detects_audio_and_image_extensions"
  labels:
    - covers:gwiki-multimodal-ai:1.3:1.3.1
    - covers:gwiki-multimodal-ai:1.3:1.3.2
    - covers:gwiki-multimodal-ai:1.3:1.3.3
    - covers:gwiki-multimodal-ai:1.3:1.3.4
    - covers:gwiki-multimodal-ai:1.3:1.3.5
    - covers:gwiki-multimodal-ai:1.3:1.3.6
    - covers:gwiki-multimodal-ai:1.3:1.3.7
  implementation_domain: backend
  tdd: true
  source_section: "1.3"
- title: "Add gcore `ai` feature and transport skeleton"
  category: code
  task_type: feature
  depends_on:
    - "1.3"
  validation_criteria: "cargo test -p gobby-core ai_error_is_transport_neutral"
  labels:
    - covers:gwiki-multimodal-ai:2.1:2.1.1
    - covers:gwiki-multimodal-ai:2.1:2.1.1a
    - covers:gwiki-multimodal-ai:2.1:2.1.1b
    - covers:gwiki-multimodal-ai:2.1:2.1.2
    - covers:gwiki-multimodal-ai:2.1:2.1.3
    - covers:gwiki-multimodal-ai:2.1:2.1.4
  implementation_domain: backend
  tdd: true
  source_section: "2.1"
- title: "Direct transcription/translation client"
  category: code
  task_type: feature
  depends_on:
    - "2.1"
  validation_criteria: "cargo test -p gobby-core builds_multipart_and_parses_segments"
  labels:
    - covers:gwiki-multimodal-ai:2.2:2.2.1
    - covers:gwiki-multimodal-ai:2.2:2.2.2
  implementation_domain: backend
  tdd: true
  source_section: "2.2"
- title: "Direct vision and text clients"
  category: code
  task_type: feature
  depends_on:
    - "2.1"
  validation_criteria: "cargo test -p gobby-core sends_image_url_and_parses"
  labels:
    - covers:gwiki-multimodal-ai:2.3:2.3.1
    - covers:gwiki-multimodal-ai:2.3:2.3.2
  implementation_domain: backend
  tdd: true
  source_section: "2.3"
- title: "Daemon clients with back-compat mapping"
  category: code
  task_type: feature
  depends_on:
    - "2.2"
    - "2.3"
  validation_criteria: "cargo test -p gobby-core legacy_text_maps_to_single_segment"
  labels:
    - covers:gwiki-multimodal-ai:2.4:2.4.1
    - covers:gwiki-multimodal-ai:2.4:2.4.2
    - covers:gwiki-multimodal-ai:2.4:2.4.3
    - covers:gwiki-multimodal-ai:2.4:2.4.4
  implementation_domain: backend
  tdd: true
  source_section: "2.4"
- title: "Add gwiki thin trait adapters over the shared gcore router"
  category: code
  task_type: feature
  depends_on:
    - "2.4"
  validation_criteria: "cargo test -p gobby-core effective_route_auto_falls_through_per_capability"
  labels:
    - covers:gwiki-multimodal-ai:3.1:3.1.1
    - covers:gwiki-multimodal-ai:3.1:3.1.2
    - covers:gwiki-multimodal-ai:3.1:3.1.3
  implementation_domain: backend
  tdd: true
  source_section: "3.1"
- title: "Add gwiki::media ffmpeg/ffprobe helpers"
  category: code
  task_type: feature
  depends_on:
    - "1.3"
  validation_criteria: "cargo test -p gobby-wiki temp_files_cleaned_asset_survives"
  labels:
    - covers:gwiki-multimodal-ai:3.2:3.2.1
    - covers:gwiki-multimodal-ai:3.2:3.2.2
  implementation_domain: backend
  tdd: true
  source_section: "3.2"
- title: "Repoint the daemon vision capability probe to a GET status route"
  category: code
  task_type: feature
  depends_on:
    - "3.1"
  validation_criteria: "cargo test -p gobby-core capability_status_routes"
  labels:
    - covers:gwiki-multimodal-ai:3.3:3.3.1
    - covers:gwiki-multimodal-ai:3.3:3.3.2
    - covers:gwiki-multimodal-ai:3.3:3.3.3
    - covers:gwiki-multimodal-ai:3.3:3.3.4
  implementation_domain: backend
  tdd: true
  source_section: "3.3"
- title: "Wire audio ingest to production transcription and extend output"
  category: code
  task_type: feature
  depends_on:
    - "3.1"
    - "3.2"
  validation_criteria: "cargo test -p gobby-wiki production_transcription_writes_fields"
  labels:
    - covers:gwiki-multimodal-ai:4.1:4.1.1
    - covers:gwiki-multimodal-ai:4.1:4.1.2
  implementation_domain: backend
  tdd: true
  source_section: "4.1"
- title: "Add language auto-detect and translation precedence"
  category: code
  task_type: feature
  depends_on:
    - "4.1"
  validation_criteria: "cargo test -p gobby-wiki precedence_and_segment_wise"
  labels:
    - covers:gwiki-multimodal-ai:4.2:4.2.1
    - covers:gwiki-multimodal-ai:4.2:4.2.2
    - covers:gwiki-multimodal-ai:4.2:4.2.3
  implementation_domain: backend
  tdd: true
  source_section: "4.2"
- title: "Add deterministic long-media chunking"
  category: code
  task_type: feature
  depends_on:
    - "4.1"
    - "3.2"
  validation_criteria: "cargo test -p gobby-wiki chunks_under_limit_fixed_codec"
  labels:
    - covers:gwiki-multimodal-ai:4.3:4.3.1
    - covers:gwiki-multimodal-ai:4.3:4.3.2
    - covers:gwiki-multimodal-ai:4.3:4.3.3
    - covers:gwiki-multimodal-ai:4.3:4.3.4
  implementation_domain: backend
  tdd: true
  source_section: "4.3"
- title: "Wire image ingest to production vision"
  category: code
  task_type: feature
  depends_on:
    - "3.1"
  validation_criteria: "cargo test -p gobby-wiki production_vision_writes_description_and_ocr"
  labels:
    - covers:gwiki-multimodal-ai:5.1:5.1.1
  implementation_domain: backend
  tdd: true
  source_section: "5.1"
- title: "Wire video to audio-first transcript plus real frames"
  category: code
  task_type: feature
  depends_on:
    - "4.1"
    - "4.3"
    - "3.2"
    - "5.1"
  validation_criteria: "cargo test -p gobby-wiki video_produces_transcript_and_frames"
  labels:
    - covers:gwiki-multimodal-ai:5.2:5.2.1
    - covers:gwiki-multimodal-ai:5.2:5.2.2
  implementation_domain: backend
  tdd: true
  source_section: "5.2"
- title: "Add partial-video degradation matrix and media metadata"
  category: code
  task_type: feature
  depends_on:
    - "5.2"
  validation_criteria: "cargo test -p gobby-wiki partial_failure_matrix"
  labels:
    - covers:gwiki-multimodal-ai:5.3:5.3.1
    - covers:gwiki-multimodal-ai:5.3:5.3.2
  implementation_domain: backend
  tdd: true
  source_section: "5.3"
- title: "Office, HTML, and structured-text document extraction"
  category: code
  task_type: feature
  depends_on:
    - "1.3"
  validation_criteria: "cargo test -p gobby-wiki extracts_office_html_and_degrades"
  labels:
    - covers:gwiki-multimodal-ai:5.4:5.4.1
  implementation_domain: backend
  tdd: true
  source_section: "5.4"
- title: "PDF — text layer combined with vision"
  category: code
  task_type: feature
  depends_on:
    - "5.4"
    - "3.1"
    - "3.2"
  validation_criteria: "cargo test -p gobby-wiki combines_text_layer_and_vision"
  labels:
    - covers:gwiki-multimodal-ai:5.5:5.5.1
  implementation_domain: backend
  tdd: true
  source_section: "5.5"
- title: "Document degradation matrix and metadata"
  category: code
  task_type: feature
  depends_on:
    - "5.4"
    - "5.5"
  validation_criteria: "cargo test -p gobby-wiki document_degradation_matrix"
  labels:
    - covers:gwiki-multimodal-ai:5.6:5.6.1
  implementation_domain: backend
  tdd: true
  source_section: "5.6"
- title: "Author the daemon capability contract (CLI side)"
  category: docs
  task_type: documentation
  depends_on:
    - "3.3"
  validation_criteria: "Author the daemon capability contract (CLI side): target docs written, reviewed, and consistent with the cited routes/contract"
  labels:
    - covers:gwiki-multimodal-ai:6.1:6.1.1
    - covers:gwiki-multimodal-ai:6.1:6.1.2
    - covers:gwiki-multimodal-ai:6.1:6.1.3
    - covers:gwiki-multimodal-ai:6.1:6.1.4
  implementation_domain: backend
  tdd: false
  source_section: "6.1"
- title: "Add gwiki and the gcore ai feature to CI"
  category: config
  task_type: chore
  depends_on:
    - "5.3"
    - "5.6"
  validation_criteria: "Add gwiki and the gcore ai feature to CI: workflow YAML parses (actionlint) and the added CI/release jobs run green"
  labels:
    - covers:gwiki-multimodal-ai:7.1:7.1.1
  implementation_domain: backend
  tdd: false
  source_section: "7.1"
- title: "Add the gwiki release workflow"
  category: config
  task_type: chore
  depends_on:
    - "7.1"
  validation_criteria: "Add the gwiki release workflow: workflow YAML parses (actionlint) and the added CI/release jobs run green"
  labels:
    - covers:gwiki-multimodal-ai:7.2:7.2.1
    - covers:gwiki-multimodal-ai:7.2:7.2.2
  implementation_domain: backend
  tdd: false
  source_section: "7.2"
- title: "Document the AI configuration matrix"
  category: docs
  task_type: documentation
  depends_on:
    - "5.3"
    - "5.6"
  validation_criteria: "Document the AI configuration matrix: target docs written, reviewed, and consistent with the cited routes/contract"
  labels:
    - covers:gwiki-multimodal-ai:7.3:7.3.1
  implementation_domain: backend
  tdd: false
  source_section: "7.3"
- title: "Extract local-backend discovery into gcore and adopt in gloc"
  category: refactor
  task_type: chore
  depends_on:
    - "2.4"
    - "5.3"
    - "5.6"
    - "6.1"
    - "7.2"
    - "7.3"
  validation_criteria: "cargo test -p gobby-core detects_first_reachable"
  labels:
    - covers:gwiki-multimodal-ai:8.1:8.1.1
    - covers:gwiki-multimodal-ai:8.1:8.1.1a
    - covers:gwiki-multimodal-ai:8.1:8.1.2
    - covers:gwiki-multimodal-ai:8.1:8.1.3
  implementation_domain: backend
  tdd: false
  source_section: "8.1"
- title: "Fold gcode embeddings under shared routing"
  category: refactor
  task_type: chore
  depends_on:
    - "8.1"
  validation_criteria: "cargo test -p gobby-code resolves_via_shared_routing"
  labels:
    - covers:gwiki-multimodal-ai:8.2:8.2.1
    - covers:gwiki-multimodal-ai:8.2:8.2.2
  implementation_domain: backend
  tdd: false
  source_section: "8.2"
- title: "Add optional LLM-backed gcode outlines"
  category: code
  task_type: feature
  depends_on:
    - "8.1"
  validation_criteria: "cargo test -p gobby-code summarizes_when_configured"
  labels:
    - covers:gwiki-multimodal-ai:8.3:8.3.1
    - covers:gwiki-multimodal-ai:8.3:8.3.2
  implementation_domain: backend
  tdd: true
  source_section: "8.3"
- title: "Give gwiki shared hub-provisioning parity via `ensure_hub`"
  category: code
  task_type: feature
  depends_on:
    - "5.3"
    - "5.6"
    - "6.1"
    - "7.2"
    - "7.3"
  validation_criteria: "cargo test -p gobby-core --test public_boundary"
  labels:
    - covers:gwiki-multimodal-ai:8.4:8.4.0
    - covers:gwiki-multimodal-ai:8.4:8.4.1
    - covers:gwiki-multimodal-ai:8.4:8.4.2
    - covers:gwiki-multimodal-ai:8.4:8.4.3
  implementation_domain: backend
  tdd: true
  source_section: "8.4"
- title: "Enforce the single-hub invariant across install orders"
  category: code
  task_type: feature
  depends_on:
    - "8.4"
  validation_criteria: "cargo test -p gobby-core no_double_provision_when_reachable"
  labels:
    - covers:gwiki-multimodal-ai:8.5:8.5.1
    - covers:gwiki-multimodal-ai:8.5:8.5.2
    - covers:gwiki-multimodal-ai:8.5:8.5.3
  implementation_domain: backend
  tdd: true
  source_section: "8.5"
- title: "gcode hierarchical code-doc generator (file → module → repo)"
  category: code
  task_type: feature
  depends_on:
    - "8.3"
  validation_criteria: "cargo test -p gobby-code generates_hierarchical_docs"
  labels:
    - covers:gwiki-multimodal-ai:9.1:9.1.1
    - covers:gwiki-multimodal-ai:9.1:9.1.2
  implementation_domain: backend
  tdd: true
  source_section: "9.1"
- title: "Module clustering from the dependency graph"
  category: code
  task_type: feature
  depends_on:
    - "9.1"
  validation_criteria: "cargo test -p gobby-code clusters_modules_from_graph"
  labels:
    - covers:gwiki-multimodal-ai:9.2:9.2.1
  implementation_domain: backend
  tdd: true
  source_section: "9.2"
- title: "Mermaid diagrams from the graph"
  category: code
  task_type: feature
  depends_on:
    - "9.2"
  validation_criteria: "cargo test -p gobby-code emits_bounded_mermaid"
  labels:
    - covers:gwiki-multimodal-ai:9.3:9.3.1
  implementation_domain: backend
  tdd: true
  source_section: "9.3"
- title: "Citation grounding and provenance frontmatter"
  category: code
  task_type: feature
  depends_on:
    - "9.1"
  validation_criteria: "cargo test -p gobby-code citations_validated_against_spans"
  labels:
    - covers:gwiki-multimodal-ai:9.4:9.4.1
  implementation_domain: backend
  tdd: true
  source_section: "9.4"
- title: "Incremental regeneration"
  category: code
  task_type: feature
  depends_on:
    - "9.1"
    - "9.4"
  validation_criteria: "cargo test -p gobby-code incremental_regenerates_only_changed"
  labels:
    - covers:gwiki-multimodal-ai:9.5:9.5.1
  implementation_domain: backend
  tdd: true
  source_section: "9.5"
- title: "gwiki ingest of generated code-docs"
  category: code
  task_type: feature
  depends_on:
    - "9.1"
    - "1.3"
  validation_criteria: "cargo test -p gobby-wiki ingests_codedocs_with_provenance"
  labels:
    - covers:gwiki-multimodal-ai:9.6:9.6.1
    - covers:gwiki-multimodal-ai:9.6:9.6.2
    - covers:gwiki-multimodal-ai:9.6:9.6.3
  implementation_domain: backend
  tdd: true
  source_section: "9.6"
- title: "codewiki CI and documentation"
  category: config
  task_type: chore
  depends_on:
    - "9.1"
    - "9.6"
  validation_criteria: "codewiki CI and documentation: workflow YAML parses (actionlint) and the added CI/release jobs run green"
  labels:
    - covers:gwiki-multimodal-ai:9.7:9.7.1
    - covers:gwiki-multimodal-ai:9.7:9.7.2
  implementation_domain: backend
  tdd: false
  source_section: "9.7"
```
