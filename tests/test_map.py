from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import verify


def test_core():
    verify.verify_core()


def test_inverse_cubics():
    verify.verify_inverse_cubics()


def test_discriminant_and_boundary():
    verify.verify_discriminant_and_boundary()


def test_nonproper_path_and_slice():
    verify.verify_nonproper_path_and_slice()


def test_inverse_jacobian_fields():
    verify.verify_inverse_jacobian_fields()

