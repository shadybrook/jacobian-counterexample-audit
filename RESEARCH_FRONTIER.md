# Research frontier after the announced Keller counterexample

Status: 21 July 2026. This is a problem ledger, not a novelty claim. A result
is called proved here only when a proof is present in `paper/main.md` and its
finite identities are covered by `src/verify.py`.

## Results completed in the 21 July revision

### 1. Equivariant quotient square law

For every Keller map equivariant for source weights `(1,-1,-2)` and target
weights `(-2,-1,1)`, the quotient Jacobian is

```text
det(D quotient) = det(D map) * (C/x)^2.
```

Thus the ramification in the announced two-dimensional quotient is forced by
the representation weights whenever `C/x` is nonconstant. This answers the
proposed quotient-obstruction question for this precise equivariant class. It
does not cover arbitrary torus weights or arbitrary dimensional reductions.

### 2. Total directional incompleteness

Every nonzero constant linear combination of the three inverse-Jacobian vector
fields is holomorphically incomplete and is not locally nilpotent. The proof
uses the exact omitted curve: a complete flow would translate some image point
onto a target that has no preimage. An explicit integral curve of the second
field escapes at finite time.

More generally, a complex Keller map is an automorphism if and only if all its
dual inverse-Jacobian fields are holomorphically complete. This converts a
global inversion problem into a completeness problem for commuting polynomial
ordinary differential equations.

### 3. Exact finite-field statistics

Closed formulas now count targets over every finite field of odd
characteristic with zero, one, or three rational preimages. The limiting
proportions are `1/3`, `1/2`, and `1/6`, exactly the proportions of three-cycles,
transpositions, and the identity in `S_3`.

This also highlights an arithmetic/geometric distinction. Geometrically the
complex map omits a curve, but over a large finite field roughly one third of
all rational targets have no rational preimage; most acquire preimages only
after extending the field.

## Investigated ideas that are not new theorems

### Finite completion in general

The statement that a nonproper Keller map embeds into a finite completion is
an application of Zariski's Main Theorem. It is therefore not a new principle.
The research content must lie in classifying when the completion is smooth,
when its boundary equals the ramification divisor, and when deleting that
boundary produces affine space.

### Direct Weyl and Poisson lifts

The explicit rank-three witnesses are important consequences, but extending a
Jacobian map to differential-operator and cotangent Poisson endomorphisms is a
known general construction. The displayed formulas are useful explicit
witnesses, not a new equivalence theory.

### Generic degree three and monodromy

The cubic and `S_3` monodromy materially overlap the same-day MathOverflow
record. They remain essential infrastructure for the new arithmetic result,
but priority is not claimed.

## Highest-value next theorem targets

### A. Classify the equivariant class

The square law reduces the three-dimensional Keller condition to a planar
Jacobian equation with a prescribed square factor. The next target is to
classify polynomial triples `(a,b,h)` for which

```text
(alpha,beta) = (h^2 a, h b),   det D(alpha,beta) = c h^2
```

and which satisfy the divisibility conditions needed to lift back to
polynomials of weights `(-2,-1,1)`. A classification could explain whether the
announced construction is forced inside a natural equivariant category and
could generate all such counterexamples.

### B. A boundary-complement classification theorem

Classify finite smooth threefolds `I -> A^3` of degree three having a
ramification divisor `D` such that

```text
I \ D is isomorphic to A^3,  and  D is isomorphic to A^2.
```

Even a theorem under the additional affine-plane-torsor hypothesis would go
beyond the automatic Zariski-Main completion and could isolate the true
geometric mechanism.

### C. Galois-closure geometry

The ordered-root cover is an open subset of the configuration space of three
ordered points on `P^1`, hence an open subset of `PGL_2`. Determine the deleted
divisor explicitly, its fundamental group, Picard group, and compactification.
This may turn the `S_3` statement into a complete topological model of every
inverse branch and every escape to infinity.

### D. Arithmetic collision varieties

The off-diagonal fiber product

```text
(A^3 x_F A^3) \ diagonal
```

is the ordered-root/Galois-closure space over the regular locus. The
finite-field theorem implies that its number of rational points is
`(q-1)(q^2+2)` outside characteristics two and three. Identify its exact
geometric decomposition and motivic class, then extend the computation to the
higher-generic-degree weighted lifts.

### E. Quantitative flow singularities

Every constant direction is incomplete. Classify the pole order and escape
divisor of the lifted flow for a generic target line. A general theorem
relating flow singularities to intersection multiplicities with the
nonproperness divisor could connect polynomial ODEs directly to the finite
completion.

### F. Minimal ordinary degree

The existing counterexample has total degree seven. Degrees four, five, and
six remain the immediate search range. A rigorous attack requires a precisely
defined normal form, coefficient scheme, symmetry quotient, exact elimination,
and independently checkable infeasibility certificates. Numerical searches
alone cannot prove minimality.

### G. The plane filling problem

For fixed nonzero first coordinate, the remaining map is etale on
`A^2 \ {xy=-1}`. Formulate a logarithmic or valuation-theoretic obstruction to
filling the deleted hyperbola while preserving a unit Jacobian. A theorem must
distinguish a mere failure of the displayed formulas to extend from a genuine
obstruction applying to a class of modifications.

### H. Optimized cubic-homogeneous and Druzkowski witnesses

Stable reduction guarantees higher-dimensional special-form counterexamples.
The concrete problem is to minimize the number of auxiliary variables while
preserving an explicit collision and a mechanically certified constant full
Jacobian. A naive arithmetic-circuit graph lift does not suffice.

## Standards before announcing a discovery

1. State the field, hypotheses, equivalence relation, and exceptional
   characteristics exactly.
2. Separate symbolic identities from geometric or literature-dependent
   deductions.
3. Include an exact verifier and tests, but also give a human proof.
4. Search current public notes and older primary literature for the exact
   statement and its natural generalizations.
5. Ask subject experts to try to falsify the result before making a priority
   claim.
6. Label a computation for this one map as such; call it a new theorem only
   when it applies to a stated class and has survived independent checking.
