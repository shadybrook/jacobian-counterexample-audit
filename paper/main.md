# An Exact Audit of an Announced Three-Dimensional Keller Map

**Status:** independent working note, 20 July 2026  
**Authorship:** AI-assisted, user-directed audit; maintainer attribution pending  
**Discovery credit:** the displayed map was announced by Levent Alpoge, whose
post credits Akhil for the question and Fable for work on the example.

## Abstract

We independently audit the polynomial map
$F=(P,Q,R):\mathbb A^3\to\mathbb A^3$ publicly announced by Levent Alpoge
on 20 July 2026. Exact
symbolic calculation gives $\det DF=-2$, while three distinct rational points
map to $(-1/4,0,0)$. Thus, under the standard formulation, the map is a
counterexample to the Jacobian Conjecture in dimension three and, after adding
identity coordinates, in every dimension at least three.

We give two inverse-cubic descriptions, prove that the generic function-field
degree is three, compute the $S_3$ Galois closure, classify all complex fibers,
determine the image and nonproperness locus, and describe a finite smooth
completion whose boundary is the normalization of the discriminant surface. We
also exhibit a weighted scaling symmetry and an infinite rational collision
family, direct same-rank nonautomorphic endomorphisms of the third Weyl and
Poisson algebras, a commuting divergence-free polynomial frame that cannot be
algebraically complete, a nonproper smooth fibration with jumping component
count, and exact real volume formulas. Finally, we audit broader claims made in
early discussions, distinguishing exact consequences from research directions
and explicitly recording priority uncertainty. Every polynomial identity used
in the main arguments is covered by reproducible exact-arithmetic scripts.

This document is not peer reviewed, does not claim discovery of the map, and
does not claim priority for structural observations that overlap same-day
public discussions.

## 1. Source, status, and conventions

