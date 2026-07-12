from __future__ import annotations

import json
import re
from pathlib import Path


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9']+", text.lower()))


def search_events(
    path: Path, query: str, start_date: str, end_date: str, top_k: int | None = None
) -> list[dict[str, str]]:
    events = json.loads(path.read_text(encoding="utf-8"))
    query_tokens = _tokens(query)
    filtered = [e for e in events if start_date <= e["date"] <= end_date]
    scored = []
    for event in filtered:
        overlap = len(query_tokens & _tokens(event["headline"]))
        scored.append((overlap, event))
    scored.sort(key=lambda pair: (pair[0], pair[1]["date"]), reverse=True)
    ranked = [event for score, event in scored if score > 0]
    if top_k is None:
        return ranked
    return ranked[:top_k]


def available_date_range(path: Path) -> tuple[str, str]:
    events = json.loads(path.read_text(encoding="utf-8"))
    dates = sorted(event["date"] for event in events)
    return dates[0], dates[-1]


def search_events_with_scores(
    path: Path, query: str, start_date: str, end_date: str, top_k: int = 3
) -> list[tuple[dict[str, str], int]]:
    events = json.loads(path.read_text(encoding="utf-8"))
    query_tokens = _tokens(query)
    filtered = [e for e in events if start_date <= e["date"] <= end_date]
    scored: list[tuple[dict[str, str], int]] = []
    for event in filtered:
        overlap = len(query_tokens & _tokens(event["headline"]))
        if overlap > 0:
            scored.append((event, overlap))
    scored.sort(key=lambda pair: (pair[1], pair[0]["date"]), reverse=True)
    return scored[:top_k]
