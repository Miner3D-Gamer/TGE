_B='^-?\\d+(\\.\\d+)?$'
_A=False
import json,json5,hjson,re
def json5_to_json(string):return json.dumps(json5.loads(string))
def json_to_json5(string):return json5.dumps(json.loads(string))
def hjson_to_json(string):return json.dumps(hjson.loads(string))
def json_to_hjson(string):return hjson.dumps(json.loads(string))
def hjson_to_json5(string):return json5.dumps(hjson.loads(string))
def json5_to_hjson(string):return hjson.dumps(json5.loads(string))
def loose_decode_json(json_str):
 B=json_str
 def A(s):
  s=s.strip()
  if s.startswith('"')and s.endswith('"'):return s[1:-1]
  elif s=='true':return True
  elif s=='false':return _A
  elif s=='null':return
  elif re.match(_B,s):return int(s)if'.'not in s else float(s)
  elif s.startswith('['):return C(s)
  elif s.startswith('{'):return E(s)
  else:raise ValueError(f"Unexpected value: {s}")
 def C(s):
  s=s[1:-1].strip()
  if not s:return[]
  B=D(s);return[A(B)for B in B]
 def E(s):
  s=s[1:-1].strip()
  if not s:return{}
  F=D(s);E={}
  for G in F:B,C=G.split(':',1);B=A(B.strip());C=A(C.strip());E[B]=C
  return E
 def D(s):
  E=[];B=0;C=0;F=0;G=_A;D=_A
  def I(char):return char in'[{'
  def J(char_):return A in']}'
  for(H,A)in enumerate(s):
   if A=='"':
    if not D:G=not G
    D=_A
   elif A=='\\':D=not D
   elif not G:
    if I(A):
     if A=='[':B+=1
     elif A=='{':C+=1
    elif J(A):
     if A==']':
      if B==0:raise ValueError("Unexpected closing bracket ']'")
      B-=1
     elif A=='}':
      if C==0:raise ValueError("Unexpected closing bracket '}'")
      C-=1
    elif A==','and B==0 and C==0:E.append(s[F:H].strip());F=H+1
   if H==len(s)-1:E.append(s[F:].strip())
  if B!=0:raise ValueError("Unmatched opening bracket '['")
  if C!=0:raise ValueError("Unmatched opening bracket '{'")
  return E
 B=B.strip();return A(B)
def is_valid_json(json_str):
 C=json_str;B=True
 def A(s):
  nonlocal B;s=s.strip()
  if s.startswith('"')and s.endswith('"'):return s[1:-1]
  elif s=='true':return True
  elif s=='false':return _A
  elif s=='null':return
  elif re.match(_B,s):return int(s)if'.'not in s else float(s)
  elif s.startswith('['):return E(s)
  elif s.startswith('{'):return F(s)
  else:B=_A
 def E(s):
  s=s[1:-1].strip()
  if not s:return[]
  B=D(s);return[A(B)for B in B]
 def F(s):
  s=s[1:-1].strip()
  if not s:return{}
  F=D(s);E={}
  for G in F:B,C=G.split(':',1);B=A(B.strip());C=A(C.strip());E[B]=C
  return E
 def D(s):
  nonlocal B;F=[];C=0;D=0;G=0;H=_A;E=_A
  def J(char):return char in'[{'
  def K(char):return char in']}'
  for(I,A)in enumerate(s):
   if A=='"':
    if not E:H=not H
    E=_A
   elif A=='\\':E=not E
   elif not H:
    if J(A):
     if A=='[':C+=1
     elif A=='{':D+=1
    elif K(A):
     if A==']':
      if C==0:B=_A
      C-=1
     elif A=='}':
      if D==0:B=_A
      D-=1
    elif A==','and C==0 and D==0:F.append(s[G:I].strip());G=I+1
   if I==len(s)-1:F.append(s[G:].strip())
  if C!=0:B=_A
  if D!=0:B=_A
  return F
 C=C.strip();A(C);return B