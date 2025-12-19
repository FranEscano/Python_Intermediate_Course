def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 3 - 1 == 2

# Specifying Test Directories: You can specify custom directories for Pytest to search for test files using the pytest command with the -k flag:
#    pytest -k my_tests
# Ignoring Specific Tests: To exclude specific tests or directories, you can use the -k flag with the not keyword:
#    pytest -k "not slow_tests"