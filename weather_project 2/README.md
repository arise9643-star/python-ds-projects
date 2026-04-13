# Weather App 🌤

A Python script that fetches real-time weather data for any city.

## What it does
- Search any city and get live weather data
- Shows temperature, humidity, wind speed and rain status
- Tells you if its windy or calm outside
- Handles errors cleanly

## How to run it

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org)
2. Paste your key in the `API_KEY` variable in the script
3. Install the required library:
pip install requests
4. Run the script:
python weather.py
5. Type any city name when asked

## Example Output
Which city's weather: Manama
City      : Manama
Weather   : clear sky
Temp      : 25.65°C
Humidity  : 48%
Wind      : 6.3 km/h — Calm 🤙
Rain      : No rainfall ☀️

## Built with
- Python
- Requests library
- [OpenWeatherMap API](https://openweathermap.org)