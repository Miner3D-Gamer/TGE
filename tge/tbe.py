# TODO: The original tge file with every single function in one big mess before splitting them across multiple files
# TODO: What a true beauty of random comments, miscellaneous code, and unfinished/discarded functions
# TODO: Anyways, what are you doing here? Idk why you would be here but hi :<



# from time import sleep, timezone
# from os import system as os_system, path as os_path, environ, makedirs as os_createDirectory, listdir as os_listdir, getcwd as os_getcwd, rename as os_rename, remove as os_remove; environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# from sys import stdout as sys_stdout


#from pytz import timezone as pytz_timezone
#from math import sqrt, log, log2, modf, ceil, floor, factorial





#from numpy import median as np_median, abs as np_abs, corrcoef as np_corrcoef
# from requests import get as requests_get, post as requests_post
# from importlib import import_module as importlib_import_module
# from bs4 import BeautifulSoup
#from re import split as re.split


#log = []

# def wtl(txt, lvl):
#     if lvl == 0:
#         pre = "[Info: '"
#     elif lvl == 1:
#         pre = "[Warning: '"
#     elif lvl == 2:
#         pre = "[Error: '"
#     else: pre = "[Info: '"
#     log.append(pre + txt + "']")

#nor = randint(0, 100)


#inventory = []
# wtl("Initialized", 0)


# def initSession(message) -> None:
#     """Initializes the session.

#     Calls initSessionTime() and prints the given message.
#     Initializes the global enemies, inventory, and AttackTypes dictionaries.
#     """
#     initSessionTime()
#     print(message)
#     global enemies
#     global inventory
#     global AttackTypes
#     enemies = {}
#     inventory = {}
#     AttackTypes = {}








# def count_len(input_item: Any) -> int:
#     """
#     Returns the length of the input item.

#     Arguments:
#     - input_item: object to determine length of

#     Returns:
#     - length of input_item if it is a string or list
#     - -1 otherwise
#     """
#     if type(input_item) == list:
#         return len(input_item)
#     else:
#         try:
#             input_item = str(input_item)
#             return len(input_item)
#         except:
#             return -1

from collections.abc import Iterable

from types import FunctionType, ModuleType, MethodType

from typing import List, Union, Tuple , Any, get_type_hints
import ast
import os
import sys
import importlib
from difflib import get_close_matches

import inspect






def pass_func(*args: Any) -> None:
    """
    This function does nothing and has no side effects.
    
    Returns:
        None: This function does not return any value.
    
    """
    pass





def execute_function(func=pass_func, *args: Any, **kwargs: Any) -> Any:
    """
    Executes a function with the given arguments and keyword arguments.

    Parameters:
        func (callable): The function to be executed. Defaults to 'pass_func'.
        *args (Any): Variable length arguments to be passed to the function.
        **kwargs (Any): Keyword arguments to be passed to the function.

    Returns:
        Any: The result of executing the function.

    Example:
        # Define a sample function
        def add_numbers(a, b):
            return a + b

        # Call the 'execute_function' with the 'add_numbers' function
        result = execute_function(add_numbers, 5, 3)
        # The result will be 8
    """
    return func(*args, **kwargs)









def determine_affirmative(text: str) -> bool:
    """
    Determines if the given text is an affirmative response or not.

    Args:
        text (str): The input text to be evaluated.

    Returns:
        bool: True if the text is an affirmative response, False if it is a negative response,
              and None if it cannot be determined.
    """
    
    text = text.strip().lower()
    
    
    positives = ["y", "yes", "yeah", "yup", "uh-huh", "sure", "affirmative", "absolutely", "indeed",
                 "certainly", "of course", "definitely", "you bet", "roger", "right on", "no doubt",
                 "by all means", "most certainly", "positively", "without a doubt", "naturally",
                 "indubitably", "sure thing", "yuppers", "aye", "ok", "okey-dokey", "all right",
                 "righto", "very well", "exactly", "precisely", "no problem", "for sure", "most assuredly",
                 "you got it", "that's right", "sure as shooting", "all righty", "of course, my dear",
                 "couldn't agree more", "a thousand times, yes", "i'm in", "it's a go", "i'll go along with that",
                 "count me in", "i'm on board", "without hesitation", "undoubtedly", "yeye"]
    
    negatives = ["n", "no", "nope", "nah", "nuh-uh", "negative", "not at all", "absolutely not", "certainly not",
                 "no way", "never", "i disagree", "i'm afraid not", "i can't agree with that", "i beg to differ",
                 "i'm not convinced", "not really", "i'm not so sure", "i have my doubts", "that's not correct",
                 "that's incorrect", "i don't think so", "i'm not on board with that", "i'm not buying it",
                 "i can't go along with that", "i can't support that", "i'm opposed to that", "i'm against it",
                 "i'm not in favor of that", "that's a negative", "no chance", "not a chance", "no siree",
                 "i can't see that happening", "i'm not inclined to agree", "i can't accept that", "i'm not on the same page",
                 "i'm not feeling it", "i have reservations", "i can't endorse that", "that's out of the question",
                 "i can't support that notion", "i'm skeptical", "that doesn't work for me", "i don't agree with that assessment",
                 "i'm not persuaded", "i'm not buying into that", "i don't subscribe to that view", "i can't go along with that",
                 "i'm not swayed by that argument", "i don't believe so", "i'm not on board", "i can't back that up",
                 "i'm not convinced of its validity", "that's not my understanding", "i'm not sold on that idea", "i can't vouch for that",
                 "i don't really feel like it", "not really"]

    
    if text in positives:
        return True
    if text in negatives:
        return False

    # Get close matches for indirect checking
    closest_positive_match = get_close_matches(text, positives, n=1, cutoff=0.8)
    closest_negative_match = get_close_matches(text, negatives, n=1, cutoff=0.8)

    # Handling positive and negative matches
    if closest_positive_match:
        return True
    if closest_negative_match:
        return False

    # If no clear determination can be made
    return None

