---
title: crates/gcode/src/commands/codewiki/repair.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/repair.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/repair.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The file crates/gcode/src/commands/codewiki/repair.rs provides a deterministic, no-LLM citation repair routine that re-anchors `[file:line]` citations within a generated vault back to the codebase's current index. When source files drift over time, updating these citations is a cheaper alternative to fully regenerating pages. The system accomplishes this by mapping the stale citations of a documented page directly to their corresponding symbols' updated locations in the codebase.

The module contains two primary structures to manage this process. The IndexCitationResolver at crates/gcode/src/commands/codewiki/repair.rs:40-51 serves as the bridge between old snapshot anchors and current symbol spans. To summarize the outcomes of a repair operation, the CitationRepairSummary at crates/gcode/src/commands/codewiki/repair.rs:21-31 tracks metrics such as the number of pages scanned, pages and individual citations repaired in place, and any stale citations left unresolved due to missing symbols.

## How it fits
[crates/gcode/src/commands/codewiki/repair.rs:21-31]
[crates/gcode/src/commands/codewiki/repair.rs:40-51]
[crates/gcode/src/commands/codewiki/repair.rs:56-97]
[crates/gcode/src/commands/codewiki/repair.rs:101-107]
[crates/gcode/src/commands/codewiki/repair.rs:109-114]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CitationRepairSummary` | class | 'CitationRepairSummary' is a metrics struct that records how many pages were scanned, how many pages and individual citations were repaired in place, and how many stale citations remained unresolved because their symbols no longer resolved in the current index. [crates/gcode/src/commands/codewiki/repair.rs:21-31] |
| `IndexCitationResolver` | class | 'IndexCitationResolver' stores current symbol spans and identity-to-range mappings plus persisted snapshot anchors to resolve index citations against the current codebase while refusing to re-anchor ambiguous snapshot line starts. [crates/gcode/src/commands/codewiki/repair.rs:40-51] |
| `IndexCitationResolver::build` | method | Builds three lookup maps from the current symbols and snapshot: per-file span lists, a '(file_path, qualified_name, kind)' to span map, and a snapshot anchor map keyed by '(file_path, line_start)' with ambiguous anchors removed. [crates/gcode/src/commands/codewiki/repair.rs:56-97] |
| `IndexCitationResolver::is_current` | method | Returns 'true' if 'current_spans' contains the given 'file' and at least one stored span fully covers the range '[line_start, line_end]', otherwise 'false'. [crates/gcode/src/commands/codewiki/repair.rs:101-107] |
| `IndexCitationResolver::resolve` | method | Looks up a snapshot anchor by '(file, line_start)' to obtain its '(qualified_name, kind)', then uses that identity tuple to return the current mapped '(usize, usize)' location from 'current_by_identity', or 'None' if either lookup fails. [crates/gcode/src/commands/codewiki/repair.rs:109-114] |
| `repair_with_resolver` | function | 'repair_with_resolver' loads the codewiki metadata for 'out_dir', scans each documented page that still exists on disk, reanchors citations using the provided 'CitationResolver', rewrites any page whose content changed, and returns a 'CitationRepairSummary' aggregating scanned, repaired, and unresolved citation counts. [crates/gcode/src/commands/codewiki/repair.rs:120-145] |
| `repair_citations` | function | Builds an 'IndexCitationResolver' from the provided 'symbols' and the codewiki metadata index snapshot in 'out_dir' (defaulting to an empty snapshot if absent), then delegates to 'repair_with_resolver' to repair citations and return a 'CitationRepairSummary'. [crates/gcode/src/commands/codewiki/repair.rs:153-162] |

