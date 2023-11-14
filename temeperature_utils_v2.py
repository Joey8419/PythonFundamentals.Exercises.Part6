from typing import Iterable, Tuple, Any

def convert_to_kelvin(fahrenheit_temp: float, fahrenheit=None) -> float:

    # Given a float representing a temperature in Fahrenheit, return the corresponding value in Kelvin.

    if fahrenheit is not None:
        # If fahrenheit is provided, ignore fahrenheit_temp and use fahrenheit
        kelvin_temp = (fahrenheit - 32 / 1.8) + 273.15
    else:
        # Use fahrenheit_temp if fahrenheit is not provided
        kelvin_temp = (fahrenheit_temp - 32 / 1.8) + 273.15
    return kelvin_temp



def convert_to_kelvin(celsius_temp: float) -> float:

    # Given a float representing a temperature in Celsius, return the corresponding value in Kelvin.

    kelvin_temp = (celsius_temp + 273.15)
    return kelvin_temp
