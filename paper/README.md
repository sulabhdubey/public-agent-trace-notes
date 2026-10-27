# Public Agent Trace Notes

**From public traces to defensible claims.**

An annotation dataset for historical incident-related agent traces, with four tables readers can recompute using only the included files.

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
- [Replay the four tables and identify the 45 missing captures](REPRODUCING.md).

## Reproduce the public aggregates
Requires Python 3.10+ and its standard library. No dependency installation, network access, model API, credentials or recovered-program execution is needed.

```sh
python verify.py
python verify.py --tables
python verify.py --missing
python -m unittest discover -s tests -v
```

The verifier checks the package inventory and hashes, recomputes descriptive tables and reconciles all 116 selected IDs. This is arithmetic replay of supplied annotations. It is not independent validation or raw-source re-extraction. Save command output outside the release directory so it does not become an unexpected package member.

In a managed Windows sandbox, tests may need `TEMP` and `TMP` set to an authorized writable temporary directory. Do not weaken filesystem permissions to run them. The verifier itself writes no files.

## What is included
The package contains the paper, brief, claim ledger, all 116 selection IDs, 71 body-free capture summaries, 56 POST metadata rows, 432 provenance-review rows, opaque relationship metadata, source bindings and an offline verifier. The 45 `not_acquired` IDs are individually listed; their payloads are not inferred. No credential values, payload bodies, inbox contents or private correspondence are distributed.

## What would help
Prior-analysis pointers; redaction-aware overlap checks against the larger corpus; and source-custodian clarification of catalog provenance or response semantics. Please do not post credentials, private logs or operational payloads in an issue or pull request. [Security and disclosure policy](SECURITY.md).

## Status
Version 2.1, 27 October 2026. AI-assisted, not peer reviewed. The repository's visibility determines current availability; the files themselves do not certify publication or endorsement. [Changes](CHANGELOG.md).

## Rights
Original prose and analysis code are supplied for review. No open-source or content license has yet been granted. Third-party material remains under its original terms. Choose a license before calling this repository open source; no raw third-party corpus is redistributed here.
