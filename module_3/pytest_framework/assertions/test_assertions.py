def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

def test_string_equality():
    assert "pytest" == "pytest"

def test_string_contains():
    word = "pytest"
    assert "py" in word

def test_list_equality():
    expected = [1,2,3]
    result = [1,2,3]
    assert result == expected

def test_dict_equality():
    expected = {"name": "Alice", "age": 25}
    result = {"name": "Alice", "age": 26}
    assert result == expected
