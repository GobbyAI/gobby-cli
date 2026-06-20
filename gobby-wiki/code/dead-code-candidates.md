---
title: Dead-Code Candidates
type: code_dead_code_candidates
provenance: []
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# Dead-Code Candidates

> **CANDIDATES, not verdicts.** Everything below is a heuristic suggestion derived deterministically from the code graph and a source scan — no LLM. A symbol appearing here is *not* proof it is dead: reflection, trait objects, macros, FFI, conditional compilation, and external/test callers can all reach code without a recorded Call edge. Treat each entry as a lead to investigate, never as a delete list.

## Heuristic

A symbol is listed as a candidate only when ALL of the following hold:

1. It is a real definition (function, struct, enum, trait, class, type, or constant) — import/use rows and other index noise are skipped.
2. It has zero inbound calls: no Call edge in the code graph targets it. (Import edges are file-level, not symbol-level, so they never count as a call.)
3. It is not an entry point: its name is not `main`, and its `(file, name)` is not one of the CLI contract handler entry points (those are reached from dispatch, not via a Call edge).
4. It is not test-gated: no `#[test]`/`#[cfg(test)]` attribute sits above it, and it does not live under a tests path.
5. It is not a trait impl or method: its signature does not start with `impl `/`unsafe impl `, and its kind is not `method`. Methods are dispatched (often via traits or dynamic dispatch), so direct Call edges do not reliably represent them — they are excluded to avoid false positives.

> Note: the code graph was truncated for this run, so some inbound calls may be missing. This list may be incomplete and may contain extra entries.

> Note: the candidate list was capped at 500 entries; additional candidates were omitted.

## [[code/files/crates/gcode/src/cli.rs|crates/gcode/src/cli.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `Cli` | class | `crates/gcode/src/cli.rs:23` |
| `AiRouteArg` | type | `crates/gcode/src/cli.rs:49` |
| `AiDepthArg` | type | `crates/gcode/src/cli.rs:68` |
| `from` | function | `crates/gcode/src/cli.rs:76` |
| `AiProseDepthArg` | type | `crates/gcode/src/cli.rs:86` |
| `from` | function | `crates/gcode/src/cli.rs:94` |
| `AiRegisterArg` | type | `crates/gcode/src/cli.rs:104` |
| `from` | function | `crates/gcode/src/cli.rs:111` |
| `Command` | type | `crates/gcode/src/cli.rs:121` |
| `GraphCommand` | type | `crates/gcode/src/cli.rs:472` |
| `VectorCommand` | type | `crates/gcode/src/cli.rs:539` |
| `EmbeddingsCommand` | type | `crates/gcode/src/cli.rs:558` |
| `non_empty_grep_pattern` | function | `crates/gcode/src/cli.rs:563` |
| `positive_usize` | function | `crates/gcode/src/cli.rs:571` |
| `grep_max_count` | function | `crates/gcode/src/cli.rs:575` |
| `bounded_positive_usize` | function | `crates/gcode/src/cli.rs:579` |
| `effective_format` | function | `crates/gcode/src/cli.rs:592` |

