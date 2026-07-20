# Exact audit of an announced three-dimensional Keller map

Public repository: <https://github.com/shadybrook/jacobian-counterexample-audit>

This repository independently checks and analyzes the polynomial map announced
by Levent Alpoge on 20 July 2026. The core calculation is exact:

\[
\det DF=-2,
\]

and three distinct rational points have the same image. Under the standard
definition, this is a counterexample to the Jacobian Conjecture in dimension
three.

This is an **independent working note**, not a peer-reviewed publication and
not a claim of priority. The original map must be credited to the announcement
linked below. Several structural observations also appeared in same-day public
notes; the paper records those overlaps explicitly.

## Contents

- `paper/main.md`: readable paper in Markdown.
- `paper/main.tex`: typeset LaTeX source.
- `output/pdf/jacobian_counterexample_audit.pdf`: built paper, when present.
- `src/verify.py`: exact symbolic certificate using SymPy.
- `tests/test_map.py`: regression tests for the main identities.
- `CONSEQUENCES.md`: claim-by-claim ledger of implications and non-implications.
- `RESEARCH_FRONTIER.md`: proved new deductions, rejected routes, and the
  highest-value next theorem targets.
- `PROMPT_AUDIT.md`: fulfillment check against the original project request.
- `paper/references.bib`: bibliography.
- `LIMITATIONS.md`: scope, status, provenance, and non-claims.

## Reproduce the exact checks

Python 3.11 or later is recommended.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make verify
make test
```

The verifier uses symbolic expansion and exact rational arithmetic. No
floating-point equality is used for a theorem-level assertion.

The revision additionally certifies weighted equivariance, an infinite
rational collision family, the ramified two-dimensional weighted quotient,
discriminant scaling, divergence-free inverse-Jacobian vector fields, and the
factorization controlling the jumping fiber of the first coordinate. It now
also certifies the general equivariant quotient square law, an explicit
finite-time escaping inverse-Jacobian trajectory, and finite-field fiber-count
formulas with small-field regression checks.

To build the PDF, install a LaTeX distribution containing `latexmk`,
`pdflatex`, `amsmath`, `amsthm`, `hyperref`, and `booktabs`, then run:

```bash
make paper
```

## Primary public source and status

- [Levent Alpoge's announcement](https://x.com/__alpoge__/status/2079028340955197566), 20 July 2026 (UTC).

As of 21 July 2026, this audit found an announcement and several same-day
technical discussions, but no peer-reviewed paper by the announcer. The
polynomial identities themselves are finite exact calculations and do not
depend on peer review. Broader claims of novelty, historical priority, and
community acceptance do.

## Attribution

Credit for the displayed counterexample belongs to Levent Alpoge and the
discovery history stated in his announcement. This repository was prepared as
an independent, user-directed, AI-assisted audit. Add maintainer authorship
before archival citation if appropriate; do not erase the discovery credit or
the AI-assistance disclosure.

Code is MIT licensed. Paper and explanatory text are CC BY 4.0.
