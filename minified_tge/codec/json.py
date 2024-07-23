import json,json5,hjson
def json5_to_json(string):return json.dumps(json5.loads(string))
def json_to_json5(string):return json5.dumps(json.loads(string))
def hjson_to_json(string):return json.dumps(hjson.loads(string))
def json_to_hjson(string):return hjson.dumps(json.loads(string))
def hjson_to_json5(string):return json5.dumps(hjson.loads(string))
def json5_to_hjson(string):return hjson.dumps(json5.loads(string))