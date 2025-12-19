from log_message import log_message
def test_log_message_with_spy(mocker):
    # Spy on the info method of the logger
    mock_logger = mocker.Mock()
    spy_info = mocker.spy(mock_logger, "info")
    # Call the function
    result = log_message(mock_logger, "Test message")
    # Assert the returned value
    assert result == "Logged: Test message"
    # Verify spy behavior
    spy_info.assert_called_once_with("Test message")
    assert spy_info.call_count == 1