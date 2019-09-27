from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city("Moscow,Russia")
    #weather = False
    if weather:
        return f"Weather: {weather['temp_C']}, feels how: {weather['FeelsLikeC']}"
    else:
        return "Service with weather is not responding on this time"


if __name__ == "__main__":
    app.run(debug=True)