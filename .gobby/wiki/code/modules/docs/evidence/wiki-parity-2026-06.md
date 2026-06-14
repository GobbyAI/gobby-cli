---
title: docs/evidence/wiki-parity-2026-06
type: code_module
provenance:
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json
  ranges:
  - 3-47
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json
  ranges:
  - 3-47
- file: docs/evidence/wiki-parity-2026-06/wp3-search-sources.json
  ranges:
  - 3-227
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs/evidence/wiki-parity-2026-06

Parent: [[code/modules/docs/evidence|docs/evidence]]

## Overview

This evidence module captures wiki-parity proof artifacts for a `gwiki` workflow: first searching a resolved project scope, then compiling a grounded explainer from the selected sources. The search artifact records the query, limit, command, degradations, code citation targets, and ranked hybrid results for “reciprocal rank fusion hybrid search,” including per-result BM25 and semantic explanations, fusion keys, snippets, source paths, titles, and wiki pages (docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:1-49).

The compile artifacts document two runs that generated the “gsqz compression shipping decision” explainer. Both runs show daemon-routed AI synthesis using the `haiku` model with successful generated status, no errors, no fallback sections, and no stripped citations, then tie the compile command to the article path, wiki index path, handoff id, outline, and created page writes for the topic article and supporting source page (docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:1-30) (docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:1-30).

Together, the files preserve the collaboration between `gwiki search` evidence and `gwiki compile` output: search results make source discovery traceable back to code documentation pages, while compile records the exact explainer prompt, daemon synthesis availability, estimated token budget, source truncation count, and requested sections used to produce the final wiki page (docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16) (docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:31-49) (docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:31-49).
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:5]

## Files

- [[code/files/docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json|docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json]] - Records the result of a `gwiki compile` run for the “gsqz compression shipping decision” explainer. It ties together the resolved project scope, AI synthesis metadata, target article and index paths, the requested outline, created wiki pages, and the prompt and source-scope details used to generate the article.
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:5]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:6]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:7]
- [[code/files/docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json|docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json]] - Records the result of a `gwiki compile` run for the wiki-parity task, tying a resolved project scope to the generated article and its supporting index/source writes. The `ai` block captures the daemon-synthesized compilation metadata, while `command`, `handoff_id`, `outline`, `page_writes`, `article_path`, and `index_path` show what was compiled and where the output landed. The nested `prompt` and `scope` fields document the requested explainer format, token estimate, source coverage, and source path set used to generate the final wiki page.
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:4]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:5]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:6]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:7]
- [[code/files/docs/evidence/wiki-parity-2026-06/wp3-search-sources.json|docs/evidence/wiki-parity-2026-06/wp3-search-sources.json]] - This JSON captures evidence for a `gwiki` search run over the project scope, recording the query, limit, command, and any degradations alongside the ranked results. Each result bundles fusion metadata and per-source explanations, plus wiki/page identity fields and citations to the related code documentation files so the search output can be traced back to its sources.
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:5]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:6]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:9]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:10]

## Components

