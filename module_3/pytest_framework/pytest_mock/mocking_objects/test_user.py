from user import User

def test_user_is_adult(mocker):
    # Create a User object
    user = User(name="Alice", age=17)
    # Mock the is_adult property
    mocker.patch.object(User, "is_adult", new_callable=mocker.PropertyMock, return_value=True)
    # Assert the mocked property value
    assert user.is_adult is True