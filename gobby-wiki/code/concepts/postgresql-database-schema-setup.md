---
title: PostgreSQL Database Schema Setup
type: code_concept
provenance:
- file: crates/gcode/src/setup/contracts.rs
  ranges:
  - 5-8
  - 10-14
  - 191-193
  - 195-197
- file: crates/gcode/src/setup/ddl.rs
  ranges:
  - 8-10
  - 13-16
  - 19-23
  - 25-27
  - 29-34
  - 36-38
  - 40-278
  - 282-284
  - 286-292
  - 294-308
  - 311-319
  - 321-338
- file: crates/gcode/src/setup/identifiers.rs
  ranges:
  - 5-15
  - 17-41
- file: crates/gcode/src/setup/postgres.rs
  ranges:
  - 12-57
  - 59-77
  - 85-101
  - 103-114
  - 116-131
  - 133-145
  - 147-179
  - 181-212
  - 214-232
  - 234-256
  - 258-262
  - 264-292
  - 294-308
- file: crates/gcode/src/setup/tests.rs
  ranges:
  - 12-55
  - 58-84
  - 87-128
  - 130-155
  - 157-162
  - 165-180
  - 183-191
  - 194-224
  - 227-231
  - 234-244
  - 247-258
  - 261-274
  - 277-297
  - 300-313
  - 316-321
  - 324-329
  - 340-407
  - 410-422
  - 424-428
  - 430-436
  - 438-443
  - 447-458
  - 462-471