def categorize_responses(text_list: Iterable[str]) -> List[str]:
    """
    Categorizes a list of text responses as affirmative, negative, or uncertain.

    This function takes a list of text responses and categorizes each response
    as either affirmative, negative, or uncertain based on the result of the
    `determine_affirmative` function.

    Args:
        text_list (List[str]): A list of text responses to be categorized.

    Returns:
        List[str]: A list of categorized responses, where each response is
        classified as 'True' for affirmative, 'False' for negative, or 'None'
        for uncertain.

    Example:
        >>> responses = ["Yes", "No", "Maybe"]
        >>> categorized = categorize_responses(responses)
        >>> print(categorized)
        [True, False, None]
    """
    response_list = []

    for text in text_list:
        response_list.append(determine_affirmative(text))
    return response_list

def get_available_variables() -> Tuple:
    """
    Retrieve and return the available global and local variables in the current scope.

    This function gathers both global and local variables, storing them in separate dictionaries.
    It collects global variables using the `globals()` function and local variables using the `locals()` function.
    The resulting dictionaries contain variable names as keys and their corresponding values as values.

    Returns:
        Tuple[Dict[str, Any], Dict[str, Any]]: A tuple containing two dictionaries.
        The first dictionary holds global variables, and the second dictionary holds local variables.
    """
    g_variables = {}
    l_variables = {}
    # Retrieve global variables
    global_vars = globals()
    for var_name, var_value in global_vars.items():
        g_variables[var_name] = var_value

    # Retrieve local variables
    local_vars = locals()
    for var_name, var_value in local_vars.items():
        l_variables[var_name] = var_value

    return g_variables, l_variables





# from tge.random_generators import randomInt
# from tge import console_utils

# def higher_lower_game(random_num: int = None, max_num: int = None, min_num: int = None, num_of_guesses: int = 0, num_range: int = None):
#     if random_num is None:
#         randomInt(0, 10, False)
    
    
#     random_num = 5
#     while True:
#         guess = console_utils.typingInput("Your Guess:", 0.01)
#         try:
#             guess = int(guess)
#             break
#         except:
#             console_utils.clear_lines(1)




# higher_lower_game()



#hi = "post_to_discord_webhook"


def get_docstring(obj: object) -> str:
    """
    Retrieve the docstring of a given object.

    This function attempts to extract and return the docstring of the provided object.
    
    Args:
        obj (object): The object for which the docstring is to be retrieved.

    Returns:
        str: The docstring of the object if available, otherwise an empty string.
    """
    try:
        return inspect.getdoc(obj)
    except:
        return ""





def convert_number_to_words_less_than_thousand(n:str, dash:bool = True) -> str:
        """
        Converts a number (less than one thousand) to its word representation.

        Args:
            n (int): The number to be converted. Should be between 0 and 999.

        Returns:
            str: The word representation of the input number.

        Example:
            >>> convert_number_to_words_less_than_thousand(356)
            'three hundred and fifty-six'
        """

        TINY_NUMBERS = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ]
        SMALL_NUMBERS = [
            "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
            ]

        if n >= 100:
            hundreds_digit = n // 100
            rest = n % 100
            result = TINY_NUMBERS[hundreds_digit] + " hundred"
            if rest > 0:
                result += " and " + convert_number_to_words_less_than_thousand(rest)
            return result
        elif n >= 20:
            tens_digit = n // 10
            rest = n % 10
            result = SMALL_NUMBERS[tens_digit]
            if rest > 0:
                if dash:
                    result += "-" + TINY_NUMBERS[rest]
                else:
                    result += " " + TINY_NUMBERS[rest]
            return result
        else:
            return TINY_NUMBERS[n]