## [[code/files/crates/gcode/src/commands/codewiki/architecture_diagrams.rs|crates/gcode/src/commands/codewiki/architecture_diagrams.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `render_architecture_diagrams` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:40` |
| `render_service_matrix` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:88` |
| `service_requirement` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:125` |
| `render_topology_flowchart` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:142` |
| `render_runtime_flow_sequence` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:250` |
| `render_ai_generation_flow` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:259` |
| `render_ghook_enqueue_flow` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:295` |
| `has_mode` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:323` |
| `ai_feature_crate` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:329` |
| `provenance_crate` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:341` |
| `node_id` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:349` |
| `service_node_id` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:362` |
| `service_edge_label` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:384` |
| `mermaid_label` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:398` |
| `fence` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:411` |
| `is_valid_mermaid` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:433` |
| `balanced_delimiters` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:482` |
| `sample_model` | function | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs:525` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/architecture.rs|crates/gcode/src/commands/codewiki/build_parts/architecture.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `build_architecture_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5` |
| `module_dependency_edges` | function | `crates/gcode/src/commands/codewiki/build_parts/architecture.rs:176` |
| `dependency_topology` | function | `crates/gcode/src/commands/codewiki/build_parts/architecture.rs:194` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/audit.rs|crates/gcode/src/commands/codewiki/build_parts/audit.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `AuditContext` | class | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:38` |
| `build_audit_context` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:55` |
| `entry_points_from_catalog` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:87` |
| `build_deprecation_index` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:111` |
| `deprecation_reason` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:137` |
| `lookback_lines` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:159` |
| `looks_like_attribute_continuation` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:202` |
| `deprecated_attribute_reason` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:213` |
| `extract_note` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:226` |
| `doc_comment_deprecation` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:244` |
| `first_meaningful_line` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:259` |
| `cap_reason` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:267` |
| `build_deprecations_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:277` |
| `build_dead_code_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:311` |
| `inbound_call_targets` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:369` |
| `is_candidate` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:380` |
| `is_real_definition_kind` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:408` |
| `is_entry_point` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:415` |
| `is_trait_impl_or_method` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:427` |
| `is_test_path` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:467` |
| `lines` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:475` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/changes.rs|crates/gcode/src/commands/codewiki/build_parts/changes.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `build_codewiki_changes_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/changes.rs:5` |
| `ChangesFrontmatter` | class | `crates/gcode/src/commands/codewiki/build_parts/changes.rs:104` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts.rs|crates/gcode/src/commands/codewiki/build_parts/concepts.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `build_curated_navigation_docs` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs|crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `normalize_concepts` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:140` |
| `normalize_sections` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:183` |
| `normalize_narrative_pages` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:219` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs|crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `chapter_link` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:136` |
| `render_concept_tree` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:140` |
| `render_concept_page` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:188` |
| `render_narrative_page` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:210` |
| `append_curated_body` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:254` |
| `append_explore_section` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:277` |
| `narrative_members` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:303` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs|crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `narrative_spans` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:15` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs|crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `degraded_sources` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:1` |
| `concept_doc_path` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:27` |
| `concept_doc_stem` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:31` |
| `narrative_doc_path` | function | `crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:35` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs|crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `CuratedNavigationPlan` | class | `crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6` |
| `ConceptModule` | class | `crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:16` |
| `ConceptSection` | class | `crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:40` |
| `NarrativePage` | class | `crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:49` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/curated_content.rs|crates/gcode/src/commands/codewiki/build_parts/curated_content.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `CuratedPageKind` | type | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28` |
| `CuratedBody` | class | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:34` |
| `curated_page_body` | function | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:51` |
| `member_evidence_rows` | function | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:140` |
| `symbol_evidence_rows` | function | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:170` |
| `span_citation` | function | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:193` |
| `structural_body` | function | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:204` |
| `append_guided_tour` | function | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:268` |
| `append_ask_hint` | function | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:284` |
| `append_tour_nav` | function | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:293` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/features.rs|crates/gcode/src/commands/codewiki/build_parts/features.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `Contract` | class | `crates/gcode/src/commands/codewiki/build_parts/features.rs:16` |
| `ContractCommand` | class | `crates/gcode/src/commands/codewiki/build_parts/features.rs:22` |
| `ContractFlag` | class | `crates/gcode/src/commands/codewiki/build_parts/features.rs:31` |
| `BinaryContract` | class | `crates/gcode/src/commands/codewiki/build_parts/features.rs:39` |
| `resolve_handler` | function | `crates/gcode/src/commands/codewiki/build_parts/features.rs:71` |
| `resolve_gcode_handler` | function | `crates/gcode/src/commands/codewiki/build_parts/features.rs:82` |
| `resolve_gwiki_handler` | function | `crates/gcode/src/commands/codewiki/build_parts/features.rs:236` |
| `section_for_binary` | function | `crates/gcode/src/commands/codewiki/build_parts/features.rs:331` |
| `build_feature_catalog_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/features.rs:382` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/file.rs|crates/gcode/src/commands/codewiki/build_parts/file.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `FileDocPosition` | class | `crates/gcode/src/commands/codewiki/build_parts/file.rs:14` |
| `build_file_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/file.rs:20` |
| `build_file_body` | function | `crates/gcode/src/commands/codewiki/build_parts/file.rs:202` |
| `structural_file_body` | function | `crates/gcode/src/commands/codewiki/build_parts/file.rs:267` |
| `file_summary_from_body` | function | `crates/gcode/src/commands/codewiki/build_parts/file.rs:289` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/hotspots.rs|crates/gcode/src/commands/codewiki/build_parts/hotspots.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `build_hotspots_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs|crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `InfraDescriptor` | class | `crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs:8` |
| `infra_descriptor` | function | `crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs:27` |
| `build_infrastructure_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs:121` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/modules.rs|crates/gcode/src/commands/codewiki/build_parts/modules.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `build_module_docs_with_filter` | function | `crates/gcode/src/commands/codewiki/build_parts/modules.rs:27` |
| `file_is_direct_module_member` | function | `crates/gcode/src/commands/codewiki/build_parts/modules.rs:203` |
| `prompt_component_ids_for_module` | function | `crates/gcode/src/commands/codewiki/build_parts/modules.rs:207` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/onboarding.rs|crates/gcode/src/commands/codewiki/build_parts/onboarding.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `build_onboarding_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7` |
| `symbol_with_signature` | function | `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:217` |

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/snapshot.rs|crates/gcode/src/commands/codewiki/build_parts/snapshot.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `build_codewiki_index_snapshot` | function | `crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6` |

## [[code/files/crates/gcode/src/commands/codewiki/cluster.rs|crates/gcode/src/commands/codewiki/cluster.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `symbols_by_file_component` | function | `crates/gcode/src/commands/codewiki/cluster.rs:227` |
| `first_component_for_file` | function | `crates/gcode/src/commands/codewiki/cluster.rs:239` |
| `files_for_import_target` | function | `crates/gcode/src/commands/codewiki/cluster.rs:249` |

## [[code/files/crates/gcode/src/commands/codewiki/generation.rs|crates/gcode/src/commands/codewiki/generation.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `generate_hierarchical_docs` | function | `crates/gcode/src/commands/codewiki/generation.rs:20` |
| `generate_hierarchical_docs_with_graph_availability` | function | `crates/gcode/src/commands/codewiki/generation.rs:30` |
| `generate_hierarchical_docs_with_ownership` | function | `crates/gcode/src/commands/codewiki/generation.rs:61` |
| `generate_hierarchical_docs_core` | function | `crates/gcode/src/commands/codewiki/generation.rs:177` |

## [[code/files/crates/gcode/src/commands/codewiki/graph.rs|crates/gcode/src/commands/codewiki/graph.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `fetch_codewiki_graph_edges` | function | `crates/gcode/src/commands/codewiki/graph.rs:5` |

## [[code/files/crates/gcode/src/commands/codewiki/io.rs|crates/gcode/src/commands/codewiki/io.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `write_doc_set` | function | `crates/gcode/src/commands/codewiki/io.rs:3` |
| `write_incremental_doc_set` | function | `crates/gcode/src/commands/codewiki/io.rs:11` |
| `write_incremental_doc_set_with_snapshot` | function | `crates/gcode/src/commands/codewiki/io.rs:30` |
| `DocPruneScope` | class | `crates/gcode/src/commands/codewiki/io.rs:46` |
| `DocSink` | class | `crates/gcode/src/commands/codewiki/io.rs:99` |
| `open_with_prune_scope` | function | `crates/gcode/src/commands/codewiki/io.rs:127` |
| `with_since` | function | `crates/gcode/src/commands/codewiki/io.rs:155` |
| `persist` | function | `crates/gcode/src/commands/codewiki/io.rs:162` |
| `flush` | function | `crates/gcode/src/commands/codewiki/io.rs:247` |
| `finish` | function | `crates/gcode/src/commands/codewiki/io.rs:262` |
| `scoped_file_doc` | function | `crates/gcode/src/commands/codewiki/io.rs:293` |
| `scoped_module_doc` | function | `crates/gcode/src/commands/codewiki/io.rs:299` |
| `write_doc` | function | `crates/gcode/src/commands/codewiki/io.rs:305` |
| `reject_symlinked_doc_path` | function | `crates/gcode/src/commands/codewiki/io.rs:315` |
| `prune_empty_doc_dirs` | function | `crates/gcode/src/commands/codewiki/io.rs:335` |
| `read_codewiki_meta` | function | `crates/gcode/src/commands/codewiki/io.rs:357` |
| `write_codewiki_meta` | function | `crates/gcode/src/commands/codewiki/io.rs:377` |
| `read_ownership_meta` | function | `crates/gcode/src/commands/codewiki/io.rs:382` |
| `write_ownership_meta` | function | `crates/gcode/src/commands/codewiki/io.rs:391` |
| `source_hashes_for_doc` | function | `crates/gcode/src/commands/codewiki/io.rs:396` |
| `neighbor_hashes_for_doc` | function | `crates/gcode/src/commands/codewiki/io.rs:423` |
| `source_files_from_frontmatter` | function | `crates/gcode/src/commands/codewiki/io.rs:448` |
| `safe_doc_path` | function | `crates/gcode/src/commands/codewiki/io.rs:528` |

## [[code/files/crates/gcode/src/commands/codewiki/ownership.rs|crates/gcode/src/commands/codewiki/ownership.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `OwnershipOptions` | class | `crates/gcode/src/commands/codewiki/ownership.rs:20` |
| `OwnershipMeta` | class | `crates/gcode/src/commands/codewiki/ownership.rs:35` |
| `CachedBlameSummary` | class | `crates/gcode/src/commands/codewiki/ownership.rs:41` |
| `OwnershipContributor` | class | `crates/gcode/src/commands/codewiki/ownership.rs:47` |
| `OwnershipStatus` | class | `crates/gcode/src/commands/codewiki/ownership.rs:56` |
| `FileOwnership` | class | `crates/gcode/src/commands/codewiki/ownership.rs:64` |
| `build_ownership_doc` | function | `crates/gcode/src/commands/codewiki/ownership.rs:69` |

## [[code/files/crates/gcode/src/commands/codewiki/ownership/analysis.rs|crates/gcode/src/commands/codewiki/ownership/analysis.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `BlameContributorsOutcome` | type | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:17` |
| `content_hash` | function | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:89` |
| `blame_file_contributors_with_timeout` | function | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:93` |
| `GitBlameOutput` | class | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:106` |
| `blame_file_contributors` | function | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:112` |
| `git_blame_output_with_timeout` | function | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:135` |
| `read_tempfile` | function | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:167` |
| `parse_git_blame_porcelain` | function | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:174` |
| `git_blame_email` | function | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:229` |
| `contributor_id` | function | `crates/gcode/src/commands/codewiki/ownership/analysis.rs:238` |

