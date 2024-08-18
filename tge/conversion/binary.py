from math import ceil

HEX_CHARACTERS = "0123456789ABCDEF"





def convert_binary_to_decimal(binary: str) -> int:
    """
    Convert a binary number to its decimal equivalent.

    Parameters:
    binary (str): A binary number represented as a string.

    Returns:
    int: The decimal equivalent of the given binary number.
    """
    decimal = 0
    power = 0

    for digit in reversed(str(binary)):
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

def convert_decimal_to_binary(decimal: int) -> str:
    """
    Convert a decimal integer to its binary representation.

    Parameters:
    decimal (int): The decimal integer to be converted.

    Returns:
    str: The binary representation of the input decimal integer.
    """
    binary = ''
    while decimal > 0:
        binary += str(decimal % 2)
        decimal //= 2
    return binary[::-1]

def convert_decimal_to_hexadecimal(decimal: int) -> str:
    """
    Convert a decimal integer to its hexadecimal representation.

    Parameters:
    decimal (int): The decimal integer to be converted.

    Returns:
    str: The hexadecimal representation of the input decimal number.
    """
    if decimal == 0:
        return "0"

    hex_string = ""
    while decimal > 0:
        remainder = decimal % 16
        hex_digit = HEX_CHARACTERS[remainder]
        hex_string = hex_digit + hex_string
        decimal = decimal // 16

    return hex_string

def convert_hexadecimal_to_decimal(hexadecimal: str) -> int:
    """
    Convert a hexadecimal string to its decimal representation.

    Parameters:
    hexadecimal (str): A string representing a hexadecimal number.

    Returns:
    int: The decimal representation of the input hexadecimal number.

    Raises:
    ValueError: If the input is not a valid hexadecimal string.
    """
    if hexadecimal == "0":
        return 0

    decimal = 0
    for hex_digit in reversed(hexadecimal):
        decimal = decimal * 16 + HEX_CHARACTERS.index(hex_digit)

def convert_bytes(value: int, from_unit: str, to_unit: str) -> int:
    units = [
        "bytes",
        "kilobytes",
        "megabytes",
        "gigabytes",
        "terabytes",
        "petabytes",
        "exabytes",
        "zettabytes",
        "yottabytes",
        "brontobytes",
        "geopbytes",
        "xobibytes",
        "yobibytes"
    ]

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit specified")

    bytes_value = value * (1024 ** units.index(from_unit))
    return ceil(bytes_value / (1024 ** units.index(to_unit)))


def convert_byte_to_kilobyte(bytes: int) -> int:
    """
    Converts a value from bytes to kilobytes.

    Args:
        bytes (int): The value in bytes.

    Returns:
        float: The equivalent value in kilobytes.
    """
    return convert_bytes(bytes, "bytes", "kilobytes")


def convert_kilobyte_to_megabyte(kilobytes: int) -> int:
    """
    Converts a value from kilobytes to megabytes.

    Args:
        kilobytes (int): The value in kilobytes.

    Returns:
        float: The equivalent value in megabytes.
    """
    return convert_bytes(kilobytes, "kilobytes", "megabytes")


def convert_megabyte_to_gigabyte(megabytes: int) -> int:
    """
    Converts a value from megabytes to gigabytes.

    Args:
        megabytes (int): The value in megabytes.

    Returns:
        float: The equivalent value in gigabytes.
    """
    return convert_bytes(megabytes, "megabytes", "gigabytes")
