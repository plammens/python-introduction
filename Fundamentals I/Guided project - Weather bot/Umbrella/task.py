# ----- Don't edit this part -----
import importlib.util
import os

HIDDEN_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../hidden.py'))
spec = importlib.util.spec_from_file_location("hidden", HIDDEN_PATH)
hidden = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hidden)

# ----- Your solution goes here -----
city = input("Enter a city: ")

forecast = hidden.get_forecast(city)  # don't edit this line

if forecast is None:
    print("Invalid city name")
else:
    rain, temp, wind, uvi = hidden.get_current_values(forecast)  # don't edit this line

    if rain:
        print("Take an umbrella!")
