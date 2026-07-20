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


def verify_inverse_jacobian_fields():
    B = simplify(J.inv())
    assert all(entry.is_polynomial(x, y, z) for entry in B)
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


def run_all():
    verify_core()
    verify_inverse_cubics()
    verify_discriminant_and_boundary()
    verify_nonproper_path_and_slice()
    verify_inverse_jacobian_fields()
    print("PASS: all exact symbolic checks completed")


if __name__ == "__main__":
    run_all()
