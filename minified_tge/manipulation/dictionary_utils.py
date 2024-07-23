def remove_duplicates_from_dictionary(dictionary):
	B=dictionary;C=set(B.values());D={}
	for(E,A)in B.items():
		if A in C:D[E]=A;C.remove(A)
	return D