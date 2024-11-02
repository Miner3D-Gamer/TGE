from typing import Tuple, Dict, List
from datetime import datetime
from typing import Union
import time


class Timer:
    def __init__(self, start_time: Union[int,float], offset: Union[int,float] = 0) -> None:
        """Timer class for tracking time.

        Args:
            start_time (Union[int,float]): The start time of the timer.
            offset (Union[int,float], optional): The offset of the timer. Defaults to 0.
        """
        self.start_time = start_time
        self.offset = offset

    def add_time(self, amount: Union[int,float]) -> float:
        """Add time to the timer.

        Args:
            amount (Union[int,float]): The amount of time to add.

        Returns:
            float: The new offset of the timer.
        """
        self.offset += amount
        return self.offset

    def subtract_time(self, amount: Union[int,float]) -> float:
        """Subtract time from the timer.

        Args:
            amount (Union[int,float]): The amount of time to subtract.

        Returns:
            float: The new offset of the timer.
        """
        self.offset -= amount
        return self.offset

    def get_timer_start_time(self) -> float:
        """Get the start time of the timer.

        Returns:
            float: The start time of the timer.
        """
        return self.start_time

    def get_timer_offset(self) -> float:
        """Get the offset of the timer.

        Returns:
            float: The offset of the timer.
        """
        return self.offset

    def set_start_time(self, value: Union[int,float]) -> None:
        """Set the start time of the timer.

        Args:
            value (Union[int,float]): The new start time of the timer.
        """
        self.start_time = value

    def set_offset(self, value: Union[int,float]) -> None:
        """Set the offset of the timer.

        Args:
            value (Union[int,float]): The new offset of the timer.
        """
        self.offset = value

    def get_time(self) -> float:
        """Get the current time of the timer.

        Returns:
            float: The current time of the timer.
        """
        return time.time() - self.start_time + self.offset


class TimerManager:
    def __init__(self) -> None:
        """TimerManager class for tracking time.
        """
        self.timers: Dict[str, Timer] = {}

    def start_timer(self, timer_name: str)-> None:
        """Start a timer.

        Args:
            timer_name (str): The name of the timer.
        """
        self.timers[timer_name] = Timer(time.time())

    def stop_timer(self, timer_name: str) -> Union[int,float]:
        """Stop a timer.

        Args:
            timer_name (str): The name of the timer.

        Returns:
            Union[int,float]: The time of the timer.
        """
        timer = self.timers.pop(timer_name, None)
        if not timer is None:
            return timer.get_time()
        return -1

    def get_timer(self, timer_name: str) -> Union[int,float]:
        """Get the time of a timer.

        Args:
            timer_name (str): The name of the timer.

        Returns:
            Union[int,float]: The time of the timer.
        """
        timer = self.timers.get(timer_name, None)
        if not timer is None:
            return timer.get_time()
        return -1

    def does_timer_exist(self, timer_name: str) -> bool:
        """Check if a timer exists."""
        return timer_name in self.timers

    def get_all_timers(self) -> List[str]:
        """Get all timers."""
        return [timer for timer in self.timers]

    def add_time_to_timer(self, timer_name: str, amount: Union[int,float]) -> float:
        """Add time to a timer.

        Args:
            timer_name (str): The name of the timer.
            amount (Union[int,float]): The amount of time to add.

        Returns:
            float: The new time of the timer.
        """
        timer = self.timers.get(timer_name, None)
        if not timer is None:
            return timer.add_time(amount)
        return -1.0

    def remove_time_from_timer(self, timer_name: str, amount: Union[int,float]) -> float:
        """Remove time from a timer.

        Args:
            timer_name (str): The name of the timer.
            amount (Union[int,float]): The amount of time to remove.

        Returns:
            float: The new time of the timer.
        """
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
    new_date = str(date).replace("-", " ").replace(":", " ").replace(".", " ").split(" ")
    return (
        int(new_date[0]),
        int(new_date[1]),
        int(new_date[2]),
        int(new_date[3]),
        int(new_date[4]),
        int(new_date[5]),
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
