from itertools import permutations as itertools_permutations
def list_max(lst):'Find and return the maximum value in a list.\n\n    Args:\n        lst (list): A list of integers.\n\n    Returns:\n        int: The highest value in the list.\n\n    Example:\n        >>> list_max([3, 1, 7, 4])\n        7\n    ';A=sorted(lst);return A[-1]
def list_min(lst):'\n    Returns the minimum value in a list of numbers.\n\n    Args:\n    - lst: a list of numbers\n\n    Returns:\n    - the lowest value in the list\n\n    Example:\n    >>> list_min([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7])\n    1\n    ';A=sorted(lst);return A[0]
def list_sum(lst):
	A=0
	for B in lst:
		if isinstance(B,(int,float)):A+=B
	return A
def list_mul(lst):
	'\n    Multiply all the numbers in the given list and return the result along with a success message.\n\n    :param lst: A list of numbers to multiply.\n    :type lst: list\n    :return: A tuple containing the product of the numbers in the list and a success message.\n    :rtype: tuple\n    :raises TypeError: If the list contains non-numeric values.\n    ';A=1
	try:
		for B in lst:
			if isinstance(B,(int,float)):A=A*B
		return A
	except TypeError:return 0
def remove_duplicates(list):
	'\n    Removes duplicates from a given list and returns it.\n\n    :param list: A list of items.\n    :type list: list\n    :return: A new list containing no duplicates.\n    :rtype: list\n    ';A=[]
	for B in list:
		if B not in A:A.append(B)
	return A
def count_occurrences(list,item):
	'\n    Counts the number of occurrences of a given item in a list.\n\n    :param list: The list to search for occurrences.\n    :type list: list\n    :param item: The item to count occurrences of.\n    :type item: str\n    :return: The number of occurrences of the given item in the list.\n    :rtype: int\n    ';A=0
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
def remove_whitespace_from_list(lst):'\n    Removes whitespace characters from all elements in a list of strings.\n    \n    Args:\n        lst (list): List of strings\n        \n    Returns:\n        list: List with whitespace removed from all elements\n    ';return[A.replace(' ','')for A in lst]
def exponential_average(lst):return sum(lst)/len(lst)
def greatest_product(lst,lst2):return list_max(lst)*list_max(lst2)
def permutations(lst):return list(itertools_permutations(lst))
def limit_list(list,limit):return list[:limit]
def get_items_from_list(list,start,end):return list[start:end]
def sort_list_of_dictionaries(lst,key):
	try:return sorted(lst,key=lambda x:x[key]),True
	except:return lst,False