## [[code/files/crates/gcode/src/commands/codewiki/ownership/codeowners.rs|crates/gcode/src/commands/codewiki/ownership/codeowners.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `Codeowners` | class | `crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5` |
| `CodeownersEntry` | class | `crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10` |

## [[code/files/crates/gcode/src/commands/codewiki/ownership/render.rs|crates/gcode/src/commands/codewiki/ownership/render.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `degraded_sources` | function | `crates/gcode/src/commands/codewiki/ownership/render.rs:10` |
| `Frontmatter` | class | `crates/gcode/src/commands/codewiki/ownership/render.rs:38` |
| `is_false` | function | `crates/gcode/src/commands/codewiki/ownership/render.rs:70` |

## [[code/files/crates/gcode/src/commands/codewiki/paths.rs|crates/gcode/src/commands/codewiki/paths.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `inline_code` | function | `crates/gcode/src/commands/codewiki/paths.rs:3` |
| `write_markdown_table_header` | function | `crates/gcode/src/commands/codewiki/paths.rs:16` |
| `write_markdown_table_row` | function | `crates/gcode/src/commands/codewiki/paths.rs:21` |
| `markdown_table_cell` | function | `crates/gcode/src/commands/codewiki/paths.rs:35` |
| `max_backtick_run` | function | `crates/gcode/src/commands/codewiki/paths.rs:43` |
| `plural` | function | `crates/gcode/src/commands/codewiki/paths.rs:57` |
| `component_label` | function | `crates/gcode/src/commands/codewiki/paths.rs:61` |
| `is_core_file` | function | `crates/gcode/src/commands/codewiki/paths.rs:70` |
| `in_scope` | function | `crates/gcode/src/commands/codewiki/paths.rs:136` |
| `module_for_file` | function | `crates/gcode/src/commands/codewiki/paths.rs:146` |
| `module_ancestors` | function | `crates/gcode/src/commands/codewiki/paths.rs:154` |
| `parent_module` | function | `crates/gcode/src/commands/codewiki/paths.rs:164` |
| `module_is_ancestor` | function | `crates/gcode/src/commands/codewiki/paths.rs:168` |
| `direct_child_modules` | function | `crates/gcode/src/commands/codewiki/paths.rs:172` |
| `module_depth` | function | `crates/gcode/src/commands/codewiki/paths.rs:182` |
| `file_doc_path` | function | `crates/gcode/src/commands/codewiki/paths.rs:186` |
| `module_doc_path` | function | `crates/gcode/src/commands/codewiki/paths.rs:190` |
| `file_wikilink` | function | `crates/gcode/src/commands/codewiki/paths.rs:194` |
| `module_wikilink` | function | `crates/gcode/src/commands/codewiki/paths.rs:198` |

## [[code/files/crates/gcode/src/commands/codewiki/progress.rs|crates/gcode/src/commands/codewiki/progress.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `CodewikiProgressSink` | type | `crates/gcode/src/commands/codewiki/progress.rs:2` |
| `CodewikiProgress` | class | `crates/gcode/src/commands/codewiki/progress.rs:10` |

