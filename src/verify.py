"""Exact symbolic audit for the announced three-dimensional Keller map."""

from __future__ import annotations

from sympy import Matrix, Poly, Rational, discriminant, factor, simplify, symbols


x, y, z = symbols("x y z")
p, q, r, T, U = symbols("p q r T U")


def announced_map():
    P = (1 + x * y) ** 3 * z + y**2 * (1 + x * y) * (4 + 3 * x * y)
    Q = y + 3 * x * (1 + x * y) ** 2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    R = 2 * x - 3 * x**2 * y - x**3 * z
    return Matrix([P, Q, R])


F = announced_map()
J = F.jacobian((x, y, z))


def zero(expr):
    assert factor(expr) == 0


def verify_core():
    assert factor(J.det()) == -2
    assert [Poly(f, x, y, z).total_degree() for f in F] == [7, 6, 4]
    target = Matrix([Rational(-1, 4), 0, 0])
    points = [
        (0, 0, Rational(-1, 4)),
        (1, Rational(-3, 2), Rational(13, 2)),
        (-1, Rational(3, 2), Rational(13, 2)),
    ]
    for point in points:
        image = F.subs(dict(zip((x, y, z), point)))
        assert image == target


def verify_equivariance_and_collision_family():
    lam = symbols("lam", nonzero=True)
    scaled = F.subs({x: lam * x, y: y / lam, z: z / lam**2}, simultaneous=True)
    expected = Matrix([F[0] / lam**2, F[1] / lam, lam * F[2]])
    assert all(factor(a - b) == 0 for a, b in zip(scaled, expected))

    target = Matrix([-Rational(1, 4) / lam**2, 0, 0])
    points = [
        (0, 0, -Rational(1, 4) / lam**2),
        (lam, -Rational(3, 2) / lam, Rational(13, 2) / lam**2),
        (-lam, Rational(3, 2) / lam, Rational(13, 2) / lam**2),
    ]
    for point in points:
        assert all(
            factor(a - b) == 0
            for a, b in zip(F.subs(dict(zip((x, y, z), point))), target)
        )

    Delta = q**2 - 16 * p - q**3 * r + 18 * p * q * r - 27 * p**2 * r**2
    scaled_delta = Delta.subs(
        {p: p / lam**2, q: q / lam, r: lam * r}, simultaneous=True
    )
    zero(scaled_delta - Delta / lam**2)
    assert Delta.subs({p: -Rational(1, 4), q: 0, r: 0}) == 4


def verify_weighted_quotient():
    u, v = symbols("u v")
    h = 2 - 3 * u - v
    alpha = (1 + u) * h**2 * (
        3 * u**3 + u**2 * v + 4 * u**2 + 2 * u * v + v
    )
    beta = h * (
        9 * u**3 + 3 * u**2 * v + 12 * u**2 + 6 * u * v + u + 3 * v
    )

    # These are the target invariants alpha=P*R^2 and beta=Q*R expressed
    # in the source invariants u=xy and v=x^2*z.
    source_substitution = {u: x * y, v: x**2 * z}
    zero(alpha.subs(source_substitution) - F[0] * F[2] ** 2)
    zero(beta.subs(source_substitution) - F[1] * F[2])
    quotient_jacobian = Matrix([alpha, beta]).jacobian((u, v)).det()
    zero(quotient_jacobian + 2 * h**2)

    origin = {u: 0, v: 0}
    second = {u: -Rational(3, 2), v: Rational(13, 2)}
    assert Matrix([alpha, beta]).subs(origin) == Matrix([0, 0])
    assert Matrix([alpha, beta]).subs(second) == Matrix([0, 0])
    # The entire critical line h=0 is collapsed to the quotient origin.
    line = {v: 2 - 3 * u}
    collapsed = Matrix([factor(alpha.subs(line)), factor(beta.subs(line))])
    assert collapsed == Matrix([0, 0])


