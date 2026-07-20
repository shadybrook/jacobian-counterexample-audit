# Five deeper directions from the three-dimensional Keller counterexample

**Status:** independent research memorandum, 21 July 2026.  This document
distinguishes proved statements, exact computer checks, classical consequences,
and conjectural extensions.  It is not peer reviewed and makes no claim of
historical priority.

## Executive result

Five directions were selected because they connect the announced map to
different parts of mathematics while still permitting exact progress now:

| Direction | Outcome of this audit | Status |
|---|---|---|
| Divisorial filling | A general residue-ratio obstruction theorem | Proved |
| Collision geometry | The collision variety is affine, smooth, factorial, has trivial Picard group, and has one independent nonconstant unit | Proved |
| Inverse-Jacobian dynamics | Complete directions form a vector space contained in the translation stabilizer of the image | Proved |
| Escape at infinity | Contact-order and Newton-polygon formulas classify a large class of tangent and cuspidal escapes | Proved under explicit nondegeneracy hypotheses |
| Maximal monodromy | No radical inverse for generic degree at least five; finite-field fibers follow fixed-point statistics of `S_n` | First claim proved; arithmetic claim follows from finite-field Chebotarev at good reductions |

These results are not a second breakthrough comparable to the counterexample.
They are reusable structural deductions prompted by it. Searches of indexed
sources did not locate these exact formulations for this map, but absence from
a search is not proof of novelty.

## 1. A general residue-ratio obstruction to polynomial filling

### Theorem 1 (residue-ratio obstruction)

Let \(\bar X\) be a normal irreducible variety over a field \(k\), let
\(D\subset\bar X\) be a prime divisor, and let \(v_D\) be its divisorial
valuation. Suppose \(f,g\in k(\bar X)\) satisfy

\[
v_D(f)=v_D(g)=-1.
\]

Choose a uniformizer \(s\) at the generic point of \(D\), and let

\[
f_0=(sf)|_D,\qquad g_0=(sg)|_D\in k(D)^*.
\]

If \(g_0/f_0\) is nonconstant in \(k(D)\), then every nonconstant polynomial
\(H\in k[U,V]\) satisfies

\[
v_D(H(f,g))=-\deg H.
\]

Consequently,

\[
k[f,g]\cap \mathcal O_{\bar X,\eta_D}=k,
\]

and hence \(k[f,g]\cap\Gamma(\bar X,\mathcal O_{\bar X})=k\) whenever the
latter ring is viewed inside \(k(\bar X)\).

### Proof

Let \(m=\deg H>0\), and let \(H_m\) be the top homogeneous part. Multiplying
by \(s^m\) and reducing at the generic point of \(D\) gives

\[
(s^mH(f,g))|_D=H_m(f_0,g_0)
=f_0^m H_m(1,g_0/f_0).
\]

A nonconstant element of \(k(D)\) is transcendental over \(k\). Therefore the
nonzero one-variable polynomial \(H_m(1,T)\) cannot vanish at \(g_0/f_0\).
The displayed residue is nonzero, proving that the pole order is exactly
\(m\).  This proves the theorem.

### Application to the fixed-\(P\) plane slice

For \(p\ne0\), put \(s=1+xy\) and

\[
S_p=R_p+\frac{Q_p^3}{27p^2}.
\]

The already certified residues are

\[
(sQ_p)|_D=3px,
\qquad
(sS_p)|_D=\frac{6px^2+1}{3px},
\]

so their ratio is

\[
\frac{2}{3p}+\frac{1}{9p^2x^2},
\]

which is nonconstant on \(D\cong\mathbb G_m\). Theorem 1 therefore recovers
and generalizes

\[
k[Q_p,R_p]\cap k[x,y]=k.
\]

### Why this matters

This converts an example-specific Laurent expansion into a portable test for
compactification and filling problems. Whenever two observables have the same
pole divisor, their projective residue map

\[
D\dashrightarrow\mathbb P^1,\qquad z\mapsto[f_0(z):g_0(z)]
\]

detects whether polynomial combinations can cancel that pole. A nonconstant
map forbids every nonconstant cancellation at once. The method is relevant to
affine modifications, logarithmic geometry, rational coordinate charts, and
polynomial inverse problems; it is not limited to Keller maps.

