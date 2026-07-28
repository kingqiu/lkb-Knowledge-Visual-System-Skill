#!/usr/bin/env python3
"""Validate structural and red-flag rules for a 两克伴 output package.

Usage: python3 validate_output.py path/to/package.md
This is a mechanical backstop, not a substitute for source or visual review.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


HEADINGS = [
    "1. 内容诊断",
    "2. 核心观点提炼",
    "3. 卡片规划",
    "4. 图片 Prompt",
    "5. 小红书标题",
    "6. 小红书正文",
    "7. 标签",
    "8. 发布前质量检查",
]
BANNED_COPY = [
    "我的判断是",
    "笔者认为",
    "本文认为",
    "根据我的判断",
    "综上所述",
    "随着时代发展",
    "在人工智能快速发展的今天",
]
VISUAL_RED_FLAGS = [
    "AI机器人",
    "蓝色机器人",
    "赛博朋克",
    "发光大脑",
    "未来城市",
    "霓虹渐变",
    "VOL.",
    "ISSUE ",
    "Magazine No.",
    "Fake Research ID",
]


def section(text: str, title: str, next_title: str | None) -> str:
    start = re.search(rf"^#\s+{re.escape(title)}\s*$", text, re.MULTILINE)
    if not start:
        return ""
    end = (
        re.search(rf"^#\s+{re.escape(next_title)}\s*$", text[start.end():], re.MULTILINE)
        if next_title
        else None
    )
    return text[start.end(): start.end() + end.start()] if end else text[start.end():]


def chinese_chars(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 validate_output.py path/to/package.md")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"ERROR: file not found: {path}")
        return 2
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    positions = []
    for heading in HEADINGS:
        match = re.search(rf"^#\s+{re.escape(heading)}\s*$", text, re.MULTILINE)
        if not match:
            errors.append(f"missing required heading: # {heading}")
        else:
            positions.append(match.start())
    if len(positions) == len(HEADINGS) and positions != sorted(positions):
        errors.append("required headings are not in the prescribed order")

    for phrase in BANNED_COPY:
        if phrase in text:
            errors.append(f"banned writing phrase found: {phrase}")
    cards = section(text, HEADINGS[2], HEADINGS[3])
    card_numbers = re.findall(r"(?:第\s*\d+\s*张|卡片\s*\d+)", cards)
    if not card_numbers:
        card_numbers = re.findall(r"^\|\s*\d+\s*\|", cards, re.MULTILINE)
    if not card_numbers:
        card_numbers = re.findall(r"^\s*\d+[.、]\s+\*{0,2}主题", cards, re.MULTILINE)
    if not 5 <= len(card_numbers) <= 12:
        errors.append(f"card plan must enumerate 5–12 cards; found {len(card_numbers)}")
    for required in ("主题", "核心信息", "视觉方向"):
        if required not in cards:
            errors.append(f"card plan missing field: {required}")

    prompts = section(text, HEADINGS[3], HEADINGS[4])
    prompt_count = len(re.findall(r"(?:第\s*\d+\s*张|卡片\s*\d+)", prompts))
    if prompt_count != len(card_numbers):
        errors.append(f"each card needs one prompt; {len(card_numbers)} cards vs {prompt_count} prompts")
    for required in ("两克伴 AI知识档案视觉系统", "3:4", "modular grid", "Bottom right: 「两克伴」出品"):
        if required not in prompts:
            errors.append(f"image prompts missing required component: {required}")
    if not re.search(r"Color System|Color Palette|色彩系统|Technical Red|Intelligence Blue|Human Orange|Future Green", prompts):
        errors.append("image prompts missing a named Color System")
    # A prompt may correctly say “不要机器人”; evaluate visual red flags only
    # within prompts and ignore lines that express an explicit prohibition.
    positive_visual_text = "\n".join(
        line
        for line in prompts.splitlines()
        if not re.search(r"无|不要|避免|禁止|不画|不使用|不出现|\bnot\b|\bno\b", line, re.IGNORECASE)
    )
    for flag in VISUAL_RED_FLAGS:
        if flag.lower() in positive_visual_text.lower():
            errors.append(f"prohibited visual/fake-information flag found: {flag}")

    diagnosis = section(text, HEADINGS[0], HEADINGS[1])
    if not re.search(r"来源|资料|事实依据|事实基础|核验|验证|source", diagnosis, re.IGNORECASE):
        errors.append("content diagnosis lacks an evidence-source or verification-status declaration")

    titles = section(text, HEADINGS[4], HEADINGS[5])
    recommended = re.findall(r"^.*推荐标题\s*\*{0,2}\s*[：:]\s*(.+?)\s*$", titles, re.MULTILINE)
    alternatives = re.findall(r"^\s*(?:[-*]\s*)?\d+[.、]\s*(.+?)\s*$", titles, re.MULTILINE)
    if not alternatives:
        alternatives = re.findall(r"^.*备选(?:标题)?\s*\*{0,2}\s*[：:]\s*(.+?)\s*$", titles, re.MULTILINE)
    if len(recommended) != 1:
        errors.append(f"titles require exactly one 推荐标题 entry; found {len(recommended)}")
    if len(alternatives) != 4:
        errors.append(f"titles require exactly four numbered alternatives; found {len(alternatives)}")
    for title in recommended + alternatives:
        if chinese_chars(title) > 20:
            errors.append(f"title exceeds 20 Chinese characters: {title}")

    body = section(text, HEADINGS[5], HEADINGS[6])
    count = chinese_chars(body)
    if count > 1000:
        errors.append(f"body exceeds 1,000 Chinese characters ({count})")
    elif not 850 <= count <= 950:
        warnings.append(f"body is outside the preferred 850–950 Chinese characters ({count})")

    tags = re.findall(r"#[\w\u4e00-\u9fff]+", section(text, HEADINGS[6], HEADINGS[7]))
    if not 5 <= len(tags) <= 8:
        errors.append(f"tags must number 5–8; found {len(tags)}")
    qa = section(text, HEADINGS[7], None)
    qa_compact = re.sub(r"\s+", "", qa)
    for required in ("事实准确", "有明确观点", "有认知价值", "无AI套话", "无咨询报告腔", "作者声音自然", "风格统一", "配色独立", "3:4比例", "品牌完整"):
        if required not in qa_compact:
            errors.append(f"QA checklist missing: {required}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("PASS: structural rules and red-flag checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