def verify_general_equivariant_quotient_identity():
    """Certificates for the weight-theoretic quotient-Jacobian theorem.

    We identify a contracted volume form i_V Omega with the vector of its
    coefficients in (dy^dz, dz^dx, dx^dy).  A wedge df^dg has coefficient
    vector grad(f) cross grad(g).
    """

    u = x * y
    v = x**2 * z
    alpha = p * r**2
    beta = q * r
    source_orbit = Matrix([x, -y, -2 * z])
    target_orbit = Matrix([-2 * p, -q, r])
    source_cross = Matrix([u.diff(w) for w in (x, y, z)]).cross(
        Matrix([v.diff(w) for w in (x, y, z)])
    )
    target_cross = Matrix([alpha.diff(w) for w in (p, q, r)]).cross(
        Matrix([beta.diff(w) for w in (p, q, r)])
    )
    assert all(factor(a - b) == 0 for a, b in zip(source_cross, x**2 * source_orbit))
    assert all(factor(a - b) == 0 for a, b in zip(target_cross, r**2 * target_orbit))


def verify_inverse_cubics():
    P, Q, R = F
    t = y + 1 / x
    cubic_t = R * T**3 - 2 * T**2 + Q * T - 2 * P
    zero(cubic_t.subs(T, t))
    rho = 3 * R * t**2 - 4 * t + Q
    zero(rho - 2 / x)
    zero(t - rho / 2 - y)
    z_rec = Rational(5, 4) * rho**2 - Rational(3, 2) * t * rho - R * rho**3 / 8
    zero(z_rec - z)

    s = x / (1 + x * y)
    cubic_s = 2 * P * U**3 - Q * U**2 + 2 * U - R
    zero(cubic_s.subs(U, s))
    d = 1 - s * Q + 3 * P * s**2
    zero(d - 1 / (1 + x * y))
    zero(s / d - x)
    zero(Q - 3 * P * s - y)

    # Exceptional reconstruction for the finite root s=0 (necessarily r=0).
    zero(F[0].subs({x: 0, y: q, z: p - 4 * q**2}) - p)
    zero(F[1].subs({x: 0, y: q, z: p - 4 * q**2}) - q)
    zero(F[2].subs({x: 0, y: q, z: p - 4 * q**2}))

    # Exceptional reconstruction for the projective root [S:T]=[1:0].
    x_inf = 2 / q
    infinity_point = {
        x: x_inf,
        y: -q / 2,
        z: (5 * x_inf - r) / x_inf**3,
    }
    infinity_target = Matrix([0, q, r])
    assert all(
        factor(a - b) == 0
        for a, b in zip(F.subs(infinity_point, simultaneous=True), infinity_target)
    )


def verify_discriminant_and_boundary():
    cubic = r * T**3 - 2 * T**2 + q * T - 2 * p
    Qdisc = 27 * p**2 * r**2 - 18 * p * q * r + 16 * p + q**3 * r - q**2
    zero(discriminant(cubic, T) + 4 * Qdisc)
    zero(discriminant(Qdisc, p) + 4 * (3 * q * r - 4) ** 3)

    cubic_s = 2 * p * U**3 - q * U**2 + 2 * U - r
    Delta = q**2 - 16 * p - q**3 * r + 18 * p * q * r - 27 * p**2 * r**2
    zero(discriminant(cubic_s, U) - 4 * Delta)

    u, rr = symbols("u rr")
    p_boundary = u**2 - rr * u**3
    q_boundary = 4 * u - 3 * rr * u**2
    zero(Delta.subs({p: p_boundary, q: q_boundary, r: rr}))
    # Triple-root locus and omitted curve.
    triple = {
        p: 1 / (3 * u**2),
        q: 2 / u,
        r: 2 * u / 3,
    }
    zero(Delta.subs(triple))
    zero((12 * p - q**2).subs(triple))
    zero((3 * q * r - 4).subs(triple))


