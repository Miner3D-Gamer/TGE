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
import os, sys, time


sys.path.append(os.path.dirname(os.getcwd()))
import tge # type: ignore
print(tge.INIT_TIME)





# while True:
    
    
#     if tge.keyboard.is_key_pressed(tge.keyboard.keys.right_shift):
#         print(tge.clipboard.get_clipboard())
#         tge.clipboard.paste_clipboard()
#         time.sleep(1)
#     time.sleep(0.1)
    