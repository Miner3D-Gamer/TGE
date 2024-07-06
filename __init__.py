# __init__.py

import time as tm; start_import = tm.time()
importing = __name__ != '__main__'

__version__ = '1.0.0'
__name__ = "tge"
__author__ = "Miner3D"
__license__ = "LGPL, GNU Lesser General Public License"

__doc__ = """
    tge - Text Game Engine
    Originally made for displaying and creating console-based games but has evolved into a general-purpose library.

    This library provides a wide range of functions and utilities for text-based game development, console operations,
    data manipulation, conversions, math calculations, user interfaces, file operations, and more.

    With a collection of over 700 functions, tge tries to simplify the development process and offers capabilities for
    building text-based games, console applications, file manipulation, and various quality of life functions. (yep)
    """

"747 Functions"
"46 Files"
"Yep"
"That's totally manageable and not messy even in the slightest. Easily manageable by a solo developer"
"I'm always open for feedback so if you found a bug or have any suggestions, I'm grateful to hear them (well not actually since they are bugs and bugs are usually not good in these situations)"

# Import Times Dictionary
import_times = {}


start_importing = tm.time()
import sys

if importing: # These mini libs take way less time to import
    from .mini_lib import import_lib_mini
    from .mini_lib import platform_mini
else:
    import importlib.util as import_lib_mini
    import platform as platform_mini

import subprocess
import os
from typing import List, Union, Tuple , Any, Optional, Dict
import subprocess
import shlex

import_times["build-in"] = tm.time() - start_importing



    


def get_system():
    """Returns the current user system"""
    if sys.platform.startswith("java"):
        return "jython"
    elif sys.platform == "darwin":
        return "darwin"
    elif sys.platform == "win32":
        return "windows"
    elif platform_mini.system() == "Linux":
        return "linux"
    else:
        return "unknown"

SYSTEM_NAME = get_system()




# Hide Pygame Support Prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'



# Function to Test for Library Existence
def test_for_library(library_name) -> bool:
    """
    Tests for the accessability of a library using a custom mini 
    version of "import_lib" mostly only using the essential 
    functions needed for existence a library.
    """

    spec = import_lib_mini.find_spec(library_name)
    return spec is not None


def download_library(library_name: str) -> Tuple[bool, str]:
    """
    Downloads and installs a Python library using pip.

    Parameters:
        library_name (str): The name of the library to be installed.

    Returns:
        tuple: A tuple containing a boolean indicating whether the installation was successful
        and a message string providing additional information in case of an error.
    """
    
    command = ['pip', 'install', library_name]
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return True, ""
    except subprocess.CalledProcessError as e:
        error_message = (
            f"Failed to install {library_name}. "
            f"Return code: {e.returncode}. "
            f"Output: {e.output}. "
            f"Error: {e.stderr}."
        )
        return False, error_message






# Printing Timing Information (if not importing as a module)
if not importing:
    INIT_TIME = tm.time() - start_import
    library_importing_time = 0
    for i in import_times:
        library_importing_time += import_times[i]
    
    
    import_times = sorted(import_times.items(), key=lambda x: x[1])
    idx = 0
    sorted_import_times = {}
    for i in import_times:
        sorted_import_times[import_times[idx][0]] = import_times[idx][1]
        idx += 1
    import_times = dict(reversed(list(sorted_import_times.items())))



    print(f"\nTotal loading time: {INIT_TIME}")
    print(f"Library importing time: {library_importing_time}")
    print(f"Total loading time without library importing time: {INIT_TIME - library_importing_time}")
    quit()

INIT_TIME_BEFORE_IMPORTING = tm.time() - start_import





#   Import modules from "manipulation"
from .manipulation import string_utils
from .manipulation import list_utils
from .manipulation import dictionary_utils as dict_utils

#   Import modules from "compatibility"
from .compatibility import tge_pygame
from .compatibility import tge_tkinter



#   Import modules from "conversion"
from .conversion import binary as binary
from .conversion import temperature as temperature
from .conversion import time as time
from .conversion import units as units
from .conversion import data as data


#   Import modules from "math_functions"
from .math_functions import financial_calculations 
from .math_functions import geometry_calculations
from .math_functions import math_functions
from .math_functions import statistics_calculations


#   Import modules from "user_interface"
from .user_interface import system_interactions
from .user_interface import clipboard



#   Import modules from root directory

from . import audio
from . import console_utils
from . import random_generators as random
from . import validation
from . import internet

from . import tbe
from . import codec
from . import time_utils
from . import file_operations
from . import formatting_utils as formatting
from . import bool_operations
from . import bitwise
#from .file_system import SimDirFilSystem



def load_image_processing():
    from . import image_processing
    return image_processing

    
def load_game_scrapper():
    from . import steam_scrapper
    return steam_scrapper





tim = tm.time()
IMPORT_TIME = tim - INIT_TIME_BEFORE_IMPORTING
INIT_TIME = tim - start_import
del tim, importing
