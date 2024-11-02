from typing import Union, Dict

# This one variable and function have replaced 80 functions
FORMATS: Dict[str, float] = {
    "plank_time": 0.0000000000000000000000000000000000000000000539,
    "yoctosecond": 0.000000000000000000000001,
    "zeptosecond": 0.000000000000000000001,
    "attosecond": 0.000000000000000001,
    "femtosecond": 0.000000000000001,
    "picosecond": 0.000000000001,
    "nanosecond": 0.000000001,
    "microsecond": 0.000001,
    "millisecond": 0.001,
    "second": 1.0,
    "minute": 60.0,
    "hour": 3600.0,
    "day": 86400.0,
    "week": 604800.0,
    "year": 31536000.0,
}


def convert_time(time: Union[int, float], from_unit: str, to_unit: str) -> float:
    """Converts a time value from one unit to another.

    Args:
        time (Union[int, float]): The time value to convert.
        from_unit (str): The unit of the input time value (e.g., "plank_time", "second").
        to_unit (str): The target unit to convert the time value to.
    
    Allowed units:
        - "plank_time"
        - "yoctosecond"
        - "zeptosecond"
        - "attosecond"
        - "femtosecond"
        - "picosecond"
        - "nanosecond"
        - "microsecond"
        - "millisecond"
        - "second"
        - "minute"
        - "hour"
        - "day"
        - "week"
        - "year"

    Returns:
        float: The converted time value in the target unit.

    Raises:
        ValueError: If an invalid unit is specified.
    """
    if from_unit not in FORMATS or to_unit not in FORMATS:
        raise ValueError("Invalid unit specified")
    return time * (FORMATS[from_unit] / FORMATS[to_unit])

__all__ = ["convert_time"]