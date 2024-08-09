# __init__.py

import time as tm

start_import = tm.time()
import os

importing = __name__ != "__main__"

if not importing:
    raise RuntimeError("This library is meant to be imported, not run directly. Dummy.")

__name__ = "tge"
__author__ = "Miner3D"
__license__ = "LGPL, GNU Lesser General Public License"
__url__ = "https://github.com/Miner3DGaming/TGE"

__doc__ = "https://github.com/Miner3DGaming/TGE/blob/main/README.MD"

"Yep"
"At this point that python takes about a whole 0.1 seconds to skip over all the documentation/docstring (tested using compile function with consistent results)"
"That's totally manageable and not messy even in the slightest. Easily manageable by a solo developer"
"I'm always open for feedback so if you found a bug or have any suggestions, I'm grateful to hear them (well not actually since they are bugs and bugs are usually not good in these situations)"


import sys
from typing import Literal

import requests


def is_tge_outdated() -> bool:
    """
    Check if the local tge module is outdated by comparing the local 'update.hashed' with the latest version from the remote repository.

    Returns:
        bool: True if the local file is outdated, False otherwise.
    """
    response = requests.get(
        "https://github.com/Miner3DGaming/TGE/raw/main/tge/update.hashed"
    )
    response.raise_for_status()
    with open(os.path.dirname(__file__) + "/update.hashed", "r") as f:
        file = f.read()
        content = str(response.content)[2:-1]
        return file != content


from .mini_lib import platform_mini

if sys.platform.startswith("java"):

    def get_system() -> str:
        "Returns the current user system"
        return "jython"

elif sys.platform == "darwin":

    def get_system() -> str:
        "Returns the current user system"
        return "darwin"

elif sys.platform == "win32":

    def get_system() -> str:
        "Returns the current user system"
        return "windows"

elif platform_mini.system() == "Linux":

    def get_system() -> str:
        "Returns the current user system"
        return "linux"

else:

    def get_system() -> str:
        "Returns the current user system"
        return "unknown"


SYSTEM_NAME: "Literal['jython', 'darwin', 'windows', 'linux', 'unknown']" = get_system()


# Hide Pygame Support Prompt
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

INIT_TIME_BEFORE_IMPORTING = tm.time() - start_import



from .manipulation import string_utils
from .manipulation import list_utils
from .manipulation import dictionary_utils as dict_utils
from .manipulation import expansions


from .compatibility import tge_pygame
from .compatibility import tge_tkinter



from .conversion import binary as binary_conversion
from .conversion import temperature as temperature_conversion
from .conversion import time as time_conversion
from .conversion import units as units_conversion
from .conversion import data as data_conversion



from .math_functions import financial_calculations
from .math_functions import geometry_calculations
from .math_functions import math_functions
from .math_functions import statistics_calculations



from .system_interactions import clipboard_operations as clipboard
from .system_interactions import cursor_operations as cursor
from .system_interactions import keyboard_operations as keyboard
from .system_interactions import window_manager


from .validation import validation
from .codec import codec
from . import console_utils as console
from . import random_generators as random
from . import internet
from . import library as library_utils
from . import tbe
from . import time_utils
from . import file_operations
from . import formatting_utils as formatting
from . import bool_operations
from . import bitwise
from .image_processing import image_operations
# from .file_system import SimDirFilSystem

import subprocess
import shutil

def is_ffmpeg_installed():
    """Checks if the generic audio library FFmpeg in installed"""
    if shutil.which("ffmpeg") is None:
        return False
    
    try:
        result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if is_ffmpeg_installed():
    from . import audio



tim = tm.time()
IMPORT_TIME = tim - INIT_TIME_BEFORE_IMPORTING
INIT_TIME = tim - start_import
del tim, importing, INIT_TIME_BEFORE_IMPORTING
