# Referee-style audit of the five frontier results

**Audit date:** 21 July 2026
**Scope:** correctness, hidden hypotheses, independent checks, failure modes,
and literature boundary.
**Status:** internal adversarial review, not external peer review.

## Overall verdict

The five directions are mathematically substantive, but they do not all have
the same novelty or evidentiary status.

| Claim | Correctness verdict | Correction or qualification | Novelty assessment |
|---|---|---|---|
| Residue-ratio obstruction | Valid after correction | Require the residue ratio to be transcendental over the ground field; ``nonconstant'' suffices over an algebraically closed constant field | Elementary associated-graded valuation lemma; likely folklore in general form, valuable in this application |
| Factorial collision variety | Valid over the stated characteristic range | Treat the collision space as the off-diagonal open subscheme of the fiber product; use both irreducible boundary divisors in the localization sequence | The explicit calculation for this collision space is a plausible contribution; the class-group method is standard |
| Translation-stabilizer obstruction | Valid over \(\mathbb C\) | No converse has been proved; replace the earlier suggestion of falsity by a precise open question | Compact general observation, possibly folklore; application to this omitted curve is exact |
| Escape laws | Valid with explicit hypotheses | The identity \(x=2/K'(t)\) is tied to the finite \(t\)-chart; the degenerate equality case needs further Newton steps | The quantitative formulation for this map is a plausible useful contribution |
| Radical and finite-field consequences | Radical obstruction valid; finite-field law valid conditionally | State extension-field asymptotics at reductions retaining geometrically connected \(S_n\) Galois closure; not an exact law for every prime | Classical Galois/Chebotarev consequences applied to the new family, not new foundational theory |

The audit found no counterexample to the corrected versions. It did find one
genuine overgeneralization in the first theorem and one unjustified sentence
about the converse in the third; both are corrected in `FIVE_DIRECTIONS.md`.

## Standards used

Each result was tested at four levels when applicable:

1. **Definition-level proof:** reconstruct the claim without relying on the
   prose already in the paper.
2. **Independent algebraic formulation:** verify the same conclusion through
   a different invariant or normal form.
3. **Exact computation:** use rational arithmetic, polynomial factorization,
   finite-field enumeration, or Galois-group computation.
4. **Failure search:** weaken hypotheses deliberately and construct edge cases.

Computer checks are certificates for finite identities, not substitutes for
the class-group, flow-completeness, Newton-polygon, or Chebotarev arguments.

## 1. Residue-ratio obstruction

### Correct statement

Let \(X\) be normal and integral over \(k\), let \(D\) be a prime divisor,
and let \(v=v_D\). Suppose \(v(f)=v(g)=-1\). If, for a uniformizer \(s\),

\[
\theta=\frac{(sg)|_D}{(sf)|_D}\in k(D)
\]

is transcendental over \(k\), then for every nonconstant
\(H\in k[U,V]\),

\[
v(H(f,g))=-\deg H.
\]

### Associated-graded proof

Normality makes \(\mathcal O_{X,\eta_D}\) a DVR. Its valuation filtration has
associated graded ring

\[
\operatorname{gr}_v k(X)\cong k(D)[\tau,\tau^{-1}]
\]

after choosing the initial form \(\tau=\operatorname{in}_v(s)\). The initial
forms of \(f,g\) in degree \(-1\) are

\[
f_0\tau^{-1},\qquad g_0\tau^{-1}.
\]

For \(H\) of degree \(m\), its potential degree \(-m\) initial term is

\[
H_m(f_0,g_0)\tau^{-m}
=f_0^mH_m(1,\theta)\tau^{-m}.
\]

Transcendence of \(\theta\) makes this nonzero. Thus no cancellation raises
the valuation. This proof makes clear that the theorem is an initial-form
criterion in a valuation's associated graded ring.

### Failure of the broader field statement

The original wording said that a ``nonconstant'' residue ratio was enough over
an arbitrary field. This is false if ``nonconstant'' only means outside
\(k\). Let

\[
k=\mathbb R,\quad X=\operatorname{Spec}\mathbb C[s],\quad D=V(s),
\quad f=1/s,\quad g=i/s.
\]

Then \(g_0/f_0=i\notin\mathbb R\) but is algebraic over \(\mathbb R\), and

\[
f^2+g^2=0.
\]

Over \(\mathbb C\), or whenever \(k\) is algebraically closed in \(k(D)\),
the simpler word ``nonconstant'' is safe.

### Weighted strengthening

The same associated-graded proof establishes the proposed extension. If
\(v(f_i)=-w_i\), the top weighted-homogeneous part of a polynomial controls
its leading valuation. A Zariski-dense residue map

\[
D\dashrightarrow\mathbb P(w_1,\ldots,w_m)
\]

prevents all leading weighted forms from vanishing. This is a theorem, not
merely a conjectural direction. The open problem is to recognize density from
the geometry of a compactification.

### Application audit

For the slice, the residue ratio

\[
\frac{2}{3p}+\frac{1}{9p^2x^2}
\]

is a nonconstant rational function on \(D\cong\mathbb G_m\) over the
characteristic-zero field used in the paper. It is therefore transcendental.
The corrected theorem applies without loss.

### Confidence

**Very high.** The proof is one paragraph in a DVR and the weakened statement
has an explicit counterexample.

## 2. Factoriality and units of the collision space

### Scheme-level object

Define

\[
\mathcal C=(\mathbb A^3\times_F\mathbb A^3)\setminus\Delta_{\mathbb A^3}
\]

as an open subscheme of the fiber product. Since \(F\) is étale and separated,
the diagonal is both open and closed in the fiber product. The projection of
the fiber product to either source factor is étale, so \(\mathcal C\) is
smooth and reduced.

Over the discriminant complement, a pair of distinct inverse roots determines
the third root, hence an ordering of all three. Over the discriminant there is
at most one affine preimage, so the off-diagonal fiber is empty. The
reconstruction formulas therefore identify \(\mathcal C\), as a scheme, with
the ordered-root cover

\[
U=\mathbb P^3\setminus(V(D)\cup V(E)).
\]

This adds the scheme-theoretic justification that was compressed in the
working paper.

### Boundary irreducibility

The determinant \(D=ad-bc\) is irreducible. Write

\[
E=b(2a+b)c+a(a+2b)d.
\]

In characteristic different from three, the two coefficients are coprime in
\(k[a,b]\). Since \(E\) is primitive and linear in \((c,d)\), it is
irreducible. The paper works away from characteristics two and three, which is
more than sufficient.

### Class group and units

The complement is the standard affine open \(D_+(DE)\subset\mathbb P^3\).
Removing its two prime boundary divisors gives

\[
\mathbb Z[V(D)]\oplus\mathbb Z[V(E)]
\longrightarrow\operatorname{Cl}(\mathbb P^3)=\mathbb Z
\longrightarrow\operatorname{Cl}(U)\longrightarrow0.
\]

The first map is \((m,n)\mapsto2m+3n\), so

\[
\operatorname{Cl}(U)=0.
\]

Because \(U\) is smooth affine, this proves factoriality and
\(\operatorname{Pic}(U)=0\). The kernel of the degree map is generated by
\((3,-2)\), yielding

\[
\mathcal O(U)^*/k^*=\langle D^3/E^2\rangle\cong\mathbb Z.
\]

### Independent exact checks

The new test suite performs two checks not used in the proof:

1. Three rational matrices in \(U\) are converted into ordered projective
   roots, targets, and three reconstructed source points. Exact substitution
   verifies that every ordered triple gives three distinct points with the
   same image.
2. Direct enumeration of \(\mathbb P^3(\mathbb F_q)\) for
   \(q=5,7,11\) gives
   \[
   \#\operatorname{PGL}_2(\mathbb F_q)=q^3-q,
   \quad \#H(\mathbb F_q)=(q-2)(q-1),
   \quad \#U(\mathbb F_q)=(q-1)(q^2+2).
   \]

These tests catch sign or scaling errors in \(E\) and in the ordered-root
normalization. They do not prove the class-group exact sequence.

### Confidence

**Very high for correctness.** Historical novelty of the explicit invariants
remains unverified.

## 3. Translation stabilizers and complete inverse flows

### General proof

For a Keller map \(G\), the dual derivations satisfy

\[
\delta_i(G_j)=\delta_{ij},\qquad [\delta_i,\delta_j]=0.
\]

If \(\delta_a\) and \(\delta_b\) are complete, their commuting global flows
compose to give the flow of \(\delta_{a+b}\); scalar reparametrization handles
multiples. Hence complete directions form a vector subspace.

For the global flow \(\phi_t^a\),

\[
\frac d{dt}G(\phi_t^a(x))=a,
\qquad G(\phi_t^a(x))=G(x)+ta.
\]

Thus completeness forces translation invariance of the image. No algebraicity
of the flow is used; holomorphic completeness suffices.

### Independent stabilizer calculation

The omitted curve has ideal

\[
I_\Gamma=(12p-q^2,3qr-4)
\]

and parametrization \(p=q^2/12\), \(r=4/(3q)\). If translation in direction
\((A,B,C)\) preserves \(\Gamma\), the directional derivatives of both
generators vanish on the curve:

\[
12A-2qB=0,
\qquad 3rB+3qC=0.
\]

The first identity for every \(q\ne0\) gives \(A=B=0\); the second then gives
\(C=0\). This is an algebraic verification independent of the argument that a
translation-invariant irreducible curve must be a line.

### Converse status

The reverse inclusion has not been proved or disproved here. Translation
invariance of the image is necessary, but a chosen inverse branch also needs
global continuation along every translated line. The current finite
completion shows exactly where such continuation questions live. Any future
converse must state an explicit path-lifting or boundary-avoidance hypothesis.

### Confidence

**Very high for the inclusion and its application.** No novelty claim should
be made until experts in complete polynomial vector fields and additive group
actions assess whether the observation is standard.

## 4. Escape exponents

### Smooth discriminant

For the binary \(t\)-cubic

\[
rT^3-2T^2U+qTU^2-2pU^3,
\]

the root at infinity cannot be multiple because the \(T^2U\) coefficient is
the nonzero constant \(-2\). Hence the double boundary root at a smooth
discriminant point lies in the finite \(t\)-chart, where

\[
x=2/K'(t).
\]

If the pulled-back discriminant has order \(k\), the separation of the two
colliding roots has order \(k/2\). The remaining projective root separation is
a unit. Therefore \(K'(t)\) also has order \(k/2\), proving

\[
x\asymp\epsilon^{-k/2}.
\]

An exact local test uses the smooth discriminant point
\((p,q,r)=(0,1,1)\), where

\[
K(T)=T(T-1)^2.
\]

Perturbing \(2p\) by \(\epsilon^k\) and writing \(T=1+u\) gives

\[
u^2(1+u)-\epsilon^k=0,
\]

which independently exhibits \(u\asymp\epsilon^{k/2}\) and
\(K'\asymp\epsilon^{k/2}\) for \(k=1,2,3,4\).

### Cuspidal Newton polygon

At the triple-root curve, \(r\ne0\) and the exact depressed form is

\[
W^3+AW+B,
\quad
A=\frac qr-\frac4{3r^2},
\quad
B=-\frac{2p}{r}+\frac{2q}{3r^2}-\frac{16}{27r^3}.
\]

The symbolic suite independently verifies

\[
\operatorname{Disc}(K)=r^4(-4A^3-27B^2).
\]

For finite \(\alpha=v(A)\), \(\beta=v(B)\), the lower Newton polygon has
vertices among \((3,0),(1,\alpha),(0,\beta)\). This yields the three cases in
`FIVE_DIRECTIONS.md`. Direct substitution in \(3W^2+A\) verifies the claimed
derivative orders.

### Essential exceptional case

The family

\[
W^3-3\epsilon^2W+2\epsilon^3+\epsilon^N
\]

shows that the separability hypothesis in the equality case cannot be
removed. It always has \((\alpha,\beta)=(2,3)\), but after writing
\(W=\epsilon+u\),

\[
u^2(3\epsilon+u)+\epsilon^N=0.
\]

For \(N>3\), two roots have
\(v(u)=(N-1)/2\) and derivative valuation \((N+1)/2\); the third branch has
derivative valuation \(2\). Thus fixed \((\alpha,\beta)\) permits arbitrarily
large half-integral escape orders. The full Newton tree, not merely the first
polygon, is necessary.

### Confidence

**High under the corrected hypotheses.** A formal Newton--Puiseux proof in a
proof assistant or a specialist review would be the next validation level.

## 5. Maximal monodromy, radicals, and finite fields

### Generic \(S_n\) theorem

For \(R\in k[W]\) of degree \(n\ge2\) in characteristic zero, set

\[
f(W)=R(W)-PW+Q.
\]

Over \(k(P)\), the critical points of \(R(W)-PW\) solve
\(R'(W)=P\). They are simple: a common root with \(R''\) would make the
transcendental \(P\) equal to a constant. Their critical values are generically
distinct because the tangent-line parametrization

\[
W\mapsto(R'(W),R(W)-WR'(W))
\]

is birational onto its image. Indeed, in its function field,
\(dB=-W\,dA\), so \(W=-dB/dA\). Thus the polynomial map is Morse over
\(\overline{k(P)}\).

The degree-\(n\) cover is connected, and its finite local branch cycles are
transpositions. A transitive permutation group generated by transpositions is
the full \(S_n\). This proves the generic theorem independently of any
specialization.

As a secondary certificate, the test suite computes the Galois groups of

\[
W^n-W+1,\qquad n=3,4,5,6,
\]

and obtains orders \(6,24,120,720\), respectively. These specializations give
independent lower-bound evidence for the generic groups in those degrees but
are not the general proof.

### Radical consequence

For \(n\ge5\), \(S_n\) is nonsolvable. Over a characteristic-zero field
containing the necessary roots of unity, an element obtainable by a radical
tower has solvable normal closure. The normal closure of a generic root field
here is the full splitting field with group \(S_n\). Therefore even one
generic branch cannot be expressed by radicals.

### Correct Chebotarev formulation

Let a good reduction over \(\mathbb F_q\) have geometrically connected regular
Galois closure with group \(S_n\), and let the regular target have dimension
\(d\). Finite-field Chebotarev and Lang--Weil give, over
\(\mathbb F_{q^m}\),

\[
N_j(q^m)=\frac{\binom njD_{n-j}}{n!}q^{md}
+O(q^{m(d-1/2)}).
\]

This is an extension-field asymptotic for a fixed good model. It is not an
exact formula for every reduction, and uniformity while varying primes needs
additional control.

The test suite exhaustively enumerates the squarefree fibers of
\(W^n-PW+Q\) over several prime fields. For example, at \(q=101\) it obtains
the expected fixed-point patterns (never \(n-1\) roots), with observed
frequencies close to the \(S_n\) proportions. These computations are evidence
for the arithmetic interpretation, while Chebotarev supplies the proof.

### Confidence

**Very high for the abstract monodromy and radical statements. High and
conditional for the arithmetic application**, exactly as stated above. The
application to every public weighted lift also assumes that its recorded
inverse equation has the required form.

## Test inventory

The repository now has 26 passing tests. The eight new referee-audit tests add:

- an exact counterexample to the overbroad residue-ratio formulation;
- exact ordered-root-to-collision reconstruction for three rational samples;
- projective finite-field counts for the collision complement at
  \(q=5,7,11\);
- an algebraic translation-stabilizer calculation;
- smooth-discriminant contact normal forms for orders one through four;
- all three Newton-polygon regimes and an infinite family of degenerate
  equality cases;
- finite-field enumeration of squarefree fibers for degrees three through
  five;
- independent Galois-group specializations for degrees three through six.

The original symbolic verifier still passes all determinant, collision,
inverse-cubic, discriminant, boundary, quotient, vector-field, and exact cubic
finite-field identities.

## Literature boundary

The following ingredients are established theory rather than new claims:

- divisorial valuations and class groups: [Stacks Project, Weil divisors](https://stacks.math.columbia.edu/tag/0BE0);
- \(\operatorname{Pic}(\mathbb P^n)=\mathbb Z\): [Stacks Project, Tag 0BXJ](https://stacks.math.columbia.edu/tag/0BXJ);
- finite-field Frobenius-class equidistribution: [Meagher, *A simple proof of Chebotarev's density theorem over finite fields*](https://doi.org/10.1017/S0004972718000448);
- Newton polygons and initial forms are standard valuation tools;
- commuting locally nilpotent derivations have a substantial existing
  literature, including the [commuting derivations conjecture](https://doi.org/10.1016/S0022-4049(02)00198-6).

The inverse cubic and \(S_3\) calculation materially overlap the
[same-day MathOverflow discussion](https://mathoverflow.net/questions/513387/).
No search can certify nonexistence of prior work. The correct public language
is therefore ``proved in this working note; priority unknown,'' not
``discovered here.''

## External validation still required

Before journal-style submission or strong novelty language:

1. Ask an algebraic geometer to check the scheme-level collision-space
   identification and localization sequence.
2. Ask a specialist in polynomial vector fields or locally nilpotent
   derivations to assess the translation-stabilizer statement and its
   literature status.
3. Ask a singularity theorist to check the Newton--Puiseux escape theorem,
   especially the degenerate equality family.
4. Ask an arithmetic geometer to confirm the exact hypotheses and constants
   in the Chebotarev application to the chosen integral models.
5. Formalize the finite algebraic identities in a proof assistant if a fully
   machine-checked certificate is desired.

The present audit supports sharing the work for expert review. It does not yet
support claiming peer-reviewed novelty.
