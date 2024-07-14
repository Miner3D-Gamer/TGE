import random
def scramble_word(word):
	if not isinstance(word,str):raise ValueError('Input must be a string')
	A=list(word);random.shuffle(A);return''.join(A)
def chop(string,substring,rem=True):
	B=string;A=substring
	if rem:
		if B.startswith(A)and B.endswith(A):return B[len(A):-len(A)]
		else:return B
	else:return lchop(rchop(B,A),A)
def truncate_string(string,length):
	B=length;A=string
	if len(A)<=B:return A
	else:return A[:B]
def reverse_string(string):return string[::-1]
def check_anagram(word1,word2):return sorted(word1)==sorted(word2)
def remove_duplicate_characters_from_string(string):
	A=''
	for B in string:
		if B not in A:A+=B
	return A
def find_longest_word(string):return max(string.split(),key=len)
def get_length_of_longest_substring_without_repeating_characters(s):
	if not s:return 0
	C=0;D=0;B={}
	for A in range(len(s)):
		if s[A]in B and D<=B[s[A]]:D=B[s[A]]+1
		else:C=max(C,A-D+1)
		B[s[A]]=A
	return C
def find_first_non_repeating_character(string):
	C=string;B={}
	for A in C:B[A]=B.get(A,0)+1
	for A in C:
		if B[A]==1:return A
def count_consonants(string):
	B='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';A=0
	for C in string:
		if C in B:A+=1
	return A
def count_substring_occurrences(string,substring):return string.count(substring)
def capitalize_sentences(paragraph):A=paragraph.split('. ');B=[A.capitalize()for A in A];C='. '.join(B);return C
def count_vowels(string):
	A=0
	for B in string:
		if B in'aeiouäöü':A+=1
	return A
def find_longest_substring(string):
	B='';A=''
	for C in string:
		if C in A:
			if len(A)>len(B):B=A
			A=A.split(C)[-1]
		A+=C
	if len(A)>len(B):B=A
	return B
def check_pangram(string):A=string;B=set(A.ascii_lowercase);C=''.join(filter(lambda c:c in B,A.lower()));return set(C)==B
def find_common_characters(string1,string2):return''.join(set(string1)&set(string2))
def split_text(text,chunk_size):A=chunk_size;return[text[B:B+A]for B in range(0,len(text),A)]
def lchop(string,substring):
	B=substring;A=string
	if A.startswith(B):return A[len(B):]
	else:return A
def rchop(string,substring):
	B=substring;A=string
	if A.endswith(B):return A[:-len(B)]
	else:return A
def left_pad(string,length,char=' '):return string.rjust(length,char)
def right_pad(string,length,char=' '):return string.ljust(length,char)
def left_replace(s,chars,replacement):
	A=0
	while A<len(s)and s[A]in chars:A+=1
	B=replacement*A;C=s[A:];return B+C
def replace_rstrip(s,chars,replacement):
	A=len(s)-1
	while A>=0 and s[A]in chars:A-=1
	B=replacement*(len(s)-A-1);C=s[:A+1];return C+B