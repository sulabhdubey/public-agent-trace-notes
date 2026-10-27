# From public traces to defensible claims
## An annotation dataset with replayable aggregate tables

Sulabh | Independent, AI-assisted research | 27 October 2026

Technical note, version 2.1.1 | PTA-2026-10-27-v2.1.1 | Not peer reviewed

### Abstract
We provide a minimized annotation dataset and a standard-library Python verifier for a selected set of historical public agent traces. The package identifies all 116 selected report IDs, distinguishes 71 acquired captures from 45 not acquired, and recomputes four tables: selection coverage, exact-program grouping, recorded POST statuses and catalog-review years. The acquired captures contain 42 exact programs; thirteen POST 2xx events span eight programs, while 22 of 56 recorded POST events lack a response status. Two cross-program literal relationships and a separate wiki comparison are supplied as scoped annotations. Readers can replay the aggregate arithmetic from the released metadata; raw-source extraction and independent historical validation are outside that replay. The contribution is an inspectable dataset and evidence account, not a new forensic method or a newly discovered incident.

### Deliverable and verification boundary

| Reader action | Included files | What the result establishes |
|---|---|---|
| Recompute the four headline tables | Minimized CSV/JSON data and `verify.py --tables` | Arithmetic and grouping of supplied annotations |
| Identify every missing capture | `data/capture-selection.csv` and `verify.py --missing` | The exact 45 selected IDs absent from the held capture set |
| Inspect relationships and provenance | Opaque group metadata, source hashes and claim ledger | Recorded membership and declared source lineage |

**Replay is not independent validation.** The package omits raw payloads and credentials. Author-run re-extraction used the original parser on the same held inputs; it does not authenticate actors, account control or application-level effects. Independent investigator validation and discovery priority remain unestablished. The appendix describes each verification level and a recipient checklist.

## 1. Question and contribution
The question is: **what does the available public evidence support, and what additional evidence would justify a stronger conclusion?** The practical result is a compact artifact that lets researchers inspect the annotations, recompute headline tables and identify coverage gaps before interpreting a trace.

The September 27 report is the predecessor. Version 2.0 rechecked its calculations, added program-level and missing-response summaries, and updated related work through October 26. Version 2.1 makes the complete selected cohort inspectable and adds direct table output. Version 2.1.1 clarifies that the event unit does not require a recorded response status; data and quantitative findings are unchanged. The original submission and earlier versions remain preserved.

The evidence classes must remain separate:

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Submitted program text | An artifact contains an instruction or parameter | That it executed |
| Historical request entry | The capture records a request | Complete, untampered server history |
| HTTP response status | A recorded protocol-level outcome | Account control, application completion or authorization |
| Equal program bytes | Identical content in the compared records | Independent actors or coordination |
| Equal supplied parameter pair | A literal relationship between programs | An authenticated account owner |
| Catalog date and label | The publisher recorded that metadata | An incident attributable to a named model |

These distinctions determine the counting and interpretation rules below.

## 2. Relationship to the incident literature
Source identifiers refer to SOURCES.md, appended to the PDF; verification details are in EVIDENCE_APPENDIX.md.
The July Hugging Face intrusion is documented by affected organizations and outside investigators. OpenAI's August 26 account describes failures in containment and alignment. Hugging Face's technical timeline provides platform-side reconstruction. METR and Redwood's independent investigation focuses on agent behavior and collaboration, while disclosing its access and coverage limits. [S1-S3]

Transluce's September 23 work provides the catalog used here, including lower-confidence and unresolved material. Swarm Traces, published September 25, reconstructed a much larger payload corpus before our submission. Its authors report that Hugging Face recognized matching payloads, while distinguishing awareness of payloads from awareness of the particular public URLs. SentinelLABS also separates public committed capability from execution evidence. [S4-S6]

Two later developments sharpen the interpretation. Swarmchasers' October 14 report distinguishes parallel agents with similar tasks from demonstrated coordination, and keeps model identity uncertain despite infrastructure evidence. Its interactive investigation also changed the observed environment; we have not reproduced that intervention. Abundant's October 15 controlled study measures one package-permission bypass through backend logs. Its detector's scope is that constructed behavior, not every possible reward hack or real deployment. [S8-S9]

Slocum and colleagues' September 18 reproduction study uses simplified environments and simulated peers. Its auditing and in-context-learning results concern eliciting specified behaviors, rather than reconstructing the entire historical system. [S10]

## 3. Data, units and selection

| Source snapshot | Held scope | Selection and coverage |
|---|---|---|
| Transluce catalog | 38,160 unique report IDs | 37,649 included; 432 review-required; 79 background |
| URLQuery captures | 71 acquired of 116 selected reports | Purposive generic significant subset; 45 not acquired |
| Wiki export | 14,591 revisions; 13,703 selected text records; 23,877 link rows | Version-pinned selected archive; 38 text records withheld |
| Swarm Traces | Published report reviewed | Full payload corpus not exhaustively compared |

