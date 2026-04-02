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
