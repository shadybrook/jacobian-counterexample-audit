# Consequence ledger

This ledger separates direct calculations, deductions proved in the paper,
consequences imported from published theorems, open problems, and statements
that do **not** follow. It is intended to prevent a true counterexample from
being surrounded by avoidable overclaims.

## A. Directly certified from the displayed formula

1. `det(DF) = -2` identically.
2. The three displayed rational points have image `(-1/4, 0, 0)`.
3. The component degrees are `(7, 6, 4)`.
4. Scaling the first output by `-1/2` gives determinant one.
5. The map is etale and locally invertible everywhere, but is not globally
   injective or a polynomial automorphism.
6. The map is nonproper; the path
   `(lambda, -1/lambda, 5/lambda^2)` maps to `(0, 2/lambda, 0)`.
7. The weighted action
   `(x,y,z) -> (lambda*x, y/lambda, z/lambda^2)` is carried to
   `(P,Q,R) -> (P/lambda^2, Q/lambda, lambda*R)`.
8. This action generates a one-parameter rational family of explicit
   three-point collisions. The announced target is off the discriminant, so
   the collision is part of the generic three-sheeted behavior.
9. The induced two-dimensional invariant-theory quotient has Jacobian
   `-2(2-3u-v)^2`. It sends two distinct quotient points to the origin and
   collapses the critical line `2-3u-v=0`, so it is not a plane Keller map.

## B. Structural deductions proved for this map

1. The inverse problem is governed by an irreducible projective cubic.
2. The generic function-field degree is exactly three.
3. The splitting-field Galois group and geometric monodromy group are `S_3`.
4. The rational deck group is trivial.
5. Complex fibers have exactly three, one, or zero points according to the
   discriminant and triple-root locus.
6. The image is affine three-space minus the explicit curve
   `Gamma = V(12p-q^2, 3qr-4)`.
7. The nonproperness set is exactly the discriminant surface `V(Delta)`.
8. The finite inverse-root completion is a smooth affine threefold; its
   boundary is `A^2` and normalizes the discriminant surface.
9. The completion is a nontrivial affine-plane torsor under
   `O(-1) + O(-2)` over `P^1`, has Picard group `Z`, and is nonfactorial.
10. The inverse-Jacobian columns are a global commuting divergence-free
    polynomial frame dual to `dP,dQ,dR`.
11. Those vector fields cannot all be locally nilpotent. Equivalently, the
    induced flat algebraic affine structure is incomplete; otherwise their
    commuting algebraic flows would make `F` a polynomial coordinate system.
12. The smooth morphism `P: A^3 -> A^1` has connected fiber
    `A^2 \ {xy=-1}` for `p != 0`, but its zero fiber is the disjoint union of
    that surface and `G_m x A^1`. Component count jumps because the morphism is
    not proper.
13. Over the reals, the sign of `Delta` gives three or one inverse branches.
    On relatively compact measurable sets away from the discriminant, the
    inverse-image volume is `3/2` or `1/2` times target volume, respectively.
14. The quotient calculation gives a precise obstruction to the most natural
    equivariant descent to dimension two: ramification necessarily appears in
    this quotient model.

## C. Consequences via established external theorems

1. The Jacobian Conjecture is false in dimension three and all dimensions
   `n >= 3` by adjoining identity coordinates.
2. The generic degree three is minimal for any Keller counterexample, using
   the birational and Galois cases.
3. The Dixmier Conjecture is false in rank three. The paper also gives a direct
   endomorphism witness.
4. The Poisson Conjecture is false in rank three, again with a direct witness.
5. Stable reduction theorems imply the existence of cubic-homogeneous and
   Druzkowski-type counterexamples in higher dimensions.
6. The Mathieu conjecture for `SU(3)` is false under the published
   fixed-dimensional implication.
7. The all-dimensional Gaussian Moments, Vanishing, and Image conjectures fail
   in at least one finite dimension. These deductions are existential unless
   explicit witnesses are separately constructed.

## D. Contemporaneous extensions not claimed as ours

A same-day weighted-lift note constructs Keller maps in dimension three of
every generic degree `n >= 3`, including rational fibers with `n` points. This
repository records and cites that result but does not claim its priority.

## E. Open or plausible research directions

1. Determine whether total-degree four, five, or six counterexamples exist in
   dimension three.
2. Produce the smallest explicit cubic-homogeneous and Druzkowski reductions.
3. Classify weighted lifts and their monodromy groups.
4. Classify smooth finite completions whose ramification-divisor complement is
   affine space.
5. Determine which inverse-Jacobian vector fields are locally nilpotent,
   complete holomorphically, or exhibit controlled degree growth.
6. Turn existential failures of related conjectures into small explicit
   witnesses.
7. Study the arithmetic of the `S_3` cubic over finite fields, including fiber
   statistics and bad reduction.
8. Analyze whether the deleted-hyperbola slice gives a genuine obstruction or
   deformation principle for the still-open plane case.
9. Formalize the core certificate in a proof assistant.

## F. Statements that do not follow

1. The two-dimensional Jacobian Conjecture is not settled.
2. Rank-one or rank-two Dixmier and Poisson cases are not settled here.
3. Total degree seven is not proved minimal.
4. The counterexample does not by itself provide an immediate physical or
   engineering application.
5. Same-day verification is not peer review and does not settle priority.
6. Exact computer algebra does not replace checking the hypotheses of every
   imported theorem.
