# from typing import Callable
# import itertools
# import inspect

# def generate_truth_table(func: Callable[..., bool]) -> None:
#     # Get function parameters
#     params = inspect.signature(func).parameters
    
#     # Extract parameter names
#     param_names = list(params.keys())
#     max_name_length = max(len(param) for param in param_names)
    
#     # Generate all possible combinations of True and False for the parameters
#     input_combinations = list(itertools.product([True, False], repeat=len(param_names)))
    
#     # Print header
#     header = "│ " + " │ ".join(param.ljust(max_name_length) for param in param_names + ["out"]) + " │"
#     print("┌" + "─" * (len(header) - 2) + "┐")
#     print(header)
#     print("├" + "─" * (len(header) - 2) + "┤")
    
#     # Evaluate the function for each input combination
#     for inputs in input_combinations:
#         result = func(*inputs)
#         print(result)
    
#     # Print footer
#     print("└" + "─" * (len(header) - 2) + "┘")

# def and_three(a: bool, hi: bool, c: bool) -> bool:
#     """
#     Returns the logical AND of three boolean values.

#     Given three boolean inputs, `a`, `b`, and `c`, this function calculates
#     their logical AND result and returns the output.

#     # ┌─────┬─────┬─────┬─────┐
#     # │  a  │  b  │  c  │ out │
#     # ├─────┼─────┼─────┼─────┤
#     # │  0  │  0  │  0  │  0  │
#     # │  0  │  0  │  1  │  0  │
#     # │  0  │  1  │  0  │  0  │
#     # │  0  │  1  │  1  │  0  │
#     # │  1  │  0  │  0  │  0  │
#     # │  1  │  0  │  1  │  0  │
#     # │  1  │  1  │  0  │  0  │
#     # │  1  │  1  │  1  │  1  │
#     # └─────┴─────┴─────┴─────┘
#     """
#     return a and hi and c

# generate_truth_table(and_three)



# Get import time of tge
# import os, sys, time


# sys.path.append(os.path.dirname(os.getcwd()))
# import tge # type: ignore
# print(tge.INIT_TIME)
# # tge.system_interactions.clipboard_operations.append_to_clipboard(str) -> None

# def get_all_folders(directory):
#     folders = []
#     try:
#         for root, dirs, files in os.walk(directory):
#             for dir_name in dirs:
#                 folders.append(os.path.join(root, dir_name))
#     except FileNotFoundError:
#         print(f"The directory '{directory}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access the directory '{directory}'.")
    
#     return folders

# def get_all_files(directory):
#     files_list = []
#     try:
#         for root, dirs, files in os.walk(directory):
#             for file_name in files:
#                 # Append the full path of the file to the list
#                 files_list.append(os.path.join(root, file_name))
#     except FileNotFoundError:
#         print(f"The directory '{directory}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access the directory '{directory}'.")
    
#     return files_list




# f = get_all_files('./tge')
# f = [s for s in f if not s.endswith(".pyc")]

# [print(s) for s in f]
# print(len([print(s) for s in f if s.endswith(".py")]))
# print(tge.platform_mini.system())
# import inspect
# import pkgutil
# import importlib

# def full_function_paths(module):
#     def get_functions_with_paths(module):
#         functions = inspect.getmembers(module, inspect.isfunction)
#         function_paths = []
#         for name, func in functions:
#             if func.__module__ == module.__name__:
#                 sig = inspect.signature(func)
#                 parameters = [
#                     f"{param_name}:{param.annotation.__name__}" if param.annotation != inspect.Parameter.empty else param_name
#                     for param_name, param in sig.parameters.items()
#                 ]
#                 parameters_str = ", ".join(parameters)
                
#                 return_annotation = sig.return_annotation
                
#                 if return_annotation == inspect.Signature.empty:
#                     return_annotation = 'None'
#                 else:
#                     return_annotation = return_annotation.__name__

#                 function_paths.append(f"{func.__module__}.{name}({parameters_str}) -> {return_annotation}")
#         return function_paths

#     for func_path in get_functions_with_paths(module):
#         print(func_path)

#     for submodule_info in pkgutil.walk_packages(module.__path__, module.__name__ + "."):
#         submodule = importlib.import_module(submodule_info.name)
#         for func_path in get_functions_with_paths(submodule):
#             print(func_path)

# full_function_paths(tge)

# while True:
    
    
#     if tge.keyboard.is_key_pressed(tge.keyboard.keys.right_shift):
#         print(tge.clipboard.get_clipboard())
#         tge.clipboard.paste_clipboard()
#         time.sleep(1)
#     time.sleep(0.1)
import ast
from typing import List
def get_function_names(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding="utf8") as file:
        tree = ast.parse(file.read())
    
    # Get all function names at the top level that don't start with "_"
    function_names = [
        node.name for node in tree.body 
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith('_')
    ]
    
    return function_names

tge.system_interactions.clipboard_operations.copy_to_clipboard("__all__ = "+str(get_function_names("tge/__init__.py")))