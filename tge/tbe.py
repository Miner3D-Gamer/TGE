# TODO: The original tge file with every single function in one big mess before splitting them across multiple files
# TODO: What a true beauty of random comments, miscellaneous code, and unfinished/discarded functions
# TODO: Anyways, what are you doing here? Idk why you would be here but hi :<



# from time import sleep, timezone
# from os import system as os_system, path as os_path, environ, makedirs as os_createDirectory, listdir as os_listdir, getcwd as os_getcwd, rename as os_rename, remove as os_remove; environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# from sys import stdout as sys_stdout


#from pytz import timezone as pytz_timezone
#from math import sqrt, log, log2, modf, ceil, floor, factorial





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



from typing import List, Union, Tuple, Any, Iterator, Dict, Callable, Optional
import ast
import os
import sys
from difflib import get_close_matches
import getpass
from typing import Union
import cProfile
import pstats
import io
import subprocess, tempfile

version = sys.version_info


__all__ = [
    "pass_func",
    "execute_function","determine_affirmative","get_available_variables","number_to_words","letter_to_number","number_to_letter","find_undocumented_functions","check_directory_for_undocumented_functions","check_directory_and_sub_directory_for_undocumented_functions","autocomplete","strict_autocomplete","is_iterable","split_with_list","analyze_text","divide","DualInfinite","generate_every_capitalization_states","remove_unused_libraries","repeat","get_username","profile","profile_function","get_current_pip_path","ArgumentHandler","HashMap","print_undocumented_functions_in_directory","minify","compress_imports_in_code"
]




def pass_func(*args: Any, **more_args:Any) -> None: 
    """This function does nothing and has no side effects."""
    pass




def execute_function(func:Callable[...,Any]=pass_func, *args: Any, **kwargs: Any) -> Any:
    """
    Executes a function with the given arguments and keyword arguments.

    Parameters:
        func (callable): The function to be executed. Defaults to 'pass_func'.
        *args (Any): Variable length arguments to be passed to the function.
        **kwargs (Any): Keyword arguments to be passed to the function.

    Returns:
        Any: The result of executing the function.

    """
    return func(*args, **kwargs)









def determine_affirmative(text: str) -> Optional[bool]:
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


def get_available_variables() -> Dict[str, Any]:
    """
    Retrieve and return the available global and local variables in the current scope.

    This function gathers both global and local variables, storing them in separate dictionaries.
    It collects global variables using the `globals()` function and local variables using the `locals()` function.
    The resulting dictionaries contain variable names as keys and their corresponding values as values.

    Returns:
        Tuple[Dict[str, Any], Dict[str, Any]]: A tuple containing two dictionaries.
        The first dictionary holds global variables, and the second dictionary holds local variables.
    """
    g_variables: Dict[str, Any] = {}
    # Retrieve global variables
    global_vars = globals()
    for var_name, var_value in global_vars.items():
        g_variables[var_name] = var_value


    return g_variables





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








def _convert_number_to_words_less_than_thousand(n:int, dash:bool = True) -> str:
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
                result += " and " + _convert_number_to_words_less_than_thousand(rest)
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
    groups: List[int] = []
    while number > 0:
        groups.append(number % 1000)
        number //= 1000
    
    
    result_parts: List[str] = []
    for i, group in enumerate(groups):
        if group != 0:
            result_parts.append(_convert_number_to_words_less_than_thousand(group) + " " + big_numbers[i])
    
    # Join the parts and return the final result
    return ", ".join(reversed(result_parts))




def letter_to_number(letter:str)->int:
    """
    Converts a string of letters to a corresponding integer based on a base-26 system.

    Parameters:
    letter (str): The input string of letters (e.g., 'A', 'B', 'AA').

    Returns:
    int: The corresponding integer value of the input string. 
         For example, 'A' returns 0, 'B' returns 1, 'Z' returns 25, and 'AA' returns 26.
    """
    number = 0
    for char in letter:
        number = number * 26 + (ord(char.lower()) - ord('a')) + 1
    return number - 1

def number_to_letter(number:int)->str:
    """
    Converts an integer to a string of letters based on a base-26 system.

    Parameters:
    number (int): The input integer value (e.g., 0 for 'A', 1 for 'B', 25 for 'Z').

    Returns:
    str: The corresponding string of letters. 
         For example, 0 returns 'A', 1 returns 'B', 25 returns 'Z', and 26 returns 'AA'.
    """
    letters = ""
    while number >= 0:
        letters = chr((number % 26) + ord('A')) + letters
        number = number // 26 - 1
        if number < 0:
            break
    return letters





