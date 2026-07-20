from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import verify


def test_core():
    verify.verify_core()


def test_equivariance_and_collision_family():
    verify.verify_equivariance_and_collision_family()


def test_weighted_quotient():
    verify.verify_weighted_quotient()


def test_general_equivariant_quotient_identity():
    verify.verify_general_equivariant_quotient_identity()


def test_inverse_cubics():
    verify.verify_inverse_cubics()


def test_discriminant_and_boundary():
    verify.verify_discriminant_and_boundary()


def test_nonproper_path_and_slice():
    verify.verify_nonproper_path_and_slice()


def test_inverse_jacobian_fields():
    verify.verify_inverse_jacobian_fields()


def test_finite_field_fiber_counts():
    verify.verify_finite_field_fiber_counts()


def test_first_coordinate_factorization():
    verify.verify_first_coordinate_factorization()