def number_to_words(number:int) -> str:
    """
    Converts a given integer into its English word representation.
    
    Args:
        number (int): The integer to be converted into words.
        
    Returns:
        str: The English word representation of the input integer.
        
    Examples:
        >>> number_to_words(123456789)
        'one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine'
        
        >>> number_to_words(-42)
        'minus forty-two'
    """

    big_numbers = [
    "", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion",
    "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion",
    "duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion",
    "septendecillion", "octodecillion", "novemdecillion", "vigintillion", "unvigintillion",
    "duovigintillion", "trevigintillion", "quattuorvigintillion", "quinvigintillion", 
    "sexvigintillion", "septenvigintillion", "octovigintillion", "novemvigintillion",
    "trigintillion", "untrigintillion", "duotrigintillion", "trevigintillion", "quattuortrigintillion",
    "quintrigintillion", "sextrigintillion", "septentrigintillion", "octotrigintillion",
    "novemtrigintillion", "quadragintillion", "unquadragintillion", "duoquadragintillion",
    "trequadragintillion", "quattuorquadragintillion", "quinquadragintillion", "sexquadragintillion",
    "septenquadragintillion", "octoquadragintillion", "novemquadragintillion", "quinquagintillion",
    "unquinquagintillion", "duoquinquagintillion", "trequinquagintillion", "quattuorquinquagintillion",
    "quinquinquagintillion", "sexquinquagintillion", "septenquinquagintillion",
    "octaquinquagintillion", "novemquinquagintillion", "sexagintillion",
    "unsexagintillion", "duosexagintillion", "tresexagintillion", "quattuorsexagintillion",
    "quinsexagintillion", "sexsexagintillion", "septensexagintillion",
    "octasexagintillion", "novemsexagintillion", "septuagintillion", "unseptuagintillion",
    "duoseptuagintillion", "treseptuagintillion", "quattuorseptuagintillion",
    "quinseptuagintillion", "sexseptuagintillion", "septenseptuagintillion",
    "octaseptuagintillion", "novemseptuagintillion", "octagintillion",
    "unoctogintillion", "duooctogintillion", "treoctogintillion","quattuoroctogintillion",
    "quinoctogintillion", "sexoctogintillion", "septenoctogintillion",
    "octaoctogintillion", "novemoctogintillion", "nonagintillion", "unnonagintillion",
    "duononagintillion", "trenonagintillion", "quattuornonagintillion",
    "quinnonagintillion", "sexnonagintillion", "septennonagintillion",
    "octanonagintillion", "novemnonagintillion", "centillion", "cenuntillion",
    "centretillion", "cenquattuortillion", "cenquintillion", "censextillion",
    "censeptentillion", "cenoctotillion", "cennovemtillion", "cendecillion",
    "centredecillion", "cenquattuordecillion", "cenquindecillion", "censexdecillion",
    "censeptendecillion", "cenoctodecillion", "cennovemdecillion", "cenvigintillion",
    "cenunvigintillion", "cendovigintillion", "centrevigintillion",
    "cenquattuorvigintillion", "cenquinvigintillion", "censexvigintillion",
    "censeptenvigintillion", "cenoctovigintillion", "cennovemvigintillion",
    "centrigintillion", "cenuntrigintillion", "cendotrigintillion",
    "centretrigintillion", "cenquattuortrigintillion", "cenquintrigintillion",
    "censextrigintillion", "censeptentrigintillion", "cenoctotrigintillion",
    "cennovemtrigintillion", "cenquadragintillion", "cenunquadragintillion",
    "cendoquadragintillion", "centrequadragintillion",
    "cenquattuorquadragintillion", "cenquinquadragintillion",
    "censexquadragintillion", "censeptenquadragintillion",
    "cenoctoquadragintillion", "cennovemquadragintillion",
    "cenquinquagintillion", "cenunquinquagintillion",
    "cendoquinquagintillion", "centrequinquagintillion",
    "cenquattuorquinquagintillion", "cenquinquinquagintillion",
    "censexquinquagintillion", "censeptenquinquagintillion",
    "cenoctoquinquagintillion", "cennovemquinquagintillion",
    "censexagintillion", "cenunsexagintillion", "cendosexagintillion",
    "centresexagintillion", "cenquattuorsexagintillion",
    "cenquinsexagintillion", "cenquinsexagintilliard", "censexagintillion",
    "censexsexagintilliard", "censeptensexagintillion", "censeptensexagintilliard",
    "cenoctosexagintillion", "cenoctosexagintilliard", "cennovemsexagintillion",
    "cennovemsexagintilliard", "censeptuagintillion", "censeptuagintilliard",
    "cenunseptuagintillion", "cenunseptuagintilliard", "cendoseptuagintillion",
    "cendoseptuagintilliard", "centreseptuagintillion", "centreseptuagintilliard",
    "cenquattuorseptuagintillion", "cenquattuorseptuagintilliard", "cenquinseptuagintillion",
    "cenquinseptuagintilliard", "censexseptuagintillion", "censexseptuagintilliard",
    "censeptenseptuagintillion", "censeptenseptuagintilliard", "cenoctoseptuagintillion",
    "cenoctoseptuagintilliard", "cennovemseptuagintillion", "cennovemseptuagintillion",
    "cennovemseptuagintilliard", "cenoctogintillion", "cenoctogintilliard", "cenunoctogintillion",
    "cenunoctogintilliard", "cendooctogintillion", "cendooctogintilliard",
    "centreoctogintillion"
    ]

        
    # Handling special cases for zero and negative numbers
    if number == 0:
        return "zero"
    elif number < 0:
        return "minus " + number_to_words(abs(number))
    
    # Split the number into groups of three digits and convert each group to words
    groups = []
    while number > 0:
        groups.append(number % 1000)
        number //= 1000
    
    
    result_parts = []
    for i, group in enumerate(groups):
        if group != 0:
            result_parts.append(convert_number_to_words_less_than_thousand(group) + " " + big_numbers[i])
    
    # Join the parts and return the final result
    return ", ".join(reversed(result_parts))










def find_undocumented_functions(file_path:str)->list:
    """Find all functions without docstrings in a Python file.

Args:
    file_path (str): Path to the Python file to scan.

Returns:
    list: A list of undocumented functions, each represented as a list with the function name and its end line number."""
    undocumented_functions = []

    with open(file_path, 'r', encoding="utf8") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                undocumented_functions.append([node.name,node.end_lineno])

    return undocumented_functions

