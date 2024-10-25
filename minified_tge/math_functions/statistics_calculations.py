from math import sqrt,log2
import numpy as np
def average_grade(grades):A=grades;return sum(A)/len(A)
def median_grade(grades):A=grades;return sorted(A)[len(A)//2]
def mode_grade(grades):A=grades;return max(set(A),key=A.count)
def standard_deviation(grades):A=grades;return sqrt(sum([(B-average_grade(A))**2 for B in A])/len(A))
def median(grades):A=grades;return sorted(A)[len(A)//2]
def median_absolute_deviation(data):A=median(data);B=[abs(B-A)for B in data];C=median(B);return C
def correlation(data1,data2):return np.corrcoef(data1,data2)[0][1]
def calculate_entropy(grades):return sum(A*log2(A)for A in grades)
def median_absolute_error(grades):A=grades;return median([abs(B-median_grade(A))for B in A])