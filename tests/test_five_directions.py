from fractions import Fraction
from math import comb, factorial

from sympy import discriminant, factor, simplify, symbols


def test_collision_complement_boundary_polynomials_are_irreducible():
    a, b, c, d = symbols("a b c d")
    determinant = a * d - b * c
    omitted_coefficient = a**2 * d + 2 * a * b * c + 2 * a * b * d + b**2 * c

    assert factor(determinant) == determinant
    assert factor(omitted_coefficient) == omitted_coefficient


def test_depressed_cubic_and_discriminant_identity():
    p, q, r, t, w = symbols("p q r t w", nonzero=True)
    cubic = r * t**3 - 2 * t**2 + q * t - 2 * p
    A = q / r - 4 / (3 * r**2)
    B = -2 * p / r + 2 * q / (3 * r**2) - 16 / (27 * r**3)

    depressed = simplify(cubic.subs(t, w + 2 / (3 * r)) / r)
    assert simplify(depressed - (w**3 + A * w + B)) == 0
    assert simplify(discriminant(cubic, t) - r**4 * (-4 * A**3 - 27 * B**2)) == 0


def _derangements(n):
    return factorial(n) * sum(Fraction((-1) ** i, factorial(i)) for i in range(n + 1))


def test_symmetric_monodromy_fixed_point_distributions():
    for n in range(3, 9):
        probabilities = {
            j: Fraction(comb(n, j) * _derangements(n - j), factorial(n))
            for j in range(n + 1)
        }
        assert sum(probabilities.values()) == 1
        assert sum(Fraction(j) * probability for j, probability in probabilities.items()) == 1

    assert {
        j: probability
        for j, probability in {
            j: Fraction(comb(3, j) * _derangements(3 - j), factorial(3))
            for j in range(4)
        }.items()
        if probability
    } == {0: Fraction(1, 3), 1: Fraction(1, 2), 3: Fraction(1, 6)}
