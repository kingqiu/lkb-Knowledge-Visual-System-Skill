---
name: lkb-knowledge-visual-system-skill
description: "Produce complete 两克伴 knowledge-archive content packages from a topic, article, research material, trend, or complex concept: diagnose the content, build a knowledge architecture, plan 5–12 Xiaohongshu cards, write per-card visual prompts, draft titles/body/tags, and run factual, authorial, readability, and visual QA. Use for AI, technology, business, product, organization, or cognition topics that need a consistent long-term 两克伴 visual identity and Xiaohongshu-ready output."
---

# 两克伴知识档案 Skill

Execute the full knowledge-asset workflow. Treat every requirement below as a release gate; do not omit a stage, collapse cards merely to reduce work, or substitute generic AI copy for an authorial judgment.

## Required reads

Read these files before producing a package:

1. [System prompt](references/system-prompt.md) — non-negotiable operating contract and workflow.
2. [Content production](references/content-production.md) — card-complexity rubric, writing rules, and Xiaohongshu requirements.
3. [Visual system](references/visual-system.md) — design language, independent color system, layout, and prompt rules.
4. [Knowledge-archive layout template](references/knowledge-archive-layout-template.md) — mandatory editorial page grammar and reference assets.
5. [Output contract and QA](references/output-contract-and-qa.md) — the exact response sequence, source handling, and release checklist.

Read [acceptance tests](references/acceptance-tests.md) only when testing, revising, or diagnosing the skill.

## Execution protocol

1. Extract the user’s topic, supplied evidence, audience, goal, and any stated color preference. If a material is supplied, distinguish its claims from your own conclusions.
2. Establish a factual basis before drafting. Verify time-sensitive or contested claims using credible primary sources where tools permit; identify uncertainty rather than inventing facts. Keep sources close to the claim they support.
3. Diagnose the topic before explaining it: find the reason it matters, the reader’s real question, the cognitive gap, and the judgment the reader will gain.
4. Build the closed-loop knowledge architecture: why it emerged → what it is → how it works → why it matters → how to judge it. Choose card count from the rubric, then assign exactly one cognitive task to every card.
5. Select the color system independently from the fixed design language. Create a visual plan before writing any image prompt. Never let color define the style.
6. Generate the complete response in the exact eight-section order in the output contract. Generate one standalone prompt per card; do not generate images unless separately asked.
7. Run every QA gate before release. Use `scripts/validate_output.py <package.md>` as a mechanical backstop after saving a draft; resolve every reported error or explicitly mark a genuinely unverifiable claim as such.

## Decision rules

- Keep professional rigor and everyday comprehension in a 50/50 balance. Explain technical terms once in plain language; retain necessary precision.
- Include fact + explanation + a natural 两克伴 viewpoint. Use natural first person such as “我觉得”“我认为”“在我看来”“我的理解是”; never use the banned authorial phrases in the content reference.
- Match title, copy, card count, visual metaphor, color, and tags to the actual topic. Do not force a template or fixed page count.
- Keep the fixed visual language: abstract symbolic knowledge visualization, Swiss grid discipline, academic editorial restraint, and a 3:4 knowledge-card format. Do not use the prohibited imagery or invented decorative information.
- If the user requests an expansion that conflicts with a core principle, preserve the core principle and explain the constraint briefly.

## Resources

- `references/`: canonical rules, prompt contract, QA gates, and acceptance cases.
- `scripts/validate_output.py`: local structural and red-flag validator; it does not prove factual accuracy or design quality, so always complete the human QA checklist.
