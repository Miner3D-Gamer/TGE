def remove_duplicates_from_dictionary(dictionary):
	'\n    Remove duplicates from a dictionary based on its values.\n\n    Parameters:\n    dictionary (dict): A dictionary to remove duplicates from based on values.\n\n    Returns:\n    dict: A new dictionary with unique values, where only the first occurrence\n          of each value is retained, preserving the original key-value pairs.\n    ';B=dictionary;C=set(B.values());D={}
	for(E,A)in B.items():
		if A in C:D[E]=A;C.remove(A)
	return D
from typing import Any
def find_index(dictionary,key,value):
	A=dictionary
	for B in A:
		if A[B][key]==value:return B