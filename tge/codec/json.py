import json
import json5
import hjson


# JSON and JSON5
def json5_to_json(string: str):
    return json.dumps(json5.loads(string))


def json_to_json5(string: str):
    return json5.dumps(json.loads(string))


# JSON and HJSON
def hjson_to_json(string: str):
    return json.dumps(hjson.loads(string))


def json_to_hjson(string: str):
    return hjson.dumps(json.loads(string))


# JSON5 and HJSON
def hjson_to_json5(string: str):
    return json5.dumps(hjson.loads(string))


def json5_to_hjson(string: str):
    return hjson.dumps(json5.loads(string))
