_d='function_utils'
_c='bool_operations'
_b='formatting'
_a='file_operations'
_Z='time_utils'
_Y='internet'
_X='random'
_W='console'
_V='validation'
_U='window_manager'
_T='keyboard'
_S='cursor'
_R='clipboard'
_Q='statistics_calculations'
_P='math_functions'
_O='geometry_calculations'
_N='financial_calculations'
_M='data_conversion'
_L='units_conversion'
_K='time_conversion'
_J='temperature_conversion'
_I='binary_conversion'
_H='tge_tkinter'
_G='tge_pygame'
_F='expansions'
_E='dict_utils'
_D='list_utils'
_C='string_utils'
_B=False
_A='windows'
import time as tm
start_import=tm.time()
importing=__name__!='__main__'
if not importing:raise RuntimeError('This library is meant to be imported, not run directly. Dummy')
__name__='tge'
__author__='Miner3D'
__license__='LGPL, GNU Lesser General Public License'
__url__='https://github.com/Miner3DGaming/TGE'
__doc__='https://github.com/Miner3DGaming/TGE/blob/main/README.MD'
import sys
import subprocess,shutil,requests,os
def is_tge_outdated():
 A=requests.get('https://github.com/Miner3DGaming/TGE/raw/main/tge/update.hashed');A.raise_for_status()
 with open(os.path.dirname(__file__)+'/update.hashed','r')as B:C=B.read();D=str(A.content)[2:-1];return C!=D
from.mini_lib import platform_mini
def burn_value_into_function(x):
 def A():return x
 return A
def get_system():
 A='darwin'
 if sys.platform.startswith('java'):return'jython'
 elif sys.platform==A:return A
 elif sys.platform=='win32':return _A
 elif platform_mini.system()=='Linux':return'linux'
 else:return'unknown'
get_system=burn_value_into_function(get_system())
SYSTEM_NAME=get_system()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='hide'
def is_ffmpeg_installed():
 A='ffmpeg'
 if shutil.which(A)is None:return _B
 try:B=subprocess.run([A,'-version'],stdout=subprocess.PIPE,stderr=subprocess.PIPE);return B.returncode==0
 except FileNotFoundError:return _B
 except Exception as C:print(f"An error occurred: {C}");return _B
pre_assured_libraries=os.getenv('TGE_ASSURED_LIBRARIES','True')
if pre_assured_libraries=='True':assured_libraries=True
elif pre_assured_libraries=='False':assured_libraries=_B
else:assured_libraries=None
INIT_TIME_BEFORE_IMPORTING=tm.time()-start_import
from.import library_utils
__all__=['library_utils','is_ffmpeg_installed','get_system','is_tge_outdated','__name__','__author__','__license__','__url__','__doc__','SYSTEM_NAME']
if assured_libraries:
 __all__.extend([_C,_D,_E,_F,_G,_H,_I,_J,_K,_L,_M,_N,_O,_P,_Q,_R,_S,_T,_U,_V,'codec',_W,_X,_Y,'tbe',_Z,_a,_b,_c,'image_operations',_d]);from.manipulation import string_utils,list_utils,dictionary_utils as dict_utils,expansions;from.compatibility import tge_pygame;from.compatibility import tge_tkinter;from.conversion import binary as binary_conversion;from.conversion import temperature as temperature_conversion;from.conversion import time as time_conversion;from.conversion import units as units_conversion;from.conversion import data as data_conversion;from.math_functions import financial_calculations;from.math_functions import geometry_calculations;from.math_functions import math_functions;from.math_functions import statistics_calculations;from.system_interactions import clipboard_operations as clipboard;from.system_interactions import cursor_operations as cursor;from.system_interactions import keyboard_operations as keyboard;from.system_interactions import window_manager;from.validation import validation;from.codec import codec;from.import console_utils as console;from.import random_generators as random;from.import internet;from.import tbe;from.import time_utils;from.import file_operations;from.import formatting_utils as formatting;from.import bool_operations;from.image_processing import image_operations;from.import function_utils
 if is_ffmpeg_installed():from.import audio;__all__.append('audio')
