---
title: Import Resolution & Syntax Parsing
type: code_concept
provenance:
- file: crates/gcode/assets/import_roots/elixir_dependency_roots.json
  ranges:
  - 2-17
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
  ranges:
  - 2-11
- file: crates/gcode/src/index/import_resolution/context.rs
  ranges:
  - 41-138
  - 144-146
  - 151-166
  - 170-187
  - 194-206
  - 212-214
  - 220-225
  - 231-236
  - 241-246
  - 248-253
  - 255-277
  - 279-284
  - 286-291
  - 297-302
  - 309-319
  - 321-326
  - 328-333
  - 335-340
  - 345-350
  - 353-363
  - 365-409
- file: crates/gcode/src/index/import_resolution/context/apple.rs
  ranges:
  - 8-12
  - 14-110
  - 112-123
  - 125-149
  - 151-169
  - 171-187
  - 189-196
  - 203-225
  - 232-274
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
  ranges:
  - 6-9
  - 12-15
  - 22-29
  - 32-38
  - 40-46
  - 48-50
  - 54-90
  - 93-96
  - 99-102
  - 105-108
- file: crates/gcode/src/index/import_resolution/context/elixir.rs
  ranges:
  - 13-49
  - 55-111
  - 113-124
  - 126-149
  - 151-156
  - 158-164
- file: crates/gcode/src/index/import_resolution/context/jvm.rs
  ranges:
  - 10-17
  - 19-79
  - 87-145
  - 152-218
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
  ranges:
  - 4-38
  - 40-49
  - 51-60
  - 66-97
  - 99-102
  - 104-130
  - 132-172
  - 174-185
  - 187-197
  - 199-201
  - 203-224
  - 226-234
  - 242-244
  - 247-249
  - 252-270
- file: crates/gcode/src/index/import_resolution/context/python.rs
  ranges:
  - 4-15
  - 22-32
  - 34-63
  - 70-80
  - 83-90
- file: crates/gcode/src/index/import_resolution/context/scripting.rs
  ranges:
  - 11-55
  - 57-66
  - 68-77
  - 79-84
  - 86-150
  - 152-218
- file: crates/gcode/src/index/import_resolution/helpers.rs
  ranges:
  - 3-5
  - 7-13
  - 15-19
  - 21-49
  - 51-88
  - 90-99
  - 101-107
  - 109-136
  - 138-166
  - 169-174
  - 177-183
  - 189-196
  - 199-214
  - 216-305
  - 307-309
  - 311-318
  - 320-332
  - 341-362
  - 368-381
  - 383-385
  - 387-389
  - 391-403
- file: crates/gcode/src/index/import_resolution/js_local.rs
  ranges:
  - 7-24
  - 26-69
  - 71-84
  - 86-99
  - 101-115
  - 117-124
  - 126-134
  - 140-142
  - 145-150
  - 153-156
  - 159-162
  - 165-169
  - 172-174
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
  ranges:
  - 12-40
  - 42-96
  - 98-125
  - 127-162
  - 164-229
  - 236-247
  - 250-260
- file: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
  ranges:
  - 9-91
  - 93-169
  - 171-173
  - 175-188
- file: crates/gcode/src/index/import_resolution/parser/lua.rs
  ranges:
  - 6-44
  - 46-68
  - 70-85
  - 87-111
  - 113-128
  - 130-137
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
  ranges:
  - 40-69
  - 71-89
  - 91-141
  - 143-218
  - 220-233
  - 235-254
  - 265-291
  - 302-323
  - 334-351
  - 360-384
  - 402-439
  - 441-453
  - 469-507
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
  ranges:
  - 9-16
  - 18-61
  - 64-68
  - 70-136
  - 138-189
  - 199-226
  - 228-247
  - 249-262
  - 264-270
  - 272-292
- file: crates/gcode/src/index/import_resolution/parser/python_js.rs
  ranges:
  - 14-123
  - 125-155
  - 157-252
  - 254-319
- file: crates/gcode/src/index/import_resolution/parser/rest.rs
  ranges:
  - 10-54
  - 56-92
  - 94-152
  - 154-233
- file: crates/gcode/src/index/import_resolution/parser/scala.rs
  ranges:
  - 6-23
  - 25-57
  - 59-103
  - 105-112
  - 114-131
  - 133-145
  - 147-155
- file: crates/gcode/src/index/import_resolution/parser/shell.rs
  ranges:
  - 8-40
  - 42-57
  - 59-78
  - 80-96
- file: crates/gcode/src/index/import_resolution/predicates.rs
  ranges:
  - 8-21
  - 23-53
  - 55-68
  - 70-77
  - 79-81
  - 83-88
  - 94-107
  - 109-179
  - 185-201
  - 203-210
  - 212-220
  - 222-231
  - 233-241
  - 243-251
  - 258-262
  - 264-276
  - 284-288
  - 290-302
  - 304-316
  - 318-328
- file: crates/gcode/src/index/import_resolution/rust_local.rs
  ranges:
  - 5-9
  - 12-15
  - 23-33
  - 35-55
  - 57-73
  - 75-93
  - 95-111
  - 113-123
  - 125-129
  - 131-136
  - 143-151
  - 154-159
  - 162-178
  - 181-194
  - 197-205
  - 208-216
- file: crates/gcode/src/index/parser/calls.rs
  ranges:
  - 26-35
  - 38-45
  - 47-61
  - 63-443
  - 445-464
- file: crates/gcode/src/index/parser/calls/ast.rs
  ranges:
  - 17-103
  - 105-135
  - 148-179
  - 181-193
  - 196-205
  - 208-217
  - 220-235
  - 238-252
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
  ranges:
  - 8-55
  - 57-77
  - 79-168
  - 170-172
  - 174-189
  - 191-216
  - 218-223
  - 226-232
  - 235-237
  - 239-243
  - 247-252
  - 255-259
  - 262-362
  - 364-366
  - 368-370
  - 373-375
  - 377-379
  - 381-391
  - 393-417
  - 419-441
  - 443-492
