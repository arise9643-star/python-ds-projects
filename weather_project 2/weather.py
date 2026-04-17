import requests
API_KEY = "e4091496937a05c0ebb604e8a6b98a0f"

def get_weather(location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url,timeout=15)
        data = response.json()
        response.raise_for_status()
        print(f"City      : {data['name']}")
        print(f"Weather   : {data['weather'][0]['description']}") 
        print(f"Temp      : {data['main']['temp']}°C")             
        print(f"Humidity  : {data['main']['humidity']}%")
        print(f"Wind  : {data["wind"]["speed"]} km/h")           
        wind_speed = data["wind"]["speed"]
        if wind_speed > 20:
            wind_status = "windy 💨"
        else:
            wind_status = "Calm 🤙" 
        print(f"its {wind_status} outside right now")
        rain = data.get('rain', {}).get('1h', 0)
        if rain > 0:
            print(f"Rain      : {rain}mm 🌧")
        else:
            print("Rain      : No rainfall ☀️")
    except requests.exceptions.HTTPError:
        print(f"location : {location} not found...")
    except requests.ConnectTimeout:
        print("Request timeout try again...")
    except requests.exceptions.ConnectionError:
        print(f"error connecting to network please try again... ")
        
city = input("Which city's weather: ")
get_weather(city)