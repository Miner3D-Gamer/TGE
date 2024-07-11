# __init__.py

import time as tm; start_import = tm.time()
import os
importing = __name__ != '__main__'

__version__ = '1.0.0'
__name__ = "tge"
__author__ = "Miner3D"
__license__ = "LGPL, GNU Lesser General Public License"
__url__  = 'https://github.com/Miner3DGaming/TGE'

__doc__ = 'https://github.com/Miner3DGaming/TGE/blob/main/README.md'


"Yep"
"At this point that python takes about a whole 0.1 seconds to skip over all the documentation/docstring (tested using compile function with consistent results)"
"That's totally manageable and not messy even in the slightest. Easily manageable by a solo developer"
"I'm always open for feedback so if you found a bug or have any suggestions, I'm grateful to hear them (well not actually since they are bugs and bugs are usually not good in these situations)"




start_importing = tm.time()
import sys

if importing: # These mini libs take way less time to import
    from .mini_lib import platform_mini
else:
    import platform as platform_mini



#from typing import List, Union, Tuple , Any, Optional, Dict

import_time_build_in = tm.time() - start_importing



    


def get_system()->str:
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




# Printing Timing Information (if not importing as a module)
if not importing:
    # This was once more impressive but a lot of stuff got cut for performance reason
    INIT_TIME = tm.time() - start_import
    library_importing_time = import_time_build_in
    print(f"\nTotal loading time: {INIT_TIME}")
    print(f"Library importing time: {import_time_build_in}")
    print(f"Total loading time without library importing time: {INIT_TIME - import_time_build_in}")
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
from .math_functions.vector_calculation import Vector


#   Import modules from "user_interface"
from .user_interface import system_interactions
from .user_interface import clipboard



#   Import modules from root directory
from . import library
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


from . import image_processing
from . import steam_scrapper






tim = tm.time()
IMPORT_TIME = tim - INIT_TIME_BEFORE_IMPORTING
INIT_TIME = tim - start_import
del tim, importing