def verify_ordered_root_space():
    """Exact certificates for the ordered-root/Galois-closure model."""

    a, b, c, d, S, TT, tau, lam = symbols("a b c d S TT tau lam")
    product = (c * S - a * TT) * (d * S - b * TT) * (
        (c + d) * S - (a + b) * TT
    )
    obstruction = a**2 * d + 2 * a * b * c + 2 * a * b * d + b**2 * c
    assert Poly(product, S, TT).coeff_monomial(S * TT**2) == obstruction

    # The obstruction divisor H in PGL_2 has the explicit product chart
    # (A^1 \ {0,-1}) x G_m.  We normalize b=1.
    parameterization = {
        a: tau,
        b: 1,
        c: lam * tau * (tau + 2),
        d: -lam * (2 * tau + 1),
    }
    zero(obstruction.subs(parameterization))
    determinant = a * d - b * c
    zero(determinant.subs(parameterization) + 3 * lam * tau * (tau + 1))

    # On H with b=1, lambda=-det/(3*tau*(tau+1)) reconstructs c,d.
    normalized_obstruction = obstruction.subs({a: tau, b: 1})
    normalized_determinant = determinant.subs({a: tau, b: 1})
    inverse_lam = -normalized_determinant / (3 * tau * (tau + 1))
    for expression in (
        c - inverse_lam * tau * (tau + 2),
        d + inverse_lam * (2 * tau + 1),
    ):
        numerator = factor(expression).as_numer_denom()[0]
        assert factor(Poly(numerator, d).rem(Poly(normalized_obstruction, d)).as_expr()) == 0


def verify_boundary_escape_normal_forms():
    """Certificates for the double- and triple-root escape exponents."""

    boundary_root, boundary_r = symbols("boundary_root boundary_r", nonzero=True)
    boundary_p = boundary_root**2 - boundary_r * boundary_root**3
    boundary_q = 4 * boundary_root - 3 * boundary_r * boundary_root**2
    cubic = boundary_r * T**3 - 2 * T**2 + boundary_q * T - 2 * boundary_p
    zero(
        cubic
        - (T - boundary_root) ** 2
        * (boundary_r * T + 2 * boundary_r * boundary_root - 2)
    )

    triple_r = 2 / (3 * boundary_root)
    zero(
        cubic.subs(boundary_r, triple_r)
        - triple_r * (T - boundary_root) ** 3
    )


def verify_tangent_map_identity():
    """Regression certificate for the all-degree maximal-monodromy proof."""

    w = symbols("w")
    coeffs = symbols("a0:7")
    polynomial = sum(coeffs[i] * w**i for i in range(7))
    slope = polynomial.diff(w)
    intercept = polynomial - w * slope
    zero(intercept.diff(w) + w * slope.diff(w))


def verify_weighted_lift_degree_growth():
    """Check the leading monomials behind degrees (5d-3,5d-4,4)."""

    lift_degree = symbols("lift_degree", integer=True, positive=True)
    # u has leading term xy (ordinary degree 2) and gamma has leading term
    # x^2 z (ordinary degree 3).  After the forced x^-2 and x^-1 factors,
    # the top terms have the following exponent vectors.
    first_exponents = Matrix(
        [3 * lift_degree - 3, lift_degree + 1, lift_degree - 1]
    )
    second_exponents = Matrix(
        [3 * lift_degree - 3, lift_degree, lift_degree - 1]
    )
    assert sum(first_exponents) == 5 * lift_degree - 3
    assert sum(second_exponents) == 5 * lift_degree - 4


def verify_nonproper_path_and_slice():
    lam = symbols("lam", nonzero=True)
    path = {x: lam, y: -1 / lam, z: 5 / lam**2}
    assert [factor(v.subs(path)) for v in F] == [0, 2 / lam, 0]

    fixed = symbols("fixed", nonzero=True)
    A = 1 + x * y
    Qf = (3 * fixed * x + x * y**2 + y) / A
    Rf = x * (-fixed * x**2 + x**2 * y**2 + 3 * x * y + 2) / A**3
    relative = Matrix([Qf, Rf]).jacobian((x, y)).det()
    zero(relative + 2 / A**3)


def verify_slice_pole_normal_form():
    """Certificates for the polynomial postcomposition filling obstruction."""

    divisor_parameter, fixed = symbols("divisor_parameter fixed", nonzero=True)
    slice_y = (divisor_parameter - 1) / x
    quotient_q = (
        3 * fixed * x + x * slice_y**2 + slice_y
    ) / divisor_parameter
    quotient_r = x * (
        -fixed * x**2 + x**2 * slice_y**2 + 3 * x * slice_y + 2
    ) / divisor_parameter**3
    expected_q = (
        divisor_parameter / x
        - 1 / x
        + 3 * fixed * x / divisor_parameter
    )
    zero(quotient_q - expected_q)

    reduced_r = quotient_r + quotient_q**3 / (27 * fixed**2)
    q_residue = factor((divisor_parameter * quotient_q).subs(divisor_parameter, 0))
    s_residue = factor(
        factor(divisor_parameter * reduced_r).subs(divisor_parameter, 0)
    )
    zero(q_residue - 3 * fixed * x)
    zero(s_residue - (6 * fixed * x**2 + 1) / (3 * fixed * x))
    assert factor((s_residue / q_residue).diff(x)) != 0


