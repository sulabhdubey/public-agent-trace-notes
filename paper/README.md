# Public Agent Trace Notes

**From public traces to defensible claims.**

A reproducible technical note on historical incident-related agent traces, with minimized metadata and offline checks.

| 71 held captures | 42 exact programs | 13 recorded POST 2xx events | 22 missing POST statuses |
|---|---|---|---|
| Of 116 selected reports | Eight duplicate groups | Across eight programs | Of 56 recorded POST events |

These counts do **not** establish compromised accounts, independent operators or a new incident.

## Start here
- [Read the technical note](PAPER.md) or [PDF](paper.pdf).
- [Read the platform-governance brief](GOVERNANCE_BRIEF.md) or [PDF](governance-brief.pdf).
- [Inspect the evidence and limitations](EVIDENCE_APPENDIX.md).
- [Check primary sources and updates](SOURCES.md).
- [Review every claim](claims.json).

## Reproduce the public aggregates
Requires Python 3.10+ and its standard library. No dependency installation, network access, model API, credentials or recovered-program execution is needed.

```sh
python verify.py
python -m unittest discover -s tests -v
```

The verifier checks the package inventory and hashes, then recomputes descriptive counts from the minimized tables. That verifies this distribution's bytes and arithmetic; it does not authenticate the source or reproduce the private literal comparisons from raw captures.

In a managed Windows sandbox, tests may need `TEMP` and `TMP` set to an authorized writable temporary directory. Do not weaken filesystem permissions to run them. The verifier itself writes no files.

## What is included
The public package contains the paper, brief, claim ledger, 71 body-free capture summaries, 56 POST metadata rows, 432 provenance-review rows, opaque relationship metadata, source bindings and an offline verifier. No credential values, payload bodies, inbox contents or private correspondence are distributed.

## What would help
Prior-analysis pointers; redaction-aware overlap checks against the larger corpus; and source-custodian clarification of catalog provenance or response semantics. Please do not post credentials, private logs or operational payloads in an issue or pull request. [Security and disclosure policy](SECURITY.md).

## Status
Version 2.0, 26 October 2026. AI-assisted, not peer reviewed. Prepared for owner review; this local candidate is not evidence of GitHub publication. No first-discovery claim or organizational endorsement. [Changes](CHANGELOG.md).

## Rights
Original prose and analysis code are supplied for review. No open-source or content license has yet been granted. Third-party material remains under its original terms. Choose a license before calling this repository open source; no raw third-party corpus is redistributed here.
