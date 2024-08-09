from binascii import hexlify,unhexlify,Error as BinasciiError
from.import msy
from.import base
from.import morse
from.import html
from.import standard_galactic_alphabet
from.import json
html,json
def encode(x):x=base.encode_base64(x);x=hexlify(x.encode()).decode('utf8');return x
def decode(data):A=data;A=unhexlify(A);B=base.decode_base64(A);return B