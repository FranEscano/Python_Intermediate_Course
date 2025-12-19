from calculate_discount import calculate_discount
from pytest_mock import mocker

def test_calculate_discount(mocker):
    # Mock the get_discount method
    mock_discount_provider = mocker.Mock()
    mock_discount_provider.get_discount.return_value = 10 # Mocked discount value
    # Call the function with the mocked dependency
    result = calculate_discount(100, mock_discount_provider)
    # Assert the calculated discount is correct
    assert result == 90
    mock_discount_provider.get_discount.assert_called_once()