def check_directory_for_undocumented_functions(directory_path:str)->dict:
    """Check a directory for Python files and find undocumented functions in each file.

Args:
    directory_path (str): Path to the directory to scan.

Returns:
    dict: A dictionary where keys are filenames and values are lists of undocumented functions, each represented as a list with the function name and its end line number."""
    undocumented_functions_dict = {}

    for filename in os.listdir(directory_path):
        if filename.endswith('.py'):
            file_path = os.path.join(directory_path, filename)
            undocumented_functions = find_undocumented_functions(file_path)
            if undocumented_functions:
                undocumented_functions_dict[filename] = undocumented_functions

    return undocumented_functions_dict

def check_directory_and_sub_directory_for_undocumented_functions(directory_path:str)->dict:
    """Check a directory and its subdirectories for Python files and find undocumented functions in each file.

Args:
    directory_path (str): Path to the directory to scan.

Returns:
    dict: A dictionary where keys are relative file paths and values are lists of undocumented functions, each represented as a list with the function name and its end line number."""
    undocumented_functions_dict = {}

    def _check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(current_path:str)->None:
        """Recursively traverse directories and files to find undocumented functions in Python files and update the dictionary with results.

Args:
    current_path (str): The path of the current directory to traverse.

Inner Updates:
    Updates `undocumented_functions_dict` with undocumented functions found in Python files, using relative paths as keys."""
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)

            if os.path.isdir(item_path):
                # Recursively traverse subdirectories
                _check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(item_path)
            elif item.endswith('.py'):
                undocumented_functions = find_undocumented_functions(item_path)
                if undocumented_functions:
                    # Store undocumented functions for the current file
                    filename = os.path.relpath(item_path, directory_path)
                    undocumented_functions_dict[filename] = undocumented_functions

    _check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(directory_path)

    return undocumented_functions_dict











# def download_multiple_videos(video_dict, save_path):
#     video_infos = [(url_id, save_path, file_name) for url_id, file_name in video_dict.items()]
    
#     with Pool() as pool:
#         results = pool.map(download_youtube_video, video_infos)
    
#     return results



def autocomplete(prefix:str, word_list:Iterable[str])->list[str]:
    """Return a list of words from `word_list` that start with the specified `prefix`.

Args:
    prefix (str): The prefix to match against.
    word_list (Iterable[str]): A list of words to search through.

Returns:
    list[str]: A list of matching words."""
    return [word for word in word_list if word.startswith(prefix)]

def strict_autocomplete(prefix:str, word_list:Iterable[str])->list[str]|str:
    """Return a single word, the prefix itself, or a list of words that start with the specified `prefix`.

Args:
    prefix (str): The prefix to match against.
    word_list (Iterable[str]): A list of words to search through.

Returns:
    str | list[str]: The single matching word, the prefix, or a list of matching words.
"""
    words = autocomplete(prefix=prefix, word_list=word_list)
    if len(words) == 1:
        return words[0]
    if prefix in words:
        return prefix
    return words


def is_iterable(thing:Any)->bool:
    """Check if a given object is iterable.

Args:
    thing (Any): The object to check.

Returns:
    bool: True if the object is iterable, otherwise False."""
    return hasattr(thing,"__iter__")



def split_with_list(string: str, separators: Iterable, limit: None | int = None) -> list[str]:
    """Split a string by multiple separators and return the resulting substrings.

Args:
    string (str): The string to split.
    separators (Iterable): A list of separators to replace with a unique delimiter.
    limit (None | int, optional): The maximum number of splits to perform. Defaults to None, meaning no limit.

Returns:
    list[str]: A list of substrings resulting from the split operation."""
    for separator in separators:
        string = string.replace(separator, "𘚟")
    return string.split("𘚟")



def analyze_text(text:str)->dict[str:str|list]:
    """Analyze the text to provide various statistics about sentences, words, and commas.

Args:
    text (str): The text to analyze.

Returns:
    dict[str, str | list]: A dictionary with the following keys:
        - "sentence_amount": Number of sentences.
        - "total_word_count": Total number of words.
        - "average_word_count_per_sentence": Average number of words per sentence.
        - "max_words_per_sentence": Maximum number of words in a sentence.
        - "min_words_per_sentence": Minimum number of words in a sentence.
        - "total_comma_count": Total number of commas.
        - "average_commas_count_per_sentence": Average number of commas per sentence.
        - "max_commas_per_sentence": Maximum number of commas in a sentence.
        - "min_commas_per_sentence": Minimum number of commas in a sentence.
        - "word_amount_list": List of word counts for each sentence.
        - "comma_amount_list": List of comma counts for each sentence."""
    text = text.replace("...", "…").replace("\n", "").strip()

    legacy_sentences = split_with_list(text, [". ", "! ", "? "])

    sentences = []
    word_amounts = []
    comma_amounts = []

    for i in range(len(legacy_sentences)):
        commas = legacy_sentences[i].count(",")
        words = legacy_sentences[i].split(" ")
        deleted = 0
        for j in range(len(words)):
            words[j] = words[j].replace(",", "")
            if words[j].strip() == "":
                words.pop(j)
                deleted += 1
            if len(words) <= j+deleted:
                break
            #print(words[j])
        if not len(words) == 0:
            word_amounts.append(len(words))
        sentences.append(words)
        comma_amounts.append(commas)





    total_word_count = 0
    for word_amount in word_amounts:
        total_word_count += word_amount

    total_comma_count = 0
    for comma_amount in comma_amounts:
        total_comma_count += comma_amount
    return {
        "sentence_amount":len(sentences),
        "total_word_count":total_word_count,
        "average_word_count_per_sentence":total_word_count/len(word_amounts),
        "max_words_per_sentence":max(word_amounts),
        "min_words_per_sentence":min(word_amounts),
        "total_comma_count":total_comma_count,
        "average_commas_count_per_sentence":total_comma_count/len(comma_amounts),
        "min_commas_per_sentence":max(comma_amounts),
        "min_commas_per_sentence":min(comma_amounts),
        "word_amount_list":word_amounts,
        "comma_amount_list":comma_amounts,
    }
    # print("Amount of Sentences: ", len(sentences))
    # print("Total word count: ", total_word_count)
    # print("Average word count per sentence: ", total_word_count/len(word_amounts))
    # print("Maximum word count in a sentence: ", max(word_amounts))
    # print("Minimum word count in a sentence: ", min(word_amounts))
    # print()
    # print("Total comma count: ", total_comma_count)
    # print("Average comma count per sentence: ", total_comma_count/len(comma_amounts))
    # print("Maximum comma count in a sentence: ", max(comma_amounts))
    # print("Minimum comma count in a sentence: ", min(comma_amounts))





