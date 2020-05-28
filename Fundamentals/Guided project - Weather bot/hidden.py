import time

import pyowm
import pyowm.exceptions.api_response_error
from pyowm.weatherapi25.forecast import Forecast
from pyowm.weatherapi25.forecaster import Forecaster
from pyowm.weatherapi25.location import Location
from pyowm.weatherapi25.weather import Weather


OWM = pyowm.OWM('2665a0fec614053a89064d726b1314df')


def get_forecast(place: str):
    try:
        return OWM.three_hours_forecast(place)
    except pyowm.exceptions.api_response_error.NotFoundError:
        return None


def get_current_values(forecaster: Forecaster):
    forecast: Forecast = forecaster.get_forecast()
    weather: Weather = forecast.get_weathers()[0]
    location: Location = forecast.get_location()

    rain = forecaster.will_be_rainy_at(weather.get_reference_time())
    temp = weather.get_temperature(unit='celsius')['temp']
    wind = weather.get_wind()['speed']
    uvi = OWM.uvindex_around_coords(location.get_lat(), location.get_lon()).get_value()

    return rain, temp, wind, uvi
