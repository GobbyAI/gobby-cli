---
title: crates/gwiki/contract
type: code_module
provenance:
- file: crates/gwiki/contract/gwiki.contract.json
  ranges:
  - 2-931
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/contract/gwiki.contract.json:2-931](crates/gwiki/contract/gwiki.contract.json#L2-L931)

</details>

# crates/gwiki/contract

Parent: [[code/modules/crates/gwiki|crates/gwiki]]

## Overview

The crates/gwiki/contract module is responsible for defining the structured JSON contract of the gwiki local-first wiki CLI, establishing a machine-readable schema for its capabilities, options, and commands crates/gwiki/contract/gwiki.contract.json:2. It serves as an integration boundary for daemons and external tools by declaring contract metadata, versioning, global options, and scoped selection mechanisms crates/gwiki/contract/gwiki.contract.json:3,5-25. The contract facilitates automated command discovery, parameter validation, and predictable output formats crates/gwiki/contract/gwiki.contract.json:7.

Key flows revolve around parsing global options such as output formatting and noise suppression crates/gwiki/contract/gwiki.contract.json:5-25, resolving target boundaries via project and topic scopes crates/gwiki/contract/gwiki.contract.json:7, and routing user requests to specialized daemon-consumed commands crates/gwiki/contract/gwiki.contract.json:7. Collaboration points are heavily structured around expected JSON output key shapes and standardized execution error codes, allowing client applications to safely interface with the local wiki system crates/gwiki/contract/gwiki.contract.json:7.

### Tool Metadata
| Property | Value | Citation |
| --- | --- | --- |
| Tool Name | gwiki | crates/gwiki/contract/gwiki.contract.json:2 |
| Contract Version | 5 | crates/gwiki/contract/gwiki.contract.json:3 |
| Summary | Local-first wiki CLI for capture, search, upkeep, and synthesis. | crates/gwiki/contract/gwiki.contract.json:4 |

### Global Flags
| Flag | Value Name | Allowed Values | Required | Repeatable | Citation |
| --- | --- | --- | --- | --- | --- |
| --format | json\|text | json, text | false | false | crates/gwiki/contract/gwiki.contract.json:5-25 |
| --quiet | None | None | false | false | crates/gwiki/contract/gwiki.contract.json:5-25 |

### Scope Selection Flags
| Flag | Value Name | Default | Required | Repeatable | Citation |
| --- | --- | --- | --- | --- | --- |
| --project | ROOT | detect project from CWD | false | false | crates/gwiki/contract/gwiki.contract.json:7 |
| --topic | NAME | None | false | false | crates/gwiki/contract/gwiki.contract.json:7 |

### Declared CLI Commands
| Command | Summary | Daemon Consumed | JSON Output Keys | Citation |
| --- | --- | --- | --- | --- |
| contract | Emit this CLI contract. | true | tool, contract_version, summary, global_flags, scope, commands, error_codes | crates/gwiki/contract/gwiki.contract.json:7 |
| index | Index markdown and source notes in the selected scope. | true | command, scope, status, indexed_pages, indexed_sources | crates/gwiki/contract/gwiki.contract.json:7 |
| search | Search wiki documents in the selected scope. | true | N/A | crates/gwiki/contract/gwiki.contract.json:7 |
[crates/gwiki/contract/gwiki.contract.json:2]
[crates/gwiki/contract/gwiki.contract.json:3]
[crates/gwiki/contract/gwiki.contract.json:4]
[crates/gwiki/contract/gwiki.contract.json:5-25]
[crates/gwiki/contract/gwiki.contract.json:7]

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/contract/gwiki.contract.json\|crates/gwiki/contract/gwiki.contract.json]] | This file defines the JSON contract for the `gwiki` local-first wiki CLI. It declares the tool metadata and contract version, shared global flags like `--format` and `--quiet`, scope-selection options for choosing a project/topic, and a long command list where each command specifies its summary, whether it is daemon-consumed, its positional arguments and flags, and the JSON keys it returns. The `error_codes` section closes out the contract with the CLI’s standardized failure responses. [crates/gwiki/contract/gwiki.contract.json:2] [crates/gwiki/contract/gwiki.contract.json:3] [crates/gwiki/contract/gwiki.contract.json:4] [crates/gwiki/contract/gwiki.contract.json:5-25] [crates/gwiki/contract/gwiki.contract.json:7] |

## Components