import uuid, hashlib




def generate_uuid_from_directory(directory, blacklisted_extensions:list=[]):
    """Generate a UUID based on the content of all files in a directory, excluding files with specified extensions.

Args:
    directory (str): Path to the directory to scan.
    blacklisted_extensions (list, optional): List of file extensions to exclude from hashing. Defaults to an empty list.

Returns:
    UUID: A UUID generated from the MD5 hash of the file contents."""
    hash_md5 = hashlib.md5()

    # Traverse all files in the directory
    for root, _, files in os.walk(directory):
        for file in sorted(files):  # Sort files to ensure consistent order
            blacklisted = True
            for ext in blacklisted_extensions:
                if file.endswith(ext):
                    break
            else:
                blacklisted = False
            if blacklisted:
                continue
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):  # Ensure it's a file
                with open(file_path, 'rb') as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
    
    # Generate UUID from the MD5 hash
    unique_hash = hash_md5.hexdigest()
    unique_uuid = uuid.UUID(unique_hash[:32])
    
    return unique_uuid























































































































































def check_for_functions_in_module_with_missing_notations(library_module: ModuleType) -> List[dict]:
    """
    Check all functions in a given library module for missing input type or return type annotations.
    Parameters:
    library_module (module): The library module to analyze.
    Returns:
    list: A list of dictionaries containing information about functions with missing type annotations.
    """
    functions_with_missing_annotations = []

    for name, obj in inspect.getmembers(library_module):
        if isinstance(obj, FunctionType):
            input_parameters = get_function_inputs(obj)
            missing_input_types = [param for param in input_parameters if param['type'] is NoInputType]

            return_type = get_return_type(obj)
            if missing_input_types or return_type is MissingReturnType:
                functions_with_missing_annotations.append({
                    'function_name': name,
                    'missing_input_types': missing_input_types,
                    'return_type': return_type
                })

    return functions_with_missing_annotations

def print_check_for_functions_in_module_with_missing_notations(library_module: ModuleType)->None:
    """Print details of functions in a module that are missing type annotations.

Args:
    library_module (ModuleType): The module to check for missing type annotations.
    
Details:
    Prints each function with missing type annotations, specifying whether the issue is a missing return type or missing input type."""
    data = check_for_functions_in_module_with_missing_notations(library_module)
    for i in data:
        print(f"Function '{i['function_name']}' of type {'Missing Return' if i['function_name'] is MissingReturnType else 'Missing Input type'}")














# class AutocompleteTrie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         current_node = self.root
#         for letter in word:
#             if letter not in current_node.children:
#                 current_node.children[letter] = TrieNode()
#             current_node = current_node.children[letter]
#         current_node.is_end_of_word = True

#     def _find_node(self, prefix):
#         current_node = self.root
#         for letter in prefix:
#             if letter not in current_node.children:
#                 return None
#             current_node = current_node.children[letter]
#         return current_node

#     def _autocomplete_helper(self, node, prefix):
#         words = []
#         if node.is_end_of_word:
#             words.append(prefix)
#         for letter, next_node in node.children.items():
#             words.extend(self._autocomplete_helper(next_node, prefix + letter))
#         return words

#     def autocomplete(self, prefix):
#         current_node = self._find_node(prefix)
#         if not current_node:
#             return []
#         return self._autocomplete_helper(current_node, prefix)

# def autocomplete(word_list):
#     "Apparently this is faster than just checking for the prefix in a list comprehension one-liner"
#     trie = AutocompleteTrie()
#     for word in word_list:
#         trie.insert(word)
#     return trie.autocomplete










def get_function_id_by_name(func_name)->None|ModuleType:
    """
    Retrieve the function object (ID) from its name.

    Parameters:
    func_name (str): The name of the function to retrieve.

    Returns:
    callable or None: The function object if found, None if not found.
    """
    # Check if the function name exists in the global namespace
    if func_name in globals():
        func_obj = globals()[func_name]
        # Ensure the retrieved object is callable (a function or method)
        if callable(func_obj):
            return func_obj
    return None



































class NoInputType:
    """Custom class to indicate that no input type annotation is specified."""
    pass

