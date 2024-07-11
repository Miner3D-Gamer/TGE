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




from typing import List, Union, Tuple , Any, get_type_hints
import types
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

def categorize_responses(text_list: List[str]) -> List[str]:
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
        
        >>> number_to_words(0)
        'zero'
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
    undocumented_functions = []

    with open(file_path, 'r', encoding="utf8") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                undocumented_functions.append([node.name,node.end_lineno])

    return undocumented_functions

def check_directory_for_undocumented_functions(directory_path:str)->dict:
    undocumented_functions_dict = {}

    for filename in os.listdir(directory_path):
        if filename.endswith('.py'):
            file_path = os.path.join(directory_path, filename)
            undocumented_functions = find_undocumented_functions(file_path)
            if undocumented_functions:
                undocumented_functions_dict[filename] = undocumented_functions

    return undocumented_functions_dict

def check_directory_and_sub_directory_for_undocumented_functions(directory_path:str)->dict:
    undocumented_functions_dict = {}

    def _check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(current_path:str)->None:
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



def autocomplete(prefix:str, word_list:list[str])->list[str]:
    return [word for word in word_list if word.startswith(prefix)]


def is_iterable(thing:Any)->True|False:
    return hasattr(thing,"__iter__")



def split_with_list(string: str, separators: list|tuple, limit: None | int = None) -> list[str]:
    for separator in separators:
        string = string.replace(separator, "𘚟")
    return string.split("𘚟")



def analyze_text(text:str)->dict[str:str|list]:
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


































































































































































def check_library_functions(library_module: types.ModuleType) -> List[dict]:
    """
    Check all functions in a given library module for missing input type or return type annotations.
    Parameters:
    library_module (module): The library module to analyze.
    Returns:
    list: A list of dictionaries containing information about functions with missing type annotations.
    """
    functions_with_missing_annotations = []

    for name, obj in inspect.getmembers(library_module):
        if isinstance(obj, types.FunctionType):
            input_parameters = get_function_inputs(obj)
            missing_input_types = [param for param in input_parameters if param['type'] is NoInputType]

            return_type = get_return_type(obj)
            if missing_input_types or return_type is NoReturnType:
                functions_with_missing_annotations.append({
                    'function_name': name,
                    'missing_input_types': missing_input_types,
                    'return_type': return_type
                })

    return functions_with_missing_annotations



























def get_function_id_by_name(func_name:str)->None|types.ModuleType:
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

def get_function_inputs(func:types.MethodType)->list[dict]:
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


class NoReturnType:
    """Custom class to indicate that no return type annotation is specified."""
    pass



def get_return_type(func:types.MethodType)->Any:
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
        return NoReturnType
    else:
        return return_type











































































































































def count_functions_in_module(module:types.ModuleType, library_name:str)->int:
    function_count = 0
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            function_count += 1
        elif inspect.ismodule(obj) and obj.__package__.startswith(library_name):
            function_count+=count_functions_in_module(obj, library_name)
    return function_count

def count_functions_in_library(library_name:str)->int:
    try:
        module = importlib.import_module(library_name)
    except ModuleNotFoundError:
        return -1
    function_count = count_functions_in_module(module,library_name)
    
    return function_count





class ArgumentHandler:
    def __init__(self, arguments: None | list = None) -> None:
        if arguments is None:
            arguments = sys.argv[1:]
        self.arguments: list = arguments
        self.argument_list_length = len(arguments)

    def get_argument(self, argument: str, delete:bool=False, default:Any=None) -> str | None:
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
        if not item in self.arguments:
            return -1
        
        
        value_id = self.arguments.index(item)
        
        return value_id

    def is_empty(self)->bool:
        return self.argument_list_length == 0
    














































def print_undocumented_functions_in_directory(directory:str=os.path.dirname(__file__)):
    undocumented = check_directory_and_sub_directory_for_undocumented_functions(directory)

    amount = 0
    for i in undocumented:
        print("\n"+i)
        for j in undocumented[i]:
            amount += 1
            print(f'\t{j[0]} ("{directory}/{i}", line {j[1]})')
    print("\nA total of %s functions are undocumented"%amount)





















































































































































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

# def create_type(name: str, weak_against_type: list, strong_against_type: list, against_self: int):
#     name = name.lower()
#     weak_against_type = [weak.lower() for weak in weak_against_type]
#     strong_against_type = [strong.lower() for strong in strong_against_type]
    
#     strengths = []
#     weaknesses = []
    
#     for other_type, other_stats in types.items():
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
#         type_stats = types.get(input_type.lower())
#         if type_stats:
#             print_type_info(input_type, type_stats)
#     else:
#         for type_name, type_stats in types.items():
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
#     for other_type, other_stats in types.items():
#         if type_name.lower() in other_stats["strong_against_type"]:
#             weaknesses.append(other_type)
#     return weaknesses

# def get_strengths(type_name: str):
#     strengths = []
#     for other_type, other_stats in types.items():
#         if type_name.lower() in other_stats["weak_against_type"]:
#             strengths.append(other_type)
#     return strengths

# def missing_types(type_name: str):
#     all_types = []
#     if type_name == "":
#         for m_type in types:
#             for strong in types[m_type]["strong_against_type"]:
#                 if strong not in all_types:
#                     all_types.append(strong)
#             for weak in types[m_type]["weak_against_type"]:
#                 if weak not in all_types:
#                     all_types.append(weak)

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