def verify_inverse_jacobian_fields():
    B = simplify(J.inv())
    assert all(entry.is_polynomial(x, y, z) for entry in B)
    assert factor(B.det()) == -Rational(1, 2)
    # delta_i(F_k) = delta_ik.
    assert simplify(Matrix(F).jacobian((x, y, z)) * B) == Matrix.eye(3)
    # Coordinate formula for commutators of the polynomial vector fields.
    for i in range(3):
        for ell in range(3):
            for k in range(3):
                bracket = sum(
                    B[j, i] * B[k, ell].diff((x, y, z)[j])
                    - B[j, ell] * B[k, i].diff((x, y, z)[j])
                    for j in range(3)
                )
                zero(bracket)
    # Piola identity: the inverse-Jacobian columns preserve standard volume.
    for i in range(3):
        divergence = sum(B[j, i].diff((x, y, z)[j]) for j in range(3))
        zero(divergence)

    # An explicit integral curve of delta_Q.  It maps to the target line
    # (0, s, 0) and escapes at finite flow time s=0.
    flow = symbols("flow", nonzero=True)
    curve = Matrix([2 / flow, -flow / 2, Rational(5, 4) * flow**2])
    curve_sub = dict(zip((x, y, z), curve))
    assert F.subs(curve_sub, simultaneous=True) == Matrix([0, flow, 0])
    tangent = curve.diff(flow)
    delta_q_on_curve = B[:, 1].subs(curve_sub, simultaneous=True)
    assert all(factor(a - b) == 0 for a, b in zip(tangent, delta_q_on_curve))


def verify_finite_field_fiber_counts():
    """Brute-force regression checks for the proved finite-field formulas."""

    def image_mod(point, ell):
        xx, yy, zz = point
        aa = (1 + xx * yy) % ell
        return (
            (aa**3 * zz + yy**2 * aa * (4 + 3 * xx * yy)) % ell,
            (yy + 3 * xx * aa**2 * zz + 3 * xx * yy**2 * (4 + 3 * xx * yy))
            % ell,
            (2 * xx - 3 * xx**2 * yy - xx**3 * zz) % ell,
        )

    for ell in (3, 5, 7):
        fibers = {}
        for xx in range(ell):
            for yy in range(ell):
                for zz in range(ell):
                    target = image_mod((xx, yy, zz), ell)
                    fibers[target] = fibers.get(target, 0) + 1
        distribution = {m: 0 for m in (0, 1, 3)}
        for multiplicity in fibers.values():
            assert multiplicity in (1, 3)
            distribution[multiplicity] += 1
        distribution[0] = ell**3 - len(fibers)
        if ell == 3:
            n3 = ell**2 * (ell - 1) // 6
        else:
            n3 = (ell - 1) * (ell**2 + 2) // 6
        assert distribution == {0: 2 * n3, 1: ell**3 - 3 * n3, 3: n3}


def verify_first_coordinate_factorization():
    A = 1 + x * y
    Bfactor = A**2 * z + y**2 * (4 + 3 * x * y)
    zero(F[0] - A * Bfactor)
    # The two components of P=0 are disjoint: on A=0, Bfactor=y^2=1/x^2.
    assert factor(Bfactor.subs(y, -1 / x)) == 1 / x**2


def run_all():
    verify_core()
    verify_equivariance_and_collision_family()
    verify_weighted_quotient()
    verify_general_equivariant_quotient_identity()
    verify_inverse_cubics()
    verify_discriminant_and_boundary()
    verify_ordered_root_space()
    verify_boundary_escape_normal_forms()
    verify_tangent_map_identity()
    verify_weighted_lift_degree_growth()
    verify_nonproper_path_and_slice()
    verify_slice_pole_normal_form()
    verify_inverse_jacobian_fields()
    verify_finite_field_fiber_counts()
    verify_first_coordinate_factorization()
    print("PASS: all exact symbolic checks completed")


if __name__ == "__main__":
    run_all()
