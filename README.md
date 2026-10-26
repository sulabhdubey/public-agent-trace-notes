# Public Agent Trace Notes

**From public traces to defensible claims.**

A technical note, a platform-governance brief and a reproducible evidence package for reviewing historical incident-related agent traces.

![Selected sample and recorded response outcomes](paper/assets/evidence-card.png)

| Start here | What it contains |
|---|---|
| [Research paper](paper/PAPER.md) · [PDF](paper/paper.pdf) | Analysis, methodology, qualified findings and limitations |
| [Governance brief](paper/GOVERNANCE_BRIEF.md) · [PDF](paper/governance-brief.pdf) | Implications for trace preservation and platform review |
| [Evidence appendix](paper/EVIDENCE_APPENDIX.md) · [PDF](paper/evidence-appendix.pdf) | Reproduction, coverage, retained negative leads and costs |
| [Complete ZIP](distribution/public-agent-trace-notes-v2.0.zip) · [SHA-256](distribution/public-agent-trace-notes-v2.0.sha256) | The exact reviewed 23-file distribution |
| [Claim ledger](paper/claims.json) · [Sources](paper/SOURCES.md) | Evidence bindings and attribution |

## What this establishes

The held sample contains 71 captures representing 42 exact programs. Its 56 recorded POST events include 13 with 2xx responses across eight programs, and 22 without a recorded response status. These counts do **not** establish compromised accounts, independent operators, global coverage or a newly discovered incident.

The contribution is inspectable annotation and explicit uncertainty. Forty-five selected captures and full-corpus overlap remain unresolved. See the paper before citing an aggregate.

## Reproduce locally

Python 3.10+ and its standard library are sufficient. No model calls, credentials, dependency installation or incident-code execution are required.

```sh
cd paper
python verify.py
python -m unittest discover -s tests -v
```

The `paper/` directory preserves the reviewed distribution exactly. The separate root index and `distribution/` downloads do not alter its internal manifest. Checksums establish byte identity, not truth, authenticity or discovery priority.

## Review status and safe sharing

This repository is intended for **private owner review**. The paper is version 2.0, dated 26 October 2026; repository packaging is dated 27 October 2026. It is AI-assisted and not peer reviewed. No organizational endorsement is implied.

Only minimized, body-free metadata is included. Raw payloads, credentials, private correspondence and model diagnostics are excluded. Please follow the [security and disclosure policy](paper/SECURITY.md); do not submit operational payloads or private logs in issues.

Original prose and analysis code are supplied for review; no open-source or content license has yet been granted. Third-party rights remain with their owners.
