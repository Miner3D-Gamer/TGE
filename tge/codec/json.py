import json
import json5
import hjson
import re


def json5_to_json(string: str):
    return json.dumps(json5.loads(string))


def json_to_json5(string: str):
    return json5.dumps(json.loads(string))



def hjson_to_json(string: str):
    return json.dumps(hjson.loads(string))


def json_to_hjson(string: str):
    return hjson.dumps(json.loads(string))



def hjson_to_json5(string: str):
    return json5.dumps(hjson.loads(string))


def json5_to_hjson(string: str):
    return hjson.dumps(json5.loads(string))



def loose_decode_json(json_str):
    def parse_value(s):
        s = s.strip()
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1]
        elif s == 'true':
            return True
        elif s == 'false':
            return False
        elif s == 'null':
            return None
        elif re.match(r'^-?\d+(\.\d+)?$', s):
            return int(s) if '.' not in s else float(s)
        elif s.startswith('['):
            return parse_array(s)
        elif s.startswith('{'):
            return parse_object(s)
        else:
            raise ValueError(f"Unexpected value: {s}")

    def parse_array(s):
        s = s[1:-1].strip()
        if not s:
            return []
        elements = split_by_comma(s)
        return [parse_value(elem) for elem in elements]

    def parse_object(s):
        s = s[1:-1].strip()
        if not s:
            return {}
        items = split_by_comma(s)
        obj = {}
        for item in items:
            key, value = item.split(':', 1)
            key = parse_value(key.strip())
            value = parse_value(value.strip())
            obj[key] = value
        return obj

    def split_by_comma(s):
        result = []
        depth_list = 0
        depth_dict = 0
        last_index = 0
        inside_string = False
        escape = False

        def is_opening_bracket(char):
            return char in '[{'

        def is_closing_bracket(char):
            return char in ']}'

        def matches_opening_closing(opening, closing):
            return (opening == '[' and closing == ']') or (opening == '{' and closing == '}')

        for i, char in enumerate(s):
            if char == '"':
                if not escape:
                    inside_string = not inside_string
                escape = False
            elif char == '\\':
                escape = not escape
            else:
                if not inside_string:
                    if is_opening_bracket(char):
                        if char == '[':
                            depth_list += 1
                        elif char == '{':
                            depth_dict += 1
                    elif is_closing_bracket(char):
                        if char == ']':
                            if depth_list == 0:
                                raise ValueError("Unexpected closing bracket ']'")
                            depth_list -= 1
                        elif char == '}':
                            if depth_dict == 0:
                                raise ValueError("Unexpected closing bracket '}'")
                            depth_dict -= 1
                    elif char == ',' and depth_list == 0 and depth_dict == 0:
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




def is_valid_json(json_str):
    valid = True
    def parse_value(s):
        nonlocal valid
        s = s.strip()
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1]
        elif s == 'true':
            return True
        elif s == 'false':
            return False
        elif s == 'null':
            return None
        elif re.match(r'^-?\d+(\.\d+)?$', s):
            return int(s) if '.' not in s else float(s)
        elif s.startswith('['):
            return parse_array(s)
        elif s.startswith('{'):
            return parse_object(s)
        else:
            valid = False

    def parse_array(s):
        s = s[1:-1].strip()
        if not s:
            return []
        elements = split_by_comma(s)
        return [parse_value(elem) for elem in elements]

    def parse_object(s):
        s = s[1:-1].strip()
        if not s:
            return {}
        items = split_by_comma(s)
        obj = {}
        for item in items:
            key, value = item.split(':', 1)
            key = parse_value(key.strip())
            value = parse_value(value.strip())
            obj[key] = value
        return obj

    def split_by_comma(s):
        nonlocal valid
        result = []
        depth_list = 0
        depth_dict = 0
        last_index = 0
        inside_string = False
        escape = False

        def is_opening_bracket(char):
            return char in '[{'

        def is_closing_bracket(char):
            return char in ']}'

        def matches_opening_closing(opening, closing):
            return (opening == '[' and closing == ']') or (opening == '{' and closing == '}')

        for i, char in enumerate(s):
            if char == '"':
                if not escape:
                    inside_string = not inside_string
                escape = False
            elif char == '\\':
                escape = not escape
            else:
                if not inside_string:
                    if is_opening_bracket(char):
                        if char == '[':
                            depth_list += 1
                        elif char == '{':
                            depth_dict += 1
                    elif is_closing_bracket(char):
                        if char == ']':
                            if depth_list == 0:
                                valid = False
                            depth_list -= 1
                        elif char == '}':
                            if depth_dict == 0:
                                valid = False
                            depth_dict -= 1
                    elif char == ',' and depth_list == 0 and depth_dict == 0:
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
    return  valid
