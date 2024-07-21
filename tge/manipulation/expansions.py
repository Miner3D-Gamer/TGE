import random, re
from typing import Iterable


class ExpandedString(str):
    def __new__(cls, value):
        # Call the __new__ method of str and pass the value
        instance = super(ExpandedString, cls).__new__(cls, value)
        return instance

    def __init__(self, value):
        # Any additional initialization can be done here
        super().__init__()

    def get_scrambled(self) -> str:
        """
        Scramble the letters of a given word.

        Returns:
        str: The scrambled word.
        """
        if not isinstance(self, str):
            raise ValueError("Input must be a string")

        word_list = list(self)
        random.shuffle(word_list)
        return "".join(word_list)

    def scramble(self) -> None:
        """
        Scramble the letters of a given word.
        """
        if not isinstance(self, str):
            raise ValueError("Input must be a string")

        word_list = list(self)
        random.shuffle(word_list)
        self = "".join(word_list)

    def chop(self, substring: str) -> None:
        if self.startswith(substring) and self.endswith(substring):
            self = self[len(substring) : -len(substring)]

    def get_chopped(self, substring: str) -> str:
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
            self = self[:length]

    def reverse(self) -> None:
        """
        Reverses the order of characters in a string.
        """
        self = self[::-1]

    def get_reversed(string: str) -> str:
        """
        Reverses the order of characters in a string.

        Returns:
            str: The reversed string.
        """
        return string[::-1]

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
        self = result

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

        max_length = 0  # stores the length of the longest substring
        start = 0  # starting index of the current substring
        char_index_map = {}  # stores the most recent index of each character

        for i in range(len(self)):
            if self[i] in char_index_map and start <= char_index_map[self[i]]:
                # If the current character is already present in the substring,
                # update the starting index of the substring to the next index of the repeated character.
                start = char_index_map[self[i]] + 1
            else:
                # Calculate the length of the current substring and update the maximum length if necessary.
                max_length = max(max_length, i - start + 1)

            # Update the most recent index of the current character.
            char_index_map[self[i]] = i

        return max_length

    def find_first_non_repeating_character(self) -> str:
        """
        Find the first non-repeating character in a given string.

        Args:
            string (str): The input string.

        Returns:
            str: The first non-repeating character found in the string, or None if no such character is found.
        """
        char_count = {}

        # Count the occurrences of each character in the string
        for char in self:
            char_count[char] = char_count.get(char, 0) + 1

        # Find the first non-repeating character
        for char in self:
            if char_count[char] == 1:
                return char

        # If no non-repeating character is found, return None
        return None

    def count_consonants(self) -> int:
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        count = 0

        for char in self:
            if char in consonants:
                count += 1

        return count

    def count_substring_occurrences(self, substring: str) -> int:
        return self.count(substring)

    def count_vowels(self) -> int:
        count = 0
        for char in self:
            if char in "aeiouäöü":
                count += 1
        return count

    def find_longest_substring(self) -> str:
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

    def check_pangram(string: str) -> bool:
        alphabet = set(string.lower)

        filtered_string = "".join(filter(lambda c: c in alphabet, string.lower()))

        return set(filtered_string) == alphabet

    def find_common_characters(self, string2: str) -> str:
        return "".join(set(self) & set(string2))

    def get_chunks(self, chunk_size: int):
        return [self[i : i + chunk_size] for i in range(0, len(self), chunk_size)]

    def lchop(self, substring: str) -> None:
        if self.startswith(substring):
            self = self[len(substring) :]

    def get_lchop(self, substring: str) -> str:
        if self.startswith(substring):
            return self[len(substring) :]
        else:
            return self

    def rchop(self, substring: str) -> None:
        if self.endswith(substring):
            self = self[: -len(substring)]

    def get_rchop(self, substring: str) -> str:
        if self.endswith(substring):

            return self[: -len(substring)]
        else:
            return self

    def left_pad(self, length:int, char:str=" ") -> None:
        """
        Pads the given string on the left with the specified character to the desired length.

        Parameters:
        length (int): The desired length after padding.
        char (str): The character to pad with (default is a space).
        """
        self = self.rjust(length, char)

    def get_left_pad(self, length:int, char:str=" ")->str:
        """
        Pads the given string on the left with the specified character to the desired length.

        Parameters:
        length (int): The desired length after padding.
        char (str): The character to pad with (default is a space).

        Returns:
        str: The left-padded string.
        """
        return self.rjust(length, char)

    def right_pad(self, length, char=" ") -> None:
        """
        Pads the given string on the right with the specified character to the desired length.

        Parameters:
        length (int): The desired length after padding.
        char (str): The character to pad with (default is a space).
        """
        self = self.ljust(length, char)

    def get_right_pad(self, length, char=" "):
        """
        Pads the given string on the right with the specified character to the desired length.

        Parameters:
        length (int): The desired length after padding.
        char (str): The character to pad with (default is a space).

        Returns:
        str: The right-padded string.
        """
        return self.ljust(length, char)

    def left_replace(self, chars: Iterable, replacement: str) -> None:
        """
        Replace leading characters in `chars` with `replacement` in the string.

        Parameters:
        chars (str): A string of characters to be replaced.
        replacement (str): The character to replace with.
        """
        # Find the first character that is not in `chars`
        index = 0
        while index < len(self) and self[index] in chars:
            index += 1

        # Create the replaced string
        replaced_part = replacement * index
        remaining_part = self[index:]

        self = replaced_part + remaining_part

    def get_left_replace(self, chars: Iterable, replacement: str)->str:
        """
        Replace leading characters in `chars` with `replacement` in the string.

        Parameters:
        chars (Iterable): A string of characters to be replaced.
        replacement (str): The character to replace with.

        Returns:
        str: The modified string with leading characters replaced.
        """
        # Find the first character that is not in `chars`
        index = 0
        while index < len(self) and self[index] in chars:
            index += 1

        # Create the replaced string
        replaced_part = replacement * index
        remaining_part = self[index:]

        return replaced_part + remaining_part

    def get_right_replace(self, chars: Iterable, replacement: str):
        """
        Replace trailing characters in `chars` with `replacement` in the string.

        Parameters:
        chars (str): A string of characters to be replaced.
        replacement (str): The character to replace with.

        Returns:
        str: The modified string with trailing characters replaced.
        """
        # Find the last character that is not in `chars`
        index = len(self) - 1
        while index >= 0 and self[index] in chars:
            index -= 1

        # Create the replaced string
        replaced_part = replacement * (len(self) - index - 1)
        remaining_part = self[: index + 1]

        return remaining_part + replaced_part

    def right_replace(self, chars: Iterable, replacement: str) -> None:
        """
        Replace trailing characters in `chars` with `replacement` in the string.

        Parameters:
        chars (str): A string of characters to be replaced.
        replacement (str): The character to replace with.
        """
        # Find the last character that is not in `chars`
        index = len(self) - 1
        while index >= 0 and self[index] in chars:
            index -= 1

        # Create the replaced string
        replaced_part = replacement * (len(self) - index - 1)
        remaining_part = self[: index + 1]

        self = remaining_part + replaced_part

    def remove_html_tags(self) -> str:
        """
        Removes HTML tags from the given string.
        """
        self = re.sub(r"<.*?>", "", self)

    def get_with_html_tags_removed(self) -> str:
        """
        Removes HTML tags from the given string.

        Returns:
            str: The modified string with HTML tags removed.
        """
        return re.sub(r"<.*?>", "", self)

    def replace_with_list_as_replacement(
        self, replacer: str, replacements: Iterable
    ) -> None:
        for replacement in replacements:
            string = string(replacer, replacement)

    def replace_with_list_as_replacer(
        string, replacers: Iterable, replacement: str
    ) -> None:
        for replacer in replacers:
            string = string(replacer, replacement)

    def get_replace_with_list_as_replacement(
        self, replacer: str, replacements: Iterable
    ) -> str:
        string = self
        for replacement in replacements:
            string = string(replacer, replacement)
        return string

    def get_replace_with_list_as_replacer(
        self, replacers: Iterable, replacement: str
    ) -> str:
        string = self
        for replacer in replacers:
            string = string(replacer, replacement)
        return string