## [[code/files/crates/gcode/src/commands/codewiki/prompts.rs|crates/gcode/src/commands/codewiki/prompts.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `with_register` | function | `crates/gcode/src/commands/codewiki/prompts.rs:36` |
| `symbol_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:53` |
| `file_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:77` |
| `content_file_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:95` |
| `module_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:103` |
| `repo_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:123` |
| `append_child_summary_table` | function | `crates/gcode/src/commands/codewiki/prompts.rs:148` |
| `append_component_table` | function | `crates/gcode/src/commands/codewiki/prompts.rs:158` |
| `append_table_guidance` | function | `crates/gcode/src/commands/codewiki/prompts.rs:165` |
| `architecture_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:171` |
| `architecture_narrative_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:192` |
| `PageEvidenceRow` | class | `crates/gcode/src/commands/codewiki/prompts.rs:228` |
| `concept_page_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:237` |
| `narrative_page_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:257` |
| `verify_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:282` |
| `build_curated_page_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:308` |
| `append_evidence_table` | function | `crates/gcode/src/commands/codewiki/prompts.rs:346` |
| `append_symbol_summary_table` | function | `crates/gcode/src/commands/codewiki/prompts.rs:361` |
| `append_relationship_section` | function | `crates/gcode/src/commands/codewiki/prompts.rs:399` |
| `build_entity_prompt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:444` |
| `append_child_summary_sections` | function | `crates/gcode/src/commands/codewiki/prompts.rs:463` |
| `append_source_excerpt_section` | function | `crates/gcode/src/commands/codewiki/prompts.rs:488` |
| `append_source_excerpt_section_n` | function | `crates/gcode/src/commands/codewiki/prompts.rs:495` |
| `summary_excerpt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:540` |
| `bounded_excerpt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:564` |
| `SymbolSummary` | class | `crates/gcode/src/commands/codewiki/prompts.rs:581` |
| `ChildSummary` | class | `crates/gcode/src/commands/codewiki/prompts.rs:592` |
| `SourceExcerpt` | class | `crates/gcode/src/commands/codewiki/prompts.rs:600` |
| `oversized_child` | function | `crates/gcode/src/commands/codewiki/prompts.rs:650` |
| `excerpt` | function | `crates/gcode/src/commands/codewiki/prompts.rs:879` |
| `evidence` | function | `crates/gcode/src/commands/codewiki/prompts.rs:962` |

## [[code/files/crates/gcode/src/commands/codewiki/relationship_facts.rs|crates/gcode/src/commands/codewiki/relationship_facts.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `SymbolRelation` | class | `crates/gcode/src/commands/codewiki/relationship_facts.rs:29` |
| `RelationshipFacts` | class | `crates/gcode/src/commands/codewiki/relationship_facts.rs:53` |
| `relationship_facts_for_file` | function | `crates/gcode/src/commands/codewiki/relationship_facts.rs:100` |
| `call_relation` | function | `crates/gcode/src/commands/codewiki/relationship_facts.rs:160` |
| `import_relation` | function | `crates/gcode/src/commands/codewiki/relationship_facts.rs:183` |
| `bound_relations` | function | `crates/gcode/src/commands/codewiki/relationship_facts.rs:203` |
| `symbol` | function | `crates/gcode/src/commands/codewiki/relationship_facts.rs:221` |
| `id_set` | function | `crates/gcode/src/commands/codewiki/relationship_facts.rs:251` |
| `by_id` | function | `crates/gcode/src/commands/codewiki/relationship_facts.rs:255` |

## [[code/files/crates/gcode/src/commands/codewiki/render/audit.rs|crates/gcode/src/commands/codewiki/render/audit.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `render_deprecations_doc` | function | `crates/gcode/src/commands/codewiki/render/audit.rs:8` |
| `render_dead_code_doc` | function | `crates/gcode/src/commands/codewiki/render/audit.rs:63` |

## [[code/files/crates/gcode/src/commands/codewiki/render/common.rs|crates/gcode/src/commands/codewiki/render/common.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `model_degraded_sources` | function | `crates/gcode/src/commands/codewiki/render/common.rs:1` |
| `cell_summary` | function | `crates/gcode/src/commands/codewiki/render/common.rs:23` |

## [[code/files/crates/gcode/src/commands/codewiki/render/diagrams.rs|crates/gcode/src/commands/codewiki/render/diagrams.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `collect_subsystem_dependency_edges` | function | `crates/gcode/src/commands/codewiki/render/diagrams.rs:7` |

## [[code/files/crates/gcode/src/commands/codewiki/render/features.rs|crates/gcode/src/commands/codewiki/render/features.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `render_feature_catalog_doc` | function | `crates/gcode/src/commands/codewiki/render/features.rs:11` |
| `render_ghook_section` | function | `crates/gcode/src/commands/codewiki/render/features.rs:78` |

## [[code/files/crates/gcode/src/commands/codewiki/render/infrastructure.rs|crates/gcode/src/commands/codewiki/render/infrastructure.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `render_infrastructure_doc` | function | `crates/gcode/src/commands/codewiki/render/infrastructure.rs:10` |

## [[code/files/crates/gcode/src/commands/codewiki/render/overview.rs|crates/gcode/src/commands/codewiki/render/overview.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `render_architecture_doc` | function | `crates/gcode/src/commands/codewiki/render/overview.rs:5` |
| `render_onboarding_doc` | function | `crates/gcode/src/commands/codewiki/render/overview.rs:65` |
| `render_hotspots_doc` | function | `crates/gcode/src/commands/codewiki/render/overview.rs:104` |
| `write_hotspot_section` | function | `crates/gcode/src/commands/codewiki/render/overview.rs:141` |
| `write_hotspot_section_with_cross_refs` | function | `crates/gcode/src/commands/codewiki/render/overview.rs:145` |

## [[code/files/crates/gcode/src/commands/codewiki/render/pages.rs|crates/gcode/src/commands/codewiki/render/pages.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `render_module_doc` | function | `crates/gcode/src/commands/codewiki/render/pages.rs:5` |
| `render_file_doc` | function | `crates/gcode/src/commands/codewiki/render/pages.rs:53` |
| `push_test_summary_line` | function | `crates/gcode/src/commands/codewiki/render/pages.rs:149` |

## [[code/files/crates/gcode/src/commands/codewiki/render/repo.rs|crates/gcode/src/commands/codewiki/render/repo.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `build_repo_doc` | function | `crates/gcode/src/commands/codewiki/render/repo.rs:4` |
| `repo_source_excerpts` | function | `crates/gcode/src/commands/codewiki/render/repo.rs:80` |
| `render_repo_doc` | function | `crates/gcode/src/commands/codewiki/render/repo.rs:102` |

