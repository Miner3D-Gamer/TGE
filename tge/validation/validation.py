import re
from ipaddress import IPv4Address, IPv6Address, AddressValueError

from . import minecraft
from . import numbers




def validate_email(email: str) -> bool:
    """
    Validate an email address using a regular expression pattern match.

    :param email: A string representing an email address.
    :type email: str
    :return: A boolean indicating whether the email address is valid or not.
    :rtype: bool
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_password(
    password: str,
    length: int,
    upper: bool,
    lower: bool,
    digit: bool,
    overwrite_special_characters: bool,
    overwritten_special_characters: str,
) -> bool:
    """
    Validates a password based on specified criteria.

    Args:
        password (str): The password string to be validated.
        length (int): The minimum required length of the password.
        upper (bool): Whether the password must contain at least one uppercase letter.
        lower (bool): Whether the password must contain at least one lowercase letter.
        digit (bool): Whether the password must contain at least one digit.
        overwrite_special_characters (bool): If True, the provided special characters will be used for validation.
                                            If False, a default set of special characters will be used.
        overwritten_special_characters (str): A string containing special characters to be used for validation,
                                            applicable only if overwrite_special_characters is True.

    Returns:
        bool: True if the password is valid based on the specified criteria, False otherwise.
    """
    if len(password) < length:
        return False

    if upper:
        if not any(char.isupper() for char in password):
            return False

    if lower:
        if not any(char.islower() for char in password):
            return False

    if digit:
        if not any(char.isdigit() for char in password):
            return False


    if overwrite_special_characters:
        special_characters = overwritten_special_characters
    else:
        special_characters = "!@#$%^&*()_-+=<>?/\\"
    if not any(char in special_characters for char in password):
        return False

    return True


def validate_strong_password(password: str) -> bool:
    """
    Validate if a given password meets the criteria for a strong password.

    A strong password must satisfy the following conditions:
    - Have a minimum length of 12 characters.
    - Contain at least one uppercase letter.
    - Contain at least one lowercase letter.
    - Contain at least one digit.
    - Optionally, special characters can be included, with the possibility to overwrite the default set of characters.

    Args:
        password (str): The password string to be validated.

    Returns:
        bool: True if the password meets the strong password criteria, False otherwise.
    """
    return validate_password(
        password,
        12,
        upper=True,
        lower=True,
        digit=True,
        overwrite_special_characters=True,
        overwritten_special_characters="!@#$%^&*()_-+=<>?/\\",
    )


def validate_credit_card(number: str) -> bool:
    """
    Validates a credit card number using the Luhn algorithm.

    This function takes an integer representing a credit card number and performs the
    Luhn algorithm to determine its validity.

    The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a
    simple checksum formula used to validate a variety of identification numbers,
    including credit card numbers. It works by performing a series of mathematical
    operations on the digits of the credit card number and checking whether the
    resulting sum is divisible by 10.

    Args:
        number (int): The credit card number to be validated.

    Returns:
        bool: True if the credit card number is valid according to the Luhn algorithm,
            False otherwise.
    """
    number = number.replace(" ", "").replace("-", "")

    if not number.isdigit():
        return False

    reversed_number = number[::-1]

    checksum = 0
    for i in range(len(reversed_number)):
        digit = int(reversed_number[i])

        if i % 2 == 1:
            digit *= 2

        if digit > 9:
            digit -= 9

        checksum += digit

    return checksum % 10 == 0


def check_valid_ipv6(ip_address: str) -> bool:
    """
    Check the validity of an IPv6 address.

    This function takes an IPv6 address in string format and attempts to create an IPv6Address
    object from the 'ip_address' parameter. If the address is valid, the function returns True;
    otherwise, it returns False.

    Parameters:
    ip_address (str): A string representing the IPv6 address to be checked.

    Returns:
    bool: True if the IPv6 address is valid, False if it is not.
    """
    try:
        _ = IPv6Address(ip_address)
    except AddressValueError:
        return False
    else:
        return True


def check_valid_ipv4(ip_address: str) -> bool:
    """
    Check the validity of an IPv4 address.

    This function takes an IPv4 address in string format and attempts
    to create an IPv4Address object from the `ipaddress` module. If the
    address is valid, the function returns True. If the address is not
    a valid IPv4 address, it returns False.

    Args:
        ip_address (str): The IPv4 address to be checked.

    Returns:
        bool: True if the input is a valid IPv4 address, False otherwise.
    """
    try:
        _ = IPv4Address(ip_address)
    except AddressValueError:
        return False
    else:
        return True

__all__ = ['minecraft', 'numbers', "check_valid_ipv4", "check_valid_ipv6", "validate_email", "validate_password", "validate_strong_password", "validate_credit_card"]