def get_function_inputs(func:MethodType)->list[dict]:
    """
    Retrieve all input parameters of a given function along with their types and default values.

    Parameters:
    func (callable): The function to analyze.

    Returns:
    list: A list of dictionaries containing {'name': parameter_name, 'type': parameter_type, 'default': default_value}.
    """
    # Get the signature of the function
    signature = inspect.signature(func)
    
    # Get type hints (annotations) for the function parameters
    type_hints = get_type_hints(func)
    
    # Extract parameter names, types, and default values from the signature
    input_parameters = []
    for param_name, param in signature.parameters.items():
        param_type = type_hints.get(param_name, None)
        
        if param.default is not inspect.Parameter.empty:
            default_value = param.default
            
            input_parameters.append({
            'name': param_name,
            'type': param_type,
            'default': default_value
        })
        else:
            input_parameters.append({
            'name': param_name,
            'type': param_type,
            'default':NoInputType
        })
        
        
    
    return input_parameters


class MissingReturnType:
    """Custom class to indicate that no return type annotation is specified."""
    pass



def get_return_type(func:MethodType)->Any:
    """
    Retrieve the return type annotation of a given function.

    Parameters:
    func (callable): The function to analyze.

    Returns:
    type: The return type of the function. Returns `NoReturnType` if no type annotation is specified.
    """
    # Get the signature of the function
    signature = inspect.signature(func)
    
    # Get the return type annotation
    return_type = signature.return_annotation
    
    if return_type == inspect.Signature.empty:
        return MissingReturnType
    else:
        return return_type


























def repeat(func:FunctionType, times:int)->Any:
    for i in range(times):
        val = func()
    return val















































































































def count_functions_in_module(module:ModuleType, library_name:str)->int:
    """Count the number of functions in a module and its submodules.

Args:
    module (ModuleType): The module to analyze.
    library_name (str): The library name to use for identifying submodules.

Returns:
    int: The total number of functions in the module and its submodules.
"""
    function_count = 0
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            function_count += 1
        elif inspect.ismodule(obj) and obj.__package__.startswith(library_name):
            function_count+=count_functions_in_module(obj, library_name)
    return function_count

def count_functions_in_library(library_name:str)->int:
    """Count the number of functions in a library by importing it and analyzing its modules.

Args:
    library_name (str): The name of the library to import and analyze.

Returns:
    int: The total number of functions in the library, or -1 if the library could not be found."""
    try:
        module = importlib.import_module(library_name)
    except ModuleNotFoundError:
        return -1
    function_count = count_functions_in_module(module,library_name)
    
    return function_count





class ArgumentHandler:
    "Handle command-line arguments by allowing retrieval, deletion, and flag-based access."
    def __init__(self, arguments: None | list = None) -> None:
        """Initialize the object with a list of arguments. If no arguments are provided, use command-line arguments excluding the script name.

Args:
    arguments (None | list, optional): A list of arguments. Defaults to None, in which case command-line arguments are used.

Attributes:
    arguments (Iterable): The list of arguments."""
        if arguments is None:
            arguments = sys.argv[1:]
        self.arguments: Iterable = arguments
        self.argument_list_length = len(arguments)

    def get_argument(self, argument: str, delete:bool=False, default:Any=None) -> str | None:
        """Retrieve the value of a specified argument. Optionally remove it from the list and adjust the argument count.

Args:
    argument (str): The argument to retrieve.
    delete (bool, optional): If True, remove the argument from the list after retrieving it. Defaults to False.
    default (Any, optional): The value to return if the argument is not found. Defaults to None.

Returns:
    str | None: The value of the argument, or `default` if the argument is not found."""
        value_id = self.get_id(argument)
        if value_id < 0:
            return default
        
        if delete:
            value = self.arguments.pop(value_id)
            self.argument_list_length-=1
        else:
            value = self.arguments.__getitem__(value_id)
            
        return value
    
    def get_argument_by_flag(self, flag: str, delete:bool=False, default:Any=None) -> str | None:
        """Retrieve the value associated with a specified flag. Optionally remove the flag and its value from the list and adjust the argument count.

Args:
    flag (str): The flag to retrieve the value for.
    delete (bool, optional): If True, remove the flag and its value from the list after retrieving it. Defaults to False.
    default (Any, optional): The value to return if the flag or its value is not found. Defaults to None.

Returns:
    str | None: The value associated with the flag, or `default` if the flag or value is not found."""
        value_id = self.get_id(flag)
        if value_id < 0:
            return default
        if value_id+1 == len(self.arguments): # We're outside the list, abort!
            return default
        
        if delete:
            self.arguments.pop(value_id)
            value = self.arguments.pop(value_id)
            self.argument_list_length-=2
        
        else:
            value = self.arguments.__getitem__(value_id+1)
        return value
    
    def get_id(self, item:str)->int:
        """Retrieve the index of a specified item in the arguments list.

Args:
    item (str): The item to find in the arguments list.

Returns:
    int: The index of the item if found, or -1 if the item is not in the list."""
        if not item in self.arguments:
            return -1
        
        
        value_id = self.arguments.index(item)
        
        return value_id

    def is_empty(self)->bool:
        """Check if the arguments list is empty.

Returns:
    bool: True if the arguments list is empty, otherwise False."""
        return self.argument_list_length == 0
    













































