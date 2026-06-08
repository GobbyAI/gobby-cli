> **RECOVERED ORPHANED CODERABBIT PLAN**
> Source: codex session #979. This review was triaged into a fix plan but the session was lost
> (codex `gpt-image-2` tool error blocked resume) before any code was committed.
> Scope: 49 rows (46 fix / 3 no-fix).
> Verified UNIMPLEMENTED as of `fb3a03b` — none of its distinctive fixes appear in any commit or the working tree.
> Re-run this plan to apply the fixes; delete this file once committed.

# RECOVERED CodeRabbit plan — session #979 (gobby-cli)
# Title: CodeRabbit 46-Finding Fix Plan
# Transcript: /Users/josh/.codex/sessions/2026/06/02/rollout-2026-06-02T16-40-43-019e8a48-2250-7f53-8b1b-5583bc42d492.jsonl
# Created: 2026-06-02T21:40:57.474430+00:00  Updated: 2026-06-02T23:43:21.963012+00:00  Status: expired

================================================================================
## ORIGINAL CODERABBIT FINDINGS (the prompt you pasted)
================================================================================

$gobby coderabbit Fix the following issues. The issues can be from different files or can overlap on same lines in one file.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/commands/codewiki.rs around lines 1703 - 1705, The component_id function currently builds IDs from symbol.file_path and symbol.name which can collide; update component_id to return a truly unique identifier using symbol.id (or another unique field) for internal identity, and if a human-readable label is still needed keep a separate renderer function (e.g., symbol_label) that derives file+name for display only; locate and change the component_id function and any consumers expecting a readable string so they use the new unique ID for graph nodes/edges and the separate label for rendering.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/commands/codewiki.rs around lines 486 - 491, The write_doc function currently trusts safe_doc_path but still follows existing symlinks when creating dirs or writing files, allowing escapes; update write_doc (and the similar logic at the other occurrence) to reject any path where any component between out_dir and the target is a symlink: after computing target via safe_doc_path, iterate from out_dir (exclusive) through each ancestor component to target, call std::fs::symlink_metadata(...) and if file_type().is_symlink() return an error; also check the final target with symlink_metadata and reject if it's a symlink before opening/writing; only then create directories and write the file (use the existing create_dir_all and write/truncate) so no symlink components are followed.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/commands/codewiki.rs around lines 450 - 483, write_incremental_doc_set currently never removes files that were present in the previous CodewikiMeta, so stale docs remain on disk; after building next_docs (and before writing the new meta via write_codewiki_meta) compute the set difference between previous.docs keys and next_docs keys and remove each corresponding file (use safe_doc_path(out_dir, &relative_path) to locate and std::fs::remove_file, handling NotFound harmlessly), and optionally remove empty parent directories; then proceed to write the new meta and return generated_docs as before.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/commands/graph/lifecycle.rs around lines 202 - 281, The rebuild currently calls clear_project and reset_graph_sync_for_project before syncing, which can leave the projection emptier on partial failure; modify rebuild_project_graph to avoid destructive pre-clear: instead build into a temporary/new graph (use with_code_graph to create an isolated graph or a staging area), perform all file syncs there, run cleanup_orphans on the staging graph, and only when the sync completes without catastrophic failure replace the live project graph and call reset_graph_sync_for_project (or, as a simpler alternative, defer clear_project/reset_graph_sync_for_project until after successful sync and on catastrophic failures restore the previous graph state); update error/reporting logic so ProjectionSyncReport::degraded continues to indicate the live graph was not replaced when staging failed.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/graph/report/render.rs around lines 37 - 66, The render_markdown output never uses high_degree_modules, causing wasted work; either add a module hotspot section by calling append_hotspot_section for input.hotspots.high_degree_modules (e.g., mirror the existing calls for "High-degree files"/"High-degree symbols"/"Incoming-call hotspots" with the title "High-degree modules" and pass input.top_n) in render.rs, or if you prefer to stop producing it, remove the population/load of high_degree_modules in summary.rs and loading.rs so the data is not computed/loaded unnecessarily.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/graph/report/rows.rs around lines 68 - 84, row_string and row_usize currently use keys.iter().find_map(...) which stops at the first present key even if it's an empty string or a non-numeric value; change both helpers to explicitly iterate the keys (e.g., for key in keys) and attempt to extract/convert each candidate in order, returning the first non-empty string for row_string (use row.get(key).and_then(Value::as_str) and skip if empty) and for row_usize try as_u64 then as_i64 converting to usize and continue to the next key if conversion fails; update the implementations of row_string and row_usize accordingly so they fall through to later candidate keys.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/api.rs around lines 77 - 97, The SQL in file_facts_exist using SELECT EXISTS with UNION ALL can be made more efficient: replace the UNION ALL subqueries with a single SELECT EXISTS that combines separate EXISTS(...) OR EXISTS(...) checks (or multiple EXISTS clauses joined by OR) so PostgreSQL can short-circuit without planning unioned subqueries; update the SQL string passed to conn.query_one in file_facts_exist to use EXISTS(SELECT 1 FROM code_indexed_files WHERE ...) OR EXISTS(SELECT 1 FROM code_symbols WHERE ...) OR ... (include code_content_chunks, code_imports using source_file, and code_calls) and keep the same parameter bindings (&project_id, &file_path) and row.try_get(0) usage.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/import_resolution/context.rs around lines 241 - 251, The loop that gathers package names from package.json skips bundledDependencies because it expects an object; update the logic around json.get(field) in the block that populates packages so bundledDependencies (and its alias "bundleDependencies") are handled when they are arrays: if json.get(field).and_then(|v| v.as_object()) yields a map, extend packages with map.keys(); otherwise if json.get(field).and_then(|v| v.as_array()) yields an array, iterate its entries, convert each entry to a string (e.g., via as_str()) and extend packages with those names; keep using the existing variables (json, field, packages) so the change is localized.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/import_resolution/predicates.rs around lines 174 - 193, The php_declared_symbols scanner currently tokenizes raw contents and can pick up keywords inside comments or string literals; modify php_declared_symbols to first call strip_comments_and_string_literals(contents) (the same helper used by declared_types) and operate on the cleaned string before splitting/tokenizing so comments/strings are removed; ensure the function references the cleaned variable (and import or make visible strip_comments_and_string_literals if needed) and otherwise keep the existing window/matching logic intact.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/indexer/util.rs around lines 107 - 148, The project lacks Windows-specific tests for lexical_relative_path and normalized_components: add unit tests exercising Windows drive-letter roots (e.g., "C:\\project" vs "D:\\other"), UNC paths ("\\\\server\\share\\path"), and mixed separators to ensure Prefix and RootDir handling works correctly; update or add tests that construct Path/PathBufs with these cases and assert expected relative outputs (including cross-drive behavior and UNC handling), or if Windows support is intentionally out-of-scope, add a clear comment/docs note in the module explaining Windows paths are untested/unsupported and why.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/parser/calls/ast.rs around lines 17 - 96, Add unit tests for extract_ast_calls that exercise its internal parsing branches: create minimal tree_sitter Tree+source fixtures to simulate (1) matches missing the "name" capture to ensure those are skipped, (2) callee names that split into qualifier and base via split_qualified_callee and trigger should_ignore_call_name behavior, (3) cases where call_node != name_node so call_qualifier_path/member_qualifier_path are used and qualifier_path is Some, and (4) a bare detected syntax from call_syntax_kind that should be upgraded to CallSyntaxKind::Member when qualifier_path is present; assert that materialize_call is invoked (or its output) and that returned CallRelation fields (callee_name, qualifier_path, name_byte, scope_byte, line, syntax) match expected values.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/parser/calls/dart_textual.rs around lines 30 - 58, The current loop rescans and clones DartScanState per-candidate via dart_textual_candidate_in_ignored_context and empty_prefix_semicolon_declaration_in_class causing O(candidates × line_len) work; change to do one forward scan per line that records comment/string/scan spans (e.g., produce a LineScanSpans or shared scan result) once before iterating candidates, then update dart_textual_candidate_in_ignored_context and empty_prefix_semicolon_declaration_in_class signatures to accept a reference to that scan result (or a lightweight &DartScanStateView/Arc) instead of cloning DartScanState, and consult that precomputed spans map during candidate checks; keep dart_state updates via dart_state_after_line as before.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/parser/calls/text.rs around lines 53 - 59, The identifier helpers is_identifier_start and is_identifier_continue currently restrict to ASCII (is_ascii_alphabetic / is_ascii_alphanumeric), which excludes valid Unicode identifier characters; to support Unicode identifiers replace these checks with the unicode-xid predicates (use unicode_xid::UnicodeXID and call UnicodeXID::is_xid_start(ch) and UnicodeXID::is_xid_continue(ch) or use the char extension methods if available), add the unicode-xid crate to Cargo.toml, and update the implementations of is_identifier_start and is_identifier_continue to call those XID functions instead of the ASCII-only checks.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/parser/tests/php_ruby_dart_elixir.rs around lines 157 - 179, The two assert_eq checks that follow the json_call find are redundant because the find closure already filters by callee_name == "parse", callee_target_kind.as_str() == "external", and callee_external_module.as_deref() == Some("json"); remove the duplicate assertions referencing json_call.callee_target_kind and json_call.callee_external_module so only the find+expect remains (leave the mkdir_p find and its assertions intact).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/index/parser/tests/php_ruby_dart_elixir.rs around lines 237 - 270, Remove the redundant assertions that re-check the same properties already enforced by the find closure for jsonDecode: delete the assert_eq lines that inspect json_call.callee_target_kind and json_call.callee_external_module (the assertions immediately after the json_call = parsed.calls.iter().find(...) block); keep the find call and its expectation as the single verification for the jsonDecode call (leave other tests like the Client checks and unresolved/run assertions untouched).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/search/fts/content.rs at line 53, The SQL ORDER BY clauses in the content search queries incorrectly reference pdb.score(c.id), causing SQL failures and fallback to ILIKE; locate the query strings in content.rs that use pdb.score(c.id) (the same pattern used in the content search code and mirrored against pg_search.score(cs.id) in common.rs) and replace both occurrences with pg_search.score(c.id) so the BM25 ranking uses the correct pg_search.score function.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/search/fts/counts.rs around lines 276 - 311, The glob_to_pg_regex function treats each '*' independently, so a recursive glob like "**" becomes ".*.*" instead of a single ".*"; update glob_to_pg_regex to detect consecutive '*' chars and collapse "**" (or any run of multiple '*') into a single ".*" to represent recursive matching, preserving existing handling for '?' and character classes and keeping escaping logic for backslashes and regex metacharacters; ensure you detect runs when matching a '*' in glob_to_pg_regex and advance the iterator appropriately so you don't emit redundant ".*" sequences.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/setup/identifiers.rs around lines 31 - 39, The length check currently uses the escaped string (`escaped`) which inflates length when quotes are doubled; change the validation to measure the raw trimmed identifier bytes (use `trimmed.as_bytes().len()`) against `POSTGRES_IDENTIFIER_MAX_BYTES` and only produce the `SetupError::CreationFailed` if that byte-length exceeds the limit; keep the escaping (`escaped = trimmed.replace('"', "\"\"")`) for later use but perform the length check on `trimmed` (refer to variables `trimmed`, `escaped`, constant `POSTGRES_IDENTIFIER_MAX_BYTES`, and error construction `SetupError::CreationFailed { object: label, message: ... }`).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/vector/code_symbols/lifecycle.rs around lines 64 - 71, Replace the current shallow Qdrant URL presence check in the constructor with a call to require_qdrant_boundary() so the constructor performs the same full service validation that ensure_collection and clear_project_vectors rely on; keep VectorLifecycleError::MissingQdrantConfig or convert the error returned by require_qdrant_boundary() into that variant so callers still see the same error type. Ensure you reference require_qdrant_boundary() from the constructor path (instead of only checking qdrant.url) and remove or document the now-redundant lines that only validate the URL string.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/vector/code_symbols/search.rs around lines 11 - 45, Replace unconditional eprintln! calls in this function with log crate calls so diagnostics respect log levels; specifically, change the three early-return messages and the vector_search error branch to use log::warn! (or log::error! for the vector_search Err if preferred) instead of eprintln!. Update the messages in the branches that check ctx.qdrant, embedding_source_from_context, and embed_query_with_source to call log::warn!("gcode: semantic vector search skipped: {}", /* reason */) and change the vector_search Err branch to log::warn!("gcode: semantic vector search failed: {}", error) while keeping the existing returns and mapping logic for collection_name, embed_query_with_source, and vector_search intact.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/visibility.rs around lines 491 - 507, The function tombstone_count currently casts the i64 result to usize with as usize which can silently wrap on platforms where usize is smaller; change the conversion to use TryInto (e.g., .try_into().unwrap_or(0)) or TryFrom to defensively handle out-of-range values from the query result. Locate tombstone_count (which matches on ProjectIndexScope::Overlay and queries code_indexed_files with TOMBSTONE_LANGUAGE) and replace the final as usize cast on the queried i64 count with a fallible conversion that returns 0 on failure.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/tests/common/mod.rs around lines 19 - 41, The closure passed to std::panic::catch_unwind (the block containing Client::connect and cleanup_project calls inside the ProjectCleanup cleanup logic) uses tab indentation mixed with spaces, which breaks cargo fmt --all --check; reformat the closure to use 4-space indentation consistent with the rest of the file and run cargo fmt to normalize formatting so the catch_unwind closure, Client::connect error handling, and cleanup_project error log lines match the project style.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/tests/common/mod.rs at line 40, The panic log "ProjectCleanup cleanup panicked for project cleanup" should include the project identifier for consistent diagnostics; update the eprintln call that prints the panic (the one emitting "ProjectCleanup cleanup panicked for project cleanup") to include the project_id variable (ensure project_id is in scope) so the message contains the actual id (e.g., mention project_id in the formatted string).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/Cargo.toml around lines 16 - 21, The Cargo feature set mixes native-tls via the synchronous postgres feature with rustls via reqwest (ai/qdrant), causing dual TLS linkage; fix by choosing one approach: either replace the sync postgres feature with an async rustls-capable client (swap the "postgres" feature to use "tokio-postgres" and enable its rustls feature, and update any code using postgres::Client to the tokio-postgres equivalents), or keep sync postgres but make TLS consistent by depending on "postgres-openssl" (replace "dep:postgres" -> "dep:postgres-openssl" and remove native-tls) so all DB TLS uses OpenSSL; update feature arrays (postgres, ai, qdrant) accordingly and adjust any calling code to match the chosen client API.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/ai/daemon.rs around lines 721 - 757, Add a short clarifying comment around the unsafe env var manipulation in EnvGuard::set_home and the Drop impl explaining that std::env::set_var/remove_var are unsafe as of Rust 1.80 because they can cause data races, and that TEST_ENV_LOCK (used to create the EnvGuard._lock) serializes access to environment variables to make this usage safe in tests; reference the EnvGuard struct, EnvGuard::set_home, the Drop impl, and TEST_ENV_LOCK so reviewers immediately understand why the unsafe blocks are guarded by the mutex.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/degradation.rs around lines 244 - 270, The test hub_conflict_display_and_json_redact_database_urls currently only covers URL-form DSNs; add a new case (or extend this test) that constructs a CoreError::HubConflict where existing_database_url and/or daemon_database_url use keyword-form DSNs (e.g. "host=... user=... password=SECRET dbname=gobby sslmode=require application_name=gobby") and assert the human-readable message (conflict.to_string()) contains the identities (cluster-a/gobby, cluster-b/gobby) but not the raw keywords like "password=", "SECRET", "sslmode", or "application_name", and also assert the JSON serialization (serde_json::to_string(&conflict)) includes sanitized DSN host/dbname forms (without secrets or keyword values) and does not contain the secret or sensitive keyword values; reference the existing test name hub_conflict_display_and_json_redact_database_urls and the CoreError::HubConflict fields existing_database_url and daemon_database_url when adding the assertions.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/degradation.rs around lines 99 - 114, redact_database_url currently only handles URL-form DSNs (checks for "://") and returns keyword-form connection strings unredacted; update redact_database_url to detect keyword/libpq-style DSNs (e.g. contain "password=" or other key=value pairs separated by whitespace) and redact sensitive keys before returning. Specifically, after handling fragments/queries, if the string contains tokens like "password=", "pass=", "pwd=", "sslkey=", "sslpassword=", "secret=" (case-insensitive), parse the string into space-separated key=value tokens, replace the value portion of those sensitive keys with "[REDACTED]" (preserving quoting/whitespace as much as practical), then rejoin and return the sanitized string; keep the existing URL-form branch (function redact_database_url) intact. Ensure comparisons are case-insensitive and do not modify non-sensitive keys.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/falkor.rs around lines 103 - 122, ensure_exact_node_index currently detects duplicate-index errors by matching error message text; open an issue in the FalkorDB driver requesting a typed DuplicateIndex error and then update this code to use that typed error instead of string matching. Specifically, change the error handling in ensure_exact_node_index to attempt a downcast or inspect a typed error variant (replace reliance on is_existing_index_error string checks) and update or remove is_existing_index_error to check the driver-provided error type/kind (e.g., match on a DuplicateIndex enum/struct or an Error::Kind) and adjust the tests (tests covering lines ~449-465) to assert the typed error path; keep the suppressed-duplicate branch behavior but use the driver's typed error once available.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/local_backend.rs around lines 68 - 105, The URL concatenation in validate_backend currently does simple string concatenation of backend.url and backend.probe which can produce double slashes if backend.url ends with '/' and backend.probe starts with '/'; update validate_backend to normalize/join the base and probe parts before building the request (e.g., trim a trailing '/' from backend.url and a leading '/' from backend.probe or use a URL-joining utility) so that the url variable contains exactly one '/' between segments and still preserves other parts of the URL; reference the backend.url, backend.probe and validate_backend function when making the change.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/test_http.rs around lines 130 - 139, The SingleRead::read implementation can panic when buffer.len() < data.len() because buffer[..data.len()].copy_from_slice(data) will out-of-bounds; modify the read method (SingleRead::read) to check buffer.len() against self.data (the data slice) and handle the short buffer defensively — either copy only up to buffer.len() and return the number of bytes copied, or return an io::Error (e.g. ErrorKind::UnexpectedEof/Other) with a clear message; ensure you still take() the data when appropriate and return the correct io::Result<usize> without causing a panic.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gsqz/Cargo.toml at line 28, Replace the incorrect dependency entry "yaml_serde" with the real crate name "serde_yaml" in the Cargo.toml for each affected crate; locate the dependency line currently written as serde_yaml = { package = "yaml_serde", version = "0.10.4" (or similar) in crates gsqz, gwiki, ghook, gloc, gcode and gcore and change it to serde_yaml = "0.10.4" (or serde_yaml = { version = "0.10.4" }) so the package name matches crates.io (remove the invalid package = "yaml_serde" override). Ensure each Cargo.toml now references serde_yaml consistently across the workspace.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ai/clients.rs around lines 107 - 144, translate_segments currently retries the same batch twice with no delay; add a small backoff between the two translate_segment_batch calls to make the retry meaningful: after the first warn_translation_batch_mismatch call insert a brief sleep (use std::time::Duration and std::thread::sleep, e.g. 100–200ms or an exponentially larger value if you want) then proceed to call translate_segment_batch the second time; keep existing calls to translate_segment_batch and warn_translation_batch_mismatch intact and do not change the per-segment fallback logic.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/collect.rs around lines 555 - 559, parse_embedded_http_url currently returns the untrimmed candidate when the trimmed version parses, producing malformed URLs; change it so when parse_http_url succeeds on the trimmed string we return that trimmed URL. Specifically, in parse_embedded_http_url bind the trimmed value (e.g., let trimmed = candidate.trim_end_matches([',', '.', ';', ')', ']'])), call parse_http_url(trimmed) and map the success to trimmed.to_string() (instead of returning candidate.to_string()); keep the first parse_http_url(candidate) branch unchanged and update the failing test to expect the trimmed URL.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/commands/audit.rs around lines 4 - 23, The audit execute function duplicates a common pattern (resolve_command_scope → resolved_scope_identity → run analysis → serde_json::to_value error mapping → super::scoped_outcome) shared with lint.rs; extract a small helper function or generic higher-order function/macro (e.g., run_analysis_command) that accepts the command name, ScopeSelection, an analysis runner (like audit::run_with_options) and a renderer (like audit::render_text), performs resolve_command_scope and resolved_scope_identity, runs the analysis, maps serde_json::to_value errors into WikiError::Json, and calls super::scoped_outcome; then replace audit::execute to call this helper (and do the same for lint::execute) so behavior (including error mapping) is preserved but duplication removed.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/commands/collect.rs at line 14, The code currently uses `let _ = vault::initialize(&scope)?;`, which redundantly binds and discards the Ok value; replace it with a plain call `vault::initialize(&scope)?;` if the return value is not needed, or if it should be used capture it into a variable (e.g., `let init = vault::initialize(&scope)?;`) and use `init` later — locate the call to `vault::initialize` in collect.rs and apply one of these two fixes accordingly.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/commands/init.rs around lines 9 - 17, The code calls vault::initialize(...) which creates on-disk state before registry::register_scope(...); if registration fails the partial vault remains—update execute to either (A) perform registration before creating vault or (B) rollback created artifacts on failure: after let created_paths = vault::initialize(&scope)?; attempt registry::register_scope(scope.registry_path(), &scope).map_err(|e| { let _ = vault::cleanup_created(&created_paths); e })? (or call the appropriate vault removal API) and return the original error; ensure the cleanup call references created_paths and that execute still returns render(...) on success.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/document.rs around lines 128 - 171, Add a new entry to the cases array to exercise DocumentFailureMode::PdfRenderBudgetExceeded: include (DocumentFailureMode::PdfRenderBudgetExceeded, DocumentUnitCount::pages(0), "pdf_render_budget_exceeded", "page_count") so the as_str() mapping "pdf_render_budget_exceeded" is covered by the table-driven test (insert alongside the other PDF-related cases in the cases array).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/wayback.rs around lines 113 - 149, The current extraction pushes each text node into parts and joins with "\n", which causes inline siblings or multi-line text nodes to become separate paragraphs in html_to_text; update collect_visible_text/extract_html_text so that text is aggregated per block-level element: treat block elements (e.g., p, div, li, h1..h6, section, article, header, footer, br) as boundaries and concatenate inline child text nodes with spaces before pushing a single entry into parts, and for block boundaries push a separator (or new entry) so extract_html_text returns one string per block; then html_to_text can safely split/normalize paragraphs without splitting inline content across lines. Ensure the functions referenced (collect_visible_text, extract_html_text, html_to_text) implement this grouping logic and ignore head/script/style as before.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/links.rs around lines 181 - 186, markdown_label_end currently returns the first unescaped ']' which breaks labels with balanced/internal brackets (e.g., "[see [note]]"); update markdown_label_end to mirror the balancing logic used in markdown_destination_end: iterate from start, ignore escaped characters via is_escaped, increment a depth counter on unescaped '[' and decrement on unescaped ']', and return the index when the depth returns to zero for a closing ']' (ensuring the initial bracket is accounted for); alternatively, if nested labels are out of scope, explicitly document that markdown_label_end does not support nested brackets instead of changing behavior.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/log.rs around lines 59 - 77, The current logic uses file.metadata().map_or(true, |metadata| metadata.len() == 0) which treats metadata errors as if the file is empty and thus may write a duplicate header; change this to only write the header when metadata() succeeds and reports len() == 0 (i.e., treat metadata errors as “do not write header”). Update the check around file.metadata() (the write_header calculation that uses file.metadata()) to use a pattern that returns false on Err (e.g., map(|m| m.len() == 0).unwrap_or(false) or a match), so that OpenOptions::open success is preserved but metadata failures won’t cause a header to be prepended.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/provenance.rs around lines 143 - 152, The temp file name currently uses only the process id (temp_path created from meta_dir.join(format!(".provenance.json.{}.tmp", std::process::id()))) which causes create_new(true) to collide for concurrent save calls; update the temp filename generation in the save routine (where temp_path/OpenOptions::new()/create_new(true) are used) to append a per-call unique suffix (e.g., a UUID, thread id, or an atomic counter) so each invocation produces a distinct temp_path before opening the file and keep the existing error mapping to WikiError::Io.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/research.rs around lines 63 - 79, When starting a new run in run_with_dispatcher (when options.resume is false) validate options.agent_count > 0 and reject zero-agent runs before creating a ResearchSession; i.e., add a guard after checking !options.resume that returns an appropriate WikiError (or constructs a descriptive error) if options.agent_count == 0, so you don't call ResearchSession::new or dispatcher.dispatch for agent_count == 0.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/search/graph_boost.rs around lines 141 - 180, The load_graph_boost_data function currently truncates results using GRAPH_BOOST_DOCUMENT_QUERY_LIMIT and GRAPH_BOOST_LINK_QUERY_LIMIT which silently biases rankings; modify load_graph_boost_data to first run COUNT(*) queries against gwiki_documents and gwiki_links (using the same scope_kind/scope_id) and compare counts to those constants, and if either count exceeds its limit return an Err (or a clear error type/message) instead of returning partial data so callers can surface degradation; reference the existing symbols load_graph_boost_data, GRAPH_BOOST_DOCUMENT_QUERY_LIMIT, GRAPH_BOOST_LINK_QUERY_LIMIT, gwiki_documents, and gwiki_links when implementing the checks.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/search/semantic.rs around lines 321 - 333, The current impl of QueryEmbedder for OpenAiEmbeddingBackend unconditionally rejects all embeds when not built with embeddings-http, which prevents SemanticEmbedding::Daemon from working in builds that have the ai feature; change the cfg so this rejecting fallback only compiles when both embeddings-http and ai are disabled (e.g., #[cfg(all(not(feature = "embeddings-http"), not(feature = "ai")))]), and preserve or add a separate branch under #[cfg(all(not(feature = "embeddings-http"), feature = "ai"))] that lets embed_query in OpenAiEmbeddingBackend handle or forward SemanticEmbedding::Daemon to the daemon code path instead of returning an error (update the embed_query method accordingly to delegate daemon embeddings to the daemon handler when feature "ai" is enabled).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/session.rs around lines 225 - 226, The comparable_path function currently canonicalizes paths directly, causing stored relative scope roots to be resolved against the current CWD at resume time; update the code so persisted scope roots are normalized to absolute paths before comparison: either (A) when persisting a scope root (e.g., in ResearchScope::project) convert and store an absolute path (Path::absolutize or join against the checkpoint location) or (B) change comparable_path to first detect relative inputs and resolve them against the checkpoint location / state-derived base path (resolve loaded_root against the checkpoint file directory) before calling canonicalize(), falling back to to_path_buf() on failure. Ensure you reference comparable_path and ResearchScope::project (or loaded_root) so the resolution happens prior to canonicalize().

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/sources.rs around lines 486 - 497, The current loop (using preserved, skipping_manifest, and iterating existing.lines()) drops every line after the "## Source manifest" header, which removes any user content placed after the manifest; change the logic so that when you encounter "## Source manifest" you enter skipping mode but only skip until the next top-level heading (a line starting with "## "), after which you exit skipping mode and resume pushing lines into preserved (i.e., treat "skipping_manifest" as temporary until the next "## " header), or alternatively document that the manifest must be the last section—update the loop around existing.lines(), preserved, and skipping_manifest accordingly so only the manifest block is removed rather than all subsequent lines.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/synthesis.rs around lines 261 - 268, The parent directory is being created with fs::create_dir_all before its location is validated, allowing symlink escape; move the call to ensure_existing_parent_inside_vault(vault_root, parent, "synthesized_page") so it runs before fs::create_dir_all, i.e. validate the parent path (using ensure_existing_parent_inside_vault and vault_root) while the path may not yet exist, and only after that call succeeds invoke fs::create_dir_all(parent) and preserve the WikiError::Io context for the create_dir_all failure.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/tests/cli_collect.rs around lines 32 - 49, The test currently asserts strict emptiness of stderr via assert!(stderr.is_empty()) which is brittle; change the check in the test function in crates/gwiki/tests/cli_collect.rs to instead assert that stderr does not contain fatal markers (for example check !stderr.contains("error") && !stderr.contains("panic") or similar) or assert that stderr.trim().is_empty() only after filtering known benign warnings; update the assertion around stderr (replace the assert!(stderr.is_empty(), ...) line) and keep the other assertions (stdout checks and args handling) intact so the test still verifies no fatal errors while allowing harmless warnings.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @docs/guides/release-guide.md around lines 81 - 92, Add a workspace-level test invocation to the validation block by inserting the command "cargo test --workspace" alongside the existing per-crate test lines (e.g., after the per-crate commands like "cargo test -p gobby-core" and before the workspace/no-default-features builds); this will run cross-crate integration tests and workspace fixtures in addition to the current per-crate checks.

================================================================================
## TRIAGE / FIX PLAN PRODUCED BY THE SESSION
================================================================================

<proposed_plan>
# CodeRabbit Fix Plan

## Summary
- Fix 46 current findings across `gcode`, `gcore`, `gwiki`, and docs.
- Skip 3 findings as no-fix: FalkorDB typed duplicate-index error is unavailable upstream, `yaml_serde` is a valid crate, and `gwiki/src/log.rs` is already fixed.
- Before edits: create/claim a Gobby task. Leave existing unrelated changes in `crates/gwiki/src/api.rs`, `crates/gwiki/src/ingest/url.rs`, and `crates/gwiki/src/main.rs` untouched.

## Finding Decisions
| # | Decision | Path/File Name | Relevant Memory/Lesson | Reason/Planned Fix |
|---|---|---|---|---|
| 1 | fix | `crates/gcode/src/commands/codewiki.rs` | No direct override | Use `symbol.id` for graph component identity; add separate label renderer for file/name display. |
| 2 | fix | `crates/gcode/src/commands/codewiki.rs` | Durability/cleanup lessons | Reject symlink ancestors and final symlink targets before doc/meta writes. |
| 3 | fix | `crates/gcode/src/commands/codewiki.rs` | Durability/cleanup lessons | Remove previous meta docs missing from `next_docs`; ignore `NotFound`; prune empty parents. |
| 4 | fix | `crates/gcode/src/commands/graph/lifecycle.rs` | Cleanup lesson, no override | Stop pre-clearing/resetting live graph; sync live graph in place and run orphan cleanup only after a clean pass. |
| 5 | fix | `crates/gcode/src/graph/report/render.rs` | No direct override | Render “High-degree modules” via `append_hotspot_section`. |
| 6 | fix | `crates/gcode/src/graph/report/rows.rs` | No direct override | Make row helpers continue past empty/invalid candidate keys. |
| 7 | fix | `crates/gcode/src/index/api.rs` | No direct override | Replace `UNION ALL` `EXISTS` SQL with `EXISTS(...) OR EXISTS(...)`. |
| 8 | fix | `crates/gcode/src/index/import_resolution/context.rs` | No direct override | Support `bundledDependencies`/`bundleDependencies` arrays as package names. |
| 9 | fix | `crates/gcode/src/index/import_resolution/predicates.rs` | No direct override | Run `strip_comments_and_string_literals` before PHP token scan. |
| 10 | fix | `crates/gcode/src/index/indexer/util.rs` | Testing preference: no mock frameworks | Add `#[cfg(windows)]` tests for drive letters, UNC paths, mixed separators. |
| 11 | fix | `crates/gcode/src/index/parser/calls/ast.rs` | Testing preference: no mock frameworks | Add focused tree-sitter unit tests for missing captures, qualifiers, scope bytes, syntax upgrade. |
| 12 | fix | `crates/gcode/src/index/parser/calls/dart_textual.rs` | No direct override | Precompute per-line Dart scan state/spans once and pass borrowed scan data to candidate checks. |
| 13 | fix | `crates/gcode/src/index/parser/calls/text.rs`, `crates/gcode/Cargo.toml` | No direct override | Add direct `unicode-xid` dep; use XID predicates while preserving `_`/`$` behavior. |
| 14 | fix | `crates/gcode/src/index/parser/tests/php_ruby_dart_elixir.rs` | No direct override | Remove redundant Ruby JSON assertions after filtered `find`. |
| 15 | fix | `crates/gcode/src/index/parser/tests/php_ruby_dart_elixir.rs` | No direct override | Remove redundant Dart `jsonDecode` assertions after filtered `find`. |
| 16 | fix | `crates/gcode/src/search/fts/content.rs` | No direct override | Replace both `pdb.score(c.id)` calls with `pg_search.score(c.id)`. |
| 17 | fix | `crates/gcode/src/search/fts/counts.rs` | No direct override | Collapse runs of `*` to one `.*`; add regression test. |
| 18 | fix | `crates/gcode/src/setup/identifiers.rs` | No direct override | Validate `trimmed.as_bytes().len()` before using escaped identifier. |
| 19 | fix | `crates/gcode/src/vector/code_symbols/lifecycle.rs` | Qdrant boundary lesson | Constructor calls `require_qdrant_boundary`; preserve missing-config error. |
| 20 | fix | `crates/gcode/src/vector/code_symbols/search.rs` | No direct override | Replace four `eprintln!` diagnostics with `log::warn!`. |
| 21 | fix | `crates/gcode/src/visibility.rs` | No direct override | Convert tombstone count with `try_into().unwrap_or(0)`. |
| 22 | fix | `crates/gcode/tests/common/mod.rs` | No direct override | Reformat `catch_unwind` closure with spaces. |
| 23 | fix | `crates/gcode/tests/common/mod.rs` | No direct override | Include `project_id` in panic log. |
| 24 | fix | `crates/gcore/Cargo.toml`, `crates/gcore/src/postgres.rs` | No direct override | Keep sync API; replace native TLS with `postgres-openssl`/`openssl`. |
| 25 | fix | `crates/gcore/src/ai/daemon.rs` | No direct override | Add comments explaining unsafe env mutation guarded by `TEST_ENV_LOCK`. |
| 26 | fix | `crates/gcore/src/degradation.rs` | No direct override | Extend HubConflict test with keyword-form DSNs. |
| 27 | fix | `crates/gcore/src/degradation.rs` | No direct override | Redact sensitive keyword DSN values case-insensitively. |
| 28 | no-fix | `crates/gcore/src/falkor.rs` | No direct override | `falkordb 0.2.1` has no typed duplicate-index error; current TODO already documents string fallback. |
| 29 | fix | `crates/gcore/src/local_backend.rs` | No direct override | Join backend base/probe with exactly one slash. |
| 30 | fix | `crates/gcore/src/test_http.rs` | No direct override | Make `SingleRead` handle short buffers without panicking. |
| 31 | no-fix | `crates/*/Cargo.toml` | No direct override | `yaml_serde = 0.10.4` is a valid maintained crate; `serde_yaml` is `0.9.34+deprecated`. |
| 32 | fix | `crates/gwiki/src/ai/clients.rs` | No direct override | Add short sleep before translate batch retry. |
| 33 | fix | `crates/gwiki/src/collect.rs` | No direct override | Return the trimmed URL after trimmed parse succeeds. |
| 34 | fix | `crates/gwiki/src/commands/audit.rs`, `crates/gwiki/src/commands/lint.rs` | No direct override | Extract shared `run_analysis_command` helper preserving JSON error mapping. |
| 35 | fix | `crates/gwiki/src/commands/collect.rs` | No direct override | Replace `let _ = vault::initialize(&scope)?;` with plain call. |
| 36 | fix | `crates/gwiki/src/commands/init.rs`, `crates/gwiki/src/vault.rs` | Cleanup lesson | Add vault rollback helper and call it if registry registration fails. |
| 37 | fix | `crates/gwiki/src/document.rs` | No direct override | Add `PdfRenderBudgetExceeded` matrix case. |
| 38 | fix | `crates/gwiki/src/ingest/wayback.rs` | No direct override | Aggregate inline text per block-level element; keep skipping head/script/style. |
| 39 | fix | `crates/gwiki/src/links.rs` | No direct override | Balance nested markdown label brackets while honoring escapes. |
| 40 | no-fix | `crates/gwiki/src/log.rs` | No direct override | Already uses `metadata().map(...).unwrap_or(false)`. |
| 41 | fix | `crates/gwiki/src/provenance.rs` | Durability/cleanup lessons | Add per-call unique temp suffix with atomic counter. |
| 42 | fix | `crates/gwiki/src/research.rs` | No direct override | Reject `agent_count == 0` before creating a new session. |
| 43 | fix | `crates/gwiki/src/search/graph_boost.rs` | No direct override | Count docs/links before load; degrade instead of truncating partial graph data. |
| 44 | fix | `crates/gwiki/src/search/semantic.rs` | Embedding config memory, no override | Let no-HTTP + `ai` builds route daemon embeddings through daemon path. |
| 45 | fix | `crates/gwiki/src/session.rs` | No direct override | Resolve relative loaded roots against checkpoint directory before canonicalization. |
| 46 | fix | `crates/gwiki/src/sources.rs` | No direct override | Skip source manifest only until next `## ` heading. |
| 47 | fix | `crates/gwiki/src/synthesis.rs` | Cleanup lesson | Validate existing parent prefix before `create_dir_all`; update helper for missing dirs. |
| 48 | fix | `crates/gwiki/tests/cli_collect.rs` | No direct override | Allow benign stderr; reject fatal markers like `error`/`panic`. |
| 49 | fix | `docs/guides/release-guide.md` | No direct override | Add `cargo test --workspace` to release validation block. |