- file: crates/gcode/src/index/parser/calls/objc_ast.rs
  ranges:
  - 16-119
  - 121-140
  - 142-150
  - 152-169
  - 171-181
  - 183-189
  - 191-197
- file: crates/gcode/src/index/parser/calls/resolution.rs
  ranges:
  - 6-10
  - 17-21
  - 23-46
  - 48-62
  - 64-66
  - 68-96
  - 98-112
  - 114-122
  - 124-145
  - 147-202
  - 204-209
  - 211-222
  - 224-229
  - 239-285
- file: crates/gcode/src/index/parser/calls/shadowing.rs
  ranges:
  - 6-23
  - 25-43
  - 45-84
  - 86-96
  - 98-113
  - 115-129
  - 131-153
  - 155-218
  - 220-224
  - 226-235
  - 237-260
  - 262-273
  - 283-299
  - 302-315
  - 318-327
  - 330-339
  - 342-351
  - 354-363
- file: crates/gcode/src/index/parser/calls/text.rs
  ranges:
  - 4-20
  - 22-30
  - 32-49
  - 51-53
  - 55-57
  - 59-61
  - 63-65
  - 67-153
  - 160-165
  - 168-174
provenance_truncated: 5
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2-17](crates/gcode/assets/import_roots/elixir_dependency_roots.json#L2-L17)
- [crates/gcode/assets/import_roots/ruby_require_roots.json:2-11](crates/gcode/assets/import_roots/ruby_require_roots.json#L2-L11)
- [crates/gcode/src/index/import_resolution/context.rs:41-138](crates/gcode/src/index/import_resolution/context.rs#L41-L138), [crates/gcode/src/index/import_resolution/context.rs:144-146](crates/gcode/src/index/import_resolution/context.rs#L144-L146), [crates/gcode/src/index/import_resolution/context.rs:151-166](crates/gcode/src/index/import_resolution/context.rs#L151-L166), [crates/gcode/src/index/import_resolution/context.rs:170-187](crates/gcode/src/index/import_resolution/context.rs#L170-L187), [crates/gcode/src/index/import_resolution/context.rs:194-206](crates/gcode/src/index/import_resolution/context.rs#L194-L206), [crates/gcode/src/index/import_resolution/context.rs:212-214](crates/gcode/src/index/import_resolution/context.rs#L212-L214), [crates/gcode/src/index/import_resolution/context.rs:220-225](crates/gcode/src/index/import_resolution/context.rs#L220-L225), [crates/gcode/src/index/import_resolution/context.rs:231-236](crates/gcode/src/index/import_resolution/context.rs#L231-L236), [crates/gcode/src/index/import_resolution/context.rs:241-246](crates/gcode/src/index/import_resolution/context.rs#L241-L246), [crates/gcode/src/index/import_resolution/context.rs:248-253](crates/gcode/src/index/import_resolution/context.rs#L248-L253), [crates/gcode/src/index/import_resolution/context.rs:255-277](crates/gcode/src/index/import_resolution/context.rs#L255-L277), [crates/gcode/src/index/import_resolution/context.rs:279-284](crates/gcode/src/index/import_resolution/context.rs#L279-L284), [crates/gcode/src/index/import_resolution/context.rs:286-291](crates/gcode/src/index/import_resolution/context.rs#L286-L291), [crates/gcode/src/index/import_resolution/context.rs:297-302](crates/gcode/src/index/import_resolution/context.rs#L297-L302), [crates/gcode/src/index/import_resolution/context.rs:309-319](crates/gcode/src/index/import_resolution/context.rs#L309-L319), [crates/gcode/src/index/import_resolution/context.rs:321-326](crates/gcode/src/index/import_resolution/context.rs#L321-L326), [crates/gcode/src/index/import_resolution/context.rs:328-333](crates/gcode/src/index/import_resolution/context.rs#L328-L333), [crates/gcode/src/index/import_resolution/context.rs:335-340](crates/gcode/src/index/import_resolution/context.rs#L335-L340), [crates/gcode/src/index/import_resolution/context.rs:345-350](crates/gcode/src/index/import_resolution/context.rs#L345-L350), [crates/gcode/src/index/import_resolution/context.rs:353-363](crates/gcode/src/index/import_resolution/context.rs#L353-L363), [crates/gcode/src/index/import_resolution/context.rs:365-409](crates/gcode/src/index/import_resolution/context.rs#L365-L409)
- [crates/gcode/src/index/import_resolution/context/apple.rs:8-12](crates/gcode/src/index/import_resolution/context/apple.rs#L8-L12), [crates/gcode/src/index/import_resolution/context/apple.rs:14-110](crates/gcode/src/index/import_resolution/context/apple.rs#L14-L110), [crates/gcode/src/index/import_resolution/context/apple.rs:112-123](crates/gcode/src/index/import_resolution/context/apple.rs#L112-L123), [crates/gcode/src/index/import_resolution/context/apple.rs:125-149](crates/gcode/src/index/import_resolution/context/apple.rs#L125-L149), [crates/gcode/src/index/import_resolution/context/apple.rs:151-169](crates/gcode/src/index/import_resolution/context/apple.rs#L151-L169), [crates/gcode/src/index/import_resolution/context/apple.rs:171-187](crates/gcode/src/index/import_resolution/context/apple.rs#L171-L187), [crates/gcode/src/index/import_resolution/context/apple.rs:189-196](crates/gcode/src/index/import_resolution/context/apple.rs#L189-L196), [crates/gcode/src/index/import_resolution/context/apple.rs:203-225](crates/gcode/src/index/import_resolution/context/apple.rs#L203-L225), [crates/gcode/src/index/import_resolution/context/apple.rs:232-274](crates/gcode/src/index/import_resolution/context/apple.rs#L232-L274)
- [crates/gcode/src/index/import_resolution/context/bindings.rs:6-9](crates/gcode/src/index/import_resolution/context/bindings.rs#L6-L9), [crates/gcode/src/index/import_resolution/context/bindings.rs:12-15](crates/gcode/src/index/import_resolution/context/bindings.rs#L12-L15), [crates/gcode/src/index/import_resolution/context/bindings.rs:22-29](crates/gcode/src/index/import_resolution/context/bindings.rs#L22-L29), [crates/gcode/src/index/import_resolution/context/bindings.rs:32-38](crates/gcode/src/index/import_resolution/context/bindings.rs#L32-L38), [crates/gcode/src/index/import_resolution/context/bindings.rs:40-46](crates/gcode/src/index/import_resolution/context/bindings.rs#L40-L46), [crates/gcode/src/index/import_resolution/context/bindings.rs:48-50](crates/gcode/src/index/import_resolution/context/bindings.rs#L48-L50), [crates/gcode/src/index/import_resolution/context/bindings.rs:54-90](crates/gcode/src/index/import_resolution/context/bindings.rs#L54-L90), [crates/gcode/src/index/import_resolution/context/bindings.rs:93-96](crates/gcode/src/index/import_resolution/context/bindings.rs#L93-L96), [crates/gcode/src/index/import_resolution/context/bindings.rs:99-102](crates/gcode/src/index/import_resolution/context/bindings.rs#L99-L102), [crates/gcode/src/index/import_resolution/context/bindings.rs:105-108](crates/gcode/src/index/import_resolution/context/bindings.rs#L105-L108)
- [crates/gcode/src/index/import_resolution/context/elixir.rs:13-49](crates/gcode/src/index/import_resolution/context/elixir.rs#L13-L49), [crates/gcode/src/index/import_resolution/context/elixir.rs:55-111](crates/gcode/src/index/import_resolution/context/elixir.rs#L55-L111), [crates/gcode/src/index/import_resolution/context/elixir.rs:113-124](crates/gcode/src/index/import_resolution/context/elixir.rs#L113-L124), [crates/gcode/src/index/import_resolution/context/elixir.rs:126-149](crates/gcode/src/index/import_resolution/context/elixir.rs#L126-L149), [crates/gcode/src/index/import_resolution/context/elixir.rs:151-156](crates/gcode/src/index/import_resolution/context/elixir.rs#L151-L156), [crates/gcode/src/index/import_resolution/context/elixir.rs:158-164](crates/gcode/src/index/import_resolution/context/elixir.rs#L158-L164)
- [crates/gcode/src/index/import_resolution/context/jvm.rs:10-17](crates/gcode/src/index/import_resolution/context/jvm.rs#L10-L17), [crates/gcode/src/index/import_resolution/context/jvm.rs:19-79](crates/gcode/src/index/import_resolution/context/jvm.rs#L19-L79), [crates/gcode/src/index/import_resolution/context/jvm.rs:87-145](crates/gcode/src/index/import_resolution/context/jvm.rs#L87-L145), [crates/gcode/src/index/import_resolution/context/jvm.rs:152-218](crates/gcode/src/index/import_resolution/context/jvm.rs#L152-L218)
- [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L4-L38), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:40-49](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L40-L49), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:51-60](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L51-L60), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L66-L97), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:99-102](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L99-L102), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:104-130](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L104-L130), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:132-172](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L132-L172), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:174-185](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L174-L185), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:187-197](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L187-L197), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:199-201](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L199-L201), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:203-224](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L203-L224), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:226-234](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L226-L234), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:242-244](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L242-L244), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:247-249](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L247-L249), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:252-270](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L252-L270)
- [crates/gcode/src/index/import_resolution/context/python.rs:4-15](crates/gcode/src/index/import_resolution/context/python.rs#L4-L15), [crates/gcode/src/index/import_resolution/context/python.rs:22-32](crates/gcode/src/index/import_resolution/context/python.rs#L22-L32), [crates/gcode/src/index/import_resolution/context/python.rs:34-63](crates/gcode/src/index/import_resolution/context/python.rs#L34-L63), [crates/gcode/src/index/import_resolution/context/python.rs:70-80](crates/gcode/src/index/import_resolution/context/python.rs#L70-L80), [crates/gcode/src/index/import_resolution/context/python.rs:83-90](crates/gcode/src/index/import_resolution/context/python.rs#L83-L90)
- [crates/gcode/src/index/import_resolution/context/scripting.rs:11-55](crates/gcode/src/index/import_resolution/context/scripting.rs#L11-L55), [crates/gcode/src/index/import_resolution/context/scripting.rs:57-66](crates/gcode/src/index/import_resolution/context/scripting.rs#L57-L66), [crates/gcode/src/index/import_resolution/context/scripting.rs:68-77](crates/gcode/src/index/import_resolution/context/scripting.rs#L68-L77), [crates/gcode/src/index/import_resolution/context/scripting.rs:79-84](crates/gcode/src/index/import_resolution/context/scripting.rs#L79-L84), [crates/gcode/src/index/import_resolution/context/scripting.rs:86-150](crates/gcode/src/index/import_resolution/context/scripting.rs#L86-L150), [crates/gcode/src/index/import_resolution/context/scripting.rs:152-218](crates/gcode/src/index/import_resolution/context/scripting.rs#L152-L218)
- [crates/gcode/src/index/import_resolution/helpers.rs:3-5](crates/gcode/src/index/import_resolution/helpers.rs#L3-L5), [crates/gcode/src/index/import_resolution/helpers.rs:7-13](crates/gcode/src/index/import_resolution/helpers.rs#L7-L13), [crates/gcode/src/index/import_resolution/helpers.rs:15-19](crates/gcode/src/index/import_resolution/helpers.rs#L15-L19), [crates/gcode/src/index/import_resolution/helpers.rs:21-49](crates/gcode/src/index/import_resolution/helpers.rs#L21-L49), [crates/gcode/src/index/import_resolution/helpers.rs:51-88](crates/gcode/src/index/import_resolution/helpers.rs#L51-L88), [crates/gcode/src/index/import_resolution/helpers.rs:90-99](crates/gcode/src/index/import_resolution/helpers.rs#L90-L99), [crates/gcode/src/index/import_resolution/helpers.rs:101-107](crates/gcode/src/index/import_resolution/helpers.rs#L101-L107), [crates/gcode/src/index/import_resolution/helpers.rs:109-136](crates/gcode/src/index/import_resolution/helpers.rs#L109-L136), [crates/gcode/src/index/import_resolution/helpers.rs:138-166](crates/gcode/src/index/import_resolution/helpers.rs#L138-L166), [crates/gcode/src/index/import_resolution/helpers.rs:169-174](crates/gcode/src/index/import_resolution/helpers.rs#L169-L174), [crates/gcode/src/index/import_resolution/helpers.rs:177-183](crates/gcode/src/index/import_resolution/helpers.rs#L177-L183), [crates/gcode/src/index/import_resolution/helpers.rs:189-196](crates/gcode/src/index/import_resolution/helpers.rs#L189-L196), [crates/gcode/src/index/import_resolution/helpers.rs:199-214](crates/gcode/src/index/import_resolution/helpers.rs#L199-L214), [crates/gcode/src/index/import_resolution/helpers.rs:216-305](crates/gcode/src/index/import_resolution/helpers.rs#L216-L305), [crates/gcode/src/index/import_resolution/helpers.rs:307-309](crates/gcode/src/index/import_resolution/helpers.rs#L307-L309), [crates/gcode/src/index/import_resolution/helpers.rs:311-318](crates/gcode/src/index/import_resolution/helpers.rs#L311-L318), [crates/gcode/src/index/import_resolution/helpers.rs:320-332](crates/gcode/src/index/import_resolution/helpers.rs#L320-L332), [crates/gcode/src/index/import_resolution/helpers.rs:341-362](crates/gcode/src/index/import_resolution/helpers.rs#L341-L362), [crates/gcode/src/index/import_resolution/helpers.rs:368-381](crates/gcode/src/index/import_resolution/helpers.rs#L368-L381), [crates/gcode/src/index/import_resolution/helpers.rs:383-385](crates/gcode/src/index/import_resolution/helpers.rs#L383-L385), [crates/gcode/src/index/import_resolution/helpers.rs:387-389](crates/gcode/src/index/import_resolution/helpers.rs#L387-L389), [crates/gcode/src/index/import_resolution/helpers.rs:391-403](crates/gcode/src/index/import_resolution/helpers.rs#L391-L403)
- [crates/gcode/src/index/import_resolution/js_local.rs:7-24](crates/gcode/src/index/import_resolution/js_local.rs#L7-L24), [crates/gcode/src/index/import_resolution/js_local.rs:26-69](crates/gcode/src/index/import_resolution/js_local.rs#L26-L69), [crates/gcode/src/index/import_resolution/js_local.rs:71-84](crates/gcode/src/index/import_resolution/js_local.rs#L71-L84), [crates/gcode/src/index/import_resolution/js_local.rs:86-99](crates/gcode/src/index/import_resolution/js_local.rs#L86-L99), [crates/gcode/src/index/import_resolution/js_local.rs:101-115](crates/gcode/src/index/import_resolution/js_local.rs#L101-L115), [crates/gcode/src/index/import_resolution/js_local.rs:117-124](crates/gcode/src/index/import_resolution/js_local.rs#L117-L124), [crates/gcode/src/index/import_resolution/js_local.rs:126-134](crates/gcode/src/index/import_resolution/js_local.rs#L126-L134), [crates/gcode/src/index/import_resolution/js_local.rs:140-142](crates/gcode/src/index/import_resolution/js_local.rs#L140-L142), [crates/gcode/src/index/import_resolution/js_local.rs:145-150](crates/gcode/src/index/import_resolution/js_local.rs#L145-L150), [crates/gcode/src/index/import_resolution/js_local.rs:153-156](crates/gcode/src/index/import_resolution/js_local.rs#L153-L156), [crates/gcode/src/index/import_resolution/js_local.rs:159-162](crates/gcode/src/index/import_resolution/js_local.rs#L159-L162), [crates/gcode/src/index/import_resolution/js_local.rs:165-169](crates/gcode/src/index/import_resolution/js_local.rs#L165-L169), [crates/gcode/src/index/import_resolution/js_local.rs:172-174](crates/gcode/src/index/import_resolution/js_local.rs#L172-L174)
- [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L12-L40), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-96](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L42-L96), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L98-L125), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:127-162](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L127-L162), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:164-229](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L164-L229), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:236-247](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L236-L247), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:250-260](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L250-L260)
- [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L9-L91), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L93-L169), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:171-173](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L171-L173), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:175-188](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L175-L188)
- [crates/gcode/src/index/import_resolution/parser/lua.rs:6-44](crates/gcode/src/index/import_resolution/parser/lua.rs#L6-L44), [crates/gcode/src/index/import_resolution/parser/lua.rs:46-68](crates/gcode/src/index/import_resolution/parser/lua.rs#L46-L68), [crates/gcode/src/index/import_resolution/parser/lua.rs:70-85](crates/gcode/src/index/import_resolution/parser/lua.rs#L70-L85), [crates/gcode/src/index/import_resolution/parser/lua.rs:87-111](crates/gcode/src/index/import_resolution/parser/lua.rs#L87-L111), [crates/gcode/src/index/import_resolution/parser/lua.rs:113-128](crates/gcode/src/index/import_resolution/parser/lua.rs#L113-L128), [crates/gcode/src/index/import_resolution/parser/lua.rs:130-137](crates/gcode/src/index/import_resolution/parser/lua.rs#L130-L137)
- [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69](crates/gcode/src/index/import_resolution/parser/mod.rs#L40-L69), [crates/gcode/src/index/import_resolution/parser/mod.rs:71-89](crates/gcode/src/index/import_resolution/parser/mod.rs#L71-L89), [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141](crates/gcode/src/index/import_resolution/parser/mod.rs#L91-L141), [crates/gcode/src/index/import_resolution/parser/mod.rs:143-218](crates/gcode/src/index/import_resolution/parser/mod.rs#L143-L218), [crates/gcode/src/index/import_resolution/parser/mod.rs:220-233](crates/gcode/src/index/import_resolution/parser/mod.rs#L220-L233), [crates/gcode/src/index/import_resolution/parser/mod.rs:235-254](crates/gcode/src/index/import_resolution/parser/mod.rs#L235-L254), [crates/gcode/src/index/import_resolution/parser/mod.rs:265-291](crates/gcode/src/index/import_resolution/parser/mod.rs#L265-L291), [crates/gcode/src/index/import_resolution/parser/mod.rs:302-323](crates/gcode/src/index/import_resolution/parser/mod.rs#L302-L323), [crates/gcode/src/index/import_resolution/parser/mod.rs:334-351](crates/gcode/src/index/import_resolution/parser/mod.rs#L334-L351), [crates/gcode/src/index/import_resolution/parser/mod.rs:360-384](crates/gcode/src/index/import_resolution/parser/mod.rs#L360-L384), [crates/gcode/src/index/import_resolution/parser/mod.rs:402-439](crates/gcode/src/index/import_resolution/parser/mod.rs#L402-L439), [crates/gcode/src/index/import_resolution/parser/mod.rs:441-453](crates/gcode/src/index/import_resolution/parser/mod.rs#L441-L453), [crates/gcode/src/index/import_resolution/parser/mod.rs:469-507](crates/gcode/src/index/import_resolution/parser/mod.rs#L469-L507)
- [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L9-L16), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L18-L61), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-68](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L64-L68), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L70-L136), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:138-189](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L138-L189), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:199-226](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L199-L226), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:228-247](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L228-L247), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:249-262](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L249-L262), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:264-270](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L264-L270), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:272-292](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L272-L292)
- [crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123](crates/gcode/src/index/import_resolution/parser/python_js.rs#L14-L123), [crates/gcode/src/index/import_resolution/parser/python_js.rs:125-155](crates/gcode/src/index/import_resolution/parser/python_js.rs#L125-L155), [crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252](crates/gcode/src/index/import_resolution/parser/python_js.rs#L157-L252), [crates/gcode/src/index/import_resolution/parser/python_js.rs:254-319](crates/gcode/src/index/import_resolution/parser/python_js.rs#L254-L319)
- [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54](crates/gcode/src/index/import_resolution/parser/rest.rs#L10-L54), [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92](crates/gcode/src/index/import_resolution/parser/rest.rs#L56-L92), [crates/gcode/src/index/import_resolution/parser/rest.rs:94-152](crates/gcode/src/index/import_resolution/parser/rest.rs#L94-L152), [crates/gcode/src/index/import_resolution/parser/rest.rs:154-233](crates/gcode/src/index/import_resolution/parser/rest.rs#L154-L233)
- [crates/gcode/src/index/import_resolution/parser/scala.rs:6-23](crates/gcode/src/index/import_resolution/parser/scala.rs#L6-L23), [crates/gcode/src/index/import_resolution/parser/scala.rs:25-57](crates/gcode/src/index/import_resolution/parser/scala.rs#L25-L57), [crates/gcode/src/index/import_resolution/parser/scala.rs:59-103](crates/gcode/src/index/import_resolution/parser/scala.rs#L59-L103), [crates/gcode/src/index/import_resolution/parser/scala.rs:105-112](crates/gcode/src/index/import_resolution/parser/scala.rs#L105-L112), [crates/gcode/src/index/import_resolution/parser/scala.rs:114-131](crates/gcode/src/index/import_resolution/parser/scala.rs#L114-L131), [crates/gcode/src/index/import_resolution/parser/scala.rs:133-145](crates/gcode/src/index/import_resolution/parser/scala.rs#L133-L145), [crates/gcode/src/index/import_resolution/parser/scala.rs:147-155](crates/gcode/src/index/import_resolution/parser/scala.rs#L147-L155)
- [crates/gcode/src/index/import_resolution/parser/shell.rs:8-40](crates/gcode/src/index/import_resolution/parser/shell.rs#L8-L40), [crates/gcode/src/index/import_resolution/parser/shell.rs:42-57](crates/gcode/src/index/import_resolution/parser/shell.rs#L42-L57), [crates/gcode/src/index/import_resolution/parser/shell.rs:59-78](crates/gcode/src/index/import_resolution/parser/shell.rs#L59-L78), [crates/gcode/src/index/import_resolution/parser/shell.rs:80-96](crates/gcode/src/index/import_resolution/parser/shell.rs#L80-L96)
- [crates/gcode/src/index/import_resolution/predicates.rs:8-21](crates/gcode/src/index/import_resolution/predicates.rs#L8-L21), [crates/gcode/src/index/import_resolution/predicates.rs:23-53](crates/gcode/src/index/import_resolution/predicates.rs#L23-L53), [crates/gcode/src/index/import_resolution/predicates.rs:55-68](crates/gcode/src/index/import_resolution/predicates.rs#L55-L68), [crates/gcode/src/index/import_resolution/predicates.rs:70-77](crates/gcode/src/index/import_resolution/predicates.rs#L70-L77), [crates/gcode/src/index/import_resolution/predicates.rs:79-81](crates/gcode/src/index/import_resolution/predicates.rs#L79-L81), [crates/gcode/src/index/import_resolution/predicates.rs:83-88](crates/gcode/src/index/import_resolution/predicates.rs#L83-L88), [crates/gcode/src/index/import_resolution/predicates.rs:94-107](crates/gcode/src/index/import_resolution/predicates.rs#L94-L107), [crates/gcode/src/index/import_resolution/predicates.rs:109-179](crates/gcode/src/index/import_resolution/predicates.rs#L109-L179), [crates/gcode/src/index/import_resolution/predicates.rs:185-201](crates/gcode/src/index/import_resolution/predicates.rs#L185-L201), [crates/gcode/src/index/import_resolution/predicates.rs:203-210](crates/gcode/src/index/import_resolution/predicates.rs#L203-L210), [crates/gcode/src/index/import_resolution/predicates.rs:212-220](crates/gcode/src/index/import_resolution/predicates.rs#L212-L220), [crates/gcode/src/index/import_resolution/predicates.rs:222-231](crates/gcode/src/index/import_resolution/predicates.rs#L222-L231), [crates/gcode/src/index/import_resolution/predicates.rs:233-241](crates/gcode/src/index/import_resolution/predicates.rs#L233-L241), [crates/gcode/src/index/import_resolution/predicates.rs:243-251](crates/gcode/src/index/import_resolution/predicates.rs#L243-L251), [crates/gcode/src/index/import_resolution/predicates.rs:258-262](crates/gcode/src/index/import_resolution/predicates.rs#L258-L262), [crates/gcode/src/index/import_resolution/predicates.rs:264-276](crates/gcode/src/index/import_resolution/predicates.rs#L264-L276), [crates/gcode/src/index/import_resolution/predicates.rs:284-288](crates/gcode/src/index/import_resolution/predicates.rs#L284-L288), [crates/gcode/src/index/import_resolution/predicates.rs:290-302](crates/gcode/src/index/import_resolution/predicates.rs#L290-L302), [crates/gcode/src/index/import_resolution/predicates.rs:304-316](crates/gcode/src/index/import_resolution/predicates.rs#L304-L316), [crates/gcode/src/index/import_resolution/predicates.rs:318-328](crates/gcode/src/index/import_resolution/predicates.rs#L318-L328)
- [crates/gcode/src/index/import_resolution/rust_local.rs:5-9](crates/gcode/src/index/import_resolution/rust_local.rs#L5-L9), [crates/gcode/src/index/import_resolution/rust_local.rs:12-15](crates/gcode/src/index/import_resolution/rust_local.rs#L12-L15), [crates/gcode/src/index/import_resolution/rust_local.rs:23-33](crates/gcode/src/index/import_resolution/rust_local.rs#L23-L33), [crates/gcode/src/index/import_resolution/rust_local.rs:35-55](crates/gcode/src/index/import_resolution/rust_local.rs#L35-L55), [crates/gcode/src/index/import_resolution/rust_local.rs:57-73](crates/gcode/src/index/import_resolution/rust_local.rs#L57-L73), [crates/gcode/src/index/import_resolution/rust_local.rs:75-93](crates/gcode/src/index/import_resolution/rust_local.rs#L75-L93), [crates/gcode/src/index/import_resolution/rust_local.rs:95-111](crates/gcode/src/index/import_resolution/rust_local.rs#L95-L111), [crates/gcode/src/index/import_resolution/rust_local.rs:113-123](crates/gcode/src/index/import_resolution/rust_local.rs#L113-L123), [crates/gcode/src/index/import_resolution/rust_local.rs:125-129](crates/gcode/src/index/import_resolution/rust_local.rs#L125-L129), [crates/gcode/src/index/import_resolution/rust_local.rs:131-136](crates/gcode/src/index/import_resolution/rust_local.rs#L131-L136), [crates/gcode/src/index/import_resolution/rust_local.rs:143-151](crates/gcode/src/index/import_resolution/rust_local.rs#L143-L151), [crates/gcode/src/index/import_resolution/rust_local.rs:154-159](crates/gcode/src/index/import_resolution/rust_local.rs#L154-L159), [crates/gcode/src/index/import_resolution/rust_local.rs:162-178](crates/gcode/src/index/import_resolution/rust_local.rs#L162-L178), [crates/gcode/src/index/import_resolution/rust_local.rs:181-194](crates/gcode/src/index/import_resolution/rust_local.rs#L181-L194), [crates/gcode/src/index/import_resolution/rust_local.rs:197-205](crates/gcode/src/index/import_resolution/rust_local.rs#L197-L205), [crates/gcode/src/index/import_resolution/rust_local.rs:208-216](crates/gcode/src/index/import_resolution/rust_local.rs#L208-L216)
- [crates/gcode/src/index/parser/calls.rs:26-35](crates/gcode/src/index/parser/calls.rs#L26-L35), [crates/gcode/src/index/parser/calls.rs:38-45](crates/gcode/src/index/parser/calls.rs#L38-L45), [crates/gcode/src/index/parser/calls.rs:47-61](crates/gcode/src/index/parser/calls.rs#L47-L61), [crates/gcode/src/index/parser/calls.rs:63-443](crates/gcode/src/index/parser/calls.rs#L63-L443), [crates/gcode/src/index/parser/calls.rs:445-464](crates/gcode/src/index/parser/calls.rs#L445-L464)
- [crates/gcode/src/index/parser/calls/ast.rs:17-103](crates/gcode/src/index/parser/calls/ast.rs#L17-L103), [crates/gcode/src/index/parser/calls/ast.rs:105-135](crates/gcode/src/index/parser/calls/ast.rs#L105-L135), [crates/gcode/src/index/parser/calls/ast.rs:148-179](crates/gcode/src/index/parser/calls/ast.rs#L148-L179), [crates/gcode/src/index/parser/calls/ast.rs:181-193](crates/gcode/src/index/parser/calls/ast.rs#L181-L193), [crates/gcode/src/index/parser/calls/ast.rs:196-205](crates/gcode/src/index/parser/calls/ast.rs#L196-L205), [crates/gcode/src/index/parser/calls/ast.rs:208-217](crates/gcode/src/index/parser/calls/ast.rs#L208-L217), [crates/gcode/src/index/parser/calls/ast.rs:220-235](crates/gcode/src/index/parser/calls/ast.rs#L220-L235), [crates/gcode/src/index/parser/calls/ast.rs:238-252](crates/gcode/src/index/parser/calls/ast.rs#L238-L252)
- [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55](crates/gcode/src/index/parser/calls/dart_textual.rs#L8-L55), [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77](crates/gcode/src/index/parser/calls/dart_textual.rs#L57-L77), [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168](crates/gcode/src/index/parser/calls/dart_textual.rs#L79-L168), [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172](crates/gcode/src/index/parser/calls/dart_textual.rs#L170-L172), [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189](crates/gcode/src/index/parser/calls/dart_textual.rs#L174-L189), [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216](crates/gcode/src/index/parser/calls/dart_textual.rs#L191-L216), [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223](crates/gcode/src/index/parser/calls/dart_textual.rs#L218-L223), [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232](crates/gcode/src/index/parser/calls/dart_textual.rs#L226-L232), [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237](crates/gcode/src/index/parser/calls/dart_textual.rs#L235-L237), [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243](crates/gcode/src/index/parser/calls/dart_textual.rs#L239-L243), [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252](crates/gcode/src/index/parser/calls/dart_textual.rs#L247-L252), [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259](crates/gcode/src/index/parser/calls/dart_textual.rs#L255-L259), [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362](crates/gcode/src/index/parser/calls/dart_textual.rs#L262-L362), [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366](crates/gcode/src/index/parser/calls/dart_textual.rs#L364-L366), [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370](crates/gcode/src/index/parser/calls/dart_textual.rs#L368-L370), [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375](crates/gcode/src/index/parser/calls/dart_textual.rs#L373-L375), [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379](crates/gcode/src/index/parser/calls/dart_textual.rs#L377-L379), [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391](crates/gcode/src/index/parser/calls/dart_textual.rs#L381-L391), [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417](crates/gcode/src/index/parser/calls/dart_textual.rs#L393-L417), [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441](crates/gcode/src/index/parser/calls/dart_textual.rs#L419-L441), [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492](crates/gcode/src/index/parser/calls/dart_textual.rs#L443-L492)
- [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119](crates/gcode/src/index/parser/calls/objc_ast.rs#L16-L119), [crates/gcode/src/index/parser/calls/objc_ast.rs:121-140](crates/gcode/src/index/parser/calls/objc_ast.rs#L121-L140), [crates/gcode/src/index/parser/calls/objc_ast.rs:142-150](crates/gcode/src/index/parser/calls/objc_ast.rs#L142-L150), [crates/gcode/src/index/parser/calls/objc_ast.rs:152-169](crates/gcode/src/index/parser/calls/objc_ast.rs#L152-L169), [crates/gcode/src/index/parser/calls/objc_ast.rs:171-181](crates/gcode/src/index/parser/calls/objc_ast.rs#L171-L181), [crates/gcode/src/index/parser/calls/objc_ast.rs:183-189](crates/gcode/src/index/parser/calls/objc_ast.rs#L183-L189), [crates/gcode/src/index/parser/calls/objc_ast.rs:191-197](crates/gcode/src/index/parser/calls/objc_ast.rs#L191-L197)
- [crates/gcode/src/index/parser/calls/resolution.rs:6-10](crates/gcode/src/index/parser/calls/resolution.rs#L6-L10), [crates/gcode/src/index/parser/calls/resolution.rs:17-21](crates/gcode/src/index/parser/calls/resolution.rs#L17-L21), [crates/gcode/src/index/parser/calls/resolution.rs:23-46](crates/gcode/src/index/parser/calls/resolution.rs#L23-L46), [crates/gcode/src/index/parser/calls/resolution.rs:48-62](crates/gcode/src/index/parser/calls/resolution.rs#L48-L62), [crates/gcode/src/index/parser/calls/resolution.rs:64-66](crates/gcode/src/index/parser/calls/resolution.rs#L64-L66), [crates/gcode/src/index/parser/calls/resolution.rs:68-96](crates/gcode/src/index/parser/calls/resolution.rs#L68-L96), [crates/gcode/src/index/parser/calls/resolution.rs:98-112](crates/gcode/src/index/parser/calls/resolution.rs#L98-L112), [crates/gcode/src/index/parser/calls/resolution.rs:114-122](crates/gcode/src/index/parser/calls/resolution.rs#L114-L122), [crates/gcode/src/index/parser/calls/resolution.rs:124-145](crates/gcode/src/index/parser/calls/resolution.rs#L124-L145), [crates/gcode/src/index/parser/calls/resolution.rs:147-202](crates/gcode/src/index/parser/calls/resolution.rs#L147-L202), [crates/gcode/src/index/parser/calls/resolution.rs:204-209](crates/gcode/src/index/parser/calls/resolution.rs#L204-L209), [crates/gcode/src/index/parser/calls/resolution.rs:211-222](crates/gcode/src/index/parser/calls/resolution.rs#L211-L222), [crates/gcode/src/index/parser/calls/resolution.rs:224-229](crates/gcode/src/index/parser/calls/resolution.rs#L224-L229), [crates/gcode/src/index/parser/calls/resolution.rs:239-285](crates/gcode/src/index/parser/calls/resolution.rs#L239-L285)
- [crates/gcode/src/index/parser/calls/shadowing.rs:6-23](crates/gcode/src/index/parser/calls/shadowing.rs#L6-L23), [crates/gcode/src/index/parser/calls/shadowing.rs:25-43](crates/gcode/src/index/parser/calls/shadowing.rs#L25-L43), [crates/gcode/src/index/parser/calls/shadowing.rs:45-84](crates/gcode/src/index/parser/calls/shadowing.rs#L45-L84), [crates/gcode/src/index/parser/calls/shadowing.rs:86-96](crates/gcode/src/index/parser/calls/shadowing.rs#L86-L96), [crates/gcode/src/index/parser/calls/shadowing.rs:98-113](crates/gcode/src/index/parser/calls/shadowing.rs#L98-L113), [crates/gcode/src/index/parser/calls/shadowing.rs:115-129](crates/gcode/src/index/parser/calls/shadowing.rs#L115-L129), [crates/gcode/src/index/parser/calls/shadowing.rs:131-153](crates/gcode/src/index/parser/calls/shadowing.rs#L131-L153), [crates/gcode/src/index/parser/calls/shadowing.rs:155-218](crates/gcode/src/index/parser/calls/shadowing.rs#L155-L218), [crates/gcode/src/index/parser/calls/shadowing.rs:220-224](crates/gcode/src/index/parser/calls/shadowing.rs#L220-L224), [crates/gcode/src/index/parser/calls/shadowing.rs:226-235](crates/gcode/src/index/parser/calls/shadowing.rs#L226-L235), [crates/gcode/src/index/parser/calls/shadowing.rs:237-260](crates/gcode/src/index/parser/calls/shadowing.rs#L237-L260), [crates/gcode/src/index/parser/calls/shadowing.rs:262-273](crates/gcode/src/index/parser/calls/shadowing.rs#L262-L273), [crates/gcode/src/index/parser/calls/shadowing.rs:283-299](crates/gcode/src/index/parser/calls/shadowing.rs#L283-L299), [crates/gcode/src/index/parser/calls/shadowing.rs:302-315](crates/gcode/src/index/parser/calls/shadowing.rs#L302-L315), [crates/gcode/src/index/parser/calls/shadowing.rs:318-327](crates/gcode/src/index/parser/calls/shadowing.rs#L318-L327), [crates/gcode/src/index/parser/calls/shadowing.rs:330-339](crates/gcode/src/index/parser/calls/shadowing.rs#L330-L339), [crates/gcode/src/index/parser/calls/shadowing.rs:342-351](crates/gcode/src/index/parser/calls/shadowing.rs#L342-L351), [crates/gcode/src/index/parser/calls/shadowing.rs:354-363](crates/gcode/src/index/parser/calls/shadowing.rs#L354-L363)
- [crates/gcode/src/index/parser/calls/text.rs:4-20](crates/gcode/src/index/parser/calls/text.rs#L4-L20), [crates/gcode/src/index/parser/calls/text.rs:22-30](crates/gcode/src/index/parser/calls/text.rs#L22-L30), [crates/gcode/src/index/parser/calls/text.rs:32-49](crates/gcode/src/index/parser/calls/text.rs#L32-L49), [crates/gcode/src/index/parser/calls/text.rs:51-53](crates/gcode/src/index/parser/calls/text.rs#L51-L53), [crates/gcode/src/index/parser/calls/text.rs:55-57](crates/gcode/src/index/parser/calls/text.rs#L55-L57), [crates/gcode/src/index/parser/calls/text.rs:59-61](crates/gcode/src/index/parser/calls/text.rs#L59-L61), [crates/gcode/src/index/parser/calls/text.rs:63-65](crates/gcode/src/index/parser/calls/text.rs#L63-L65), [crates/gcode/src/index/parser/calls/text.rs:67-153](crates/gcode/src/index/parser/calls/text.rs#L67-L153), [crates/gcode/src/index/parser/calls/text.rs:160-165](crates/gcode/src/index/parser/calls/text.rs#L160-L165), [crates/gcode/src/index/parser/calls/text.rs:168-174](crates/gcode/src/index/parser/calls/text.rs#L168-L174)

_5 more source files omitted._

</details>

# Import Resolution & Syntax Parsing

## Overview

Implements language-agnostic and language-specific parsers to resolve external imports, qualified namespaces, and function call definitions.

## Reference Modules

- [[code/modules/crates/gcode/assets|crates/gcode/assets]]
- [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]]
- [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]
- [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]
- [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]
- [[code/modules/crates/gcode/src/index/parser|crates/gcode/src/index/parser]]

## Source Files

- [[code/files/crates/gcode/assets/import_roots/elixir_dependency_roots.json|crates/gcode/assets/import_roots/elixir_dependency_roots.json]]
- [[code/files/crates/gcode/assets/import_roots/ruby_require_roots.json|crates/gcode/assets/import_roots/ruby_require_roots.json]]
- [[code/files/crates/gcode/build.rs|crates/gcode/build.rs]]
