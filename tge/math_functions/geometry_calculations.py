from math import sqrt

from .math_functions import get_pi

from numbers import Number


def volume_of_cuboid(
    length: Number, width: Number, height: Number
) -> Number:
    """Calculate the volume of a cuboid.

    Args:
        length (Number): The length of the cuboid.
        width (Number): The width of the cuboid.
        height (Number): The height of the cuboid.

    Returns:
        Number: The volume of the cuboid."""
    return length * width * height


def volume_of_cube(side: Number) -> Number:
    """Calculate the volume of a cube.

    Args:
        side (Number): The length of each side of the cube.

    Returns:
        Number: The volume of the cube."""
    return side**3


def volume_of_sphere(radius: Number) -> Number:
    """Calculate the volume of a sphere using an approximation for π (pi).

    Args:
        radius (Number): The radius of the sphere.

    Returns:
        Number: The volume of the sphere using π ≈ 3.14159.
    """
    return (4 / 3) * 3.14159 * (radius**3)


def volume_of_sphere_with_accuracy(radius: Number, accuracy: Number) -> float:
    """Calculate the volume of a sphere with a specified accuracy for π (pi).

    Args:
        radius (float): The radius of the sphere.
        accuracy (Number): The level of accuracy for π.

    Returns:
        float: The volume of the sphere using the provided π accuracy.
    """
    return (4 / 3) * get_pi(accuracy) * (radius**3)


def volume_of_cylinder(radius: Number, height: Number) -> Number:
    """Calculate the volume of a cylinder using an approximation for π (pi).

    Args:
        radius (Number): The radius of the base of the cylinder.
        height (Number): The height of the cylinder.

    Returns:
        Number: The volume of the cylinder using π ≈ 3.14159.
    """
    return 3.14159 * (radius**2) * height


def volume_of_cylinder_with_accuracy(
    radius: Number, height: Number, accuracy: Number
) -> float:
    """Calculate the volume of a cylinder with a specified accuracy for π (pi).

    Args:
        radius (float): The radius of the base of the cylinder.
        height (float): The height of the cylinder.
        accuracy (Number): The level of accuracy for π.

    Returns:
        float: The volume of the cylinder using the provided π accuracy.
    """
    return get_pi(accuracy) * (radius**2) * height


def area_of_square(side: Number) -> Number:
    """Calculate the area of a square.

    Args:
        side (Number): The length of one side of the square.

    Returns:
        Number: The area of the square."""
    return side**2


def area_of_rectangle(length: Number, width: Number) -> Number:
    """Calculate the area of a rectangle.

    Args:
        length (Number): The length of the rectangle.
        width (Number): The width of the rectangle.

    Returns:
        Number: The area of the rectangle."""
    return length * width


def area_of_circle(radius: Number) -> Number:
    """Calculate the area of a circle using an approximation for π (pi).

    Args:
        radius (Number): The radius of the circle.

    Returns:
        Number: The area of the circle using π ≈ 3.14159.
    """
    return 3.14159 * (radius**2)


def area_of_circle_with_accuracy(radius: Number, accuracy: Number) -> float:
    """Calculate the area of a circle with a specified accuracy for π (pi).

    Args:
        radius (float): The radius of the circle.
        accuracy (Number): The level of accuracy for π.

    Returns:
        float: The area of the circle using the provided π accuracy.
    """
    return get_pi(accuracy) * (radius**2)


def area_of_trapezoid(
    base_length: Number, base_width: Number, height: Number
) -> Number:
    """Calculate the area of a trapezoid.

    Args:
        base_length (Number): The length of one base of the trapezoid.
        base_width (Number): The length of the other base of the trapezoid.
        height (Number): The height of the trapezoid.

    Returns:
        Number: The area of the trapezoid.
    """
    return ((base_length + base_width) * height) / 2


def volume_of_pyramid(
    base_length: Number, base_width: Number, height: Number
) -> Number:
    """Calculate the volume of a pyramid.

    Args:
        base_length (Number): The length of the base of the pyramid.
        base_width (Number): The width of the base of the pyramid.
        height (Number): The height of the pyramid.

    Returns:
        Number: The volume of the pyramid."""
    return (base_length * base_width * height) / 3