## [[code/files/crates/gcode/src/commands/codewiki/repair.rs|crates/gcode/src/commands/codewiki/repair.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `CitationRepairSummary` | class | `crates/gcode/src/commands/codewiki/repair.rs:21` |
| `IndexCitationResolver` | class | `crates/gcode/src/commands/codewiki/repair.rs:40` |
| `repair_citations` | function | `crates/gcode/src/commands/codewiki/repair.rs:153` |

## [[code/files/crates/gcode/src/commands/codewiki/reuse.rs|crates/gcode/src/commands/codewiki/reuse.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `ReusePlan` | class | `crates/gcode/src/commands/codewiki/reuse.rs:11` |
| `span_files` | function | `crates/gcode/src/commands/codewiki/reuse.rs:235` |
| `set_matches` | function | `crates/gcode/src/commands/codewiki/reuse.rs:241` |

## [[code/files/crates/gcode/src/commands/codewiki/run.rs|crates/gcode/src/commands/codewiki/run.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `run_repair` | function | `crates/gcode/src/commands/codewiki/run.rs:230` |
| `validate_edge_limit` | function | `crates/gcode/src/commands/codewiki/run.rs:252` |
| `git_changed_files` | function | `crates/gcode/src/commands/codewiki/run.rs:263` |
| `documents_file` | function | `crates/gcode/src/commands/codewiki/run.rs:290` |
| `should_document_file` | function | `crates/gcode/src/commands/codewiki/run.rs:296` |
| `load_symbols_for_codewiki` | function | `crates/gcode/src/commands/codewiki/run.rs:300` |
| `load_leading_chunks` | function | `crates/gcode/src/commands/codewiki/run.rs:312` |

## [[code/files/crates/gcode/src/commands/codewiki/system_model.rs|crates/gcode/src/commands/codewiki/system_model.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `Crate` | class | `crates/gcode/src/commands/codewiki/system_model.rs:30` |
| `Edge` | class | `crates/gcode/src/commands/codewiki/system_model.rs:45` |
| `ServiceKind` | type | `crates/gcode/src/commands/codewiki/system_model.rs:54` |
| `ServiceBoundary` | class | `crates/gcode/src/commands/codewiki/system_model.rs:85` |
| `RuntimeMode` | type | `crates/gcode/src/commands/codewiki/system_model.rs:98` |
| `SystemModel` | class | `crates/gcode/src/commands/codewiki/system_model.rs:110` |
| `build_system_model` | function | `crates/gcode/src/commands/codewiki/system_model.rs:148` |
| `workspace_members` | function | `crates/gcode/src/commands/codewiki/system_model.rs:266` |
| `package_name` | function | `crates/gcode/src/commands/codewiki/system_model.rs:303` |
| `has_table_array` | function | `crates/gcode/src/commands/codewiki/system_model.rs:313` |
| `dependency_entries` | function | `crates/gcode/src/commands/codewiki/system_model.rs:324` |
| `dependency_features` | function | `crates/gcode/src/commands/codewiki/system_model.rs:340` |
| `feature_table_keys` | function | `crates/gcode/src/commands/codewiki/system_model.rs:358` |
| `feature_services` | function | `crates/gcode/src/commands/codewiki/system_model.rs:369` |
| `service_name` | function | `crates/gcode/src/commands/codewiki/system_model.rs:380` |
| `service_boundaries` | function | `crates/gcode/src/commands/codewiki/system_model.rs:398` |
| `toolchain_boundaries` | function | `crates/gcode/src/commands/codewiki/system_model.rs:481` |
| `fixture_workspace` | function | `crates/gcode/src/commands/codewiki/system_model.rs:540` |
| `crate_named` | function | `crates/gcode/src/commands/codewiki/system_model.rs:561` |

