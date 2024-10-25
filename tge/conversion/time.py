from typing import Union


def seconds_to_minutes(seconds: Union[int, float]) -> float:
    return seconds // 60


def minutes_to_seconds(minutes: Union[int, float]) -> float:
    return minutes * 60


def seconds_to_hours(seconds: Union[int, float]) -> float:
    return seconds // 3600


def hours_to_seconds(hours: Union[int, float]) -> float:
    return hours * 3600


def seconds_to_days(seconds: Union[int, float]) -> float:
    return seconds // 86400


def days_to_seconds(days: Union[int, float]) -> float:
    return days * 86400


def seconds_to_weeks(seconds: Union[int, float]) -> float:
    return seconds // 604800


def weeks_to_seconds(weeks: Union[int, float]) -> float:
    return weeks * 604800


def seconds_to_years(seconds: Union[int, float]) -> float:
    return seconds // 31536000


def years_to_seconds(years: Union[int, float]) -> float:
    return years * 31536000


def minutes_to_hours(minutes: Union[int, float]) -> float:
    return minutes // 60


def hours_to_minutes(hours: Union[int, float]) -> float:
    return hours * 60


def minutes_to_days(minutes: Union[int, float]) -> float:
    return minutes // 1440


def days_to_minutes(days: Union[int, float]) -> float:
    return days * 1440


def minutes_to_weeks(minutes: Union[int, float]) -> float:
    return minutes // 10080


def weeks_to_minutes(weeks: Union[int, float]) -> float:
    return weeks * 10080


def minutes_to_years(minutes: Union[int, float]) -> float:
    return minutes // 525600


def years_to_minutes(years: Union[int, float]) -> float:
    return years * 525600


def weeks_to_years(weeks: Union[int, float]) -> float:
    return weeks * 52


def years_to_weeks(years: Union[int, float]) -> float:
    return years // 52


def years_to_days(years: Union[int, float]) -> float:
    return years * 365


def days_to_years(days: Union[int, float]) -> float:
    return days // 365


def days_to_weeks(days: Union[int, float]) -> float:
    return days // 7


def weeks_to_days(weeks: Union[int, float]) -> float:
    return weeks * 7


def days_to_hours(days: Union[int, float]) -> float:
    return days * 24


def hours_to_days(hours: Union[int, float]) -> float:
    return hours * 24


def second_to_milliseconds(seconds: Union[int, float]) -> float:
    return seconds * 1000


def milliseconds_to_second(milliseconds: Union[int, float]) -> float:
    return milliseconds / 1000


def minutes_to_milliseconds(minutes: Union[int, float]) -> float:
    return minutes * 60000


def milliseconds_to_minutes(milliseconds: Union[int, float]) -> float:
    return milliseconds / 60000


def hours_to_milliseconds(hours: Union[int, float]) -> float:
    return hours * 3600000


def milliseconds_to_hours(milliseconds: Union[int, float]) -> float:
    return milliseconds / 3600000


def days_to_milliseconds(days: Union[int, float]) -> float:
    return days * 86400000


def milliseconds_to_days(milliseconds: Union[int, float]) -> float:
    return milliseconds / 86400000


def weeks_to_milliseconds(weeks: Union[int, float]) -> float:
    return weeks * 604800000


def milliseconds_to_weeks(milliseconds: Union[int, float]) -> float:
    return milliseconds / 604800000


def years_to_milliseconds(years: Union[int, float]) -> float:
    return years * 31536000000


def milliseconds_to_years(milliseconds: Union[int, float]) -> float:
    return milliseconds / 31536000000


def seconds_to_microseconds(seconds: Union[int, float]) -> float:
    return seconds * 1000000


def microseconds_to_seconds(microseconds: Union[int, float]) -> float:
    return microseconds / 1000000


def seconds_to_nanoseconds(seconds: Union[int, float]) -> float:
    return seconds * 1000000000


def nanoseconds_to_seconds(nanoseconds: Union[int, float]) -> float:
    return nanoseconds / 1000000000


def milliseconds_to_nanoseconds(milliseconds: Union[int, float]) -> float:
    return milliseconds * 1000000000


