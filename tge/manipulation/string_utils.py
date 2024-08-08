import random
from typing import Iterable, Union, List


def scramble_word(word:str)->str:
    """
    Scramble the letters of a given word.

    Parameters:
    word (str): The word to scramble.

    Returns:
    str: The scrambled word.
    """
    if not isinstance(word, str):
        raise ValueError("Input must be a string")

    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)


def chop(string: str, substring: str, rem: bool = True) -> str:
    """
    Remove a specified substring from the beginning and end of a string if it is present on both sides.

    Args:
        string (str): The input string to process.
        substring (str): The substring to remove from both the start and end of the string.
        rem (bool): If True, the substring will be removed from both ends if present. If False, no removal is performed.

    Returns:
        str: The modified string with the substring removed from both ends if it was present.
    """
    if rem and string.startswith(substring) and string.endswith(substring):
        return string[len(substring): -len(substring)]
    else:
        return string



def truncate_string(string: str, length: int) -> str:
    """
    Truncates a string to the specified length.

    Args:
        string (str): The string to be truncated.
        length (int): The maximum length of the truncated string.

    Returns:
        str: The truncated string.
    """
    if len(string) <= length:
        return string
    else:
        return string[:length]


def reverse_string(string: str) -> str:
    """
    Reverses the order of characters in a string.

    Args:
        string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return string[::-1]


def check_anagram(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.

    Args:
        word1 (str): The first word to check.
        word2 (str): The second word to check.

    Returns:
        bool: True if the words are anagrams, False otherwise.
    """
    return sorted(word1) == sorted(word2)


def remove_duplicate_characters_from_string(string: str) -> str:
    """
    Remove duplicate characters from a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The string with duplicate characters removed.
    """
    result = ""
    for char in string:
        if char not in result:
            result += char
    return result


def find_longest_word(string: str) -> str:
    """
    Find the longest word in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The longest word found in the string.
    """
    return max(string.split(), key=len)


