"""Calculator クラスの基本テスト"""

import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


class TestAdd:
    def test_integers(self, calc):
        assert calc.add(2, 3) == 5

    def test_floats(self, calc):
        assert calc.add(1.5, 2.5) == 4.0

    def test_negative(self, calc):
        assert calc.add(-1, -2) == -3


class TestSubtract:
    def test_integers(self, calc):
        assert calc.subtract(10, 3) == 7

    def test_negative_result(self, calc):
        assert calc.subtract(3, 10) == -7


class TestMultiply:
    def test_integers(self, calc):
        assert calc.multiply(3, 4) == 12

    def test_zero(self, calc):
        assert calc.multiply(100, 0) == 0


class TestDivide:
    def test_integers(self, calc):
        assert calc.divide(10, 2) == 5.0

    def test_float_result(self, calc):
        assert calc.divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

    def test_zero_division(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.divide(5, 0)


class TestPower:
    def test_positive_exp(self, calc):
        assert calc.power(2, 10) == 1024

    def test_zero_exp(self, calc):
        assert calc.power(5, 0) == 1

    def test_negative_exp(self, calc):
        assert calc.power(2, -1) == pytest.approx(0.5)
