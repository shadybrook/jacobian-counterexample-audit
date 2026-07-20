# Audit against the original publication request

Status date: 20 July 2026.

| Requested outcome | Status before this revision | Status now | Evidence |
|---|---|---|---|
| Independently reverify the determinant and collision | Fulfilled | Fulfilled and regression-tested | `src/verify.py`; `tests/test_map.py` |
| Formulate a polished paper | Fulfilled | Expanded | `paper/main.md`, `paper/main.tex`, PDF |
| Search for additional rigorous mathematics | Partly fulfilled | Expanded with new certified deductions | Sections on equivariance, vector fields, fiber topology, and real volume |
| Audit all earlier claimed consequences | Mostly fulfilled | Explicitly classified | `CONSEQUENCES.md`, `LIMITATIONS.md` |
| Search primary sources and check priority/current status | Fulfilled as of the status date | Fulfilled, with same-day overlap disclosed | bibliography and source/status sections |
| Avoid overclaiming novelty or peer-review status | Fulfilled | Fulfilled | abstract, README, limitations, citation metadata |
| Provide reproducible scripts and tests | Fulfilled | Expanded from five to eight test groups | `src/verify.py`, `tests/test_map.py`, CI workflow |
| Provide Markdown and LaTeX/PDF | Fulfilled | Fulfilled and visually rechecked after revision | `paper/`, `output/pdf/` |
| Make the work usable by people and machine indexing | Mostly fulfilled | Strengthened | README, `CITATION.cff`, licenses, CI, consequence ledger |
| Publish a new public GitHub repository | Not fulfilled: invalid saved token | Pending user reauthentication | `gh auth login -h github.com` required |
| Open a draft PR if a new repository cannot be created | Not applicable without a selected target repository | Not required if public repository creation succeeds | GitHub step pending |
| Guarantee that the mathematics is accepted by experts | Not possible to guarantee | Explicitly not claimed | peer review and independent expert review remain external steps |

## Remaining external step

The local repository is complete and committed. GitHub publication requires a
valid authenticated account. Once `gh auth login -h github.com` succeeds, the
intended action is to create `jacobian-counterexample-audit` as a **public**
repository, push `main`, set an accurate description and topics, and verify the
public files and Actions run.
