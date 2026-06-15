---
title: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json
type: code_file
provenance:
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json
  ranges:
  - 2-84
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json

Module: [[code/modules/docs/evidence/wiki-parity-2026-06|docs/evidence/wiki-parity-2026-06]]

## Purpose

This JSON records an evidence snapshot for a wiki-parity search run about reciprocal rank fusion in `gobby-cli`. It stores the search command, query, result limit, and an ordered `results` array where each hit includes fused scores, rank-source explanations from BM25 and semantic retrieval, provenance fields like `source_path`, `wiki_page`, `title`, and `sources`, plus `code_citations` that link the evidence back to the corresponding `rrf.rs` documentation files.
[docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:2-11]
[docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:5]
[docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:8]
[docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:9]

## API Symbols

- `code_citations` (property) component `code_citations [property]` (`02dbe7c8-8e30-59e0-b245-35326175b9b6`) lines 2-11 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:2-11]
  - Signature: `"code_citations": [`
  - Purpose: Indexed property `code_citations` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:2-11]
- `file` (property) component `file [property]` (`6c507ccc-cf82-578c-835f-43f1f4359cb4`) lines 4-4 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:4]
  - Signature: `"file": "code/files/crates/gcode/src/search/rrf.rs.md",`
  - Purpose: Indexed property `file` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:4]
- `symbol` (property) component `symbol [property]` (`f6086d77-a689-5442-a741-f31e9550f09e`) lines 5-5 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:5]
  - Signature: `"symbol": "crates/gcode/src/search/rrf.rs"`
  - Purpose: Indexed property `symbol` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:5]
- `file` (property) component `file [property]` (`1f02896c-472c-5191-a934-c0a6bc7ee951`) lines 8-8 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:8]
  - Signature: `"file": "code/files/crates/gwiki/src/search/rrf.rs.md",`
  - Purpose: Indexed property `file` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:8]
- `symbol` (property) component `symbol [property]` (`14e0ce57-6917-5449-a843-793fe44ab57a`) lines 9-9 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:9]
  - Signature: `"symbol": "crates/gwiki/src/search/rrf.rs"`
  - Purpose: Indexed property `symbol` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:9]
- `command` (property) component `command [property]` (`79d44998-dc51-54fb-b419-e3a5fc38a019`) lines 12-12 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:12]
  - Signature: `"command": "search",`
  - Purpose: Indexed property `command` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:12]
- `degradations` (property) component `degradations [property]` (`07109d58-49fe-5ffe-a152-5ed2b089b5e8`) lines 13-13 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:13]
  - Signature: `"degradations": [],`
  - Purpose: Indexed property `degradations` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:13]
- `limit` (property) component `limit [property]` (`4aa4d299-c04e-51fd-95c4-81fab49e3d99`) lines 14-14 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:14]
  - Signature: `"limit": 3,`
  - Purpose: Indexed property `limit` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:14]
- `query` (property) component `query [property]` (`8ecd2f8c-ce50-5f5d-98a5-f7232cd17331`) lines 15-15 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:15]
  - Signature: `"query": "How does gobby-cli merge hybrid search results with reciprocal rank fusion?",`
  - Purpose: Indexed property `query` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:15]
- `results` (property) component `results [property]` (`d20ae862-62d0-5ed8-a78f-683745f00639`) lines 16-80 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:16-80]
  - Signature: `"results": [`
  - Purpose: Indexed property `results` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:16-80]
- `explanations` (property) component `explanations [property]` (`17fdf8e5-551b-5a7a-8c5e-93c6dc7223f5`) lines 18-29 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:18-29]
  - Signature: `"explanations": [`
  - Purpose: Indexed property `explanations` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:18-29]
- `rank` (property) component `rank [property]` (`cced73bd-7ed5-53d8-a021-30c773d7c303`) lines 20-20 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:20]
  - Signature: `"rank": 2,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:20]
- `score` (property) component `score [property]` (`3243d93f-caf4-5e63-89c0-0e66dd627e91`) lines 21-21 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:21]
  - Signature: `"score": 0.016129032258064516,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:21]
- `source` (property) component `source [property]` (`34f95257-0706-5732-9e45-9779bf7d81ca`) lines 22-22 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:22]
  - Signature: `"source": "bm25"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:22]
- `rank` (property) component `rank [property]` (`32a03b7e-7e96-56ee-bda0-f4301e697154`) lines 25-25 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:25]
  - Signature: `"rank": 0,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:25]
- `score` (property) component `score [property]` (`03ef3e82-02ec-5c6b-9b9d-dfb183f97624`) lines 26-26 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:26]
  - Signature: `"score": 0.016666666666666666,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:26]
- `source` (property) component `source [property]` (`e7f9df16-d206-5ed5-8ae7-06c639dc1d0b`) lines 27-27 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:27]
  - Signature: `"source": "semantic"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:27]
