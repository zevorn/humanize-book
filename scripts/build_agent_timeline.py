#!/usr/bin/env python3
"""Build a high-recall, chronological Agent discussion corpus.

The output is an excerpt, not a summary: selected source lines are copied in
their original order and wording. The selection deliberately favors recall so
that a human can perform the later interpretation and analysis.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


DEFAULT_SOURCE = Path(
    "/Users/zevorn/Downloads/jing/Humanize聊天记录_完整并行OCR_去重版.md"
)
DEFAULT_OUTPUT = Path(
    "/Users/zevorn/humanize-book/materials/timeline/Agent发展史_时间序语料初筛.md"
)

# Sparse but historically important passages can be missed by density-based
# filtering. These ranges were manually selected after reading the source and
# checking the historical evidence ledger. They preserve inflection points in
# model usage, Humanize H1/H2/H3, OpenClaw/Pi, and long-running Agent practice.
MANDATORY_RANGES = [
    (60, 145),
    (186, 275),
    (615, 705),
    (789, 842),
    (949, 1305),
    (1520, 1605),
    (2440, 2630),
    (3678, 3710),
    (5700, 6030),
    (6970, 7010),
    (8990, 9175),
    (11510, 11535),
    (12820, 13020),
    (13255, 13320),
    (13960, 14315),
    (14575, 14595),
    (15290, 15330),
    (15438, 15720),
    (16790, 16835),
    (16970, 16990),
    (17524, 17570),
    (17742, 17797),
    (18295, 18410),
    (18790, 18910),
    (19090, 19200),
    (19472, 19554),
    (19880, 19981),
    (20651, 20695),
    (21886, 21935),
    (22098, 22125),
    (22423, 22436),
    (23353, 23375),
    (24737, 24920),
    (25674, 25718),
    (25994, 26012),
    (26500, 26580),
    (26875, 27015),
    (27995, 28050),
    (28715, 28835),
    (29630, 29655),
    (31195, 31235),
    (32220, 32345),
    (34690, 35095),
    (35444, 35508),
    (36555, 36587),
    (37904, 38108),
    (38238, 38290),
    (40370, 40425),
    (40620, 40640),
    (42410, 42645),
    (42888, 42920),
    (43340, 43365),
    (43770, 43830),
    (44115, 44236),
    (44525, 44620),
    (45028, 45048),
    (45700, 45745),
    (46155, 46189),
    (46650, 46765),
    (47290, 47440),
    (48276, 48294),
    (48765, 48814),
    (49830, 49920),
    (51128, 51183),
    (51943, 51975),
    (52166, 52560),
    (53013, 53050),
    (53933, 54115),
    (54420, 54475),
    (55846, 55935),
    (57440, 57590),
    (57735, 57810),
    (58269, 58305),
    (58670, 58900),
    (58894, 58966),
    (59770, 59870),
    (59908, 59940),
    (61570, 61610),
    (62235, 62265),
    (62566, 63210),
    (64473, 65024),
    (66085, 66187),
    (67657, 67693),
    (68085, 68142),
    (68200, 68225),
    (68543, 68550),
    (68605, 68615),
    (68637, 68659),
    (68773, 68819),
    (68910, 68923),
    (68947, 68975),
]


TIMESTAMP_RE = re.compile(
    r"^-\s*(?P<label>(?:[3-7]月\d{1,2}日|星期[一二三四五六日天]|昨天|今天|前天))"
    r"(?:\s*[.．]?\s*\d{1,2}[:：]\d{2})\s*$"
)

# The group title / one participant's display name contains "agent flow". It
# must not make an otherwise unrelated message look relevant.
DISPLAY_NAME_RE = re.compile(
    r"[\"“”]?开源芯片\s*agent\s*flow\s*张宇鑫[\"“”]?\s*[:：]?",
    re.IGNORECASE,
)

SYSTEM_NOTICE_RE = re.compile(
    r"邀请.*加入了?群聊|与群里其他人都不是朋友关系|撤回了.*消息|引用内容不存在"
)

STRONG_PATTERNS = [
    # Core Agent / Humanize vocabulary.
    r"agent",
    r"智能体",
    r"humanize",
    r"oh-my-humanize",
    r"\bomh\b",
    r"oh-my-pi",
    r"\bomp\b",
    r"\bh[1234]\b",
    r"harness",
    r"agentic",
    r"sub[-_ ]?agent",
    r"agent[-_ ]?teams?",
    r"teammate",
    r"swarm",
    r"ralph",
    r"superpowers",
    r"pdb[br]",
    r"\bhumz\b",
    r"\bhcc\b",
    r"\bhvm\b",
    # Flow, orchestration and isolation.
    r"workflow",
    r"worktree",
    r"orchestrat",
    r"编排",
    r"工作流",
    r"上下文",
    r"context",
    r"委派",
    r"delegate",
    r"并行",
    r"并发",
    r"隔离",
    r"小兵",
    r"分治",
    # Roles and control mechanisms.
    r"reviewer",
    r"planner",
    r"builder",
    r"monitor(?:ing)?\s+agent",
    r"memory",
    r"记忆",
    r"permission",
    r"权限",
    r"sandbox",
    r"沙箱",
    r"artifact",
    r"产物中心",
    r"可观测",
    r"checkpoint",
    r"snapshot",
    r"快照",
    r"回滚",
    # Common implementation primitives discussed as part of the Flow.
    r"\bskill(?:s)?\b",
    r"\bmcp\b",
    r"\bhook(?:s)?\b",
    r"\bbatch\b",
    r"\bloop(?:s)?\b",
    r"\bgoal(?:s)?\b",
    r"\beval(?:s)?\b",
    r"benchmark",
    r"提示词",
    r"prompt",
    r"任务拆",
    # The chat's "lobster" thread refers to OpenClaw/Pi; AutoGPT is kept
    # separate unless a primary source explicitly connects the names.
    r"openclaw",
    r"小龙虾",
    r"龙虾",
    r"moltbook",
    r"自动.*(?:调用|派发|启动|创建).*(?:agent|智能体)",
    r"(?:agent|智能体).*(?:调用|派发|启动|创建)",
]

WEAK_PATTERNS = [
    r"\bflow\b",
    r"流程",
    r"\bplan(?:ning)?\b",
    r"计划",
    r"\breview(?:ing)?\b",
    r"审查",
    r"评审",
    r"\btask(?:s)?\b",
    r"任务",
    r"\btool(?:s)?\b",
    r"工具",
    r"\bsession(?:s)?\b",
    r"\bmodel(?:s)?\b",
    r"模型",
    r"kimi",
    r"glm",
    r"deepseek",
    r"qwen",
    r"minimax",
    r"国产",
    r"开源模型",
    r"\bcodex\b",
    r"claude\s*code",
    r"\bcc\b",
    r"代码",
    r"项目",
    r"测试",
    r"验证",
    r"脚本",
    r"自动",
    r"控制",
    r"人类",
    r"协作",
    r"分工",
    r"构建",
    r"探索",
    r"收敛",
    r"状态",
    r"依赖",
    r"运行时",
    r"编译器",
    r"编程语言",
    r"\bdsl\b",
    r"接口",
    r"文档",
    r"长期任务",
    r"长程",
    r"递归",
    r"调度",
    r"停止条件",
    r"验收",
]

STRONG_RE = re.compile("|".join(f"(?:{p})" for p in STRONG_PATTERNS), re.IGNORECASE)
WEAK_RES = [re.compile(pattern, re.IGNORECASE) for pattern in WEAK_PATTERNS]


@dataclass
class DaySection:
    label: str
    occurrence: int
    start: int
    end: int


@dataclass
class Span:
    start: int
    end: int
    day: DaySection


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--before", type=int, default=8)
    parser.add_argument("--after", type=int, default=10)
    parser.add_argument("--bridge", type=int, default=10)
    parser.add_argument(
        "--min-seeds",
        type=int,
        default=1,
        help="Keep only merged spans containing at least this many relevant seed lines.",
    )
    parser.add_argument(
        "--no-mandatory",
        action="store_true",
        help="Do not add the manually reviewed historical anchor ranges.",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def scoring_text(line: str) -> str:
    return DISPLAY_NAME_RE.sub("", line).strip()


def is_system_notice(line: str) -> bool:
    return bool(SYSTEM_NOTICE_RE.search(line))


def is_obvious_noise(line: str) -> bool:
    """Remove only high-confidence chat/OCR debris inside retained spans."""
    if is_system_notice(line):
        return True

    content = line.removeprefix("-").strip()
    if not content:
        return True
    if TIMESTAMP_RE.match(line):
        return False

    lowered = content.casefold()
    fixed_noise = {
        "woc",
        "wc",
        "hhhh",
        "hhhhh",
        "fo",
        "fe",
        "國",
        "日",
        "酒",
        "愛",
        "爱",
        "心",
        "？",
        "?",
        "。",
        "+",
        "+1",
        "1",
        "2",
        "3",
    }
    if lowered in fixed_noise:
        return True

    # A single isolated glyph is overwhelmingly likely to be an OCR fragment,
    # emoji label, or reaction. Do not remove short words of two or more chars.
    if len(content) == 1:
        return True
    return False


def is_seed(line: str) -> bool:
    if is_system_notice(line) or TIMESTAMP_RE.match(line):
        return False

    text = scoring_text(line)
    if not text:
        return False
    if STRONG_RE.search(text):
        return True

    weak_hits = sum(bool(pattern.search(text)) for pattern in WEAK_RES)
    if weak_hits >= 2:
        return True

    # Long technical statements often contain only one term from the compact
    # lexicon. Preserve them; nearby-span merging will provide the context.
    if weak_hits == 1 and len(text) >= 72:
        return True
    return False


def build_day_sections(lines: list[str]) -> list[DaySection]:
    sections: list[DaySection] = []
    current_label: str | None = None
    current_start = 1
    occurrence_by_label: dict[str, int] = {}

    for lineno, line in enumerate(lines, start=1):
        match = TIMESTAMP_RE.match(line)
        if not match:
            continue
        label = match.group("label")
        if label == current_label:
            continue
        if current_label is not None:
            sections.append(
                DaySection(
                    label=current_label,
                    occurrence=occurrence_by_label[current_label],
                    start=current_start,
                    end=lineno - 1,
                )
            )
        current_label = label
        occurrence_by_label[label] = occurrence_by_label.get(label, 0) + 1
        current_start = lineno

    if current_label is not None:
        sections.append(
            DaySection(
                label=current_label,
                occurrence=occurrence_by_label[current_label],
                start=current_start,
                end=len(lines),
            )
        )
    return sections


def merge_ranges(ranges: list[tuple[int, int]], bridge: int) -> list[tuple[int, int]]:
    if not ranges:
        return []
    merged: list[tuple[int, int]] = [ranges[0]]
    for start, end in ranges[1:]:
        old_start, old_end = merged[-1]
        if start <= old_end + bridge + 1:
            merged[-1] = (old_start, max(old_end, end))
        else:
            merged.append((start, end))
    return merged


def build_spans(
    lines: list[str],
    days: list[DaySection],
    before: int,
    after: int,
    bridge: int,
    min_seeds: int,
) -> list[Span]:
    spans: list[Span] = []
    for day in days:
        ranges: list[tuple[int, int]] = []
        for lineno in range(day.start, day.end + 1):
            if not is_seed(lines[lineno - 1]):
                continue
            ranges.append(
                (
                    max(day.start, lineno - before),
                    min(day.end, lineno + after),
                )
            )
        for start, end in merge_ranges(ranges, bridge):
            seed_count = sum(is_seed(lines[lineno - 1]) for lineno in range(start, end + 1))
            if seed_count >= min_seeds:
                spans.append(Span(start=start, end=end, day=day))
    return spans


def add_mandatory_ranges(
    spans: list[Span],
    days: list[DaySection],
    ranges: list[tuple[int, int]],
) -> list[Span]:
    combined = list(spans)
    for range_start, range_end in ranges:
        for day in days:
            start = max(range_start, day.start)
            end = min(range_end, day.end)
            if start <= end:
                combined.append(Span(start=start, end=end, day=day))

    combined.sort(key=lambda span: (span.start, span.end))
    merged: list[Span] = []
    for span in combined:
        if (
            merged
            and merged[-1].day is span.day
            and span.start <= merged[-1].end + 3
        ):
            merged[-1].end = max(merged[-1].end, span.end)
        else:
            merged.append(span)
    return merged


def period_heading(label: str, previous: str | None) -> str | None:
    if re.match(r"3月\d+日", label) and previous != "3月":
        return "## 3 月｜3 月 18 日—3 月 31 日"
    if re.match(r"4月\d+日", label) and previous != "4月":
        return "## 4 月"
    if re.match(r"5月\d+日", label) and previous != "5月":
        return "## 5 月"
    if re.match(r"6月\d+日", label) and previous != "6月":
        return "## 6 月"
    if re.match(r"7月\d+日", label) and previous != "7月":
        return "## 7 月（含记录中的绝对日期部分）"
    if not re.match(r"[3-7]月\d+日", label) and previous != "相对日期":
        return "## 记录后段｜原文件只保留了相对日期"
    return None


def period_key(label: str) -> str:
    match = re.match(r"([3-7])月\d+日", label)
    if match:
        return f"{match.group(1)}月"
    return "相对日期"


def render(
    source: Path,
    lines: list[str],
    spans: list[Span],
) -> str:
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    selected_raw_lines = sum(span.end - span.start + 1 for span in spans)
    selected_kept_lines = sum(
        not is_obvious_noise(lines[lineno - 1])
        for span in spans
        for lineno in range(span.start, span.end + 1)
    )

    output: list[str] = [
        "# Humanize 聊天记录：Agent 相关内容时间序初筛版",
        "",
        "> 这是一份供后续人工分析使用的原始语料初筛，不是总结文章。",
        ">",
        "> 配套阅读：[关键节点导览](Agent发展史_关键节点导览.md)；[一手资料核查](../research/Agent发展史_一手资料核查.md)；[群聊引用链接索引](../indexes/Agent发展史_群聊引用链接索引.md)。",
        ">",
        "> - 所有聊天正文均按原文件顺序保留，未改写、未纠正 OCR、未重排发言。",
        "> - 仅删除明显无关区段，以及群聊邀请/撤回提示、单字符 OCR 残片等高置信噪声。",
        "> - 筛选采用高召回策略：Agent、Humanize、Harness、Flow、上下文、并行、Review、Memory、Skill、MCP、人类在环等内容及其前后语境均尽量保留。",
        "> - 每个片段都标有原文件行号。署名、引用关系和数字如需公开，仍应回到原截图核对。",
        "> - 原文中的“龙虾/小龙虾/虾”按上下文指 OpenClaw；AutoGPT 不在这份群聊中，不能混称。",
        "",
        "## 文件信息",
        "",
        f"- 原文件：`{source}`",
        f"- 原文件 SHA-256：`{source_hash}`",
        f"- 原文件总行数：{len(lines):,}",
        f"- 命中片段：{len(spans):,}",
        f"- 进入片段的原始行数：{selected_raw_lines:,}",
        f"- 删除高置信噪声后保留行数：{selected_kept_lines:,}",
        "",
        "---",
        "",
    ]

    previous_period: str | None = None
    previous_day_identity: tuple[str, int] | None = None

    for span in spans:
        current_period = period_key(span.day.label)
        heading = period_heading(span.day.label, previous_period)
        if heading:
            output.extend([heading, ""])
        previous_period = current_period

        day_identity = (span.day.label, span.day.occurrence)
        if day_identity != previous_day_identity:
            suffix = "" if span.day.occurrence == 1 else f"（第 {span.day.occurrence} 段）"
            output.extend([f"### {span.day.label}{suffix}", ""])
            previous_day_identity = day_identity

        output.extend(
            [
                f"#### 原文 L{span.start}–L{span.end}",
                "",
                f"[回到原文件 L{span.start}]({source}:{span.start})",
                "",
            ]
        )
        for lineno in range(span.start, span.end + 1):
            line = lines[lineno - 1]
            if is_obvious_noise(line):
                continue
            output.append(line)
        output.extend(["", "---", ""])

    return "\n".join(output).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    lines = args.source.read_text(encoding="utf-8").splitlines()
    days = build_day_sections(lines)
    spans = build_spans(
        lines,
        days,
        args.before,
        args.after,
        args.bridge,
        args.min_seeds,
    )
    if not args.no_mandatory:
        spans = add_mandatory_ranges(spans, days, MANDATORY_RANGES)
    rendered = render(args.source, lines, spans)

    if args.dry_run:
        print(f"source_lines={len(lines)}")
        print(f"day_sections={len(days)}")
        print(f"seed_lines={sum(is_seed(line) for line in lines)}")
        print(f"spans={len(spans)}")
        print(f"output_chars={len(rendered)}")
        print(f"output_lines={rendered.count(chr(10))}")
        return

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
