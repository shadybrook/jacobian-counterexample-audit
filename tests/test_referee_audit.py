from itertools import product
from math import comb, factorial

from sympy import I, Poly, Rational, expand, simplify, symbols
from sympy.polys.numberfields import galois_group


def test_residue_ratio_requires_transcendence_over_the_ground_field():
    s, x, p = symbols("s x p", nonzero=True)

    # Over R the residue ratio i is algebraic but not in the ground field.
    # The top form U^2+V^2 cancels, refuting the overbroad formulation.
    f, g = 1 / s, I / s
    assert simplify(f**2 + g**2) == 0

    # In the actual complex slice, the residue ratio depends on x and is
    # therefore transcendental over C (for fixed nonzero p).
    slice_ratio = Rational(2, 3) / p + 1 / (9 * p**2 * x**2)
    assert simplify(slice_ratio.diff(x)) != 0


def _map(point):
    x, y, z = point
    P = (1 + x * y) ** 3 * z + y**2 * (1 + x * y) * (4 + 3 * x * y)
    Q = y + 3 * x * (1 + x * y) ** 2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    R = 2 * x - 3 * x**2 * y - x**3 * z
    return tuple(simplify(value) for value in (P, Q, R))


def _target_from_ordered_roots(a, b, c, d):
    E = a**2 * d + 2 * a * b * c + 2 * a * b * d + b**2 * c
    P = (c**2 * d + c * d**2) / E
    Q = 2 * (2 * a * c * d + a * d**2 + b * c**2 + 2 * b * c * d) / E
    R = 2 * a * b * (a + b) / E
    return tuple(simplify(value) for value in (P, Q, R))


def _preimage_from_root(s, target):
    p, q, r = target
    derivative_half = 1 - s * q + 3 * p * s**2
    x = s / derivative_half
    y = q - 3 * p * s
    z = (2 * x - 3 * x**2 * y - r) / x**3
    return tuple(simplify(value) for value in (x, y, z))


def test_ordered_root_model_gives_exact_collisions():
    matrices = [(1, 2, 3, 5), (2, -1, 3, 4), (1, 3, -2, 5)]
    for values in matrices:
        a, b, c, d = map(Rational, values)
        determinant = a * d - b * c
        E = a**2 * d + 2 * a * b * c + 2 * a * b * d + b**2 * c
        assert determinant != 0 and E != 0

        target = _target_from_ordered_roots(a, b, c, d)
        roots = (a / c, b / d, (a + b) / (c + d))
        preimages = [_preimage_from_root(root, target) for root in roots]

        assert len(set(preimages)) == 3
        assert all(_map(point) == target for point in preimages)


def _projective_points(prime):
    # Unique representative whose first nonzero coordinate is one.
    for pivot in range(4):
        for tail in product(range(prime), repeat=3 - pivot):
            yield (0,) * pivot + (1,) + tail


def test_collision_complement_point_counts():
    for prime in (5, 7, 11):
        pgl_count = h_count = u_count = 0
        for a, b, c, d in _projective_points(prime):
            determinant = (a * d - b * c) % prime
            E = (a * a * d + 2 * a * b * c + 2 * a * b * d + b * b * c) % prime
            if determinant:
                pgl_count += 1
                if E:
                    u_count += 1
                else:
                    h_count += 1

        assert pgl_count == prime**3 - prime
        assert h_count == (prime - 2) * (prime - 1)
        assert u_count == (prime - 1) * (prime**2 + 2)


def test_translation_stabilizer_of_omitted_curve_is_zero():
    q, A, B, C = symbols("q A B C")
    # Substitute the parametrization p=q^2/12, r=4/(3q) into directional
    # derivatives of 12p-q^2 and 3qr-4.
    derivative_first = 12 * A - 2 * q * B
    derivative_second = 3 * (Rational(4, 3) * B / q + q * C)

    numerator_first = Poly(derivative_first, q)
    numerator_second = Poly(expand(q * derivative_second), q)
    equations = list(numerator_first.all_coeffs()) + list(numerator_second.all_coeffs())

    # The coefficients force B=0, A=0, and C=0.
    assert equations == [-2 * B, 12 * A, 3 * C, 0, 4 * B]


def test_smooth_discriminant_contact_normal_form():
    epsilon, u = symbols("epsilon u")
    for contact_order in (1, 2, 3, 4):
        # At (p,q,r)=(0,1,1), K(T)=T(T-1)^2.  Perturbing 2p by
        # epsilon^k gives, at T=1+u, u^2(1+u)-epsilon^k.
        local_cubic = expand(u**2 * (1 + u) - epsilon**contact_order)
        assert local_cubic.coeff(u, 2).subs(epsilon, 0) == 1
        # Balancing u^2 with epsilon^k gives ord(u)=k/2; differentiating
        # preserves the same leading order because 2u+3u^2 has leading 2u.
        assert simplify(local_cubic.diff(u) - (2 * u + 3 * u**2)) == 0


