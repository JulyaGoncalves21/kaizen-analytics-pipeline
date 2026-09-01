# Technical decisions

- **Local adapter only:** corporate list and attachment clients are excluded.
- **CSV public contract:** makes the synthetic example inspectable without reproducing proprietary workbook layouts.
- **Local-first resolution:** reflects the proven operational priority and makes fallback explicit.
- **Per-record error isolation:** one malformed or missing file is converted into a pending item.
- **Explicit publication gate:** technical validity alone is insufficient; business validation is required.
- **Separate presentation:** the pipeline exports data but does not change HTML or operate Power BI.
- **No permissive license yet:** ownership clearance for the source material has not been established.

