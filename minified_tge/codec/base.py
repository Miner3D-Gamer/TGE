from base64 import b64encode as e64,b64decode as d64
def encode_base64(string):return e64(string.encode()).decode()
def decode_base64(string):return d64(string.encode()).decode()