def nanoseconds_to_milliseconds(nanoseconds: Union[int, float]) -> float:
    return nanoseconds / 1000000000


def nanoseconds_to_microseconds(nanoseconds: Union[int, float]) -> float:
    return nanoseconds / 1000000


def microseconds_to_nanoseconds(microseconds: Union[int, float]) -> float:
    return microseconds * 1000000


def hours_to_nanoseconds(hours: Union[int, float]) -> float:
    return hours * 1000000000000


def nanoseconds_to_hours(nanoseconds: Union[int, float]) -> float:
    return nanoseconds / 1000000000000


def days_to_nanoseconds(days: Union[int, float]) -> float:
    return days * 8640000000000


def nanoseconds_to_days(nanoseconds: Union[int, float]) -> float:
    return nanoseconds / 8640000000000


def weeks_to_nanoseconds(weeks: Union[int, float]) -> float:
    return weeks * 60480000000000


def nanoseconds_to_weeks(nanoseconds: Union[int, float]) -> float:
    return nanoseconds / 60480000000000


def years_to_nanoseconds(years: Union[int, float]) -> float:
    return years * 315360000000000


def nanoseconds_to_years(nanoseconds: Union[int, float]) -> float:
    return nanoseconds / 315360000000000


def hours_to_microseconds(hours: Union[int, float]) -> float:
    return hours * 1000000


def microseconds_to_hours(microseconds: Union[int, float]) -> float:
    return microseconds / 1000000


def day_to_microseconds(day: Union[int, float]) -> float:
    return day * 86400000


def microseconds_to_day(microseconds: Union[int, float]) -> float:
    return microseconds / 86400000


def week_to_microseconds(hour: Union[int, float]) -> float:
    return hour * 604800000


def microseconds_to_week(microseconds: Union[int, float]) -> float:
    return microseconds / 604800000


def year_to_microseconds(year: Union[int, float]) -> float:
    return year * 31536000000


def microseconds_to_year(microseconds: Union[int, float]) -> float:
    return microseconds / 31536000000


def seconds_to_picoseconds(seconds: Union[int, float]) -> float:
    return seconds * 1000000000


def picoseconds_to_seconds(picoseconds: Union[int, float]) -> float:
    return picoseconds / 1000000000


def microseconds_to_picoseconds(microseconds: Union[int, float]) -> float:
    return microseconds * 1000000000


def picoseconds_to_microseconds(picoseconds: Union[int, float]) -> float:
    return picoseconds / 1000000000


def nanoseconds_to_picoseconds(nanoseconds: Union[int, float]) -> float:
    return nanoseconds * 1000000000000


def picoseconds_to_nanoseconds(picoseconds: Union[int, float]) -> float:
    return picoseconds / 1000000000000


def milliseconds_to_picoseconds(milliseconds: Union[int, float]) -> float:
    return milliseconds * 1000000


def picoseconds_to_milliseconds(picoseconds: Union[int, float]) -> float:
    return picoseconds / 1000000


def minutes_to_picoseconds(minutes: Union[int, float]) -> float:
    return minutes * 60000000000


def picoseconds_to_minutes(picoseconds: Union[int, float]) -> float:
    return picoseconds / 60000000000


def hours_to_picoseconds(hours: Union[int, float]) -> float:
    return hours * 3600000000000


def picoseconds_to_hours(picoseconds: Union[int, float]) -> float:
    return picoseconds / 3600000000000


def weeks_to_picoseconds(weeks: Union[int, float]) -> float:
    return weeks * 60480000000000


def picoseconds_to_weeks(picoseconds: Union[int, float]) -> float:
    return picoseconds / 60480000000000


def years_to_picoseconds(years: Union[int, float]) -> float:
    return years * 315360000000000


def picoseconds_to_years(picoseconds: Union[int, float]) -> float:
    return picoseconds / 315360000000000


def milliseconds_to_seconds(milliseconds: Union[int, float]) -> float:
    return milliseconds / 1000


def seconds_to_milliseconds(seconds: Union[int, float]) -> float:
    return seconds * 1000