- `fusion_key` (property) component `fusion_key [property]` (`afdda403-9fbe-5f08-8d3b-958791120eeb`) lines 30-30 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:30]
  - Signature: `"fusion_key": "project:3bf57fe7-2a0c-4074-8912-a83d9cd4df01:code/files/crates/gcode/src/search/rrf.rs.md",`
  - Purpose: Indexed property `fusion_key` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:30]
- `result_type` (property) component `result_type [property]` (`96e57949-10f9-5446-a7e1-4ea6579b267b`) lines 31-31 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:31]
  - Signature: `"result_type": "code",`
  - Purpose: Indexed property `result_type` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:31]
- `score` (property) component `score [property]` (`b419a7db-67d4-514f-8603-a26e2e373c22`) lines 32-32 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:32]
  - Signature: `"score": 0.03279569892473118,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:32]
- `snippet` (property) component `snippet [property]` (`f1dac136-5df8-57cd-93da-8e8d30eec47c`) lines 33-33 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:33]
  - Signature: ``"snippet": "## Purpose This file provides a small Reciprocal Rank Fusion wrapper for search results. It defines `MergedResult` as the merged output shape `(symbol_id, com",``
  - Purpose: Indexed property `snippet` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:33]
- `source_path` (property) component `source_path [property]` (`20a8d0ab-9123-56f0-88bc-8be360839f90`) lines 34-34 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:34]
  - Signature: `"source_path": "code/files/crates/gcode/src/search/rrf.rs.md",`
  - Purpose: Indexed property `source_path` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:34]
- `sources` (property) component `sources [property]` (`e0d47d8f-e7e0-546d-8247-4f9f1269f86b`) lines 35-38 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:35-38]
  - Signature: `"sources": [`
  - Purpose: Indexed property `sources` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:35-38]
- `title` (property) component `title [property]` (`8b9bc344-45e1-5454-ae50-c67edc7fbd31`) lines 39-39 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:39]
  - Signature: `"title": "crates/gcode/src/search/rrf.rs",`
  - Purpose: Indexed property `title` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:39]
- `wiki_page` (property) component `wiki_page [property]` (`ac99adc0-6fe3-56d7-bdd6-968c98ef6f76`) lines 40-40 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:40]
  - Signature: `"wiki_page": "code/files/crates/gcode/src/search/rrf.rs.md"`
  - Purpose: Indexed property `wiki_page` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:40]
- `explanations` (property) component `explanations [property]` (`4f0cfce9-ff51-57de-84fd-e1346a506669`) lines 43-49 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:43-49]
  - Signature: `"explanations": [`
  - Purpose: Indexed property `explanations` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:43-49]
- `rank` (property) component `rank [property]` (`b6140668-d2b8-5d5b-b851-5dcb08771936`) lines 45-45 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:45]
  - Signature: `"rank": 0,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:45]
- `score` (property) component `score [property]` (`701cd339-ee00-57bc-98c1-f97476699074`) lines 46-46 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:46]
  - Signature: `"score": 0.016666666666666666,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:46]
- `source` (property) component `source [property]` (`9ec52a87-a98f-5d57-b790-d6051f821500`) lines 47-47 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:47]
  - Signature: `"source": "bm25"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:47]
- `fusion_key` (property) component `fusion_key [property]` (`33984c63-f37f-5a9a-a0af-098f963507f6`) lines 50-50 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:50]
  - Signature: `"fusion_key": "project:3bf57fe7-2a0c-4074-8912-a83d9cd4df01:code/modules/docs/evidence.md",`
  - Purpose: Indexed property `fusion_key` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:50]
- `result_type` (property) component `result_type [property]` (`3ca3abf1-6f60-5107-bb68-280f682bdaec`) lines 51-51 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:51]
  - Signature: `"result_type": "wiki",`
  - Purpose: Indexed property `result_type` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:51]
- `score` (property) component `score [property]` (`b679b374-d6c1-5357-b7be-a620e9c41b45`) lines 52-52 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:52]
  - Signature: `"score": 0.016666666666666666,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:52]
- `snippet` (property) component `snippet [property]` (`385a43ff-ec6c-52cf-9199-8d1f89c041a8`) lines 53-53 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:53]
  - Signature: `"snippet": "ores proof artifacts for a gwiki parity workflow that first searches a resolved project scope and then uses selected sources to compile a grounded explainer. The key flow is searc",`
  - Purpose: Indexed property `snippet` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:53]
- `source_path` (property) component `source_path [property]` (`c47e6a12-125f-5906-afe7-1aab71293bce`) lines 54-54 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:54]
  - Signature: `"source_path": "code/modules/docs/evidence.md",`
  - Purpose: Indexed property `source_path` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:54]
