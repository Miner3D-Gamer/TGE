_A='Input must be a string'
import random,re
class ExpandedString(str):
 def __new__(A,value):B=super(ExpandedString,A).__new__(A,value);return B
 def __init__(A,value):super().__init__()
 def get_scrambled(A):
  if not isinstance(A,str):raise ValueError(_A)
  B=list(A);random.shuffle(B);return''.join(B)
 def scramble(A):
  if not isinstance(A,str):raise ValueError(_A)
  B=list(A);random.shuffle(B);A=ExpandedString(''.join(B))
 def chop(A,substring):
  B=substring
  if A.startswith(B)and A.endswith(B):A=ExpandedString(A[len(B):-len(B)])
 def get_chopped(A,substring):
  B=substring
  if A.startswith(B)and A.endswith(B):return A[len(B):-len(B)]
  else:return A
 def get_truncated(A,length):
  B=length
  if len(A)<=B:return A
  else:return A[:B]
 def truncate(A,length):
  B=length
  if not len(A)<=B:A=ExpandedString(A[:B])
 def reverse(A):A=ExpandedString(A[::-1])
 def get_reversed(A):return A[::-1]
 def check_anagram(A,word2):return sorted(A)==sorted(word2)
 def remove_duplicate_characters(B):
  A=''
  for C in B:
   if C not in A:A+=C
  B=ExpandedString(A)
 def get_string_after_removing_duplicate_characters(C):
  A=''
  for B in C:
   if B not in A:A+=B
  return A
 def find_longest_word(A):return max(A.split(),key=len)
 def get_length_of_longest_substring_without_repeating_characters(A):
  if not A:return 0
  D=0;E=0;C={}
  for B in range(len(A)):
   if A[B]in C and E<=C[A[B]]:E=C[A[B]]+1
   else:D=max(D,B-E+1)
   C[A[B]]=B
  return D
 def find_first_non_repeating_character(C):
  B={}
  for A in C:B[A]=B.get(A,0)+1
  for A in C:
   if B[A]==1:return A
 def count_consonants(B):
  C='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';A=0
  for D in B:
   if D in C:A+=1
  return A
 def count_substring_occurrences(A,substring):return A.count(substring)
 def count_vowels(B):
  A=0
  for C in B:
   if C in'aeiouäöü':A+=1
  return A
 def find_longest_substring(D):
  B='';A=''
  for C in D:
   if C in A:
    if len(A)>len(B):B=A
    A=A.split(C)[-1]
   A+=C
  if len(A)>len(B):B=A
  return B
 def check_pangram(A):B=set(A.lower());C=''.join(filter(lambda c:c in B,A.lower()));return set(C)==B
 def find_common_characters(A,string2):return''.join(set(A)&set(string2))
 def get_chunks(A,chunk_size):B=chunk_size;return[A[C:C+B]for C in range(0,len(A),B)]
 def lchop(A,substring):
  B=substring
  if A.startswith(B):A=ExpandedString(A[len(B):])
 def get_lchop(A,substring):
  B=substring
  if A.startswith(B):return A[len(B):]
  else:return A
 def rchop(A,substring):
  B=substring
  if A.endswith(B):A=ExpandedString(A[:-len(B)])
 def get_rchop(A,substring):
  B=substring
  if A.endswith(B):return A[:-len(B)]
  else:return A
 def left_pad(A,length,char=' '):A=ExpandedString(A.rjust(length,char))
 def get_left_pad(A,length,char=' '):return A.rjust(length,char)
 def right_pad(A,length,char=' '):A=ExpandedString(A.ljust(length,char))
 def get_right_pad(A,length,char=' '):return A.ljust(length,char)
 def left_replace(B,chars,replacement):
  A=0
  while A<len(B)and B[A]in chars:A+=1
  C=replacement*A;D=B[A:];B=ExpandedString(C+D)
 def get_left_replace(B,chars,replacement):
  A=0
  while A<len(B)and B[A]in chars:A+=1
  C=replacement*A;D=B[A:];return C+D
 def get_right_replace(B,chars,replacement):
  A=len(B)-1
  while A>=0 and B[A]in chars:A-=1
  C=replacement*(len(B)-A-1);D=B[:A+1];return D+C
 def right_replace(A,chars,replacement):
  B=len(A)-1
  while B>=0 and A[B]in chars:B-=1
  C=replacement*(len(A)-B-1);D=A[:B+1];A=ExpandedString(D+C);return A
 def remove_html_tags(A):A=ExpandedString(re.sub('<.*?>','',A));return A
 def get_with_html_tags_removed(A):return re.sub('<.*?>','',A)
 def replace_with_list_as_replacement(A,replacer,replacements):
  for B in replacements:A=ExpandedString(A.replace(replacer,B))
 def replace_with_list_as_replacer(A,replacers,replacement):
  for B in replacers:A=ExpandedString(A.replace(B,replacement))
 def get_replace_with_list_as_replacement(B,replacer,replacements):
  A=B
  for C in replacements:A=ExpandedString(A.replace(replacer,C))
  return A
 def get_replace_with_list_as_replacer(A,replacers,replacement):
  for B in replacers:A=ExpandedString(A.replace(B,replacement))
  return A