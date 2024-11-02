#type: ignore
def decode(data):
 C={};B=None;D=data.split('\n')
 for A in D:
  A=A.strip()
  if A.startswith('#'):B=A[1:].strip();C[B]=[]
  elif A:
   if B is not None:C[B].append(A)
   else:raise ValueError('Data format error: Item found before list name.')
 return C
def encode(data):
 A=''
 for(B,C)in data.items():
  A+=f"#{B}\n"
  for D in C:A+=f"{D}\n"
  A+='\n'
 return A
__all__=['decode','encode']