def print_undocumented_functions_in_directory(directory:str=os.path.dirname(__file__))->int:
    """Print undocumented functions in all Python files within a directory and its subdirectories.

Args:
    directory (str, optional): Path to the directory to scan. Defaults to the directory of the current file.

Returns:
    int: The total number of undocumented functions found."""
    undocumented = check_directory_and_sub_directory_for_undocumented_functions(directory)

    amount = 0
    for i in undocumented:
        print("\n\n"+i)
        for j in undocumented[i]:
            amount += 1
            print(f'\n\t{j[0]} \n\tFile "{directory}\\{i}", line {j[1]}')
    return amount























































def get_from_dict_by_list(data_dict:dict, keys:Iterable)->Any:
    """
    Access a nested dictionary with a list of keys.
    
    :param data_dict: Dictionary to access.
    :param keys: List of keys to access the dictionary.
    :return: Value from the dictionary.
    """
    for key in keys:
        data_dict = data_dict[key]
    return data_dict

def set_in_dict_by_list(data_dict:dict, keys:Iterable, value:Any)->None:
    """
    Set a value in a nested dictionary with a list of keys.
    
    :param data_dict: Dictionary to set the value in.
    :param keys: List of keys to access the dictionary.
    :param value: Value to set in the dictionary.
    """
    for key in keys[:-1]:
        data_dict = data_dict.setdefault(key, {})
    data_dict[keys[-1]] = value




























































from collections import defaultdict


class TrieNode:
    def __init__(self):
        "Node in a Trie data structure with a dictionary of child nodes and a boolean flag to mark the end of a path."
        self.children = defaultdict(TrieNode)
        self.is_end_of_path = False

def _insert_path(root:TrieNode, path:Iterable)->None:
    "Insert a path into a Trie data structure."
    node = root
    for part in path:
        node = node.children[part]
    node.is_end_of_path = True

def _build_trie(paths:Iterable)->TrieNode:
    "Build a Trie from a list of file paths."
    root = TrieNode()
    for path in paths:
        _insert_path(root, path.split('/'))
    return root

def _serialize_trie(node:TrieNode)->dict:
    "Serialize a Trie into a compressed dictionary format representing a directory structure."
    if not node.children:
        return []

    if len(node.children) == 1 and node.is_end_of_path == False:
        key, child = next(iter(node.children.items()))
        serialized_child = _serialize_trie(child)
        if isinstance(serialized_child, list) and not serialized_child:
            return key
        if isinstance(serialized_child, str):
            return f"{key}/{serialized_child}"
        return {key: serialized_child}

    result = {}
    for key, child in node.children.items():
        serialized_child = _serialize_trie(child)
        if isinstance(serialized_child, list) and not serialized_child:
            result.setdefault('files', []).append(key)
        else:
            result[key] = serialized_child

    return result

def compress_directory_list(paths:Iterable)->dict[list|str]:
    "Compress a list of file paths into a dictionary format representing the directory structure."
    trie = _build_trie(paths)
    compressed = _serialize_trie(trie)
    return compressed








def decompress_directory_list(compressed:dict)->list[str]:
    """Decompress a directory structure from a nested dictionary format into a list of file paths.

Args:
    compressed (dict): The compressed directory structure in dictionary format.

Returns:
    list[str]: A list of file paths extracted from the compressed structure."""
    paths = []

    def dfs(node:str|list|dict, current_path=""):
        "Inner loop"
        if isinstance(node, list):
            paths.append(f"{current_path}/{node[0]}".strip('/'))
            return
        if isinstance(node, str):
            paths.append(node)
            return

        for key, value in node.items():
            if key == 'files':
                for file_path in value:
                    paths.append(f"{current_path}/{file_path}".strip('/'))
            else:
                dfs(value, f"{current_path}/{key}".strip('/'))

    dfs(compressed)
    return paths


import python_minifier

def minify(text:str, rename_important_names:bool=False,remove_docstrings:bool=True)->str:
    """Minify Python code by optionally renaming important names and removing docstrings.

Args:
    text (str): The Python code to minify.
    rename_important_names (bool, optional): Whether to rename important names (variables, functions) to shorter names. Defaults to False.
    remove_docstrings (bool, optional): Whether to remove docstrings from the code. Defaults to True.

Returns:
    str: The minified Python code."""
    return python_minifier.minify(text, rename_globals=rename_important_names, remove_literal_statements=remove_docstrings)



    











# Old way to check if a library exist. Very inefficient. Don't use.
# def test_for_library(library_name) -> bool:
#     if library_name in IGNORE_LIBRARIES:
#         return False
#     try:
#         start_importing = tm.time()
#         __import__(library_name)
#         import_times[library_name] = tm.time() - start_importing
#         installed_libraries.append(library_name)
#         del library_name
#         return True
#     except ModuleNotFoundError:
#         missing_libraries.append(library_name)
#         return False
#     except ImportError:
#         error_libraries.append(library_name)
#         return False














# types = {}

# def create_type(name: str, weak_against_type: Iterable, strong_against_type: Iterable, against_self: int):
#     name = name.lower()
#     weak_against_type = [weak.lower() for weak in weak_against_type]
#     strong_against_type = [strong.lower() for strong in strong_against_type]
    
#     strengths = []
#     weaknesses = []
    
#     for other_type, other_stats in items():
#         if name in other_stats["weak_against_type"]:
#             strengths.append(other_type)
#         if name in other_stats["strong_against_type"]:
#             weaknesses.append(other_type)
    
#     strengths.extend(strong_against_type)
#     weaknesses.extend(weak_against_type)
    
