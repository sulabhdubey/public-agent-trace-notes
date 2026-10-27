# Release checks: v2.1

27 October 2026. These are author-run artifact checks, not independent investigator validation, peer review or a security certification.

- Archive SHA-256: `08b6669a9105d8018248634ccc879aaafbc4fffce16896b462977b6e33b51eed`.
- Distribution: 27 files; 179716 bytes in the ZIP; member hashes checked.
- Runtime checked: Python 3.13.7 on Windows. The declared Python 3.10+ minimum is a source compatibility target; other versions were not exercised in this run.
- Fresh-directory replay: verifier, table output, missing-ID output and 22 unit tests passed with site packages disabled. The replay's Python audit guard denied network, child execution and non-runtime inputs outside the extracted package and its scratch directory. This is not an OS isolation qualification.
- Separate arithmetic implementation: all four headline tables, all 45 missing IDs, POST event/program totals and printed POST/year table cells agree. It used the same released rows and the same research workflow, not another investigator.
- Scope: no original raw captures, private work files, model calls or credentials were required by the replay. Full catalog/wiki receipts and literal relationships remain annotations rather than independently re-extracted results.
- PDF review: eight-page paper, two-page governance brief and two-page appendix rendered and inspected.
- Publication minimization: the release contains only the allowlisted data/documents/verifier. Five disclosure-pattern categories and private comparison with the four supported source-literal pairs produced zero matches; this is scoped checking, not a guarantee against all secrets.

## Publication security review

The pre-publication review covered the 35 intended repository files, the current and prior ZIP members, extracted PDF text/actions, reachable Git history and author metadata. Author addresses use GitHub noreply. The GitHub-side inventory contained one branch, no tags, no releases, no issues/pull requests and no Actions runs at the check; no private logs or workflow artifacts were present in those inventories.

Gitleaks 8.30.1 used its default rules with an explicit empty ignore file and inline suppressions disabled. It flagged two copies of a SHA-256 field in `selection-provenance.json`, one inside the ZIP. The digest was independently recalculated from the original `capture-access-gaps.json` archive member; it is a source fingerprint, not an API key. The finding was classified against that exact field, rather than suppressing the file or rule. A fabricated, nonfunctional credential added to a private copy of the same file was still detected. No real credential was used for this control. Raw scanner records and the fixture remain private.

No confirmed credential or private-path disclosure was found in the reviewed artifact. These checks cover known patterns and inspected material, not every possible credential format or private detail. Public availability is not a security certification.

## Corrections retained

The v2.0 verifier's checks passed, but its distribution omitted the exact missing-capture list and did not emit all four headline tables. Version 2.1 closes those artifact gaps without changing the incident findings. The original ZIP remains under `distribution/` and earlier paper bytes remain in Git history.

One direct test attempt encountered the managed Windows default temporary-directory restriction: 20 tests passed and two filesystem tests errored. The fresh-directory replay used an authorized scratch directory and all 22 passed without changing those tests or weakening permissions. An initial prose assertion in the separate checker misread “distinguishes 71 acquired captures from 45 not acquired” as a denominator; the assertion was corrected to test the actual statement. Neither failure was treated as a pass.

Instrumented final replay commands totaled 4.6365 seconds. That excludes preparation, earlier attempts, source review, rendering, publication, model usage and electricity; it is not the total project cost.