| Component ID |
| --- |
| `d6bebc49-8b7b-5bbd-bce2-1aeb8d231aa8` |
| `adc77e32-1340-53d6-87d9-327025bc5ba4` |
| `ec25b4ee-2154-50d5-a880-92f7339a8154` |
| `7b7c5919-4aec-5ced-ad43-b5b37721f94e` |
| `d0a3f0ef-e655-5667-adb9-a913420ea9e1` |
| `8c5005c8-0236-5bb4-9fee-2a80b68ad910` |
| `5061f4d8-30e8-5b4a-b764-0483eb89199b` |
| `610f20ce-2044-54b7-a7fb-659e7a05733a` |
| `b21136b1-0d98-5270-b7dc-642769ac93bb` |
| `868845e9-81a4-5209-99db-943a8906af60` |
| `e49a0285-ad13-5a6b-9aab-6c5b4f973886` |
| `21e64a61-61eb-5a67-ab24-cd80e00206de` |
| `e2cd0315-b252-5873-91f6-5287e3b5e6bd` |
| `6262385a-c14d-576a-a233-c308a84e74f0` |
| `c7c0edb4-448a-577f-875e-a7d10895bdde` |
| `8c682e20-5c35-5b16-9edc-0d53962b4111` |
| `a419ffc8-f394-57df-936e-589a6e5f07dd` |
| `eef6fb36-385c-5569-88ba-40b2c3623ec4` |
| `455218b2-4ecb-58be-a7c2-2364fc639aa1` |
| `0ca1c66e-291c-54b3-b8e9-985b7dd75fa3` |
| `e8f9d4f3-b294-5442-a652-5bafd89d6cab` |
| `4eb3acda-bcfd-58de-b3be-6c067ce6db4c` |
| `3ebd9e2d-1a9a-51a8-a009-5fa2710840b4` |
| `7bf3dc44-997c-5129-bae6-939f8199dfde` |
| `84007c9c-7999-580c-96c1-b409eb92ea62` |
| `e24499a1-55de-507b-a47d-ef03a1e399ee` |
| `49df87b5-2b1a-59d9-9869-8ef0e6233b1c` |
| `27e21d63-e0ca-529f-81b3-b5869d8c2f39` |
| `bbc6b5a8-0f0e-54b7-b069-764067f2489b` |
| `a20635cb-5a79-5278-8fb2-b5aaaf8b8e08` |
| `d64b6a76-e59d-5cf5-9f48-70decc081ddd` |
| `b20ee172-2804-5698-9e24-c4755ffb7684` |
| `40449839-5ca1-5d50-9ef4-a50837289a43` |
| `5e40d585-357e-5d54-81ce-87bbe2816124` |
| `5dafb9c4-5b63-5f05-9b45-fff170b06959` |
| `71604008-b359-5099-bbdd-b081b6b7f6b9` |
| `700f352a-2e9b-54c1-a034-e4c39366cd89` |
| `ef4143a5-edbb-5ed4-9f24-d064a5d78a0b` |
| `873b3e5d-5149-5e73-a6a0-78eeb7487a3a` |
| `355833b0-1e19-5852-811e-4e36e6e55854` |
| `694157c6-242b-53d6-bed2-9338b2542247` |
| `9c92eddf-c26e-514d-8485-b03650cff147` |
| `2bb637b8-de08-5940-8c75-f4eeb355e949` |
| `468ef5e9-e190-5ec0-a83d-af30d3bd29ab` |
| `7e98a115-a59d-5507-b647-8570d23e2609` |
| `d05ccc93-844c-5156-ae9d-49c94278f510` |
| `e34299a1-6e42-5201-9d89-3c0321256e46` |
| `f84f9091-a2d5-542a-930c-0e6e97fa5a82` |
| `17a4e30d-206b-5ff7-9791-195549fde977` |
| `bd8eea27-f069-5bd0-a9a8-515728ace367` |
| `31343cee-8463-5e01-9568-b6f1be92997a` |
| `1550f263-11b1-577b-bd9b-24405010c022` |
| `c36429a4-ee23-524c-b7b5-054678d12bef` |
| `1f810be4-dd70-59b3-9e40-67ce589d7190` |
| `5425a0df-0295-5e19-b4cf-49fc28574f13` |
| `c19334d6-73fb-5b5a-a7c6-57819a555acd` |
| `c2217715-e20c-5961-9bfa-0af7c03b3583` |
| `0ec5adfb-a4ad-52e9-87af-24084b50d342` |
| `4f997412-f95c-5482-b628-58b753835e3b` |
| `607d8ad0-7748-5d3e-8dc5-481cd5e490f6` |
| `863095cf-9e6d-5af1-a84b-daffc21847df` |
| `dd95db19-9f34-583b-95b2-48ca3b3d3c01` |
| `46163400-ab2a-5c00-81a8-a635c077f1ab` |
| `a14dee50-bde9-5c84-a2e6-59b3d4902a8a` |
| `7b3a60e5-8b3b-506a-b48b-cd90b194c6c2` |
| `99db162f-9f31-5cb3-8fa3-a6fa844e0caa` |
| `46bd438d-1af7-5619-b01d-4ec2a00ecad3` |
| `f42b4ca0-69d1-507f-908e-c96f1bc0f52c` |
| `c7072c94-55ea-5f87-b43d-e9a6d10f0fc5` |
| `79c8efb9-4ff9-5fcc-81e6-6538a2fe9e14` |
| `e5fa4554-7dd9-5593-8433-5abe8843d44f` |
| `ce02931b-087e-5906-8bae-7ce9d06463af` |
| `6b1b7fde-f266-58d6-abf0-2467689731a1` |
| `0a1de659-10cf-53eb-9606-7ee93029bf72` |
| `c6a36583-c967-561a-90e0-9b2d8bd7f027` |
| `e299cbe7-62ef-5893-a9cb-e4fdc1784372` |
| `1e26b8af-1283-5107-9002-53f2d500324c` |
| `b903b021-6497-5824-a28c-025d1fbf0a71` |
| `e744edb6-53b9-5bb3-b7b0-1914b2200635` |
| `92a43797-2d88-5bd6-b464-f0ebe7424085` |
| `b4128bce-b08f-5b32-84de-e77add9d670b` |
| `cd10fbbf-cbce-5bbe-92e1-e112d6d0a2ff` |
| `c4643100-53e7-57e0-b442-5131eb89c6dd` |
| `e1fbd1db-a4ab-597d-b384-1db97aebcce0` |
| `0571a69c-afe1-5c4a-9de9-c1a2d768ec43` |
| `a6fd9251-6de2-520a-844d-3747bf8303e3` |
| `a38b0031-1b46-5a0c-8bc1-3a11db975fa9` |
| `47371b4f-68e4-57d7-b24a-bdf2ae378e32` |
| `4d934793-622d-5234-a888-cb0bc6877bc4` |
| `eaeef2b9-e8f2-5707-8602-4b10d8cc66bc` |
| `b4ad851f-72b7-5f8f-8ec8-194c94b4d2da` |
| `183c33ab-1951-5669-b53a-7326d65488c0` |
| `0e41c29a-c7eb-5331-9b75-4475f507a7dc` |
| `5d8447be-864a-5ba9-945a-e336f1f99d0a` |
| `ccdf7173-a7ca-5759-bebd-f599a1e5ee5f` |
| `f83198b0-bb73-55e6-836f-073faac959f1` |
| `2a5f0ffe-3095-526d-87f0-067282b803bb` |
| `9d3109af-f2c8-56f9-aba6-adc24351bf91` |
| `c8383aa5-37c8-544c-9593-6d849a663bcd` |
| `24820e80-1965-51af-8f71-e5e6b66f7733` |
| `d7906d4e-bea2-5f75-adc3-f94709228ed5` |
| `72574373-5a7b-589f-811c-4fc094d6b52a` |
| `cbb51ffc-42bf-5819-9cd4-54bddec26f06` |
| `e160d359-b610-5f65-93e1-f6e549c38dcc` |
| `527128ad-09e4-5556-8cea-0adfa69b3d19` |
| `2bb0b2e4-5bee-58cb-a310-df6cd48222b4` |
| `89d205ea-1696-5780-b916-9dbf481fac8a` |
| `62f0bea8-4680-5628-b9b5-33b052a196e6` |
| `6754ac1d-f8cb-552b-8688-21ef7a71e633` |
| `d8def073-1842-5f23-a218-8486684f4218` |
| `3b381bc6-e42b-5b48-9c3a-fabd74501a5c` |
| `f5839817-59ec-5905-b5bf-ac72b67edfc4` |
| `38c05e9e-1fb5-50cd-85f8-34629a50201c` |
| `0898f276-ed5e-53d5-b94b-231aa7d2eed9` |
| `82e1544c-7fa7-51fe-a6c7-f9f9a1b094b6` |
| `6d40ce20-34d7-568b-9d23-4d8dc0b80992` |
| `cf86ca54-4893-59d9-9b69-68d4fbb6081e` |
| `2903609f-a39c-56c2-85d2-ea5382529ff7` |
| `c93dafd5-17a7-59bb-b123-63b004d8a5f7` |
| `07872db9-5e85-5cbd-9b15-7311796b56e8` |
| `1243051f-eece-5dc0-b512-bdd3b9009d8e` |
| `8a40835a-bb4f-5fb2-91ca-a1b415ff0c5c` |
| `1e5d8202-0ab3-5ee6-9e77-231f42da3b58` |
| `2d05c0f6-7a61-572b-87ef-a39552dd4248` |
| `99c28c35-4c37-5f64-b466-973f49872186` |
| `72245736-6154-5f6a-9cb0-13c3ff61173a` |
| `9f6f03cb-58c3-5526-916a-5aedf650e8c5` |
| `38c986c3-7f3f-5ed9-b687-0f21748de81e` |
| `8408c609-5371-5c92-b9c3-b38bf5f70575` |
| `0a26bc84-2b56-5d49-96c0-bf4cf45a5b3d` |
| `f95df176-e30c-5fa0-ac80-7b0dd8e934b3` |
| `3a371098-15fd-5e6a-835b-2779644d6ff8` |
| `8af6a542-0706-5741-be39-fa5c8ddd71a5` |
| `61cf2529-e36a-5644-8dfd-eac68ea5170c` |
| `dfcd9cb0-32d2-52b2-af31-eb6a2b78b629` |
| `80cd4996-7ee4-59b9-9542-c6cb13cfce03` |
| `3539bbed-fca9-5a36-abf1-ada5a48c4726` |
| `6502a3a3-e7fc-52a3-a917-9906dee52822` |
| `cdbca505-8783-50d9-8030-2eacfa4def42` |
| `bc323508-3537-5119-a464-022e74ce5d18` |
| `a9b488aa-4256-53e8-97ef-cb78d6f7fd3a` |
| `a9ecc04f-058c-52da-9a47-1c077e216b53` |
| `ede6b36d-449b-5394-b196-6a92f91c742c` |
| `e0983435-d4ba-529e-8d6b-8969034c34e9` |
| `9abfe98f-de99-51fc-8ea0-3199fe5defb4` |
| `c592b75e-0d05-5070-85cd-b9821a0b82dd` |
| `8d875005-fcf2-52e4-b26d-9f25ebc83a8b` |
| `e6cc5e24-463e-5719-aa62-b84f9ba11749` |
| `eab7dd6a-d223-5021-8d09-2a2697c7a7f4` |
| `cc113228-3fb5-5dfc-bbb0-3f1a65fc083a` |
| `3df2ce20-ea79-5fb4-8074-1b075e186e6f` |
| `3a0782d7-f62b-5fcd-997d-8fc1d6292782` |
| `cf957708-0dae-5101-ac93-b280ad8decd0` |
| `d27bc4a9-e572-5991-a90e-e6d4897cd68c` |
| `26acf766-49f8-556c-941d-ec27e3dd1e6c` |
| `02dfa3b2-b81c-541a-83c7-a6bf58df6687` |
| `cc1b9b0f-9dfc-5d9e-875c-9b62cc215a93` |
| `38ad483e-dd81-508d-8328-27940fdfbfbd` |
| `3d53397e-9a22-5397-8fc8-22101a27944f` |
| `46febe1c-11f2-5356-bad8-1523a6b0e828` |
| `338a25af-556e-5a1d-8499-9fdde6e36337` |
| `ac012fd2-b095-52e3-876c-64fb80a6a3d3` |
| `6485f8fb-1627-547a-8201-d3b6bed76a7f` |
| `b8e41343-46cd-5792-8067-f30f68eb6121` |
| `a20790ca-0b98-5bfb-aead-4a4f1880205b` |
| `a0579fe8-9c54-5cdd-8cba-797ce430a403` |
| `3add8cc8-7cff-5266-bc62-81691e650d0c` |
| `11f072ba-d7fb-55eb-9b95-a14d73e50406` |
| `3e3d35b8-ba8e-5d38-a6ec-0fb895a90911` |
| `86645885-a0c0-5cab-9920-a843d81a820d` |
| `e7ce887c-529a-52d0-be6b-a3ded93c4abf` |
| `45a0b09b-c49e-5d12-914d-a2e3ed19a3a4` |
| `4fbb3261-532a-5766-aaba-7d85a484ca46` |
| `a9ed36e6-9535-5fd3-a054-688a2491e4a7` |
| `b2b27821-109c-5dff-a814-dea790bc92f5` |
| `a416f37f-0cda-5da1-81a7-4eeb417d02f8` |
| `3e15cd65-4535-552c-bdc2-fa5aa6784d98` |
| `e73f8d58-378a-561f-86ae-7da1d0c8fd1c` |
| `01402c05-b467-5be1-9066-5b8de735e28b` |
| `69d1a192-c322-5bd9-a2fc-e5b5391296e8` |
| `06305bb8-7ce2-58ce-87a5-6ad85cc976e4` |
| `04fd07ed-ac33-52a4-8263-a4d3260c0172` |
| `35cc0153-a60c-5436-a61f-15632f967c9f` |
| `ff980ef0-1f46-52e0-ad5a-bc857559b1b5` |
| `453e7f1c-6ce6-5214-acf9-8f6ebfc09c4a` |
| `34d03058-f270-5977-be09-9cdc84ee8f54` |
| `85951fd5-dbba-5e44-9d1f-8fda0a6bf636` |
| `e53ab389-226e-572e-bcd4-5c0f9a5ad1ce` |
| `9f003335-87ac-5e68-89c5-992ba04156e6` |
| `932632df-2405-512e-8c90-77abca7891a5` |
| `1ea33e11-37f7-5852-98bc-a743fda0545b` |
| `332c916b-bbb0-5bd1-bb34-fb795f90a2fd` |
| `471d07fd-82e8-54b6-a482-80dfb551fe5c` |
| `ce7935a8-85af-53e6-8f45-d0ba5360febb` |
| `d9e7754c-0890-5d3a-bb58-3d439e64a66e` |
| `da28740a-8ec3-5711-9642-bdf0db881402` |
| `7dc6bcc3-c9c1-591c-8987-7ab8c2a851f6` |
| `187c3886-ec2a-5916-a165-d206bf923973` |
| `81059b32-8d3c-5b4b-be7b-6adcca70f8bb` |
| `35d4bda5-13e7-55da-8648-11d2880d0a95` |
| `6688a5a6-7dad-524c-bc98-3fdbd58a530a` |
| `bce411e0-8114-583b-9609-04e87dec2597` |
| `db6cd30a-9b2d-55e4-a5ff-b7440934bf5c` |
| `4b42324f-07b2-5e2c-841f-aafb725d3f45` |
| `6eb28d86-eed2-5647-8edc-04be54973c3c` |
| `5662788b-6e74-5ed6-9784-f8c7cb718bfc` |
| `2723afd2-a13d-55f8-80db-9a2f56340192` |
| `012ff497-e3ed-5935-b2f8-10b6604feafd` |
| `58149708-f46f-5f64-9b73-0ec856a23acf` |
| `fb92256a-57d9-51bb-8ff2-8d8275358be2` |
| `0a3d3354-7373-5841-85c2-a635caaf7dba` |
| `6e46147c-c492-563b-a06f-94d3248279ad` |
| `2c87b94a-675f-5ba3-ae3b-b06f4d5f3cf0` |
| `54598d2b-47c9-564c-866a-e25d2a6928a2` |
| `c7d8127e-2525-59dc-9b44-133216b3db7b` |
| `9f818ed2-874a-52e6-bfc3-fcc1961d1c62` |
| `a194e902-c23b-5a9a-9270-588f43952055` |
| `782278de-6d74-5c69-a84b-8fa5007c308c` |
| `80d945b6-68a4-5360-98dd-adafc52c4f7a` |
| `b51644eb-9b27-544f-b4f2-3464bfb5ac9c` |
| `453db711-18d2-59be-8aa8-c9a32712e497` |
| `ad2ce9ec-4940-598d-8a5c-9361eb51cf65` |
| `0880c6c4-74ca-521c-9abb-93d6c827006d` |
| `6c2defbf-83af-53bd-9ba1-648ab4edff4d` |
| `c195e16d-1901-56a8-9d98-3b60fe088bd4` |
| `6e984d7a-a78e-5810-8310-83daeef9bc80` |
| `603f65fc-6e8e-5b32-a65c-50be3edc6573` |
| `1d803b6d-22ed-57cf-865e-92b2d4664405` |
| `b0d80c36-f8d6-5108-9ec3-677231e2a14a` |
| `47301e7e-9406-54b2-9e85-64902014915a` |
| `1d58ac43-1ce4-58ed-9b70-b326af11dc1b` |
| `9822f405-283f-538c-899a-eb2cac1e1eca` |
| `68b12041-c65c-5c32-9fd0-436b6b4bfbf7` |
| `74ff6c27-4edd-5c4e-bf71-85e587ed4f26` |
| `f159067a-3c74-55c2-bd00-17b7e9f11890` |
| `9ce56da0-364f-5b28-b748-8609244884c2` |
| `528b7230-22b2-5778-be6a-3fba856b180b` |
| `ff27ddb6-ad62-5f39-becb-78d669903e64` |
| `505d3967-2170-589c-a6d1-4a0adfb0c2d1` |
| `0c3e0511-2b8d-5acd-b23f-df6a4b292015` |
| `800516bf-25e5-5732-a779-9bde66b4f448` |
| `85bb1a60-c19d-59e6-9bb0-62b11ed70ecc` |
| `cc771da8-7cf7-5a31-a037-145399211543` |
| `4609e252-a345-5526-950b-ecef735d74d7` |
| `12b653e6-6857-5a06-befa-ff9eb344402c` |
| `b10ba3e0-37ff-5400-8efa-404061fa6557` |
| `80acc0f9-8f47-50e7-90e2-70c3b81dd89c` |
| `26f2a071-7e7f-540d-ba3d-760801528a34` |
| `1966a76f-5564-5681-9f05-d748a70b0595` |
| `d9ff4531-ceec-54bf-bdb2-d3ef9116be78` |
| `f8a29c9b-402c-5751-a367-7a55d5f00456` |
| `c7349aef-4fe3-5805-bb6b-9b9feb2ade2d` |
| `f35c9df8-5845-597f-babb-ed9652b94cc7` |
| `3573f498-8e30-5b76-ac76-51ae7f7993b0` |
| `b7e34540-ea6e-5fd5-98ad-5c3ed9898fc7` |
| `916cd6b8-9d13-5b1e-a614-7db965157a06` |
| `e71c79c3-442b-5c53-99be-0d292143cf20` |
| `0e3d6b9d-e971-5fcb-8db0-143442702b72` |
| `648e368d-1d8a-593a-bba6-566aeb1eeb85` |
| `fd06bcaf-7b44-57a1-84ea-ca8867da279a` |
| `028731f3-3639-59fb-aeeb-c510a57b505d` |
| `e7d013e7-bc7c-5b70-abb6-334eaeffb5b9` |
| `0bf2e733-1cd6-5c82-9d1c-d997a2fbea61` |
| `e4ec806b-f719-5949-9c95-3f78955a7b8a` |
| `aeb161e3-4ae5-5e4d-9d06-931ecf440251` |
| `2e75c865-bdda-5e7a-8d62-2c6b0c867d3a` |
| `feaa0980-0cfd-5c3e-82ab-da766c285e93` |
| `1ac5f71f-4f8e-58f1-bcf1-0cfb3b9ed0f1` |
| `5c40681f-469c-590a-87c2-5d6a9945938b` |
| `c82cf4d1-d689-5843-bb50-4ba71bd50557` |
| `d172ef44-31ea-50a0-901c-f99d7ec0e42c` |
| `26e5755a-2cda-5663-b7b9-870622bf59ad` |
| `4447713e-73f9-5b97-a102-2e127fac420f` |
| `c0b67f42-8762-588f-add3-21653cd44474` |
| `b6e39d56-a20b-53fd-b053-771b48212a66` |
| `98a13c9a-47ad-5da8-81b4-424423ecd748` |
| `5cb864a8-0da9-50f6-8707-a98f2d48b58a` |
| `ce7883f8-abf1-52c6-b5e3-fe51223d2530` |
| `4835f452-64c2-5b13-a65d-4461e221d379` |
| `c658b498-c631-57c0-aecc-e01e781bd77c` |
| `c4947a8a-4d50-5d1a-8877-d379d0979ee7` |
| `58f47f94-6833-50f2-baa0-e5a787918a0d` |
| `b1eb4032-f561-55ce-b1dd-8f59d366b25e` |
| `e6d53687-76b9-5f45-8831-ff51181ea7fb` |
| `b6872583-74dc-5471-a10b-1cccef1c284f` |
| `5f78cdf8-768b-5de2-a20e-348ed1c02f82` |
| `e7053a83-e5e0-5357-83f7-b62c10ec52ce` |
| `f93fb1f2-5c17-55fb-b747-83e24c06c760` |
| `b9aab2c6-a737-5b38-81fa-e7a5e598e45d` |
| `f696a1e9-68c7-5d54-a19a-dc9c4f72c287` |
| `3729408e-b4ba-56a5-bf24-78a6d509440d` |
| `4f9c4b4c-db5a-5878-92b7-9d00731d8884` |
| `169cb8a6-9f8b-5657-9be9-4275aae81d0b` |
| `8c91faa4-7ef4-5569-a895-eac680c3e71b` |
| `78f79381-dc3d-5c72-9b12-093d26b4d9d2` |
| `6a55b426-a215-56b9-ba24-79930fdab483` |
| `42ab2004-8eaa-57c1-b853-298e4df36930` |
| `d4217ff6-20f5-5809-804a-e6c8d248000d` |
| `bc372db6-f61e-5636-b86e-cb0621a3b55d` |
| `d6d3a935-3e40-54e8-a9c2-8bb8f6f3af22` |
| `2ed9076d-5583-5eb8-bde6-4764ab789d87` |
| `a7150d30-fcc3-5702-b29d-02d1f6daebc3` |
| `449c3dcd-87b1-59f7-a2c3-a3a7a332b58d` |
| `41796075-a8d9-5f2d-b04f-2c2b99e408bc` |
| `e3e092b3-86c1-52f6-898d-82c513579ea8` |
| `4e802e26-4aea-583f-b1b7-4957be233656` |
| `e939b97a-c553-500c-8173-a6b9560bcc7f` |
| `fe5da660-0096-5645-b00c-4aa857981878` |
| `2f2e4f9d-477d-574b-9937-3c98d84aab07` |
| `d74d864b-91e2-5c0d-be2b-0992776b3cf0` |
| `3776e826-098a-5b0e-b668-61bc1e13d53d` |
| `e27855b0-b9bd-53f7-a92a-319c7f10d0bf` |
| `be4accae-0e7c-545a-827c-dda4d75a6c9c` |
| `b8b72309-5580-5679-b8ef-8714ea8da661` |
| `14b7640c-d525-5019-8559-a6d4a114788d` |
| `4d1bf858-b2ab-5f4a-827a-e2afe0d99e86` |
| `eb93bc84-95fd-5746-b2b6-7c9b9a4e00c1` |
| `4cb685f1-9a68-5601-bbbe-d5d65bc192cd` |
| `c91c8397-2df3-5982-ab10-17980823ba7f` |
| `9a1eefb8-0e1f-571d-9bb6-ad8614e01d03` |
| `2d5e1e5b-ea92-5f70-a2a9-711aca19cb86` |
| `b6aed644-b4ca-50b7-9b49-bf078b70d021` |
| `62b36b82-a2f8-5e22-b34a-0dab3b4c5275` |
| `62c84b41-5d0b-5f3c-9166-28ad10aafe1d` |
| `8f7d404f-66e7-5c0f-83f8-a994c9d5ed80` |
| `3a1b9116-50fd-5087-a01e-e16ed046cf56` |
| `0472eb25-fd3f-5dbd-9826-2dd2349caccb` |
| `84b7b796-a5df-5a33-8bd0-6af9d44e4244` |
| `bd991042-55e5-5ada-8b58-026c9238f429` |
| `a4c50a8a-c1e4-54d6-af82-5e67907bfbc4` |
| `1dbb0a83-4fa5-5ef5-9cd8-138986be09c3` |
| `766d3714-872c-58d2-83a1-a6b6850fe4b5` |
| `b7732569-6a8f-572c-98b1-89e5ea033a23` |
| `0e3292ad-8d8b-5351-b1ea-ce6ec5817bd3` |
| `83bc4f26-86f3-5780-8c3e-539667da5a8c` |
| `0bd8430d-d013-5bce-911f-40af2dfd8ade` |
| `2f3c358b-f65f-5580-8fa2-08ca282d2db3` |
| `0f87bee2-f358-557e-b51d-d4c5e78002cb` |
| `02459929-6d22-54e0-8bf2-b3b66b016efa` |
| `5de62f49-876c-5c3c-8ff4-c26ac8dbf983` |
| `5250c5d3-6234-52cf-a923-84c3c5dc1907` |
| `9440f323-5ed3-5ad7-8538-7ca81b107bb4` |
| `769acf8d-1c50-5b14-a6d4-f2698e03fff2` |
| `54c36f29-74c0-50e9-ab5b-6ac7e63dbf93` |
| `3345c387-5721-5ca3-8a71-7d8eb22512c1` |
| `7b540872-38ea-5159-8de6-896bbc1323bc` |
| `7aab2731-9b26-5e9e-a227-eba1cad2c21e` |
| `88588b32-a81c-51ca-be52-3bd78a852e47` |
| `c94d4f5a-e148-58dc-95c8-67ddf5ce72fc` |
| `f9a5de12-246f-5749-a6cc-46e8612d6ec2` |
| `6782724d-000b-5c04-9abd-fb89ced1aafb` |
| `d2be0000-57b3-5289-a17c-3cb08c55c769` |
| `ea1e307c-baa1-5bce-b094-dd11111e5415` |
| `d5f7d325-dc0f-5379-b9ab-0e5d52bb4d24` |
| `7e3734e4-672f-5c6b-b301-3def2d4d01b2` |
| `70c53caf-0776-598b-af6b-a372e3f31d4f` |
| `12d6903e-78d3-568b-8e2c-02949ec414b8` |
| `852b4a07-3ba5-5498-97af-f2820bf1ad1f` |
| `6a2a98ea-ee2d-50b0-a504-979674eeea8f` |
| `df8cbb13-fbb6-56bd-bdee-6798edf8f1c2` |
| `054b093c-59bc-56d9-b04c-60530da10acc` |
| `f9ac95d5-c627-5892-a4bd-dfbcd425147d` |
| `c43048eb-02c9-5210-bdb8-eb1d268cfec4` |
| `18963082-86ff-58c2-b1d1-af9503b9a8e0` |
| `77d50c40-0423-569d-8379-7830afee514c` |
| `ad59615d-9296-526f-b7b2-98d2d45bccf3` |
| `f27382f8-cc2c-56c2-89f1-458be42e15c9` |
| `41b9df62-3f7d-583f-8e95-ebc8c7a24c5e` |
| `ed2018cd-1808-5b1c-b58d-7de6dda2ee3c` |
| `ba5c88c4-2dbe-5353-ae33-f3d6bad7e0a2` |
| `4cd938a6-ee94-515e-8e75-eb3cae61d198` |
| `6ce82217-3583-5e2d-ae3c-c7e84bbf558c` |
| `65935799-4e0d-5f3c-9248-7d99e33fa2d1` |
| `53cbe4cd-a32a-5c94-82f6-aa69496a2664` |
| `73d8051f-1e6e-52dc-a4d4-11f9109a2330` |
| `657ced5e-e616-5448-b339-0ce30d0de869` |
| `01307d01-fef2-5e5e-ba30-21a3283fc927` |
| `deebad5c-3bc1-58f8-b6b0-28ccf4919b41` |
| `e3313ee2-da2e-5410-b578-ed6e456911a8` |
| `277e13c9-5540-5f87-9f62-dce7dd907893` |
| `6f33c339-6d5e-5e9a-937b-8f55ecea2a11` |
| `00048b2d-a4f3-54d4-904b-dbaf7f65c202` |
| `599e1356-20af-5485-a408-23464255eab6` |
| `417c5926-c714-5d79-b6e1-ae4b76ec98fa` |
| `594c880a-4ac7-5527-bfac-729cce03e645` |
| `5a7ad2a5-4376-596b-bb72-848f7c579585` |
| `80f95d69-1087-5f94-a6e7-7db9eb682bcc` |
| `39da70a5-091d-5d79-baef-0a51740f3a8d` |
| `998bd6bd-93f0-584b-a549-e8ac656239bd` |
| `34b011cb-3da0-5a9a-a937-40bc4161c6cc` |
| `b8ca567c-0eb1-5f66-9070-7670e5ac98c8` |
| `a075323c-857d-5822-ba63-1172c74f6f65` |
| `74690188-7569-517f-8c08-9877dd497a99` |
| `54013d16-d3d1-5163-868c-d1a6afbacdeb` |
| `65119898-81ab-5977-bfba-b2e048c2fb23` |
| `62364dc1-aa57-5738-9a0b-6e6a7b4a0d54` |
| `07717498-c7d9-5bf3-9255-95699dc422df` |
| `ebaf8edd-6a26-5497-88b8-cf0dde54cb7d` |
| `47d75e6c-0592-5254-8c44-1e2d934d6bdd` |
| `34c8ad30-fa64-50d7-b383-5ecef1a3c085` |
| `a7010ff1-c004-5728-9816-e3089882f2f5` |
| `c2c20bbd-acf1-578b-887f-e8037c1d1528` |
| `e38f96bd-ae39-508f-98b6-6870b7e217a0` |
| `d26fbf5b-6b88-50b9-be72-afdc1f068415` |
| `07274dcb-6395-556a-8195-d8dfd3642cc0` |
| `542bfca0-3d8b-51c0-aca1-0e32429bbced` |
| `f58d2dbf-d0fa-5337-b13c-8d6741e16273` |
| `6adf4043-0d40-5ab6-a9e3-00dacdc0cacb` |
| `b3a353b8-dc00-5df7-b5ff-41f6bed1fc52` |
| `2b6bfb6e-faff-5b41-9e7b-9525fd884f48` |
| `ee0e4b5a-400c-51ea-a788-be621b88085c` |
| `f11604b8-900f-55b3-b1b5-8eb48a88f143` |
| `31fd854e-5d44-5477-8eca-2f08d4b81868` |
| `b35017f3-345d-5bfa-8a52-30ccbc1b5349` |
| `9f772039-c842-5022-bc34-98fbe2b16479` |
| `a8ed286c-9310-5f7e-b6a7-a832996267bb` |
| `3f0fd254-179d-564c-b151-d923ea6d2c16` |
| `5dc4051a-157b-5fa5-afe7-f600fe8e1e01` |
| `bcfe03b8-dca1-5df0-87e6-55ae581e3e35` |
| `fc96403c-f3d9-5901-b93a-aa3841610189` |
| `28a61016-f57a-5b5c-a6ec-0739ae1975e7` |
| `c9bf073e-27a2-5280-848d-e85174a449aa` |
| `345c2e3f-28ed-5ad0-8f2a-3675c91896f2` |
| `63af79cb-fe6d-5a86-9433-bc480e170cc3` |
| `f275f65d-af1a-57ca-b8ef-5ed9ab6344ef` |
| `fc12948e-19c6-5697-8e37-a9635ca8ef80` |
| `c5435623-cb6f-5cca-81ea-01dfa7181dc8` |
| `cca03961-4b1c-53a2-bd59-e64eb97fcce5` |
| `1286af07-8b7f-584d-a471-3f7329fe628d` |