def linear_regression_slope(
    x1: Number, y1: Number, x2: Number, y2: Number
) -> float:
    """Calculate the slope of the line through two points.

    Args:
        x1 (Number): The x-coordinate of the first point.
        y1 (Number): The y-coordinate of the first point.
        x2 (Number): The x-coordinate of the second point.
        y2 (Number): The y-coordinate of the second point.

    Returns:
        float: The slope of the line through the two points."""
    return (y2 - y1) / (x2 - x1)


def surface_area_of_cylinder(radius: Number, height: Number) -> Number:
    """Calculate the surface area of a cone (not a cylinder) using an approximation for π (pi).

    Args:
        radius (Number): The radius of the base of the cone.
        height (Number): The height of the cone.

    Returns:
        Number: The surface area of the cone using π ≈ 3.14159.
    """
    slant_height = sqrt(radius**2 + height**2)

    surface_area = 3.14159 * radius * slant_height

    return surface_area


def surface_area_of_cylinder_with_accuracy(
    radius: Number, height: Number, accuracy: Number
) -> Number:
    """Calculate the surface area of a cone (not a cylinder) with a specified accuracy for π (pi).

    Args:
        radius (Number): The radius of the base of the cone.
        height (Number): The height of the cone.
        accuracy (Number): The level of accuracy for π.

    Returns:
        Number: The surface area of the cone using the provided π accuracy."""
    slant_height = sqrt(radius**2 + height**2)

    surface_area = get_pi(accuracy) * radius * slant_height

    return surface_area


def surface_area_of_sphere(radius: Number) -> Number:
    """Calculate the surface area of a sphere using an approximation for π (pi).

    Args:
        radius (Number): The radius of the sphere.

    Returns:
        Number: The surface area of the sphere using π ≈ 3.14159.
    """
    surface_area = 4 * 3.14159 * (radius**2)

    return surface_area


def surface_area_of_sphere_with_accuracy(
    radius: Number, accuracy: Number
) -> Number:
    """Calculate the surface area of a sphere with a specified accuracy for π (pi).

    Args:
        radius (Number): The radius of the sphere.
        accuracy (Number): The level of accuracy for π.

    Returns:
        Number: The surface area of the sphere using the provided π accuracy."""
    surface_area = get_pi(accuracy) * (radius**2)

    return surface_area


def surface_area_of_cube(side_length: Number) -> Number:
    """Calculate the surface area of a cube.

    Args:
        side_length (Number): The length of one side of the cube.

    Returns:
        Number: The surface area of the cube.
    """
    return 6 * (side_length**2)


def surface_area_of_rectangle(length: Number, width: Number) -> Number:
    """Calculate the surface area of a rectangle.

    Args:
        length (Number): The length of the rectangle.
        width (Number): The width of the rectangle.

    Returns:
        Number: The surface area of the rectangle.
    """
    return length * width


def surface_area_of_cuboid(
    length: Number, width: Number, height: Number
) -> Number:
    """Calculate the surface area of a cuboid.

    Args:
        length (Number): The length of the cuboid.
        width (Number): The width of the cuboid.
        height (Number): The height of the cuboid.

    Returns:
        Number: The surface area of the cuboid."""
    return 2 * (length * width + width * height + height * length)


def volume_of_cone(radius: Number, height: Number) -> Number:
    """Calculate the volume of a cone using an approximation for π (pi).

    Args:
        radius (Number): The radius of the base of the cone.
        height (Number): The height of the cone.

    Returns:
        Number: The volume of the cone using π ≈ 3.14159."""
    return (1 / 3) * 3.14159 * (radius**2) * height


def volume_of_cone_with_accuracy(
    radius: Number, height: Number, accuracy: Number
) -> Number:
    """
    Calculate the volume of a cone using a specified precision for π (pi).

    Args:
        radius (Number): The radius of the base of the cone.
        height (Number): The height of the cone.
        accuracy (Number): Precision level for π.

    Returns:
        Number: The volume of the cone calculated with the given π accuracy."""
    return (1 / 3) * get_pi(accuracy) * (radius**2) * height


def surface_area_of_cone(radius: Number, height: Number) -> Number:
    """Calculate the surface area of a cone using an approximation for π (pi).

    Args:
        radius (Number): The radius of the base of the cone.
        height (Number): The height of the cone.

    Returns:
        Number: The surface area of the cone, using π ≈ 3.14159.
    """
    base_area = 3.14159 * radius**2
    side_area = 3.14159 * radius * sqrt(radius**2 + height**2)
    surface_area = base_area + side_area
    return surface_area