- file: crates/gcode/src/setup/types.rs
  ranges:
  - '5'
  - 8-10
  - 12-14
  - 16-18
  - 20-22
  - 26-28
  - 32-37
  - 41-66
  - 69-87
  - 95-110
  - 114-118
  - 121-129
  - 132-135
  - 138-147
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/setup/contracts.rs:5-8](crates/gcode/src/setup/contracts.rs#L5-L8), [crates/gcode/src/setup/contracts.rs:10-14](crates/gcode/src/setup/contracts.rs#L10-L14), [crates/gcode/src/setup/contracts.rs:191-193](crates/gcode/src/setup/contracts.rs#L191-L193), [crates/gcode/src/setup/contracts.rs:195-197](crates/gcode/src/setup/contracts.rs#L195-L197)
- [crates/gcode/src/setup/ddl.rs:8-10](crates/gcode/src/setup/ddl.rs#L8-L10), [crates/gcode/src/setup/ddl.rs:13-16](crates/gcode/src/setup/ddl.rs#L13-L16), [crates/gcode/src/setup/ddl.rs:19-23](crates/gcode/src/setup/ddl.rs#L19-L23), [crates/gcode/src/setup/ddl.rs:25-27](crates/gcode/src/setup/ddl.rs#L25-L27), [crates/gcode/src/setup/ddl.rs:29-34](crates/gcode/src/setup/ddl.rs#L29-L34), [crates/gcode/src/setup/ddl.rs:36-38](crates/gcode/src/setup/ddl.rs#L36-L38), [crates/gcode/src/setup/ddl.rs:40-278](crates/gcode/src/setup/ddl.rs#L40-L278), [crates/gcode/src/setup/ddl.rs:282-284](crates/gcode/src/setup/ddl.rs#L282-L284), [crates/gcode/src/setup/ddl.rs:286-292](crates/gcode/src/setup/ddl.rs#L286-L292), [crates/gcode/src/setup/ddl.rs:294-308](crates/gcode/src/setup/ddl.rs#L294-L308), [crates/gcode/src/setup/ddl.rs:311-319](crates/gcode/src/setup/ddl.rs#L311-L319), [crates/gcode/src/setup/ddl.rs:321-338](crates/gcode/src/setup/ddl.rs#L321-L338)
- [crates/gcode/src/setup/identifiers.rs:5-15](crates/gcode/src/setup/identifiers.rs#L5-L15), [crates/gcode/src/setup/identifiers.rs:17-41](crates/gcode/src/setup/identifiers.rs#L17-L41)
- [crates/gcode/src/setup/postgres.rs:12-57](crates/gcode/src/setup/postgres.rs#L12-L57), [crates/gcode/src/setup/postgres.rs:59-77](crates/gcode/src/setup/postgres.rs#L59-L77), [crates/gcode/src/setup/postgres.rs:85-101](crates/gcode/src/setup/postgres.rs#L85-L101), [crates/gcode/src/setup/postgres.rs:103-114](crates/gcode/src/setup/postgres.rs#L103-L114), [crates/gcode/src/setup/postgres.rs:116-131](crates/gcode/src/setup/postgres.rs#L116-L131), [crates/gcode/src/setup/postgres.rs:133-145](crates/gcode/src/setup/postgres.rs#L133-L145), [crates/gcode/src/setup/postgres.rs:147-179](crates/gcode/src/setup/postgres.rs#L147-L179), [crates/gcode/src/setup/postgres.rs:181-212](crates/gcode/src/setup/postgres.rs#L181-L212), [crates/gcode/src/setup/postgres.rs:214-232](crates/gcode/src/setup/postgres.rs#L214-L232), [crates/gcode/src/setup/postgres.rs:234-256](crates/gcode/src/setup/postgres.rs#L234-L256), [crates/gcode/src/setup/postgres.rs:258-262](crates/gcode/src/setup/postgres.rs#L258-L262), [crates/gcode/src/setup/postgres.rs:264-292](crates/gcode/src/setup/postgres.rs#L264-L292), [crates/gcode/src/setup/postgres.rs:294-308](crates/gcode/src/setup/postgres.rs#L294-L308)
- [crates/gcode/src/setup/tests.rs:12-55](crates/gcode/src/setup/tests.rs#L12-L55), [crates/gcode/src/setup/tests.rs:58-84](crates/gcode/src/setup/tests.rs#L58-L84), [crates/gcode/src/setup/tests.rs:87-128](crates/gcode/src/setup/tests.rs#L87-L128), [crates/gcode/src/setup/tests.rs:130-155](crates/gcode/src/setup/tests.rs#L130-L155), [crates/gcode/src/setup/tests.rs:157-162](crates/gcode/src/setup/tests.rs#L157-L162), [crates/gcode/src/setup/tests.rs:165-180](crates/gcode/src/setup/tests.rs#L165-L180), [crates/gcode/src/setup/tests.rs:183-191](crates/gcode/src/setup/tests.rs#L183-L191), [crates/gcode/src/setup/tests.rs:194-224](crates/gcode/src/setup/tests.rs#L194-L224), [crates/gcode/src/setup/tests.rs:227-231](crates/gcode/src/setup/tests.rs#L227-L231), [crates/gcode/src/setup/tests.rs:234-244](crates/gcode/src/setup/tests.rs#L234-L244), [crates/gcode/src/setup/tests.rs:247-258](crates/gcode/src/setup/tests.rs#L247-L258), [crates/gcode/src/setup/tests.rs:261-274](crates/gcode/src/setup/tests.rs#L261-L274), [crates/gcode/src/setup/tests.rs:277-297](crates/gcode/src/setup/tests.rs#L277-L297), [crates/gcode/src/setup/tests.rs:300-313](crates/gcode/src/setup/tests.rs#L300-L313), [crates/gcode/src/setup/tests.rs:316-321](crates/gcode/src/setup/tests.rs#L316-L321), [crates/gcode/src/setup/tests.rs:324-329](crates/gcode/src/setup/tests.rs#L324-L329), [crates/gcode/src/setup/tests.rs:340-407](crates/gcode/src/setup/tests.rs#L340-L407), [crates/gcode/src/setup/tests.rs:410-422](crates/gcode/src/setup/tests.rs#L410-L422), [crates/gcode/src/setup/tests.rs:424-428](crates/gcode/src/setup/tests.rs#L424-L428), [crates/gcode/src/setup/tests.rs:430-436](crates/gcode/src/setup/tests.rs#L430-L436), [crates/gcode/src/setup/tests.rs:438-443](crates/gcode/src/setup/tests.rs#L438-L443), [crates/gcode/src/setup/tests.rs:447-458](crates/gcode/src/setup/tests.rs#L447-L458), [crates/gcode/src/setup/tests.rs:462-471](crates/gcode/src/setup/tests.rs#L462-L471)
- [crates/gcode/src/setup/types.rs:5](crates/gcode/src/setup/types.rs#L5), [crates/gcode/src/setup/types.rs:8-10](crates/gcode/src/setup/types.rs#L8-L10), [crates/gcode/src/setup/types.rs:12-14](crates/gcode/src/setup/types.rs#L12-L14), [crates/gcode/src/setup/types.rs:16-18](crates/gcode/src/setup/types.rs#L16-L18), [crates/gcode/src/setup/types.rs:20-22](crates/gcode/src/setup/types.rs#L20-L22), [crates/gcode/src/setup/types.rs:26-28](crates/gcode/src/setup/types.rs#L26-L28), [crates/gcode/src/setup/types.rs:32-37](crates/gcode/src/setup/types.rs#L32-L37), [crates/gcode/src/setup/types.rs:41-66](crates/gcode/src/setup/types.rs#L41-L66), [crates/gcode/src/setup/types.rs:69-87](crates/gcode/src/setup/types.rs#L69-L87), [crates/gcode/src/setup/types.rs:95-110](crates/gcode/src/setup/types.rs#L95-L110), [crates/gcode/src/setup/types.rs:114-118](crates/gcode/src/setup/types.rs#L114-L118), [crates/gcode/src/setup/types.rs:121-129](crates/gcode/src/setup/types.rs#L121-L129), [crates/gcode/src/setup/types.rs:132-135](crates/gcode/src/setup/types.rs#L132-L135), [crates/gcode/src/setup/types.rs:138-147](crates/gcode/src/setup/types.rs#L138-L147)

</details>

# PostgreSQL Database Schema Setup

## Overview

Orchestrates direct SQL and DDL provisioning, extensions like pg_search, and schema validation across the PostgreSQL code index.

## Reference Modules

- [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]
