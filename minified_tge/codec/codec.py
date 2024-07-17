_A='latin-1'
from binascii import hexlify,unhexlify,Error as BinasciiError
from typing import List,Union,Tuple,Any
from.import msy
from.import base
from.import morse
from.import html
from.import standard_galactic_alphabet
def encode(x):
	try:x=base.b64encode(bytes(x,_A));x=hexlify(x).decode(_A);return x
	except:return''
def decode(data):
	C=False;B=data
	try:B=unhexlify(B);D=base.b64decode(B);return D.decode(_A),True
	except BinasciiError as A:return f"Error decoding string (BinasciiError): {A}",C
	except UnicodeError as A:return f"Error decoding string (UnicodeError): {A}",C
	except Exception as A:return f"Unknown error decoding string (UnknownError): {A}",C