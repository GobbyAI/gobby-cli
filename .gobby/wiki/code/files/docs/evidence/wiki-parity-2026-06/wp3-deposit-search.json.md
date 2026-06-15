---
title: docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json
type: code_file
provenance:
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json
  ranges:
  - 2-90
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json

Module: [[code/modules/docs/evidence/wiki-parity-2026-06|docs/evidence/wiki-parity-2026-06]]

## Purpose

This JSON file records evidence for a wiki-parity search run in `wp3-deposit-search`: it stores the search command, query, limit, and any degradations, then captures the top ranked results with their BM25/semantic explanations, scores, snippets, source paths, titles, and wiki page references. The `code_citations` link the output back to the referenced source files, and the `results` entries group the per-hit metadata needed to audit how the search output was assembled.
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:2-11]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:5]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:8]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:9]

## API Symbols

- `code_citations` (property) component `code_citations [property]` (`fbd922db-420c-5add-824a-8b8c6bf169d1`) lines 2-11 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:2-11]
  - Signature: `"code_citations": [`
  - Purpose: Indexed property `code_citations` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:2-11]
- `file` (property) component `file [property]` (`bf3ed0f9-4a33-5905-a413-4bc3aff0d9e2`) lines 4-4 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:4]
  - Signature: `"file": "code/files/crates/gsqz/src/compressor.rs.md",`
  - Purpose: Indexed property `file` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:4]
- `symbol` (property) component `symbol [property]` (`82b5c00a-f433-5f80-a981-8ace40d60ef6`) lines 5-5 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:5]
  - Signature: `"symbol": "crates/gsqz/src/compressor.rs"`
  - Purpose: Indexed property `symbol` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:5]
- `file` (property) component `file [property]` (`742fc406-4d7a-5ecb-8f78-13f2cb296c80`) lines 8-8 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:8]
  - Signature: `"file": "code/files/crates/gsqz/src/main.rs.md",`
  - Purpose: Indexed property `file` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:8]
- `symbol` (property) component `symbol [property]` (`a66985f6-f530-5e24-b51a-bb3d0ed07391`) lines 9-9 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:9]
  - Signature: `"symbol": "crates/gsqz/src/main.rs"`
  - Purpose: Indexed property `symbol` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:9]
- `command` (property) component `command [property]` (`4dabe075-a307-54bf-bc35-be8862fed6fe`) lines 12-12 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:12]
  - Signature: `"command": "search",`
  - Purpose: Indexed property `command` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:12]
- `degradations` (property) component `degradations [property]` (`080965ae-ed1d-584b-9f1d-ddc327bf7e2c`) lines 13-13 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:13]
  - Signature: `"degradations": [],`
  - Purpose: Indexed property `degradations` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:13]
- `limit` (property) component `limit [property]` (`84a6d42e-f1f6-56cf-bf2a-e3888b81db20`) lines 14-14 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:14]
  - Signature: `"limit": 3,`
  - Purpose: Indexed property `limit` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:14]
- `query` (property) component `query [property]` (`8526566e-d028-5510-9ecc-e5ecec1190bb`) lines 15-15 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:15]
  - Signature: `"query": "gsqz always exit code 0 compressed output contract",`
  - Purpose: Indexed property `query` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:15]
- `results` (property) component `results [property]` (`27abe5f8-b3ed-5561-950e-e70ec219e749`) lines 16-86 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:16-86]
  - Signature: `"results": [`
  - Purpose: Indexed property `results` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:16-86]
- `explanations` (property) component `explanations [property]` (`d8f2911c-9161-52d9-aef7-e4b61f16a06f`) lines 18-29 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:18-29]
  - Signature: `"explanations": [`
  - Purpose: Indexed property `explanations` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:18-29]
- `rank` (property) component `rank [property]` (`7860bc12-ff41-5dfc-89ae-5d1d29594b08`) lines 20-20 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:20]
  - Signature: `"rank": 0,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:20]
- `score` (property) component `score [property]` (`8cabaa0d-9522-5af1-8802-611c8b619e67`) lines 21-21 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:21]
  - Signature: `"score": 0.016666666666666666,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:21]
- `source` (property) component `source [property]` (`afca837c-7111-59b1-8d76-3deee8d70064`) lines 22-22 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:22]
  - Signature: `"source": "bm25"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:22]
- `rank` (property) component `rank [property]` (`0141d307-868c-5980-8921-c340c1978aa2`) lines 25-25 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:25]
  - Signature: `"rank": 1,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:25]
- `score` (property) component `score [property]` (`be38d265-fa1f-5e53-af6f-6c4b0227b385`) lines 26-26 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:26]
  - Signature: `"score": 0.01639344262295082,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:26]
- `source` (property) component `source [property]` (`b499868b-f0c5-5a36-9b79-a082ee8704f0`) lines 27-27 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:27]
  - Signature: `"source": "semantic"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:27]