The primary public source located in our search is [Alpoge's announcement on
X](https://x.com/__alpoge__/status/2079028340955197566). As of the status date,
we found same-day explanatory and technical notes, including a [weighted-lift
analysis](https://github.com/algal/jacobianfun/blob/main/RESEARCH.md), a
[MathOverflow question on the cubic and monodromy](https://mathoverflow.net/questions/513387/),
and a [note on consequences for related
conjectures](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/).
We did not locate a peer-reviewed paper or an arXiv manuscript by the
announcer. Accordingly, we say "announced" rather than "published" and make no
claim that the priority search is exhaustive.

Let $k$ be a characteristic-zero field. A Keller map is a polynomial map
$G:\mathbb A_k^n\to\mathbb A_k^n$ whose Jacobian determinant is a nonzero
constant. The Jacobian Conjecture asserts that every Keller map is a polynomial
automorphism. Scaling one target coordinate normalizes any nonzero constant
determinant to one.

## 2. The exact counterexample

Define

$$
\begin{aligned}
P&=(1+xy)^3z+y^2(1+xy)(4+3xy),\\
Q&=y+3x(1+xy)^2z+3xy^2(4+3xy),\\
R&=2x-3x^2y-x^3z.
\end{aligned}
$$

### Theorem 2.1

The map $F=(P,Q,R)$ satisfies

$$
\det DF=-2.
$$

Moreover,

$$
F\left(0,0,-\frac14\right)
=F\left(1,-\frac32,\frac{13}{2}\right)
=F\left(-1,\frac32,\frac{13}{2}\right)
=\left(-\frac14,0,0\right).
$$

The component degrees are $(7,6,4)$.

**Proof.** Differentiate, expand the $3\times3$ determinant, and substitute
the three points. All operations take place in
$\mathbb Z[x,y,z,1/2]$. The exact symbolic certificate in `src/verify.py`
performs both calculations without floating point. A hand-friendly
factorization is also available from the inverse-coordinate derivation below.
$\square$

### Corollary 2.2

The Jacobian Conjecture is false in dimension three. It is false in every
dimension $n\ge3$, because $F\times\mathrm{id}_{\mathbb A^{n-3}}$ has the
same collision and determinant. Replacing $P$ by $-P/2$ gives determinant
one. The formula and witnesses are rational, so the same conclusion holds over
every characteristic-zero field.

This does **not** decide the two-dimensional case.

### 2.3. Weighted equivariance and a collision family

For every $\lambda\in k^*$, define

$$
\sigma_\lambda(x,y,z)
=\left(\lambda x,\frac y\lambda,\frac z{\lambda^2}\right),
\qquad
\tau_\lambda(p,q,r)
=\left(\frac p{\lambda^2},\frac q\lambda,\lambda r\right).
$$

Exact substitution gives the equivariance identity

$$
F\circ\sigma_\lambda=\tau_\lambda\circ F.
$$

Thus the displayed collision is not isolated. For every nonzero $\lambda$,

$$
\begin{aligned}
F\left(0,0,-\frac1{4\lambda^2}\right)
&=F\left(\lambda,-\frac3{2\lambda},\frac{13}{2\lambda^2}\right)\\
&=F\left(-\lambda,\frac3{2\lambda},\frac{13}{2\lambda^2}\right)
=\left(-\frac1{4\lambda^2},0,0\right).
\end{aligned}
$$

The discriminant introduced below has weight $-2$:

$$
\Delta(\tau_\lambda(p,q,r))=\lambda^{-2}\Delta(p,q,r).
$$

At the announced target $\Delta(-1/4,0,0)=4\ne0$. Consequently the famous
three-point collision is a regular generic three-sheet fiber, not an
exceptional discriminant fiber. The involution
$F(-x,-y,z)=(P,-Q,-R)$ is the special case $\lambda=-1$.

### 2.4. The two-dimensional weighted quotient

The invariant rings of the source and target actions are polynomial rings:

$$
k[x,y,z]^{\mathbb G_m}=k[u,v],\qquad u=xy,\quad v=x^2z,
$$

$$
k[p,q,r]^{\mathbb G_m}=k[\alpha,\beta],\qquad
\alpha=pr^2,\quad\beta=qr.
$$

Every invariant monomial factors through the displayed generators.
Equivariance therefore induces a polynomial quotient map
$\bar F:\mathbb A^2_{u,v}\to\mathbb A^2_{\alpha,\beta}$. Put
$h=2-3u-v$. Exact elimination gives

$$
\begin{aligned}
\alpha&=(1+u)h^2(3u^3+u^2v+4u^2+2uv+v),\\
\beta&=h(9u^3+3u^2v+12u^2+6uv+u+3v),
\end{aligned}
$$

and

$$
\det D\bar F=-2h^2.
$$

The distinct quotient points $(0,0)$ and $(-3/2,13/2)$ both map to
$(0,0)$. More strongly, the entire critical line $h=0$ maps to the origin.
Thus the equivariant quotient preserves a visible shadow of noninjectivity but
introduces ramification. It is not a two-dimensional Keller counterexample;
the formula pinpoints why this natural dimensional reduction fails.

## 3. Two inverse cubics and generic degree

Write target coordinates as $(p,q,r)$.

### 3.1. The $t=y+1/x$ chart

In the function field $k(x,y,z)$, put

$$
t=y+\frac1x.
$$

Direct simplification gives

$$
q=4t+\frac2x-3rt^2,
\qquad
2p=rt^3-2t^2+qt.
$$

Thus $t$ satisfies

$$
C_{p,q,r}(T)=rT^3-2T^2+qT-2p=0.
$$

If $\rho=C'_{p,q,r}(t)$, then

$$
\rho=\frac2x,
\quad
x=\frac2\rho,
\quad
y=t-\frac\rho2,
\quad
z=\frac54\rho^2-\frac32t\rho-\frac r8\rho^3.
$$

Consequently

$$
k(x,y,z)=k(p,q,r)(t)
\quad\text{and}\quad
[k(x,y,z):k(p,q,r)]\le3.
$$

The three simple points in Theorem 2.1 have disjoint analytic neighborhoods
mapping biholomorphically to a common neighborhood of the target. Hence a
nonempty open set of targets has at least three preimages. The generic degree
is therefore at least three and hence exactly three. Equivalently,
$C_{p,q,r}$ is irreducible over $k(p,q,r)$.

### 3.2. The projective $s=x/(1+xy)$ chart

Put $s=x/(1+xy)$. A second identity is

$$
H_{p,q,r}(s)=2ps^3-qs^2+2s-r=0.
$$

Its homogenization

$$
\Phi_{p,q,r}(S,T)
=2pS^3-qS^2T+2ST^2-rT^3
$$

correctly retains roots at infinity. For a finite simple root $s$, let

$$
d=1-sq+3ps^2=\frac12H'_{p,q,r}(s).
$$

Then

$$
x=\frac{s}{d},\qquad y=q-3ps,
\qquad z=\frac{2x-3x^2y-r}{x^3}\quad(s\ne0).
$$

If $s=0$ is a root, then $r=0$ and the reconstruction is instead

$$
(x,y,z)=(0,q,p-4q^2).
$$

If the projective root is $[S:T]=[1:0]$, simplicity forces $p=0$ and
$q\ne0$, and its preimage is

$$
x=\frac2q,\qquad y=-\frac q2,qquad
z=\frac{5x-r}{x^3}.
$$

Direct substitution verifies both exceptional formulas. Conversely, an
affine point with $1+xy\ne0$ gives $H'(s)=2/(1+xy)\ne0$; a point with
$1+xy=0$ gives a simple root at infinity. Thus simple projective roots are
in bijection with affine preimages.

At the announced collision target, the $t$-cubic becomes
$-2T^2+1/2$. Its finite roots $\pm1/2$ give the two points with
$x=\pm1$, while the projective root at infinity gives the point with $x=0$.

## 4. Discriminant, monodromy, fibers, and image

The discriminant of the $t$-cubic is $-4\mathcal Q$, where

$$
\mathcal Q
=27p^2r^2-18pqr+16p+q^3r-q^2.
$$

As a quadratic in $p$, its discriminant is

$$
\operatorname{Disc}_p(\mathcal Q)=-4(3qr-4)^3.
$$

It follows by Gauss's lemma that $\mathcal Q$ is irreducible and not a
square in $k(p,q,r)$. Since the cubic is irreducible, its splitting-field
Galois group is

$$
\operatorname{Gal}(C/k(p,q,r))\cong S_3.
$$

In particular the corresponding three-sheeted cover has full $S_3$
monodromy and no nontrivial rational deck transformation. The latter follows
also from
$\operatorname{Aut}_K(L)=N_{S_3}(S_2)/S_2=1$ for the nonnormal cubic
subextension $L/K$.

For the $s$-cubic, write

$$
\Delta=q^2-16p-q^3r+18pqr-27p^2r^2.
$$

Its discriminant is $4\Delta$. A cubic has no simple projective root exactly
when it has a triple root. Comparing
$2p(s-u)^3$ with $H_{p,q,r}(s)$ gives the triple-root curve

$$
\Gamma=
\left\{\left(\frac1{3u^2},\frac2u,\frac{2u}3\right):u\in k^*\right\}
=V(12p-q^2,3qr-4).
$$

### Theorem 4.1 (complete complex fiber count)

Over $\mathbb C$,

$$
\#F^{-1}(p,q,r)=
\begin{cases}
3,&\Delta(p,q,r)\ne0,\\
1,&\Delta(p,q,r)=0\text{ and }(p,q,r)\notin\Gamma,\\
0,&(p,q,r)\in\Gamma.
\end{cases}
$$

Hence

$$
F(\mathbb C^3)=\mathbb C^3\setminus\Gamma.
$$

**Proof.** Off the discriminant, the projective cubic has three simple roots.
On the discriminant but off the triple-root locus, it has one double root and
one simple root. Only the simple root reconstructs an affine point, because
$F$ is étale and hence has no ramified affine point. On $\Gamma$, the only
root is triple, so no affine preimage exists. The reconstruction formulas prove
both existence and uniqueness for every simple root. $\square$

### Corollary 4.2 (minimal generic degree)

No Keller counterexample can have generic field degree one or two. Degree one
is the classical birational case. A separable degree-two extension is Galois,
and the Galois case of the Jacobian Conjecture is known. Thus generic degree
three is the smallest possible, and this map attains it.

## 5. Failure at infinity and a finite completion

The map is not proper. An elementary certificate is

$$
(x,y,z)=\left(\lambda,-\frac1\lambda,\frac5{\lambda^2}\right),
\qquad
F(x,y,z)=\left(0,\frac2\lambda,0\right).
$$

As $\lambda\to\infty$, the source escapes while the image converges to the
origin.

The projective inverse cubic packages all behavior at infinity. Define

$$
I=\{((p,q,r),[S:T])\in\mathbb A^3\times\mathbb P^1:
\Phi_{p,q,r}(S,T)=0\}.
$$

The projection $\pi:I\to\mathbb A^3$ is finite of degree three. The partial
derivatives of $\Phi$ with respect to $(p,q,r)$ are
$(2S^3,-S^2T,-T^3)$, which never vanish simultaneously on
$\mathbb P^1$; hence $I$ is smooth. The map

$$
(x,y,z)\longmapsto(F(x,y,z),[x:1+xy])
$$

identifies $\mathbb A^3$ with $I\setminus D$, where $D$ is the multiple-root
(ramification) divisor.

On the chart $S=1$, put $u=T/S$. Solving
$\Phi=\partial\Phi/\partial u=0$ gives

$$
p=u^2-ru^3,
\qquad q=4u-3ru^2.
$$

Therefore $D\cong\mathbb A^2_{u,r}$. The finite birational map

$$
(u,r)\mapsto(u^2-ru^3,4u-3ru^2,r)
$$

normalizes the discriminant surface $\Sigma=V(\Delta)$. Its triple-root
locus $3ru=2$ maps to $\Gamma$. Standard cubic-discriminant geometry shows
that the transverse singularity along $\Gamma$ is an ordinary cusp.

It follows immediately from this completion that the full nonproperness set is

$$
S_F=\Sigma.
$$

Indeed, approaching $D$ from $I\setminus D$ produces escaping source
sequences with limits in $\pi(D)=\Sigma$, and properness of the finite map
$I\to\mathbb A^3$ excludes every other finite limit.

There is also a useful bundle description. Projection $I\to\mathbb P^1$
makes $I$ a nontrivial affine-plane torsor under

$$
E=\ker\bigl(\mathcal O^{\oplus3}\xrightarrow{(2S^3,-S^2T,-T^3)}
\mathcal O(3)\bigr)
\cong\mathcal O(-1)\oplus\mathcal O(-2).
$$

The syzygies $(T,2S,0)$ and $(0,T^2,-S^2)$ give the splitting. The torsor
has no global section, since constants $(p,q,r)$ cannot produce the missing
$ST^2$ term. Homotopy invariance for affine bundles gives

$$
\operatorname{Pic}(I)\cong\operatorname{Pic}(\mathbb P^1)\cong\mathbb Z.
$$

Adjunction gives $K_I\cong\rho^*\mathcal O(1)$, while the ramification
formula identifies $K_I$ with $D$. Thus $D$ generates the divisor class
group. The smooth affine threefold $I$ is not factorial, although
$I\setminus D\cong\mathbb A^3$ is factorial.

## 6. Direct rank-three Dixmier and Poisson consequences

Let $J=DF$ and $B=J^{-1}=-\frac12\operatorname{adj}(J)$. Since
$\det J=-2$, all entries of $B$ are polynomials. Define vector fields

$$
\delta_i=\sum_{j=1}^3 B_{ji}\frac{\partial}{\partial x_j}.
$$

Then $\delta_i(F_k)=\delta_{ik}$. The commutator
$[\delta_i,\delta_j]$ annihilates every $F_k$. It therefore annihilates
$k(F_1,F_2,F_3)$, and hence also its finite separable extension
$k(x_1,x_2,x_3)$. Thus the three vector fields commute.

Let $A_3(k)$ be the third Weyl algebra with
$[D_i,X_j]=\delta_{ij}$. The assignments

$$
X_i\mapsto F_i(X),
\qquad
D_i\mapsto\sum_jB_{ji}(X)D_j
$$

preserve all Weyl relations and define an endomorphism. It is not an
automorphism. If it were, it would send the centralizer of $k[X]$, which is
$k[X]$, onto the centralizer of $k[F]$. But every polynomial in $X$
commutes with every $F_i(X)$, forcing
$k[X]\subseteq k[F]$, and hence $k[X]=k[F]$, contrary to the
noninjectivity of $F$.

Therefore the Dixmier Conjecture is false already in rank three. This also
follows abstractly by contraposition from the classical implication
$DC(3)\Rightarrow JC(3)$, but the displayed formula is an explicit witness.

On the canonical polynomial Poisson algebra
$k[x_1,x_2,x_3,\xi_1,\xi_2,\xi_3]$, the parallel assignments

$$
x_i\mapsto F_i(x),
\qquad
\xi_i\mapsto\sum_jB_{ji}(x)\xi_j
$$

preserve the Poisson bracket. The same centralizer argument proves that this is
not an automorphism. Thus the Poisson Conjecture is false in rank three.

### 6.1. A commuting volume-preserving frame and its incompleteness

The columns of $B$ have three further exact properties:

$$
[\delta_i,\delta_j]=0,
\qquad
\operatorname{div}\delta_i=0,
\qquad
\det(B)=-\frac12.
$$

The divergence identities are the polynomial Piola identity for the adjugate
of a gradient matrix and are also checked directly by the verifier. Therefore
$\delta_1,\delta_2,\delta_3$ form an everywhere independent, commuting,
standard-volume-preserving polynomial frame dual to the exact coframe
$dP,dQ,dR$.

They cannot all be locally nilpotent. If they were, their commuting
exponentials would define an algebraic $\mathbb G_a^3$-action. Since the
fields form a basis everywhere, each orbit would be open. Irreducibility of
$\mathbb A^3$ permits only one open orbit. Moreover,

$$
F(\exp(s_1\delta_1)\exp(s_2\delta_2)\exp(s_3\delta_3)x)
=F(x)+(s_1,s_2,s_3),
$$

so the action would be free and transitive and $F$ would be a polynomial
coordinate system, a contradiction.

Equivalently, the exact coframe defines a flat algebraic affine structure on
$\mathbb A^3$ whose developing map is $F$, but that structure is incomplete.
This translates the obstruction at infinity into the failure of at least one
dual polynomial flow to be algebraically complete.

## 7. Real fibers and a two-dimensional slice

For real targets, the sign of the cubic discriminant counts real simple roots:

$$
\#\bigl(F^{-1}(p,q,r)\cap\mathbb R^3\bigr)=
\begin{cases}
3,&\Delta>0,\\
1,&\Delta<0,\\
1,&\Delta=0\text{ off }\Gamma,\\
0,&(p,q,r)\in\Gamma(\mathbb R).
\end{cases}
$$

Consequently

$$
F(\mathbb R^3)=\mathbb R^3\setminus\Gamma(\mathbb R).
$$

This is
an explicit constant-Jacobian local diffeomorphism whose number of global
inverse branches changes because branches escape to infinity, not because a
critical point appears.

There is also an exact measure-theoretic form of this statement. If
$E\subset\{\Delta>0\}$ is relatively compact and measurable, then the three
real inverse branches and $|\det DF|=2$ give

$$
\operatorname{vol}(F^{-1}(E))=\frac32\operatorname{vol}(E).
$$

For relatively compact measurable $E\subset\{\Delta<0\}$, there is one real
branch and

$$
\operatorname{vol}(F^{-1}(E))=\frac12\operatorname{vol}(E).
$$

Thus each local orientation contribution is $-1$, while the signed sum over a
regular real fiber changes from $-3$ to $-1$ when two branches escape at the
discriminant. This is not a global topological degree: the map is not proper.

Fix $P=p\ne0$. Solving for $z$ identifies the level surface with

$$
X=\mathbb A^2\setminus V(1+xy).
$$

The remaining coordinates are

$$
Q_p=\frac{3px+xy^2+y}{1+xy},
\qquad
R_p=\frac{x(-px^2+x^2y^2+3xy+2)}{(1+xy)^3},
$$

and

$$
\det\frac{\partial(Q_p,R_p)}{\partial(x,y)}
=-\frac2{(1+xy)^3}.
$$

This is an étale map from a punctured affine plane, not a counterexample on
$\mathbb A^2$. The nonconstant unit $1+xy$ proves
$X\not\cong\mathbb A^2$. The calculation isolates a concrete obstruction for
attempts to descend the mechanism to dimension two: one would need to fill the
deleted hyperbola without destroying the unit-Jacobian condition.

The first coordinate itself gives another nonproperness diagnostic. Put

$$
A=1+xy,
\qquad B=A^2z+y^2(4+3xy),
\qquad P=AB.
$$

Because the full Jacobian is invertible, $dP$ never vanishes and
$P:\mathbb A^3\to\mathbb A^1$ is smooth. Nevertheless,

$$
P^{-1}(p)\cong X\quad(p\ne0),
$$

whereas

$$
P^{-1}(0)=\{B=0\}\sqcup\{A=0\}
\cong X\sqcup(\mathbb G_m\times\mathbb A^1).
$$

The two zero-fiber components are disjoint because $A=0$ forces
$B=y^2\ne0$. Hence a smooth polynomial morphism has connected nonzero fibers
but a disconnected zero fiber. Proper smooth families cannot behave this way;
the extra component enters from infinity.

## 8. Audit of the eight proposed research directions

1. **Lower degree in dimension three.** The total degree here is seven.
   Published work proves the three-dimensional conjecture through degree three,
   so degrees four, five, and six remain the immediate minimality search range.
   No exclusion of all three degrees was located.
2. **Is degree seven minimal?** Unknown. The earlier claim that the map is
   "forced in a natural minimal PDE ansatz" was not precise enough to publish;
   it is excluded from our theorem list.
3. **Fibers and generic degree.** Solved for this map in Sections 3 and 4:
   generic degree three, exact fiber counts, full $S_3$ monodromy, and trivial
   deck group.
4. **Nonproperness set.** Solved in Section 5:
   $S_F=V(\Delta)$, with omitted curve $\Gamma$.
5. **Infinite families.** A contemporaneous public weighted-lift note gives
   maps in fixed dimension three of every generic degree $n\ge3$. Its
   construction is independently consistent with the determinant identity,
   but priority belongs to that public note unless earlier work is found. A
   classification remains open.
6. **Cubic-homogeneous and Druzkowski reduction.** Bass-Connell-Wright and
   Druzkowski reduction theorems guarantee counterexamples in special cubic
   form after stabilization. This audit does not give an optimized explicit
   reduced map. A naive arithmetic-circuit lift is insufficient because it need
   not preserve a constant full Jacobian away from the constraint graph.
7. **Dixmier and Poisson.** Section 6 gives direct nonautomorphic endomorphisms
   in rank three. The low-rank-one and rank-two cases do not follow.
8. **Dimension two.** Not settled. Section 7 gives a near-example on
   $\mathbb A^2\setminus\{xy=-1\}$, which may be a useful geometric test case.

The weighted symmetry, collision orbit, divergence-free inverse frame,
algebraic incompleteness, jumping component count, and real volume formulas
were added in the present revision as independently proved deductions. We do
not assert historical priority for them without a longer literature review.

## 9. Further established implications and research questions

Published implication theorems now have the following logical consequences:

- the Mathieu conjecture for $SU(3)$ is false, assuming the fixed-dimensional
  implication recorded in Mathieu's approach;
- the all-dimensional Gaussian Moments Conjecture fails in at least one finite
  dimension;
- Zhao's all-dimensional Vanishing Conjecture fails in at least one finite
  dimension;
- the Image Conjecture fails in at least one finite dimension.

These are existential consequences. This audit does not supply small explicit
witnesses for the last three.

The most concrete next problems are:

1. eliminate or construct total-degree $4$, $5$, or $6$ Keller counterexamples in
   dimension three;
2. compute a small explicit cubic-homogeneous and Druzkowski reduction, with a
   mechanically checked collision;
3. classify affine-plane torsors $I\to\mathbb P^1$ for which removing the
   ramification divisor yields $\mathbb A^3$;
4. classify the weighted-lift families and their possible monodromy groups;
5. find explicit low-complexity witnesses for the Gaussian Moments, Vanishing,
   Image, Mathieu, Dixmier, and Poisson failures;
6. understand whether the deleted-hyperbola slice admits any meaningful filling
   theorem, obstruction, or deformation relevant to the plane case.
7. determine exactly which inverse-Jacobian fields are locally nilpotent or
   holomorphically complete, and quantify the growth of their flows;
8. exploit the weighted $\mathbb C^*$-action to form quotient surfaces and
   classify equivariant Keller maps;
9. formalize the determinant, collision, and inverse-cubic certificate in a
   proof assistant;
10. study reductions modulo primes through the $S_3$ cubic, including fiber
    statistics and bad-reduction behavior.

## 10. What is proved, what is sourced, and what is not claimed

The determinant, collision, weighted quotient, inverse identities,
discriminants, boundary parametrization, nonproper path, relative slice
Jacobian, and commuting inverse
Jacobian vector fields are exact symbolic identities tested in this repository.
The fiber and completion theorems then follow by the proofs given above. The
classical reductions and implications are literature-dependent and are cited in
the bibliography.

The priority record is unusually fluid because the announcement and several
follow-on analyses appeared on the same date. We therefore claim neither
historical novelty nor formal publication status for this audit. The reliable
contribution of this repository is a reproducible separation of:

- finite exact identities;
- deductions proved from those identities;
- consequences imported from named theorems; and
- open questions or contemporaneous claims that still require independent
  review.

## References

See `references.bib` for full bibliographic data. Core references include the
original announcement; Keller; Bass-Connell-Wright; Campbell; Razar; Wright;
Vistoli; Adjamagbo-van den Essen; Zhao; Derksen-van den Essen-Zhao; and van den
Essen-Wright-Zhao. Same-day web notes are cited as priority evidence, not as
substitutes for proof.