#     types[name] = {
#         "weak_against_type": weak_against_type,
#         "strong_against_type": strong_against_type,
#         "self": against_self,
#         "strengths": Iterable(set(strengths)),
#         "weaknesses": Iterable(set(weaknesses))
#     }




# def print_type_stats(input_type: str):
#     if input_type != "":
#         type_stats = get(input_type.lower())
#         if type_stats:
#             print_type_info(input_type, type_stats)
#     else:
#         for type_name, type_stats in items():
#             print_type_info(type_name, type_stats)
#             print()

# def print_type_info(type_name: str, type_stats: dict):
#     print(type_name.title() + ":")
#     print("\t•Weak against:")
#     weak_against_type = type_stats["weak_against_type"]
#     print_type_attributes(weak_against_type)
    
#     print("\n\t•Strong against:")
#     strong_against_type = type_stats["strong_against_type"]
#     print_type_attributes(strong_against_type)
    
#     print("\n")
#     print_type_damage_to_self(type_stats["self"])


# def print_type_attributes(attributes: Iterable):
#     for attribute in attributes:
#         print("\t\t" + attribute.title())

# def print_type_damage_to_self(damage_value: int):
#     if damage_value == 0:
#         print("\t•Deals normal damage to its own type")
#     elif damage_value == 1:
#         print("\t•Deals strong damage to its own type")
#     elif damage_value == 2:
#         print("\t•Deals weak damage to its own type")
#     elif damage_value == 3:
#         print("\t•Is immune to its own type")

# def get_weaknesses(type_name: str):
#     weaknesses = []
#     for other_type, other_stats in items():
#         if type_name.lower() in other_stats["strong_against_type"]:
#             weaknesses.append(other_type)
#     return weaknesses

# def get_strengths(type_name: str):
#     strengths = []
#     for other_type, other_stats in items():
#         if type_name.lower() in other_stats["weak_against_type"]:
#             strengths.append(other_type)
#     return strengths

# def missing_types(type_name: str):
#     all_types = []
#     if type_name == "":
#         for m_type in types:
#             for strong in types[m_type]["strong_against_type"]:
#                 if strong not in all_types:
#                     all_append(strong)
#             for weak in types[m_type]["weak_against_type"]:
#                 if weak not in all_types:
#                     all_append(weak)

#         print("Missing types:")
        
#         for check_type in all_types:
#             if check_type not in types and check_type != "":
#                 print(check_type.title())

# create_type("ice", ["lava", ""], ["fire"], 2)
# create_type("wood", ["lava","magma", "fire"], ["earth"], 0)
# create_type("wind", ["stone", "earth"], ["water"], 3)
# create_type("fire", ["stone"], ["wood"], 0)
# create_type("water", ["magma", "lava", "ice"], ["fire", "stone"], 2)
# create_type("rock", ["magma"], [""], 1)
# create_type("grass", ["fire", "lava", "magma", "rock"], ["earth"], 0)
# create_type("stone", ["water"], ["wind"], 0)
# create_type("magma", ["fire"], [""], 0)

# print_type_stats("")
# missing_types("")

# def newEnemy(name: str, entity_type: str, health: int, attack: int, defense: int, speed: int, resistant: Iterable, weakness: Iterable, behavior: int, loot: Iterable):
#     if type(weakness) != list:
#         try:
#             weakness = list(weakness)
#         except: return False, "Weakness must be lists or strings"
#     if not type(resistant) != list:
#         try:
#             resistant = list(resistant)
#         except: return False, "Resistance must be lists or strings"

#     if not type(resistant) == list:
#         return False, "Resistance must be a list"
#     elif not type(weakness) == list:
#         return False, "Weakness must be a list"

#     if not name in enemies:
#         if name != "":
#             if entity_type != "":
#                 if health > 0:
#                     if attack >= 0:
#                         if defense >= 0:
#                             if behavior >= 0:
#                                 enemies[name] = {"health": health, "type": entity_type, "attack": attack, "defense": defense, "speed": speed, "resistance": resistant, "weakness": weakness, "behavior": behavior, "loot": loot}
#                                 return True, "Enemy created"
#                             else: return False, "Behavior must be greater or equal to 0"
#                         else: return False, "Defense must be greater or equal to 0"
#                     else: return False, "Attack must be greater or equal to 0"
#                 else: return False, "Health must be greater than 0"
#             else: return False, "Entity type cannot be empty"
#         else: return False, "Name cannot be empty"
#     else: return False, "Enemy already exists"


#def doesEnemyExist(name: str):
#    return name in enemies


#def attackEnemy(name: str, damage: int, type):
#    x = enemies.items()
#    damage = damage-enemies[name]["resistance"]
#    if damage <= 0: 
#        damage = 0
#    
#    if name in enemies:
#        enemies[name] = {**enemies[name], "health": enemies[name]["health"] - damage, "type": type}
#    else: return False, "Enemy does not exist"

#def newAttackType(name, weakness):
#    AttackTypes[name]



#initSession()
#newEnemy("test", 10, 10, 10, 10, 10, 10, 10, 10, [])
#x, y = newEnemy("test2", 10, 10, 10, 10, ["hi"], ["no"], 10, 10, ["stuff"])
#print(x)
#print(y)
#newEnemy("test2", 10, 10, 10, 10, 10, 10, 10, 10, [])
#print(doesEnemyExist("test"))
#attackEnemy("test", 10, "test")

#print(enemies)


