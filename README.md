# PLATZHALTER: Projektname

PLATZHALTER: was das Projekt macht, in zwei Sätzen.

Aus der Vorlage [`template-python-cli`](https://github.com/waldonso2/template-python-cli) des
[quality-kit](https://github.com/waldonso2/quality-kit): Sicherheit, Barrierefreiheit und Leistung werden in der CI
geprüft, die Kennzahlen stehen in [`KENNZAHLEN.md`](KENNZAHLEN.md).

## Nach „Use this template“ ersetzen

- [ ] `PLATZHALTER` in `README.md`, `CLAUDE.md`, `KENNZAHLEN.md` und `pyproject.toml` (`name`, `description`)
- [ ] den Paketnamen `tool` (Ordner `src/tool`, `pyproject.toml`, `--cov=tool` in `.github/workflows/ci.yml`, Imports)
- [ ] `scripts/lock.sh` laufen lassen, sobald eigene Abhängigkeiten dazukommen
- [ ] die Einstellungen aus [`SETUP.md`](https://github.com/waldonso2/quality-kit/blob/main/SETUP.md) setzen

## Entwickeln

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install --require-hashes --only-binary :all: -r requirements.txt
pip install --no-deps --no-build-isolation -e .
pip install --require-hashes --only-binary :all: -r requirements-dev.txt
ruff check src tests && mypy src && pytest -q --cov=tool
pytest tests/perf_report.py -q          # Performance-Bericht (perf-report.md)
tool --help
```

## Security baseline

This template enforces the shared security-exception policy in CI. Keep `security-exceptions.json` as `[]` unless an explicitly approved, time-limited exception is required. See the [quality-kit security baseline](https://github.com/waldonso2/quality-kit/blob/main/SECURITY_BASELINE.md), [project checklist](https://github.com/waldonso2/quality-kit/blob/main/SECURITY_CHECKLIST.md), and [setup requirements](https://github.com/waldonso2/quality-kit/blob/main/SETUP.md). Configure `security-policy` as a required status check in the repository ruleset.
