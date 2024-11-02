#type: ignore
__all__=['celsius_to_fahrenheit','fahrenheit_to_celsius','celsius_to_kelvin','kelvin_to_celsius','kelvin_to_fahrenheit','fahrenheit_to_kelvin']
def celsius_to_fahrenheit(celsius):return celsius*1.8+32
def fahrenheit_to_celsius(fahrenheit):return(fahrenheit-32)/1.8
def celsius_to_kelvin(celsius):return celsius+273.15
def kelvin_to_celsius(kelvin):return kelvin-273.15
def kelvin_to_fahrenheit(kelvin):return(kelvin-273.15)*1.8+32
def fahrenheit_to_kelvin(fahrenheit):return(fahrenheit-32)/1.8+273.15