## [[code/files/crates/gcode/src/commands/codewiki/text/citations.rs|crates/gcode/src/commands/codewiki/text/citations.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `is_asset_or_data_file` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:26` |
| `lexical_tokens` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:38` |
| `citation_relevance` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:46` |
| `fallback_spans` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:58` |
| `citation_list` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:100` |
| `wrap_citation_items` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:108` |
| `citation_markers` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:130` |
| `citation_references` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:144` |
| `replace_citations_with_markers` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:155` |
| `write_references` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:166` |
| `ground_text` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:181` |
| `strip_invalid_citations` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:199` |
| `contains_valid_citation` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:227` |
| `contains_bare_citation` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:256` |
| `citation_parts` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:270` |
| `citation_inner` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:288` |
| `CitationResolver` | type | `crates/gcode/src/commands/codewiki/text/citations.rs:301` |
| `ReanchorResult` | class | `crates/gcode/src/commands/codewiki/text/citations.rs:316` |
| `reanchor_citations` | function | `crates/gcode/src/commands/codewiki/text/citations.rs:329` |

## [[code/files/crates/gcode/src/commands/codewiki/text/frontmatter.rs|crates/gcode/src/commands/codewiki/text/frontmatter.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `Frontmatter` | class | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:7` |
| `FrontmatterSourceFile` | class | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:26` |
| `FrontmatterVerifyNote` | class | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:33` |
| `frontmatter_with_degradation` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:50` |
| `frontmatter_with_degradation_without_ranges` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:59` |
| `frontmatter_with_degradation_and_verify_notes_without_ranges` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:68` |
| `frontmatter_with_options` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:85` |
| `append_relevant_source_files` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:126` |
| `append_curated_source_files` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:170` |
| `frontmatter_source_files` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:200` |
| `format_frontmatter_ranges` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:248` |
| `source_range_href` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:274` |
| `encode_markdown_path` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:282` |
| `escape_markdown_link_label` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:293` |
| `spans` | function | `crates/gcode/src/commands/codewiki/text/frontmatter.rs:304` |

## [[code/files/crates/gcode/src/commands/codewiki/text/generation.rs|crates/gcode/src/commands/codewiki/text/generation.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `resolve_text_generator` | function | `crates/gcode/src/commands/codewiki/text/generation.rs:23` |
| `resolve_text_verifier` | function | `crates/gcode/src/commands/codewiki/text/generation.rs:89` |
| `generate_with_bounded_retry` | function | `crates/gcode/src/commands/codewiki/text/generation.rs:159` |
| `retryable_generation_error` | function | `crates/gcode/src/commands/codewiki/text/generation.rs:175` |
| `resolve_ai_context` | function | `crates/gcode/src/commands/codewiki/text/generation.rs:185` |
| `Generation` | type | `crates/gcode/src/commands/codewiki/text/generation.rs:205` |
| `maybe_generate` | function | `crates/gcode/src/commands/codewiki/text/generation.rs:230` |
| `is_prompt_echo` | function | `crates/gcode/src/commands/codewiki/text/generation.rs:253` |
| `clean_generated` | function | `crates/gcode/src/commands/codewiki/text/generation.rs:265` |

## [[code/files/crates/gcode/src/commands/codewiki/text/sanitize.rs|crates/gcode/src/commands/codewiki/text/sanitize.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `sanitize_model_markdown_links` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:7` |
| `citation_anchor_replacements` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:20` |
| `anchor_citation_target` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:64` |
| `is_ascii_line_number` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:86` |
| `neutralize_symbol_purpose_links` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:90` |
| `markdown_link_replacements` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:97` |
| `markdown_code_ranges` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:107` |
| `wikilink_replacements` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:117` |
| `replacement_for_range` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:142` |
| `range_contains` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:149` |
| `range_overlaps` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:155` |
| `apply_replacements` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:161` |
| `LinkFrame` | class | `crates/gcode/src/commands/codewiki/text/sanitize.rs:183` |
| `Replacement` | class | `crates/gcode/src/commands/codewiki/text/sanitize.rs:189` |
| `unsafe_link_replacements` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:194` |
| `push_label_text` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:236` |
| `is_unsafe_link_target` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:242` |
| `is_windows_absolute_path` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:266` |
| `has_uri_scheme` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:274` |
| `contains_parent_dir_segment` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:286` |
| `starts_with_ignore_ascii_case` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:291` |
| `span` | function | `crates/gcode/src/commands/codewiki/text/sanitize.rs:303` |

## [[code/files/crates/gcode/src/commands/codewiki/text/structural.rs|crates/gcode/src/commands/codewiki/text/structural.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `structural_symbol_purpose` | function | `crates/gcode/src/commands/codewiki/text/structural.rs:7` |
| `display_child_summary` | function | `crates/gcode/src/commands/codewiki/text/structural.rs:38` |
| `structural_module_summary` | function | `crates/gcode/src/commands/codewiki/text/structural.rs:43` |
| `structural_repo_summary` | function | `crates/gcode/src/commands/codewiki/text/structural.rs:57` |
| `write_section` | function | `crates/gcode/src/commands/codewiki/text/structural.rs:65` |
| `collect_link_spans` | function | `crates/gcode/src/commands/codewiki/text/structural.rs:69` |

## [[code/files/crates/gcode/src/commands/codewiki/text/verify.rs|crates/gcode/src/commands/codewiki/text/verify.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `VerifyOutcome` | type | `crates/gcode/src/commands/codewiki/text/verify.rs:19` |
| `VerifyNoteResponse` | class | `crates/gcode/src/commands/codewiki/text/verify.rs:79` |
| `symbols` | function | `crates/gcode/src/commands/codewiki/text/verify.rs:113` |

## [[code/files/crates/gcode/src/commands/codewiki/types.rs|crates/gcode/src/commands/codewiki/types.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `CodewikiInput` | class | `crates/gcode/src/commands/codewiki/types.rs:11` |
| `LeadingChunk` | class | `crates/gcode/src/commands/codewiki/types.rs:26` |
| `source_excerpt_for_file` | function | `crates/gcode/src/commands/codewiki/types.rs:33` |
| `ranked_source_excerpts` | function | `crates/gcode/src/commands/codewiki/types.rs:50` |
| `CodewikiGraphEdge` | class | `crates/gcode/src/commands/codewiki/types.rs:65` |
| `CodewikiGraphEdgeKind` | type | `crates/gcode/src/commands/codewiki/types.rs:96` |
| `CodewikiGraph` | class | `crates/gcode/src/commands/codewiki/types.rs:102` |
| `CodewikiGraphAvailability` | type | `crates/gcode/src/commands/codewiki/types.rs:131` |
| `FileDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:138` |
| `SymbolDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:161` |
| `ModuleDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:185` |
| `ArchitectureDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:201` |
| `ArchitectureSubsystem` | class | `crates/gcode/src/commands/codewiki/types.rs:221` |
| `InfraSection` | class | `crates/gcode/src/commands/codewiki/types.rs:234` |
| `InfrastructureDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:247` |
| `FeatureEntry` | class | `crates/gcode/src/commands/codewiki/types.rs:258` |
| `FeatureBinarySection` | class | `crates/gcode/src/commands/codewiki/types.rs:269` |
| `FeatureCatalogDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:279` |
| `DeprecationIndex` | type | `crates/gcode/src/commands/codewiki/types.rs:289` |
| `TestIndex` | type | `crates/gcode/src/commands/codewiki/types.rs:295` |
| `DeprecatedSymbol` | class | `crates/gcode/src/commands/codewiki/types.rs:301` |
| `DeprecationsDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:314` |
| `DeadCodeCandidate` | class | `crates/gcode/src/commands/codewiki/types.rs:324` |
| `DeadCodeDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:337` |
| `OnboardingDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:352` |
| `OnboardingEntryPoint` | class | `crates/gcode/src/commands/codewiki/types.rs:360` |
| `OnboardingStep` | class | `crates/gcode/src/commands/codewiki/types.rs:367` |
| `HotspotsDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:375` |
| `HotspotFinding` | class | `crates/gcode/src/commands/codewiki/types.rs:384` |
| `HotspotNode` | class | `crates/gcode/src/commands/codewiki/types.rs:393` |
| `FileLink` | class | `crates/gcode/src/commands/codewiki/types.rs:403` |
| `ModuleLink` | class | `crates/gcode/src/commands/codewiki/types.rs:410` |
| `SourceSpan` | class | `crates/gcode/src/commands/codewiki/types.rs:417` |
| `VerifyNote` | class | `crates/gcode/src/commands/codewiki/types.rs:427` |
| `normalize_verify_note_reason` | function | `crates/gcode/src/commands/codewiki/types.rs:441` |
| `CodewikiRunSummary` | class | `crates/gcode/src/commands/codewiki/types.rs:454` |
| `CodewikiMeta` | class | `crates/gcode/src/commands/codewiki/types.rs:469` |
| `CodewikiDocMeta` | class | `crates/gcode/src/commands/codewiki/types.rs:479` |
| `BuiltDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:518` |
| `CodewikiIndexSnapshot` | class | `crates/gcode/src/commands/codewiki/types.rs:573` |
| `CodewikiFileSnapshot` | class | `crates/gcode/src/commands/codewiki/types.rs:583` |
| `CodewikiSymbolSnapshot` | class | `crates/gcode/src/commands/codewiki/types.rs:589` |
| `TextGenerator` | type | `crates/gcode/src/commands/codewiki/types.rs:597` |
| `TextVerifier` | type | `crates/gcode/src/commands/codewiki/types.rs:605` |
| `PromptTier` | type | `crates/gcode/src/commands/codewiki/types.rs:612` |
| `AiDepth` | type | `crates/gcode/src/commands/codewiki/types.rs:621` |
| `ProseDepth` | type | `crates/gcode/src/commands/codewiki/types.rs:654` |
| `ProseRegister` | type | `crates/gcode/src/commands/codewiki/types.rs:681` |
| `CodewikiAiOptions` | class | `crates/gcode/src/commands/codewiki/types.rs:693` |

