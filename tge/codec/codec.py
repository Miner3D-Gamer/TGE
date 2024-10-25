from binascii import hexlify, unhexlify



from . import msy # type: ignore
from . import morse # type: ignore
from . import html # type: ignore
from . import standard_galactic_alphabet # type: ignore
from . import json # type: ignore










def base_x_decode_from_binary(binary_data:bytes, base:int) -> str:
    decimal_value = int.from_bytes(binary_data, byteorder='big')

    if base < 2 or base > 95:
        raise ValueError("Base must be between 2 and 95 included")

    digits = r"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
    result = ""

    while decimal_value > 0:
        result = digits[decimal_value % base] + result
        decimal_value //= base

    return result or "0"

def base_x_encode_to_binary(data_in_base_x:str, base:int) -> bytes:
    if base < 2 or base > 95:
        raise ValueError("Base must be between 2 and 95 included")

    digits = r"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
    digit_map = {char: index for index, char in enumerate(digits)}

    decimal_value = 0
    for char in data_in_base_x:
        if char not in digit_map:
            raise ValueError(f"Invalid character {char} for base {base}")
        decimal_value = decimal_value * base + digit_map[char]

    binary_data = decimal_value.to_bytes((decimal_value.bit_length() + 7) // 8, byteorder='big')

    return binary_data







def encode(x: str) -> str:
    """
    Encode a string using base64 and hexadecimal encoding.

    Args:
        x (str): The string to be encoded.

    Returns:
        Tuple[bool, Union[str, bytes]]: A tuple containing a boolean value indicating whether
            the encoding was successful or not, and either the encoded string or an error message
            if the encoding failed.
    """
    y = base_x_encode_to_binary(x, 95)
    x = hexlify(y).decode("utf8")
    return x


def decode(data: str) -> str:
    """
    Decodes a string from hexadecimal and base64 encoding.

    Args:
        data (str): A string to decode.

    Returns:
        A tuple containing a boolean indicating whether the decoding was successful and
        the decoded string if successful, or an error message if unsuccessful.
    """
    new_data = unhexlify(data)
    decoded_data = base_x_decode_from_binary(new_data, 95)
    return decoded_data














