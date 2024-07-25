import re


def is_valid_function_name(name: str) -> bool:
    # Check if name starts or ends with a slash
    if name.startswith("/") or name.endswith("/"):
        return False

    # Check if name contains consecutive slashes
    if "//" in name:
        return False

    # Check if name contains invalid characters
    if not re.match(r"^[a-z0-9_/]+$", name):
        return False

    return True


def is_valid_registry_name(input_str: str) -> bool:
    """
    Checks if the input string is a valid Minecraft registry name in the format "{str}:{str}".

    Args:
    input_str (str): The input string to be checked.

    Returns:
    bool: True if the input string is a valid Minecraft registry name, False otherwise.
    """
    # Regular expression pattern to match "{str}:{str}"
    pattern = r"^\w+:\w+$"

    # Check if the input string matches the pattern
    if re.match(pattern, input_str):
        return True
    else:
        return False


def is_number_range(s: str) -> bool:
    # Define the regex pattern for the range "{whole number}..{whole number}"
    pattern = r"^\d+\.\.\d+$"

    # Use the fullmatch method to check if the entire string matches the pattern
    if re.fullmatch(pattern, s):
        # Split the string by '..' and check if both parts are whole numbers
        start, end = s.split("..")
        return start.isdigit() and end.isdigit()
    return False


def is_valid_scoreboard_name(name: str) -> bool:
    if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):
        return True
    else:
        return False