A next theorem should treat unequal pole orders using weighted-homogeneous top
parts and a residue map to a weighted projective space.

## 2. The collision variety is a factorial affine threefold

Let \(\mathcal C\) be the off-diagonal collision variety. The paper proves

\[
\mathcal C\cong
U=\operatorname{PGL}_2\setminus V(E),
\]

where, in homogeneous matrix coordinates \([a:b:c:d]\in\mathbb P^3\),

\[
D=ad-bc,
\qquad
E=a^2d+2abc+2abd+b^2c.
\]

Equivalently,

\[
U=\mathbb P^3\setminus\bigl(V(D)\cup V(E)\bigr)
=D_+(DE).
\]

The quadric \(D\) and cubic \(E\) are irreducible and distinct in
characteristic different from \(2,3\). Irreducibility of \(E\) also follows
directly because it is primitive and linear in \((c,d)\), with coprime
coefficients \(b(2a+b)\) and \(a(a+2b)\).

### Theorem 2 (factoriality and units)

Over an algebraically closed field of characteristic different from \(2,3\),
the collision variety \(\mathcal C\) is a smooth affine factorial threefold.
Moreover,

\[
\operatorname{Cl}(\mathcal C)
=\operatorname{Pic}(\mathcal C)=0,
\]

and

\[
\Gamma(\mathcal C,\mathcal O)^*/k^*\cong\mathbb Z.
\]

One generator of the unit group modulo constants is

\[
\boxed{\;D^3/E^2\;}.
\]

The canonical line bundle is consequently trivial.

### Proof

The open set \(D_+(DE)\) is affine and is smooth because it is open in
\(\mathbb P^3\). The localization sequence for Weil divisor class groups gives

\[
\mathbb Z[V(D)]\oplus\mathbb Z[V(E)]
\longrightarrow \operatorname{Cl}(\mathbb P^3)\cong\mathbb Z
\longrightarrow \operatorname{Cl}(U)\longrightarrow0.
\]

The first map is \((m,n)\mapsto2m+3n\). Since \(\gcd(2,3)=1\), it is
surjective, so \(\operatorname{Cl}(U)=0\). A smooth affine normal domain with
trivial class group is a UFD, and smoothness also identifies Picard and divisor
class groups.

The units exact sequence identifies units modulo constants with the kernel of
\((m,n)\mapsto2m+3n\). This kernel is generated by \((3,-2)\), represented by
the degree-zero rational function \(D^3/E^2\). Finally, the canonical bundle
is a line bundle and hence trivial because \(\operatorname{Pic}(U)=0\).

### Further exact consequences

The previously proved motivic class gives

\[
[\mathcal C]=(\mathbb L-1)(\mathbb L^2+2).
\]

Therefore its compactly supported Hodge--Deligne polynomial is

\[
E_c(\mathcal C;u,v)=(uv-1)((uv)^2+2),
\]

and its compactly supported Euler characteristic is zero. This does not by
itself determine the full cohomology ring or fundamental group.

### Why this matters

The entire space of ordered collisions has unique factorization even though it
supports nontrivial \(S_3\) monodromy and records escape to infinity. Thus the
global obstruction is not hidden divisor-class torsion. This narrows future
topological work: nontriviality must be carried by the boundary arrangement,
fundamental group, and monodromy rather than by the Picard group.

The variety is also a compact benchmark for algorithms computing class groups,
units, monodromy, and cohomology of affine complements.

## 3. Complete inverse-Jacobian directions and translation symmetry

Let \(G:\mathbb A^n_\mathbb C\to\mathbb A^n_\mathbb C\) be a Keller map and
let \(\delta_1,\ldots,\delta_n\) be the commuting polynomial vector fields
dual to \(dG_1,\ldots,dG_n\). For \(a\in\mathbb C^n\), put

\[
\delta_a=\sum_i a_i\delta_i.
\]

Define

\[
\mathrm{Comp}(G)=
\{a\in\mathbb C^n:\delta_a\text{ is holomorphically complete}\}
\]

and, for \(Y=G(\mathbb A^n)\),

\[
\mathrm{Stab}_{\mathrm{tr}}(Y)=
\{a:Y+ta=Y\text{ for every }t\in\mathbb C\}.
\]

### Theorem 3 (translation-stabilizer obstruction)

