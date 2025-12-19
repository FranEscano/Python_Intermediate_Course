import pytest
from process_payment import process_payment

def test_process_payment_with_side_effects(mocker):
    # Mock the charge method of the payment gateway
    mock_payment_gateway = mocker.Mock()
    # Add side effects: Success on first call, raise exception on second call
    mock_payment_gateway.side_effect = ["Success", ValueError("Insufficient funds")]
    # Test successful payment
    assert process_payment(mock_payment_gateway, 100) == "Payment processed successfully"
    # Test payment failure
    with pytest.raises(ValueError, match="Insufficient funds"):
        process_payment(mock_payment_gateway, 200)
    # Verify the mock's behavior
    assert mock_payment_gateway.call_count == 2