from typing import Tuple, Dict, List
from datetime import datetime
from numbers import Number
import time


class Timer:
    def __init__(self, start_time: Number, offset: Number = 0) -> None:
        self.start_time = start_time
        self.offset = offset

    def add_time(self, amount: Number) -> float:
        self.offset += amount
        return self.offset

    def subtract_time(self, amount: Number) -> float:
        self.offset -= amount
        return self.offset

    def get_timer_start_time(self) -> float:
        return self.start_time

    def get_timer_offset(self) -> float:
        return self.offset

    def set_start_time(self, value: Number) -> None:
        self.start_time = value

    def set_offset(self, value: Number) -> None:
        self.offset = value

    def get_time(self) -> float:
        return time.time() - self.start_time + self.offset


class TimerManager:
    def __init__(self) -> None:
        self.timers: Dict[str, Timer] = {}

    def start_timer(self, timer_name: str):
        self.timers[timer_name] = Timer(time.time())

    def stop_timer(self, timer_name: str) -> Number:
        timer = self.timers.pop(timer_name, None)
        if not timer is None:
            return timer.get_time()
        return -1

    def get_timer(self, timer_name: str) -> Number:
        timer = self.timers.get(timer_name, None)
        if not timer is None:
            return timer.get_time()
        return -1

    def does_timer_exist(self, timer_name: str) -> bool:
        return timer_name in self.timers

    def get_all_timers(self) -> List[str]:
        return [timer for timer in self.timers]

    def add_time_to_timer(self, timer_name: str, amount: Number) -> float:
        timer = self.timers.get(timer_name, None)
        if not timer is None:
            return timer.add_time(amount)
        return -1.0

    def remove_time_from_timer(self, timer_name: str, amount: Number) -> float:
        timer = self.timers.get(timer_name, None)
        if not timer is None:
            return timer.subtract_time(amount)
        return -1.0


def get_date() -> Tuple[int, int, int, int, int, int, int]:
    """
    Get the current date and time.

    Returns:
        Tuple[int, int, int, int, int, int, int]: A tuple containing year, month, day,
        hour, minute, second, and day of the week (as an integer, where Monday is 0 and Sunday is 6).
    """
    date = datetime.now()
    day = datetime.weekday(date)
    date = str(date).replace("-", " ").replace(":", " ").replace(".", " ").split(" ")
    return (
        int(date[0]),
        int(date[1]),
        int(date[2]),
        int(date[3]),
        int(date[4]),
        int(date[5]),
        int(day),
    )


def get_timezone_offset() -> int:
    """
    Get the time.timezone offset in hours from UTC (Coordinated Universal Time).

    Returns:
        int: The time.timezone offset, where positive values indicate time ahead of UTC,
             and negative values indicate time behind UTC.
    """
    return int(time.timezone / 3600)


def unix_converter(time: int) -> str:
    """
    Converts a Unix timestamp to a formatted string representing the date and time.

    Args:
        time (int): A Unix timestamp, representing the number of seconds since the epoch.

    Returns:
        str: A formatted string in the format "YYYY MM DD HH MM SS".

    Example:
        >>> unix_converter(1628784000)
        '2021 08 13 00 00 00'
    """
    return datetime.fromtimestamp(time).strftime("%Y %m %d %H %M %S")
