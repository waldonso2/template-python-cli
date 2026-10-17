"""Performance report (KENNZAHLEN.md): measured, compared with the reference values, never failing.

Not collected by `pytest` (no `test_` prefix); the CI job `performance` runs it on its own with continue-on-error:
`pytest tests/perf_report.py -q`. The table goes to $GITHUB_STEP_SUMMARY (the run's summary page) and to
$PERF_REPORT (default perf-report.md). Measure the project's own main operations here, with realistic data sizes.
"""

from __future__ import annotations

import os
import statistics
import time
from collections.abc import Callable
from pathlib import Path

import pytest

from tool import core

ROWS: list[tuple[str, str, str, str, str]] = []  # area, measure, value, reference, verdict


def record(area: str, measure: str, value: float, unit: str, good: float | None = None, source: str = "") -> None:
    verdict = "–" if good is None else ("✅" if value <= good else "⚠️")
    reference = "" if good is None else f"≤ {good:g} {unit} ({source})"
    ROWS.append((area, measure, f"{value:,.1f} {unit}", reference, verdict))


def timed_ms(fn: Callable[[], object], runs: int = 5) -> float:
    times = []
    for _ in range(runs):
        began = time.perf_counter()
        fn()
        times.append((time.perf_counter() - began) * 1000)
    return statistics.median(times)


@pytest.fixture(scope="module", autouse=True)
def report():
    yield
    lines = ["## Performance (nur Bericht, hält die CI nicht an)", "",
             "| Bereich | Messung | Wert | Referenz | |", "|---|---|---|---|---|"]
    lines += [f"| {' | '.join(r)} |" for r in ROWS]
    text = "\n".join(lines) + "\n"
    print("\n" + text)
    Path(os.environ.get("PERF_REPORT", "perf-report.md")).write_text(text, encoding="utf-8")
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a", encoding="utf-8") as f:
            f.write(text)


def test_core():
    text = " ".join(f"wort{i % 5000}" for i in range(1_000_000))
    # Nielsen: up to 1 s the user's flow of thought stays uninterrupted.
    record("Kern", "word_counts über 1 Mio. Wörter", timed_ms(lambda: core.word_counts(text), 3), "ms", 1000,
           "Nielsen 1 s")
