  Goal: Parity-plus — validate gcode codewiki + gwiki against the leading open-source repo-wiki generators

  Mission

  We built gobby-code (gcode) and gobby-wiki (gwiki) to be a better DeepWiki/OpenDeepWiki/llm-wiki/CodeWiki/Graphify. Neither has been fully put
  through its paces end-to-end. Review our stack crate by crate, benchmark our wiki/codewiki output against those tools, fix what blocks parity-plus,
  and turn everything else into well-scoped tasks. Bias strongly toward analysis, investigation, and task creation over hands-on fixing.

  Definition of done: all deliverables below exist, the parity-plus verdict is supported by evidence in the analysis doc, and a fresh user following
  only docs/guides can reproduce the validated wiki/codewiki output without hitting a documented-but-wrong step.

  Phase 0 — Build & deploy

  1. cargo build --workspace --release
  2. Install gcode, gwiki, gsqz, gloc, ghook into ~/.gobby/bin/ (atomic cp to <name>.new then mv), refresh each .{name}-version sidecar, and run
  ghook --version to rewrite .ghook-runtime.json.

  Phase 1 — Epic with per-crate review tasks

  Create the epic immediately, structured as one review task per crate with dependencies:

  1. gobby-core — first; nothing else starts until it's done.
  2. gobby-code and gobby-wiki — each blocked on the gobby-core review.
  3. gsqz, gloc, ghook — lighter-weight reviews; may run after gobby-core.

  Each review task covers: architecture and seams, correctness risks, error-handling consistency, test-coverage gaps, consolidation opportunities
  (duplicated logic that belongs in gcore), and cleanup stragglers (any legacy/compat/deprecated remnants from prior cleanup passes). Findings do not
  get fixed inline — each becomes a new task in the epic (see execution boundary below). Roll the findings up into ./fable-repo-analysis.md.

  Phase 2 — Competitor feature analysis (not code review)

  For each competitor, do a feature analysis and comparison — what they have implemented vs. what we have. No in-depth code review of their
  codebases; they can spend their own tokens on that.

  ┌──────────────┬─────────────────────────────────────┐
  │     Tool     │                Repo                 │
  ├──────────────┼─────────────────────────────────────┤
  │ DeepWiki     │ AsyncFuncAI/deepwiki-open (~16.8k★) │
  ├──────────────┼─────────────────────────────────────┤
  │ OpenDeepWiki │ AIDotNet/OpenDeepWiki (~3.3k★)      │
  ├──────────────┼─────────────────────────────────────┤
  │ llm-wiki     │ Pratiyush/llm-wiki                  │
  ├──────────────┼─────────────────────────────────────┤
  │ CodeWiki     │ FSoft-AI4Code/CodeWiki              │
  ├──────────────┼─────────────────────────────────────┤
  │ Graphify     │ safishamsi/graphify                 │
  └──────────────┴─────────────────────────────────────┘

  Before cloning each, verify it is the most popular/canonical repo by that name — not a fork or clone (check GitHub stars). Cloning into a temp dir
  and running them locally to inspect real output is allowed and encouraged.

  Compare on concrete dimensions: coverage (files/modules documented), structure & navigation, diagram/graph quality, AI prose quality,
  citations/provenance, incremental-update story, and search over the generated wiki. Record a parity matrix with examples in fable-repo-analysis.md,
  ending in an explicit parity-plus verdict per dimension.

  Scope guards:
  - Web UI parity is not required. If replicating HTML file generation makes sense, a standalone HTML-export utility in gcode/gwiki is acceptable —
  nothing beyond that.
  - Do not redesign our stack. If a competitor capability would require new stack components, write it up in the documentation/analysis as a possible
  future direction — do not implement it and do not create implementation tasks for it.

  Phase 3 — Fresh wiki + codewiki, by the book

  Start from scratch (delete any existing vault/codewiki output — rebuilding from zero is always allowed):

  1. Follow docs/guides/gwiki-user-guide.md and docs/guides/codewiki.md exactly as written — gwiki init/setup, gcode index, gcode codewiki with AI
  prose enabled, ingest into the vault, gwiki index, then exercise search, ask, and compile.
  2. Daemon connectivity is assumed. If the CLI↔daemon contract needs updating, update the daemon side as well — contract parity across repos is
  required, and cross-repo daemon work is in scope.
  3. Treat every inaccuracy, missing step, or friction point in the guides as a doc bug and fix the docs (doc updates are a deliverable Fable works
  directly).
  4. The end state must include AI-generated prose (citation-checked, not AST-only degraded output), verified end-to-end.

  Execution boundary — what Fable works vs. only creates

  Fable works directly (running gobby-sessions:compact_self after completing each leaf task):
  - Parity gaps identified in Phase 2.
  - Bugs that block the end-to-end wiki/codewiki pipeline.
  - End-to-end verification of the wiki/codewiki output.
  - docs/guides and README.md corrections.
  - Daemon-side updates needed for contract parity (cross-repo).

  Fable creates as tasks only (for Josh's review / another agent later):
  - Code-quality findings from the per-crate reviews.
  - Consolidation/simplification opportunities.
  - Legacy/compat straggler removals.
  - New features beyond the parity-plus baseline — documented as possible follow-up tasks, not implemented.

  Hard constraints

  - Never create or suggest compatibility shims or legacy fallbacks for existing functionality or configs. This repo is unannounced and has exactly
  one user. Stragglers get removal tasks, not preservation.
  - Gobby-owned hub schema, project.json, and config_store are not mutated unilaterally from the CLIs — but coordinated schema/contract changes made
  through the daemon (with matching daemon updates) are explicitly allowed.
  - No stack redesign; stack-level additions go into documentation only.
  - Wiki/codewiki output may be wiped and rebuilt from scratch at any point.

  Deliverables

  1. ./fable-repo-analysis.md — per-crate review findings + competitor feature comparison + per-dimension parity-plus verdict.
  2. Updated docs/guides/ and README.md matching observed reality.
  3. A validated, end-to-end wiki/codewiki output with AI-generated, citation-checked prose.
  4. The epic: per-crate review tasks completed; parity-gap/blocking-bug tasks worked (compact_self after each leaf); all other findings filed as
  tasks for later review.
