# Replay the released annotations

Version 2.1, 27 October 2026. This is an author-supplied arithmetic replay, not independent historical validation. It operates on minimized annotations; it does not collect or decode original incident payloads.

## Start from only the distribution

Extract `public-agent-trace-notes-v2.1.zip` into a new empty directory. Alternatively, use the repository's `paper/` directory. Python 3.10+ and its standard library suffice. Do not install dependencies or supply credentials. Run the following **inside the extracted directory**:

```sh
python -B verify.py
python -B verify.py --tables
python -B verify.py --missing
python -B -m unittest discover -s tests -v
```

To omit third-party site packages, Python also accepts `-S`. The verifier works with `-I`; direct unittest discovery needs the package directory on its import path. Do not redirect output into the release directory: unlisted files deliberately fail the manifest check. Save receipts outside it.

## Expected headline results

| Derived table | Paper location | Expected output |
|---|---|---|
| Selection coverage | Section 3 | 116 selected; 71 acquired; 45 not acquired |
| Exact-program grouping | Section 5.4 | 42 programs; 8 duplicate groups comprising 37 reports; 34 singleton programs; 29 repeats |
| Recorded POST statuses | Section 5.2 | 200: 9; 201: 1; 204: 3; 307: 8; 400: 9; 401: 1; 422: 1; 429: 2; Missing: 22; total: 56 |
| Catalog review years | Section 5.3 | 2023: 113; 2024: 56; 2025: 111; 2026: 152; total: 432 |

The default JSON output also checks 13 recorded POST 2xx events across 13 reports and 8 programs, 48 reports with recorded POSTs, and the full list of not-acquired IDs. `--tables` prints the four derived tables as Markdown; `--missing` prints only the 45 IDs as JSON after the same checks.

## Exactly which captures are missing?

`data/capture-selection.csv` is the full 116-ID cohort. Filter `acquisition_status` for `not_acquired`, or use `--missing`. The 71 `acquired` IDs must equal the IDs in `data/captures.json`, and the two groups cannot overlap. The verifier rejects duplicate IDs, unexpected labels and inconsistent membership. The ledger's source-member hashes and construction are in `data/selection-provenance.json`.

These labels describe the original held sample. They do not claim that a missing capture is unavailable now, that retrieval failed for a particular reason, or that raw bodies are distributed for acquired captures. All raw capture bodies remain excluded.

## What a successful run does and does not check

- **Recomputed from released rows:** the four headline tables, POST/report/program totals and selection membership.
- **Inspectable metadata, not independently re-extracted:** opaque mailbox relationships, source hashes and wiki findings. The complete catalog/wiki totals are carried in prior audit receipts rather than derived from this minimized release.
- **Not performed:** raw-source extraction, credential testing, live endpoint requests, actor/model attribution or authentication of effects.

The manifest detects changes relative to itself. It is not a signature: a modified dataset plus a modified manifest can agree. Exact archive hashes bind versions, not the truth of the annotations.

## Recipient checklist

Record the archive digest, Python version, command, exit status, output and any edits required. Confirm the status table has a separate Missing row; confirm all 45 absent IDs are listed and excluded from the acquired rows. Report disagreements against a specific table cell or report ID. Do not post raw payloads or credentials.

An author-run fresh-directory replay was used to test this interface. A separate arithmetic check did not import `verify.py`, but used the same released data and was performed by the same research workflow. A new directory or a second implementation does not make the investigator independent. No external-review badge is claimed.

## If a check fails

Preserve the error and package hash. For missing or altered members, extract a new copy rather than rewriting the manifest to silence the failure. In managed Windows environments, tests may need `TEMP` and `TMP` directed to an authorized temporary directory outside the release. No filesystem-security setting needs to be weakened.