else:
 pygame_installed=library_utils.is_library_installed('pygame');numpy_installed=library_utils.is_library_installed('numpy');json5_installed=library_utils.is_library_installed('json5');hjson_installed=library_utils.is_library_installed('hjson');python_minifier_installed=library_utils.is_library_installed('python_minifier');pytube_installed=library_utils.is_library_installed('pytube');pillow_installed=library_utils.is_library_installed('PIL');gtts_installed=library_utils.is_library_installed('gtts');pyperclip_installed=library_utils.is_library_installed('pyperclip');pynput_installed=library_utils.is_library_installed('pynput');xlib_installed=library_utils.is_library_installed('Xlib');quartz_installed=library_utils.is_library_installed('Quartz');appKit_installed=library_utils.is_library_installed('AppKit');simpleaudio_installed=library_utils.is_library_installed('simpleaudio');yt_dlp_installed=library_utils.is_library_installed('yt_dlp');__all__.extend([_C,_D,_E,_F,_I,_J,_K,_L,_M,_H,_N,_O,_d,_Z,_b,_c,_V]);from.manipulation import string_utils,list_utils,dictionary_utils as dict_utils,expansions;from.compatibility import tge_tkinter;from.conversion import binary as binary_conversion;from.conversion import temperature as temperature_conversion;from.conversion import time as time_conversion;from.conversion import units as units_conversion;from.conversion import data as data_conversion;from.math_functions import financial_calculations;from.math_functions import geometry_calculations;from.validation import validation;from.import time_utils;from.import formatting_utils as formatting;from.import bool_operations;from.import function_utils
 if pygame_installed:__all__.extend([_G]);from.compatibility import tge_pygame
 if numpy_installed:__all__.extend([_P,_Q]);from.math_functions import math_functions,statistics_calculations
 if SYSTEM_NAME==_A or pyperclip_installed:__all__.append(_R);from.system_interactions import clipboard_operations as clipboard
 if SYSTEM_NAME==_A or pynput_installed:__all__.append(_S);from.system_interactions import cursor_operations as cursor
 if SYSTEM_NAME==_A or xlib_installed:__all__.append(_T);from.system_interactions import keyboard_operations as keyboard
 if SYSTEM_NAME==_A or SYSTEM_NAME=='linux'or quartz_installed and appKit_installed:__all__.append(_U);from.system_interactions import window_manager
 if json5_installed and hjson_installed:__all__.extend(['codec',_X,_a]);from.codec import codec;from.import random_generators as random;from.import file_operations
 if python_minifier_installed:__all__.extend(['tbe',_W]);from.import tbe,console_utils as console
 if pytube_installed and yt_dlp_installed:__all__.append(_Y);from.import internet
 if pillow_installed and numpy_installed:__all__.append('image_processing');from.image_processing import image_operations
 if gtts_installed and simpleaudio_installed:
  if is_ffmpeg_installed():__all__.append('audio');from.import audio
 if assured_libraries is None:
  if not pygame_installed:print('(tge.compatibility.tge_pygame) Missing Library: pygame')
  if not numpy_installed:print('(tge.math_functions.math_functions, tge.math_functions.statistics_calculations) Missing Library: numpy')
  if not(json5_installed and hjson_installed):print('(tge.codec.codec, tge.random_generators) Missing Libraries: hjson, json5')
  if not python_minifier_installed:print('(tge.tbe) Missing Library: python_minifier')
  if not pytube_installed:print('(tge.internet) Missing Library: pytube')
  if not pillow_installed:print('(tge.image_processing.image_operations) Missing Library: pillow')
  if not gtts_installed:print('(tge.audio) Missing Library: gtts')
tim=tm.time()
IMPORT_TIME=tim-INIT_TIME_BEFORE_IMPORTING
INIT_TIME=tim-start_import
del tim,importing,INIT_TIME_BEFORE_IMPORTING,pre_assured_libraries,assured_libraries