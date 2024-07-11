def convertFloat(input_string):
	'\n    Checks if the given string can be converted to a float.\n    ';A=input_string
	try:A=float(A);return A
	except ValueError:return 0
def convertInt(input_string):
	'\n    Checks if the given string can be converted to an integer.\n    ';A=input_string
	try:A=int(A);return A
	except ValueError:return 0
def compareType(*B):
	'\n    Check if any of the objects share a common ancestor class in their class hierarchy.\n    '
	def C(cls):
		'\n        Get the class hierarchy of a class, including all base classes.\n        ';A=cls;B=set();C=[A]
		while C:A=C.pop(0);B.add(A);C.extend(A for A in A.__bases__ if A not in B and A is not object)
		return tuple(B)
	A=[C(A.__class__)for A in B];D={B for B in A[0]if all(B in A for A in A[1:])};return len(D)>0