def surface_area_of_cone_with_accuracy(
    radius: Number, height: Number, accuracy: Number
) -> Number:
    """Calculate the surface area of a cone with a specified precision for π (pi).

    Args:
        radius (Number): The radius of the base of the cone.
        height (Number): The height of the cone.
        accuracy (Number): Precision level for π.

    Returns:
        Number: The surface area of the cone calculated with the given π accuracy.
    """
    base_area = get_pi(accuracy) * radius**2
    side_area = get_pi(accuracy) * radius * sqrt(radius**2 + height**2)
    surface_area = base_area + side_area
    return surface_area


def area_of_ellipse(radius: Number, height: Number) -> Number:
    """Calculate the area of an ellipse using an approximation for π (pi).

    Args:
        radius (Number): The semi-major axis of the ellipse.
        height (Number): The semi-minor axis of the ellipse.

    Returns:
        Number: The area of the ellipse using π ≈ 3.14159.
    """
    return 3.14159 * radius * height


def area_of_ellipse_with_accuracy(
    radius: Number, height: Number, accuracy: Number
) -> Number:
    """Calculate the area of an ellipse with a specified accuracy for π (pi).

    Args:
        radius (Number): The semi-major axis of the ellipse.
        height (Number): The semi-minor axis of the ellipse.
        accuracy (Number): The level of accuracy for π.

    Returns:
        Number: The area of the ellipse using the provided π accuracy."""
    return get_pi(accuracy) * radius * height


def area_of_oval(width: int, height: int) -> int:
    """Calculate the area of an oval approximated as a combination of a rectangle and a triangle.

    Args:
        width (int): The width of the oval.
        height (int): The height of the oval.

    Returns:
        int: The approximated area of the oval."""
    rectangle_area = width * height
    triangle_area = (width - height) * height / 2
    area = rectangle_area + triangle_area
    return area


def area_of_triangle(base: Number, height: Number) -> float:
    """Calculate the area of a triangle.

    Args:
        base (Number): The base length of the triangle.
        height (Number): The height of the triangle.

    Returns:
        Number: The area of the triangle."""
    return 0.5 * base * height


def calculate_distance_between_two_points(
    x: Number, y: Number
) -> Number:
    """
    Calculate the distance between two points using the Euclidean formula.

    :param x: An integer representing the x-coordinate of the first point.
    :param y: An integer representing the y-coordinate of the second point.
    :return: An integer representing the distance between the two points.
    """
    return ((x - y) ** 2) ** 0.5


def calculate_distance_between_three_points(
    x: Number, y: Number, z: Number
) -> Number:
    """
    Calculate the distance between three points in a 3D space.

    :param x: An integer representing the x-coordinate of the first point.
    :param y: An integer representing the y-coordinate of the second point.
    :param z: An integer representing the z-coordinate of the third point.

    :return: An integer representing the distance between the three points.
    """
    return ((x - z) ** 2 + (y - z) ** 2) ** 0.5


def calculate_distance_between_four_points(
    x: Number, y: Number, z: Number, a: Number
) -> Number:
    """
    Calculates the distance between four points represented by their x, y, and z coordinates.

    :param x: An integer representing the first point.
    :param y: An integer representing the second point.
    :param z: An integer representing the third point.
    :param a: An integer representing the fourth point.

    :return: A float representing the distance between the four points.
    """
    return ((x - a) ** 2 + (y - a) ** 2 + (z - a) ** 2) ** 0.5


from collections.abc import Iterable


def calculate_distance_between_points(*points: Iterable) -> int:
    """Calculate the total distance between a sequence of points in 2D space.

    Args:
        *points (Iterable): A variable number of tuples representing points (x, y) in 2D space.

    Returns:
        int: The total distance between the points. Returns 0 if fewer than two points are provided.
    """
    if len(points) < 2:
        return 0.0  

    total_distance = 0.0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total_distance += distance

    return total_distance


def vector_magnitude(vector: Iterable) -> float:
    """Calculate the magnitude of a 2D vector.

    Args:
        vector (Iterable): A tuple or list representing the vector (x, y).

    Returns:
        float: The magnitude of the vector.
    """
    return sqrt(vector[0] ** 2 + vector[1] ** 2)


def hamming_distance(string1: str, string2: str) -> Number:
    """Calculate the Hamming distance between two strings.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        Number: The Hamming distance, which is the number of positions at which the characters differ. Returns an integer.
    """
    return sum(ch1 != ch2 for ch1, ch2 in zip(string1, string2))
