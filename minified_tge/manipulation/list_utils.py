from itertools import permutations as itertools_permutations
def list_max(lst):A=sorted(lst);return A[-1]
def list_min(lst):A=sorted(lst);return A[0]
def list_sum(lst):
	A=0
	for B in lst:
		if isinstance(B,(int,float)):A+=B
	return A
def list_mul(lst):
	A=1
	try:
		for B in lst:
			if isinstance(B,(int,float)):A=A*B
		return A
	except TypeError:return 0
def remove_duplicates(list):
	A=[]
	for B in list:
		if B not in A:A.append(B)
	return A
def count_occurrences(list,item):
	A=0
	for B in list:
		if B==item:A+=1
	return A
def calculate_average(lst):
	B=list_sum(lst);A=len([A for A in lst if isinstance(A,(int,float))])
	if A==0:return 0
	C=B/A;return C
def find_common_elements(lst1,lst2):
	A=[]
	for B in lst1:
		if B in lst2:A.append(B)
	return A
def median(lst):
	A=lst;A.sort()
	if len(A)%2==0:return(A[len(A)//2-1]+A[len(A)//2])/2
	else:return A[len(A)//2]
def reverse_list(lst):return lst[::-1]
def find_max_min_difference(lst):return max(lst)-min(lst)
def find_missing_number(lst):return sum(range(1,len(lst)+1))-sum(lst)
def remove_whitespace_from_list(lst):return[A.replace(' ','')for A in lst]
def exponential_average(lst):return sum(lst)/len(lst)
def greatest_product(lst,lst2):return list_max(lst)*list_max(lst2)
def permutations(lst):return list(itertools_permutations(lst))
def limit_list(list,limit):return list[:limit]
def get_items_from_list(list,start,end):return list[start:end]
def sort_list_of_dictionaries(lst,key):
	try:return sorted(lst,key=lambda x:x[key]),True
	except:return lst,False