- `df826027-066c-58cc-bdbf-f938bfec12ce`
- `3e4c955a-d9e7-540c-bfdf-b3c17044ad11`
- `f46d2c75-a8de-563a-af83-d37abbe6d19a`
- `fbb30788-f2d5-55ea-bd56-8b0fd23e62ac`
- `319d5134-b71a-5b15-ab54-68f021bf29e3`
- `455ca5bb-77d5-59cd-974a-4172661af13c`
- `374b3ec5-5dbe-5ff0-80f8-1d040a53fd93`
- `589a6585-32c4-54d5-9dc1-3c1326eab5c4`
- `3f38d5cd-b1f8-509e-a6af-4122722ef3bb`
- `ca5d2a82-c888-5822-8e12-cb237b1a5f00`
- `2bf11f8f-4f7a-5700-a1b8-eb6a814d1df7`
- `a928fd51-727d-545e-b6d6-c05565f76a6d`
- `c58cfb62-3f54-56af-8f57-dba6cddcc44a`
- `a991d8ef-dae7-5dee-bc1b-a5607da266dd`
- `0bf03c55-94fa-59e5-96f0-d53e8478d827`
- `d8125856-3fa8-58c5-ba69-ecbb2da09c7c`
- `8a5441bf-c17f-5b18-b86f-9f951a1cb23a`
- `f61fde12-8f97-5019-b69b-98dd30839504`
- `f4f5ef2d-6901-5e4b-8f29-51797dd656e1`
- `03c6a720-2929-512e-aa80-7332164e653f`
- `8809f281-865d-5443-9f58-55e344e07bfc`
- `d40389f9-535a-5c2d-bb72-894454256c61`
- `c7ed06bc-84ee-5d43-afaf-f5c2cc2afde0`
- `83bf7243-d27d-51ef-a983-c29d3d05b0b2`
- `59c5ba1f-f137-56e1-9310-0a4da4eab416`
- `2def85b8-7d87-5f80-84b0-d48e1c5f2529`
- `ae31dd41-b752-51eb-a5ad-127b2c7ae01c`
- `926da5cd-f078-5ac3-84c4-a08cfd6a59dc`
- `1f146a9d-6724-588b-973b-8c0878ceb0d7`
- `25cf65b9-f4f4-5ea7-9880-a77cd4c2790e`
- `8c0efc1d-3b93-5bd8-88b0-5ce30dccb40e`
- `898672fb-8d4a-551e-b922-d52d3484b4d0`
- `39461b11-e8ef-5781-b6cf-cf5d8926739d`
- `e0eb2ba5-aea5-591a-9412-8390d4f264f5`
- `1cddca69-c198-5a13-8f62-9d15dfb454c9`
- `d7d0b8ba-1749-5e3f-bb7a-d48a817dfda0`
- `e37f0651-8cd9-571d-a2c8-0a8b897a87b0`
- `d87b3229-4d10-54a9-9d56-a50f0b84506e`
- `7daed047-73de-5a94-8781-498e91004172`
- `6313a0f7-198b-5efa-b2e2-b2e1046c386c`
- `43041662-59a9-5c67-814d-02ec81b2957b`
- `7f88a36d-fee9-5180-8980-633e032b9d6d`
- `7601c43d-fd24-521a-94a5-cb92cba92af7`
- `24f8f6dd-1d92-5d8a-9576-898f9ca1ed59`
- `b70134f2-4ef0-5827-8238-53768bbb6d59`
- `c08d03cb-8da7-5cdc-9dd0-4fd2808704d3`
- `4c1f1f13-0893-5f50-b3ff-79654033ed57`
- `25edd7d6-d82c-5da7-8662-dbcbf154c88d`
- `1f73b2e8-0d88-5fc5-ab55-31790458e445`
- `80db9cde-e37c-5097-8bb4-dcd5ade0b7c3`
- `b1a24ee9-7df2-5c02-ad92-53477234ed0f`
- `63777d74-62e7-54e4-b490-fbfbf8106380`
- `b5ddd8c5-3c0a-5581-9866-09bd3439967d`
- `da06ba6f-35f1-5068-b8c3-462c8d5a2f34`
- `4aa87082-b97f-5063-8daf-c461e9c88cac`
- `c852e05d-e930-572c-92d2-03174a1ef0b4`
- `d3b8af24-bb88-56af-bc07-08b0894b0ea4`
- `9d61ccae-28d7-5720-a28d-db55d161e658`
- `ace3d794-89ad-533a-a7a3-951c80702798`
- `3b2d1f35-998f-55b8-9ae3-160c56a02045`
- `7ba31266-a20a-5a10-bae0-a5786c5e9e7b`
- `bf026c56-8963-5293-8d8d-c25317c4132b`
- `3a8d6e39-d6c4-59d9-93b8-e66d3e62f261`
- `f8c0b405-61c0-5912-bde8-3ee43732cf2b`
- `da538a5a-795c-54b1-9acf-a3eab770ec09`
- `622214e3-6d0e-54be-8d3b-7710a8655ffa`
- `f543cf01-4e80-5481-8d64-e7d1b2173d26`
- `c1567c00-63cb-5d91-a1c9-6a4f2a312832`
- `bb23a29e-8b0e-54c8-86e7-a0d64d328a89`
- `b892e8e7-c3d3-5393-a6e4-f4c07b60e507`
- `e40ace98-3611-5b70-ba3f-e314132dad90`
- `4f0e3957-28e2-59a6-9bce-6062c097da87`
- `67915b65-59cc-5c39-992e-e4030fb120da`
- `332aff75-60d2-5f15-94d8-a37c691f3ffe`
- `06e8292c-5357-5eae-8604-528f6e4ce6eb`
- `af17642c-6961-59de-881a-064718412cfc`
- `68489333-8b81-5223-9a28-ada8fb9776b8`
- `0057a245-5e91-53bd-991f-0e119e677d42`
- `84e8c869-0a4f-51c5-bfca-5c1ea7409bb6`
- `b4cee7a1-c7f1-554f-9633-b2c61a900ca9`
- `c58ed984-638e-5cc6-9ce0-62b218198079`
- `618108bd-7040-5835-96f0-5078b31b2caf`
- `8b84009e-f5af-524b-9466-fab69bd55e6f`
- `f5a00bbf-435e-52ab-a462-b087f1a5687d`
- `c25d3a19-2dce-53b2-90db-ca7126cca475`
- `041aae37-a364-5d1d-87cf-11b4fd98d07a`
- `319d1269-f907-51b7-8707-0dd1fe5af015`
- `d0ec2b17-329c-561e-bcd2-9f1398a1bec4`
- `7ba76e22-713e-559f-9312-926d80835c69`
- `16bd62e3-bb5d-533a-a3da-a3c175c4b5b8`
- `89d5e6b9-c65d-59f3-969d-dc97886bd006`
- `c9718cf8-8709-5181-847d-19c76069f965`
- `4c1ec701-6552-545d-abd0-43337f80737c`
- `8df1ce98-8deb-5e70-aa4b-e79e3e5574d0`
- `aa419568-6e6f-5678-b224-d8d8dc480d80`
- `33ddf083-a76f-595f-a24f-d41159987335`
- `b361d3ab-ac9b-5ee7-a909-7c9c5797b3dc`
- `acde1921-c85c-5eb6-9324-b4362ab5b56c`
- `d1575464-d630-5dda-86dd-6b8912d4699b`
- `c524e01b-1d34-5bd2-9af0-6adfc4c7c781`
- `06b4d3ed-aa51-56ce-9b01-5db43419e213`
- `f7fdeeb2-c0a1-5435-8dff-458d83abd37e`
- `3e6494d9-2e4b-5137-8577-4b88a9514a43`
- `2f2f080d-dc28-5ea8-b976-f08935f9c0fe`
- `e5125725-4f24-5c94-874d-9671877005fc`
- `b323a03b-1d1b-5e4b-ba6d-91f92cd0a069`
- `17ade520-a4e7-5cbd-8e4a-c2ab7157ff9a`
- `bb92b678-f368-5ec0-99dd-7de4b051dec1`
- `9841c71e-18c8-5f24-88f0-f928d9d1b3f6`
- `01b6fd43-5812-579f-8636-e519d893ed01`
- `939e0c96-7af0-5045-a969-29f0bf90c4fe`
- `0ae19ad0-e81c-5214-ba1e-4c001337f17d`
- `f2789cad-2266-5e46-967e-b668b83037d8`
- `13d4f593-a9d6-5f43-8f6b-9da114478ec7`
- `00b51cb1-7cc5-5b5d-8a2b-b92711e2e79e`
- `68e2fce8-d711-5dad-88d5-b0228dd03769`
- `9f4cc3e2-2a97-53b2-b68d-01f8dadfd228`
- `daf50b27-7e3b-59f1-9213-64e1c4ac0c1f`
- `d3dbc5de-84b9-5089-8cc8-8b38973a41b2`
- `caf1ea09-8502-5108-99d8-d995da0ef6f4`
- `cd922a4f-a7e1-5679-91dd-42420d1af963`
- `a2e6768f-4d9d-53e5-879e-c25b44593ce9`
- `3743effb-3da9-554c-92ff-47f991cbf8aa`
- `735ee7aa-1a58-578d-89db-c6d584949842`
- `eaeaccf8-8f13-572b-a237-c7c7e037bab5`
- `a790f8c5-cbec-5bcd-9cce-380b707e579e`
- `c4492c47-be17-5838-9a26-0d5cde892445`
- `63ffa922-5270-5f7c-83f9-61dcdf689704`
- `869c0c16-f4c2-55c4-8b74-65d780618778`
- `b13dacc5-bd6a-5270-8b22-5df8d9a44f8a`
- `07d3e6b2-5dff-550f-9d0d-013d228f09b3`
- `a09f0cde-d1fe-5ad7-90f6-2d785556e862`
- `a98f9913-4328-58ce-92bc-52cb486ab5af`
- `b652f42a-8184-5149-a209-67b5f9e25170`
- `bbcada76-fed3-5b0e-9cad-7f1976dca0b8`
- `3fddb5cd-f1e3-5307-9629-849e0b5a5d3e`
- `d15a689a-ac4a-5d35-9dcf-4005a0ccac35`
- `b1ac29ef-9d4a-517e-bc2f-033aff135596`
- `eea93c39-ff7b-5b11-bee5-45d304b646ab`
- `6cbba32d-006b-5b41-9432-e77056cb4d85`
- `a4b50a23-007d-564f-b5b7-b222a00f30fc`
- `6242d18a-8a25-5697-b478-5e9be89e5d8f`
- `f30a84ca-aa82-5b59-9348-3055f72f81ca`
- `17184173-e91e-52fa-9b1a-ad8ee1b5a7bc`
- `f0751df9-e40a-5161-8634-5a82684ae8f8`
- `fbcf285b-5f15-58bc-8e0d-7b4ccdf8f4e9`
- `a09d46f3-fd9c-5d80-9f17-cf0ac4e5a7d4`
- `f454bfad-e965-59bc-b3f3-2158be6b1d9f`
- `ec354909-3187-53c9-ba75-811ae5be29b1`
- `4bae15e0-ccd5-5a1c-9171-e8cd93e5c982`
- `23cec4c0-886b-544f-aa00-38f635b6300a`
- `bd161524-796f-5174-8fda-8f216ba9004f`
- `cf09d6ec-096f-5ca3-96d8-cc3aec4cc7d5`
- `a5379638-4ec6-5953-883d-d99de28164e8`
- `bd4faeed-1d6a-5b86-bd98-3acb672928db`
- `a45d3041-159b-586b-b8a6-fc63d909aafe`
- `c3cfc50e-06f0-5263-9d9c-3776f5ea8775`
- `2290a525-de97-5da0-b76e-53c7493e956b`
- `5f7384cd-36f7-5137-90ec-f5fe6c9c40c8`
- `90f2fa6a-7458-5b6f-8d6f-fa7c94ce6f35`
- `55c7fd8f-912d-53fa-b0b0-b883a8dd7490`
- `8eb05b87-941a-58d4-b644-1cc3803c29be`
- `3e6ce7ad-1882-55c0-9d9f-975074d3e752`
- `aef690f1-a8d9-5ed3-a9bc-fbf159be2b18`
- `e27f8f31-0302-5fbf-b969-260dd0719253`
- `97a96ee5-5618-54d4-9491-6883197f4c64`
- `2b4e7506-3469-54ba-b0f1-ed2b059d040e`
- `3fdacad4-2cb3-5b68-aba6-d0e671eceb9d`
- `bee129a7-e572-5092-9184-0e73441ccb96`
- `03f021b1-cdb3-5e89-a056-d3db2c1a6a93`
- `20ea3b54-2016-5857-94a5-272330c8afc8`
- `a7842246-f001-5eff-abb4-2c043d91f4dc`
- `ef308355-0b2a-50af-bd06-299dc8c3a0c0`
- `521a379a-677b-520b-969e-6c7cef12cdf0`
- `e0a9f44a-45af-58be-9242-73fcd611c789`
- `19f81e04-4288-593a-9c41-cc1db36ac82c`
- `69a0e90c-598a-5c95-ab6a-4416ae0eabaa`
- `f6a22bfc-66d5-5e9d-99cf-9f8ac22fd9a3`
- `9d2ef07a-f745-53b3-85a3-b09f90409af0`
- `0759d1be-9890-52c9-a18a-e138ab63ccb1`
- `a6c969cd-4bf6-5c55-a28c-0a55acaab172`
- `65350a64-bec1-53f6-b67e-a3a80f274947`
- `797eb361-c01d-5edc-a67f-55fd9dc283df`
- `7bfc1589-d330-57cc-9427-5119411dbbae`
- `a0c5a6f1-577e-56a2-8000-0080037b1a40`
- `998eea2b-3d04-5a67-9756-a02d22c9b8a9`
- `d0f7bdc0-b3e6-5114-b347-74f693616085`
- `55f7c269-7b81-5406-8bee-e3687e38fe78`
- `030c8957-567c-5518-b472-2b24e151f478`
- `24b71dc1-f152-5e1f-a457-0ca14cfd048a`
- `5fe3e307-49e3-5f0f-ad74-d748354fd800`
- `1ecb3510-ad3e-5dba-8415-288a1c72b035`
- `282f06bc-2638-57cf-aa6a-ff4704d284ee`
- `71f6bb7d-337b-547a-8012-704a403d0530`
- `2b8883c1-fc3d-5d4a-90a2-e1b710de39ca`
- `34ce628b-e563-5717-b074-31e0222e7556`
- `00abbd45-c3ba-5f4e-9e37-af24e7589ea3`
- `348ee3ac-5b76-5c06-9817-f1cf13320b16`
- `96579c7a-8181-5ef0-ae4c-f5ae33db7702`
- `f0ffc4e4-83b5-5e99-8e7f-39b7feeb70f8`
- `5f588bdd-1fa4-5349-bde5-dff0328eb84b`
- `06639ba5-35d2-5f93-950f-0f9621fc96d6`

