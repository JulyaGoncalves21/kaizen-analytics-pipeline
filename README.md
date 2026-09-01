# Kaizen Analytics Pipeline

A sanitized, local-only portfolio adaptation of a workflow that consolidates individual Kaizen files, reconciles them with an improvement registry, records exceptions, requires business validation, and prepares a structured analytical dataset.

## Problem

Improvement records were distributed across files owned by different people while analysis required one consistent dataset. Missing files, alternate remote attachments, template differences and business approval made a simple file merge unsafe.

## Solution

The source workflow locates each file, prefers a local copy, tries an attachment fallback, parses and validates records independently, lists unresolved items, and applies a human validation gate before data becomes publishable. The resulting layer supports an HTML analysis view and later Power BI consumption; Power BI refresh remains manual.

This repository implements that boundary with synthetic CSV data. It intentionally excludes corporate adapters and proprietary workbook layouts.

## Architecture and data flow

1. Read the synthetic improvement registry.
2. Resolve each expected source using local-first, fallback-second precedence.
3. Read the public key/value format and validate identifier, category and date.
4. Isolate missing or malformed records as pending.
5. Join explicit business validations.
6. Export CSV and JSON; do not mutate the portfolio HTML or Power BI.

See [architecture](docs/architecture.md) and [technical decisions](docs/technical-decisions.md).

## Main components

- `data_sources.py`: registry and business-validation adapters.
- `file_discovery.py`: deterministic local/fallback resolution.
- `workbook_reader.py`: transparent public input reader.
- `validation.py`: pure, testable rules.
- `transformation.py`: publication-gate model.
- `export.py`: local analytical outputs.
- `cli.py`: orchestration with per-record error isolation.

## Repository structure

```text
src/kaizen_pipeline/  Python package
tests/                pure-rule tests
sample-data/          invented demonstration records
power-bi/             safe semantic-layer documentation
docs/                 architecture and decisions
site/                 GitHub Pages case study
```

## Technologies

Python standard library, CSV/JSON, pytest and ruff for development, semantic HTML and CSS, and GitHub Actions. The private workflow also uses Excel and corporate data sources; those integrations are not included.

## Run with synthetic data

```bash
python -m venv .venv
python -m pip install -e .
python -m kaizen_pipeline.cli --show-summary
```

Expected summary for the included sample: six processed records, three publishable and three pending. This is a deterministic demo outcome, not an operational metric.

## Security and anonymization

All public records are fictional. No original spreadsheets, endpoints, credentials, employee/client data, executables, logs, PBIX/PBIT files or browser state are included. Review [PUBLIC_RELEASE_AUDIT.md](PUBLIC_RELEASE_AUDIT.md) before reuse.

## Limitations of the public version

- The original Excel template parsers and corporate attachment/list clients remain private.
- The public adapter uses CSV instead of reproducing corporate workbook structures.
- No Power BI file is distributed; only a safe data contract is documented.
- The site explains the case and is not rewritten by the pipeline.
- Power BI refresh is not automated.

## Next steps

- Add an XLSX synthetic sample when the controlled workbook-generation tool is available.
- Add a pluggable read-only API contract without shipping corporate implementation.
- Extend validation tests with more malformed synthetic inputs.

## Author

Portfolio project maintained by the repository owner.

## Resumo em português

Versão pública e sanitizada de um pipeline de consolidação de Kaizens. A demonstração usa somente dados fictícios, prioriza arquivo local, usa fallback local de exemplo, registra pendências e exige validação do negócio antes da publicação. Integrações corporativas, planilhas reais, executáveis e Power BI original permanecem privados.