- `fusion_key` (property) component `fusion_key [property]` (`f513e500-9733-59cc-ae9a-3367b1a8e8a1`) lines 30-30 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:30]
  - Signature: `"fusion_key": "project:3bf57fe7-2a0c-4074-8912-a83d9cd4df01:code/files/crates/gsqz/src/compressor.rs.md",`
  - Purpose: Indexed property `fusion_key` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:30]
- `result_type` (property) component `result_type [property]` (`f66b5ae2-27ed-5868-8e4b-2b8912fb0b86`) lines 31-31 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:31]
  - Signature: `"result_type": "code",`
  - Purpose: Indexed property `result_type` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:31]
- `score` (property) component `score [property]` (`f2523e49-9ad7-5bf3-b3bf-917a1a52ce72`) lines 32-32 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:32]
  - Signature: `"score": 0.03306010928961749,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:32]
- `snippet` (property) component `snippet [property]` (`49841e40-2ec5-50f8-8e9d-efd476defbff`) lines 33-33 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:33]
  - Signature: ``"snippet": "## Purpose This file implements the `gsqz` compression engine for command output. It defines `CompressionResult` for reporting the compressed text, size stat",``
  - Purpose: Indexed property `snippet` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:33]
- `source_path` (property) component `source_path [property]` (`db9adbbb-8fec-511c-9d38-db1d7f914492`) lines 34-34 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:34]
  - Signature: `"source_path": "code/files/crates/gsqz/src/compressor.rs.md",`
  - Purpose: Indexed property `source_path` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:34]
- `sources` (property) component `sources [property]` (`04739275-a9a8-5ead-a5d5-eee2a143adad`) lines 35-38 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:35-38]
  - Signature: `"sources": [`
  - Purpose: Indexed property `sources` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:35-38]
- `title` (property) component `title [property]` (`b3f5a71e-e752-5069-b330-c082602256d5`) lines 39-39 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:39]
  - Signature: `"title": "crates/gsqz/src/compressor.rs",`
  - Purpose: Indexed property `title` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:39]
- `wiki_page` (property) component `wiki_page [property]` (`a4797e22-7c98-5a08-b004-216b3ae4b4dc`) lines 40-40 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:40]
  - Signature: `"wiki_page": "code/files/crates/gsqz/src/compressor.rs.md"`
  - Purpose: Indexed property `wiki_page` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:40]
- `explanations` (property) component `explanations [property]` (`7910f46b-72cf-5a84-a28a-98118a293940`) lines 43-54 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:43-54]
  - Signature: `"explanations": [`
  - Purpose: Indexed property `explanations` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:43-54]
- `rank` (property) component `rank [property]` (`de051630-dda3-5d88-9753-9c6a4915cfc9`) lines 45-45 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:45]
  - Signature: `"rank": 1,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:45]
- `score` (property) component `score [property]` (`c8f0c9e3-e651-5c74-98eb-0e727c03a4f1`) lines 46-46 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:46]
  - Signature: `"score": 0.01639344262295082,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:46]
- `source` (property) component `source [property]` (`b8ee1344-7fba-5d8b-b9e2-2fc444b5d4c7`) lines 47-47 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:47]
  - Signature: `"source": "bm25"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:47]
- `rank` (property) component `rank [property]` (`7c126f23-bfa4-5bd5-b947-a6fbbeab30f2`) lines 50-50 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:50]
  - Signature: `"rank": 0,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:50]
- `score` (property) component `score [property]` (`00e39f12-32f1-5584-bf8f-754c1b7a09fc`) lines 51-51 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:51]
  - Signature: `"score": 0.016666666666666666,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:51]
- `source` (property) component `source [property]` (`5897ada8-a32d-54b8-acc9-848d474f871a`) lines 52-52 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:52]
  - Signature: `"source": "semantic"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:52]
- `fusion_key` (property) component `fusion_key [property]` (`008a2b08-699b-5460-b357-8f7f58c3f386`) lines 55-55 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:55]
  - Signature: `"fusion_key": "project:3bf57fe7-2a0c-4074-8912-a83d9cd4df01:code/files/crates/gsqz/src/main.rs.md",`
  - Purpose: Indexed property `fusion_key` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:55]
- `result_type` (property) component `result_type [property]` (`ecc30739-ae64-5384-a225-229fbf8c11a9`) lines 56-56 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:56]
  - Signature: `"result_type": "code",`
  - Purpose: Indexed property `result_type` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:56]
- `score` (property) component `score [property]` (`a25c5b97-7dd0-5bc0-805a-bdeb35ea5626`) lines 57-57 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:57]
  - Signature: `"score": 0.03306010928961749,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:57]
- `snippet` (property) component `snippet [property]` (`941612e9-144e-5e78-9fe0-2fdf657255a2`) lines 58-58 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:58]
  - Signature: `"snippet": "--- title: crates/gsqz/src/main.rs type: code_file provenance: - file: crates/gsqz/src/main.rs ranges: - 25-48 - 50-65 - 67-139",`
  - Purpose: Indexed property `snippet` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:58]
