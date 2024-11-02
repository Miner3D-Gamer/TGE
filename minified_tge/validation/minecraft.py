#type: ignore
import re
_A=False
__all__=['is_valid_function_name','is_valid_registry_name','is_number_range','is_valid_scoreboard_name']
def is_valid_function_name(name):
 A=name
 if A.startswith('/')or A.endswith('/'):return _A
 if'//'in A:return _A
 if not re.match('^[a-z0-9_/]+$',A):return _A
 return True
def is_valid_registry_name(input_str):
 A='^\\w+:\\w+$'
 if re.match(A,input_str):return True
 else:return _A
def is_number_range(s):
 A='^\\d+\\.\\.\\d+$'
 if re.fullmatch(A,s):B,C=s.split('..');return B.isdigit()and C.isdigit()
 return _A
def is_valid_scoreboard_name(name):
 if re.match('^[a-zA-Z_][a-zA-Z0-9_]*$',name):return True
 else:return _A