The set \(\mathrm{Comp}(G)\) is a complex vector subspace and

\[
\boxed{\mathrm{Comp}(G)\subseteq\mathrm{Stab}_{\mathrm{tr}}(Y).}
\]

Equivalently, if \(Y=\mathbb A^n\setminus Z\), every complete direction must
preserve the omitted set \(Z\) under all translations in that direction.

### Proof

The inverse-Jacobian fields commute. If \(\delta_a\) and \(\delta_b\) are
complete, their global commuting flows compose to give the flow of
\(\delta_{a+b}\); scalar multiples are complete by reparametrization. Thus
\(\mathrm{Comp}(G)\) is a vector subspace.

For the flow \(\phi_t^a\), the chain rule gives

\[
\frac{d}{dt}G(\phi_t^a(x))=a,
\qquad
G(\phi_t^a(x))=G(x)+ta.
\]

If the flow exists for every complex \(t\), then \(Y+ta\subseteq Y\); using
\(-t\) gives equality. This proves the inclusion.

### Corollary for the announced map

Here

\[
Y=\mathbb A^3\setminus\Gamma,
\qquad
\Gamma=\left\{\left(q^2/12,q,4/(3q)\right):q\ne0\right\}.
\]

The irreducible curve \(\Gamma\) is not an affine line. If it were invariant
under a nonzero translation direction, each translation orbit would be a line
contained in \(\Gamma\), forcing the irreducible one-dimensional variety
\(\Gamma\) itself to be that line. Hence

\[
\mathrm{Stab}_{\mathrm{tr}}(Y)=0
\quad\text{and}\quad
\mathrm{Comp}(F)=0.
\]

This supplies a conceptual proof of total directional incompleteness.

### Why this matters

The theorem replaces integration of complicated polynomial vector fields by a
geometric calculation on the image. For a future Keller map, computing the
translation stabilizer of its omitted locus immediately bounds the dimension
of its complete inverse frame. It connects global inversion to additive group
actions, locally nilpotent derivations, affine geometry, and completeness of
flat algebraic affine structures.

The converse is false without additional path-lifting hypotheses: translation
invariance of the image does not alone guarantee that a lifted trajectory
cannot escape inside the finite completion. Determining hypotheses under which
equality holds is a precise next problem.

## 4. Contact order and a Newton polygon for escape rates

The original paper proved transverse exponents \(1/2\) at a smooth point of
the discriminant and \(2/3\) at its cuspidal edge. These can be extended.

### Theorem 4A (arbitrary contact at a smooth discriminant point)

Let a target arc meet the smooth discriminant with finite intersection
multiplicity

\[
k=\operatorname{ord}_\epsilon\Delta(\gamma(\epsilon)).
\]

Choose a projective root chart in which the leading coefficient is a unit. The
two branches converging to the double boundary root satisfy

\[
t_+-t_-\asymp\epsilon^{k/2},
\qquad
K'(t_\pm)\asymp\epsilon^{k/2},
\qquad
\boxed{x_\pm\asymp\epsilon^{-k/2}}.
\]

Thus tangency of order \(k\) multiplies the pole order by \(k\). The earlier
square-root law is the case \(k=1\).

### Proof

