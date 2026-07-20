# An Exact Audit of an Announced Three-Dimensional Keller Map

**Status:** independent working note, revised 21 July 2026
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
Poisson algebras, a commuting divergence-free polynomial frame with no
complete constant direction, a nonproper smooth fibration with jumping
component count, an equivariant square law for quotient Jacobians, exact
finite-field fiber statistics, and exact real volume formulas. Finally, we audit broader claims made in
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

The square in this formula is forced by the weights, rather than being an
accident of the announced coefficients.

### Theorem 2.3 (equivariant quotient square law)

Let $G=(A,B,C):\mathbb A^3\to\mathbb A^3$ be a polynomial map equivariant
for source weights $(1,-1,-2)$ and target weights $(-2,-1,1)$, in the order
displayed. Suppose $\det DG=c\in k^*$. With quotient coordinates

$$
u=xy,\quad v=x^2z,\qquad \alpha=AC^2,\quad\beta=BC,
$$

write $C=xh(u,v)$; every weight-one source polynomial has this form. Then the
induced quotient map satisfies

$$
\boxed{\det D\bar G=c\,h(u,v)^2.}
$$

In particular, if $h$ is nonconstant, the quotient necessarily has a critical
divisor. The quotient can be Keller only when $C/x$ is a nonzero constant.

**Proof.** Let $\xi=(x,-y,-2z)$ and $\eta=(-2A,-B,C)$ be the infinitesimal
orbit fields, and let $\Omega_x=dx\wedge dy\wedge dz$ and
$\Omega_y=dA\wedge dB\wedge dC$. Direct exterior algebra gives

$$
du\wedge dv=x^2\iota_\xi\Omega_x,
\qquad
d\alpha\wedge d\beta=C^2\iota_\eta\Omega_y.
$$

Equivariance gives $DG(\xi)=\eta\circ G$, while the constant Jacobian gives
$G^*\Omega_y=c\Omega_x$. Pulling back the second identity therefore yields

$$
(\det D\bar G)du\wedge dv
=cC^2\iota_\xi\Omega_x
=c(C/x)^2du\wedge dv.
$$

Since $C/x=h(u,v)$, the result follows. The two exterior-form identities are
also certified coefficientwise in the verifier. $\square$

This proves a restricted but general obstruction: every equivariant Keller
map with this precise weight pattern develops quotient ramification unless its
weight-one coordinate is merely a constant multiple of $x$. It does **not**
prove that every conceivable quotient or every route to dimension two must
ramify.

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

