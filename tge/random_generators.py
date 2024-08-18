from typing import List, Union, Tuple, Any
import random

from requests import get as requests_get
from .codec.codec import html

# number between 0 and 1:


def generate_name(
    gender: int,
) -> str:
    """
    Generate a random name based on the specified gender or unisex option.

    Args:
        gen (int): An integer representing the desired gender or option for the name.
                0: Male (can also be represented as "m" or "male")
                1: Female (can also be represented as "f" or "female")
                2: Unisex (can also be represented as "u", "unisex", or "unidentified")
                3: Both (can also be represented as "both" or "b")

    Returns:
        str: A randomly generated name based on the specified gender or option.
            Returns an empty string if the input is invalid.

    Note:
        This function uses the "https://www.behindthename.com/random/random.php" endpoint to
        generate random names.

    """

    if gender == 0 or "m" or "male":
        gender = "m"
    elif gender == 1 or "f" or "female":
        gender = "f"
    elif gender == 2 or "u" or "unisex" or "unidentified":
        gender = "u"
    elif gender == 3 or "both" or "b":
        gender = "both"
    else:
        raise ValueError("Invalid gender input.")
    url = "https://www.behindthename.com/random/random.php"
    params = {"gender": gender, "number": "1", "sets": "1", "surname": "", "all": "yes"}
    response = requests_get(url, params=params)
    name_text = str(response.text.split("\n")[165])
    idx = name_text.find('class="plain">') + 14
    name_text = name_text[idx:]
    idx2 = name_text.find("<")

    name = name_text[:idx2]
    name = html.decode(name)
    return name


def generate_password(length: int) -> str:
    """
    Generates a random password of the given length.

    :param length: An integer representing the length of the password.
    :type length: int

    :return: A string representing the generated password.
    :rtype: str
    """
    chars = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
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
            """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        )
        for _ in range(length)
    )


def random_int(min: int, max: int, float: bool = False) -> int:
    """
    Returns a random integer between `min` and `max`, inclusive.

    Args:
        min (int): The minimum value the random integer can take.
        max (int): The maximum value the random integer can take.
        float (bool): If True, returns a float instead of an integer.

    Returns:
        Tuple[bool, Union[int, float]] or Tuple[bool, str]:
            If the function succeeds, returns a tuple with the first element False and the random integer or float as the second element.
            If the function fails because `min` is greater than `max`, returns a tuple with the first element True and a message as the second element.
    """

    if min < max:
        if float:
            return random.uniform(min, max)
        else:
            return random.randint(min, max)
    else:
        if min == max:
            return min
        else:
            return 0
