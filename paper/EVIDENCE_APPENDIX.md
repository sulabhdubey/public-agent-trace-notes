# Evidence appendix

## Public files and verification strength
| File | Content | What its reproduction establishes |
|---|---|---|
| data/captures.json | Report ID, report date, input digest, exact-program digest, decoded length | Held inventory and exact-byte grouping |
| data/post-events.json | Parent report ID, recorded time, public endpoint class and response status | Event census and missingness |
| data/catalog-review.csv | 432 IDs, report dates and broad classes | Year/class distributions; not attribution |
| data/mailbox-groups.json | Opaque pair labels and report/program relationships | Public relationship metadata; literal equality requires held raw inputs |
| data/wiki-findings.json | Body-free revision identifiers, fingerprints and timing metadata | Held-source comparison receipt; not a fresh collection |
| data/source-bindings.json | Source and original package digests | Identity of the original source bytes |
| audit-results.json | October re-extraction and aggregation receipt | What was run locally and its limitations |
| claims.json | Claim, evidence and explicit non-claim | Scope of publication assertions |

## Reproduction levels
1. Public package integrity: verify the SHA-256 inventory. A maliciously changed package and manifest can agree; the manifest is not a signature or trusted attestation.
2. Public arithmetic: recompute groups, statuses and catalog-year counts using the included minimized tables.
3. Held-source re-extraction: six original scripts were inspected and executed locally against hash-matched original inputs. Capture observations are semantically identical. Those raw inputs are not redistributed because they can contain credentials or executable content.
4. Independent authentication: not completed. Actor identity, authorization, application-level effect, complete corpus overlap and novelty remain outside these checks.

The original extraction implementation is reused at level 3. The new public aggregator is separately implemented. Neither provides independent historical data collection.

## Historical timeline checks
On June 19, report dates for the first mailbox relationship span 12:29:38 to 12:49:35 UTC. Recorded account POST error events precede three later token POST 200 events. On June 14, the second relationship spans 22:58:10 to 23:22:19 UTC. Dates describe different evidence fields; temporal proximity does not prove causation.

The catalog queue spans September 22, 2023 through September 9, 2026. Its older records remain unresolved metadata, not an earlier-incident discovery. Forty-three indirection candidates concentrate on May 11-12, 2026; their payload bodies remain unreviewed.

## Tests and correction
The original census recognized a fixed set of status codes. The revised public predicate recognizes integer statuses 200 through 299, including valid codes absent from this sample. Tests cover POST versus OPTIONS, missing values, redirects, invalid types, duplicate IDs, orphan events and tampered package members. These fixtures test the verifier, not the behavior or safety of agents.

## Reproducibility limits
The smaller package intentionally cannot recreate credential-literal equality from scratch. It exposes the relationship membership and source hashes so an authorized holder of the same original captures can compare results. No reader should obtain, authenticate with or test credentials to validate the paper. The 45 missing captures and complete Swarm Traces overlap remain open.

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
