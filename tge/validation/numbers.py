def is_prime(number: int) -> bool:
    """
    Determines whether a given integer is a prime number or not.
    
    :param number: An integer to check for primality.
    :type number: int
    :return: True if the given number is prime, False otherwise.
    :rtype: bool
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_palindrome(string: str) -> bool:
    """
    Check if a given string is a palindrome.

    :param string: A string to be checked.
    :type string: str
    :return: True if the string is a palindrome, False otherwise.
    :rtype: bool
    """
    return string == string[::-1]

def is_leap_year(year: int) -> bool:
    """
    Determine if a given year is a leap year or not.

    A leap year occurs every 4 years, except for years that are both divisible
    by 100 and not divisible by 400. These exceptions ensure that the calendar
    year remains synchronized with the astronomical year.

    Args:
        year (int): The year to be checked for leap year status.

    Returns:
        bool: True if the input year is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_even(number: int) -> bool:
    """
    Determine whether the given integer is an even number.

    Parameters:
    number (int): The integer to be checked for evenness.

    Returns:
    bool: True if the input number is even, False otherwise.
    """
    return number % 2 == 0

def is_odd(number: int) -> bool:
    """
    Determine whether an integer is odd.

    Args:
        number (int): The integer to be checked for oddness.

    Returns:
        bool: True if the input integer is odd, False if it's even.
    """
    return number % 2 == 1 # not is_even(number)