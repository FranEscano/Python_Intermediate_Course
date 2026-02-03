import pytest
import sys

# ===================== Skipping tests (skip) ========================

# A test that will always be skipped
@pytest.mark.skip(reason="This test is temporarily disabled.")
def test_example_skip():
    assert 2 + 2 == 4

# A test that will be skipped if it's run on a Python version earlier that 3.8
@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or later")
def test_example_skipif():
    assert 3 * 3 == 9

# ===================== Expected Failures (xfail) ========================

# A test that's expected to fail
@pytest.mark.xfail(reason="Expected to fail until we fix the bug")
def test_example_xfail():
    assert 2 * 3 == 7

# A normal test that's exptected to pass
def test_example_xpass():
    assert 3 *2 == 6

# ===================== Specifying Fixtures (usefixtures) ========================

@pytest.fixture
def database_data():
    return {"username": "Alice", "password": "password123"}

@pytest.mark.usefixtures("database_data")
@pytest.mark.xfail(reason="The error is happening because @usefixtures does NOT inject the fixture as a variable into the test. It only runs the fixture for setup/teardown")
# Test function using the database_data fixture
def test_database_entry():
    assert database_data["username"] == "Alice"
    assert database_data["password"] == "password123"

# ===================== Specifying Fixtures (fixtures as input argument) ========================

# A fixture returning a sample database entry
@pytest.fixture
def database_data2():
    return {"username": "Alice", "password": "password123"}

# Test function using the database_data fixture as a parameter
def test_database_entry2(database_data):
    assert database_data["username"] == "Alice"
    assert database_data["password"] == "password123"

# ===================== Parameterization (Parametrize) ========================

@pytest.mark.parametrize(
    "test_input,expected", # the input args to parametrize
    [ # the parameters are given as a list of tuples
        (1, 3),
        (3, 5),
        (5, 7)
    ]
)
def test_addition(test_input, expected):
    assert test_input + 2 == expected

# ===================== Parameterization (Parametrize with ids) ========================

@pytest.mark.parametrize("input, expected", [(1, 2), (3, 4)], ids=["case_1", "case_2"])
def test_add(input, expected):
    assert input + 1 ==  expected

def idfn(val):
    return f"input_{val}"

@pytest.mark.parametrize("input, expected", [(2, 3), (3, 4)], ids=idfn)
def test_add2(input, expected):
    assert input + 1 ==  expected

@pytest.mark.parametrize("a, b, op, expected", [
    pytest.param(1, 2, "+", 3, id="add"),
    pytest.param(3, 1, "-", 2, id="sub"),
    pytest.param(2, 3, "*", 7, marks=pytest.mark.xfail, id="xfail_case"),
    pytest.param(3, 4, "/", 1, marks=pytest.mark.skip, id="skip_case"),
])
def test_calc(a, b, op, expected):
    assert calc(a, b, op) == expected

def calc(a, b, op):
    if(op == "+"):
        return a + b
    if(op == "-"):
        return a - b
    if(op == "*"):
        return a * b
    if(op == "/"):
        return a / b
    
from dataclasses import dataclass
@dataclass
class CalcCase:
    name: str
    a: int
    b: int
    result: int
    op: str = "+"

@pytest.mark.parametrize("tc", [
    CalcCase("add", a=1, b=2, result=3),
    CalcCase("add-neg", a=-2, b=-3, result=-5),
    CalcCase("sub", a=2, b=1, op="-", result=1),
], ids=lambda tc: tc.name)
def test_calc2(tc):
    assert calc(tc.a, tc.b, tc.op) == tc.result

# ===================== Custom Markers (Tagging Tests) ========================

@pytest.mark.smoke
def test_homepage_loads():
    # Test to check if the homepage loads quickly
    assert ...

@pytest.mark.regression
def test_login_successful():
    # Test to check if the login process works as expected
    assert ...

@pytest.mark.regression
def test_user_profile_uodate():
    # Test to check if user profile updates are saved correctly
    assert ...