from typing import Iterable, Tuple, Any


def convert_to_celsius(fahrenheit_temp: float, fahrenheit=None) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.
z
    :param fahrenheit:
    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    if fahrenheit is not None:
        # If fahrenheit is provided, ignore fahrenheit_temp and use fahrenheit
        celsius_temp = (fahrenheit - 32) * 5 / 9
    else:
        # Use fahrenheit_temp if fahrenheit is not provided
        celsius_temp = (fahrenheit_temp - 32) * 5 / 9
    return celsius_temp


def convert_to_fahrenheit(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    fahrenheit_temp = (celsius_temp * 9 / 5) + 32
    return fahrenheit_temp


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> tuple[tuple[Any, float], ...]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    # Create a list to store tuples of original and converted temps
    converted_temperatures = []

    # Iterate through each temp
    for temp in temperatures:
        # Check the specified unit of measurement for conversion
        if input_unit_of_measurement == 'c':
            # Convert temp to Fahrenheit if the unit is Celsius
            converted_temperatures.append((temp, convert_to_fahrenheit(temp)))
        elif input_unit_of_measurement == 'f':
            # Convert temp to Celsius if unit is Fahrenheit
            converted_temperatures.append((temp, convert_to_celsius(temp)))

    # Return result as tuple
    return tuple(converted_temperatures)

