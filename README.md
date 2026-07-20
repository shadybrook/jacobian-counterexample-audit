# Geometry and monodromy of a three-dimensional Keller counterexample

Public repository: <https://github.com/shadybrook/jacobian-counterexample-audit>

This repository develops a reproducible structural study of the polynomial map
announced by Levent Alpoge on 20 July 2026. It begins with an independent exact
certificate:

\[
\det DF=-2,
\]

and three distinct rational points have the same image. Under the standard
definition, this disproves the Jacobian Conjecture in dimension three. The
main purpose of the repository, however, is to understand the mathematics the
example opens up: its fibers, Galois closure, monodromy, behavior at infinity,
inverse-Jacobian dynamics, equivariant quotient, and obstruction to descending
the construction to the affine plane.

This is an **independent working note**, not a peer-reviewed publication and
not a blanket claim of priority. The original map must be credited to the
announcement linked below. Several structural observations also appeared in
same-day public notes; the paper records those overlaps explicitly.

## Strongest results developed here

The paper proves, with exact symbolic checks where applicable:

- an explicit ordered-root/Galois-closure model as the complement of a smooth
  hypersurface in `PGL_2`, including its product structure, Grothendieck class,
  and finite-field point counts;
- full symmetric-group monodromy `S_n` for every generic degree in the
  contemporaneous one-variable weighted-lift family, via a general theorem for
  `R(w)-Pw+Q` when `R` is a Morse polynomial;
- exact escape exponents at infinity: two inverse branches escape like
  `epsilon^(-1/2)` across a smooth discriminant point, while three escape like
  `epsilon^(-2/3)` at the omitted cusp;
- a strong plane-slice obstruction:
  `k[Q_p,R_p] \cap k[x,y]=k`, so no nonconstant polynomial in the two outputs
  fills across the deleted hyperbola, even after polynomial target
  postcomposition;
- a general square law for the Jacobian of weighted quotients, together with
  an explicit collapsed critical divisor in this example;
- commuting, divergence-free inverse-Jacobian vector fields that form a global
  algebraic frame, plus an explicit finite-time escaping trajectory and a
  completeness criterion relevant to invertibility;
- a finite smooth completion with boundary `A^2`, its affine-bundle/torsor
  description, and uniqueness of the nontrivial torsor up to bundle
  automorphism;
- ordinary-degree growth formulas for the all-degree family, exact real and
  finite-field fiber statistics, and a consequences ledger separating proved
  implications from open questions.

These are proof-level results about this example and its associated families,
not a claim of a second breakthrough comparable to the counterexample itself.
Some may be independently useful or new, but historical priority requires
expert literature review. `LIMITATIONS.md` and the paper state the known
overlaps and non-claims.

## Contents

- `paper/main.md`: readable paper in Markdown.
- `paper/main.tex`: typeset LaTeX source.
- `output/pdf/jacobian_counterexample_audit.pdf`: built paper, when present.
- `src/verify.py`: exact symbolic certificate using SymPy.
- `tests/test_map.py`, `tests/test_five_directions.py`, and
  `tests/test_referee_audit.py`: exact regression and adversarial tests for the
  main identities and the five-direction research audit.
- `CONSEQUENCES.md`: claim-by-claim ledger of implications and non-implications.
- `FIVE_DIRECTIONS.md`: five new deep investigations, with general theorems,
  proofs, realistic applications, and explicit next conjectures.
- `REFEREE_AUDIT_FIVE_RESULTS.md`: hidden-hypothesis audit, counterexamples to
  overbroad formulations, independent checks, and confidence assessments.
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

The verification suite covers the core certificate and the machine-checkable
identities used by the structural arguments. The paper distinguishes these
computer-checked identities from arguments proved in prose.

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