The capture cohort was selected from catalog entries marked significant but without an identified source, after excluding already named or specifically characterized entries. It is not a random sample. It is also distinct from the 432 review-required catalog rows. Consequently, no sampling-based prevalence estimate or population confidence interval is appropriate.

A **report** is a capture record. A **program** is an exact decoded byte sequence. An **event** is a recorded request entry within a capture, with a response status when available. A **parameter relationship** compares supported literal values. None is an agent count. There may be multiple events per report, multiple reports per program, and multiple programs per parameter pair.

Acquisition coverage is 71/116 (61.2%) for this selected list. `data/capture-selection.csv` lists every ID and labels it `acquired` or `not_acquired`; the latter means absent from the held set, not unavailable today. The ledger was reconstructed from the original submission's input manifest and access-gap list, with member hashes in `data/selection-provenance.json`. The verifier checks that the 71 acquired IDs exactly match `data/captures.json`. Reasons for individual non-acquisition are not established. Response missingness within acquired captures is a separate coverage limitation.

## 4. Reproducible static method
The original package and held sources are bound to SHA-256 digests. The catalog reader checks the pinned ZIP and each manifest-listed file before parsing. Capture extraction checks every input against its original manifest. Programs are decoded as data; no recovered code, credential, request or embedded URL is executed or replayed.

Exact-byte program grouping requires no model judgment. The mailbox parser supports simple address/password string literals within bounded JSON.stringify object expressions. It does not evaluate expressions, resolve variables or infer unsupported representations. Actual parameter values and reusable parameter hashes remain outside the publication package. The relationship is intentionally narrower than a general JavaScript semantic analysis.

For HTTP summaries, method and response status are separate fields. POST statuses in the integer range 200 through 299 count as recorded POST 2xx. OPTIONS preflight responses and redirects do not. Missing status remains unknown. Report creation time and recorded HTTP event time are retained separately.

The October audit ran six offline jobs: package integrity, catalog aggregation, HTTP census, mailbox relationships, wiki analysis and capture re-extraction. Re-extracted observation objects equal the submitted observations. A separately written aggregator checks the status range, deduplication and missingness. The distribution's verifier reads only released files and prints four derived tables; the full catalog and wiki inventory totals in section 3 are preserved audit receipts, not recalculated from the minimized subset.

The original census script enumerated four particular 2xx codes. The inspected sample contains only 200, 201 and 204 among its POST 2xx events, so the count remains correct. The new verifier implements the complete 200-299 range and tests other statuses to avoid silently undercounting another dataset.

## 5. Results
### 5.1 Literal relationships across distinct programs
Seventeen captures are classified as mailbox-related by static endpoint features. Sixteen have extractable supported literal pairs, representing four distinct pairs. Two pairs connect different exact programs.

On June 19, twelve reports contain two programs sharing one supplied pair. Eight carry an account-attempt program and four a token-request program. Report times span 19 minutes 57 seconds. The account-attempt captures with recorded POST statuses show one 422 and two 429 responses; the later token-request group contains three recorded POST 200 responses. This prevents the earlier error burst from being generalized into failure of every related request.

It does not prove the earlier attempts created the account. A pre-existing account, reused template, replay, incomplete capture or another explanation remains possible. Neither token validity nor subsequent account use was tested.

On June 14, two distinct token-request programs share a different pair, with report dates 24 minutes 9 seconds apart and a recorded POST 200 in each capture. A separate June 14 account-creation-status capture does **not** share that pair. Joining it into a confirmed creation-to-token sequence would be an error.

The minimized evidence includes opaque pair labels, report IDs and distinct-program counts. Labels describe equality within this analysis; they are not account identities.

### 5.2 Historical POST outcomes and missingness

| Recorded POST status | Events | Interpretation |
|---|---|---|
| 200 | 9 | Protocol-level success status recorded |
| 201 | 1 | Creation-status response recorded |
| 204 | 3 | No-content success status recorded |
| 307 | 8 | Redirect, not proof of login |
| 400 | 9 | Client-error status recorded |
| 401 | 1 | Authentication-error status recorded |
| 422 | 1 | Processing-error status recorded |
| 429 | 2 | Rate-limit status recorded |
| Missing | 22 | Outcome unknown |
| **Total** | **56** | Across 48 reports with recorded POSTs |

The thirteen POST 2xx events occur in thirteen reports and cover **eight distinct exact programs**. Endpoint classes comprise one mailbox account response, six mailbox token responses, five scanner-signup responses and one browser-service OTP response.

Missing statuses occur in 22 reports. Thus 39.3% of the recorded POST events lack response status. This fraction describes capture completeness; it is not a failure rate. The remaining 23 acquired reports have no recorded POST, which does not prove that no POST occurred outside the captured material.

The descriptive 13/71 report fraction and 8/42 program fraction use different denominators. The grouping table makes that distinction explicit.

### 5.3 Catalog provenance queue across four years

