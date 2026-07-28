# 两克伴 AI知识档案视觉系统

## Fixed Design Language

**Name:** 两克伴 AI知识档案视觉系统

**Purpose:** convert complex knowledge into orderly, structured, collectible visual knowledge assets.

Use internationalist graphic design, Swiss Grid System, IDEA/BranD academic-editorial sensibility, information visualization, abstract symbolic systems, geometric composition, rational order, postmodern editorial tension, experimental typography, and a knowledge-archive character.

The mood is rational, calm, academic, avant-garde, restrained, intelligent, future-facing, information-dense, and made for long-term collection. This language is fixed and independent of the selected palette.

Apply the mandatory page grammar in [knowledge-archive-layout-template.md](knowledge-archive-layout-template.md) for every generated card. The template is the concrete expression of this Design Language; it overrides any generic interpretation of “editorial”, “Swiss”, or “infographic”.

## Visual subjects

Prioritize abstract symbolic expression: data structures, network topology, information nodes, system architecture, parameter matrices, abstract apparatuses, knowledge crystals, relation networks, information-flow structures, and geometric models.

| Topic | Use | Express |
| --- | --- | --- |
| Graph Engineering | nodes, edges, state layers, topology | how multiple intelligent units connect |
| Open Weights | opened model structure, parameter matrix, weight modules | model capability boundaries being opened |
| Agent Harness | control system, scheduling structure, tool interfaces, state-management modules | how an intelligent system runs reliably |

Never use real-person portraits, AI robot figures, cyberpunk, science-fiction movie scenes, generic technology illustration, glowing brains, blue robot avatars, or fake future cities. These are popular symbols, not durable 两克伴 brand symbols.

## Independent Color System

Always state both the Design Language and a Color System. Do not define the visual style by color.

Every Color System owns four visual roles: **canvas** (the page field), **ink** (headlines, rails, table headers, conclusion panel), **structure** (tables, cards, grids, secondary diagram planes), and **signal** (key nodes, decisive arrows, key words, exceptions). Do not keep a universal ivory base or universal black ink across palettes.

| Palette | Canvas | Ink | Structure | Signal | Use for |
| --- | --- | --- | --- | --- | --- |
| Technical Red / 深墨工程红 | deep ink `#171B22` | warm ivory `#F5F0EA` | technical gray `#80858B`; large ivory information planes `#F5F0EA` | precision red `#C91F2C` | infrastructure, Agent architecture, engineering systems, technical paradigm change |
| Vermilion Archive / 朱印档案 | archive ivory `#F5F1EB` | carbon black `#111317` | warm gray `#B8B8B4`; ash gray `#D5D3CF` for pixel/plane texture | vermilion `#D9251C` | AI foundations, knowledge infrastructure, research architecture, analytical frameworks, durable knowledge assets |
| Intelligence Blue | cold paper blue `#E8F0F5` | deep navy `#183247` | harbour blue `#6E96AE` | scientific blue `#276FBF` | foundation models, algorithms, research, theoretical study |
| Warm Earth Shell / 深壳暖土 | deep cocoa `#30231F` | warm ivory `#F6EBDD` | parchment planes `#E7CFB8`; brushwood `#8A5A3C` | terracotta `#C86B35`; reserve rain blue `#43718E` for an analytical relationship layer | AI and people, education, organization, career, cognition, humanistic business |
| Future Green | mist green paper `#E6EEE7` | forest ink `#25372E` | sage `#8FA997` | growth green `#3F7754` | open source, ecosystems, open platforms, communities |
| Archive Blue / 档案蓝 | ash blue-gray `#D3D9DA` | archive charcoal `#252D37` | harbour blue `#427390` | clay `#B37121`; reserve oxblood `#88150C` for risk | deep research, industry analysis, enterprise strategy, governance, risk |
| Moss Archive / 苔藓档案 | mist blue-gray `#AAB8B4` | orka black `#28241C` | boreal gray-green `#6E8175` | moss `#405740`; amber `#CC680A` for warnings | long-term ecosystems, sustainability, distributed systems, open-source strategy |
| Rose Noir / 玫红夜航 | softened solar yellow `#FFF0B1` (derived from `#FFC845`) | ink blue `#1F385A` | muted marigold `#E5BC63` | rose `#E83A6E` | creative industries, cultural trends, urban business, brand cases |

