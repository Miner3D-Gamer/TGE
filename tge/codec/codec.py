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

def encode(x: str) -> "Tuple[bool, str]":
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
        x = base.encode_base64(bytes(x, "latin-1"))
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
        decoded_data = base.decode_base64(data)
        return decoded_data.decode("latin-1"), True
    except BinasciiError as e:
        return f"Error decoding string (BinasciiError): {e}", False
    except UnicodeError as e:
        return f"Error decoding string (UnicodeError): {e}", False
    except Exception as e:
        return f"Unknown error decoding string (UnknownError): {e}", False