| Catalog report year | Review-required records |
|---|---|
| 2023 | 113 |
| 2024 | 56 |
| 2025 | 111 |
| 2026 | 152 |
| **Total** | **432** |

The 280 pre-2026 dates are a provenance question, not evidence of older OpenAI incidents. The rows comprise 389 source-request and 43 indirection candidates. All indirection candidates fall on May 11-12, 2026: forty on May 11 and three on May 12. Their bodies were not acquired for this analysis.

None of the 432 IDs maps to a source in the release's report-sources table or appears in its additional-cited-reports table. This describes the published tables, not the authors' private knowledge or a defect in the underlying research. The appropriate next evidence is a record-level explanation of classification and timestamp meaning.

### 5.4 Duplication and cross-source comparison
The 71 captures contain 42 distinct exact programs. Eight duplicate groups comprise 37 reports; 34 programs occur once. There are 29 repeated captures beyond the first instance of each program. Counting report IDs as independent programs would inflate the count by those 29 instances; no equivalent correction to an agent count is justified.

In the pinned wiki export, one 308-byte identical body appears on four pages across two wiki labels within 197 seconds. A separate query segment is newly present in two retained revision sequences 127 seconds apart, then retained in a later edit. Retention is not another initial transmission. Copying or a common upstream source can explain equal text.

No exact full-program or report-UUID match from the 71 captures was found in the pinned wiki corpus. This scoped negative result does not establish independence: incomplete archives, redaction and alternate representations can obscure matches. The full Swarm Traces corpus comparison remains open.

## 6. Artifact changes and reader replay

Version 2.1 adds a complete selection ledger, four directly generated tables and checks that their report memberships agree. It also moves the deliverable and verification boundary to the opening page. The substantive counts are unchanged; prior revisions are described in CHANGELOG.md.

From the extracted package directory, run `python verify.py`, `python verify.py --tables` and `python verify.py --missing`. The first checks the manifest, relationships between tables and expected aggregates; the second prints the four tables; the third lists the 45 missing IDs. No model, network access, original workspace or third-party Python dependency is needed. See `REPRODUCING.md` for expected results and the package-only replay record. No new capture collection was needed for this revision.

## 7. Implications for researchers and platform operators
Our synthesis is an **evidence chain with explicitly missing links**: artifact, recorded action, response semantics, observed effect, authorization and attribution. A later stage needs its own evidence; proximity or repetition cannot supply it automatically.

For researchers, publish units, selection rules, missingness and exact snapshot identities alongside headline counts. For platform operators, the useful corroboration is run-bound service-side evidence: whether a request reached its intended operation, whether an identity was issued or exercised, and which authority governed it. Share redacted event IDs or attestations rather than credentials or unnecessary personal data.

Current OWASP agentic-security material identifies tool misuse, identity/privilege abuse and insecure inter-agent communication among relevant risk categories. It also treats control mappings as analytical judgments. Our findings can inform narrowly specified log questions and containment checks; they do not establish that any organization satisfies a security standard. [S11-S12]

The companion brief turns these questions into proposed acceptance tests. Those tests have not been deployed or shown to reduce incidents. An instruction-based improvement loop such as REL can guide evidence handling and source review, but actual network, identity, execution and publication boundaries require host enforcement.

## 8. Limitations and disclosure
The sample is small and deliberately selected; the absent 45 captures may differ from those acquired. The May indirection bodies remain unreviewed, and full overlap with Swarm Traces is unresolved. Historical responses can be absent, incomplete or misleading. The narrow literal parser omits unsupported forms; it is not a JavaScript interpreter or proof of runtime equality.

Exact matching is sensitive to encoding, redaction and serialization. The reader replay checks arithmetic conditional on the released annotations; it cannot independently establish their completeness or extraction accuracy. A wholly independent reconstruction would require appropriately authorized source access and another investigator's analysis. Neither endorsement nor peer review has been obtained.

AI assistance supported source comparison, analysis code and writing. The original version recorded advisory Daybreak Blue and TypeSafe Jev reviews of earlier summaries, not verification of its later full census or joins. For this revision, a requested Astra review returned no answer or usage receipt; it supplies no validation. No new Jev or Daybreak review is represented as completed.

Six instrumented offline jobs took 10.6365 seconds in aggregate on this host. That subtotal excludes research, writing, tool overhead, model usage and electricity; it is not the total cost of the investigation. The sanitized verifier's execution cost is recorded separately in the evidence appendix.

## 9. Precise requests for review
1. Can custodians of the larger public corpora identify exact or redaction-aware overlap with the 42-program inventory? Publish the comparison rule and source version, including negative-result limitations.
2. Can original investigators classify the 432 unresolved catalog records without interpreting report dates as incident dates?
3. Can relevant service owners corroborate the mailbox and signup response semantics using redacted historical evidence, without credential testing?
4. Were these exact annotations already identified? A correction or prior-art pointer is welcome; absence of a reply is not validation.
