import math
class Vector:
	"\n    A class representing a mathematical vector.\n\n    Parameters:\n    *components (float): Variable number of components for the vector.\n\n    Attributes:\n    components (List[float]): List containing the components of the vector.\n\n    Methods:\n    __init__(*components) -> None: Initializes a vector with the given components.\n    __repr__() -> str: Returns a string representation of the vector.\n    __len__() -> int: Returns the number of components in the vector.\n    __getitem__(index: int) -> float: Returns the component at the specified index.\n    __eq__(other: 'Vector') -> bool: Checks if two vectors are equal.\n    __add__(other: 'Vector') -> 'Vector': Adds two vectors element-wise.\n    __sub__(other: 'Vector') -> 'Vector': Subtracts two vectors element-wise.\n    dot(other: 'Vector') -> float: Calculates the dot product of two vectors.\n    magnitude() -> float: Calculates the magnitude (length) of the vector.\n    normalize() -> 'Vector': Returns a normalized (unit) vector.\n    "
	def __init__(A,*B):A.components=list(B)
	def __repr__(A):'\n        Returns a string representation of the vector.\n\n        Returns:\n        str: String representation of the vector.\n        ';return f"Vector{tuple(A.components)}"
	def __len__(A):'\n        Returns the number of components in the vector.\n\n        Returns:\n        int: Number of components in the vector.\n        ';return len(A.components)
	def __getitem__(A,index):'\n        Returns the component at the specified index.\n\n        Parameters:\n        index (int): Index of the component to retrieve.\n\n        Returns:\n        float: The component at the specified index.\n        ';return A.components[index]
	def __eq__(A,other):'\n        Checks if two vectors are equal.\n\n        Parameters:\n        other (Vector): Another vector for comparison.\n\n        Returns:\n        bool: True if the vectors are equal, False otherwise.\n        ';return A.components==other.components
	def __add__(A,other):
		'\n        Adds two vectors element-wise.\n\n        Parameters:\n        other (Vector): Another vector for addition.\n\n        Returns:\n        Vector: Resultant vector after addition.\n        ';B=other
		if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for addition.')
		C=[A+B for(A,B)in zip(A.components,B.components)];return Vector(*C)
	def __sub__(A,other):
		'\n        Subtracts two vectors element-wise.\n\n        Parameters:\n        other (Vector): Another vector for subtraction.\n\n        Returns:\n        Vector: Resultant vector after subtraction.\n        ';B=other
		if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for subtraction.')
		C=[A-B for(A,B)in zip(A.components,B.components)];return Vector(*C)
	def dot(A,other):
		'\n        Calculates the dot product of two vectors.\n\n        Parameters:\n        other (Vector): Another vector for the dot product.\n\n        Returns:\n        float: Dot product of the two vectors.\n        ';B=other
		if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for dot product.')
		return sum(A*B for(A,B)in zip(A.components,B.components))
	def magnitude(A):'\n        Calculates the magnitude (length) of the vector.\n\n        Returns:\n        float: Magnitude of the vector.\n        ';return math.sqrt(sum(A**2 for A in A.components))
	def normalize(A):
		'\n        Returns a normalized (unit) vector.\n\n        Returns:\n        Vector: Normalized (unit) vector.\n        ';B=A.magnitude()
		if B==0:raise ValueError('Cannot normalize a zero vector.')
		return Vector(*[A/B for A in A.components])