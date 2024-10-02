# __init__.py

import time as tm

start_import = tm.time()


importing = __name__ != "__main__"

if not importing:
    raise RuntimeError("This library is meant to be imported, not run directly. Dummy")

__name__ = "tge"
__author__ = "Miner3D"
__license__ = "LGPL, GNU Lesser General Public License"
__url__ = "https://github.com/Miner3DGaming/TGE"

__doc__ = "https://github.com/Miner3DGaming/TGE/blob/main/README.MD"

"Yep"
"Over 900 functions in almost 60 files"
"This's totally manageable and not messy even in the slightest. Easily manageable by a solo developer"
"I'm always open for feedback so if you found a bug or have any suggestions, I'm grateful to hear your feedback"


import sys
from typing import Literal
import subprocess
import shutil
import requests
import os


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


from .mini_lib import platform_mini  # For faster import time

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

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


def is_ffmpeg_installed():
    """Checks if the generic audio library FFmpeg in installed"""
    if shutil.which("ffmpeg") is None:
        return False

    try:
        result = subprocess.run(
            ["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


assured_libraries = os.getenv("TGE_ASSURED_LIBRARIES", "True")

if assured_libraries == "True":
    assured_libraries = True
elif assured_libraries == "False":
    assured_libraries = False
else:
    assured_libraries = None

INIT_TIME_BEFORE_IMPORTING = tm.time() - start_import


from . import library_utils

__all__ = [
    "library_utils",
    "is_ffmpeg_installed",
    "get_system",
    "is_tge_outdated",
    "__name__",
    "__author__",
    "__license__",
    "__url__",
    "__doc__",
    "SYSTEM_NAME",
]


if assured_libraries:
    __all__.extend(
        [
            "string_utils",
            "list_utils",
            "dict_utils",
            "expansions",
            "tge_pygame",
            "tge_tkinter",
            "binary_conversion",
            "temperature_conversion",
            "time_conversion",
            "units_conversion",
            "data_conversion",
            "financial_calculations",
            "geometry_calculations",
            "math_functions",
            "statistics_calculations",
            "clipboard",
            "cursor",
            "keyboard",
            "window_manager",
            "validation",
            "codec",
            "console",
            "random",
            "internet",
            "tbe",
            "time_utils",
            "file_operations",
            "formatting",
            "bool_operations",
            "image_operations",
            "function_utils",
        ]
    )
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
    from . import tbe
    from . import time_utils
    from . import file_operations
    from . import formatting_utils as formatting
    from . import bool_operations
    from .image_processing import image_operations
    from . import function_utils

    if is_ffmpeg_installed():
        from . import audio

        __all__.append("audio")
else:
    pygame_installed = library_utils.is_library_installed("pygame")
    numpy_installed = library_utils.is_library_installed("numpy")
    json5_installed = library_utils.is_library_installed("json5")
    hjson_installed = library_utils.is_library_installed("hjson")
    python_minifier_installed = library_utils.is_library_installed("python_minifier")
    pytube_installed = library_utils.is_library_installed("pytube")
    pillow_installed = library_utils.is_library_installed("PIL")
    gtts_installed = library_utils.is_library_installed("gtts")
    pyperclip_installed = library_utils.is_library_installed("pyperclip")
    pynput_installed = library_utils.is_library_installed("pynput")
    xlib_installed = library_utils.is_library_installed("Xlib")
    quartz_installed = library_utils.is_library_installed("Quartz")
    appKit_installed = library_utils.is_library_installed("AppKit")
    simpleaudio_installed = library_utils.is_library_installed("simpleaudio")
    yt_dlp_installed = library_utils.is_library_installed("yt_dlp")

    __all__.extend(
        [
            "string_utils",
            "list_utils",
            "dict_utils",
            "expansions",
            "binary_conversion",
            "temperature_conversion",
            "time_conversion",
            "units_conversion",
            "data_conversion",
            "tge_tkinter",
            "financial_calculations",
            "geometry_calculations",
            "function_utils",
            "time_utils",
            "formatting",
            "bool_operations",
            "validation",
        ]
    )
    from .manipulation import string_utils
    from .manipulation import list_utils
    from .manipulation import dictionary_utils as dict_utils
    from .manipulation import expansions
    from .compatibility import tge_tkinter
    from .conversion import binary as binary_conversion
    from .conversion import temperature as temperature_conversion
    from .conversion import time as time_conversion
    from .conversion import units as units_conversion
    from .conversion import data as data_conversion
    from .math_functions import financial_calculations
    from .math_functions import geometry_calculations
    from .validation import validation
    from . import time_utils
    from . import formatting_utils as formatting
    from . import bool_operations
    from . import function_utils

    if pygame_installed:
        __all__.extend(["tge_pygame"])
        from .compatibility import tge_pygame

    if numpy_installed:
        __all__.extend(["math_functions", "statistics_calculations"])
        from .math_functions import math_functions
        from .math_functions import statistics_calculations

    if SYSTEM_NAME == "windows" or pyperclip_installed:
        __all__.append("clipboard")
        from .system_interactions import clipboard_operations as clipboard
    
    if SYSTEM_NAME == "windows" or pynput_installed:
        __all__.append("cursor")
        from .system_interactions import cursor_operations as cursor
    
    if SYSTEM_NAME == "windows" or xlib_installed:
        __all__.append("keyboard")
        from .system_interactions import keyboard_operations as keyboard
    
    if (
        SYSTEM_NAME == "windows"
        or SYSTEM_NAME == "linux"
        or (quartz_installed and appKit_installed)
    ):
        __all__.append("window_manager")
        from .system_interactions import window_manager

    if json5_installed and hjson_installed:
        __all__.extend(["codec", "random", "file_operations"])
        from .codec import codec
        from . import random_generators as random
        from . import file_operations

    if python_minifier_installed:
        __all__.extend(["tbe", "console_utils"])
        from . import tbe
        from . import console_utils as console
    if pytube_installed and yt_dlp_installed:
        __all__.append("internet")
        from . import internet

    if pillow_installed and numpy_installed:
        __all__.append("image_processing")
        from .image_processing import image_operations

    if gtts_installed and simpleaudio_installed:
        if is_ffmpeg_installed():
            __all__.append("audio")
            from . import audio

    if assured_libraries is None:
        if not pygame_installed:
            print("(tge.compatibility.tge_pygame) Missing Library: pygame")
        if not numpy_installed:
            print(
                "(tge.math_functions.math_functions, tge.math_functions.statistics_calculations) Missing Library: numpy"
            )
        if not (json5_installed and hjson_installed):
            print(
                "(tge.codec.codec, tge.random_generators) Missing Libraries: hjson, json5"
            )
        if not python_minifier_installed:
            print("(tge.tbe) Missing Library: python_minifier")
        if not pytube_installed:
            print("(tge.internet) Missing Library: pytube")
        if not pillow_installed:
            print("(tge.image_processing.image_operations) Missing Library: pillow")
        if not gtts_installed:
            print("(tge.audio) Missing Library: gtts")


tim = tm.time()
IMPORT_TIME = tim - INIT_TIME_BEFORE_IMPORTING
INIT_TIME = tim - start_import
del tim, importing, INIT_TIME_BEFORE_IMPORTING
