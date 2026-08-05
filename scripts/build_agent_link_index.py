#!/usr/bin/env python3
"""Index URLs retained by the chronological Agent corpus."""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

from build_agent_timeline import (
    DEFAULT_SOURCE,
    MANDATORY_RANGES,
    add_mandatory_ranges,
    build_day_sections,
    build_spans,
    is_obvious_noise,
)


OUTPUT = Path(
    "/Users/zevorn/humanize-book/materials/indexes/02_Agent发展史_群聊引用链接索引.md"
)
URL_RE = re.compile(r"https?://[^\s<>]+", re.IGNORECASE)
TRAILING = ".,;:!?，。；：！？、)]}）】>"


@dataclass
class LinkRecord:
    url: str
    line: int
    day_label: str
    day_occurrence: int
    context: str
    possibly_truncated: bool


def clean_url(raw: str) -> str:
    return raw.rstrip(TRAILING)


def readable_context(lines: list[str], lineno: int, url: str) -> str:
    same_line = lines[lineno - 1].replace(url, "").removeprefix("-").strip()
    if same_line and len(same_line) >= 5:
        return same_line[:220]

    for distance in (1, -1, 2, -2, 3, -3):
        candidate_lineno = lineno + distance
        if not 1 <= candidate_lineno <= len(lines):
            continue
        candidate = lines[candidate_lineno - 1]
        if is_obvious_noise(candidate) or URL_RE.search(candidate):
            continue
        text = candidate.removeprefix("-").strip()
        if text and not re.match(
            r"(?:[3-7]月\d{1,2}日|星期[一二三四五六日天]|昨天|今天|前天)",
            text,
        ):
            return text[:220]
    return "（附近没有可可靠提取的文字语境）"


def domain_label(url: str) -> str:
    parsed = urlparse(url)
    domain = parsed.netloc or "未知域名"
    path = parsed.path.rstrip("/")
    if len(path) > 58:
        path = path[:55] + "…"
    return f"{domain}{path}"


def is_possibly_truncated(url: str) -> bool:
    return (
        bool(re.search(r"[\u3400-\u9fff]", url))
        or url.endswith(("...", "…", "?", "-", "_"))
        or "github.c" == url.removeprefix("https://").removeprefix("http://")
        or len(url) < 14
    )


def main() -> None:
    source = DEFAULT_SOURCE
    lines = source.read_text(encoding="utf-8").splitlines()
    days = build_day_sections(lines)
    spans = build_spans(
        lines,
        days,
        before=1,
        after=2,
        bridge=2,
        min_seeds=4,
    )
    spans = add_mandatory_ranges(spans, days, MANDATORY_RANGES)

    records: list[LinkRecord] = []
    seen_occurrences: set[tuple[int, str]] = set()
    for span in spans:
        for lineno in range(span.start, span.end + 1):
            line = lines[lineno - 1]
            for match in URL_RE.finditer(line):
                url = clean_url(match.group(0))
                occurrence = (lineno, url)
                if occurrence in seen_occurrences:
                    continue
                seen_occurrences.add(occurrence)
                records.append(
                    LinkRecord(
                        url=url,
                        line=lineno,
                        day_label=span.day.label,
                        day_occurrence=span.day.occurrence,
                        context=readable_context(lines, lineno, url),
                        possibly_truncated=is_possibly_truncated(url),
                    )
                )

    excluded_count = sum(record.possibly_truncated for record in records)
    records = [record for record in records if not record.possibly_truncated]

    grouped: dict[tuple[str, int], list[LinkRecord]] = defaultdict(list)
    group_order: list[tuple[str, int]] = []
    for record in records:
        key = (record.day_label, record.day_occurrence)
        if key not in grouped:
            group_order.append(key)
        grouped[key].append(record)

    unique_urls = len({record.url for record in records})
    out = [
        "# Humanize Agent 发展史：群聊引用链接索引",
        "",
        "> 这是录音/OCR 高召回语料中可可靠解析的链接目录，不等于已完成事实核查。关键资料的发布日期、内容与证据等级见[一手资料核查](../research/00_Agent发展史_一手资料核查.md)。疑似 OCR 截断项已从主索引移除，源语料仍保留原行号。",
        "",
        f"- 链接出现次数：{len(records):,}",
        f"- 去重后 URL：{unique_urls:,}",
        f"- 已排除疑似 OCR 截断：{excluded_count:,}",
        "- 排序：沿用原聊天记录顺序；日期相同也不擅自按时钟重排。",
        "",
    ]

    current_period = ""
    for key in group_order:
        label, occurrence = key
        period_match = re.match(r"([3-7])月", label)
        period = f"{period_match.group(1)} 月" if period_match else "相对日期记录段"
        if period != current_period:
            out.extend([f"## {period}", ""])
            current_period = period
        suffix = "" if occurrence == 1 else f"（第 {occurrence} 段）"
        out.extend([f"### {label}{suffix}", ""])

        for record in grouped[key]:
            source_link = f"{source}:{record.line}"
            out.append(
                f"- [{domain_label(record.url)}]({record.url}) — [原文 L{record.line}]({source_link})"
            )
            out.append(f"  - 邻近语境：{record.context}")
        out.append("")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