- `source_path` (property) component `source_path [property]` (`6bee8ff2-b78b-5494-9fe6-baabe1fa18b8`) lines 59-59 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:59]
  - Signature: `"source_path": "code/files/crates/gsqz/src/main.rs.md",`
  - Purpose: Indexed property `source_path` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:59]
- `sources` (property) component `sources [property]` (`c94f99b5-4bd8-578e-874b-0168fe424d6a`) lines 60-63 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:60-63]
  - Signature: `"sources": [`
  - Purpose: Indexed property `sources` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:60-63]
- `title` (property) component `title [property]` (`2595b863-ed54-5a7a-8269-21235cbb6a78`) lines 64-64 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:64]
  - Signature: `"title": "crates/gsqz/src/main.rs",`
  - Purpose: Indexed property `title` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:64]
- `wiki_page` (property) component `wiki_page [property]` (`2b10e399-af09-5e7f-9042-f39ee2509638`) lines 65-65 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:65]
  - Signature: `"wiki_page": "code/files/crates/gsqz/src/main.rs.md"`
  - Purpose: Indexed property `wiki_page` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:65]
- `explanations` (property) component `explanations [property]` (`642c139e-9056-5527-a348-46b4a92f8c57`) lines 68-74 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:68-74]
  - Signature: `"explanations": [`
  - Purpose: Indexed property `explanations` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:68-74]
- `rank` (property) component `rank [property]` (`5bfc9866-393f-5fd9-aa6d-a3718a8f406c`) lines 70-70 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:70]
  - Signature: `"rank": 2,`
  - Purpose: Indexed property `rank` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:70]
- `score` (property) component `score [property]` (`d4cbccdb-c523-5b4e-8c9c-1d51c6e56b35`) lines 71-71 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:71]
  - Signature: `"score": 0.016129032258064516,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:71]
- `source` (property) component `source [property]` (`3bf4750a-9553-5021-9d21-72fedb2dd46a`) lines 72-72 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:72]
  - Signature: `"source": "bm25"`
  - Purpose: Indexed property `source` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:72]
- `fusion_key` (property) component `fusion_key [property]` (`7b85c2f3-aa91-56cc-9613-6715b9c850ef`) lines 75-75 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:75]
  - Signature: `"fusion_key": "project:3bf57fe7-2a0c-4074-8912-a83d9cd4df01:code/modules/crates.md",`
  - Purpose: Indexed property `fusion_key` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:75]
- `result_type` (property) component `result_type [property]` (`65eba6de-9f5d-58ca-b872-04ab634a8311`) lines 76-76 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:76]
  - Signature: `"result_type": "wiki",`
  - Purpose: Indexed property `result_type` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:76]
- `score` (property) component `score [property]` (`73c35db5-99a8-5cd5-b5e0-e2c42a2022e7`) lines 77-77 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:77]
  - Signature: `"score": 0.016129032258064516,`
  - Purpose: Indexed property `score` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:77]
- `snippet` (property) component `snippet [property]` (`39bbe2f1-39ec-5be6-8253-238815f996bd`) lines 78-78 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:78]
  - Signature: `"snippet": "## Child Modules - [[code/modules/crates/gcode|crates/gcode]] - The crates/gcode module packages the Rust gcode tool as both a CLI and a reus",`
  - Purpose: Indexed property `snippet` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:78]
- `source_path` (property) component `source_path [property]` (`cd0f80a3-97e2-5171-9ea8-b00e9da5feb1`) lines 79-79 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:79]
  - Signature: `"source_path": "code/modules/crates.md",`
  - Purpose: Indexed property `source_path` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:79]
- `sources` (property) component `sources [property]` (`9eb1106d-bd2c-5e2b-922f-da6a26706b7b`) lines 80-82 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:80-82]
  - Signature: `"sources": [`
  - Purpose: Indexed property `sources` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:80-82]
- `title` (property) component `title [property]` (`088a6329-eda2-52d6-b863-23dbc7efd19f`) lines 83-83 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:83]
  - Signature: `"title": "crates",`
  - Purpose: Indexed property `title` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:83]
- `wiki_page` (property) component `wiki_page [property]` (`b89cfa99-2da6-5a5f-99b3-f5dda5ac5243`) lines 84-84 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:84]
  - Signature: `"wiki_page": "code/modules/crates.md"`
  - Purpose: Indexed property `wiki_page` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:84]
- `scope` (property) component `scope [property]` (`c51d596a-e55d-5800-ad85-cadf3c994d91`) lines 87-90 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:87-90]
  - Signature: `"scope": {`
  - Purpose: Indexed property `scope` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:87-90]
- `id` (property) component `id [property]` (`7711c47b-4bf3-55b2-b031-71708e35b9b3`) lines 88-88 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:88]
  - Signature: `"id": "3bf57fe7-2a0c-4074-8912-a83d9cd4df01",`
  - Purpose: Indexed property `id` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:88]
- `kind` (property) component `kind [property]` (`3bb092be-7827-5d3c-9ca4-6f53e1cb4359`) lines 89-89 [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:89]
  - Signature: `"kind": "project"`
  - Purpose: Indexed property `kind` in `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json`. [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:89]

