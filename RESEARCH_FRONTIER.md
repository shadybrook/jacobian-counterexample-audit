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

### 4. The Galois closure is an explicit complement in PGL(2)

The full ordered-root cover, equivalently the off-diagonal collision variety,
is

```text
U = PGL(2) \ H,
H = V(a^2 d + 2abc + 2abd + b^2 c).
```

The divisor is smooth and has the product description

```text
H is isomorphic to (A^1 \ {0,-1}) x G_m.
```

Consequently `[U]=(L-1)(L^2+2)` in the Grothendieck ring. Over every finite
extension of a finite field of characteristic other than two or three,
`#U(F_{q^m})=(q^m-1)(q^(2m)+2)`, giving an explicit zeta function. This
completes the proposed arithmetic collision-variety target for the cubic map.

### 5. Quantitative escape exponents

For a target arc transverse to the smooth discriminant, the two disappearing
inverse branches have Puiseux escape order `x ~ epsilon^(-1/2)`. At a generic
arc through the cuspidal omitted curve, all three branches escape with order
`x ~ epsilon^(-2/3)`. The exponents follow from exact double- and triple-root
normal forms and the reconstruction formula `x=2/P'(t)`.

For target lines these are movable algebraic singularities of the
inverse-Jacobian flows. Tangential directions can have different exponents and
remain to be classified.

### 6. Maximal monodromy in every generic degree

For any characteristic-zero polynomial `R` of degree `n`, the two-parameter
polynomial

```text
R(w) - P*w + Q
```

has Galois group `S_n` over `C(P,Q)`. The proof uses the tangent-line map
`w -> (R'(w), R(w)-wR'(w))`, the identity `dB=-w dA`, and the standard
monodromy of a Morse polynomial.

Applied to the contemporaneous one-variable weighted lifts, this proves that
their dimension-three Keller counterexamples have full `S_n` monodromy in
every generic degree `n >= 3`. The all-degree construction belongs to the
cited public note; the uniform monodromy deduction is proved in our paper.

### 7. Exact ordinary-degree growth in the one-variable family

If the seed polynomial has degree `d >= 2`, the weighted lift has component
degrees

```text
(5d-3, 5d-4, 4)
```

and generic degree `d+1`. Thus its total degree is `5n-8` at generic degree
`n`. The announced map is forced to have total degree seven inside this
particular construction. This is a restricted minimality statement only; it
does not eliminate degrees four, five, or six in the full Keller problem.

### 8. Restricted classification of the completion torsor

Torsors under `E=O(-1)+O(-2)` are classified by
`H^1(P^1,E)=0+k`. Bundle automorphisms act transitively on nonzero classes.
Therefore the completion is, up to an automorphism of `E`, the unique
nontrivial `E`-torsor over `P^1`.

This classifies the affine-plane bundle under the exact bundle hypothesis. It
does not yet classify the finite map to `A^3`, the boundary embedding, or all
smooth completions with complement `A^3`.

### 9. A sharp no-go theorem for filling the displayed plane slice

For fixed nonzero first output, let `(Q_p,R_p)` be the etale map on
`A^2 \ {xy=-1}`. Every nonconstant element of `k[Q_p,R_p]` has a pole along
the missing hyperbola. Equivalently,

```text
k[Q_p,R_p] intersection k[x,y] = k.
```

Thus no polynomial postcomposition, including no polynomial target
automorphism, can make this slice extend across the hyperbola. Any successful
plane mechanism must change more than the target coordinates of this slice.

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

The one-variable subfamily now has known maximal monodromy in every degree;
the remaining problem is to determine whether every equivariant example is
polynomially equivalent to such a lift or whether genuinely different
monodromy and boundary types occur.

### B. A boundary-complement classification theorem

Classify finite smooth threefolds `I -> A^3` of degree three having a
ramification divisor `D` such that

```text
I \ D is isomorphic to A^3,  and  D is isomorphic to A^2.
```

Even a theorem under the additional affine-plane-torsor hypothesis would go
beyond the automatic Zariski-Main completion and could isolate the true
geometric mechanism. The underlying `O(-1)+O(-2)` torsor is now classified;
the remaining content lies in the finite map and its distinguished divisor.

### C. Topology of the explicit Galois-closure complement

The ordered-root cover and deleted divisor are now explicit. Determine the
fundamental group, Picard group, cohomology ring, and a normal-crossings
compactification of

```text
PGL(2) \ ((A^1 \ {0,-1}) x G_m).
```

This may turn the algebraic `S_3` statement into a complete topological model
of every inverse branch and every escape to infinity.

### D. Higher-degree arithmetic collision varieties

The off-diagonal fiber product

```text
(A^3 x_F A^3) \ diagonal
```

is the ordered-root/Galois-closure space over the regular locus. For the cubic
map its decomposition, motivic class, and extension-field zeta function are
now proved. Extend the computation to higher-generic-degree weighted lifts,
where the ordered-root space is an open subset of the configuration space of
`d` points on `P^1` and the omitted coefficient defines a new divisor.

### E. Full classification of flow singularities

The generic transverse exponents `1/2` and `2/3` are proved. Classify tangent
lines and higher-contact arcs. A general theorem should express the Puiseux
exponents of lifted flows in terms of contact order with the discriminant and
root multiplicity in the finite completion.

### F. Minimal ordinary degree

The existing counterexample has total degree seven. Degrees four, five, and
six remain the immediate search range. A rigorous attack requires a precisely
defined normal form, coefficient scheme, symmetry quotient, exact elimination,
and independently checkable infeasibility certificates. Numerical searches
alone cannot prove minimality.

### G. The plane filling problem

For fixed nonzero first coordinate, the remaining map is etale on
`A^2 \ {xy=-1}`. Formulate a logarithmic or valuation-theoretic obstruction to
filling the deleted hyperbola while preserving a unit Jacobian. Polynomial
postcomposition has now been ruled out completely. The remaining problem is
to study source modifications, logarithmic fillings, or deformations of the
map itself and to prove an obstruction for one of those broader classes.

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
