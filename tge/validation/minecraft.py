import re
__all__ = ['is_valid_function_name', 'is_valid_registry_name', 'is_number_range', 'is_valid_scoreboard_name']
def is_valid_function_name(name: str) -> bool:
    """
    Checks if a given name is a valid function name based on the following criteria:
    - Does not start or end with a slash ("/").
    - Does not contain double slashes ("//").
    - Only contains lowercase letters, digits, underscores, and slashes.
    """
    if name.startswith("/") or name.endswith("/"):
        return False

    if "//" in name:
        return False

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
    pattern = r"^\w+:\w+$"

    if re.match(pattern, input_str):
        return True
    else:
        return False





def is_number_range(s: str) -> bool:
    """
    Validates if a string represents a number range in the format 'start..end',
    where both 'start' and 'end' are non-negative integers.
    """
    pattern = r"^\d+\.\.\d+$"

    if re.fullmatch(pattern, s):
        start, end = s.split("..")
        return start.isdigit() and end.isdigit()
    return False


def is_valid_scoreboard_name(name: str) -> bool:
    """
    Determines if a given name is a valid scoreboard name consisting of:
    - Starts with a letter or underscore.
    - Contains only letters, digits, and underscores.
    """
    if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):
        return True
    else:
        return False