## [[code/files/crates/gcode/src/commands/embeddings_doctor.rs|crates/gcode/src/commands/embeddings_doctor.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `EmbeddingsDoctorExit` | class | `crates/gcode/src/commands/embeddings_doctor.rs:19` |
| `EmbeddingsDoctorReport` | class | `crates/gcode/src/commands/embeddings_doctor.rs:43` |
| `EmbeddingsDoctorDrift` | class | `crates/gcode/src/commands/embeddings_doctor.rs:58` |
| `PeerDoctorReport` | class | `crates/gcode/src/commands/embeddings_doctor.rs:66` |
| `PeerDoctorOutcome` | type | `crates/gcode/src/commands/embeddings_doctor.rs:73` |
| `probe_dim` | function | `crates/gcode/src/commands/embeddings_doctor.rs:97` |
| `build_doctor_report` | function | `crates/gcode/src/commands/embeddings_doctor.rs:101` |
| `report_without_peer` | function | `crates/gcode/src/commands/embeddings_doctor.rs:167` |
| `base_report` | function | `crates/gcode/src/commands/embeddings_doctor.rs:178` |
| `drift_fields` | function | `crates/gcode/src/commands/embeddings_doctor.rs:197` |
| `push_drift` | function | `crates/gcode/src/commands/embeddings_doctor.rs:225` |
| `fetch_daemon_peer` | function | `crates/gcode/src/commands/embeddings_doctor.rs:241` |
| `details` | function | `crates/gcode/src/commands/embeddings_doctor.rs:283` |

## [[code/files/crates/gcode/src/commands/graph/lifecycle.rs|crates/gcode/src/commands/graph/lifecycle.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `GraphSyncContractError` | class | `crates/gcode/src/commands/graph/lifecycle.rs:12` |
| `LifecycleBackend` | type | `crates/gcode/src/commands/graph/lifecycle.rs:78` |
| `CodeGraphLifecycleBackend` | class | `crates/gcode/src/commands/graph/lifecycle.rs:86` |
| `GraphFileSyncOutcome` | type | `crates/gcode/src/commands/graph/lifecycle.rs:131` |

## [[code/files/crates/gcode/src/commands/graph/reads.rs|crates/gcode/src/commands/graph/reads.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `empty_paged_response` | function | `crates/gcode/src/commands/graph/reads.rs:61` |
| `graph_read_or_empty` | function | `crates/gcode/src/commands/graph/reads.rs:86` |
| `GraphPathEndpoint` | class | `crates/gcode/src/commands/graph/reads.rs:155` |
| `GraphPathResponse` | class | `crates/gcode/src/commands/graph/reads.rs:162` |
| `GraphResolutionProjectCleanup` | class | `crates/gcode/src/commands/graph/reads.rs:663` |
| `uuid_input_resolves_exact_symbol_for_active_project` | function | `crates/gcode/src/commands/graph/reads.rs:767` |
| `unknown_uuid_input_does_not_fall_back_to_name_resolution` | function | `crates/gcode/src/commands/graph/reads.rs:801` |
| `ambiguous_name_behavior_remains_unchanged` | function | `crates/gcode/src/commands/graph/reads.rs:833` |

## [[code/files/crates/gcode/src/commands/grep.rs|crates/gcode/src/commands/grep.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `GrepOptions` | class | `crates/gcode/src/commands/grep.rs:21` |
| `IndexedContentChunk` | class | `crates/gcode/src/commands/grep.rs:36` |
| `LoadedIndexedChunks` | class | `crates/gcode/src/commands/grep.rs:43` |
| `GrepSpan` | class | `crates/gcode/src/commands/grep.rs:49` |
| `GrepContextLine` | class | `crates/gcode/src/commands/grep.rs:55` |
| `GrepMatch` | class | `crates/gcode/src/commands/grep.rs:61` |
| `GrepResponse` | class | `crates/gcode/src/commands/grep.rs:71` |
| `GrepResult` | class | `crates/gcode/src/commands/grep.rs:87` |
| `load_indexed_chunks` | function | `crates/gcode/src/commands/grep.rs:127` |
| `push_grep_sql_prefilters` | function | `crates/gcode/src/commands/grep.rs:236` |
| `push_grep_sql_prefix_filter` | function | `crates/gcode/src/commands/grep.rs:256` |
| `grep_chunks_with_filters` | function | `crates/gcode/src/commands/grep.rs:287` |
| `context_line_numbers` | function | `crates/gcode/src/commands/grep.rs:354` |
| `collect_context_lines` | function | `crates/gcode/src/commands/grep.rs:377` |
| `GrepFilters` | class | `crates/gcode/src/commands/grep.rs:409` |
| `sql_like_prefixes` | function | `crates/gcode/src/commands/grep.rs:441` |
| `escape_like_prefix` | function | `crates/gcode/src/commands/grep.rs:458` |
| `CompiledGlob` | class | `crates/gcode/src/commands/grep.rs:469` |
| `context_before` | function | `crates/gcode/src/commands/grep.rs:499` |
| `context_after` | function | `crates/gcode/src/commands/grep.rs:517` |
| `format_text_matches` | function | `crates/gcode/src/commands/grep.rs:535` |
| `push_grouped_grep_line` | function | `crates/gcode/src/commands/grep.rs:584` |
| `chunk` | function | `crates/gcode/src/commands/grep.rs:603` |
| `options` | function | `crates/gcode/src/commands/grep.rs:611` |

