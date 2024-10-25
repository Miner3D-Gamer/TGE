from typing import Any, List
import math
def list_mul(lst):return math.prod(lst)
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
def greatest_product(lst,lst2):return max(lst)*max(lst2)
def zipper_insert(list1,list2):
 C=list2;B=list1;D=min(len(B),len(C));A=[]
 for E in range(D):A.append(B[E]);A.append(C[E])
 A.extend(B[D:]);A.extend(C[D:]);return A
def compress_list(list_to_compress):
 B=list_to_compress;G=len(B);A=[];C=B[0];D=0
 def E(amount,char):
  A=amount
  if A>1 and A!=G:return[A,char]
  else:return[char]
 for H in range(len(B)):
  F=B[H]
  if F==C:D+=1
  else:A+=E(D,C);C=F;D=1
 else:A+=E(D,C)
 if len(A)==1:A=A[0]
 return A
def compress_list_of_lists(list_to_compress):
 A=[]
 for B in list_to_compress:A.append(compress_list(B))
 return A
def decompress_list(list_to_decompress,width):
 B=list_to_decompress
 if not isinstance(B,list):return[B]*width
 D=[];C=1
 for A in B:
  A:0
  if isinstance(A,int):C=A
  else:D+=C*[A];C=1
 return D
def decompress_list_of_lists(list_to_decompress,width):
 A=[]
 for B in list_to_decompress:A.append(decompress_list(B,width))
 return A
class MaxSizeList(List[Any]):
 def __init__(A,max_size):super().__init__();A.max_size=max_size
 def append(A,item):
  super().append(item)
  if len(A)>A.max_size:A.pop(0)
 def extend(A,iterable):
  super().extend(iterable)
  while len(A)>A.max_size:A.pop(0)