Apply the roles as a coherent visual field: canvas 45–60%, ink 20–30%, structure 15–25%, signal 5–15%. Allow the selected Ink color to form title blocks, headers, rails, and conclusion panels; allow Structure to fill tables, cards, and diagram planes. Use Signal for decisive visual contrast, not merely tiny dots. Preserve readable contrast and never deploy all colors at equal weight.

The palettes must not all use the same light-canvas / dark-ink composition. Keep four distinct luminance regimes: **light color field** (Intelligence Blue, Future Green, Archive Blue, Moss Archive), **deep shell with reverse type and pale information planes** (Technical Red, Warm Earth Shell), **high-chroma proposition field** (Rose Noir), and **monochrome research archive** (Vermilion Archive). A deep-shell palette must visibly use its dark canvas for at least 55% of the page and place its diagrams/evidence on a small number of intentional pale planes. Vermilion Archive must preserve a warm ivory canvas with black as the dominant information skeleton, use gray only for structure/texture, and keep vermilion to 5–8% of visible area: decisive terms, nodes, underlines, and state changes only. Never reduce a palette change to a pale background substitution or a few signal dots.

If the user does not specify a palette: engineering implementation, system change, or a strong technical proposition → Technical Red; AI foundations, knowledge infrastructure, research architecture, analytical framework, or durable knowledge asset → Vermilion Archive; model research → Intelligence Blue; introductory AI-and-people, education, organization, career, cognition, or humanistic business → Warm Earth Shell; open platform/community → Future Green; deep research, strategy, governance, or risk → Archive Blue; long-term ecosystem, sustainability, or distributed-system strategy → Moss Archive; creative/cultural trend or brand case → Rose Noir. Choose the more specific palette when categories overlap. Do not add further palettes unless they preserve the fixed Design Language, a limited color system, high-end editorial feeling, and avoid cheap gradients or neon.

## Layout system

Default to a 3:4 vertical Xiaohongshu card, **1080 × 1440**.

Use the knowledge-archive layout template rather than a generic cover layout. The page must retain its palette-specific canvas and ink system, heavy upper-left Chinese headline, narrow right legend rail, one dominant central technical visual, one subordinate evidence pattern, editorial texture, and a compact brand lock-up across every palette. Do not add a decorative left magazine rail. The lower-right string `「两克伴」出品` is mandatory in the image-generation prompt and must be natively typeset as part of the footer system; never append or overlay it after generation. Release only an exactly 1080 × 1440 raster.

Use asymmetric balance, modular grids, golden proportion, whitespace cuts, scale change, density gradients, layering, and clear information hierarchy. Avoid PPT layout, dense tiny text, a text-wall without a reading path, or decoration outweighing content.

## Prompt construction

Complete visual planning first. Create one standalone prompt per card. Include all six components:

1. **Visual metaphor**: transform the knowledge subject into an abstract symbol (for Graph Engineering, a dynamic knowledge network of nodes, edges, and state layers—not an AI robot).
2. **Information structure**: identify the relevant concept, comparison, system, key modules, or causal relation.
3. **Visual style**: name `两克伴 AI知识档案视觉系统`, International Typographic Style, Swiss Grid System, Academic Editorial Design, Information Visualization, and Abstract Symbolic Visualization.
4. **Color palette**: name the current Color System.
5. **Layout**: include `3:4 vertical poster`, `modular grid`, `editorial layout`, and `clear information hierarchy`.
6. **Brand requirement**: include `Bottom right: 「两克伴」出品`.

Do not request or add false information (`VOL.07`, `ISSUE 2026`, `MAY 2026`, `Magazine No.`, fake research IDs), random English, numbers, code, or symbols. All text must serve information expression. Avoid meaningless embellishment, overdone technology glow, neon gradients, and generic commercial-PPT styling.