def find_undocumented_functions(file_path:str)->List[List[Union[str, Optional[int]]]]:
    """Find all functions without docstrings in a Python file.

Args:
    file_path (str): Path to the Python file to scan.

Returns:
    list: A list of undocumented functions, each represented as a list with the function name and its end line number."""
    undocumented_functions:List[List[Union[str, Optional[int]]]] = []

    with open(file_path, 'r', encoding="utf8") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                undocumented_functions.append([node.name,node.end_lineno])

    return undocumented_functions

def check_directory_for_undocumented_functions(directory_path:str)->Dict[str, List[List[Union[str, Optional[int]]]]]:
    """Check a directory for Python files and find undocumented functions in each file.

Args:
    directory_path (str): Path to the directory to scan.

Returns:
    dict: A dictionary where keys are filenames and values are lists of undocumented functions, each represented as a list with the function name and its end line number."""
    undocumented_functions_dict:Dict[str, List[List[Union[str, Optional[int]]]]] = {}

    for filename in os.listdir(directory_path):
        if filename.endswith('.py'):
            file_path = os.path.join(directory_path, filename)
            undocumented_functions = find_undocumented_functions(file_path)
            if undocumented_functions:
                undocumented_functions_dict[filename] = undocumented_functions

    return undocumented_functions_dict

def check_directory_and_sub_directory_for_undocumented_functions(directory_path:str)->Dict[str, List[List[Union[str, Optional[int]]]]]:
    """Check a directory and its subdirectories for Python files and find undocumented functions in each file.

Args:
    directory_path (str): Path to the directory to scan.

Returns:
    dict: A dictionary where keys are relative file paths and values are lists of undocumented functions, each represented as a list with the function name and its end line number."""
    undocumented_functions_dict:Dict[str, List[List[Union[str, Optional[int]]]]] = {}

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





from typing import List
def get_surface_defined_names(file_path: str) -> List[str]:
    """Get all surface-defined names in a Python file.
    Surface-defined names are defined as top-level functions and classes that don't start with an underscore (_).
    Args:
        file_path (str): Path to the Python file to scan.
    Returns:
        list: A list of surface-defined names, each represented as a string."""
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    # Get all function names at the top level that don't start with "_"
    function_names = [
        node.name for node in tree.body 
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith('_')
    ]
    
    return function_names





# def download_multiple_videos(video_dict, save_path):
#     video_infos = [(url_id, save_path, file_name) for url_id, file_name in video_dict.items()]
    
#     with Pool() as pool:
#         results = pool.map(download_youtube_video, video_infos)
    
#     return results



def autocomplete(prefix: str, word_list: List[str]) -> List[str]:
    """Return a list of words from `word_list` that start with the specified `prefix`.

Args:
    prefix (str): The prefix to match against.
    word_list (list[str]): A list of words to search through.

Returns:
    list[str]: A list of matching words."""
    return [word for word in word_list if word.startswith(prefix)]

def strict_autocomplete(prefix:str, word_list:List[str])->Union[List[str], str]:
    """Return a single word, the prefix itself, or a list of words that start with the specified `prefix`.

Args:
    prefix (str): The prefix to match against.
    word_list ("list[str]"): A list of words to search through.

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



def split_with_list(string: str, separators: List[str], limit: Union[None, int] = None) -> List[str]:
    """Split a string by multiple separators and return the resulting substrings.

Args:
    string (str): The string to split.
    separators (list): A list of separators to replace with a unique delimiter.
    

Returns:
    list[str]: A list of substrings resulting from the split operation."""
    d = 0
    for separator in separators:
        string = string.replace(separator, "𘚟")
        d+=1
        if limit is not None and d >= limit:
            break
    return string.split("𘚟")



def analyze_text(text:str)->Dict[str, Union[str,List[int],float]]:
    """Analyze the text to provide various statistics about sentences, words, and commas.

Args:
    text (str): The text to analyze.

Returns:
    dict[str, str  list]: A dictionary with the following keys:
        - "sentence_amount": Union[int,float] of sentences.
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

    sentences:List[List[str]] = []
    word_amounts:List[int] = []
    comma_amounts:List[int] = []

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


































































































































































    
