Near a split double root, the leading coefficient and the differences from the
third root are units. The cubic discriminant is therefore a unit times
\((t_+-t_-)^2\). At either root, the derivative is a unit times
\(t_+-t_-\). The reconstruction identity \(x=2/K'(t)\) proves the result.

### Theorem 4B (Newton polygon at the omitted cusp)

Near \(\Gamma\), the leading coefficient \(r\) is nonzero. Depress the cubic
exactly by writing

\[
T=W+\frac{2}{3r},
\qquad
\frac{K(T)}r=W^3+A W+B,
\]

where

\[
A=\frac qr-\frac4{3r^2},
\qquad
B=-\frac{2p}{r}+\frac{2q}{3r^2}-\frac{16}{27r^3}.
\]

Both \(A\) and \(B\) vanish on \(\Gamma\), and the exact discriminant identity
is

\[
\operatorname{Disc}(K)=r^4(-4A^3-27B^2).
\]

Let \(\alpha=\operatorname{ord}A\) and
\(\beta=\operatorname{ord}B\), and suppose the target arc lies off the
discriminant for \(\epsilon\ne0\). Then, provided the first rescaled cubic is
separable in the equality case:

1. If \(2\beta<3\alpha\), all three roots have
   \(\operatorname{ord}W=\beta/3\), and
   \[
   x\asymp\epsilon^{-2\beta/3}.
   \]
2. If \(2\beta>3\alpha\), two roots have order \(\alpha/2\), the third has
   order \(\beta-\alpha\), and all three branches satisfy
   \[
   x\asymp\epsilon^{-\alpha}.
   \]
3. If \(2\beta=3\alpha\) and the leading rescaled cubic is separable, all
   roots have order \(\alpha/2=\beta/3\), and
   \[
   x\asymp\epsilon^{-\alpha}.
   \]

In all nondegenerate cases the common pole exponent is therefore

\[
\boxed{\kappa=\min\left(\alpha,\frac{2\beta}{3}\right).}
\]

Moreover \(y\to t_0\) and \(z=O(\epsilon^\kappa)\).

### Proof

The lower Newton polygon of \(W^3+AW+B\) uses the points
\((3,0),(1,\alpha),(0,\beta)\). Its slopes give the root valuations listed
above. Substitution into \(3W^2+A\) shows that every simple root has derivative
valuation \(2\beta/3\) in the first case and \(\alpha\) in the other two.
The reconstruction formulas then give \(x\), \(y\), and \(z\).

If the rescaled cubic in the equality case has a multiple root, the orders
\((\alpha,\beta)\) alone do not determine the answer; one must continue the
Newton--Puiseux algorithm. This is an explicit limitation, not an omitted
genericity detail.

### Why this matters

The result turns “failure at infinity” into a quantitative singularity
spectrum. It can guide adaptive numerical continuation: the exponent predicts
how quickly coordinates blow up as a target path approaches the nonproperness
set. It also relates the finite completion to Newton polygons, Puiseux series,
singularity theory, and incomplete polynomial flows.

## 5. Algorithmic and arithmetic consequences of maximal monodromy

The paper proves that the inverse equation

\[
R(w)-Pw+Q=0
\]

has geometric Galois group \(S_n\) when \(\deg R=n\) in characteristic zero.

### Theorem 5A (generic inverse branches are not solvable by radicals)

For \(n\ge5\), no generic inverse branch in this family can be expressed over
\(k(P,Q)\) by a tower of radicals.

### Proof

An algebraic equation is solvable by radicals only if its Galois group is
solvable. The symmetric group \(S_n\) is not solvable for \(n\ge5\). Since the
inverse equation has Galois group \(S_n\), a radical expression for a generic
root cannot exist.

This does not prevent numerical approximation, local analytic continuation,
or formulas using more general special functions. It says that the familiar
quadratic/cubic/quartic radical paradigm provably stops at generic degree five.

### Theorem 5B (finite-field fiber law at good reductions)

Fix \(n\) and a member of the family defined over a number field. At reductions
where the regular inverse cover remains geometrically connected with group
\(S_n\), finite-field Chebotarev implies that the proportion of regular target
points with exactly \(j\) rational inverse branches approaches

\[
\boxed{
\Pr(N=j)=\frac{\binom nj D_{n-j}}{n!}
}
\]

as the finite field grows, with a square-root error after fixing the model.
Here

\[
D_m=m!\sum_{i=0}^m\frac{(-1)^i}{i!}
\]

is the number of derangements of \(m\) letters. The formula is simply the
proportion of permutations in \(S_n\) having exactly \(j\) fixed points,
because rational simple roots are Frobenius-fixed sheets.

For \(n=3\) this recovers

\[
\Pr(0)=\frac13,
\qquad
\Pr(1)=\frac12,
\qquad
\Pr(3)=\frac16.
\]

For fixed \(j\) and \(n\to\infty\), the distribution tends the Poisson law of
mean one:

\[
\Pr(N=j)\longrightarrow\frac{e^{-1}}{j!}.
\]

In particular the mean number of rational preimages remains exactly one in the
permutation model, while the omitted-target proportion approaches \(e^{-1}\).

### Why this matters

Maximal monodromy gives a lower bound on exact symbolic inversion complexity
and tells continuation algorithms that all \(n\) branches can be permuted.
The finite-field law supplies predictable datasets for testing point-counting,
factorization, and monodromy software. It also shows why these maps are not
cryptographic permutations: a large fraction of targets have no rational
preimage, while others have several.

The finite-field statement is asymptotic at good reductions, not an exact
formula for every prime or every member. Exact counts require the geometry of
the particular ordered-root space, as achieved for the cubic.

## Real-world usefulness: a calibrated assessment

There is no justified claim that this work immediately changes engineering,
medicine, finance, or cryptography. Its near-term usefulness is primarily in
mathematics and mathematical computation:

1. **Reliable symbolic-computation benchmark.** The map combines a constant
   local Jacobian with global collisions, missing values, monodromy, and
   singular escape. It is a unusually compact adversarial example for computer
   algebra and formal theorem-proving systems.
2. **Nonlinear inverse-problem benchmark.** It demonstrates exactly how a
   nonsingular derivative can coexist with global ambiguity when properness is
   absent. Numerical continuation software can be tested against the proved
   square-, cube-, and higher-contact escape laws.
3. **Polynomial-flow benchmark.** The commuting polynomial frame is
   everywhere nonsingular and divergence free, yet every nonzero constant
   direction is incomplete over \(\mathbb C\). This is a clean test case for
   detecting finite-time escape in complex polynomial ODEs.
4. **Arithmetic benchmark.** The cubic has exact finite-field fiber counts,
   while the higher-degree family has a predicted `S_n` fixed-point law. This
   is useful for testing Galois-group, point-counting, and factorization
   algorithms.
5. **Geometry of affine complements.** The smooth factorial collision variety,
   its unit, and its boundary arrangement provide a small explicit laboratory
   for affine geometry, monodromy, divisor complements, and motivic invariants.

The broader lesson—relevant far beyond this example—is that local
nonsingularity, global solvability, algebraic expressibility, and numerical
stability are four different properties. This example separates all four in a
form that can be calculated exactly.

## Five next conjectures generated by the audit

These are research targets, not results.

1. **Weighted residue theorem.** Extend Theorem 1 to functions of unequal pole
   order using a dominant residue map to weighted projective space.
2. **Collision-complement topology.** Compute \(\pi_1(U)\), the integral
   cohomology ring, and the map \(\pi_1(U)\twoheadrightarrow S_3\). The class
   group calculation shows that Picard theory will not detect this topology.
3. **Completeness equality criterion.** Find geometric path-lifting hypotheses
   under which
   \(\mathrm{Comp}(G)=\mathrm{Stab}_{\mathrm{tr}}(G(\mathbb A^n))\).
4. **Full Newton tree.** Classify the exceptional equality case in Theorem 4B
   and all arcs contained in the discriminant using an iterated Newton tree of
   the finite completion.
5. **Exact higher-degree fiber enumerators.** Replace the Chebotarev asymptotic
   in Theorem 5B by exact formulas for the weighted-lift families, analogous to
   the cubic count.

## Verification and source boundary

The accompanying test file `tests/test_five_directions.py` checks exactly:

- irreducibility factorizations for \(D\) and \(E\);
- the depressed-cubic substitution;
- the discriminant identity \(r^4(-4A^3-27B^2)\);
- the `S_n` fixed-point probabilities for \(3\le n\le8\), including total mass
  one and mean one.

The divisor-valuation formalism is standard; see the
[Stacks Project discussion of Weil divisors](https://stacks.math.columbia.edu/tag/0BE0).
The use of a finite completion is an application of
[Zariski's Main Theorem](https://stacks.math.columbia.edu/tag/05W7), not a new
general principle. Quantitative nonproperness sets have an established
literature, including
[Jelonek--Lasoń](https://arxiv.org/abs/1411.5011). The relation between
Frobenius classes and finite-field fibers follows finite-field Chebotarev; a
convenient primary reference is
[Meagher, *A simple proof of Chebotarev's density theorem over finite fields*](https://doi.org/10.1017/S0004972718000448).

The cubic, degree-three extension, and `S_3` calculation overlap the
[same-day MathOverflow discussion](https://mathoverflow.net/questions/513387/).
The all-degree family overlaps the
[same-day weighted-lift discussion](https://mathoverflow.net/questions/513390/)
and the public source cited in the main paper. The results above should be
presented as candidate independent deductions until expert review and a fuller
literature search establish priority.
