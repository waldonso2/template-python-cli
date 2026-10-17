"""The tool's logic, without input/output - what the tests and the performance report call."""

from __future__ import annotations

from collections import Counter


def word_counts(text: str) -> list[tuple[str, int]]:
    """PLACEHOLDER example: the words of ``text`` by frequency, most frequent first (then alphabetically)."""
    counts = Counter(w.strip(".,;:!?\"'()").lower() for w in text.split())
    counts.pop("", None)
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
