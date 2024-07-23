def remove_duplicates_from_dictionary(dictionary):
	B=dictionary;C=set(B.values());D={}
	for(E,A)in B.items():
		if A in C:D[E]=A;C.remove(A)
	return D
from typing import Any
def find_index(dictionary,key,value):
	A=dictionary
	for B in A:
		if A[B][key]==value:return B