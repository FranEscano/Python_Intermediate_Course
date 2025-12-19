import sys
import pytest

@pytest.mark.skip(reason="This test is not ready yet")
def test_skip_example():
    assert 1 + 1 == 2

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_skip_if_example():
    assert 2 * 2 == 4

@pytest.mark.xfail(reason="Known bug #123")
def test_expected_failure():
    assert 1 / 0 == 1

@pytest.mark.xfail(strict=True, reason="Known bug #124")
def test_expected_failure_strict():
    assert 1 + 1 == 2