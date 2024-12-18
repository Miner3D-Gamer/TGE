import json
import json5
import hjson
import re
from typing import Dict, Any, List


def json5_to_json(string: str) -> str:
    """Convert JSON5 to JSON."""
    return json.dumps(json5.loads(string))


def json_to_json5(string: str) -> str:
    """Convert JSON to JSON5."""
    return json5.dumps(json.loads(string))


def hjson_to_json(string: str) -> str:
    """Convert HJSON to JSON."""
    return json.dumps(hjson.loads(string))


def json_to_hjson(string: str) -> str:
    """Convert JSON to HJSON."""
    return hjson.dumps(json.loads(string))


def hjson_to_json5(string: str) -> str:
    """Convert HJSON to JSON5."""
    return json5.dumps(hjson.loads(string))


def json5_to_hjson(string: str)->str:
    """Convert JSON5 to HJSON."""
    return hjson.dumps(json5.loads(string))


def loose_decode_json(json_str: str) -> Dict[str, Any]:
    """Fast Decode JSON with loose rules."""

    def parse_value(s: str) -> Any:
        """Parse a value from a string."""
        s = s.strip()
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1]
        elif s == "true":
            return True
        elif s == "false":
            return False
        elif s == "null":
            return None
        elif re.match(r"^-?\d+(\.\d+)?$", s):
            return int(s) if "." not in s else float(s)
        elif s.startswith("["):
            return parse_array(s)
        elif s.startswith("{"):
            return parse_object(s)
        else:
            raise ValueError(f"Unexpected value: {s}")

    def parse_array(s: str) -> Any:
        """Parse an array from a string."""
        s = s[1:-1].strip()
        if not s:
            return []
        elements = split_by_comma(s)
        return [parse_value(elem) for elem in elements]

    def parse_object(s: str) -> Dict[str, Any]:
        """Parse an object from a string."""
        s = s[1:-1].strip()
        if not s:
            return {}
        items = split_by_comma(s)
        obj: Dict[str, Any] = {}
        for item in items:
            key, value = item.split(":", 1)
            key = parse_value(key.strip())
            value = parse_value(value.strip())
            obj[key] = value
        return obj

    def split_by_comma(s: str) -> Any:
        """Split a string by comma."""
        result: List[str] = []
        depth_list = 0
        depth_dict = 0
        last_index = 0
        inside_string = False
        escape = False

        def is_opening_bracket(char: str) -> bool:
            """
            Check if a character is an opening bracket.
            """
            return char in "[{"

        def is_closing_bracket(char_: str) -> bool:
            """
            Check if a character is a closing bracket.
            """
            return char in "]}"

        # def matches_opening_closing(opening: str, closing: str)->bool:
        #     return (opening == '[' and closing == ']') or (opening == '{' and closing == '}')

        for i, char in enumerate(s):
            if char == '"':
                if not escape:
                    inside_string = not inside_string
                escape = False
            elif char == "\\":
                escape = not escape
            else:
                if not inside_string:
                    if is_opening_bracket(char):
                        if char == "[":
                            depth_list += 1
                        elif char == "{":
                            depth_dict += 1
                    elif is_closing_bracket(char):
                        if char == "]":
                            if depth_list == 0:
                                raise ValueError("Unexpected closing bracket ']'")
                            depth_list -= 1
                        elif char == "}":
                            if depth_dict == 0:
                                raise ValueError("Unexpected closing bracket '}'")
                            depth_dict -= 1
                    elif char == "," and depth_list == 0 and depth_dict == 0:
                        result.append(s[last_index:i].strip())
                        last_index = i + 1

            if i == len(s) - 1:
                result.append(s[last_index:].strip())

        if depth_list != 0:
            raise ValueError("Unmatched opening bracket '['")
        if depth_dict != 0:
            raise ValueError("Unmatched opening bracket '{'")

        return result

    json_str = json_str.strip()
    return parse_value(json_str)


def is_valid_json(json_str: str) -> bool:
    """Check if a string is valid JSON."""
    valid = True

    def parse_value(s: str) -> Any:
        """Parse a value from a string."""
        nonlocal valid
        s = s.strip()
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1]
        elif s == "true":
            return True
        elif s == "false":
            return False
        elif s == "null":
            return None
        elif re.match(r"^-?\d+(\.\d+)?$", s):
            return int(s) if "." not in s else float(s)
        elif s.startswith("["):
            return parse_array(s)
        elif s.startswith("{"):
            return parse_object(s)
        else:
            valid = False

    def parse_array(s: str) -> Any:
        """Parse an array from a string."""
        s = s[1:-1].strip()
        if not s:
            return []
        elements = split_by_comma(s)
        return [parse_value(elem) for elem in elements]

    def parse_object(s: str) -> Any:
        """Parse an object from a string."""
        s = s[1:-1].strip()
        if not s:
            return {}
        items = split_by_comma(s)
        obj: Dict[str, Any] = {}
        for item in items:
            key, value = item.split(":", 1)
            key = parse_value(key.strip())
            value = parse_value(value.strip())
            obj[key] = value
        return obj

    def split_by_comma(s: str):
        """Split a string by comma."""
        nonlocal valid
        result: List[str] = []
        depth_list = 0
        depth_dict = 0
        last_index = 0
        inside_string = False
        escape = False

        def is_opening_bracket(char: str) -> bool:
            """
            Check if a character is an opening bracket.
            """
            return char in "[{"

        def is_closing_bracket(char: str) -> bool:
            """
            Check if a character is a closing bracket.
            """
            return char in "]}"

        # def matches_opening_closing(opening, closing):
        #     return (opening == '[' and closing == ']') or (opening == '{' and closing == '}')

        for i, char in enumerate(s):
            if char == '"':
                if not escape:
                    inside_string = not inside_string
                escape = False
            elif char == "\\":
                escape = not escape
            else:
                if not inside_string:
                    if is_opening_bracket(char):
                        if char == "[":
                            depth_list += 1
                        elif char == "{":
                            depth_dict += 1
                    elif is_closing_bracket(char):
                        if char == "]":
                            if depth_list == 0:
                                valid = False
                            depth_list -= 1
                        elif char == "}":
                            if depth_dict == 0:
                                valid = False
                            depth_dict -= 1
                    elif char == "," and depth_list == 0 and depth_dict == 0:
                        result.append(s[last_index:i].strip())
                        last_index = i + 1

            if i == len(s) - 1:
                result.append(s[last_index:].strip())

        if depth_list != 0:
            valid = False
        if depth_dict != 0:
            valid = False

        return result

    json_str = json_str.strip()
    parse_value(json_str)
    return valid


__all__ = [
    "json5_to_json",
    "json_to_json5",
    "hjson_to_json",
    "json_to_hjson",
    "hjson_to_json5",
    "json5_to_hjson",
    "loose_decode_json",
    "is_valid_json",
]
