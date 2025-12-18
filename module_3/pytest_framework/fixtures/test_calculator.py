import pytest
from module_3.pytest_framework.fixtures.calculator import Calculator

@pytest.fixture
def calc():
    """Provides a Calculator instance."""
    return Calculator()

def test_addition(calc):
    """Test addition method."""
    assert calc.add(2, 3) == 5

def test_substraction(calc):
    """Test substraction method."""
    assert calc.subtract(5, 3) == 2
def test_multiplication(calc):
    """Test multiplication method."""
    assert calc.multiply(3, 4) == 12
def test_division(calc):
    """Test division method."""
    assert calc.divide(8, 2) == 4
def test_division_by_zero(calc):
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        calc.divide(10, 0)