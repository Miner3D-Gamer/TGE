from typing import Tuple
import random


# from .codec.codec import html


__all__ = [ "generate_password", "random_bool", "generate_random_hex_color","generate_random_color","generate_random_hex_color"]

def generate_password(length: int) -> str:
    """
    Generates a random password of the given length.

    :param length: An integer representing the length of the password.
    :type length: int

    :return: A string representing the generated password.
    :rtype: str
    """
    chars = r"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return "".join(random.choice(chars) for _ in range(length))


def random_bool() -> bool:
    """
    Returns a random boolean value.

    The function uses the `getrandbits` method from the `random` module to
    generate a random integer with one bit (i.e., either 0 or 1), and then
    converts it to a boolean value using the `bool` function. The probability
    of getting a `True` or `False` result is equal (i.e., 50/50).

    :return: A random boolean value (`True` or `False`).
    :rtype: bool
    """
    return bool(random.getrandbits(1))


def generate_random_hex_color() -> str:
    """
    Generates a random hex color code.

    :return: A string representing a hex color code.
    :rtype: str
    """
    return "#" + "".join(random.choice("0123456789ABCDEF") for _ in range(6))


def generate_random_color() -> Tuple[int, int, int]:
    """
    Generates a random color by generating three random integers between 0 and 255, inclusive.
    No parameters are taken in.
    Returns a tuple of three integers representing the RGB values of the generated color.
    """
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def generate_random_string(length: int = 1) -> str:
    """
    Generates a random string of specified length.

    Args:
        length (int): The length of the random string to be generated.

    Returns:
        str: A random string of specified length.
    """
    return "".join(
        random.choice(
            r"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        )
        for _ in range(length)
    )

