

def convert_meters_to_miles(meters: float) -> float:
    """
    Convert a distance in meters to miles.

    Parameters:
    meters (float): Distance in meters to be converted to miles.

    Returns:
    float: Distance in miles.
    """
    return meters * 0.000621371192237334

def convert_miles_to_meters(miles: float) -> int:
    """
    Convert miles to meters.

    Parameters:
    miles (float): The distance in miles to be converted to meters.

    Returns:
    int: The equivalent distance in meters.
    """
    return miles * 1609.344

def convert_pounds_to_kilograms(pounds: float) -> float:
    """
    Convert a weight in pounds to kilograms.

    Parameters:
    pounds (float): The weight in pounds to be converted to kilograms.

    Returns:
    float: The equivalent weight in kilograms.
    """
    return pounds * 0.45359237

def convert_kilograms_to_pounds(kilograms: float) -> float:
    """
    Convert a weight in kilograms to pounds.

    Parameters:
        kilograms (float): The weight in kilograms to be converted.

    Returns:
        float: The converted weight in pounds.
    """
    return kilograms / 0.45359237