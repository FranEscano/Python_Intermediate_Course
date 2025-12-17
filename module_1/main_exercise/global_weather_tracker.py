class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name}, {self.country}"

class WeatherRecord:
    def __init__(self, temperature, condition, humidity):
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity

    def __str__(self):
        return (
            f"Temperature: {self.temperature}°C, "
            f"Condition: {self.condition}, "
            f"Humidity: {self.humidity}%"
        )

class WeatherTracker:
    def __init__(self):
        self.records = {}

    def add_city(self, city, weather_record):
        self.records[city] = weather_record

    def update_weather(self, city, weather_record):
        if city in self.records:
            self.records[city] = weather_record
        else:
            print(f"{city} not found in records")

    def list_cities_weather(self):
        for city, weather in self.records.items():
            print(f"{city} -> {weather}")
    
sevilla = City("Sevilla", "Spain")
edinburgh = City("Edinburgh", "UK")

sevilla_weather = WeatherRecord(25, "Sunny", 12)
edinburgh_weather = WeatherRecord(10, "Windy", 63)

tracker = WeatherTracker()
tracker.add_city(sevilla, sevilla_weather)
tracker.add_city(edinburgh, edinburgh_weather)

tracker.list_cities_weather()

print("==========================================================")

tracker.update_weather(
    edinburgh,
    WeatherRecord(9, "Mostly cloudy", 80)
)
tracker.list_cities_weather()

print("==========================================================")

tracker.update_weather(
    "rome",
    WeatherRecord(12, "Rainy", 33)
)

tracker.list_cities_weather()