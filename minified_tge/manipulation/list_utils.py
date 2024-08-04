from itertools import permutations as itertools_permutations
def list_mul(lst):
 A=1
 for B in lst:
  if isinstance(B,(int,float)):A=A*B
 return A
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
 A=len(lst)
 if A==0:return 0
 B=sum(lst);C=B/A;return C
def find_common_elements(lst1,lst2):
 A=[]
 for B in lst1:
  if B in lst2:A.append(B)
 return A
def median(lst):
 A=sorted(lst);B=len(A)
 if B%2==0:return(A[B//2-1]+A[B//2])/2
 else:return A[B//2]
def reverse_list(lst):return lst[::-1]
def find_max_min_difference(lst):return max(lst)-min(lst)
def find_missing_number(lst):return sum(range(1,len(lst)+1))-sum(lst)
def remove_whitespace_from_list(lst):return[A.replace(' ','')for A in lst]
def exponential_average(lst):return sum(lst)/len(lst)
def greatest_product(lst,lst2):return max(lst)*max(lst2)
def permutations(lst):return list(itertools_permutations(lst))
def limit_list(lst,limit):return lst[:limit]
def get_items_from_list(lst,start,end):return lst[start:end]
def sort_list_of_dictionaries(lst,key):
 try:return sorted(lst,key=lambda x:x[key]),True
 except:return lst,False
def zipper_insert(list1,list2):
 C=list2;B=list1;D=min(len(B),len(C));A=[]
 for E in range(D):A.append(B[E]);A.append(C[E])
 A.extend(B[D:]);A.extend(C[D:]);return A