# Evidence appendix

## Public files and verification strength
| File | Content | What its reproduction establishes |
|---|---|---|
| data/captures.json | Report ID, report date, input digest, exact-program digest, decoded length | Held inventory and exact-byte grouping |
| data/capture-selection.csv | All 116 selected IDs and acquisition labels | Exact membership of 71 acquired and 45 not-acquired captures |
| data/selection-provenance.json | Original archive/member hashes and construction | Lineage of the coverage ledger; not new capture collection |
| data/post-events.json | Parent report ID, recorded time, public endpoint class and response status | Event census and missingness |
| data/catalog-review.csv | 432 IDs, report dates and broad classes | Year/class distributions; not attribution |
| data/mailbox-groups.json | Opaque pair labels and report/program relationships | Public relationship metadata; literal equality requires held raw inputs |
| data/wiki-findings.json | Body-free revision identifiers, fingerprints and timing metadata | Held-source comparison receipt; not a fresh collection |
| data/source-bindings.json | Source and original package digests | Identity of the original source bytes |
| audit-results.json | October re-extraction and aggregation receipt | What was run locally and its limitations |
| claims.json | Claim, evidence and explicit non-claim | Scope of publication assertions |

## Verification levels
1. Public package integrity: verify the SHA-256 inventory. A maliciously changed package and manifest can agree; the manifest is not a signature or trusted attestation.
2. Released-metadata arithmetic: `verify.py --tables` recomputes selection coverage, program grouping, statuses and catalog-year counts. `--missing` lists the 45 absent IDs. See REPRODUCING.md for commands and expected results.
3. Held-source re-extraction: six original scripts were inspected and executed locally against hash-matched original inputs. Capture observations are semantically identical. Those raw inputs are not redistributed because they can contain credentials or executable content.
4. Independent authentication: not completed. Actor identity, authorization, application-level effect, complete corpus overlap and novelty remain outside these checks.

The original extraction implementation is reused at level 3. The public aggregator is separately implemented, but all checks so far belong to the same research workflow. A fresh-directory package replay is an author-run usability and arithmetic check, not another investigator's reproduction. Complete catalog/wiki totals are preserved audit receipts rather than recalculated from the released subsets.

## Tests and correction
The original census recognized a fixed set of status codes. The public predicate recognizes statuses 200 through 299, including valid codes absent from this sample. Tests cover POST versus OPTIONS, missing values, redirects, invalid types, duplicate IDs, orphan events and tampered package members. Version 2.1 adds selection-set reconciliation and actual table-generation checks: absent/acquired contradictions, duplicate selection IDs, invalid labels, integer/string status grouping, a changed status and a changed year. These fixtures test the verifier's changed behavior.

## Reproducibility limits
The package cannot recreate credential-literal equality from scratch. It exposes relationship membership and source hashes for comparison by an authorized source holder. No reader should obtain or test credentials to validate the paper. All 45 absent capture IDs are now identified; their contents and complete Swarm Traces overlap remain open.

## Earlier leads retained as negative or limited findings
The predecessor examined additional leads that did not justify a discovery claim. They are retained here to prevent repeated work or selective reporting:
- The original RubyGems metadata check returned 404 for 79 distinct candidate package names, while a control returned 200. These are historical acquisition observations, not a fresh October availability check or proof that no copy exists elsewhere.
- Nineteen public Hugging Face repository containers had already been independently inventoried. Their existence did not authenticate an operator or prove execution.
- Public mirror and Iowa paste recovery leads were already being examined by other researchers; the existence of a recoverable archive was not our first discovery.
- A public GIS schema did not establish an attributable missing upload.
- An encoding review found 251 revision-hash differences explained by byte encoding. Syntactically decodable base64 tokens were not counted as executable programs. The fresh held-source wiki audit retains its encoding result in data/wiki-findings.json.

These earlier lead conclusions are carried forward at their original scope. No new live registry, repository or incident-endpoint request was made to turn them into current-state assertions.

## Cost
Original-source audit jobs: 10.6365 seconds summed instrumented wall time. Reproduction timing is host-specific and excludes startup surrounding the measured jobs, research, model calls, writing and electricity. A separate model-review attempt returned unknown usage and no review. Total investigation cost is unknown. The validation receipt records the public verifier/test result separately.
