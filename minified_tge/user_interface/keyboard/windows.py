import ctypes
from ctypes import wintypes
from.virtual_keys import*
user32=ctypes.WinDLL('user32')
user32.GetAsyncKeyState.restype=wintypes.SHORT
def is_key_pressed(key_code):state=user32.GetAsyncKeyState(key_code);return state&32768!=0