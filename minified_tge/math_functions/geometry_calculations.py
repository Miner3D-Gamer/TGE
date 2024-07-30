from math import sqrt
from.math_functions import get_pi
def volume_of_cuboid(length,width,height):return length*width*height
def volume_of_cube(side):return side**3
def volume_of_sphere(radius):return 4/3*3.14159*radius**3
def volume_of_sphere_with_accuracy(radius,accuracy):return 4/3*get_pi(accuracy)*radius**3
def volume_of_cylinder(radius,height):return 3.14159*radius**2*height
def volume_of_cylinder_with_accuracy(radius,height,accuracy):return get_pi(accuracy)*radius**2*height
def area_of_square(side):return side**2
def area_of_rectangle(length,width):return length*width
def area_of_circle(radius):return 3.14159*radius**2
def area_of_circle_with_accuracy(radius,accuracy):return get_pi(accuracy)*radius**2
def area_of_trapezoid(base_length,base_width,height):return(base_length+base_width)*height/2
def volume_of_pyramid(base_length,base_width,height):return base_length*base_width*height/3
def linear_regression_slope(x1,y1,x2,y2):return(y2-y1)/(x2-x1)
def surface_area_of_cylinder(radius,height):A=radius;B=sqrt(A**2+height**2);C=3.14159*A*B;return C
def surface_area_of_cylinder_with_accuracy(radius,height,accuracy):A=radius;B=sqrt(A**2+height**2);C=get_pi(accuracy)*A*B;return C
def surface_area_of_sphere(radius):A=4*3.14159*radius**2;return A
def surface_area_of_sphere_with_accuracy(radius,accuracy):A=get_pi(accuracy)*radius**2;return A
def surface_area_of_cube(side_length):return 6*side_length**2
def surface_area_of_rectangle(length,width):return length*width
def surface_area_of_cuboid(length,width,height):C=height;B=width;A=length;return 2*(A*B+B*C+C*A)
def volume_of_cone(radius,height):return 1/3*3.14159*radius**2*height
def volume_of_cone_with_accuracy(radius,height,accuracy):return 1/3*get_pi(accuracy)*radius**2*height
def surface_area_of_cone(radius,height):A=radius;B=3.14159*A**2;C=3.14159*A*sqrt(A**2+height**2);D=B+C;return D
def surface_area_of_cone_with_accuracy(radius,height,accuracy):B=accuracy;A=radius;C=get_pi(B)*A**2;D=get_pi(B)*A*sqrt(A**2+height**2);E=C+D;return E
def area_of_ellipse(radius,height):return 3.14159*radius*height
def area_of_ellipse_with_accuracy(radius,height,accuracy):return get_pi(accuracy)*radius*height
def area_of_oval(width,height):B=width;A=height;C=B*A;D=(B-A)*A/2;E=C+D;return E
def area_of_triangle(base,height):return .5*base*height
def calculate_distance_between_two_points(x,y):return((x-y)**2)**.5
def calculate_distance_between_three_points(x,y,z):return((x-z)**2+(y-z)**2)**.5
def calculate_distance_between_four_points(x,y,z,a):return((x-a)**2+(y-a)**2+(z-a)**2)**.5
def calculate_distance_between_points(*A):
 if len(A)<2:return .0
 B=.0
 for C in range(len(A)-1):D,E=A[C];F,G=A[C+1];H=sqrt((F-D)**2+(G-E)**2);B+=H
 return B
def vector_magnitude(vector):A=vector;return sqrt(A[0]**2+A[1]**2)
def hamming_distance(string1,string2):return sum(A!=B for(A,B)in zip(string1,string2))