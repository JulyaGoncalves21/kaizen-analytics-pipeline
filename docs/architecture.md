# Architecture

```text
Individual files ── local first ──┐
Remote attachment ── fallback ────┼─> read and validate ─> pending queue
Improvement registry ─────────────┘                         │
Business validation file ──────────────────────────────────┤
                                                          v
                                      publishable CSV/JSON layer
                                             │          │
                                      static HTML   Power BI (manual)
```

The original application contains desktop UI, Excel-template parsers, incremental state and corporate adapters. The public package implements only the safe local boundary. A failed record becomes pending and does not stop the remaining records.

The static portfolio page is documentation; the pipeline never rewrites its visual content. Power BI refresh remains outside the automation and is manual in the source workflow.

