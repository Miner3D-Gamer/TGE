import math

class Vector:
    """
    A class representing a mathematical vector.

    Parameters:
    *components (float): Variable number of components for the vector.

    Attributes:
    components (List[float]): Iterable containing the components of the vector.

    Methods:
    __init__(*components) -> None: Initializes a vector with the given components.
    __repr__() -> str: Returns a string representation of the vector.
    __len__() -> int: Returns the number of components in the vector.
    __getitem__(index: int) -> float: Returns the component at the specified index.
    __eq__(other: 'Vector') -> bool: Checks if two vectors are equal.
    __add__(other: 'Vector') -> 'Vector': Adds two vectors element-wise.
    __sub__(other: 'Vector') -> 'Vector': Subtracts two vectors element-wise.
    dot(other: 'Vector') -> float: Calculates the dot product of two vectors.
    magnitude() -> float: Calculates the magnitude (length) of the vector.
    normalize() -> 'Vector': Returns a normalized (unit) vector.
    """
    def __init__(self, *components: float) -> None:
        """Initialize an object with a list of float components.

Args:
    *components (float): Variable number of float arguments to initialize the `components` list."""
        self.components = list(components)

    def __repr__(self) -> str:
        """
        Returns a string representation of the vector.

        Returns:
        str: String representation of the vector.
        """
        return f"Vector{tuple(self.components)}"

    def __len__(self) -> int:
        """
        Returns the number of components in the vector.

        Returns:
        int: Number of components in the vector.
        """
        return len(self.components)

    def __getitem__(self, index: int) -> float:
        """
        Returns the component at the specified index.

        Parameters:
        index (int): Index of the component to retrieve.

        Returns:
        float: The component at the specified index.
        """
        return self.components[index]

    def __eq__(self, other: 'Vector') -> bool:
        """
        Checks if two vectors are equal.

        Parameters:
        other (Vector): Another vector for comparison.

        Returns:
        bool: True if the vectors are equal, False otherwise.
        """
        return self.components == other.components

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Adds two vectors element-wise.

        Parameters:
        other (Vector): Another vector for addition.

        Returns:
        Vector: Resultant vector after addition.
        """
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for addition.")
        result_components = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*result_components)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Subtracts two vectors element-wise.

        Parameters:
        other (Vector): Another vector for subtraction.

        Returns:
        Vector: Resultant vector after subtraction.
        """
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for subtraction.")
        result_components = [a - b for a, b in zip(self.components, other.components)]
        return Vector(*result_components)

    def dot(self, other: 'Vector') -> float:
        """
        Calculates the dot product of two vectors.

        Parameters:
        other (Vector): Another vector for the dot product.

        Returns:
        float: Dot product of the two vectors.
        """
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self) -> float:
        """
        Calculates the magnitude (length) of the vector.

        Returns:
        float: Magnitude of the vector.
        """
        return math.sqrt(sum(component**2 for component in self.components))

    def normalize(self) -> 'Vector':
        """
        Returns a normalized (unit) vector.

        Returns:
        Vector: Normalized (unit) vector.
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[component / mag for component in self.components])
    
