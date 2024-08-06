import tkinter as tk
import requests

API_KEY = 'd19769ea1e6df01a4ed10964f20475ea'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather():
    city = entry_city.get()
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404':
        label_weather.config(text="City not found.")
    else:
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = data['weather'][0]['description']
        weather_info = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {weather_description}"
        label_weather.config(text=weather_info)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
label_city = tk.Label(root, text="Enter City:")
label_city.pack()

entry_city = tk.Entry(root)
entry_city.pack()

button_get_weather = tk.Button(root, text="Get Weather", command=get_weather)
button_get_weather.pack()

label_weather = tk.Label(root, text="Weather info will appear here")
label_weather.pack()

# Start the main loop
root.mainloop()
