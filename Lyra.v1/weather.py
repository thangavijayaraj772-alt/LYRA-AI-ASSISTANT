import requests
import json
from API import CONFIG_FILE
import os

def saved_key():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE,"r") as f:
            config = json.load(f)
            return config.get("weather_api","")
    return ""

def get_weather(city):
    API_KEY=saved_key()
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {desc}."
    except:
        return "Sorry, I couldn't fetch the weather right now."