class DualInfinite:
    """A value that is both positively and negatively infinite, not as range but as literal value"""


def divide(a:Union[int,float], b:Union[int,float])->Union[float,DualInfinite]:
    """
    Divides two numbers and handles division by zero.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        Union[float, DualInfinite]: The result of the division if b != 0, otherwise an instance of DualInfinite.
    """
    return a/b if b!=0 else DualInfinite()


















def generate_every_capitalization_states(s:str)->List[str]:
    """
    Generates all possible capitalization combinations of a given string.

    Parameters:
    s (str): The input string for which to generate capitalization states.

    Returns:
    List[str]: A list of all unique capitalization combinations of the input string.

    This function uses a backtracking approach to explore every possible way to capitalize 
    the letters in the input string, including all lowercase and uppercase variations.
    
    Example: 
        > generate_every_capitalization_state('png')
        > ['PNg', 'pNG', 'png', 'pnG', 'PnG', 'PNG', 'pNg', 'Png']
    """
    def backtrack(index:int, path:List[str])->None:
        """
        Recursively generates all possible capitalization combinations of a given string.
        """
        if index == len(s):
            result.append(''.join(path))
            return
        backtrack(index + 1, path + [s[index].lower()])
        backtrack(index + 1, path + [s[index].upper()])

    result:List[str] = []
    backtrack(0, [])
    return list(set(result))
















def remove_unused_libraries(code_str:str)->str:
    """Remove unused variables from code using autoflake."""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
        temp_file.write(code_str.encode('utf-8'))
        temp_file_path = temp_file.name

    try:
        command = ['autoflake', '--in-place', '--remove-unused-variables', temp_file_path]
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise RuntimeError(f'Error running autoflake: {result.stderr}')
        
        with open(temp_file_path, 'r', encoding="utf8") as temp_file:
            cleaned_code = temp_file.read()

        return cleaned_code

    finally:
        os.remove(temp_file_path)














def repeat(times: int, func: Callable[...,Any], *args: Any, **kwargs: Any) -> Any:
    """Call func multiple times and return the last result."""
    val = None
    for _ in range(times):
        val = func(*args, **kwargs)
    return val

def get_username() -> str:
    """Return the current system username."""
    return getpass.getuser()


















































































