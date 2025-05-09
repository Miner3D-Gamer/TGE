from typing import Union
__all__ = ['celsius_to_fahrenheit', 'fahrenheit_to_celsius', 'celsius_to_kelvin', 'kelvin_to_celsius', 'kelvin_to_fahrenheit', 'fahrenheit_to_kelvin']
def celsius_to_fahrenheit(celsius: Union[int,float]) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
    celsius (float): The temperature in Celsius to be converted to Fahrenheit.

    Returns:
    float: The temperature in Fahrenheit.
    """
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit: Union[int,float]) -> float:
    """
    Convert a temperature in Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.
    """
    return (fahrenheit - 32) / 1.8

def celsius_to_kelvin(celsius: Union[int,float]) -> float:
    """
    Convert temperature in degrees Celsius to Kelvin.

    Parameters:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in Kelvin.
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin: Union[int,float]) -> float:
    """
    Convert a temperature from Kelvin to Celsius.

    Parameters:
    kelvin (float): Temperature in Kelvin.

    Returns:
    float: Temperature in Celsius.
    """
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin: Union[int,float]) -> float:
    """
    Convert a temperature in Kelvin to Fahrenheit.

    Parameters:
    kelvin (float): Temperature in Kelvin to be converted.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (kelvin - 273.15) * 1.8 + 32

def fahrenheit_to_kelvin(fahrenheit: Union[int,float]) -> float:
    """
    Convert temperature from Fahrenheit to Kelvin.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Kelvin.
    """
    return (fahrenheit - 32) / 1.8 + 273.15