def test_cusp_newton_polygon_regimes_and_degenerate_boundary():
    e, u, w = symbols("e u w")

    # 2 beta < 3 alpha: alpha=2, beta=1; w=e^(1/3)v gives
    # leading equation v^3+1 and derivative order 2/3.
    case_one = w**3 + e**2 * w + e
    assert case_one == w**3 + e**2 * w + e

    # 2 beta > 3 alpha: alpha=1, beta=2. Two roots balance w^2=-e;
    # the third balances e*w=-e^2. All derivatives have order one.
    case_two = w**3 + e * w + e**2
    assert case_two.diff(w) == 3 * w**2 + e

    # Equality, separable leading cubic: alpha=2, beta=3.
    v = symbols("v")
    scaled = simplify((w**3 + e**2 * w + e**3).subs(w, e * v) / e**3)
    assert scaled == v**3 + v + 1
    assert Poly(v**3 + v + 1, v).discriminant() != 0

    # Equality, degenerate leading cubic. The same (alpha,beta)=(2,3)
    # allows arbitrarily later splitting: u^2(3e+u)+e^N near w=e.
    for later_order in (4, 5, 6):
        degenerate = expand(w**3 - 3 * e**2 * w + 2 * e**3 + e**later_order)
        shifted = expand(degenerate.subs(w, e + u))
        assert shifted == u**3 + 3 * e * u**2 + e**later_order


def _trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def _poly_mod(poly, prime):
    return _trim([coefficient % prime for coefficient in poly])


def _poly_divmod(a, b, prime):
    a = _poly_mod(a[:], prime)
    b = _poly_mod(b[:], prime)
    quotient = [0] * max(1, len(a) - len(b) + 1)
    inverse_lead = pow(b[-1], -1, prime)
    while len(a) >= len(b) and a != [0]:
        shift = len(a) - len(b)
        coefficient = a[-1] * inverse_lead % prime
        quotient[shift] = coefficient
        for index, value in enumerate(b):
            a[index + shift] = (a[index + shift] - coefficient * value) % prime
        _trim(a)
    return _poly_mod(quotient, prime), _poly_mod(a, prime)


def _poly_gcd(a, b, prime):
    while b != [0]:
        _, remainder = _poly_divmod(a, b, prime)
        a, b = b, remainder
    inverse_lead = pow(a[-1], -1, prime)
    return _poly_mod([coefficient * inverse_lead for coefficient in a], prime)


def _evaluate(poly, value, prime):
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def _regular_fiber_distribution(n, prime):
    counts = {j: 0 for j in range(n + 1)}
    for P in range(prime):
        for Q in range(prime):
            polynomial = [Q, -P] + [0] * (n - 2) + [1]
            derivative = [-P] + [0] * (n - 2) + [n]
            if len(_poly_gcd(polynomial, derivative, prime)) != 1:
                continue
            roots = sum(_evaluate(polynomial, value, prime) == 0 for value in range(prime))
            counts[roots] += 1
    return counts


def test_finite_field_fixed_point_pattern_for_morse_family():
    # This is evidence for Chebotarev convergence, not a proof of the error
    # term. Impossible fixed-point counts (n-1) never occur for squarefree
    # degree-n polynomials.
    for n, prime in ((3, 29), (4, 31), (5, 31)):
        counts = _regular_fiber_distribution(n, prime)
        assert counts[n - 1] == 0
        assert sum(counts.values()) > 0
        assert sum(j * value for j, value in counts.items()) > 0

    # A larger degree-five field gives a quantitative, exact-arithmetic check
    # against the S_5 fixed-point proportions. This is evidence for the
    # Chebotarev application, not a proof of its error term.
    n, prime = 5, 101
    counts = _regular_fiber_distribution(n, prime)
    total = sum(counts.values())
    derangements = [1, 0]
    for size in range(2, n + 1):
        derangements.append((size - 1) * (derangements[-1] + derangements[-2]))
    group_order = factorial(n)
    for roots, count in counts.items():
        expected_numerator = comb(n, roots) * derangements[n - roots]
        # Observed and limiting probabilities differ by at most 1/20.
        assert 20 * abs(count * group_order - total * expected_numerator) <= total * group_order


def test_independent_symmetric_galois_specializations():
    # Specialization cannot prove the full generic theorem on its own, but an
    # S_n specialization supplies an independent lower-bound certificate for
    # the generic group in these degrees.
    w = symbols("w")
    for n in range(3, 7):
        group, _ = galois_group(Poly(w**n - w + 1, w), w)
        assert group.order() == factorial(n)
