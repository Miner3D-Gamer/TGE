import ctypes
from ctypes import wintypes
from.import virtual_keys as keys
user32=ctypes.WinDLL('user32')
user32.GetAsyncKeyState.restype=wintypes.SHORT
def is_key_pressed(key_code):A=user32.GetAsyncKeyState(key_code);return A&32768!=0