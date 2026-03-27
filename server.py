from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/weather")
def fetch_weather():
    city = request.args.get('city')

    if not bool(city.strip()):
        city = "Doha"

    weather_data = get_weather(city)

    if not weather_data['cod'] == 200:
        return render_template('city_not_found.html', city=city,)

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        humidity=weather_data["main"]["humidity"],
        wind_speed=f"{weather_data['wind']['speed']:.1f}",
        temp_min=f"{weather_data['main']['temp_min']:.1f}",
        temp_max=f"{weather_data['main']['temp_max']:.1f}",
        icon=weather_data["weather"][0]["icon"],
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