def get_length_of_longest_substring_without_repeating_characters(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """
    if not s:
        return 0

    max_length = 0  # stores the length of the longest substring
    start = 0  # starting index of the current substring
    char_index_map = {}  # stores the most recent index of each character

    for i in range(len(s)):
        if s[i] in char_index_map and start <= char_index_map[s[i]]:
            # If the current character is already present in the substring,
            # update the starting index of the substring to the next index of the repeated character.
            start = char_index_map[s[i]] + 1
        else:
            # Calculate the length of the current substring and update the maximum length if necessary.
            max_length = max(max_length, i - start + 1)

        # Update the most recent index of the current character.
        char_index_map[s[i]] = i

    return max_length


def find_first_non_repeating_character(string: str) -> str:
    """
    Find the first non-repeating character in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The first non-repeating character found in the string, or None if no such character is found.
    """
    char_count = {}

    # Count the occurrences of each character in the string
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for char in string:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found, return None
    return None


def count_consonants(string: str) -> int:
    """
    Count the number of consonants in a given string.

    Args:
        string (str): The input string to analyze.

    Returns:
        int: The count of consonants in the string. Consonants include all letters except vowels.
    """
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    for char in string:
        if char in consonants:
            count += 1

    return count


def count_substring_occurrences(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring within a given string.

    Args:
        string (str): The input string to search within.
        substring (str): The substring to count occurrences of.

    Returns:
        int: The number of times the substring appears in the string.
    """
    return string.count(substring)



def count_vowels(string: str) -> int:
    """
    Count the number of vowels in a given string.

    Args:
        string (str): The input string to analyze.

    Returns:
        int: The count of vowels in the string. Vowels include 'a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü'.
    """
    count = 0
    for char in string:
        if char in "aeiouäöü":
            count += 1
    return count

def find_longest_substring(string: str) -> str:
    """
    Find the longest substring of unique characters in a given string.

    Args:
        string (str): The input string to analyze.

    Returns:
        str: The longest substring of unique characters found in the input string.
    """
    longest_substring = ""
    current_substring = ""

    for char in string:
        if char in current_substring:
            # Found a repeating character, update the longest substring if needed
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            # Reset the current substring after the repeated character
            current_substring = current_substring.split(char)[-1]

        # Add the current character to the current substring
        current_substring += char

    # Check if the current substring is longer than the longest substring
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring

def check_pangram(string: str) -> bool:
    """
    Check if a given string is a pangram (contains every letter of the alphabet at least once).

    Args:
        string (str): The input string to check.

    Returns:
        bool: True if the string is a pangram, False otherwise.
    """
    import string as st
    alphabet = set(st.ascii_lowercase)  # Create a set of all lowercase letters

    # Convert the string to lowercase and remove any non-alphabetic characters
    # by using only the characters present in the alphabet set
    filtered_string = "".join(filter(lambda c: c in alphabet, string.lower()))

    # Check if the filtered string contains all the letters of the alphabet
    return set(filtered_string) == alphabet



def find_common_characters(string1: str, string2: str) -> str:
    """
    Find common characters between two strings.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        str: A string containing characters that are common to both input strings.
    """
    return "".join(set(string1) & set(string2))

def split_text(text: str, chunk_size: int) -> List[str]:
    """
    Split a string into chunks of a specified size.

    Args:
        text (str): The input string to split.
        chunk_size (int): The size of each chunk.

    Returns:
        list[str]: A list of substrings, each of length `chunk_size`, except possibly the last one.
    """
    return [text[i: i + chunk_size] for i in range(0, len(text), chunk_size)]

def lchop(string: str, substring: str) -> str:
    """
    Remove a substring from the beginning of a string if it exists.

    Args:
        string (str): The input string.
        substring (str): The substring to remove from the start of `string`.

    Returns:
        str: The modified string with the leading `substring` removed, if it was present.
    """
    if string.startswith(substring):
        return string[len(substring):]
    return string

def rchop(string: str, substring: str) -> str:
    """
    Remove a substring from the end of a string if it exists.

    Args:
        string (str): The input string.
        substring (str): The substring to remove from the end of `string`.

    Returns:
        str: The modified string with the trailing `substring` removed, if it was present.
    """
    if string.endswith(substring):
        return string[:-len(substring)]
    return string



def left_pad(string:str, length:int, char:str=" ")->str:
    """
    Pads the given string on the left with the specified character to the desired length.

    Parameters:
    string (str): The original string.
    length (int): The desired length after padding.
    char (str): The character to pad with (default is a space).

    Returns:
    str: The left-padded string.
    """
    return string.rjust(length, char)


def right_pad(string:str, length:int, char:str=" ")->str:
    """
    Pads the given string on the right with the specified character to the desired length.

    Parameters:
    string (str): The original string.
    length (int): The desired length after padding.
    char (str): The character to pad with (default is a space).

    Returns:
    str: The right-padded string.
    """
    return string.ljust(length, char)


def left_replace(s, chars: Iterable, replacement: str)->str:
    """
    Replace leading characters in `chars` with `replacement` in the string `s`.

    Parameters:
    s (str): The original string.
    chars (str): A string of characters to be replaced.
    replacement (str): The character to replace with.

    Returns:
    str: The modified string with leading characters replaced.
    """
    # Find the first character that is not in `chars`
    index = 0
    while index < len(s) and s[index] in chars:
        index += 1

    # Create the replaced string
    replaced_part = replacement * index
    remaining_part = s[index:]

    return replaced_part + remaining_part


def right_replace(s, chars, replacement)->str:
    """
    Replace trailing characters in `chars` with `replacement` in the string `s`.

    Parameters:
    s (str): The original string.
    chars (str): A string of characters to be replaced.
    replacement (str): The character to replace with.

    Returns:
    str: The modified string with trailing characters replaced.
    """
    # Find the last character that is not in `chars`
    index = len(s) - 1
    while index >= 0 and s[index] in chars:
        index -= 1

    # Create the replaced string
    replaced_part = replacement * (len(s) - index - 1)
    remaining_part = s[: index + 1]

    return remaining_part + replaced_part


def replace_with_list_as_replacement(
    string: str, replacer: str, replacements: Iterable
) -> str:
    """
    Replace all occurrences of a single character in a string with multiple replacement strings.

    Args:
        string (str): The input string to modify.
        replacer (str): The character or substring to replace.
        replacements (Iterable): An iterable of replacement strings.

    Returns:
        str: The modified string after replacements.
    """
    for replacement in replacements:
        string = string.replace(replacer, replacement)
    return string

def replace_with_list_as_replacer(
    string: str, replacers: Iterable, replacement: str
) -> str:
    """
    Replace multiple characters in a string with a single replacement string.

    Args:
        string (str): The input string to modify.
        replacers (Iterable): An iterable of characters or substrings to replace.
        replacement (str): The replacement string.

    Returns:
        str: The modified string after replacements.
    """
    for replacer in replacers:
        string = string.replace(replacer, replacement)
    return string

def replace_list_with_list(
    string: str, replacers: Iterable, replacements: Iterable
) -> str:
    """
    Replace multiple characters in a string with multiple replacement strings, matching the lengths.

    Args:
        string (str): The input string to modify.
        replacers (Iterable): An iterable of characters or substrings to replace.
        replacements (Iterable): An iterable of replacement strings.

    Returns:
        str: The modified string after replacements.

    Raises:
        ValueError: If the lengths of `replacers` and `replacements` do not match.
    """
    if len(replacements) == len(replacers):
        for replacer, replacement in zip(replacers, replacements):
            string = string.replace(replacer, replacement)
        return string
    raise ValueError("List lengths don't match")

def replace(
    string: str, replacers: Union[str , Iterable], replacements: Union[str , Iterable]
) -> str:
    """
    Replace substrings in a string based on the types of `replacers` and `replacements`.

    Args:
        string (str): The input string to modify.
        replacers (Union[str , Iterable]): A single character/substring to replace or an iterable of such substrings.
        replacements (Union[str , Iterable]): A single replacement string or an iterable of replacement strings.

    Returns:
        str: The modified string after replacements.

    Notes:
        - If `replacers` is a string and `replacements` is also a string, it performs a simple replacement.
        - If `replacers` is a string and `replacements` is an iterable, it replaces occurrences of the string `replacers` with each element in `replacements`.
        - If `replacers` is an iterable and `replacements` is a string, it replaces each element in `replacers` with the single `replacement` string.
        - If both `replacers` and `replacements` are iterables, their lengths must match, and it performs element-wise replacements.
    """
    if isinstance(replacers, str):
        if isinstance(replacements, str):
            return string.replace(replacers, replacements)
        return replace_with_list_as_replacement(string, replacers, replacements)
    if isinstance(replacements, str):
        return replace_with_list_as_replacer(string, replacers, replacements)
    return replace_list_with_list(string, replacers, replacements)
