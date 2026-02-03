import requests
from dotenv import load_dotenv
import os

# Try to load it
load_dotenv()

def clean_env_var(name):
    val = os.getenv(name)
    if val:
        return val.encode('ascii', 'ignore').decode('ascii').strip().strip("'").strip('"')
    return None

api_key = clean_env_var('WEATHER_API_KEY')
apiUrl = clean_env_var('BASE_URL')

def get_weather_by_city(city):

    try:
        manual_url=f"{apiUrl}?key={api_key}&q={city.name}&aqi=no"   
        response = requests.get(manual_url)

        return response.json()
    
    except requests.exceptions.HTTPError:
        return f"Error: Could not find weather for '{city}'. Check the spelling!"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name}, {self.country}"

class WeatherRecord:
    def __init__(self, city):
        self.temperature = 0
        self.condition = "Unknown"
        self.humidity = 0

        if not isinstance(city, City):
            print(f"Cannot fetch weather for {city}. It's not a City object!")
            return
        
        try:
            data = get_weather_by_city(city)

            self.temperature = data['current']['temp_c']
            self.condition = data['current']['condition']['text']
            self.humidity = data['current']['humidity']
    
        except Exception as e:
            print(f"API error: {e}")

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
        if not isinstance(city, City):
            print(f"FAIL: '{city}' must be a City object, not a string")
            return
        
        if city in self.records:
            self.records[city] = weather_record
            print(f"Updated weather for {city.name}.")
        else:
            print(f"FAILED: {city} not found in records")

    def list_cities_weather(self):
        for city, weather in self.records.items():
            print(f"{city} -> {weather}")
    
# sevilla = City("Sevilla", "Spain")
# edinburgh = City("Edinburgh", "UK")

# sevilla_weather = WeatherRecord(sevilla)
# edinburgh_weather = WeatherRecord(edinburgh)


# tracker = WeatherTracker()
# tracker.add_city(sevilla, sevilla_weather)
# tracker.add_city(edinburgh, edinburgh_weather)

# tracker.list_cities_weather()

# print("==========================================================")

# tracker.update_weather(
#     edinburgh,
#     WeatherRecord(edinburgh)
# )
# tracker.list_cities_weather()

# print("==========================================================")
# rome = "Rome"
# tracker.update_weather(
#     "Rome",
#     WeatherRecord(rome)
# )

# tracker.list_cities_weather()