- `sources` (property) component `sources [property]` (`7a07db7b-4e0d-5c96-a397-cb77d7ce925a`) lines 55-57 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:55-57]
  - Signature: `"sources": [`
  - Purpose: Indexed property `sources` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:55-57]
- `title` (property) component `title [property]` (`5483826a-1dda-597a-a5ce-5f322c2c8994`) lines 58-58 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:58]
  - Signature: `"title": "docs/evidence",`
  - Purpose: Indexed property `title` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:58]
- `wiki_page` (property) component `wiki_page [property]` (`61bd1bdd-72db-5b3e-af9d-1ada184789ae`) lines 59-59 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:59]
  - Signature: `"wiki_page": "code/modules/docs/evidence.md"`
  - Purpose: Indexed property `wiki_page` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:59]
- `explanations` (property) component `explanations [property]` (`3483bff0-a735-5daf-a810-49c36305066c`) lines 62-68 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:62-68]
  - Signature: `"explanations": [`
  - Purpose: Indexed property `explanations` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:62-68]
- `rank` (property) component `rank [property]` (`ed5c1683-cee5-5fb4-baf7-2a6a372d8bb4`) lines 64-64 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:64]
  - Signature: `"rank": 1,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:64]
- `score` (property) component `score [property]` (`d6141bc0-1771-5fa9-b460-07c7687a4966`) lines 65-65 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:65]
  - Signature: `"score": 0.01639344262295082,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:65]
- `source` (property) component `source [property]` (`2864ae6f-327b-558e-8d41-b86856081d21`) lines 66-66 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:66]
  - Signature: `"source": "semantic"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:66]
- `fusion_key` (property) component `fusion_key [property]` (`3e5919a5-86f0-5ded-b683-fd71346583ab`) lines 69-69 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:69]
  - Signature: `"fusion_key": "project:3bf57fe7-2a0c-4074-8912-a83d9cd4df01:code/files/crates/gwiki/src/search/rrf.rs.md",`
  - Purpose: Indexed property `fusion_key` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:69]
- `result_type` (property) component `result_type [property]` (`e419451c-ca23-58d8-8b29-f8580f66a3b2`) lines 70-70 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:70]
  - Signature: `"result_type": "code",`
  - Purpose: Indexed property `result_type` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:70]
- `score` (property) component `score [property]` (`aaee00f8-4a78-56a8-b912-85401174a2f7`) lines 71-71 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:71]
  - Signature: `"score": 0.01639344262295082,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:71]
- `snippet` (property) component `snippet [property]` (`36de2eef-7060-5875-bd96-51922caf1d54`) lines 72-72 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:72]
  - Signature: `"snippet": "## Purpose",`
  - Purpose: Indexed property `snippet` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:72]
- `source_path` (property) component `source_path [property]` (`ccfe9cde-e609-5b42-8f3a-89f38af26615`) lines 73-73 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:73]
  - Signature: `"source_path": "code/files/crates/gwiki/src/search/rrf.rs.md",`
  - Purpose: Indexed property `source_path` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:73]
- `sources` (property) component `sources [property]` (`9368df7f-0fea-5872-b812-dcf73a57a325`) lines 74-76 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:74-76]
  - Signature: `"sources": [`
  - Purpose: Indexed property `sources` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:74-76]
- `title` (property) component `title [property]` (`42ef37dd-947d-5f38-b1ff-c10a745e5852`) lines 77-77 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:77]
  - Signature: `"title": "crates/gwiki/src/search/rrf.rs",`
  - Purpose: Indexed property `title` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:77]
- `wiki_page` (property) component `wiki_page [property]` (`17564b4c-3cab-5de5-9426-a77c9f25fbac`) lines 78-78 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:78]
  - Signature: `"wiki_page": "code/files/crates/gwiki/src/search/rrf.rs.md"`
  - Purpose: Indexed property `wiki_page` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:78]
- `scope` (property) component `scope [property]` (`946e50ad-94f1-521b-be0e-925adba8bd97`) lines 81-84 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:81-84]
  - Signature: `"scope": {`
  - Purpose: Indexed property `scope` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:81-84]
- `id` (property) component `id [property]` (`ae8980f6-4eae-5d75-b608-c5fa43c6ef40`) lines 82-82 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:82]
  - Signature: `"id": "3bf57fe7-2a0c-4074-8912-a83d9cd4df01",`
  - Purpose: Indexed property `id` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:82]
- `kind` (property) component `kind [property]` (`55c37974-6323-5d9b-a863-645a3f87e4ad`) lines 83-83 [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:83]
  - Signature: `"kind": "project"`
  - Purpose: Indexed property `kind` in `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:83]