## Key Implementation Changes
- Add small local helpers only where needed: Codewiki symlink validation/removal cleanup, GWiki vault rollback, shared audit/lint command runner, keyword DSN redaction, graph boost limit checks.
- Keep public CLI behavior unchanged except safer diagnostics/degradation and corrected rendered reports/docs.
- Cargo/interface changes: add direct `unicode-xid` to `gobby-code`; switch `gobby-core` PostgreSQL TLS feature deps to `postgres-openssl`/`openssl`.

## Test Plan
- Run formatting after edits: `cargo fmt --all`, then `cargo fmt --all --check`.
- Run focused compile/tests:
  - `cargo test -p gobby-code --no-default-features`
  - `cargo test -p gobby-core --features postgres,ai,falkor,qdrant`
  - `cargo test -p gobby-wiki`
  - `cargo test -p gobby-wiki --no-default-features --features ai`
- Run CI-shaped checks if time allows:
  - `cargo build --workspace --no-default-features`
  - `cargo clippy --workspace --no-default-features -- -D warnings`
- Add/extend regression tests for all parser/path/redaction/search/Wayback/link/session/synthesis changes noted above.

## Assumptions
- No `reports/coderabbit-*.md` files exist; only pasted findings are in scope.
- Windows path behavior is tested with `#[cfg(windows)]` because Rust `Path` parses drive prefixes only on Windows.
- FalkorDB typed duplicate-index handling is deferred until the driver exposes a typed error variant.
</proposed_plan>