The broad completion principle itself is not new. Zariski's Main Theorem says
that every separated quasi-finite morphism factors as an open immersion into a
finite morphism. Since every Keller map is etale and hence quasi-finite, any
Keller counterexample admits such a finite completion
([Stacks Project, Tag 05W7](https://stacks.math.columbia.edu/tag/05W7)). What is special here is
that the completion, its boundary, its ramification, and its torsor structure
are all completely explicit. Thus a genuinely new classification result would
need hypotheses that force or classify this particular boundary geometry; the
mere existence of a finite completion is classical.

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

There is a useful general criterion behind this observation.

### Proposition 6.1 (completeness criterion)

For any complex Keller map $G:\mathbb A^n\to\mathbb A^n$, let
$\partial_1,\ldots,\partial_n$ be the commuting polynomial fields dual to
$dG_1,\ldots,dG_n$. Then $G$ is a polynomial automorphism if and only if all
$\partial_i$ are complete holomorphic vector fields. In particular, $G$ is an
automorphism if all the $\partial_i$ are locally nilpotent.

**Proof.** For an automorphism the fields are pullbacks of the complete
constant coordinate fields. Conversely, completeness and commutativity give a
holomorphic $\mathbb C^n$-action, and

$$
G(\exp(s_1\partial_1)\cdots\exp(s_n\partial_n)x)
=G(x)+(s_1,\ldots,s_n).
$$

The fields form a basis everywhere, so every orbit is open. Connectedness of
$\mathbb A^n(\mathbb C)$ leaves one orbit. The displayed identity makes the
action free and makes $G$ bijective. Ax--Grothendieck then makes the inverse
polynomial. Locally nilpotent fields have algebraic, hence holomorphically
complete, flows. $\square$

For the announced map the conclusion can be strengthened maximally.

### Theorem 6.2 (total directional incompleteness)

For every nonzero $a=(a_1,a_2,a_3)\in\mathbb C^3$, the polynomial vector
field

$$
\delta_a=a_1\delta_1+a_2\delta_2+a_3\delta_3
$$

is not holomorphically complete. Consequently no nonzero constant linear
combination of the inverse-Jacobian columns is locally nilpotent.

**Proof.** A local flow of $\delta_a$ satisfies
$F(\phi_t(x))=F(x)+ta$. The omitted curve $\Gamma$ contains no affine line:
it is parametrized by $q\in\mathbb C^*$ as

$$
(p,q,r)=\left(\frac{q^2}{12},q,\frac4{3q}\right).
$$

Choose $\gamma\in\Gamma$. Since $\Gamma$ contains no line parallel to $a$,
there is a $t_0\ne0$ for which $y=\gamma-t_0a\notin\Gamma$. The image theorem
provides $x$ with $F(x)=y$. If $\delta_a$ were complete, then
$F(\phi_{t_0}(x))=\gamma$, contradicting
$F(\mathbb A^3)=\mathbb A^3\setminus\Gamma$. $\square$

One incomplete trajectory is especially simple. Along the target line
$(0,t,0)$, one inverse branch is

$$
\gamma(t)=\left(\frac2t,-\frac t2,\frac54t^2\right),\qquad t\ne0.
$$

Exact differentiation gives $\gamma'(t)=\delta_2(\gamma(t))$, while
$F(\gamma(t))=(0,t,0)$. This trajectory escapes at the finite flow time
$t=0$, even though the target origin itself has a different finite preimage.

Equivalently, the exact coframe defines a flat algebraic affine structure on
$\mathbb A^3$ whose developing map is $F$, but that structure is incomplete.
This translates the obstruction at infinity into failure of every nonzero
constant direction in the dual polynomial frame to be complete.

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

## 8. Exact arithmetic over finite fields

The same formula defines an etale map over every finite field $\mathbb F_q$
of odd characteristic. Let $N_j(q)$ denote the number of targets having
exactly $j$ rational preimages. The projective inverse cubic shows that only
$j=0,1,3$ occur.

### Theorem 8.1 (finite-field fiber distribution)

If $\operatorname{char}\mathbb F_q\ne2,3$, then

$$
\begin{aligned}
N_3(q)&=\frac{(q-1)(q^2+2)}6,\\
N_1(q)&=\frac{q^3+q^2-2q+2}2,\\
N_0(q)&=\frac{(q-1)(q^2+2)}3.
\end{aligned}
$$

If $\operatorname{char}\mathbb F_q=3$, then

$$
N_3(q)=\frac{q^2(q-1)}6,
\qquad
N_1(q)=\frac{q^2(q+1)}2,
\qquad
N_0(q)=\frac{q^2(q-1)}3.
$$

Thus, as $q\to\infty$, the proportions of targets with three, one, and zero
rational preimages tend respectively to

$$
\frac16,\qquad\frac12,\qquad\frac13,
$$

the proportions of the identity, transpositions, and three-cycles in $S_3$.

**Proof.** A target determines the binary cubic

$$
2pS^3-qS^2T+2ST^2-rT^3,
$$

and rational preimages correspond exactly to its simple
$\mathbb F_q$-rational projective roots. A three-element subset of
$\mathbb P^1(\mathbb F_q)$ determines a cubic up to scale; it gives a unique
target precisely when its $ST^2$ coefficient is nonzero, since that coefficient
must be scaled to $2$.

There are $\binom{q+1}{3}$ root triples. A triple containing infinity is bad
exactly when its two finite roots are $a,-a$, giving $(q-1)/2$ bad triples.
For three finite roots, vanishing of the linear coefficient is
$ab+ac+bc=0$. None is zero, and inversion turns this into a triple of distinct
nonzero elements with sum zero. Counting ordered pairs and dividing by six
gives

$$
\frac{(q-1)(q-5)}6
$$

bad finite triples in characteristic other than three. In characteristic
three the three equality exclusions coincide, giving instead
$\frac{(q-1)(q-3)}6$. Subtracting the bad triples proves the formula for
$N_3$.

Finally, both source and target contain $q^3$ points. Hence

$$
N_0+N_1+N_3=q^3,
\qquad
N_1+3N_3=q^3.
$$

Therefore $N_0=2N_3$, and the remaining formulas follow. The verifier
brute-force checks the distributions over $\mathbb F_3,\mathbb F_5$, and
$\mathbb F_7$. $\square$

## 9. Audit of the eight proposed research directions

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

The weighted symmetry, collision orbit, quotient square law, divergence-free
inverse frame, total directional incompleteness, jumping component count,
finite-field distribution, and real volume formulas were added as
independently proved deductions. We do not assert historical priority for them
without a longer literature review and expert review.

## 10. Further established implications and research questions

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
7. classify the pole orders, escape divisors, and degree growth of the
   incomplete inverse-Jacobian flows;
8. exploit the weighted $\mathbb C^*$-action to form quotient surfaces and
   classify equivariant Keller maps;
9. formalize the determinant, collision, and inverse-cubic certificate in a
   proof assistant;
10. study reductions modulo primes through the $S_3$ cubic, including fiber
    statistics beyond Theorem 8.1, extension-field zeta functions, and
    bad-reduction behavior.

## 11. What is proved, what is sourced, and what is not claimed

The determinant, collision, weighted quotient, inverse identities,
discriminants, boundary parametrization, nonproper path, relative slice
Jacobian, equivariant quotient square law, finite-field regression counts,
and commuting inverse
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
