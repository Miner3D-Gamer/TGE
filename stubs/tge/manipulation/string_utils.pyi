__all__=['scramble_word','chop','truncate_string','reverse_string','check_anagram','remove_duplicate_characters_from_string','find_longest_word','get_length_of_longest_substring_without_repeating_characters','find_first_non_repeating_character','count_consonants','count_substring_occurrences','count_vowels','find_longest_substring','check_pangram','find_common_characters','split_text','lchop','rchop','left_pad','right_pad','left_replace','right_replace','replace_with_list_as_replacement','replace_with_list_as_replacer','replace_list_with_list','replace']
def scramble_word(word:str)->str:...
def chop(string:str,substring:str,rem:bool=True)->str:...
def truncate_string(string:str,length:int)->str:...
def reverse_string(string:str)->str:...
def check_anagram(word1:str,word2:str)->bool:...
def remove_duplicate_characters_from_string(string:str)->str:...
def find_longest_word(string:str)->str:...
def get_length_of_longest_substring_without_repeating_characters(s:str)->int:...
def find_first_non_repeating_character(string:str)->str|None:...
def count_consonants(string:str)->int:...
def count_substring_occurrences(string:str,substring:str)->int:...
def count_vowels(string:str)->int:...
def find_longest_substring(string:str)->str:...
def check_pangram(string:str)->bool:...
def find_common_characters(string1:str,string2:str)->str:...
def split_text(text:str,chunk_size:int)->list[str]:...
def lchop(string:str,substring:str)->str:...
def rchop(string:str,substring:str)->str:...
def left_pad(string:str,length:int,char:str=' ')->str:...
def right_pad(string:str,length:int,char:str=' ')->str:...
def left_replace(s:str,chars:list[str]|str,replacement:str)->str:...
def right_replace(s:str,chars:list[str],replacement:str)->str:...
def replace_with_list_as_replacement(string:str,replacer:str,replacements:list[str])->str:...
def replace_with_list_as_replacer(string:str,replacers:list[str],replacement:str)->str:...
def replace_list_with_list(string:str,replacers:list[str],replacements:list[str])->str:...
def replace(string:str,replacers:str|list[str],replacements:str|list[str])->str:...