from binascii import hexlify, unhexlify, Error as BinasciiError
from typing import List, Union, Tuple, Any



from . import msy
from . import base
from . import morse
from . import html
from . import standard_galactic_alphabet
from . import json

# To make sure the imports stay when minifying
html, json

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
    x = base.encode_base64(x)
    x = hexlify(x.encode()).decode("utf8")
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
    data = unhexlify(data)
    decoded_data = base.decode_base64(data)
    return decoded_data