## [[code/files/crates/gcode/src/commands/grep/grep_matcher.rs|crates/gcode/src/commands/grep/grep_matcher.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `GrepMatcher` | class | `crates/gcode/src/commands/grep/grep_matcher.rs:6` |
| `matched_texts` | function | `crates/gcode/src/commands/grep/grep_matcher.rs:86` |

## [[code/files/crates/gcode/src/commands/index.rs|crates/gcode/src/commands/index.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `index_text` | function | `crates/gcode/src/commands/index.rs:62` |
| `pluralize` | function | `crates/gcode/src/commands/index.rs:96` |
| `IndexSyncProjectionsOutput` | class | `crates/gcode/src/commands/index.rs:107` |
| `sync_projections_payload` | function | `crates/gcode/src/commands/index.rs:119` |
| `sync_projections_text` | function | `crates/gcode/src/commands/index.rs:134` |
| `resolve_index_context` | function | `crates/gcode/src/commands/index.rs:140` |
| `clone_context` | function | `crates/gcode/src/commands/index.rs:197` |
| `path_filter_for` | function | `crates/gcode/src/commands/index.rs:218` |
| `sample_outcome` | function | `crates/gcode/src/commands/index.rs:264` |
| `sample_reports` | function | `crates/gcode/src/commands/index.rs:274` |

## [[code/files/crates/gcode/src/commands/scope.rs|crates/gcode/src/commands/scope.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `ProjectMatch` | class | `crates/gcode/src/commands/scope.rs:9` |
| `normalize_file_arg` | function | `crates/gcode/src/commands/scope.rs:14` |
| `current_indexed_path_is_valid` | function | `crates/gcode/src/commands/scope.rs:62` |
| `other_project_for_path` | function | `crates/gcode/src/commands/scope.rs:71` |

## [[code/files/crates/gcode/src/commands/search.rs|crates/gcode/src/commands/search.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `SearchOptions` | class | `crates/gcode/src/commands/search.rs:13` |
| `SymbolGraphSearchContext` | class | `crates/gcode/src/commands/search.rs:305` |
| `visible_search_degraded_hint` | function | `crates/gcode/src/commands/search.rs:672` |
| `is_dotted_literal_char` | function | `crates/gcode/src/commands/search.rs:725` |
| `format_symbol_lookup_text` | function | `crates/gcode/src/commands/search.rs:754` |
| `compact_snippet` | function | `crates/gcode/src/commands/search.rs:771` |

## [[code/files/crates/gcode/src/commands/setup.rs|crates/gcode/src/commands/setup.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `OverwriteProjectionConfigs` | class | `crates/gcode/src/commands/setup.rs:97` |
| `clear_overwrite_projections` | function | `crates/gcode/src/commands/setup.rs:102` |
| `overwrite_projection_configs` | function | `crates/gcode/src/commands/setup.rs:120` |
| `resolve_or_provision_database` | function | `crates/gcode/src/commands/setup.rs:168` |
| `apply_service_overrides` | function | `crates/gcode/src/commands/setup.rs:189` |
| `connect_postgres_with_retry` | function | `crates/gcode/src/commands/setup.rs:204` |
| `write_gcore_config` | function | `crates/gcode/src/commands/setup.rs:222` |
| `remove_embedding_keys` | function | `crates/gcode/src/commands/setup.rs:290` |
| `service_configured_compose_file` | function | `crates/gcode/src/commands/setup.rs:303` |
| `resolve_embedding_bootstrap` | function | `crates/gcode/src/commands/setup.rs:308` |
| `explicit_embedding_bootstrap` | function | `crates/gcode/src/commands/setup.rs:358` |
| `endpoint_reachable` | function | `crates/gcode/src/commands/setup.rs:379` |
| `standalone_command_installs_public_code_index_subset` | function | `crates/gcode/src/commands/setup.rs:573` |

## [[code/files/crates/gcode/src/commands/status.rs|crates/gcode/src/commands/status.rs]]

| Symbol | Kind | Location |
| --- | --- | --- |
| `format_timestamp` | function | `crates/gcode/src/commands/status.rs:18` |
| `overlay_status_json` | function | `crates/gcode/src/commands/status.rs:136` |
| `cleanup_project_projections` | function | `crates/gcode/src/commands/status.rs:187` |
| `collect_projects` | function | `crates/gcode/src/commands/status.rs:200` |
| `indexed_project_from_row` | function | `crates/gcode/src/commands/status.rs:229` |
| `format_coverage` | function | `crates/gcode/src/commands/status.rs:248` |
| `display_name` | function | `crates/gcode/src/commands/status.rs:259` |
| `is_stale` | function | `crates/gcode/src/commands/status.rs:296` |
| `StaleProject` | class | `crates/gcode/src/commands/status.rs:313` |
| `ProjectionCleanupScope` | type | `crates/gcode/src/commands/status.rs:319` |
| `ProjectionPruneTotals` | class | `crates/gcode/src/commands/status.rs:325` |
| `projection_cleanup_scope` | function | `crates/gcode/src/commands/status.rs:361` |
| `stale_projects` | function | `crates/gcode/src/commands/status.rs:369` |

