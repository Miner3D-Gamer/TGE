def chop(string,substring,rem=True):
	B=string;A=substring
	if rem:
		if B.startswith(A)and B.endswith(A):return B[len(A):-len(A)]
		else:return B
	else:return lchop(rchop(B,A),A)
def truncate_string(string,length):
	'\n    Truncates a string to the specified length.\n\n    Args:\n        string (str): The string to be truncated.\n        length (int): The maximum length of the truncated string.\n\n    Returns:\n        str: The truncated string.\n    ';B=length;A=string
	if len(A)<=B:return A
	else:return A[:B]
def reverse_string(string):'\n    Reverses the order of characters in a string.\n\n    Args:\n        string (str): The string to be reversed.\n\n    Returns:\n        str: The reversed string.\n    ';return string[::-1]
def check_anagram(word1,word2):'\n    Check if two words are anagrams of each other.\n\n    Args:\n        word1 (str): The first word to check.\n        word2 (str): The second word to check.\n\n    Returns:\n        bool: True if the words are anagrams, False otherwise.\n    ';return sorted(word1)==sorted(word2)
def remove_duplicate_characters_from_string(string):
	'\n    Remove duplicate characters from a given string.\n\n    Args:\n        string (str): The input string.\n\n    Returns:\n        str: The string with duplicate characters removed.\n\n    Examples:\n        >>> remove_duplicates_from_string("hello")\n        \'helo\'\n        >>> remove_duplicates_from_string("abbcccdd")\n        \'abcd\'\n    ';A=''
	for B in string:
		if B not in A:A+=B
	return A
def find_longest_word(string):'\n    Find the longest word in a given string.\n\n    Args:\n        string (str): The input string.\n\n    Returns:\n        str: The longest word found in the string.\n\n    Examples:\n        >>> find_longest_word("Hello world")\n        \'Hello\'\n        >>> find_longest_word("This is a sentence")\n        \'sentence\'\n    ';return max(string.split(),key=len)
def get_length_of_longest_substring_without_repeating_characters(s):
	'\n    Find the length of the longest substring without repeating characters.\n\n    Args:\n        s (str): The input string.\n\n    Returns:\n        int: The length of the longest substring without repeating characters.\n\n    Examples:\n        >>> get_length_of_longest_substring("abcabcbb")\n        3\n        >>> get_length_of_longest_substring("bbbbb")\n        1\n        >>> get_length_of_longest_substring("pwwkew")\n        3\n    '
	if not s:return 0
	C=0;D=0;B={}
	for A in range(len(s)):
		if s[A]in B and D<=B[s[A]]:D=B[s[A]]+1
		else:C=max(C,A-D+1)
		B[s[A]]=A
	return C
def find_first_non_repeating_character(string):
	'\n    Find the first non-repeating character in a given string.\n\n    Args:\n        string (str): The input string.\n\n    Returns:\n        str: The first non-repeating character found in the string, or None if no such character is found.\n    ';C=string;B={}
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
def left_pad(string,length,char=' '):'\n    Pads the given string on the left with the specified character to the desired length.\n    \n    Parameters:\n    string (str): The original string.\n    length (int): The desired length after padding.\n    char (str): The character to pad with (default is a space).\n    \n    Returns:\n    str: The left-padded string.\n    ';return string.rjust(length,char)
def right_pad(string,length,char=' '):'\n    Pads the given string on the right with the specified character to the desired length.\n    \n    Parameters:\n    string (str): The original string.\n    length (int): The desired length after padding.\n    char (str): The character to pad with (default is a space).\n    \n    Returns:\n    str: The right-padded string.\n    ';return string.ljust(length,char)