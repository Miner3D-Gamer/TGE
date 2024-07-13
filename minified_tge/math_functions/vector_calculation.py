import math
class Vector:
	def __init__(A,*B):A.components=list(B)
	def __repr__(A):return f"Vector{tuple(A.components)}"
	def __len__(A):return len(A.components)
	def __getitem__(A,index):return A.components[index]
	def __eq__(A,other):return A.components==other.components
	def __add__(A,other):
		B=other
		if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for addition.')
		C=[A+B for(A,B)in zip(A.components,B.components)];return Vector(*C)
	def __sub__(A,other):
		B=other
		if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for subtraction.')
		C=[A-B for(A,B)in zip(A.components,B.components)];return Vector(*C)
	def dot(A,other):
		B=other
		if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for dot product.')
		return sum(A*B for(A,B)in zip(A.components,B.components))
	def magnitude(A):return math.sqrt(sum(A**2 for A in A.components))
	def normalize(A):
		B=A.magnitude()
		if B==0:raise ValueError('Cannot normalize a zero vector.')
		return Vector(*[A/B for A in A.components])