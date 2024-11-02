#type: ignore
__all__=['convertFloat','convertInt','compareType']
def convertFloat(input_string):
 A=input_string
 try:A=float(A);return A
 except ValueError:return 0
def convertInt(input_string):
 A=input_string
 try:A=int(A);return A
 except ValueError:return 0
def compareType(*B):
 def C(cls):
  A=cls;B=set();C=[A]
  while C:A=C.pop(0);B.add(A);C.extend(A for A in A.__bases__ if A not in B and A is not object)
  return tuple(B)
 A=[C(A.__class__)for A in B];D={B for B in A[0]if all(B in A for A in A[1:])};return len(D)>0