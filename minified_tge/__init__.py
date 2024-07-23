_A='darwin'
import time as tm
start_import=tm.time()
import os
importing=__name__!='__main__'
if not importing:print('This library is meant to imported, not to be run.');quit()
__name__='tge'
__author__='Miner3D'
__license__='LGPL, GNU Lesser General Public License'
__url__='https://github.com/Miner3DGaming/TGE'
__doc__='https://github.com/Miner3DGaming/TGE/blob/main/README.MD'
import sys,requests
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
from.conversion import binary as binary
from.conversion import temperature as temperature
from.conversion import time as time
from.conversion import units as units
from.conversion import data as data
from.math_functions import financial_calculations
from.math_functions import geometry_calculations
from.math_functions import math_functions
from.math_functions import statistics_calculations
from.user_interface import system_interactions as system
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
del tim,importing,INIT_TIME_BEFORE_IMPORTING