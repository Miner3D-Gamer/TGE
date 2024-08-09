_A='darwin'
import time as tm
start_import=tm.time()
import os
importing=__name__!='__main__'
if not importing:raise RuntimeError('This library is meant to be imported, not run directly. Dummy.')
__name__='tge'
__author__='Miner3D'
__license__='LGPL, GNU Lesser General Public License'
__url__='https://github.com/Miner3DGaming/TGE'
__doc__='https://github.com/Miner3DGaming/TGE/blob/main/README.MD'
import sys
import requests
def is_tge_outdated():
 A=requests.get('https://github.com/Miner3DGaming/TGE/raw/main/tge/update.hashed');A.raise_for_status()
 with open(os.path.dirname(__file__)+'/update.hashed','r')as B:C=B.read();D=str(A.content)[2:-1];return C!=D
from.mini_lib import platform_mini
if sys.platform.startswith('java'):
 def get_system():return'jython'
elif sys.platform==_A:
 def get_system():return _A
elif sys.platform=='win32':
 def get_system():return'windows'
elif platform_mini.system()=='Linux':
 def get_system():return'linux'
else:
 def get_system():return'unknown'
SYSTEM_NAME=get_system()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='hide'
INIT_TIME_BEFORE_IMPORTING=tm.time()-start_import
from.manipulation import string_utils
from.manipulation import list_utils
from.manipulation import dictionary_utils as dict_utils
from.manipulation import expansions
from.compatibility import tge_pygame
from.compatibility import tge_tkinter
from.conversion import binary as binary_conversion
from.conversion import temperature as temperature_conversion
from.conversion import time as time_conversion
from.conversion import units as units_conversion
from.conversion import data as data_conversion
from.math_functions import financial_calculations
from.math_functions import geometry_calculations
from.math_functions import math_functions
from.math_functions import statistics_calculations
from.system_interactions import clipboard_operations as clipboard
from.system_interactions import cursor_operations as cursor
from.system_interactions import keyboard_operations as keyboard
from.system_interactions import window_manager
from.validation import validation
from.codec import codec
from.import console_utils as console
from.import random_generators as random
from.import internet
from.import library as library_utils
from.import tbe
from.import time_utils
from.import file_operations
from.import formatting_utils as formatting
from.import bool_operations
from.import bitwise
from.image_processing import image_operations
import subprocess,shutil
def is_ffmpeg_installed():
 B='ffmpeg';A=False
 if shutil.which(B)is None:return A
 try:C=subprocess.run([B,'-version'],stdout=subprocess.PIPE,stderr=subprocess.PIPE);return C.returncode==0
 except FileNotFoundError:return A
 except Exception as D:print(f"An error occurred: {D}");return A
if is_ffmpeg_installed():from.import audio
tim=tm.time()
IMPORT_TIME=tim-INIT_TIME_BEFORE_IMPORTING
INIT_TIME=tim-start_import
del tim,importing,INIT_TIME_BEFORE_IMPORTING