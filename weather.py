from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_weather(city):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n ** Get current weather ** ")
    city = input("\nPlease enter city name : ")

    if not bool(city.strip()):
        city = "Doha"

    weather_data = get_weather(city)
    pprint(weather_data)
