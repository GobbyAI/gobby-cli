# CodeRabbit Fix Checklist

Fix the following issues. The issues can be from different files or can overlap on same lines in one file.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @.github/workflows/release-gcore.yml around lines 26 - 44, Replace the crate-scoped invocations that use "-p gobby-core" with workspace-scoped flags and ensure we still run both default-feature and no-default-features passes: change the Clippy, Nextest and doctest commands so they use "--workspace" instead of "-p gobby-core" (e.g., update the cargo clippy, cargo nextest run and cargo test --doc invocations) and keep the existing separate "--no-default-features" runs (i.e., ensure you have both "cargo nextest run --profile ci --workspace" and "cargo nextest run --profile ci --workspace --no-default-features", and similarly "cargo test --doc --workspace" and "cargo test --doc --workspace --no-default-features").

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/commands/codewiki/mod.rs around lines 317 - 324, The match in run currently returns () implicitly; make the success path explicit by appending an explicit Ok(()) return from the run function after the match (i.e., keep the existing match on Format::{Json,Text} calling output::print_json and output::print_text, then return Ok(()) so run clearly returns Result<(), _>).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/commands/codewiki/prompts.rs at line 20, Replace the infallible write! calls that target the String variable prompt with more idiomatic String operations: use prompt.push_str(&format!(...)) when you need interpolation (e.g., replacing write!(prompt, "\nSignature: {signature}") ) and use prompt.push_str("literal") or prompt.push_str(&format!(...)) for other occurrences; for plain literals prefer push_str without format!. Update every write!(prompt, ...) instance in this file (the occurrences reported around the signature and other prompt-building lines) accordingly so string construction is direct and consistent.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcode/src/commands/symbol_at.rs around lines 201 - 217, Add a short doc comment to the function line_column_to_byte_offset explaining that it expects 1-based line and column inputs (matching LSP/editor UX) and that it returns a 0-based byte offset; mention behavior on out-of-range values (it bails) and that column/line are validated to be > 0 to clarify the conversion logic for future maintainers.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/provisioning/bootstrap.rs at line 3, Add a brief explanatory comment above the MAX_YAML_FLATTEN_DEPTH constant (and the other occurrence around the flatten logic at the code that enforces the limit) stating why 64 was chosen — e.g., "generous limit for legitimate config nesting while preventing infinite recursion/stack overflow on malformed YAML" — so maintainers understand the tradeoff; reference the constant name MAX_YAML_FLATTEN_DEPTH and the YAML flattening/checking block where the limit is enforced when adding the comment.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/provisioning/hub.rs around lines 227 - 228, The two variables existing_redacted and daemon_redacted both call redacted_postgres_dsn_placeholder() and end up identical, making error messages (e.g., HubConflict and the later warning) ambiguous; change the assignments so each uses a distinct placeholder string (for example "<existing-postgres-dsn>" for existing_redacted and "<daemon-postgres-dsn>" for daemon_redacted) or update redacted_postgres_dsn_placeholder to accept a label argument and invoke it with different labels; update any resulting log/error messages that reference existing_redacted and daemon_redacted to use the new distinct values so operators can tell them apart.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/provisioning/tests.rs around lines 144 - 160, The test gcore_yaml_rejects_excessive_nesting constructs a 66-level YAML but should use a 65-level input to more cleanly exercise the boundary; change the loop that builds the nested keys from 0..=65 to 0..65 and change the final indentation repeat from 66 to 65 so the YAML has 65 nested levels, then keep the call to StandaloneConfig::from_yaml_str and the existing assertion unchanged.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gcore/src/search.rs around lines 18 - 27, Wrap the raw string row identifier in a newtype to encode the safety contract: add a pub(crate) struct TrustedRowId(String) with an unsafe constructor unsafe fn new_unchecked(s: &str) -> TrustedRowId (or a private constructor and verified public helpers if you prefer), change pub fn bm25_score_expr(row_id: &str) -> String to accept row_id: &TrustedRowId and format using the inner string, and make the newtype and bm25_score_expr pub(crate) to restrict usage to internal crates; this keeps callers explicit about the trust boundary (use the symbol TrustedRowId and update all call sites that currently pass "c.id"/"d.id"/"cs.id" to wrap them with TrustedRowId::new_unchecked).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/commands/refresh/vault.rs at line 1, Replace the glob import `use super::*;` with explicit imports of only the symbols this module uses: inspect the code in this file for parent-module types/functions (e.g., Vault, VaultCommand, refresh_vault, Error, Result, any helper functions or traits) and write a `use super::{...};` listing them individually so dependencies are explicit and easier to refactor.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/commands/search.rs around lines 107 - 120, The code currently calls falkor.ok_or_else(|| required_search_config("FalkorDB"))? which fails when FalkorDB config is absent; change this to handle None gracefully like qdrant: leave falkor as an Option and build graph_backend by matching on that Option—if Some(config) try FalkorGraphBoostBackend::new(&config) and on Err wrap with UnavailableGraphBoostBackend::unreachable(error.to_string()), and if None directly construct UnavailableGraphBoostBackend::unreachable("FalkorDB config missing") (or similar message); update usage of the falkor variable accordingly and remove the ok_or_else that forces an early error.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/compile/tests.rs around lines 216 - 238, The test compile_rejects_target_page_through_symlinked_parent is unix-only; add a Windows counterpart gated with #[cfg(windows)] that performs the same assertion using std::os::windows::fs::symlink_file (or symlink_dir if appropriate) to create a symlinked parent and then calls write_target_page, expecting an Err matching WikiError::InvalidInput for field "target_page"; mirror the same assertions and error matching as the existing unix test and reuse the same helper write_target_page to keep behavior identical across platforms.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/document/mod.rs around lines 155 - 157, write_asset is invoked before subsequent writes (render_raw_document_markdown and write_raw_markdown), so if those later operations fail an orphaned asset may remain; modify the ingest flow in mod.rs to either perform markdown writes first or wrap the asset write in error-handling that removes the asset on failure (e.g., call cleanup/remove on the path returned by write_asset when render_raw_document_markdown or write_raw_markdown returns an Err). Locate the sequence using write_asset, render_raw_document_markdown, and write_raw_markdown and ensure any early return/error path after write_asset removes the created asset to avoid leaving files behind.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/document/office.rs around lines 271 - 285, The markdown_table function currently renders every input row including rows whose cells are all empty; update markdown_table to filter out fully-empty rows before computing column_count and rendering so blank rows are not emitted as noisy empty table rows—use the existing markdown_table and push_table_row identifiers to locate the function, remove rows where every cell is empty or whitespace, then proceed to compute column_count, write header/separator and remaining rows as before, returning the trimmed markdown string.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/document/office.rs around lines 232 - 269, The extract_xml_paragraphs function currently assumes <p> contains <t> and silently skips unexpected structure; update it to validate and log unexpected patterns: inside extract_xml_paragraphs (using reader, local_name, Event::Start/End, current, in_text, paragraphs) detect and emit a warning when you encounter a </p> with empty current or when text appears outside a <t> (or when Start/End events are for unexpected tags inside a <p>), and optionally count / record malformed paragraphs so callers can decide how to handle them; use the project’s logging (e.g., tracing::warn or the crate’s logging helper) to include context (tag names and a snippet of current) rather than silently dropping content.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/mod.rs at line 247, The _content_hash parameter on write_immutable_file is unused; either remove it or enforce validation—prefer enforcing it: update write_immutable_file to accept content_hash (rename to content_hash) and pass that into validate_existing_raw_file, then change validate_existing_raw_file (and any helper calls) to first compare the provided content_hash against the hash of source_path and return an error if they differ, and only after that check existing persisted file hashes; ensure all call sites that invoked write_immutable_file are updated to supply the expected content_hash (or remove the param everywhere if you choose the removal option).

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/mod.rs around lines 165 - 184, The yaml_plain_scalar_is_safe function currently misses timestamp-like strings (e.g., "2026-05-29") that YAML parsers can treat as dates; update yaml_plain_scalar_is_safe to detect common timestamp/date patterns (ISO date YYYY-MM-DD, datetime with T or space, optional timezone, and other common variants) and return false for matches, and add corresponding test cases to markdown_metadata_quotes_yaml_sensitive_scalars to cover those examples so the limitation is documented and prevented; reference yaml_plain_scalar_is_safe and the test markdown_metadata_quotes_yaml_sensitive_scalars when making the change.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/pdf/markdown.rs around lines 90 - 105, sanitize_pdf_page_markdown currently only replaces the exact substring "<!-- gwiki-page:" which misses variants like "<!-- gwiki-page :" or additional whitespace; update sanitize_pdf_page_markdown to more robustly neutralize any user text starting with the gwiki page marker (e.g., match the pattern "<!--\s*gwiki-page" using a regex or normalizing whitespace) and replace or escape it (for example convert the leading "<" to an HTML entity or insert a safe separator) so all variants (with or without space) are prevented from becoming internal page split markers.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/pdf/markdown.rs around lines 262 - 283, The dedupe_ocr_text flow relies on overlap_key (used on text_layer, each paragraph and full OCR via normalize_page_text) which currently strips everything to lowercase alphanumerics and thus can create false collisions (e.g., "A-1" vs "A1", emails, punctuation-sensitive tokens); update overlap_key (and callers in dedupe_ocr_text) to preserve more distinguishing structure or switch to a less lossy approach — e.g., keep punctuation characters like @ . - and underscores, or collapse only whitespace and lowercase (or use token-based/keyed n-grams) so keys better reflect real differences; adjust the logic in dedupe_ocr_text to rely on the new keys (function names: dedupe_ocr_text, overlap_key, normalize_page_text) and add a small unit test covering cases like "A-1" vs "A1" and "email@example.com" vs "emailexamplecom".

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/ingest/pdf/text.rs around lines 30 - 35, Add additional unit tests for normalize_page_text to cover edge cases: multiple consecutive blank lines, trailing blank lines, lines containing only whitespace, empty input, a single line without paragraph breaks, and input with no blank lines. For each case create a test function (e.g., normalize_page_text_multiple_blank_lines, normalize_page_text_trailing_blank_lines, normalize_page_text_whitespace_only_lines, normalize_page_text_empty_input, normalize_page_text_single_line, normalize_page_text_no_blank_lines) that calls normalize_page_text with representative inputs and asserts the expected normalized output preserving paragraph breaks and collapsing internal wraps; reuse the existing normalize_page_text_preserves_paragraph_breaks pattern for naming and assertions so tests are consistent and focused on the edge behaviors.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/main.rs around lines 10 - 33, The CLI_SUBCOMMANDS constant is a manually maintained list that can get out of sync with the CliCommand enum; add a unit test (e.g., cli_subcommands_list_is_complete) that iterates over all CliCommand variants and asserts each corresponding string is present in CLI_SUBCOMMANDS and that the lengths match, so missing or extra entries fail CI; implement the test by converting every CliCommand variant name to the expected kebab-case string (or provide the canonical expected strings derived from the enum) and use CLI_SUBCOMMANDS.contains(...) and an assert_eq!(CLI_SUBCOMMANDS.len(), expected.len()) to enforce completeness and prevent regressions.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/research/notes.rs around lines 67 - 70, The cleanup on write failure currently ignores fs::remove_file(&path); update the error handling after write_file_atomically returns Err to check the Result of fs::remove_file and log any removal error (including the path and error) instead of silencing it—use the existing logging facility (e.g., tracing::error! or process logger) in the same block that returns Err(error) for failed write of the "accepted research note"; keep the original return of the write error but ensure removal failures are emitted to logs for debugging.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/research/notes.rs around lines 277 - 288, Add a brief comment above the RESEARCH_NOTE_NAMESPACE constant explaining that research notes use a different UUID namespace than the Symbol ID namespace (e.g., c0de1de0-0000-4000-8000-000000000000) because note draft IDs are used for content deduplication/identity of research notes (via accepted_note_draft_id) rather than codebase symbol indexing, and that keeping a separate namespace prevents collisions and preserves semantic separation between symbol IDs and research-note UUIDs.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/research_loop/types.rs around lines 243 - 252, The builder's build() currently returns Result<ResearchLoopDeps<'a>, &'static str> with bare field-name strings; replace this with a small typed error (e.g., an enum BuildError with variants like MissingModel, MissingAsk, MissingSearch, MissingRead, MissingIngest, MissingNoteWriter) and change the signature of build() to Result<ResearchLoopDeps<'a>, BuildError>, then replace each ok_or("...")? with ok_or(BuildError::MissingModel)? (and corresponding variants for each field); optionally implement Display/std::error::Error for BuildError to preserve nice error messages when needed.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/session.rs around lines 64 - 66, Add a short inline comment above the default_project_id() function explaining that it returns "current" to maintain backward compatibility with old checkpoints and that this is safe because checkpoint validation (the root path matching logic used elsewhere) does not rely on project_id; also add the same explanatory comment where the "current" default is used elsewhere in this file (the other occurrence of the "current" default) so reviewers understand the compatibility rationale.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @crates/gwiki/src/video.rs around lines 880 - 882, The YAML frontmatter currently emits file_size_bytes and duration_seconds as quoted strings (via .to_string()); instead pass actual numeric values into markdown_metadata so the YAML serializer preserves them as numbers. Locate where metadata is assembled (look for markdown_metadata and the variables file_size_bytes and duration_seconds) and stop converting those numeric fields to strings—provide u64/i64 or f64 values directly; leave media_degradation as a string if intended. Ensure the metadata type passed to markdown_metadata uses numeric types so the resulting YAML frontmatter renders unquoted numbers.

- Verify each finding against current code. Fix only still-valid issues, skip the rest with a brief reason, keep changes minimal, and validate.

In @docs/guides/gcore-development-guide.md around lines 164 - 171, The docs list incorrect feature gate names: replace the "http" feature entry with "local-backend" (i.e., change the key name from http to local-backend and keep its dependencies ["dep:ureq"]) and update the "ai" feature dependencies to include "local-backend" instead of "http" (so "ai" should be ["dep:reqwest","dep:base64","dep:bytes","dep:httpdate","dep:rand","local-backend","reqwest/multipart"]); adjust those entries for the features "http"/"local-backend" and "ai" in the shown feature map to match Cargo.toml.
