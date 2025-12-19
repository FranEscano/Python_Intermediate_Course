from contextlib import nullcontext
import pytest

@pytest.mark.parametrize(
    "divisor, expectation",
    [
        (3, nullcontext(2)),
        (2, nullcontext(3)),
        (1, nullcontext(6)),
        (0, pytest.raises(ZeroDivisionError)),
    ],
)
def test_division(divisor, expectation):
    with expectation as e:
        assert (6 / divisor) == e