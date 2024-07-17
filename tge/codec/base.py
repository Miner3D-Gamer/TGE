from base64 import b64encode as e64, b64decode as d64
def encode_base64(string: str) -> str:
    """
    Encodes a given string in base64 format.

    Args:
        string (str): The string to be encoded.

    Returns:
        str: The encoded string in base64 format.
    """
    return e64(string.encode()).decode()


def decode_base64(string: str) -> str:
    """
    This function decodes a given string in base64 format and returns the decoded string.

    Args:
        string (str): A string in base64 format to be decoded.

    Returns:
        str: The decoded string.
    """
    return d64(string.encode()).decode()