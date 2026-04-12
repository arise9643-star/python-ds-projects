base_url = "https://api.open-meteo.com/v1/forecast?latitude=26.22&longitude=50.58&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto"
import requests
import pandas as pd
import matplotlib.pyplot as plt
response = requests.get(base_url)
if response.status_code == 200 :
    print("Data retrived")
    response_json = response.json()
    df = pd.DataFrame(response_json["daily"])
else:
    print(f"Failed to collect data Error: {response.status_code}")
highest = df[df["temperature_2m_max"] == df["temperature_2m_max"].max()]
lowest = df[df["temperature_2m_max"] == df["temperature_2m_max"].min()]
print(f"Hottest day: {highest['time'].values[0]} — {highest['temperature_2m_max'].values[0]}°C")
print(f"Coldest day: {lowest['time'].values[0]} — {lowest['temperature_2m_max'].values[0]}°C")
plt.plot(df["time"], df["temperature_2m_max"])
plt.xlabel("date")
plt.ylabel("Max temp")
plt.title("temp over tym")
plt.show()
plt.bar(df["time"], df["precipitation_sum"])
plt.xlabel("Date")
plt.ylabel("Percipitation")
plt.title("percipetation over time")
plt.show()

