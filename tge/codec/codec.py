from binascii import hexlify, unhexlify, Error as BinasciiError
from typing import List, Union, Tuple, Any



from . import msy
from . import base
from . import morse
from . import html
from . import standard_galactic_alphabet


def encode(x: str) -> Tuple[bool, str]:
    """
    Encode a string using base64 and hexadecimal encoding.

    Args:
        x (str): The string to be encoded.

    Returns:
        Tuple[bool, Union[str, bytes]]: A tuple containing a boolean value indicating whether
            the encoding was successful or not, and either the encoded string or an error message
            if the encoding failed.
    """
    try:
        x = base.b64encode(bytes(x, "latin-1"))
        x = hexlify(x).decode("latin-1")
        return x
    except:
        return ""


def decode(data: str) -> Tuple[str, bool]:
    """
    Decodes a string from hexadecimal and base64 encoding.

    Args:
        data (str): A string to decode.

    Returns:
        A tuple containing a boolean indicating whether the decoding was successful and
        the decoded string if successful, or an error message if unsuccessful.
    """
    try:
        data = unhexlify(data)
        decoded_data = base.b64decode(data)
        return decoded_data.decode("latin-1"), True
    except BinasciiError as e:
        return f"Error decoding string (BinasciiError): {e}", False
    except UnicodeError as e:
        return f"Error decoding string (UnicodeError): {e}", False
    except Exception as e:
        return f"Unknown error decoding string (UnknownError): {e}", False











# def decimal_to_binary(n: int) -> int: Inefficient!
#     """
#     Convert a decimal integer to its binary representation.

#     Parameters:
#     n (int): The decimal integer to be converted.

#     Returns:
#     str: The binary representation of the decimal integer 'n'.

#     Examples:
#     >>> decimal_to_binary(10)
#     '1010'
#     >>> decimal_to_binary(-5)
#     '1011'
#     >>> decimal_to_binary(0)
#     '0'
#     """

#     if n < 0:
#         n = abs(n)
#     elif n == 0:
#         return "0"
#     else:
#         binary_str = ""
#         while n > 0:
#             remainder = n % 2
#             binary_str = str(remainder) + binary_str
#             n = n // 2
#         return binary_str

# def binary_to_decimal(binary_str: int | str) -> int: Inefficient!
#     """
#     Convert a binary string or integer to its decimal representation.

#     Parameters:
#     binary_str (int | str): The binary string or integer to be converted to decimal.

#     Returns:
#     int: The decimal representation of the input binary string or integer.
#     """
#     decimal_num = 0
#     binary_str = str(binary_str[::-1])  # Reverse the binary string for easier processing

#     for i in range(len(binary_str)):
#         if binary_str[i] == '1':
#             decimal_num += 2 ** i

#     return decimal_num
