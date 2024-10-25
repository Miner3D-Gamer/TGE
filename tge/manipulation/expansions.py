import random, re
from typing import List, Dict, Optional


class ExpandedString(str):
    def __new__(cls, value: str):
        """
        Create a new instance of the ExpandedString class.

        Args:
            cls: The class being instantiated.
            value (str): The initial value for the new instance, which will be passed to the str constructor.

        Returns:
            ExpandedString: A new instance of the ExpandedString class.

        Notes:
            This method uses the __new__ method of the str class to create a new string instance.
            It then returns this instance as an ExpandedString object.
        """
        instance = super(ExpandedString, cls).__new__(cls, value)
        return instance

    def __init__(self, value: str):
        """
        Initialize an instance of the ExpandedString class.

        Args:
            value (str): The initial value for the instance. This is passed to the __new__ method and used to initialize the string.

        Notes:
            Any additional initialization code specific to the ExpandedString class can be added here.
            The superclass __init__ method is not explicitly called because str objects are immutable and 
            their initialization is handled by the __new__ method.
        """
        super().__init__()

    def get_scrambled(self) -> str:
        """
        Scramble the letters of a given word.

        Returns:
        str: The scrambled word.
        """

        word_list = list(self)
        random.shuffle(word_list)
        return "".join(word_list)

    def scramble(self) -> None:
        """
        Scramble the letters of a given word.
        """

        word_list = list(self)
        random.shuffle(word_list)
        self = ExpandedString("".join(word_list))

    def chop(self, substring: str) -> None:
        """
        Remove a specified substring from the beginning and end of the string.

        Args:
            substring (str): The substring to be removed from both the start and end of the string.

        Modifies:
            self: The string is modified in place to remove the specified substring from both ends.
        """
        if self.startswith(substring) and self.endswith(substring):
            self = ExpandedString(self[len(substring) : -len(substring)]
)
    def get_chopped(self, substring: str) -> str:
        """
        Return a new string with a specified substring removed from the beginning and end.

        Args:
            substring (str): The substring to be removed from both the start and end of the string.

        Returns:
            str: A new string with the specified substring removed from both the start and end if present;
                otherwise, returns the original string.
        """
        if self.startswith(substring) and self.endswith(substring):
            return self[len(substring) : -len(substring)]
        else:
            return self

    def get_truncated(self, length: int) -> str:
        """
        Truncates a string to the specified length.

        Args:
            length (int): The maximum length of the truncated string.

        Returns:
            str: The truncated string.
        """
        if len(self) <= length:
            return self
        else:
            return self[:length]

    def truncate(self, length: int) -> None:
        """
        Truncates a string to the specified length.
        """
        if not (len(self) <= length):
            self = ExpandedString(self[:length])

    def reverse(self) -> None:
        """
        Reverses the order of characters in a string.
        """
        self = ExpandedString(self[::-1])

    def get_reversed(self: str) -> str:
        """
        Reverses the order of characters in a string.

        Returns:
            str: The reversed string.
        """
        return self[::-1]

    def check_anagram(self, word2: str) -> bool:
        """
        Check if two words are anagrams of each other.

        Args:
            word1 (str): The first word to check.
            word2 (str): The second word to check.

        Returns:
            bool: True if the words are anagrams, False otherwise.
        """
        return sorted(self) == sorted(word2)

    def remove_duplicate_characters(self) -> None:
        """
        Remove duplicate characters from a given string.
        """
        result = ""
        for char in self:
            if char not in result:
                result += char
        self = ExpandedString(result)

    def get_string_after_removing_duplicate_characters(self) -> str:
        """
        Remove duplicate characters from a given string.

        Returns:
            str: The string with duplicate characters removed.
        """
        result = ""
        for char in self:
            if char not in result:
                result += char
        return result

    def find_longest_word(self) -> str:
        """
        Find the longest word in a given string.

        Returns:
            str: The longest word found in the string.
        """
        return max(self.split(), key=len)

    def get_length_of_longest_substring_without_repeating_characters(self) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        if not self:
            return 0

        max_length = 0  
        start = 0 
        char_index_map:Dict[str, int] = {}  

        for i in range(len(self)):
            if self[i] in char_index_map and start <= char_index_map[self[i]]:
                start = char_index_map[self[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            char_index_map[self[i]] = i

        return max_length

    def find_first_non_repeating_character(self) ->Optional [str]:
        """
        Find the first non-repeating character in a given string.

        Args:
            string (str): The input string.

        Returns:
            str: The first non-repeating character found in the string, or None if no such character is found.
        """
        char_count:Dict[str, int] = {}

        for char in self:
            char_count[char] = char_count.get(char, 0) + 1

        for char in self:
            if char_count[char] == 1:
                return char

        return None

    def count_consonants(self) -> int:
        """
        Count the number of consonants in the string.

        Consonants are defined as letters that are not vowels. This method considers both uppercase and lowercase 
        consonants and counts each occurrence within the string.

        Returns:
            int: The number of consonant characters in the string.
        """
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        count = 0

        for char in self:
            if char in consonants:
                count += 1

        return count


    def count_substring_occurrences(self, substring: str) -> int:
        """
        Count the number of occurrences of a substring within the string.

        Args:
            substring (str): The substring to search for within the string.

        Returns:
            int: The number of times the substring appears in the string.
        """
        return self.count(substring)


    def count_vowels(self) -> int:
        """
        Count the number of vowels in the string.

        Returns:
            int: The total number of vowels (including 'a', 'e', 'i', 'o', 'u', and 'ä', 'ö', 'ü') in the string.
        """
        count = 0
        for char in self:
            if char in "aeiouäöü":
                count += 1
        return count

    def find_longest_substring(self) -> str:
        """
        Find the longest substring without repeating characters.

        Returns:
            str: The longest substring within the string that does not contain any repeating characters.
        """
        longest_substring = ""
        current_substring = ""

        for char in self:
            if char in current_substring:
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                current_substring = current_substring.split(char)[-1]

            current_substring += char

        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring

        return longest_substring

    def check_pangram(self) -> bool:
        """
        Check if the string is a pangram (contains every letter of the alphabet at least once).

        Returns:
            bool: True if the string contains every letter of the alphabet, False otherwise.
        """
        alphabet = set(self.lower())

        filtered_string = "".join(filter(lambda c: c in alphabet, self.lower()))

        return set(filtered_string) == alphabet

    def find_common_characters(self, string2: str) -> str:
        """
        Find the common characters between two strings.

        Args:
            string2 (str): The second string to compare with.

        Returns:
            str: A string of characters that are common to both strings.
        """
        return "".join(set(self) & set(string2))

    def get_chunks(self, chunk_size: int):
        """
        Split the string into chunks of a specified size.

        Args:
            chunk_size (int): The size of each chunk.

        Returns:
            list: A list of string chunks.
        """
        return [self[i : i + chunk_size] for i in range(0, len(self), chunk_size)]

    def lchop(self, substring: str) -> None:
        """
        Remove the specified prefix substring from the start of the string in-place.

        Args:
            substring (str): The prefix substring to be removed.

        Returns:
            None: The method modifies the string in place, no return value.
        """
        if self.startswith(substring):
            self = ExpandedString(self[len(substring) :])

    def get_lchop(self, substring: str) -> str:
        """
        Return a string with the specified prefix substring removed from the start.

        Args:
            substring (str): The prefix substring to be removed.

        Returns:
            str: The modified string with the prefix removed, or the original string if the prefix is not present.
        """
        if self.startswith(substring):
            return self[len(substring) :]
        else:
            return self

    def rchop(self, substring: str) -> None:
        """
        Remove the specified suffix substring from the end of the string in-place.

        Args:
            substring (str): The suffix substring to be removed.

        Returns:
            None: The method modifies the string in place, no return value.
        """
        if self.endswith(substring):
            self = ExpandedString(self[: -len(substring)])

    def get_rchop(self, substring: str) -> str:
        """
        Remove the specified substring from the end of the string if it exists.

        Args:
            substring (str): The substring to be removed from the end of the string.

        Returns:
            str: The modified string with the specified substring removed from the end if it was present.
                If the substring is not found at the end, the original string is returned.
        """
        if self.endswith(substring):

            return self[: -len(substring)]
        else:
            return self

    def left_pad(self, length: int, char: str = " ") -> None:
        """
        Pads the given string on the left with the specified character to the desired length.

        Parameters:
        length (int): The desired length after padding.
        char (str): The character to pad with (default is a space).
        """
        self = ExpandedString(self.rjust(length, char))

    def get_left_pad(self, length: int, char: str = " ") -> str:
        """
        Pads the given string on the left with the specified character to the desired length.

        Parameters:
        length (int): The desired length after padding.
        char (str): The character to pad with (default is a space).

        Returns:
        str: The left-padded string.
        """
        return self.rjust(length, char)

    def right_pad(self, length: int, char:str=" ") -> None:
        """
        Pads the given string on the right with the specified character to the desired length.

        Parameters:
        length (int): The desired length after padding.
        char (str): The character to pad with (default is a space).
        """
        self = ExpandedString(self.ljust(length, char))

    def get_right_pad(self, length:int, char:str=" "):
        """
        Pads the given string on the right with the specified character to the desired length.

        Parameters:
        length (int): The desired length after padding.
        char (str): The character to pad with (default is a space).

        Returns:
        str: The right-padded string.
        """
        return self.ljust(length, char)

    def left_replace(self, chars: List[str], replacement: str) -> None:
        """
        Replace leading characters in `chars` with `replacement` in the string.

        Parameters:
        chars (str): A string of characters to be replaced.
        replacement (str): The character to replace with.
        """
        index = 0
        while index < len(self) and self[index] in chars:
            index += 1

        replaced_part = replacement * index
        remaining_part = self[index:]

        self = ExpandedString(replaced_part + remaining_part)

    def get_left_replace(self, chars: List[str], replacement: str) -> str:
        """
        Replace leading characters in `chars` with `replacement` in the string.

        Parameters:
        chars (List[str]): A string of characters to be replaced.
        replacement (str): The character to replace with.

        Returns:
        str: The modified string with leading characters replaced.
        """
        index = 0
        while index < len(self) and self[index] in chars:
            index += 1

        replaced_part = replacement * index
        remaining_part = self[index:]

        return replaced_part + remaining_part

    def get_right_replace(self, chars: List[str], replacement: str):
        """
        Replace trailing characters in `chars` with `replacement` in the string.

        Parameters:
        chars (str): A string of characters to be replaced.
        replacement (str): The character to replace with.

        Returns:
        str: The modified string with trailing characters replaced.
        """
        index = len(self) - 1
        while index >= 0 and self[index] in chars:
            index -= 1

        replaced_part = replacement * (len(self) - index - 1)
        remaining_part = self[: index + 1]

        return remaining_part + replaced_part

    def right_replace(self, chars: List[str], replacement: str) -> str:
        """
        Replace trailing characters in `chars` with `replacement` in the string.

        Parameters:
        chars (str): A string of characters to be replaced.
        replacement (str): The character to replace with.
        """
        index = len(self) - 1
        while index >= 0 and self[index] in chars:
            index -= 1

        replaced_part = replacement * (len(self) - index - 1)
        remaining_part = self[: index + 1]

        self = ExpandedString(remaining_part + replaced_part)
        return self

    def remove_html_tags(self) -> str:
        """
        Removes HTML tags from the given string.
        """
        self = ExpandedString(re.sub(r"<.*?>", "", self))
        return self

    def get_with_html_tags_removed(self) -> str:
        """
        Removes HTML tags from the given string.

        Returns:
            str: The modified string with HTML tags removed.
        """
        return re.sub(r"<.*?>", "", self)

    def replace_with_list_as_replacement(
        self, replacer: str, replacements: List[str]
    ) -> None:
        """
        Replace all occurrences of a specified substring in a string with a list of replacement substrings.

        Args:
            replacer (str): The substring to be replaced.
            replacements (List[str]): An iterable of replacement substrings.

        Returns:
            None: The method modifies the string in place, no return value.
        """
        for replacement in replacements:
            self = ExpandedString(self.replace(replacer, replacement))

    def replace_with_list_as_replacer(
        self, replacers: List[str], replacement: str
    ) -> None:
        """
        Replace all occurrences of each substring in a list of replacers with a specified replacement substring in the given string.

        Args:
            string (str): The string in which replacements will be made.
            replacers (List[str]): An iterable of substrings to be replaced.
            replacement (str): The replacement substring.

        Returns:
            None: The method modifies the string in place, no return value.
        """

        for replacer in replacers:
            self = ExpandedString(self.replace(replacer, replacement))

    def get_replace_with_list_as_replacement(
        self, replacer: str, replacements: List[str]
    ) -> str:
        """
        Return a new string where all occurrences of a specified substring are replaced with a list of replacement substrings.

        Args:
            replacer (str): The substring to be replaced.
            replacements (List[str]): An iterable of replacement substrings.

        Returns:
            str: The modified string with replacements applied.
        """
        string = self
        for replacement in replacements:
            string = ExpandedString(string.replace(replacer, replacement))
        return string

    def get_replace_with_list_as_replacer(
        self, replacers: List[str], replacement: str
    ) -> str:
        """
        Return a new string where all occurrences of each substring in a list of replacers are replaced with a specified replacement substring.

        Args:
            replacers (List[str]): An iterable of substrings to be replaced.
            replacement (str): The replacement substring.

        Returns:
            str: The modified string with replacements applied.
        """
        
        for replacer in replacers:
            self = ExpandedString(self.replace(replacer, replacement))
        return self
