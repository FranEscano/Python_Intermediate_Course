from global_weather_tracker import get_weather_by_city, City, WeatherTracker, WeatherRecord
import pytest

@pytest.mark.api_mock
def test_update_weather(mocker):
    mock_api_client = mocker.Mock()

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current":{
            "temp_c": 20, 
            "condition": {"text":"Sunny"}, 
            "humidity": 34
            }
    }

    mock_get = mocker.patch("global_weather_tracker.requests.get", return_value = mock_response)
    
    tracker = WeatherTracker()
    dummy_city = City("TestCity", "TestCountry")

    tracker.add_city(dummy_city, None)

    dummy_weather = WeatherRecord(dummy_city)

    tracker.update_weather(dummy_city, dummy_weather)

    assert (tracker.records[dummy_city].temperature >= -50 and tracker.records[dummy_city].temperature <= 60)
    assert isinstance(tracker.records[dummy_city].condition, str) and tracker.records[dummy_city].condition.strip() != ""
    assert (tracker.records[dummy_city].humidity >= 0 and tracker.records[dummy_city].humidity <= 100)
    mock_get.assert_called_once()

@pytest.mark.parametrize(
        "city, country",
        [
            ("Sevilla", "Spain"),
            ("Edinburgh", "United Kingdom"),
            ("Dunedin", "New Zealand"),
            ("Yakutsk", "Russia"),
            ("Agadir", "Morocco"),
            ("Longyearbyen", "Norway"),
            ("Kinshasa", "Democratic Republic of the Congo")
        ]
)
@pytest.mark.api_live
def test_real_api_call(city, country):
    newCity = City(city, country)

    newWeather = WeatherRecord(newCity)

    tracker = WeatherTracker()

    tracker.add_city(newCity, newWeather)

    record = tracker.records[newCity]

    print(record)

    assert (int(record.temperature) >= -50 and int(record.temperature) <= 60)
    assert isinstance(record.condition, str) and record.condition.strip() != ""
    assert (record.humidity >= 0 and record.humidity <= 100)