def profile(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that profiles the execution time of a function.

    This decorator uses the cProfile module to profile the function's 
    execution. It captures and prints the profiling statistics, sorted 
    by cumulative time, to standard output.

    Args:
        func (function): The function to be profiled.

    Returns:
        function: The wrapped function with profiling enabled.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        "The profile wrapper"
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()

        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

        return result

    return wrapper









def profile_function(function:Callable[...,Any], filename:str, *inputs:Any, **extra:Any)->Any:
    """Profile a function and save performance stats to files."""



    profile = cProfile.Profile()
    profile.enable()

    return_ = function(*inputs, **extra)

    profile.disable()


    profile_filename = f'{filename}.pstats'
    profile.dump_stats(profile_filename)
    stats = pstats.Stats(profile_filename)

    with open(f'{filename}.txt', 'w') as f:
        stats = pstats.Stats(profile_filename, stream=f)
        stats.sort_stats("cumulative")
        stats.print_stats()
    
    return return_







if os.name == 'nt':
    def get_current_pip_path():
        """
        Get the path to the current pip executable on Windows.
        """
        python_executable = sys.executable
        if os.name == 'nt':
            pip_path = os.path.join(os.path.dirname(python_executable), 'Scripts', 'pip.exe')
        
        if os.path.isfile(pip_path):
            return pip_path
        else:
            return None
else:
    def get_current_pip_path():
        """
        Get the path to the current pip executable on non-Windows platforms.
        """
        python_executable = sys.executable
        pip_path = os.path.join(os.path.dirname(python_executable), 'bin', 'pip')
        
        if os.path.isfile(pip_path):
            return pip_path
        else:
            return None




class ArgumentHandler:
    "Handle command-line arguments by allowing retrieval, deletion, and flag-based access."
    def __init__(self, arguments: Union[None , List[str]] = None) -> None:
        """Initialize the object with a list of arguments. If no arguments are provided, use command-line arguments excluding the script name.

Args:
    arguments (Union[None , list], optional): A list of arguments. Defaults to None, in which case command-line arguments are used.

Attributes:
    arguments (list): The list of arguments."""
        if arguments is None:
            arguments = sys.argv[1:]
        self.arguments = arguments
        self.argument_list_length = len(arguments)

    def has_argument(self, argument: str, delete:bool=False) -> bool:
        """Check if the argument list contains the specified argument. Optionally remove the argument from the list and adjust the argument count.

Args:
    argument (str): The argument to check for.
    delete (bool, optional): If True, remove the argument from the list after checking. Defaults to False.

Returns:
    str  None: The value associated with the argument, or `None` if the argument is not found."""
        value_id = self.get_id(argument)
        if value_id < 0:
            return False
        
        if delete:
            self.arguments.pop(value_id)
            self.argument_list_length-=1
            
        return True
    
    def get_argument_by_flag(self, flag: str, delete:bool=False, default:Any=None) -> Union[str , None]:
        """Retrieve the value associated with a specified flag. Optionally remove the flag and its value from the list and adjust the argument count.

        Args:
            flag (str): The flag to retrieve the value for.
            delete (bool, optional): If True, remove the flag and its value from the list after retrieving it. Defaults to False.
            default (Any, optional): The value to return if the flag or its value is not found. Defaults to None.

        Returns:
        str  None: The value associated with the flag, or `default` if the flag or value is not found."""
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
    













class HashMap:
    "A Custom Hashmap"
    def __init__(self, *items: Any) -> None:
        """Initialize with items."""
        self.map: List[Any] = list(items)

    def append(self, value: Any) -> None:
        """Add value if not present."""
        if value not in self.map:
            self.map.append(value)

    def extend(self, values: List[Any]) -> None:
        """Add multiple values if not present."""
        for value in values:
            if value not in self.map:
                self.map.append(value)

    def pop(self, index: int) -> Any:
        """Remove and return item at index."""
        return self.map.pop(index)

    def remove(self, value: Any) -> None:
        """Remove the first occurrence of value."""
        self.map.remove(value)

    def index(self, value: Any) -> int:
        """Return index of value."""
        return self.map.index(value)

    def __getitem__(self, index: int) -> Any:
        """Get item at index."""
        return self.map[index]

    def clear(self) -> None:
        """Remove all items."""
        self.map.clear()

    def __iter__(self) -> Iterator[Any]:
        """Return an iterator."""
        return iter(self.map)

    def __repr__(self) -> str:
        """Return string representation."""
        return str(self.map)

    def __contains__(self, item: Any) -> bool:
        """Check if item is present."""
        return item in self.map



























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































































































































if version.minor < 12:
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
else:
    def minify(text:str, rename_important_names:bool=False,remove_docstrings:bool=True)->str:
        """'python_minifier' isn't installed, the text will 1 to 1 be returned"""
        return text



    











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



#from .manipulation.list_utils import zipper_insert


def _separate_imports(lines: List[str]) -> Tuple[List[str], List[str]]:
    """Separate imports from other lines."""
    import_lines: List[str] = []
    other_lines: List[str] = []
    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith("import ") or stripped_line.startswith("from "):
            if not line.startswith(" "):
                import_lines.append(line)
            else:
                other_lines.append(line)
        else:
            other_lines.append(line)

    return import_lines, other_lines


def _compress_imports(import_lines: List[str]) -> List[str]:
    """Compress imports."""
    from_imports: List[str] = []
    import_imports: List[str] = []

    for line in import_lines:
        line = line.strip()

        if line.startswith("from "):
            from_imports.append(line)
        elif line.startswith("import "):
            import_imports.extend(line.replace("import ", "").split(","))

    import_imports = sorted(set(import_imports))
    compressed_import_line = f"import {','.join(import_imports)}"
    output_lines = from_imports + ([compressed_import_line] if import_imports else [])
    return output_lines


def compress_imports_in_code(code: List[str]) -> List[str]:
    """Compress imports in code."""
    imports, rest = _separate_imports(code)
    imports = _compress_imports(imports)
    return imports + rest







# types = {}

# def create_type(name: str, weak_against_type: list, strong_against_type: list, against_self: int):
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
#         "strengths": list(set(strengths)),
#         "weaknesses": list(set(weaknesses))
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


# def print_type_attributes(attributes: list):
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

# def newEnemy(name: str, entity_type: str, health: int, attack: int, defense: int, speed: int, resistant: list, weakness: list, behavior: int, loot: list):
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


