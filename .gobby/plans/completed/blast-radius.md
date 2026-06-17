 Fix gcode blast radius for cross-file imported call targets (#776)

 Context

 In the gobby project, gcode blast-radius recluster_project_entities and
 gcode blast-radius KnowledgeGraphService return no results even though the
 symbols exist and are called. KnowledgeGraphService.recluster_entities calls
 recluster_project_entities() (imported from another module), but the code graph
 records that call as an UnresolvedCallee node instead of a CALLS edge to the
 canonical function symbol. callers/blast-radius therefore find nothing, because
 blast_radius_query only walks (affected:CodeSymbol)-[:CALLS*]->(target:CodeSymbol).

 Root cause (verified)

 For an intra-project (local) import, the call target is never resolved to the
 canonical local symbol:

 1. Local import bindings are dropped at parse time.
 crates/gcode/src/index/import_resolution/parser/python_js.rs::parse_python_import_statement
 does if !is_external_python_module(module, ctx) { return Ok(()); } for both the
 from X import … and import X forms — so for a local module no per-name
 binding is recorded in ImportBindings.
 2. Resolution falls through. crates/gcode/src/index/parser/calls.rs::materialize_call
 resolves in order: same-file (resolve_same_file_callee_for_language) →
 import_resolution::resolve_external_callee (external-only; returns None for locals)
 → semantic resolver (C/C++ clangd only) → else unresolved. A cross-file local import
 matches none → CallRelation { callee_symbol_id: None, callee_target_kind: Unresolved }.
 3. Projection makes an unresolved node. crates/gcode/src/graph/code_graph/write/mutation.rs::GraphCallTarget::from_call
 emits a CALLS edge to a CodeSymbol only when callee_symbol_id is set;
 otherwise External, otherwise an UnresolvedCallee node (ADD_UNRESOLVED_CALLS_CYPHER).

 Constructor calls compound this: crates/gcode/src/index/parser/calls/resolution.rs::is_callable_kind
 is matches!(kind, "function" | "method") — it excludes "class", so even a
 same-file Service() never resolves to the class symbol.

 Cross-language finding (answer to "does this affect all T1/T2 languages?")

 Yes — it affects every Tier 1/Tier 2 language with module imports. The same
 if !is_external_<lang>(…) { return Ok(()) } guard drops local bindings in every
 parser (JS, Go, Rust, Java, C#, PHP, Kotlin, Swift, Ruby, Dart, Elixir), and
 resolve_external_callee never returns a canonical local symbol id for any
 language. Only same-file calls resolve canonically today. C/C++ are different — they
 resolve via the clangd SemanticCallResolver, which already leaves local definitions
 unresolved (a separate mechanism, separate follow-up).

 Batching ("start with 3, create follow-up tasks"): #776 = the
 language-agnostic core + Python (the repro; matches #776's validation criteria, and
 includes Python relative imports — see below). The other two of the first three
 languages — JavaScript/TypeScript and Rust — are the top-priority follow-up
 tasks built on the now-existing core (JS/TS share the python_js.rs parser; Rust +
 Python are the dominant languages here). Lower-priority follow-ups cover Go, Java, C#,
 Ruby, PHP, Swift, Kotlin, Dart, Elixir, and a separate C/C++ semantic-resolver item.
 (See Follow-up tasks below.)

 Approach

 Resolve cross-file local imports to the canonical CodeSymbol at graph-sync time,
 where it is order-independent, and reuse the existing symbol-call projection.

 Why sync time, not parse time. Symbol IDs are deterministic UUID5 of
 {project_id}:{file_path}:{name}:{kind}:{byte_start} — the id cannot be synthesized; the
 actual indexed target symbol must be looked up. At parse time the target file may not be
 indexed yet (forward references during a full index → order-dependent, flaky). But
 crates/gcode/src/commands/index.rs:48 runs sync::sync_after_index(...) after
 index_files fully completes, so every file's code_symbols rows are already in
 PostgreSQL before graph sync begins. A per-file PostgreSQL lookup at sync is therefore
 order-independent without any final link pass or graph-MATCH Cypher — we just set
 callee_symbol_id and the existing ADD_SYMBOL_CALLS_CYPHER path creates the CALLS edge.

 Carry mechanism (per user decision: explicit kind). Add CallTargetKind::LocalImport
 (persisted as "local_import"). For a local-import call the durable code_calls row is:
 callee_target_kind = "local_import", callee_name = <original imported name> (not the
 alias), callee_external_module = <local module dotted-path> (reusing the existing column
 for "the module the callee lives in"), callee_symbol_id = "". This requires a
 coordinated Python-daemon change — see step D.

 Invariant (do not leak LocalImport + non-empty callee_symbol_id). The persisted
 row stays local_import with an empty callee_symbol_id. Resolution does not
 mutate that row. Instead, at projection time the enrichment helper clones the call and
 applies with_symbol_target(id) (kind → Symbol) for the projection input only. So we
 never rely on the leaky "non-empty id implies Symbol" coincidence in
 from_call/partition_call_graph_items; the projected call is a genuine Symbol target.
 An unresolved local import is left as LocalImport and degrades through from_call's
 default arm to an UnresolvedCallee (same as today — no regression).

 Implementation

 A. Language-agnostic core (gcode)

 1. Models — crates/gcode/src/models.rs
   - Add CallTargetKind::LocalImport; as_str() → "local_import".
   - Add CallRelation::with_local_import_target(callee_name, local_module) (mirrors
 with_external_target): sets kind LocalImport, callee_name = original name,
 callee_external_module = Some(local_module), leaves callee_symbol_id = None.
 2. Module→file reverse map (DB-agnostic) — crates/gcode/src/index/import_resolution/context.rs
 Module-name logic stays in the import-resolution layer, not in db/.
   - Factor the per-path module derivation out of build_python_module_index into
 python_module_names_for_path(rel_path) -> Vec<String> so the forward index and the
 reverse map can never drift.
   - Add build_python_module_file_map(file_paths) -> HashMap<String, Vec<String>>
 (module dotted-path → candidate files; handles mod.py, pkg/__init__.py, src. alias),
 wrapped in a small LocalImportResolver { module_files } with
 candidate_files(&self, module) -> &[String].
 3. DB lookup only — crates/gcode/src/db/queries.rs (keep DB code DB-shaped)
   - call_target_kind_from_str (~line 242): add "local_import" => Ok(CallTargetKind::LocalImport).
 Mandatory — read_calls_for_file bail!s on unknown kinds, so without this any file
 containing a local-import call would hard-error on read-back. (upsert_calls in api.rs
 already persists callee_target_kind/callee_external_module, no change.)
   - Add resolve_local_callee_symbol_id(conn, project_id, target_files: &[String], name):
 SELECT id, kind, parent_symbol_id, file_path, byte_start FROM code_symbols WHERE project_id=$1 AND file_path = ANY($2) AND name=$3 — fetch enough columns
 to enforce
 the selection rule, not just id. In Rust, rank candidates into preference tiers
 (tier 1: top-level function/class with parent_symbol_id IS NULL; tier 2: method),
 pick the unique candidate in the best non-empty tier; if the best tier has >1 candidate
 (after stable ordering by file_path, byte_start), return None (ambiguous → no false edge).
 Accepting a set of candidate files supports package-granularity languages (Go) in follow-ups.
 4. One shared enrichment helper, applied at all three projection read sites.
 Add it in a new crates/gcode/src/projection/local_imports.rs module with a
 pub(crate) export (cleaner than living in sync.rs, since commands/graph/lifecycle.rs
 imports it):
 resolve_local_import_calls(conn, resolver: &LocalImportResolver, facts: &mut GraphFileFacts):
 for each call with callee_target_kind == LocalImport, get candidate files via
 resolver.candidate_files(callee_external_module), call resolve_local_callee_symbol_id, and
 on a hit replace that entry with call.clone().with_symbol_target(id) (kind → Symbol).
 It mutates only the in-memory projection facts — the persisted code_calls row is untouched.
 Build the LocalImportResolver once per run from db::list_indexed_file_paths
 (queries.rs:15) and pass/cache it. Call this helper from all three sites that read
 GraphFileFacts and bypass each other today:
   - crates/gcode/src/projection/sync.rs::sync_graph_file (index-time sync; build the resolver
 once in sync_graph_files before the file loop),
   - crates/gcode/src/commands/graph/lifecycle.rs::sync_file_graph (~line 183, gcode graph sync-file),
   - crates/gcode/src/commands/graph/lifecycle.rs::rebuild_project_graph (~line 257, gcode graph rebuild — build the resolver once before its file loop).

 Then partition_call_graph_items → from_call returns Symbol → ADD_SYMBOL_CALLS_CYPHER
 makes the canonical CALLS edge. No mutation.rs change is needed (an unresolved
 LocalImport keeps the empty id and degrades to UnresolvedCallee via from_call's default).
 This is order-independent everywhere because code_symbols is fully populated by the time any
 of these paths run; for sync-file/rebuild, target symbols persist from prior indexing.

 B. Python capture (parse time)

 5. Bindings — crates/gcode/src/index/import_resolution/context.rs
   - Add LocalImportBinding { module, callee_name } (parallels ExternalImportBinding).
   - Add local_bare: HashMap<String, LocalImportBinding> and
 local_member: HashMap<String, String> to ImportBindings — separate from the
 external bare/member maps so resolve_external_callee is untouched (no external regressions).
 6. Parser — crates/gcode/src/index/import_resolution/parser/python_js.rs
   - In parse_python_import_statement, replace the two local-module return Ok(()) paths.
 Do not blindly mirror the external member insertion — that would create false local
 edges for from pkg import obj; obj.method(). v1 binding rules (binding keys must match the
 call-site root alias exactly as the external path does):
       - from X import Y [as a] (X local) → local_bare[a→Y] = { module: X, callee_name: Y }
 (enables the bare call Y()/a()). Add local_member[a] = "X.Y" only when X.Y is
 itself a known local module (i.e. Y is a submodule, enabling Y.fn()); otherwise add
 no member binding.
     - import X (unaliased, X local) → local_member[<first segment of X>] = X — e.g.
 import pkg.mod → local_member["pkg"] = "pkg.mod" (call site pkg.mod.fn() has root alias
 pkg), matching the external branch's module.split('.').next() key.
     - import X as m (X local) → local_member["m"] = X.
   - Relative imports are in scope (predicates.rs:12 already classifies ./.. as
 non-external, so they hit the same bug): normalize the leading dots against the caller's
 package (derived from rel_path, stripping a trailing __init__ so pkg/__init__.py's
 package is pkg, not pkg.__init__). One leading dot = caller's package; each extra dot =
 one parent. Reject paths that walk above the package root (record nothing). Use the single
 normalized absolute module for both the import-edge binding (ImportRelation.module_name)
 and the local-resolution metadata, so they can't diverge. If normalization can't resolve,
 record nothing (degrade to unresolved — no regression).
 7. Resolver + materialization
   - crates/gcode/src/index/import_resolution/parser/mod.rs: add resolve_local_import_callee
 returning LocalCallTarget { module, callee_name }, mirroring resolve_external_callee's
 shadow guards exactly: for a bare call, return None if any same-file symbol matches
 the call name/alias (symbols.iter().any(|s| s.name == callee_name)); for a member call,
 guard on the root_alias (symbols.iter().any(|s| s.name == root_alias)), not on
 callee_name — otherwise local shadowing of m in m.fn() is missed.
   - Member-call module computation goes through a tiny tested helper
 resolve_member_target_module(binding_module, qualifier_path, root_alias) (callee_name is the
 final qualifier segment). Rule: if qualifier_path == binding_module or starts with
 binding_module + ".", the qualifier is already absolute → return it; otherwise substitute the
 leading root_alias with binding_module. Required cases (binding value = module as written):
       - import pkg; pkg.mod.fn() → local_member["pkg"]="pkg" → pkg.mod
     - import pkg.mod; pkg.mod.fn() → local_member["pkg"]="pkg.mod" → pkg.mod
     - import pkg.mod as m; m.fn() → local_member["m"]="pkg.mod" → pkg.mod
   - crates/gcode/src/index/parser/calls.rs::materialize_call: rename the existing
 external_shadowed flag to import_shadowed and gate the new local branch on it too.
 Add the branch after external, before semantic: only when !import_shadowed, if
 resolve_local_import_callee returns Some, build via
 with_local_import_target(target.callee_name, target.module). This prevents
 helper = ...; helper() from resolving to an imported local function.
   - Semantic fallback gate: add local_import_target.is_none() to the existing
 local_target.is_none() && external_target.is_none() && !import_shadowed condition, so the
 semantic resolver does not run for a call already classified as a local import.
 8. Constructor case — crates/gcode/src/index/parser/calls/resolution.rs
   - Include "class" in callable kinds gated by language in
 resolve_same_file_callee_for_language (Python now; JS/TS when added) rather than globally,
 so same-file Service() resolves to the class symbol without risking false edges in
 Rust/Go where a bare name is not a constructor. Cross-file imported classes resolve through
 the same local-import path (the sync lookup's top-level class preference picks the class).

 C. Tests (gcode)

 9. Parser unit tests — crates/gcode/src/index/parser/tests/python_javascript_typescript.rs
   - Update the bug-encoding test (leaves_local_python_imports_unresolved): the persisted row
 is now local_import with callee_name = original, callee_external_module = local module.
   - Add: aliased (from m import f as g; g()), module-aliased (import pkg.mod as m; m.fn()),
 unaliased member (import pkg.mod; pkg.mod.fn() keyed on root pkg), submodule-from-import
 (from pkg import mod; mod.fn() where pkg.mod is a known local module — validates the
 restricted local_member[a]="X.Y" rule fires only for submodules), relative
 (from .sibling import f; f()), relative from a package init (pkg/__init__.py doing
 from .sibling import f; f() → module pkg.sibling, not pkg.__init__.sibling), and
 same-file constructor (Service() → class symbol id).
   - Negative/shadowing: from pkg import obj; obj.method() does not get a false local member
 edge; a local variable shadow (from m import helper; def f(): helper = 1; helper()) does
 not resolve to the import. Keep classifies_external_python_from_import_calls green.
 10. Import-resolution tests — crates/gcode/src/index/import_resolution/tests/: assert
 local_bare/local_member populated per the v1 rules (and the member-binding restriction) for
 local modules, bare/member untouched; assert python_module_names_for_path /
 build_python_module_file_map (incl. __init__.py / src. forms).
 11. Indexer count / contract tests — update fixtures that key off CallTargetKind::Unresolved,
 since some now become LocalImport: crates/gcode/src/index/indexer/tests/facts.rs:78
 (the unresolved-count filter) and crates/gcode/src/index/indexer/tests/api_contract.rs:82-83.
   - Projection fallback unit test: a LocalImport call whose resolve_local_import_calls
 finds no matching symbol stays LocalImport, and partition_call_graph_items/from_call
 route it to the unresolved bucket (writes an UnresolvedCallee) — proving the
 degradation path is unchanged.
 12. Integration (live FalkorDB+PostgreSQL, env-gated) — crates/gcode/tests/graph_standalone.rs
   - 2-file Python project: a.py defines recluster_project_entities() and class Service;
 b.py does from a import recluster_project_entities / from a import Service as Svc and
 calls both. Run gcode index, then assert callers recluster_project_entities and
 blast-radius recluster_project_entities include b.py's caller, and Svc() resolves to
 the Service class. Cover the aliased and relative-import forms. A specific import of a
 specific module does resolve even if the name also exists elsewhere — so the negative
 case is genuine ambiguity within the selected candidates: a module alias whose dotted-path
 yields two candidate files that each define the name (e.g. pkg/x.py and pkg/x/__init__.py),
 or two same-tier symbol matches in the candidate set → stays unresolved (no false edge).
   - Exercise all three projection paths, since they were the bypass risk: after gcode index,
 also run gcode graph rebuild and gcode graph sync-file --file b.py and assert the canonical
 CALLS edge survives/recreates in each (not just index-time sync).
   - Order-independence holds for free (every path reads fully-populated code_symbols).

 D. Python daemon coordination (/Users/josh/Projects/gobby)

 13. src/gobby/code_index/models.py:343: extend
 callee_target_kind: Literal["symbol","unresolved","external"] → add "local_import".
 The column is TEXT with no CHECK constraint, so existing rows/inserts are unaffected; this
 keeps Rust↔Python parity and any future strict validation. Verify the daemon does not run its
 own competing code-call graph projection that would re-emit an UnresolvedCallee
 (per CLAUDE.md, Rust owns code projection mutation — relations.py is storage-only). Track as
 a tightly-coupled companion change to #776.

 Files to modify (gcode)

 - crates/gcode/src/models.rs — CallTargetKind::LocalImport, with_local_import_target
 - crates/gcode/src/index/import_resolution/context.rs — LocalImportBinding, new binding maps,
 python_module_names_for_path, build_python_module_file_map, LocalImportResolver
 - crates/gcode/src/db/queries.rs — kind parse (local_import), resolve_local_callee_symbol_id (SQL only)
 - crates/gcode/src/projection/local_imports.rs (new, pub(crate)) — shared resolve_local_import_calls
 - crates/gcode/src/projection/sync.rs — build resolver in sync_graph_files, enrich in sync_graph_file
 - crates/gcode/src/commands/graph/lifecycle.rs — enrich in sync_file_graph (~183) and rebuild_project_graph (~257)
 - crates/gcode/src/index/import_resolution/parser/python_js.rs — record local bindings (incl. relative)
 - crates/gcode/src/index/import_resolution/parser/mod.rs — resolve_local_import_callee (root-alias shadow guard)
 - crates/gcode/src/index/parser/calls.rs — external_shadowed→import_shadowed, gated local branch in materialize_call
 - crates/gcode/src/index/parser/calls/resolution.rs — language-gated class callable
 - Tests: parser/tests/python_javascript_typescript.rs, import_resolution/tests/*,
 indexer/tests/{facts.rs,api_contract.rs}, tests/graph_standalone.rs
 - Daemon (companion): gobby/src/gobby/code_index/models.py

 Verification

 1. cargo nextest run -p gobby-code and cargo test --doc -p gobby-code.
 2. cargo clippy --workspace -- -D warnings and cargo fmt --all --check.
 3. Live graph test: run graph_standalone.rs against a local FalkorDB + PostgreSQL
 (set GCODE_GRAPH_STANDALONE_* env) — confirm the 2-file callers/blast-radius/constructor cases.
 4. Real-world: reindex the gobby project with the rebuilt gcode, then confirm
 gcode callers recluster_project_entities and gcode blast-radius recluster_project_entities
 include KnowledgeGraphService.recluster_entities, and KnowledgeGraphService resolves its
 constructor callers. Rebuild/install the binary into ~/.gobby/bin per CLAUDE.md.

 Execution workflow

 - Claim #776 before making any edits.
 - Create the follow-up tasks (below) before closing #776.
 - The Python daemon Literal change (step D) lands in /Users/josh/Projects/gobby — track it as
 its own companion task/commit there, not folded into the gcode commit.

 Follow-up tasks to create (after approval)

 - JavaScript/TypeScript local-import resolution on the shared core (shares python_js.rs;
 needs relative-specifier + index-file + extension module resolution). High priority — completes
 the first 3.
 - Rust local call resolution — highest-priority follow-up (this repo is Rust; callers/
 blast-radius are broken on gobby-cli until it lands). Needs, on top of the shared core:
 crate/workspace-aware module→file mapping (crate::/self::/super:: and cross-member
 gobby_core::… → mod tree: foo.rs vs foo/mod.rs); path-qualified calls with no use
 (crate::m::f()) resolved against the module tree; use alias bindings; and Type::assoc_fn()
 constructor resolution (impl-block/associated fns). Its own Rust fixtures + validation criteria.
 - One per remaining T1/T2 language: Go (package-granularity: resolve against all files in the
 package dir), Java, C#, Ruby, PHP, Swift, Kotlin, Dart, Elixir.
 - C/C++: extend the clangd SemanticCallResolver to resolve local definitions to canonical
 symbols (different mechanism from import bindings).

 Risks

 - Daemon parity — mitigated by step D (extend the Literal); column is unconstrained TEXT.
 - Name collisions — resolve_local_callee_symbol_id returns None unless unique among
 top-level symbols → never a wrong edge (degrades to today's behavior).
 - Same-file class callable — language-gated to avoid false edges in non-constructor languages;
 unique_symbol_id already suppresses ambiguous same-name matches.
 - Incremental: only the callee file changes — caller edges are owned by the caller file's sync;
 a full re-sync (or the caller's next index) relinks. Matches existing edge-lifecycle semantics.
 - Graph rebuild / sync-file bypass — commands/graph/lifecycle.rs reads GraphFileFacts
 independently of projection/sync.rs; mitigated by routing all three sites through the one shared
 resolve_local_import_calls helper (step A.4) so rebuild can't recreate unresolved edges.
 - LocalImport/Symbol invariant — never persisted together; projection clones to a Symbol
 target (step "Invariant" above), so we don't lean on from_call's id-implies-Symbol coincidence.
 - Non-Python languages — out of #776 scope; tracked as follow-ups, no regression (they remain
 unresolved as today). Python relative imports are in scope for #776.