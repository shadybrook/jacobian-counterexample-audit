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


def test_ordered_root_space():
    verify.verify_ordered_root_space()


def test_boundary_escape_normal_forms():
    verify.verify_boundary_escape_normal_forms()


def test_tangent_map_identity():
    verify.verify_tangent_map_identity()


def test_weighted_lift_degree_growth():
    verify.verify_weighted_lift_degree_growth()


def test_nonproper_path_and_slice():
    verify.verify_nonproper_path_and_slice()


def test_slice_pole_normal_form():
    verify.verify_slice_pole_normal_form()


def test_inverse_jacobian_fields():
    verify.verify_inverse_jacobian_fields()


def test_finite_field_fiber_counts():
    verify.verify_finite_field_fiber_counts()


def test_first_coordinate_factorization():
    verify.verify_first_coordinate_factorization()
