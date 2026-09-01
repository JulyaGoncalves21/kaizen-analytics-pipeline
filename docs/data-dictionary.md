# Synthetic data dictionary

Every name, project title, identifier, category and date is fictional.

## Improvement registry

| Field | Type | Example | Purpose | Validation |
| --- | --- | --- | --- | --- |
| `kaizen_id` | string | `KZ-001` | Synthetic initiative key | Required; reconciled with detail record |
| `title` | string | `Reduce handoff delay` | Fictional initiative title | Required in registry |
| `owner` | string | `Ana Lima` | Fictional owner | Demonstration only; not employee data |
| `expected_file` | string | `KZ-001.csv` | Local fixture filename | Resolved without network access |
| `status` | string | `Completed` | Conceptual lifecycle state | Demo vocabulary |

## Individual record

| Field | Type | Example | Purpose | Validation |
| --- | --- | --- | --- | --- |
| `kaizen_id` | string | `KZ-001` | Links detail to registry | Must equal registry identifier |
| `category` | string | `Process flow` | Synthetic improvement category | Must be non-empty |
| `completion_date` | ISO date | `2026-01-15` | Synthetic completion date | Must parse as ISO date |

## Business validation

| Field | Type | Example | Purpose | Validation |
| --- | --- | --- | --- | --- |
| `kaizen_id` | string | `KZ-001` | Links validation to initiative | Must reference synthetic registry |
| `validated` | boolean-like string | `true` | Demonstrates a separate human gate | `true`, `1` or `yes` means validated |

## Curated output

The pipeline combines the fields above with `source`, `business_validated`, `publishable` and `pending_reason`. These are demonstration governance fields, not a copy of a corporate semantic model.

