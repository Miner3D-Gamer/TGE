import time as tm
start_import=tm.time()
import os
importing=__name__!='__main__'
__version__='1.0.0'
__name__='tge'
__author__='Miner3D'
__license__='LGPL, GNU Lesser General Public License'
__url__='https://github.com/Miner3DGaming/TGE'
__doc__='https://github.com/Miner3DGaming/TGE/blob/main/README.md'
start_importing=tm.time()
import sys
if importing:from.mini_lib import platform_mini
else:import platform as platform_mini
import_time_build_in=tm.time()-start_importing
import requests
def is_tge_outdated():
	A=requests.get('https://github.com/Miner3DGaming/TGE/raw/main/tge/update.hashed');A.raise_for_status()
	with open(os.path.dirname(__file__)+'/update.hash','r')as B:print(B.read(),A.content);return B.read()!=A.content
def get_system():
	A='darwin'
	if sys.platform.startswith('java'):return'jython'
	elif sys.platform==A:return A
	elif sys.platform=='win32':return'windows'
	elif platform_mini.system()=='Linux':return'linux'
	else:return'unknown'
SYSTEM_NAME=get_system()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='hide'
if not importing:INIT_TIME=tm.time()-start_import;library_importing_time=import_time_build_in;print(f"\nTotal loading time: {INIT_TIME}");print(f"Library importing time: {import_time_build_in}");print(f"Total loading time without library importing time: {INIT_TIME-import_time_build_in}");quit()
INIT_TIME_BEFORE_IMPORTING=tm.time()-start_import
from.manipulation import string_utils,list_utils,dictionary_utils as dict_utils
from.compatibility import tge_pygame
from.compatibility import tge_tkinter
from.conversion import binary as binary
from.conversion import temperature as temperature
from.conversion import time as time
from.conversion import units as units
from.conversion import data as data
from.math_functions import financial_calculations
from.math_functions import geometry_calculations
from.math_functions import math_functions
from.math_functions import statistics_calculations
from.math_functions.vector_calculation import Vector
from.user_interface import system_interactions
from.user_interface import clipboard
from.import audio
from.import console_utils as console
from.import random_generators as random
from.import validation
from.import internet
from.import library as library_utils
from.import tbe
from.codec import codec
from.import time_utils
from.import file_operations
from.import formatting_utils as formatting
from.import bool_operations
from.import bitwise
from.import hello_world
from.import image_processing
from.import steam_utils
tim=tm.time()
IMPORT_TIME=tim-INIT_TIME_BEFORE_IMPORTING
INIT_TIME=tim-start_import
del tim,importing